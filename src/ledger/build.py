#!/usr/bin/env python3
"""Build beiz.com.au, "Ledger" edition (Nov 2026).

Run from the repo root:  python3 src/ledger/build.py
Writes the published pages into the repo root, plus sitemap.xml, robots.txt and llms.txt.
Content lives in src/ledger/content.py; this file is layout only.
"""
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ASSET_V = "L9"  # bump on every CSS or JS change
SITE = "https://beiz.com.au"
e = html.escape

NAV = [("/services/", "Services"), ("/how-we-work/", "How it works"), ("/prices/", "Prices"),
       ("/bill-check/", "Free bill check"), ("/about/", "About")]

LD = """{"@context":"https://schema.org","@type":"ProfessionalService","name":"Beiz Data & Accounting Pty Ltd",
"url":"https://beiz.com.au/","email":"hello@beiz.com.au","logo":"https://beiz.com.au/assets/brand/beiz-icon-512.png",
"address":{"@type":"PostalAddress","addressLocality":"Canberra","addressRegion":"ACT","addressCountry":"AU"},
"areaServed":"AU","sameAs":["https://github.com/TheBeizWay"],"taxID":"53 691 755 496",
"description":"AI for real business work, with guardrails, set up and checked by an Australian Chartered Accountant."}"""


def head(path, title, desc):
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/assets/og-card.png">
<meta property="og:type" content="website">
<meta name="theme-color" content="#F5F2EA">
<link rel="icon" href="/assets/brand/beiz-icon.svg">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/source-serif-4-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/ledger/ledger.css?v={ASSET_V}">
<script type="application/ld+json">{LD}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(path):
    links = "".join(
        f'<a href="{h}"{" aria-current=page" if path == h else ""}>{t}</a>' for h, t in NAV) + '<a class="m" href="/contact/">Contact</a>'
    return f"""<header class="top"><div class="wrap">
<a class="brand" href="/" aria-label="Beiz Data &amp; Accounting, home"><img src="/assets/ledger/beiz-lockup.png" alt="Beiz Data &amp; Accounting" width="149" height="44"></a>
<nav class="nav" aria-label="Main">{links}</nav>
<a class="btn" href="/contact/">Talk to us</a>
<button class="menu" type="button" aria-expanded="false" aria-label="Open menu">Menu</button>
</div></header>
"""


def footer():
    return f"""<footer class="foot"><div class="wrap">
<div class="grid">
<div>
<p><b>Beiz Data &amp; Accounting</b><br>AI for real business work, set up and checked by an Australian Chartered Accountant. Canberra, working Australia-wide.</p>
<p><a href="mailto:hello@beiz.com.au">hello@beiz.com.au</a></p>
<div class="ca"><img src="/assets/media/ca-logo-reversed.png" alt="Chartered Accountants Australia and New Zealand" width="140" height="80" ></div>
</div>
<div><h4>Work with us</h4><ul>
<li><a href="/services/">Services</a></li><li><a href="/how-we-work/">How it works</a></li><li><a href="/prices/">Prices</a></li><li><a href="/bill-check/">Free bill check</a></li></ul></div>
<div><h4>Company</h4><ul>
<li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy/">Privacy</a></li><li><a href="/card/">Digital card</a></li></ul></div>
</div>
<div class="legal">
<p>{C.FACTS_LINE}</p>
<p>Liability limited by a scheme approved under Professional Standards Legislation. Professional indemnity insurance held.</p>
<p>Trade mark of Chartered Accountants Australia and New Zealand and used with permission.</p>
<p>&copy; <span data-yr>2026</span> Beiz Data &amp; Accounting Pty Ltd</p>
</div>
</div></footer>
<script src="/assets/ledger/ledger.js?v={ASSET_V}" defer></script>
"""


def page(path, title, desc, body, extra_js=""):
    return head(path, title, desc) + header(path) + f'<main id="main">\n{body}\n</main>\n' + footer() + extra_js + "</body>\n</html>\n"


def sec(label, inner, cls="", sid=""):
    i = f' id="{sid}"' if sid else ""
    return f'<section class="sec {cls}"{i}><div class="wrap"><div class="lab">{label}</div><div class="body">{inner}</div></div></section>\n'


def phead(h1, lede):
    return f'<header class="phead"><div class="wrap"><h1>{h1}</h1><p class="lede">{lede}</p></div></header>\n'


def rows(items):
    return '<div class="rows">' + "".join(f'<div class="row"><h3>{a}</h3><p>{b}</p></div>' for a, b in items) + "</div>"


def price_table(items, head3=("Offer", "What you get", "Price")):
    out = f'<table class="led"><thead><tr><th>{head3[0]}</th><th>{head3[1]}</th><th class="amt">{head3[2]}</th></tr></thead><tbody>'
    for name, desc, price, link in items:
        nm = f'<a href="{link}">{name}</a>' if link else name
        out += f'<tr><td>{nm}</td><td data-h="">{desc}</td><td class="amt">{price}</td></tr>'
    return out + "</tbody></table>"


def who_block(full=False):
    bio = C.BIO_FULL if full else C.BIO
    return f"""<div class="who">
<img class="p" src="/assets/media/purav-mehta-2.jpg" alt="Purav Mehta" width="200" height="267" loading="lazy">
<div><h3>Purav Mehta CA, GAICD</h3><p class="role">Founder and principal</p>{bio}
<div class="calogo"><img src="/assets/media/ca-logo.svg" alt="Chartered Accountants Australia and New Zealand" width="147" height="84">
<p>Trade mark of Chartered Accountants Australia and New Zealand and used with permission.</p></div></div></div>"""


# ---------------------------------------------------------------- pages
def home():
    rowsb = "".join(
        f'<tr><td class="s"><span class="dot {c}"></span>{lab}</td><td>{t}</td><td class="n">{n}</td></tr>'
        for c, lab, t, n in C.HERO_BOOK)
    book = f"""<div class="book" role="img" aria-label="Example week for a made-up business: 42 bills received, 38 matched, 3 held for a person, 1 stopped.">
<div class="cap"><span>Bills this week</span><span>Example, made-up business</span></div>
<table><tbody><tr><td class="s"></td><td>Bills received</td><td class="n">42</td></tr>{rowsb}
<tr class="tot"><td class="s"></td><td>Paid without a person's sign-off</td><td class="n">0</td></tr></tbody></table>
<p class="bnote">Each held or stopped bill shows the reason and the records behind it.</p></div>"""
    hero = f"""<section class="hero"><div class="wrap">
<div><h1>{C.HERO_H1}</h1><p class="lede">{C.HERO_LEDE}</p>
<div class="acts"><a class="btn" href="/contact/">Book a 20-minute call</a><a class="btn line" href="/bill-check/">Try the free bill check</a></div>
<div class="credrow"><img src="/assets/media/ca-logo.svg" alt="Chartered Accountants Australia and New Zealand" width="147" height="84"><p class="cred">{C.HERO_CRED}<br><span class="tm">Trade mark of Chartered Accountants Australia and New Zealand and used with permission.</span></p></div></div>
{book}</div></section>
"""
    jobs = '<table class="led tw"><thead><tr><th>Job</th><th>Today</th><th>With a Beiz agent</th></tr></thead><tbody>' + "".join(
        f'<tr><td>{a}</td><td data-h="Today">{b}</td><td data-h="With a Beiz agent">{c}</td></tr>' for a, b, c in C.JOBS) + "</tbody></table>"
    body = hero
    body += sec("Where it helps", f"<h2>The routine work an agent takes on</h2><p class=\"intro\">{C.JOBS_INTRO}</p>{jobs}")
    bcl = "".join(f"<li>{x}</li>" for x in C.HOME_BC)
    body += sec("Try it now", f"<h2>Run the free bill check on your own bills</h2><p class=\"intro\">Export your bills from Xero, MYOB or QuickBooks and drop the file in. Eight checks run in your browser in a few seconds. Nothing is uploaded or sent to us.</p><ul class=\"plain\">{bcl}</ul><div class=\"acts\"><a class=\"btn\" href=\"/bill-check/\">Run the free bill check</a></div>")
    body += sec("Ways to start", f"<h2>Three ways to start</h2>{price_table(C.START)}<p class=\"note\">{C.PRICE_NOTE} <a href=\"/prices/\">See every price</a>.</p>")
    body += sec("How it stays safe", f"<h2>Nothing runs on its own on day one</h2>{rows(C.SAFE)}<p class=\"note\">{C.NOT_DO} <a href=\"/how-we-work/\">How a build runs</a>.</p>")
    body += sec("Who you'll deal with", f"<h2>One accountable person, from first call to handover</h2>{who_block()}")
    body += sec("Next step", f"<h2>Talk or write. Either way, a reply by the next business day.</h2><p class=\"intro\">{C.CTA_TEXT}</p><div class=\"acts\"><a class=\"btn\" href=\"/contact/\">Start in writing</a><a class=\"btn line\" href=\"/contact/?topic=Discovery%20call\">Book a 20-minute call</a></div>", "dark")
    return page("/", "Beiz Data & Accounting | AI for real work, checked by a Chartered Accountant", C.HOME_DESC, body)


def services():
    body = phead("Services", C.SERVICES_LEDE)
    for g in C.GROUPS:
        body += sec(g["title"], f'<h2>{g["intro"]}</h2>' + price_table(g["items"], ("Service", "What it covers", "Price")))
    body += sec("What we don't do", f"<p class=\"intro\">{C.NOT_DO}</p>")
    body += sec("Next step", f"<h2>Not sure which one fits?</h2><p class=\"intro\">Describe the problem in a few lines. If we're not the right fit, we'll say so.</p><div class=\"acts\"><a class=\"btn\" href=\"/contact/\">Describe the problem</a></div>", "dark")
    return page("/services/", "Services | Beiz Data & Accounting", "Finance, data, automation and governance work for Australian small businesses, with fixed prices where the scope allows.", body)


def how():
    body = phead("How it works", C.HOW_LEDE)
    body += sec("The first 30 days", f"<h2>From first message to a working agent</h2>{rows(C.FIRST30)}")
    body += sec("How it's built", f"<h2>Rules first. AI only for the exceptions.</h2><p class=\"intro\">Most finance work follows rules, so rules do most of the work. That keeps every step traceable and the running costs low.</p>{rows(C.RULES_FIRST)}")
    body += sec("Every agent", f"<h2>What every Beiz build includes</h2><ul class=\"plain\">{''.join(f'<li>{x}</li>' for x in C.INCLUDES)}</ul>")
    body += sec("Findings", f"<h2>We report what the records support</h2>{rows(C.FINDINGS)}")
    body += sec("Scope", f"<h2>What we don't do</h2><p class=\"intro\">{C.NOT_DO}</p>")
    body += sec("Next step", "<h2>Start with one workflow</h2><p class=\"intro\">Tell us which piece of work takes the most hours. We'll reply in writing by the next business day.</p><div class=\"acts\"><a class=\"btn\" href=\"/contact/\">Talk to us</a></div>", "dark")
    return page("/how-we-work/", "How it works | Beiz Data & Accounting", "How Beiz sets up an AI agent: tested on your past records, shadow mode first, a person signs off, every decision logged.", body)


def prices():
    body = phead("Prices", C.PRICES_LEDE)
    body += sec("Fixed and starting prices", "<h2>What things cost</h2>" + price_table(C.PRICES))
    body += sec("The fine print", f"<h2>Terms that matter</h2>{rows(C.PRICE_TERMS)}")
    body += sec("Next step", "<h2>Want a fixed price for your job?</h2><p class=\"intro\">Proposals come within three business days, with a fixed price, a timeline and a definition of done.</p><div class=\"acts\"><a class=\"btn\" href=\"/contact/\">Ask for a proposal</a></div>", "dark")
    return page("/prices/", "Prices | Beiz Data & Accounting", "Beiz prices in AUD: free bill check, $1,500 two-week cash and data check, compliance sprint from $3,500, and more.", body)


def about():
    facts = '<table class="facts"><tbody>' + "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in C.FACTS) + "</tbody></table>"
    body = phead("About Beiz", C.ABOUT_LEDE)
    body += sec("Founder", f"<h2>Who does the work</h2>{who_block(full=True)}")
    body += sec("How we're set up", f"<h2>Founder-led, by design</h2><p class=\"intro\">{C.SETUP}</p>")
    body += sec("Company details", f"<h2>The facts</h2>{facts}")
    body += sec("What we don't do", f"<p class=\"intro\">{C.NOT_DO}</p>")
    return page("/about/", "About | Beiz Data & Accounting", "Beiz Data & Accounting Pty Ltd: a Canberra practice led by Purav Mehta CA, GAICD, setting up AI with guardrails for Australian businesses.", body)


def contact():
    opts = "".join(f"<option>{e(o)}</option>" for o in C.TOPICS)
    form = f"""<form class="form" id="contactForm" novalidate>
<div><label for="f-name">Name</label><input id="f-name" name="name" autocomplete="name" required></div>
<div><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
<div><label for="f-org">Business or organisation</label><input id="f-org" name="organisation" autocomplete="organization"></div>
<div><label for="f-topic">Area</label><select id="f-topic" name="topic">{opts}</select></div>
<div class="full"><label for="f-msg">What's the problem?</label><textarea id="f-msg" name="message" required placeholder="For example: month-end takes eight days and half of it is copying data between Xero and Excel."></textarea></div>
<input class="hp" name="company_website" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="full"><button class="btn" type="submit">Send</button><p class="fine" style="margin-top:12px">We only use your details to reply. Please don't include passwords or bank details. See our <a href="/privacy/">privacy policy</a>.</p></div>
<p class="formmsg full" id="formMsg" role="status" aria-live="polite"></p>
</form>"""
    body = phead("Talk to us", C.CONTACT_LEDE)
    body += sec("Write", f"<h2>Start in writing</h2>{form}", sid="form")
    body += sec("What to expect", rows(C.EXPECT))
    body += sec("Email", '<p class="intro"><a href="mailto:hello@beiz.com.au">hello@beiz.com.au</a></p>')
    return page("/contact/", "Contact | Beiz Data & Accounting", "Write to Beiz Data & Accounting. A written reply by the next business day; calls are 20 minutes, early morning or after 5pm.", body)


def bill_check():
    tool = """<div class="bck" id="bc">
<div class="bck-in">
<label class="bck-drop" id="bcDrop"><input type="file" id="bcFile" accept=".csv,.txt,.tsv,text/csv"><b>Drop your bills CSV here</b><span>or click to choose a file</span><span class="bck-dfmt">Dates should be DD/MM/YYYY. You'll see how they're read and confirm before any check runs.</span></label>
<div class="bck-side">
<button type="button" class="btn" id="bcSample">Try it with sample data</button>
<p class="fine">Six months of bills from a made-up building company, with a few problems planted. <a href="/data/sample-bills.csv" download>Download the sample file</a> to see the format.</p>
<label class="bck-lim">Your approval limit ($)<input id="bcLimit" type="number" value="5000" min="1" step="100" inputmode="decimal"></label>
</div></div>
<p class="bck-status" id="bcStatus" aria-live="polite"></p>
<div id="bcMap"></div>
<div id="bcOut" aria-live="polite"></div>
</div>"""
    faq = "".join(f"<div class=\"row\"><h3>{q}</h3><p>{a}</p></div>" for q, a in C.BC_FAQ)
    ld = '<script type="application/ld+json">' + __import__("json").dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in C.BC_FAQ]}) + "</script>"
    body = phead("Free bill check", C.BC_LEDE)
    body += sec("Run it", f"<h2>Check your bills for duplicates and red flags</h2>{tool}")
    body += sec("What it checks", f"<ul class=\"plain\">{''.join(f'<li>{x}</li>' for x in C.BC_CHECKS)}</ul>")
    body += sec("Getting the file", f"<p class=\"intro\">{C.BC_FILE}</p>")
    body += sec("Common questions", f'<div class="rows">{faq}</div>')
    body += sec("Limits", f"<p class=\"intro\">{C.BC_LIMITS}</p>")
    body += sec("Next step", "<h2>Want these checks on every bill?</h2><p class=\"intro\">They're a small slice of the two-week cash and data check ($1,500 fixed), and of a bills agent that runs them before anything is paid and holds anything odd for a person.</p><div class=\"acts\"><a class=\"btn\" href=\"/contact/?topic=Two-week%20cash%20%26%20data%20check\">Ask about the check</a></div>", "dark")
    js = f'<script src="/assets/billcheck.js?v={ASSET_V}" defer></script>\n'
    return page("/bill-check/", "Free bill check | Beiz Data & Accounting", "Check a bills export from Xero, MYOB or QuickBooks for duplicates, changed bank details and split bills. Runs in your browser; nothing is uploaded.", body, js + ld)


def privacy():
    body = phead("Privacy policy", "How we handle personal information. Last updated 5 November 2026.")
    body += f'<section class="sec"><div class="wrap"><div class="lab">Policy</div><div class="body prose">{C.PRIVACY}</div></div></section>'
    return page("/privacy/", "Privacy policy | Beiz Data & Accounting", "How Beiz Data & Accounting Pty Ltd handles personal information.", body)


def notfound():
    body = phead("Page not found", "That page has moved or no longer exists. The site was simplified in November 2026.")
    body += sec("Try", '<ul class="plain"><li><a href="/">Home</a></li><li><a href="/services/">Services</a></li><li><a href="/prices/">Prices</a></li><li><a href="/bill-check/">Free bill check</a></li><li><a href="/contact/">Contact</a></li></ul>')
    return page("/404.html", "Page not found | Beiz Data & Accounting", "Page not found.", body)


def redirect(to):
    return f'<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>Moved</title><meta name="robots" content="noindex"><link rel="canonical" href="{SITE}{to}"><meta http-equiv="refresh" content="0; url={to}"></head><body><p>This page has moved to <a href="{to}">{SITE}{to}</a>.</p></body></html>\n'


PAGES = {"/": home, "/services/": services, "/how-we-work/": how, "/prices/": prices, "/about/": about,
         "/contact/": contact, "/bill-check/": bill_check, "/privacy/": privacy}


def write(path, text):
    f = os.path.join(ROOT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w", encoding="utf-8").write(text)


def main():
    for p, fn in PAGES.items():
        write(p, fn())
    write("/404.html", notfound())
    for old, new in C.REDIRECTS.items():
        write(old, redirect(new))
    urls = "".join(f"<url><loc>{SITE}{p}</loc></url>" for p in PAGES)
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    open(os.path.join(ROOT, "llms.txt"), "w").write(C.LLMS)
    print("built", len(PAGES), "pages,", len(C.REDIRECTS), "redirects")


if __name__ == "__main__":
    main()
