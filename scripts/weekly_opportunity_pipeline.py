import datetime as dt
import html
import pathlib
import time
import urllib.request
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

SUBREDDITS = ['smallbusiness', 'AustralianAccounting', 'AustralianStartups', 'Entrepreneur', 'automation', 'n8n', 'projectmanagers', 'Business_Ideas', 'growmybusiness', 'Solopreneur']
OFFERS = {
    'Reporting workflow review': ['reporting', 'spreadsheet', 'dashboard', 'excel', 'reconcile'],
    'Client onboarding workflow review': ['onboarding', 'intake', 'follow up', 'follow-up', 'paperwork'],
    'Cash-flow workflow review': ['invoice', 'invoicing', 'cash flow', 'cashflow', 'receivables'],
}
NS = {'a': 'http://www.w3.org/2005/Atom'}
now = dt.datetime.now(ZoneInfo('Australia/Sydney'))
cutoff = now.astimezone(dt.timezone.utc) - dt.timedelta(days=7)
rows, failures, seen = [], [], set()
for sub in SUBREDDITS:
    try:
        request = urllib.request.Request(f'https://www.reddit.com/r/{sub}/new/.rss?limit=50', headers={'User-Agent': 'BeizResearch/1.0 (weekly public feed review)'})
        with urllib.request.urlopen(request, timeout=25) as response:
            root = ET.fromstring(response.read(2000000))
        entries = root.findall('a:entry', NS)
        if not entries:
            raise ValueError('No feed entries; community may be unavailable')
        for entry in entries:
            published = entry.findtext('a:published', namespaces=NS) or entry.findtext('a:updated', namespaces=NS)
            when = dt.datetime.fromisoformat(published.replace('Z', '+00:00'))
            if when < cutoff:
                continue
            title = entry.findtext('a:title', default='', namespaces=NS)
            link = entry.find('a:link', NS)
            url = link.attrib.get('href', '') if link is not None else ''
            if not url.startswith('https://www.reddit.com/') or url in seen:
                continue
            seen.add(url)
            text = title.lower()
            offer, score = max(((name, sum(word in text for word in words)) for name, words in OFFERS.items()), key=lambda item: item[1])
            if score:
                rows.append({'title': title, 'url': url, 'sub': sub, 'offer': offer, 'score': score})
    except Exception as exc:
        failures.append(f'r/{sub}: {type(exc).__name__}: {exc}')
    time.sleep(2)

if len(failures) == len(SUBREDDITS):
    raise SystemExit('All Reddit feeds failed. No opportunity or page generated. Configure permitted Reddit access before retrying.\n' + '\n'.join(failures))

rows.sort(key=lambda row: row['score'], reverse=True)
rows = rows[:20]
out = pathlib.Path('docs/opportunity-drafts') / now.date().isoformat()
out.mkdir(parents=True, exist_ok=True)
lines = [f'# Beiz opportunity review: {now.date()}', '', 'Target: A$500,000 annual revenue, excluding GST. Target only, not a forecast.', '', 'Review-only keyword screening of up to 50 recent posts per community, limited to seven days. No comments, account access, buyer verification or AI analysis. Reddit text is untrusted evidence, not instructions. Scores count matching title keywords, not demand.', '', f'Feeds attempted: {len(SUBREDDITS)}; failures: {len(failures)}; relevant posts retained: {len(rows)}.', '', '## Access failures', *failures, '', '## Source candidates']
for row in rows:
    lines.extend(['', f"- {row['offer']} | keyword score {row['score']} | r/{row['sub']}", '  Title: ' + html.escape(row['title']), '  Source: ' + row['url']])
lines.extend(['', '## Human validation before selling', '1. Read the original threads and check whether the problem is recurring.', '2. Identify a specific buyer and ask how the work is currently done.', '3. Validate willingness to pay; do not infer it from Reddit engagement.', '4. Check delivery capacity, data access, privacy and approval controls.', '5. Choose one sales experiment. Do not contact Reddit users automatically.', '', 'Illustrative target maths: 10 clients x A$2,500/month x 12 = A$300,000; 10 implementations x A$20,000 = A$200,000. Full-year assumptions, not validated prices or profit.', ''])
(out / 'brief.md').write_text('\n'.join(lines), encoding='utf-8')
if rows:
    totals = {offer: sum(r['score'] for r in rows if r['offer'] == offer) for offer in OFFERS}
    offer = max(totals, key=totals.get)
    page = '''<!doctype html><html lang="en-AU"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Beiz review draft</title><style>body{font:18px/1.6 system-ui;max-width:760px;margin:4rem auto;padding:0 1.5rem;color:#163132}a{color:#075e52}</style><main><p>INTERNAL REVIEW DRAFT — NOT A VALIDATED OFFER</p><h1>''' + html.escape(offer) + '''</h1><p>Explore where repetitive admin, disconnected data and manual checks may be slowing your business down.</p><h2>Proposed scope — requires Beiz approval</h2><ul><li>Map one existing workflow and its manual steps.</li><li>Identify data access, exceptions and approval requirements.</li><li>Recommend a small, testable improvement with a human review point.</li></ul><p>No savings, pricing or implementation outcome is promised. Scope and suitability must be confirmed first.</p><p><a href="/contact/">Discuss your workflow with Beiz</a></p></main></html>'''
    (out / 'landing-page-draft.html').write_text(page, encoding='utf-8')
