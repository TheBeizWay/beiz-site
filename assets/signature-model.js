/* Beiz signature experience: calculation model. Pure functions over a fictional business; no DOM, no network, no AI.
   Used by signature.js and the homepage panel in the browser, and by tools/site-tests/signature.test.js under Node. */
(function (root) {
  "use strict";
  const WEEKS = 13; // forecast day 0 = Monday of week 1; week w covers days (w-1)*7 .. w*7-1

  // Fictional: Harbourline Joinery, 14 staff. Not a client. AUD, GST ignored for clarity.
  const DATA = {
    business: "Harbourline Joinery (fictional)",
    opening: 96000, buffer: 20000, labourCost: 58, targetMargin: 0.25, invoiceLag: 9,
    customers: [
      { id: "C1", name: "Northshore Builders", terms: 30 },
      { id: "C2", name: "Coastal Fitouts", terms: 14 },
      { id: "C3", name: "Private clients", terms: 7 },
    ],
    // complete: forecast day the job finished. value: agreed price. quoted*: what the quote assumed. hours/materials: actuals from records.
    jobs: [
      { id: "J-104", customer: "C1", title: "Kitchen joinery, 6 units", complete: 4, value: 36300, quotedHours: 280, hours: 290, quotedMaterials: 9200, materials: 9400 },
      { id: "J-105", customer: "C2", title: "Retail counter and shelving", complete: 9, value: 18300, quotedHours: 150, hours: 150, quotedMaterials: 4100, materials: 4100 },
      { id: "J-106", customer: "C3", title: "Built-in wardrobes", complete: 11, value: 7700, quotedHours: 60, hours: 64, quotedMaterials: 1900, materials: 1900 },
      { id: "J-107", customer: "C1", title: "Townhouse stairs, 4 units", complete: 18, value: 42800, quotedHours: 330, hours: 410, quotedMaterials: 10800, materials: 12600 },
      { id: "J-108", customer: "C2", title: "Café fit-out joinery", complete: 25, value: 27700, quotedHours: 220, hours: 240, quotedMaterials: 6600, materials: 6800 },
      { id: "J-109", customer: "C3", title: "Library wall unit", complete: 30, value: 11200, quotedHours: 96, hours: 128, quotedMaterials: 2300, materials: 2300 },
      { id: "J-110", customer: "C1", title: "Apartment vanities, 12 units", complete: 39, value: 36500, quotedHours: 290, hours: 300, quotedMaterials: 8700, materials: 8900 },
      { id: "J-111", customer: "C2", title: "Office reception desk", complete: 46, value: 12800, quotedHours: 110, hours: 118, quotedMaterials: 2600, materials: 3600 },
      { id: "J-112", customer: "C3", title: "Kitchen renovation", complete: 53, value: 26600, quotedHours: 230, hours: 236, quotedMaterials: 7400, materials: 7400 },
      { id: "J-113", customer: "C1", title: "Display home cabinetry", complete: 60, value: 42500, quotedHours: 340, hours: 352, quotedMaterials: 10000, materials: 10200 },
    ],
    staff: ["A. Nguyen", "B. Kowalski", "C. Patel", "D. O'Brien", "E. Rossi"],
    suppliers: ["Timber Direct", "Edge & Laminate Co", "Hardware Wholesale"],
    outgoings: [["Wages", 3, 14, 23800], ["Workshop rent", 0, 28, 6400], ["Vehicle and equipment finance", 14, 28, 2900], ["Insurance and software", 21, 28, 1400]],
    bills: [["Timber Direct", 8420, 6], ["Hardware Wholesale", 1260, 10], ["Edge & Laminate Co", 3380, 17], ["Timber Direct", 9150, 27], ["Coastal Glass", 2240, 31],
            ["Fasteners Plus", 640, 38], ["Hardware Wholesale", 1480, 45], ["Edge & Laminate Co", 3910, 55], ["Timber Direct", 10300, 66]],
  };
  const LIMITS = { labourCost: [30, 150], targetMargin: [0, 0.6] };

  const weekOf = day => Math.floor(day / 7) + 1;
  const cust = (d, id) => d.customers.find(c => c.id === id);
  // Accept a number inside the limits; anything else (blank, text, out of range) falls back to the default.
  function clean(key, v, d) { const n = Number(v), [lo, hi] = LIMITS[key]; return v !== "" && v != null && isFinite(n) && n >= lo && n <= hi ? n : d[key]; }

  /* Source records for a job, generated deterministically so they always add back to the job totals. */
  function records(d, jobId) {
    const j = d.jobs.find(x => x.id === jobId); if (!j) return null;
    let s = [...jobId].reduce((a, c) => a * 31 + c.charCodeAt(0), 7) >>> 0;
    const rnd = () => ((s = (s * 1103515245 + 12345) >>> 0) / 4294967296);
    const ts = [], start = j.complete - Math.max(5, Math.ceil(j.hours / 40)) * 3;
    let left = j.hours, i = 0;
    while (left > 0) { const h = Math.min(left, 6 + Math.floor(rnd() * 3)); ts.push({ date: start + i, staff: d.staff[i % d.staff.length], hours: h, cost: h * d.labourCost }); left -= h; i++; }
    const n = j.materials > 5000 ? 3 : 2, parts = [];
    let mleft = j.materials;
    const wts = n === 3 ? [0.46, 0.33] : [0.62]; // uneven split, last bill takes the remainder so the total is exact
    for (let k = 0; k < n; k++) { const amt = k === n - 1 ? mleft : Math.round(j.materials * wts[k] / 10) * 10; parts.push({ supplier: d.suppliers[k % d.suppliers.length], amount: amt, ref: `${jobId}-M${k + 1}` }); mleft -= amt; }
    return { timesheets: ts, materials: parts, invoice: { ref: `INV-${jobId.slice(2)}`, amount: j.value } };
  }

  /* Job margin = price - (hours x labour cost) - materials. Cause flags compare actuals with the quote. */
  function margins(d, opts = {}) {
    const lc = clean("labourCost", opts.labourCost, d), tm = clean("targetMargin", opts.targetMargin, d);
    return d.jobs.map(j => {
      const labour = j.hours * lc, cost = labour + j.materials, margin = j.value - cost, pct = margin / j.value;
      const causes = [];
      if (j.hours > j.quotedHours * 1.1) causes.push({ kind: "hours", text: `Hours ran ${Math.round((j.hours / j.quotedHours - 1) * 100)}% over the quote (${j.hours} vs ${j.quotedHours})` });
      if (j.materials > j.quotedMaterials * 1.1) causes.push({ kind: "materials", text: `Materials ran ${Math.round((j.materials / j.quotedMaterials - 1) * 100)}% over the quote` });
      if (!causes.length && pct < tm) causes.push({ kind: "price", text: "Actuals are close to the quote, so the quoted price or the labour-cost assumption is the likely gap" });
      return { job: j.id, title: j.title, customer: cust(d, j.customer).name, value: j.value, hours: j.hours, quotedHours: j.quotedHours, labour, materials: j.materials, cost, margin, pct, below: pct < tm, causes, labourCost: lc, target: tm };
    });
  }

  function receipts(d, opts = {}) {
    const lag = opts.invoiceLag ?? d.invoiceLag;
    return d.jobs.map(j => { const c = cust(d, j.customer), invoiced = j.complete + lag, paid = invoiced + c.terms + ((opts.delay || {})[j.customer] || 0);
      return { job: j.id, customer: c.name, amount: j.value, complete: j.complete, invoiced, paid, week: weekOf(paid), inHorizon: weekOf(paid) <= WEEKS }; });
  }
  function payments(d) {
    const out = [];
    for (const [label, first, every, amount] of d.outgoings) for (let day = first; weekOf(day) <= WEEKS; day += every) out.push({ label, day, week: weekOf(day), amount });
    for (const [label, amount, day] of d.bills) if (weekOf(day) <= WEEKS) out.push({ label, day, week: weekOf(day), amount });
    return out;
  }
  /* 13-week cash: closing = opening + in - out, each week. */
  function forecast(d, opts = {}) {
    const rc = receipts(d, opts), pay = payments(d), weeks = []; let bal = d.opening;
    for (let w = 1; w <= WEEKS; w++) {
      const ins = rc.filter(r => r.inHorizon && r.week === w), outs = pay.filter(p => p.week === w);
      const tin = ins.reduce((s, r) => s + r.amount, 0), tout = outs.reduce((s, p) => s + p.amount, 0), opening = bal; bal = opening + tin - tout;
      weeks.push({ week: w, opening, in: tin, out: tout, closing: bal, belowBuffer: bal < d.buffer });
    }
    const low = weeks.reduce((a, b) => (b.closing < a.closing ? b : a));
    return { weeks, lowest: { week: low.week, closing: low.closing }, belowBuffer: weeks.filter(w => w.belowBuffer).map(w => w.week), afterHorizon: rc.filter(r => !r.inHorizon),
             totalIn: weeks.reduce((s, w) => s + w.in, 0), totalOut: weeks.reduce((s, w) => s + w.out, 0) };
  }
  /* Work finished but not yet invoiced at the end of a week: a list to review, not lost revenue. */
  function unbilled(d, opts, asAtWeek) {
    const end = asAtWeek * 7 - 1;
    return receipts(d, opts).filter(r => r.complete <= end && r.invoiced > end).map(r => ({ ...r, daysWaiting: end - r.complete }));
  }

  const api = { WEEKS, DATA, LIMITS, weekOf, clean, records, margins, receipts, payments, forecast, unbilled };
  if (typeof module === "object" && module.exports) module.exports = api; else root.BeizModel = api;
})(this);
