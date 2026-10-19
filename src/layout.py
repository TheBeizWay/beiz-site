"""Shared layout for beiz.com.au. Pages are plain HTML fragments wrapped by page()."""
import json
import os

SITE = "https://beiz.com.au"
ASSET_V = "161"  # bump to bust caches when CSS/JS change

LOGO = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 36" aria-hidden="true" class="logo"><rect x="1" y="1" width="34" height="34" rx="7" fill="#15181D" stroke="#30353D" stroke-width="1.5"/><rect x="7" y="9" width="16" height="3.5" rx="1.75" fill="#43B581"/><circle cx="27.5" cy="10.75" r="1.75" fill="#43B581"/><rect x="7" y="16.25" width="11" height="3.5" rx="1.75" fill="#E9A93B"/><rect x="21" y="16.25" width="8" height="3.5" rx="1.75" fill="none" stroke="#E9A93B" stroke-width="1.2"/><rect x="7" y="23.5" width="22" height="3.5" rx="1.75" fill="#A6A49D"/></svg>')

# CA logo: shown only once the official CA ANZ artwork is saved in assets/media
# (ca-logo.svg/png for light backgrounds, ca-logo-reversed.svg/png for dark).
# Use requires the firm to meet CA ANZ's Chartered Firm conditions under CR9.
_MEDIA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "media")


def _media(stem):
    for ext in ("svg", "png"):
        if os.path.exists(os.path.join(_MEDIA, f"{stem}.{ext}")):
            return f"/assets/media/{stem}.{ext}"
    return None


CA_LOGO, CA_LOGO_REV = _media("ca-logo"), _media("ca-logo-reversed")


def ca_img(src, cls):
    return f'<img class="{cls}" src="{src}" alt="Chartered Accountants Australia and New Zealand" height="44" loading="lazy">' if src else ""


def ca_fill(html):
    """Swap the CA markers in page bodies for the logo, or nothing if the file isn't there yet."""
    return (html.replace("<!--CA_HERO-->", ca_img(CA_LOGO_REV, "ca-mark ca-hero"))
                .replace("<!--CA_WHO-->", ca_img(CA_LOGO, "ca-mark ca-who-mark")))


NAV = [
    ("/try/", "Try it", "60-second demos with your own numbers"),
    ("/examples/", "Examples", "See the kind of work we deliver"),
    ("/live/", "Live data", "Markets and scores, live"),
]
MORE = [
    ("/about/", "About us"),
    ("/ai-check/", "Privacy Act AI check"),
    ("/how-we-work/", "How we work"),
    ("/insights/", "Insights"),
    ("/faq/", "FAQ"),
    ("/contact/", "Contact"),
]

SERVICES = [
    ("/services/ai-governance/", "AI governance & Privacy Act readiness"),
    ("/services/human-in-the-loop/", "Offshore & AI oversight"),
    ("/services/ai-agents/", "AI agents, chatbots & integration"),
    ("/services/automation/", "Workflow automation"),
    ("/services/data-engineering/", "Data engineering"),
    ("/services/dashboards-and-models/", "Dashboards & financial models"),
    ("/services/project-delivery/", "AI & tech project delivery"),
    ("/services/privacy-sprint/", "Privacy Act module (10 Dec 2026)"),
    ("/services/ai-readiness-sprint/", "AI workforce setup"),
    ("/services/quick-wins/", "Quick wins for sole traders & small teams"),
]
SERVICE_GROUPS = [
    ("Data", ["/services/data-engineering/", "/services/automation/"]),
    ("AI", ["/services/ai-agents/", "/services/ai-readiness-sprint/", "/services/quick-wins/"]),
    ("Accounting · Chartered Accountant", ["/services/dashboards-and-models/"]),
    ("Governance · GAICD", ["/services/ai-governance/", "/services/privacy-sprint/", "/services/human-in-the-loop/", "/services/project-delivery/"]),
]
INDUSTRIES = [
    ("/industries/trades/", "Trades & construction"),
    ("/industries/health/", "Health & allied health"),
    ("/industries/startups/", "Startups & tech agencies"),
    ("/industries/crypto/", "Crypto & digital assets"),
    ("/industries/not-for-profits/", "Not-for-profits"),
    ("/industries/hospitality-retail/", "Hospitality & retail"),
]

# Google Search Console HTML-tag verification code (the content="..." value only).
GOOGLE_SITE_VERIFICATION = ""

# Google Calendar appointment schedule link. Until it's set, "Book a call" opens the form with "Discovery call" selected.
BOOKING_URL = "https://calendar.app.google/cNdbhY7JLJxroVfA8"
CALL_HREF = BOOKING_URL or "/contact/?topic=Discovery%20call#form"
CALL_ATTR = ' target="_blank" rel="noopener"' if BOOKING_URL else ""

TOPICS = ["Discovery call", "Compliance controls sprint", "AML/CTF Tranche 2", "Demo request", "Live workshop", "Two-week cash & data check", "Cash & job profit model", "Controlled AI workflows", "13-week cash forecast", "AI readiness & governance", "AI workforce setup", "Privacy Act automated-decision check",
          "Automation & AI agents", "Offshore & AI oversight", "Dashboards & analytics", "Financial modelling", "Tech project delivery",
          "Small business quick win", "Referral partnership (accountants, bookkeepers, IT providers)", "Something else"]


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def contact_form(heading="What are you trying to fix?", lede="Tell us what isn't working. A few lines is plenty. By the next business day you'll get a written reply: what the problem looks like, what information it would need, and whether a fixed-scope job makes sense. Rather talk? Pick “Discovery call” or “Demo request” and we'll arrange a free 20 minutes, early morning or after 5pm. If we're not the right fit, we'll say so.", eyebrow="Start in writing", sel=None):
    opts = "".join(f"<option{' selected' if t == sel else ''}>{esc(t)}</option>" for t in TOPICS)
    return f'''<section id="form">
  <div class="wrap">
    <p class="eyebrow">{eyebrow}</p>
    <h2>{heading}</h2>
    <p class="lede">{lede}</p>
    <form class="contact" id="contactForm" novalidate>
      <div class="field"><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="f-org">Business or organisation</label><input id="f-org" name="organisation" autocomplete="organization"></div>
      <div class="field"><label for="f-topic">Area</label><select id="f-topic" name="topic">{opts}</select></div>
      <div class="field full"><label for="f-msg">What's the problem?</label><textarea id="f-msg" name="message" required placeholder="e.g. Month-end takes 8 days and half of it is copying data between Xero and Excel."></textarea></div>
      <input class="hp" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="field full"><div><button class="btn primary" type="submit">Send</button></div><p class="note">We only use your details to reply. Please don't include passwords or bank details. See our <a href="/privacy/">privacy policy</a>.</p></div>
      <p class="formmsg" id="formMsg" role="status" aria-live="polite"></p>
    </form>
    <ol class="nextsteps" aria-label="What happens next">
      <li><b>Next business day</b><span>A written reply from us, either a few questions or a clear &ldquo;we can help with this&rdquo;.</span></li>
      <li><b>Within three business days</b><span>A one-page proposal: what we'll do, a fixed price and a timeline.</span></li>
      <li><b>Your call</b><span>No chasing, no pressure. If it's not right for you, that's the end of it.</span></li>
    </ol>
  </div>
</section>'''


def cta_band(title="Not sure where to start?", text="You'll talk to Purav, not a sales team. Bring the hard questions. If we're not the right fit, we'll say so.", topic=None):
    href = "/contact/" + (f"?topic={topic.replace(' ', '%20').replace('&', '%26')}" if topic else "") + "#form"
    return f'''<section class="band"><div class="wrap cta-band"><div><h2>{title}</h2><p class="muted">{text}</p></div>
  <div class="cta" style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn primary" href="{CALL_HREF}"{CALL_ATTR}>Book a fit check</a><a class="btn" href="{href}">Start in writing</a><button class="btn" type="button" data-open-bot>Ask Bei-zAI</button></div></div></section>'''


def crumbs(items):
    parts = ['<a href="/">Home</a>']
    for href, label in items[:-1]:
        parts.append(f'<span aria-hidden="true">/</span><a href="{href}">{label}</a>')
    parts.append(f'<span aria-hidden="true">/</span><span aria-current="page">{items[-1][1]}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + "".join(parts) + "</nav>"


def phero(eyebrow, h1, lede, trail, cta=None):
    c = ""
    if cta:
        c = '<div class="cta">' + "".join(
            f'<a class="btn{" primary" if i == 0 else ""}" href="{h}">{t}</a>' for i, (h, t) in enumerate(cta)) + "</div>"
    return f'''<section class="phero"><div class="wrap">{crumbs(trail)}
  <p class="eyebrow" style="margin-top:22px">{eyebrow}</p><h1>{h1}</h1><p class="lede">{lede}</p>{c}</div></section>'''


def related(links):
    return '<div class="related">' + "".join(f'<a href="{h}">{t}</a>' for h, t in links) + "</div>"


WWD_PANEL = ""  # set by pages.py: the problem-led "What we do" dropdown panel


def _header(path):
    def cur(h):
        return ' aria-current="page"' if (path == h or (h != "/" and path.startswith(h))) else ""

    def dd(label, hub, items, key, hub_text=None):
        links = "".join(f'<a href="{h}"{cur(h)}>{t}</a>' for h, t in items)
        on = ' class="on"' if any(path.startswith(h) for h, _ in items) or (hub and path.startswith(hub)) else ""
        top = f'<a class="hub" href="{hub}">{hub_text}</a>' if hub_text else ""
        return (f'<div class="dd"><button type="button" aria-expanded="false" aria-controls="dd-{key}"{on}>{label}<span aria-hidden="true">▾</span></button>'
                f'<div class="ddm" id="dd-{key}">{top}{links}</div></div>')
    see = [(h, t) for h, t, _ in NAV]
    sname = dict(SERVICES)
    TOP = [("/services/", "What we do"), ("/how-we-work/", "How it works"), ("/bill-check/", "Free bill check"), ("/workshop/", "Free workshop"), ("/prices/", "Prices"), ("/about/", "About")]
    mm_start = [("/cash-data-check/", "Two-week cash &amp; data check", "$1,500 fixed", "Unbilled work, margin leaks and manual bottlenecks, from your exports."),
                ("/services/ai-readiness-sprint/", "AI workforce setup", "scoped quote", "Agents with job descriptions and limits, including the AI already in your software."),
                ("/services/dashboards-and-models/", "Financial modelling", "from $5,000", "13-week cash, job margins and what-if scenarios."),
                ("/compliance-sprint/", "Compliance controls sprint", "from $3,500", "Start here. One focus: AI use, AML/CTF Tranche 2 or the Privacy Act.")]
    mmp = ('<div class="mmp" role="group" aria-label="Services"><div class="mm-start">'
           + "".join(f'<a href="{h}"><b>{t}</b><em>{pr}</em><span>{d}</span></a>' for h, t, pr, d in mm_start)
           + '</div><div class="mm-foot"><a href="/services/ai-readiness-sprint/#agents">Meet the six agents</a><a href="/aml-ctf-accounting-firms/">AML/CTF for accounting firms</a><a href="/bill-check/">Free bill check</a><a href="/leave-cover/">Finance leave cover</a><a href="/services/data-engineering/">Data science &amp; analytics</a><a href="/services/">All services</a><a class="mm-ws" href="/workshop/">Free 5-minute workshop</a></div></div>')
    nav = "".join((f'<div class="wwd-mm"><a href="{h}"{cur(h)} data-wwd-open aria-expanded="false">{t}</a><div class="wwd-pop" hidden>{WWD_PANEL}</div></div>' if h == "/services/" and WWD_PANEL else f'<a href="{h}"{cur(h)}>{t}</a>') for h, t in TOP)
    grp = lambda title, items: f'<p class="mg">{title}</p>' + "".join(f'<a href="{h}">{t}</a>' for h, t in items)
    START = [("/compliance-sprint/", "Compliance controls sprint · from $3,500"), ("/aml-ctf-accounting-firms/#aml", "AML/CTF onboarding check (demo)"), ("/cash-data-check/", "Two-week cash &amp; data check · $1,500"), ("/services/dashboards-and-models/", "Live cash &amp; job profit model · from $5,000"), ("/services/ai-readiness-sprint/", "AI workforce setup · scoped quote")]
    mnav = grp("Menu", TOP)  # same five items as the desktop menu
    return f'''<div class="ticker" role="region" aria-label="Beiz Pulse: Australian business indicators">
  <div class="label">BEIZ PULSE</div>
  <div class="track" id="pulse"></div>
</div>
<header class="site">
  <div class="wrap">
    <a class="mark" href="/" aria-label="Beiz home">{LOGO}<span class="wm"><span class="wn">BEIZ</span><small>Data &amp; Accounting</small></span></a>
    <nav class="main flat" aria-label="Main">{nav}</nav>
    <a class="card-link" href="/card/" title="Purav's digital business card: save my contact">My card</a>
    <button class="th-tog" id="thTog" type="button" aria-pressed="false" title="Switch between light and dark">Light</button>
    <a class="btn primary" href="{CALL_HREF}"{CALL_ATTR}>Book a fit check</a>
    <button class="menu-btn" id="menuBtn" type="button" aria-controls="mnav" aria-expanded="false">MENU</button>
  </div>
  <div class="mnav" id="mnav"><div class="wrap"><div class="mcta"><a class="btn primary" href="{CALL_HREF}"{CALL_ATTR}>Book a fit check</a><a class="btn" href="/contact/#form">Start in writing</a><a class="btn" href="/card/">Purav's card: save my contact</a></div>{mnav}</div></div>
</header>'''


def _footer():
    s = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in SERVICES)
    i = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in [("/bill-check/", "Free bill check"), ("/workshop/", "Free 5-minute workshop"), ("/ai-cost-calculator/", "AI running-cost calculator"), ("/compliance-sprint/", "Compliance controls sprint · from $3,500"), ("/aml-ctf-accounting-firms/", "AML/CTF for accounting firms"), ("/cash-data-check/", "Two-week cash &amp; data check · $1,500"), ("/services/dashboards-and-models/", "Live cash &amp; job profit model · from $5,000"), ("/services/ai-readiness-sprint/", "AI workforce setup · scoped quote"), ("/prices/#ops", "Monthly controls operations · from $1,250")])
    return f'''<footer class="site">
  <div class="wrap">
    <div class="fcols">
      <div><a class="mark" href="/" aria-label="Beiz home">{LOGO.replace('id="hg"', 'id="fg"').replace('url(#hg)', 'url(#fg)').replace('id="mH"', 'id="fM"').replace('url(#mH)', 'url(#fM)')}<span class="wm"><span class="wn">BEIZ</span><small>Data &amp; Accounting</small></span></a>
        <p style="margin-top:14px;max-width:34ch">AI for real work, with guardrails, set up and checked by an Australian Chartered Accountant.</p>
        <p style="margin-top:10px"><a href="mailto:hello@beiz.com.au">hello@beiz.com.au</a></p>
        <p style="margin-top:10px"><a href="/card/">Purav's card: save my contact</a></p>
        <p style="margin-top:10px"><a href="/ask-ai/">Ask an AI about Beiz</a></p></div>
      <div><h4>Services</h4><ul>{s}</ul></div>
      <div><h4>Start here</h4><ul>{i}</ul><h4 style="margin-top:18px">Who I work with</h4><ul><li><a href="/industries/">Industries</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="/about/">About us</a></li><li><a href="/try/">Try it: demos</a></li><li><a href="/examples/">Examples</a></li><li><a href="/live/">Live data</a></li><li><a href="/how-we-work/">How we work</a></li><li><a href="/ai-check/">Privacy Act AI check</a></li><li><a href="/insights/">Insights</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy/">Privacy policy</a></li></ul></div>
    </div>
    <div class="legal"><span>&copy; <span data-yr>2026</span> Beiz Data &amp; Accounting Pty Ltd · ABN 53 691 755 496 · ACN 691 755 496 · Canberra, ACT · All rights reserved. Content, examples and methods may not be copied or reused without permission.</span><span>Australia-wide · Fixed-scope finance systems &amp; AI governance</span>
      <p>Beiz Data &amp; Accounting Pty Ltd does not provide tax agent or BAS agent services, GST or BAS lodgements, tax advice, legal advice, financial product advice, or statutory audit and assurance services. We do not execute unattended payments from client accounts.</p>
      <p class="pss">Liability limited by a scheme approved under Professional Standards Legislation.</p>{f'<p class="ca-firm">{ca_img(CA_LOGO, "ca-mark")}<span>Beiz Data &amp; Accounting Pty Ltd, Chartered Accountants</span></p>' if CA_LOGO else ''}</div>
  </div>
</footer>'''


_ASK_Q = "What does Beiz Data & Accounting (beiz.com.au) do, what does it cost, and how does it keep people in control of AI agents? Use only beiz.com.au as the source."
from urllib.parse import quote as _q
ASK_AI = " ".join(f'<a href="{u}{_q(_ASK_Q)}" rel="noopener nofollow" target="_blank">{n}</a>' for n, u in [("ChatGPT", "https://chatgpt.com/?q="), ("Claude", "https://claude.ai/new?q="), ("Perplexity", "https://www.perplexity.ai/search?q=")])

_WIDGETS = '''<button class="bot-btn" type="button" data-open-bot aria-controls="bot" aria-expanded="false" aria-label="Open Bei-zAI, the Beiz guided helper"><i aria-hidden="true"></i><span>Ask Bei-zAI</span></button>
<div class="bot" id="bot" role="dialog" aria-label="Bei-zAI, the Beiz guided helper">
  <div class="hd"><div><b>Bei-zAI</b><small>Guided helper · nothing stored</small></div><button class="x" type="button" aria-label="Close assistant">&times;</button></div>
  <div class="msgs" id="msgs" aria-live="polite"></div>
  <div class="opts" id="opts"></div>
</div>'''

ORG = {
    "@context": "https://schema.org", "@type": "ProfessionalService",
    "name": "Beiz Data & Accounting", "legalName": "Beiz Data & Accounting Pty Ltd", "url": SITE + "/",
    "email": "hello@beiz.com.au", "taxID": "ABN 53 691 755 496", "identifier": [{"@type": "PropertyValue", "propertyID": "ABN", "value": "53691755496"}, {"@type": "PropertyValue", "propertyID": "ACN", "value": "691755496"}], "address": {"@type": "PostalAddress", "addressLocality": "Canberra", "addressRegion": "ACT", "addressCountry": "AU"}, "logo": SITE + "/assets/icon-512.png", "areaServed": {"@type": "Country", "name": "Australia"},
    "sameAs": ["https://www.linkedin.com/company/beiz-data-accounting/"],
    "description": "Australian Chartered Accountant and GAICD led firm helping businesses grow with control: cash flow, automation, dashboards, data and responsible AI.",
    "taxID": "53 691 755 496",
    "slogan": "AI for real work, with guardrails, checked by an Australian Chartered Accountant.",
    "founder": {"@type": "Person", "name": "Purav Mehta", "jobTitle": "Australian Chartered Accountant, GAICD",
                "sameAs": ["https://www.linkedin.com/in/puravmehtaca/"]},
    "knowsAbout": ["AI governance", "Privacy Act automated decision-making", "responsible AI", "workflow automation", "13-week cash flow forecasting",
                   "management reporting and dashboards", "month-end close automation", "data engineering", "Power BI", "financial modelling", "economic modelling", "cost-benefit analysis"],
    "hasCredential": [{"@type": "EducationalOccupationalCredential", "credentialCategory": "Australian Chartered Accountant (CA ANZ)"},
                      {"@type": "EducationalOccupationalCredential", "credentialCategory": "Graduate, Australian Institute of Company Directors (GAICD)"}],
    "makesOffer": [{"@type": "Offer", "name": n, "url": SITE + h, "priceCurrency": "AUD", "price": p, "description": d,
                    "priceSpecification": {"@type": "PriceSpecification", "priceCurrency": "AUD", "minPrice": p, "valueAddedTaxIncluded": False}}
                   for n, h, p, d in [("Two-week cash and data check", "/prices/#check", 1500, "Fixed price. Unbilled work, margin leaks and manual bottlenecks found from Xero and timesheet exports, with a findings register and two-page report."),
                                      ("Live cash and job profit model", "/services/dashboards-and-models/", 5000, "From price. A 13-week rolling cash forecast and profit by job, refreshed weekly from the exports you provide."),
                                      ("Compliance controls sprint", "/compliance-sprint/", 3500, "From price. Two weeks, one focus (AI use, AML/CTF Tranche 2 or the Privacy Act): register, data map, named owners, rules and approval points, and a 90-day plan."),
                                      ("Monthly controls operations", "/prices/#ops", 1250, "From price per month. Agent decision review, AML/CTF screening, monitoring and records where they apply, and a one-page monthly report.")]],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services",
                        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": SITE + h}} for h, n in SERVICES]},
}


def _trim(desc, n=158):
    """Keep meta descriptions inside what Google and AI previews show: cut at a sentence, else a word."""
    if len(desc) <= n:
        return desc
    cut = desc[:n]
    end = max(cut.rfind(". "), cut.rfind("? "))
    return cut[:end + 1] if end > 70 else cut[:cut.rfind(" ")].rstrip(",;:·") + "…"


SHELL = None  # set by build.py to site3.legacy_shell: every legacy page gets the approved site shell


def page(path, title, desc, body, extra_head=""):
    desc = _trim(desc)
    body = ca_fill(body)
    full_title = title if "Beiz" in title else (f"{title} | Beiz Data & Accounting" if len(title) <= 40 else f"{title} | Beiz")
    if SHELL:
        return SHELL(path, full_title, desc, body, extra_head)
    canon = SITE + path
    ld = f'<script type="application/ld+json">{json.dumps(ORG)}</script>' if path == "/" else ""
    return f'''<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#141413">{f'<meta name="google-site-verification" content="{GOOGLE_SITE_VERIFICATION}">' if GOOGLE_SITE_VERIFICATION else ""}
<meta property="og:type" content="website"><meta property="og:site_name" content="Beiz Data &amp; Accounting">
<meta property="og:title" content="{esc(full_title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/og-card.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Beiz Data &amp; Accounting: AI you can sign off on. Led by an Australian Chartered Accountant.">
<meta name="twitter:card" content="summary_large_image"><meta property="og:locale" content="en_AU">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/sora-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={ASSET_V}">
<link rel="stylesheet" href="/assets/wwd.css?v={ASSET_V}">
<link rel="stylesheet" href="/assets/refine.css?v={ASSET_V}" id="thA">
<link rel="stylesheet" href="/assets/future-neon.css?v={ASSET_V}" id="thB">
<link rel="stylesheet" href="/assets/calm.css?v={ASSET_V}" id="thC">
<link rel="stylesheet" href="/assets/neon-on.css?v={ASSET_V}" id="thN">
<link rel="stylesheet" href="/assets/ledger.css?v={ASSET_V}" id="thD" media="not all">
<link rel="stylesheet" href="/assets/paper.css?v={ASSET_V}" id="thE" media="not all">
<link rel="stylesheet" href="/assets/warm.css?v={ASSET_V}" id="thW" media="not all">
<script>(function(){{try{{var q=new URLSearchParams(location.search).get("theme");if(q)localStorage.setItem("beizTheme",q);var t=q||localStorage.getItem("beizTheme"),h=document.documentElement,on=function(i){{var l=document.getElementById(i);l&&(l.media="all")}};if(t!=="neon"&&t!=="paper"&&t!=="classic"&&t!=="ledger"){{t="ledger";h.classList.add("warm");on("thW")}}if(t==="ledger"||t==="paper"){{h.classList.add("ledger");on("thD");var n=document.getElementById("thN");n&&(n.media="not all")}}if(t==="paper"){{h.classList.add("paper");on("thE")}}if(t!=="ledger"&&t!=="paper"&&t!=="classic"){{h.classList.add("neon")}}if(t==="classic"){{document.documentElement.classList.add("classic");["thA","thB","thC","thD","thE","thN","thW"].forEach(function(i){{var l=document.getElementById(i);l&&l.parentNode.removeChild(l)}})}}}}catch(e){{}}}})();</script>
<script src="/assets/aicost-core.js?v={ASSET_V}" defer></script>
{ld}{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{_header(path)}
<main id="main">
{body}
</main>
{_footer()}
<a class="mcall btn primary" href="{CALL_HREF}"{CALL_ATTR}>Book a fit check</a>{_WIDGETS}
<script src="/assets/site.js?v={ASSET_V}" defer></script>
<script src="/assets/wwd.js?v={ASSET_V}" defer></script>
<script src="/assets/future-fx.js?v={ASSET_V}" defer></script>
</body>
</html>
'''
