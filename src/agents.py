"""Homepage interactive blocks: agent console, live pipeline strip, wiring diagram, video strip.
The console runs on a made-up business and says so. The pipeline strip reads the site's real run log (data/markets.json)."""

AGENTS = [("cash", "Cash agent"), ("margin", "Margin agent"), ("collect", "Collections agent"), ("risk", "Risk agent")]

CONSOLE = '''<div class="console" id="console" role="region" aria-label="Interactive demo: AI agents brief the owner of a made-up business">
      <div class="con-bar"><span class="con-dots" aria-hidden="true"><i></i><i></i><i></i></span><b>Monday briefing</b><button class="con-run" type="button">Run the agents</button></div>
      <p class="con-biz">Sample data from a made-up 18-person electrical contractor. You're the owner.</p>
      <div class="con-agents">''' + "".join(
    f'<div class="ag" data-ag="{k}"><b>{n}</b><span class="ag-line">Ready</span><span class="ag-bar"><i></i></span></div>' for k, n in AGENTS) + '''</div>
      <div class="con-brief" aria-live="polite"><p class="con-hint">Press <b>Run the agents</b>. They'll read the books, then ask you to decide five things.</p></div>
      <div class="con-foot"><span class="con-count">0 of 5 decided</span><details class="con-audit"><summary>Audit trail</summary><ol></ol></details></div>
    </div>'''

PIPELINE = '''<section id="pipeline">
  <div class="wrap pipe">
    <p class="pipe-l"><span class="live-dot" aria-hidden="true"></span><b>Live, not a mock-up.</b> This website runs its own data pipeline. A scheduled job pulls the RBA cash rate, ASX and currency data, checks every figure against written rules, and holds anything that looks wrong instead of publishing it. Same pattern we build for your numbers.</p>
    <div class="pipe-r">
      <div><small>Last run</small><b data-pipe-ago>loading</b></div>
      <div><small>Sources up</small><b data-pipe-src>–</b></div>
      <div><small>Checks passed</small><b data-pipe-chk>–</b></div>
      <div><small>Held back</small><b data-pipe-held>–</b></div>
    </div>
    <details class="pipe-det"><summary>What the last run checked</summary><ul data-pipe-checks></ul><p class="fine">Recent runs: <span data-pipe-log></span></p></details>
  </div>
</section>'''


def _wiring_svg():
    W, H = 1160, 430
    src = ["Bank feed", "Xero or MYOB", "Job app", "CRM", "Inbox"]
    ags = ["Cash", "Margin", "Collections", "Risk"]
    outs = ["Monday brief", "Board pack", "Updates in Xero", "Customer emails"]
    sy = [30 + i * 78 for i in range(5)]            # source box tops, h=50
    ay = [52 + i * 86 for i in range(4)]            # agent box tops, h=56
    oy = [52 + i * 86 for i in range(4)]            # outcome box tops, h=50
    g = []
    box = lambda x, y, w, h, t, cls="": g.append(f'<g class="wb {cls}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/><text x="{x + w / 2}" y="{y + h / 2 + 5}" text-anchor="middle">{t}</text></g>')
    paths, dots = [], []

    def curve(pid, x1, y1, x2, y2, cls="wl"):
        mx = (x1 + x2) / 2
        paths.append(f'<path id="{pid}" class="{cls}" d="M{x1},{y1} C{mx},{y1} {mx},{y2} {x2},{y2}"/>')

    links = [(0, 0), (1, 0), (1, 1), (2, 1), (1, 2), (3, 2), (4, 3), (0, 3)]
    for i, (s_, a) in enumerate(links):
        curve(f"w{i}", 172, sy[s_] + 25, 290, ay[a] + 28)
        dots.append((f"w{i}", 2.6 + (i % 3) * .5, i * .45, "d"))
    for a in range(4):
        curve(f"c{a}", 450, ay[a] + 28, 560, 175 + a * 30)
        dots.append((f"c{a}", 2.2, .3 + a * .7, "d"))
    # controls -> outcomes (within rules) and controls -> you (outside rules)
    curve("ok", 730, 150, 990, oy[0] + 25, "wl ok")
    curve("you", 730, 290, 810, 290, "wl held")
    for o in range(4):
        curve(f"o{o}", 930, 290, 990, oy[o] + 25)
        dots.append((f"o{o}", 1.8, 1.2 + o * .6, "d"))
    dots += [("ok", 2.4, .2, "d"), ("ok", 2.4, 1.4, "d"), ("you", 1.6, .8, "r"), ("you", 1.6, 2.4, "r")]
    for i, t in enumerate(src):
        box(10, sy[i], 162, 50, t)
    for i, t in enumerate(ags):
        box(290, ay[i], 160, 56, t + " agent", "ag2")
    g.append('<g class="wb ctl"><rect x="560" y="120" width="170" height="210" rx="8"/>'
             '<text x="645" y="160" text-anchor="middle" class="h">Your rules</text>'
             '<text x="645" y="196" text-anchor="middle" class="s">Approval limits</text>'
             '<text x="645" y="222" text-anchor="middle" class="s">Who can change what</text>'
             '<text x="645" y="248" text-anchor="middle" class="s">Sanity checks</text>'
             '<text x="645" y="274" text-anchor="middle" class="s">Everything logged</text></g>')
    g.append('<g class="wb you"><rect x="810" y="250" width="120" height="80" rx="40"/><text x="870" y="286" text-anchor="middle" class="h">You</text><text x="870" y="308" text-anchor="middle" class="s">approve</text></g>')
    for i, t in enumerate(outs):
        box(990, oy[i], 160, 50, t)
    labels = ('<text x="742" y="178" class="lab ok">Within your rules: runs, logged</text>'
              '<text x="738" y="350" class="lab held">Outside your rules: held for you</text>'
              '<text x="10" y="18" class="cap">YOUR SYSTEMS</text><text x="290" y="40" class="cap">AGENTS PREPARE</text>'
              '<text x="560" y="108" class="cap">CONTROLS DECIDE</text><text x="990" y="40" class="cap">WHAT YOU GET</text>')
    dot_svg = "".join(
        f'<circle class="dot {c}" r="{5 if c == "r" else 4}"><animateMotion dur="{d}s" begin="{b}s" repeatCount="indefinite" rotate="auto"><mpath href="#{p}"/></animateMotion></circle>'
        for p, d, b, c in dots)
    return (f'<svg class="wire" viewBox="0 0 {W} {H}" role="img" aria-label="Diagram: your systems feed four agents; their work passes through your rules; anything within the rules runs and is logged, anything outside is held for your approval">'
            + "".join(paths) + "".join(g) + labels + dot_svg + "</svg>")


WIRING = '''<section id="wiring" class="band">
  <div class="wrap">
    <h2>How it's wired.</h2>
    <p class="lede">Agents only prepare the work. Your rules decide what runs on its own and what waits for you. Every step is written to a log you can show your auditor, your bank or your board.</p>
    ''' + _wiring_svg() + '''
    <ol class="wire-m" aria-hidden="true">
      <li><small>Your systems</small><span>Bank feed</span><span>Xero or MYOB</span><span>Job app</span><span>CRM</span><span>Inbox</span></li>
      <li><small>Agents prepare</small><span>Cash</span><span>Margin</span><span>Collections</span><span>Risk</span></li>
      <li class="ctl"><small>Controls decide</small><span>Approval limits</span><span>Who can change what</span><span>Sanity checks</span><span>Everything logged</span></li>
      <li class="you"><small>Outside the rules</small><span>Held for you to approve</span></li>
      <li><small>What you get</small><span>Monday brief</span><span>Board pack</span><span>Updates in Xero</span><span>Customer emails</span></li>
    </ol>
  </div>
</section>'''

_V = "?v=44"
_VIDS = [
    ("cash-forecast-demo", "13 weeks of cash, ahead.", "Add one big bill and watch the buffer break before it happens."),
    ("bill-check-demo", "Controls on money going out.", "Eight payments checked. Four held for a person, each with the reason."),
    ("how-beiz-adds-value-3", "Rules an accountant sets.", "How the controls layer decides what runs and what waits."),
]
WATCH = '''<section id="watch">
  <div class="wrap">
    <h2>Watch it work.</h2>
    <p class="lede">Screen recordings of our own builds on sample data. No stock footage, no voice-over.</p>
    <div class="watch">''' + "".join(
    f'<figure><video data-src="/assets/media/{f}.mp4{_V}" poster="/assets/media/{f}.jpg{_V}" muted loop playsinline preload="none" aria-label="{t} {c}"></video><figcaption><b>{t}</b> {c}</figcaption></figure>'
    for f, t, c in _VIDS) + '''</div>
    <p style="margin-top:16px"><a class="textlink" href="/try/">Try the demos with your own numbers</a></p>
  </div>
</section>'''
