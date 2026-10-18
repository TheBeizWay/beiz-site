/* "What we do" problem-led panel. Tabs work wherever a .wwd appears; on desktop the header link opens it as a dropdown
   (hover, click, keyboard; Escape or a click outside closes it). On phones the link goes to /services/, which shows the same panel. */
(() => {

  const initTabs = root => {
    const tabs = [...root.querySelectorAll('[role="tab"]')], panes = [...root.querySelectorAll('[role="tabpanel"]')];
    const show = (i, focus) => {
      tabs.forEach((t, j) => { t.setAttribute("aria-selected", j === i); t.tabIndex = j === i ? 0 : -1; });
      panes.forEach((p, j) => { p.hidden = j !== i; });
      if (focus) tabs[i].focus();
    };
    tabs.forEach((t, i) => {
      t.addEventListener("click", () => show(i));
      t.addEventListener("mouseenter", () => { if (root.closest(".wwd-pop")) show(i); });
      t.addEventListener("keydown", e => {
        const k = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[e.key];
        if (k) { e.preventDefault(); show((i + k + tabs.length) % tabs.length, true); }
        if (e.key === "Home") { e.preventDefault(); show(0, true); }
        if (e.key === "End") { e.preventDefault(); show(tabs.length - 1, true); }
      });
    });
    root.querySelectorAll(".wwd-sw").forEach(sw => sw.addEventListener("click", e => {
      const b = e.target.closest("button"); if (!b) return;
      const pane = sw.closest('[role="tabpanel"]');
      sw.querySelectorAll("button").forEach(x => x.setAttribute("aria-pressed", x === b));
      pane.querySelectorAll(".wwd-flow").forEach(f => { f.hidden = f.dataset.v !== b.dataset.v; });
    }));
    show(0);
  };
  document.querySelectorAll(".wwd").forEach(initTabs);

  const mm = document.querySelector(".wwd-mm");
  if (!mm || innerWidth < 1000) return;
  const link = mm.querySelector("[data-wwd-open]"), pop = mm.querySelector(".wwd-pop");
  mm.classList.add("wwd-on");
  let tOpen = 0, tClose = 0;
  const open = () => { clearTimeout(tClose); pop.hidden = false; link.setAttribute("aria-expanded", "true"); };
  const close = (focusLink) => { clearTimeout(tOpen); pop.hidden = true; link.setAttribute("aria-expanded", "false"); if (focusLink) link.focus(); };
  link.addEventListener("click", e => { e.preventDefault(); pop.hidden ? open() : close(); });
  mm.addEventListener("mouseenter", () => { clearTimeout(tClose); tOpen = setTimeout(open, 120); });
  mm.addEventListener("mouseleave", () => { clearTimeout(tOpen); if (!mm.contains(document.activeElement)) tClose = setTimeout(() => close(), 350); });
  link.addEventListener("keydown", e => { if (e.key === "ArrowDown") { e.preventDefault(); open(); const t = pop.querySelector('[role="tab"][aria-selected="true"]'); t && t.focus(); } });
  document.addEventListener("keydown", e => { if (e.key === "Escape" && !pop.hidden) close(true); });
  document.addEventListener("click", e => { if (!pop.hidden && !mm.contains(e.target)) close(); });
  mm.addEventListener("focusout", e => { if (!mm.contains(e.relatedTarget)) tClose = setTimeout(() => { if (!mm.contains(document.activeElement)) close(); }, 150); });
})();
