#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wire-overview-lotse.py — je Stadt-Uebersicht einen Link aus dem Gebuehren-Kasten
zur Vergleichs-Lotse (/friedhoefe/gebuehren/) einfuegen. 50 Inbound-Links = Crawl-Signal.
Idempotent. Asserts vor Write. DRY default; --apply schreibt (nur geaenderte Dateien).
"""
import os, sys, re, glob, io

DRY = "--apply" not in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LINK = ('\n      <p style="margin:8px 0 0;font-size:13px;line-height:1.5">'
        '<a href="/friedhoefe/gebuehren/" style="color:var(--mr-accent,#866E45);font-weight:600;text-decoration:none">'
        '&rarr; Im bundesweiten Vergleich</a>: Was ein Grab in 50 St&auml;dten kostet '
        '(805&nbsp;&euro; Berlin bis 4.714&nbsp;&euro; Mainz).</p>')

changed, skipped, errors = [], [], []
for fp in sorted(glob.glob(os.path.join(ROOT, "friedhoefe", "*", "index.html"))):
    rel = os.path.relpath(fp, ROOT).replace("\\", "/")
    s = io.open(fp, encoding="utf-8").read()
    if 'class="fh-gebuehren-beispiel"' not in s:
        continue  # kein Gebuehren-Kasten (z. B. Hub liegt nicht hier)
    if "/friedhoefe/gebuehren/" in s:
        skipped.append(rel); continue  # schon verlinkt
    i = s.index('class="fh-gebuehren-beispiel"')
    open_start = s.rfind("<div", 0, i)
    close = s.index("</div>", i)
    inner = s[open_start:close]
    # Kasten darf keine verschachtelte <div> enthalten (sonst falsches Schliess-Tag)
    if inner.count("<div") != 1:
        errors.append((rel, f"verschachtelte div im Kasten ({inner.count('<div')})")); continue
    new = s[:close] + LINK + s[close:]
    assert new.count("/friedhoefe/gebuehren/") == 1, f"{rel}: Link-Anzahl != 1"
    assert new.count('class="fh-gebuehren-beispiel"') == 1, f"{rel}: Kasten dupliziert"
    if not DRY:
        io.open(fp, "w", encoding="utf-8").write(new)
    changed.append(rel)

print(f"{'[DRY] ' if DRY else ''}Gebühren-Kasten -> Lotse verlinkt:")
print(f"  geändert: {len(changed)}   schon verlinkt: {len(skipped)}   Fehler: {len(errors)}")
if errors:
    for e in errors: print("  FEHLER", e)
if changed[:3]: print("  Beispiele:", ", ".join(changed[:3]))
sys.exit(1 if errors else 0)
