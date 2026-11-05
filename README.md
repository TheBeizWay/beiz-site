# beiz.com.au

Static site for Beiz Data & Accounting, hosted on GitHub Pages.

- Build: `python3 src/ledger/build.py` (writes the pages into the repo root, plus sitemap.xml and llms.txt). Python 3 only.
- Content: `src/ledger/content.py`. Layout: `src/ledger/build.py`. Styles and script: `assets/ledger/`.
- Fonts are self-hosted in `assets/fonts/`.
- Archived pages live in `_archive/` and aren't published. `src/legacy/` holds the old generator; don't run it.
- Working rules: `CLAUDE.md`.
