/* Beiz "Ledger" site script: phone menu and contact form. Nothing is tracked or stored. */
(() => {
  const $ = s => document.querySelector(s);
  document.querySelectorAll("[data-yr]").forEach(e => (e.textContent = new Date().getFullYear()));

  const top = $(".top"), mb = $(".menu");
  if (top && mb) {
    mb.addEventListener("click", () => {
      const o = !top.classList.contains("open");
      top.classList.toggle("open", o);
      mb.setAttribute("aria-expanded", o);
      mb.textContent = o ? "Close" : "Menu";
    });
    document.addEventListener("keydown", e => {
      if (e.key === "Escape" && top.classList.contains("open")) { mb.click(); mb.focus(); }
    });
  }

  /* ---- browse-and-reveal layer ---- */
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const top0 = $(".top");
  const setMegaTop = () => { if (top0) document.documentElement.style.setProperty("--megatop", Math.max(0, top0.getBoundingClientRect().bottom) + "px"); };
  setMegaTop(); addEventListener("scroll", setMegaTop, { passive: true }); addEventListener("resize", setMegaTop);
  const bar = document.createElement("div"); bar.className = "progress"; bar.setAttribute("aria-hidden", "true"); document.body.appendChild(bar);
  const prog = () => { const h = document.documentElement.scrollHeight - innerHeight; bar.style.transform = `scaleX(${h > 0 ? Math.min(1, scrollY / h) : 0})`; };
  prog(); addEventListener("scroll", prog, { passive: true });
  if (!reduce && "IntersectionObserver" in window) {
    document.documentElement.classList.add("js-anim");
    const targets = [...document.querySelectorAll(".sec .body>*, .reveal, .led tbody tr, .row")];
    const io = new IntersectionObserver(es => es.forEach(en => {
      if (!en.isIntersecting) return;
      const el = en.target, sib = el.parentElement ? [...el.parentElement.children].indexOf(el) : 0;
      el.style.transitionDelay = Math.min(sib, 6) * 60 + "ms";
      el.classList.add("in"); io.unobserve(el);
    }), { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    targets.forEach(t => io.observe(t));
    /* bills panel: rows post in one by one, counts tick up, status rows flash */
    const rowsB = [...document.querySelectorAll(".hero .book tbody tr")];
    rowsB.forEach((tr, i) => setTimeout(() => {
      tr.classList.add("in");
      const n = tr.querySelector("td.n"); if (n) {
        const end = parseInt(n.textContent, 10) || 0, t0 = performance.now(), dur = 700;
        const step = t => { const k = Math.min(1, (t - t0) / dur); n.textContent = Math.round(end * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(step); };
        n.textContent = "0"; requestAnimationFrame(step);
      }
      const d = tr.querySelector(".dot:not(.none)");
      if (d) { d.classList.add("pulse"); tr.classList.add("flash", d.classList.contains("ok") ? "okf" : d.classList.contains("stop") ? "stopf" : "heldf"); setTimeout(() => tr.classList.remove("flash"), 900); }
    }, 250 + i * 230));
  }

  /* ---- interactive bills panel ---- */
  const book = $(".book");
  if (book) {
    const btns = [...book.querySelectorAll(".rowbtn")];
    btns.forEach(b => b.addEventListener("click", () => {
      btns.forEach(x => {
        const on = x === b;
        x.setAttribute("aria-expanded", on);
        const d = document.getElementById("log-" + x.dataset.log);
        if (d) { d.hidden = !on; if (on) { const n = d.querySelector(".dnote"); if (n) n.textContent = ""; } }
      });
    }));
    book.querySelectorAll("[data-demo]").forEach(b => b.addEventListener("click", () => {
      const n = b.closest(".drawer").querySelector(".dnote");
      n.textContent = "\u201C" + b.textContent + "\u201D chosen. " + book.dataset.demoNote;
    }));
  }

  /* ---- plain / technical view ---- */
  const sw = $(".viewsw");
  if (sw) {
    const set = v => {
      sw.querySelectorAll("button").forEach(b => b.setAttribute("aria-pressed", b.dataset.view === v));
      $(".vplain").hidden = v !== "plain"; $(".vtech").hidden = v !== "tech"; $(".vplain").classList.add("in"); $(".vtech").classList.add("in");
    };
    let saved = null; try { saved = localStorage.getItem("beizView"); } catch (_) {}
    if (saved === "tech" || location.hash === "#hood-tech") set("tech");
    if (location.hash === "#hood-tech") { const h = document.getElementById("hood"); if (h) h.scrollIntoView(); }
    sw.addEventListener("click", e => {
      const b = e.target.closest("button[data-view]"); if (!b) return;
      set(b.dataset.view); try { localStorage.setItem("beizView", b.dataset.view); } catch (_) {}
    });
  }

  /* ---- command palette: Ctrl/Cmd + K ---- */
  const ITEMS = [
    ["Home", "/"], ["Services", "/services/"], ["How it works", "/how-we-work/"],
    ["Rules first, AI for the exceptions", "/how-we-work/", "How it works"],
    ["Decision log: the five fields", "/how-we-work/#log", "How it works"],
    ["Prices", "/prices/"], ["Run the free bill check", "/bill-check/"],
    ["Under the hood: technical view", "/#hood-tech", "Home"],
    ["About Beiz", "/about/"], ["Book a 20-minute call", "/contact/?topic=Discovery%20call"],
    ["Write to us", "/contact/"], ["Email hello@beiz.com.au", "mailto:hello@beiz.com.au"], ["Privacy policy", "/privacy/"]
  ];
  const mac = /Mac|iPhone|iPad/.test(navigator.platform || navigator.userAgent);
  document.querySelectorAll("[data-pal]").forEach(b => { if (mac) b.textContent = "Jump to (\u2318K)"; });
  let pal = null, sel = 0;
  function render(q) {
    const ul = pal.querySelector("ul"); q = q.trim().toLowerCase();
    const hits = ITEMS.filter(i => !q || (i[0] + " " + (i[2] || "")).toLowerCase().includes(q));
    sel = 0;
    ul.innerHTML = hits.map((i, n) => `<li role="option"><a href="${i[1]}" aria-selected="${n === 0}">${i[0]}${i[2] ? `<small>${i[2]}</small>` : ""}</a></li>`).join("") || '<li><span style="display:block;padding:10px 18px;color:var(--muted)">No match</span></li>';
  }
  function openPal() {
    if (!pal) {
      pal = document.createElement("dialog"); pal.className = "pal"; pal.setAttribute("aria-label", "Jump to a page");
      pal.innerHTML = '<input type="text" placeholder="Jump to..." aria-label="Search pages" autocomplete="off"><ul role="listbox"></ul><p class="phint">Arrow keys to move, Enter to open, Esc to close.</p>';
      document.body.appendChild(pal);
      const inp = pal.querySelector("input");
      inp.addEventListener("input", () => render(inp.value));
      inp.addEventListener("keydown", e => {
        const links = [...pal.querySelectorAll("li a")];
        if (e.key === "ArrowDown" || e.key === "ArrowUp") {
          e.preventDefault(); if (!links.length) return;
          sel = (sel + (e.key === "ArrowDown" ? 1 : -1) + links.length) % links.length;
          links.forEach((a, n) => a.setAttribute("aria-selected", n === sel)); links[sel].scrollIntoView({ block: "nearest" });
        } else if (e.key === "Enter" && links[sel]) { e.preventDefault(); location.href = links[sel].getAttribute("href"); pal.close(); }
      });
      pal.addEventListener("click", e => { if (e.target === pal) pal.close(); });
    }
    const inp = pal.querySelector("input"); inp.value = ""; render("");
    if (!pal.open) pal.showModal(); inp.focus();
  }
  document.addEventListener("keydown", e => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") { e.preventDefault(); openPal(); }
  });
  document.querySelectorAll("[data-pal]").forEach(b => b.addEventListener("click", openPal));

  const EMAIL = "hello@beiz.com.au";
  const FORM_ENDPOINT = "https://script.google.com/macros/s/AKfycbw3iLtpS-Pubb6fLiWK2A8TgFGi9Joq0u-c7UyZqBO2-ciPcQbgdxmygnsBMKWXjm8FJg/exec";
  const form = $("#contactForm"), msg = $("#formMsg");
  if (!form) return;
  const q = new URLSearchParams(location.search);
  if (q.get("topic")) [...form.topic.options].forEach(o => { if (o.text === q.get("topic")) o.selected = true; });
  if (q.get("msg")) form.message.value = q.get("msg").slice(0, 1500);

  form.addEventListener("submit", async e => {
    e.preventDefault();
    if (form.company_website.value) return;
    if (!form.name.value.trim() || !form.email.value.trim() || !form.email.checkValidity() || !form.message.value.trim()) {
      msg.style.color = "var(--stop)";
      msg.textContent = "Please add your name, a valid email and a line about the problem.";
      return;
    }
    const data = Object.fromEntries(new FormData(form));
    delete data.company_website;
    data.page = location.pathname;
    msg.style.color = "var(--muted)";
    msg.textContent = "Sending...";
    try {
      const r = await fetch(FORM_ENDPOINT, { method: "POST", headers: { "Content-Type": "text/plain;charset=utf-8" }, body: JSON.stringify(data) });
      const res = r.ok ? await r.json().catch(() => ({})) : {};
      if (!res.ok) throw new Error();
      const thx = document.createElement("div");
      thx.className = "thx"; thx.tabIndex = -1;
      thx.innerHTML = `<h3>Received. Here's what happens next.</h3>
        <p>You'll get a written reply by the next business day. If a call makes sense, it's 20 minutes, early morning or after 5pm.</p>
        <p>To make that reply useful, think about three things:</p>
        <ol><li>What the problem costs you now, in hours a week or dollars.</li><li>Which systems hold the records: your accounting software, job software, spreadsheets.</li><li>Who would approve the work, and whether there's a date it has to be done by.</li></ol>
        <p class="fine">You can reply to our email with the answers. Please don't send passwords or bank details.</p>`;
      form.replaceWith(thx); msg.textContent = ""; thx.focus();
    } catch (_) {
      const body = `Name: ${data.name}\nEmail: ${data.email}\nOrganisation: ${data.organisation || "-"}\nArea: ${data.topic}\n\n${data.message}`;
      location.href = `mailto:${EMAIL}?subject=${encodeURIComponent("Enquiry: " + data.topic)}&body=${encodeURIComponent(body)}`;
      msg.style.color = "var(--ink)";
      msg.textContent = "Opening your email app with the details filled in. Just press send.";
    }
  });
})();
