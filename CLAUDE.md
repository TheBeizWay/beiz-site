# beiz.com.au: working rules

Read this before changing anything in this repo. It describes the site as it is, the facts it may state, and how to change it without breaking it. If a request conflicts with this file, say so before building.

## Ownership (Purav, 14 Nov 2026)

Only the Claude session Purav works with on Beiz pushes to `main`. Other tools may review or suggest, never push. On 13–14 Nov other tools pushed 12 commits (a dark "financial intelligence" homepage with prices, "board assurance" and "signed off" claims, a B-symbol logo, and a deploy step that rewrote pages at publish time); all of it was reverted to the 13 Nov version. Deploys now copy the committed files as they are (`.github/workflows/deploy-beiz.yml`); never add build-time rewriting.

## Homepage "A" (Purav, 14 Nov 2026: "I like A")

- The homepage is the hand-built dark page in `src/home/index.html`; `build.py` copies it over the generated `index.html` at the end of every build. Edit that file for homepage changes. Inner pages still come from the ledger build.
- Fixes applied to A before going live: real Beiz logo (`assets/brand/beiz-logo-dark-trimmed.png`), CA ANZ logo at 140px wide, self-hosted fonts (no Google Fonts), the enquiry form posts to the Apps Script (it used to open the visitor's email app), and no "signed off by a Chartered Accountant", "board assurance", "many of our clients" or n8n wording.
- Fees (Purav, 14 Nov 2026: "only put prices if competitors do the same"): prices show only where comparable Australian firms publish theirs: the reporting & controls diagnostic ($2,500, changed from $4,500 on 14 Nov), cross-system reporting & close rescue ($4,500–$8,000), fractional CFO + reporting (from $3,500 a month) and AI workflow builds (from $8,500). Quality of earnings was removed (due-diligence work, no evidence of demand). Checked 14 Nov: Roar Data publishes a $1,950 incl. GST diagnostic and builds from $3,250; Standard Ledger publishes fractional CFO from $5,500 + GST a month. Everything else says "Quoted in writing". This supersedes the 5 Nov no-prices rule for the homepage only.
- Every page now shares one dark single-row header (`header.top.dk`): new wordmark, reversed CA ANZ logo at 140px (hidden on phones; the footer carries it), nav Services · Why Beiz · How it works · Pricing · Bill check, and "Book a strategy call". Inner pages use Space Grotesk headings and Inter body. The WebMCP script is no longer loaded. Not added on purpose: instant-download kits (no files exist) and a hire-vs-Beiz calculator (compares a sprint with a salary, which misleads).
- Argon ideas applied 14 Nov 2026: the lede is "the data layer between your operations and your ledger"; Why Beiz says software reconciles inside its own walls; How it works is "A commit isn't proof. Reconciled numbers are." with three checks; the form asks which two systems or reports don't reconcile; the footer excludes payroll tax and super compliance interpretation. Buyers are Australian businesses generally, not only accounting firms.
- Kits (Purav, 14 Nov 2026): two real Excel kits are on sale (13-week cash forecast $290, supplier bank-change control kit $190; files kept outside this public repo and emailed after an invoice is paid). Two more are shown as "Concept · In design" with "Register interest" and no price; never take payment for a concept.
- Finance continuity line (14 Nov 2026): interactive Normal / Microsoft 365 down / Recovery simulation (labelled made-up) plus four quoted offers: continuity check, continuity kit, recovery reconciliation, continuity exercise. Beiz doesn't repair Microsoft, ledgers or IT; suspected cyber incidents go to the client's IT/security provider.
- Purav dropped the no-tool-names rule (14 Nov 2026). The hero lists "Every deliverable reviewed by a Chartered Accountant before handover". Inner pages are dark to match the homepage.
- Workbench (14 Nov 2026, from the Google/Reddit/YouTube/competitor layout review): the hero is one column (short lede, "Explore the workbench", "Discuss your workflow", four role tabs: business owner, finance manager, accounting firm, operations lead). A full-width BEIZ WORKBENCH sits under it with four modules (Reporting, Reconciliation, Controls, Continuity), a four-step flow, scenario/sources, a clickable result table and an evidence panel (what differs, records, rule, next step) with JSON under "Technical details". Role tabs switch the lede and the module. Labelled made-up and not connected to any real system. The mid-page trust strip is gone; the CA trade mark line sits directly under the header. Kit cards say what's inside and why the price; fix-or-refund if a file doesn't work as described.
- Month-end workflow sprint, multi-page, new logo, hero refinement (Purav, 14 Nov 2026):
  - Lead offer: fit conversation (free), workflow diagnostic ($1,500–$2,500), implementation sprint ($4,000–$8,000), maintenance quoted. Supersedes the $2,500 diagnostic and the close rescue. Other services sit in an "Also available" list. Signature builds and QoE are off the page.
  - The two regulatory concept kits are deferred: only the two real kits show.
  - New pages cut from the homepage at build time from the committed source (not a deploy rewrite): /workbench/, /kits/, /continuity/ (`HOME_PAGES` in build.py). Nav everywhere: Services · Workbench · Kits · Continuity · How it works.
  - Logo: new mark `assets/brand/beiz-mark.svg` (two sources joining into a checked decision) with the BEIZ wordmark; `beiz-mark-512.png` for schema. Purav ordered the change.
  - Hero: two-line headline, lede "We connect your job system and ledger, check the differences and give your team a clear list to review.", no particle network, no countdown pill; credentials sit in one line above the workbench. At 1440x900 the workbench tabs are visible without scrolling.
  - Workbench: "Interactive example · Sample data"; five modules (Client info added); filters All / Needs a person / Stopped / Matched with an empty state; recon shows ambiguous match, invalid input and a long name; evidence includes corrected output; JSON under Technical details.
- Exception review naming (14 Nov 2026, from the Reddit/YouTube synthesis): the offer is the "System-to-ledger exception review" ($1,500–$2,500) then the "System-to-ledger exception sprint" ($4,000–$8,000); payables is one example module, not the identity. Bill check is out of the main nav (the page stays). No grid or dots behind the hero or inner pages. Catalogue frozen: no new services until three buyer conversations produce one approved paid-scope hypothesis. Inner pages (/services/, /prices/, /contact/, /cash-data-check/) match the homepage offer; "Who reviews" replaces "Who signs off".
- Research applied 14 Nov 2026: positioning is "builds and tests finance workflows across the systems you already use", every build has written acceptance tests, AI workflows start by checking what Xero or MYOB already does, and the catalogue offers supplier payment controls and automation acceptance testing (the "Queryable Company" concept was removed: no evidence of demand).

## Update, 13 Nov 2026: "Studio" refresh of the homepage (Purav: "fix this site, looks like a kids project")

- Removed site-wide: the scrolling "What's changing" ticker under the header, the floating "Ask Beiz" helper, the "Jump to (Ctrl K)" link, the scroll progress line, fade-ins and the ticking counters. The site is still; nothing moves on scroll.
- The NEWS items now show once, as a static "What's changing for Australian businesses" grid near the end of the homepage, each linked to its official source.
- Homepage order: hero (photo of Purav, links to About and LinkedIn) → four jobs with example log entries → amber band → three ways to start → bill check with an example-results card → four safety steps → what's changing → closing call to action. The "who you'll deal with" block is off the homepage (it duplicated the hero photo); /about/ carries it. "Everything Beiz does" tiles and "Under the hood" are off the homepage; /services/ and /how-we-work/ cover them.
- "Book a 20-minute call" goes to /contact/?topic=Discovery%20call until Purav supplies a calendar booking link.
- Hero is now light and photo-led (`hero2`): headline, lede, two buttons, three plain facts, and Purav's photo with a caption. The bills panel left the hero.
- Each homepage job column carries one example decision-log entry (`JOB_LOGS` in `content.py`, made-up business, labelled).
- /how-we-work/ has the "Under the hood" plain/technical view of one decision record (no WebMCP list).
- The Services nav item is a plain link; the 13-item hover panel is gone.
- The bill check shows a "20-minute walk-through" offer (`#bcNext`) once results appear. No prices, no "signed report" wording.
- 30-day site freeze from 13 Nov 2026 unless Purav asks: selling comes first.

## Update, 5 Nov 2026: the "Ledger" revamp (Purav chose the direction, scope and branch build)

The site was rebuilt from scratch and cut to six pages plus the free bill check. **This section overrides anything older below.**

- **Build:** `python3 src/ledger/build.py` from the repo root. Content is in `src/ledger/content.py`, layout in `src/ledger/build.py`. Styles `assets/ledger/ledger.css`, script `assets/ledger/ledger.js`. Bump `ASSET_V` in `build.py` on every CSS or JS change.
- **Published pages:** `/`, `/services/`, `/how-we-work/`, `/prices/`, `/about/`, `/contact/`, `/bill-check/`, `/privacy/`, plus `/card/` (static, unchanged) and `404.html`. Restored 5 Nov 2026 with Purav's yes ("keep the good parts"): one page per service (`SERVICES` in `src/ledger/content_more.py`), `/aml-ctf-accounting-firms/`, `/workshops-speaking/`, `/faq/`, `/insights/` with two articles (`KEEP_ARTS` in `build.py`: the Privacy Act automated-decisions guide and the supplier bill checks). Industries pages and the other four articles stay archived: the trades copy promised sending without a person. Don't add pages without Purav's yes, and check restored copy against sections 1 to 3 before publishing it.
- **Archived:** every other page moved to `_archive/` (not published). Old URLs get a redirect stub written by the build (`REDIRECTS` in `content.py`). The old generator is in `src/legacy/` and must not be run: it would overwrite the new pages.
- **Removed features:** the live data page, theme switcher, neon/warm/classic themes and calculators. Don't bring any back without Purav's explicit yes.
- **Brought back 5 Nov 2026 (Purav: "GO LIVE GO AHEAD"):** (1) "What's changing" strip under the header: `NEWS` in `content.py`, each item a dated official source (OAIC, AUSTRAC, ATO, Scamwatch, NAIC, ABR) plus the Beiz page it relates to; countdowns are computed in the browser; static and scrollable with reduced motion. Only add items with a primary government source link. (2) "Ask Beiz" guided helper: scripted answers from `HELPER_EXTRA` plus the FAQ, keyword matching in `ledger.js`. It isn't AI, stores and sends nothing, and falls back to /contact/ with the question prefilled. (3) "See it working" homepage clips `assets/media/demo-log.mp4` and `demo-bc.mp4`, recorded from this site with the made-up business; muted, play only while on screen, controls instead with reduced motion. Re-record them with Playwright if the hero panel or bill check changes.
- **Design ("Ledger"):** warm ledger paper `#F5F2EA`, near-black ink, hairline rules, double rule under page heads, Source Serif 4 headlines, IBM Plex Sans body, tabular numbers. Each section is a ledger entry: a label column and a content column. No cards, pills, shadows, gradients, glow, monospace labels or all-caps labels. Colour carries meaning only: ok `#2B7652`, held `#A86A12`, stop `#B23A2E`. Colour pass (Purav, 5 Nov 2026, "colour looks dead"): brand colours come from the Beiz logo only: deep green `#1F6B4A` for buttons, links and section labels; logo green `#43B581` for primary buttons on dark; amber `#E8B04A` for the hero rule and the bills panel header; forest `#13221B` for the hero and closing sections. Never use CA ANZ blue or red as site colours. On the dark hero the CA logo is the reversed file.
- **Redesign pass (Purav, 5 Nov 2026, "looks same old"):** the homepage no longer repeats the label-column ledger entry for every section. It uses full-width sections (`wsec()` in `build.py`) that alternate paper, white (`--white`) and forest backgrounds: four job columns, an amber statement band ("Nothing is paid or sent without a person."), service tiles with a green top rule (bordered, no shadows), the bill check and clips on forest, three numbered ways to start, and the four safety steps with large amber numerals on forest. The hero headline is larger and the hero carries faint horizontal ledger lines. Inner pages keep the ledger-entry layout. Still no shadows, glow, pills or all-caps labels.
- **Reddit and AI search notes applied (Purav, 5 Nov 2026):** every service page opens with an "In brief" block (`BRIEF` in `content_more.py`, three bullets phrased the way a buyer asks); /services/ opens with "Is Beiz a fit?" (`FIT`: who it's for, hard limits, who signs off, what we won't do), also written into `llms.txt`; /how-we-work/ has "How a bill gets in" (`INTAKE`), "Control status" (`CONTROL_STATES`) and "Stop conditions" (`STOPS`); all of it feeds `llms-full.txt`. Purav's calls (5 Nov 2026): no low-price entry offer or "pay nothing" guarantee; LinkedIn yes (company page in the organisation `sameAs` and footer, his profile in the founder `sameAs` and the founder block); ABN status check waits for his ABR GUID. Don't name receipt apps or competitors.
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

### Fees (Purav, 5 Nov 2026: "no professional firm does prices")

The site publishes no fee amounts. Every engagement is a fixed fee, set out in a written proposal (fee, timeline, definition of done) within three business days, before any work starts. `/prices/` is the "How fees work" page (nav label "Fees"). The free bill check stays free. Don't put dollar amounts for Beiz's own work back on any page, meta tag, `llms.txt`, WebMCP output or helper answer without Purav's yes. Internal reference only (not for the site): two-week cash & data check was $1,500, compliance sprint from $3,500.

### Promises already on the site (keep them consistent everywhere)

- Written reply by the next business day. Proposal within three business days, with a fixed price, timeline and definition of done.
- Calls are 20 minutes, early morning or after 5pm.
- Agents: written job description, limits, a named person they report to, tested on the client's past records against a pass mark agreed in writing, shadow mode before live, decision log in the client's own accounts, monthly spending cap and off switch, day-30 review.
- The client keeps an operating folder: business context, procedures and agent memory, as plain files.
- Nothing is paid or sent without a person.
- Credit (agreed 18 Oct 2026): the fee for the two-week check is credited once against the next Beiz build (cash model, AI workforce setup, compliance sprint or leave cover setup) if the client accepts the proposal and pays the deposit within 60 days of the findings. Not redeemable for cash; not for monthly support.
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

### Logo (refreshed 14 Nov 2026, Purav: "make your final call")

The icon stays. The wordmark is now live text: "BEIZ" in Space Grotesk 700 with "Data & Accounting" in the body font underneath (`.bword`). Light pages use `assets/brand/beiz-icon.svg`; the dark homepage uses `assets/brand/beiz-icon-dark.svg` (lighter square so it shows on black). The old PNG lockups stay in `assets/` for LinkedIn and documents until those are updated.

### Logo (locked 18 Oct 2026, superseded by the refresh above)

The charcoal rounded square with green, amber and grey ledger marks, plus the spaced BEIZ wordmark and "Data & Accounting". No new concepts, no rebrand, no animation. The header uses `assets/ledger/beiz-lockup.png` (the light-background lockup trimmed of padding). Source files: `assets/brand/`.

---

## 5. Before you say a change is done

1. List the links, anchors and scripts on the page you changed, and confirm none broke.
2. Check every fact against section 1: ABN, prices, credentials and scope.
3. Check the page on desktop (1440) and phone (390).
4. Run the link check and confirm there are no page errors.
5. Deploy, confirm the new `ASSET_V` is live, and tell Purav in one or two lines what changed.

The GitHub repo is public, so write nothing here you would not want read. `_config.yml` keeps this file, `notes/`, `src/` and `scripts/` off beiz.com.au itself.
