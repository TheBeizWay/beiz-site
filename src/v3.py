"""Standalone redesign preview at /preview/firm/: firm-led, product visuals. (19 Oct 2026). Light, founder-led, five numbered sections."""
from layout import ASSET_V, CALL_HREF, CALL_ATTR

CSS = """
@font-face{font-family:Serif4;font-weight:500;font-display:swap;src:url(/assets/fonts/source-serif-4-latin-500-normal.woff2) format('woff2')}
@font-face{font-family:Serif4;font-weight:600;font-display:swap;src:url(/assets/fonts/source-serif-4-latin-600-normal.woff2) format('woff2')}
@font-face{font-family:Inter;font-weight:400;font-display:swap;src:url(/assets/fonts/inter-latin-400-normal.woff2) format('woff2')}
@font-face{font-family:Inter;font-weight:500;font-display:swap;src:url(/assets/fonts/inter-latin-500-normal.woff2) format('woff2')}
@font-face{font-family:Inter;font-weight:600;font-display:swap;src:url(/assets/fonts/inter-latin-600-normal.woff2) format('woff2')}
:root{--bg:#F5F1E8;--card:#FBF9F4;--ink:#1C1B18;--soft:#5C5950;--faint:#8A867B;--line:#E2DCCD;--green:#1F5A40;--green2:#E3EDE6;--amber:#B9781B;--amber2:#F6EAD4;--dark:#1C1B18}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.6 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}
.w{max-width:1160px;margin:0 auto;padding:0 32px}
h1,h2,h3{font-family:Serif4,Georgia,serif;font-weight:500;letter-spacing:-.015em;margin:0}
.top{position:sticky;top:0;z-index:20;background:rgba(245,241,232,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.top .w{display:flex;align-items:center;gap:28px;height:72px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none}
.brand img{width:36px;height:36px;border-radius:8px}
.brand b{font:600 15px/1.1 Inter,sans-serif;letter-spacing:.14em}
.brand small{display:block;font-size:12px;color:var(--soft);letter-spacing:.02em;margin-top:3px}
.top nav{display:flex;gap:26px;margin-left:auto}
.top nav a{text-decoration:none;font-size:15px;color:var(--soft)}
.top nav a:hover{color:var(--ink)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;padding:0 22px;border-radius:999px;font:500 15px Inter,sans-serif;text-decoration:none;border:1px solid var(--ink);transition:transform .15s,background .15s}
.btn:hover{transform:translateY(-1px)}
.btn.p{background:var(--ink);color:var(--bg)}
.btn.g{background:transparent;color:var(--ink)}
.top .btn{min-height:40px;padding:0 18px;font-size:14px}
.hero{padding:88px 0 96px}
.hero .w{display:grid;grid-template-columns:1.1fr .9fr;gap:72px;align-items:center}
.pill{display:inline-flex;gap:8px;align-items:center;font-size:14px;color:var(--soft);border:1px solid var(--line);border-radius:999px;padding:6px 14px;margin-bottom:28px;background:var(--card)}
.pill i{width:7px;height:7px;border-radius:50%;background:var(--green)}
.hero h1{font-size:clamp(2.6rem,5.6vw,4.6rem);line-height:1.02;margin-bottom:28px}
.hero p.l{font-size:1.2rem;color:var(--soft);max-width:31em;margin:0 0 36px}
.hero p.l b{color:var(--ink);font-weight:500}
.ctas{display:flex;gap:12px;flex-wrap:wrap}
.ph{position:relative}
.ph img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:24px}
.log{position:absolute;left:-48px;bottom:-36px;width:330px;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 18px;box-shadow:0 18px 40px rgba(28,27,24,.12);font-size:14px}
.log .h{display:flex;justify-content:space-between;font-size:12px;color:var(--faint);margin-bottom:6px}
.log .r{display:flex;align-items:center;gap:10px;padding:9px 0;border-top:1px solid var(--line)}
.log .s{margin-left:auto;font-size:12px;padding:2px 9px;border-radius:999px;white-space:nowrap}
.log .ok .s{background:var(--green2);color:var(--green)}
.log .held .s{background:var(--amber2);color:var(--amber)}
.sec{padding:104px 0;border-top:1px solid var(--line)}
.lab{font-size:14px;color:var(--faint);margin:0 0 18px;font-variant-numeric:tabular-nums}
.lab b{color:var(--green);font-weight:600;margin-right:10px}
.sec h2{font-size:clamp(2rem,3.6vw,3rem);line-height:1.1;max-width:20ch;margin-bottom:18px}
.sec .lead{font-size:1.12rem;color:var(--soft);max-width:38em;margin:0 0 52px}
.offers{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.off{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:20px;padding:30px;text-decoration:none;transition:border-color .2s,transform .2s}
.off:hover{border-color:var(--ink);transform:translateY(-2px)}
.off .n{font-size:13px;color:var(--faint)}
.off h3{font-size:1.5rem;line-height:1.2;margin:22px 0 12px}
.off p{color:var(--soft);margin:0 0 26px;flex:1}
.off .pr{display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid var(--line);padding-top:18px}
.off .pr b{font:600 1.1rem Inter,sans-serif}
.off .pr span{font-size:14px;color:var(--soft);text-decoration:underline;text-underline-offset:3px}
.more{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:20px}
.more a{display:flex;justify-content:space-between;gap:12px;padding:18px 22px;border:1px solid var(--line);border-radius:14px;text-decoration:none;font-size:15px}
.more a:hover{border-color:var(--ink)}
.more a span{color:var(--soft)}
.nodo{margin-top:28px;font-size:15px;color:var(--soft)}
.quote{font-family:Serif4,Georgia,serif;font-size:clamp(1.7rem,3vw,2.5rem);line-height:1.2;max-width:24ch;margin:0 0 56px}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:32px;list-style:none;margin:0;padding:0;counter-reset:s}
.steps li{counter-increment:s;border-top:2px solid var(--ink);padding-top:22px}
.steps li:before{content:"0" counter(s);font-size:13px;color:var(--faint);display:block;margin-bottom:14px}
.steps b{display:block;font:500 1.15rem Inter,sans-serif;margin-bottom:8px}
.steps p{margin:0;color:var(--soft);font-size:15.5px}
.dark{background:var(--dark);color:#EEEAE0;border-top:0}
.dark .lab{color:#9C978A}.dark .lab b{color:#7FC79D}
.dark .lead{color:#B7B2A6}
.tools{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.tool{display:block;border:1px solid #3A3833;border-radius:20px;padding:30px;text-decoration:none;transition:border-color .2s}
.tool:hover{border-color:#EEEAE0}
.tool .k{display:inline-block;font-size:12px;border:1px solid #4A4842;border-radius:999px;padding:3px 10px;color:#B7B2A6}
.tool h3{font-size:1.4rem;margin:22px 0 10px;color:#FAF8F2}
.tool p{margin:0 0 22px;color:#B7B2A6;font-size:15.5px}
.tool span{text-decoration:underline;text-underline-offset:3px;font-size:15px}
.me{display:grid;grid-template-columns:.8fr 1.2fr;gap:72px;align-items:start}
.me .story p{font-size:1.1rem;color:var(--soft);margin:0 0 18px;max-width:34em}
.me .story p:first-of-type{font-family:Serif4,Georgia,serif;font-size:1.5rem;line-height:1.35;color:var(--ink)}
.facts{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.facts li{display:flex;justify-content:space-between;gap:20px;padding:16px 0;border-bottom:1px solid var(--line);font-size:15px}
.facts li span{color:var(--soft)}
.contact .w{display:grid;grid-template-columns:1.1fr .9fr;gap:72px;align-items:end}
.contact h2{max-width:14ch}
.ways{display:grid;gap:12px}
.ways a{display:flex;justify-content:space-between;align-items:center;padding:20px 24px;background:var(--card);border:1px solid var(--line);border-radius:16px;text-decoration:none}
.ways a:hover{border-color:var(--ink)}
.ways a b{font-weight:500}
.ways a span{font-size:14px;color:var(--soft)}
footer{border-top:1px solid var(--line);padding:40px 0 56px;font-size:13px;color:var(--faint)}
footer .w{display:grid;gap:8px}
footer a{color:var(--soft)}
@media (max-width:980px){.top nav{display:none}.top .btn{margin-left:auto}.hero .w,.me,.contact .w{grid-template-columns:1fr;gap:56px}.offers,.tools,.more{grid-template-columns:1fr}.steps{grid-template-columns:1fr 1fr}.ph{max-width:460px}.log{left:16px;right:16px;width:auto;bottom:-44px}.hero{padding:56px 0 96px}.sec{padding:80px 0}}
@media (max-width:560px){.w{padding:0 20px}.top .w{gap:12px}.brand small{display:none}.steps{grid-template-columns:1fr}.hero h1{font-size:2.5rem}.log .r{flex-wrap:wrap}.ctas{flex-direction:column}.ctas .btn{width:100%}.top .btn{margin-left:auto}}

.hero{padding:80px 0 72px}
.hero .w{grid-template-columns:1fr 1fr;gap:56px}
.hero h1{max-width:13ch}
.panel{background:#1C1B18;border-radius:22px;padding:22px;color:#EEEAE0;box-shadow:0 30px 60px rgba(28,27,24,.18)}
.panel .bar{display:flex;gap:6px;margin-bottom:16px}.panel .bar i{width:10px;height:10px;border-radius:50%;background:#3A3833}
.panel .ttl{display:flex;justify-content:space-between;font-size:13px;color:#9C978A;margin-bottom:12px}
.kp{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:14px}
.kp div{background:#26251F;border-radius:12px;padding:12px 14px}
.kp span{display:block;font-size:12px;color:#9C978A}.kp b{font:600 22px Inter,sans-serif}
.kp .g b{color:#7FC79D}.kp .a b{color:#E9B460}
.pl .r{display:flex;align-items:center;gap:10px;padding:11px 2px;border-top:1px solid #33312B;font-size:14px}
.pl .s{margin-left:auto;font-size:12px;padding:2px 9px;border-radius:999px;white-space:nowrap}
.pl .ok .s{background:#21402F;color:#8FD3AB}.pl .held .s{background:#4A3818;color:#F0C27A}.pl .stop .s{background:#4A2420;color:#F2A69C}
.panel .ft{font-size:12px;color:#8A857A;margin-top:12px}
.strip{border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:var(--card)}
.strip .w{display:grid;grid-template-columns:repeat(4,1fr);gap:0}
.strip div{padding:26px 24px;border-left:1px solid var(--line)}.strip div:first-child{border-left:0;padding-left:0}
.strip b{display:block;font:600 15px Inter,sans-serif;margin-bottom:4px}.strip span{font-size:14px;color:var(--soft)}
.areas{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.area{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:30px;display:flex;flex-direction:column}
.area .k{font-size:13px;color:var(--green);font-weight:600;margin-bottom:16px}
.area h3{font-size:1.45rem;line-height:1.2;margin-bottom:12px}
.area p{color:var(--soft);margin:0 0 22px}
.area ul{list-style:none;margin:auto 0 0;padding:0;border-top:1px solid var(--line)}
.area li a{display:flex;justify-content:space-between;gap:12px;padding:13px 0;border-bottom:1px solid var(--line);text-decoration:none;font-size:15px}
.area li a:hover{color:var(--green)}
.area li span{color:var(--soft);white-space:nowrap}
.lead2{display:grid;grid-template-columns:200px 1fr auto;gap:36px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:22px;padding:28px}
.lead2 img{width:200px;height:200px;object-fit:cover;border-radius:16px}
.lead2 h3{font-size:1.6rem;margin-bottom:6px}.lead2 .c{font-size:14px;color:var(--green);font-weight:600;margin:0 0 12px}
.lead2 p{color:var(--soft);margin:0;max-width:40em}
@media (max-width:980px){.hero .w{grid-template-columns:1fr}.hero .w>*{min-width:0}.strip .w,.areas{grid-template-columns:1fr 1fr}.strip div:nth-child(3){border-left:0;padding-left:0}.lead2{grid-template-columns:1fr}.lead2 img{width:140px;height:140px}}
@media (max-width:560px){.strip .w,.areas{grid-template-columns:1fr}.strip div{border-left:0;padding-left:0;border-top:1px solid var(--line)}.strip div:first-child{border-top:0}.kp b{font-size:18px}.pl .r{flex-wrap:wrap}.pl .s{margin-left:0}}

@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
"""

def build():
    areas = [
      ("Your work", "AI agents that do the checking", "Routine finance and admin work, done by agents with written limits and a person they report to.",
       [("/services/ai-readiness-sprint/", "AI workforce setup", "from $8,500"), ("/leave-cover/", "Finance leave cover", "from $3,500"), ("/bill-check/", "Free bill check", "Free")]),
      ("Your numbers", "Cash and profit you can trust", "Models built on your own ledger and job data, with every assumption written down.",
       [("/cash-data-check/", "Two-week cash and data check", "$1,500"), ("/services/dashboards-and-models/", "Cash and job profit models", "from $5,000"), ("/ai-cost-calculator/", "AI running-cost calculator", "Free")]),
      ("Your controls", "AI and compliance that hold up", "Clear owners, approval points and evidence for AI use, AML/CTF and the Privacy Act.",
       [("/compliance-sprint/", "Compliance controls sprint", "from $3,500"), ("/aml-ctf-accounting-firms/", "AML/CTF for accounting firms", "Guide"), ("/prices/#ops", "Monthly controls operations", "from $1,250/mo")]),
    ]
    ar = "".join(f'<div class="area"><span class="k">{k}</span><h3>{t}</h3><p>{d}</p><ul>' + "".join(f'<li><a href="{h}">{n}<span>{p}</span></a></li>' for h, n, p in links) + '</ul></div>' for k, t, d, links in areas)
    tools = [("/bill-check/", "Free · no upload", "Bill check", "Drop in a bills export and see duplicates and changed bank details. Runs in your browser; nothing leaves your computer.", "Check your bills"),
             ("/workshop/", "Free · 5 minutes", "AI workshop", "Map your week, pick the first job worth handing to an agent, and set its limits.", "Take the workshop"),
             ("/ai-cost-calculator/", "Free", "AI running-cost calculator", "What an agent actually costs to run each month, by job and model, in Australian dollars.", "Work it out")]
    tl = "".join(f'<a class="tool" href="{h}"><span class="k">{k}</span><h3>{t}</h3><p>{d}</p><span>{c}</span></a>' for h, k, t, d, c in tools)
    return f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Beiz Data &amp; Accounting · redesign preview v3</title>
<meta name="robots" content="noindex"><meta name="theme-color" content="#F5F1E8">
<link rel="icon" href="/assets/brand/beiz-icon.svg">
<style>{CSS}</style></head>
<body>
<header class="top"><div class="w">
  <a class="brand" href="/preview/firm/"><img src="/assets/brand/beiz-icon.svg" alt=""><span><b>BEIZ</b><small>Data &amp; Accounting</small></span></a>
  <nav aria-label="Main"><a href="#services">Services</a><a href="#how">How it works</a><a href="#try">Free tools</a><a href="/prices/">Prices</a><a href="/about/">About</a></nav>
  <a class="btn p" href="{CALL_HREF}"{CALL_ATTR}>Book a call</a>
</div></header>
<main>
<section class="hero"><div class="w">
  <div>
    <span class="pill"><i></i>Chartered Accountant led · Canberra, working Australia-wide</span>
    <h1>We build the systems behind your numbers.</h1>
    <p class="l">AI agents, cash models and compliance controls for Australian businesses. Every system is tested on your own records before it goes live, and nothing is paid or sent until a person approves it.</p>
    <div class="ctas"><a class="btn p" href="{CALL_HREF}"{CALL_ATTR}>Book a 20-minute call</a><a class="btn g" href="/bill-check/">Try the free bill check</a></div>
  </div>
  <div class="panel" aria-label="Example control panel for a made-up business">
    <div class="bar"><i></i><i></i><i></i></div>
    <div class="ttl"><span>This week · payables agent</span><span>Example, made-up business</span></div>
    <div class="kp"><div class="g"><span>Bills matched</span><b>41</b></div><div class="a"><span>Held for a person</span><b>3</b></div><div><span>Paid without a person</span><b>0</b></div></div>
    <div class="pl">
      <div class="r ok">6 bills matched to orders and deliveries<span class="s">approved</span></div>
      <div class="r held">Electrician billed 22 h, timesheet shows 14 h<span class="s">held for a person</span></div>
      <div class="r stop">Email asks to change a supplier's bank details<span class="s">blocked</span></div>
      <div class="r held">Same invoice, new number<span class="s">held for a person</span></div>
    </div>
    <p class="ft">Every action logged in your own accounts. Figures illustrative, excluding GST.</p>
  </div>
</div></section>

<section class="strip"><div class="w">
  <div><b>Tested on your records</b><span>Live only at a pass mark agreed in writing</span></div>
  <div><b>A person approves</b><span>Nothing is paid or sent on its own</span></div>
  <div><b>Fixed prices</b><span>Scope and price agreed before we start</span></div>
  <div><b>Chartered Accountant led</b><span>CA ANZ · Certificate of Public Practice · GAICD</span></div>
</div></section>

<section class="sec" id="services" style="border-top:0"><div class="w">
  <p class="lab"><b>01</b>Services</p>
  <h2>Three areas. One firm that owns the whole thing.</h2>
  <p class="lead">Fixed prices, agreed in writing. Beiz isn't registered for GST, so no GST is added. We don't do tax returns, BAS or statutory audit; your tax agent keeps that work.</p>
  <div class="areas">{ar}</div>
</div></section>

<section class="sec" id="how"><div class="w">
  <p class="lab"><b>02</b>How it works</p>
  <p class="quote">AI can prepare the work. Your people approve the decisions.</p>
  <ol class="steps">
    <li><b>Written down</b><p>One job, its limits and the person it reports to, signed off by you.</p></li>
    <li><b>Locked down</b><p>It reaches only what that job needs, and it can't pay anyone or send anything.</p></li>
    <li><b>Tested</b><p>It runs in shadow mode over your past records and goes live only at a pass mark you agree in writing.</p></li>
    <li><b>Watched</b><p>Every action is logged in your own accounts. We review it monthly and re-test before any change.</p></li>
  </ol>
</div></section>

<section class="sec dark" id="try"><div class="w">
  <p class="lab"><b>03</b>Free tools</p>
  <h2>Try it before you talk to anyone.</h2>
  <p class="lead">No sign-up, and nothing to install.</p>
  <div class="tools">{tl}</div>
</div></section>

<section class="sec" id="lead"><div class="w">
  <p class="lab"><b>04</b>Who leads Beiz</p>
  <div class="lead2">
    <img src="/assets/media/purav-mehta-2.jpg?v=43" alt="Purav Mehta" width="200" height="200" loading="lazy">
    <div><h3>Purav Mehta</h3><p class="c">Director · Chartered Accountant (CA ANZ) · GAICD</p>
    <p>Audit, controls and finance background. Purav designs the controls and signs off every system before it goes live. Beiz is named after his border collie, who doesn't stop until the job is done properly.</p></div>
    <a class="btn g" href="/about/">About Beiz</a>
  </div>
</div></section>

<section class="sec contact" id="contact"><div class="w">
  <div>
    <p class="lab"><b>05</b>Get in touch</p>
    <h2>Tell us what you're trying to fix.</h2>
    <p class="lead" style="margin-bottom:0">A written reply by the next business day, and a fixed-price proposal within three if it's a fit. If we're not the right fit, we'll say so.</p>
  </div>
  <div class="ways">
    <a href="{CALL_HREF}"{CALL_ATTR}><b>Book a 20-minute call</b><span>Early morning or after 5pm</span></a>
    <a href="/contact/#form"><b>Start in writing</b><span>A few lines is plenty</span></a>
    <a href="mailto:hello@beiz.com.au"><b>hello@beiz.com.au</b><span>Email</span></a>
  </div>
</div></section>
</main>
<footer><div class="w">
  <p>© 2026 Beiz Data &amp; Accounting Pty Ltd · ABN 53 691 755 496 · Canberra, ACT · <a href="/privacy/">Privacy</a> · <a href="https://www.linkedin.com/company/beiz-data-accounting/" rel="noopener">LinkedIn</a></p>
  <p>Beiz doesn't provide tax agent or BAS agent services, GST or BAS lodgements, tax advice, legal advice, financial product advice, or statutory audit and assurance services. We don't release payments without a person.</p>
  <p>Liability limited by a scheme approved under Professional Standards Legislation.</p>
</div></footer>
</body></html>'''
