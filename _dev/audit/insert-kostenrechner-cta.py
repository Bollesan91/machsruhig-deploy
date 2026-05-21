"""
Insert Kostenrechner-CTA in alle Stadt-Pages.
Pattern: kleiner CTA-Hint am Ende der Bestattungskosten-Sektion.
"""
import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"

CTA_HTML = """    <div class="mr-hint" style="border-left-color:var(--mr-primary);background:var(--mr-bg-card)">
      <strong>Was kostet die Bestattung konkret?</strong> Berechne deinen Kostenrahmen mit anonymer Eingabe in zwei Minuten: <a href="/tools/bestattungskosten-rechner"><strong>→ Bestattungskosten-Rechner</strong></a>. Vergleicht Erd-, Feuer- und Seebestattung mit aktuellen Friedhofsgebühren und Bestatterleistungen.
    </div>
"""

# Match the heading of Bestattungskosten section
KOSTEN_H2_RE = re.compile(r'<h2[^>]*>[^<]*[Kk]osten in [^<]+</h2>')
# Fallback: just "Bestattungskosten" / "Kosten einer Bestattung" / "Friedhofsgebühren"
KOSTEN_H2_FALLBACK_RE = re.compile(r'<h2[^>]*>[^<]*(?:Bestattungskosten|Kosten einer Bestattung|Friedhofsgebühren in)[^<]*</h2>', re.IGNORECASE)
# Marker for the start of next mr-section (div or section)
NEXT_SECTION_RE = re.compile(r'<(?:div|section) class="mr-section[" ]')

processed = []
skipped_no_section = []
skipped_already = []

for city_dir in sorted(BESTATTER.iterdir()):
    if not city_dir.is_dir():
        continue
    idx = city_dir / "index.html"
    if not idx.exists():
        continue

    text = idx.read_text(encoding="utf-8", errors="replace")
    slug = city_dir.name

    # Skip if already has the CTA link
    if '/tools/bestattungskosten-rechner' in text and 'Was kostet die Bestattung konkret' in text:
        skipped_already.append(slug)
        continue

    # Find Kosten heading
    m = KOSTEN_H2_RE.search(text)
    if not m:
        m = KOSTEN_H2_FALLBACK_RE.search(text)
    if not m:
        skipped_no_section.append(slug)
        continue

    # Find next mr-section after this heading
    next_match = NEXT_SECTION_RE.search(text, m.end())
    if not next_match:
        skipped_no_section.append(slug)
        continue

    # Find the </div> immediately before the next section
    insertion_zone_start = m.end()
    insertion_zone_end = next_match.start()
    section_block = text[insertion_zone_start:insertion_zone_end]
    # The closing </div> or </section> of the kosten section is the last one before the next mr-section opening
    closing_div_offset = max(section_block.rfind("</div>"), section_block.rfind("</section>"))
    if closing_div_offset == -1:
        skipped_no_section.append(slug)
        continue

    absolute_insert_pos = insertion_zone_start + closing_div_offset
    # Insert CTA right before this </div>
    new_text = text[:absolute_insert_pos] + CTA_HTML + text[absolute_insert_pos:]

    idx.write_text(new_text, encoding="utf-8")
    processed.append(slug)

print(f"Processed: {len(processed)} cities")
for s in processed[:5]:
    print(f"  {s}")
if len(processed) > 5:
    print(f"  ... +{len(processed)-5} more")
print(f"\nSkipped (no Kosten section / no boundary): {len(skipped_no_section)}")
for s in skipped_no_section:
    print(f"  {s}")
print(f"\nSkipped (already has CTA): {len(skipped_already)}")
for s in skipped_already:
    print(f"  {s}")
