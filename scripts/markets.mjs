// Fetches ASX index + AUD levels server-side (GitHub Actions) so visitors' browsers never call third parties.
import { writeFileSync, readFileSync, existsSync } from 'node:fs';
const SYMS = [['^AXJO', 'ASX 200'], ['^AORD', 'All Ords'], ['AUDUSD=X', 'AUD/USD']];
const UA = { 'User-Agent': 'Mozilla/5.0 (compatible; beiz-markets/1.0)' };
async function yahoo(sym, range, interval) {
  for (const host of ['query1', 'query2']) {
    try {
      const r = await fetch(`https://${host}.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(sym)}?range=${range}&interval=${interval}`, { headers: UA });
      if (!r.ok) continue;
      return (await r.json()).chart.result[0];
    } catch (e) { /* try next host */ }
  }
  return null;
}
async function quote(sym) {
  const d = await yahoo(sym, '1d', '15m');
  if (!d) return null;
  const m = d.meta, prev = m.chartPreviousClose ?? m.previousClose;
  const q = { price: m.regularMarketPrice, prev, chg: prev ? (m.regularMarketPrice / prev - 1) * 100 : null, time: m.regularMarketTime };
  // One-month angle: change over the month and a daily-close sparkline. Optional: the tile works without it.
  try {
    const mo = await yahoo(sym, '1mo', '1d');
    const closes = (mo?.indicators?.quote?.[0]?.close || []).filter(x => typeof x === 'number');
    if (closes.length >= 5) {
      q.m1 = (m.regularMarketPrice / closes[0] - 1) * 100;
      q.spark = closes.map(x => +x.toPrecision(6));
    }
  } catch (e) { /* skip the angle */ }
  return q;
}
const file = 'data/markets.json';
const prev = existsSync(file) ? readFileSync(file, 'utf8') : '';
let old = {}; try { old = JSON.parse(prev); } catch (e) {}
const t0 = Date.now();
const out = { source: 'Yahoo Finance (delayed), CoinGecko, RBA', items: [], crypto: [] };
const run = { at: new Date().toISOString(), sources: [], checks: [], held: [] };
const check = (name, pass) => { run.checks.push({ name, pass: !!pass }); return !!pass; };
const hold = (item, reason) => run.held.push({ item, reason });
const oldItem = sym => (old.items || []).find(i => i.sym === sym);
for (const [sym, label] of SYMS) {
  const q = await quote(sym);
  if (!q || typeof q.price !== 'number') continue;
  const o = oldItem(sym);
  // Control: a move of more than 10% since the last run is more likely bad data than a real move. Keep the old value and say why.
  if (o && !check(`${label}: moved less than 10% since last run`, Math.abs(q.price / o.price - 1) < 0.10)) { hold(label, 'Moved more than 10% since the last run. Kept the previous value.'); out.items.push(o); continue; }
  if (sym === 'AUDUSD=X' && !check('AUD/USD between 0.40 and 1.20', q.price > 0.4 && q.price < 1.2)) { hold(label, 'Outside the plausible range. Kept the previous value.'); if (o) out.items.push(o); continue; }
  out.items.push({ sym, label, ...q });
}
run.sources.push({ name: 'Yahoo Finance', ok: out.items.length > 0 });
if (!out.items.length && old.items) out.items = old.items;
try {
  const r = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=aud&include_24hr_change=true', { headers: UA });
  const d = await r.json();
  for (const [id, label, short] of [['bitcoin', 'Bitcoin', 'BTC'], ['ethereum', 'Ethereum', 'ETH'], ['solana', 'Solana', 'SOL']])
    if (d[id] && check(`${label}: price above zero, 24h move under 50%`, d[id].aud > 0 && Math.abs(d[id].aud_24h_change || 0) < 50)) out.crypto.push({ id, label, short, price: d[id].aud, chg: d[id].aud_24h_change });
    else if (d[id]) hold(label, 'Failed the sanity check. Kept the previous value.');
} catch (e) { /* keep previous */ }
run.sources.push({ name: 'CoinGecko', ok: out.crypto.length > 0 });
if (!out.crypto.length && old.crypto) out.crypto = old.crypto;
// RBA cash rate target (table F1). Series FIRMMCRTD; FIRMMCCRT holds the change on decision days.
try {
  const r = await fetch('https://www.rba.gov.au/statistics/tables/csv/f1-data.csv', { headers: UA });
  const rows = (await r.text()).split(/\r?\n/).map(l => l.split(','));
  const hdr = rows.find(x => x[0] === 'Series ID');
  const iR = hdr.indexOf('FIRMMCRTD');
  // Use the level series only. The change column (FIRMMCCRT) is filled in late, so it can point at an older move.
  const pts = rows.filter(x => /^\d{2}-[A-Za-z]{3}-\d{4}$/.test(x[0]) && x[iR] && x[iR].trim() !== '')
    .map(x => ({ d: x[0], t: Date.parse(x[0].replace(/-/g, ' ')), r: +x[iR] }));
  const last = pts[pts.length - 1];
  if (last && old.rba && !check('RBA cash rate: change since last run of 1 point or less', Math.abs(last.r - old.rba.rate) <= 1)) { hold('RBA cash rate', 'Changed by more than 1 point. Kept the previous value for a person to confirm.'); }
  else if (last && check('RBA cash rate between 0% and 15%', last.r >= 0 && last.r <= 15)) {
    let lastChange = null;
    for (let i = pts.length - 1; i > 0; i--) if (pts[i].r !== pts[i - 1].r) { lastChange = { date: pts[i].d, by: +(pts[i].r - pts[i - 1].r).toFixed(2) }; break; }
    const yr = [...pts].reverse().find(p => p.t <= last.t - 365 * 864e5);
    const above = [...pts].reverse().find(p => p.r > last.r);            // last time it was higher than today
    const t12 = last.t - 365 * 864e5;
    let moves12 = 0; for (let i = 1; i < pts.length; i++) if (pts[i].t > t12 && pts[i].r !== pts[i - 1].r) moves12++;
    out.rba = { rate: last.r, asAt: last.d, lastChange, yearAgo: yr ? yr.r : null, moves12, higherLast: above ? above.d : null, source: 'RBA statistical table F1' };
  }
} catch (e) { /* keep previous */ }
run.sources.push({ name: 'RBA', ok: !!out.rba });
if (!out.rba && old.rba) out.rba = old.rba;
run.ms = Date.now() - t0;
const passed = run.checks.filter(c => c.pass).length;
out.run = run;
out.log = [{ at: run.at, sources: run.sources.filter(x => x.ok).length + '/' + run.sources.length, checks: passed + '/' + run.checks.length, held: run.held.length }, ...(old.log || [])].slice(0, 10);
if (!out.items.length && !out.crypto.length) { console.log('no data, leaving file unchanged'); process.exit(0); }
const next = JSON.stringify(out);
// Always write: the run record itself is the point. The site shows when the pipeline last ran and what it checked.
writeFileSync(file, next + '\n');
console.log('updated', next);
