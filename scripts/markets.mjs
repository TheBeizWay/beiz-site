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
const out = { source: 'Yahoo Finance (delayed), CoinGecko, RBA', items: [], crypto: [] };
for (const [sym, label] of SYMS) { const q = await quote(sym); if (q) out.items.push({ sym, label, ...q }); }
if (!out.items.length && old.items) out.items = old.items;
try {
  const r = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=aud&include_24hr_change=true', { headers: UA });
  const d = await r.json();
  for (const [id, label, short] of [['bitcoin', 'Bitcoin', 'BTC'], ['ethereum', 'Ethereum', 'ETH'], ['solana', 'Solana', 'SOL']])
    if (d[id]) out.crypto.push({ id, label, short, price: d[id].aud, chg: d[id].aud_24h_change });
} catch (e) { /* keep previous */ }
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
  if (last) {
    let lastChange = null;
    for (let i = pts.length - 1; i > 0; i--) if (pts[i].r !== pts[i - 1].r) { lastChange = { date: pts[i].d, by: +(pts[i].r - pts[i - 1].r).toFixed(2) }; break; }
    const yr = [...pts].reverse().find(p => p.t <= last.t - 365 * 864e5);
    const above = [...pts].reverse().find(p => p.r > last.r);            // last time it was higher than today
    const t12 = last.t - 365 * 864e5;
    let moves12 = 0; for (let i = 1; i < pts.length; i++) if (pts[i].t > t12 && pts[i].r !== pts[i - 1].r) moves12++;
    out.rba = { rate: last.r, asAt: last.d, lastChange, yearAgo: yr ? yr.r : null, moves12, higherLast: above ? above.d : null, source: 'RBA statistical table F1' };
  }
} catch (e) { /* keep previous */ }
if (!out.rba && old.rba) out.rba = old.rba;
if (!out.items.length && !out.crypto.length) { console.log('no data, leaving file unchanged'); process.exit(0); }
const next = JSON.stringify(out);
if (prev.trim() === next) { console.log('unchanged'); process.exit(0); }
writeFileSync(file, next + '\n');
console.log('updated', next);
