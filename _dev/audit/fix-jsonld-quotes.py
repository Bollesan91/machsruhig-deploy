"""
Fix pre-existing JSON-LD quote-bugs in darmstadt + muenster.

Pattern: `„text"` (low quote U+201E opener, straight quote U+0022 closer) inside JSON strings.
The closing straight quote breaks JSON parsing. Replace with U+201D right curly quote.
"""

import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
BESTATTER = _HERE.parent.parent / "bestatter"

JSON_LD_RE = re.compile(
    r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',
    re.DOTALL | re.IGNORECASE,
)

# Match a low quote opener, then any chars (non-greedy, no straight quote inside),
# then a straight quote U+0022 followed by punctuation or whitespace (i.e. close-quote position).
QUOTE_FIX = re.compile(r'(„[^"„]+?)"(?=[\s.,;:!?\)\]])')

def fix_one(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")

    fixes = 0
    def replace_in_script(m):
        nonlocal fixes
        opener, body, closer = m.group(1), m.group(2), m.group(3)
        new_body, n = QUOTE_FIX.subn(lambda mm: mm.group(1) + "”", body)
        fixes += n
        return opener + new_body + closer

    new_text = JSON_LD_RE.sub(replace_in_script, text)

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return fixes


def main():
    for slug in ("darmstadt", "muenster"):
        idx = BESTATTER / slug / "index.html"
        if not idx.exists():
            print(f"{slug}: missing")
            continue
        n = fix_one(idx)
        print(f"{slug}: {n} quote-pairs fixed")


if __name__ == "__main__":
    main()
