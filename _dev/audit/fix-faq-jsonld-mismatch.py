"""
Reviewer-Sweep-Fix: FAQPage-JSON-LD entfernen wo FAQ nur JS-gerendert ist
(verstößt sonst gegen Googles Rich-Result-Richtlinie für sichtbaren Inhalt).

Betroffene Tools: bestattungskosten-rechner, kostenrechner, notfallkarte,
                  checkliste-todesfall, vorsorge-check
(fristen-radar: FAQ ist initial sichtbar — bleibt mit kleinem Wortlaut-Fix;
 beerdigungsplaner: hat keine FAQPage)
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
TOOLS = ROOT / "tools"

TARGETS = [
    "bestattungskosten-rechner",
    "kostenrechner",
    "notfallkarte",
    "checkliste-todesfall",
    "vorsorge-check",
]

results = []
for slug in TARGETS:
    p = TOOLS / slug / "index.html"
    if not p.exists():
        results.append((slug, "MISSING"))
        continue
    text = p.read_text(encoding="utf-8")

    # Find and remove the FAQPage entry from @graph
    # Pattern: {"@type":"FAQPage", ... } either as last element or middle
    # Match the FAQPage object with its mainEntity array including closing braces
    pattern_last = r',\s*\{"@type":"FAQPage","mainEntity":\[.*?\]\}(?=\]\})'
    pattern_mid  = r'\{"@type":"FAQPage","mainEntity":\[.*?\]\},\s*'

    new_text, n1 = re.subn(pattern_last, '', text, count=1, flags=re.DOTALL)
    if n1 == 0:
        new_text, n1 = re.subn(pattern_mid, '', text, count=1, flags=re.DOTALL)

    # Also handle multi-line ld+json with newlines (checkliste-todesfall, fristen-radar)
    if n1 == 0:
        pattern_multi = r',\s*\{"@type":"FAQPage","mainEntity":\[[^\]]+(?:\][^\]]*)*\]\}'
        new_text, n1 = re.subn(pattern_multi, '', text, flags=re.DOTALL, count=1)

    if n1 > 0:
        p.write_text(new_text, encoding="utf-8")
        results.append((slug, f"REMOVED FAQPage ({n1} match)"))
    else:
        results.append((slug, "NO FAQPage found"))

for r in results:
    print(r)
