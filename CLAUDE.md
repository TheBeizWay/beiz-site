# beiz.com.au: working rules

Read this before changing anything in this repo. It describes the site as it is, the facts it may state, and how to change it without breaking it. If a request conflicts with this file, say so before building.

## Update, 5 Nov 2026: the "Ledger" revamp (Purav chose the direction, scope and branch build)

The site was rebuilt from scratch and cut to six pages plus the free bill check. **This section overrides anything older below.**

- **Build:** `python3 src/ledger/build.py` from the repo root. Content is in `src/ledger/content.py`, layout in `src/ledger/build.py`. Styles `assets/ledger/ledger.css`, script `assets/ledger/ledger.js`. Bump `ASSET_V` in `build.py` on every CSS or JS change.
- **Published pages:** `/`, `/services/`, `/how-we-work/`, `/prices/`, `/about/`, `/contact/`, `/bill-check/`, `/privacy/`, plus `/card/` (static, unchanged) and `404.html`. Restored 5 Nov 2026 with Purav's yes ("keep the good parts"): one page per service (`SERVICES` in `src/ledger/content_more.py`), `/aml-ctf-accounting-firms/`, `/workshops-speaking/`, `/faq/`, `/insights/` with two articles (`KEEP_ARTS` in `build.py`: the Privacy Act automated-decisions guide and the supplier bill checks). Industries pages and the other four articles stay archived: the trades copy promised sending without a person. Don't add pages without Purav's yes, and check restored copy against sections 1 to 3 before publishing it.
- **Archived:** every other page moved to `_archive/` (not published). Old URLs get a redirect stub written by the build (`REDIRECTS` in `content.py`). The old generator is in `src/legacy/` and must not be run: it would overwrite the new pages.
- **Removed features:** the ticker, chatbot, live data page, theme switcher, neon/warm/classic themes, demos, calculators and insights. Don't bring any back without Purav's explicit yes.
- **Design ("Ledger"):** warm ledger paper `#F5F2EA`, near-black ink, hairline rules, double rule under page heads, Source Serif 4 headlines, IBM Plex Sans body, tabular numbers. Each section is a ledger entry: a label column and a content column. No cards, pills, shadows, gradients, glow, monospace labels or all-caps labels. Colour carries meaning only: ok `#2B7652`, held `#A86A12`, stop `#B23A2E`. Colour pass (Purav, 5 Nov 2026, "colour looks dead"): brand colours come from the Beiz logo only: deep green `#1F6B4A` for buttons, links and section labels; logo green `#43B581` for primary buttons on dark; amber `#E8B04A` for the hero rule and the bills panel header; forest `#13221B` for the hero and closing sections. Never use CA ANZ blue or red as site colours. On the dark hero the CA logo is the reversed file.
- **Hero line (new with the revamp):** "AI that does the checking. A Chartered Accountant who checks the AI." Don't change it without Purav.
- **CA ANZ logo:** official files are in `assets/media/` (`ca-logo.svg` for light backgrounds, `ca-logo-reversed.png` for dark). Rules from CA ANZ's Members in Practice guidelines: never recolour, crop, stretch, rotate, outline, add effects or transparency; the horizontal logo's artwork must be at least 110px wide (the files include built-in clear space, so render the file at least 140px wide / 80px tall); show "Trade mark of Chartered Accountants Australia and New Zealand and used with permission." near the logo. Use depends on Beiz meeting CR 9: on 5 Nov 2026 the CA ANZ Service Centre confirmed Purav's membership and Certificate of Public Practice, supplied the logo suite and asked to review screenshots of the placements (sent by Purav). Change placements only after that review, and follow any feedback from CA ANZ. Header co-branding (Purav, 5 Nov 2026): on desktop (over 1100px) the primary vertical CA logo (`ca-logo-vertical.svg`, rendered 108px tall so its artwork is just over 65px wide, the minimum) sits beside the Beiz logo, which is rendered 78px tall to match the CA artwork's height, with a divider and 2X space; the trade mark statement runs in a thin strip directly under the header; the header is not sticky at that size. On smaller screens the CA logo shows beside the credentials line under the hero instead.
- **Naming (CA ANZ guidelines):** write "Chartered Accountants Australia and New Zealand" in full at the first visible mention on a page; "Chartered Accountants ANZ" or "CA ANZ" after that. Designations (CA, GAICD) in the same font, size and colour as the name.
- **Liability line is mandatory** on every page (CA ANZ requires it for Australian members): "Liability limited by a scheme approved under Professional Standards Legislation."
- **PI insurance is in force** (Purav confirmed 5 Nov 2026). The site says "Professional indemnity insurance held with Chubb." (insurer named with Purav's approval, 5 Nov 2026). Never state the cover amount, and don't claim cyber cover unless Purav confirms it.
- **Interactive layer (Purav, 5 Nov 2026):** the hero bills panel opens a five-field decision log per row (examples from the made-up business in `data/sample-bills.csv`; demo buttons only show a note, nothing is sent). Homepage "Under the hood" has a Plain / Technical view switch (stored in `localStorage.beizView`). Ctrl/Cmd+K opens a jump-to palette of live pages (list in `ledger.js`; only live pages and anchors). `assets/ledger/webmcp.js` is generated by the build from `content.py` and registers three read-only WebMCP tools only where the browser supports `document.modelContext` / `navigator.modelContext`; the privacy tool is general information with the OAIC source, never a determination or advice. The code block in the technical view is the only monospace on the site. `llms-full.txt` is generated by the build. Browse layer (Purav, 5 Nov 2026, "services should show when we browse, futuristic"): desktop Services menu opens a services panel on hover or keyboard focus (built from `GROUPS`); homepage "What we do" lists every service and price; sections and rows fade in as you scroll, a green progress line runs along the top, and the bills panel posts its rows in one by one with the counts ticking up. All motion is off for anyone with reduced motion set, and the CA logo never animates.
- AI workforce setup stays a scoped quote. Positioning: small businesses, startups and solo operators first; company-first, founder credentials as support.

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
| Live cash & job profit model | scoped quote (no public price, Purav 5 Nov 2026) |
| AI workforce setup (/services/ai-readiness-sprint/) | scoped quote (no public price, Purav 19 Oct 2026) |
| Leave cover | scoped quote (no public price, Purav 5 Nov 2026) |
| Monthly controls operations | scoped quote (no public price, Purav 5 Nov 2026) |

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
- **Badges or certifications Beiz doesn't hold.** No "compliant", "certified", "audited" or "immutable". The CA ANZ logo is the only third-party mark, used under the rules above.
- **State the PI cover amount or claim cyber cover.** Say only "Professional indemnity insurance held with Chubb." Keep the Professional Standards line on every page.
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

See the 5 Nov 2026 update at the top for build, pages and design. Also:

- Always `git pull --rebase` before pushing. `data/markets.json` is still committed by a workflow every 30 minutes (no published page uses it now).
- GitHub Pages deploys `main`. Pages are cached for about 10 minutes; check the live site with `curl "https://beiz.com.au/?nc=$RANDOM"`.
- Test locally with `python3 -m http.server 8765` and Playwright, on desktop (1440 wide) and phone (390 wide). No page errors, no horizontal scroll, every internal link resolves.
- The contact form posts to the Google Apps Script in `src/apps-script/Code.gs`; the endpoint URL is in `assets/ledger/ledger.js`.
- The bill check is `assets/billcheck.js`, unchanged; its output classes are styled in `ledger.css`. The bill check FAQ carries `FAQPage` JSON-LD and must stay visible on the page.
- `llms.txt` and `sitemap.xml` are written by the build from `content.py`. IndexNow still runs after each push to `main`; the key file in the repo root must stay.

### Logo (locked 18 Oct 2026, Purav's final call)

The charcoal rounded square with green, amber and grey ledger marks, plus the spaced BEIZ wordmark and "Data & Accounting". No new concepts, no rebrand, no animation. The header uses `assets/ledger/beiz-lockup.png` (the light-background lockup trimmed of padding). Source files: `assets/brand/`.

---

## 5. Before you say a change is done

1. List the links, anchors and scripts on the page you changed, and confirm none broke.
2. Check every fact against section 1: ABN, prices, credentials and scope.
3. Check the page on desktop (1440) and phone (390).
4. Run the link check and confirm there are no page errors.
5. Deploy, confirm the new `ASSET_V` is live, and tell Purav in one or two lines what changed.

The GitHub repo is public, so write nothing here you would not want read. `_config.yml` keeps this file, `notes/`, `src/` and `scripts/` off beiz.com.au itself.
