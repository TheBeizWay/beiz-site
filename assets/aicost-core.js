/* Shared prices and arithmetic for the AI running-cost calculator (/ai-cost-calculator/) and the Bei-zAI helper.
   Prices: USD per million tokens, standard tier, text. Checked 18 Oct 2026 on each vendor's own pricing page:
   platform.claude.com/docs/en/about-claude/pricing · developers.openai.com/api/docs/pricing · ai.google.dev/gemini-api/docs/pricing
   Recheck monthly. Where a vendor has published a dated price change, each step has a "from" date and the one in force today is used.
   Runs in the browser; nothing is stored or sent. */
window.BeizAICost = (() => {
  const CHECKED = "18 October 2026";
  const FX = 0.6946; // US$ per A$1, AUD/USD close 16 Oct 2026
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
    bill: { label: "Checking supplier bills", runs: 300, pages: 2, words: 120, steps: 4, mins: 0.5, say: "Most bills pass. A person looks at the few that are held." },
    email: { label: "Drafting replies to customer emails", runs: 400, pages: 1, words: 180, steps: 3, mins: 1.5, say: "A person reads every draft before it's sent." },
    bank: { label: "Matching bank lines to the ledger", runs: 22, pages: 12, words: 300, steps: 6, mins: 5, say: "One run each business day. A person clears the lines that don't match." },
    client: { label: "New client checks (AML/CTF)", runs: 10, pages: 15, words: 400, steps: 8, mins: 20, say: "Your compliance officer decides every possible match and every high-risk client." },
    report: { label: "Monthly report commentary", runs: 1, pages: 40, words: 1500, steps: 12, mins: 60, say: "One pack a month. The owner reviews every number before it leaves the business." },
  };
  const DEFAULTS = { instrWords: 2500, think: 400, margin: 25, cache: true, rate: 60, fx: FX };

  const TOK_PER_WORD = 1.4, WORDS_PER_PAGE = 500;
  const today = new Date().toISOString().slice(0, 10);
  const rateFor = m => { let r = m.p[0]; m.p.forEach(x => { if (x.from && x.from <= today) r = x; }); return r; };

  const aud = (x, small) => {
    if (small && x < 0.01) return x < 0.001 ? "under A$0.001" : "A$" + x.toFixed(3);
    if (x < 10) return "A$" + x.toFixed(2);
    return "A$" + Math.round(x).toLocaleString("en-AU");
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

  // One job on one model, with the default assumptions. Used by the Bei-zAI helper.
  const estimate = (jobKey, modelId) => {
    const j = JOBS[jobKey], m = MODELS.find(x => x.id === modelId);
    if (!j || !m) return null;
    const x = Object.assign({}, DEFAULTS, j);
    const run = perRunUSD(m, x).usd / x.fx, aiMonth = run * x.runs, people = x.runs * x.mins / 60 * x.rate;
    return { job: j, model: m, run, aiMonth, people, share: aiMonth + people > 0 ? aiMonth / (aiMonth + people) : 0 };
  };

  return { CHECKED, FX, MODELS, JOBS, DEFAULTS, rateFor, perRunUSD, aud, estimate };
})();
