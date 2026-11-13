from pathlib import Path
import json,re,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '_publish')
if not (root/'index.html').is_file(): raise SystemExit('Published site folder missing')
icon='<svg class="beiz-symbol" viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false"><rect width="80" height="80" rx="17" fill="#123c32"/><path fill="#fafbf8" fill-rule="evenodd" d="M22 15h23c16 0 24 15 13 25 15 10 9 25-10 25H22zm14 12v9h10c8 0 8-9 0-9zm0 21v6h12c7 0 7-6 0-6z"/><path d="M17 50 54 13h9L17 59z" fill="#123c32"/></svg>'
brand='<a class="ed-brand" href="/" aria-label="Beiz Data and Accounting home">'+icon+'<span class="beiz-wordmark"><strong>BEIZ</strong><small>DATA &amp; ACCOUNTING</small></span></a>'
changed=0
for p in root.rglob('*.html'):
 text=p.read_text(encoding='utf-8')
 updated=re.sub(r'<a\b[^>]*class="ed-brand"[^>]*>[\s\S]*?</a>',lambda _:brand,text)
 if updated!=text: p.write_text(updated,encoding='utf-8');changed+=1
css=root/'assets/editorial.css'
if not css.exists(): raise SystemExit('Shared stylesheet missing')
css.write_text(css.read_text(encoding='utf-8')+'''
/* Beiz logo and readable header. Official CA artwork is unchanged. */
body{font-size:18px}.ed-bar{min-height:116px;gap:24px}.ed-id{gap:24px}.ed-brand{display:inline-flex;align-items:center;gap:14px;text-decoration:none;letter-spacing:normal;flex-shrink:0}.ed-brand .beiz-symbol{display:block;width:58px;height:58px;flex-shrink:0}.ed-brand .beiz-wordmark strong{display:block;font:800 38px/1 system-ui,sans-serif;letter-spacing:3px}.ed-brand .beiz-wordmark small{display:block;font:500 13px/1.4 system-ui,sans-serif;letter-spacing:1px;margin-top:9px}.ed-nav{font-size:17px;gap:26px;font-weight:550}.ed-ca{width:76px;height:auto;padding-left:20px}.ed-tm{font-size:12px;line-height:1.5;padding-bottom:12px}.ed-legal{font-size:13px;line-height:1.7}.ed-links{font-size:15px}.ed-foot .ed-brand .beiz-symbol{width:50px;height:50px}.ed-foot .ed-brand .beiz-wordmark strong{font-size:32px}.ed-mobile{font-size:17px}.ed-mobile a{font-size:16px}@media(max-width:850px){.ed-bar{min-height:106px;gap:12px}.ed-id{gap:13px}.ed-brand{gap:10px}.ed-brand .beiz-symbol{width:42px;height:42px}.ed-brand .beiz-wordmark strong{font-size:30px;letter-spacing:2px}.ed-brand .beiz-wordmark small{font-size:11px;letter-spacing:.5px;margin-top:7px}.ed-ca{width:50px;padding-left:12px}.ed-tm{font-size:11px}.ed-legal{font-size:12px}}
''',encoding='utf-8')
release_path=root/'release.json'
release=json.loads(release_path.read_text());release['branding']='green-b-readable-v1';release['branding_pages_updated']=changed
release_path.write_text(json.dumps(release),encoding='utf-8')
if 'beiz-symbol' not in (root/'index.html').read_text(): raise SystemExit('Homepage logo replacement failed')
print('Installed green B logo on',changed,'pages')
