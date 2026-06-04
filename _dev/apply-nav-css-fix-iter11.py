#!/usr/bin/env python3
"""
iter-11 Fix (2026-06-04): Kaputte Navigation/Breadcrumb auf Stadt-Seiten.
Root Cause: Markup nutzt class="mr-logo" + nacktes <ul>/<ol>, das vorhandene
Inline-CSS stylt aber .mr-nav-links/.mr-nav-logo (Klassen-Mismatch nach iter-10).
Fix: self-contained Compat-CSS vor das letzte </style> jeder betroffenen Seite
injizieren — stylt das tatsaechliche Markup direkt, mit var()-Fallbacks, additiv.
Idempotent: Seiten mit dem Marker werden uebersprungen.
"""
import glob, sys

MARKER = "iter-11 nav-compat"
COMPAT = """
/* """ + MARKER + """ (2026-06-04): Nav/Breadcrumb-Markup nutzt <ul>/<ol>+.mr-logo statt .mr-nav-links — Styling robust nachgezogen */
.mr-nav-inner{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
a.mr-logo{font-family:'Fraunces',Georgia,serif;font-size:18px;font-weight:700;color:var(--mr-text,#2D2319);text-decoration:none}
.mr-nav-inner>ul{display:flex;flex-wrap:wrap;gap:4px;align-items:center;list-style:none;margin:0;padding:0}
.mr-nav-inner>ul>li{list-style:none}
.mr-nav-inner>ul a{font-size:13px;font-weight:500;color:var(--mr-text-muted,#73655A);text-decoration:none;padding:6px 12px;border-radius:8px;transition:color .2s,background .2s}
.mr-nav-inner>ul a:hover{color:var(--mr-text,#2D2319);background:rgba(122,107,93,.08)}
.mr-breadcrumb ol{list-style:none;display:flex;flex-wrap:wrap;gap:0;margin:0;padding:0}
.mr-breadcrumb ol li{display:inline-flex;align-items:center}
.mr-breadcrumb ol li+li::before{content:'\\203A';margin:0 8px;color:var(--mr-text-muted,#73655A)}
@media(max-width:640px){.mr-nav-inner>ul a{font-size:12px;padding:5px 8px}}
"""

fixed, skipped, untouched = [], [], 0
for f in sorted(glob.glob("bestatter/*/index.html")):
    html = open(f, encoding="utf-8").read()
    if 'class="mr-logo"' not in html:
        untouched += 1
        continue
    if MARKER in html:
        skipped.append(f)
        continue
    idx = html.rfind("</style>")
    if idx == -1:
        print("  !! KEIN </style> in", f); continue
    new = html[:idx] + COMPAT + html[idx:]
    open(f, "w", encoding="utf-8").write(new)
    fixed.append(f)

print(f"Gefixt: {len(fixed)} | Schon-gefixt-uebersprungen: {len(skipped)} | Nicht-betroffen: {untouched}")
for f in fixed: print("  +", f)
