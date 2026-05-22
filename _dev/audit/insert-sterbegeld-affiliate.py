"""
Insert Sterbegeld-Affiliate-Hint (Check24) in 52 City-Pages.
Position: Am Ende der Sozialbestattung-Sektion (logisch: Vorsorge-Pendant zur Notfall-Hilfe).
Falls keine Sozial-Sektion: vor FAQ-Sektion.

Block: subtil, mit rel="sponsored", klare Affiliate-Disclosure.
"""
import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"

AFFILIATE_BLOCK = """    <div class="mr-hint" style="border-left-color:var(--mr-accent);background:var(--mr-bg-card)">
      <strong>Vorsorge-Tipp gegen Sozialbestattung:</strong> Eine Sterbegeldversicherung deckt die Bestattungskosten ab, damit Angehörige nicht in die § 74-Lage geraten. Vergleichsrechner für Tarife und Versicherungssummen: <a href="https://www.check24.de/sterbegeldversicherung/" rel="sponsored noopener" target="_blank">→ Sterbegeldversicherung vergleichen (Check24)</a>. Hinweis: machsruhig verlinkt diesen Vergleich als Affiliate, der dabei verdiente Anteil finanziert die Redaktion — ohne Mehrkosten für Dich.
    </div>
"""

# Find Sozialbestattung section + insert at end (before closing </div> or </section>)
SOZIAL_H2_RE = re.compile(r'<h2[^>]*>[^<]*Sozialbestattung', re.IGNORECASE)
# Next section opener after the Sozial-h2 — match mr-section OR mr-faq OR mr-sources OR </main>
NEXT_SECTION_RE = re.compile(r'<(?:div|section)[^>]*class="(?:mr-section|mr-faq|mr-sources|mr-trust)|</main>', re.IGNORECASE)


def patch_city(slug):
    p = BESTATTER / slug / "index.html"
    if not p.exists():
        return "missing"
    text = p.read_text(encoding="utf-8", errors="replace")

    # Skip if already has the affiliate block
    if "check24.de/sterbegeldversicherung" in text and "Vorsorge-Tipp gegen Sozialbestattung" in text:
        return "already"

    # Find Sozial-h2
    m = SOZIAL_H2_RE.search(text)
    if not m:
        return "no-sozial-section"

    # Find next mr-section opener after this h2
    after = text[m.end():]
    next_match = NEXT_SECTION_RE.search(after)
    if not next_match:
        return "no-next-section-boundary"

    # The closing </div> or </section> is the last one before next opening
    insertion_zone_end = m.end() + next_match.start()
    section_block = text[m.end():insertion_zone_end]
    closing_offset = max(section_block.rfind("</div>"), section_block.rfind("</section>"))
    if closing_offset == -1:
        return "no-closing"

    absolute_insert_pos = m.end() + closing_offset
    new_text = text[:absolute_insert_pos] + AFFILIATE_BLOCK + text[absolute_insert_pos:]
    p.write_text(new_text, encoding="utf-8")
    return "patched"


processed = []
skipped = []
for c in sorted(BESTATTER.iterdir()):
    if not c.is_dir():
        continue
    if c.name in {"lübeck", "mönchengladbach"}:  # umlaut duplicates
        continue
    status = patch_city(c.name)
    if status == "patched":
        processed.append(c.name)
    else:
        skipped.append((c.name, status))

print(f"Processed: {len(processed)}")
for s in processed[:10]:
    print(f"  {s}")
if len(processed) > 10:
    print(f"  ... +{len(processed)-10} more")
print(f"\nSkipped: {len(skipped)}")
for s, reason in skipped:
    print(f"  {s}: {reason}")
