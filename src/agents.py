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

_V = "?v=69"
_VIDS = [
    ("briefing-demo", "The Monday briefing.", "Bills checked, two held for the owner, the owner decides."),
    ("cash-forecast-dark", "13 weeks of cash, ahead.", "Add one big bill and watch the buffer break before it happens."),
    ("two-agents", "Same bill, two agents.", "A hidden instruction and changed bank details. One agent pays, ours holds it."),
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


# ---------------------------------------------------------------- hero flow diagram (v17)
_FIN = [("Xero or MYOB", "Your ledger"), ("Job &amp; timesheets", "Hours and quotes"), ("Bank feed", "Cash in and out"), ("Bills inbox", "Supplier invoices")]
_FOUT = [("13-week cash", "Every Monday"), ("Profit by job", "Every week"), ("Bills to approve", "Only the risky ones"), ("Drafted emails", "You press send")]


def _flow_desktop():
    ys = [40, 136, 232, 328]
    h = 60
    s = ['<svg class="flow flow-d" viewBox="0 0 600 400" role="img" aria-labelledby="flowT"><title id="flowT">Your systems flow into Beiz, where code checks the numbers, AI drafts, and you approve. Out come a 13-week cash view, profit by job, bills to approve and drafted emails.</title>']
    s.append('<text class="fl-h" x="0" y="18">YOUR SYSTEMS</text><text class="fl-h" x="300" y="18" text-anchor="middle">BEIZ</text><text class="fl-h" x="600" y="18" text-anchor="end">WHAT YOU GET</text>')
    cy = 220
    for i, y in enumerate(ys):
        c = y + h / 2
        s.append(f'<path id="fi{i}" class="fl-l" d="M150,{c} C195,{c} 190,{cy} 228,{cy}"/>')
        s.append(f'<path id="fo{i}" class="fl-l" d="M382,{cy} C415,{cy} 405,{c} 450,{c}"/>')
    for i, y in enumerate(ys):
        t, sub = _FIN[i]
        s.append(f'<g class="fl-n"><rect x="0" y="{y}" width="150" height="{h}" rx="6"/><text x="14" y="{y+26}" class="fl-t">{t}</text><text x="14" y="{y+45}" class="fl-s">{sub}</text></g>')
        t, sub = _FOUT[i]
        s.append(f'<g class="fl-n fl-out"><rect x="450" y="{y}" width="150" height="{h}" rx="6"/><text x="464" y="{y+26}" class="fl-t">{t}</text><text x="464" y="{y+45}" class="fl-s">{sub}</text></g>')
    s.append(f'<g class="fl-core"><rect x="218" y="{cy-96}" width="164" height="192" rx="8"/>'
             f'<text x="300" y="{cy-60}" text-anchor="middle" class="fl-t">Checks &amp; agents</text>'
             f'<circle cx="236" cy="{cy-24}" r="5" class="fl-ok"/><text x="248" y="{cy-20}" class="fl-s2">Code checks numbers</text>'
             f'<circle cx="236" cy="{cy+8}" r="5" class="fl-ai"/><text x="248" y="{cy+12}" class="fl-s2">AI drafts the work</text>'
             f'<circle cx="236" cy="{cy+40}" r="5" class="fl-gate"/><text x="248" y="{cy+44}" class="fl-s2">You approve</text>'
             f'<text x="300" y="{cy+78}" text-anchor="middle" class="fl-s">Built in your accounts</text></g>')
    for i in range(4):
        s.append(f'<circle r="3.5" class="fl-dot"><animateMotion dur="2.6s" begin="-{i*0.55:.2f}s" repeatCount="indefinite"><mpath href="#fi{i}"/></animateMotion></circle>')
        s.append(f'<circle r="3.5" class="fl-dot o"><animateMotion dur="2.6s" begin="-{(1.3+i*0.55)%2.6:.2f}s" repeatCount="indefinite"><mpath href="#fo{i}"/></animateMotion></circle>')
    s.append('</svg>')
    return "".join(s)


def _flow_mobile():
    s = ['<svg class="flow flow-m" viewBox="0 0 360 560" role="img" aria-labelledby="flowM"><title id="flowM">Your systems flow into Beiz, where code checks the numbers, AI drafts, and you approve. Out come a 13-week cash view, profit by job, bills to approve and drafted emails.</title>']
    s.append('<text class="fl-h" x="0" y="14">YOUR SYSTEMS</text><text class="fl-h" x="0" y="402">WHAT YOU GET</text>')
    boxes_in = [(0, 26), (184, 26), (0, 92), (184, 92)]
    boxes_out = [(0, 414), (184, 414), (0, 480), (184, 480)]
    w, h = 176, 56
    core_top, core_bot = 196, 352
    for i, (x, y) in enumerate(boxes_in[2:]):
        cx = x + w / 2
        s.append(f'<path id="mi{i}" class="fl-l" d="M{cx},{y+h} C{cx},{core_top-20} 180,{core_top-30} 180,{core_top}"/>')
    for i, (x, y) in enumerate(boxes_out[:2]):
        cx = x + w / 2
        s.append(f'<path id="mo{i}" class="fl-l" d="M180,{core_bot} C180,{core_bot+30} {cx},{y-24} {cx},{y}"/>')
    for i, (x, y) in enumerate(boxes_in):
        t, sub = _FIN[i]
        s.append(f'<g class="fl-n"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/><text x="{x+12}" y="{y+24}" class="fl-t">{t}</text><text x="{x+12}" y="{y+42}" class="fl-s">{sub}</text></g>')
    for i, (x, y) in enumerate(boxes_out):
        t, sub = _FOUT[i]
        s.append(f'<g class="fl-n fl-out"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/><text x="{x+12}" y="{y+24}" class="fl-t">{t}</text><text x="{x+12}" y="{y+42}" class="fl-s">{sub}</text></g>')
    s.append(f'<g class="fl-core"><rect x="60" y="{core_top}" width="240" height="{core_bot-core_top}" rx="8"/>'
             f'<text x="180" y="{core_top+30}" text-anchor="middle" class="fl-t">Checks &amp; agents</text>'
             f'<circle cx="90" cy="{core_top+62}" r="5" class="fl-ok"/><text x="104" y="{core_top+66}" class="fl-s2">Code checks numbers</text>'
             f'<circle cx="90" cy="{core_top+92}" r="5" class="fl-ai"/><text x="104" y="{core_top+96}" class="fl-s2">AI drafts the work</text>'
             f'<circle cx="90" cy="{core_top+122}" r="5" class="fl-gate"/><text x="104" y="{core_top+126}" class="fl-s2">You approve</text></g>')
    for i in range(4):
        s.append(f'<circle r="3.5" class="fl-dot"><animateMotion dur="2.4s" begin="-{i*0.6:.2f}s" repeatCount="indefinite"><mpath href="#mi{i%2}"/></animateMotion></circle>')
        s.append(f'<circle r="3.5" class="fl-dot o"><animateMotion dur="2.4s" begin="-{(1.2+i*0.6)%2.4:.2f}s" repeatCount="indefinite"><mpath href="#mo{i%2}"/></animateMotion></circle>')
    s.append('</svg>')
    return "".join(s)


FLOW = '<figure class="flowfig">' + _flow_desktop() + _flow_mobile() + '<figcaption>Your systems in. Clear answers out. A person signs off anything that touches money or customers.</figcaption></figure>'


WATCH_HOME = '<div class="watch hwatch">' + "".join(
    f'<figure><video data-src="/assets/media/{f}.mp4{_V}" poster="/assets/media/{f}.jpg{_V}" muted loop playsinline preload="none" aria-label="{t} {c}"></video><figcaption><b>{t}</b> {c}</figcaption></figure>'
    for f, t, c in _VIDS) + '</div><p style="margin-top:14px"><a class="textlink" href="/try/">Try the demos with your own numbers →</a></p>'


# ---------------------------------------------------------------- v20 animated agent team (hero)
def _agent(cx, cy, key, name, icon):
    return (f'<g class="ag" data-k="{key}" transform="translate({cx},{cy})">'
            f'<circle r="70" class="ag-halo"/>'
            f'<circle r="54" class="ag-ring"/>'
            f'<circle r="46" class="ag-disc"/>'
            f'{icon}'
            f'<text y="88" text-anchor="middle" class="ag-name">{name}</text></g>')


_I_PLAN = ('<g class="ic"><rect x="-15" y="-19" width="30" height="38" rx="4"/><rect x="-7" y="-23" width="14" height="7" rx="2" class="icf"/>'
           '<path d="M-8 -6 l3 3 5-6"/><path d="M3 -6 h6"/><path d="M-8 4 l3 3 5-6"/><path d="M3 4 h6"/><path d="M-8 13 h17"/></g>')
_I_EXEC = ('<g class="ic"><path d="M0 -20 L17 -11 L0 -2 L-17 -11 Z" class="icf"/><path d="M-17 -11 L-17 9 L0 18 L0 -2"/><path d="M17 -11 L17 9 L0 18"/>'
           '<path d="M-9 1 v6 M-5 3 v6" /><path d="M6 4 l5 -3 M6 9 l5 -3"/></g>')
_I_VAL = ('<g class="ic"><circle cx="-4" cy="-4" r="13"/><path d="M5 5 L17 17" stroke-width="5"/><path d="M-10 -4 l4 4 8 -9"/></g>')

_I_GOV = ('<g class="ic"><path d="M-20 -8 L0 -20 L20 -8 Z" class="icf"/><path d="M-20 -8 H20"/><path d="M-13 -4 V12 M-4 -4 V12 M5 -4 V12 M14 -4 V12"/><path d="M-21 16 H21"/></g>')


def _agent4(cx, cy, key, name, world, icon, wy):
    return (f'<g class="ag" data-k="{key}" transform="translate({cx},{cy})">'
            f'<circle r="74" class="ag-halo"/><circle r="52" class="ag-ring"/><circle r="44" class="ag-disc"/>{icon}'
            f'<text y="{wy if wy > 0 else wy-22}" text-anchor="middle" class="ag-world">{world}</text>'
            f'<text y="{wy+22 if wy > 0 else wy}" text-anchor="middle" class="ag-name">{name}</text></g>')


_NODES = [(130, 130, "plan", "Data scientist agent", "DATA SCIENCE · PLAN", _I_PLAN),
          (510, 130, "exec", "Accounting agent", "ACCOUNTING · DO", _I_EXEC),
          (510, 400, "val", "Reviewer agent", "REVIEW · CHECK", _I_VAL),
          (130, 400, "gov", "Governance agent", "GOVERNANCE · REPORT", _I_GOV)]

AGENT_TEAM = ('<figure class="team" id="team" aria-label="Animated illustration: four AI agents (data science, accounting, review and governance) work in a loop around a Chartered Accountant who signs off">'
  '<svg viewBox="-10 -10 660 580" class="team-svg" role="img" aria-hidden="true">'
  '<defs>'
  '<linearGradient id="tg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2DD4BF"/><stop offset="1" stop-color="#818CF8"/></linearGradient>'
  '<radialGradient id="halo" r=".5"><stop offset="0" stop-color="#2DD4BF" stop-opacity=".30"/><stop offset=".6" stop-color="#818CF8" stop-opacity=".10"/><stop offset="1" stop-color="#818CF8" stop-opacity="0"/></radialGradient>'
  '<radialGradient id="coreg" r=".5"><stop offset="0" stop-color="#818CF8" stop-opacity=".5"/><stop offset="1" stop-color="#818CF8" stop-opacity="0"/></radialGradient>'
  '<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
  '</defs>'
  '<g class="traces">'
  + "".join(f'<path d="{d}" class="tr"/><path d="{d}" class="tr-lit" style="animation-delay:-{i*0.6:.1f}s"/>' for i, d in enumerate([
      "M-10 245 H40 L70 215", "M650 245 H600 L570 215", "M-10 540 H60 L90 510", "M650 540 H580 L550 510",
      "M-10 20 H30 L55 45", "M650 20 H610 L585 45", "M250 570 V545 L275 520", "M390 570 V545 L365 520"]))
  + '</g>'
  # orbit loop through the four agents (clockwise)
  '<path id="orbit" d="M130 130 H510 V400 H130 Z" class="orbit"/>'
  + "".join(f'<circle r="4.5" class="pulse"><animateMotion dur="8s" begin="-{i*2:.0f}s" repeatCount="indefinite" rotate="auto"><mpath href="#orbit"/></animateMotion></circle>' for i in range(4))
  # spokes into the core
  + "".join(f'<path id="sp{i}" d="M{x} {y} L320 250" class="spoke"/>' for i, (x, y, *_r) in enumerate(_NODES))
  + "".join(f'<circle r="3.5" class="pulse s"><animateMotion dur="2.2s" begin="-{i*0.55:.2f}s" repeatCount="indefinite"><mpath href="#sp{i}"/></animateMotion></circle>' for i in range(4))
  + '<g class="core" transform="translate(320,250)"><circle r="96" fill="url(#coreg)" class="core-glow"/><circle r="70" class="core-ring"/>'
  '<path d="M0 -44 L36 -30 V2 C36 26 19 40 0 48 C-19 40 -36 26 -36 2 V-30 Z" class="shield"/>'
  '<path d="M-13 2 l9 9 18 -20" class="shield-tick"/></g>'
  '<text x="320" y="350" text-anchor="middle" class="core-world">YOUR HUMAN IN THE LOOP</text>'
  '<text x="320" y="372" text-anchor="middle" class="core-name">CA · DATA &amp; AI</text>'
  + "".join(_agent4(x, y, k, n, w, ic, -66 if y < 200 else 72) for x, y, k, n, w, ic in _NODES) +
  '</svg>'
  '<div class="team-feed" aria-live="polite"><span class="tf-dot"></span><span id="teamFeed">Data scientist agent: 13-week forecast refreshed from your ledger and bank feed</span></div>'
  '<figcaption>Example workforce on sample data. Typically live in three weeks.</figcaption></figure>')
