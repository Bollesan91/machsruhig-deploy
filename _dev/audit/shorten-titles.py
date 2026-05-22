"""
Kürze <title>-Tags auf <= 60 char.
Strategie: Brand-Suffix entfernen ("| machsruhig" etc.).
Wenn dann immer noch >60: Truncate-am-Komma.
Auch og:title parallel updaten wenn identisch.
"""
import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"

TARGET = 60
BRAND_SUFFIXES = [
    " | machsruhig.de",
    " | machsruhig",
    " | mach's ruhig",
    " — machsruhig.de",
    " — machsruhig",
    " — mach's ruhig",
]


def shorten(title):
    new = title
    for sfx in BRAND_SUFFIXES:
        if new.endswith(sfx):
            new = new[: -len(sfx)]
            break
    if len(new) <= TARGET:
        return new
    # Truncate am letzten Komma vor TARGET-1
    cut = new[: TARGET - 1]
    last_comma = cut.rfind(", ")
    if last_comma >= TARGET - 30:
        return cut[:last_comma]
    # Sonst am letzten Leerzeichen
    last_space = cut.rfind(" ")
    if last_space >= TARGET - 30:
        return cut[:last_space]
    return cut


TITLE_RE = re.compile(r"<title[^>]*>([^<]+)</title>", re.IGNORECASE)
OG_TITLE_RE = re.compile(r'(<meta[^>]*property="og:title"[^>]*content=")([^"]+)(")', re.IGNORECASE)


def fix_file(p: Path) -> tuple:
    text = p.read_text(encoding="utf-8", errors="replace")
    m = TITLE_RE.search(text)
    if not m:
        return False, "no-title"
    old_title = m.group(1)
    if len(old_title) <= TARGET:
        return False, "already-ok"
    new_title = shorten(old_title)
    if new_title == old_title:
        return False, "no-shortening-applicable"

    # Replace title
    new_text = text[: m.start(1)] + new_title + text[m.end(1):]

    # If og:title was identical to old title, replace it too
    og_m = OG_TITLE_RE.search(new_text)
    if og_m and og_m.group(2) == old_title:
        new_text = (
            new_text[: og_m.start(2)] + new_title + new_text[og_m.end(2):]
        )

    p.write_text(new_text, encoding="utf-8")
    return True, f"{len(old_title)}→{len(new_title)}"


processed = []
for city_dir in sorted(BESTATTER.iterdir()):
    if not city_dir.is_dir():
        continue
    idx = city_dir / "index.html"
    if not idx.exists():
        continue
    modified, info = fix_file(idx)
    if modified:
        processed.append((city_dir.name, info))

print(f"Processed: {len(processed)} files")
for slug, info in processed[:10]:
    print(f"  {slug}: {info}")
if len(processed) > 10:
    print(f"  ... +{len(processed)-10} more")
