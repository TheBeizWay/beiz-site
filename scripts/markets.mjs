// Fetches the RBA cash rate target (statistical table F1, published under CC BY 4.0) server-side,
// so visitors' browsers never call third parties. Series FIRMMCRTD; FIRMMCCRT holds the change on decision days.
import { writeFileSync, readFileSync, existsSync } from 'node:fs';
const UA = { 'User-Agent': 'Mozilla/5.0 (compatible; beiz-data/1.0)' };
const file = 'data/markets.json';
const prev = existsSync(file) ? readFileSync(file, 'utf8') : '';
let old = {}; try { old = JSON.parse(prev); } catch (e) {}
const out = { source: 'RBA' };
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
if (!out.rba) { console.log('no data, leaving file unchanged'); process.exit(0); }
const next = JSON.stringify(out);
if (prev.trim() === next) { console.log('unchanged'); process.exit(0); }
writeFileSync(file, next + '\n');
console.log('updated', next);
