"""Page content for beiz.com.au. Australian English, plain words, no prices, no names."""
from layout import (page, phero, related, cta_band, contact_form, SERVICES, INDUSTRIES)
from charts import cash13, job_margins, runway, runway_facts

PAGES = {}


def add(path, title, desc, body):
    PAGES[path] = page(path, title, desc, body)


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
      <div><b>"Aren't Chartered Accountants just tax people?"</b><p>Tax is one thing CAs do, and we don't do it at all. Chartered Accountants are also trained in audit, risk, systems, forecasting and business advice. That's our lane.</p></div>
      <div><b>"What does GAICD mean?"</b><p>A graduate of the Australian Institute of Company Directors: trained in how boards govern a business and oversee risk. It's why we build AI with controls and sign-offs, not just speed.</p></div>
    </div>
    <p style="margin-top:22px"><a class="btn primary" href="/examples/">See example outputs</a></p>
  </div>
</section>'''


def home():
    ind = "".join(f'<li><a href="{h}"><b>{t}</b><span>{d}</span><span class="go">Read more →</span></a></li>' for (h, t), d in zip(INDUSTRIES, [
        "Quotes, job costing, chasing payment", "Bookings, billing, practice reporting, patient privacy",
        "Runway scenarios, investor metrics, board packs", "Wallet and stablecoin reconciliations, controls",
        "Grant reporting, board packs, donor data", "Wages, suppliers, margins, weekly cash"]))
    body = f'''<section class="hero" id="top">
  <div class="wrap">
    <p class="eyebrow">Governed AI · Finance · Data · Modelling</p>
    <h1>AI you can sign off on.</h1>
    <p class="lede">Everyone's racing to use AI. Most small businesses are either falling behind or taking risks they can't see. We help you catch up safely: <strong>automation that saves hours, forecasts that show what's coming, and controls that keep your data and your name safe</strong>. Built by a Chartered Accountant, so the numbers are right.</p>
    <div class="cta">
      <a class="btn primary" href="#fix">What we fix</a>
      <a class="btn" href="/examples/">See examples</a>
    </div>
    <div class="grid2">
      <div class="panel">
        <h4><span>Agent run · control log · example</span><span aria-hidden="true">live</span></h4>
        <ul class="log" id="log" aria-label="Example automated control log"></ul>
      </div>
      <div class="panel">
        <h4><span>Capabilities</span></h4>
        <ul class="caps">
          <li><a href="/services/ai-governance/">AI strategy &amp; governance</a> <span>board-ready</span></li>
          <li><a href="/services/automation/">AI agents &amp; assistants</a> <span>with guardrails</span></li>
          <li><a href="/services/automation/">Finance process automation</a> <span>n8n · power automate</span></li>
          <li><a href="/services/dashboards-and-models/">Dashboards &amp; analytics</a> <span>power bi · python</span></li>
          <li><a href="/services/dashboards-and-models/">Financial modelling</a> <span>runway · scenarios</span></li>
          <li><a href="/services/project-delivery/">Tech project delivery</a> <span>scope · vendors · risk</span></li>
        </ul>
      </div>
    </div>
    <div class="trust" aria-label="Credentials">
      <div><img class="ca-logo" src="/ca-logo.png" alt="Chartered Accountants Australia and New Zealand" onerror="this.remove()"><b>Chartered Accountant</b><small>CA ANZ member holding a Certificate of Public Practice. Bound by the APES code of ethics.</small></div>
      <div><b>GAICD</b><small>Graduate of the Australian Institute of Company Directors. We write for owners and boards, not for IT.</small></div>
      <div><b>Audit &amp; risk</b><small>Internal audit, fraud and controls background. We design systems the way an auditor would test them.</small></div>
      <div><b>Data science</b><small>Python, R, Power BI and automation, built by people who understand the ledger.</small></div>
    </div>
  </div>
</section>

<section id="fix">
  <div class="wrap">
    <p class="eyebrow">What we fix</p>
    <h2>Sound like you? That's what we fix.</h2>
    <p class="lede">We solve specific, expensive problems. Each one below is a fixed-price piece of work with a result you can see.</p>
    <div class="fixcols">
      <div><h3>Running the business</h3><ul class="fix">
        <li><a href="/services/quick-wins/"><q>I spend every week chasing money.</q><span>→ <b>Invoices that chase themselves</b>, with a pay-now link</span><i>→</i></a></li>
        <li><a href="/services/dashboards-and-models/"><q>I don't know if I'll have enough cash next month.</q><span>→ <b>13-week cash forecast</b> that warns you early</span><i>→</i></a></li>
        <li><a href="/industries/trades/"><q>I don't know which jobs actually make money.</q><span>→ <b>Profit by job, client or service</b>, every month</span><i>→</i></a></li>
        <li><a href="/services/automation/"><q>Month-end eats a week.</q><span>→ <b>Reconciliations and checks automated</b>, you sign off</span><i>→</i></a></li>
      </ul></div>
      <div><h3>Leading the business</h3><ul class="fix">
        <li><a href="/ai-check/"><q>Will the new Privacy Act AI rules catch us?</q><span>→ <b>Free 2-minute check</b>, then a written action list</span><i>→</i></a></li>
        <li><a href="/services/ai-governance/"><q>My team uses ChatGPT and I don't know what goes in it.</q><span>→ <b>AI register, policy and controls</b></span><i>→</i></a></li>
        <li><a href="/industries/startups/"><q>Investors want numbers I can't produce.</q><span>→ <b>Runway model and investor metrics</b></span><i>→</i></a></li>
        <li><a href="/insights/burned-by-an-ai-product/"><q>Our tech project or developer went sideways.</q><span>→ <b>Get control back</b>, then finish it properly</span><i>→</i></a></li>
      </ul></div>
    </div>
  </div>
</section>

<section id="why">
  <div class="wrap">
    <p class="eyebrow">Why work with us</p>
    <h2>Why owners trust us with the numbers.</h2>
    <ul class="why">
      <li><span class="ic">CA</span><b>The numbers are right</b><p>Chartered Accountant built. Everything reconciles back to your ledger, not just to a nice chart.</p></li>
      <li><span class="ic">GA</span><b>Controls come first</b><p>GAICD trained in governance. Approvals, limits and an audit trail are built in, not added later.</p></li>
      <li><span class="ic">$</span><b>Fixed price, in writing</b><p>You know the cost and the deliverables before we start. No hourly meter, no lock-in contracts.</p></li>
      <li><span class="ic">🔒</span><b>Your data stays yours</b><p>We build inside your own accounts, use business-grade AI that doesn't train on your data, and are bound by professional confidentiality under the CA ANZ code of ethics.</p></li>
      <li><span class="ic">✓</span><b>Accountable</b><p>Certificate of Public Practice, professional indemnity insured, liability limited under an approved Professional Standards scheme.</p></li>
    </ul>
  </div>
</section>

{PLAIN}

<section id="see">
  <div class="wrap">
    <p class="eyebrow">What you actually get</p>
    <h2>Real outputs. Made-up businesses.</h2>
    <p class="lede">A forecast that warns you before cash gets tight. A view of which jobs make money. We show the result here; how it's built stays with us.</p>
    <div class="grid2" style="margin-top:28px">
      <div class="panel"><h4><span>13-week cash forecast · sample</span><span>fictional joinery business</span></h4>{cash13(compact=True)}<p class="fine">The amber week is the one to plan for. You'd know about it seven weeks early.</p></div>
      <div class="panel"><h4><span>Startup dashboard · sample</span></h4>
        <div class="tiles t2"><div class="tile"><small>MRR</small><b>$86.4k</b><span>▲ 6.1% on last month</span></div><div class="tile"><small>Runway</small><b>{runway_facts()["Base"]} mo</b><span>base case</span></div><div class="tile"><small>CAC payback</small><b>9.5 mo</b><span>target under 12</span></div><div class="tile"><small>Churn</small><b>1.6%</b><span>monthly, logo</span></div></div>
        <p class="fine" style="margin-top:12px">Investor-ready numbers, refreshed from your own systems.</p></div>
    </div>
    <p style="margin-top:20px"><a class="btn" href="/examples/">See all examples →</a></p>
  </div>
</section>

<section id="what">
  <div class="wrap">
    <p class="eyebrow">What we do</p>
    <h2>Accounting rigour, engineering speed.</h2>
    <p class="lede">Most firms can either build the tech or understand the numbers. We do both, so nothing gets lost between the finance team and the code.</p>
    <div class="cards two">
      <a class="card" href="/services/ai-governance/"><span class="k">Govern</span><h3>AI governance &amp; Privacy Act readiness</h3><p>Find where AI is already being used, map the risks, set the controls and give your board or your own team a clear one-page view.</p><span class="go">Learn more →</span></a>
      <a class="card" href="/services/automation/"><span class="k">Build</span><h3>Agents &amp; automation</h3><p>Invoice matching, month-end, reporting, inbox triage. Automated end to end, with approvals and a full log of every action.</p><span class="go">Learn more →</span></a>
      <a class="card" href="/services/dashboards-and-models/"><span class="k">See</span><h3>Dashboards &amp; financial models</h3><p>Live dashboards, 13-week cash forecasts, runway scenarios and investor metrics your lender, investors or board will trust.</p><span class="go">Learn more →</span></a>
      <a class="card" href="/services/project-delivery/"><span class="k">Deliver</span><h3>AI &amp; tech project delivery</h3><p>Already bought the software, or about to? We run the project: scope, vendors, milestones, risks and reporting, so it lands and gets used.</p><span class="go">Learn more →</span></a>
    </div>
    <div class="feed"><b>We don't replace your tax accountant. We feed them.</b><span>Your accountant looks after the ATO, looking back. We look out the windscreen: what's coming next week, and the systems that get you there. Different jobs, and we make theirs easier. <a href="/insights/we-feed-your-tax-accountant/">Why that matters →</a></span></div>
  </div>
</section>

<section id="who">
  <div class="wrap">
    <p class="eyebrow">Who we work with</p>
    <h2>Three kinds of business. One standard.</h2>
    <p class="lede">We group clients by the problem they have, not the logo on the van.</p>
    <div class="cards">
      <div class="card"><span class="k">Regulated &amp; high-stakes</span><h3>Governance, audit trails, Privacy Act</h3><p>Health practices, not-for-profits and businesses with boards, where getting it wrong costs trust, not just money.</p><p class="related" style="margin-top:12px"><a href="/industries/health/">Health</a><a href="/industries/not-for-profits/">Not-for-profits</a><a href="/services/ai-governance/">Governance</a></p></div>
      <div class="card"><span class="k">Transaction-heavy operators</span><h3>Reconciliations, margins, quote to cash</h3><p>Trades, hospitality, retail and professional services, where hundreds of small transactions hide where the money goes.</p><p class="related" style="margin-top:12px"><a href="/industries/trades/">Trades</a><a href="/industries/hospitality-retail/">Hospitality &amp; retail</a><a href="/services/quick-wins/">Quick wins</a></p></div>
      <div class="card"><span class="k">Tech &amp; digital assets</span><h3>Runway, investor metrics, treasury</h3><p>Startups, tech agencies and businesses holding or paid in digital assets, where the numbers move fast and investors ask hard questions.</p><p class="related" style="margin-top:12px"><a href="/industries/startups/">Startups</a><a href="/industries/crypto/">Crypto &amp; digital assets</a><a href="/services/dashboards-and-models/">Models</a></p></div>
    </div>
  </div>
</section>

<section id="how">
  <div class="wrap">
    <p class="eyebrow">How it works</p>
    <h2>No sales calls. Everything in writing.</h2>
    <p class="lede">You get a considered written answer, not a pitch, and a record of exactly what was agreed.</p>
    <ol class="steps">
      <li><h3>Tell us in writing</h3><p>Use the form or the guided assistant. A few lines is enough.</p></li>
      <li><h3>Written proposal</h3><p>Fixed price, scope and timeline within three business days.</p></li>
      <li><h3>Build with updates</h3><p>Weekly written progress notes and a working demo you can click.</p></li>
      <li><h3>Handover pack</h3><p>Documentation, controls and training so your team owns it.</p></li>
    </ol>
    <p style="margin-top:18px"><a class="btn" href="/how-we-work/">How we work and protect you →</a></p>
  </div>
</section>

<section id="sprint">
  <div class="wrap">
    <div class="offer">
      <div>
        <p class="eyebrow">Start here</p>
        <h2>AI Readiness Sprint</h2>
        <p class="price" style="font-size:1.5rem">Fixed price. <small>Quoted in writing.</small></p>
        <p>Ten business days. A clear picture of where AI can help, where it's already a risk, and one working prototype to prove it.</p>
        <p style="margin-top:18px"><a class="btn primary" href="/services/ai-readiness-sprint/">About the Sprint</a></p>
      </div>
      {ticks(["Inventory of AI tools already in use, including the free ones", "Risk and controls map for each use case", "One working automation or agent prototype on your own data", "A one-page board paper with recommendations", "A prioritised roadmap with fixed-price next steps"])}
    </div>
  </div>
</section>

{contact_form()}'''
    add("/", "Beiz Data & Accounting | Governed AI, automation and finance systems",
        "Accountants who build the systems behind a business's money: AI agents, automation, dashboards and financial models with controls and a human sign-off. Chartered Accountant and GAICD led. Australia-wide.", body)


# ------------------------------------------------------------------ services
def services_hub():
    cards = [
        ("/services/ai-governance/", "Govern", "AI governance & Privacy Act readiness", "Know what AI is in use, what it decides and who's accountable. Ready for 10 December 2026."),
        ("/services/automation/", "Build", "Agents & automation", "Accounts payable, month-end, reporting and admin, automated with approvals and an audit trail."),
        ("/services/dashboards-and-models/", "See", "Dashboards & financial models", "Cash forecasts, runway scenarios, job profitability and board or investor dashboards."),
        ("/services/project-delivery/", "Deliver", "AI & tech project delivery", "Scope, vendors, milestones and honest reporting, so your tech project actually lands."),
        ("/services/ai-readiness-sprint/", "Start here", "AI Readiness Sprint", "Ten business days: AI inventory, risk map, one working prototype and a roadmap."),
        ("/services/quick-wins/", "Small business", "Quick wins", "Small, fixed-price fixes that give you back evenings and bring cash in faster."),
    ]
    c = "".join(f'<a class="card" href="{h}"><span class="k">{k}</span><h3>{t}</h3><p>{d}</p><span class="go">Learn more →</span></a>' for h, k, t, d in cards)
    body = phero("Services", "Six ways we help.", "Every engagement is fixed price, agreed in writing, and ends with something your team can run. Pick the one closest to your problem, or tell us the problem and we'll pick.",
                 [("/services/", "Services")]) + f'<section style="padding-top:8px"><div class="wrap"><div class="cards">{c}</div></div></section>' + cta_band()
    add("/services/", "Services", "AI governance, automation, dashboards and financial models, tech project delivery and small business quick wins. Fixed price, in writing.", body)


def svc(path, crumb, eyebrow, h1, lede, prose, dl, side, scene, rel, topic, title, desc):
    body = (phero(eyebrow, h1, lede, [("/services/", "Services"), (path, crumb)]) +
            f'''<section style="padding-top:8px"><div class="wrap split"><div class="prose">{prose}<h2>What you get</h2>{deliv(dl)}{scene}{related(rel)}</div>{side}</div></section>''' +
            cta_band(topic=topic))
    add(path, title, desc, body)


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
                     ["One register, owned by the COO", "Business-grade tools only, training switched off", "Automated decisions described in plain English", "One-page board paper each quarter"], "Example scenario"),
        [("/ai-check/", "Free 2-minute Privacy Act check"), ("/insights/privacy-act-automated-decisions/", "The new rule in plain English"), ("/services/ai-readiness-sprint/", "AI Readiness Sprint")],
        "AI readiness & governance", "AI governance & Privacy Act readiness",
        "AI register, automated-decision mapping, AI use policy, controls and board reporting, ready for the Privacy Act automated-decision rules from 10 December 2026.")

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
<p>We use the tools that fit what you already own: Xero, MYOB, Microsoft 365 and Power Automate, Google Workspace, n8n, Python and business-grade AI models with training on your data switched off.</p>''',
        [("Working automation", "Built and tested on your real data."), ("Controls", "Approvals, limits and exception rules."), ("Audit trail", "Every action logged: what, when, why, who approved."),
         ("Runbook", "What it does, what to do when it stops."), ("Training", "Short, recorded, for the people who'll use it."), ("Handover", "It's yours: your accounts, your data, your logins.")],
        aside("Typical builds", ["Quick wins: days", "Single process: 2 to 4 weeks", "Multi-step agent: 4 to 8 weeks", "Fixed price, agreed in writing"], "Automation & AI agents"),
        before_after("Accounts payable, 400 invoices a month", ["Two days a month keying and matching", "A duplicate payment every quarter", "Bank detail changes by email, unchecked", "No record of who approved what"],
                     ["Matching done overnight", "Duplicates flagged before payment", "Changed bank details held until verified by phone", "Every approval logged"], "Example scenario"),
        [("/examples/", "See a sample control log"), ("/services/quick-wins/", "Small business quick wins"), ("/how-we-work/", "How we protect you")],
        "Automation & AI agents", "Agents & automation for finance",
        "AI agents and finance automation with approvals, delegation limits and a full audit trail: accounts payable, invoicing, month-end, reporting and admin.")

    rf = runway_facts()
    svc("/services/dashboards-and-models/", "Dashboards & models", "Dashboards & financial models",
        "See next month, not just last month.",
        "Live dashboards and financial models built from your own data: cash forecasts that warn you early, profitability by job or client, runway scenarios and the investor metrics people actually check.",
        f'''<h2>What we build</h2>
<ul><li><strong>13-week cash forecast:</strong> refreshed from your ledger and bank, with an early warning when cash will dip below your buffer.</li>
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
                     ["Monday cash email with a 13-week view", "Model the team can update safely", "Board pack refreshes itself", "Every hire tested against runway first"], "Example scenario"),
        [("/examples/", "See sample charts"), ("/industries/startups/", "For startups & tech agencies"), ("/industries/trades/", "For trades & construction")],
        "Dashboards & analytics", "Dashboards & financial models",
        "13-week cash forecasts, runway and scenario models, job profitability and investor metrics, built from your own data and reconciled to the ledger.")

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
                     ["Scope and migration signed off in writing", "Weekly status against milestones", "Go-live on the agreed date", "Training done, old system switched off"], "Example scenario"),
        [("/insights/burned-by-an-ai-product/", "Burned by a developer? Start here"), ("/services/automation/", "Agents & automation"), ("/how-we-work/", "How we work")],
        "Tech project delivery", "AI & tech project delivery",
        "Project delivery for AI and technology projects: scoping, vendor comparison, milestones, risk logs and plain-English status reporting. Rescue for stalled projects.")

    svc("/services/ai-readiness-sprint/", "AI Readiness Sprint", "Start here",
        "AI Readiness Sprint. Ten business days.",
        "A short, fixed-price engagement that gives you a clear picture of where AI can help, where it's already a risk, and one working prototype to prove the value on your own data.",
        '''<h2>Why a Sprint first</h2>
<p>Most businesses either rush into AI or avoid it. Both are expensive. The Sprint is the sensible middle: two weeks, a fixed price, and at the end you know what to do next and what it will cost, in writing.</p>
<h2>How the ten days run</h2>
<ol><li><strong>Days 1 to 2:</strong> short written survey of your team, review of your systems and subscriptions.</li>
<li><strong>Days 3 to 5:</strong> AI register, risk and controls map, and the automated-decision check for the Privacy Act.</li>
<li><strong>Days 6 to 9:</strong> build one working prototype on your own data, with a human sign-off step.</li>
<li><strong>Day 10:</strong> a one-page board or owner paper and a prioritised roadmap with fixed-price next steps.</li></ol>
<p>No obligation to continue with us afterwards. The roadmap is yours.</p>''',
        [("AI inventory", "Every tool in use, including the free ones."), ("Risk & controls map", "For each use case, what could go wrong and what stops it."), ("Working prototype", "One real automation or agent on your data."),
         ("Privacy Act check", "Where you stand on the automated-decision rules."), ("One-page paper", "For the board or for yourself."), ("Roadmap", "Prioritised next steps, each with a fixed price.")],
        aside("The fine print", ["Fixed price, quoted in writing", "Ten business days from kickoff", "Everything in writing, no sales calls", "No lock-in: the roadmap is yours"], "AI Readiness Sprint"),
        "", [("/services/ai-governance/", "AI governance"), ("/services/automation/", "Agents & automation"), ("/examples/", "Examples")],
        "AI Readiness Sprint", "AI Readiness Sprint",
        "A ten-day, fixed-price AI Readiness Sprint: AI inventory, risk and controls map, Privacy Act check, one working prototype and a costed roadmap.")

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
    body = (phero("Small business quick wins", "The jobs you keep meaning to get to.", "Small, fixed-price fixes that give you back evenings and bring cash in faster. Most take days, not months. No lock-in contracts.",
                  [("/services/", "Services"), ("/services/quick-wins/", "Quick wins")], [("/contact/?topic=Small%20business%20quick%20win#form", "Ask about a quick win"), ("/examples/", "See examples")]) +
            f'<section style="padding-top:8px"><div class="wrap"><div class="cards quick">{c}</div>' +
            before_after("A two-van plumbing business", ["Invoices sent on Sunday nights", "$18k owed, nobody chasing", "No idea which jobs lost money", "Receipts in the glovebox"],
                         ["Invoice sent when the job's marked done", "Reminders go out automatically", "Monthly margin by job type", "Receipts snapped and matched"], "Example scenario") +
            related([("/industries/trades/", "For trades & construction"), ("/industries/hospitality-retail/", "For hospitality & retail"), ("/examples/", "See a sample Monday cash email")]) +
            "</div></section>" + cta_band(topic="Small business quick win"))
    add("/services/quick-wins/", "Small business quick wins", "Fixed-price quick wins for small businesses: invoices that chase themselves, quote to invoice automation, Xero health checks, Monday cash emails and job profitability.", body)


# ------------------------------------------------------------------ industries
def industries_hub():
    groups = [
        ("Regulated & high-stakes", "Governance, audit trails and Privacy Act readiness, where getting it wrong costs trust.",
         [("/industries/health/", "Health & allied health", "Billing, practice reporting, patient privacy"), ("/industries/not-for-profits/", "Not-for-profits", "Grant reporting, board packs, donor data")],
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
                     ["Invoices out the day the job closes", "Reminders run themselves", "Margin by job, every month", "13-week cash view, no surprises"], "Example scenario"),
        [("/services/quick-wins/", "Quick wins"), ("/examples/", "Sample job profitability chart"), ("/services/dashboards-and-models/", "Cash forecasts")],
        "Small business quick win", "For trades & construction",
        "Automated quoting, invoicing, payment reminders and job costing for Australian tradies and construction businesses. Fixed price, no lock-in.")

    ind("/industries/health/", "Health & allied health", "Run the practice, not the paperwork.",
        "Bookings, billing reconciliations and practice reporting, automated with care. And because health practices hold sensitive information, privacy and AI controls come first.",
        [("Billing that doesn't reconcile", "Payments, rebates and fund claims arrive in different places, and matching them takes hours."),
         ("No-shows and gaps", "Empty appointments cost money, and nobody has time to chase rebookings."),
         ("AI and patient data", "Staff want to use AI for notes and letters, and you're not sure what's allowed.")],
        [("Billing reconciliation", "Payments matched to appointments automatically, exceptions listed."), ("Practice dashboard", "Utilisation, revenue per practitioner, no-show rate, weekly."),
         ("Reminder and rebooking flows", "Using your existing booking system, within its rules."), ("AI use policy", "What staff can and can't put into AI tools, in plain English."),
         ("Privacy Act readiness", "Health service providers are generally covered regardless of size."), ("Controls", "Access, approvals and logs around anything touching patient data.")],
        before_after("An allied health practice, 4 clinicians", ["Friday afternoons spent reconciling", "No-show rate unknown", "Staff pasting notes into a free chatbot", "Privacy policy last updated years ago"],
                     ["Reconciliation done nightly", "No-shows tracked and followed up", "Approved, business-grade AI only", "Policy reviewed for automated decisions"], "Example scenario"),
        [("/ai-check/", "Privacy Act AI check"), ("/services/ai-governance/", "AI governance"), ("/services/automation/", "Automation")],
        "AI readiness & governance", "For health & allied health practices",
        "Billing reconciliation, practice dashboards and AI governance for Australian health and allied health practices, with patient privacy built in.")

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
                     [f"Base case runway {rf['Base']} months, worst case {rf['Worst']}", "Metrics dashboard, same definitions monthly", "Costs tagged as they happen", "One-page AI governance summary"], "Example scenario"),
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
                     ["Daily reconciliation to the ledger", "Stablecoin receipts matched on arrival", "Two-person approval, logged", "Clean records for the tax agent"], "Example scenario"),
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
                     ["Acquittals from tagged spend", "Board dashboard refreshes itself", "Donors reconciled monthly", "12-month reserves forecast"], "Example scenario"),
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
                     ["Wages tracked daily against sales", "Price rises flagged on arrival", "Margin by menu item", "13-week cash view"], "Example scenario"),
        [("/services/quick-wins/", "Quick wins"), ("/services/dashboards-and-models/", "Dashboards"), ("/examples/", "Sample Monday cash email")],
        "Small business quick win", "For hospitality & retail",
        "Wages versus sales, supplier price monitoring, margins and weekly cash reporting for Australian cafés, restaurants and retailers.")


# ------------------------------------------------------------------ examples
def examples():
    rf = runway_facts()
    body = phero("Examples", "See the work. Not the recipe.",
                 "Every example here uses a made-up business and made-up numbers. What's real is the format: this is what lands in your inbox or on your screen. How it's built is what you're paying for, so that part stays with us.",
                 [("/examples/", "Examples")]) + f'''<section style="padding-top:8px"><div class="wrap">

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

</div></section>''' + cta_band("Want this for your business?", "Tell us which of these you'd use first. A few lines in writing is enough.", "Dashboards & analytics")
    add("/examples/", "Examples", "Sample outputs from fictional businesses: Monday cash email, 13-week cash forecast, job profitability, startup runway model, AI register, board paper and wallet reconciliation.", body)


# ------------------------------------------------------------------ AI check
def ai_check():
    body = phero("Free · 2 minutes · nothing sent anywhere", "Will the new Privacy Act AI rules catch you?",
                 "From 10 December 2026, organisations covered by the Privacy Act must explain in their privacy policy when computer programs make, or substantially help make, decisions that significantly affect people. Nine questions tell you where you stand.",
                 [("/ai-check/", "Privacy Act AI check")]) + '''<section style="padding-top:8px"><div class="wrap">
    <div class="chk"><ol id="chkQ"></ol><div class="res" id="chkRes" aria-live="polite"><p class="muted">Answer the questions to see where you stand.</p></div></div>
    <p class="fine">General information only, not legal advice. Your answers stay in your browser unless you choose to send them to us.</p>
  </div></section>
<section><div class="wrap split"><div class="prose">
<h2>What counts as an automated decision?</h2>
<p>It's broader than most people think. It covers software that decides on its own, and software that does something substantially and directly related to a decision a person then makes. If the outcome could significantly affect someone's rights or interests, and personal information is involved, it's likely in scope.</p>
<ul><li>Credit terms or payment plans set by payment history</li><li>Booking systems that block or deprioritise customers</li><li>Software that screens or ranks job applicants</li><li>Fraud tools that freeze an account</li><li>Pricing that changes by customer</li></ul>
<h2>What you'll need to do</h2>
<p>Update your privacy policy to describe the kinds of personal information used and the kinds of decisions involved. That means knowing which of your tools do this, which most businesses don't yet.</p>
<p><a href="/insights/privacy-act-automated-decisions/">Read the plain-English guide →</a></p>
</div><aside class="aside"><h3>Days until 10 December 2026</h3><p class="price" data-adm-days>&nbsp;</p><p class="muted">The obligation applies to organisations covered by the Privacy Act. Many small businesses are exempt today, but health service providers are generally covered regardless of size.</p><a class="btn primary" href="/services/ai-governance/">How we help</a></aside></div></section>''' + contact_form("Want the written version?", "Send your result and we'll reply with a short written action list.", "Next step")
    add("/ai-check/", "Privacy Act AI check (free, 2 minutes)", "Free 2-minute check: will the Privacy Act automated-decision transparency rules starting 10 December 2026 apply to your business? Runs in your browser; nothing is sent.", body)


# ------------------------------------------------------------------ how we work / faq / contact
FAQ = [
    ("What does Beiz actually do?", "We're accountants who build the systems behind a business's money: automation that does the grunt work, dashboards and forecasts that show what's coming, and the controls that keep AI safe. We don't do tax."),
    ("Aren't Chartered Accountants just tax accountants?", "Tax is one thing CAs do, and we don't do it at all. Chartered Accountants are trained in audit, risk, systems, forecasting and business advice. GAICD means we're also trained in how boards govern a business and oversee risk."),
    ("Who's behind Beiz?", "Beiz is led by a Chartered Accountant holding a Certificate of Public Practice and a graduate of the Australian Institute of Company Directors, with a background in internal audit, fraud and controls, corporate finance, project delivery and data science. Your written proposal names who does the work, and you can verify credentials before you sign anything."),
    ("Are you insured?", "Yes. We hold professional indemnity insurance, as required for public practice, and our liability is limited by a scheme approved under Professional Standards Legislation."),
    ("Is my data safe with AI?", "We only use business-grade AI services whose terms stop your data being used to train models, and we build inside your own Microsoft, Google or Xero accounts wherever we can. Sensitive steps stay with a human."),
    ("What happens if the AI gets it wrong?", "It will, sometimes. That's why every build has approval steps, limits and a log. The AI prepares the work, a person signs it off, and anything unusual gets flagged rather than actioned."),
    ("Do you replace my accountant or bookkeeper?", "No. We don't replace your tax accountant, we feed them. They keep you right with the ATO, looking back at what happened. We work on what happens next week. At year end they get clean, reconciled data and do their job faster."),
    ("Do you do tax, BAS or R&D tax incentive claims?", "No. We don't provide tax agent or BAS services. What we do is make your records clean: crypto transactions reconciled, development costs tagged by project and activity, everything traceable. Your registered tax agent or R&D adviser then works from data they can rely on."),
    ("Which tools do you work with?", "Xero, MYOB, Microsoft 365, Power BI, Power Automate, Google Workspace, n8n, Python and leading AI models. We pick what fits what you already own."),
    ("Why no phone calls?", "Written briefs get better answers and leave a clear record of what was agreed. If a call genuinely helps later in a project, we'll schedule one."),
    ("Do I need a board or a big business?", "No. Plenty of our work is for owner-operators who are flat out and just want the admin to stop eating their evenings. We size the work to the business."),
    ("How much does it cost?", "Every job is fixed price, quoted in writing after we understand the problem. Quick wins are priced like quick wins; larger builds are scoped individually. No hourly meter and no lock-in contracts."),
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
<section style="padding-top:8px"><div class="wrap">
  <ol class="steps">
    <li><h3>Tell us in writing</h3><p>Use the form or the guided assistant. A few lines is enough. We check for conflicts before replying.</p></li>
    <li><h3>Written proposal</h3><p>Within three business days: scope, fixed price, timeline and who does the work.</p></li>
    <li><h3>Build with updates</h3><p>Weekly written progress notes and a working demo you can click.</p></li>
    <li><h3>Handover pack</h3><p>Documentation, controls, training and your logins. It's yours.</p></li>
  </ol>
</div></section>
<section><div class="wrap"><p class="eyebrow">How we protect you</p><h2>The controls come first. The AI comes second.</h2><div class="cards">{p}</div></div></section>
<section><div class="wrap split"><div class="prose">
<h2>What you won't get from us</h2>
<ul><li><strong>Sales calls.</strong> Everything is in writing, so there's a record of what was promised.</li>
<li><strong>An hourly meter.</strong> Fixed price, agreed before we start.</li>
<li><strong>Lock-in.</strong> No long contracts. Everything we build runs in your accounts, with your logins.</li>
<li><strong>Jargon.</strong> If we can't explain it simply, we haven't understood it well enough.</li>
<li><strong>Tax or BAS work.</strong> We leave that to your tax agent and make their job easier.</li></ul>
<h2>Who's behind Beiz</h2>
<p>Beiz is led by a Chartered Accountant (CA ANZ, Certificate of Public Practice) and graduate of the Australian Institute of Company Directors. The background: internal audit, fraud and controls, corporate finance, large-portfolio project delivery and data science. Your written proposal names who does the work, and you can verify credentials before signing.</p>
<p>We're professional indemnity insured, as required for public practice, and bound by the APES code of ethics.</p>
</div><aside class="aside"><h3>Working with your accountant</h3><p class="muted">Already have a tax accountant or bookkeeper? Good. We work alongside them and hand over clean, reconciled data.</p><a class="btn primary" href="/insights/we-feed-your-tax-accountant/">How that works</a></aside></div></section>''' + cta_band()
    add("/how-we-work/", "How we work", "How a Beiz engagement runs: written brief, fixed-price proposal, weekly updates and a full handover. Human sign-off, audit trail, confidentiality and conflict checks.", body)


def faq():
    body = phero("FAQ", "The things people ask first.", "Straight answers. If yours isn't here, ask it in writing.", [("/faq/", "FAQ")]) + f'<section style="padding-top:8px"><div class="wrap">{faq_html(FAQ)}</div></section>' + cta_band("Still have a question?", "Ask it in writing. You'll get a straight answer.")
    ld = '<script type="application/ld+json">' + __import__("json").dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}) + "</script>"
    PAGES["/faq/"] = page("/faq/", "FAQ", "Answers about Beiz: what we do, who's behind it, insurance, data safety, pricing, tax, crypto and why everything is in writing.", body, ld)


def contact():
    body = phero("Contact", "Start in writing.", "A few lines about the problem is plenty. No sales calls, no pressure. You'll get a considered written reply within three business days.", [("/contact/", "Contact")]) + '''
<section style="padding:8px 0 0"><div class="wrap"><ol class="steps three">
<li><h3>You write</h3><p>What's broken, what you've tried, and what good would look like.</p></li>
<li><h3>We check</h3><p>A conflict check, then a proper look at the problem.</p></li>
<li><h3>We reply</h3><p>A written answer: what we'd do, how long, and a fixed price if it's a fit.</p></li></ol></div></section>''' + contact_form("Tell us what you're trying to fix.", "Prefer email? Write to hello@beiz.com.au.")
    add("/contact/", "Contact", "Send Beiz a short written brief. No sales calls. A considered written reply within three business days. hello@beiz.com.au", body)


def privacy():
    body = phero("Privacy policy", "Privacy policy", "How we handle personal information. Last updated 1 October 2026.", [("/privacy/", "Privacy policy")]) + '''<section style="padding-top:8px"><div class="wrap prose">
<p>Beiz Data &amp; Accounting Pty Ltd (ABN 53 691 755 496), "we", respects your privacy. This policy explains what we collect, why, and what we do with it. We aim to handle personal information consistently with the Australian Privacy Principles.</p>
<h2>What we collect</h2>
<ul><li><strong>What you send us:</strong> your name, email, organisation and message when you use our contact form or email us.</li>
<li><strong>Engagement information:</strong> if you become a client, the information needed to deliver the work, invoice you and meet our professional obligations.</li></ul>
<h2>What our website does and doesn't do</h2>
<ul><li>We don't use analytics, advertising cookies or tracking pixels.</li>
<li>Fonts and market data are served from our own site. Pages don't call third-party services when they load.</li>
<li>Our website host (GitHub Pages) may log technical information such as IP addresses for security and operations, under its own privacy statement.</li>
<li><strong>Live Data panel and page:</strong> only if you open the panel or visit the Live Data page, your browser connects to ESPN (sports scores) and CoinGecko (crypto prices), which will see your IP address.</li>
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
    ("/insights/privacy-act-automated-decisions/", "The Privacy Act's new AI rule, in plain English", "What the automated-decision transparency obligation starting 10 December 2026 means, who it applies to, and five things to do now.", "1 October 2026 · 5 minute read"),
    ("/insights/burned-by-an-ai-product/", "Burned by an AI product or a developer who vanished? Get these back first", "A practical checklist for taking back control of your domain, website, data and AI accounts when a supplier relationship goes wrong.", "1 October 2026 · 4 minute read"),
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
<p class="fine">General information only, not legal advice. Source: Office of the Australian Information Commissioner, <a href="https://www.oaic.gov.au/__data/assets/pdf_file/0027/263925/ADM-Issues-Paper.pdf" rel="noopener">automated decision-making issues paper</a>.</p>''', "Privacy Act automated-decision check")

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

    art(2, '''<p>People sometimes ask whether we'll replace their accountant. We won't, and we don't want to. It's a different job.</p>
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
  <div class="panel"><h4><span>Markets</span><span>ASX delayed · crypto 24h</span></h4><div class="labgrid" id="labMk"></div>
    <p class="labsrc">ASX and AUD via Yahoo Finance (delayed), crypto via CoinGecko. Indicative only, not financial advice.</p></div>
  <div class="panel"><h4><span>Scores</span><span>your time zone</span></h4><div class="labtabs" role="tablist" id="labNav"></div><div id="labList"></div>
    <p class="labsrc">Scores via ESPN. Football shows the EPL, Champions League, A-Leagues and the Socceroos and Matildas. Liverpool gets top billing.</p></div>
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


def not_found():
    body = phero("404", "That page isn't here.", "It may have moved when we rebuilt the site. Try one of these instead.", [("/404.html", "Not found")],
                 [("/", "Home"), ("/services/", "Services"), ("/examples/", "Examples"), ("/contact/", "Contact")])
    PAGES["/404.html"] = page("/404.html", "Page not found", "Page not found.", body)


def build_all():
    home(); services_hub(); services(); industries_hub(); industries(); examples(); ai_check()
    how_we_work(); faq(); contact(); privacy(); insights(); live_page(); not_found()
    return PAGES
