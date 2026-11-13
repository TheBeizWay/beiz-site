#!/usr/bin/env python3
"""Build beiz.com.au, "Ledger" edition (Nov 2026).

Run from the repo root:  python3 src/ledger/build.py
Writes the published pages into the repo root, plus sitemap.xml, robots.txt and llms.txt.
Content lives in src/ledger/content.py; this file is layout only.
"""
import html, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C
import content_more as M
import json
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ASSET_V = "L30"  # bump on every CSS or JS change
SITE = "https://beiz.com.au"
e = html.escape

NAV = [("/services/", "Services"), ("/how-we-work/", "How it works"), ("/prices/", "Fees"),
       ("/bill-check/", "Try the bill check"), ("/about/", "About")]

HELPER_TMPL = """<button type="button" class="hbtn" aria-controls="helper" aria-expanded="false">Ask Beiz</button>
<div class="helper" id="helper" role="dialog" aria-label="Ask Beiz, guided helper" hidden>
<div class="hhead"><b>Ask Beiz</b><button type="button" class="hclose" aria-label="Close helper">Close</button></div>
<p class="hintro">{intro}</p>
<div class="hlog" aria-live="polite"></div>
<div class="hqs"></div>
<form class="hform"><label class="skip" for="hq">Your question</label><input id="hq" type="text" placeholder="Ask about fees, AML, the bill check..." autocomplete="off" maxlength="200"><button class="btn" type="submit">Ask</button></form>
</div>
<script type="application/json" id="helper-data">{data}</script>
"""

LD = """{"@context":"https://schema.org","@type":"ProfessionalService","name":"Beiz Data & Accounting Pty Ltd",
"url":"https://beiz.com.au/","email":"hello@beiz.com.au","logo":"https://beiz.com.au/assets/brand/beiz-icon-512.png",
"address":{"@type":"PostalAddress","addressLocality":"Canberra","addressRegion":"ACT","addressCountry":"AU"},
"areaServed":"AU","sameAs":["https://www.linkedin.com/company/beiz-data-accounting/","https://github.com/TheBeizWay"],"taxID":"53 691 755 496",
"description":"AI for real business work, with guardrails, set up and checked by an Australian Chartered Accountant.",
"founder":{"@type":"Person","name":"Purav Mehta","jobTitle":"Principal","sameAs":["https://www.linkedin.com/in/puravmehtaca/"],"hasCredential":[{"@type":"EducationalOccupationalCredential","credentialCategory":"Professional membership","name":"Chartered Accountant (CA) with a Certificate of Public Practice","recognizedBy":{"@type":"Organization","name":"Chartered Accountants Australia and New Zealand","url":"https://www.charteredaccountantsanz.com"}},{"@type":"EducationalOccupationalCredential","name":"Graduate of the Australian Institute of Company Directors (GAICD)","recognizedBy":{"@type":"Organization","name":"Australian Institute of Company Directors","url":"https://www.aicd.com.au"}}]}}"""


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
<meta name="theme-color" content="#13221B">
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


def gslug(t):
    return re.sub(r"[^a-z]+", "-", t.lower()).strip("-")


def header(path):
    def item(h, t):
        a = f'<a href="{h}"{" aria-current=page" if path == h else ""}>{t}</a>'
        if h != "/services/":
            return a
        cols = "".join(
            f'<div class="mcol"><a class="mh" href="/services/#{gslug(g["title"])}">{g["title"]}</a><p>{g["intro"]}</p><ul>'
            + "".join(f'<li><a href="{DETAIL.get(n, "/services/#" + gslug(g["title"]))}">{n}</a><span>{p}</span></li>' for n, d, p, _ in g["items"])
            + "</ul></div>" for g in C.GROUPS)
        return f'<div class="dd">{a}<div class="mega" role="region" aria-label="Services"><div class="wrap">{cols}</div></div></div>'
    links = "".join(item(h, t) for h, t in NAV) + '<a class="m" href="/contact/">Contact</a>'
    return f"""<header class="top"><div class="wrap">
<a class="brand" href="/" aria-label="Beiz Data &amp; Accounting, home"><img src="/assets/ledger/beiz-lockup.png" alt="Beiz Data &amp; Accounting" width="149" height="44"></a>
<span class="cobrand"><img src="/assets/media/ca-logo-vertical.svg" alt="Chartered Accountants Australia and New Zealand" width="96" height="108"></span>
<nav class="nav" aria-label="Main">{links}</nav>
<a class="btn" href="/contact/">Talk to us</a>
<button class="menu" type="button" aria-expanded="false" aria-label="Open menu">Menu</button>
</div><div class="tmstrip"><div class="wrap">Trade mark of Chartered Accountants Australia and New Zealand and used with permission.</div></div></header>
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
<li><a href="/services/">Services</a></li><li><a href="/aml-ctf-accounting-firms/">AML/CTF for accounting firms</a></li><li><a href="/how-we-work/">How it works</a></li><li><a href="/prices/">Fees</a></li><li><a href="/bill-check/">Free bill check</a></li></ul></div>
<div><h4>Company</h4><ul>
<li><a href="/about/">About</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/insights/">Insights</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy/">Privacy</a></li><li><a href="/card/">Digital card</a></li><li><a href="https://www.linkedin.com/company/beiz-data-accounting/" rel="noopener">LinkedIn</a></li></ul></div>
</div>
<div class="legal">
<p>{C.FACTS_LINE}</p>
<p>Liability limited by a scheme approved under Professional Standards Legislation. Professional indemnity insurance held with Chubb.</p>
<p>Trade mark of Chartered Accountants Australia and New Zealand and used with permission.</p>
<p>&copy; <span data-yr>2026</span> Beiz Data &amp; Accounting Pty Ltd</p>
</div>
</div></footer>
<script src="/assets/ledger/ledger.js?v={ASSET_V}" defer></script>
<script src="/assets/ledger/webmcp.js?v={ASSET_V}" defer></script>
"""


def helper_html():
    import json as _j, re as _re
    strip = lambda t: _re.sub(r"<[^>]+>", "", t).replace("&amp;", "&")
    data = [dict(x) for x in C.HELPER_EXTRA]
    for q, a in M.FAQ:
        data.append({"q": strip(q), "k": "", "a": strip(a), "href": "/faq/", "link": "Open the FAQ"})
    js = _j.dumps(data).replace("</", "<\\/")
    return HELPER_TMPL.format(intro=C.HELPER_INTRO, data=js)


def news_strip():
    items = "".join(
        f'<li class="ni"><span class="ntag">{e(n["tag"])}</span><a class="ntext" href="{n["src"]}" rel="noopener" target="_blank">{e(n["text"])}</a>'
        + (f'<span class="nwhen" data-date="{n["date"]}"></span>' if n["date"] else "")
        + f'<a class="nbeiz" href="{n["href"]}">{e(n["beiz"])}</a></li>' for n in C.NEWS)
    return (f'<section class="news" aria-label="What\'s changing for Australian businesses"><div class="wrap">'
            f'<span class="nlabel">What\'s changing</span><div class="nview"><ul class="ntrack">{items}</ul></div>'
            f'<button type="button" class="npause" aria-pressed="false">Pause</button></div></section>\n')


def page(path, title, desc, body, extra_js=""):
    return head(path, title, desc) + header(path) + f'<main id="main">\n{body}\n</main>\n' + footer() + extra_js + "</body>\n</html>\n"


def sec(label, inner, cls="", sid=""):
    i = f' id="{sid}"' if sid else ""
    return f'<section class="sec {cls}"{i}><div class="wrap"><div class="lab">{label}</div><div class="body">{inner}</div></div></section>\n'


def wsec(kicker, inner, cls="", sid=""):
    i = f' id="{sid}"' if sid else ""
    k = f'<p class="kick">{kicker}</p>' if kicker else ""
    return f'<section class="wsec {cls}"{i}><div class="wrap">{k}{inner}</div></section>\n'


def phead(h1, lede, crumb=None, byline=""):
    c = f'<p class="crumb"><a href="{crumb[0]}">{crumb[1]}</a></p>' if crumb else ""
    b = f'<p class="byline">{byline}</p>' if byline else ""
    return f'<header class="phead"><div class="wrap">{c}<h1>{h1}</h1><p class="lede">{lede}</p>{b}</div></header>\n'


def rows(items):
    return '<div class="rows">' + "".join(f'<div class="row"><h3>{a}</h3><p>{b}</p></div>' for a, b in items) + "</div>"


def price_table(items, head3=("Engagement", "What you get", "")):
    out = f'<table class="led"><thead><tr><th>{head3[0]}</th><th>{head3[1]}</th></tr></thead><tbody>'
    items = [(n, d, pr, DETAIL.get(n) or l) for n, d, pr, l in items]
    for name, desc, price, link in items:
        nm = f'<a href="{link}">{name}</a>' if link else name
        out += f'<tr><td>{nm}</td><td data-h="">{desc}</td></tr>'
    return out + "</tbody></table>"


def who_block(full=False):
    bio = C.BIO_FULL if full else C.BIO
    return f"""<div class="who">
<img class="p" src="/assets/media/purav-mehta-2.jpg" alt="Purav Mehta" width="200" height="267">
<div><h3>Purav Mehta CA, GAICD</h3><p class="role">Founder and principal</p>{bio}
<p class="li"><a href="https://www.linkedin.com/in/puravmehtaca/" rel="noopener">Purav on LinkedIn</a></p>
<div class="calogo"><img src="/assets/media/ca-logo.svg" alt="Chartered Accountants Australia and New Zealand" width="147" height="84">
<p>Trade mark of Chartered Accountants Australia and New Zealand and used with permission.</p></div></div></div>"""


# ---------------------------------------------------------------- pages
def home():
    hero = f"""<section class="hero2"><div class="wrap">
<div class="h2main">
<p class="hkick">Beiz Data &amp; Accounting, Canberra</p>
<h1>AI that does the checking. <br>A Chartered Accountant who checks the AI.</h1>
<p class="lede">{C.HERO_LEDE}</p>
<div class="acts"><a class="btn" href="/contact/?topic=Discovery%20call">Book a 20-minute call</a><a class="btn line" href="/bill-check/">Try the free bill check</a></div>
<ul class="hfacts"><li><b>Chartered Accountant</b><span>Member of Chartered Accountants Australia and New Zealand, with a Certificate of Public Practice</span></li><li><b>Fixed fee</b><span>Agreed in writing before any work starts</span></li><li><b>A person signs off</b><span>Nothing is paid or sent by an agent alone</span></li></ul>
<div class="credrow"><img src="/assets/media/ca-logo.svg" alt="Chartered Accountants Australia and New Zealand" width="147" height="84"><p class="cred">Trade mark of Chartered Accountants Australia and New Zealand and used with permission.</p></div>
</div>
<figure class="hphoto"><img src="/assets/media/purav-mehta-2.jpg" alt="Purav Mehta" width="480" height="640" fetchpriority="high">
<figcaption><b>Purav Mehta CA, GAICD</b><span>Founder. You deal with him from the first call to handover.</span></figcaption></figure>
</div></section>
"""
    body = hero
    jobs = '<div class="jobs4">' + "".join(
        f'<article class="job"><p class="num">{i:02d}</p><h3>{a}</h3><p class="was"><span>Today</span>{b}</p><p class="now"><span>With a Beiz agent</span>{c}</p></article>'
        for i, (a, b, c) in enumerate(C.JOBS, 1)) + "</div>"
    body += wsec("Where it helps", f'<div class="whead"><h2>The routine work an agent takes on</h2><p class="intro">{C.JOBS_INTRO}</p></div>{jobs}')
    body += ('<section class="band"><div class="wrap"><p class="big">Nothing is paid or sent without a person.</p>'
             '<p>Every agent is tested on your past records, runs alongside your team in shadow mode first, and logs every decision in your own accounts.</p></div></section>\n')
    start = '<div class="start3">' + "".join(
        f'<a class="st" href="{DETAIL.get(n) or l}"><p class="num">{i:02d}</p><h3>{n}</h3><p>{d}</p><span class="go">Read more</span></a>'
        for i, (n, d, _p, l) in enumerate(C.START, 1)) + "</div>"
    body += wsec("Ways to start", f'<div class="whead"><h2>Three ways to start</h2><p class="intro">{C.PRICE_NOTE} <a href="/prices/">How fees work</a>.</p></div>{start}<p class="allsvc"><a href="/services/">See every service</a>: cash and profit models, workflow automation, dashboards, AI governance, AML/CTF for accounting firms and workshops.</p>', "white")
    bcl = "".join(f"<li>{x}</li>" for x in C.HOME_BC)
    sample = ('<div class="bcard" aria-label="Example bill check results on a made-up building company\'s bills">'
              '<div class="bchead"><span>Bill check results</span><span>Example results, made-up business</span></div>'
              '<ul>'
              '<li><span class="dot stop"></span><div><b>Bank details changed</b><p>One supplier\'s account number differs from earlier bills.</p></div></li>'
              '<li><span class="dot held"></span><div><b>Possible duplicate</b><p>Same supplier and amount within 14 days, sent as an updated invoice.</p></div></li>'
              '<li><span class="dot held"></span><div><b>Invoice number reused</b><p>One supplier used the same invoice number twice.</p></div></li>'
              '<li><span class="dot held"></span><div><b>Looks split under the limit</b><p>Two bills on the same day, each just under your approval limit.</p></div></li>'
              '</ul><p class="bcnote">A flag is a prompt for a person to look. Many have an innocent explanation.</p></div>')
    body += wsec("Try it now", f'<div class="split"><div><h2>Run the free bill check on your own bills</h2><p class="intro">Export your bills from Xero, MYOB or QuickBooks and drop the file in. Eight checks run in your browser in a few seconds. Nothing is uploaded or sent to us.</p><ul class="ticks">{bcl}</ul><div class="acts"><a class="btn" href="/bill-check/">Run the free bill check</a></div></div>{sample}</div>', "forest", sid="see")
    safe = '<ol class="steps4">' + "".join(f'<li><span class="num">{i:02d}</span><h3>{a}</h3><p>{b}</p></li>' for i, (a, b) in enumerate(C.SAFE, 1)) + "</ol>"
    body += wsec("How it stays safe", f'<div class="whead"><h2>Nothing runs on its own on day one</h2></div>{safe}<p class="note">{C.NOT_DO} <a href="/how-we-work/">How a build runs</a>.</p>')
    body += wsec("Who you'll deal with", f"<div class=\"whead\"><h2>One accountable person, from first call to handover</h2></div>{who_block()}", "white who-sec")
    news = '<ul class="chg">' + "".join(
        f'<li><p class="ctag">{e(n["tag"])}</p><p class="ctext"><a href="{n["src"]}" rel="noopener" target="_blank">{e(n["text"])}</a></p><p class="cbeiz"><a href="{n["href"]}">{e(n["beiz"])}</a></p></li>' for n in C.NEWS) + "</ul>"
    body += wsec("Official sources", f'<div class="whead"><h2>What&rsquo;s changing for Australian businesses</h2><p class="intro">Each item links to the official source. General information, not advice.</p></div>{news}', sid="changing")
    body += wsec("", f"<div class=\"closer\"><h2>Talk or write. Either way, a reply by the next business day.</h2><p class=\"intro\">{C.CTA_TEXT}</p><div class=\"acts\"><a class=\"btn\" href=\"/contact/?topic=Discovery%20call\">Book a 20-minute call</a><a class=\"btn line\" href=\"/contact/\">Start in writing</a></div></div>", "forest")
    return page("/", "Beiz Data & Accounting | AI for real work, checked by a Chartered Accountant", C.HOME_DESC, body)


def services():
    body = phead("Services", C.SERVICES_LEDE)
    body += sec("Is Beiz a fit?", f"<h2>Who it's for, and the limits we work to</h2>{rows(C.FIT)}", sid="fit")
    for g in C.GROUPS:
        body += sec(g["title"], f'<h2>{g["intro"]}</h2>' + price_table(g["items"], ("Service", "What it covers", "")), sid=gslug(g["title"]))
    body += sec("What we don't do", f"<p class=\"intro\">{C.NOT_DO}</p>")
    body += sec("Next step", f"<h2>Not sure which one fits?</h2><p class=\"intro\">Describe the problem in a few lines. If we're not the right fit, we'll say so.</p><div class=\"acts\"><a class=\"btn\" href=\"/contact/\">Describe the problem</a></div>", "dark")
    return page("/services/", "Services | Beiz Data & Accounting", "Finance, data, automation and governance work for Australian small businesses, each a fixed fee agreed in writing.", body)


def how():
    body = phead("How it works", C.HOW_LEDE)
    body += sec("The first 30 days", f"<h2>From first message to a working agent</h2>{rows(C.FIRST30)}")
    body += sec("How it's built", f"<h2>Rules first. AI only for the exceptions.</h2><p class=\"intro\">Most finance work follows rules, so rules do most of the work. That keeps every step traceable and the running costs low.</p>{rows(C.RULES_FIRST)}")
    body += sec("How a bill gets in", f"<h2>Sorted, checked for doubles, then handled one at a time</h2>{rows(C.INTAKE)}", sid="intake")
    body += sec("Control status", f"<h2>A control isn't live until it's signed off</h2><p class=\"intro\">Every control moves through four states, and each change is recorded. An AI answer is a draft until a person approves it.</p>{rows(C.CONTROL_STATES)}", sid="status")
    body += sec("Stop conditions", f"<h2>When the work stops and waits for a person</h2><ul class=\"plain\">{''.join(f'<li>{x}</li>' for x in C.STOPS)}</ul><p class=\"note\">A stop can't be released by anything further down the line. Only the named person can clear it, and their decision is logged.</p>", sid="stops")
    body += sec("Decision log", f"<h2>Five things every check records</h2><p class=\"intro\">The log lives in your own accounts. Here is what each entry holds.</p>{rows(C.LOG_FIELDS)}", sid="log")
    body += sec("Every agent", f"<h2>What every Beiz build includes</h2><ul class=\"plain\">{''.join(f'<li>{x}</li>' for x in C.INCLUDES)}</ul>")
    body += sec("Findings", f"<h2>We report what the records support</h2>{rows(C.FINDINGS)}")
    body += sec("Scope", f"<h2>What we don't do</h2><p class=\"intro\">{C.NOT_DO}</p>")
    body += sec("Next step", "<h2>Start with one workflow</h2><p class=\"intro\">Tell us which piece of work takes the most hours. We'll reply in writing by the next business day.</p><div class=\"acts\"><a class=\"btn\" href=\"/contact/\">Talk to us</a></div>", "dark")
    return page("/how-we-work/", "How it works | Beiz Data & Accounting", "How Beiz sets up an AI agent: tested on your past records, shadow mode first, a person signs off, every decision logged.", body)


def prices():
    body = phead("How fees work", C.PRICES_LEDE)
    body += sec("How a fee is set", f"<h2>Scope first, then a fixed fee in writing</h2>{rows(C.FEES_HOW)}")
    body += sec("Where to start", "<h2>The usual first engagements</h2>" + price_table(C.PRICES))
    body += sec("Terms", f"<h2>Terms that matter</h2>{rows(C.PRICE_TERMS)}")
    body += sec("Next step", "<h2>Want a fixed fee for your job?</h2><p class=\"intro\">Describe the work in a few lines. You'll get a written reply by the next business day and a proposal within three business days if it's a fit.</p><div class=\"acts\"><a class=\"btn\" href=\"/contact/\">Ask for a proposal</a></div>", "dark")
    return page("/prices/", "How fees work | Beiz Data & Accounting", "Every Beiz engagement is a fixed fee, set out in a written proposal with the timeline and what done looks like, before any work starts.", body)


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
    body += sec("Next step", "<h2>Want these checks on every bill?</h2><p class=\"intro\">They're a small slice of the two-week cash and data check, and of a bills agent that runs them before anything is paid and holds anything odd for a person.</p><div class=\"acts\"><a class=\"btn\" href=\"/contact/?topic=Two-week%20cash%20%26%20data%20check\">Ask about the check</a></div>", "dark")
    js = f'<script src="/assets/billcheck.js?v={ASSET_V}" defer></script>\n'
    app = '<script type="application/ld+json">' + __import__("json").dumps({
        "@context": "https://schema.org", "@type": "WebApplication", "name": "Beiz free bill check",
        "url": "https://beiz.com.au/bill-check/", "applicationCategory": "FinanceApplication", "operatingSystem": "Any modern browser",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "AUD"},
        "description": "Eight checks on a bills export (duplicates, repeated invoice numbers, changed supplier bank details, split bills and more). Runs in the browser; the file isn't uploaded.",
        "provider": {"@type": "ProfessionalService", "name": "Beiz Data & Accounting Pty Ltd", "url": "https://beiz.com.au/"}}) + "</script>"
    return page("/bill-check/", "Free bill check | Beiz Data & Accounting", "Check a bills export from Xero, MYOB or QuickBooks for duplicates, changed bank details and split bills. Runs in your browser; nothing is uploaded.", body, js + ld + app)


def privacy():
    body = phead("Privacy policy", "How we handle personal information. Last updated 5 November 2026.")
    body += f'<section class="sec"><div class="wrap"><div class="lab">Policy</div><div class="body prose">{C.PRIVACY}</div></div></section>'
    return page("/privacy/", "Privacy policy | Beiz Data & Accounting", "How Beiz Data & Accounting Pty Ltd handles personal information.", body)


def notfound():
    body = phead("Page not found", "That page has moved or no longer exists. The site was simplified in November 2026.")
    body += sec("Try", '<ul class="plain"><li><a href="/">Home</a></li><li><a href="/services/">Services</a></li><li><a href="/prices/">Fees</a></li><li><a href="/bill-check/">Free bill check</a></li><li><a href="/contact/">Contact</a></li></ul>')
    return page("/404.html", "Page not found | Beiz Data & Accounting", "Page not found.", body)


# ---------------------------------------------------------------- restored pages (5 Nov 2026)
DETAIL = {s["name"]: s["path"] for s in M.SERVICES}
DETAIL.update({"Live cash &amp; job profit model": "/services/cash-and-job-profit-model/",
               "Workshops for owners &amp; teams": "/workshops-speaking/#workshops",
               "Coaching for finance professionals": "/workshops-speaking/#coaching"})


def ul(items, cls="plain"):
    return f'<ul class="{cls}">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def chref(topic, msg=""):
    return "/contact/?topic=" + quote(topic) + (("&amp;msg=" + quote(msg)) if msg else "") + "#form"


def cta(h2, text, topic, label="Start in writing"):
    return sec("Next step", f'<h2>{h2}</h2><p class="intro">{text}</p><div class="acts"><a class="btn" href="{chref(topic)}">{label}</a><a class="btn line" href="{chref("Discovery call")}">Book a 20-minute call</a></div>', "dark")


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>\n"


def _plain(t):
    return html.unescape(re.sub(r"<[^>]+>", "", t))


def faq_ld(pairs):
    return ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": _plain(q), "acceptedAnswer": {"@type": "Answer", "text": _plain(a)}} for q, a in pairs]})


def related(links):
    links = [(h, t) for h, t in (links or []) if h.split("#")[0] in LIVE_PATHS]
    return ul([f'<a href="{h}">{t}</a>' for h, t in links]) if links else ""


def price_block(s):
    extra = f'<p class="note">{s["price_extra"]}</p>' if s.get("price_extra") else ""
    return ('<h2>A fixed fee, agreed in writing before work starts</h2>' + rows([("Timing", s["timing"])]) + extra +
            f'<p class="note">{C.PRICE_NOTE} <a href="/prices/">How fees work</a>.</p>')


def service_page(s):
    body = phead(s.get("h1", s["name"]), s["lede"], ("/services/", "Services"))
    if M.BRIEF.get(s["path"]):
        body += sec("In brief", '<ul class="brief">' + "".join(f"<li>{x}</li>" for x in M.BRIEF[s["path"]]) + "</ul>")
    extra_ld = ""
    if s.get("aml"):
        body += sec("In short", rows(M.AML_SPLIT) + f'<p class="note">Not legal advice: your AML/CTF program sets the actual rules. Obligations as described by <a href="{M.AUSTRAC_ENROL}" rel="noopener">AUSTRAC</a>.</p>')
        body += sec("Is your firm caught?", f'<h2>It depends on the services you provide, not on being an accountant</h2><p class="intro">The regulated services accounting firms most often provide are:</p>{ul(M.AML_CAUGHT)}<p class="note">A practice that only does tax returns, BAS and bookkeeping is probably outside scope. If you provide any of the services above, even occasionally, check them against <a href="{M.AUSTRAC_SUMMARY}" rel="noopener">AUSTRAC&#39;s guidance for tranche 2 entities</a> or with your adviser.</p>')
        body += sec("Key dates", rows(M.AML_DATES))
        body += sec("What firms must do", "<h2>Your obligations</h2>" + rows(M.AML_DUTIES))
        t = '<table class="led tw"><thead><tr><th>Step</th><th>The agent</th><th>Your people</th></tr></thead><tbody>' + "".join(
            f'<tr><td>{a}</td><td data-h="The agent">{b}</td><td data-h="Your people">{c}</td></tr>' for a, b, c in M.AML_TABLE) + "</tbody></table>"
        body += sec("Where an agent stops", f'<h2>The agent collects, checks and files. Your people decide.</h2>{t}')
        body += sec("Ways to start", "<h2>Three ways to start</h2>" + price_table(M.AML_COSTS) + f'<p class="note">{C.PRICE_NOTE}</p>')
        body += sec("What we don't do", f'<p class="intro">{M.AML_NOT}</p>')
        body += sec("Questions firms ask", rows(M.AML_FAQ))
        body += sec("Sources", f'<p class="note"><a href="{M.AUSTRAC_SUMMARY}" rel="noopener">AUSTRAC, summary of AML/CTF obligations for tranche 2 entities</a>; <a href="{M.AUSTRAC_ENROL}" rel="noopener">AUSTRAC, enrolment for new professions</a>; <a href="{M.AUSTRAC_SMR}" rel="noopener">AUSTRAC, suspicious matter reporting reference guide</a>. Checked 16 October 2026.</p>')
        extra_ld = faq_ld(M.AML_FAQ)
    elif s.get("ai_workforce"):
        body += sec("The agents", "<h2>Six roles agents can take on</h2>" + rows(M.AIW_AGENTS) + "<p class=\"note\">You don't need all six on day one. Most businesses start with the one or two that save the most hours, and add the rest once those are working.</p>")
        body += sec("Every agent", "<h2>Six controls every agent gets</h2>" + rows(M.AIW_CONTROLS), sid="agents")
        body += sec("How it runs", "<h2>A three-week rollout, then a day-30 review</h2>" + rows(M.AIW_WEEKS))
        body += sec("The part demos skip", f'<p class="intro">{M.AIW_SKIP}</p>')
        body += sec("Do you need one?", f'<h2>When you don&#39;t need an agent</h2><h3 class="sub">Use what you already have when</h3>{ul(M.AIW_NO_AGENT)}<h3 class="sub">An agent is worth setting up when</h3>{ul(M.AIW_AGENT)}<p class="note">{M.AIW_ISNT}</p>')
        body += sec("What you get", rows(M.AIW_GETS))
        body += sec("Fee", price_block(s))
        body += sec("Frameworks we work to", "<h2>Responsible AI isn't our invention. We make it practical.</h2>" + ul([f'<a href="{u}" rel="noopener">{t}</a>: {d}' for u, t, d in M.AIW_FRAMEWORKS]) + "<p class=\"note\">Links go to the publishers' own sites. We're not affiliated with or endorsed by any of them.</p>")
    elif s.get("rows"):
        body += sec("How it works", "<h2>Before, during and after</h2>" + rows(s["rows"]))
        body += sec("Their job stays theirs", '<p class="intro">The agent covers routine work only. Decisions, customers and anything about people stay with your team. Best booked three to four weeks before the leave starts.</p>')
        body += sec("Fee", price_block(s))
    else:
        if not M.BRIEF.get(s["path"]):
            body += sec("Who it's for", f'<p class="intro">{s["who"]}</p>')
        body += sec("The problem", f'<h2>{s["problem"]}</h2>')
        body += sec("What you get", f'<div class="pair"><div><h3>What you get</h3>{ul(s["gets"])}</div><div><h3>Limits</h3>{ul(s["limits"])}</div></div>')
        body += sec("How it runs", rows(M.STEPS))
        body += sec("Fee", price_block(s))
    if related(s.get("related")):
        body += sec("Read more", related(s["related"]))
    body += cta("Not sure it fits?", "Write a few lines about the problem. You'll get a written reply by the next business day. If it isn't a fit, we'll say so.", s["topic"], "Discuss this")
    return page(s["path"], s["title"], s["desc"], body, extra_ld)


def workshops_page():
    w = ""
    for x in M.WORKSHOPS:
        w += (f'<div class="block"><h2>{x["name"]}</h2>' + rows([("For", x["for"]), ("Format", x["format"])]) +
              f'<h3 class="sub">Participants will</h3>{ul(x["will"])}<h3 class="sub">Sample agenda</h3>{ul(x["agenda"])}'
              f'<h3 class="sub">Takeaways</h3>{ul(x["take"])}<p class="note">Priced after we understand your audience and format.</p>'
              f'<div class="acts"><a class="btn line" href="{chref("Workshop", "Workshop proposal: " + html.unescape(x["name"]) + ". Audience and format: ")}">Request a workshop proposal</a></div></div>')
    c, sp = M.COACHING, M.SPEAKING
    body = phead("Workshops, coaching and speaking", M.WORKSHOPS_LEDE, ("/services/", "Services"))
    body += sec("Workshops", w, sid="workshops")
    body += sec("Coaching", "<h2>Coaching for finance professionals</h2>" + rows([("For", c["for"]), ("Format", c["format"])]) + f'<h3 class="sub">You&#39;ll leave with</h3>{ul(c["leave"])}<p class="note">{c["limits"]}</p><div class="acts"><a class="btn line" href="{chref("Something else", "Coaching enquiry: what I want to build: ")}">Ask about coaching</a></div>', sid="coaching")
    body += sec("Speaking", "<h2>Speaking and panels</h2>" + rows([("For", sp["for"]), ("Formats", sp["formats"])]) + f'<h3 class="sub">Topics</h3>{ul(sp["topics"])}<div class="acts"><a class="btn line" href="{chref("Something else", "Speaking or panel enquiry. Event, audience, date and length: ")}">Invite Beiz to speak</a></div>', sid="speaking")
    body += cta("Planning a session?", "Tell us who it's for and what you'd like them to leave with. You'll get a written reply by the next business day.", "Workshop")
    return page("/workshops-speaking/", "Workshops, coaching and speaking | Beiz Data & Accounting", "Practical workshops and coaching on putting AI and data to work in finance and small business, using made-up data.", body)


def faq_page():
    body = phead("FAQ", "Straight answers to the things people ask first. If yours isn't here, ask it in writing.")
    body += sec("Questions", '<div class="rows">' + "".join(f'<div class="row"><h3>{q}</h3><p>{a}</p></div>' for q, a in M.FAQ) + "</div>")
    body += cta("Still have a question?", "Ask it in writing. You'll get a straight answer by the next business day.", "Something else", "Ask in writing")
    return page("/faq/", "FAQ | Beiz Data & Accounting", "Straight answers about Beiz: what we do and don't do, AI and your data, prices, who does the work and how we work with your tax accountant.", body, faq_ld(M.FAQ))


KEEP_ARTS = ['/insights/privacy-act-automated-decisions/', '/insights/check-bills-before-you-pay/']
ARTS = sorted([a for a in M.ARTICLES if a["path"] in KEEP_ARTS], key=lambda a: a["date"], reverse=True)


def insights_page():
    items = "".join(f'<div class="row"><h3><a href="{a["path"]}">{html.escape(a["title"])}</a></h3><p>{a["desc"]}<br><span class="fine">{a["shown"]} · {a["mins"]} minute read</span></p></div>' for a in ARTS)
    body = phead("Insights", M.INSIGHTS_LEDE)
    body += sec("Articles", f'<div class="rows">{items}</div>')
    return page("/insights/", "Insights | Beiz Data & Accounting", "Plain-English notes on cash, controls, data and AI for Australian businesses, by Purav Mehta CA, GAICD.", body)


def article_page(a):
    by = f'By <a href="/about/">Purav Mehta</a>, Chartered Accountant · {a["shown"]} · {a["mins"]} minute read'
    src = f'<p class="note">{a["sources"]}</p>' if a["sources"] else ""
    body = phead(html.escape(a["title"]), a["desc"], ("/insights/", "Insights"), by)
    body += f'<section class="sec"><div class="wrap"><div class="lab">Article</div><div class="body prose">{a["body"]}{src}</div></div></section>\n'
    body += cta("Want this set up in your business?", "Write a few lines about your setup. You'll get a written reply by the next business day. If we're not the right fit, we'll say so.", a["topic"])
    art = ld({"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
              "datePublished": a["date"], "author": {"@type": "Person", "name": "Purav Mehta", "url": SITE + "/about/"},
              "publisher": {"@type": "Organization", "name": "Beiz Data & Accounting Pty Ltd", "url": SITE + "/"},
              "mainEntityOfPage": SITE + a["path"]})
    return page(a["path"], a["title"] + " | Beiz", a["desc"], body, art)


MORE = {s["path"]: (lambda s=s: service_page(s)) for s in M.SERVICES}
MORE.update({"/workshops-speaking/": workshops_page, "/faq/": faq_page, "/insights/": insights_page})
MORE.update({a["path"]: (lambda a=a: article_page(a)) for a in ARTS})



def redirect(to):
    return f'<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><title>Moved</title><meta name="robots" content="noindex"><link rel="canonical" href="{SITE}{to}"><meta http-equiv="refresh" content="0; url={to}"></head><body><p>This page has moved to <a href="{to}">{SITE}{to}</a>.</p></body></html>\n'


PAGES = {"/": home, "/services/": services, "/how-we-work/": how, "/prices/": prices, "/about/": about,
         "/contact/": contact, "/bill-check/": bill_check, "/privacy/": privacy}
PAGES.update(MORE)
LIVE_PATHS = set(PAGES)


def write(path, text):
    f = os.path.join(ROOT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w", encoding="utf-8").write(text)


def webmcp_js():
    """Browser-agent tools (WebMCP). Facts come straight from content.py so they can't drift from the pages."""
    import json, re
    strip = lambda t: re.sub(r"<[^>]+>", "", t).replace("&amp;", "&").replace("&middot;", "\u00b7")
    services = {
        "name": "Beiz Data & Accounting Pty Ltd", "abn": "53 691 755 496", "acn": "691 755 496",
        "gst": "Not registered, so no GST is added.", "location": "Canberra, ACT. Works Australia-wide.",
        "principal": "Purav Mehta: Chartered Accountant (member of Chartered Accountants Australia and New Zealand) with a Certificate of Public Practice, GAICD",
        "positioning": "AI for real work, with guardrails, set up and checked by an Australian Chartered Accountant.",
        "fees": "Every engagement is a fixed fee in a written proposal. The bill check is free.", "offers": [{"offer": strip(n), "what": strip(d)} for n, d, p, _ in C.PRICES],
        "every_build_includes": [strip(x) for x in C.INCLUDES],
        "does_not_do": strip(C.NOT_DO),
        "contact": {"email": "hello@beiz.com.au", "page": "https://beiz.com.au/contact/",
                    "reply": "Written reply by the next business day; proposal within three business days."},
        "source": "https://beiz.com.au/",
    }
    bill = {"url": "https://beiz.com.au/bill-check/", "checks": [strip(x) for x in C.BC_CHECKS],
            "file_handling": "Runs in the visitor's browser. The file isn't uploaded, stored or sent.",
            "limits": strip(C.BC_LIMITS)}
    adm = {
        "commences": "10 December 2026",
        "rule": "New APP 1.7 to 1.9 (Privacy and Other Legislation Amendment Act 2024): an APP entity's privacy policy must describe its use of computer programs in decisions.",
        "applies_when_all": [
            "the organisation is an APP entity covered by the Privacy Act",
            "a computer program makes a decision, or does something substantially and directly related to making one",
            "the decision could reasonably be expected to significantly affect an individual's rights or interests",
            "personal information is used in the program's operation for that decision"],
        "what_it_requires": "Transparency in the privacy policy. It is a disclosure obligation.",
        "source": "https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines/chapter-1-app-1-open-and-transparent-management-of-personal-information",
        "note": "General information only, not legal advice. Confirm with your own adviser."}
    return """/* Beiz WebMCP tools. Generated by src/ledger/build.py; edit content.py, not this file.
   Progressive enhancement: does nothing unless the browser exposes document.modelContext (or navigator.modelContext). */
(() => {
  const mc = document.modelContext || navigator.modelContext;
  if (!mc || typeof mc.registerTool !== "function") return;
  const SERVICES = %s, BILL = %s, ADM = %s;
  const out = o => ({ content: [{ type: "text", text: JSON.stringify(o, null, 2) }] });
  const reg = t => { try { const r = mc.registerTool(t); if (r && r.catch) r.catch(() => {}); } catch (_) {} };
  reg({ name: "get_beiz_services", description: "Facts about Beiz Data & Accounting: who it is, how fees work, what every build includes, what it does not do, and how to make contact. Read-only.",
        inputSchema: { type: "object", properties: {} }, annotations: { readOnlyHint: true }, execute: async () => out(SERVICES) });
  reg({ name: "get_bill_check_rules", description: "The eight checks the free browser-based bill check runs, how the file is handled, and its limits. Read-only.",
        inputSchema: { type: "object", properties: {} }, annotations: { readOnlyHint: true }, execute: async () => out(BILL) });
  reg({ name: "privacy_adm_overview",
        description: "General information on Australia's Privacy Act automated-decision transparency rules (APP 1.7 to 1.9, from 10 December 2026). Optionally pass what the user knows; returns which conditions are met, unknown or not met. Not legal advice.",
        inputSchema: { type: "object", properties: {
          app_entity: { type: "string", enum: ["yes", "no", "unsure"], description: "Is the organisation covered by the Privacy Act?" },
          computer_program_decides: { type: "string", enum: ["yes", "no", "unsure"], description: "Does a computer program make, or substantially help make, the decision?" },
          significant_effect: { type: "string", enum: ["yes", "no", "unsure"], description: "Could the decision reasonably be expected to significantly affect an individual's rights or interests?" },
          uses_personal_information: { type: "string", enum: ["yes", "no", "unsure"], description: "Is personal information used in making it?" } } },
        annotations: { readOnlyHint: true },
        execute: async (a = {}) => {
          const k = ["app_entity", "computer_program_decides", "significant_effect", "uses_personal_information"];
          const v = k.map(x => a[x] || "unsure");
          const summary = v.includes("no") ? "At least one condition is not met, so the new disclosure rule is unlikely to apply to this decision."
            : v.includes("unsure") ? "Some conditions are unknown. The rule may apply; confirm the unknowns."
            : "All four conditions are met, so the privacy policy will likely need the new disclosures from 10 December 2026.";
          return out({ ...ADM, answers: Object.fromEntries(k.map((x, i) => [x, v[i]])), summary });
        } });
})();
""" % (json.dumps(services), json.dumps(bill), json.dumps(adm))


def llms_full():
    import re
    t = lambda x: re.sub(r"<[^>]+>", "", x).replace("&amp;", "&").replace("&middot;", "·")
    L = [C.LLMS.strip(), "", "---", "", "# Full detail", "", "## What Beiz does", t(C.HERO_LEDE), "", t(C.HERO_CRED), ""]
    L += ["## Is Beiz a fit?"] + [f"- {a}: {t(b)}" for a, b in C.FIT] + [""]
    L += ["## Where it helps"] + [f"- {a}: today, {t(b)[:1].lower() + t(b)[1:]} With a Beiz agent: {t(c)}" for a, b, c in C.JOBS] + [""]
    L += ["## Services"]
    for g in C.GROUPS:
        L += [f"### {t(g['title'])}", t(g["intro"])] + [f"- {t(n)} ({t(p)}): {t(d)}" for n, d, p, _ in g["items"]] + [""]
    L += ["## Fees", C.PRICES_LEDE, "No GST is added (not registered).", ""] + [f"- {t(n)}: {t(d)}" for n, d, p, _ in C.PRICES] + [""]
    L += ["## Terms"] + [f"- {a}: {t(b)}" for a, b in C.PRICE_TERMS] + [""]
    L += ["## How a build runs"] + [f"- {a}: {t(b)}" for a, b in C.FIRST30] + [""]
    L += ["## Rules first, AI for the exceptions"] + [f"- {a}: {t(b)}" for a, b in C.RULES_FIRST] + [""]
    L += ["## Every build includes"] + [f"- {t(x)}" for x in C.INCLUDES] + [""]
    L += ["## How a bill gets in"] + [f"- {a}: {t(b)}" for a, b in C.INTAKE] + [""]
    L += ["## Control status"] + [f"- {a}: {t(b)}" for a, b in C.CONTROL_STATES] + [""]
    L += ["## Stop conditions (work stops and waits for a person)"] + [f"- {t(x)}" for x in C.STOPS] + [""]
    L += ["## Each service in brief"] + sum(([f"### {t(sv['name'])} ({SITE}{sv['path']})"] + [f"- {t(x)}" for x in M.BRIEF.get(sv["path"], [])] for sv in M.SERVICES), []) + [""]
    L += ["## Decision log fields"] + [f"- {a}: {t(b)}" for a, b in C.LOG_FIELDS] + [""]
    L += ["## Free bill check", t(C.BC_LEDE)] + [f"- {t(x)}" for x in C.BC_CHECKS] + [""] + [f"Q: {q}\nA: {t(a)}" for q, a in C.BC_FAQ] + ["", t(C.BC_LIMITS), ""]
    L += ["## What Beiz does not do", t(C.NOT_DO), "", "## Company details"] + [f"- {a}: {t(b)}" for a, b in C.FACTS]
    L += ["", "Liability limited by a scheme approved under Professional Standards Legislation.",
          "Trade mark of Chartered Accountants Australia and New Zealand and used with permission.", ""]
    return "\n".join(L)


def main():
    for p, fn in PAGES.items():
        write(p, fn())
    write("/404.html", notfound())
    for old, new in C.REDIRECTS.items():
        write(old, redirect(new))
    urls = "".join(f"<url><loc>{SITE}{p}</loc></url>" for p in PAGES)
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    open(os.path.join(ROOT, "llms.txt"), "w").write(C.LLMS.rstrip() + "\n\n## Is Beiz a fit?\n" + "".join(f"- {a}: {b}\n" for a, b in C.FIT))
    open(os.path.join(ROOT, "llms-full.txt"), "w").write(llms_full())
    open(os.path.join(ROOT, "assets", "ledger", "webmcp.js"), "w").write(webmcp_js())
    print("built", len(PAGES), "pages,", len(C.REDIRECTS), "redirects")


if __name__ == "__main__":
    main()
