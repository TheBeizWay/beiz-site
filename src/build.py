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
        "> Australian firm that sets up AI, automation, dashboards and cash forecasts for small and mid-sized businesses, "
        "with a person signing off anything that touches money, customers or data. Chartered Accountant (CA ANZ, Certificate of Public Practice) and GAICD led.", "",
        "Key facts:",
        "- Beiz Data & Accounting Pty Ltd, ABN 53 691 755 496. Led by Purav Mehta, CA (Certificate of Public Practice), GAICD. Based in Canberra, working Australia-wide.",
        "- Fixed scope and fixed price, agreed in writing before work starts. Prices are not published; a written proposal follows within three business days.",
        "- Independent: no software of its own to sell. Builds inside the client's own accounts (e.g. Xero, MYOB, Microsoft 365, Google Workspace) with business-grade AI that doesn't train on client data.",
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
