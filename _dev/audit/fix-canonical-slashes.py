"""
Vereinheitlicht Canonical-URLs auf trailing-slash für Directory-Pages.
Vorher: <link rel="canonical" href="https://machsruhig.de/tools/abschiedsbrief">
Nachher: <link rel="canonical" href="https://machsruhig.de/tools/abschiedsbrief/">

Plus: og:url + Schema-JSON-LD url-Felder werden konsistent.
"""
import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent

# Directories die trailing-slash bekommen sollen
DIRS = ["tools", "vorsorge", "bestatter", "bestattung-in"]


def fix_file(p: Path) -> tuple:
    text = p.read_text(encoding="utf-8", errors="replace")
    orig = text
    fixes = []

    for d in DIRS:
        # canonical
        text, n1 = re.subn(
            r'(<link[^>]*rel="canonical"[^>]*href=")https://machsruhig\.de/(' + re.escape(d) + r'/[a-z0-9-]+)("\s*/?>)',
            lambda m: m.group(1) + "https://machsruhig.de/" + m.group(2) + "/" + m.group(3),
            text,
        )
        # og:url
        text, n2 = re.subn(
            r'(<meta[^>]*property="og:url"[^>]*content=")https://machsruhig\.de/(' + re.escape(d) + r'/[a-z0-9-]+)(")',
            lambda m: m.group(1) + "https://machsruhig.de/" + m.group(2) + "/" + m.group(3),
            text,
        )
        # Schema JSON-LD: "url":"https://machsruhig.de/tools/x"
        text, n3 = re.subn(
            r'("url"\s*:\s*")https://machsruhig\.de/(' + re.escape(d) + r'/[a-z0-9-]+)(")',
            lambda m: m.group(1) + "https://machsruhig.de/" + m.group(2) + "/" + m.group(3),
            text,
        )
        # Schema "@id":"https://machsruhig.de/tools/x#..."
        text, n4 = re.subn(
            r'("@id"\s*:\s*")https://machsruhig\.de/(' + re.escape(d) + r'/[a-z0-9-]+)(#)',
            lambda m: m.group(1) + "https://machsruhig.de/" + m.group(2) + "/" + m.group(3),
            text,
        )
        # Schema "@id":"https://machsruhig.de/tools/x"
        text, n5 = re.subn(
            r'("@id"\s*:\s*")https://machsruhig\.de/(' + re.escape(d) + r'/[a-z0-9-]+)(")',
            lambda m: m.group(1) + "https://machsruhig.de/" + m.group(2) + "/" + m.group(3),
            text,
        )

        total = n1 + n2 + n3 + n4 + n5
        if total > 0:
            fixes.append(f"{d}:{total}")

    if text != orig:
        p.write_text(text, encoding="utf-8")
        return True, ", ".join(fixes)
    return False, ""


changed = []
for root in DIRS:
    base = ROOT / root
    if not base.exists():
        continue
    # Per-directory index.html files
    for idx in base.glob("*/index.html"):
        modified, info = fix_file(idx)
        if modified:
            changed.append(f"{idx.relative_to(ROOT)} ({info})")

# Also fix /vorsorge/index.html, /bestatter/index.html, /tools/index.html if they reference sub-pages
for root_hub in ["vorsorge/index.html", "bestatter/index.html"]:
    p = ROOT / root_hub
    if p.exists():
        modified, info = fix_file(p)
        if modified:
            changed.append(f"{root_hub} ({info})")

print(f"Fixed: {len(changed)} files")
for c in changed[:15]:
    print(f"  {c}")
if len(changed) > 15:
    print(f"  ... +{len(changed)-15} more")
