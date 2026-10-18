/* Beiz bill review: a six-step walk through one supplier bill. Fictional data, nothing connected. */
(() => {
  const root = document.getElementById("br");
  if (!root) return;
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) root.classList.add("br-still");

  const STEPS = [
    ["Records arrive", "Three records about one job arrive from three places: the bill from the accounts inbox, the quote from the job folder and the timesheet from the time app."],
    ["Checks run", "The checks are rules, not guesses: same supplier, same job, same rate, and hours within both the quote and the timesheet."],
    ["Something doesn't match", "One check fails. The bill is held automatically. It's a possible discrepancy, not proof of an error: there may be a good reason."],
    ["See the evidence", "The three records side by side, with the lines that disagree marked. This is what your approver sees, so nobody has to dig through three systems."],
    ["A person decides", "The agent can't pay, change or send anything on its own. It drafts the question; your approver chooses what happens. Try a choice."],
    ["The outcome, on record", "Every step is logged with who did what and why. The corrected bill goes through the same checks before anyone pays it."]
  ];
  const CHOICES = {
    hold: ["Hold and send the question", "ok", "Good call. The question goes to Quoll Electrical from your approver's email, and the bill stays held until it's answered."],
    pay: ["Pay as billed", "warn", "Allowed for someone with authority, but they have to record a reason, and it's logged. The agent still can't release the payment itself."],
    part: ["Pay $1,960 now", "warn", "Paying a different amount from the bill without a corrected bill usually starts a dispute. Ask first, then pay what's agreed."]
  };
  let step = 0, choice = null;

  const tick = '<i class="br-ic ok" aria-hidden="true">✓</i>', cross = '<i class="br-ic bad" aria-hidden="true">!</i>';
  const card = (cls, title, src, rows) =>
    `<article class="br-doc ${cls}"><header><b>${title}</b><span>${src}</span></header><dl>${rows.map(([k, v, m]) => `<div${m ? ` class="${m}"` : ""}><dt>${k}</dt><dd>${v}</dd></div>`).join("")}</dl></article>`;
  const docs = () => `<div class="br-docs">
    ${card("d-bill", "Supplier bill", "from the accounts inbox", [["Supplier", "Quoll Electrical"], ["Job", "J2204, Kestrel fit-out"], ["Rate", "$140 an hour"], ["Hours", "22", "hrs"], ["Amount", "$3,080.00"]])}
    ${card("d-quote", "Quote", "from the job folder", [["Supplier", "Quoll Electrical"], ["Job", "J2204, Kestrel fit-out"], ["Rate", "$140 an hour"], ["Hours", "Capped at 16", "hrs"], ["Signed", "3 Sep 2026"]])}
    ${card("d-time", "Timesheet", "from the time app", [["Worker", "Quoll Electrical crew"], ["Job", "J2204, Kestrel fit-out"], ["Days", "8, 9 and 10 Oct"], ["Hours", "14", "hrs"], ["Approved by", "Site lead"]])}
  </div>`;
  const checks = () => `<ol class="br-checks">
    <li>${tick}<span>Same supplier on all three</span></li>
    <li>${tick}<span>Same job, J2204</span></li>
    <li>${tick}<span>Rate matches the quote, $140 an hour</span></li>
    <li class="bad">${cross}<span>Hours billed (22) are over the quote cap (16) and the timesheet (14)</span></li>
  </ol>`;
  const exception = () => `<div class="br-exc" role="note"><b>Held for a person</b>
    <p>22 hours billed. 14 on the timesheet. The quote caps the job at 16.</p>
    <p class="br-diff">Unexplained: 8 hours, $1,120</p>
    <p class="br-fine">A possible discrepancy. Travel, a variation or a missing timesheet could explain it.</p></div>`;
  const decide = () => `<div class="br-decide">
    <div class="br-draft"><span>Drafted for your approver to send</span><p>Hi, your bill for job J2204 shows 22 hours. Our timesheet records 14, and the quote caps the job at 16 hours. Could you send the timesheets for the extra hours, or a corrected bill?</p></div>
    <div class="br-opts" role="group" aria-label="What should happen to this bill?">${Object.entries(CHOICES).map(([k, [t]]) => `<button type="button" data-c="${k}" aria-pressed="${choice === k}">${t}</button>`).join("")}</div>
    <p class="br-fb ${choice ? CHOICES[choice][1] : ""}" aria-live="polite">${choice ? CHOICES[choice][2] : "The agent has done its part. Pick what your approver would do."}</p></div>`;
  const trail = () => {
    const how = choice && choice !== "hold" ? `chose "${CHOICES[choice][0].toLowerCase()}" and recorded a reason` : "held the bill and sent the question";
    const rows = [
      ["Mon 09:12", "Payables agent", "Bill received from Quoll Electrical, $3,080.00", "log"],
      ["Mon 09:12", "Payables agent", "Checked against quote and timesheet: 1 exception, hours", "log"],
      ["Mon 09:12", "Payables agent", "Held: hours over timesheet and quote cap", "held"],
      ["Mon 09:40", "Sam, approver", `Reviewed the evidence and ${how}`, "ok"]
    ];
    if (!choice || choice === "hold") rows.push(
      ["Tue 14:05", "Payables agent", "Corrected bill received: 14 hours, $1,960.00. Checks passed", "log"],
      ["Tue 16:20", "Sam, approver", "Approved for the next pay run", "ok"]);
    return `<table class="br-log"><thead><tr><th>When</th><th>Who</th><th>What happened</th></tr></thead><tbody>${rows.map(([w, who, t, s]) => `<tr class="s-${s}"><td>${w}</td><td>${who}</td><td>${t}</td></tr>`).join("")}</tbody></table>
      <p class="br-pay">You review the discrepancy, instead of hunting through three systems to find it.</p>`;
  };

  const stage = root.querySelector(".br-stage"), cap = root.querySelector(".br-cap"), dots = root.querySelector(".br-dots");
  const back = root.querySelector("[data-a=back]"), next = root.querySelector("[data-a=next]");
  dots.innerHTML = STEPS.map(([t], i) => `<li><button type="button" data-s="${i}" aria-label="Step ${i + 1}: ${t}"><span>${i + 1}</span><em>${t}</em></button></li>`).join("");

  const render = () => {
    root.dataset.step = step;
    const parts = [docs()];
    if (step >= 1 && step < 4) parts.push(checks());
    if (step === 2 || step === 3) parts.push(exception());
    if (step === 4) parts.push(decide());
    if (step === 5) parts.push(trail());
    stage.innerHTML = parts.join("");
    cap.innerHTML = `<b>${step + 1}. ${STEPS[step][0]}</b> ${STEPS[step][1]}`;
    dots.querySelectorAll("button").forEach((b, i) => { b.setAttribute("aria-current", i === step ? "step" : "false"); b.classList.toggle("done", i < step); });
    back.disabled = step === 0;
    next.textContent = step === STEPS.length - 1 ? "Start again" : step === 0 ? "Run the checks" : "Next step";
    stage.querySelectorAll("[data-c]").forEach(b => b.addEventListener("click", () => { choice = b.dataset.c; render(); }));
  };
  next.addEventListener("click", () => { if (step === STEPS.length - 1) { step = 0; choice = null; } else step++; render(); });
  back.addEventListener("click", () => { if (step > 0) step--; render(); });
  dots.addEventListener("click", e => { const b = e.target.closest("[data-s]"); if (b) { step = +b.dataset.s; render(); } });
  root.addEventListener("keydown", e => {
    if (e.target.closest("textarea,input")) return;
    if (e.key === "ArrowRight") { next.click(); e.preventDefault(); }
    if (e.key === "ArrowLeft" && step > 0) { back.click(); e.preventDefault(); }
  });
  root.classList.add("br-on");
  render();
})();
