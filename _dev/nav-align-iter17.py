#!/usr/bin/env python3
"""
iter-17 (2026-06-04): Nav bündig zum Inhalt.
nav-inner zentrierte 20px links neben Content/Breadcrumb, weil .mr-nav padding:0 20px
hat (Inner zentriert IM gepolsterten Bereich). .mr-content/.mr-breadcrumb haben aber
max-width:720 + padding:0 20px direkt. Fix: Polsterung von .mr-nav auf .mr-nav-inner
verlagern -> identisches Box-Model -> exakt bündig. Append (last-wins) auf alle
Seiten mit iter-15- oder iter-16-Nav.
"""
import glob, os

MARKER = "iter-17 nav-align"
CSS = """
/* """ + MARKER + """ (2026-06-04): nav-inner Box-Model = .mr-content -> linke Kante bündig */
.mr-nav{padding-left:0;padding-right:0}
.mr-nav-inner{padding-left:20px;padding-right:20px}
"""

changed = 0
for f in glob.glob("**/*.html", recursive=True):
    nf = f.replace("\\", "/")
    if nf.startswith("_dev/"):
        continue
    html = open(f, encoding="utf-8").read()
    if "iter-15 nav-slim" not in html and "iter-16 nav-graft" not in html:
        continue
    if MARKER in html:
        continue
    idx = html.rfind("</style>")
    if idx == -1:
        continue
    open(f, "w", encoding="utf-8").write(html[:idx] + CSS + html[idx:])
    changed += 1
print(f"Geaendert: {changed}")
