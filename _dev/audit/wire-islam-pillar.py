#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# De-orphan: Islam-Bestattung-Pillar in den "Passend dazu"-Block jeder Friedhof-Uebersicht.
# Strukturell (mr-related <ul>), idempotent, mit Asserts. DRY-RUN default; --apply schreibt.
import os, re, sys, glob
DRY = "--apply" not in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LI = '\n      <li><a href="/islamische-bestattung">Islamische Bestattung</a> — Ablauf, Recht und Grabfeld-Suche in Deutschland</li>'
re_anchor = re.compile(r'(<div class="mr-related">\s*<h2>Passend dazu</h2>\s*<ul>)')

paths = sorted(glob.glob(os.path.join(ROOT,"friedhoefe","*","index.html")))
done=[]; skip=[]; err=[]
for p in paths:
    html = open(p,encoding="utf-8").read()
    rel = os.path.relpath(p, ROOT)
    if '/islamische-bestattung' in html: skip.append(rel+"(schon)"); continue
    if not re_anchor.search(html): skip.append(rel+"(kein-Anker)"); continue
    new = re_anchor.sub(r'\1'+LI, html, count=1)
    if new.count('/islamische-bestattung')!=1: err.append(rel+": Link-Count!=1"); continue
    if new.count('mr-related')!=html.count('mr-related'): err.append(rel+": mr-related veraendert"); continue
    if not DRY: open(p,"w",encoding="utf-8").write(new)
    done.append(rel)
print(f"=== {'DRY-RUN' if DRY else 'APPLY'} === Uebersichten: {len(paths)} | geaendert {len(done)} | skip {len(skip)} | fehler {len(err)}")
for s in skip[:5]: print("  SKIP",s)
for e in err: print("  ERR",e)
