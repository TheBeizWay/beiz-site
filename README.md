# beiz.com.au

Static site for Beiz Data & Accounting, hosted on GitHub Pages.

- Edit content in `src/pages.py`, layout in `src/layout.py`, charts in `src/charts.py`.
- Build: `python3 src/build.py` (writes HTML into the repo root, plus sitemap.xml and robots.txt).
- Styles: `assets/site.css` · Script: `assets/site.js` · Fonts self-hosted in `assets/fonts/`.
- Market data: `.github/workflows/markets.yml` refreshes `data/markets.json` every 30 minutes.
