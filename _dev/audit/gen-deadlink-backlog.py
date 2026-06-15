#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, re, glob, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
res = io.open(os.path.join(ROOT, '_dev/audit/_extres.txt'), encoding='utf-8')
dead = [l.split(' ', 1)[1].strip() for l in res if l[:4] in ('404 ', '410 ')]
files = [f for f in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)
         if os.sep + '_dev' + os.sep not in f]
pmap = {u: [] for u in dead}
for f in files:
    t = io.open(f, encoding='utf-8').read()
    rel = os.path.relpath(f, ROOT).replace(os.sep, '/')
    for u in dead:
        if u in t:
            pmap[u].append(rel)

def pname(p):
    return p.split('/')[-2] if p.endswith('/index.html') else p.split('/')[-1].replace('.html', '')

P1 = ['bsg.bund.de', 'mwg.rlp.de', 'aeternitas.de', 'verbraucherzentrale.de', 'caritas',
      'recht.nrw.de', 'voris.', 'lexsoft.de', 'justiz.nrw', 'bestattungsdienst.freiburg',
      'bestatterdeutschland', 'bestatter.de', 'bestatter-nrw', 'afilio', 'smartlaw',
      'bremische-buergerschaft', 'bau.bremen', 'buerger.sachsen-anhalt', 'amt24.sachsen', 'bravors']
P2KEYS = ['friedhof', 'standesamt', 'satzung', 'friedhoefe', 'gebuehr', 'sterbefall',
          'krematorium', 'umweltbetrieb', 'produkte', 'ortsrecht', 'grabsuche',
          'dienstleistung', 'leistung', 'amtsblatt']

def prio(u):
    if any(k in u for k in P1):
        return 'P1'
    if any(k in u for k in P2KEYS):
        return 'P2'
    return 'P3'

buckets = {'P1': [], 'P2': [], 'P3': []}
for u in dead:
    buckets[prio(u)].append(u)

EMD = '—'
BT = '`'
lab = {
    'P1': '## P1 ' + EMD + ' YMYL/Recht/Quelle (zuerst, claim-kritisch)',
    'P2': '## P2 ' + EMD + ' Behoerde/Satzung/Friedhofsamt (meist Stadtseiten)',
    'P3': '## P3 ' + EMD + ' Historie/Promi/nice-to-have (entfernen oder ersetzen)',
}
out = []
out.append('# Tote externe Quelllinks ' + EMD + ' Sweep 15.06.2026')
out.append('')
out.append('> 74 harte 404 (selbst gecurlt 15.06. + WebFetch-stichprobenverifiziert: bsg.bund.de, aeternitas) von 821 Nicht-Wikipedia-Quelllinks. NICHT blind ersetzen ' + EMD +
           ' jede Ersatz-URL primaerverifizieren (LEKTIONEN #6), bei YMYL-Recht auch Claim<->Fundstelle erneut pruefen. Bereits gefixt: 6 test.de-Tote (Hub) + aeternitas-bestattungsgesetze (bestattung-in-Hub).')
out.append('')
for k in ['P1', 'P2', 'P3']:
    out.append(lab[k])
    out.append('')
    for u in sorted(buckets[k]):
        pages = ','.join(sorted(set(pname(p) for p in pmap[u])))
        out.append('- [ ] ' + BT + u + BT + ' ' + EMD + ' ' + pages)
    out.append('')
io.open(os.path.join(ROOT, '_dev/docs/DEAD-LINKS-2026-06-15.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('P1=%d P2=%d P3=%d total=%d' % (len(buckets['P1']), len(buckets['P2']), len(buckets['P3']), len(dead)))
