#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modell V2 (2026-06-10) — Herleitung des regionalen Kostenniveaus, kalibriert an
realen Friedhofsgebuehren statt redaktioneller Schaetzung (Helper-V3-R3-Befunde
1+2: Berlin-Paradox, 56%-Spread durch Einheitsfaktor aufgeblaeht).

DATENBASIS (verifiziert 10.06.2026):
  Aeternitas e.V., Friedhofsgebuehren der 16 Landeshauptstaedte, Stand 01/2025,
  vereinheitlicht auf 20 Jahre Nutzungszeit. Abgerufen ueber:
  https://www.check24.de/sterbegeldversicherung/friedhofsgebuehren-deutschland/
  (Primaerquelle: https://www.aeternitas.de/ Gebuehrendatenbank; PM:
  https://www.aeternitas.de/verein/presse/pressemitteilungen/detail/friedhofsgebuehren-aller-grossstaedte-im-vergleich)

METHODE:
  1. Je Stadt 6 Grabarten-Gebuehren (k.A. = fehlend). Jede Spalte wird auf ihren
     Spaltenmittelwert normiert (Skalenunterschiede der Grabarten), dann je Stadt
     der Mittelwert der verfuegbaren normierten Werte = Friedhofs-Faktor.
  2. Der Faktor skaliert NUR die ortsgebundenen Posten (Friedhofsgebuehren,
     Beisetzung, Grabpflege). Bestatterleistungen, Sarg/Urne, Einaescherung,
     Leichenschau bleiben bundesweit konstant (eigene Aussage der Seite:
     "weniger regional gespreizt").
  3. Index = Mittelwert der Szenario-Mittelpunkte (Feuer+Erd) bei Faktor f
     relativ zu Faktor 1,0, mal 100. Spannen auf 50 EUR gerundet.

EHRLICHE GRENZE: Anker ist die Landeshauptstadt, nicht der Landesdurchschnitt —
wird auf Seite + Methodik explizit benannt.
"""
import io, os, json

# Aeternitas 01/2025 via CHECK24: Sargwahl, Baum, Sargreihe, Urnenwahl, Urnenreihe, Urne anonym
CITY_FEES = {
    # BL: (Landeshauptstadt, [6 Gebuehren, None=k.A.])
    'Berlin':                 ('Berlin',      [964, 1462, 887, 776, 746, 652]),
    'Bremen':                 ('Bremen',      [2408, 2243, 2276, 1526, 1390, 1043]),
    'Sachsen':                ('Dresden',     [1637, 1109, 1493, 933, 976, 725]),
    'Nordrhein-Westfalen':    ('Düsseldorf',  [3301, 3369, 2492, 2442, 1955, 1947]),
    'Thüringen':              ('Erfurt',      [2810, 2783, 2682, 1224, 1139, 1196]),
    'Hamburg':                ('Hamburg',     [2995, 2695, 2279, 2115, 1539, 1335]),
    'Niedersachsen':          ('Hannover',    [3398, 2594, 2223, 2065, 1608, 1292]),
    'Schleswig-Holstein':     ('Kiel',        [1865, 780, 1865, 1385, 1205, 830]),
    'Sachsen-Anhalt':         ('Magdeburg',   [2804, 3372, 2610, 1546, 1398, 1683]),
    'Rheinland-Pfalz':        ('Mainz',       [3798, 1293, 2389, 1647, 1112, 841]),
    'Bayern':                 ('München',     [4578, 4161, None, 3001, None, 2468]),
    'Mecklenburg-Vorpommern': ('Schwerin',    [2537, 2188, 2537, 1260, 1121, 1089]),
    'Brandenburg':            ('Potsdam',     [1649, None, 1653, 1033, 997, None]),
    'Saarland':               ('Saarbrücken', [2675, 2900, 2555, 1860, 1820, 2073]),
    'Baden-Württemberg':      ('Stuttgart',   [3527, 2980, 2427, 2420, 1320, 960]),
    'Hessen':                 ('Wiesbaden',   [3583, 1581, 2114, 2176, 1328, 1373]),
}

# Spaltenmittel (nur vorhandene Werte)
ncols = 6
col_means = []
for c in range(ncols):
    vals = [v[1][c] for v in CITY_FEES.values() if v[1][c] is not None]
    col_means.append(sum(vals) / len(vals))

factors = {}
for bl, (stadt, fees) in CITY_FEES.items():
    norm = [fees[c] / col_means[c] for c in range(ncols) if fees[c] is not None]
    factors[bl] = sum(norm) / len(norm)

# Szenario-Komponenten (aus Kostenrechner, Standard-Szenario):
# Erd:   konstant: bestatter 2000-3500 + sarg 800-2200            = 2800-5700
#        ortsgebunden: friedhof 600-2800 + beisetzung 300-800 + grabpflege 1600-5000 = 2500-8600
# Feuer: konstant: bestatter 1800-3200 + sarg 600-1800 + einaesch 300-550
#        + leichenschau 50-150 + urne 80-400                       = 2830-6100
#        ortsgebunden: friedhof_urne 300-1500 + beisetzung 250-600 + grabpflege 400-1500 = 950-3600
ERD_CONST = (2800, 5700); ERD_LOCAL = (2500, 8600)
FEUER_CONST = (2830, 6100); FEUER_LOCAL = (950, 3600)

def r50(x):
    return int(round(x / 50.0)) * 50

def scenario(f):
    fe = (FEUER_CONST[0] + FEUER_LOCAL[0] * f, FEUER_CONST[1] + FEUER_LOCAL[1] * f)
    er = (ERD_CONST[0] + ERD_LOCAL[0] * f, ERD_CONST[1] + ERD_LOCAL[1] * f)
    return fe, er

fe1, er1 = scenario(1.0)
mid1 = (sum(fe1) / 2 + sum(er1) / 2) / 2

rows = []
for bl, f in factors.items():
    fe, er = scenario(f)
    mid = (sum(fe) / 2 + sum(er) / 2) / 2
    idx = round(mid / mid1 * 100)
    rows.append({
        'bl': bl, 'stadt': CITY_FEES[bl][0], 'faktor': round(f, 2), 'index': idx,
        'feuer': (r50(fe[0]), r50(fe[1])), 'erd': (r50(er[0]), r50(er[1])),
    })
rows.sort(key=lambda r: (-r['index'], r['bl']))

print('%-24s %-12s %6s %5s  %-15s %-15s' % ('Bundesland', 'Anker', 'Faktor', 'Index', 'Feuer', 'Erd'))
for r in rows:
    print('%-24s %-12s %6.2f %5d  %5d-%-8d %5d-%-8d' % (
        r['bl'], r['stadt'], r['faktor'], r['index'],
        r['feuer'][0], r['feuer'][1], r['erd'][0], r['erd'][1]))

mx, mn = rows[0], rows[-1]
print('\nSpread Index: %d vs %d -> teuerstes %.0f%% ueber guenstigstem' % (
    mx['index'], mn['index'], (mx['index'] / mn['index'] - 1) * 100))
print('Mittelwert Index: %.1f' % (sum(r['index'] for r in rows) / 16.0))

# Artefakte fuer die Folge-Patches
out = {
    'factors': {r['bl']: r['faktor'] for r in rows},
    'rows': rows,
    'spread_pct': round((mx['index'] / mn['index'] - 1) * 100),
    'basis_feuer': [r50(v) for v in fe1], 'basis_erd': [r50(v) for v in er1],
}
here = os.path.dirname(os.path.abspath(__file__))
with io.open(os.path.join(here, 'bundesland-modell-v2.json'), 'w', encoding='utf-8') as fjson:
    fjson.write(json.dumps(out, ensure_ascii=False, indent=1))
print('\nJSON geschrieben: bundesland-modell-v2.json')
