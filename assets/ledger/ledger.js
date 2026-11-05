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
