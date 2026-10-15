"""Shared layout for beiz.com.au. Pages are plain HTML fragments wrapped by page()."""
import json

SITE = "https://beiz.com.au"
ASSET_V = "74"  # bump to bust caches when CSS/JS change

LOGO = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" aria-hidden="true" class="logo"><defs><linearGradient id="hg" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#2DD4BF"/><stop offset="1" stop-color="#818CF8"/><animateTransform attributeName="gradientTransform" type="rotate" values="0 .5 .5;360 .5 .5" dur="9s" repeatCount="indefinite"/></linearGradient><mask id="mH" maskUnits="userSpaceOnUse" x="0" y="0" width="200" height="200"><rect width="200" height="200" fill="#fff"/><circle cx="126.4" cy="69.9" r="6.5" fill="#000"/></mask></defs><rect x="5" y="5" width="190" height="190" rx="44" fill="#0D1115" stroke="url(#hg)" stroke-width="6"/><g stroke="#818CF8" stroke-width="3" fill="none" stroke-linecap="round"><path d="M113.0 75.4 L150 75.4 L165 53.4"/><path d="M150 75.4 L165 97.4"/></g><g fill="#818CF8"><circle cx="165" cy="53.4" r="6"><animate attributeName="r" values="6;8.5;6" dur="2.4s" repeatCount="indefinite"/></circle><circle cx="165" cy="97.4" r="6"><animate attributeName="r" values="6;8.5;6" dur="2.4s" begin="1.2s" repeatCount="indefinite"/></circle></g><circle cx="150" cy="75.4" r="4" fill="#5EEAD4"><animate attributeName="opacity" values="1;.35;1" dur="1.6s" repeatCount="indefinite"/></circle><circle r="3.2" fill="#fff"><animateMotion dur="2.4s" repeatCount="indefinite" path="M113 75.4 L150 75.4 L165 53.4"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.85;1" dur="2.4s" repeatCount="indefinite"/></circle><g transform="translate(16,25.1) scale(.72)"><g mask="url(#mH)" fill="none" stroke="url(#hg)" stroke-width="27" stroke-linejoin="round"><path d="M58 120 L110 120 A33 33 0 0 1 110 186 L58 186 L58 22 L102 58 A31 31 0 0 1 102 120 L58 120"/></g></g></svg>')

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
    ("/services/privacy-sprint/", "Automated-Decision Privacy Sprint"),
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
BOOKING_URL = ""
CALL_HREF = BOOKING_URL or "/contact/?topic=Discovery%20call#form"
CALL_ATTR = ' target="_blank" rel="noopener"' if BOOKING_URL else ""

TOPICS = ["Discovery call", "Demo request", "Two-week cash & data check", "Cash & job profit model", "Controlled AI workflows", "13-week cash forecast", "AI readiness & governance", "AI workforce setup", "Privacy Act automated-decision check",
          "Automation & AI agents", "Offshore & AI oversight", "Dashboards & analytics", "Financial modelling", "Tech project delivery",
          "Small business quick win", "Something else"]


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def contact_form(heading="What are you trying to fix?", lede="Tell us what isn't working. A few lines is plenty. By the next business day you'll get a written reply: what the problem looks like, what information it would need, and whether a fixed-scope job makes sense. Rather talk? Pick “Discovery call” or “Demo request” and we'll arrange a free 20 minutes, early morning or after 5pm. If we're not the right fit, we'll say so.", eyebrow="Start in writing"):
    opts = "".join(f"<option>{esc(t)}</option>" for t in TOPICS)
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
      <li><b>Next business day</b><span>A written reply from us, either a few questions or a clear "we can help with this".</span></li>
      <li><b>Within three business days</b><span>A one-page proposal: what we'll do, a fixed price and a timeline.</span></li>
      <li><b>Your call</b><span>No chasing, no pressure. If it's not right for you, that's the end of it.</span></li>
    </ol>
  </div>
</section>'''


def cta_band(title="Not sure where to start?", text="Book a free 20-minute call, or send a few lines in writing. Either way you get a considered reply, not a sales pitch.", topic=None):
    href = "/contact/" + (f"?topic={topic.replace(' ', '%20').replace('&', '%26')}" if topic else "") + "#form"
    return f'''<section class="band"><div class="wrap cta-band"><div><h2>{title}</h2><p class="muted">{text}</p></div>
  <div class="cta" style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn primary" href="{CALL_HREF}"{CALL_ATTR}>Book a call</a><a class="btn" href="{href}">Start in writing</a><button class="btn" type="button" data-open-bot>Ask Bei-zAI</button></div></div></section>'''


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
    TOP = [("/services/", "Services"), ("/services/ai-readiness-sprint/", "AI Workforce"), ("/#pricing", "Pricing"), ("/about/", "About"), ("/contact/", "Contact")]
    nav = "".join(f'<a href="{h}"{cur(h)}>{t}</a>' for h, t in TOP)
    grp = lambda title, items: f'<p class="mg">{title}</p>' + "".join(f'<a href="{h}">{t}</a>' for h, t in items)
    START = [("/#check", "Two-week cash &amp; data check · $1,500"), ("/services/dashboards-and-models/", "Live cash &amp; job profit model · from $5,000"), ("/services/ai-readiness-sprint/", "AI workforce setup · from $6,000")]
    mnav = (grp("Start here", START) + grp("Menu", TOP + [("/how-we-work/", "How we work")]) + grp("See it working", see) +
            grp("More", [("/services/ai-governance/", "AI governance"), ("/ai-check/", "Privacy Act AI check"), ("/insights/", "Insights"), ("/faq/", "FAQ")]))
    return f'''<div class="ticker" role="region" aria-label="Beiz Pulse: Australian business indicators">
  <div class="label">BEIZ PULSE</div>
  <div class="track" id="pulse"></div>
</div>
<header class="site">
  <div class="wrap">
    <a class="mark" href="/" aria-label="Beiz home">{LOGO}<span class="wm"><span class="wn">BEIZ</span><small>Data &amp; Accounting</small></span></a>
    <nav class="main flat" aria-label="Main">{nav}</nav>
    <a class="btn primary" href="{CALL_HREF}"{CALL_ATTR}>Book a call</a>
    <button class="menu-btn" id="menuBtn" type="button" aria-controls="mnav" aria-expanded="false">MENU</button>
  </div>
  <div class="mnav" id="mnav"><div class="wrap"><div class="mcta"><a class="btn primary" href="{CALL_HREF}"{CALL_ATTR}>Book a call</a><a class="btn" href="/contact/#form">Start in writing</a></div>{mnav}</div></div>
</header>'''


def _footer():
    s = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in SERVICES)
    i = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in [("/#check", "Two-week cash &amp; data check · $1,500"), ("/services/dashboards-and-models/", "Live cash &amp; job profit model · from $5,000"), ("/services/ai-readiness-sprint/", "AI workforce setup · from $6,000"), ("/#pricing", "Monthly support · from $750")])
    return f'''<footer class="site">
  <div class="wrap">
    <div class="fcols">
      <div><a class="mark" href="/" aria-label="Beiz home">{LOGO.replace('id="hg"', 'id="fg"').replace('url(#hg)', 'url(#fg)').replace('id="mH"', 'id="fM"').replace('url(#mH)', 'url(#fM)')}<span class="wm">Beiz<small>Data · AI · Accounting</small></span></a>
        <p style="margin-top:14px;max-width:34ch">Governed AI, automation, dashboards and financial models for Australian businesses. Led by an Australian Chartered Accountant.</p>
        <p style="margin-top:10px"><a href="mailto:hello@beiz.com.au">hello@beiz.com.au</a></p></div>
      <div><h4>Services</h4><ul>{s}</ul></div>
      <div><h4>Start here</h4><ul>{i}</ul><h4 style="margin-top:18px">Who I work with</h4><ul><li><a href="/industries/">Industries</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="/about/">About us</a></li><li><a href="/try/">Try it: demos</a></li><li><a href="/examples/">Examples</a></li><li><a href="/live/">Live data</a></li><li><a href="/how-we-work/">How we work</a></li><li><a href="/ai-check/">Privacy Act AI check</a></li><li><a href="/insights/">Insights</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy/">Privacy policy</a></li></ul></div>
    </div>
    <div class="legal"><span>&copy; <span data-yr>2026</span> Beiz Data &amp; Accounting Pty Ltd · ABN 53 691 755 496 · All rights reserved. Content, examples and methods may not be copied or reused without permission.</span><span>Australia-wide · Fixed-scope finance systems &amp; AI governance</span>
      <p>Beiz does not prepare tax returns or BAS, does not provide tax agent or BAS agent services, statutory audit or assurance, legal advice or financial product advice.</p>
      <p class="pss">Liability limited by a scheme approved under Professional Standards Legislation.</p></div>
  </div>
</footer>'''


_WIDGETS = '''<button class="bot-btn" type="button" data-open-bot aria-controls="bot" aria-expanded="false" aria-label="Open Bei-zAI, the Beiz guided helper"><i aria-hidden="true"></i><span>Ask Bei-zAI</span></button>
<div class="bot" id="bot" role="dialog" aria-label="Bei-zAI, the Beiz guided helper">
  <div class="hd"><div><b>Bei-zAI</b><small>Guided helper · nothing stored</small></div><button class="x" type="button" aria-label="Close assistant">&times;</button></div>
  <div class="msgs" id="msgs" aria-live="polite"></div>
  <div class="opts" id="opts"></div>
</div>'''

ORG = {
    "@context": "https://schema.org", "@type": "ProfessionalService",
    "name": "Beiz Data & Accounting", "legalName": "Beiz Data & Accounting Pty Ltd", "url": SITE + "/",
    "email": "hello@beiz.com.au", "logo": SITE + "/assets/icon-512.png", "areaServed": {"@type": "Country", "name": "Australia"},
    "description": "Australian Chartered Accountant and GAICD led firm helping businesses grow with control: cash flow, automation, dashboards, data and responsible AI.",
    "taxID": "53 691 755 496",
    "slogan": "AI you can sign off on.",
    "founder": {"@type": "Person", "name": "Purav Mehta", "jobTitle": "Chartered Accountant, GAICD",
                "sameAs": ["https://www.linkedin.com/in/puravmehtaca/"]},
    "knowsAbout": ["AI governance", "Privacy Act automated decision-making", "responsible AI", "workflow automation", "13-week cash flow forecasting",
                   "management reporting and dashboards", "month-end close automation", "data engineering", "Power BI", "financial modelling", "economic modelling", "cost-benefit analysis"],
    "hasCredential": [{"@type": "EducationalOccupationalCredential", "credentialCategory": "Chartered Accountant, CA ANZ Certificate of Public Practice"},
                      {"@type": "EducationalOccupationalCredential", "credentialCategory": "Graduate, Australian Institute of Company Directors (GAICD)"}],
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


def page(path, title, desc, body, extra_head=""):
    desc = _trim(desc)
    full_title = title if "Beiz" in title else (f"{title} | Beiz Data & Accounting" if len(title) <= 40 else f"{title} | Beiz")
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
<meta name="theme-color" content="#05070B">{f'<meta name="google-site-verification" content="{GOOGLE_SITE_VERIFICATION}">' if GOOGLE_SITE_VERIFICATION else ""}
<meta property="og:type" content="website"><meta property="og:site_name" content="Beiz Data &amp; Accounting">
<meta property="og:title" content="{esc(full_title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/og-card.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Beiz Data &amp; Accounting: AI you can sign off on. Led by an Australian Chartered Accountant.">
<meta name="twitter:card" content="summary_large_image"><meta property="og:locale" content="en_AU">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/sora-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={ASSET_V}">
{ld}{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{_header(path)}
<main id="main">
{body}
</main>
{_footer()}
<a class="mcall btn primary" href="{CALL_HREF}"{CALL_ATTR}>Book a call</a>{_WIDGETS}
<script src="/assets/site.js?v={ASSET_V}" defer></script>
</body>
</html>
'''
