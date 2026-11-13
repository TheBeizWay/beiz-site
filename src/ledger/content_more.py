"""beiz.com.au content, "Ledger" edition: service, industry, insight, FAQ and workshop pages.

Restored 5 Nov 2026 (Purav: "I want a multiple page website"; chose service pages, insights, industries, FAQ
and workshops). Wording comes from the pages archived that morning (_archive/), with links to removed demos,
calculators and the Ask-AI block taken out. Prices are only the ones already on /services/ and /prices/.
Australian English. Plain words. No invented clients or results: industry examples are made up and say so.
"""

STEPS = [
    ("Talk or write", "A 20-minute call or a few lines in writing. A written reply by the next business day."),
    ("Fixed proposal", "Within three business days: fee, timeline and definition of done."),
    ("Build and test", "In your own tools, tested on your past records. Anything involving AI runs alongside your team first."),
    ("Hand over", "Documentation, procedures and a review once it's running."),
]

# ---------------------------------------------------------------- service pages
# Standard service page: who, problem, gets, limits, then STEPS and price.
# "extra" sections (label, h2, html) go after "What you get"; "custom" replaces the standard body entirely.
SERVICES = [
    {"path": "/cash-data-check/", "group": "Finance and decisions", "name": "Two-week cash &amp; data check",
     "title": "Two-week cash & data check | Beiz",
     "desc": "Bills, invoices and timesheets checked against each other, with every finding traced to its record. Two weeks, fixed fee, from exports.",
     "lede": "Your bills, invoices and timesheets checked against each other, with every finding traced to its record.",
     "who": "Owners and finance leads of businesses that bill time or fixed fees.",
     "problem": "Bills, timesheets and invoices sit in different systems, so nobody can say which hours never reached an invoice or which bills don't match the job.",
     "gets": ["Bills, invoices and timesheets joined from your exports",
              "A findings register: each item confirmed, needing information or explained, with the record behind it",
              "A short read-out of what to look at first"],
     "limits": ["Works from exports, with no logins to your ledger",
                "Reports what the records support; some findings need your explanation before action",
                "No tax or BAS advice"],
     "price": "$1,500 fixed", "timing": "Two weeks",
     "price_extra": "Credited once against your next Beiz build (cash model, AI workforce setup, compliance sprint or leave cover setup) if you accept the proposal and pay the deposit within 60 days of the findings. Not redeemable for cash; not for monthly support.",
     "topic": "Two-week cash & data check"},
    {"path": "/services/cash-and-job-profit-model/", "group": "Finance and decisions", "name": "Cash &amp; job profit model",
     "title": "Cash & job profit model | Beiz Data & Accounting",
     "desc": "A 13-week cash view and profit by job or client, tied back to the ledger and refreshed from your weekly exports. Scoped quote.",
     "lede": "A 13-week cash view and profit by job or client, tied back to the ledger.",
     "who": "Businesses that need to see cash and job margins ahead, not after month-end.",
     "problem": "The bank balance and last month's profit and loss don't show which week cash gets tight or which jobs make money.",
     "gets": ["A 13-week cash forecast that refreshes from your weekly exports",
              "Profit by job or client, reconciled to the ledger",
              "Written assumptions and a handover session"],
     "limits": ["A model and its assumptions, not financial product advice",
                "You run it after handover; ongoing review only where agreed in writing"],
     "price": "Fixed fee", "timing": "Fixed scope in writing",
     "price_extra": "You drop in fresh exports weekly and the model refreshes. Beiz reviews the forecast only where the support agreement sets out how often and what.",
     "topic": "Cash & job profit model",
     "related": [("/insights/why-13-weeks/", "Why 13 weeks? Your cash cycle in plain English")]},
    {"path": "/leave-cover/", "group": "Finance and decisions", "name": "Leave cover",
     "title": "Finance leave cover | Beiz Data & Accounting",
     "desc": "When someone in finance goes on leave, an agent carries the routine part of their role, a Chartered Accountant reviews its work, and it's handed back the day they return.",
     "h1": "Someone's going on leave. The work doesn't have to stop.",
     "lede": "Parental leave, long service leave, a month in Europe. Bills still arrive, invoices still need to go out and someone has to watch the cash. An agent carries the routine part of their role, an Australian Chartered Accountant reviews its work, and everything is handed back the day they return.",
     "custom": [
         ("How it works", "Before, during and after", "rows:" ),
         ("Their job stays theirs", "The agent covers routine work only", "p:Decisions, customers and anything about people stay with your team. Best booked three to four weeks before the leave starts."),
     ],
     "rows": [("Before they go", "We shadow them for a week and write the agent's job description from how they actually do the work. They sign it off."),
              ("While they're away", "The agent matches bills, drafts invoices and reminders and keeps the reconciliation current. Anything unusual is held for a named person. You get a one-page update every Friday."),
              ("When they're back", "A handover note: what was done, what was held and what's waiting. The agent can stay on to help them, or be switched off.")],
     "price": "Fixed fee", "timing": "Best booked three to four weeks ahead",
     "topic": "Leave cover"},
    {"path": "/services/ai-readiness-sprint/", "group": "AI agents and automation", "name": "AI workforce setup",
     "title": "AI workforce setup: AI agents with a Chartered Accountant in the loop | Beiz",
     "desc": "AI agents for routine finance work, each with a job description, limits, a test on your past records and shadow mode first. Three-week rollout; scoped quote.",
     "h1": "Your AI workforce, set up properly, on a three-week rollout plan.",
     "lede": "Start with one defined workflow. We set up its agent, access, approval steps and tests inside the tools you already use, plus limits, approvers and a decision log for the AI already inside your software, like Xero and Microsoft 365. Further agents, and monthly monitoring, are scoped and priced separately.",
     "price": "Fixed fee", "timing": "Three-week rollout, subject to scope and system access",
     "price_extra": "Setup is fixed and quoted in writing after scoping. Monthly monitoring and review is quoted separately. Built in your accounts, with no lock-in.",
     "topic": "AI workforce setup", "ai_workforce": True},
    {"path": "/services/workflow-redesign/", "group": "AI agents and automation", "name": "Workflow review &amp; redesign",
     "title": "Workflow review & redesign | Beiz Data & Accounting",
     "desc": "One process mapped end to end, with the handoffs, re-keying and waiting taken out before anything is automated.",
     "lede": "One process mapped end to end, with the handoffs, re-keying and waiting taken out before anything is automated.",
     "who": "Small businesses, startups and solo operators whose admin keeps growing with the work.",
     "problem": "The same information is typed into several places, jobs wait on one person, and nobody can see where time goes.",
     "gets": ["A map of the current process and where time and errors build up",
              "A redesigned process with named owners and approval points",
              "A short list of what to automate, what to simplify and what to leave alone"],
     "limits": ["Recommendations and design; building them is scoped separately", "Your people decide what changes"],
     "price": "Fixed fee", "timing": "Set in your written proposal", "topic": "Automation & AI agents"},
    {"path": "/services/automation/", "group": "AI agents and automation", "name": "Workflow automation",
     "title": "Workflow automation | Beiz Data & Accounting",
     "desc": "One repetitive finance or admin workflow automated, tested on your past records and handed over, with approval steps for anything touching money.",
     "lede": "One repetitive finance or admin workflow automated, tested and handed over.",
     "who": "Teams doing the same matching, chasing and checking every week.",
     "problem": "Routine steps take hours and errors surface late.",
     "gets": ["One workflow mapped, built and tested on your past records",
              "Approval steps and limits for anything touching money or customers",
              "A log of what ran and what was held for a person",
              "A runbook and handover"],
     "limits": ["Nothing is paid or sent without a person", "No payments initiated from your bank accounts by software"],
     "price": "Fixed fee", "timing": "Set in your written proposal", "topic": "Automation & AI agents",
     "related": [("/insights/check-bills-before-you-pay/", "Five checks to run on every supplier bill before you pay it")]},
    {"path": "/services/chatbots-ai-assistants/", "group": "AI agents and automation", "name": "Chatbots &amp; AI assistants",
     "title": "Chatbots & AI assistants | Beiz Data & Accounting",
     "desc": "One assistant for one defined task, answering only from information you approve, tested against questions it should refuse, with a hand-over to a person.",
     "lede": "Answers from approved business information only, with clear limits and a hand-over to a person.",
     "who": "Small businesses and startups answering the same questions by email, phone and chat, or whose team keeps searching for the same internal information.",
     "problem": "Generic chat widgets guess when they don't know, can be talked into ignoring their rules, and leave staff to untangle half-captured enquiries.",
     "gets": ["One assistant for one defined task: a customer enquiry assistant, an internal knowledge assistant, or a workflow assistant that prepares actions for approval",
              "An approved knowledge pack, with every answer linked to its source",
              "Tested against real questions, including ones it should refuse, and attempts to override its instructions",
              "A clear hand-over to a person, with an enquiry summary they can act on",
              "A usage and cost cap, logging you control, and a written runbook"],
     "limits": ["Answers only from information you approve; says so when it doesn't know",
                "Doesn't send messages, book jobs, take payments or change records without a person approving",
                "No financial, legal or tax advice to your customers",
                "Model, hosting and data-retention choices agreed with you before anything goes live"],
     "price": "Fixed fee", "timing": "Set in your written proposal", "topic": "Automation & AI agents"},
    {"path": "/services/data-engineering/", "group": "Data and reporting", "name": "Data engineering",
     "title": "Data engineering | Beiz Data & Accounting",
     "desc": "Your accounting software, CRM, job app and spreadsheets connected into one clean source, with checks that flag missing or odd records.",
     "lede": "Your accounting software, CRM, job app and spreadsheets connected into one clean source.",
     "who": "Teams whose numbers live across several systems and spreadsheets.",
     "problem": "Every report starts with copy and paste, and the same figure means different things in different systems.",
     "gets": ["A map of systems, owners and where the numbers disagree",
              "A plain-English data dictionary",
              "Scheduled pipelines with checks that flag missing or odd records",
              "One clean source for reports, models and AI tools"],
     "limits": ["Built in your own accounts; you keep the code and documentation", "Source records are never changed"],
     "price": "Fixed fee", "timing": "Set in your written proposal", "topic": "Dashboards & reporting"},
    {"path": "/services/dashboards-and-models/", "group": "Data and reporting", "name": "Dashboards &amp; management reporting",
     "title": "Dashboards & management reporting | Beiz Data & Accounting",
     "desc": "A reporting pack or dashboard on agreed definitions, reconciled to the ledger, in tools you already use.",
     "lede": "A reporting pack or dashboard on agreed definitions, reconciled to the ledger.",
     "who": "Owners, boards and finance leads who want one view they can trust.",
     "problem": "Reports arrive late, disagree with each other or answer last month's question.",
     "gets": ["A dashboard or report pack on agreed definitions",
              "Reconciliation back to the ledger",
              "Notes on what each measure means and where it comes from"],
     "limits": ["Built in tools you already use, such as Excel or Power BI, where practical",
                "Commentary and decisions stay with your team"],
     "price": "Fixed fee", "timing": "Set in your written proposal", "topic": "Dashboards & reporting"},
    {"path": "/compliance-sprint/", "group": "Governance", "name": "Compliance controls sprint",
     "title": "Compliance controls sprint | Beiz",
     "desc": "Two weeks on one obligation: AI use, AML/CTF Tranche 2 or the Privacy Act automated-decision rules. What's in scope, who owns it and where a person must approve.",
     "lede": "One obligation mapped in two weeks: AI use, AML/CTF Tranche 2 or the Privacy Act automated-decision rules.",
     "who": "Businesses facing one specific obligation now.",
     "problem": "It is unclear what is in scope, who owns it and where a person must approve.",
     "gets": ["A register of what is in scope",
              "Named owners, rules and approval points",
              "A 90-day plan and the first workflow worth running under controls"],
     "limits": ["General information and controls design, not legal advice; legal interpretation stays with your adviser",
                "No ledger access needed"],
     "price": "From $3,500", "timing": "Two weeks", "topic": "Compliance controls sprint",
     "related": [("/aml-ctf-accounting-firms/", "AML/CTF Tranche 2 for accounting firms"),
                 ("/insights/privacy-act-automated-decisions/", "Privacy Act automated decisions from 10 December 2026")]},
    {"path": "/aml-ctf-accounting-firms/", "group": "Governance", "name": "AML/CTF for accounting firms",
     "title": "AML/CTF Tranche 2 for accounting firms | Beiz",
     "desc": "Which accounting services are caught by AML/CTF Tranche 2 since 1 July 2026, what firms must do, and where an agent helps and where it stops. General information, sourced to AUSTRAC.",
     "h1": "AML/CTF for accounting firms, without a compliance team.",
     "lede": "Since 1 July 2026, accounting firms that set up companies and trusts, act as directors or trustees, or help clients buy and sell businesses have AML/CTF obligations. Agents can do the routine checks and paperwork. Your compliance officer keeps every decision.",
     "price": "", "topic": "AML/CTF Tranche 2", "aml": True},
    {"path": "/services/ai-governance/", "group": "Governance", "name": "AI governance for boards &amp; owners",
     "title": "AI governance for boards & owners | Beiz Data & Accounting",
     "desc": "A register, policy and reporting line for the AI already in use, including staff pasting client records into public AI tools.",
     "lede": "A register, policy and reporting line for the AI already in use, including staff pasting client records into public AI tools.",
     "who": "Boards, directors and owners who need to oversee AI use.",
     "problem": "AI is already inside staff habits and software, with no register, policy or board reporting.",
     "gets": ["An AI register and automated-decision map", "An AI use policy and control set", "A board reporting format"],
     "limits": ["Not legal advice", "Running the controls each month is a separate, scoped arrangement"],
     "price": "Fixed fee", "timing": "Set in your written proposal", "topic": "Compliance controls sprint",
     "related": [("/insights/shortcut-to-a-good-ai-tool/", "Six questions to ask before any AI tool touches your money")]},
]

AIW_AGENTS = [
    ("Data scientist agent", "Cleans your exports, joins the records, builds the cash and margin models and flags outliers. Never changes a source record."),
    ("Financial controller agent", "Reconciles bank to ledger, matches bills to orders and timesheets, and prepares the month-end checklist. Never posts a journal or releases a payment."),
    ("CFO desk agent", "Drafts the weekly cash view, board pack numbers and variance notes. Never sends anything to your board, bank or investors."),
    ("Systems agent", "Watches integrations, data feeds and who has access, and flags new AI tools staff start using. Never changes a permission or a setting."),
    ("Compliance agent", "Prepares AML/CTF client checks and screening, sets monitoring dates and files the evidence. Never clears a possible match or accepts a high-risk client."),
    ("Risk officer agent", "Keeps the controls register current, logs every exception and drafts the monthly risk report. Never signs off its own controls."),
]
AIW_CONTROLS = [
    ("A named role and owner", "A written job description: what the agent does, the tools it may use, and the person it reports to."),
    ("Limits it can't cross", "Read-only access where possible, and a delegation limit. Changed bank details, new suppliers and anything over the limit always go to a person. AI usage is billed by volume, so each agent also gets a monthly spending cap, logged usage and an off switch you control."),
    ("Human checkpoints", "Anything that moves money, reaches a customer or decides something about a person waits for a human yes."),
    ("A log of every decision", "What the agent did, why, and who approved it, kept in your own accounts."),
    ("Tested before it goes live", "We run the agent over a few months of your past records and check each result against what actually happened. It moves on only when it meets a pass mark agreed with you in writing, and it's re-tested before any change."),
    ("Monthly monitoring and review", "We read the log, check for drift and errors, and adjust the limits. Rules like the Privacy Act's automated-decision disclosures are covered as they apply to you."),
]
AIW_WEEKS = [
    ("Week 1: map and limit", "We list the repetitive work, pick the agents worth having, and write each job description with you."),
    ("Week 2: test and shadow", "First the agents run over your past records and we check their results against what actually happened. Then they run alongside your team without acting, and we compare their answers with yours."),
    ("Week 3: live within limits", "The agents start work. Anything over a limit comes to a person."),
    ("Day 30: review", "Errors, time saved and exceptions, measured. We fix what isn't working and tell you plainly whether to add more."),
]
AIW_SKIP = ("Getting an agent to work in a demo is the easy part. Most of the setup is what keeps it working after week one: "
            "checking inputs before it acts, holding anything it isn't sure about, logging every decision, failing safely when a "
            "supplier sends a scanned PDF or a system is down, and a person reviewing the exceptions. Purav is the one on your calls "
            "and the one who builds those checks.")
AIW_NO_AGENT = ["The work happens in one system, on a simple rule: the bank rules and bill approvals built into your accounting software.",
                "One person needs help drafting, summarising or searching: the AI licence your team already pays for.",
                "It happens a few times a month and a checklist would do."]
AIW_AGENT = ["The work crosses systems: ledger, job or practice software, inbox and screening service.",
             "Records have to be checked against each other before anyone acts.",
             "Your limits and approvers have to be enforced every time, with a log someone can review later."]
AIW_ISNT = ("It isn't an audit or assurance engagement, custom software that needs a development team, or a licence sale. "
            "You buy any subscriptions directly, in your name. We don't do tax returns or BAS. If your own software can do it, "
            "we'll say so on the fit call and you won't pay for a build.")
AIW_GETS = [
    ("Agent job descriptions", "Role, tools, limits and owner for each agent, agreed with you."),
    ("Working agents", "Built in your own accounts and tools."),
    ("Approval steps", "Money, customers and people always need a human yes."),
    ("Test results", "How each agent did on your past records, before it went live."),
    ("Your operating folder", "Plain files you own: your business context, your procedures written as skills, and the agent's memory. Any major AI tool can read them, so you're not locked in."),
    ("Decision log", "Every action recorded, in your accounts."),
    ("AI use policy and training", "One page your team can follow, plus a session on the agents."),
    ("Day-30 review", "Errors, time saved and exceptions, measured."),
]
AIW_FRAMEWORKS = [
    ("https://www.industry.gov.au/publications/guidance-for-ai-adoption", "Guidance for AI Adoption", "National AI Centre, Australia. The government's practical starting point for businesses using AI."),
    ("https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-the-use-of-commercially-available-ai-products", "Privacy and commercially available AI products", "OAIC. What the Privacy Act expects when you put personal information into AI tools."),
    ("https://www.unesco.org/en/artificial-intelligence/recommendation-ethics", "Recommendation on the Ethics of AI", "UNESCO. A global standard on human oversight, transparency, fairness and privacy."),
    ("https://www.nist.gov/itl/ai-risk-management-framework", "AI Risk Management Framework", "NIST, United States. Four functions, Govern, Map, Measure and Manage, that we use to structure each agent's risk register."),
    ("https://www.iso.org/standard/42001", "ISO/IEC 42001", "The international management-system standard for AI, for organisations that want to be assessed against one."),
]

# AML/CTF page (sources checked 16 October 2026 when first published)
AUSTRAC_SUMMARY = "https://austrac.gov.au/node/1158"
AUSTRAC_ENROL = "https://www.austrac.gov.au/new-and-media/news/austrac-opens-enrolment-new-professions-next-step-aml-reforms"
AUSTRAC_SMR = "https://www.austrac.gov.au/sites/default/files/2025-12/AUSTRAC%20Suspicious%20Matter%20Reporting%20-%20Reference%20Guide%20December%202025.pdf"
AML_SPLIT = [("What the agents do", "Check whether the service is caught, confirm the client and its owners, run the screening, draft the risk rating, file the evidence and set the next monitoring date."),
             ("What stays with your people", "Every possible match, every high-risk client and the decision to take the work on. Your AML/CTF compliance officer stays accountable; we prepare, check and keep the record.")]
AML_CAUGHT = ["Setting up or restructuring companies, trusts and partnerships",
              "Acting as a director, company secretary, trustee or partner for a client, or arranging for someone else to",
              "Acting as a nominee shareholder, or arranging one",
              "Providing a registered office or principal place of business address",
              "Helping a client buy, sell or transfer a business, or interests in a company or trust",
              "Helping with equity or debt financing",
              "Receiving, holding or controlling client money or property as part of those services",
              "Helping a client buy, sell or transfer real estate"]
AML_DATES = [("1 July 2026", "Obligations started."),
             ("Within 28 days", "Of first providing a regulated service: enrol with AUSTRAC."),
             ("Every three years", "Independent evaluation of your program.")]
AML_DUTIES = [
    ("Enrol with AUSTRAC", "Within 28 days of first providing a regulated service."),
    ("An AML/CTF program", "A written risk assessment and policies, approved by a senior manager, kept up to date and independently evaluated at least every three years."),
    ("A compliance officer", "A fit and proper person who runs the program day to day. In a sole practice, that can be the principal."),
    ("Customer due diligence", "Identify and verify the client, and the people who own or control it, before you provide the service. Then keep monitoring."),
    ("Reports", "A suspicious matter report within three business days (24 hours for terrorism financing), and a threshold transaction report for physical cash of $10,000 or more."),
    ("Records and an annual report", "Keep records for at least seven years, and report each year on how you met your obligations."),
]
AML_TABLE = [
    ("Is this engagement a regulated service?", "Asks the intake questions and suggests the answer", "Decides"),
    ("Identify the client and its owners", "Collects and checks documents, drafts the ownership chart", "Reviews anything that doesn't match"),
    ("Screening for politically exposed persons and sanctions", "Runs the screen and records the result", "Clears or escalates every possible match"),
    ("Risk rating", "Drafts the rating with its reasons", "Approves it, and decides on every high-risk client"),
    ("Ongoing monitoring", "Sets review dates, chases expired documents, flags changes", "Decides what changes the risk"),
    ("Unusual activity", "Flags it to the compliance officer and never contacts the client about it", "Decides whether to report"),
    ("Records", "Files the evidence: who did what, when and why", "Owns them"),
]
AML_COSTS = [
    ("Compliance controls sprint, AML/CTF focus", "Two weeks. Which of your services are caught, how new clients are checked today, who owns each step, where a person must approve, the records you keep, and a 90-day plan for the first controlled workflow.", "Fixed fee", "/compliance-sprint/"),
    ("AI workforce setup, compliance agent", "The agent's job description, limits and decision log, rolled out over three weeks: map and limit, a test on your past records and shadow mode, then live within limits.", "Fixed fee", "/services/ai-readiness-sprint/"),
    ("Monthly controls operations", "We keep screening, monitoring dates and records current, review the agent's decisions and send you one page a month.", "Fixed fee", "/prices/"),
]
AML_NOT = ("We don't act as your AML/CTF compliance officer, write the legal wording of your program or decide whether to report. "
           "Program wording stays with your adviser or lawyer; we hand them the facts. This page is general information, not legal advice.")
AML_FAQ = [
    ("We only do tax returns, BAS and bookkeeping. Are we caught?", "Probably not, on those services alone. It turns on what you do, not on being an accountant. If you provide any of the services listed above, even occasionally, check them with AUSTRAC's guidance or your adviser."),
    ("Can an AI agent be our AML/CTF compliance officer?", "No. The compliance officer has to be a fit and proper person. The agent prepares the checks; your officer makes the decisions and signs off."),
    ("What about clients we had before 1 July 2026?", "AUSTRAC's summary says you generally only need to do due diligence on existing clients when a suspicious matter report is due or their risk changes significantly to medium or high."),
    ("Do you need access to our ledger or client files?", "Not for the sprint. It runs on short interviews and the documents you already have. If you go on to set up an agent, it works inside your own systems and screening service, with access agreed in writing."),
]

# ---------------------------------------------------------------- workshops, coaching and speaking
WORKSHOPS_LEDE = ("Practical sessions on putting AI and data to work in finance and small business. Worked examples use made-up data, "
                  "so your people can run more of it themselves.")
WORKSHOPS = [
    {"name": "From manual task to tested AI workflow",
     "for": "Owners, operations and finance staff in small businesses and startups who repeat the same admin every week.",
     "will": ["Choose one workflow worth automating, and one to leave alone", "Map its steps, data and exceptions",
              "Decide where a person must approve, and the limits that apply", "Estimate running cost and time released with your own figures",
              "Leave with a completed Automation Candidate Canvas"],
     "agenda": ["Where AI helps in admin and finance work, and where it doesn't: a live walk-through on made-up data",
                "Map one of your processes (exercise)", "Exceptions, approval points and what gets logged (exercise)",
                "Running costs and time released, with your own figures", "Your canvas and next steps"],
     "format": "Half day, or two 90-minute sessions. Online or in person. Small groups so everyone works on their own process.",
     "take": ["Your completed Automation Candidate Canvas", "A controls checklist: limits, approvals, logging, off switch", "The slides"]},
    {"name": "From spreadsheet reporting to decision-ready dashboards",
     "for": "Owners and finance leads who report from spreadsheets and want numbers they can act on.",
     "will": ["Agree the handful of measures that drive your decisions", "Define each measure so it means the same thing every month",
              "Spot the data-quality problems that make reports untrustworthy", "See a worked dashboard built on made-up data",
              "Set a simple refresh and review routine"],
     "agenda": ["What decisions your reports should support", "Measures and definitions (exercise)",
                "Data sources and quality checks (exercise on a sample export)", "Worked example: from export to dashboard, on made-up data",
                "Your measure sheet and next steps"],
     "format": "Half day, online or in person. Works best with your finance lead and one person who uses the reports.",
     "take": ["A measure-definition sheet for your business", "A data-quality checklist", "The worked example's structure to reuse"]},
]
COACHING = {"for": "Accountants and finance leads building practical data and AI skills.",
            "format": "A short series of one-to-one sessions, agreed in advance, each tied to something you're building.",
            "leave": ["A working model, report or automation built by you, on made-up or approved data",
                      "Your build reviewed and explained, with the reasoning written down", "A plan for the next skill to practise"],
            "limits": "Skills coaching only: not career, financial or legal advice. No employer or client confidential data in sessions."}
SPEAKING = {"for": "Event organisers, professional bodies, industry groups and boards.",
            "topics": ["What changes when AI enters the finance workflow, and what shouldn't",
                       "Testing, limits and approval points before an AI system goes live",
                       "Getting your data in shape before you automate anything"],
            "formats": "Keynote, workshop-style session, panel or fireside Q&amp;A, tailored to the audience, with worked examples on made-up data."}

# ---------------------------------------------------------------- FAQ
FAQ = [
    ("Are you an AI company?", "We don't make or sell AI software, and we're not tied to any vendor. We set AI up properly for your business: we pick the right tools, connect them to your systems and your team, build the automations, dashboards and agents, and put the controls an accountant would expect around them."),
    ("What does Beiz actually do?", "We're accountants who build the systems behind a business's money: automation that does the grunt work, dashboards and forecasts that show what's coming, and the controls that keep AI safe. We don't do tax."),
    ("Isn't a Chartered Accountant just a tax accountant?", "Tax is one thing a Chartered Accountant can do, and we don't do it at all. A Chartered Accountant is trained in audit, risk, systems, forecasting and business advice. GAICD means we're also trained in how boards govern a business and oversee risk."),
    ("Who's behind Beiz?", "Beiz is led by Purav Mehta, an Australian Chartered Accountant and a graduate of the Australian Institute of Company Directors, with a background in internal audit, fraud and controls, corporate finance, project portfolio governance and data science. Your written proposal confirms who does the work, and you can verify his credentials before you sign anything."),
    ("Is my data safe with AI?", "We only use business-grade AI services whose terms stop your data being used to train models, and we build inside your own Microsoft, Google or Xero accounts wherever we can. Sensitive steps stay with a human."),
    ("What happens if the AI gets it wrong?", "It will, sometimes. That's why every build has approval steps, limits and a log. The AI prepares the work, a person signs it off, and anything unusual gets flagged rather than actioned."),
    ("Do you replace my accountant or bookkeeper?", "No. We don't replace your tax accountant, we feed them. They keep you right with the ATO, looking back at what happened. We work on what happens next week. At year end they get clean, reconciled data and do their job faster."),
    ("Do you do tax, BAS or R&amp;D tax incentive claims?", "No. We don't provide tax agent or BAS services. What we do is make your records clean: crypto transactions reconciled, development costs tagged by project and activity, everything traceable. Your registered tax agent or R&amp;D adviser then works from data they can rely on."),
    ("Doesn't Xero already do a cash forecast?", "Xero's own short-term forecast works mainly from the invoices and bills already entered in Xero. Most cash surprises come from what isn't: payroll and super, the BAS, loan repayments, the big job coming up, and bills nobody has entered yet. We build a 13-week forecast that includes all of it, and a short Monday note that tells you the one thing worth acting on."),
    ("Why 13 weeks?", "It's one quarter, so it always includes a BAS payment, several pay runs and three months of rent and loans. Customers on 30 to 60 day terms pay inside the window, so most of it is money you already know about. It's far enough ahead to act, and near enough to be reliable. Each Monday the oldest week drops off and a new one is added."),
    ("Do you do SMSF work or business valuations?", "No. SMSF advice and audits need licences and registrations we don't hold, and valuations are a specialist field with their own professional standard. What we can do is get your numbers clean and sale-ready, so the valuer, broker or adviser you choose has what they need."),
    ("Which tools do you work with?", "Xero, MYOB, Microsoft 365, Power BI, Google Workspace and the leading business AI tools. We pick what fits what you already own, so there's nothing new to learn unless it earns its place."),
    ("Why do you work in writing first?", "It respects your time and gets better answers. A written brief lets us think properly before replying, and you get a fixed-fee proposal with a clear record of what was agreed, instead of a sales pitch. If a conversation genuinely helps, we'll schedule one."),
    ("Why use an Australian CA rather than just AI or an offshore team?", "Use them too. AI and offshore teams are great for speed and volume. What an Australian Chartered Accountant adds is accountability here: bound by the CA ANZ Code of Ethics, across Australian rules like Payday Super, BAS timing and the Privacy Act, and answerable for the result. If you already outsource, we can set up the access, review steps and checks so it runs safely."),
    ("Is any of the work done offshore?", "Every engagement is scoped, built and signed off by Purav Mehta in Australia. Where outside help is used, it works under his review, only with your written consent, and your engagement letter names who does the work, where, and what they can see."),
    ("How do we find out if all our work has been billed?", "That's the two-week cash and data check. We reconcile timesheets, the job list and the invoices from exports, with no logins. You get a findings register where every gap is marked confirmed, needing information or explained, with the records and the arithmetic behind it."),
    ("Can we see profit by job without hiring a management accountant?", "Often, yes. In most small project businesses the numbers already exist in the accounting software and the job or timesheet app; they just don't agree. We join them, agree one definition of margin, and set up a monthly report reconciled to your accounts, in Power BI or Excel."),
    ("Who owns what you build?", "You own the outcome: the automations, dashboards and models run inside your own accounts, with your logins. The rules, scripts and procedure files for your build are yours to keep and run without us. Our reusable templates, frameworks and code libraries remain our intellectual property, licensed to you for your business. That's how we keep delivery fast and fees fixed."),
    ("Do I need a board or a big business?", "No. Much of what we do is built for sole traders and owner-operators who are flat out and just want the admin to stop eating their evenings. We size the work to the business."),
    ("How much does it cost?", "The two-week cash and data check is $1,500 fixed. The AML/CTF or compliance controls sprint starts from $3,500. Everything else is a fixed fee, set out in a written proposal within three business days of a short scoping conversation, with the timeline and what done looks like. The fee for the two-week cash and data check is credited once against your next build if you accept the proposal and pay the deposit within 60 days of getting the findings. Beiz isn't registered for GST, so no GST is added. <a href=\"/prices/\">How fees work</a>."),
    ("Do you work with crypto businesses?", "Yes: reconciliations, stablecoin payment matching, treasury reporting and controls. We don't give tax, financial product or licensing advice."),
    ("Where are you based?", "Canberra. We work remotely with clients across Australia."),
]

# ---------------------------------------------------------------- industries
INDUSTRIES_LEDE = ("We group clients by the problem they have, not the logo on the van. Every one of them gets the same accounting "
                   "rigour, controls and human sign-off.")
INDUSTRY_GROUPS = [
    ("Regulated and high-stakes", "Governance, audit trails and Privacy Act readiness, where getting it wrong costs trust.", ["/industries/health/", "/industries/not-for-profits/"], "Also: businesses with boards, professional services."),
    ("Transaction-heavy operators", "Reconciliations, margin protection and quote to cash, where small transactions hide where the money goes.", ["/industries/trades/", "/industries/hospitality-retail/"], "Also: e-commerce, childcare and education."),
    ("Tech and digital assets", "Runway modelling, investor metrics, treasury reporting and integrations, where numbers move fast.", ["/industries/startups/", "/industries/crypto/"], ""),
]
INDUSTRIES = [
    {"path": "/industries/trades/", "name": "Trades &amp; construction", "short": "Quotes, job costing, chasing payment",
     "title": "For trades & construction | Beiz Data & Accounting",
     "h1": "You're on the tools all day. The admin shouldn't wait for Sunday night.",
     "lede": "Quotes, job costing, invoicing and chasing payment, set up so they mostly run themselves. You approve, it does the rest.",
     "hear": [("Invoicing lags the work", "The job's done Tuesday, the invoice goes out three weeks later, and you get paid a month after that."),
              ("Chasing money", "You're a tradie, not a debt collector, but there's always money sitting in overdue invoices."),
              ("Quotes that lose money", "The price felt right. Then materials went up, the job ran over, and the margin disappeared.")],
     "build": [("Quote to invoice", "Mark the job done on your phone, and the invoice goes out the same day."),
               ("Automatic reminders", "Polite, then firm, with a pay-now link. You approve the wording once."),
               ("Job costing", "Materials, labour and subbies against each job, so you know what made money."),
               ("Quoting model", "Built from your real past jobs, with contingency that reflects risk."),
               ("Monday cash email", "What's in the bank, what's owed, what's due, before you hit the site."),
               ("Supplier price watch", "Flags when a supplier's prices creep up.")],
     "eg": ("A cabinet-making business, 6 staff",
            ["Invoices typed up on the weekend", "Customers paying a month or more after the job", "A couple of jobs a quarter quietly losing money", "Cash surprises every BAS quarter"],
            ["Invoices out the day the job closes", "Reminders run themselves", "Margin by job, every month", "13-week cash view, no surprises"]),
     "links": [("/services/automation/", "Workflow automation"), ("/services/cash-and-job-profit-model/", "Cash &amp; job profit model")]},
    {"path": "/industries/health/", "name": "Health &amp; allied health", "short": "Billing, rostering, reporting, privacy",
     "title": "For health & allied health providers | Beiz Data & Accounting",
     "h1": "Run the practice, not the paperwork.",
     "lede": "For clinics and allied health practices: bookings, billing reconciliations, rostering and reporting, automated with care. You hold some of the most sensitive information there is, so privacy, AI controls and human sign-off come first.",
     "hear": [("Billing that doesn't reconcile", "Payments, rebates and fund claims arrive in different places, and matching them takes hours."),
              ("No-shows and gaps", "Empty appointments cost money, and nobody has time to chase rebookings."),
              ("AI and patient data", "Staff want to use AI for notes and letters, and you're not sure what's allowed.")],
     "build": [("Billing reconciliation", "Payments matched to appointments automatically, exceptions listed."),
               ("Practice dashboard", "Utilisation, revenue per practitioner and no-show rate, weekly."),
               ("Reminder and rebooking flows", "Using your existing booking system, within its rules."),
               ("AI use policy", "What staff can and can't put into AI tools, in plain English."),
               ("Privacy Act readiness", "Health service providers are generally covered by the Privacy Act regardless of size."),
               ("Controls", "Access, approvals and logs around anything touching patient data.")],
     "eg": ("An allied health practice, 4 clinicians",
            ["Friday afternoons spent reconciling", "No-show rate unknown", "Staff pasting notes into a free chatbot", "Privacy policy last updated years ago"],
            ["Reconciliation done nightly", "No-shows tracked and followed up", "Approved, business-grade AI only", "Policy reviewed for automated decisions"]),
     "links": [("/services/ai-governance/", "AI governance"), ("/insights/privacy-act-automated-decisions/", "Privacy Act automated decisions: a plain-English guide")]},
    {"path": "/industries/hospitality-retail/", "name": "Hospitality &amp; retail", "short": "Wages, suppliers, margins, weekly cash",
     "title": "For hospitality & retail | Beiz Data & Accounting",
     "h1": "Know your numbers before the week gets away from you.",
     "lede": "Wages against sales, supplier price creep, stock and margins, and a weekly cash view. Built from your POS, rostering and accounting systems.",
     "hear": [("Wages creep", "You only find out wages were too high for sales after the pay run."),
              ("Suppliers edging prices up", "A few cents a line, every order, adding up over a year."),
              ("Cash is tight midweek", "Busy weekends, big supplier bills on Tuesday, and no forward view.")],
     "build": [("Wages against sales", "A daily view from your POS and rostering."),
               ("Supplier price watch", "Flags price increases line by line."),
               ("Margin by product", "Which items make money and which just move."),
               ("Weekly cash email", "In the bank, owed, due, and next week's big bills."),
               ("Stock alerts", "Slow movers and reorder points from your sales history."),
               ("Invoice capture", "Supplier bills captured and coded without the shoebox.")],
     "eg": ("A café with two sites",
            ["Wages against sales found out monthly", "Supplier prices unchecked", "Menu priced by gut feel", "Cash crunch every quarter"],
            ["Wages tracked daily against sales", "Price rises flagged on arrival", "Margin by menu item", "13-week cash view"]),
     "links": [("/services/dashboards-and-models/", "Dashboards &amp; management reporting"), ("/insights/check-bills-before-you-pay/", "Five checks to run on every supplier bill")]},
    {"path": "/industries/startups/", "name": "Startups &amp; tech agencies", "short": "Runway, investor metrics, board packs",
     "title": "For startups & tech agencies | Beiz Data & Accounting",
     "h1": "Know your runway before your investors ask.",
     "lede": "Scenario models, investor-ready metrics and board packs, built from your real data. Plus the AI policy and controls that due diligence now asks about.",
     "hear": [("Runway is a guess", "One spreadsheet, one founder who understands it, and no idea what a new hire really does to the numbers."),
              ("Investor metrics on the fly", "MRR, churn and CAC calculated differently every time someone asks."),
              ("Due diligence questions", "Investors and enterprise customers now ask how you govern AI and data. You need a straight answer.")],
     "build": [("Runway and scenario model", "Hiring, ad spend and AI API costs tested over 6, 12 and 24 months."),
               ("Investor metrics", "MRR, net revenue retention, CAC payback, churn and gross margin, calculated the same way every month."),
               ("Board pack", "Monthly, refreshed from your systems, with commentary."),
               ("Data room financials", "Clean, reconciled and documented."),
               ("R&amp;D cost tagging", "Development time and costs tagged by project, ready for your R&amp;D adviser."),
               ("AI governance", "Register, policy and controls for due diligence.")],
     "eg": ("A 12-person software startup",
            ["Runway 'about 18 months'", "Metrics rebuilt before every raise", "R&amp;D costs untangled at year end", "No answer on AI governance"],
            ["Runway shown as a base case and a worst case", "Metrics dashboard, same definitions monthly", "Costs tagged as they happen", "One-page AI governance summary"]),
     "links": [("/services/dashboards-and-models/", "Dashboards &amp; management reporting"), ("/services/ai-governance/", "AI governance")]},
    {"path": "/industries/not-for-profits/", "name": "Not-for-profits", "short": "Grant reporting, board packs, donor data",
     "title": "For not-for-profits | Beiz Data & Accounting",
     "h1": "More time for the mission. Less for the paperwork.",
     "lede": "Grant reporting, board packs and donor data, automated and reconciled, so your team spends its time on the work that matters.",
     "hear": [("Grant acquittals", "Every funder wants a different report, and each one takes days to pull together."),
              ("Board packs", "Volunteer directors need clear numbers, not 40 pages of spreadsheets."),
              ("Donor data everywhere", "The CRM, the payment platform and the ledger never quite agree.")],
     "build": [("Grant tracking", "Spend tagged by grant as it happens, acquittals ready when due."),
               ("Board dashboard", "A few measures directors can read in five minutes."),
               ("Donor reconciliation", "Payments, CRM and ledger matched automatically."),
               ("Cash and reserves forecast", "So the board can see the next 12 months."),
               ("AI use policy", "Sensible rules for staff and volunteers using AI."),
               ("Reporting data", "Ready for your ACNC annual information statement.")],
     "eg": ("A community organisation with 3 grants",
            ["Acquittals built from scratch each time", "Board pack takes a week", "Donor totals don't match the ledger", "Reserves discussed by feel"],
            ["Acquittals from tagged spend", "Board dashboard refreshes itself", "Donors reconciled monthly", "12-month reserves forecast"]),
     "links": [("/services/dashboards-and-models/", "Dashboards &amp; management reporting"), ("/services/ai-governance/", "AI governance")]},
    {"path": "/industries/crypto/", "name": "Crypto &amp; digital assets", "short": "Wallet and stablecoin reconciliations, controls",
     "title": "For crypto & digital asset businesses | Beiz Data & Accounting",
     "h1": "Yes, we work with crypto businesses.",
     "lede": "Reconciliations, treasury reporting and controls for businesses that hold, pay or get paid in digital assets, with the record-keeping discipline an accountant expects.",
     "hear": [("Ledger and chain disagree", "What the wallets say and what the accounts say don't match, and nobody knows why."),
              ("Stablecoin receipts", "Customers pay in USDC or AUD stablecoins, and matching them to invoices is manual."),
              ("Weak controls", "Who can move funds, with whose approval, and where's the record? It's usually one person and a hardware wallet.")],
     "build": [("Wallet reconciliation", "On-chain balances matched to the ledger, differences explained."),
               ("Stablecoin matching", "Incoming payments matched to invoices automatically."),
               ("Treasury reporting", "Holdings, movements and exposure, weekly."),
               ("Transaction records", "Complete, categorised and traceable, ready for your tax agent."),
               ("Controls", "Documented approvals, segregation of duties and access reviews."),
               ("Evidence trail", "The records your auditor will ask for, kept as you go.")],
     "eg": ("A software company paid partly in stablecoins",
            ["Three wallets, one spreadsheet", "Payments matched by hand monthly", "One person can move funds alone", "Year-end records rebuilt from scratch"],
            ["Daily reconciliation to the ledger", "Stablecoin receipts matched on arrival", "Two-person approval, logged", "Clean records for the tax agent"]),
     "note": "We don't provide tax, financial product, investment or licensing advice. We make your records and controls clean so the advisers who do can rely on them.",
     "links": [("/services/automation/", "Workflow automation"), ("/services/dashboards-and-models/", "Dashboards &amp; management reporting")]},
]

# ---------------------------------------------------------------- insights
INSIGHTS_LEDE = "Plain-English notes on cash, controls, data and AI for Australian businesses. General information, not advice."
ARTICLES = [
    {"path": "/insights/privacy-act-automated-decisions/", "date": "2026-10-06", "shown": "Updated 6 October 2026", "mins": 5,
     "title": "Privacy Act automated decisions from 10 December 2026: a plain-English guide",
     "desc": "What the new automated-decision rule means for Australian businesses, the OAIC's three-part test, who it applies to, and five things to do now.",
     "body": """<p>On 10 December 2026, a new transparency obligation in the Privacy Act starts. It came in with the Privacy and Other Legislation Amendment Act 2024, and it's aimed squarely at software that makes decisions about people.</p>
<h2>What the rule says</h2>
<p>If your organisation is covered by the Privacy Act, your privacy policy must explain when you use a computer program to make a decision, or to do something substantially and directly related to making a decision, that could reasonably be expected to significantly affect an individual's rights or interests, where personal information is used.</p>
<p>The policy needs to describe the kinds of personal information used, the kinds of decisions made by the program alone, and the kinds of decisions where the program does something substantially and directly related to the decision.</p>
<h2>The three-part test</h2>
<p>The OAIC's fact sheet, published on 30 September 2026, boils it down to three conditions. The rule applies when all three are true:</p>
<ol><li>A computer program makes a decision, or does something substantially and directly related to making it.</li><li>The decision could reasonably be expected to significantly affect someone's rights or interests.</li><li>Personal information is used to do it.</li></ol>
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
<ol><li>List every tool that touches customer, staff or applicant information, including free AI tools staff use.</li><li>Find the decisions. For each tool, ask: does it decide, or substantially shape, an outcome for a person?</li><li>Check the stakes. Could that outcome significantly affect someone: money, access to a service, a job?</li><li>Decide where a human genuinely reviews, and make sure that review is real, not a click-through.</li><li>Update your privacy policy in plain English, with your lawyer confirming the wording where needed.</li></ol>
<p>If you'd like this mapped for you, the <a href="/compliance-sprint/">compliance controls sprint</a> can take the Privacy Act as its focus.</p>""",
     "sources": 'General information only, not legal advice. Sources: Office of the Australian Information Commissioner, <a href="https://www.oaic.gov.au/__data/assets/pdf_file/0021/269013/APP-1.7-1.9-Transparency-Obligation-Fact-Sheet.PDF" rel="noopener">APP 1.7–1.9 transparency obligation fact sheet</a> and <a href="https://www.oaic.gov.au/__data/assets/pdf_file/0019/269011/OAIC-APP-1.7-1.9-Transparency-Obligation-Flowchart_v4.pdf" rel="noopener">flowchart</a> (30 September 2026); <a href="https://www.oaic.gov.au/privacy/australian-privacy-principles-guidelines/chapter-1-app-1-open-and-transparent-management-of-personal-information/" rel="noopener">APP 1 guidelines</a>.',
     "topic": "Compliance controls sprint"},
    {"path": "/insights/check-bills-before-you-pay/", "date": "2026-10-06", "shown": "6 October 2026", "mins": 4,
     "title": "Five checks to run on every supplier bill before you pay it",
     "desc": "Duplicate bills, changed bank details and quiet price rises cost small businesses real money. Here's how to catch them, by hand or automatically in Xero or MYOB.",
     "body": """<p>Most money lost on supplier bills isn't lost to anything clever. It's a bill paid twice, a price that crept up and nobody noticed, or a payment sent to bank details that changed last week. Five simple checks catch nearly all of it.</p>
<h2>1. Have we paid this already?</h2>
<p>Look for the same supplier and the same amount within a few weeks, or the same invoice number twice. Duplicates usually come from a bill arriving by email and again by post, or a reminder being entered as a new bill.</p>
<h2>2. Have the bank details changed?</h2>
<p>This is the one that matters most. Payment-redirection scams work by sending a convincing email saying a supplier has new bank details. Never pay new bank details on the strength of an email. Hold the payment and phone the supplier on a number you already had, not one from the email.</p>
<h2>3. Is it over the approval limit?</h2>
<p>Set a dollar limit above which a bill needs a second pair of eyes, even in a two-person business. It costs a minute and stops most mistakes that matter.</p>
<h2>4. Has the price moved?</h2>
<p>Compare the unit price with the last order from the same supplier. A 10% rise might be fine, but you should decide that, not find out at year end.</p>
<h2>5. Is this a new supplier?</h2>
<p>First bills from new suppliers deserve a quick check: ABN, contact details and whether anyone actually ordered from them.</p>
<h2>Doing it automatically</h2>
<p>All five checks are rules, which makes them a good fit for automation. An automated workflow can pull new bills from Xero or MYOB each morning, run the checks, and sort them into <em>ready to pay</em> and <em>held for a person</em>, each held bill with its reason. Nothing is paid automatically: you still approve the payment run, you just stop reading every bill line by line.</p>
<p>You can try several of these checks on your own bills with the <a href="/bill-check/">free bill check</a>. It runs in your browser, and nothing is uploaded.</p>
<h2>What it won't do</h2>
<p>It won't catch a fake bill from a real supplier with unchanged details and a normal price; that still needs someone who knows what was ordered. And the rules are only as good as your data: if supplier records are messy, cleaning them up comes first.</p>""",
     "sources": 'General information only. If you think you\'ve paid a scammer, contact your bank immediately and report it at <a href="https://www.scamwatch.gov.au/" rel="noopener">Scamwatch</a>.',
     "topic": "Automation & AI agents"},
    {"path": "/insights/shortcut-to-a-good-ai-tool/", "date": "2026-10-19", "shown": "19 October 2026", "mins": 4,
     "title": "Don't let a shortcut to a good AI tool fool you",
     "desc": "AI tools, agent templates and AI courses for finance are arriving every week. Six questions to ask before any of them touches your money.",
     "body": """<p>Every week there's a new AI tool for finance, a new agent template, a new course promising AI skills in a weekend. Some of them are good. The demo almost always works.</p>
<p>The demo is the easy part. The work is what happens next: a supplier changes their bank details, a bill arrives as a scanned PDF, the same invoice turns up twice with a new number, or a data feed fails halfway through a run. What the tool does then is the product you're buying.</p>
<h2>What a shortcut usually skips</h2>
<ul><li><strong>A person who answers for it.</strong> Someone at your business approves what matters, by name, and someone who built it is still around when it goes wrong.</li><li><strong>A test on records like yours.</strong> Run it over a few months of your past work, where you already know the right answer, and look at every result, including the ones it got wrong.</li><li><strong>Experience of where finance goes wrong.</strong> Duplicate payments, changed bank details, bills split to stay under a limit, numbers that add up and still mislead. Knowing these comes from years of checking real records, and a weekend course won't give it to you.</li></ul>
<h2>Six questions to ask before any AI tool touches your money</h2>
<ol><li><strong>Who approves what it does, by name?</strong> If the answer is "it's automatic", ask what happens when it's wrong.</li><li><strong>What can it never do?</strong> And is that a permission it doesn't have, or just an instruction it's been given? A prompt that says "don't pay" can be ignored or misread. A tool with no permission to pay can't pay.</li><li><strong>Was it tested on your past records?</strong> Ask to see the results, including the failures, and the pass mark it had to meet.</li><li><strong>What does it do when it isn't sure?</strong> A good tool holds the item for a person and says why. A risky one guesses.</li><li><strong>Can you see what it did last Tuesday?</strong> Every action, the reason, and who approved it, kept in your own accounts.</li><li><strong>If the person who built it disappears, can you switch it off and keep running?</strong> You should own the logins, the instructions and the log.</li></ol>
<p>You don't need us to ask these. Ask them of any tool, agency or course before you rely on it. If the answers are vague, treat it as a demo until they aren't.</p>
<h2>How we set agents up</h2>
<p>Every Beiz agent starts with those six answers written down: a job description, limits it can't cross, a named approver, a test on your past records against a pass mark agreed with you, a few weeks running beside your team before it acts, and a log you can read. <a href="/services/ai-readiness-sprint/#agents">See the controls every agent gets</a>, or <a href="/bill-check/">try the free bill check</a> on your own bills.</p>""",
     "sources": "", "topic": "AI workforce setup"},
    {"path": "/insights/why-13-weeks/", "date": "2026-10-01", "shown": "1 October 2026", "mins": 4,
     "title": "Why 13 weeks? Your cash cycle in plain English",
     "desc": "Why a weekly view of the next quarter catches the problems a monthly report hides, and what Xero's own forecast leaves out.",
     "body": """<p>Most small businesses don't run out of money because they're unprofitable. They run out because a few big payments land in the same week, before the money customers owe them arrives. A 13-week cash forecast is built to catch that week before it happens.</p>
<h2>Why a quarter</h2>
<p>Thirteen weeks is one quarter. That matters because most of a small business's big cash movements run on a quarterly or shorter cycle:</p>
<ul><li><strong>The BAS.</strong> For many businesses it's the biggest single payment of the quarter, and a 13-week view always includes one.</li><li><strong>Payroll and super.</strong> Wages go out weekly or fortnightly, and since Payday Super started on 1 July 2026, super goes out with every pay run too.</li><li><strong>Customer terms.</strong> On 30 to 60 day terms, invoices you raise today are paid inside the window. So most of the forecast is money you already know about, not guesses.</li><li><strong>Rent, loans and leases.</strong> Monthly payments show up three times, so nothing sneaks up on you.</li></ul>
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
<p>If your year is seasonal, a simple 12-month view alongside it shows the quiet months coming too. See the <a href="/services/cash-and-job-profit-model/">cash &amp; job profit model</a>.</p>""",
     "sources": "General information only, not financial advice.", "topic": "Cash & job profit model"},
    {"path": "/insights/burned-by-an-ai-product/", "date": "2026-10-01", "shown": "1 October 2026", "mins": 4,
     "title": "Burned by an AI product or a developer who vanished? Get these back first",
     "desc": "A practical checklist for taking back control of your domain, website, data and AI accounts when a supplier relationship goes wrong.",
     "body": """<p>It happens more than people admit. You paid a developer or an agency for a website, a chatbot or an automation. It didn't work, or they stopped replying, or they now want more money to hand things over. Before anything else, get control back. Here's the order that matters.</p>
<h2>1. Your domain name</h2>
<p>The domain is the keys to everything: website and email. Log in to the registrar and make sure the registrant is your business, the account is in your name, and two-factor authentication is on. Remove any other users. Then change the domain password (sometimes called the auth or EPP code) so nobody else can transfer it.</p>
<h2>2. Where your domain points (DNS)</h2>
<p>If your DNS is managed in someone else's account, your email and website depend on them. Move it to an account you control. Make a copy of the existing records first so nothing breaks.</p>
<h2>3. Email</h2>
<p>Make sure you are the super-admin of your email system, not the supplier. Check mail forwarding rules too; a forgotten one can copy your email to someone else.</p>
<h2>4. Website and code</h2>
<p>Get an export or backup of the site and any code, and admin access to wherever it's hosted. If it's in a code repository, the repository should belong to your account.</p>
<h2>5. AI and software accounts</h2>
<p>Chatbots and automations run on accounts with API keys. Make sure those accounts are in your business's name, billing is on your card, and rotate the keys the supplier had.</p>
<h2>6. Your data</h2>
<p>Export customer lists, conversation logs and anything the tool collected. It's your data; get a copy now.</p>
<h2>Then decide what's worth keeping</h2>
<p>Once you're in control, look at what you actually have. Sometimes it's most of the way there and worth finishing. Sometimes it's quicker to start clean. Either way, the decision is yours, made with the facts.</p>
<p>Keep everything in writing. Don't pay extra to get access to things you've already paid for without getting advice first.</p>""",
     "sources": "General information only, not legal advice.", "topic": "Something else"},
    {"path": "/insights/we-feed-your-tax-accountant/", "date": "2026-10-01", "shown": "1 October 2026", "mins": 3,
     "title": "We don't replace your tax accountant. We feed them.",
     "desc": "Why compliance and finance systems are different jobs, and how clean data makes both better.",
     "body": """<p>People sometimes ask whether we'll replace their accountant. We won't, and we don't want to. It's a different job.</p>
<h2>Two different jobs</h2>
<table class="led"><thead><tr><th></th><th>Your tax accountant</th><th>Beiz</th></tr></thead><tbody>
<tr><td>Main focus</td><td data-h="Your tax accountant">Compliance: tax returns, BAS, keeping the ATO happy</td><td data-h="Beiz">Operations: automation, forecasts, dashboards, AI controls</td></tr>
<tr><td>Looks at</td><td data-h="Your tax accountant">What happened last quarter or last year</td><td data-h="Beiz">What happens next week and next quarter</td></tr>
<tr><td>Delivers</td><td data-h="Your tax accountant">Lodgements and annual statements</td><td data-h="Beiz">Systems that run every day, and the numbers to steer by</td></tr>
<tr><td>Registered with</td><td data-h="Your tax accountant">The Tax Practitioners Board</td><td data-h="Beiz">CA ANZ public practice; we don't do tax</td></tr>
</tbody></table>
<p>Both matter. A good tax accountant keeps you compliant. But they're not usually the person who connects your job app to your invoicing, builds the 13-week cash forecast, or puts controls around the AI your staff are using.</p>
<h2>How it works together</h2>
<p>We build the systems that keep your records clean all year: invoices matched, bank reconciled, costs tagged by job or project, crypto transactions complete. When it's time to lodge, your accountant gets tidy, reconciled data. Less back-and-forth, fewer surprises, and often a smaller bill from them.</p>
<h2>Why we don't do tax</h2>
<p>Focus. Tax is a specialist field with its own registration. We'd rather be very good at the systems and the numbers that run your business, and let your tax agent be very good at theirs.</p>""",
     "sources": "", "topic": "Something else"},
]

# ---------------------------------------------------------------- "In brief" blocks (5 Nov 2026, from the AI search notes:
# three plain bullets at the top of each service page, phrased the way a buyer would ask)
BRIEF = {
    "/cash-data-check/": ["For owners and finance leads who bill time or fixed fees and suspect work or money is slipping.",
                          "Two weeks, from your exports: bills, invoices and timesheets checked against each other, every finding traced to its record.",
                          "No logins to your ledger, no tax or BAS advice. The fee is credited if you go ahead with a build."],
    "/services/cash-and-job-profit-model/": ["For businesses that need to see the tight cash week before it arrives, not after month-end.",
                          "A 13-week cash view built from when your customers actually pay, your payroll, super and tax dates, and profit by job, tied to the ledger.",
                          "A model with written assumptions that you run after handover. Not financial product advice."],
    "/leave-cover/": ["For small finance teams where one person going on leave means bills and invoices stall.",
                      "An agent carries the routine part of the role, holds anything unusual for a named person, and you get a one-page update every Friday.",
                      "Decisions, customers and people stay with your team. A Chartered Accountant reviews the agent's work."],
    "/services/ai-readiness-sprint/": ["For businesses that want AI doing real finance and admin work, with limits a board or owner can defend.",
                          "One workflow first: the agent's job description, limits, a test on your past records and shadow mode before anything goes live.",
                          "Nothing is paid or sent without a person, and every decision is logged in your own accounts."],
    "/services/workflow-redesign/": ["For small businesses, startups and solo operators whose admin grows with every new job.",
                          "One process mapped end to end, with re-keying, handoffs and waiting taken out before anything is automated.",
                          "You get a redesigned process with named owners, and a short list of what to automate and what to leave alone."],
    "/services/automation/": ["For teams doing the same matching, chasing and checking every week.",
                          "One workflow automated with fixed rules for the routine records and AI only for the exceptions, then tested and handed over.",
                          "Runs in your own accounts, with a run history your staff can read and a person approving anything that matters."],
    "/services/chatbots-ai-assistants/": ["For businesses answering the same questions by email, phone and chat.",
                          "An assistant that answers only from information you approve, and hands anything else to a person.",
                          "Clear limits on what it may say, tested on real questions before it goes live."],
    "/services/data-engineering/": ["For teams whose numbers live across an accounting system, a CRM, a job app and spreadsheets.",
                          "One clean source, refreshed on a schedule, reconciled back to the ledger.",
                          "Built in your own accounts and documented so someone else can run it."],
    "/services/dashboards-and-models/": ["For owners and boards who want three answers each week: which jobs made money, where cash is stuck, and what's due in the next 14 days.",
                          "A reporting pack or dashboard on agreed definitions, reconciled to the ledger.",
                          "A few numbers you trust, rather than twenty charts nobody reads."],
    "/compliance-sprint/": ["For businesses facing one obligation now: AI use, AML/CTF tranche 2 or the Privacy Act automated-decision rules.",
                          "Two weeks: what's in scope, who owns each step, where a person must approve, and a plan for the first controlled workflow.",
                          "General information, not legal advice. Your adviser or lawyer keeps the legal wording."],
    "/aml-ctf-accounting-firms/": ["For accounting firms working out whether the services they provide bring them under AUSTRAC's AML/CTF rules.",
                          "Agents collect, check and file the routine client checks. Your compliance officer decides every risk rating and every report.",
                          "Sized for small firms. General information, not legal advice."],
    "/services/ai-governance/": ["For boards, directors and owners who need to oversee the AI already in use, including staff pasting client records into public AI tools.",
                          "A register of AI use, a short policy, and a reporting line the board can follow.",
                          "Practical controls mapped to published frameworks. General information, not legal advice."],
}
