#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R1c (2026-06-10) — Top-Nav: "Notfallkarte" -> "Angebot pruefen" (1:1-Tausch,
bleibt bei 7 Links / iter-15-Disziplin). Notfallkarte bleibt im Footer ("Themen")
site-weit erreichbar. Begruendung: Angebotspruefer = staerkster USP (Roadmap Rang 1,
Cross-Hebel 4: Produktmitte).
"""
import io, glob, os

OLD = '      <a href="/trauerrede-schreiben">Trauerrede</a>\n      <a href="/notfallkarte">Notfallkarte</a>'
NEW = '      <a href="/trauerrede-schreiben">Trauerrede</a>\n      <a href="/tools/angebotspruefer/">Angebot prüfen</a>'

files = [p for p in glob.glob('**/*.html', recursive=True)
         if not p.replace(os.sep, '/').startswith('_dev/')]
n = 0
miss = []
for p in files:
    t = io.open(p, encoding='utf-8').read()
    c = t.count(OLD)
    if c == 1:
        io.open(p, 'w', encoding='utf-8', newline='').write(t.replace(OLD, NEW))
        n += 1
    elif c > 1:
        raise SystemExit('MEHRFACH in ' + p)
    elif 'mr-nav-links' in t:
        miss.append(p)
print('Nav getauscht auf %d Seiten' % n)
if miss:
    print('Seiten mit mr-nav-links OHNE Standard-Muster (%d):' % len(miss))
    for p in miss[:10]:
        print('  -', p)
