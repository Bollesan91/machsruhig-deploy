"""
Insert <div class="mr-article-meta"> on city pages without it.
Inserted right after the closing </p> of the lead paragraph.
"""
import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"

META_BLOCK = '\n    <div class="mr-article-meta"><div><strong>Redaktion machsruhig.de</strong><span class="mr-meta-sep" aria-hidden="true"> · </span><span>Stand: 21. Mai 2026</span></div><div><a href="/methodik">Wie entstehen unsere Inhalte?</a><span class="mr-meta-sep" aria-hidden="true"> · </span><span>Lesezeit: ca. 10 Minuten</span></div></div>'

# Match the lead <p>... </p>
# Note: <p class="lead"> or <p class="mr-lead">
LEAD_P_RE = re.compile(r'<p[^>]*class="(?:mr-)?(?:hero-)?lead"[^>]*>.*?</p>', re.DOTALL)

processed = []
skipped_already = []
skipped_no_lead = []

for city_dir in sorted(BESTATTER.iterdir()):
    if not city_dir.is_dir():
        continue
    idx = city_dir / "index.html"
    if not idx.exists():
        continue

    text = idx.read_text(encoding="utf-8", errors="replace")
    slug = city_dir.name

    if 'class="mr-article-meta"' in text:
        skipped_already.append(slug)
        continue

    m = LEAD_P_RE.search(text)
    if not m:
        skipped_no_lead.append(slug)
        continue

    new_text = text[:m.end()] + META_BLOCK + text[m.end():]
    idx.write_text(new_text, encoding="utf-8")
    processed.append(slug)

print(f"Processed: {len(processed)}")
for s in processed:
    print(f"  {s}")
print(f"\nSkipped (already): {len(skipped_already)}")
print(f"Skipped (no lead-p): {len(skipped_no_lead)}")
for s in skipped_no_lead:
    print(f"  {s}")
