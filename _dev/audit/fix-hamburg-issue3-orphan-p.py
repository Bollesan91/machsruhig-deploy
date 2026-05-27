#!/usr/bin/env python3
"""Issue 3 fix — orphan <p> in Cross-City block extracted into its own
mr-section ('Gebühren & Kostenvoranschläge'), placed BEFORE the
'Bestatter in anderen Städten' section."""
from pathlib import Path
import re, sys

FP = Path("bestatter/hamburg/index.html")
src = FP.read_text(encoding="utf-8")

# Detect orphan <p> still inside Cross-City section. Pattern:
#   </div>                              [closes mr-container]
#   <orphan p block>
#   </section>
ORPHAN_P_RE = re.compile(
    r'(    </div>\n)'
    r'(    <p>Die exakten Gebühren[^\n]*</p>\n)'
    r'(  </section>\n)',
    re.DOTALL,
)
m = ORPHAN_P_RE.search(src)
if not m:
    print("ERROR: orphan <p> pattern not found"); sys.exit(1)

orphan_p_html = m.group(2).strip()  # the <p>...</p>

# Remove orphan <p> from the section
without_orphan = src[:m.start()] + m.group(1) + m.group(3) + src[m.end():]

# Build new mr-section to insert BEFORE the Cross-City section
NEW_SECTION = '''  <div class="mr-section">
    <h2>Gebühren & Kostenvoranschläge — Tipps zur Bestatter-Wahl</h2>
    <p>Die exakten Gebühren — Grabnutzung, Beisetzung, Nutzung der Trauerhalle — stellt die <a href="https://www.friedhof-hamburg.de/" rel="noopener" target="_blank">Hamburger Friedhöfe AöR</a> in ihrer Gebührenordnung bereit. Bestatterleistungen werden frei vereinbart; Stiftung Warentest und die Verbraucherzentrale empfehlen, mindestens drei Kostenvoranschläge einzuholen und auf Transparenz bei den durchlaufenden Posten (Friedhofs- und Gebührenanteil) zu achten. Vergleichshilfe: <a href="/bestattungskosten">Bestattungskosten — Aufschlüsselung der Posten</a>.</p>
  </div>

'''

# Locate Cross-City section start in the cleaned-up text
CROSS_CITY_PAT = re.compile(r'<section class="mr-section"[^>]*>\s*\n\s*<div class="mr-container">\s*\n\s*<h2>Bestatter in anderen Städten</h2>')
m2 = CROSS_CITY_PAT.search(without_orphan)
if not m2:
    print("ERROR: Cross-City section anchor not found"); sys.exit(1)

# Insert new section right before the section opening tag, accounting for indent
section_start = m2.start()
out = without_orphan[:section_start] + NEW_SECTION + without_orphan[section_start:]

# Sanity: still exactly one occurrence of the orphan-p text, but now inside an mr-section block
if out.count("Die exakten Gebühren") != 1:
    print(f"ERROR: orphan-p text count={out.count('Die exakten Gebühren')}"); sys.exit(1)
# Sanity: Cross-City section no longer has trailing <p>
cross_section = re.search(
    r'<section class="mr-section"[^>]*>.*?</section>',
    out, re.DOTALL
)
if cross_section and "Die exakten Gebühren" in cross_section.group(0):
    print("ERROR: orphan <p> still inside Cross-City section"); sys.exit(1)

FP.write_text(out, encoding="utf-8")
print(f"OK Issue 3  src={len(src)}B  out={len(out)}B  diff={len(out)-len(src):+d}B  orphan-p-relocated")
