"""
Kürze meta descriptions auf <= 158 Zeichen.
Strategie: Truncate am letzten Komma vor Position 158, fallback Punkt.
Update sowohl <meta name="description"> als auch <meta property="og:description">.
"""
import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"

TARGET_MAX = 158
SAFE_MIN = 110  # don't cut below this

DESC_RE = re.compile(r'(<meta[^>]*name="description"[^>]*content=")([^"]+)(")', re.IGNORECASE)
OG_DESC_RE = re.compile(r'(<meta[^>]*property="og:description"[^>]*content=")([^"]+)(")', re.IGNORECASE)


def truncate_smart(s: str) -> str:
    """Truncate at last comma or period before TARGET_MAX, append . if needed."""
    if len(s) <= TARGET_MAX:
        return s

    cut = s[:TARGET_MAX]
    # Try comma boundary
    last_comma = cut.rfind(", ")
    last_period = cut.rfind(". ")
    last_semicolon = cut.rfind("; ")

    # Use the latest boundary >= SAFE_MIN
    best = max(last_comma, last_period, last_semicolon)
    if best >= SAFE_MIN:
        cut = cut[:best]
        if not cut.endswith(("."," !","?")):
            cut = cut.rstrip(",;: ") + "."
        return cut

    # Fallback: cut at word boundary
    last_space = cut.rfind(" ")
    if last_space >= SAFE_MIN:
        cut = cut[:last_space].rstrip(",;: ") + "."
        return cut

    # Hard cut
    return cut.rstrip(",;: ") + "."


processed = []
already_ok = []

for city_dir in sorted(BESTATTER.iterdir()):
    if not city_dir.is_dir():
        continue
    idx = city_dir / "index.html"
    if not idx.exists():
        continue
    slug = city_dir.name
    text = idx.read_text(encoding="utf-8", errors="replace")

    # Find description
    desc_m = DESC_RE.search(text)
    if not desc_m:
        continue
    desc_full = desc_m.group(2)
    if len(desc_full) <= TARGET_MAX:
        already_ok.append(slug)
        continue

    new_desc = truncate_smart(desc_full)
    new_text = DESC_RE.sub(lambda m: m.group(1) + new_desc + m.group(3), text, count=1)

    # Also try og:description (often same content)
    og_m = OG_DESC_RE.search(new_text)
    if og_m and og_m.group(2) == desc_full:
        new_text = OG_DESC_RE.sub(lambda m: m.group(1) + new_desc + m.group(3), new_text, count=1)

    if new_text != text:
        idx.write_text(new_text, encoding="utf-8")
        processed.append((slug, len(desc_full), len(new_desc), new_desc[:80]))

print(f"Processed: {len(processed)}")
for s, old, new, sample in processed[:8]:
    print(f"  {s}: {old} -> {new} chars  ('{sample}...')")
if len(processed) > 8:
    print(f"  ... +{len(processed)-8} more")
print(f"\nAlready OK: {len(already_ok)}")
