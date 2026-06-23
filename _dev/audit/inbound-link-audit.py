# -*- coding: utf-8 -*-
"""Read-only: interner Inbound-Link-Audit. Zaehlt je Seite, wie viele andere
Seiten auf sie verlinken. Findet schwach verlinkte Seiten (Index-Risiko)."""
import os, glob

pages = [p for p in glob.glob('**/*.html', recursive=True)
         if (os.sep + '_dev') not in (os.sep + p) and os.path.basename(p) != '404.html']

def url(p):
    p = p.replace(os.sep, '/')
    if p.endswith('/index.html'):
        return '/' + p[:-len('index.html')]   # .../  (trailing slash)
    return '/' + p[:-len('.html')]

texts = {p: open(p, encoding='utf-8').read() for p in pages}
rows = []
for p in pages:
    u = url(p)
    base = u.rstrip('/')
    pats = ['href="%s"' % base, 'href="%s/"' % base]
    inb = sum(1 for q in pages if q != p and any(x in texts[q] for x in pats))
    rows.append((inb, u))
rows.sort()

print("=== 18 schwaechste Seiten (Inbound-Links) ===")
for inb, u in rows[:18]:
    print("%3d  %s" % (inb, u))

print("\n=== Transparenz-Cluster + angebot-pruefen-Satelliten ===")
key = ['angebotsstandard', 'transparenz-kriterien', 'transparenzprofil', 'fuer-bestatter',
       'angebot-pruefen', 'angebot-vergleichen', 'rechnung-pruefen']
for inb, u in rows:
    if any(k in u for k in key):
        print("%3d  %s" % (inb, u))

import statistics
vals = [r[0] for r in rows]
print("\nSeiten gesamt: %d | Median Inbound: %d | <3 Inbound: %d"
      % (len(rows), statistics.median(vals), sum(1 for v in vals if v < 3)))
