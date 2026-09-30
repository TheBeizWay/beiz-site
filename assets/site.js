// Beiz site script. Every block is guarded, so each page only runs what it contains.
// No third-party requests on page load: fonts and market data are served from beiz.com.au.
// Live sports and live crypto are fetched only when a visitor opens the Live Data drawer.
(function () {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const esc = t => String(t ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const J = u => fetch(u).then(r => (r.ok ? r.json() : Promise.reject(r.status)));
  const store = {
    get(k) { try { return sessionStorage.getItem(k); } catch (_) { return null; } },
    set(k, v) { try { sessionStorage.setItem(k, v); return true; } catch (_) { return false; } },
    del(k) { try { sessionStorage.removeItem(k); } catch (_) {} }
  };
  const EMAIL = "hello@beiz.com.au";
  // Set to a form endpoint (e.g. a Google Apps Script web app) to receive submissions directly.
  const FORM_ENDPOINT = "";

  $$("[data-yr]").forEach(e => (e.textContent = new Date().getFullYear()));

  // ---------- Mobile menu ----------
  const mb = $("#menuBtn"), mn = $("#mnav");
  if (mb && mn) {
    mb.addEventListener("click", () => {
      const o = !mn.classList.contains("open");
      mn.classList.toggle("open", o);
      mb.setAttribute("aria-expanded", o);
      mb.textContent = o ? "CLOSE" : "MENU";
    });
  }

  // ---------- Contact prefill (works across pages) ----------
  const form = $("#contactForm"), fmsg = $("#formMsg");
  function fill(topic, text) {
    if (!form) return;
    if (topic) [...form.topic.options].forEach(o => { if (o.text === topic) o.selected = true; });
    if (text) form.message.value = text;
  }
  function prefill(topic, text) {
    if (form) {
      fill(topic, text);
      form.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
      setTimeout(() => { form.message.focus(); }, 450);
      return;
    }
    const ok = store.set("beiz_prefill", JSON.stringify({ topic, text }));
    const q = new URLSearchParams();
    if (topic) q.set("topic", topic);
    if (!ok && text) q.set("msg", text.slice(0, 1500));
    location.href = "/contact/" + (q.toString() ? "?" + q : "") + "#form";
  }
  window.beizPrefill = prefill;
  if (form) {
    const q = new URLSearchParams(location.search);
    let saved = null;
    try { saved = JSON.parse(store.get("beiz_prefill") || "null"); } catch (_) {}
    store.del("beiz_prefill");
    fill(q.get("topic") || saved?.topic, q.get("msg") || saved?.text);
    form.addEventListener("submit", async e => {
      e.preventDefault();
      if (form.company_website.value) return;
      if (!form.name.value.trim() || !form.email.value.trim() || !form.email.checkValidity() || !form.message.value.trim()) {
        fmsg.style.color = "var(--warn)";
        fmsg.textContent = "Please add your name, a valid email and a line about the problem.";
        return;
      }
      const data = Object.fromEntries(new FormData(form));
      delete data.company_website;
      if (FORM_ENDPOINT) {
        try {
          const r = await fetch(FORM_ENDPOINT, { method: "POST", headers: { "Content-Type": "text/plain;charset=utf-8" }, body: JSON.stringify(data) });
          if (!r.ok) throw new Error();
          form.reset();
          fmsg.style.color = "var(--accent)";
          fmsg.textContent = "Received. You'll get a written reply within three business days.";
          return;
        } catch (_) {}
      }
      const body = `Name: ${data.name}\nEmail: ${data.email}\nOrganisation: ${data.organisation || "-"}\nArea: ${data.topic}\n\n${data.message}`;
      location.href = `mailto:${EMAIL}?subject=${encodeURIComponent("Enquiry: " + data.topic)}&body=${encodeURIComponent(body)}`;
      fmsg.style.color = "var(--accent)";
      fmsg.textContent = "Opening your email app with the details filled in. Just press send.";
    });
  }
  $$("[data-topic]").forEach(a => a.addEventListener("click", e => {
    if (form) { e.preventDefault(); prefill(a.dataset.topic); }
  }));

  // ---------- Beiz Pulse ticker ----------
  const track = $("#pulse");
  const today = new Date(); today.setHours(0, 0, 0, 0);
  const dleft = Math.round((new Date(2026, 11, 10) - today) / 864e5);
  $$("[data-adm-days]").forEach(e => (e.textContent = dleft > 0 ? dleft + " days" : "now in force"));
  // One purpose only: regulatory countdown + Australian market benchmarks.
  const base = [
    dleft > 0 ? `Privacy Act: automated-decision disclosures start <b>10 Dec 2026</b> · ${dleft} days`
              : `Privacy Act: automated-decision disclosures <b>in force</b> since 10 Dec 2026`
  ];
  const renderTicker = items => {
    if (!track) return;
    const html = items.map(i => `<span>${i}</span>`).join("");
    track.innerHTML = reduce ? html : html + html;
  };
  renderTicker(base);

  // ---------- Market data (same-origin JSON, refreshed by a scheduled job) ----------
  const data = { markets: [], cricket: [], nrl: [], afl: [], football: [] };
  const fmtMk = i => ({
    n: i.label, a: i.short || i.label, c: i.chg, g: i.group,
    v: i.cur === "AUD" ? "A$" + Math.round(i.price).toLocaleString("en-AU")
      : i.sym && i.sym.includes("=X") ? Number(i.price).toFixed(4)
      : Number(i.price).toLocaleString("en-AU", { maximumFractionDigits: 1 })
  });
  const marketsReady = J("/data/markets.json?" + Math.floor(Date.now() / 6e5)).then(d => {
    const asx = (d.items || []).map(i => fmtMk({ ...i, group: "ASX & AUD · delayed" }));
    const cr = (d.crypto || []).map(i => fmtMk({ ...i, cur: "AUD", group: "Crypto · 24h" }));
    data.markets = [...asx, ...cr];
    const mk = data.markets.filter(m => m.g.startsWith("ASX"))
      .map(m => `${esc(m.a)} <b>${esc(m.v)}</b>${m.c == null ? "" : ` <i class="${m.c >= 0 ? "up" : "dn"}">${m.c >= 0 ? "▲" : "▼"}${Math.abs(m.c).toFixed(1)}%</i>`}`)
      .join(" &nbsp;·&nbsp; ");
    if (mk) {
      renderTicker([base[0], mk + ' <i class="note">delayed · indicative only</i>']);
    }
  }).catch(() => {});

  // ---------- Live data engine (drawer + /live/ page) ----------
  const ESPN = "https://site.api.espn.com/apis/site/v2/sports/";
  const when = d => new Date(d).toLocaleString("en-AU", { weekday: "short", day: "numeric", month: "short", hour: "numeric", minute: "2-digit" });
  const fromEspn = (ev, fav) => {
    const c = ev.competitions[0], st = ev.status.type.state;
    const t = c.competitors.slice().sort(a => (a.homeAway === "home" ? -1 : 1))
      .map(x => ({ n: x.team.shortDisplayName || x.team.displayName, a: x.team.abbreviation, s: x.score?.displayValue ?? x.score ?? "", w: x.winner }));
    return { t, st, det: st === "pre" ? when(ev.date) : ev.status.type.shortDetail, date: ev.date, fav: !!(fav && t.some(x => fav.test(x.n))) };
  };
  const card = m => `<div class="sm${m.fav ? " fav" : ""}">${m.t.map(x => `<div class="row${x.w ? " win" : ""}"><span>${esc(x.n)}</span><span>${m.st === "pre" ? "" : esc(x.s)}</span></div>`).join("")}<div class="st">${m.st === "in" ? '<span class="live">LIVE</span>' : ""}${esc(m.lg ? m.lg + " · " : "")}${esc(m.det)}</div></div>`;
  let loaded = false, loading = null;
  const views = [];
  const redraw = () => views.forEach(v => v());
  const loadLive = () => {
    if (loading) return loading;
    const jobs = [
      J(ESPN + "australian-football/afl/scoreboard").then(d => { data.afl = (d.events || []).map(e => fromEspn(e)); }),
      J(ESPN + "rugby-league/3/scoreboard").then(d => { data.nrl = (d.events || []).map(e => fromEspn(e)); }),
      Promise.allSettled(
        [["eng.1", "EPL"], ["uefa.champions", "Champions League"], ["aus.1", "A-League Men"], ["aus.w.1", "A-League Women"], ["fifa.friendly", "Socceroos"], ["fifa.friendly.w", "Matildas"]]
          .map(([k, lg]) => J(ESPN + "soccer/" + k + "/scoreboard").then(d => (d.events || []).map(x => ({ ...fromEspn(x, /Liverpool/i), lg }))))
          .concat(J(ESPN + "soccer/eng.1/teams/364/schedule").then(d => {
            const p = (d.events || []).filter(e => e.competitions?.[0]?.status?.type?.state === "post").sort((x, y) => new Date(x.date) - new Date(y.date));
            const e = p[p.length - 1];
            if (!e || Date.now() - new Date(e.date) > 10 * 864e5) return [];
            const m = fromEspn({ ...e, status: e.competitions[0].status }, /Liverpool/i);
            return [{ ...m, st: "post", fav: true, lg: "EPL · Liverpool last result", det: "FT · " + new Date(e.date).toLocaleDateString("en-AU", { day: "numeric", month: "short" }) }];
          }))
      ).then(rs => {
        const all = rs.flatMap(r => (r.status === "fulfilled" ? r.value : []))
          .filter(m => !["Socceroos", "Matildas"].includes(m.lg) || m.t.some(x => /Australia/i.test(x.n)));
        const rank = m => (m.fav ? 0 : 10) + (m.st === "in" ? 0 : m.st === "post" ? 1 : 2);
        data.football = all.sort((x, y) => rank(x) - rank(y) || (x.st === "post" ? new Date(y.date) - new Date(x.date) : new Date(x.date) - new Date(y.date))).slice(0, 18);
      }),
      J(ESPN + "cricket/scorepanel").then(d => {
        const big = /Test|ODI|T20I|Big Bash|Sheffield|Marsh|WBBL|World Cup|IPL/i, all = [];
        (d.scores || []).forEach(g => (g.events || []).forEach(ev => {
          const c = ev.competitions[0];
          const t = c.competitors.map(x => ({ n: x.team?.shortDisplayName || x.team?.displayName || x.team?.abbreviation, a: x.team?.abbreviation, s: x.score || "", w: x.winner }));
          const lg = g.leagues?.[0]?.name || "", cls = c.class?.generalClassCard || "";
          const aus = t.some(x => /^AUS|^AU-/.test(x.a || "")) || /Australia|Big Bash|Sheffield|Marsh|WBBL/i.test(lg);
          all.push({ t, st: ev.status?.type?.state, det: ev.status?.type?.shortDetail || ev.status?.summary || "", lg: (cls ? cls + " · " : "") + lg, rk: (aus ? 0 : 10) + (big.test(cls + " " + lg) ? 0 : 5) + (ev.status?.type?.state === "in" ? 0 : 2) });
        }));
        data.cricket = all.sort((a, b) => a.rk - b.rk).slice(0, 8);
      }),
      J("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=aud&include_24hr_change=true").then(d => {
        const live = [["bitcoin", "Bitcoin", "BTC"], ["ethereum", "Ethereum", "ETH"], ["solana", "Solana", "SOL"]]
          .filter(([id]) => d[id]).map(([id, n, a]) => fmtMk({ label: n, short: a, price: d[id].aud, chg: d[id].aud_24h_change, cur: "AUD", group: "Crypto · 24h · live" }));
        if (live.length) data.markets = [...data.markets.filter(m => !m.g.startsWith("Crypto")), ...live];
      })
    ];
    jobs.forEach(j => j.then(redraw, redraw));
    loading = Promise.allSettled(jobs).then(() => { loaded = true; redraw(); });
    return loading;
  };
  const sportsList = (k) => {
    const rows = data[k];
    if (!rows.length) return `<p class="st muted">${loaded ? "Nothing on right now." : "Loading…"}</p>`;
    const grp = { in: "Live", post: "Results", pre: "Coming up" }; let g = "";
    return rows.slice().sort((a, b) => ({ in: 0, post: 1, pre: 2 }[a.st] ?? 3) - ({ in: 0, post: 1, pre: 2 }[b.st] ?? 3))
      .map(m => { const h = grp[m.st] !== g ? `<div class="grp">${grp[m.st] || ""}</div>` : ""; g = grp[m.st]; return h + card(m); }).join("");
  };
  const marketsList = () => {
    if (!data.markets.length) return '<p class="st muted">Loading…</p>';
    let g = "";
    return data.markets.map(m => {
      const h = m.g !== g ? `<div class="grp">${esc(m.g)}</div>` : ""; g = m.g;
      const c = m.c == null ? "" : `<span class="${m.c >= 0 ? "up" : "dn"}">${m.c >= 0 ? "▲" : "▼"}${Math.abs(m.c).toFixed(2)}%</span>`;
      return h + `<div class="sm"><div class="row"><span>${esc(m.n)}</span><span>${esc(m.v)} ${c}</span></div></div>`;
    }).join("");
  };
  const mountTabs = (nav, list, tabs, start) => {
    let cur = start;
    const draw = () => {
      nav.innerHTML = tabs.map(([k, l]) => `<button role="tab" type="button" aria-selected="${k === cur}" data-k="${k}">${l}</button>`).join("");
      list.innerHTML = cur === "markets" ? marketsList() : sportsList(cur);
    };
    nav.addEventListener("click", e => { const k = e.target.closest("[data-k]")?.dataset.k; if (k) { cur = k; draw(); } });
    views.push(draw); draw();
  };
  const TABS = [["markets", "Markets"], ["cricket", "Cricket"], ["nrl", "NRL"], ["afl", "AFL"], ["football", "Football"]];
  marketsReady.then(redraw);

  const sb = $("#sb"), tab = $("#sbTab");
  if (sb && tab) {
    mountTabs($("#sbNav"), $("#sbList"), TABS, "markets");
    const set = o => {
      sb.classList.toggle("open", o); sb.setAttribute("aria-hidden", !o); tab.setAttribute("aria-expanded", o);
      if (o) loadLive();
    };
    tab.addEventListener("click", () => set(!sb.classList.contains("open")));
    $("#sbClose").addEventListener("click", () => set(false));
    document.addEventListener("keydown", e => { if (e.key === "Escape") set(false); });
  }
  // Homepage teaser tiles (same-origin data only; no third-party calls)
  const mkHome = $("#labMkHome");
  if (mkHome) {
    marketsReady.then(() => {
      const pick = data.markets.filter(m => ["ASX 200", "AUD/USD", "Bitcoin", "Ethereum"].includes(m.n));
      mkHome.innerHTML = pick.map(m => `<div class="mtile"><small>${esc(m.n)}</small><b>${esc(m.v)}</b>${m.c == null ? "" : `<span class="${m.c >= 0 ? "up" : "dn"}">${m.c >= 0 ? "▲" : "▼"} ${Math.abs(m.c).toFixed(2)}%</span>`}</div>`).join("");
    });
  }
  // Full page: /live/
  const labMk = $("#labMk");
  if (labMk) {
    const tiles = () => {
      if (!data.markets.length) { labMk.innerHTML = '<p class="muted">Loading…</p>'; return; }
      labMk.innerHTML = data.markets.map(m => `<div class="mtile"><small>${esc(m.n)}</small><b>${esc(m.v)}</b>${m.c == null ? "" : `<span class="${m.c >= 0 ? "up" : "dn"}">${m.c >= 0 ? "▲" : "▼"} ${Math.abs(m.c).toFixed(2)}%</span>`}<span class="muted" style="display:block;margin-top:2px;font-size:.72rem">${esc(m.g)}</span></div>`).join("");
    };
    views.push(tiles); tiles();
    mountTabs($("#labNav"), $("#labList"), TABS.slice(1).concat([]), "cricket");
    loadLive();
  }

  // ---------- Dropdown menus ----------
  $$(".dd>button").forEach(b => b.addEventListener("click", e => {
    const d = b.parentElement, o = !d.classList.contains("open");
    $$(".dd.open").forEach(x => { x.classList.remove("open"); x.firstElementChild.setAttribute("aria-expanded", "false"); });
    d.classList.toggle("open", o); b.setAttribute("aria-expanded", o);
    e.stopPropagation();
  }));
  document.addEventListener("click", e => { if (!e.target.closest(".dd")) $$(".dd.open").forEach(x => { x.classList.remove("open"); x.firstElementChild.setAttribute("aria-expanded", "false"); }); });
  document.addEventListener("keydown", e => { if (e.key === "Escape") $$(".dd.open").forEach(x => x.classList.remove("open")); });

  // ---------- Example agent control log ----------
  const log = $("#log");
  if (log) {
    const lines = [
      ["02:00", "ok", "Agent started · accounts payable run"],
      ["02:03", "ok", "418 invoices matched to purchase orders"],
      ["02:07", "flag", "Supplier bank details changed · payment held", "Why it held: payment-redirection scams are among the costliest frauds hitting Australian businesses. The agent never pays new bank details until a person verifies them on a number already on file."],
      ["02:09", "flag", "$48,200 exceeds delegation · routed to CFO", "Why it routed: the agent works inside the same delegation limits as your staff. Above the limit it prepares the payment and the evidence, then stops and waits."],
      ["02:14", "ok", "Segregation of duties check passed"],
      ["02:18", "ok", "Every decision written to audit trail"],
      ["06:00", "ok", "Board dashboard refreshed · 13-week cash forecast"]
    ];
    lines.forEach(([t, c, m, why], i) => {
      const li = document.createElement("li");
      li.style.animationDelay = reduce ? "0s" : i * 0.7 + "s";
      li.innerHTML = `<time>${t}</time><span class="${c}">${c === "ok" ? "✓" : "!"}</span><span>${why ? `<button type="button" class="why" aria-expanded="false">${m} <u>why?</u></button><small class="whytxt" hidden>${why}</small>` : m}</span>`;
      log.appendChild(li);
    });
    const end = document.createElement("li");
    end.style.animationDelay = reduce ? "0s" : lines.length * 0.7 + "s";
    end.innerHTML = '<time>06:01</time><span class="ok">&gt;</span><span>Awaiting human approval <span class="cursor" aria-hidden="true"></span></span>';
    log.appendChild(end);
    log.addEventListener("click", e => {
      const b = e.target.closest(".why"); if (!b) return;
      const t = b.nextElementSibling, o = t.hidden; t.hidden = !o; b.setAttribute("aria-expanded", o);
    });
  }

  // ---------- Privacy Act automated-decision check (client-side only) ----------
  const ol = $("#chkQ"), res = $("#chkRes");
  if (ol && res) {
    const Q = [
      ["cov", "Are you a health, allied health or NDIS provider, trade in personal information, or turn over more than $3 million a year?", "Health service providers, including many allied health and NDIS providers, are generally covered regardless of turnover."],
      ["dec", "Does any software or AI make or recommend decisions about individual people?", "e.g. credit terms, pricing, bookings, screening applicants, fraud flags, rosters"],
      ["pi", "Does it use personal information to do that?", ""],
      ["sig", "Could the outcome significantly affect someone: their money, access to a service, or a job?", ""],
      ["hum", "Does a person genuinely review each outcome before it takes effect?", ""],
      ["pol", "Does your privacy policy already explain any automated decisions?", ""],
      ["reg", "Do you have a current list of every AI tool your team uses, including free ones?", ""],
      ["dat", "Do you know whether those tools store or train on your data?", ""],
      ["own", "Is one named person accountable for how AI is used in the business?", ""]
    ];
    const A = {};
    ol.innerHTML = Q.map(([k, q, h]) => `<li><div>${q}${h ? `<small>${h}</small>` : ""}</div><div class="opts" role="group" aria-label="${esc(q)}">${["Yes", "No", "Not sure"].map(o => `<button type="button" data-k="${k}" data-v="${o}" aria-pressed="false">${o}</button>`).join("")}</div></li>`).join("");
    const fix = { pol: "Update your privacy policy to describe automated decisions", reg: "Build a register of every AI tool in use", dat: "Check each tool's data storage and training terms", own: "Name one person accountable for AI use", hum: "Add a genuine human review step where outcomes matter" };
    const drawChk = () => {
      const n = Object.keys(A).length;
      if (n < Q.length) { res.innerHTML = `<p class="muted">${Q.length - n} question${Q.length - n > 1 ? "s" : ""} to go.</p>`; return; }
      const y = k => A[k] === "Yes", u = k => A[k] !== "No";
      const exposed = y("dec") && u("pi") && u("sig"), auto = !y("hum");
      const gaps = ["pol", "reg", "dat", "own"].filter(k => !y(k)); if (exposed && auto) gaps.unshift("hum");
      let lvl, cls, h, t;
      if (exposed && y("cov")) { lvl = "Likely in scope"; cls = "hi"; h = "You probably need to act before 10 December 2026."; t = "You appear to be covered by the Privacy Act and using automated decisions that affect people."; }
      else if (exposed && A.cov === "Not sure") { lvl = "Worth checking"; cls = "md"; h = "Confirm whether the Privacy Act covers you."; t = "Your tools look like the kind the new rule targets. Coverage is the open question."; }
      else if (exposed) { lvl = "Probably exempt, still exposed"; cls = "md"; h = "The rule may not bind you yet, but your customers' trust does."; t = "Small businesses are generally exempt today. The government has flagged further reform, and larger clients increasingly ask suppliers about AI use."; }
      else if (A.dec === "Not sure") { lvl = "Worth checking"; cls = "md"; h = "Find out what your software actually decides."; t = "Many businesses use automated decisions without realising it, inside booking, finance and HR tools."; }
      else { lvl = "Low exposure today"; cls = "lo"; h = "Good position. Keep it that way."; t = "Nothing here suggests automated decisions about people, but basic AI hygiene still pays off."; }
      res.innerHTML = `<span class="lvl ${cls}">${lvl}</span><h3>${h}</h3><p class="muted" style="font-size:.9rem">${t}</p>${gaps.length ? `<ul>${gaps.map(g => `<li>${fix[g]}</li>`).join("")}</ul>` : '<p style="margin:12px 0">No obvious gaps. Nice.</p>'}<button class="btn primary" type="button" id="chkSend">Get this as a written action list</button>`;
      $("#chkSend").onclick = () => {
        const sum = Q.map(([k, q]) => `- ${q} ${A[k]}`).join("\n");
        prefill("Privacy Act automated-decision check", `My check result: ${lvl}\n\n${sum}\n\nPlease send me a written action list.`);
      };
    };
    ol.addEventListener("click", e => {
      const b = e.target.closest("button[data-k]"); if (!b) return;
      A[b.dataset.k] = b.dataset.v;
      b.parentElement.querySelectorAll("button").forEach(x => x.setAttribute("aria-pressed", x === b));
      drawChk();
    });
  }

  // ---------- Guided assistant: rule-based, no AI, nothing stored ----------
  const bot = $("#bot"), msgs = $("#msgs"), opts = $("#opts");
  if (bot && msgs && opts) {
    const openers = $$("[data-open-bot]");
    const flow = {
      start: { say: ["Hi. I'm a guided assistant, not an AI. Three quick questions and I'll point you to the right starting place.", "What's on your mind?"],
        opts: [["Using AI safely", "ai"], ["Small business admin", "sb"], ["Automating a finance process", "auto"], ["Dashboards & reporting", "dash"], ["A financial model or business case", "model"], ["A tech project that's stuck", "pm"], ["Not sure yet", "unsure"]] },
      ai: { topic: "AI readiness & governance", say: ["Good place to start. Which is closest?"],
        opts: [["Staff already use ChatGPT or Copilot", "ai1"], ["The board is asking about AI risk", "ai2"], ["The new Privacy Act rules", "ai4"], ["We want to build our first agent", "ai3"]] },
      ai1: { topic: "AI Readiness Sprint", say: ["That's the most common one. Free AI tools often mean business data leaving without anyone noticing.", "The AI Readiness Sprint finds what's in use, maps the risk and sets simple rules people will actually follow."], next: "size" },
      ai2: { topic: "AI Readiness Sprint", say: ["Boards want a clear view, not a technical lecture.", "We'd start with the AI Readiness Sprint: a register, a risk and controls map, and a one-page board paper."], next: "size" },
      ai3: { topic: "AI Readiness Sprint", say: ["The safest first agent does one well-defined job with a human approving the output.", "We'd scope it in the Sprint and build a working prototype on your own data."], next: "size" },
      ai4: { topic: "Privacy Act automated-decision check", say: ["From 10 December 2026, businesses covered by the Privacy Act must explain automated decisions in their privacy policy.", "The free 2-minute check on our site is a good first step. We can then map what your tools actually decide."], next: "size" },
      auto: { topic: "Automation & AI agents", say: ["Which process hurts most?"],
        opts: [["Month-end close", "a1"], ["Invoices & payments", "a2"], ["Reporting packs", "a3"], ["Chasing documents", "a4"]] },
      a1: { say: ["Month-end usually loses days to copying and checking. We automate the pulls, reconciliations and checks, and leave the judgement calls with your team."], next: "size" },
      a2: { say: ["We match invoices to POs, flag changed bank details and duplicate payments, and route anything over your delegation limit for approval. Nothing gets paid without a human."], next: "size" },
      a3: { say: ["We connect your ledger to a live dashboard, so the pack builds itself and your time goes on the commentary."], next: "size" },
      a4: { say: ["An agent can chase, collect and file documents on a schedule, with a clear log of who sent what and when."], next: "size" },
      sb: { topic: "Something else", say: ["Which one sounds most like your week?"],
        opts: [["Chasing unpaid invoices", "sb1"], ["Jobs not invoiced on time", "sb2"], ["No idea where cash is", "sb3"], ["Xero is a mess", "sb4"]] },
      sb1: { say: ["Automatic reminders with a pay-now link usually fix most of this. You approve the wording once and it runs itself."], next: "size" },
      sb2: { say: ["We connect your quotes or job system to your invoicing, so a finished job becomes an invoice the same day."], next: "size" },
      sb3: { say: ["A short weekly cash email (what's in the bank, what's owed, what's due) is one of the quickest wins there is."], next: "size" },
      sb4: { say: ["A Xero health check cleans up bank rules and duplicates and gets reconciliation back on track, then we keep it that way."], next: "size" },
      dash: { topic: "Dashboards & analytics", say: ["What do you need to see that you can't see now?"],
        opts: [["Cash position & forecast", "d1"], ["Job or project profitability", "d2"], ["Board or investor KPIs", "d3"]] },
      d1: { say: ["A 13-week cash forecast that refreshes itself is one of the most useful things a business can have. We build it from your actual data."], next: "size" },
      d2: { say: ["We pull costs, time and revenue together so you can see margin by job while there's still time to fix it."], next: "size" },
      d3: { say: ["We design dashboards the way directors and investors read them: a few measures, clear trends, flagged exceptions."], next: "size" },
      model: { topic: "Financial modelling", say: ["What's the model for?"],
        opts: [["Business case or investment", "m1"], ["Pricing or quoting", "m2"], ["Runway & scenarios", "m3"]] },
      m1: { say: ["We build business cases that stand up to a lender, board or auditor: clear assumptions, scenarios and sensitivity, fully documented."], next: "size" },
      m2: { say: ["We model your real costs from past jobs so quotes protect your margin, with risk-adjusted contingency."], next: "size" },
      m3: { say: ["Driver-based forecasts over 6, 12 and 24 months, so you can see what a new hire or a bigger ad budget does to your runway before you commit."], next: "size" },
      pm: { topic: "Tech project delivery", say: ["Stalled projects usually have the same three problems: fuzzy scope, no one owning the vendor, and nobody reporting honestly.", "We take over delivery, reset the plan in writing and get it landing."], next: "size" },
      unsure: { topic: "Something else", say: ["That's fine. Most people start with a vague itch. Describe the problem in plain words and we'll suggest where to begin."], next: "size" },
      size: { say: ["Roughly how big is the organisation?"], opts: [["Just me", "s"], ["2–20 people", "s"], ["20–200 people", "s"], ["200+ people", "s"], ["Not-for-profit", "s"]] },
      s: { say: ["Thanks. Last step: send us a short written brief. I'll fill in what you've told me so far, and you add the details."], opts: [["Write my brief", "go"], ["Start again", "start"]] }
    };
    let path = [], topic = "Something else";
    const add = (text, who) => { const d = document.createElement("div"); d.className = "m " + who; d.textContent = text; msgs.appendChild(d); msgs.scrollTop = msgs.scrollHeight; };
    const closeBot = () => { bot.classList.remove("open"); openers.forEach(x => x.setAttribute("aria-expanded", "false")); };
    const renderOpts = listx => {
      opts.innerHTML = "";
      listx.forEach(([label, key]) => {
        const b = document.createElement("button"); b.type = "button"; b.textContent = label;
        b.onclick = () => { add(label, "u"); if (key !== "go" && key !== "start") path.push(label); step(key); };
        opts.appendChild(b);
      });
    };
    function step(key) {
      if (key === "go") { closeBot(); prefill(topic, path.join(" → ") + "\n\n"); return; }
      if (key === "start") { path = []; topic = "Something else"; msgs.innerHTML = ""; }
      const n = flow[key]; if (n.topic) topic = n.topic;
      let says = [...n.say], o = n.opts;
      if (n.next) { const nx = flow[n.next]; says = says.concat(nx.say); o = nx.opts; }
      opts.innerHTML = "";
      says.forEach((t, i) => setTimeout(() => add(t, "b"), reduce ? 0 : i * 350));
      setTimeout(() => renderOpts(o || []), reduce ? 0 : says.length * 350);
    }
    openers.forEach(o => o.addEventListener("click", () => {
      const open = !bot.classList.contains("open");
      bot.classList.toggle("open", open);
      openers.forEach(x => x.setAttribute("aria-expanded", String(open)));
      if (open && !msgs.children.length) step("start");
    }));
    bot.querySelector(".x").onclick = closeBot;
    document.addEventListener("keydown", e => { if (e.key === "Escape" && bot.classList.contains("open")) closeBot(); });
  }
})();
