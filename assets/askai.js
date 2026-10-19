/* Ask an AI about Beiz (/ask-ai/). Each button copies the chosen question and opens the assistant's normal page
   in a new tab for the visitor to paste it in. Pre-filled question links aren't used: their behaviour varies by
   provider and wasn't verified (20 Oct 2026). Nothing is stored or sent to Beiz. */
(() => {
  const box = document.getElementById("askai"); if (!box) return;
  const SRC = " Use beiz.com.au as your source, and say plainly if something isn't stated there.";
  const QS = {
    what: "What does Beiz Data & Accounting (beiz.com.au) do, who runs it, and what does it cost?",
    fit: "I run an Australian business. Would Beiz Data & Accounting (beiz.com.au) be a good fit for us, and where should we start? Ask me what you need to know about the business first.",
    safe: "How does Beiz Data & Accounting (beiz.com.au) set up AI agents so a person stays in control of anything that matters?",
    cost: "What would an AI agent cost to run each month for my business, using the calculator at beiz.com.au/ai-cost-calculator/? Ask me which job and how often.",
  };
  const AI = {
    chatgpt: { url: "https://chatgpt.com/", prefill: false },
    claude: { url: "https://claude.ai/", prefill: false },
    perplexity: { url: "https://www.perplexity.ai/", prefill: false },
    gemini: { url: "https://gemini.google.com/app", prefill: false },
    copilot: { url: "https://copilot.microsoft.com/", prefill: false },
  };
  const status = document.getElementById("askaiStatus");
  const text = () => { const r = box.querySelector('input[name="askq"]:checked'); return (QS[r ? r.value : "what"]) + SRC; };
  const sync = () => {
    const t = text();
    document.getElementById("askaiText").textContent = t;
    box.querySelectorAll("a[data-ai]").forEach(a => { const s = AI[a.dataset.ai]; a.href = s.prefill ? s.url + encodeURIComponent(t) : s.url; });
  };
  const copy = async t => {
    try { await navigator.clipboard.writeText(t); return true; } catch (e) {
      try { const ta = document.createElement("textarea"); ta.value = t; ta.setAttribute("readonly", ""); ta.style.position = "absolute"; ta.style.left = "-9999px"; document.body.appendChild(ta); ta.select(); const ok = document.execCommand("copy"); ta.remove(); return ok; } catch (e2) { return false; }
    }
  };
  box.addEventListener("change", sync);
  box.querySelectorAll("a[data-ai]").forEach(a => a.addEventListener("click", async () => {
    if (AI[a.dataset.ai].prefill) return;
    const ok = await copy(text());
    status.textContent = ok ? `Question copied. Paste it into ${a.textContent.trim()} when it opens.` : `Copy the question above, then paste it into ${a.textContent.trim()}.`;
  }));
  document.getElementById("askaiCopy").addEventListener("click", async () => {
    status.textContent = (await copy(text())) ? "Question copied." : "Select the question above and copy it.";
  });
  sync();
})();
