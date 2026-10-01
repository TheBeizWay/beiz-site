// Fetches ASX index + AUD levels server-side (GitHub Actions) so visitors' browsers never call third parties.
import { writeFileSync, readFileSync, existsSync } from 'node:fs';
const SYMS = [['^AXJO', 'ASX 200'], ['^AORD', 'All Ords'], ['AUDUSD=X', 'AUD/USD']];
const UA = { 'User-Agent': 'Mozilla/5.0 (compatible; beiz-markets/1.0)' };
async function quote(sym) {
  for (const host of ['query1', 'query2']) {
    try {
      const r = await fetch(`https://${host}.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(sym)}?range=1d&interval=15m`, { headers: UA });
      if (!r.ok) continue;
      const m = (await r.json()).chart.result[0].meta;
      const prev = m.chartPreviousClose ?? m.previousClose;
      return { price: m.regularMarketPrice, prev, chg: prev ? (m.regularMarketPrice / prev - 1) * 100 : null, time: m.regularMarketTime };
    } catch (e) { /* try next host */ }
  }
  return null;
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
  const iR = hdr.indexOf('FIRMMCRTD'), iC = hdr.indexOf('FIRMMCCRT');
  const data = rows.filter(x => /^\d{2}-[A-Za-z]{3}-\d{4}$/.test(x[0]));
  const last = [...data].reverse().find(x => x[iR] && x[iR].trim() !== '');
  const chg = [...data].reverse().find(x => x[iC] && x[iC].trim() !== '');
  if (last) out.rba = { rate: +last[iR], asAt: last[0], lastChange: chg ? { date: chg[0], by: +chg[iC] } : null, source: 'RBA statistical table F1' };
} catch (e) { /* keep previous */ }
if (!out.rba && old.rba) out.rba = old.rba;
if (!out.items.length && !out.crypto.length) { console.log('no data, leaving file unchanged'); process.exit(0); }
const next = JSON.stringify(out);
if (prev.trim() === next) { console.log('unchanged'); process.exit(0); }
writeFileSync(file, next + '\n');
console.log('updated', next);
