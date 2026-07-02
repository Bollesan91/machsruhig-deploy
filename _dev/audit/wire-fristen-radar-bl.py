#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fristen-Radar-Hinweis in die Fristen-Sektion aller 16 BL-Seiten (idempotent, Asserts vor Write).
# Text bewusst ehrlich: Radar = Verwaltungsfristen ab Sterbedatum (Ergaenzung zu Bestattungsfristen).
import os, re, sys, glob
DRY = "--apply" not in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HINT = '''    <div class="mr-hint no-print">
      <strong>Neben den Bestattungsfristen laufen weitere Fristen:</strong> Erbausschlagung, Rentenanträge, Kündigungen. Der kostenlose <a href="/tools/fristen-radar/">Fristen-Radar</a> berechnet die konkreten Termine ab Sterbedatum — mit Kalender-Export.
    </div>
'''
re_h2 = re.compile(r'<h2>[^<]*[Ff]rist[^<]*</h2>')
done=[];skip=[];err=[]
for p in sorted(glob.glob(os.path.join(ROOT,"bestattung-in","*","index.html"))):
    rel=os.path.relpath(p,ROOT)
    html=open(p,encoding="utf-8").read()
    if '/tools/fristen-radar/' in html: skip.append(rel+"(schon)"); continue
    m=re_h2.search(html)
    if not m: err.append(rel+": keine Fristen-H2"); continue
    # naechstes schliessendes </div> der Sektion (2-Spaces-Einrueckung) nach der H2
    idx=html.find("\n  </div>", m.end())
    if idx<0: err.append(rel+": kein Sektions-Ende"); continue
    new=html[:idx+1]+HINT+html[idx+1:]
    # Asserts
    if new.count('/tools/fristen-radar/')!=1: err.append(rel+": Link!=1"); continue
    if new.count('<div class="mr-hint')!=html.count('<div class="mr-hint')+1: err.append(rel+": hint-Count"); continue
    if new.count('</div>')!=html.count('</div>')+1: err.append(rel+": div-Balance"); continue
    if not DRY: open(p,"w",encoding="utf-8").write(new)
    done.append(rel)
print(f"=== {'DRY' if DRY else 'APPLY'} === ok {len(done)} | skip {len(skip)} | err {len(err)}")
for e in err+skip[:3]: print("  ", e)
