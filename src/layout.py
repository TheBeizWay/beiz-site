"""Shared layout for beiz.com.au. Pages are plain HTML fragments wrapped by page()."""
import json

SITE = "https://beiz.com.au"
ASSET_V = "16"  # bump to bust caches when CSS/JS change

LOGO = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" aria-hidden="true" class="logo">'
        '<defs><linearGradient id="hg" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#2DD4BF"/>'
        '<stop offset="1" stop-color="#818CF8"/></linearGradient>'
        '<mask id="mH" maskUnits="userSpaceOnUse" x="0" y="0" width="200" height="200"><rect width="200" height="200" fill="#fff"/>'
        '<circle cx="126.4" cy="69.9" r="6" fill="#000"/></mask></defs>'
        '<g mask="url(#mH)" fill="none" stroke="url(#hg)" stroke-width="26" stroke-linejoin="round" stroke-linecap="butt">'
        '<path d="M58 120 L110 120 A33 33 0 0 1 110 186 L58 186 L58 22 L102 58 A31 31 0 0 1 102 120 L58 120"/></g></svg>')

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
    ("/services/automation/", "Agents & automation"),
    ("/services/dashboards-and-models/", "Dashboards & financial models"),
    ("/services/project-delivery/", "AI & tech project delivery"),
    ("/services/privacy-sprint/", "Automated-Decision Privacy Sprint"),
    ("/services/ai-readiness-sprint/", "AI Readiness Sprint"),
    ("/services/quick-wins/", "Small business quick wins"),
]
INDUSTRIES = [
    ("/industries/trades/", "Trades & construction"),
    ("/industries/health/", "Health & allied health"),
    ("/industries/startups/", "Startups & tech agencies"),
    ("/industries/crypto/", "Crypto & digital assets"),
    ("/industries/not-for-profits/", "Not-for-profits"),
    ("/industries/hospitality-retail/", "Hospitality & retail"),
]

TOPICS = ["AI readiness & governance", "AI Readiness Sprint", "Privacy Act automated-decision check",
          "Automation & AI agents", "Dashboards & analytics", "Financial modelling", "Tech project delivery",
          "Small business quick win", "Something else"]


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def contact_form(heading="Tell us what you're trying to fix.", lede="A few lines is plenty. We work in writing first: you'll get a written reply within three business days, and any call is arranged by agreement.", eyebrow="Start in writing"):
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
  </div>
</section>'''


def cta_band(title="Not sure where to start?", text="Send a few lines in writing. You'll get a considered reply, not a sales pitch.", topic=None):
    href = "/contact/" + (f"?topic={topic.replace(' ', '%20').replace('&', '%26')}" if topic else "") + "#form"
    return f'''<section class="band"><div class="wrap cta-band"><div><h2>{title}</h2><p class="muted">{text}</p></div>
  <div class="cta" style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn primary" href="{href}">Start in writing</a><button class="btn" type="button" data-open-bot>Ask Beiz</button></div></div></section>'''


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

    def dd(label, hub, items, key):
        links = "".join(f'<a href="{h}"{cur(h)}>{t}</a>' for h, t in items)
        on = ' class="on"' if path.startswith(hub) else ""
        return (f'<div class="dd"><button type="button" aria-expanded="false" aria-controls="dd-{key}"{on}>{label}<span aria-hidden="true">▾</span></button>'
                f'<div class="ddm" id="dd-{key}"><a class="hub" href="{hub}">All {label.lower()} →</a>{links}</div></div>')
    live = lambda h, t: f'<a href="{h}"{cur(h)}>{t}{" <i class=live-dot aria-hidden=true></i>" if h == "/live/" else ""}</a>'
    nav = (dd("Services", "/services/", SERVICES, "s") + dd("Industries", "/industries/", INDUSTRIES, "i") +
           "".join(live(h, t) for h, t, _ in NAV) + dd("About", "/about/", MORE, "m").replace('<a class="hub" href="/about/">All about →</a>', ""))
    grp = lambda title, items: f'<p class="mg">{title}</p>' + "".join(f'<a href="{h}">{t}</a>' for h, t in items)
    mnav = (grp("Services", SERVICES) + grp("Industries", INDUSTRIES) +
            grp("See it", [(h, t) for h, t, _ in NAV]) + grp("About", MORE))
    return f'''<div class="ticker" role="region" aria-label="Beiz Pulse: regulatory countdown and market benchmarks">
  <div class="label">BEIZ PULSE</div>
  <div class="track" id="pulse"></div>
</div>
<header class="site">
  <div class="wrap">
    <a class="mark" href="/" aria-label="Beiz home">{LOGO}<span class="wm"><span class="wn">Beiz<span class="wx"> Data &amp; Accounting</span></span><small>CA · GAICD · AI · Data</small></span></a>
    <nav class="main" aria-label="Main">{nav}</nav>
    <a class="btn primary" href="/contact/#form">Start in writing</a>
    <button class="menu-btn" id="menuBtn" type="button" aria-controls="mnav" aria-expanded="false">MENU</button>
  </div>
  <div class="mnav" id="mnav"><div class="wrap">{mnav}<a class="btn primary" href="/contact/#form">Start in writing</a></div></div>
</header>'''


def _footer():
    s = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in SERVICES)
    i = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in INDUSTRIES)
    return f'''<footer class="site">
  <div class="wrap">
    <div class="fcols">
      <div><a class="mark" href="/" aria-label="Beiz home">{LOGO.replace('id="hg"', 'id="fg"').replace('url(#hg)', 'url(#fg)').replace('id="mH"', 'id="fM"').replace('url(#mH)', 'url(#fM)')}<span class="wm">Beiz<small>Data · AI · Accounting</small></span></a>
        <p style="margin-top:14px;max-width:34ch">Governed AI, automation, dashboards and financial models for Australian businesses. Chartered Accountant and GAICD led.</p>
        <p style="margin-top:10px"><a href="mailto:hello@beiz.com.au">hello@beiz.com.au</a></p></div>
      <div><h4>Services</h4><ul>{s}</ul></div>
      <div><h4>Industries</h4><ul>{i}</ul></div>
      <div><h4>Company</h4><ul><li><a href="/about/">About us</a></li><li><a href="/try/">Try it: demos</a></li><li><a href="/examples/">Examples</a></li><li><a href="/live/">Live data</a></li><li><a href="/how-we-work/">How we work</a></li><li><a href="/ai-check/">Privacy Act AI check</a></li><li><a href="/insights/">Insights</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy/">Privacy policy</a></li></ul></div>
    </div>
    <div class="legal"><span>&copy; <span data-yr>2026</span> Beiz Data &amp; Accounting Pty Ltd · ABN 53 691 755 496</span><span>Australia-wide · Fixed-scope finance systems &amp; AI governance</span>
      <p>Liability limited by a scheme approved under Professional Standards Legislation. Beiz does not provide tax agent, BAS agent, legal or financial product advice services.</p></div>
  </div>
</footer>'''


_WIDGETS = '''<button class="bot-btn" type="button" data-open-bot aria-controls="bot" aria-expanded="false" aria-label="Open Ask Beiz, the guided assistant"><i aria-hidden="true"></i><span>Ask Beiz</span></button>
<button class="sb-tab" type="button" id="sbTab" aria-controls="sb" aria-expanded="false"><i aria-hidden="true"></i>LIVE<span> MARKETS &amp; SCORES</span></button>
<aside class="sb" id="sb" aria-label="Live data lab: markets and scores" aria-hidden="true">
  <header><b>LIVE DATA LAB</b><button type="button" id="sbClose" aria-label="Close">&times;</button></header>
  <p class="lab">A live demonstration of resilient data pipelines: multiple public sources pulled in, normalised and shown clearly, with no client-side tracking and automatic fail-safes if a source drops.</p>
  <nav role="tablist" id="sbNav"></nav>
  <div class="list" id="sbList"><p class="st">Loading&hellip;</p></div>
  <div class="foot"><a href="/live/" style="color:var(--accent)">Open the full Live Data page →</a><br>Scores via ESPN and live crypto via CoinGecko, loaded only when you open this panel. ASX delayed. Indicative only, not financial advice. Times in your time zone.</div>
</aside>
<div class="bot" id="bot" role="dialog" aria-label="Beiz guided assistant">
  <div class="hd"><div><b>Ask Beiz</b><small>GUIDED · NO AI · NOTHING STORED</small></div><button class="x" type="button" aria-label="Close assistant">&times;</button></div>
  <div class="msgs" id="msgs" aria-live="polite"></div>
  <div class="opts" id="opts"></div>
</div>'''

ORG = {
    "@context": "https://schema.org", "@type": "ProfessionalService",
    "name": "Beiz Data & Accounting", "legalName": "Beiz Data & Accounting Pty Ltd", "url": SITE + "/",
    "email": "hello@beiz.com.au", "logo": SITE + "/assets/icon-512.png", "areaServed": {"@type": "Country", "name": "Australia"},
    "description": "Australian Chartered Accountant and GAICD led firm helping businesses grow with control: cash flow, automation, dashboards, data and responsible AI.",
    "taxID": "53 691 755 496",
}


def page(path, title, desc, body, extra_head=""):
    full_title = title if "Beiz" in title else f"{title} | Beiz"
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
<meta name="theme-color" content="#07090b">
<meta property="og:type" content="website"><meta property="og:site_name" content="Beiz Data &amp; Accounting">
<meta property="og:title" content="{esc(full_title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/assets/icon-512.png">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/inter-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
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
{_WIDGETS}
<script src="/assets/site.js?v={ASSET_V}" defer></script>
</body>
</html>
'''
