"""Page content for beiz.com.au. Australian English, plain words. Published prices are "from" anchors only."""
import json
from layout import (SITE, page, phero, related, cta_band, contact_form, SERVICES, INDUSTRIES, CALL_HREF, CALL_ATTR)
from charts import cash13, job_margins, runway, runway_facts
from agents import CONSOLE, PIPELINE, WIRING, WATCH, FLOW, WATCH_HOME, AGENT_TEAM

PAGES = {}


def add(path, title, desc, body, extra_head=""):
    PAGES[path] = page(path, title, desc, body, extra_head)


def deliv(items):
    return '<ul class="deliv">' + "".join(f"<li><b>{b}</b>{t}</li>" for b, t in items) + "</ul>"


def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{t}</li>" for t in items) + "</ul>"


def before_after(title, before, after, k="A typical week"):
    return f'''<div class="scene"><span class="k">{k}</span><h3 style="margin-top:6px">{title}</h3>
  <div class="ba"><div class="b4"><b>Before</b><ul>{"".join(f"<li>{x}</li>" for x in before)}</ul></div>
  <div class="af"><b>After</b><ul>{"".join(f"<li>{x}</li>" for x in after)}</ul></div></div></div>'''


def aside(title, items, topic, note=None):
    href = "/contact/?topic=" + topic.replace(" ", "%20").replace("&", "%26") + "#form"
    n = f'<p class="fine">{note}</p>' if note else ""
    return f'<aside class="aside"><h3>{title}</h3>{ticks(items)}<a class="btn primary" href="{href}">Ask about this</a>{n}</aside>'


PLAIN = '''<section id="plain">
  <div class="wrap">
    <p class="eyebrow">In plain English</p>
    <h2>We're accountants who build the systems behind a business's money.</h2>
    <p class="lede">Most businesses run their finances across a dozen places: the accounting software, spreadsheets, the inbox, the bank, a job app. We connect those, add the checks an auditor would want, and give you a clear view of what's happening. Here's what that looks like.</p>
    <ol class="flow">
      <li><span class="k">01 · Today</span><h3>Your numbers are everywhere</h3>
        <div class="chips"><span>Xero or MYOB</span><span>Spreadsheets</span><span>Inbox</span><span>Bank feed</span><span>Job app</span><span>Receipts</span></div>
        <p>Someone copies data between them by hand, usually late at night.</p></li>
      <li><span class="k">02 · We build</span><h3>Connected, checked, logged</h3>
        <ul class="mini-log"><li><i class="ok">✓</i> 212 invoices matched</li><li><i class="ok">✓</i> Bank reconciled</li><li><i class="fl">!</i> New bank details, held for you</li><li><i class="ok">✓</i> Everything logged</li></ul>
        <p>Automation does the grunt work. A person signs off anything that matters.</p></li>
      <li><span class="k">03 · You see</span><h3>What matters, every Monday</h3>
        <div class="mini-mail"><b>Monday cash email</b><span>In the bank <em>$42,000</em></span><span>Owed to you <em>$31,400</em></span><span>Going out this week <em>$12,900</em></span><span class="w">Heads up: cash dips mid-November</span></div>
        <p>A short email, a live dashboard or a forecast you can trust.</p></li>
    </ol>
    <div class="explain">
      <div><b>"Which AI should we use?"</b><p>Whichever fits the job and the tools you already pay for: Copilot, Gemini, ChatGPT or Claude all have business versions that keep your data out of training. We're independent, so we recommend, set it up and train your team. We don't resell any of them.</p></div>
      <div><b>"What does GAICD mean?"</b><p>A graduate of the Australian Institute of Company Directors: trained in how boards govern a business and oversee risk. It's why we build AI with controls and sign-offs, not just speed.</p></div>
    </div>
    <p style="margin-top:22px"><a class="btn primary" href="/examples/">See example outputs</a></p>
  </div>
</section>'''


def home():
    body = f'''<div class="bz hx hz">
<section class="hz-hero dark" id="top"><div class="wrap hero32">
  <div class="hz-copy">
    <p class="bz-kick"><svg class="au-flag" viewBox="0 0 120 60" width="27" height="14" role="img" aria-label="Australian flag"><clipPath id="auS1"><rect width="60" height="30"/></clipPath><clipPath id="auT1"><path d="M30,15h30v15zv15h-30zh-30v-15zv-15h30z"/></clipPath><rect width="120" height="60" fill="#012169"/><g clip-path="url(#auS1)"><path d="M0,0L60,30M60,0L0,30" stroke="#fff" stroke-width="6"/><path d="M0,0L60,30M60,0L0,30" clip-path="url(#auT1)" stroke="#C8102E" stroke-width="4"/><path d="M30,0v30M0,15h60" stroke="#fff" stroke-width="10"/><path d="M30,0v30M0,15h60" stroke="#C8102E" stroke-width="6"/></g><g fill="#fff"><polygon points="30.00,36.00 31.74,41.40 37.04,39.39 33.90,44.11 38.77,47.00 33.13,47.49 33.90,53.11 30.00,49.00 26.10,53.11 26.87,47.49 21.23,47.00 26.10,44.11 22.96,39.39 28.26,41.40"/><polygon points="90.00,45.50 90.87,48.20 93.52,47.19 91.95,49.55 94.39,51.00 91.56,51.25 91.95,54.05 90.00,52.00 88.05,54.05 88.44,51.25 85.61,51.00 88.05,49.55 86.48,47.19 89.13,48.20"/><polygon points="75.00,24.50 75.87,27.20 78.52,26.19 76.95,28.55 79.39,30.00 76.56,30.25 76.95,33.05 75.00,31.00 73.05,33.05 73.44,30.25 70.61,30.00 73.05,28.55 71.48,26.19 74.13,27.20"/><polygon points="90.00,4.50 90.87,7.20 93.52,6.19 91.95,8.55 94.39,10.00 91.56,10.25 91.95,13.05 90.00,11.00 88.05,13.05 88.44,10.25 85.61,10.00 88.05,8.55 86.48,6.19 89.13,7.20"/><polygon points="102.50,19.50 103.37,22.20 106.02,21.19 104.45,23.55 106.89,25.00 104.06,25.25 104.45,28.05 102.50,26.00 100.55,28.05 100.94,25.25 98.11,25.00 100.55,23.55 98.98,21.19 101.63,22.20"/><polygon points="96.50,31.40 97.15,33.11 98.97,33.20 97.55,34.34 98.03,36.10 96.50,35.10 94.97,36.10 95.45,34.34 94.03,33.20 95.85,33.11"/></g></svg>Beiz Data &amp; Accounting<!--CA_HERO--></p>
    <h1><span>The Chartered Accountant</span> <span>who builds your AI workforce.</span> <span class="h1-2">Code. Financial models. Data. Governance. One Australian CA.</span></h1>
    <p class="hz-sub">Purav Mehta, Australian Chartered Accountant · GAICD, writes the code, builds the models and sets up the AI agents himself. An unchecked AI agent can pay the wrong bill, leak client data or miss a deadline, at scale and before anyone notices. Ours work inside limits you agree, a person approves what matters, and every action is traceable.</p>
    <div class="hz-ctas"><a class="btn primary" href="/contact/?topic=AI%20readiness%20%26%20governance#form" data-topic="AI readiness &amp; governance">Book a 20-minute sprint fit check</a><a class="btn ghost" href="#model-demo">Try the cash model</a></div>
    <p class="hz-alt">Or take the <a href="/workshop/">free 5-minute workshop</a> and leave with a written plan.</p>
  </div>
  <figure class="bmap" id="bmap" aria-label="How Beiz works across your business">
    <svg viewBox="0 0 560 470" role="group">
      <defs><marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#17201B"/></marker></defs>
      <g class="bm-lines" fill="none" stroke="#17201B" stroke-width="1.6">
        <path id="bl1" d="M280 70 C280 110 100 110 100 150"/><path id="bl2" d="M280 70 L280 150"/><path id="bl3" d="M280 70 C280 110 460 110 460 150"/>
        <path id="bl4" d="M100 222 C100 270 280 262 280 300" marker-end="url(#arw)"/><path id="bl5" d="M280 222 L280 300" marker-end="url(#arw)"/><path id="bl6" d="M460 222 C460 270 280 262 280 300" marker-end="url(#arw)"/>
        <path id="bl7" d="M280 372 L280 398" marker-end="url(#arw)"/>
      </g>
      <g class="bm-dots">
        <circle r="4" fill="#1E6B44"><animateMotion dur="3.2s" repeatCount="indefinite" begin="-0.4s"><mpath href="#bl4"/></animateMotion></circle>
        <circle r="4" fill="#1E6B44"><animateMotion dur="3.2s" repeatCount="indefinite" begin="-1.5s"><mpath href="#bl5"/></animateMotion></circle>
        <circle r="4" fill="#1E6B44"><animateMotion dur="3.2s" repeatCount="indefinite" begin="-2.6s"><mpath href="#bl6"/></animateMotion></circle>
      </g>
      <g class="bm-node bm-top"><rect x="190" y="22" width="180" height="48" rx="2"/><text x="280" y="52">Your business</text></g>
      <a href="#lineage" class="bm-node bm-go" data-cap="Your data: connected, cleaned and traced, so every number on a dashboard can be followed back to its source."><rect x="20" y="150" width="160" height="72" rx="2"/><text x="100" y="180" class="t1">Your data</text><text x="100" y="204" class="t2">Connect it</text></a>
      <a href="#model-demo" class="bm-node bm-go" data-cap="Your numbers: a live 13-week cash and job profit model you can question, with every assumption written down."><rect x="200" y="150" width="160" height="72" rx="2"/><text x="280" y="180" class="t1">Your numbers</text><text x="280" y="204" class="t2">Model it</text></a>
      <a href="#limits" class="bm-node bm-go" data-cap="Your work: AI agents that check bills, prepare admin and chase payments, each with a job description and limits."><rect x="380" y="150" width="160" height="72" rx="2"/><text x="460" y="180" class="t1">Your work</text><text x="460" y="204" class="t2">Automate it</text></a>
      <a href="#ca" class="bm-node bm-go bm-ca" data-cap="Checks and approvals: limits you agree, a person who approves what matters, and an Australian Chartered Accountant who designs the controls and reviews the work."><rect x="150" y="300" width="260" height="72" rx="2"/><text x="280" y="330" class="t1">Checks &amp; approvals</text><text x="280" y="354" class="t2">You approve. A CA reviews.</text><ellipse class="pen" cx="392" cy="306" rx="26" ry="16" transform="rotate(-8 392 306)"/><text x="392" y="312" class="pen-t">CA</text></a>
      <a href="#pricing" class="bm-node bm-go bm-end" data-cap="Better decisions: clearer cash, profit you can see by job, and less admin, at a fixed price agreed in writing."><rect x="180" y="400" width="200" height="48" rx="2"/><text x="280" y="430">Better decisions</text></a>
    </svg>
    <figcaption id="bmCap">Click any part of the map to try it.</figcaption>
  </figure>
</div></section>

<section class="hz-sec sp" id="sprint"><div class="wrap">
  <p class="demo-k">Start here</p>
  <h2>Your team is already using AI. Make it accountable.</h2>
  <p class="sp-line">Find every tool. Name an owner. Set the limit. Keep the evidence.</p>
  <p class="lede">The AI workflow &amp; controls sprint. In two weeks we find the AI tools your people actually use, what data goes into them and who owns each one. Then we set practical limits and pick the first workflow worth running under controls. It starts with short interviews and a list of tools. We don't need access to your ledger.</p>
  <ul class="sp5">
    <li><b>Tool register</b><span>What's in use, by whom and for what.</span></li>
    <li><b>Data map</b><span>Which customer, staff, financial or confidential data goes into each tool.</span></li>
    <li><b>Named owners</b><span>One accountable person for each use that matters.</span></li>
    <li><b>Use rules</b><span>Approved tools, data that never goes in, when a person must check and who to escalate to.</span></li>
    <li><b>90-day plan</b><span>The first controlled workflow, its owner, how it's measured and the next decision.</span></li>
  </ul>
  <div class="cv-foot"><p><b>Includes a Privacy Act check.</b> From 10 December 2026, some organisations covered by the Privacy Act must update their privacy policy when personal information is used in computer-assisted decisions that could significantly affect a person. We check whether that threshold looks relevant to you and draft wording for your lawyer to review. We don't give legal advice.</p><div class="cv-price"><span>Fixed price from</span><b>$3,500</b><span>two weeks, agreed in writing</span></div></div>
  <div class="hz-ctas"><a class="btn primary" href="/contact/?topic=AI%20readiness%20%26%20governance#form" data-topic="AI readiness &amp; governance">Book a 20-minute fit check</a><a class="btn ghost" href="#limits">Try setting an agent's limits</a></div>
</div></section>

<section class="diff" id="different"><div class="wrap">
  <h2>The AI is the same. The setup isn't.</h2>
  <p class="lede">Every firm can buy the same AI models we use. What makes a Beiz agent different is the rules it runs under. A human is always in the loop.</p>
  <ol class="diff4">
    <li><b>A written policy for every agent</b><span>What it may do, what it must never do, and the limit it stops at. Signed off by you before it goes live.</span></li>
    <li><b>Human approval, every time it matters</b><span>Payments, anything sent to a customer and any decision about a person wait for a named approver. No exceptions.</span></li>
    <li><b>Every action traceable</b><span>What the agent did, why, and who approved it, recorded in a log kept in your own accounts.</span></li>
    <li><b>Reviewed by an Australian Chartered Accountant</b><span>Decisions are reviewed and re-tested before any change goes live, against the policy you agreed.</span></li>
  </ol>
</div></section>

<section class="hz-sec xdemo" id="model-demo"><div class="wrap">
  <p class="demo-k">Your numbers · Model it</p>
  <h2>Make the decision before the cash runs out</h2>
  <p class="lede">A 13-week cash model for a made-up trade business. Move the sliders and watch the low point move. Every number can be opened up.</p>
  <div class="cm-grid">
    <div class="cm-ctl">
      <label>Customers on account pay in <output id="cmDelayV"></output><input type="range" id="cmDelay" min="7" max="90" step="1" value="45"></label>
      <label>Wages per fortnight <output id="cmWageV"></output><input type="range" id="cmWage" min="20000" max="60000" step="1000" value="32000"></label>
      <label>Sales growth per month <output id="cmGrowV"></output><input type="range" id="cmGrow" min="-15" max="25" step="1" value="5"></label>
      <div class="cm-fixed"><b>Held steady in this demo</b><span>Opening cash $50,000 · sales $48,000 a week: 60% paid within a week, 40% on account (30-day terms until now) · suppliers 40% of sales, paid after 30 days · overheads $6,000 a week · super 12% with each pay run · buffer $40,000</span></div>
    </div>
    <div class="cm-out">
      <div class="cm-kpis"><div><span>Lowest point</span><b id="cmLow"></b><small id="cmLowWk"></small></div><div><span>Weeks under buffer</span><b id="cmUnder"></b></div><div><span>Cash in week 13</span><b id="cmEnd"></b></div></div>
      <svg id="cmChart" viewBox="0 0 640 260" role="img" aria-label="13-week cash forecast"></svg>
      <p class="cm-why" id="cmWhy"></p>
      <button type="button" class="btn ghost" id="cmOpen" aria-expanded="false" aria-controls="cmBehind">Show me what sits behind this number</button>
    </div>
  </div>
  <div class="cm-behind" id="cmBehind" hidden>
    <div class="lg-scroll"><table class="cm-t" id="cmTable"></table></div>
    <div class="cm-notes"><div><b>How each week is calculated</b><span>Closing cash = opening cash + customer receipts − supplier payments − wages and super − overheads. 60% of each week's sales arrive the following week. Invoices already sent arrive on the old 30-day terms; new invoices on account arrive on the terms you set.</span></div><div><b>What this demo leaves out</b><span>GST and BAS, tax, loans, one-off costs and seasonality. A real model is built from your ledger with assumptions we agree and write down.</span></div></div>
  </div>
  <p class="nx">Not sure how close your own buffer is? <a href="#check">The two-week cash &amp; data check</a> works it out from your exports. $1,500 fixed.</p>
</div></section>

<section class="hz-sec xdemo" id="lineage"><div class="wrap">
  <p class="demo-k">Your data · Connect it</p>
  <h2>Follow the number back to where it came from</h2>
  <p class="lede">A dashboard is only as good as the records under it. Click the margin, then keep going until you reach the raw exports. Switch between the data as it arrived and after cleaning.</p>
  <div class="lnx" id="ln">
    <div class="ln-bar"><ol class="ln-steps" id="lnSteps"><li><button type="button" data-s="0">Dashboard</button></li><li><button type="button" data-s="1">Calculation</button></li><li><button type="button" data-s="2">Cleaned records</button></li><li><button type="button" data-s="3">Source data</button></li></ol>
      <div class="ln-sw" role="group" aria-label="Which data"><button type="button" data-v="raw">As it arrived</button><button type="button" data-v="clean" aria-pressed="true">After cleaning</button></div></div>
    <div class="ln-stage" id="lnStage" aria-live="polite"></div>
  </div>
  <p class="nx">Can't trace a number like this in your business? <a href="#check">Start with the cash &amp; data check.</a> Every finding comes with the records behind it.</p>
</div></section>

<section class="hz-sec xdemo" id="limits"><div class="wrap">
  <p class="demo-k">Your work · Automate it</p>
  <h2>AI without controls is a risk. AI with controls is a workforce.</h2>
  <p class="lede">Everyone talks about AI. Few understand its limits. AI agents don't fail quietly; they fail at scale. Here are five requests a payables agent might face in a week. You decide: allow it, hold it for a person, or block it. Then see what we'd set, and why. A simulation, not connected to any real accounts.</p>
  <div class="lm" id="lm"></div>
  <p class="nx">You just set the limits for one agent. <a href="#sprint">The controls sprint</a> does this for every AI tool your team already uses.</p>
</div></section>

<section class="hz-sec xdemo" id="trace"><div class="wrap">
  <p class="demo-k">How we work with you</p>
  <h2>Watch your project as it happens</h2>
  <p class="lede">No black box and no chasing us for news. You see the plan, a short update every Friday, and every action the agents took, with who approved it. A sample project:</p>
  <div class="tr" id="tr">
    <div class="tr-tabs" role="tablist"><button role="tab" aria-selected="true" data-t="plan">Project plan</button><button role="tab" aria-selected="false" data-t="upd">Friday update</button><button role="tab" aria-selected="false" data-t="act">Every action</button></div>
    <div class="tr-body" id="trBody"></div>
  </div>
</div></section>

<section class="hz-sec" id="ca"><div class="wrap ca-grid">
  <div>
    <p class="demo-k">Checks &amp; approvals</p>
    <h2>What an Australian Chartered Accountant adds</h2>
    <p class="lede">The agents do the matching. A Chartered Accountant designs the limits and asks the questions the software can't. Red ink below shows the kind of review notes we write.</p>
    <p class="au-line"><svg class="au-flag" viewBox="0 0 120 60" width="27" height="14" role="img" aria-label="Australian flag"><clipPath id="auS2"><rect width="60" height="30"/></clipPath><clipPath id="auT2"><path d="M30,15h30v15zv15h-30zh-30v-15zv-15h30z"/></clipPath><rect width="120" height="60" fill="#012169"/><g clip-path="url(#auS2)"><path d="M0,0L60,30M60,0L0,30" stroke="#fff" stroke-width="6"/><path d="M0,0L60,30M60,0L0,30" clip-path="url(#auT2)" stroke="#C8102E" stroke-width="4"/><path d="M30,0v30M0,15h60" stroke="#fff" stroke-width="10"/><path d="M30,0v30M0,15h60" stroke="#C8102E" stroke-width="6"/></g><g fill="#fff"><polygon points="30.00,36.00 31.74,41.40 37.04,39.39 33.90,44.11 38.77,47.00 33.13,47.49 33.90,53.11 30.00,49.00 26.10,53.11 26.87,47.49 21.23,47.00 26.10,44.11 22.96,39.39 28.26,41.40"/><polygon points="90.00,45.50 90.87,48.20 93.52,47.19 91.95,49.55 94.39,51.00 91.56,51.25 91.95,54.05 90.00,52.00 88.05,54.05 88.44,51.25 85.61,51.00 88.05,49.55 86.48,47.19 89.13,48.20"/><polygon points="75.00,24.50 75.87,27.20 78.52,26.19 76.95,28.55 79.39,30.00 76.56,30.25 76.95,33.05 75.00,31.00 73.05,33.05 73.44,30.25 70.61,30.00 73.05,28.55 71.48,26.19 74.13,27.20"/><polygon points="90.00,4.50 90.87,7.20 93.52,6.19 91.95,8.55 94.39,10.00 91.56,10.25 91.95,13.05 90.00,11.00 88.05,13.05 88.44,10.25 85.61,10.00 88.05,8.55 86.48,6.19 89.13,7.20"/><polygon points="102.50,19.50 103.37,22.20 106.02,21.19 104.45,23.55 106.89,25.00 104.06,25.25 104.45,28.05 102.50,26.00 100.55,28.05 100.94,25.25 98.11,25.00 100.55,23.55 98.98,21.19 101.63,22.20"/><polygon points="96.50,31.40 97.15,33.11 98.97,33.20 97.55,34.34 98.03,36.10 96.50,35.10 94.97,36.10 95.45,34.34 94.03,33.20 95.85,33.11"/></g></svg><span>Your agents work under Australian rules: the Privacy Act, GST and BAS, super and payroll. An Australian Chartered Accountant works under those rules every day and is bound by the APES 110 Code of Ethics.</span></p>
    <div class="ca-who"><img src="/assets/media/purav-mehta-2-160.jpg?v=43" alt="" width="64" height="64"><p><b>Purav Mehta, Australian Chartered Accountant · GAICD</b><br>Builds the data models and agents himself, with a background in internal audit, corporate finance and SAP systems. Canberra, working Australia-wide.</p></div><!--CA_WHO-->
    <p class="partner-line">Works alongside your accountant, or inside your firm. Beiz doesn&rsquo;t do tax, BAS or statutory audit work, so there&rsquo;s nothing to compete with.</p>
    <dl class="hz-four"><dt>CA</dt><dd>financial judgement and reconciliation</dd><dt>GAICD</dt><dd>governance, risk and what a board needs to see</dd><dt>Data</dt><dd>models, and where each number came from</dd><dt>AI</dt><dd>how the agents are set up and limited</dd></dl>
    <p><a class="textlink" href="/about/">More about Beiz</a></p>
  </div>
  <figure class="lg" id="dlog">
    <div class="lg-h"><b>Decision log</b><span>Sample records · illustrative review, not client work</span></div>
    <div class="lg-scroll"><table class="lg-t"><thead><tr><th>Time</th><th>Agent</th><th>Entry</th><th class="a">$</th><th class="s">Status</th></tr></thead>
    <tbody><tr class="lg-r st-log"><td class="t">08:55</td><td class="w">Bank agent</td><td class="x">41 bank lines matched to the ledger</td><td class="a"></td><td class="s"><em>Logged</em><svg class="pen-tick" viewBox="0 0 24 18" aria-hidden="true"><path d="M2 10 L8 16 L22 2"/></svg></td></tr><tr class="lg-r st-log"><td class="t">09:03</td><td class="w">Data scientist agent</td><td class="x">13-week forecast refreshed. Low point week 7</td><td class="a">52,000.00</td><td class="s"><em>Logged</em><svg class="pen-tick" viewBox="0 0 24 18" aria-hidden="true"><path d="M2 10 L8 16 L22 2"/></svg></td></tr><tr class="lg-r st-held"><td class="t">09:12</td><td class="w">Payables agent</td><td class="x">Quoll Electrical bill: <span class="pen-ring">22 h</span> billed, timesheet shows 14 h<span class="pen-note">Only 14 h recorded on the timesheet. Ask the supplier why. PM</span></td><td class="a">3,080.00</td><td class="s"><em>Held</em></td></tr><tr class="lg-r st-ok"><td class="t">09:20</td><td class="w">Payables agent</td><td class="x">6 bills matched to orders and deliveries</td><td class="a">7,412.60</td><td class="s"><em>Approved</em><svg class="pen-tick" viewBox="0 0 24 18" aria-hidden="true"><path d="M2 10 L8 16 L22 2"/></svg></td></tr><tr class="lg-r st-stop"><td class="t">09:31</td><td class="w">Payables agent</td><td class="x">Email asks to change a supplier's bank details<span class="pen-note">Never by email. Call them on the known number.</span></td><td class="a"></td><td class="s"><em>Blocked</em></td></tr><tr class="lg-r st-held"><td class="t">09:44</td><td class="w">Accounting agent</td><td class="x">Reminder drafted, invoice 30 days overdue</td><td class="a">4,350.00</td><td class="s"><em>Held</em></td></tr><tr class="lg-r st-held"><td class="t">10:02</td><td class="w">Reviewer agent</td><td class="x">Board pack figure not found in the ledger<span class="pen-note">Agree to the trial balance first.</span></td><td class="a"></td><td class="s"><em>Held</em></td></tr></tbody>
    <tfoot><tr><td colspan="5"><span id="dlCount"></span></td></tr></tfoot></table></div>
    <figcaption class="lg-f"><span class="pen-sig">Example review notes, P. Mehta CA</span><span>Red ink shows the kind of questions a Chartered Accountant asks. In your business the log sits in your own accounts.</span></figcaption>
    <p class="nx">Every agent we set up keeps a log like this. <a href="#ai">See AI workforce setup.</a></p>
  </figure>
</div></section>

<section class="hz-sec" id="cover"><div class="wrap">
  <p class="demo-k">Finance leave cover</p>
  <h2>Someone's going on leave. The work doesn't have to stop.</h2>
  <p class="lede">Parental leave, long service leave, a month in Europe. Bills still arrive, invoices still need to go out and someone has to watch the cash. We set up an agent to carry the routine part of their role, with an Australian Chartered Accountant reviewing its work, and hand everything back the day they return.</p>
  <ol class="cv">
    <li><b>Before they go</b><span>We shadow them for a week and write the agent's job description from how they actually do the work. They sign it off.</span></li>
    <li><b>While they're away</b><span>The agent matches bills, drafts invoices and reminders and keeps the reconciliation current. Anything unusual is held for a named person. You get a one-page update every Friday.</span></li>
    <li><b>When they're back</b><span>A handover note: what was done, what was held and what's waiting. The agent can stay on to help them, or be switched off.</span></li>
  </ol>
  <div class="cv-foot"><p><b>Their job stays theirs.</b> The agent covers routine work only. Decisions, customers and anything about people stay with your team. Best booked three to four weeks before the leave starts.</p><div class="cv-price"><span>Setup from</span><b>$3,500</b><span>then from $2,000 a month of cover</span></div></div>
  <div class="hz-ctas"><a class="btn primary" href="/contact/?topic=Discovery%20call#form" data-topic="Discovery call">Plan cover for someone's leave</a></div>
</div></section>

<section class="hz-sec" id="pricing"><div class="wrap">
  <h2>Prices, and how to start</h2>
  <p class="lede">Fixed prices, agreed in writing before we start. Prices are in Australian dollars. Beiz isn't registered for GST, so no GST is added.</p>
  <table class="hz-price">
    <thead><tr><th>Offer</th><th>What you get</th><th class="n">Price</th></tr></thead>
    <tbody>
      <tr id="sprint-row" class="start"><td><a href="#sprint">AI workflow &amp; controls sprint</a><small>Start here</small></td><td>Two weeks. A register of the AI tools your team uses, the data going into them, named owners, use rules and a 90-day plan for the first controlled workflow. Includes a check of whether the privacy-policy changes for computer-assisted decisions starting 10 December 2026 look relevant to you, with draft wording for your lawyer to review. No ledger access needed.</td><td class="n">from $3,500</td></tr>
      <tr id="check"><td><a href="/contact/?topic=Two-week%20cash%20%26%20data%20check#form">Two-week cash &amp; data check</a></td><td>From your Xero and job or timesheet exports: unbilled work, margin leaks and manual bottlenecks, with the records behind each finding. One business, up to 12 months of exports. You get a findings register, a two-page report and a 30-minute walkthrough. Doesn't include fixing the records, tax or BAS. Credited if you go ahead. <a class="hz-dl" href="/assets/beiz-sample-check-report.pdf">See a sample report (PDF)</a> <a class="hz-dl" href="/assets/beiz-sample-findings-register.xlsx">and its findings register (Excel)</a></td><td class="n">$1,500 fixed</td></tr>
      <tr id="model"><td><a href="/services/dashboards-and-models/">Live cash &amp; job profit model</a></td><td>A 13-week rolling cash flow and profit by job against what you quoted, updated weekly, in your own Excel or Power BI.</td><td class="n">from $5,000</td></tr>
      <tr id="ai"><td><a href="/services/ai-readiness-sprint/">AI workforce setup</a></td><td>Your first agent with its job description, limits and decision log, plus limits and approvers for the AI already inside your software. Each further agent is quoted in writing. Planned as a three-week rollout: map and limit, shadow mode, live within limits. Includes a review at day 30; ongoing monitoring is the monthly service below.</td><td class="n">from $8,500</td></tr>
      <tr><td><a href="#cover">Leave cover</a></td><td>An agent carries the routine part of a role while someone is on leave, reviewed by an Australian Chartered Accountant, with a handover note when they return.</td><td class="n">from $3,500 setup, then from $2,000 a month</td></tr>
      <tr><td>Monthly monitoring and review</td><td>We review the agents' decisions, re-test before changes, keep the model current and send you one page on what was caught and what changed.</td><td class="n">from $1,250 a month</td></tr>
    </tbody>
  </table>
  <div class="hz-ws">
    <div><h3>Confused by AI? We're not.</h3><p>Take the free 5-minute workshop: map your week, set your first agent's limits and leave with a written plan. Or apply for a seat at a live small-group session.</p></div>
    <div class="hz-ctas"><a class="btn primary" href="/workshop/">Take the workshop</a><a class="btn ghost" href="/workshop/#live">Join a live session</a></div>
  </div>
</div></section>
</div>
{contact_form(heading="Tell us what you're trying to fix", lede="A few lines is plenty. By the next business day you'll get a written reply: what the problem looks like, what information it would need, and whether a fixed-scope job makes sense. Rather talk? Pick “Discovery call” or “Demo request” and we'll arrange a free 20 minutes, early morning or after 5pm.")}'''
    add("/", "Beiz Data & Accounting | The Chartered Accountant who builds your AI workforce",
        "Beiz connects your data, models your cash and job profit, and sets up AI agents with limits and approvals. Led by Purav Mehta, Australian Chartered Accountant and GAICD. Fixed prices from $1,500.", body)

# ------------------------------------------------------------------ services
START_HERE = '''<section style="padding-top:8px"><div class="wrap"><p class="eyebrow">Start here</p><h2>Three ways to start, with fixed prices.</h2>
<div class="cards" style="margin-top:22px">
<a class="card" href="/#check"><span class="k">$1,500 fixed · credited if you go ahead</span><h3>Two-week cash &amp; data check</h3><p>From your Xero and job or timesheet exports, we find unbilled work, margin leaks and manual bottlenecks, with a fixed-price next step.</p><span class="go">About the check →</span></a>
<a class="card" href="/services/dashboards-and-models/"><span class="k">From $5,000</span><h3>Live cash &amp; job profit model</h3><p>A 13-week rolling cash flow and weekly job profitability your team can actually read.</p><span class="go">How the model works →</span></a>
<a class="card" href="/services/ai-readiness-sprint/"><span class="k">From $8,500</span><h3>AI workforce setup</h3><p>AI agents for supplier bills, quotes, reporting and admin, each with a job description and a person who approves anything touching money or customers.</p><span class="go">How the setup works →</span></a>
</div><p class="fine" style="margin-top:14px">Then monthly support from $1,250 a month, if you want it. Prices are confirmed in writing before work starts. Beiz isn't registered for GST, so no GST is added.</p></div></section>'''


def services_hub():
    cards = [
        ("/services/ai-governance/", "Govern", "AI governance & Privacy Act readiness", "Know what AI is in use, what it decides and who's accountable. Ready for 10 December 2026."),
        ("/services/human-in-the-loop/", "Oversee", "Offshore & AI oversight", "Outsourcing or using AI? We set up the access, review steps and checks, with an Australian CA in the loop."),
        ("/services/ai-agents/", "Adopt", "AI agents, chatbots & integration", "Not sure which AI to use? We pick it, build assistants and agents into your team's daily work, and train people to use them."),
        ("/services/automation/", "Build", "Workflow automation", "Accounts payable, month-end, reporting and admin, automated with approvals and an audit trail."),
        ("/services/data-engineering/", "Connect", "Data engineering", "Your systems connected, cleaned and flowing into one source your reports, models and AI can trust."),
        ("/services/dashboards-and-models/", "See", "Dashboards & financial models", "Cash forecasts, runway scenarios, job profitability and board or investor dashboards."),
        ("/services/project-delivery/", "Deliver", "AI & tech project delivery", "Scope, vendors, milestones and honest reporting, so your tech project actually lands."),
        ("/#sprint", "Start here", "AI workflow & controls sprint", "Find the AI your team uses, name owners, set limits and pick the first controlled workflow. Includes the Privacy Act check. From $3,500, two weeks."),
        ("/services/ai-readiness-sprint/", "Start here", "AI workforce setup", "AI agents with job descriptions, limits, a decision log and a person who approves what matters. Planned as a three-week rollout. From $8,500."),
        ("/services/quick-wins/", "Small business", "Quick wins", "Small, fixed-price fixes from $1,200 that give you back evenings and bring cash in faster. Built for sole traders and small teams who don't have time for admin. Most are scoped in days, not months, with no lock-in. Your BAS and tax stay with your tax or BAS agent; we make their job easier."),
    ]
    c = "".join(f'<a class="card" href="{h}"><span class="k">{k}</span><h3>{t}</h3><p>{d}</p><span class="go">Learn more →</span></a>' for h, k, t, d in cards)
    body = phero("Services", "What we build and fix.", "Every engagement is fixed price, agreed in writing, and ends with something your team can run. Pick the one closest to your problem, or tell us the problem and we'll pick.",
                 [("/services/", "Services")]) + START_HERE + f'<section style="padding-top:8px"><div class="wrap"><p class="eyebrow">Everything else</p><h2>Other fixed-price work.</h2><div class="cards" style="margin-top:22px">{c}</div></div></section>' + cta_band()
    add("/services/", "Services", "AI governance, automation, dashboards and financial models, tech project delivery and small business quick wins. Fixed price, in writing.", body)


FRAMEWORKS = '''<section id="frameworks"><div class="wrap">
  <p class="eyebrow">Frameworks we work to</p>
  <h2>Responsible AI isn't our invention. We just make it practical.</h2>
  <p class="lede">These are the public standards behind our AI policies, controls and sign-offs. Read them for free; we turn them into a one-page policy, an approved-tools list and a checklist your team actually uses.</p>
  <ul class="fwlist">
    <li><a href="https://www.industry.gov.au/publications/guidance-for-ai-adoption" rel="noopener"><b>Guidance for AI Adoption</b><span>National AI Centre, Australia. The government's practical starting point for businesses using AI.</span></a></li>
    <li><a href="https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-the-use-of-commercially-available-ai-products" rel="noopener"><b>Privacy and commercially available AI products</b><span>OAIC. What the Privacy Act expects when you put personal information into AI tools.</span></a></li>
    <li><a href="https://www.unesco.org/en/artificial-intelligence/recommendation-ethics" rel="noopener"><b>Recommendation on the Ethics of AI</b><span>UNESCO, adopted by 193 member states in 2021. The first global standard: human oversight, transparency, fairness, privacy.</span></a></li>
    <li><a href="https://www.nist.gov/itl/ai-risk-management-framework" rel="noopener"><b>AI Risk Management Framework</b><span>NIST, United States. Four functions, Govern, Map, Measure and Manage, that we use to structure each agent's risk register.</span></a></li>
    <li><a href="https://www.iso.org/standard/42001" rel="noopener"><b>ISO/IEC 42001</b><span>The international management-system standard for AI, for organisations that want to be audited against one.</span></a></li>
  </ul>
  <p class="fine">Links go to the publishers' own sites. We're not affiliated with or endorsed by any of them.</p>
</div></section>'''


def svc(path, crumb, eyebrow, h1, lede, prose, dl, side, scene, rel, topic, title, desc):
    body = (phero(eyebrow, h1, lede, [("/services/", "Services"), (path, crumb)]) +
            f'''<section style="padding-top:8px"><div class="wrap split"><div class="prose">{prose}<h2>What you get</h2>{deliv(dl)}{scene}{related(rel)}</div>{side}</div></section>''' +
            (FRAMEWORKS if path in ("/services/ai-governance/", "/services/ai-readiness-sprint/") else "") +
            cta_band(topic=topic))
    ld = {"@context": "https://schema.org", "@type": "Service", "name": h1, "serviceType": crumb, "description": desc,
          "url": SITE + path, "areaServed": {"@type": "Country", "name": "Australia"},
          "provider": {"@type": "ProfessionalService", "name": "Beiz Data & Accounting", "url": SITE + "/"}}
    add(path, title, desc, body, f'<script type="application/ld+json">{json.dumps(ld)}</script>')


def services():
    svc("/services/ai-governance/", "AI governance", "AI governance & Privacy Act readiness",
        "Know what your AI is doing before someone asks.",
        "Your staff are already using AI. Some of your software is already making decisions about customers. From 10 December 2026, if the Privacy Act covers you, your privacy policy has to say so. We find it, map it and put sensible controls around it.",
        '''<h2>The problem</h2>
<p>Most businesses can't answer three simple questions: which AI tools are in use, what data goes into them, and which of them make or shape decisions about people. Free tools get adopted quietly. Booking, lending, HR and pricing software ships with automated decisions built in. Nobody owns it.</p>
<p>That's a privacy risk, a reputational risk and, from December 2026, a disclosure obligation for businesses covered by the Privacy Act. It's also the first thing an investor, insurer or large customer will ask about.</p>
<h2>How we do it</h2>
<ol><li><strong>Find it.</strong> A short survey of your team and a review of your software and subscriptions. The free tools included.</li>
<li><strong>Map it.</strong> For each use: what data goes in, what comes out, what it decides, and what could go wrong.</li>
<li><strong>Control it.</strong> Practical rules people will actually follow, human sign-off where outcomes matter, and a named owner.</li>
<li><strong>Report it.</strong> A one-page view for the board or owner, and plain-English wording describing your automated decisions, for your privacy policy. Your lawyer confirms the final policy where needed.</li></ol>''',
        [("AI register", "Every tool in use, what data it touches, and its risk rating."), ("Automated-decision map", "Which systems decide or shape outcomes for people."),
         ("AI use policy", "Two pages your team will read, not twenty they won't."), ("Controls", "Sign-offs, limits and logging where they matter."),
         ("Privacy policy wording", "Plain-English description of your automated decisions."), ("Board or owner paper", "One page: where you stand and what to do next.")],
        aside("Good fit if", ["You're covered by the Privacy Act, or not sure", "Staff use ChatGPT, Copilot or Gemini", "A board, investor or big customer is asking about AI", "You want AI, just not the headline"], "AI readiness & governance",
              "Not legal advice. We work alongside your lawyer where the law needs interpreting."),
        before_after("A 40-person services firm", ["Nine AI tools in use, three approved", "Client data pasted into a free chatbot", "Privacy policy silent on automation", "Board asks, nobody can answer"],
                     ["One register, owned by the COO", "Business-grade tools only, training switched off", "Automated decisions described in plain English", "One-page board paper each quarter"], "Illustrative example, not a client"),
        [("/ai-check/", "Free 2-minute Privacy Act check"), ("/insights/privacy-act-automated-decisions/", "The new rule in plain English"), ("/services/ai-readiness-sprint/", "AI workforce setup")],
        "AI readiness & governance", "AI governance & Privacy Act readiness",
        "AI register, automated-decision mapping, AI use policy, controls and board reporting, ready for the Privacy Act automated-decision rules from 10 December 2026.")

    svc("/services/human-in-the-loop/", "Human in the loop", "Offshore & AI oversight",
        "Outsource with confidence. Keep an Australian CA in the loop.",
        "Offshore teams and AI tools are a smart way to get more done for less. They work best with clear instructions, the right access and someone here checking the result. We set that up, and can stay on as your reviewer.",
        '''<h2>Where it usually goes wrong</h2>
<p>Rarely in the work itself. Usually at the handover: instructions that live in someone's head, a shared login with more access than the job needs, and nobody checking the output until something has already gone out the door.</p>
<p>There's an obligation too. If the Privacy Act covers your business and you send personal information overseas, you generally stay accountable for how it's handled there. The same care applies to what goes into AI tools.</p>
<h2>How we do it</h2>
<ol><li><strong>Map the work.</strong> What goes offshore or to AI, what data it touches, and what must stay with you, like approving payments.</li>
<li><strong>Set the access.</strong> Each person gets their own login with only the access the job needs. Nothing shared by email, and a clear way to remove access when someone leaves.</li>
<li><strong>Build the checks.</strong> Review steps, owner sign-off where money moves, numbers tied back to the bank and ledger, and a log of who did what.</li>
<li><strong>Write it down.</strong> A short runbook for your team and the offshore staff, plus the points to cover in your contract and privacy policy. Your lawyer confirms the final wording.</li>
<li><strong>Stay on, if you like.</strong> A monthly sample check by a Chartered Accountant, with a one-page note on what we found.</li></ol>''',
        [("Work map", "What's outsourced or automated, and what stays with you."), ("Access plan", "Who can see and change what, in each system."),
         ("Review checklist", "The checks that happen before work is used or sent."), ("Runbook", "Plain instructions your team and offshore staff can follow."),
         ("Contract and privacy points", "What to raise with your provider and your lawyer."), ("Monthly review (optional)", "Sample checks and a one-page note.")],
        aside("Good fit if", ["You use an offshore bookkeeper, VA or admin team", "You're about to outsource and want it set up right", "Staff use AI on customer or financial data", "You want an Australian Chartered Accountant overseeing the work"], "Offshore & AI oversight",
              "Not an audit or assurance engagement, and not legal advice."),
        before_after("A 15-person trades business with an offshore bookkeeper", ["One shared login to Xero and the bank", "Bookkeeper can pay bills and change supplier bank details", "Nobody checks the reconciliations", "Customer data sent to personal email"],
                     ["Own login with read-and-draft access", "Owner approves payments and bank-detail changes", "Monthly sample check by a CA", "Work stays in the business's own accounts"], "Illustrative example, not a client"),
        [("/services/ai-governance/", "AI governance & Privacy Act readiness"), ("/services/automation/", "Workflow automation"), ("/faq/", "FAQ")],
        "Offshore & AI oversight", "Offshore & AI oversight: human in the loop",
        "Set up offshore teams and AI tools with the right access, review steps and checks, overseen by an Australian Chartered Accountant.")

    svc("/services/automation/", "Agents & automation", "Agents & automation",
        "Let the machine do the grunt work. Keep the judgement.",
        "We automate the repetitive parts of finance and admin: matching, chasing, checking, reporting. Every build has approvals, limits and a log, so nothing important happens without a person saying yes.",
        '''<h2>What we automate</h2>
<ul><li><strong>Accounts payable:</strong> invoices matched to orders, duplicates caught, changed bank details held, anything over your limit routed for approval.</li>
<li><strong>Getting paid:</strong> quotes turned into invoices the day the job finishes, polite reminders with a pay-now link, a weekly list of who owes what.</li>
<li><strong>Month-end:</strong> data pulled, reconciliations run, checks done, exceptions listed for a human.</li>
<li><strong>Reporting:</strong> the pack builds itself; your time goes on the commentary.</li>
<li><strong>Inbox and documents:</strong> triage, chasing missing paperwork, filing, with a record of who sent what.</li>
<li><strong>Assistants:</strong> a website or internal assistant that answers the same questions, inside limits you set.</li></ul>
<h2>How we keep it safe</h2>
<p>We design every automation the way an auditor would test it. It works inside your own accounts wherever possible. It has the same delegation limits your staff have. It writes every action to a log. And it stops and asks when something looks unusual, instead of guessing.</p>
<p>We use the tools that fit what you already own: Xero, MYOB, Microsoft 365, Google Workspace and business-grade AI with training on your data switched off.</p>''',
        [("Working automation", "Built and tested on your real data."), ("Controls", "Approvals, limits and exception rules."), ("Audit trail", "Every action logged: what, when, why, who approved."),
         ("Runbook", "What it does, what to do when it stops."), ("Training", "Short, recorded, for the people who'll use it."), ("Handover", "It's yours: your accounts, your data, your logins.")],
        aside("Typical builds", ["Quick wins: days", "Single process: 2 to 4 weeks", "Multi-step agent: 4 to 8 weeks", "Fixed price, agreed in writing"], "Automation & AI agents"),
        before_after("Accounts payable, 400 invoices a month", ["Two days a month keying and matching", "A duplicate payment every quarter", "Bank detail changes by email, unchecked", "No record of who approved what"],
                     ["Matching done overnight", "Duplicates flagged before payment", "Changed bank details held until verified by phone", "Every approval logged"], "Illustrative example, not a client"),
        [("/examples/", "See a sample control log"), ("/services/quick-wins/", "Small business quick wins"), ("/how-we-work/", "How we protect you")],
        "Automation & AI agents", "Agents & automation for finance",
        "AI agents and finance automation with approvals, delegation limits and a full audit trail: accounts payable, invoicing, month-end, reporting and admin.")

    svc("/services/ai-agents/", "AI agents & chatbots", "AI agents, chatbots & integration",
        "AI that works with your team, not around it.",
        "Chatbots that answer from your own information, assistants that draft and check, and agents that handle routine steps across your tools. Each one has limits, a log and a person who signs off.",
        '''<h2>Which AI should we use?</h2>
<p>It's usually the first question, and the honest answer depends on what you already pay for and what the job is. Microsoft 365 Copilot, Google Gemini, ChatGPT and Claude all have business versions that keep your data out of training. We look at your tools, your data and your budget, and recommend the smallest setup that does the job. We don't resell any of them.</p>
<h2>What we build</h2>
<ul><li><strong>Website and customer chatbots</strong> that answer from your own pages, policies and FAQs, say "I don't know" when they don't, and hand over to a person.</li>
<li><strong>Internal assistants</strong> that find answers in your procedures, contracts and past work, so staff stop asking the same questions.</li>
<li><strong>Drafting and checking:</strong> quotes, emails, reports and summaries drafted for a person to approve.</li>
<li><strong>Agents</strong> that carry routine steps across your tools: read the email, update the job, draft the invoice, ask for approval.</li></ul>
<h2>Bringing your team along</h2>
<p>AI only speeds you up if people use it. We set simple rules for what goes in, train your team on real examples from their own work, and measure the time saved, so you know it's working.</p>
<h2>How we keep it safe</h2>
<p>Business-grade tools with training on your data switched off. Each assistant sees only what it needs. Anything that sends, pays or changes a record waits for a person. Every action is logged.</p>''',
        [("Tool recommendation", "Which AI fits your business and budget, and why."), ("Working assistant or agent", "Built on your own information and tested on real questions."), ("Guardrails", "What it can see, what it can do, when it must ask."),
         ("Team training", "Short sessions using your team's own work."), ("Usage rules", "One page on what staff can and can't put into AI."), ("Measured results", "Time saved, questions answered, errors caught.")],
        aside("Good fit if", ["You don't know which AI to use", "Staff already use free AI tools", "The same questions get asked every day", "You want speed without losing control"], "Automation & AI agents"),
        before_after("A 15-person trades business", ["Office answers the same 30 questions by phone", "Quotes typed from scratch", "Staff pasting customer details into free tools", "No idea if AI saves any time"],
                     ["Website assistant answers the common ones and hands over the rest", "Quotes drafted from past jobs, checked by a person", "One approved business AI tool, with rules", "Hours saved reported monthly"], "Illustrative example, not a client"),
        [("/services/automation/", "Workflow automation"), ("/services/ai-governance/", "AI governance"), ("/services/ai-readiness-sprint/", "AI workforce setup")],
        "Automation & AI agents", "AI agents, chatbots & AI integration",
        "Not sure which AI to use? We pick the right tool, build chatbots, assistants and agents into your team's work, and train your people, with limits, logs and human sign-off.")

    svc("/services/data-engineering/", "Data engineering", "Data engineering",
        "One version of the numbers.",
        "Your data lives in Xero, a CRM, a job app, a POS and a few spreadsheets. We connect it, clean it and keep it flowing, so your dashboards, models and AI all work from the same trusted information.",
        '''<h2>The problem</h2>
<p>Every report starts with someone copying and pasting. Revenue means three different things in three systems. Nobody trusts the numbers enough to act on them, and any AI you add just repeats the mess faster.</p>
<h2>What we do</h2>
<ol><li><strong>Map it.</strong> Every system, what it holds, who owns it, and where the numbers disagree.</li>
<li><strong>Define it.</strong> A plain-English data dictionary: what each number means and where it comes from.</li>
<li><strong>Connect it.</strong> Automated pipelines that pull data from your tools on a schedule, with checks that flag missing or odd records.</li>
<li><strong>Serve it.</strong> One clean source that your dashboards, models and AI assistants all use.</li></ol>
<h2>Right-sized tools</h2>
<p>We use what fits your size, usually tools you already pay for, and a simple database or your existing SharePoint or Google Drive where that's enough. No platform you don't need.</p>
<h2>What gets in the way (we'll tell you upfront)</h2>
<ul><li><strong>Messy source data.</strong> Unreconciled accounts, duplicate customers and bills that never get entered. A pipeline moves data faster; it doesn't make it right. Clean-up comes first, and we'll say if it's a bigger job than the build.</li>
<li><strong>Systems that don't talk.</strong> Some software has no proper connection, or limits how much you can pull. Then the honest answer is a scheduled export, not a fragile workaround.</li>
<li><strong>Things change.</strong> Vendors update their systems and pipelines break. Every build has alerts when a run fails and a runbook for fixing it, and keeping it running is a small, ongoing job, not set-and-forget.</li>
<li><strong>Where data lives.</strong> Some cloud tools store data overseas. If your data needs to stay in Australia, we host it here, and that's decided before we build, not after.</li>
<li><strong>AI isn't a calculator.</strong> AI can read, sort and summarise. The numbers themselves come from your systems and are checked by a person, never made up by a model.</li></ul>''',
        [("Data map", "Every system and how they connect."), ("Data dictionary", "What each number means, its source and its owner."), ("Automated pipelines", "Scheduled, with checks and alerts."),
         ("Clean data store", "One source for reports, models and AI."), ("Quality checks", "Missing, duplicate and odd records flagged."), ("Runbook", "What runs when, and what to do if it stops.")],
        aside("Good fit if", ["Reports start with copy and paste", "Systems disagree about the same number", "You want AI, but your data isn't ready", "You're outgrowing spreadsheets"], "Dashboards & analytics"),
        before_after("A multi-site hospitality group", ["Sales in the POS, wages in payroll, costs in Xero", "Weekly report built by hand every Monday", "Three versions of revenue", "Nobody trusts the numbers"],
                     ["All three connected nightly", "Weekly report ready by 6am Monday", "One agreed definition of revenue", "Owners act on the numbers"], "Illustrative example, not a client"),
        [("/services/dashboards-and-models/", "Dashboards & financial models"), ("/services/automation/", "Workflow automation"), ("/services/ai-agents/", "AI agents & chatbots")],
        "Dashboards & analytics", "Data engineering & integration",
        "Data engineering for Australian businesses: Xero, CRM, POS and spreadsheets connected, cleaned and flowing into one trusted source for dashboards, models and AI.")

    rf = runway_facts()
    svc("/services/dashboards-and-models/", "Dashboards & models", "Dashboards & financial models",
        "See next month, not just last month.",
        "Live dashboards and financial models built from your own data: cash forecasts that warn you early, profitability by job or client, runway scenarios and the investor metrics people actually check.",
        f'''<h2>What we build</h2>
<ul><li><strong>13-week cash forecast:</strong> the cash visibility of a part-time CFO, without the CFO cost. Refreshed from your ledger and bank, with an early warning when cash will dip below your buffer. Built for Payday Super timing: since 1 July 2026, super goes out with each pay run rather than quarterly, so the cash leaves sooner.</li>
<li><strong>Profitability by job, client or service:</strong> find out what actually makes money while there's still time to change it.</li>
<li><strong>Runway and scenario models:</strong> what does a new hire, a bigger ad budget or an expensive AI tool do to your cash over 6, 12 and 24 months?</li>
<li><strong>Investor and board metrics:</strong> MRR, churn, CAC payback, gross margin and runway, calculated the same way every month.</li>
<li><strong>Business cases and pricing models:</strong> clear assumptions, scenarios and sensitivity, documented well enough for a lender or auditor.</li></ul>
<h2>Why accountants build better models</h2>
<p>A model is only as good as the numbers feeding it. We reconcile the inputs back to the ledger, document every assumption, and build it so your team can update it without breaking it. In the sample runway model on our examples page, the base case runs out of cash in month {rf["Base"]} and the worst case in month {rf["Worst"]}. That's the conversation a founder needs to have now, not at month {rf["Worst"] - 1}.</p>''',
        [("Dashboard or model", "Power BI, Excel or Google Sheets, whichever you'll actually use."), ("Data connections", "Pulled from your ledger and systems, not retyped."), ("Assumptions log", "Every number explained and sourced."),
         ("Scenarios", "Best, base and worst, with the drivers you can change."), ("Walkthrough", "A recorded explanation of how to read and update it."), ("Refresh routine", "Weekly or monthly, automated where possible.")],
        aside("Good fit if", ["You find out about cash problems too late", "Investors or the bank want numbers you can defend", "You're deciding on a hire, a loan or a big spend", "Your spreadsheet has become fragile"], "Dashboards & analytics"),
        before_after("A growing agency", ["Cash checked by logging into the bank", "Forecast in a spreadsheet only the founder understands", "Board pack takes three days", "Hiring decisions made on gut feel"],
                     ["Monday cash email with a 13-week view", "Model the team can update safely", "Board pack refreshes itself", "Every hire tested against runway first"], "Illustrative example, not a client"),
        [("/examples/", "See sample charts"), ("/industries/startups/", "For startups & tech agencies"), ("/industries/trades/", "For trades & construction")],
        "Dashboards & analytics", "Dashboards & financial models",
        "13-week cash forecasts, runway and scenario models, job profitability and investor metrics, built from your own data and reconciled to the ledger. The cash visibility of a part-time CFO, without the CFO cost.")

    svc("/services/project-delivery/", "Project delivery", "AI & tech project delivery",
        "Tech projects that land on time and actually get used.",
        "Bought new software and it's not sticking? About to sign with a vendor? Stuck with a developer who's gone quiet? We run the project for you: scope, vendors, milestones, risks and honest written reporting.",
        '''<h2>Why tech projects go wrong</h2>
<p>It's rarely the technology. It's a fuzzy scope, nobody owning the vendor, and reporting that says "on track" right up until it isn't. Small businesses feel this most, because there's no project office to catch it.</p>
<h2>What we do</h2>
<ul><li><strong>Before you sign:</strong> turn what you want into a clear written scope, compare vendors on the same terms, and flag the commercial risks for your lawyer to look at.</li>
<li><strong>During delivery:</strong> milestones, a risk and issue log, weekly written status, and someone who holds the vendor to what was agreed.</li>
<li><strong>Stalled projects:</strong> an honest health check, a reset plan in writing, and a decision on what to keep.</li>
<li><strong>After go-live:</strong> adoption, training and checking the benefits you were promised actually turn up.</li></ul>
<p>We bring large-portfolio project management experience, sized down for an owner-run business. No jargon, no 40-page status reports.</p>''',
        [("Written scope", "What's in, what's out, what done looks like."), ("Vendor comparison", "Like for like, with the risks spelled out."), ("Plan & milestones", "Realistic dates you can hold people to."),
         ("Risk & issue log", "Kept current, not filled in after the fact."), ("Weekly status", "One page, in plain English, every week."), ("Benefits check", "Did it deliver what was promised?")],
        aside("Good fit if", ["You're about to buy software or hire a developer", "A project is late, over budget or stuck", "Nobody internally has time to run it", "You want someone on your side of the table"], "Tech project delivery"),
        before_after("A clinic changing booking systems", ["Vendor chosen from a demo", "No data migration plan", "Go-live date slipped twice", "Staff still using the old system"],
                     ["Scope and migration signed off in writing", "Weekly status against milestones", "Go-live on the agreed date", "Training done, old system switched off"], "Illustrative example, not a client"),
        [("/insights/burned-by-an-ai-product/", "Burned by a developer? Start here"), ("/services/automation/", "Agents & automation"), ("/how-we-work/", "How we work")],
        "Tech project delivery", "AI & tech project delivery",
        "Project delivery for AI and technology projects: scoping, vendor comparison, milestones, risk logs and plain-English status reporting. Rescue for stalled projects.")

    svc("/services/ai-readiness-sprint/", "AI workforce", "AI workforce setup",
        "Your AI workforce, set up properly, on a three-week rollout plan.",
        "We set up AI agents that do real finance and admin work inside the tools you already use: a data scientist agent, an accounting agent, a reviewer agent and a governance agent. Each one has a job description, limits and a person it reports to. We also set the limits, approvers and decision log for the AI already inside your software, like Xero and Microsoft 365. Then we keep them all in check every month.",
        '''<h2>The agents</h2>
<ul><li><strong>Data scientist agent:</strong> forecasts cash for the next 13 weeks, spots margin drift by job, and flags what's unusual.</li>
<li><strong>Accounting agent:</strong> reconciles transactions, matches bills to orders and deliveries, and drafts invoices and reminders.</li>
<li><strong>Reviewer agent:</strong> traces figures back to the ledger and holds anything it can't trace for a person to check.</li>
<li><strong>Governance agent:</strong> keeps the decision log, the register of AI in use and the monthly board or owner report.</li></ul>
<p>You don't need all four on day one. Most businesses start with the one or two that save the most hours, and add the rest once those are working.</p>
<h2>Five controls every agent gets</h2>
<ol><li><strong>A named role and owner.</strong> A written job description: what the agent does, the tools it may use, and the person it reports to.</li>
<li><strong>Limits it can't cross.</strong> Read-only access where possible, and a delegation limit. Changed bank details, new suppliers and anything over the limit always go to a person.</li>
<li><strong>Human checkpoints.</strong> Anything that moves money, reaches a customer or decides something about a person waits for a human yes.</li>
<li><strong>A log of every decision.</strong> What the agent did, why, and who approved it, kept in your own accounts.</li>
<li><strong>Monthly monitoring and review.</strong> We read the log, check for drift and errors, and adjust the limits. Rules like the Privacy Act's automated-decision disclosures are covered as they apply to you.</li></ol>
<h2>How it runs</h2>
<ol><li><strong>Week 1, map and limit:</strong> we list the repetitive work, pick the agents worth having, and write each job description with you.</li>
<li><strong>Week 2, shadow mode:</strong> the agents run alongside your team without acting. We compare their answers with yours.</li>
<li><strong>Week 3, live within limits:</strong> the agents start work. Anything over a limit comes to a person.</li>
<li><strong>Day 30, review:</strong> errors, time saved and exceptions, measured. We fix what isn't working and tell you plainly whether to add more.</li></ol>
<h2>What it isn't</h2>
<p>It isn't an audit or assurance engagement, custom software that needs a development team, or a licence sale. You buy any subscriptions directly, in your name. We don't do tax returns or BAS.</p>''',
        [("Agent job descriptions", "Role, tools, limits and owner for each agent, agreed with you."), ("Working agents", "Built in your own accounts and tools."), ("Approval steps", "Money, customers and people always need a human yes."),
         ("Decision log", "Every action recorded, in your accounts."), ("AI use policy and training", "One page your team can follow, plus a session on the agents."), ("Day-30 review", "Errors, time saved and exceptions, measured.")],
        aside("The fine print", ["Setup from $8,500, fixed and quoted in writing", "Three-week rollout plan, subject to scope and system access", "Monthly monitoring and review from $1,250", "Built in your accounts. No lock-in."], "AI workforce setup"),
        "", [("/services/ai-governance/", "AI governance"), ("/services/automation/", "Workflow automation"), ("/#wrong", "What goes wrong without controls")],
        "AI workforce setup", "AI workforce setup: AI agents with a Chartered Accountant in the loop",
        "Fixed-price AI workforce setup for Australian businesses: data scientist, accounting, reviewer and governance agents with job descriptions, limits, a decision log and monthly review. From $8,500.")

    quick = [("Invoices that chase themselves", "Automatic reminders and pay-now links, so you stop ringing late payers."),
             ("Quote to invoice, automatically", "Finished jobs get invoiced the same day, not three weeks later."),
             ("Xero health check", "Bank rules fixed, duplicates cleaned up, reconciliation back on track."),
             ("Which jobs actually make money", "A simple profitability view by job, client or service."),
             ("Your Monday cash email", "One short email each week: cash in the bank, what's owed, what's due."),
             ("Duplicate & price-creep check", "Catch bills paid twice and suppliers quietly putting prices up."),
             ("Receipts, sorted", "Snap and forget. Receipts captured and matched without the shoebox."),
             ("A website assistant", "Answers the same customer questions for you, with limits you set."),
             ("Quoting you can trust", "A pricing model built from your real costs, so quotes protect your margin."),
             ("Get your access back", "Domain, website, email and data back in your name after a supplier leaves.")]
    c = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in quick)
    body = (phero("Small business quick wins", "The jobs you keep meaning to get to.", "Small, fixed-price fixes from $1,200 that give you back evenings and bring cash in faster. Built for sole traders and small teams. Most are scoped in days, not months. No lock-in contracts.",
                  [("/services/", "Services"), ("/services/quick-wins/", "Quick wins")], [("/contact/?topic=Small%20business%20quick%20win#form", "Ask about a quick win"), ("/examples/", "See examples")]) +
            f'<section style="padding-top:8px"><div class="wrap"><div class="cards quick">{c}</div>' +
            before_after("A two-van plumbing business", ["Invoices sent on Sunday nights", "$18k owed, nobody chasing", "No idea which jobs lost money", "Receipts in the glovebox"],
                         ["Invoice sent when the job's marked done", "Reminders go out automatically", "Monthly margin by job type", "Receipts snapped and matched"], "Illustrative example, not a client") +
            related([("/industries/trades/", "For trades & construction"), ("/industries/hospitality-retail/", "For hospitality & retail"), ("/examples/", "See a sample Monday cash email")]) +
            "</div></section>" + cta_band(topic="Small business quick win"))
    add("/services/quick-wins/", "Small business quick wins", "Fixed-price quick wins for small businesses, from $1,200: invoices that chase themselves, quote to invoice automation, Xero health checks, Monday cash emails and job profitability.", body)


def privacy_sprint():
    svc("/services/privacy-sprint/", "Privacy Act module", "Before 10 December 2026",
        "The Privacy Act module of the controls sprint.",
        "For organisations covered by the Privacy Act, including health and allied health providers and businesses over $3 million. It runs inside the <a href=\"/#sprint\">AI workflow &amp; controls sprint</a>: we find what your software decides about people, and hand your lawyer what they need to update your privacy policy before 10 December 2026.",
        """<h2>Why now</h2>
<p>From 10 December 2026, if the Privacy Act covers you, your privacy policy has to say when computer programs make, or substantially help make, decisions that could significantly affect people, and what personal information they use. Most businesses don't yet know which of their tools do that. It's often buried inside booking, finance, HR and fraud software.</p>
<h2>Who it's for</h2>
<ul><li>Health and allied health providers, who are generally covered regardless of turnover</li><li>Businesses with annual turnover over $3 million</li><li>Businesses that trade in personal information</li><li>Commonwealth contractors, AML/CTF reporting entities, credit reporting bodies, businesses related to a covered business, and those that opt in. The <a href="https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/organisations/small-business" rel="noopener">OAIC has the full list</a></li></ul>
<p>Not sure you're covered? Take the <a href="/ai-check/">free 2-minute check</a> first.</p>
<h2>How the module runs</h2>
<p>Every controls sprint checks whether the rule looks relevant. Where it does, the sprint goes deeper:</p>
<ol><li><strong>Inventory:</strong> every system and AI tool that touches customer, patient, staff or applicant information, the free ones included.</li>
<li><strong>Decision map:</strong> for each, what it decides or shapes, what personal information it uses, and how significant the outcome is for the person.</li>
<li><strong>Human review:</strong> where a person genuinely reviews outcomes, and where they should.</li>
<li><strong>Handover to your lawyer:</strong> plain-English draft wording describing your automated decisions, with the evidence behind it, ready for legal review.</li></ol>
<p class="fine">We don't give legal advice. The module produces the facts and draft wording; your lawyer confirms the final privacy policy.</p>""",
        [("System & AI tool inventory", "Including tools staff adopted on their own."), ("Automated-decision map", "What decides what, using which personal information."),
         ("Significance assessment", "Which decisions could significantly affect people."), ("Human-review design", "Where a person must genuinely check outcomes."),
         ("Draft policy wording", "Plain English, for your lawyer to finalise."), ("One-page summary", "For the board, the owner or the practice manager.")],
        aside("The fine print", ["Part of the controls sprint, fixed price from $3,500", "Two weeks; quoted in writing if your systems need more", "Built to finish before 10 December 2026"], "AI readiness & governance",
              "General information and process support only, not legal advice."),
        before_after("An allied health practice, 12 staff", ["Booking system auto-declines repeat no-shows", "Billing software sets payment plans automatically", "Privacy policy silent on automation", "No one knows what the tools decide"],
                     ["Both decisions mapped, with the data they use", "Human review added for payment plans", "Draft wording with the lawyer", "One-page summary for the practice owner"], "Illustrative example, not a client"),
        [("/ai-check/", "Free 2-minute check"), ("/insights/privacy-act-automated-decisions/", "The rule in plain English"), ("/services/ai-governance/", "Wider AI governance")],
        "AI readiness & governance", "The Privacy Act module",
        "The Privacy Act module of the AI workflow & controls sprint: map automated decisions and prepare privacy policy wording for your lawyer before the transparency obligation starts on 10 December 2026.")


# ------------------------------------------------------------------ industries
def industries_hub():
    groups = [
        ("Regulated & high-stakes", "Governance, audit trails and Privacy Act readiness, where getting it wrong costs trust.",
         [("/industries/health/", "Health & allied health", "Billing, rostering, reporting, privacy"), ("/industries/not-for-profits/", "Not-for-profits", "Grant reporting, board packs, donor data")],
         "Also: businesses with boards, professional services."),
        ("Transaction-heavy operators", "Reconciliations, margin protection and quote to cash, where small transactions hide where the money goes.",
         [("/industries/trades/", "Trades & construction", "Quotes, job costing, chasing payment"), ("/industries/hospitality-retail/", "Hospitality & retail", "Wages, suppliers, margins, weekly cash")],
         "Also: e-commerce, childcare and education."),
        ("Tech & digital assets", "Runway modelling, investor metrics, treasury reporting and integrations, where numbers move fast.",
         [("/industries/startups/", "Startups & tech agencies", "Runway, investor metrics, board packs"), ("/industries/crypto/", "Crypto & digital assets", "Wallet and stablecoin reconciliations, controls")],
         ""),
    ]
    html = ""
    for title, d, items, also in groups:
        li = "".join(f'<li><a href="{h}"><b>{t}</b><span>{x}</span><span class="go">Read more →</span></a></li>' for h, t, x in items)
        html += f'<div style="margin-bottom:34px"><p class="eyebrow">{title}</p><p class="muted" style="margin-top:6px">{d}</p><ul class="sectors" style="margin-top:14px">{li}</ul>{f"<p class=fine>{also}</p>" if also else ""}</div>'
    body = phero("Industries", "Three kinds of business. One standard.", "We group clients by the problem they have, not the logo on the van. Every one of them gets the same accounting rigour, controls and human sign-off.",
                 [("/industries/", "Industries")]) + f'<section style="padding-top:8px"><div class="wrap">{html}</div></section>' + cta_band("Your industry not listed?", "The problems are usually the same. Tell us yours in writing.")
    add("/industries/", "Industries", "Beiz works with regulated and high-stakes organisations, transaction-heavy operators, and tech and digital asset businesses: governance, automation, dashboards and models.", body)


def ind(path, crumb, h1, lede, pains, builds, scene, rel, topic, title, desc, extra=""):
    p = "".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in pains)
    body = (phero(crumb, h1, lede, [("/industries/", "Industries"), (path, crumb)], [("/contact/?topic=" + topic.replace(" ", "%20").replace("&", "%26") + "#form", "Start in writing"), ("/examples/", "See examples")]) +
            f'''<section style="padding-top:8px"><div class="wrap"><p class="eyebrow">Sound familiar?</p><h2>What we hear most.</h2><div class="cards">{p}</div></div></section>
<section><div class="wrap"><p class="eyebrow">What we build</p><h2>What changes.</h2>{deliv(builds)}{scene}{extra}{related(rel)}</div></section>''' + cta_band(topic=topic))
    add(path, title, desc, body)


def industries():
    ind("/industries/trades/", "Trades & construction", "You're on the tools all day. The admin shouldn't wait for Sunday night.",
        "Quotes, job costing, invoicing and chasing payment, set up so they mostly run themselves. You approve, it does the rest.",
        [("Invoicing lags the work", "The job's done Tuesday, the invoice goes out three weeks later, and you get paid a month after that."),
         ("Chasing money", "You're a tradie, not a debt collector. But $20k is sitting in overdue invoices."),
         ("Quotes that lose money", "The price felt right. Then materials went up, the job ran over, and the margin disappeared.")],
        [("Quote to invoice", "Mark the job done on your phone, the invoice goes out the same day."), ("Automatic reminders", "Polite, then firm, with a pay-now link. You approve the wording once."),
         ("Job costing", "Materials, labour and subbies against each job, so you know what made money."), ("Quoting model", "Built from your real past jobs, with contingency that reflects risk."),
         ("Monday cash email", "What's in the bank, what's owed, what's due, before you hit the site."), ("Supplier price watch", "Flags when a supplier's prices creep up.")],
        before_after("A cabinet-making business, 6 staff", ["Invoices typed up on the weekend", "31 days average to get paid", "Two jobs a quarter quietly lose money", "Cash surprises every BAS quarter"],
                     ["Invoices out the day the job closes", "Reminders run themselves", "Margin by job, every month", "13-week cash view, no surprises"], "Illustrative example, not a client"),
        [("/services/quick-wins/", "Quick wins"), ("/examples/", "Sample job profitability chart"), ("/services/dashboards-and-models/", "Cash forecasts")],
        "Small business quick win", "For trades & construction",
        "Automated quoting, invoicing, payment reminders and job costing for Australian tradies and construction businesses. Fixed price, no lock-in.")

    ind("/industries/health/", "Health & allied health", "Run the practice, not the paperwork.",
        "For clinics and allied health practices: bookings, billing reconciliations, rostering and reporting, automated with care. You hold some of the most sensitive information there is, so privacy, AI controls and human sign-off come first.",
        [("Billing that doesn't reconcile", "Payments, rebates and fund claims arrive in different places, and matching them takes hours."),
         ("No-shows and gaps", "Empty appointments cost money, and nobody has time to chase rebookings."),
         ("AI and patient data", "Staff want to use AI for notes and letters, and you're not sure what's allowed.")],
        [("Billing reconciliation", "Payments matched to appointments automatically, exceptions listed."), ("Practice dashboard", "Utilisation, revenue per practitioner, no-show rate, weekly."),
         ("Reminder and rebooking flows", "Using your existing booking system, within its rules."), ("AI use policy", "What staff can and can't put into AI tools, in plain English."),
         ("Privacy Act readiness", "Health service providers are generally covered regardless of size."), ("Controls", "Access, approvals and logs around anything touching patient data.")],
        before_after("An allied health practice, 4 clinicians", ["Friday afternoons spent reconciling", "No-show rate unknown", "Staff pasting notes into a free chatbot", "Privacy policy last updated years ago"],
                     ["Reconciliation done nightly", "No-shows tracked and followed up", "Approved, business-grade AI only", "Policy reviewed for automated decisions"], "Illustrative example, not a client"),
        [("/ai-check/", "Privacy Act AI check"), ("/services/ai-governance/", "AI governance"), ("/services/automation/", "Automation")],
        "AI readiness & governance", "For health & allied health providers",
        "Billing reconciliation, rostering, practice dashboards and AI governance for Australian clinics and allied health practices, with privacy and human sign-off built in.")

    rf = runway_facts()
    ind("/industries/startups/", "Startups & tech agencies", "Know your runway before your investors ask.",
        "Scenario models, investor-ready metrics and board packs, built from your real data. Plus the AI policy and controls that due diligence now asks about.",
        [("Runway is a guess", "One spreadsheet, one founder who understands it, and no idea what a new hire really does to the numbers."),
         ("Investor metrics on the fly", "MRR, churn and CAC calculated differently every time someone asks."),
         ("Due diligence questions", "Investors and enterprise customers now ask how you govern AI and data. You need a straight answer.")],
        [("Runway & scenario model", "Hiring, ad spend and AI API costs tested over 6, 12 and 24 months."), ("Investor metrics", "MRR, net revenue retention, CAC payback, churn, gross margin, the same way every month."),
         ("Board pack", "Monthly, refreshed from your systems, with commentary."), ("Data room financials", "Clean, reconciled and documented."),
         ("R&D cost tagging", "Development time and costs tagged by project, ready for your R&D adviser."), ("AI governance", "Register, policy and controls for due diligence.")],
        before_after("A 12-person SaaS startup", ["Runway 'about 18 months'", "Metrics rebuilt before every raise", "R&D costs untangled at year end", "No answer on AI governance"],
                     [f"Base case runway {rf['Base']} months, worst case {rf['Worst']}", "Metrics dashboard, same definitions monthly", "Costs tagged as they happen", "One-page AI governance summary"], "Illustrative example, not a client"),
        [("/examples/", "Sample runway model"), ("/services/dashboards-and-models/", "Dashboards & models"), ("/services/ai-governance/", "AI governance")],
        "Financial modelling", "For startups & tech agencies",
        "Runway and scenario models, investor metrics (MRR, CAC, churn), board packs, R&D cost tagging and AI governance for Australian startups and tech agencies.")

    ind("/industries/crypto/", "Crypto & digital assets", "Yes, we work with crypto businesses.",
        "Reconciliations, treasury reporting and controls for businesses that hold, pay or get paid in digital assets. We bring the discipline an auditor expects to a fast-moving asset class.",
        [("Ledger and chain disagree", "What the wallets say and what the accounts say don't match, and nobody knows why."),
         ("Stablecoin receipts", "Customers pay in USDC or AUD stablecoins, and matching them to invoices is manual."),
         ("Weak controls", "Who can move funds, with whose approval, and where's the record? It's usually one person and a hardware wallet.")],
        [("Wallet reconciliation", "On-chain balances matched to the ledger, differences explained."), ("Stablecoin matching", "Incoming payments matched to invoices automatically."),
         ("Treasury reporting", "Holdings, movements and exposure, weekly."), ("Transaction records", "Complete, categorised and traceable, ready for your tax agent."),
         ("Controls", "Documented approvals, segregation of duties and access reviews."), ("Audit readiness", "The evidence trail your auditor will ask for.")],
        before_after("A software company paid partly in stablecoins", ["Three wallets, one spreadsheet", "Payments matched by hand monthly", "One person can move funds alone", "Year-end records rebuilt from scratch"],
                     ["Daily reconciliation to the ledger", "Stablecoin receipts matched on arrival", "Two-person approval, logged", "Clean records for the tax agent"], "Illustrative example, not a client"),
        [("/examples/", "Sample wallet reconciliation"), ("/services/automation/", "Automation"), ("/services/dashboards-and-models/", "Treasury dashboards")],
        "Something else", "For crypto & digital asset businesses",
        "Wallet and stablecoin reconciliations, treasury reporting, transaction records and controls for Australian businesses working with digital assets.",
        '<p class="fine" style="margin-top:18px">We don\'t provide tax, financial product, investment or licensing advice. We make your records and controls clean so the advisers who do can rely on them.</p>')

    ind("/industries/not-for-profits/", "Not-for-profits", "More time for the mission. Less for the paperwork.",
        "Grant reporting, board packs and donor data, automated and reconciled, so your team spends its time on the work that matters.",
        [("Grant acquittals", "Every funder wants a different report, and each one takes days to pull together."),
         ("Board packs", "Volunteer directors need clear numbers, not 40 pages of spreadsheets."),
         ("Donor data everywhere", "The CRM, the payment platform and the ledger never quite agree.")],
        [("Grant tracking", "Spend tagged by grant as it happens, acquittals ready when due."), ("Board dashboard", "A few measures directors can read in five minutes."),
         ("Donor reconciliation", "Payments, CRM and ledger matched automatically."), ("Cash & reserves forecast", "So the board can see the next 12 months."),
         ("AI use policy", "Sensible rules for staff and volunteers using AI."), ("Reporting data", "Ready for your ACNC annual information statement.")],
        before_after("A community organisation, 3 grants", ["Acquittals built from scratch each time", "Board pack takes a week", "Donor totals don't match the ledger", "Reserves discussed by feel"],
                     ["Acquittals from tagged spend", "Board dashboard refreshes itself", "Donors reconciled monthly", "12-month reserves forecast"], "Illustrative example, not a client"),
        [("/services/dashboards-and-models/", "Dashboards"), ("/services/automation/", "Automation"), ("/services/ai-governance/", "AI governance")],
        "Something else", "For not-for-profits",
        "Grant reporting, board dashboards, donor reconciliation and reserves forecasting for Australian not-for-profits and charities.")

    ind("/industries/hospitality-retail/", "Hospitality & retail", "Know your numbers before the week gets away from you.",
        "Wages against sales, supplier price creep, stock and margins, and a weekly cash view. Built from your POS, rostering and accounting systems.",
        [("Wages creep", "You only find out wages were too high for sales after the pay run."),
         ("Suppliers edging prices up", "A few cents a line, every order, adding up to thousands a year."),
         ("Cash is tight midweek", "Busy weekends, big supplier bills on Tuesday, and no forward view.")],
        [("Wages vs sales", "Daily view from your POS and rostering."), ("Supplier price watch", "Flags price increases line by line."),
         ("Margin by product", "Which items make money and which just move."), ("Weekly cash email", "In the bank, owed, due, and next week's big bills."),
         ("Stock alerts", "Slow movers and reorder points from your sales history."), ("Invoice capture", "Supplier bills captured and coded without the shoebox.")],
        before_after("A café with two sites", ["Wages 38% of sales, found out monthly", "Supplier prices unchecked", "Menu priced by gut feel", "Cash crunch every quarter"],
                     ["Wages tracked daily against sales", "Price rises flagged on arrival", "Margin by menu item", "13-week cash view"], "Illustrative example, not a client"),
        [("/services/quick-wins/", "Quick wins"), ("/services/dashboards-and-models/", "Dashboards"), ("/examples/", "Sample Monday cash email")],
        "Small business quick win", "For hospitality & retail",
        "Wages versus sales, supplier price monitoring, margins and weekly cash reporting for Australian cafés, restaurants and retailers.")


# ------------------------------------------------------------------ examples
def examples():
    rf = runway_facts()
    body = phero("Examples", "See the work. Not the recipe.",
                 "Every example here uses a made-up business and made-up numbers. What's real is the format: this is what lands in your inbox or on your screen. How it's built is what you're paying for, so that part stays with us.",
                 [("/examples/", "Examples")]) + f'''<section style="padding-top:8px"><div class="wrap">

<figure class="vid" style="max-width:760px;margin-bottom:28px"><video src="/assets/media/cash-forecast-dark.mp4?v=60" poster="/assets/media/cash-forecast-dark.jpg?v=60" autoplay muted loop playsinline preload="none" aria-label="Screen recording: a 13-week cash forecast redraws as a large bill moves between weeks"></video><figcaption><b>A 13-week cash forecast.</b> Move one big bill and see which week drops below your buffer. <a href="/try/#cash">Try it with your numbers</a></figcaption></figure>

<div class="ex"><div class="exh"><b>1. The Monday cash email</b><span>Sample · fictional joinery business</span></div>
<div class="exb"><div class="mail"><div class="mh">From: Beiz reports · To: Sam · Monday 6:00am<br><b>Subject: Cash this week: $42,000 in the bank, one thing to watch</b></div>
<p>Morning Sam,</p>
<div class="kpis"><div><small>In the bank</small><b>$42,000</b></div><div><small>Owed to you</small><b>$31,400</b></div><div><small>Going out this week</small><b>$12,900</b></div></div>
<p><b>Overdue:</b> 3 invoices, $9,850. Reminders went out Friday. Harbour Kitchens (21 days, $6,200) hasn't opened theirs.</p>
<p class="flag"><b>Heads up:</b> cash is forecast to dip to $17,600 in the week of 16 November, below your $20,000 buffer. Two big supplier bills and wages land together. Options: bring forward the Cronulla invoice, or ask Timber Co for 14 days.</p>
<p>Full 13-week view: tap here.</p></div></div>
<p class="cap">What it replaces: logging into the bank, the accounting software and a spreadsheet every Monday. It arrives before you do.</p></div>

<div class="ex"><div class="exh"><b>2. The 13-week cash forecast</b><span>Sample · same business</span></div>
<div class="exb">{cash13()}</div>
<p class="cap">Refreshed weekly from the ledger and bank. The amber week breaches the minimum buffer, and you see it seven weeks out, with time to act. Hover a bar for the figure.</p></div>

<div class="ex"><div class="exh"><b>3. Which jobs actually make money</b><span>Sample · fictional joinery business</span></div>
<div class="exb">{job_margins()}</div>
<p class="cap">Materials, labour and subcontractors against each job. Two jobs fell below the 20% target. The office fit-out ran 40 hours over quote, which changes how the next one gets priced.</p></div>

<div class="ex"><div class="exh"><b>4. Startup runway and investor metrics</b><span>Sample · fictional software startup</span></div>
<div class="exb"><div class="tiles"><div class="tile"><small>MRR</small><b>$86.4k</b><span>▲ 6.1% on last month</span></div><div class="tile"><small>Net revenue retention</small><b>108%</b><span>trailing 12 months</span></div><div class="tile"><small>CAC payback</small><b>9.5 mo</b><span>target under 12</span></div><div class="tile"><small>Gross margin</small><b>78%</b><span>after hosting &amp; AI costs</span></div></div>
<div style="margin-top:18px">{runway()}</div></div>
<p class="cap">Three scenarios from the same model. The base case runs out of cash in month {rf["Base"]}, the worst case in month {rf["Worst"]}. That's when to start raising, and it's a conversation to have now.</p></div>

<div class="ex"><div class="exh"><b>5. The AI register</b><span>Sample excerpt · fictional services firm</span></div>
<div class="exb"><div class="tblw"><table class="tbl"><thead><tr><th>Tool</th><th>Used for</th><th>Personal info?</th><th>Trains on your data?</th><th>Decides about people?</th><th>Risk</th></tr></thead><tbody>
<tr><td>Free chatbot (personal accounts)</td><td>Drafting client emails</td><td>Yes</td><td>Possibly</td><td>No</td><td><span class="pill r">▲ High</span></td></tr>
<tr><td>Business AI assistant</td><td>Meeting notes, drafting</td><td>Yes</td><td>No (switched off)</td><td>No</td><td><span class="pill g">● Low</span></td></tr>
<tr><td>Booking system</td><td>Auto-declines late cancellers</td><td>Yes</td><td>No</td><td>Yes</td><td><span class="pill a">■ Medium</span></td></tr>
<tr><td>Accounting software</td><td>Credit terms by payment history</td><td>Yes</td><td>No</td><td>Yes</td><td><span class="pill a">■ Medium</span></td></tr>
</tbody></table></div></div>
<p class="cap">The first thing we build in a governance engagement. Two of these four tools make decisions about people, so they belong in the privacy policy from 10 December 2026.</p></div>

<div class="ex"><div class="exh"><b>6. The one-page board paper</b><span>Sample excerpt</span></div>
<div class="exb prose" style="max-width:none"><p style="color:var(--text)"><b>AI use: where we stand, Q4</b></p>
<p><b>Headline:</b> AI saves the team about 30 hours a month. One high risk remains: client data in personal chatbot accounts.</p>
<p><b>Decisions for the board:</b></p><ol><li>Approve the AI use policy (attached, two pages).</li><li>Fund business AI licences for all staff and block personal accounts.</li><li>Approve the privacy policy wording on automated decisions before 10 December.</li></ol>
<p><b>Owner:</b> Chief Operating Officer. <b>Next review:</b> March.</p></div>
<p class="cap">Directors get one page with decisions on it, not a technical report.</p></div>

<div class="ex"><div class="exh"><b>7. Wallet reconciliation</b><span>Sample · fictional digital asset business</span></div>
<div class="exb"><div class="tblw"><table class="tbl"><thead><tr><th>Wallet</th><th class="n">On-chain</th><th class="n">Ledger</th><th class="n">Difference</th><th>Status</th></tr></thead><tbody>
<tr><td>Operating (USDC)</td><td class="n">184,220.50</td><td class="n">184,220.50</td><td class="n">0.00</td><td><span class="pill g">✓ Matched</span></td></tr>
<tr><td>Treasury (BTC)</td><td class="n">3.41820000</td><td class="n">3.41820000</td><td class="n">0.00</td><td><span class="pill g">✓ Matched</span></td></tr>
<tr><td>Payments (AUD stablecoin)</td><td class="n">52,904.00</td><td class="n">55,404.00</td><td class="n">&minus;2,500.00</td><td><span class="pill a">! Unmatched receipt</span></td></tr>
</tbody></table></div></div>
<p class="cap">Differences are explained, not just flagged: here, a customer payment recorded in the ledger that hasn't arrived on-chain.</p></div>

<div class="ex"><div class="exh"><b>8. An agent's control log</b><span>Sample · accounts payable run</span></div>
<div class="exb"><ul class="log" id="log" aria-label="Example automated control log"></ul></div>
<p class="cap">Every action written down. Tap "why?" on the flagged lines to see the reasoning.</p></div>

<div class="ex" id="ex9"><div class="exh"><b>9. Behind the Monday email: the workflow</b><span>How it runs</span></div>
<div class="exb"><div class="vscroll"><svg class="flowsvg" viewBox="0 0 1226 210" role="img" aria-label="Workflow: schedule, pull from Xero read-only, run checks, update forecast, AI drafts the note, you approve, send and log. Failed checks stop the run and alert you."><defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="#9AA6B6"/></marker></defs><g><title>Every Monday: 5:00am schedule</title><rect x="10" y="20" width="150" height="78" rx="10" fill="#0E131D" stroke="#34425C" stroke-width="1.5"/><text x="22" y="40" font-family="Inter,sans-serif" font-size="9.5"  fill="#9AA6B6">STEP 1</text><text x="22" y="62" font-family="Inter,sans-serif" font-size="14" font-weight="600" fill="#E8EEF5">Every Monday</text><text x="22" y="81" font-family="Inter,sans-serif" font-size="10.5" fill="#9AA6B6">5:00am schedule</text></g><line x1="162" y1="59.0" x2="183" y2="59.0" stroke="#9AA6B6" stroke-width="1.5" marker-end="url(#ar)"/><g><title>Pull from Xero: read-only access</title><rect x="186" y="20" width="150" height="78" rx="10" fill="#0E131D" stroke="#34425C" stroke-width="1.5"/><text x="198" y="40" font-family="Inter,sans-serif" font-size="9.5"  fill="#9AA6B6">STEP 2</text><text x="198" y="62" font-family="Inter,sans-serif" font-size="14" font-weight="600" fill="#E8EEF5">Pull from Xero</text><text x="198" y="81" font-family="Inter,sans-serif" font-size="10.5" fill="#9AA6B6">read-only access</text></g><line x1="338" y1="59.0" x2="359" y2="59.0" stroke="#9AA6B6" stroke-width="1.5" marker-end="url(#ar)"/><g><title>Run the checks: ties to bank? bills missing?</title><rect x="362" y="20" width="150" height="78" rx="10" fill="#0E131D" stroke="#10B981" stroke-width="2"/><text x="374" y="40" font-family="Inter,sans-serif" font-size="9.5"  fill="#10B981">STEP 3</text><text x="374" y="62" font-family="Inter,sans-serif" font-size="14" font-weight="600" fill="#E8EEF5">Run the checks</text><text x="374" y="81" font-family="Inter,sans-serif" font-size="10.5" fill="#9AA6B6">ties to bank? bills missing?</text></g><line x1="514" y1="59.0" x2="535" y2="59.0" stroke="#9AA6B6" stroke-width="1.5" marker-end="url(#ar)"/><g><title>Update forecast: 13 weeks, rolled on</title><rect x="538" y="20" width="150" height="78" rx="10" fill="#0E131D" stroke="#34425C" stroke-width="1.5"/><text x="550" y="40" font-family="Inter,sans-serif" font-size="9.5"  fill="#9AA6B6">STEP 4</text><text x="550" y="62" font-family="Inter,sans-serif" font-size="14" font-weight="600" fill="#E8EEF5">Update forecast</text><text x="550" y="81" font-family="Inter,sans-serif" font-size="10.5" fill="#9AA6B6">13 weeks, rolled on</text></g><line x1="690" y1="59.0" x2="711" y2="59.0" stroke="#9AA6B6" stroke-width="1.5" marker-end="url(#ar)"/><g><title>Draft the note: AI writes, cites figures</title><rect x="714" y="20" width="150" height="78" rx="10" fill="#0E131D" stroke="#34425C" stroke-width="1.5"/><text x="726" y="40" font-family="Inter,sans-serif" font-size="9.5"  fill="#9AA6B6">AI · CHECKED</text><text x="726" y="62" font-family="Inter,sans-serif" font-size="14" font-weight="600" fill="#E8EEF5">Draft the note</text><text x="726" y="81" font-family="Inter,sans-serif" font-size="10.5" fill="#9AA6B6">AI writes, cites figures</text></g><line x1="866" y1="59.0" x2="887" y2="59.0" stroke="#9AA6B6" stroke-width="1.5" marker-end="url(#ar)"/><g><title>You approve: nothing sends without you</title><rect x="890" y="20" width="150" height="78" rx="10" fill="#0E131D" stroke="#F59E0B" stroke-width="2"/><text x="902" y="40" font-family="Inter,sans-serif" font-size="9.5"  fill="#F59E0B">HUMAN</text><text x="902" y="62" font-family="Inter,sans-serif" font-size="14" font-weight="600" fill="#E8EEF5">You approve</text><text x="902" y="81" font-family="Inter,sans-serif" font-size="10.5" fill="#9AA6B6">nothing sends without you</text></g><line x1="1042" y1="59.0" x2="1063" y2="59.0" stroke="#9AA6B6" stroke-width="1.5" marker-end="url(#ar)"/><g><title>Send + log: email out, all logged</title><rect x="1066" y="20" width="150" height="78" rx="10" fill="#0E131D" stroke="#34425C" stroke-width="1.5"/><text x="1078" y="40" font-family="Inter,sans-serif" font-size="9.5"  fill="#9AA6B6">STEP 7</text><text x="1078" y="62" font-family="Inter,sans-serif" font-size="14" font-weight="600" fill="#E8EEF5">Send + log</text><text x="1078" y="81" font-family="Inter,sans-serif" font-size="10.5" fill="#9AA6B6">email out, all logged</text></g><path d="M437.0,100 L437.0,142" stroke="#F87171" stroke-width="1.5" stroke-dasharray="4 3" fill="none" marker-end="url(#ar)"/><g><title>If a check fails, the run stops and you get an alert instead of a wrong email</title><rect x="317.0" y="146" width="240" height="50" rx="10" fill="#0E131D" stroke="#F87171" stroke-width="1.5"/><text x="329.0" y="166" font-family="Inter,sans-serif" font-size="13" font-weight="600" fill="#E8EEF5">Check fails? Stop and alert you</text><text x="329.0" y="184" font-family="Inter,sans-serif" font-size="10.5" fill="#9AA6B6">No wrong numbers ever reach your inbox</text></g></svg></div></div>
<p class="cap">Every Monday the same seven steps run on their own. The red line is the safety net: if the numbers don't tie to the bank, the run stops and you get an alert, not a wrong email. Nothing goes out until a person approves it.</p></div>

<div class="ex" id="ex10"><div class="exh"><b>10. Time given back</b><span>Illustrative example · 12-person business</span></div>
<div class="exb"><div class="vlegend"><span><i style="background:#5B6678"></i>Before (hours a month)</span><span><i style="background:#10B981"></i>After</span></div><div class="vscroll"><svg class="timesvg" viewBox="0 0 700 300" role="img" aria-label="Hours per month before and after automation, by task. Total 52 hours before, 12.5 after."><line x1="230.0" y1="22" x2="230.0" y2="274" stroke="#243048" stroke-width="1"/><text x="230.0" y="290" text-anchor="middle" font-size="10" fill="#9AA6B6" font-family="Inter,sans-serif">0h</text><line x1="332.5" y1="22" x2="332.5" y2="274" stroke="#243048" stroke-width="1"/><text x="332.5" y="290" text-anchor="middle" font-size="10" fill="#9AA6B6" font-family="Inter,sans-serif">4h</text><line x1="435.0" y1="22" x2="435.0" y2="274" stroke="#243048" stroke-width="1"/><text x="435.0" y="290" text-anchor="middle" font-size="10" fill="#9AA6B6" font-family="Inter,sans-serif">8h</text><line x1="537.5" y1="22" x2="537.5" y2="274" stroke="#243048" stroke-width="1"/><text x="537.5" y="290" text-anchor="middle" font-size="10" fill="#9AA6B6" font-family="Inter,sans-serif">12h</text><line x1="640.0" y1="22" x2="640.0" y2="274" stroke="#243048" stroke-width="1"/><text x="640.0" y="290" text-anchor="middle" font-size="10" fill="#9AA6B6" font-family="Inter,sans-serif">16h</text><text x="218" y="43" text-anchor="end" font-size="12.5" fill="#E8EEF5" font-family="Inter,sans-serif">Matching supplier bills</text><g><title>Matching supplier bills: before 12 hours a month</title><rect x="230" y="26" width="307.5" height="13" rx="3" fill="#5B6678"/></g><text x="543.5" y="37" font-size="10.5" fill="#9AA6B6" font-family="Inter,sans-serif">12h</text><g><title>Matching supplier bills: after 3 hours a month</title><rect x="230" y="42.0" width="76.875" height="13" rx="3" fill="#10B981"/></g><text x="312.875" y="53.0" font-size="10.5" fill="#E8EEF5" font-family="Inter,sans-serif">3h</text><text x="218" y="91" text-anchor="end" font-size="12.5" fill="#E8EEF5" font-family="Inter,sans-serif">Chasing payments</text><g><title>Chasing payments: before 10 hours a month</title><rect x="230" y="74" width="256.25" height="13" rx="3" fill="#5B6678"/></g><text x="492.25" y="85" font-size="10.5" fill="#9AA6B6" font-family="Inter,sans-serif">10h</text><g><title>Chasing payments: after 2 hours a month</title><rect x="230" y="90.0" width="51.25" height="13" rx="3" fill="#10B981"/></g><text x="287.25" y="101.0" font-size="10.5" fill="#E8EEF5" font-family="Inter,sans-serif">2h</text><text x="218" y="139" text-anchor="end" font-size="12.5" fill="#E8EEF5" font-family="Inter,sans-serif">Month-end checks</text><g><title>Month-end checks: before 16 hours a month</title><rect x="230" y="122" width="410.0" height="13" rx="3" fill="#5B6678"/></g><text x="646.0" y="133" font-size="10.5" fill="#9AA6B6" font-family="Inter,sans-serif">16h</text><g><title>Month-end checks: after 6 hours a month</title><rect x="230" y="138.0" width="153.75" height="13" rx="3" fill="#10B981"/></g><text x="389.75" y="149.0" font-size="10.5" fill="#E8EEF5" font-family="Inter,sans-serif">6h</text><text x="218" y="187" text-anchor="end" font-size="12.5" fill="#E8EEF5" font-family="Inter,sans-serif">Building the reporting pack</text><g><title>Building the reporting pack: before 8 hours a month</title><rect x="230" y="170" width="205.0" height="13" rx="3" fill="#5B6678"/></g><text x="441.0" y="181" font-size="10.5" fill="#9AA6B6" font-family="Inter,sans-serif">8h</text><g><title>Building the reporting pack: after 1 hours a month</title><rect x="230" y="186.0" width="25.625" height="13" rx="3" fill="#10B981"/></g><text x="261.625" y="197.0" font-size="10.5" fill="#E8EEF5" font-family="Inter,sans-serif">1h</text><text x="218" y="235" text-anchor="end" font-size="12.5" fill="#E8EEF5" font-family="Inter,sans-serif">Working out cash for the month</text><g><title>Working out cash for the month: before 6 hours a month</title><rect x="230" y="218" width="153.75" height="13" rx="3" fill="#5B6678"/></g><text x="389.75" y="229" font-size="10.5" fill="#9AA6B6" font-family="Inter,sans-serif">6h</text><g><title>Working out cash for the month: after 0.5 hours a month</title><rect x="230" y="234.0" width="12.8125" height="13" rx="3" fill="#10B981"/></g><text x="248.8125" y="245.0" font-size="10.5" fill="#E8EEF5" font-family="Inter,sans-serif">0.5h</text></svg></div>
<div class="vkpis"><div><small>Before</small><b>52 h a month</b></div><div><small>After</small><b>12.5 h a month</b></div><div><small>Back to the business</small><b>About 40 h a month</b></div></div></div>
<p class="cap">Illustrative only: your numbers depend on your volume and how tidy your data is. We measure your real before-and-after hours, so you see the actual result, not a promise.</p></div>

<div class="ex" id="ex11"><div class="exh"><b>11. The accountant's check</b><span>Sample · before anything is sent</span></div>
<div class="exb"><ul class="cacheck">
<li class="ok"><b>Opening cash ties to the bank statement</b><span>$61,500 at 5 October · matched</span></li>
<li class="ok"><b>Money owed to you ties to Xero</b><span>8 invoices, $109,700 · matched to aged receivables</span></li>
<li class="ok"><b>Bills owed tie to Xero</b><span>6 bills, $57,350 · matched to aged payables</span></li>
<li class="ok"><b>Payroll and super match the last pay run</b><span>$18,500 net wages + $3,400 super, fortnightly</span></li>
<li class="ok"><b>BAS amount confirmed</b><span>$21,600 due 28 October · confirmed with your tax agent</span></li>
<li class="ok"><b>Last week's forecast vs what happened</b><span>Receipts 4% under forecast · inside the 10% tolerance</span></li>
<li class="fl"><b>1 exception raised</b><span>A $4,800 bill paid from the bank isn't in Xero · sent to you to confirm</span></li>
</ul><p class="stamp">Reviewed and signed off · CA</p></div>
<p class="cap">This is the part software skips. The forecast is only as good as the numbers under it, so every figure is tied back to its source before you see it.</p></div>

<div class="ex" id="ex12"><div class="exh"><b>12. The board's view of risk</b><span>Sample · governance lens</span></div>
<div class="exb"><div class="riskwrap"><div><svg class="risksvg" viewBox="0 0 312 294" role="img" aria-label="Risk heat map: likelihood across, impact up."><rect x="71" y="165" width="72" height="72" rx="6" fill="#10B981" fill-opacity="0.1" stroke="#243048"/><rect x="71" y="91" width="72" height="72" rx="6" fill="#10B981" fill-opacity="0.18" stroke="#243048"/><rect x="71" y="17" width="72" height="72" rx="6" fill="#10B981" fill-opacity="0.26" stroke="#243048"/><rect x="145" y="165" width="72" height="72" rx="6" fill="#10B981" fill-opacity="0.18" stroke="#243048"/><rect x="145" y="91" width="72" height="72" rx="6" fill="#10B981" fill-opacity="0.34" stroke="#243048"/><rect x="145" y="17" width="72" height="72" rx="6" fill="#10B981" fill-opacity="0.5" stroke="#243048"/><rect x="219" y="165" width="72" height="72" rx="6" fill="#10B981" fill-opacity="0.26" stroke="#243048"/><rect x="219" y="91" width="72" height="72" rx="6" fill="#10B981" fill-opacity="0.5" stroke="#243048"/><rect x="219" y="17" width="72" height="72" rx="6" fill="#10B981" fill-opacity="0.74" stroke="#243048"/><g><title>1. Cash short in the BAS week · owner: Owner · control: 13-week forecast, buffer alert</title><circle cx="255.0" cy="53.0" r="11" fill="#E8EEF5" stroke="#0E131D" stroke-width="2"/><text x="255.0" y="57.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0E131D" font-family="Inter,sans-serif">1</text></g><g><title>2. Biggest customer pays late · owner: Owner · control: Weekly debtor check, reminder flow</title><circle cx="170.0" cy="53.0" r="11" fill="#E8EEF5" stroke="#0E131D" stroke-width="2"/><text x="170.0" y="57.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0E131D" font-family="Inter,sans-serif">2</text></g><g><title>3. Staff paste customer data into free AI · owner: Office manager · control: Approved tool only, one-page rules</title><circle cx="255.0" cy="127.0" r="11" fill="#E8EEF5" stroke="#0E131D" stroke-width="2"/><text x="255.0" y="131.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0E131D" font-family="Inter,sans-serif">3</text></g><g><title>4. Fake supplier bank details · owner: Bookkeeper · control: Bank changes held until phone-verified</title><circle cx="192.0" cy="53.0" r="11" fill="#E8EEF5" stroke="#0E131D" stroke-width="2"/><text x="192.0" y="57.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0E131D" font-family="Inter,sans-serif">4</text></g><g><title>5. Only one person knows the books · owner: Owner · control: Runbook and a second login</title><circle cx="181.0" cy="127.0" r="11" fill="#E8EEF5" stroke="#0E131D" stroke-width="2"/><text x="181.0" y="131.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0E131D" font-family="Inter,sans-serif">5</text></g><g><title>6. Xero not reconciled · owner: Bookkeeper · control: Weekly reconciliation check</title><circle cx="255.0" cy="201.0" r="11" fill="#E8EEF5" stroke="#0E131D" stroke-width="2"/><text x="255.0" y="205.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0E131D" font-family="Inter,sans-serif">6</text></g><text x="107.0" y="256" text-anchor="middle" font-size="10.5" fill="#9AA6B6" font-family="Inter,sans-serif">Unlikely</text><text x="181.0" y="256" text-anchor="middle" font-size="10.5" fill="#9AA6B6" font-family="Inter,sans-serif">Possible</text><text x="255.0" y="256" text-anchor="middle" font-size="10.5" fill="#9AA6B6" font-family="Inter,sans-serif">Likely</text><text x="62" y="205.0" text-anchor="end" font-size="10.5" fill="#9AA6B6" font-family="Inter,sans-serif">Low</text><text x="62" y="131.0" text-anchor="end" font-size="10.5" fill="#9AA6B6" font-family="Inter,sans-serif">Medium</text><text x="62" y="57.0" text-anchor="end" font-size="10.5" fill="#9AA6B6" font-family="Inter,sans-serif">High</text><text x="181.0" y="278" text-anchor="middle" font-size="10"  fill="#9AA6B6" font-family="Inter,sans-serif">LIKELIHOOD →</text></svg><p class="muted" style="font-size:.8rem;margin-top:4px">Impact goes up the side · darker = higher priority</p></div><ol class="rlist"><li><b>Cash short in the BAS week</b><span>Owner: Business owner · Control: 13-week forecast, buffer alert</span></li><li><b>Biggest customer pays late</b><span>Owner: Business owner · Control: Weekly debtor check, reminder flow</span></li><li><b>Staff paste customer data into free AI</b><span>Owner: Office manager · Control: Approved tool only, one-page rules</span></li><li><b>Fake supplier bank details</b><span>Owner: Bookkeeper · Control: Bank changes held until phone-verified</span></li><li><b>Only one person knows the books</b><span>Owner: Business owner · Control: Runbook and a second login</span></li><li><b>Xero not reconciled</b><span>Owner: Bookkeeper · Control: Weekly reconciliation check</span></li></ol></div></div>
<p class="cap">Every risk gets a name, an owner and a control, the way a board would want it. It's one page, reviewed each quarter, and it covers cash, people, fraud and AI together.</p></div>

<div class="ex" id="ex13"><div class="exh"><b>13. Revenue leakage findings</b><span>Sample · fictional 8-person engineering firm · one quarter</span></div>
<div class="exb"><div class="vkpis"><div><small>Revenue not invoiced</small><b>$72,586</b></div><div><small>Effort not recovered</small><b>$40,068</b></div><div><small>Total to review</small><b>$112,654</b></div></div>
<div class="tblw" style="margin-top:16px"><table class="tbl"><thead><tr><th>Where it leaks</th><th class="n">This quarter</th></tr></thead><tbody>
<tr><td>Time and materials work not invoiced</td><td class="n">$54,586</td></tr>
<tr><td>Fixed fees not invoiced on finished jobs</td><td class="n">$18,000</td></tr>
<tr><td>Fixed-fee jobs over budget, no variation raised</td><td class="n">$19,795</td></tr>
<tr><td>Client time marked non-billable</td><td class="n">$20,273</td></tr>
</tbody></table></div>
<p style="margin:18px 0 6px"><b>Five jobs to review first</b></p><div class="vscroll"><svg class="timesvg" viewBox="0 0 700 250" role="img" aria-label="Five jobs to review first, by dollars to review: J103 $22,580, J107 $22,513, J102 $20,387, J104 $19,770, J109 $13,437."><text x="238" y="37" text-anchor="end" font-size="12.5" fill="#E8EEF5" font-family="Inter,sans-serif">J103 Warehouse fit-out design</text><g><title>J103 Warehouse fit-out design: $22,580 to review. Fixed fee: effort 28% over the fee, no variation raised</title><rect x="250" y="24" width="343.2" height="18" rx="3" fill="#10B981"/></g><text x="601.2" y="37" font-size="10.5" fill="#E8EEF5" font-family="Inter,sans-serif">$22,580</text><text x="238" y="81" text-anchor="end" font-size="12.5" fill="#E8EEF5" font-family="Inter,sans-serif">J107 Clinic services upgrade</text><g><title>J107 Clinic services upgrade: $22,513 to review. Time and materials: September time of about $19,450 never invoiced</title><rect x="250" y="68" width="342.2" height="18" rx="3" fill="#10B981"/></g><text x="600.2" y="81" font-size="10.5" fill="#E8EEF5" font-family="Inter,sans-serif">$22,513</text><text x="238" y="125" text-anchor="end" font-size="12.5" fill="#E8EEF5" font-family="Inter,sans-serif">J102 Site inspections</text><g><title>J102 Site inspections: $20,387 to review. Time and materials: only 55% of time value invoiced</title><rect x="250" y="112" width="309.9" height="18" rx="3" fill="#10B981"/></g><text x="567.9" y="125" font-size="10.5" fill="#E8EEF5" font-family="Inter,sans-serif">$20,387</text><text x="238" y="169" text-anchor="end" font-size="12.5" fill="#E8EEF5" font-family="Inter,sans-serif">J104 Racking certification</text><g><title>J104 Racking certification: $19,770 to review. Fixed fee: job marked complete, half the fee never invoiced</title><rect x="250" y="156" width="300.5" height="18" rx="3" fill="#10B981"/></g><text x="558.5" y="169" font-size="10.5" fill="#E8EEF5" font-family="Inter,sans-serif">$19,770</text><text x="238" y="213" text-anchor="end" font-size="12.5" fill="#E8EEF5" font-family="Inter,sans-serif">J109 Pump station review</text><g><title>J109 Pump station review: $13,437 to review. Time and materials: 80% invoiced, $4,298 of time marked non-billable</title><rect x="250" y="200" width="204.2" height="18" rx="3" fill="#10B981"/></g><text x="462.2" y="213" font-size="10.5" fill="#E8EEF5" font-family="Inter,sans-serif">$13,437</text></svg></div></div>
<p class="cap">Timesheets, jobs and Xero invoices reconciled for one quarter. Each item is marked for the owner to confirm, not called money owed, because time is valued at the rate card and some write-offs are fair. Synthetic data: the leakage level was built to show every measure and isn't typical of any firm. The fixes were a month-end billing check, an overrun alert and a rule that no job closes before its final invoice.</p></div>

</div></section>''' + cta_band("Want this for your business?", "Tell us which of these you'd use first. A few lines in writing is enough.", "Dashboards & analytics")
    add("/examples/", "Examples", "Sample outputs from fictional businesses: Monday cash email, 13-week cash forecast, job profitability, runway model, AI register, board paper, reconciliation, the workflow behind it, time saved, the accountant's check, a board risk map and revenue leakage findings.", body)


# ------------------------------------------------------------------ AI check
def ai_check():
    body = phero("Free · 2 minutes · nothing sent anywhere", "Do the new automated-decision privacy rules apply to you?",
                 "From 10 December 2026, organisations covered by the Privacy Act must explain in their privacy policy when computer programs make, or substantially help make, decisions that significantly affect people. Nine questions tell you where you stand.",
                 [("/ai-check/", "Privacy Act AI check")]) + '''<section style="padding-top:8px"><div class="wrap">
    <div class="chk"><ol id="chkQ"></ol><div class="res" id="chkRes" aria-live="polite"><p class="muted">Answer the questions to see where you stand.</p></div></div>
    <p class="fine">An initial screen, not a full coverage decision. General information only, not legal advice. Your answers stay in your browser unless you choose to send them to us. For the complete list of when small businesses are covered, see the <a href="https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/organisations/small-business" rel="noopener">OAIC small business guidance and checklist</a>.</p>
  </div></section>
<section><div class="wrap split"><div class="prose">
<h2>What counts as an automated decision?</h2>
<p>It's broader than most people think. It covers software that decides on its own, and software that does something substantially and directly related to a decision a person then makes. If the outcome could significantly affect someone's rights or interests, and personal information is involved, it's likely in scope.</p>
<ul><li>Credit terms or payment plans set by payment history</li><li>Booking systems that block or deprioritise customers</li><li>Software that screens or ranks job applicants</li><li>Fraud tools that freeze an account</li><li>Pricing that changes by customer</li></ul>
<h2>What you'll need to do</h2>
<p>Update your privacy policy to describe the kinds of personal information used and the kinds of decisions involved. That means knowing which of your tools do this, which most businesses don't yet.</p>
<p><a href="/insights/privacy-act-automated-decisions/">Read the plain-English guide</a></p>
</div><aside class="aside"><h3>Days until 10 December 2026</h3><p class="price" data-adm-days>&nbsp;</p><p class="muted">The obligation applies to organisations covered by the Privacy Act. Many small businesses are exempt, but health service providers and several other kinds of business are covered regardless of size.</p><a class="btn primary" href="/#sprint">The controls sprint, with the Privacy Act module</a></aside></div></section>''' + contact_form("Want the written version?", "Send your result and we'll reply with a short written action list.", "Next step")
    add("/ai-check/", "Privacy Act AI check (free, 2 minutes)", "Free 2-minute check: will the Privacy Act automated-decision transparency rules starting 10 December 2026 apply to your business? Runs in your browser; nothing is sent.", body)


def workshop():
    body = phero("Free · 5 minutes · runs in your browser", "The AI workforce workshop",
                 "Five short chapters: where AI is heading, where your week goes, which jobs an agent should take, the limits you'd set, and a written plan at the end. Nothing you enter leaves your browser unless you choose to send it.",
                 [("/workshop/", "AI workforce workshop")]) + '''<section style="padding-top:8px"><div class="wrap">
  <div class="ws" id="ws">
    <ol class="ws-steps" id="wsSteps" aria-label="Workshop chapters"></ol>
    <div class="ws-stage" id="wsStage" aria-live="polite"></div>
    <div class="ws-nav"><button type="button" class="btn ghost" id="wsBack">Back</button><span class="ws-count" id="wsCount"></span><button type="button" class="btn primary" id="wsNext">Next</button></div>
  </div>
  <p class="fine">Time estimates use your inputs and our planning assumptions for each task. They're a starting point to test, not a promise. General information, not financial advice.</p>
</div></section>
<section class="live" id="live"><div class="wrap live-grid">
  <div>
    <h2>Prefer it live? Join a small-group workshop</h2>
    <p class="lede">Sixty minutes online with Purav Mehta CA, for owners and finance leads of Australian businesses. A small group, so every person gets time on their own business, not a webinar where you watch someone else's slides.</p>
    <ol class="live-ag">
      <li><b>Where AI actually is</b><span>Ten minutes on what's changed, what's hype and what the new Privacy Act rule means for you.</span></li>
      <li><b>Watch the agents work</b><span>A live run on a demo business in accounting software: a scam bill held for approval, a cash warning, the decision log.</span></li>
      <li><b>Map your first agent</b><span>You fill in its job description and limits for your own business, with help as you go.</span></li>
      <li><b>Your questions</b><span>Straight answers, including &ldquo;not yet&rdquo; when that's the right one.</span></li>
    </ol>
    <ul class="live-facts"><li><b>Free</b> while we run the first sessions</li><li><b>Up to 12 people</b>, by application</li><li><b>Online</b>, early evening Canberra time</li></ul>
  </div>
</div></section>
''' + contact_form(heading="Apply for a seat", lede="Tell us a little about your business and the job you'd most like to hand to an agent. We'll email you the next date and confirm your seat. Seats go to the applications we can help most in the hour.", eyebrow="Live workshop", sel="Live workshop")
    add("/workshop/", "AI workforce workshop (free, 5 minutes)", "A free, interactive 5-minute workshop: see where AI is heading, map your week, decide which jobs an agent should take, set its limits and get a written plan. Runs in your browser.", body)


# ------------------------------------------------------------------ how we work / faq / contact
FAQ = [
    ("Are you an AI company?", "We don't make or sell AI software, and we're not tied to any vendor. We set AI up properly for your business: we pick the right tools, connect them to your systems and your team, build the automations, dashboards and agents, and put the controls an accountant would expect around them."),
    ("What does Beiz actually do?", "We're accountants who build the systems behind a business's money: automation that does the grunt work, dashboards and forecasts that show what's coming, and the controls that keep AI safe. We don't do tax."),
    ("Isn't a Chartered Accountant just a tax accountant?", "Tax is one thing a Chartered Accountant can do, and we don't do it at all. A Chartered Accountant is trained in audit, risk, systems, forecasting and business advice. GAICD means we're also trained in how boards govern a business and oversee risk."),
    ("Who's behind Beiz?", "Beiz is led by Purav Mehta, an Australian Chartered Accountant and a graduate of the Australian Institute of Company Directors, with a background in internal audit, fraud and controls, corporate finance, project portfolio governance and data science. Your written proposal confirms who does the work, and you can verify his credentials before you sign anything."),
    ("Is my data safe with AI?", "We only use business-grade AI services whose terms stop your data being used to train models, and we build inside your own Microsoft, Google or Xero accounts wherever we can. Sensitive steps stay with a human."),
    ("What happens if the AI gets it wrong?", "It will, sometimes. That's why every build has approval steps, limits and a log. The AI prepares the work, a person signs it off, and anything unusual gets flagged rather than actioned."),
    ("Do you replace my accountant or bookkeeper?", "No. We don't replace your tax accountant, we feed them. They keep you right with the ATO, looking back at what happened. We work on what happens next week. At year end they get clean, reconciled data and do their job faster."),
    ("Do you do tax, BAS or R&D tax incentive claims?", "No. We don't provide tax agent or BAS services. What we do is make your records clean: crypto transactions reconciled, development costs tagged by project and activity, everything traceable. Your registered tax agent or R&D adviser then works from data they can rely on."),
    ("Doesn't Xero already do a cash forecast?", "Xero's own short-term forecast works mainly from the invoices and bills already entered in Xero. Most cash surprises come from what isn't: payroll and super, the BAS, loan repayments, the big job coming up, and bills nobody has entered yet. We build a 13-week forecast that includes all of it, and a short Monday note that tells you the one thing worth acting on."),
    ("Why 13 weeks?", "It's one quarter, so it always includes a BAS payment, several pay runs and three months of rent and loans. Customers on 30 to 60 day terms pay inside the window, so most of it is money you already know about. It's far enough ahead to act, and near enough to be reliable. Each Monday the oldest week drops off and a new one is added."),
    ("Do you do SMSF work or business valuations?", "No. SMSF advice and audits need licences and registrations we don't hold, and valuations are a specialist field with their own professional standard. What we can do is get your numbers clean and sale-ready, so the valuer, broker or adviser you choose has what they need."),
    ("Which tools do you work with?", "Xero, MYOB, Microsoft 365, Power BI, Google Workspace and the leading business AI tools. We pick what fits what you already own, so there's nothing new to learn unless it earns its place."),
    ("Why do you work in writing first?", "It respects your time and gets better answers. A written brief lets us think properly before replying, and you get a fully priced blueprint with a clear record of what was agreed, instead of a sales pitch. Once work is under way, if a conversation genuinely helps, we'll schedule one."),
    ("Why use an Australian CA rather than just AI or an offshore team?", "Use them too. AI and offshore teams are great for speed and volume. What an Australian Chartered Accountant adds is accountability here: bound by the CA ANZ Code of Ethics, across Australian rules like Payday Super, BAS timing and the Privacy Act, and answerable for the result. If you already outsource, we can set up the access, review steps and checks so it runs safely."),
    ("Is any of the work done offshore?", "No. Today every engagement is done by Purav Mehta in Australia. If that ever changes, your engagement letter will name who does the work, where, and what they can see, and nothing is shared without your written consent."),
    ("How do we find out if all our work has been billed?", "Start with three completed jobs. We reconcile one month of timesheets, the job list and the invoices, from exports, with no logins. You get a findings register where every gap is marked Confirmed, Needs information or Explained, with the records and the arithmetic behind it. Fixed price, agreed in writing before we start."),
    ("Can we see profit by job without hiring a management accountant?", "Often, yes. In most small project businesses the numbers already exist in the accounting software and the job or timesheet app; they just don't agree. We join them, agree one definition of margin, and set up a monthly report reconciled to your accounts, in Power BI or Excel."),
    ("Who owns what you build?", "You own the outcome: the automations, dashboards and models run inside your own accounts, with your logins. Our reusable templates, frameworks and code libraries remain our intellectual property, licensed to you for your business. That's how we keep delivery fast and prices fixed."),
    ("Do I need a board or a big business?", "No. Much of what we do is built for sole traders and owner-operators who are flat out and just want the admin to stop eating their evenings. We size the work to the business."),
    ("How much does it cost?", "Every job is fixed price, quoted in writing before work starts. The two-week cash and data check is $1,500 fixed and credited if you go ahead. A live cash and job profit model starts from $5,000, AI workforce setup from $8,500, and monthly monitoring and review from $1,250. Beiz isn't registered for GST, so no GST is added. No hourly meter and no lock-in contracts."),
    ("Do you work with crypto businesses?", "Yes: reconciliations, stablecoin payment matching, treasury reporting and controls. We don't give tax, financial product or licensing advice."),
    ("Where are you based?", "Australia. We work remotely with clients across the country."),
]


def faq_html(items):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


def how_we_work():
    prot = [("01 · Human sign-off", "Nothing material happens without a person approving it.", "Payments, filings and client communications always stop for a human."),
            ("02 · Your data stays yours", "We build inside your own accounts wherever possible.", "Business-grade AI only, on terms that stop your data being used for training."),
            ("03 · Audit trail", "Every automated decision is logged.", "You can see what happened, when, why, and who approved it."),
            ("04 · Written scope", "Fixed price, fixed deliverables, agreed in writing", "before any work starts. No hourly meter running."),
            ("05 · Confidentiality", "Professional confidentiality obligations apply to everything you share.", "We don't name clients without permission."),
            ("06 · Conflict checks", "Every enquiry is checked for conflicts of interest", "before we respond with a proposal.")]
    p = "".join(f'<div class="card"><span class="k">{k}</span><p><strong>{a}</strong> {b}</p></div>' for k, a, b in prot)
    body = phero("How we work", "Everything in writing. Nothing without your sign-off.", "How an engagement runs, how we protect you, and what you won't get from us.", [("/how-we-work/", "How we work")]) + f'''
{WIRING}

<section style="padding-top:8px"><div class="wrap">
  <ol class="steps">
    <li><h3>Tell us in writing</h3><p>Use the form or the guided assistant. A few lines is enough. We check for conflicts before replying.</p></li>
    <li><h3>Written proposal</h3><p>Within three business days: scope, fixed price, timeline and who does the work.</p></li>
    <li><h3>Build with updates</h3><p>Weekly written progress notes and a working demo you can click.</p></li>
    <li><h3>Handover pack</h3><p>Documentation, controls, training and your logins. It's yours.</p></li>
  </ol>
</div></section>
<section id="diligence">
  <div class="wrap">
    <p class="eyebrow">AI with due diligence</p>
    <h2>Anyone can use AI. Using it with due diligence is different.</h2>
    <p class="lede">AI is more than writing good prompts. Prompts are the easy part. The hard part is knowing your data, your obligations and your risks, and building the checks around them. That's the part we do.</p>
    <div class="ddt" role="table" aria-label="Prompting compared with due diligence">
      <div class="dd-h" role="row"><span role="columnheader">Just prompting</span><span role="columnheader">With due diligence</span></div>
      <div role="row"><span role="cell">Pick a tool and start typing</span><span role="cell">Check your data, privacy obligations and costs first</span></div>
      <div role="row"><span role="cell">Paste in whatever's handy</span><span role="cell">Decide what goes in, and keep customer data out of free tools</span></div>
      <div role="row"><span role="cell">Write clever prompts</span><span role="cell">Design the process: who approves, what's logged, what it can't touch</span></div>
      <div role="row"><span role="cell">Trust the answer</span><span role="cell">Tie every number back to your ledger before anyone acts on it</span></div>
      <div role="row"><span role="cell">A demo that looks good</span><span role="cell">Tested on your real data, with accuracy measured</span></div>
      <div role="row"><span role="cell">Done when it runs</span><span role="cell">Done when your team uses it, it's documented and you own it</span></div>
    </div>
    <p class="dd-so"><b>We set it up properly for you.</b> The speed of AI, with an accountant, board-level governance and a data specialist behind it.</p>
  </div>
</section>
<section><div class="wrap"><p class="eyebrow">How we protect you</p><h2>The controls come first. The AI comes second.</h2><div class="cards">{p}</div></div></section>
<section><div class="wrap split"><div class="prose">
<h2>What you won't get from us</h2>
<ul><li><strong>A sales pitch.</strong> Talk to us or write to us, whichever suits. Either way, what we'll do and the price are written down before you commit.</li>
<li><strong>An hourly meter.</strong> Fixed price, agreed before we start.</li>
<li><strong>Lock-in.</strong> No long contracts. Everything we build runs in your accounts, with your logins.</li>
<li><strong>Jargon.</strong> If we can't explain it simply, we haven't understood it well enough.</li>
<li><strong>Tax or BAS work.</strong> We leave that to your tax agent and make their job easier.</li></ul>
<h2>Who's behind Beiz</h2>
<p>Beiz is led by Purav Mehta, an Australian Chartered Accountant (CA ANZ) and graduate of the Australian Institute of Company Directors. His background: internal audit, fraud and controls, corporate finance, large-portfolio governance and data science. Your written proposal confirms who does the work, and you can verify his credentials before signing. <a href="https://www.linkedin.com/in/puravmehtaca/" rel="noopener">Purav on LinkedIn</a>.</p>
<p>We're bound by the CA ANZ Code of Ethics (APES 110).</p>
<h2>Led in Australia</h2>
<p>All strategy, architecture, governance and sign-off happen in Australia, by a Chartered Accountant and GAICD. For some build work we use a small, vetted delivery team, only with your written consent and always under our direct review. Your engagement letter says where any of your information will be handled, before you sign.</p>
<h2>Who owns what</h2>
<p>You own the outcome: everything runs in your accounts, with your logins, and it keeps running if we part ways. Our reusable templates, frameworks and code libraries stay our intellectual property, licensed to you. That's what keeps delivery fast and prices fixed.</p>
</div><aside class="aside"><h3>Working with your accountant</h3><p class="muted">Already have a tax accountant or bookkeeper? Good. We work alongside them and hand over clean, reconciled data.</p><a class="btn primary" href="/insights/we-feed-your-tax-accountant/">How that works</a></aside></div></section>''' + cta_band()
    add("/how-we-work/", "How we work", "How a Beiz engagement runs: written brief, fixed-price proposal, weekly updates and a full handover. Human sign-off, audit trail, confidentiality and conflict checks.", body)


def faq():
    body = phero("FAQ", "The things people ask first.", "Straight answers. If yours isn't here, ask it in writing.", [("/faq/", "FAQ")]) + f'<section style="padding-top:8px"><div class="wrap">{faq_html(FAQ)}</div></section>' + cta_band("Still have a question?", "Ask it in writing. You'll get a straight answer.")
    ld = '<script type="application/ld+json">' + __import__("json").dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}) + "</script>"
    PAGES["/faq/"] = page("/faq/", "FAQ", "Answers about Beiz: what we do, who's behind it, insurance, data safety, pricing, tax, crypto and why everything is in writing.", body, ld)


def contact():
    body = phero("Contact", "Start in writing.", "A few lines about the problem is plenty. No sales pitch, no pressure. You'll get a considered written reply by the next business day. Rather talk? Pick “Discovery call” below and I'll arrange a free 20 minutes, early morning or after 5pm. You'll know what the problem looks like, roughly what fixing it costs, and whether I'm the right fit. If I'm not, I'll say so.", [("/contact/", "Contact")]) + '''
<section style="padding:8px 0 0"><div class="wrap"><ol class="steps three">
<li><h3>You write</h3><p>What's broken, what you've tried, and what good would look like.</p></li>
<li><h3>We check</h3><p>A conflict check, then a proper look at the problem.</p></li>
<li><h3>We reply</h3><p>A written answer: what we'd do, how long, and a fixed price if it's a fit.</p></li></ol></div></section>''' + contact_form("Tell us what you're trying to fix.", "Prefer email? Write to hello@beiz.com.au.")
    add("/contact/", "Contact", "Book a free 20-minute discovery call or send a short written brief. No sales pitch, and a written reply by the next business day. hello@beiz.com.au", body)


def privacy():
    body = phero("Privacy policy", "Privacy policy", "How we handle personal information. Last updated 1 October 2026.", [("/privacy/", "Privacy policy")]) + '''<section style="padding-top:8px"><div class="wrap prose">
<p>Beiz Data &amp; Accounting Pty Ltd (ABN 53 691 755 496), "we", respects your privacy. This policy explains what we collect, why, and what we do with it. We aim to handle personal information consistently with the Australian Privacy Principles.</p>
<h2>What we collect</h2>
<ul><li><strong>What you send us:</strong> your name, email, organisation and message when you use our contact form or email us.</li>
<li><strong>Engagement information:</strong> if you become a client, the information needed to deliver the work, invoice you and meet our professional obligations.</li></ul>
<h2>What our website does and doesn't do</h2>
<ul><li>We don't use analytics, advertising cookies or tracking pixels.</li>
<li>Fonts and market data are served from our own site. Pages don't call third-party services when they load.</li>
<li><strong>Live Data panel and page:</strong> only if you open the panel or visit the Live Data page, your browser connects to ESPN (sports scores) and CoinGecko (crypto prices), which will see your IP address.</li>
<li>Our website host (GitHub Pages) may log technical information such as IP addresses for security and operations, under its own privacy statement.</li>
<li><strong>Privacy Act check and guided assistant:</strong> these run entirely in your browser. Nothing is sent to us unless you choose to send it through the contact form or email.</li>
<li>We use your browser's session storage only to carry a prefilled message to our contact page. It's cleared once used.</li></ul>
<h2>How we use it</h2>
<p>To reply to you, prepare proposals, deliver and invoice our work, keep records we're required to keep, and meet our professional and legal obligations. We don't sell personal information or use it for unrelated marketing.</p>
<h2>Who we share it with</h2>
<p>We use service providers to run the business, including email and document storage (Google Workspace). Some providers, including carefully selected support providers, may store or access information outside Australia. Where that happens we take reasonable steps to ensure they handle it consistently with the Australian Privacy Principles and under confidentiality obligations. We may also disclose information where required by law or by our professional bodies.</p>
<h2>AI tools</h2>
<p>We may use business-grade AI tools to help prepare work, under terms that stop your data being used to train models. A person reviews the output. Please don't send passwords, bank details or sensitive information through our website.</p>
<h2>Security, access and correction</h2>
<p>We take reasonable steps to protect personal information, including two-factor authentication and access controls. You can ask to access or correct the personal information we hold about you by emailing <a href="mailto:hello@beiz.com.au">hello@beiz.com.au</a>.</p>
<h2>Complaints</h2>
<p>If you have a concern, email us and we'll respond in writing within 30 days. If you're not satisfied, you can contact the Office of the Australian Information Commissioner at <a href="https://www.oaic.gov.au" rel="noopener">oaic.gov.au</a>.</p>
<h2>Automated decisions</h2>
<p>We don't use computer programs to make decisions about individuals that could significantly affect their rights or interests.</p>
</div></section>'''
    add("/privacy/", "Privacy policy", "How Beiz Data & Accounting handles personal information. No analytics, no tracking cookies, no third-party calls on page load.", body)


# ------------------------------------------------------------------ insights
ARTICLES = [
    ("/insights/privacy-act-automated-decisions/", "Privacy Act automated decisions from 10 December 2026: a plain-English guide", "What the new automated-decision rule means for Australian businesses, the OAIC's three-part test, who it applies to, and five things to do now.", "Updated 6 October 2026 · 5 minute read"),
    ("/insights/burned-by-an-ai-product/", "Burned by an AI product or a developer who vanished? Get these back first", "A practical checklist for taking back control of your domain, website, data and AI accounts when a supplier relationship goes wrong.", "1 October 2026 · 4 minute read"),
    ("/insights/why-13-weeks/", "Why 13 weeks? Your cash cycle in plain English", "Why a weekly view of the next quarter catches the problems a monthly report hides, and what Xero's own forecast leaves out.", "1 October 2026 · 4 minute read"),
    ("/insights/check-bills-before-you-pay/", "Five checks to run on every supplier bill before you pay it", "Duplicate bills, changed bank details and quiet price rises cost small businesses real money. Here's how to catch them, by hand or automatically in Xero or MYOB.", "6 October 2026 · 4 minute read"),
    ("/insights/we-feed-your-tax-accountant/", "We don't replace your tax accountant. We feed them.", "Why compliance and finance systems are different jobs, and how clean data makes both better.", "1 October 2026 · 3 minute read"),
]


def insights():
    c = "".join(f'<a class="card" href="{h}"><span class="k">{m}</span><h3>{t}</h3><p>{d}</p><span class="go">Read →</span></a>' for h, t, d, m in ARTICLES)
    body = phero("Insights", "Plain-English articles.", "Short, practical and written for owners, not IT departments.", [("/insights/", "Insights")]) + f'<section style="padding-top:8px"><div class="wrap"><div class="cards">{c}</div></div></section>'
    add("/insights/", "Insights", "Plain-English articles on AI governance, the Privacy Act automated-decision rules, finance automation and getting back control of your tech.", body)

    def art(i, prose, topic):
        h, t, d, m = ARTICLES[i]
        body = phero("Insights", t, d, [("/insights/", "Insights"), (h, t.split(",")[0].split("?")[0][:40])]) + f'<section style="padding-top:0"><div class="wrap"><p class="meta">{m}</p><div class="prose" style="margin-top:18px">{prose}</div></div></section>' + cta_band(topic=topic)
        add(h, t, d, body)

    art(0, '''<p>On 10 December 2026, a new transparency obligation in the Privacy Act starts. It came in with the Privacy and Other Legislation Amendment Act 2024, and it's aimed squarely at software that makes decisions about people.</p>
<h2>What the rule says</h2>
<p>If your organisation is covered by the Privacy Act, your privacy policy must explain when you use a computer program to make a decision, or to do something substantially and directly related to making a decision, that could reasonably be expected to significantly affect an individual's rights or interests, where personal information is used.</p>
<p>The policy needs to describe the kinds of personal information used, the kinds of decisions made by the program alone, and the kinds of decisions where the program does something substantially and directly related to the decision.</p>
<h2>The three-part test</h2>
<p>The OAIC's fact sheet, published on 30 September 2026, boils it down to three conditions. The rule applies when all three are true:</p>
<ol><li>A computer program makes a decision, or does something substantially and directly related to making it.</li>
<li>The decision could reasonably be expected to significantly affect someone's rights or interests.</li>
<li>Personal information is used to do it.</li></ol>
<p>If any one of the three is missing, this particular rule doesn't bite. If all three are there, your privacy policy needs to say so.</p>
<h2>Who it applies to</h2>
<p>Organisations covered by the Privacy Act. That generally means businesses with annual turnover over $3 million, plus some smaller ones regardless of size, including health service providers and businesses that trade in personal information. Government agencies are covered too.</p>
<p>If you're a small business that's exempt today, it's still worth knowing. Larger customers increasingly ask suppliers how they use AI, and the government has signalled further privacy reform.</p>
<h2>What might be caught</h2>
<ul><li>Setting credit or payment terms automatically from a customer's history</li><li>Booking or membership systems that automatically block or deprioritise people</li><li>Software that screens, scores or ranks job applicants</li><li>Fraud or risk tools that freeze accounts or transactions</li><li>Prices or offers that change by individual customer</li></ul>
<p>The key phrase is "substantially and directly related". Software that produces a score a person then rubber-stamps may still count. The regulator has signalled it will read the obligation broadly.</p>
<h2>What it doesn't do</h2>
<p>It doesn't ban automated decisions. It's a transparency obligation: say what you do. But you can't describe what you don't know about, and most businesses haven't mapped which of their tools make decisions.</p>
<h2>Five things to do now</h2>
<ol><li><strong>List every tool</strong> that touches customer, staff or applicant information, including free AI tools staff use.</li>
<li><strong>Find the decisions.</strong> For each tool, ask: does it decide, or substantially shape, an outcome for a person?</li>
<li><strong>Check the stakes.</strong> Could that outcome significantly affect someone: money, access to a service, a job?</li>
<li><strong>Decide where a human genuinely reviews,</strong> and make sure that review is real, not a click-through.</li>
<li><strong>Update your privacy policy</strong> in plain English, with your lawyer confirming the wording where needed.</li></ol>
<p>Our <a href="/ai-check/">free 2-minute check</a> is a quick way to see where you stand.</p>
<p class="fine">General information only, not legal advice. Sources: Office of the Australian Information Commissioner, <a href="https://www.oaic.gov.au/__data/assets/pdf_file/0021/269013/APP-1.7-1.9-Transparency-Obligation-Fact-Sheet.PDF" rel="noopener">APP 1.7–1.9 transparency obligation fact sheet</a> and <a href="https://www.oaic.gov.au/__data/assets/pdf_file/0019/269011/OAIC-APP-1.7-1.9-Transparency-Obligation-Flowchart_v4.pdf" rel="noopener">flowchart</a> (30 September 2026); <a href="https://www.oaic.gov.au/privacy/australian-privacy-principles-guidelines/chapter-1-app-1-open-and-transparent-management-of-personal-information/" rel="noopener">APP 1 guidelines</a>.</p>''', "Privacy Act automated-decision check")

    art(1, '''<p>It happens more than people admit. You paid a developer or an agency for a website, a chatbot or an automation. It didn't work, or they stopped replying, or they now want more money to hand things over. Before anything else, get control back. Here's the order that matters.</p>
<h2>1. Your domain name</h2>
<p>The domain is the keys to everything: website and email. Log in to the registrar and make sure the registrant is your business, the account is in your name, and two-factor authentication is on. Remove any other users. Then <strong>change the domain password</strong> (sometimes called the auth or EPP code) so nobody else can transfer it.</p>
<h2>2. Where your domain points (DNS)</h2>
<p>If your DNS is managed in someone else's account, your email and website depend on them. Move it to an account you control. Make a copy of the existing records first so nothing breaks.</p>
<h2>3. Email</h2>
<p>Make sure you are the super-admin of your email system, not the supplier. Check mail forwarding rules too; a forgotten one can copy your email to someone else.</p>
<h2>4. Website and code</h2>
<p>Get an export or backup of the site and any code, and admin access to wherever it's hosted. If it's in a code repository, the repository should belong to your account.</p>
<h2>5. AI and software accounts</h2>
<p>Chatbots and automations run on accounts with API keys. Make sure those accounts are in your business's name, billing is on your card, and <strong>rotate the keys</strong> the supplier had.</p>
<h2>6. Your data</h2>
<p>Export customer lists, conversation logs and anything the tool collected. It's your data; get a copy now.</p>
<h2>Then decide what's worth keeping</h2>
<p>Once you're in control, look at what you actually have. Sometimes it's 80% there and worth finishing. Sometimes it's quicker to start clean. Either way, the decision is yours, made with the facts.</p>
<blockquote>Keep everything in writing. Don't pay extra to get access to things you've already paid for without getting advice first.</blockquote>
<p>We help businesses do exactly this, calmly and quickly. <a href="/contact/?topic=Something%20else#form">Tell us what happened</a>.</p>''', "Something else")

    art(2, '''<p>Most small businesses don't run out of money because they're unprofitable. They run out because a few big payments land in the same week, before the money customers owe them arrives. A 13-week cash forecast is built to catch that week before it happens.</p>
<h2>Why a quarter</h2>
<p>Thirteen weeks is one quarter. That matters because most of a small business's big cash movements run on a quarterly or shorter cycle:</p>
<ul><li><strong>The BAS.</strong> For many businesses it's the biggest single payment of the quarter, and a 13-week view always includes one.</li>
<li><strong>Payroll and super.</strong> Wages go out weekly or fortnightly, and since Payday Super started on 1 July 2026, super goes out with every pay run too.</li>
<li><strong>Customer terms.</strong> On 30 to 60 day terms, invoices you raise today are paid inside the window. So most of the forecast is money you already know about, not guesses.</li>
<li><strong>Rent, loans and leases.</strong> Monthly payments show up three times, so nothing sneaks up on you.</li></ul>
<h2>Why weekly, not monthly</h2>
<p>A monthly report averages everything out. If payroll, super and the BAS all land in the last week of October, a monthly view says October is fine. The weekly view shows that one week goes short, and that's the week that matters.</p>
<h2>The cash loop</h2>
<p>Every business runs the same loop: pay staff and suppliers, do the work, send the invoice, wait to be paid. The gap between paying out and getting paid is where cash runs short. For most small businesses that loop takes 30 to 90 days, so 13 weeks covers one or two full loops. It's far enough ahead to act on, and close enough to be reliable.</p>
<h2>Doesn't Xero already do this?</h2>
<p>Xero has a short-term cash view built from the invoices and bills already in it. That's useful. But most cash surprises come from what isn't in it yet:</p>
<ul><li>Payroll, super and the BAS</li><li>Loan and lease repayments</li><li>The big job you've quoted but not invoiced</li><li>Bills sitting in someone's inbox</li><li>The customer who always pays three weeks late</li></ul>
<p>A proper 13-week forecast puts all of that in, week by week, and is updated with what actually happened each Monday.</p>
<h2>What to do with it</h2>
<p>The point isn't a pretty chart. It's the one decision it lets you make early: chase that invoice now, move a purchase back a fortnight, or talk to the bank before the tight week rather than during it.</p>
<p>If your year is seasonal, a simple 12-month view alongside it shows the quiet months coming too.</p>''', "13-week cash forecast")

    art(3, '''<p>Most money lost on supplier bills isn't lost to anything clever. It's a bill paid twice, a price that crept up and nobody noticed, or a payment sent to bank details that changed last week. Five simple checks catch nearly all of it.</p>
<h2>1. Have we paid this already?</h2>
<p>Look for the same supplier and the same amount within a few weeks, or the same invoice number twice. Duplicates usually come from a bill arriving by email and again by post, or a reminder being entered as a new bill.</p>
<h2>2. Have the bank details changed?</h2>
<p>This is the one that matters most. Payment-redirection scams work by sending a convincing email saying a supplier has new bank details. <strong>Never pay new bank details on the strength of an email.</strong> Hold the payment and phone the supplier on a number you already had, not one from the email.</p>
<h2>3. Is it over the approval limit?</h2>
<p>Set a dollar limit above which a bill needs a second pair of eyes, even in a two-person business. It costs a minute and stops most mistakes that matter.</p>
<h2>4. Has the price moved?</h2>
<p>Compare the unit price with the last order from the same supplier. A 10% rise might be fine, but you should decide that, not find out at year end.</p>
<h2>5. Is this a new supplier?</h2>
<p>First bills from new suppliers deserve a quick check: ABN, contact details and whether anyone actually ordered from them.</p>
<h2>Doing it automatically</h2>
<p>All five checks are rules, which makes them a good fit for automation. An automated workflow can pull new bills from Xero or MYOB each morning, run the checks, and sort them into <em>ready to pay</em> and <em>held for a person</em>, each held bill with its reason. Nothing is paid automatically: you still approve the payment run, you just stop reading every bill line by line.</p>
<p>You can watch it work on our <a href="/try/#bills">bill-checking demo</a>, which runs these checks on eight made-up bills in your browser.</p>

<h2>What it won't do</h2>
<p>It won't catch a fake bill from a real supplier with unchanged details and a normal price; that still needs someone who knows what was ordered. And the rules are only as good as your data: if supplier records are messy, cleaning them up comes first.</p>
<p>If you'd like these checks running on your own bills, <a href="/contact/?topic=Automation%20%26%20AI%20agents#form">tell us about your setup</a>. It's usually a few days' work.</p>
<p class="fine">General information only. If you think you've paid a scammer, contact your bank immediately and report it at <a href="https://www.scamwatch.gov.au/" rel="noopener">Scamwatch</a>.</p>''', "Automation & AI agents")

    art(4, '''<p>People sometimes ask whether we'll replace their accountant. We won't, and we don't want to. It's a different job.</p>
<h2>Two different jobs</h2>
<div class="tblw"><table class="tbl"><thead><tr><th></th><th>Your tax accountant</th><th>Beiz</th></tr></thead><tbody>
<tr><td>Main focus</td><td>Compliance: tax returns, BAS, keeping the ATO happy</td><td>Operations: automation, forecasts, dashboards, AI controls</td></tr>
<tr><td>Looks at</td><td>What happened last quarter or last year</td><td>What happens next week and next quarter</td></tr>
<tr><td>Delivers</td><td>Lodgements and annual statements</td><td>Systems that run every day, and the numbers to steer by</td></tr>
<tr><td>Registered with</td><td>The Tax Practitioners Board</td><td>CA ANZ public practice; we don't do tax</td></tr>
</tbody></table></div>
<p>Both matter. A good tax accountant keeps you compliant. But they're not usually the person who connects your job app to your invoicing, builds the 13-week cash forecast, or puts controls around the AI your staff are using.</p>
<h2>How it works together</h2>
<p>We build the systems that keep your records clean all year: invoices matched, bank reconciled, costs tagged by job or project, crypto transactions complete. When it's time to lodge, your accountant gets tidy, reconciled data. Less back-and-forth, fewer surprises, and often a smaller bill from them.</p>
<h2>Why we don't do tax</h2>
<p>Focus. Tax is a specialist field with its own registration. We'd rather be very good at the systems and the numbers that run your business, and let your tax agent be very good at theirs.</p>''', "Something else")



# ------------------------------------------------------------------ live data page
def live_page():
    body = phero("Live Data Lab", "Resilient live data, demonstrated.",
                 "A live demonstration of the data pipelines we build for clients: multiple public sources pulled in, normalised, cached safely and shown clearly. No client-side tracking, and if a source drops out, the page carries on without it.",
                 [("/live/", "Live data")]) + '''<section style="padding-top:8px"><div class="wrap labwrap">
  <div class="panel econ"><h4><span>The economy, in numbers</span><span>Australia</span></h4>
    <div class="labgrid">
      <div class="mtile"><small>RBA cash rate</small><b data-rba>4.60%</b><span class="muted" data-rba-note style="display:block;margin-top:2px;font-size:.72rem">Raised 0.25, effective 30 Sep 2026</span></div>
      <div class="mtile"><small>Inflation (CPI, year to Aug)</small><b>4.0%</b><span class="muted" style="display:block;margin-top:2px;font-size:.72rem">Underlying 3.6% · ABS</span></div>
      <div class="mtile"><small>Unemployment (Aug)</small><b>4.6%</b><span class="muted" style="display:block;margin-top:2px;font-size:.72rem">Up 0.2 points · ABS</span></div>
      <div class="mtile"><small>Company insolvencies FY26</small><b>14,152</b><span class="muted" style="display:block;margin-top:2px;font-size:.72rem">Construction 3,472 · ASIC</span></div>
      <div class="mtile"><small>Businesses in Australia</small><b>2.73m</b><span class="muted" style="display:block;margin-top:2px;font-size:.72rem">437,150 started in FY25 · ABS</span></div>
      <div class="mtile"><small>SMEs using AI</small><b>43%</b><span class="muted" style="display:block;margin-top:2px;font-size:.72rem">65% of the rest want human control · NAIC</span></div>
    </div>
    <p class="labsrc">Cash rate refreshed automatically from the <a href="https://www.rba.gov.au/statistics/cash-rate/" rel="noopener">RBA</a>. Other figures from the latest releases: <a href="https://www.abs.gov.au/media-centre/media-releases/cpi-rose-40-year-august-2026" rel="noopener">ABS CPI</a> (Aug 2026), <a href="https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia/latest-release" rel="noopener">ABS Labour Force</a> (Aug 2026), <a href="https://www.asic.gov.au/about-asic/news-centre/news-items/annual-asic-insolvency-data-reveals-increase-in-companies-failing" rel="noopener">ASIC insolvency data</a> (FY2025–26), <a href="https://www.abs.gov.au/media-centre/media-releases/7-facts-about-australian-businesses" rel="noopener">ABS business counts</a> (June 2025) and the <a href="https://www.ai.gov.au/news-and-insights/blog/ai-adoption-insights-december-2025-february-2026" rel="noopener">National AI Centre</a> (Dec 2025 to Feb 2026).</p>
    <p class="econ-so"><b>What it means:</b> borrowing is dearer, costs are rising and more businesses are failing, while most haven't worked out AI yet. The owners who see their cash weeks ahead, and use AI safely, are the ones who get through and pull ahead.</p></div>
  <div class="panel"><h4><span>Markets</span><span>ASX delayed · crypto 24h</span></h4><div class="labgrid" id="labMk"></div>
    <p class="labsrc">ASX and AUD via Yahoo Finance (delayed), crypto via CoinGecko. Indicative only, not financial advice.</p></div>
  <div class="panel"><h4><span>Scores</span><span>your time zone</span></h4><div class="labtabs" role="tablist" id="labNav"></div><div id="labList"></div>
    <p class="labsrc">Scores via ESPN. Soccer shows the EPL, Champions League, A-Leagues and the Socceroos and Matildas. Liverpool gets top billing.</p></div>
</div></section>
<section><div class="wrap split"><div class="prose">
<h2>Why this matters for your business</h2>
<p>Market benchmarks and live sport are simply public feeds everyone recognises. The engineering behind this page is the same engineering behind the systems we build for clients:</p>
<ul><li><strong>A live cash dashboard</strong> that refreshes from your bank and ledger, instead of a spreadsheet updated once a month.</li>
<li><strong>A sales or jobs board</strong> for the office wall, showing today's bookings, jobs finished and invoices out.</li>
<li><strong>Alerts that come to you</strong>: a supplier price jump, a big customer paying late, cash heading below your buffer.</li></ul>
<p>Same principles every time: pull from the source, check it, cache it safely, show only what matters, and keep working when something upstream breaks.</p>
</div><aside class="aside"><h3>Want this for your numbers?</h3><p class="muted">A live view of cash, sales or jobs, built from your own systems.</p><a class="btn primary" href="/contact/?topic=Dashboards%20%26%20analytics#form">Start in writing</a><a class="btn" style="margin-top:10px" href="/examples/">See examples</a></aside></div></section>'''
    add("/live/", "Live Data Lab", "Live ASX, AUD and crypto prices with cricket, NRL, AFL, EPL, Champions League and A-League scores. A working demo of the live dashboards Beiz builds for businesses.", body)


# ------------------------------------------------------------------ try-it demos
def try_page():
    def n(i, label, v, step="1"):
        return f'<label for="{i}">{label}<input id="{i}" type="number" inputmode="decimal" min="0" step="{step}" value="{v}"></label>'
    def r(i, label, v, mx=20):
        return f'<div class="rng"><label for="{i}">{label}</label><output for="{i}">{v} h</output><input id="{i}" type="range" min="0" max="{mx}" step="1" value="{v}"></div>'
    body = phero("Try it · 60 seconds each", "Find your problem in 60 seconds.",
                 "Four quick demos using your own numbers. They run entirely in your browser: nothing is sent to us unless you press send. Pick the one that sounds like your week.",
                 [("/try/", "Try it")]) + f'''<section style="padding-top:0"><div class="wrap">
<nav class="trynav" aria-label="Demos"><a href="#late">Late payers</a><a href="#cash">Cash forecast</a><a href="#bills">Bill checker</a><a href="#hours">Admin hours</a><a href="/ai-check/">Privacy Act check</a></nav>

<div class="demo" id="late"><div><span class="k">Demo 1 · Getting paid</span><h2>What are late payers costing you?</h2><p class="muted">Enter your rough numbers. We'll show how much of your money is sitting with customers.</p>
  <div class="fields" id="dLate">{n("lpN","Invoices you send a month",40)}{n("lpAvg","Average invoice ($)",2500,"50")}{n("lpTerms","Your payment terms (days)",14)}{n("lpActual","How long customers actually take (days)",38)}{n("lpHrs","Hours a week spent chasing",3)}</div></div>
  <div><div id="dLateOut"></div><button class="btn primary" type="button" id="dLateSend">Send me this with a fix</button></div></div>

<div class="demo" id="cash"><div><span class="k">Demo 2 · Cash</span><h2>Will you have enough cash?</h2><p class="muted">A simple 13-week forecast. Add one big bill and see what happens.</p>
  <div class="fields" id="dCash">{n("cfStart","Cash in the bank now ($)",42000,"500")}{n("cfIn","Money in, typical week ($)",11000,"250")}{n("cfOut","Money out, typical week ($)",11800,"50")}{n("cfBig","One big bill ($)",18000,"500")}{n("cfWk","Big bill lands in week (1 to 13)",7)}{n("cfBuf","Minimum buffer you want ($)",20000,"500")}</div></div>
  <div><div id="dCashOut"></div><button class="btn primary" type="button" id="dCashSend">Send me this with a fix</button></div></div>

<div class="demo" id="bills"><div><span class="k">Demo 3 · Controls</span><h2>Watch an agent check your bills.</h2><p class="muted">Eight supplier bills from a made-up business. Press run and watch what gets paid and what gets held for a human.</p>
  <button class="btn primary" type="button" id="dBillsRun">Run the checks</button><div id="dBillsRes"></div></div>
  <div class="tblw"><table class="tbl" style="min-width:0"><thead><tr><th>Bill</th><th>Supplier</th><th class="n">Amount</th><th>Result</th></tr></thead><tbody id="dBillsBody"></tbody></table></div></div>

<div class="demo" id="hours"><div><span class="k">Demo 4 · Time</span><h2>How many hours is admin eating?</h2><p class="muted">Slide to your typical week.</p>
  <div class="fields" id="dHrs">{r("ahInv","Invoicing &amp; quotes",3)}{r("ahChase","Chasing payments",2)}{r("ahData","Data entry &amp; reconciling",4)}{r("ahRep","Reports &amp; spreadsheets",2)}{n("ahRate","What an hour of your time is worth ($)",90,"5")}</div></div>
  <div><div id="dHrsOut"></div><button class="btn primary" type="button" id="dHrsSend">Send me this with a fix</button></div></div>

<p class="fine" style="margin-top:18px">Demos are simplified estimates from the numbers you enter. They're illustrations, not financial advice. The real versions are built from your own data.</p>
</div></section>''' + WATCH + cta_band("Found your problem?", "Tell us in a few lines. You'll get a written, fixed-price way to fix it.")
    add("/try/", "Try it: 60-second demos", "Four 60-second demos using your own numbers: what late payers cost you, a 13-week cash forecast, an AI bill checker and admin hours. Runs in your browser.", body)


# ------------------------------------------------------------------ about
def about():
    principles = [
        ("Controls before code", "We design every system the way an auditor would test it. The approvals, limits and logs come first; the clever part comes second."),
        ("A human signs off", "AI prepares the work. A person approves anything that moves money, reaches a customer or makes a decision about someone."),
        ("Fixed price, in writing", "You know the scope, the deliverables and the price before we start. No hourly meter, no lock-in."),
        ("Your data stays yours", "We build inside your own accounts, using only AI plans whose terms say your data isn't used for training. When we part ways, everything keeps running."),
        ("Plain English", "If we can't explain it simply, we haven't understood it. Board papers are one page. Status reports are one page."),
    ]
    pr = "".join(f'<div class="card"><span class="k">0{i+1}</span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(principles))
    body = phero("About Beiz", "An accountant's firm, built for the AI era.",
                 "Beiz Data &amp; Accounting helps Australian businesses use AI, automation and data without losing control of their numbers. Chartered Accountant and GAICD led, and set up to be small, careful and fast.",
                 [("/about/", "About us")], [("/contact/#form", "Start in writing"), ("/examples/", "See our work")]) + f'''
<section style="padding-top:8px"><div class="wrap"><h2 style="margin-top:0">Four disciplines, one firm.</h2>
<ul class="why" style="grid-template-columns:repeat(4,1fr)">
<li><span class="ic">CA</span><b>Chartered Accountant</b><p>Australian Chartered Accountant, CA ANZ member. Numbers that reconcile to your ledger, and professional standards you can hold us to.</p></li>
<li><span class="ic">GAICD</span><b>GAICD governance</b><p>Trained by the Australian Institute of Company Directors in how boards oversee risk. AI policies, controls and board reporting that directors can sign off.</p></li>
<li><span class="ic">DM</span><b>Data, financial and economic modelling</b><p>Financial models, economic and cost-benefit modelling, forecasts, dashboards and AI agents, built on your own data.</p></li>
<li><span class="ic">🔒</span><b>Your data, secured</b><p>Built inside your own accounts, with two-factor access, least-privilege permissions and only AI plans whose terms say your data isn't used for training. Covered by professional confidentiality under the CA ANZ code of ethics.</p></li>
</ul></div></section>
<section style="padding-top:0"><div class="wrap split"><div class="prose">
<h2>Why Beiz exists</h2>
<p>Small and mid-sized businesses are being sold AI from two directions. On one side, tech agencies that can build fast but have never reconciled a ledger, tested a control or sat in front of an auditor. On the other, accountants who understand the numbers but can't build the tools.</p>
<p>Most owners end up in the gap between them: a chatbot nobody uses, an automation that breaks at month-end, a spreadsheet only one person understands, and no idea what their AI tools are doing with customer data.</p>
<p>Beiz sits in that gap. We're accountants who build. The systems we deliver save real hours, and they're built with the controls, sign-offs and audit trail a Chartered Accountant would expect.</p>
<h2>Why the name, and the dog</h2>
<p>Beiz is named after Purav's chocolate-and-white Border Collie, who is also the reason he works the way he does. The name comes from <span lang="zh">贝仔</span> (bèi zǎi). <span lang="zh">贝</span> is short for <span lang="zh">宝贝</span>, “baby” or “treasure”, and <span lang="zh">仔</span> is an affectionate word for a little boy or a young animal. Put together: little treasure, or baby boy.</p>
<p>Collies are working dogs. They turn up every day, stay on the job until it's done, and nothing slips past them through the gate. That's how Purav works, and it's the standard we hold our systems to.</p>
<h2 id="who">Who's behind it</h2>
<figure class="founderfig"><img src="/assets/media/purav-mehta-2.jpg?v=43" alt="Purav Mehta" width="480" height="640" loading="lazy"><figcaption><b>Purav Mehta</b> CA · GAICD</figcaption></figure>
<p>Beiz is led by Purav Mehta, an Australian Chartered Accountant (CA ANZ) and a graduate of the Australian Institute of Company Directors.</p>
<p>His background: internal audit, fraud and controls; corporate finance and enterprise finance systems, including SAP; governance and reporting for large project portfolios; and data analysis, dashboards and automation. He's based in Canberra and works with businesses Australia-wide.</p>
<p>When you work with Beiz, you work with him. Your written proposal confirms who does what, and you can verify his credentials before you sign anything. <a href="https://www.linkedin.com/in/puravmehtaca/" rel="noopener">Purav on LinkedIn</a>.</p>
<h2>How we're set up</h2>
<p>Strategy, architecture, governance, client communication and sign-off all happen in Australia. For some build work we may use a small, vetted delivery team, always under our direct review. We also use business-grade AI tools to work faster. That's how a small firm delivers quickly at a fixed price, and your engagement letter spells out exactly who touches your information and where.</p>
<h2>What we don't do</h2>
<p>We don't do tax returns, BAS, SMSF advice or audits, business valuations, legal advice or financial product advice. Those need licences, registrations or specialist standards, and we'd rather do one thing properly. We work alongside the people who do them, and make their jobs easier with clean, reconciled data.</p>
</div>
<aside class="aside"><h3>At a glance</h3>
<ul class="ticks"><li>Led by Purav Mehta</li><li>Australian Chartered Accountant (CA ANZ)</li><li>GAICD</li><li>Bound by the APES 110 code of ethics</li><li>Beiz Data &amp; Accounting Pty Ltd · ABN 53 691 755 496</li><li>Australia-wide, remote-first</li></ul>
<a class="btn primary" href="/how-we-work/">How we work</a></aside></div></section>
<section><div class="wrap"><p class="eyebrow">What we believe</p><h2>Five rules we don't bend.</h2><div class="cards">{pr}</div></div></section>''' + cta_band("Sound like the kind of firm you want?", "Tell us what you're trying to fix. A few lines in writing is enough.")
    add("/about/", "About us", "About Beiz Data & Accounting: a Chartered Accountant and GAICD led firm helping Australian businesses use AI, automation and data without losing control of their numbers.", body)


def not_found():
    body = phero("404", "That page isn't here.", "It may have moved when we rebuilt the site. Try one of these instead.", [("/404.html", "Not found")],
                 [("/", "Home"), ("/services/", "Services"), ("/examples/", "Examples"), ("/contact/", "Contact")])
    PAGES["/404.html"] = page("/404.html", "Page not found", "Page not found.", body)


def build_all():
    home(); services_hub(); services(); privacy_sprint(); industries_hub(); industries(); examples(); ai_check(); workshop()
    how_we_work(); faq(); contact(); privacy(); insights(); live_page(); try_page(); about(); not_found()
    return PAGES
