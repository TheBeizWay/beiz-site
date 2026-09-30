"""Inline SVG sample charts (fictional data). Dark surface, validated palette:
blue #3987e5, orange #d95926, aqua #199e70 (dataviz reference, dark steps; passes CVD checks on #0d1115).
Status warning uses the site's amber and always ships with an icon + label."""

BLUE, ORANGE, AQUA = "#3987e5", "#d95926", "#199e70"
WARN = "#fbbf24"
INK, MUTED, GRID = "#e8edf1", "#93a0ab", "#1c232a"
FONT = 'font-family="Inter,system-ui,sans-serif"'
MONO = 'font-family="JetBrains Mono,ui-monospace,monospace"'


def _k(v):
    return f"${v/1000:,.0f}k" if abs(v) < 1_000_000 else f"${v/1_000_000:,.2f}m"


def _bar_top(x, y, w, h, r=4):
    """Column with rounded top corners, square at the baseline."""
    r = min(r, w / 2, h)
    return (f"M{x:.1f},{y+h:.1f} V{y+r:.1f} Q{x:.1f},{y:.1f} {x+r:.1f},{y:.1f} "
            f"H{x+w-r:.1f} Q{x+w:.1f},{y:.1f} {x+w:.1f},{y+r:.1f} V{y+h:.1f} Z")


def _table(headers, rows, cls=""):
    th = "".join(f'<th class="{"n" if i else ""}">{h}</th>' for i, h in enumerate(headers))
    tr = "".join("<tr>" + "".join(f'<td class="{"n" if i else ""}">{c}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<details class="numbers"><summary>See the numbers</summary><div class="tblw"><table class="tbl {cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div></details>'


# ---------------------------------------------------------------- 13-week cash
CASH_WEEKS = ["5 Oct", "12 Oct", "19 Oct", "26 Oct", "2 Nov", "9 Nov", "16 Nov", "23 Nov", "30 Nov", "7 Dec", "14 Dec", "21 Dec", "28 Dec"]
CASH = [42000, 38500, 45200, 36800, 31400, 27100, 17600, 23900, 33200, 39400, 35100, 44300, 48700]
BUFFER = 20000


def cash13(compact=False):
    W, H = (720, 300) if not compact else (560, 220)
    L, R, T, B = 52, 14, 22, 34
    pw, ph = W - L - R, H - T - B
    ymax = 50000
    n = len(CASH)
    band = pw / n
    bw = band * 0.62
    y = lambda v: T + ph - v / ymax * ph
    out = [f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="Sample 13-week cash forecast. Closing cash dips to $17,600 in the week of 16 November, below the $20,000 buffer, then recovers to $48,700.">']
    for g in range(0, ymax + 1, 10000):
        out.append(f'<line x1="{L}" x2="{W-R}" y1="{y(g):.1f}" y2="{y(g):.1f}" stroke="{GRID}" stroke-width="1"/>')
        out.append(f'<text x="{L-8}" y="{y(g)+4:.1f}" text-anchor="end" font-size="11" fill="{MUTED}" {MONO}>{_k(g)}</text>')
    for i, v in enumerate(CASH):
        x = L + i * band + (band - bw) / 2
        low = v < BUFFER
        col = WARN if low else BLUE
        out.append(f'<g><title>Week of {CASH_WEEKS[i]}: closing cash {_k(v)}{" · below buffer" if low else ""}</title>'
                   f'<rect x="{L+i*band:.1f}" y="{T}" width="{band:.1f}" height="{ph}" fill="transparent"/>'
                   f'<path d="{_bar_top(x, y(v), bw, T+ph-y(v))}" fill="{col}"/></g>')
        if not compact or i % 2 == 0:
            out.append(f'<text x="{x+bw/2:.1f}" y="{H-12}" text-anchor="middle" font-size="10.5" fill="{MUTED}" {MONO}>{CASH_WEEKS[i]}</text>')
    out.append(f'<line x1="{L}" x2="{W-R}" y1="{y(BUFFER):.1f}" y2="{y(BUFFER):.1f}" stroke="{INK}" stroke-width="1.2" stroke-dasharray="4 4" opacity=".7"/>')
    out.append(f'<text x="{W-R}" y="{y(BUFFER)-6:.1f}" text-anchor="end" font-size="11" fill="{INK}" {FONT}>Minimum buffer {_k(BUFFER)}</text>')
    i = CASH.index(min(CASH))
    x = L + i * band + band / 2
    out.append(f'<text x="{x:.1f}" y="{y(CASH[i])-8:.1f}" text-anchor="middle" font-size="11.5" font-weight="600" fill="{WARN}" {FONT}>▼ {_k(CASH[i])}</text>')
    if not compact:
        out.append(f'<text x="{L+band/2:.1f}" y="{y(CASH[0])-8:.1f}" text-anchor="middle" font-size="11" fill="{INK}" {FONT}>{_k(CASH[0])}</text>')
        out.append(f'<text x="{L+(n-0.5)*band:.1f}" y="{y(CASH[-1])-8:.1f}" text-anchor="middle" font-size="11" fill="{INK}" {FONT}>{_k(CASH[-1])}</text>')
    out.append("</svg>")
    svg = "".join(out)
    if compact:
        return svg
    return svg + _table(["Week of", "Closing cash", "Status"], [[w, f"${v:,.0f}", "Below buffer" if v < BUFFER else "OK"] for w, v in zip(CASH_WEEKS, CASH)])


# ---------------------------------------------------------------- job margins
JOBS = [("Wardrobes, Parramatta", 34), ("Kitchen, Bondi", 31), ("Deck, Manly", 28), ("Laundry, Epping", 26),
        ("Kitchen, Cronulla", 22), ("Stairs, Mosman", 19), ("Bathroom, Ryde", 12), ("Office fit-out, CBD", 8)]
TARGET = 20


def job_margins():
    W, H = 720, 34 * len(JOBS) + 40
    L, R, T = 170, 70, 26
    pw = W - L - R
    xmax = 40
    x = lambda v: L + v / xmax * pw
    out = [f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="Sample job profitability. Six of eight jobs beat the 20% target margin; Bathroom Ryde at 12% and Office fit-out CBD at 8% fall below.">']
    for g in range(0, xmax + 1, 10):
        out.append(f'<line x1="{x(g):.1f}" x2="{x(g):.1f}" y1="{T-6}" y2="{H-10}" stroke="{GRID}"/>')
        out.append(f'<text x="{x(g):.1f}" y="{T-12}" text-anchor="middle" font-size="10.5" fill="{MUTED}" {MONO}>{g}%</text>')
    for i, (name, m) in enumerate(JOBS):
        yy = T + i * 34 + 6
        low = m < TARGET
        col = WARN if low else BLUE
        bw = x(m) - L
        out.append(f'<g><title>{name}: {m}% margin{" · below target" if low else ""}</title>'
                   f'<rect x="0" y="{yy-5}" width="{W}" height="32" fill="transparent"/>'
                   f'<text x="{L-10}" y="{yy+15}" text-anchor="end" font-size="12.5" fill="{INK}" {FONT}>{name}</text>'
                   f'<path d="M{L},{yy+2} H{L+bw-4:.1f} Q{L+bw:.1f},{yy+2} {L+bw:.1f},{yy+6} V{yy+16} Q{L+bw:.1f},{yy+20} {L+bw-4:.1f},{yy+20} H{L} Z" fill="{col}"/>'
                   f'<text x="{L+bw+8:.1f}" y="{yy+15}" font-size="12" fill="{INK}" {MONO}>{m}%{" ▼" if low else ""}</text></g>')
    out.append(f'<line x1="{x(TARGET):.1f}" x2="{x(TARGET):.1f}" y1="{T-2}" y2="{H-10}" stroke="{INK}" stroke-width="1.2" stroke-dasharray="4 4" opacity=".7"/>')
    out.append(f'<text x="{x(TARGET)+6:.1f}" y="{H-14}" font-size="11" fill="{INK}" {FONT}>Target {TARGET}%</text>')
    out.append("</svg>")
    return "".join(out) + _table(["Job", "Margin", "Status"], [[n, f"{m}%", "Below target" if m < TARGET else "OK"] for n, m in JOBS])


# ---------------------------------------------------------------- runway scenarios
def _scenario(start, burn0, dburn, months=24):
    cash, out, burn = start, [start], burn0
    for _ in range(months):
        cash -= burn
        burn += dburn
        out.append(max(cash, 0))
    return out


START = 1_500_000
SCEN = [("Base", BLUE, _scenario(START, 105_000, -2_000)),
        ("Worst", ORANGE, _scenario(START, 128_000, 2_500)),
        ("Best", AQUA, _scenario(START, 98_000, -6_000))]


def _runway(series):
    for i, v in enumerate(series):
        if v <= 0:
            return i
    return None


def runway():
    W, H = 720, 320
    L, R, T, B = 60, 150, 20, 36
    pw, ph = W - L - R, H - T - B
    ymax = 2_000_000
    x = lambda m: L + m / 24 * pw
    y = lambda v: T + ph - v / ymax * ph
    out = [f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="Sample runway scenarios for a fictional software startup over 24 months: worst case runs out of cash in month {_runway(SCEN[1][2])}, base case in month {_runway(SCEN[0][2])}, best case never runs out.">']
    for g in range(0, ymax + 1, 500_000):
        out.append(f'<line x1="{L}" x2="{L+pw}" y1="{y(g):.1f}" y2="{y(g):.1f}" stroke="{GRID}"/>')
        out.append(f'<text x="{L-8}" y="{y(g)+4:.1f}" text-anchor="end" font-size="11" fill="{MUTED}" {MONO}>{"$0" if g == 0 else _k(g)}</text>')
    for m in range(0, 25, 6):
        out.append(f'<text x="{x(m):.1f}" y="{H-14}" text-anchor="middle" font-size="10.5" fill="{MUTED}" {MONO}>{"Now" if m == 0 else f"M{m}"}</text>')
    for name, col, s in SCEN:
        pts = " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(s))
        out.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round"/>')
        rw = _runway(s)
        end_i = rw if rw is not None else 24
        cx, cy = x(end_i), y(s[end_i])
        out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.5" fill="{col}" stroke="#0d1115" stroke-width="2"/>')
        label = f"{name}: {rw} months" if rw is not None else f"{name}: 24+ months"
        ly = cy if rw is None else cy
        out.append(f'<text x="{L+pw+10}" y="{(y(s[24]) if rw is None else y(0)) + (0 if rw is None else (-8 if name == "Worst" else 12)):.1f}" font-size="12" fill="{INK}" {FONT}><tspan fill="{col}">●</tspan> {label}</text>')
        for i, v in enumerate(s):
            out.append(f'<circle cx="{x(i):.1f}" cy="{y(v):.1f}" r="7" fill="transparent"><title>{name}, month {i}: {_k(v)}</title></circle>')
    out.append("</svg>")
    rows = [[f"Month {m}"] + [f"${s[m]:,.0f}" for _, _, s in SCEN] for m in range(0, 25, 3)]
    return "".join(out) + _table(["Month", "Base", "Worst", "Best"], rows)


def runway_facts():
    return {n: _runway(s) for n, _, s in SCEN}
