"""Connected Intelligence homepage (approved by Purav 20 Oct 2026). site3.home() puts these sections inside the shared shell.
Graphite hero with a connected-system visual (Finance / Operations / AI views, synthetic), light sections below.
Business facts, prices and simulation labels come from the same sources as the live site."""
import json, re
from html import escape as e
from site3 import load, contact, SITE, BOOKING_URL

VIEWS = {
    "finance": {"label": "Finance", "sources": [("Invoices", "148 this month"), ("Timesheets", "1,206 hours"), ("Job records", "32 open jobs")],
                "steps": [("Validate", "3 invoices missing a job code", "held"), ("Reconcile", "hours ↔ invoices ↔ ledger", "ok"), ("Flag exceptions", "5 items for review", "held"), ("Request approval", "a person signs off", "person")],
                "outputs": [("Cash visibility", "Lowest week: week 7, $18.4k", "ok"), ("Job profitability", "3 jobs below target margin", "held"), ("Review queue", "5 items with reasons", "held")],
                "note": "Finance view: the numbers a business runs on, reconciled before anyone relies on them."},
    "operations": {"label": "Operations", "sources": [("Job app", "jobs marked complete"), ("Invoicing", "draft invoices"), ("Inbox", "supplier bills")],
                   "steps": [("Detect handoff gaps", "complete but not invoiced", "held"), ("Assign an owner", "named person per item", "ok"), ("Set a due date", "agreed turnaround", "ok"), ("Track to close", "until resolved", "ok")],
                   "outputs": [("Unbilled after completion", "2 jobs, 9+ days", "held"), ("Owner assigned", "every open item", "ok"), ("Complete to invoice", "average 4.2 days", "ok")],
                   "note": "Operations view: where work stalls between people and systems, and who closes it."},
    "ai": {"label": "AI", "sources": [("Bills", "PDFs and emails"), ("Bank transactions", "from the ledger"), ("Enquiries", "website form")],
           "steps": [("Extract fields", "AI reads the document", "ok"), ("Match and check", "fixed rules", "ok"), ("Draft a reply", "AI prepares it", "ok"), ("Approve", "a person decides", "person")],
           "outputs": [("Automated", "reading, matching, drafting", "ok"), ("Needs approval", "sending, paying, changing records", "held"), ("Logged", "every decision, with its reason", "ok")],
           "note": "AI view: what software does on its own, and what always waits for a person."},
}

CSS = """
@font-face{font-family:Inter;font-weight:400;font-display:swap;src:url(/assets/fonts/inter-latin-400-normal.woff2) format('woff2')}
@font-face{font-family:Inter;font-weight:500;font-display:swap;src:url(/assets/fonts/inter-latin-500-normal.woff2) format('woff2')}
@font-face{font-family:Inter;font-weight:600;font-display:swap;src:url(/assets/fonts/inter-latin-600-normal.woff2) format('woff2')}
@font-face{font-family:Mono;font-weight:400;font-display:swap;src:url(/assets/fonts/jetbrains-mono-latin-400-normal.woff2) format('woff2')}
@font-face{font-family:Mono;font-weight:500;font-display:swap;src:url(/assets/fonts/jetbrains-mono-latin-500-normal.woff2) format('woff2')}
:root{--g0:#0E1316;--g1:#141B1F;--g2:#1B2429;--gl:#2A353B;--gt:#ECF0EE;--gs:#AAB5B1;--em:#34C28F;--am:#F2B35B;
 --p:#F6F4EF;--card:#FFFFFF;--ink:#14191C;--soft:#4A525A;--line:#E1DED6;--emd:#17664A;--amd:#8A5208}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--p);color:var(--ink);font:400 17px/1.6 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}.w{max-width:1240px;margin:0 auto;padding:0 clamp(18px,4vw,40px)}
:focus-visible{outline:3px solid var(--em);outline-offset:3px;border-radius:4px}
.mono{font-family:Mono,ui-monospace,monospace;font-size:12.5px;letter-spacing:.04em}
.skip{position:absolute;left:-999px;top:8px;background:#fff;color:#000;padding:10px 14px;border-radius:8px;z-index:60}.skip:focus{left:12px}
.cbar{background:#F2B35B;color:#1a1200;font-size:13.5px;text-align:center;padding:6px 12px}
.cbar a{font-weight:600}
/* header */
.dark{background:var(--g0);color:var(--gt)}
.top{position:sticky;top:0;z-index:40;background:rgba(14,19,22,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--gl)}
.top .w{display:flex;align-items:center;gap:28px;min-height:68px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--gt);flex:none;font-size:16px}
.brand img{width:32px;height:32px}.brand b{font-weight:600}
.nav{display:flex;gap:4px;list-style:none;margin:0 0 0 auto;padding:0}
.nav a{display:block;padding:8px 12px;border-radius:8px;text-decoration:none;color:var(--gs);font-size:15px}
.nav a:hover{color:var(--gt);background:var(--g2)}
.nav .sep{color:var(--gl);padding:8px 2px}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:46px;padding:0 20px;border-radius:10px;font:500 15px Inter,sans-serif;text-decoration:none;border:1px solid transparent;cursor:pointer;transition:background .15s,border-color .15s}
.btn.em{background:var(--em);color:#06221A}.btn.em:hover{background:#4FD3A1}
.btn.ol{border-color:#46545B;color:var(--gt);background:transparent}.btn.ol:hover{border-color:var(--gt)}
.btn.ink{background:var(--ink);color:#fff}.btn.ink:hover{background:#2A3136}
.btn.lt{border-color:var(--ink);color:var(--ink)}
.top .btn{min-height:40px;padding:0 16px;font-size:14px}
.menu{display:none;margin-left:auto;background:none;border:1px solid var(--gl);color:var(--gt);border-radius:8px;padding:8px 13px;font:500 14px Inter,sans-serif}
/* hero */
.hero{padding:64px 0 72px;border-bottom:1px solid var(--gl);background:radial-gradient(1200px 500px at 85% 20%,rgba(52,194,143,.07),transparent 60%),var(--g0)}
.hero .w{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1.25fr);gap:44px;align-items:center}
.eyb{color:var(--em);margin:0 0 18px}
.hero h1{font:600 clamp(2rem,3.05vw,2.95rem)/1.1 Inter,sans-serif;letter-spacing:-.035em;margin:0 0 20px;text-wrap:balance}
.hero h1 span{display:block}.hero h1 .b{color:var(--em)}
.hero .l{color:var(--gs);font-size:1.08rem;margin:0 0 28px;max-width:34em}
.ctas{display:flex;gap:12px;flex-wrap:wrap}
/* system panel */
.sys{background:var(--g1);border:1px solid var(--gl);border-radius:16px;box-shadow:0 30px 80px rgba(0,0,0,.35);overflow:hidden}
.sys .hd{display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between;padding:12px 14px;border-bottom:1px solid var(--gl)}
.syn{color:var(--am)}
.tabs{display:flex;gap:4px;background:var(--g0);border:1px solid var(--gl);border-radius:10px;padding:3px}
.tabs button{font:500 14px Inter,sans-serif;color:var(--gs);background:none;border:0;border-radius:7px;padding:7px 14px;cursor:pointer}
.tabs button[aria-selected=true]{background:var(--g2);color:var(--gt);box-shadow:inset 0 0 0 1px var(--gl)}
.view{padding:18px 16px 16px}
.cols{display:grid;grid-template-columns:minmax(0,1fr) 36px minmax(0,1.15fr) 36px minmax(0,1fr);align-items:stretch}
.col{display:flex;flex-direction:column}.stack{flex:1;display:flex;flex-direction:column;justify-content:space-around;gap:8px}.stack .node{margin:0}
.col h3{font:500 11.5px Mono,monospace;letter-spacing:.08em;color:var(--gs);text-transform:uppercase;margin:0 0 10px}
.node{background:var(--g2);border:1px solid var(--gl);border-radius:10px;padding:10px 12px;font-size:14px}
.node b{display:block;color:var(--gt);font-weight:500}.node span{color:var(--gs);font-size:13px}
.wf{flex:1;display:flex;flex-direction:column;justify-content:space-around;background:#10171A;border:1px solid #2F5D4C;border-radius:12px;padding:12px}
.wf .st{display:flex;gap:10px;align-items:flex-start;padding:8px 2px;border-top:1px solid var(--gl);font-size:14px}
.wf .st:first-of-type{border-top:0}
.dot{flex:none;width:9px;height:9px;border-radius:50%;margin-top:6px;background:var(--em)}
.dot.held{background:var(--am)}.dot.person{background:var(--gt)}
.wf b{display:block;color:var(--gt);font-weight:500}.wf span{color:var(--gs);font-size:13px}
.out .node{border-left:3px solid var(--em)}.out .node.held{border-left-color:var(--am)}
.lk{position:relative}.lk svg{position:absolute;inset:28px 0 0;width:100%;height:calc(100% - 28px)}
.lk path{fill:none;stroke:#3A6E5B;stroke-width:1.5}
.view .nt{margin:12px 2px 0;color:var(--gs);font-size:13.5px}
.legend{display:flex;gap:16px;flex-wrap:wrap;margin-top:10px;color:var(--gs);font-size:12.5px}
.legend i{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px;vertical-align:middle}
@media (prefers-reduced-motion:no-preference){
 .lk path{stroke-dasharray:4 6}
 .view.on .lk path{animation:flow 1.6s linear 1}
 @keyframes flow{from{stroke-dashoffset:40}to{stroke-dashoffset:0}}
 .view.on .node,.view.on .st{animation:fade .45s ease-out both}
 @keyframes fade{from{opacity:.25}to{opacity:1}}
}
/* light sections */
.sec{padding:84px 0;border-top:1px solid var(--line)}
.sh{display:flex;flex-wrap:wrap;gap:12px 40px;align-items:end;justify-content:space-between;margin-bottom:32px}
.sh h2{font:600 clamp(1.7rem,2.8vw,2.4rem)/1.12 Inter,sans-serif;letter-spacing:-.025em;margin:0;max-width:20ch}
.sh p{margin:0;color:var(--soft);max-width:34em}
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.grid4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px;text-decoration:none;display:flex;flex-direction:column;transition:border-color .15s}
a.card:hover{border-color:var(--ink)}
.card .pr{font:500 13px Mono,monospace;color:var(--emd)}
.card h3{font:600 1.12rem/1.3 Inter,sans-serif;margin:10px 0 6px;letter-spacing:-.01em}
.card p{margin:0;color:var(--soft);font-size:15px;flex:1}
.tag{align-self:flex-start;display:inline-block;font:500 11.5px Mono,monospace;padding:2px 8px;border-radius:6px;background:#ECE9E2;color:var(--soft)}
.ctrls{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}
.ctrls span{font:500 13px Mono,monospace;border:1px solid var(--line);background:var(--card);border-radius:999px;padding:6px 12px}
.steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;counter-reset:s}
.steps li{counter-increment:s;border-top:2px solid var(--ink);padding-top:14px}
.steps li:before{content:"0" counter(s);font:500 12px Mono,monospace;color:var(--soft);display:block;margin-bottom:8px}
.steps b{display:block;font-weight:600;margin-bottom:4px}.steps p{margin:0;color:var(--soft);font-size:15px}
.nodo{margin:22px 0 0;color:var(--soft);font-size:15px}
.co{display:grid;grid-template-columns:1.2fr 1fr;gap:28px;align-items:start}
.facts{width:100%;border-collapse:collapse;font-size:15px}.facts th,.facts td{padding:10px 0;border-top:1px solid var(--line);text-align:left}
.facts th{font:500 12.5px Mono,monospace;color:var(--soft);width:38%}
.band{display:flex;flex-wrap:wrap;gap:18px;align-items:center;justify-content:space-between}
.cta{background:var(--g0);color:var(--gt);border-radius:18px;padding:clamp(26px,5vw,48px);display:flex;flex-wrap:wrap;gap:20px;align-items:center;justify-content:space-between}
.cta h2{font:600 clamp(1.6rem,2.6vw,2.2rem) Inter,sans-serif;margin:0 0 6px;letter-spacing:-.02em}.cta p{margin:0;color:var(--gs)}
footer{background:var(--g0);color:var(--gs);font-size:14px;padding:36px 0 44px;margin-top:84px}
footer .w{display:flex;flex-wrap:wrap;gap:12px 28px;justify-content:space-between}footer a{color:var(--gt)}
footer p{margin:6px 0 0}
@media (max-width:1100px){.hero .w{grid-template-columns:1fr}.grid4{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:980px){.nav,.top .navx{display:none}.menu{display:inline-flex}.top .w{flex-wrap:wrap}
 .nav.open{display:flex;flex-direction:column;width:100%;order:9;padding:6px 0 14px;margin:0}.nav.open .sep{display:none}}
@media (max-width:820px){.cols{grid-template-columns:1fr}.stack{gap:8px}.lk{height:22px}.lk svg{display:none}.lk:after{content:"↓";display:block;text-align:center;color:#3A6E5B;font-size:16px}
 .grid3,.co,.steps{grid-template-columns:1fr}.sec{padding:60px 0}}
@media (max-width:560px){.grid4{grid-template-columns:1fr}.hero{padding:40px 0 48px}.top .btn{display:none}.ctas .btn{flex:1 1 100%}
 .sys .hd{flex-direction:column;align-items:flex-start}.tabs{width:100%}.tabs button{flex:1}}
"""

JS = """document.documentElement.classList.add('js');
(function(){var b=document.querySelector('.menu'),n=document.getElementById('nav');b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});
var tabs=[].slice.call(document.querySelectorAll('[role=tab]')),views=[].slice.call(document.querySelectorAll('[role=tabpanel]'));
function sel(i,focus){tabs.forEach(function(t,j){var on=j===i;t.setAttribute('aria-selected',on);t.tabIndex=on?0:-1;views[j].hidden=!on;views[j].classList.toggle('on',on)});if(focus)tabs[i].focus()}
tabs.forEach(function(t,i){t.addEventListener('click',function(){sel(i)});t.addEventListener('keydown',function(ev){var k=ev.key,n2=tabs.length;
 if(k==='ArrowRight'){sel((i+1)%n2,true);ev.preventDefault()}if(k==='ArrowLeft'){sel((i-1+n2)%n2,true);ev.preventDefault()}if(k==='Home'){sel(0,true);ev.preventDefault()}if(k==='End'){sel(n2-1,true);ev.preventDefault()}})});
sel(0);})();"""


def connector(n_left, n_right, flip=False):
    """SVG curves from n_left node centres to n_right node centres (percent coordinates)."""
    ys = lambda n: [100 * (i + .5) / n for i in range(n)]
    paths = "".join(f'<path d="M0 {a:.1f} C 18 {a:.1f}, 18 {b:.1f}, 36 {b:.1f}"/>' for a in ys(n_left) for b in ys(n_right))
    return f'<div class="lk" aria-hidden="true"><svg viewBox="0 0 36 100" preserveAspectRatio="none">{paths}</svg></div>'


def view_html(key, v, first):
    src = "".join(f'<div class="node"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in v["sources"])
    steps = "".join(f'<div class="st"><i class="dot {c}" aria-hidden="true"></i><div><b>{e(a)}</b><span>{e(b)}</span></div></div>' for a, b, c in v["steps"])
    outs = "".join(f'<div class="node {c}"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b, c in v["outputs"])
    return (f'<div class="view" role="tabpanel" id="v-{key}" aria-labelledby="t-{key}" tabindex="0"{"" if first else ""}>'
            f'<div class="cols"><div class="col"><h3>Source systems</h3><div class="stack">{src}</div></div>{connector(3, 1)}'
            f'<div class="col"><h3>Beiz workflow</h3><div class="wf">{steps}</div></div>{connector(1, 3)}'
            f'<div class="col out"><h3>Business output</h3><div class="stack">{outs}</div></div></div>'
            f'<p class="nt">{e(v["note"])}</p></div>')


def _standalone(cat):
    sid = {s["id"]: s for s in cat["services"]}
    discuss = contact("Discovery call")
    caps = [("ai-agents", "AI agents & workflow automation"), ("dashboards", "Business intelligence & dashboards"), ("cash-model", "Financial modelling & scenarios"),
            ("data-engineering", "Data engineering & analytics"), ("ai-governance", "AI governance & controls"), ("cash-data-check", "Cash & data check")]
    services = "".join(f'<a class="card" href="/{sid[k]["slug"]}"><span class="pr">{e(sid[k]["price"])}</span><h3>{e(sid[k]["title"])}</h3><p>{e(sid[k]["summary"])}</p></a>' for k, _ in caps if k in sid)  # catalogue titles, same as /services/
    demos = [("/bill-check/", "Free tool", "Bill check", "Your own bills export, checked in your browser for possible duplicates and changed bank details. Nothing is uploaded."),
             ("/products-demos/ai-workflow/", "Simulation", "Enquiry to approved reply", "AI reads, rules check, a person decides."),
             ("/products-demos/enquiry-assistant/", "Simulation", "Enquiry assistant", "Answers from approved sources, or says it doesn't know."),
             ("/products-demos/missing-receipts/", "Simulation", "Missing receipts", "Reminders and matching, every send approved.")]
    dm = "".join(f'<a class="card" href="{h}"><span class="tag">{e(t)}</span><h3>{e(a)}</h3><p>{e(b)}</p></a>' for h, t, a, b in demos)
    tabs = "".join(f'<button role="tab" id="t-{k}" aria-controls="v-{k}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{e(v["label"])}</button>' for i, (k, v) in enumerate(VIEWS.items()))
    views = "".join(view_html(k, v, i == 0) for i, (k, v) in enumerate(VIEWS.items()))
    call = f'<a class="btn ol" href="{BOOKING_URL}" target="_blank" rel="noopener">Book a 20-minute call</a>' if BOOKING_URL else ""
    html = f'''<!doctype html>
<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Concept: Connected Intelligence | Beiz Data &amp; Accounting</title>
<meta name="robots" content="noindex"><meta name="theme-color" content="#0E1316"><link rel="icon" href="/assets/brand/beiz-icon.svg">
<style>{CSS}</style></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="cbar" role="note">Concept preview: "Connected Intelligence". Not live. <a href="/">Compare with the current homepage</a></div>
<header class="top dark"><div class="w">
 <a class="brand" href="/preview/ci/"><img src="/assets/brand/beiz-icon.svg" alt="" width="32" height="32"><span><b>Beiz</b> Data &amp; Accounting</span></a>
 <button class="menu" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
 <ul class="nav" id="nav" aria-label="Main"><li><a href="/services/">Services</a></li><li><a href="/products-demos/">Demos</a></li><li><a href="/about/">Company</a></li><li><a href="/insights/">Insights</a></li><li class="sep" aria-hidden="true">|</li><li><a href="/workshops-speaking/">Workshops &amp; Speaking</a></li></ul>
 <a class="btn em" href="{discuss}">Discuss your business</a>
</div></header>
<main id="main">
<section class="hero dark"><div class="w">
 <div>
  <p class="eyb mono">Chartered Accountant-led · Finance, governance, data and AI</p>
  <h1><span>AI agents, automation and business intelligence.</span> <span class="b">Built for your business.</span></h1>
  <p class="l">Beiz helps small businesses, startups and solo operators connect their data, automate repetitive work and make clearer financial decisions, combining financial judgement with AI engineering and data science.</p>
  <div class="ctas"><a class="btn em" href="#services">Explore services</a><a class="btn ol" href="/products-demos/ai-workflow/">Try the demo</a></div>
 </div>
 <div class="sys" aria-label="Example of a connected business system, synthetic data">
  <div class="hd"><span class="mono syn">Synthetic example · not a live integration</span><div class="tabs" role="tablist" aria-label="Choose a view">{tabs}</div></div>
  {views}
  <div class="legend" style="padding:0 16px 14px" aria-hidden="true"><span><i style="background:var(--em)"></i>ok</span><span><i style="background:var(--am)"></i>held for review</span><span><i style="background:var(--gt)"></i>a person decides</span></div>
 </div>
</div></section>

<section class="sec" id="services" aria-labelledby="h-s"><div class="w">
 <div class="sh"><h2 id="h-s">Services you can buy now.</h2><p>Scope, deliverables and price agreed in writing. Custom implementations are quoted after discovery.</p></div>
 <div class="grid3">{services}</div>
 <p class="nodo"><a href="/services/">All services</a> · <a href="/products-demos/">Free tools and pilots</a></p>
</div></section>

<section class="sec" aria-labelledby="h-d"><div class="w">
 <div class="sh"><h2 id="h-d">See the work before you talk to us.</h2><p>A free check that runs on your own bills export, and three simulations on synthetic data. Nothing is sent or connected.</p></div>
 <div class="grid4">{dm}</div>
</div></section>

<section class="sec" aria-labelledby="h-c"><div class="w">
 <div class="sh"><h2 id="h-c">How it's delivered, and what keeps it safe.</h2><p>Built in your own systems, tested on your past records, with a person approving anything that matters.</p></div>
 <ol class="steps"><li><b>Talk or write</b><p>A written reply by the next business day.</p></li><li><b>Fixed proposal</b><p>Price, timeline and definition of done within three business days.</p></li><li><b>Build and test</b><p>On your past records, alongside your team first.</p></li><li><b>Hand over</b><p>Documentation and a review once it's running.</p></li></ol>
 <div class="ctrls" aria-label="Controls on every build"><span>approval points</span><span>written limits</span><span>decision log</span><span>spending cap</span><span>off switch</span></div>
 <p class="nodo">Beiz doesn't provide tax or BAS agent services, statutory audit, legal or financial product advice, or payments released without a person.</p>
</div></section>

<section class="sec" aria-labelledby="h-co"><div class="w co">
 <div><h2 id="h-co" style="font:600 clamp(1.6rem,2.6vw,2.2rem) Inter,sans-serif;letter-spacing:-.02em;margin:0 0 12px">A finance and AI practice, founder-led.</h2>
 <p style="color:var(--soft)">Founded by a Chartered Accountant (CA ANZ) and graduate of the Australian Institute of Company Directors (GAICD), with a background in AI engineering and data science. We agree scope, delivery dates and capacity before work begins.</p>
 <p><a href="/about/">About Beiz</a> · <a href="/how-we-work/">How we work</a></p></div>
 <table class="facts"><tbody><tr><th scope="row">Legal name</th><td>Beiz Data &amp; Accounting Pty Ltd</td></tr><tr><th scope="row">ABN</th><td>53 691 755 496</td></tr><tr><th scope="row">GST</th><td>Not registered</td></tr><tr><th scope="row">Based in</th><td>Canberra, working Australia-wide</td></tr></tbody></table>
</div></section>

<section class="sec" aria-labelledby="h-w" style="padding:48px 0"><div class="w band">
 <div><h2 id="h-w" style="font:600 1.45rem Inter,sans-serif;margin:0 0 4px">Workshops, coaching and speaking</h2><p style="margin:0;color:var(--soft)">Practical sessions so your team can run more of it themselves.</p></div>
 <a class="btn lt" href="/workshops-speaking/">See sessions and topics</a>
</div></section>

<section aria-labelledby="h-e"><div class="w"><div class="cta">
 <div><h2 id="h-e">Discuss your business.</h2><p>A written reply by the next business day. If we're not the right fit, we'll say so.</p></div>
 <div class="ctas"><a class="btn em" href="{discuss}">Start in writing</a>{call}</div>
</div></div></section>
</main>
<footer><div class="w"><div>Beiz Data &amp; Accounting Pty Ltd · ABN 53 691 755 496 · Not registered for GST<p>Liability limited by a scheme approved under Professional Standards Legislation.</p></div>
<nav aria-label="Footer"><a href="/services/">Services</a> · <a href="/products-demos/">Demos</a> · <a href="/about/">Company</a> · <a href="/privacy/">Privacy</a> · <a href="/contact/">Contact</a></nav></div></footer>
<script>{JS}</script>
</body></html>'''
    return html


SKIP = re.compile(r"^(\*|html|body|a|\.w|:focus-visible|\.skip.*|\.cbar.*|\.top.*|\.brand.*|\.nav.*|\.menu|footer.*)$")


def _scope(css, pre=".ci"):
    """Prefix each selector with .ci; drop page-level rules (fonts, header, footer) that the shared shell owns."""
    out, i = [], 0
    while i < len(css):
        j = css.find("{", i)
        if j < 0:
            break
        sel = css[i:j].strip()
        depth, k = 1, j + 1
        while depth:
            depth += {"{": 1, "}": -1}.get(css[k], 0); k += 1
        inner = css[j + 1:k - 1]
        if sel.startswith("@font-face"):
            pass
        elif sel.startswith("@keyframes"):
            out.append(f"{sel}{{{inner}}}")
        elif sel.startswith("@media"):
            body = _scope(inner, pre)
            if body:
                out.append(f"{sel}{{{body}}}")
        else:
            parts = [p.strip() for p in sel.split(",")]
            keep = [pre if p == ":root" else f"{pre} {p}" for p in parts if not SKIP.match(p)]
            if keep:
                out.append(",".join(keep) + "{" + inner + "}")
        i = k
    return "\n".join(out)


def home_parts(cat):
    """(body, scripts) for the homepage: the concept's main sections, scoped CSS and the view-tab script."""
    html = _standalone(cat)
    main = html.split('<main id="main">', 1)[1].split("</main>", 1)[0]
    js = JS.replace("document.documentElement.classList.add('js');\n", "").replace(
        "var b=document.querySelector('.menu'),n=document.getElementById('nav');b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});\n", "")
    css = _scope(CSS) + "\n.ci{display:block;padding-bottom:84px;color:var(--ink)}.ci .w.band{padding:0 clamp(18px,4vw,40px)}"
    return f'<div class="ci">{main}</div>', f"<style>{css}</style><script>{js}</script>"
