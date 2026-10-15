"""Build beiz.com.au: python3 src/build.py  (writes static HTML into the repo root)."""
import os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from pages import build_all
from layout import SITE, SERVICES, INDUSTRIES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages = build_all()
urls = []
for path, html in pages.items():
    out = os.path.join(ROOT, path.lstrip("/")) if path.endswith(".html") else os.path.join(ROOT, path.lstrip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(html)
    if path != "/404.html":
        urls.append(path)
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
sm += [f"  <url><loc>{SITE}{u}</loc><lastmod>{datetime.date.today().isoformat()}</lastmod></url>" for u in sorted(urls)]
sm.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
AI_TRAINING_BOTS = ["GPTBot", "Google-Extended", "CCBot", "ClaudeBot", "anthropic-ai", "Applebot-Extended", "Bytespider", "meta-externalagent"]
open(os.path.join(ROOT, "robots.txt"), "w").write(
    "# Search engines and AI search assistants are welcome. AI model-training crawlers are not.\n"
    + "".join(f"User-agent: {b}\nDisallow: /\n\n" for b in AI_TRAINING_BOTS)
    + f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
# llms.txt: a plain summary for AI search assistants (https://llmstxt.org)
llms = ["# Beiz Data & Accounting", "",
        "> Chartered Accountant-led practice in Australia that makes business information reliable, reporting useful and automation accountable. "
        "Data, AI, accounting and governance for private-sector small and mid-sized businesses, with a person signing off anything that touches money, customers or data.", "",
        "Key facts:",
        "- Beiz Data & Accounting Pty Ltd, ABN 53 691 755 496. Led by Purav Mehta, CA (Certificate of Public Practice), GAICD. Based in Canberra, working Australia-wide.",
        "- Fixed scope and fixed price, agreed in writing before work starts. Ways to start: Numbers & AI check $1,500 fixed (credited if the client goes ahead), AI team setup from $6,000, decision model from $5,000, then monthly support from $750 a month. Other work: quick wins from $1,200, Privacy Act automated-decision sprint from $3,500. Prices exclude GST. A written proposal with the exact price follows within three business days.",
        "- Independent: no software of its own to sell. Builds inside the client's own accounts (e.g. Xero, MYOB, Microsoft 365, Google Workspace) with business-grade AI that doesn't train on client data.",
        "- Four disciplines: Data (reconciliation, reporting, forecasting), AI (automation with approval steps), Accounting (management reports, cash forecasts, financial and economic models, profit by job), Governance (board reporting, risk, AI use policy, Privacy Act automated-decision readiness).",
        "- Also offered: a fixed-price billing review of three completed jobs. Timesheets, job list and invoices are reconciled from exports (no logins) into a findings register where each item is Confirmed, Needs information or Explained, with source records and arithmetic. Sample register (made-up data): " + SITE + "/assets/media/sample-findings.xlsx",
        "- Typical clients: private-sector businesses of about 5 to 50 staff, especially project businesses that bill time or fixed fees (engineering, IT, consulting, trades).",
        "- Does not provide tax agent, BAS agent, legal, audit or financial product advice services.",
        "- Contact: hello@beiz.com.au, or book a discovery call at https://beiz.com.au/contact/", "",
        "## Services"] + [f"- [{t}]({SITE}{h})" for h, t in SERVICES] + ["", "## Who we help"] + [f"- [{t}]({SITE}{h})" for h, t in INDUSTRIES] + [
        "", "## See it working",
        f"- [60-second demos]({SITE}/try/): late payers, 13-week cash forecast, an agent checking bills, admin hours",
        f"- [Example outputs]({SITE}/examples/): made-up businesses, real formats",
        f"- [Free Privacy Act AI check]({SITE}/ai-check/): for the automated-decision disclosure rules starting 10 December 2026",
        "", "## About", f"- [About Beiz]({SITE}/about/)", f"- [How we work]({SITE}/how-we-work/)", f"- [FAQ]({SITE}/faq/)", ""]
open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(llms))
print(f"built {len(pages)} pages")
