# beiz.com.au

Static site for Beiz Data & Accounting, hosted on GitHub Pages.

- Edit content in `src/pages.py`, layout in `src/layout.py`, charts in `src/charts.py`.
- Build: `python3 src/build.py` (writes HTML into the repo root, plus sitemap.xml and robots.txt).
- Build needs **Python 3** and **Node.js** (tested with Node 22 and Python 3.13). The homepage panel figures are calculated at build time by running `assets/signature-model.js` with Node, so they always match `/products-demos/job-profitability/`.
- Styles: `assets/site.css` · Script: `assets/site.js` · Fonts self-hosted in `assets/fonts/`.
- Market data: `.github/workflows/markets.yml` refreshes `data/markets.json` every 30 minutes.
