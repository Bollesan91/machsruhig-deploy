#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Interne Verlinkung: Der Friedhofs-Cluster (67 Seiten) hing an EINEM Hub mit nur 2
# Content-Links; jede Stadt hatte genau 2 eingehende Links. Die 16 Bundesland-Seiten
# verlinkten auf /bestatter/<stadt>/, aber auf KEINE einzige /friedhoefe/<stadt>/-Seite
# (0 von 16 geprueft). Das ist die wahrscheinlichste Ursache fuer "entdeckt, nicht
# indexiert" im Friedhofs-Cluster. Fix: je Bundesland-Seite ein Absatz mit Links auf
# die Friedhofs-Stadtseiten dieses Landes (Quelle: verifiziertes Gebuehren-Register).
# Asserts vor jedem Write.
import json, io, os, re

reg = json.load(io.open('_dev/claims/friedhofsgebuehren.json', encoding='utf-8'))
LAND = {'BW':('baden-wuerttemberg','Baden-Wuerttemberg'), 'BY':('bayern','Bayern'),
        'BE':('berlin','Berlin'), 'BB':('brandenburg','Brandenburg'), 'HB':('bremen','Bremen'),
        'HH':('hamburg','Hamburg'), 'HE':('hessen','Hessen'),
        'MV':('mecklenburg-vorpommern','Mecklenburg-Vorpommern'), 'NI':('niedersachsen','Niedersachsen'),
        'NRW':('nordrhein-westfalen','Nordrhein-Westfalen'), 'NW':('nordrhein-westfalen','Nordrhein-Westfalen'),
        'RP':('rheinland-pfalz','Rheinland-Pfalz'), 'SL':('saarland','Saarland'),
        'SN':('sachsen','Sachsen'), 'ST':('sachsen-anhalt','Sachsen-Anhalt'),
        'SH':('schleswig-holstein','Schleswig-Holstein'), 'TH':('thueringen','Thueringen')}
EXC = {'Frankfurt am Main':'frankfurt', 'Freiburg im Breisgau':'freiburg', 'Halle (Saale)':'halle',
       'Ludwigshafen am Rhein':'ludwigshafen', 'Muelheim an der Ruhr':'muelheim'}

EXCS = None  # wird nach slug() befuellt

def slug(s):
    t = s.lower()
    for a, b in (('ä','ae'), ('ö','oe'), ('ü','ue'), ('ß','ss')):
        t = t.replace(a, b)
    return re.sub(r'[^a-z]', '', t)

EXCS = {}
for _full, _sl in EXC.items():
    EXCS[slug(_full)] = _sl

def short(name):
    # Anzeigename kuerzen: "Frankfurt am Main" -> "Frankfurt"
    for full, sl in EXC.items():
        if slug(name) == slug(full):
            return name.split(' am ')[0].split(' im ')[0].split(' (')[0]
    return name

by = {}
for c in reg['staedte']:
    key = c['bundesland']
    if key not in LAND:
        raise SystemExit('unbekanntes Bundesland-Kuerzel: ' + key)
    land_slug = LAND[key][0]
    sl = EXCS.get(slug(c['stadt']), slug(c['stadt']))
    if not os.path.isdir('friedhoefe/' + sl):
        raise SystemExit('keine Friedhofs-Seite fuer ' + c['stadt'] + ' (' + sl + ')')
    by.setdefault(land_slug, []).append((short(c['stadt']), sl))

done, errs, links_total = [], [], 0
for land_slug, staedte in sorted(by.items()):
    p = 'bestattung-in/%s/index.html' % land_slug
    if not os.path.isfile(p):
        errs.append('Seite fehlt: ' + p); continue
    s = io.open(p, encoding='utf-8').read()
    if 'mr-bl-friedhoefe' in s:
        continue  # idempotent
    staedte = sorted(set(staedte))
    links = ', '.join('<a href="/friedhoefe/%s/">%s</a>' % (sl, nm) for nm, sl in staedte)
    land_name = LAND[[k for k, v in LAND.items() if v[0] == land_slug][0]][1].replace('ue','ü') \
        if land_slug == 'baden-wuerttemberg' else \
        [v[1] for v in LAND.values() if v[0] == land_slug][0]
    para = ('\n<p class="mr-bl-friedhoefe">Friedhofsgebühren aus der amtlichen Satzung, '
            'mit Paragraf und Stand — für %s: %s. '
            'Übersicht aller Städte: <a href="/friedhoefe/">Friedhofsgebühren im Vergleich</a>.</p>\n'
            % (land_name, links))
    if s.count('</main>') != 1:
        errs.append(p + ': </main> nicht eindeutig'); continue
    new = s.replace('</main>', para + '</main>')
    # Asserts vor Write
    if new.count('mr-bl-friedhoefe') != 1:
        errs.append(p + ': Absatz nicht eindeutig'); continue
    if new.count('href="/friedhoefe/') != len(staedte) + 1:
        errs.append(p + ': Linkzahl unerwartet'); continue
    if len(new) <= len(s):
        errs.append(p + ': nicht gewachsen'); continue
    io.open(p, 'w', encoding='utf-8').write(new)
    done.append((land_slug, len(staedte)))
    links_total += len(staedte) + 1

print('Bundesland-Seiten ergaenzt: %d | neue interne Links: %d | Fehler: %d'
      % (len(done), links_total, len(errs)))
for l, n in done:
    print('   %-26s %d Staedte' % (l, n))
for e in errs:
    print('   ERR', e)
