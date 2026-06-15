#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regeneriert das Dead-Link-Backlog aus _extres.txt + aktuellem Live-Stand.
Markiert gefixt vs. verbleibend; Sonder-Bucket fuer gesponserte CTAs (Bolle-Entscheid)."""
import io, re, glob, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
res = io.open(os.path.join(ROOT, '_dev/audit/_extres.txt'), encoding='utf-8')
dead = [l.split(' ', 1)[1].strip() for l in res if l[:4] in ('404 ', '410 ')]
files = [f for f in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)
         if os.sep + '_dev' + os.sep not in f]
blob = {os.path.relpath(f, ROOT).replace(os.sep, '/'): io.open(f, encoding='utf-8').read() for f in files}

def pages_of(u):
    # exakte href-Praesenz (vermeidet Substring-FP wie aachen-Bare-URL in laengerem Live-Link)
    return sorted(set(k for k, v in blob.items() if ('href="' + u + '"') in v))

def pname(p):
    return p.split('/')[-2] if p.endswith('/index.html') else p.rsplit('/', 1)[-1].replace('.html', '')

remaining = [(u, pages_of(u)) for u in dead if pages_of(u)]
fixed = len(dead) - len(remaining)

SPONSORED = ['afilio.de', 'smartlaw.de']
P2KEYS = ['friedhof', 'standesamt', 'satzung', 'friedhoefe', 'gebuehr', 'sterbefall',
          'krematorium', 'umweltbetrieb', 'produkte', 'ortsrecht', 'grabsuche',
          'dienstleistung', 'leistung', 'amtsblatt', 'Infoblatt', 'aachener_stadtbetrieb']

def bucket(u):
    if any(k in u for k in SPONSORED):
        return 'SPONSORED'
    if any(k in u for k in P2KEYS):
        return 'P2'
    # Recht/Verzeichnis/News-Reste
    if any(k in u for k in ['bestatter', 'caritas', 'taspo', 'voris', 'lexsoft', 'justiz', 'recht.', 'verband']):
        return 'P1'
    return 'P3'

buckets = {'SPONSORED': [], 'P1': [], 'P2': [], 'P3': []}
for u, pgs in remaining:
    buckets[bucket(u)].append((u, pgs))

EMD, BT = '—', '`'
out = []
out.append('# Tote externe Quelllinks ' + EMD + ' Sweep 15.06.2026')
out.append('')
out.append('> Ausgangslage: 74 harte 404 von 821 Nicht-Wikipedia-Quelllinks (curl + WebFetch-verifiziert). '
           + '**%d gefixt** (test.de-Hub, aeternitas, BestG NRW/RLP, BSG- + LSG-NRW-Entscheidung, Nds/Bremen-Statut, VZ-Cluster), **%d verbleibend.**' % (fixed, len(remaining)))
out.append('')
out.append('## ' + EMD + ' Bolle-Entscheid: gesponserte CTAs (Monetarisierung, NICHT raten)')
out.append('Tote `rel="sponsored"`-CTA-Buttons ' + EMD + ' Partner-URL/Affiliate-Tracking pruefen, evtl. Partnerschaft beendet:')
for u, pgs in buckets['SPONSORED']:
    out.append('- [ ] ' + BT + u + BT + ' ' + EMD + ' ' + ','.join(pname(p) for p in pgs))
out.append('')
out.append('## P1-Rest ' + EMD + ' Recht/Verzeichnis/News (verifiziert reparieren oder ent-linken)')
for u, pgs in sorted(buckets['P1']):
    out.append('- [ ] ' + BT + u + BT + ' ' + EMD + ' ' + ','.join(sorted(set(pname(p) for p in pgs))))
out.append('')
out.append('## P2 ' + EMD + ' kommunale Friedhof/Standesamt-Links (' + str(len(buckets['P2'])) + ', eigene Fokus-Session pro Stadt)')
out.append('Niedrige Prio (einzelne Stadtseiten). Korrekt = je Stadt aktuelle Friedhof/Standesamt-Landingpage suchen+verifizieren ODER ent-linken. NICHT blind raten.')
for u, pgs in sorted(buckets['P2']):
    out.append('- [ ] ' + BT + u + BT + ' ' + EMD + ' ' + ','.join(sorted(set(pname(p) for p in pgs))))
out.append('')
out.append('## P3 ' + EMD + ' Historie/Promi/nice-to-have (ent-linken ok)')
for u, pgs in sorted(buckets['P3']):
    out.append('- [ ] ' + BT + u + BT + ' ' + EMD + ' ' + ','.join(sorted(set(pname(p) for p in pgs))))
out.append('')
io.open(os.path.join(ROOT, '_dev/docs/DEAD-LINKS-2026-06-15.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('fixed=%d remaining=%d  SPONSORED=%d P1=%d P2=%d P3=%d'
      % (fixed, len(remaining), len(buckets['SPONSORED']), len(buckets['P1']), len(buckets['P2']), len(buckets['P3'])))

if __name__ == '__main__':
    pass
