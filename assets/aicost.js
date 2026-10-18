/* AI running-cost calculator page. Prices, job assumptions and arithmetic live in aicost-core.js.
   Runs in the browser; nothing is stored or sent. */
(() => {
  const root = document.getElementById("aic"); if (!root) return;

  const C = window.BeizAICost; if (!C) return;
  const { CHECKED, MODELS, JOBS, perRunUSD, aud } = C;
  const $ = id => document.getElementById(id);
  const num = (id, d) => { const v = parseFloat($(id).value); return Number.isFinite(v) && v >= 0 ? v : d; };

  // Model select
  const sel = $("aicModel");
  MODELS.forEach(m => { const o = document.createElement("option"); o.value = m.id; o.textContent = `${m.name} (${m.v})`; sel.appendChild(o); });
  sel.value = "sonnet";

  const loadJob = k => {
    const j = JOBS[k]; if (!j) return;
    $("aicRuns").value = j.runs; $("aicPages").value = j.pages; $("aicWords").value = j.words; $("aicSteps").value = j.steps; $("aicMins").value = j.mins;
  };

  const render = () => {
    const x = {
      runs: num("aicRuns", 0), pages: num("aicPages", 0), words: num("aicWords", 0), steps: num("aicSteps", 1),
      mins: num("aicMins", 0), rate: num("aicRate", 0), instrWords: num("aicInstr", 0), think: num("aicThink", 0),
      margin: num("aicMargin", 0), fx: num("aicFx", C.FX) || C.FX, cache: $("aicCache").checked,
    };
    const rows = MODELS.map(m => { const r = perRunUSD(m, x); const run = r.usd / x.fx; return { m, run, month: run * x.runs, longOn: r.longOn, tokIn: r.tokIn, tokOut: r.tokOut }; })
      .sort((a, b) => a.month - b.month);
    const pick = rows.find(r => r.m.id === sel.value) || rows[0];
    const people = x.runs * x.mins / 60 * x.rate;
    const total = pick.month + people;
    const share = total > 0 ? pick.month / total : 0;

    $("aicK1").textContent = aud(pick.month); $("aicK1s").textContent = pick.m.name;
    $("aicK2").textContent = aud(pick.run, true); $("aicK2s").textContent = `about ${Math.round(pick.tokIn + pick.tokOut).toLocaleString("en-AU")} tokens`;
    $("aicK3").textContent = aud(people); $("aicK3s").textContent = `${(x.runs * x.mins / 60).toLocaleString("en-AU", { maximumFractionDigits: 1 })} hours of checking`;
    $("aicK4").textContent = Math.round(share * 100) + "%"; $("aicK4s").textContent = "of the running cost is the model";

    const job = $("aicJob"), jobName = job.options[job.selectedIndex].text;
    let line = `${jobName}: about ${aud(pick.month)} a month in AI usage on ${pick.m.name}, against about ${aud(people)} of your people's time checking the work.`;
    if (total > 0 && share < 0.3) line += " Here the model is the small part. What moves the total is how long the checking takes, so clear evidence for the person approving matters more than a cheaper model.";
    else if (share >= 0.5) line += " Here the model is most of the running cost. A smaller model, or sending less text at each step, is worth testing on your past records.";
    $("aicSay").textContent = line;
    const j = JOBS[job.value]; $("aicJobSay").textContent = j ? j.say : "Your own figures.";

    $("aicRows").innerHTML = rows.map(r => {
      const note = [r.m.note, r.longOn ? "Long-prompt rate applied" : ""].filter(Boolean).join(". ");
      const on = r.m.id === pick.m.id;
      return `<tr${on ? ' class="on" aria-current="true"' : ""}><td><button type="button" data-m="${r.m.id}" aria-pressed="${on}">${r.m.name}</button><small>${r.m.v} · ${r.m.tier}${note ? " · " + note : ""}</small></td><td class="n">${aud(r.run, true)}</td><td class="n">${aud(r.month)}</td></tr>`;
    }).join("");
  };

  $("aicJob").addEventListener("change", e => { loadJob(e.target.value); render(); });
  root.addEventListener("input", e => {
    if (e.target.closest(".aic-job-fields")) $("aicJob").value = "custom";
    render();
  });
  sel.addEventListener("change", render);
  $("aicRows").addEventListener("click", e => { const b = e.target.closest("button[data-m]"); if (b) { sel.value = b.dataset.m; render(); } });
  $("aicChecked").textContent = CHECKED;

  loadJob("bill"); render();
})();
