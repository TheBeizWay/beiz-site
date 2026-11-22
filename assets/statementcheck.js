/* Beiz free supplier statement check (Nov 2026).
   Compares a supplier statement with the same supplier's entries exported from Xero (or any ledger).
   Runs entirely in the browser: files are read locally and never uploaded or sent anywhere. */
(function () {
  "use strict";
  var $ = function (s) { return document.querySelector(s); };
  var root = $("#sc");
  if (!root) return;

  var files = { st: null, xe: null };
  var CENT = 0.005;

  /* ---------- helpers ---------- */
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function money(n) { var a = Math.abs(n), s = a.toLocaleString("en-AU", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); return (n < -CENT ? "-$" : "$") + s; }
  function fmtDate(d) { return d ? d.toLocaleDateString("en-AU", { day: "2-digit", month: "short", year: "numeric" }) : ""; }
  function days(a, b) { return a && b ? Math.round(Math.abs(a - b) / 864e5) : 9999; }
  function eq(a, b) { return Math.abs(a - b) < CENT; }

  function parseCSV(text) {
    var rows = [], row = [], f = "", q = false, i, c;
    text = text.replace(/^﻿/, "");
    var delim = (text.split("\n")[0].match(/\t/g) || []).length > (text.split("\n")[0].match(/,/g) || []).length ? "\t" : ",";
    for (i = 0; i < text.length; i++) {
      c = text[i];
      if (q) { if (c === '"') { if (text[i + 1] === '"') { f += '"'; i++; } else q = false; } else f += c; }
      else if (c === '"') q = true;
      else if (c === delim) { row.push(f); f = ""; }
      else if (c === "\n" || c === "\r") { if (c === "\r" && text[i + 1] === "\n") i++; row.push(f); rows.push(row); row = []; f = ""; }
      else f += c;
    }
    if (f !== "" || row.length) { row.push(f); rows.push(row); }
    return rows.filter(function (r) { return r.some(function (x) { return String(x).trim() !== ""; }); });
  }

  function parseAmount(s) {
    s = String(s || "").trim(); if (!s) return null;
    var neg = /^\(.*\)$/.test(s) || /^-/.test(s) || /-$/.test(s) || /\bCR\b/i.test(s);
    var n = parseFloat(s.replace(/[^0-9.]/g, ""));
    if (isNaN(n)) return null;
    return neg ? -n : n;
  }

  var MON = { jan: 0, feb: 1, mar: 2, apr: 3, may: 4, jun: 5, jul: 6, aug: 7, sep: 8, oct: 9, nov: 10, dec: 11 };
  function parseDate(s) {
    s = String(s || "").trim(); var m;
    if ((m = s.match(/^(\d{4})-(\d{1,2})-(\d{1,2})/))) return new Date(+m[1], +m[2] - 1, +m[3]);
    if ((m = s.match(/^(\d{1,2})[\/.\-](\d{1,2})[\/.\-](\d{2,4})/))) { var y = +m[3]; if (y < 100) y += 2000; return new Date(y, +m[2] - 1, +m[1]); }
    if ((m = s.match(/^(\d{1,2})[\s\-]([A-Za-z]{3})[A-Za-z]*[\s\-,]+(\d{2,4})/))) { var yy = +m[3]; if (yy < 100) yy += 2000; var mo = MON[m[2].toLowerCase()]; if (mo != null) return new Date(yy, mo, +m[1]); }
    return null;
  }

  function findCol(head, tests) {
    for (var t = 0; t < tests.length; t++) for (var i = 0; i < head.length; i++) if (tests[t].test(head[i])) return i;
    return -1;
  }

  function typeOf(text, ref, signed) {
    var t = String(text || "").toLowerCase();
    if (/credit/.test(t)) return "credit";
    /* "Payable Invoice" (Xero) is a bill, so look for invoice words before payment words, and don't treat "payable" as a payment */
    if (/inv|bill|charge/.test(t)) return "invoice";
    if (/\bpayments?\b|\bpaid\b|remit|spend money|receipt|\beft\b|\bbpay\b|bank transfer|direct debit/.test(t)) return "payment";
    if (/^\s*(cn|crn|credit)/i.test(ref || "")) return "credit";
    if (signed != null && signed < 0) return "payment";
    return "invoice";
  }

  /* side: "st" (supplier statement: debit = invoice) or "xe" (ledger: credit = bill) */
  function readLines(text, side) {
    var rows = parseCSV(text);
    if (rows.length < 2) throw new Error("The file has no data rows.");
    var head = rows[0].map(function (h) { return String(h).trim().toLowerCase(); });
    var col = {
      date: findCol(head, [/^date$/, /date/]),
      ref: findCol(head, [/^reference$/, /invoice\s*(no|number|#)/, /^(ref|reference|number|invoice|document|doc(ument)? no|inv no)$/, /ref/, /number|invoice|document/]),
      type: findCol(head, [/^type$/, /transaction type|doc(ument)? type|^source$/, /type/]),
      desc: findCol(head, [/description|details|memo|narration|particulars/]),
      amount: findCol(head, [/^amount$/, /^(total|gross|amount aud|value)$/, /amount|total/]),
      debit: findCol(head, [/^debit/, /debit/]),
      credit: findCol(head, [/^credit$/, /^credit\b(?!\s*note)/])
    };
    if (col.date < 0 || col.ref < 0 || (col.amount < 0 && col.debit < 0 && col.credit < 0)) {
      throw new Error("Couldn't find Date, Reference and Amount columns. Headers found: " + rows[0].join(", "));
    }
    var out = [];
    rows.slice(1).forEach(function (r, idx) {
      var d = parseDate(r[col.date]);
      var ref = String(r[col.ref] || "").trim();
      var tText = col.type >= 0 ? r[col.type] : "";
      var dText = col.desc >= 0 ? r[col.desc] : "";
      var amt = null, signed = null;
      if (col.amount >= 0) { amt = parseAmount(r[col.amount]); signed = amt; }
      if ((amt == null || amt === 0) && (col.debit >= 0 || col.credit >= 0)) {
        var dr = col.debit >= 0 ? parseAmount(r[col.debit]) : null, cr = col.credit >= 0 ? parseAmount(r[col.credit]) : null;
        if (dr) { amt = dr; signed = side === "st" ? Math.abs(dr) : -Math.abs(dr); }
        else if (cr) { amt = cr; signed = side === "st" ? -Math.abs(cr) : Math.abs(cr); }
      }
      if (amt == null || !d) return;
      if (/^(opening|closing|balance|total)/i.test(ref + " " + tText + " " + dText)) return;
      var type = typeOf(tText || dText, ref, signed);
      var val = Math.abs(amt) * (type === "invoice" ? 1 : -1);
      out.push({ row: idx + 2, date: d, ref: ref, type: type, amount: val, raw: tText || dText, used: false });
    });
    if (!out.length) throw new Error("No rows with a readable date and amount. Dates should be DD/MM/YYYY or YYYY-MM-DD.");
    return { lines: out, map: { date: rows[0][col.date], ref: rows[0][col.ref], type: col.type >= 0 ? rows[0][col.type] : "(worked out from the reference and sign)", amount: col.amount >= 0 ? rows[0][col.amount] : [col.debit >= 0 ? rows[0][col.debit] : null, col.credit >= 0 ? rows[0][col.credit] : null].filter(Boolean).join(" / ") } };
  }

  function alnum(r) { return String(r || "").toUpperCase().replace(/[^A-Z0-9]/g, ""); }
  function core(r) { var d = String(r || "").replace(/[^0-9]/g, "").replace(/^0+/, ""); return d.length >= 3 ? d : null; }

  /* ---------- matching ---------- */
  function reconcile(st, xe) {
    var res = [], endDate = st.reduce(function (m, l) { return !m || l.date > m ? l.date : m; }, null);
    var docs = function (arr) { return arr.filter(function (l) { return l.type !== "payment"; }); };
    var pays = function (arr) { return arr.filter(function (l) { return l.type === "payment"; }); };

    // 1. invoices and credit notes by reference (exact, then digit core), same type only
    docs(st).forEach(function (s) {
      if (!alnum(s.ref)) return;
      var cand = docs(xe).filter(function (x) { return !x.used && x.type === s.type && alnum(x.ref) && alnum(x.ref) === alnum(s.ref); })[0]
        || docs(xe).filter(function (x) { return !x.used && x.type === s.type && core(x.ref) && core(x.ref) === core(s.ref); })[0];
      if (!cand) return;
      s.used = cand.used = true;
      if (eq(s.amount, cand.amount)) { res.push({ k: "ok", what: "Matched", s: s, x: cand, diff: 0 }); return; }
      var gap = cand.amount - s.amount;
      var cn = docs(xe).filter(function (x) { return !x.used && x.type === "credit" && eq(-x.amount, gap) && days(x.date, cand.date) <= 31; })[0];
      if (cn) { cn.used = true; res.push({ k: "ex", what: "Credit note netted on the statement", s: s, x: cand, x2: cn, diff: 0, next: "The supplier shows " + esc(s.ref) + " net of credit note " + esc(cn.ref) + ". Both are in Xero, so nothing to change." }); return; }
      res.push({ k: "look", what: "Amount differs", s: s, x: cand, diff: gap, next: "Check the original tax invoice. A keying error in Xero is the usual cause." });
    });

    // 2. payments: exact amount near the date, then same amount further apart, then batches of 2-3
    var sp = pays(st), xp = pays(xe);
    sp.forEach(function (s) {
      var c = xp.filter(function (x) { return !x.used && eq(x.amount, s.amount) && days(x.date, s.date) <= 10; }).sort(function (a, b) { return days(a.date, s.date) - days(b.date, s.date); })[0];
      if (c) { s.used = c.used = true; res.push({ k: "ok", what: days(c.date, s.date) ? "Payment matched (dates " + days(c.date, s.date) + " day" + (days(c.date, s.date) > 1 ? "s" : "") + " apart)" : "Payment matched", s: s, x: c, diff: 0 }); }
    });
    sp.forEach(function (s) {
      if (s.used) return;
      var c = xp.filter(function (x) { return !x.used && eq(x.amount, s.amount) && days(x.date, s.date) <= 45; })[0];
      if (c) { s.used = c.used = true; res.push({ k: "look", what: "Payment matched, but dates " + days(c.date, s.date) + " days apart", s: s, x: c, diff: 0, next: "Check the payment date recorded in Xero." }); }
    });
    function combos(target, pool, d0) {
      pool = pool.filter(function (x) { return !x.used && days(x.date, d0) <= 10 && Math.abs(x.amount) < Math.abs(target) + CENT; }).slice(0, 25);
      for (var i = 0; i < pool.length; i++) for (var j = i + 1; j < pool.length; j++) {
        if (eq(pool[i].amount + pool[j].amount, target)) return [pool[i], pool[j]];
        for (var k = j + 1; k < pool.length; k++) if (eq(pool[i].amount + pool[j].amount + pool[k].amount, target)) return [pool[i], pool[j], pool[k]];
      }
      return null;
    }
    sp.forEach(function (s) {
      if (s.used) return;
      var c = combos(s.amount, xp, s.date);
      if (c) { s.used = true; c.forEach(function (x) { x.used = true; }); res.push({ k: "ex", what: "One statement payment = " + c.length + " payments in Xero", s: s, xs: c, diff: 0, next: "Part-payments or a batched remittance. Nothing to change." }); }
    });
    xp.forEach(function (x) {
      if (x.used) return;
      var c = combos(x.amount, sp, x.date);
      if (c) { x.used = true; c.forEach(function (s) { s.used = true; }); res.push({ k: "ex", what: "One Xero payment = " + c.length + " payments on the statement", ss: c, x: x, diff: 0, next: "The supplier applied one payment in parts. Nothing to change." }); }
    });

    // 3. leftovers
    var xeDocs = docs(xe);
    xe.forEach(function (x) {
      if (x.used) return;
      if (x.type === "payment") {
        var transit = endDate && x.date > endDate;
        res.push({ k: transit ? "ex" : "look", what: transit ? "Payment after the statement date (in transit)" : "Payment in Xero, not on the statement", x: x, diff: x.amount, next: transit ? "Should appear on next month's statement." : "Ask the supplier whether they received it, or check it wasn't paid to another supplier." });
        return;
      }
      var twin = xeDocs.filter(function (o) { return o !== x && o.type === x.type && eq(o.amount, x.amount) && days(o.date, x.date) <= 3; })[0];
      res.push({ k: "stop", what: twin ? "Possible duplicate bill in Xero" : (x.type === "credit" ? "Credit note in Xero, not on the statement" : "Bill in Xero, not on the statement"), x: x, diff: x.amount, next: twin ? "Same amount and date as " + esc(twin.ref) + ". Check before it's paid twice." : "Check it belongs to this supplier and hasn't been entered twice under another reference." });
    });
    st.forEach(function (s) {
      if (s.used) return;
      res.push({ k: "stop", what: s.type === "payment" ? "Payment on the statement, not in Xero" : (s.type === "credit" ? "Credit note on the statement, not in Xero" : "On the statement, not in Xero"), s: s, diff: -s.amount, next: s.type === "payment" ? "Find the payment in your bank account and record it." : "Ask the supplier for a copy, check it, then enter it if it's valid." });
    });

    var sum = function (a) { return a.reduce(function (t, l) { return t + l.amount; }, 0); };
    return { res: res, stBal: sum(st), xeBal: sum(xe), endDate: endDate };
  }

  /* ---------- render ---------- */
  var LABEL = { ok: "Matched", ex: "Explained", look: "Needs a look", stop: "Missing or extra" };
  function lineTxt(l) { return l ? esc(l.ref || "(no ref)") + "<small>" + fmtDate(l.date) + " · " + money(l.amount) + "</small>" : "<small>—</small>"; }
  function many(ls) { return ls.map(lineTxt).join("<br>"); }

  function render(out, maps) {
    var r = out.res, n = { ok: 0, ex: 0, look: 0, stop: 0 };
    r.forEach(function (x) { n[x.k]++; });
    var unexplainedItems = r.filter(function (x) { return x.k !== "ok"; });
    var bridge = unexplainedItems.filter(function (x) { return Math.abs(x.diff) > CENT; });
    var bridged = out.stBal + bridge.reduce(function (t, x) { return t + x.diff; }, 0);
    var html = '<div class="sc-map"><b>How your files were read</b>' +
      ["Statement", "Xero"].map(function (lab, i) { var m = maps[i]; return "<p>" + lab + ": date = <i>" + esc(m.date) + "</i>, reference = <i>" + esc(m.ref) + "</i>, type = <i>" + esc(m.type) + "</i>, amount = <i>" + esc(m.amount) + "</i></p>"; }).join("") + "</div>";
    html += '<div class="sc-sum">' + ["ok", "ex", "look", "stop"].map(function (k) { return '<div class="sc-n ' + k + '"><b>' + n[k] + "</b><span>" + LABEL[k] + "</span></div>"; }).join("") + "</div>";
    html += '<h3 class="sc-h">From the statement balance to the Xero balance</h3><table class="sc-br"><tbody>' +
      "<tr><td>Balance per supplier statement" + (out.endDate ? " (to " + fmtDate(out.endDate) + ")" : "") + "</td><td>" + money(out.stBal) + "</td></tr>" +
      bridge.map(function (x) { var l = x.x || x.s; return "<tr><td>" + esc(x.what) + ": " + esc(l.ref || "(no ref)") + "</td><td>" + (x.diff > 0 ? "+" : "") + money(x.diff) + "</td></tr>"; }).join("") +
      '<tr class="tot"><td>Balance per Xero</td><td>' + money(out.xeBal) + "</td></tr>" +
      (Math.abs(bridged - out.xeBal) > CENT ? '<tr class="warn"><td>Not explained by the lines above</td><td>' + money(out.xeBal - bridged) + "</td></tr>" : "") +
      "</tbody></table>";
    var order = { stop: 0, look: 1, ex: 2, ok: 3 };
    r.sort(function (a, b) { return order[a.k] - order[b.k]; });
    html += '<h3 class="sc-h">Line by line</h3><div class="sc-tw"><table class="sc-t"><thead><tr><th>Status</th><th>Statement</th><th>Xero</th><th>Difference</th><th>What to do</th></tr></thead><tbody>' +
      r.map(function (x) {
        return '<tr class="' + x.k + '"><td><span class="sc-s ' + x.k + '">' + LABEL[x.k] + "</span><br>" + esc(x.what) + "</td><td>" + (x.ss ? many(x.ss) : lineTxt(x.s)) + "</td><td>" + (x.xs ? many(x.xs) : lineTxt(x.x) + (x.x2 ? "<br>" + lineTxt(x.x2) : "")) + "</td><td>" + (Math.abs(x.diff) > CENT ? money(x.diff) : "") + "</td><td>" + (x.next || "") + "</td></tr>";
      }).join("") + "</tbody></table></div>";
    html += '<p class="sc-dl"><button type="button" class="btn line" id="scCsv">Download the results (CSV)</button></p>';
    $("#scOut").innerHTML = html;
    $("#scCsv").addEventListener("click", function () {
      var rowsOut = [["Status", "Finding", "Statement ref", "Statement date", "Statement amount", "Xero ref", "Xero date", "Xero amount", "Difference", "What to do"]];
      r.forEach(function (x) {
        var s = x.s || (x.ss && x.ss[0]) || {}, xx = x.x || (x.xs && x.xs[0]) || {};
        rowsOut.push([LABEL[x.k], x.what, s.ref || "", s.date ? fmtDate(s.date) : "", s.amount != null ? s.amount.toFixed(2) : "", xx.ref || "", xx.date ? fmtDate(xx.date) : "", xx.amount != null ? xx.amount.toFixed(2) : "", Math.abs(x.diff) > CENT ? x.diff.toFixed(2) : "", String(x.next || "").replace(/<[^>]+>/g, "")]);
      });
      var csv = rowsOut.map(function (row) { return row.map(function (v) { v = String(v).replace(/&amp;/g, "&").replace(/&#39;/g, "'"); return /[",\n]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v; }).join(","); }).join("\n");
      var a = document.createElement("a");
      a.href = URL.createObjectURL(new Blob([csv], { type: "text/csv" }));
      a.download = "statement-check-results.csv"; document.body.appendChild(a); a.click(); a.remove();
    });
    var nx = $("#scNext"); if (nx) nx.hidden = false;
  }

  function status(msg, bad) { var el = $("#scStatus"); el.textContent = msg; el.className = "bck-status" + (bad ? " bad" : ""); }

  function run(stText, xeText) {
    try {
      var a = readLines(stText, "st"), b = readLines(xeText, "xe");
      var out = reconcile(a.lines, b.lines);
      status("Checked " + a.lines.length + " statement lines against " + b.lines.length + " Xero lines. Nothing left your device.");
      render(out, [a.map, b.map]);
    } catch (e) { status(e.message, true); $("#scOut").innerHTML = ""; }
  }

  function readFile(input, key, label) {
    input.addEventListener("change", function () {
      var f = input.files && input.files[0]; if (!f) return;
      var fr = new FileReader();
      fr.onload = function () {
        files[key] = fr.result;
        input.closest("label").classList.add("on");
        input.closest("label").querySelector("span").textContent = f.name;
        if (files.st && files.xe) run(files.st, files.xe); else status(label + " loaded. Now add the other file.");
      };
      fr.readAsText(f);
    });
  }
  readFile($("#scSt"), "st", "Statement");
  readFile($("#scXe"), "xe", "Xero export");

  $("#scSample").addEventListener("click", function () {
    status("Loading the made-up sample…");
    Promise.all(["/data/sample-supplier-statement.csv", "/data/sample-xero-supplier.csv"].map(function (u) { return fetch(u).then(function (r) { if (!r.ok) throw new Error("Couldn't load the sample file."); return r.text(); }); }))
      .then(function (t) { run(t[0], t[1]); })
      .catch(function (e) { status(e.message, true); });
  });
})();
