"""Build beiz.com.au: python3 src/build.py  (writes static HTML into the repo root)."""
import os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from pages import build_all
from trust import trust_pages
from oversight import oversight_pages
from layout import SITE, SERVICES, INDUSTRIES, ASSET_V
from card import card_page

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages = build_all()
pages.update(trust_pages())
pages.update(oversight_pages())
urls = []
os.makedirs(os.path.join(ROOT, 'card'), exist_ok=True)
open(os.path.join(ROOT, 'card', 'index.html'), 'w', encoding='utf-8').write(card_page(ASSET_V))
for path, html in pages.items():
    out = os.path.join(ROOT, path.lstrip("/")) if path.endswith(".html") else os.path.join(ROOT, path.lstrip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(html)
    if path != "/404.html":
        urls.append(path)
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sm += [f"  <url><loc>{SITE}{u}</loc><lastmod>{datetime.date.today().isoformat()}</lastmod></url>" for u in sorted(urls) if not u.startswith("/preview/")]
sm.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
AI_TRAINING_BOTS = ["GPTBot", "CCBot", "ClaudeBot", "anthropic-ai", "Applebot-Extended", "Bytespider", "meta-externalagent"]
open(os.path.join(ROOT, "robots.txt"), "w").write(
    "# Search engines and AI search assistants are welcome (Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User).\n"
    "# Google-Extended is allowed so the Gemini app can cite and link beiz.com.au. Other AI model-training crawlers are not.\n"
    + "".join(f"User-agent: {b}\nDisallow: /\n\n" for b in AI_TRAINING_BOTS)
    + f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
# llms.txt: a plain summary for AI search assistants (https://llmstxt.org)
llms = ["# Beiz Data & Accounting", "",
        "> AI for real work in Australian businesses, with guardrails, set up and checked by an Australian Chartered Accountant. AI agents with written limits and a person approving what matters, plus AML/CTF, privacy and AI controls, cash models and finance automation, led by Purav Mehta, an Australian Chartered Accountant and GAICD. "
        "Beiz connects a business's data, builds cash and job profit models, and sets up AI agents for routine finance work with limits, approvals and a decision log. "
        "A person approves anything that touches money, customers or decisions about people.", "",
        "Key facts:",
        "- Beiz Data & Accounting Pty Ltd, ABN 53 691 755 496. Led by Purav Mehta, Australian Chartered Accountant, GAICD. Based in Canberra, working Australia-wide. Holds professional indemnity insurance.",
        "- Fixed scope and fixed price, agreed in writing before work starts. Ways to start: compliance controls sprint from $3,500 (two weeks, one focus: AI use, AML/CTF Tranche 2 or the Privacy Act automated-decision rules starting 10 December 2026; register, data map, named owners, rules and approval points, and a 90-day plan; legal wording stays with the client's adviser or lawyer; no ledger access needed), two-week cash & data check $1,500 fixed (credited if the client goes ahead), live cash & job profit model from $5,000, AI workforce setup from $8,500 (first agent), leave cover from $3,500 setup then from $2,000 a month, then monthly controls operations from $1,250 a month (agent decision review, and AML/CTF screening, monitoring and records where they apply). Other work: quick wins from $1,200. Beiz is not registered for GST, so no GST is added to prices. A written proposal with the exact price follows within three business days.",
        "- Independent: no software of its own to sell. Builds inside the client's own accounts (e.g. Xero, MYOB, Microsoft 365, Google Workspace) using AI plans whose terms exclude training on client data.",
        "- Four disciplines: Data (reconciliation, reporting, forecasting), AI (automation with approval steps), Accounting (management reports, cash forecasts, financial and economic models, profit by job), Governance (board reporting, risk, AI use policy, Privacy Act automated-decision readiness).",
        "- Also offered: a fixed-price billing review of three completed jobs. Timesheets, job list and invoices are reconciled from exports (no logins) into a findings register where each item is Confirmed, Needs information or Explained, with source records and arithmetic. Sample register (made-up data): " + SITE + "/assets/media/sample-findings.xlsx",
        "- Typical clients: private-sector businesses of about 5 to 50 staff, especially project businesses that bill time or fixed fees (engineering, IT, consulting, trades).",
        "- Does not provide tax agent, BAS agent, legal, audit or financial product advice services.",
        "- Contact: hello@beiz.com.au, or book a discovery call at https://beiz.com.au/contact/",
        "- LinkedIn: https://www.linkedin.com/company/beiz-data-accounting/", "",
        "## Services"] + [f"- [{t}]({SITE}{h})" for h, t in SERVICES] + ["", "## Who we help"] + [f"- [{t}]({SITE}{h})" for h, t in INDUSTRIES] + [
        "", "## Start here", f"- [Two-week cash & data check]({SITE}/cash-data-check/): $1,500 fixed; duplicate bills, unbilled hours, invoices below the rate card, unapplied credits and overdue invoices, from exports", f"- [Compliance controls sprint]({SITE}/compliance-sprint/): from $3,500, two weeks, one focus: AI use, AML/CTF Tranche 2 or the Privacy Act", f"- [AML/CTF Tranche 2 for accounting firms]({SITE}/aml-ctf-accounting-firms/): which services are caught, what firms must do, where agents help and where they stop", f"- [AML/CTF client onboarding check (interactive demo)]({SITE}/aml-ctf-accounting-firms/#aml): customer due diligence, screening and the decision a person has to make",
        f"- [Free bill check on your own data]({SITE}/bill-check/): drop in a bills export; possible duplicates, bank detail changes, split bills and ABN problems; runs in the browser, nothing is sent",
        f"- [AI running-cost calculator]({SITE}/ai-cost-calculator/): monthly AI usage cost of an agent in AUD by model, next to the cost of the person who checks its work; vendor prices dated on the page",
        "", "## See it working",
        f"- [Homepage demonstrations]({SITE}/): an interactive 13-week cash model, a data lineage walk-through from dashboard to source records, and an AI controls simulation (allow, hold or block)",
        f"- [Free 5-minute AI workforce workshop]({SITE}/workshop/): map the week, set an agent's limits, get a written plan",
        f"- [Sample two-week check report (PDF)]({SITE}/assets/beiz-sample-check-report.pdf) on made-up data",
        f"- [60-second demos]({SITE}/try/): late payers, 13-week cash forecast, an agent checking bills, admin hours",
        f"- [Example outputs]({SITE}/examples/): made-up businesses, real formats",
        f"- [Free Privacy Act AI check]({SITE}/ai-check/): for the automated-decision disclosure rules starting 10 December 2026",
        "", "## About", f"- [About Beiz]({SITE}/about/)", f"- [Ask an AI about Beiz]({SITE}/ask-ai/): the key facts in one table, and links to ask ChatGPT, Claude, Perplexity, Gemini or Copilot", f"- [Why trust Beiz: commitments and limits]({SITE}/trust/)", f"- [Human and organisation in the loop]({SITE}/oversight/)", f"- [How we work]({SITE}/how-we-work/)", f"- [FAQ]({SITE}/faq/)", ""]
open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(llms))
print(f"built {len(pages)} pages")
