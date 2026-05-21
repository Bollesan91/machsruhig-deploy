"""
Fix broken /bestattung-Link in Breadcrumbs.

Vorher: href="/bestattung"  (404)
Nachher: href="/bestattung-in/"  (existiert jetzt als Hub-Page)

Betroffen: alle bestatter/*/index.html und bestattung-in/*/index.html, auch JSON-LD-BreadcrumbList.
"""
import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent

# HTML attribute form
PAT_HTML = re.compile(r'href="/bestattung"')
# JSON-LD form (in BreadcrumbList "item": "https://machsruhig.de/bestattung")
PAT_JSONLD = re.compile(r'"https://machsruhig\.de/bestattung"')

REPLACE_HTML = 'href="/bestattung-in/"'
REPLACE_JSONLD = '"https://machsruhig.de/bestattung-in/"'

dirs_to_scan = [ROOT / "bestatter", ROOT / "bestattung-in"]
changed = 0
for d in dirs_to_scan:
    for idx in d.glob("*/index.html"):
        text = idx.read_text(encoding="utf-8", errors="replace")
        new = PAT_HTML.sub(REPLACE_HTML, text)
        new = PAT_JSONLD.sub(REPLACE_JSONLD, new)
        if new != text:
            n_html = len(PAT_HTML.findall(text))
            n_json = len(PAT_JSONLD.findall(text))
            idx.write_text(new, encoding="utf-8")
            print(f"  {idx.relative_to(ROOT)}: replaced {n_html} html + {n_json} jsonld")
            changed += 1

print(f"\nTotal files changed: {changed}")
