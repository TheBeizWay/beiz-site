"""Trust page for beiz.com.au: the commitments, limits and low-risk ways to start.
Every claim here is already stated elsewhere on the site (llms.txt, footer, pricing). Add nothing that is not true."""
from layout import page, phero, cta_band, related, CALL_HREF, CALL_ATTR


def trust_pages():
    hero = phero(
        "Why trust Beiz",
        "What we commit to, what we won't do, and how to start small.",
        "Hiring someone to touch your finance data or AI is a trust decision. Here is the plain version: the promises we make, the work we refuse, and three ways to start where you risk very little.",
        [("/trust/", "Why trust Beiz")],
        [("/contact/?topic=Discovery%20call#form", "Book a free 20-minute call"), ("/examples/", "See sample work first")],
    )

    promises = '''<section><div class="wrap">
  <p class="eyebrow">Four commitments</p>
  <h2>Promises you can hold us to</h2>
  <div class="cards two">
    <div class="card"><span class="k">01 · Price</span><h3>Fixed scope, fixed price, in writing</h3><p>You get a one-page proposal with the exact price and timeline within three business days. Nothing starts until you agree to it. Beiz is not registered for GST, so no GST is added.</p></div>
    <div class="card"><span class="k">02 · People</span><h3>A person approves what matters</h3><p>Anything that touches money, customers or decisions about people is approved by a human. Agents prepare and flag; they do not post, pay or decide.</p></div>
    <div class="card"><span class="k">03 · Independence</span><h3>No software of our own to sell</h3><p>Work is built inside your own accounts, such as Xero, MYOB, Microsoft 365 or Google Workspace. If you leave, you keep what was built.</p></div>
    <div class="card"><span class="k">04 · Data</span><h3>AI plans that exclude training on your data</h3><p>We use AI plans whose terms exclude training on client data. Please do not send passwords or bank details; exports are enough for most checks.</p></div>
  </div>
</div></section>'''

    limits = '''<section class="band"><div class="wrap">
  <p class="eyebrow">Clear limits</p>
  <h2>What Beiz does not do</h2>
  <p class="lede">Being clear about the edges is part of being trustworthy. If you need one of these, we will say so and point you to the right professional.</p>
  <ul class="ticks" style="margin-top:20px">
    <li>No tax returns or BAS, and no tax agent or BAS agent services.</li>
    <li>No statutory audit or assurance.</li>
    <li>No legal advice. Where a client needs legal wording, such as Privacy Act disclosure text, we draft it for their lawyer to review.</li>
    <li>No financial product advice.</li>
    <li>No claim that AI guidance is law. Australian AI guidance is voluntary; the Privacy Act automated-decision rules apply only to organisations the Act covers.</li>
  </ul>
</div></section>'''

    proof = '''<section><div class="wrap">
  <p class="eyebrow">Check before you buy</p>
  <h2>See the work before you spend a dollar</h2>
  <p class="lede">Everything below uses made-up data in real formats, so you can judge the quality first.</p>
  <ol class="steps three">
    <li><h3>Try a demo</h3><p>Put in your own numbers: late payers, a 13-week cash forecast, an agent checking bills. Sixty seconds each.</p><a class="more" href="/try/">Open the demos &rarr;</a></li>
    <li><h3>Read a sample report</h3><p>The two-week check report and a findings register, where every item is Confirmed, Needs information or Explained.</p><a class="more" href="/assets/beiz-sample-check-report.pdf">Sample report (PDF) &rarr;</a></li>
    <li><h3>Run the Privacy Act check</h3><p>A short free check for the automated-decision rules starting 10 December 2026.</p><a class="more" href="/ai-check/">Start the check &rarr;</a></li>
  </ol>
</div></section>'''

    start = '''<section class="band"><div class="wrap">
  <p class="eyebrow">Low-risk starts</p>
  <h2>Three ways to begin without a big commitment</h2>
  <div class="cards">
    <div class="card"><span class="k">$1,500 fixed</span><h3>Two-week cash &amp; data check</h3><p>We work from exports, not logins, and look for unbilled work, margin leaks and manual bottlenecks. The fee is credited if you go ahead with more work.</p><a class="more" href="/#check">See the check &rarr;</a></div>
    <div class="card"><span class="k">from $3,500</span><h3>Compliance controls sprint</h3><p>Two weeks, one focus: AI use, AML/CTF Tranche 2 or the Privacy Act. No ledger access needed. You get a register, data map, named owners, rules and a 90-day plan.</p><a class="more" href="/#sprint">See the sprint &rarr;</a></div>
    <div class="card"><span class="k">Free</span><h3>5-minute workshop</h3><p>Map your week, set an agent's limits and leave with a written plan. No obligation.</p><a class="more" href="/workshop/">Try the workshop &rarr;</a></div>
  </div>
  <p class="fine">Prices are starting points; the written proposal sets the exact figure before any work begins.</p>
</div></section>'''

    who = '''<section><div class="wrap">
  <p class="eyebrow">Who is behind it</p>
  <h2>One accountable person, not a faceless platform</h2>
  <p class="lede">Beiz is led by <strong>Purav Mehta</strong>, an Australian Chartered Accountant and Graduate of the Australian Institute of Company Directors (GAICD), based in Canberra and working Australia-wide.</p>
  <p class="muted" style="margin-top:14px">Beiz Data &amp; Accounting Pty Ltd · ABN 53 691 755 496 · ACN 691 755 496 · Liability limited by a scheme approved under Professional Standards Legislation. <a href="https://www.linkedin.com/in/puravmehtaca/" rel="noopener">LinkedIn</a> · <a href="/about/">About us</a></p>
</div></section>'''

    faq = '''<section class="band"><div class="wrap">
  <p class="eyebrow">Questions people ask first</p>
  <h2>Straight answers</h2>
  <div class="faq">
    <details><summary>Will AI make decisions about my money?</summary><p>No. Agents prepare, check and flag. A named person approves anything that touches money, customers or decisions about people, and each decision is logged so it can be reviewed later.</p></details>
    <details><summary>What data do you need from me?</summary><p>For the cash &amp; data check, exports from your accounting and timesheet tools, not logins. For the compliance sprint, staff interviews and a list of the AI tools in use; no ledger access.</p></details>
    <details><summary>What if it is not a fit?</summary><p>We say so, in writing, and often point you to someone better placed. There is no chasing and no pressure.</p></details>
    <details><summary>Is this legal or tax advice?</summary><p>No. Beiz does not provide tax agent, BAS agent, audit, legal or financial product advice. Where legal wording is needed, it is drafted for your lawyer to review.</p></details>
    <details><summary>What do I own at the end?</summary><p>The register, models, policies and workflows are built in your own accounts and documented, so they stay with you.</p></details>
  </div>
</div></section>'''

    rel = '<section><div class="wrap"><p class="eyebrow">Keep exploring</p>' + related([("/how-we-work/", "How we work"), ("/faq/", "FAQ"), ("/examples/", "Examples"), ("/about/", "About us"), ("/contact/", "Contact")]) + "</div></section>"

    body = hero + promises + limits + proof + start + who + faq + rel + cta_band("Want to talk it through?", "Book a free 20-minute call, or send a few lines in writing. You get a considered reply, not a sales pitch.")
    return {"/trust/": page("/trust/", "Why trust Beiz: commitments and limits", "What Beiz commits to, what it will not do, and three low-risk ways to start: fixed prices, human approval, your own accounts, made-up sample work.", body)}
