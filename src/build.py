"""Build beiz.com.au: python3 src/build.py  (writes static HTML into the repo root)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pages import build_all
from layout import SITE

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
sm += [f"  <url><loc>{SITE}{u}</loc><lastmod>2026-10-01</lastmod></url>" for u in sorted(urls)]
sm.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
AI_TRAINING_BOTS = ["GPTBot", "Google-Extended", "CCBot", "ClaudeBot", "anthropic-ai", "Applebot-Extended", "Bytespider", "meta-externalagent"]
open(os.path.join(ROOT, "robots.txt"), "w").write(
    "# Search engines and AI search assistants are welcome. AI model-training crawlers are not.\n"
    + "".join(f"User-agent: {b}\nDisallow: /\n\n" for b in AI_TRAINING_BOTS)
    + f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print(f"built {len(pages)} pages")
