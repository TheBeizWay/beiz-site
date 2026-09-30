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
const out = { source: 'Yahoo Finance, delayed', items: [] };
for (const [sym, label] of SYMS) { const q = await quote(sym); if (q) out.items.push({ sym, label, ...q }); }
if (!out.items.length) { console.log('no data, leaving file unchanged'); process.exit(0); }
const file = 'data/markets.json';
const prev = existsSync(file) ? readFileSync(file, 'utf8') : '';
const next = JSON.stringify(out);
if (prev.trim() === next) { console.log('unchanged'); process.exit(0); }
writeFileSync(file, next + '\n');
console.log('updated', next);
