/* Job profitability experience: UI over BeizModel (signature-model.js). Everything is calculated in the browser from fictional records. */
(function () {
  "use strict";
  const M = window.BeizModel, root = document.getElementById("jp"); if (!M || !root) return;
  const D = M.DATA, $ = s => root.querySelector(s);
  const aud = n => (n < 0 ? "-$" : "$") + Math.abs(Math.round(n)).toLocaleString("en-AU");
  const pc = x => (Math.round(x * 1000) / 10).toFixed(1) + "%";
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const BASE = Date.UTC(2026, 6, 6); // day 0 of the fictional records: Mon 6 Jul 2026
  const day = d => new Date(BASE + d * 864e5).toLocaleDateString("en-AU", { weekday: "short", day: "numeric", month: "short", timeZone: "UTC" });
  const MEANS = {
    hours: ["Labour ran over the quote. Check whether the quoted hours were realistic, whether there was rework, and whether extra work was agreed but not billed.",
            "Timesheets show hours booked to the job, not why. They may include rework, travel, or time coded to the wrong job. Extra hours aren't revenue until a variation is agreed and billed."],
    materials: ["Materials cost more than quoted. Check supplier price changes, waste, and whether extra items should have been charged to the customer.",
                "Bills are linked to the job by reference. A bill coded to the wrong job would distort this result."],
    price: ["Hours and materials are close to the quote, so the quote itself left too little margin at this labour cost.",
            "The labour cost per hour is an assumption, and overheads aren't included. Pricing needs a decision, not just a recalculation."],
  };
  let lc = D.labourCost, view = "fin", openJob = null;

  const range = $("#jpRange"), num = $("#jpNum"), msg = $("#jpMsg");
  function setLc(v, from) {
    const c = M.clean("labourCost", v, D), ok = c === Number(v) && v !== "";
    msg.textContent = ok ? "" : `Enter a number from ${M.LIMITS.labourCost[0]} to ${M.LIMITS.labourCost[1]}. Using $${c}.`;
    if (c === lc) { if (from !== "range") range.value = c; if (from !== "num" || !ok) num.value = c; return; } // nothing changed: no redraw
    lc = c; if (from !== "range") range.value = Math.min(Math.max(c, +range.min), +range.max); if (from !== "num" || !ok) { if (from !== "num") num.value = c; }
    render();
  }
  range.addEventListener("input", () => setLc(range.value, "range"));
  num.addEventListener("change", () => setLc(num.value, "num"));
  $("#jpReset").addEventListener("click", () => { num.value = D.labourCost; setLc(D.labourCost); });

  const tabs = [...root.querySelectorAll("[role=tab]")];
  tabs.forEach((t, i) => {
    t.addEventListener("click", () => select(i));
    t.addEventListener("keydown", e => { const k = e.key, n = tabs.length; let j = k === "ArrowRight" ? (i + 1) % n : k === "ArrowLeft" ? (i - 1 + n) % n : k === "Home" ? 0 : k === "End" ? n - 1 : -1; if (j >= 0) { e.preventDefault(); select(j); tabs[j].focus(); } });
  });
  function select(i) { tabs.forEach((t, j) => { t.setAttribute("aria-selected", i === j); t.tabIndex = i === j ? 0 : -1; }); view = tabs[i].dataset.v; render(); }

  function render() {
    const fj = document.activeElement && document.activeElement.classList.contains("jp-open") ? document.activeElement.dataset.job : null; // keep focus across redraws
    const ms = M.margins(D, { labourCost: lc }), rev = ms.reduce((s, m) => s + m.value, 0), cost = ms.reduce((s, m) => s + m.cost, 0), below = ms.filter(m => m.below);
    $("#jpRev").textContent = aud(rev); $("#jpCost").textContent = aud(cost); $("#jpMar").textContent = pc((rev - cost) / rev);
    $("#jpBelow").textContent = `${below.length} of ${ms.length}`;
    $("#jpBelowNote").textContent = below.length ? below.map(m => m.job).join(", ") : "None below target";
    const head = view === "fin" ? ["Job", "Price", "Cost", "Margin", "Margin vs 25% target", ""] : ["Job", "Hours: actual / quoted", "Materials: actual / quoted", "Main cause", ""];
    $("#jpHead").innerHTML = "<tr>" + head.map((h, i) => `<th scope="col"${i && i < head.length - 1 && view === "fin" && i < 4 ? ' class="n"' : ""}>${h}</th>`).join("") + "</tr>";
    $("#jpBody").innerHTML = ms.map(m => {
      const j = D.jobs.find(x => x.id === m.job), st = m.below ? '<span class="chip c-held">Below target</span>' : '<span class="chip c-ok">On target</span>';
      const open = `<button type="button" class="jp-open" data-job="${m.job}" aria-label="Open ${m.job} records">${m.below ? "Investigate" : "Records"}</button>`;
      const id = `<th scope="row"><b>${m.job}</b><span>${esc(m.title)} · ${esc(m.customer)}</span></th>`;
      if (view === "fin") {
        const w = Math.max(0, Math.min(100, m.pct * 100 / 0.4));
        return `<tr class="${m.below ? "lo" : ""}">${id}<td class="n">${aud(m.value)}</td><td class="n">${aud(m.cost)}</td><td class="n">${aud(m.margin)}</td>
          <td><div class="bar" aria-hidden="true"><i style="width:${w}%"></i><em style="left:${(25 / 40) * 100}%"></em></div><span class="pc">${pc(m.pct)}</span> ${st}</td><td>${open}</td></tr>`;
      }
      const ho = j.hours > j.quotedHours * 1.1, mo = j.materials > j.quotedMaterials * 1.1;
      return `<tr class="${m.below ? "lo" : ""}">${id}<td class="${ho ? "hot" : ""}">${j.hours} / ${j.quotedHours}</td><td class="${mo ? "hot" : ""}">${aud(j.materials)} / ${aud(j.quotedMaterials)}</td>
        <td>${m.causes.length ? esc(m.causes[0].text) : "On quote"}</td><td>${open}</td></tr>`;
    }).join("");
    root.querySelectorAll(".jp-open").forEach(b => b.addEventListener("click", () => detail(b.dataset.job, b)));
    if (fj) { const f = root.querySelector(`.jp-open[data-job="${fj}"]`); f && f.focus(); }
    if (openJob) detail(openJob);
  }

  function detail(id, from) {
    openJob = id;
    const m = M.margins(D, { labourCost: lc }).find(x => x.job === id), r = M.records(D, id), box = $("#jpDetail");
    const why = m.causes.length ? m.causes : [{ kind: null, text: "No cause flagged: actuals are within 10% of the quote." }];
    const means = m.below ? why.filter(c => c.kind).map(c => `<li>${MEANS[c.kind][0]}</li>`).join("") : "<li>On target at this labour cost. No action suggested.</li>";
    const unsure = [...new Set(why.filter(c => c.kind).map(c => MEANS[c.kind][1]))].map(t => `<li>${t}</li>`).join("") || "<li>The labour cost per hour is an assumption, and overheads aren't included.</li>";
    const tsRows = r.timesheets.map(t => `<tr><td>${day(t.date)}</td><td>${esc(t.staff)}</td><td class="n">${t.hours}</td><td class="n">${aud(t.hours * lc)}</td></tr>`).join("");
    box.hidden = false;
    box.innerHTML = `<div class="jp-dh"><div><p class="mono eyb">${m.job} · ${esc(m.customer)} · ${m.below ? "below target" : "on target"}</p><h3 id="jpDT" tabindex="-1">${esc(m.title)}</h3></div><button type="button" class="jp-x" id="jpClose">Close</button></div>
      <div class="jp-calc" aria-label="Margin calculation">
        <div><span>Price (invoice ${r.invoice.ref})</span><b>${aud(m.value)}</b></div>
        <div><span>Labour: ${m.hours} hours × $${lc}</span><b>− ${aud(m.labour)}</b></div>
        <div><span>Materials: ${r.materials.length} supplier bills</span><b>− ${aud(m.materials)}</b></div>
        <div class="tot"><span>Margin</span><b>${aud(m.margin)} <small>${pc(m.pct)}</small></b></div></div>
      <div class="jp-cols"><div><h4>Why it was flagged</h4><ul>${why.map(c => `<li>${esc(c.text)}</li>`).join("")}</ul></div>
      <div><h4>What it may mean</h4><ul>${means}</ul></div><div><h4>What the records can't tell you</h4><ul>${unsure}</ul></div></div>
      <h4>Source records</h4>
      <div class="tblw"><table class="tbl"><caption>Supplier bills for materials</caption><thead><tr><th>Reference</th><th>Supplier</th><th class="n">Amount</th></tr></thead><tbody>${r.materials.map(x => `<tr><td>${x.ref}</td><td>${esc(x.supplier)}</td><td class="n">${aud(x.amount)}</td></tr>`).join("")}<tr class="sum"><td colspan="2">Total</td><td class="n">${aud(m.materials)}</td></tr></tbody></table></div>
      <details><summary>Timesheet lines (${r.timesheets.length}, ${m.hours} hours)</summary><div class="tblw"><table class="tbl"><thead><tr><th>Date</th><th>Staff</th><th class="n">Hours</th><th class="n">At $${lc}/h</th></tr></thead><tbody>${tsRows}<tr class="sum"><td colspan="2">Total</td><td class="n">${m.hours}</td><td class="n">${aud(m.labour)}</td></tr></tbody></table></div></details>`;
    $("#jpClose").addEventListener("click", close);
    if (from) { box.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" }); $("#jpDT").focus({ preventScroll: true }); }
  }
  function close() { const b = $("#jpDetail"), id = openJob; b.hidden = true; b.innerHTML = ""; openJob = null; const o = root.querySelector(`.jp-open[data-job="${id}"]`) || root.querySelector(".jp-open"); o && o.focus(); }
  document.addEventListener("keydown", e => { if (e.key === "Escape" && openJob) close(); });
  render();
})();
