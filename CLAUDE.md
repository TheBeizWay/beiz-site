# beiz.com.au: working rules

Read this before changing anything in this repo. It describes the site as it is, the facts it may state, and how to change it without breaking it. If a request conflicts with this file, say so before building.

---

## 0. The anchor: every page traces back to these three sentences

1. **Who:** an Australian Chartered Accountant (Certificate of Public Practice) and GAICD, who has worked in audit, controls and finance. Not a development shop or a prompt agency.
2. **What:** Beiz sets up and runs an AI workforce for compliance and finance. Agents do the routine checking and preparation: bills, cash, reconciliations, client checks.
3. **Why it's safe:** nothing runs on its own on day one. Each agent is tested on the client's past records, runs alongside staff in shadow mode first, and needs a person's sign-off for anything that matters, with every decision logged.

The homepage runs in this order: what it is (hero), proof it works (control room and bill check), what it costs (three offers), why it won't break anything (how agents are set up), and who you'll talk to. Explain how it's built (models, workflow tools, schemas) only when a buyer asks. Never call any of this "audit".

---

## 1. Facts the site may state

Use only these. Never substitute, round or "improve" them.

| Fact | Value |
|---|---|
| Legal entity | Beiz Data & Accounting Pty Ltd |
| ABN / ACN | 53 691 755 496 / 691 755 496 |
| GST | Not registered. Prices are AUD with no GST added |
| Location | Canberra, ACT. Works Australia-wide |
| Principal | Purav Mehta: Chartered Accountant (CA ANZ) with a Certificate of Public Practice, GAICD |
| Positioning | AI for real work, with guardrails, set up and checked by an Australian Chartered Accountant (widened 17 Oct 2026) |
| Buyers | Any Australian business that wants to use AI for real work but needs guardrails; accounting and bookkeeping firms and finance teams remain the core |
| Email | hello@beiz.com.au |

### Prices (change only when Purav says so)

| Offer | Price |
|---|---|
| Free bill check (/bill-check/) | Free, runs in the browser |
| Two-week cash & data check | $1,500 fixed, credited if they go ahead |
| Compliance controls sprint (/compliance-sprint/) | from $3,500, two weeks, one focus |
| Live cash & job profit model | from $5,000 |
| AI workforce setup (/services/ai-readiness-sprint/) | from $8,500, three-week rollout |
| Leave cover (/leave-cover/) | from $3,500 setup, then from $2,000 a month |
| Monthly controls operations | from $1,250 a month |

### Promises already on the site (keep them consistent everywhere)

- Written reply by the next business day. Proposal within three business days, with a fixed price, timeline and definition of done.
- Calls are 20 minutes, early morning or after 5pm.
- Agents: written job description, limits, a named person they report to, tested on the client's past records against a pass mark agreed in writing, shadow mode before live, decision log in the client's own accounts, monthly spending cap and off switch, day-30 review.
- The client keeps an operating folder: business context, procedures and agent memory, as plain files.
- Nothing is paid or sent without a person.
- Credit (agreed 18 Oct 2026): the $1,500 check is credited once against the next Beiz build (cash model, AI workforce setup, compliance sprint or leave cover setup) if the client accepts the proposal and pays the deposit within 60 days of the findings. Not redeemable for cash; not for monthly support.
- Cash model: the client drops in fresh exports weekly and the model refreshes; Beiz builds it, ties actuals to the ledger, documents assumptions and hands over. A Beiz review of the forecast only where its frequency and scope are set out in the support agreement.
- Monthly controls operations: up to two agreed agents or one model; monthly control review, log sample, test-set re-run, up to two hours of fixes in total; more is quoted. Requests acknowledged within two business days. Not round-the-clock monitoring or an emergency service.
- Findings: "We report what the records support"; findings may need an explanation before action; weak records are reported as a limitation.
- Demo figures are illustrative and exclude GST.

---

## 2. Never

- **Invent anything:** clients, results, testimonials, case studies, uptime figures, user counts, time savings or "studies show". Demo data is labelled as made-up where it appears.
- **Unsourced statistics.** A number from outside Beiz needs a primary source linked on the page (AUSTRAC, OAIC, ABS, NAIC, legislation). AI-generated "research" doesn't count until the original has been read.
- **Badges or certifications Beiz doesn't hold.** No "compliant", "certified", "audited" or "immutable". No CA ANZ logo until the official artwork file is supplied (the slot in `src/layout.py` renders it when `CA_LOGO` is set).
- **Claim PI insurance** until Purav confirms the policy is in force. Keep the Professional Standards line in the footer.
- **Scope Beiz doesn't do:** tax returns, BAS or GST lodgements, tax or BAS agent services, statutory audit or assurance, legal advice, financial product advice, payments released without a person.
- **Call an AI agent a Chartered Accountant,** or imply an agent signs anything off.
- **Mention DFAT, government employers or public-sector work.** Beiz is private sector only.
- **Name or quote anyone from Reddit, LinkedIn or calls.** `notes/` is for copy ideas only.
- **Scrape sites or get around blocks** (Reddit API, YouTube bot checks, paywalls).
- **Write regulatory checkers or pages as advice.** They're general information, not legal advice, and say so.

---

## 3. How words are written

Australian English (organisation, analyse, program). Plain words, short sentences, active voice.

1. **Concrete over jargon.** Say "check", "hold", "sign off", "log" and "connect". Never "synergy", "transformative", "hyper-automation", "unlock", "seamless", "skyrocket" or "10x".
2. **Control first, then benefit.** Say what stops a mistake before saying what saves time: "Tested on your past records and held for a person, so bills clear faster without losing control."
3. **Pictures, not percentages.** "6 bills matched, 1 held for a person" beats "40% faster". Use numbers only when they're real or clearly labelled as a demo.
4. **Show the unglamorous part.** Input checks, holding what it isn't sure about, logging, failing safely, people reviewing exceptions. That's what Beiz sells.
5. **Let the buyer choose.** "Talk or write." "If we're not the right fit, we'll say so." No countdown pressure, fake scarcity or "only 2 spots left".
6. **Say what the first 30 days look like** in steps, with the three-business-day proposal.

Avoid the tells of generated copy: a word or phrase singled out in a headline, all-caps labels, "→" on every link, "not X, but Y" constructions, rhetorical questions as hooks, and lists of three adjectives.

---

## 4. The site as it is

### Build and deploy

- Content: `src/pages.py`. Layout, header, footer and head script: `src/layout.py`. Build: `python3 src/build.py`, which writes the HTML into the repo root along with `sitemap.xml`, `robots.txt` and `llms.txt`.
- **Bump `ASSET_V` in `src/layout.py` on every CSS or JS change.**
- Always `git pull --rebase` before pushing. `data/markets.json` is committed by a workflow every 30 minutes.
- GitHub Pages deploys `main`. Pages are cached for about 10 minutes; check the live site with `curl "https://beiz.com.au/?nc=$RANDOM"`.
- Test locally with `python3 -m http.server 8765` and Playwright, on desktop (1440 wide) and phone (390 wide). There must be no page errors and no horizontal scroll, and every internal link must resolve.

### Themes

- **Default: warm** (since 17 Oct 2026, Purav's choice, claude.com feel): `warm.css` on top of `ledger.css`, warm near-black, ivory type, no ruled lines. The header button switches between warm and light. Bottle-green **Ledger** is at `?theme=ledger`. **Neon** is reached at `?theme=neon`: dark navy with cyan `#2EF2E2`, glow on primary buttons, cursor glow, scroll progress bar, sections that fade in, and the agent-network canvas in the hero on desktop only. Files: `refine.css`, `future-neon.css`, `calm.css` (structural fixes) and `neon-on.css`. Effects come from `future-fx.js`.
- **Light:** the header button switches to `paper.css` (with `ledger.css`). The control room and demo panels stay dark inside it.
- **Classic:** `?theme=classic`.
- The theme is chosen in the head script in `src/layout.py`, and the choice is stored in `localStorage.beizTheme`.
- Status colours mean something and are never decoration: ok (green), held (amber), stop (red). Respect `prefers-reduced-motion`.

### Homepage, in five sections (keep it at five)

Purav's plan is the brief: hero "Use AI in your business, with guardrails. Set up, tested and checked by an Australian Chartered Accountant." (changed 17 Oct 2026 with Purav's yes), a "What we don't do" box under the offers, a "What every Beiz build includes" table in #how (replaced the AI-on-its-own comparison 18 Oct 2026, Purav's yes), and a header menu (What we do, How it works, Free bill check, Prices, About; order changed 18 Oct 2026 with Purav's yes). The phone menu shows the same five items as desktop, plus the fit-check and start-in-writing buttons. On desktop "What we do" opens a problem-led dropdown panel (four problems, today vs with Beiz, links); on phones it goes to /services/, which shows the same panel. The one-bill walk-through lives at /how-we-work/#bill-review. Control room rows open the reason and records behind them (18 Oct 2026, Purav: "you decide"), the control room and bill check as proof, three priced offers ($1,500 check, from $3,500 sprint, from $8,500 AI workforce), the four-step setup, then Purav and the form. Keep the ticker (Purav likes it), chatbot, hero map and control room. The footer links to the digital card at /card/; the "Ask an AI about Beiz" links were dropped 18 Oct 2026. Reviews from other AI tools are suggestions only: never remove or replace an existing section, the tagline or a feature without Purav's explicit yes.


1. **Hero:** the control room (ordinary-day and bad-day switch, labelled as a made-up business) beside the headline, Purav's credentials line, "Book a 20-minute fit check" and "Try the free bill check". (Swapped with the bill map on 18 Oct 2026, Purav's yes.)
2. **#workforce:** "Follow one bill through the checks": the bill map, wrapped in `.bm-host` (its styles mirror the old `.hz-hero.dark .bm-*` rules).
3. **#offers:** three priced offers (sprint, check, AI workforce) and a line linking the rest.
4. **#how:** declare, contain, test, watch.
5. **#ca:** who you'll talk to, and the contact form.

Detail lives on its own page: `/compliance-sprint/`, `/aml-ctf-accounting-firms/`, `/bill-check/`, `/prices/`, `/leave-cover/`, `/try/`, `/how-we-work/` and `/about/`. Don't move anchors without updating every link to them: `src/layout.py` (menus, footer, JSON-LD), `assets/site.js` (chatbot, bill journey) and `llms.txt`.

### Search and AI answers

- Visible FAQs on the AML/CTF, bill check and compliance sprint pages carry `FAQPage` JSON-LD (`faq_ld()` in `src/pages.py`). Any new FAQ must be visible on the page as well as in the markup.
- The `ProfessionalService` JSON-LD is in `src/layout.py`. `llms.txt` lists the main pages and must be updated when pages are added.
- Publish at most one to three articles a week, each answering a real question first and then showing a worked example from Beiz's own test data.

---

## 5. Before you say a change is done

1. List the links, anchors and scripts on the page you changed, and confirm none broke.
2. Check every fact against section 1: ABN, prices, credentials and scope.
3. Check the page in the neon and light themes, on desktop and phone.
4. Run the link check and confirm there are no page errors.
5. Deploy, confirm the new `ASSET_V` is live, and tell Purav in one or two lines what changed.

The GitHub repo is public, so write nothing here you would not want read. `_config.yml` keeps this file, `notes/`, `src/` and `scripts/` off beiz.com.au itself.
