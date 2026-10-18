/* "What we do" discovery panel (preview). Problem-led tabs; works with mouse, keyboard and touch. */
(() => {
  const root = document.getElementById("wwd"); if (!root) return;
  const tabs = [...root.querySelectorAll('[role="tab"]')], panes = [...root.querySelectorAll('[role="tabpanel"]')];
  const show = (i, focus) => {
    tabs.forEach((t, j) => { t.setAttribute("aria-selected", j === i); t.tabIndex = j === i ? 0 : -1; });
    panes.forEach((p, j) => { p.hidden = j !== i; });
    if (focus) tabs[i].focus();
  };
  tabs.forEach((t, i) => {
    t.addEventListener("click", () => show(i));
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
})();
