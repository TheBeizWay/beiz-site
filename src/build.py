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
        "> Beiz finds where an Australian business is losing money, then keeps watch with AI agents that a Chartered Accountant sets up and checks. Led by Purav Mehta, Australian Chartered Accountant (Certificate of Public Practice) and GAICD.", "",
        "Key facts:",
        "- Beiz Data & Accounting Pty Ltd, ABN 53 691 755 496. Canberra, working Australia-wide. Not registered for GST, so no GST is added to prices.",
        "- Start here: the two-week cash & data check, $1,500 fixed, credited if the client goes ahead. From exports of bills, invoices and timesheets (no logins), it checks bills against timesheets and quotes, hours worked against invoices, invoices against the rate card, duplicate bills, unapplied credits and overdue invoices. Output: a findings register, a two-page report and a 30-minute walkthrough.",
        "- Then: a live cash & job profit model from $5,000; AI agents (AI workforce setup) from $8,500, each tested on the client's past records, run in shadow mode first, with limits, a named approver and a decision log; finance leave cover from $3,500 setup; monthly support from $1,250.",
        "- For accounting firms: AML/CTF Tranche 2 guidance and a two-week compliance controls sprint from $3,500 (AI use, AML/CTF or the Privacy Act automated-decision rules).",
        "- Nothing is paid or sent by an agent without a person. Builds inside the client's own accounts.",
        "- Does not provide tax agent, BAS agent, statutory audit or assurance, legal or financial product advice services.",
        "- Proposal within three business days of a call. Contact: hello@beiz.com.au or https://beiz.com.au/contact/", "",
        "## Main pages",
        f"- [Two-week cash & data check]({SITE}/cash-data-check/): $1,500 fixed",
        f"- [Sample check report (PDF)]({SITE}/assets/beiz-sample-check-report.pdf): made-up business",
        f"- [Free bill check]({SITE}/bill-check/): runs in the browser on a bills export; nothing is sent",
        f"- [AI agents]({SITE}/services/ai-readiness-sprint/): AI workforce setup from $8,500",
        f"- [Live cash & job profit model]({SITE}/services/dashboards-and-models/): from $5,000",
        f"- [How we work]({SITE}/how-we-work/): including a control room simulation",
        f"- [Prices]({SITE}/prices/)",
        f"- [AML/CTF Tranche 2 for accounting firms]({SITE}/aml-ctf-accounting-firms/)",
        f"- [Compliance controls sprint]({SITE}/compliance-sprint/)",
        f"- [Finance leave cover]({SITE}/leave-cover/)",
        f"- [About Purav Mehta]({SITE}/about/)", f"- [FAQ]({SITE}/faq/)", ""]
open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(llms))
print(f"built {len(pages)} pages")
