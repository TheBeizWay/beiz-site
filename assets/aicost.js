/* AI running-cost calculator. Runs in the browser; nothing is stored or sent.
   Prices: USD per million tokens, standard tier, text. Checked 18 Oct 2026 on each vendor's own pricing page.
   Where a vendor has published a dated price change, each step has a "from" date and the page uses the one in force today. */
(() => {
  const root = document.getElementById("aic"); if (!root) return;

  const CHECKED = "18 October 2026";
  const MODELS = [
    { id: "haiku", name: "Claude Haiku 5.5", v: "Anthropic", tier: "Small", p: [{ in: 0.10, c: 0.01, out: 0.50 }], long: { at: 100000, in: 0.50, c: 0.05, out: 2.50 }, note: "Higher rate for prompts over 100,000 tokens" },
    { id: "luna", name: "GPT-6 Luna", v: "OpenAI", tier: "Small", p: [{ in: 0.10, c: 0.01, out: 0.50 }] },
    { id: "flite", name: "Gemini 3.5 Flash-Lite", v: "Google", tier: "Small", p: [{ in: 0.30, c: 0.03, out: 2.50 }] },
    { id: "flash", name: "Gemini 3.8 Flash", v: "Google", tier: "Mid", p: [{ in: 0.75, c: 0.075, out: 3.75 }, { from: "2027-01-01", in: 1.50, c: 0.15, out: 7.50 }], note: "Introductory price; doubles from 1 January 2027" },
    { id: "sonnet", name: "Claude Sonnet 5.5", v: "Anthropic", tier: "Mid", p: [{ in: 2, c: 0.10, out: 10 }] },
    { id: "sol", name: "GPT-6.1 Sol", v: "OpenAI", tier: "Mid", p: [{ in: 2, c: 0.10, out: 10 }] },
    { id: "argon", name: "Gemini 4 Argon", v: "Google", tier: "Top", p: [{ in: 2, c: 0.10, out: 10 }, { from: "2026-12-01", in: 4, c: 0.20, out: 20 }], note: "Introductory price; doubles from 1 December 2026" },
    { id: "opus", name: "Claude Opus 5.5", v: "Anthropic", tier: "Top", p: [{ in: 4, c: 0.20, out: 20 }] },
    { id: "astra", name: "GPT-6 Astra", v: "OpenAI", tier: "Top", p: [{ in: 10, c: 1, out: 50 }] },
  ];

  // Starting assumptions for each job. They are guesses to change, not measurements.
  const JOBS = {
    bill: { runs: 300, pages: 2, words: 120, steps: 4, mins: 0.5, say: "Most bills pass. A person looks at the few that are held." },
    email: { runs: 400, pages: 1, words: 180, steps: 3, mins: 1.5, say: "A person reads every draft before it's sent." },
    bank: { runs: 22, pages: 12, words: 300, steps: 6, mins: 5, say: "One run each business day. A person clears the lines that don't match." },
    client: { runs: 10, pages: 15, words: 400, steps: 8, mins: 20, say: "Your compliance officer decides every possible match and every high-risk client." },
    report: { runs: 1, pages: 40, words: 1500, steps: 12, mins: 60, say: "One pack a month. The owner reviews every number before it leaves the business." },
    custom: null,
  };

  const TOK_PER_WORD = 1.4, WORDS_PER_PAGE = 500;
  const $ = id => document.getElementById(id);
  const num = (id, d) => { const v = parseFloat($(id).value); return Number.isFinite(v) && v >= 0 ? v : d; };
  const today = new Date().toISOString().slice(0, 10);
  const rateFor = m => { let r = m.p[0]; m.p.forEach(x => { if (x.from && x.from <= today) r = x; }); return r; };

  const aud = (x, small) => {
    if (small && x < 0.01) return x < 0.001 ? "under A$0.001" : "A$" + x.toFixed(3);
    if (x < 10) return "A$" + x.toFixed(2);
    return "A$" + Math.round(x).toLocaleString("en-AU");
  };

  // Model select
  const sel = $("aicModel");
  MODELS.forEach(m => { const o = document.createElement("option"); o.value = m.id; o.textContent = `${m.name} (${m.v})`; sel.appendChild(o); });
  sel.value = "sonnet";

  const loadJob = k => {
    const j = JOBS[k]; if (!j) return;
    $("aicRuns").value = j.runs; $("aicPages").value = j.pages; $("aicWords").value = j.words; $("aicSteps").value = j.steps; $("aicMins").value = j.mins;
  };

  const perRunUSD = (m, x) => {
    const instr = x.instrWords * TOK_PER_WORD, docs = x.pages * WORDS_PER_PAGE * TOK_PER_WORD;
    const perStep = instr + docs;
    let r = rateFor(m), longOn = false;
    if (m.long && perStep > m.long.at) { r = m.long; longOn = true; }
    // Step 1 sends everything fresh. Later steps reuse the standing instructions from the cache if caching is on.
    // Documents are counted as fresh on every step, which errs on the high side.
    const steps = Math.max(1, Math.round(x.steps));
    const cached = x.cache ? (steps - 1) * instr : 0;
    const fresh = steps * perStep - cached;
    const out = x.words * TOK_PER_WORD + steps * x.think;
    const usd = (fresh * r.in + cached * r.c + out * r.out) / 1e6 * (1 + x.margin / 100);
    return { usd, longOn, tokIn: steps * perStep, tokOut: out };
  };

  const render = () => {
    const x = {
      runs: num("aicRuns", 0), pages: num("aicPages", 0), words: num("aicWords", 0), steps: num("aicSteps", 1),
      mins: num("aicMins", 0), rate: num("aicRate", 0), instrWords: num("aicInstr", 0), think: num("aicThink", 0),
      margin: num("aicMargin", 0), fx: num("aicFx", 0.6946) || 0.6946, cache: $("aicCache").checked,
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
