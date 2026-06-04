#!/usr/bin/env python3
"""
iter-13 (2026-06-04): Nav linksbuendig (User-Wunsch). Site-weit.
Ersetzt justify-content:space-between -> flex-start NUR innerhalb der
.mr-nav-inner{...}-Regel (nicht global). Idempotent.
"""
import glob, re, os

def fix(html):
    def repl(m):
        return m.group(0).replace('justify-content:space-between', 'justify-content:flex-start')
    return re.sub(r'\.mr-nav-inner\{[^}]*\}', repl, html)

changed = 0
for f in glob.glob("**/*.html", recursive=True):
    nf = f.replace("\\", "/")
    if nf.startswith("_dev/"):
        continue
    html = open(f, encoding="utf-8").read()
    new = fix(html)
    if new != html:
        open(f, "w", encoding="utf-8").write(new)
        changed += 1

print(f"Geaendert: {changed} Produktivseiten")
