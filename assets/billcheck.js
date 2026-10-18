/* Beiz bill check. Reads a bills export in the browser. Nothing is uploaded, stored or sent. */
(() => {
  const root = document.getElementById("bc"); if (!root) return;
  const $ = s => root.querySelector(s);
  const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const aud = n => (n < 0 ? "-$" : "$") + Math.abs(n).toLocaleString("en-AU", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const aud0 = n => "$" + Math.round(n).toLocaleString("en-AU");
  const DAY = 864e5, MON = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"];
  const fmtD = t => t == null ? "" : new Date(t * DAY).toLocaleDateString("en-AU", { day: "numeric", month: "short", year: "numeric", timeZone: "UTC" });
  const MAX_BYTES = 25e6, MAX_ROWS = 100000;

  /* ---------- CSV ---------- */
  function parseCSV(text) {
    text = text.replace(/^﻿/, "");
    const first = text.slice(0, text.indexOf("\n") + 1 || text.length);
    const cnt = ch => (first.match(new RegExp("\\" + ch, "g")) || []).length;
    const d = [",", ";", "\t"].sort((a, b) => cnt(b) - cnt(a))[0];
    const rows = []; let row = [], f = "", q = false;
    for (let i = 0; i < text.length; i++) {
      const c = text[i];
      if (q) { if (c === '"') { if (text[i + 1] === '"') { f += '"'; i++; } else q = false; } else f += c; continue; }
      if (c === '"') q = true; else if (c === d) { row.push(f); f = ""; }
      else if (c === "\n" || c === "\r") { if (c === "\r" && text[i + 1] === "\n") i++; row.push(f); f = ""; if (row.some(x => x.trim())) rows.push(row); row = []; if (rows.length > MAX_ROWS) break; }
      else f += c;
    }
    row.push(f); if (row.some(x => x.trim())) rows.push(row);
    return rows;
  }

  /* ---------- columns ---------- */
  const norm = s => String(s).toLowerCase().replace(/^\*/, "").replace(/[^a-z0-9]/g, "");
  const FIELDS = [
    ["supplier", "Supplier", true, ["contactname", "contact", "supplier", "suppliername", "vendor", "vendorname", "payee", "colastname", "name", "company", "creditor"]],
    ["amount", "Bill total", true, ["total", "totalamount", "amount", "amountincgst", "totalincgst", "gross", "grossamount", "invoicetotal", "billtotal", "value", "debit"]],
    ["date", "Bill date", true, ["invoicedate", "billdate", "date", "transactiondate", "documentdate", "issuedate"]],
    ["invoice", "Bill or invoice number", false, ["invoicenumber", "invoiceno", "supplierinvoiceno", "billnumber", "billno", "reference", "ref", "documentnumber", "number"]],
    ["paid", "Date paid", false, ["paiddate", "datepaid", "paymentdate", "fullypaidondate", "paidon"]],
    ["bank", "Supplier bank account", false, ["bankaccount", "bankaccountnumber", "accountnumber", "bankdetails", "bsbaccount", "bsbandaccount"]],
    ["abn", "Supplier ABN", false, ["abn", "supplierabn", "taxnumber", "contactabn"]],
  ];
  const LINE_COLS = ["description", "quantity", "unitamount", "lineamount", "accountcode", "itemcode", "taxtype"];
  function guess(headers) {
    const h = headers.map(norm), map = {}, used = new Set();
    for (const [k, , , syn] of FIELDS) {
      let i = -1;
      for (const s of syn) { i = h.findIndex((x, j) => x === s && !used.has(j)); if (i >= 0) break; }
      if (i < 0) for (const s of syn) { if (s.length < 4) continue; i = h.findIndex((x, j) => x.includes(s) && !used.has(j)); if (i >= 0) break; }
      map[k] = i; if (i >= 0) used.add(i);
    }
    return map;
  }

  /* ---------- values ---------- */
  function pDate(s) {
    s = String(s || "").trim(); if (!s) return null; let m, y, mo, d;
    if ((m = s.match(/^(\d{4})-(\d{1,2})-(\d{1,2})/))) [y, mo, d] = [+m[1], +m[2], +m[3]];
    else if ((m = s.match(/^(\d{1,2})[\/.-](\d{1,2})[\/.-](\d{2,4})/))) [d, mo, y] = [+m[1], +m[2], +m[3]];
    else if ((m = s.match(/^(\d{1,2})[\s-]([A-Za-z]{3})[A-Za-z]*[\s-](\d{2,4})/))) [d, mo, y] = [+m[1], MON.indexOf(m[2].toLowerCase()) + 1, +m[3]];
    else return null;
    if (y < 100) y += 2000; if (!mo || mo > 12 || !d || d > 31) return null;
    const t = new Date(Date.UTC(y, mo - 1, d));
    if (t.getUTCFullYear() !== y || t.getUTCMonth() !== mo - 1 || t.getUTCDate() !== d) return null; // e.g. 31/02 doesn't roll into March
    return Math.floor(t.getTime() / DAY);
  }
  function pAmt(s) {
    s = String(s || "").trim(); if (!s) return null;
    const neg = /^\(.*\)$/.test(s) || /^-/.test(s) || /\bCR\b/i.test(s);
    const n = parseFloat(s.replace(/[^0-9.]/g, "")); if (isNaN(n)) return null;
    return Math.round((neg ? -n : n) * 100) / 100;
  }
  const sKey = s => String(s).toLowerCase().replace(/\b(pty|ltd|limited|the|co|trust|trustee|for)\b/g, "").replace(/[^a-z0-9]/g, "");
  const iKey = s => String(s).toLowerCase().replace(/[^a-z0-9]/g, "").replace(/^(inv|invoice|bill|no)+/, "").replace(/^0+/, "");
  function abnOk(s) {
    const d = String(s).replace(/\D/g, ""); if (d.length !== 11) return false;
    const w = [10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19];
    return d.split("").reduce((t, c, i) => t + (i === 0 ? +c - 1 : +c) * w[i], 0) % 89 === 0;
  }

  /* ---------- checks ---------- */
  const CHECKS = {
    dup: ["Possible duplicate bills", "hi", "Same supplier, same amount, within 14 days. The commonest way money is paid twice; often the invoice number is changed by a letter or a digit. Regular charges a month apart aren't flagged."],
    inv: ["Same invoice number used twice", "hi", "One supplier, one invoice number, more than one bill. Either a duplicate or a keying error in the amount."],
    bank: ["Supplier bank details changed", "hi", "Payment redirection fraud starts with a request to update bank details. Each change should be confirmed by phone, on a number you already had."],
    split: ["Bills that look split to stay under the approval limit", "md", "Same supplier, same day, each under your limit but over it together."],
    limit: ["Bills just under the approval limit", "md", "Within 5% under your limit. One on its own is usually nothing; a pattern is worth a question."],
    news: ["Large first bill from a supplier first seen in this file", "md", "A supplier that first appears in this export, more than 30 days in, with a first bill at least twice your approval limit. It may not be new to your business. Check the supplier is real and the work was done."],
    wkd: ["Paid on a weekend", "md", "Payments released on a Saturday or Sunday. Normal for some businesses; unusual for most."],
    abn: ["ABN missing or failing the check-digit test", "md", "An ABN that fails the official check-digit test is a typo or made up. Passing the test doesn't confirm the ABN is registered or who owns it. If a supplier doesn't quote an ABN, you may need to withhold 47% of the payment under the ATO's no-ABN withholding rules, unless an exception applies, such as a payment of $75 or less excluding GST. General information, not tax advice."],
  };
  function run(rows, map, limit) {
    const hdr = rows[0].map(norm);
    const lineLevel = map.invoice >= 0 && LINE_COLS.some(c => hdr.includes(c));
    let bills = [], skipped = 0, merged = 0; const seen = new Set();
    for (let r = 1; r < rows.length; r++) {
      const v = rows[r], g = k => map[k] >= 0 ? (v[map[k]] ?? "").trim() : "";
      const supplier = g("supplier"), amount = pAmt(g("amount")), date = pDate(g("date"));
      if (!supplier || amount == null || date == null) { skipped++; continue; }
      const b = { row: r + 1, supplier, sk: sKey(supplier) || supplier.toLowerCase(), amount, date, invoice: g("invoice"), paid: pDate(g("paid")), bank: g("bank").replace(/\s+/g, " "), abn: g("abn") };
      if (lineLevel) { const k = [b.sk, iKey(b.invoice), date, amount].join("|"); if (seen.has(k)) { merged++; continue; } seen.add(k); }
      bills.push(b);
    }
    const F = [], add = (type, items, detail, risk = 0) => F.push({ type, items, detail, risk });
    const twice = new Map(); // row -> amount: each extra bill counted once, even if two checks flag it
    const by = {}; bills.forEach(b => (by[b.sk] ||= []).push(b));
    const start = Math.min(...bills.map(b => b.date));
    for (const list of Object.values(by)) {
      list.sort((a, b) => a.date - b.date);
      // duplicates
      const done = new Set();
      for (let i = 0; i < list.length; i++) for (let j = i + 1; j < list.length && list[j].date - list[i].date <= 14; j++) {
        const a = list[i], b = list[j];
        if (a.amount > 0 && a.amount === b.amount && !done.has(j) && !(a.invoice && b.invoice && iKey(a.invoice) === iKey(b.invoice))) {
          done.add(j); add("dup", [a, b], `${b.date - a.date} days apart`, b.amount); twice.set(b.row, b.amount);
        }
      }
      // same invoice number
      const ig = {}; list.forEach(b => { const k = iKey(b.invoice); if (k) (ig[k] ||= []).push(b); });
      for (const g of Object.values(ig)) if (g.length > 1) { const lo = Math.min(...g.map(b => b.amount)); add("inv", g, g[0].amount === g[1].amount ? "Same amount" : "Different amounts", lo * (g.length - 1)); g.slice(1).forEach(b => { if (!twice.has(b.row)) twice.set(b.row, Math.min(lo, b.amount)); }); }
      // bank changes
      const banks = [...new Set(list.map(b => b.bank).filter(Boolean))];
      if (banks.length > 1) { const firstNew = list.find(b => b.bank === banks[1]); add("bank", [firstNew], `${banks.length} different accounts: ${banks.join(" → ")}`); }
      // splits
      const dg = {}; list.forEach(b => { if (b.amount > 0 && b.amount < limit) (dg[b.date] ||= []).push(b); });
      for (const g of Object.values(dg)) { const t = g.reduce((s, b) => s + b.amount, 0); if (g.length > 1 && t >= limit) add("split", g, `${aud(t)} together`); }
      // new supplier, large first bill
      const f = list[0]; if (f.date - start > 30 && f.amount >= 2 * limit) add("news", [f], `First bill in this file, ${f.date - start} days after it starts`);
      // abn
      if (map.abn >= 0) { const a = list.find(b => !b.abn) || list.find(b => !abnOk(b.abn)); if (a) add("abn", [a], a.abn ? `ABN ${a.abn} fails the check-digit test` : "No ABN recorded"); }
    }
    bills.forEach(b => {
      if (b.amount >= limit * 0.95 && b.amount < limit) add("limit", [b], `${aud(limit - b.amount)} under your ${aud0(limit)} limit`);
      if (b.paid != null) { const wd = new Date(b.paid * DAY).getUTCDay(); if (wd === 0 || wd === 6) add("wkd", [b], `Paid ${wd === 6 ? "Saturday" : "Sunday"} ${fmtD(b.paid)}`); }
    });
    const NA = [["inv", "invoice", "no bill-number column"], ["bank", "bank", "no bank-account column"], ["wkd", "paid", "no date-paid column"], ["abn", "abn", "no ABN column"]].filter(([, k]) => map[k] < 0);
    return { bills, skipped, merged, F, risk: [...twice.values()].reduce((s, a) => s + Math.max(0, a), 0), na: NA };
  }

  /* ---------- UI ---------- */
  let data = null, map = null, name = "";
  const out = $("#bcOut"), mapBox = $("#bcMap"), limIn = $("#bcLimit"), status = $("#bcStatus");
  function load(text, label) {
    const rows = parseCSV(text);
    if (rows.length < 2) { status.textContent = "That file has no rows we can read. Export the bills list as CSV and try again."; return; }
    data = rows; name = label; map = guess(rows[0]); renderMap(); go();
    root.classList.add("has");
  }
  function renderMap() {
    const opts = sel => `<option value="-1">Not in this file</option>` + data[0].map((h, i) => `<option value="${i}"${i === sel ? " selected" : ""}>${esc(h || "Column " + (i + 1))}</option>`).join("");
    const open = FIELDS.some(([k, , req]) => req && map[k] < 0) ? " open" : "";
    mapBox.innerHTML = `<details class="bck-map"${open}><summary>Columns used from <b>${esc(name)}</b> <span>Change</span></summary><div class="bck-mg">` +
      FIELDS.map(([k, l, req]) => `<label><span>${l}${req ? "" : " <small>(optional)</small>"}</span><select data-f="${k}">${opts(map[k])}</select></label>`).join("") + "</div></details>";
    mapBox.querySelectorAll("select").forEach(s => s.onchange = () => { map[s.dataset.f] = +s.value; go(); });
  }
  function go() {
    const limit = Math.max(1, +limIn.value || 5000);
    const miss = FIELDS.filter(([k, , req]) => req && map[k] < 0).map(f => f[1].toLowerCase());
    if (miss.length) { out.innerHTML = `<p class="bck-err">We couldn't find the ${miss.length > 1 ? miss.slice(0, -1).join(", ") + " and " + miss.at(-1) + " columns" : miss[0] + " column"}. Pick ${miss.length > 1 ? "them" : "it"} in the lists above.</p>`; status.textContent = ""; return; }
    const t0 = performance.now(), r = run(data, map, limit), ms = Math.round(performance.now() - t0);
    if (!r.bills.length) { out.innerHTML = `<p class="bck-err">No rows had a supplier, an amount and a date we could read. Check the columns above.</p>`; return; }
    const value = r.bills.reduce((s, b) => s + b.amount, 0), risk = r.risk;
    const sup = new Set(r.bills.map(b => b.sk)).size;
    const span = `${fmtD(Math.min(...r.bills.map(b => b.date)))} to ${fmtD(Math.max(...r.bills.map(b => b.date)))}`;
    status.textContent = `Checked ${r.bills.length} bills in ${ms} ms. Your file stayed on this device.`;
    let h = `<div class="bck-k"><div><span>Bills checked</span><b>${r.bills.length.toLocaleString("en-AU")}</b><small>${sup} suppliers · ${span}</small></div>
      <div><span>Value checked</span><b>${aud0(value)}</b></div>
      <div class="${r.F.length ? "w" : ""}"><span>Worth a look</span><b>${r.F.length}</b><small>Prompts for a person, not conclusions</small></div>
      <div class="${risk ? "r" : ""}"><span>Could have been paid twice</span><b>${aud0(risk)}</b><small>Duplicates and repeated invoice numbers</small></div></div>`;
    if (r.skipped || r.merged) h += `<p class="fine">${r.skipped ? `${r.skipped} ${r.skipped === 1 ? "row" : "rows"} skipped (no supplier, amount or date). ` : ""}${r.merged ? `${r.merged} line-item ${r.merged === 1 ? "row" : "rows"} combined into ${r.merged === 1 ? "its bill" : "their bills"}.` : ""}</p>`;
    const ran = 8 - r.na.length;
    if (r.na.length) h += `<p class="bck-na"><b>Not assessed:</b> ${r.na.map(([t, , why]) => `${CHECKS[t][0].toLowerCase()} (${why})`).join("; ")}. Add those columns to run ${r.na.length === 1 ? "it" : "them"}.</p>`;
    if (!r.F.length) h += `<p class="bck-ok">Nothing flagged by the ${ran} checks that ran. That's a good sign, not a clean bill of health: these are the quick checks, not all of them.</p>`;
    h += `<p class="fine">Dates are read as day/month/year. "Could have been paid twice" counts each extra bill once.</p>`;
    for (const [type, [title, lvl, why]] of Object.entries(CHECKS)) {
      const fs = r.F.filter(f => f.type === type); if (!fs.length) continue;
      const rowsH = fs.slice(0, 40).map(f => f.items.map((b, i) => `<tr${i ? ' class="c"' : ""}><td>${i ? "" : esc(b.supplier)}</td><td>${esc(b.invoice) || "<i>none</i>"}</td><td>${fmtD(b.date)}</td><td class="n">${aud(b.amount)}</td><td>${i ? "" : esc(f.detail)}</td></tr>`).join("")).join("");
      h += `<details class="bck-f ${lvl}" open><summary><b>${title}</b><em>${fs.length}</em></summary><p>${why}</p>
        <div class="tblw"><table class="tbl"><thead><tr><th>Supplier</th><th>Bill no.</th><th>Date</th><th class="n">Amount</th><th>Why</th></tr></thead><tbody>${rowsH}</tbody></table></div>
        ${fs.length > 40 ? `<p class="fine">And ${fs.length - 40} more in the download.</p>` : ""}</details>`;
    }
    h += `<div class="bck-act"><button type="button" class="btn" id="bcCsv"${r.F.length ? "" : " disabled"}>Download the findings (CSV)</button><button type="button" class="btn ghost" id="bcClear">Clear everything</button></div>`;
    h += `<div class="bck-next"><h3>${risk ? `${aud0(risk)} in this file could have been paid twice. Want these checks on every bill, before it's paid?` : r.F.length ? "Want these checks on every bill, before it's paid?" : "Want the checks these eight can't do?"}</h3>
      <p>The two-week cash &amp; data check goes further, from your full exports: unbilled work, margin leaks and manual bottlenecks, with the records behind each finding. $1,500 fixed, credited if you go ahead. Or set up a financial controller agent that runs these checks on every bill and holds anything odd for you.</p>
      <div class="hz-ctas"><a class="btn primary" href="/contact/?topic=Two-week%20cash%20%26%20data%20check#form">Ask about the check</a><a class="btn ghost" href="/contact/?topic=Discovery%20call#form">Book a 20-minute fit check</a><a class="btn ghost" href="/services/ai-readiness-sprint/">About the agent</a></div></div>`;
    out.innerHTML = h;
    $("#bcCsv").onclick = () => {
      const q = s => { let v = String(s ?? ""); if (/^[=+@\t\r]/.test(v) || (/^-/.test(v) && isNaN(+v))) v = "'" + v; return `"${v.replace(/"/g, '""')}"`; }; // stop spreadsheet formulas
      const lines = [["Check", "Supplier", "Bill no.", "Bill date", "Amount", "Row in file", "Why"].join(",")];
      r.F.forEach(f => f.items.forEach(b => lines.push([CHECKS[f.type][0], b.supplier, b.invoice, fmtD(b.date), b.amount.toFixed(2), b.row, f.detail].map(q).join(","))));
      const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([lines.join("\r\n")], { type: "text/csv" }));
      a.download = "bill-check-findings.csv"; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 4000);
    };
    $("#bcClear").onclick = () => { data = map = null; out.innerHTML = mapBox.innerHTML = ""; status.textContent = "Cleared. Nothing was kept."; root.classList.remove("has"); $("#bcFile").value = ""; };
  }
  function readFile(f) {
    if (!f) return;
    if (f.size > MAX_BYTES) { status.textContent = "That file is over 25 MB. Export a shorter date range."; return; }
    if (!/\.(csv|txt|tsv)$/i.test(f.name) && !/csv|text/.test(f.type)) { status.textContent = "Save it as CSV first (in Excel: File, Save As, CSV). Then drop it here."; return; }
    status.textContent = "Reading…";
    const fr = new FileReader(); fr.onload = () => load(fr.result, f.name); fr.onerror = () => status.textContent = "Couldn't read that file."; fr.readAsText(f);
  }
  const drop = $("#bcDrop");
  $("#bcFile").onchange = e => readFile(e.target.files[0]);
  ["dragenter", "dragover"].forEach(ev => drop.addEventListener(ev, e => { e.preventDefault(); drop.classList.add("on"); }));
  ["dragleave", "drop"].forEach(ev => drop.addEventListener(ev, e => { e.preventDefault(); drop.classList.remove("on"); }));
  drop.addEventListener("drop", e => readFile(e.dataTransfer.files[0]));
  $("#bcSample").onclick = () => { status.textContent = "Loading the sample…"; fetch("/data/sample-bills.csv").then(r => r.text()).then(t => load(t, "sample-bills.csv (made-up building company)")).catch(() => status.textContent = "Couldn't load the sample. Try again."); };
  limIn.addEventListener("change", () => data && go());
})();
