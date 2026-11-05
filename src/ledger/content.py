"""beiz.com.au content, "Ledger" edition (Nov 2026).

Every fact and price here must match CLAUDE.md section 1. Change prices only when Purav says so.
Australian English. Plain words. Control first, then benefit. No invented results.
"""

FACTS_LINE = "Beiz Data &amp; Accounting Pty Ltd &middot; ABN 53 691 755 496 &middot; ACN 691 755 496 &middot; Not registered for GST &middot; Canberra, ACT"

HOME_DESC = ("Beiz sets up AI agents for routine finance and admin work in Australian businesses. Tested on your past records, "
             "held for a person when unsure, checked by a Chartered Accountant.")

HERO_H1 = "AI that does the checking. A Chartered Accountant who checks the AI."
HERO_LEDE = ("Beiz Data &amp; Accounting sets up AI agents for the routine finance and admin work in your business: bills, cash, "
             "reconciliations and client checks. Each agent is tested on your past records first, and anything it isn't sure "
             "about waits for a person.")
HERO_CRED = ("Led by a Chartered Accountant, a member of Chartered Accountants Australia and New Zealand with a Certificate of Public Practice, and GAICD. "
             "Canberra, working Australia-wide.")

# (status class, status label, row text, count) for the made-up example week
HERO_BOOK = [
    ("ok", "ok", "Matched to supplier and order", "38"),
    ("held", "held", "Held for a person: possible duplicate or over limit", "3"),
    ("stop", "stop", "Stopped: supplier bank details changed", "1"),
]

JOBS_INTRO = "Start with one job. The agent does the checking and preparation; a person still decides anything that matters."
JOBS = [
    ("Bills", "Evenings spent copying between emailed PDFs, bank feeds and your accounting software.",
     "Matched to the supplier and order. Duplicates, split bills and changed bank details held for you."),
    ("Cash", "The bank balance today and a guess about next month.",
     "A 13-week cash view that refreshes from your weekly exports and ties back to the ledger."),
    ("Reconciliations", "Month-end spent copying between your accounting software and spreadsheets.",
     "Accounts matched on a schedule, with the exceptions listed for a person to clear."),
    ("Client checks", "New-client checks done from memory or an old checklist.",
     "Each new client checked against your written procedure, with gaps flagged before work starts."),
]

# (name, description, price, link)
START = [
    ("Two-week cash &amp; data check",
     "Your bills, invoices and timesheets checked against each other, with every finding traced to its record. "
     "Credited against your next Beiz build if you go ahead.", "$1,500 fixed", "/prices/"),
    ("Compliance controls sprint",
     "Two weeks on one obligation: AI use, AML/CTF Tranche 2 or the Privacy Act automated-decision rules. "
     "What's in scope, who owns it and where a person must approve.", "from $3,500", "/prices/"),
    ("AI workforce setup",
     "Agents for your bills, cash or client checks, each with written limits, tested on your records and run "
     "in shadow mode before going live.", "Scoped quote", "/how-we-work/"),
]
PRICE_NOTE = "Prices are in AUD, with no GST added."

SAFE = [
    ("Declare", "Each agent gets a written job description, its limits and a named person it reports to."),
    ("Contain", "It works only in the systems you approve, with a monthly spending cap and an off switch. Nothing is paid or sent without a person."),
    ("Test", "It's tested on your past records against a pass mark agreed in writing, then runs alongside your staff in shadow mode."),
    ("Watch", "Every decision is logged in your own accounts, and we review it with you at day 30."),
]

NOT_DO = ("Beiz doesn't do tax returns, BAS or GST lodgements, tax or BAS agent services, statutory audit or assurance, "
          "legal advice or financial product advice, and never releases payments without a person. Your tax agent keeps that work.")

CTA_TEXT = ("Tell us which piece of work takes the most hours. You'll get a written reply by the next business day, "
            "and a fixed-price proposal within three business days if it's a fit. If we're not the right fit, we'll say so.")

BIO = ("<p>Chartered Accountant, a member of Chartered Accountants Australia and New Zealand (CA ANZ) with a Certificate of Public Practice and a graduate of the Australian Institute "
       "of Company Directors, with a background in audit, controls, finance, data science and AI engineering. "
       "Every engagement is scoped, built and signed off by him.</p>")
BIO_FULL = BIO + ("<p>Where a job needs a lawyer, tax agent or IT provider, we say so and work alongside them. "
                  "Beiz takes on a limited number of projects at a time, with capacity agreed in writing before work begins.</p>")

# ---------------------------------------------------------------- services
SERVICES_LEDE = ("Finance, data, automation and governance work for Australian small businesses, startups and solo operators. "
                 "Fixed prices where the scope allows; a written quote everywhere else.")
GROUPS = [
    {"title": "Finance and decisions", "intro": "Know where cash and margin are going, from your own records.", "items": [
        ("Two-week cash &amp; data check", "Bills, invoices and timesheets checked against each other, every finding traced to its record.", "$1,500 fixed", ""),
        ("Cash &amp; job profit model", "A 13-week cash view and profit by job or client, tied back to the ledger. You drop in fresh exports weekly and it refreshes.", "Scoped quote", ""),
        ("Leave cover", "When someone in finance goes on leave, an agent carries the routine part of their role, a Chartered Accountant reviews its work, and everything is handed back the day they return.", "Scoped quote", ""),
    ]},
    {"title": "AI agents and automation", "intro": "Fewer handoffs and less re-keying, with a person signing off what matters.", "items": [
        ("AI workforce setup", "Agents for routine checking and preparation, each with a job description, limits, a test on your past records and shadow mode first.", "Scoped quote", ""),
        ("Workflow review &amp; redesign", "One process mapped end to end, with the handoffs, re-keying and waiting taken out before anything is automated.", "Scoped quote", ""),
        ("Workflow automation", "One repetitive finance or admin workflow automated, tested and handed over.", "Scoped quote", ""),
        ("Chatbots &amp; AI assistants", "Answers from approved business information only, with clear limits and a hand-over to a person.", "Scoped quote", ""),
        ("Monthly controls operations", "Up to two agreed agents or one model: monthly control review, log sample, test re-run and up to two hours of fixes.", "Scoped quote", ""),
    ]},
    {"title": "Data and reporting", "intro": "One trusted set of numbers, flowing on a schedule.", "items": [
        ("Data engineering", "Your accounting software, CRM, job app and spreadsheets connected into one clean source.", "Scoped quote", ""),
        ("Dashboards &amp; management reporting", "A reporting pack or dashboard on agreed definitions, reconciled to the ledger.", "Scoped quote", ""),
    ]},
    {"title": "Governance", "intro": "Know what's in scope, who owns it and where a person must approve.", "items": [
        ("Compliance controls sprint", "One obligation mapped in two weeks: AI use, AML/CTF Tranche 2 or the Privacy Act automated-decision rules. General information, not legal advice.", "from $3,500", ""),
        ("AI governance for boards &amp; owners", "A register, policy and reporting line for the AI already in use, including staff pasting client records into public AI tools.", "Scoped quote", ""),
    ]},
    {"title": "Workshops", "intro": "Build your own team's capability, not just a system.", "items": [
        ("Workshops for owners &amp; teams", "Small-group or in-house sessions on putting AI and data to work safely in day-to-day finance and admin.", "Scoped quote", ""),
        ("Coaching for finance professionals", "One-to-one sessions for accountants and finance leads building working data and AI skills.", "On request", ""),
    ]},
]

# ---------------------------------------------------------------- how it works
HOW_LEDE = ("Nothing runs on its own on day one. Every agent is tested on your past records, runs alongside your staff first, "
            "and needs a person's sign-off for anything that matters.")
FIRST30 = [
    ("Write or talk", "You describe the problem. A written reply by the next business day; calls are 20 minutes, early morning or after 5pm."),
    ("Fixed proposal", "Within three business days: a fixed price, a timeline and a definition of done."),
    ("Build and test", "Built in your own systems and replayed on a period of your past records agreed in the proposal. You get a one-page test report: how many it cleared, held and stopped, and every case where it disagreed with what your team actually did, measured against the pass mark agreed in writing."),
    ("Shadow mode", "The agent runs alongside your team. Its work is compared with theirs before anything goes live."),
    ("Hand over", "Documentation, the decision log in your own accounts, and a review with you at day 30. The rules, scripts and procedure files are yours to keep, so you aren't tied to Beiz to keep it running."),
]
INCLUDES = [
    "A written job description, limits and a named person the agent reports to",
    "A test report from replaying your past records, measured against a pass mark agreed in writing",
    "Shadow mode before live",
    "A decision log kept in your own accounts",
    "A monthly spending cap and an off switch",
    "Nothing paid or sent without a person",
    "A day-30 review",
    "An operating folder you keep: business context, procedures, the rules and scripts, and agent memory, as plain files",
]
FINDINGS = [
    ("What we report", "We report what the records support. Some findings need an explanation before anyone acts on them."),
    ("Weak records", "Where records are incomplete, we say so and report it as a limitation, not a finding."),
    ("Demo figures", "Figures in demos are illustrative, from made-up businesses, and exclude GST."),
]

# ---------------------------------------------------------------- prices
PRICES_LEDE = "Prices are in AUD, with no GST added. Every proposal has a fixed price, a timeline and a definition of done."
PRICES = [
    ("Free bill check", "Eight quick checks on a bills export, run in your browser. Nothing is uploaded.", "Free", "/bill-check/"),
    ("Two-week cash &amp; data check", "Bills, invoices and timesheets checked against each other, every finding traced to its record.", "$1,500 fixed", ""),
    ("Compliance controls sprint", "Two weeks, one focus: AI use, AML/CTF Tranche 2 or the Privacy Act automated-decision rules.", "from $3,500", ""),
    ("Live cash &amp; job profit model", "13-week cash and profit by job or client, tied to the ledger, documented and handed over.", "Scoped quote", ""),
    ("AI workforce setup", "Agents with written limits, tested on your records, shadow mode first.", "Scoped quote", ""),
    ("Leave cover", "An agent carries the routine part of a finance role during leave, reviewed by a Chartered Accountant.", "Scoped quote", ""),
    ("Monthly controls operations", "Ongoing review of up to two agreed agents or one model.", "Scoped quote", ""),
]
PRICE_TERMS = [
    ("Credit", "The $1,500 check is credited once against your next Beiz build (cash model, AI workforce setup, compliance sprint "
               "or leave cover setup) if you accept the proposal and pay the deposit within 60 days of the findings. "
               "It isn't redeemable for cash and doesn't apply to monthly support."),
    ("Monthly operations", "Covers up to two agreed agents or one model: a monthly control review, a log sample, a test re-run and up "
                           "to two hours of fixes in total. More is quoted. Requests are acknowledged within two business days. "
                           "It isn't round-the-clock monitoring or an emergency service."),
    ("Cash model", "You drop in fresh exports weekly and the model refreshes. Beiz builds it, ties actuals to the ledger, documents "
                   "the assumptions and hands it over. Beiz reviews the forecast only where the support agreement sets out how often and what."),
    ("Proposals", "Every proposal has a fixed price, a timeline and a definition of done, and arrives within three business days."),
]

# ---------------------------------------------------------------- about
ABOUT_LEDE = ("Beiz Data &amp; Accounting Pty Ltd sets up AI for real work in Australian businesses, with the controls a "
              "Chartered Accountant expects. Small businesses, startups and solo operators first; accounting firms and finance teams at the core.")
SETUP = ("Beiz is a company, led by its founder. Every engagement is scoped, built and signed off by him, and outside help "
         "works under his review. We take on a limited number of projects at a time.")
FACTS = [
    ("Legal name", "Beiz Data &amp; Accounting Pty Ltd"),
    ("ABN", "53 691 755 496"),
    ("ACN", "691 755 496"),
    ("GST", "Not registered. Prices are AUD with no GST added"),
    ("Principal", "Purav Mehta: Chartered Accountant (CA ANZ) with a Certificate of Public Practice, GAICD"),
    ("Insurance", "Professional indemnity insurance held with Chubb"),
    ("Based in", "Canberra, ACT. Working Australia-wide"),
    ("Email", '<a href="mailto:hello@beiz.com.au">hello@beiz.com.au</a>'),
]

# ---------------------------------------------------------------- contact
CONTACT_LEDE = "Write a few lines about the problem. You'll get a written reply by the next business day."
TOPICS = ["Discovery call", "Two-week cash & data check", "Compliance controls sprint", "AML/CTF Tranche 2",
          "AI workforce setup", "Cash & job profit model", "Leave cover", "Automation & AI agents",
          "Dashboards & reporting", "Workshop", "Referral partnership (accountants, bookkeepers, IT providers)", "Something else"]
EXPECT = [
    ("Reply", "In writing, by the next business day."),
    ("Calls", "20 minutes, early morning or after 5pm, if a call helps."),
    ("Proposal", "Within three business days: fixed price, timeline and definition of done."),
    ("Fit", "If we're not the right fit, we'll say so and point you elsewhere where we can."),
]

# ---------------------------------------------------------------- bill check
BC_LEDE = ("Catch an updated invoice about to be paid twice, or a supplier whose bank details just changed, before the payment run. "
           "Drop in a bills export from Xero, MYOB or QuickBooks, or any spreadsheet saved as CSV. Eight checks run on this "
           "device in a few seconds. Your file isn't uploaded, stored or sent to us.")
BC_CHECKS = [
    "Possible duplicate bills: same supplier, same amount, within 14 days, including an updated invoice sent after the original",
    "The same invoice number used twice by one supplier",
    "A supplier's bank details changing",
    "Bills that look split to stay under your approval limit",
    "Bills just under your approval limit",
    "A large first bill from a supplier first seen in your file",
    "Payments made on a weekend",
    "ABNs missing or failing the check-digit test",
]
BC_FILE = ("In your accounting software, open the bills or supplier invoices list (or a payables report), pick a date range and "
           "export it as CSV. Six or twelve months is a good start. If it only exports to Excel, open the file and save it as CSV. "
           "The check needs a supplier, an amount and a date; invoice numbers, payment dates, bank details and ABNs make it sharper.")
BC_FAQ = [
    ("Is my bills file uploaded anywhere?", "No. The check runs in your browser on your own device. Your file isn't uploaded, stored or sent to Beiz."),
    ("Which accounting software does it work with?", "Any bills or payables export saved as CSV, including from Xero, MYOB and QuickBooks. It needs a supplier, an amount and a date; invoice numbers, payment dates, bank details and ABNs make it sharper."),
    ("Why not paste my bills into ChatGPT?", "You can, but a chat assistant reads a file loosely and can skip or misread rows in a long export. This check runs the same fixed rules on every row, shows each flag with the records behind it, and your file never leaves your device. Check your own obligations before putting supplier bank details or client information into any online AI tool."),
    ("Is this an audit?", "No. It's eight quick checks. A flag is a prompt for a person to look, and many flags will have an innocent explanation."),
    ("What does it cost?", "Nothing. The paid two-week cash and data check goes further, from your full exports, for $1,500 fixed."),
]
BC_LIMITS = ("It's eight quick checks, not an audit. It can't see your bank, your emails or the bills you never entered, and it "
             "doesn't tell you whether anyone did anything wrong. It's general information, not tax, legal or accounting advice, "
             "and you decide what to do with any flag. Xero, MYOB and QuickBooks are named only to describe file formats; "
             "Beiz isn't affiliated with them.")

# ---------------------------------------------------------------- privacy
PRIVACY = """<p>Beiz Data &amp; Accounting Pty Ltd (ABN 53 691 755 496), "we", respects your privacy. This policy explains what we collect, why, and what we do with it. We aim to handle personal information consistently with the Australian Privacy Principles.</p>
<h2>What we collect</h2>
<ul><li><strong>What you send us:</strong> your name, email, organisation and message when you use our contact form or email us.</li>
<li><strong>Engagement information:</strong> if you become a client, the information needed to deliver the work, invoice you and meet our professional obligations.</li></ul>
<h2>What our website does and doesn't do</h2>
<ul><li>We don't use analytics, advertising cookies or tracking pixels.</li>
<li>Fonts and scripts are served from our own site. Pages don't call third-party services when they load.</li>
<li>Our website host (GitHub Pages) may log technical information such as IP addresses for security and operations, under its own privacy statement.</li>
<li>The free bill check runs entirely in your browser. Nothing is sent to us unless you choose to send it through the contact form or email.</li>
<li>When you send the contact form, it goes through a Google Apps Script on our Google Workspace account and lands in our inbox. If that fails, your email app opens with the message filled in instead.</li></ul>
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
<p>We don't use computer programs to make decisions about individuals that could significantly affect their rights or interests.</p>"""

# ---------------------------------------------------------------- old URLs -> new pages
REDIRECTS = {'/ai-check/': '/services/',
 '/ai-cost-calculator/': '/prices/',
 '/ai-value-calculator/': '/prices/',
 '/aml-ctf-accounting-firms/': '/services/',
 '/ask-ai/': '/about/',
 '/cash-data-check/': '/prices/',
 '/compliance-sprint/': '/services/',
 '/examples/': '/services/',
 '/faq/': '/how-we-work/',
 '/industries/': '/services/',
 '/industries/crypto/': '/services/',
 '/industries/health/': '/services/',
 '/industries/hospitality-retail/': '/services/',
 '/industries/not-for-profits/': '/services/',
 '/industries/startups/': '/services/',
 '/industries/trades/': '/services/',
 '/insights/': '/',
 '/insights/burned-by-an-ai-product/': '/',
 '/insights/check-bills-before-you-pay/': '/',
 '/insights/privacy-act-automated-decisions/': '/',
 '/insights/shortcut-to-a-good-ai-tool/': '/',
 '/insights/we-feed-your-tax-accountant/': '/',
 '/insights/why-13-weeks/': '/',
 '/leave-cover/': '/services/',
 '/live/': '/',
 '/oversight/': '/how-we-work/',
 '/products-demos/': '/bill-check/',
 '/products-demos/ai-workflow/': '/bill-check/',
 '/products-demos/enquiry-assistant/': '/bill-check/',
 '/products-demos/job-profitability/': '/bill-check/',
 '/products-demos/missing-receipts/': '/bill-check/',
 '/services/ai-agents/': '/services/',
 '/services/ai-governance/': '/services/',
 '/services/ai-readiness-sprint/': '/services/',
 '/services/automation/': '/services/',
 '/services/cash-and-job-profit-model/': '/services/',
 '/services/chatbots-ai-assistants/': '/services/',
 '/services/coaching/': '/services/',
 '/services/dashboards-and-models/': '/services/',
 '/services/data-engineering/': '/services/',
 '/services/human-in-the-loop/': '/services/',
 '/services/privacy-sprint/': '/services/',
 '/services/project-delivery/': '/services/',
 '/services/quick-wins/': '/services/',
 '/services/speaking/': '/services/',
 '/services/workflow-redesign/': '/services/',
 '/services/workshops/': '/services/',
 '/trust/': '/how-we-work/',
 '/try/': '/bill-check/',
 '/workshop/': '/services/',
 '/workshops-speaking/': '/services/'}

LLMS = """# Beiz Data & Accounting

> AI for real business work, with guardrails, set up and checked by an Australian Chartered Accountant. Canberra, working Australia-wide.

Beiz Data & Accounting Pty Ltd (ABN 53 691 755 496) sets up AI agents for routine finance and admin work: bills, cash, reconciliations and client checks. Each agent has a written job description and limits, is tested on the client's past records, runs in shadow mode first, and needs a person's sign-off for anything that matters. Principal: Purav Mehta, Chartered Accountant (CA ANZ) with a Certificate of Public Practice, GAICD. Not registered for GST; prices are AUD with no GST added.

Beiz does not provide tax returns, BAS or GST lodgements, tax or BAS agent services, statutory audit or assurance, legal advice or financial product advice.

## Pages
- [Home](https://beiz.com.au/)
- [Services](https://beiz.com.au/services/): finance, AI agents and automation, data and reporting, governance, workshops
- [How it works](https://beiz.com.au/how-we-work/): first 30 days and what every build includes
- [Prices](https://beiz.com.au/prices/): free bill check; $1,500 fixed two-week cash & data check; compliance controls sprint from $3,500; cash & job profit model, AI workforce setup, leave cover and monthly controls operations by scoped quote
- [Free bill check](https://beiz.com.au/bill-check/): runs in the browser, nothing uploaded
- [About](https://beiz.com.au/about/)
- [Contact](https://beiz.com.au/contact/): hello@beiz.com.au
- [Full detail for AI assistants](https://beiz.com.au/llms-full.txt)
"""

# ---------------------------------------------------------------- added 5 Nov 2026 (Reddit research, Purav's go)
RULES_FIRST = [
    ("Rules first", "Fixed rules do the routine checking: matching amounts, dates, suppliers and invoice numbers. They behave the same way every time and cost nothing to run."),
    ("AI for the exceptions", "AI only looks at what the rules can't settle, like a supplier invoice laid out in an unusual way. It hands back a structured answer for the rules to check again."),
    ("Figures from PDFs", "PDF tables are positions on a page, not a spreadsheet, which is why general AI tools often misread them. Tables are read separately from the text, and every figure keeps a link to its document, page and line before it's checked against your ledger."),
    ("A person decides", "Anything held, unusual or over your limit goes to a named person, and a hold always wins: nothing further down the line can release it. Every run is kept in a history your staff can read, step by step."),
]
HOME_BC = [
    "An updated invoice about to be paid twice",
    "The same invoice number used twice by one supplier",
    "A supplier's bank details changing",
    "Bills split to stay under your approval limit",
]

# ---------------------------------------------------------------- interactive hero (5 Nov 2026, Purav's request)
# Decision-log examples come from the same made-up business as /data/sample-bills.csv.
LOG_FIELDS = [
    ("Record", "The bill: supplier, invoice number, date and amount."),
    ("Check", "The rule that ran, in plain words."),
    ("Finding", "What the check saw in the records, with the records it compared."),
    ("Status", "ok, held for a person, or stopped before payment."),
    ("Who decides", "The named person who clears it, and what they do next. Their decision is logged with their name and the time."),
]
HERO_LOG = {
    "ok": {
        "row": "Matched to supplier and order",
        "log": [("Record", "Gecko Fleet Fuel &middot; GF1434 &middot; 6 Apr 2026 &middot; $537.22"),
                ("Check", "Supplier known, invoice number not seen before, amount in the usual range, bank details unchanged"),
                ("Finding", "Nothing unusual against the supplier's last 26 bills"),
                ("Status", "ok: ready for the normal payment run"),
                ("Who decides", "No action needed. Still logged, so the record shows it was checked")],
        "acts": [("Open the bill check", "/bill-check/")],
    },
    "held": {
        "row": "Held for a person: possible duplicate or over limit",
        "log": [("Record", "Wattlebird Electrical &middot; INV-2207A &middot; 19 Aug 2026 &middot; $3,960.00"),
                ("Check", "Same supplier, same amount, within 14 days of another bill"),
                ("Finding", "Matches INV-2207 from 12 Aug 2026 for $3,960.00. Looks like an updated invoice sent after the original"),
                ("Status", "held: not in the payment run until a person decides"),
                ("Who decides", "The accounts payable lead: pay it, or mark it as a duplicate")],
        "acts": [("Mark as duplicate", "demo"), ("Approve to pay", "demo")],
    },
    "stop": {
        "row": "Stopped: supplier bank details changed",
        "log": [("Record", "Bluetongue Plumbing &middot; BT1911 &middot; 25 Aug 2026 &middot; $2,423.87"),
                ("Check", "Bank details compared with the supplier's previous bills"),
                ("Finding", "Account changed from BSB 062-208, account ending 4580 (9 bills since April) to BSB 082-991, account ending 1192"),
                ("Status", "stopped: kept out of the payment file"),
                ("Who decides", "The owner rings the supplier on a number already on file, never one from the email, before anything is paid")],
        "acts": [("Ring the supplier first", "demo"), ("Open the bill check", "/bill-check/")],
    },
}
DEMO_ACT_NOTE = "Demo only. In a real setup this decision is logged with your name and the time. Nothing is paid or sent."

# ---------------------------------------------------------------- technical view, agent tools
TECH_PLAIN = ("Every check an agent runs leaves a record: what it looked at, the rule it used, what it found, and who decided. "
              "That record lives in your own accounts, not ours. The free bill check runs entirely in your browser; your file isn't sent anywhere.")
LOG_SCHEMA = """{
  "record":      { "supplier": "Bluetongue Plumbing", "invoice": "BT1911",
                   "date": "2026-08-25", "amount_aud": 2423.87 },
  "check":       "bank_details_changed",
  "finding":     "BSB/account differs from the supplier's previous 9 bills",
  "status":      "stopped",
  "who_decides": { "role": "owner", "decision": null, "decided_at": null }
}"""
AGENT_TOOLS = [
    ("get_beiz_services", "Company facts, prices and what Beiz doesn't do, from this site."),
    ("get_bill_check_rules", "The eight checks the free bill check runs, and how your file is handled."),
    ("privacy_adm_overview", "General information on the Privacy Act automated-decision rules starting 10 December 2026, with the OAIC source. Not legal advice."),
]
