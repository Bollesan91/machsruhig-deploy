#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welle 6 (2026-06-10) — Helper-V3-R5-Findings (NO-GO 72, "ein Satz"):
K1/K2 Lead auf Muenchen/Berlin (beide 20J, aus der verlinkten Kalibriertabelle,
      modellkonsistent: Bayern = teuerstes Land; loest Mainz-vs-Index-96-Widerspruch) |
M3 Rundung 50 -> 100 EUR (von R4+R5 unabhaengig gefordert; Tabelle/CSV/SVGs regeneriert,
   Methodik-Konvention angepasst; Index/Spread unveraendert da vor Rundung berechnet) |
M4 "Erfurt teurer als Schnitt" gestrichen (Index 100 ~ Mittel 100,4) |
K6 Grabpflege-Hinweis an der Tabelle | K8 Zitiervorschlag im Presse-Block.
"""
import io, sys

V2 = [('Bayern', 'München', 1.76), ('Nordrhein-Westfalen', 'Düsseldorf', 1.36),
      ('Saarland', 'Saarbrücken', 1.24), ('Sachsen-Anhalt', 'Magdeburg', 1.15),
      ('Baden-Württemberg', 'Stuttgart', 1.13), ('Niedersachsen', 'Hannover', 1.13),
      ('Hamburg', 'Hamburg', 1.12), ('Hessen', 'Wiesbaden', 1.05),
      ('Thüringen', 'Erfurt', 0.99), ('Bremen', 'Bremen', 0.94),
      ('Mecklenburg-Vorpommern', 'Schwerin', 0.91), ('Rheinland-Pfalz', 'Mainz', 0.91),
      ('Schleswig-Holstein', 'Kiel', 0.70), ('Brandenburg', 'Potsdam', 0.68),
      ('Sachsen', 'Dresden', 0.60), ('Berlin', 'Berlin', 0.48)]
SLUG = {'Bayern': 'bayern', 'Baden-Württemberg': 'baden-wuerttemberg', 'Hamburg': 'hamburg',
        'Berlin': 'berlin', 'Hessen': 'hessen', 'Bremen': 'bremen',
        'Nordrhein-Westfalen': 'nordrhein-westfalen', 'Niedersachsen': 'niedersachsen',
        'Rheinland-Pfalz': 'rheinland-pfalz', 'Schleswig-Holstein': 'schleswig-holstein',
        'Saarland': 'saarland', 'Sachsen': 'sachsen', 'Brandenburg': 'brandenburg',
        'Thüringen': 'thueringen', 'Mecklenburg-Vorpommern': 'mecklenburg-vorpommern',
        'Sachsen-Anhalt': 'sachsen-anhalt'}
ERD_CONST = (2800, 5700); ERD_LOCAL = (2500, 8600)
FEUER_CONST = (2830, 6100); FEUER_LOCAL = (950, 3600)

def r100(x):
    # round half to even auf 100er (Python-round)
    return int(round(x / 100.0)) * 100

def de(n): return '{:,}'.format(n).replace(',', '.')

mid1 = ((FEUER_CONST[0] + FEUER_LOCAL[0] + FEUER_CONST[1] + FEUER_LOCAL[1]) / 2.0 +
        (ERD_CONST[0] + ERD_LOCAL[0] + ERD_CONST[1] + ERD_LOCAL[1]) / 2.0) / 2.0
rows = []
for bl, stadt, f in V2:
    fe = (r100(FEUER_CONST[0] + FEUER_LOCAL[0] * f), r100(FEUER_CONST[1] + FEUER_LOCAL[1] * f))
    er = (r100(ERD_CONST[0] + ERD_LOCAL[0] * f), r100(ERD_CONST[1] + ERD_LOCAL[1] * f))
    mid = ((FEUER_CONST[0] + FEUER_LOCAL[0] * f + FEUER_CONST[1] + FEUER_LOCAL[1] * f) / 2.0 +
           (ERD_CONST[0] + ERD_LOCAL[0] * f + ERD_CONST[1] + ERD_LOCAL[1] * f) / 2.0) / 2.0
    rows.append({'bl': bl, 'stadt': stadt, 'f': f, 'idx': int(round(mid / mid1 * 100)),
                 'fe': fe, 'er': er})
rows.sort(key=lambda r: (-r['idx'], r['bl']))
assert rows[0]['idx'] == 136 and rows[-1]['idx'] == 75

def patch(path, replacements):
    with io.open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()
    for i, (old, new, expect) in enumerate(replacements):
        c = text.count(old)
        if c != expect:
            print('FATAL #%d: %r -> %d (erwartet %d) in %s' % (i, old[:70], c, expect, path)); sys.exit(1)
        text = text.replace(old, new)
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)
    print('%s: %d OK' % (path, len(replacements)))

def splice(path, start_marker, end_marker, new_block, label):
    with io.open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()
    i = text.find(start_marker)
    j = text.find(end_marker, i)
    if i < 0 or j < 0 or text.count(start_marker) != 1:
        print('FATAL splice %s' % label); sys.exit(1)
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text[:i] + new_block + text[j + len(end_marker):])
    print('splice %s OK' % label)

PAGE = 'bestattungskosten-nach-bundesland.html'

def idx_cls(i): return 'bl-hi' if i >= 110 else ('bl-lo' if i <= 86 else 'bl-mid')

tb = []
for r in rows:
    tb.append('        <tr><td><a href="/bestattung-in/%s/">%s</a></td><td><span class="bl-idx %s">%d</span></td><td class="num">%s–%s €</td><td class="num">%s–%s €</td></tr>' % (
        SLUG[r['bl']], r['bl'], idx_cls(r['idx']), r['idx'],
        de(r['fe'][0]), de(r['fe'][1]), de(r['er'][0]), de(r['er'][1])))
splice(PAGE, '<tbody>', '</tbody>', '<tbody>\n' + '\n'.join(tb) + '\n      </tbody>', 'tbody')

maxidx = float(rows[0]['idx'])
svg_rows = []
for i, r in enumerate(rows):
    y = 8 + i * 28
    w = int(round(r['idx'] / maxidx * 380))
    svg_rows.append('<text x="186" y="%d" text-anchor="end" font-size="13" fill="var(--mr-text,#2e2620)">%s</text>'
                    '<rect x="194" y="%d" width="%d" height="16" rx="3" fill="var(--mr-primary,#8a7355)"/>'
                    '<text x="%d" y="%d" font-size="13" font-weight="700" fill="var(--mr-text,#2e2620)">%d</text>'
                    % (y + 13, r['bl'], y, w, 194 + w + 8, y + 13, r['idx']))
FIGURE = ('<figure style="margin:28px 0 8px">\n'
          '      <svg viewBox="0 0 660 460" role="img" aria-label="Balkendiagramm: Kostenniveau-Index der 16 Bundesländer, von Bayern (136) bis Berlin (75)" style="width:100%;height:auto;font-family:inherit">\n'
          '        ' + '\n        '.join(svg_rows) + '\n'
          '      </svg>\n'
          '      <figcaption style="font-size:12px;color:var(--mr-text-muted);margin-top:8px">Kostenniveau-Index nach Bundesland (100 = bundesweiter Referenzwert; verankert an den Friedhofsgebühren der Landeshauptstädte, Aeternitas 2025). Eigene Modellrechnung machsruhig.de, Stand Juni 2026 — Grafik frei verwendbar mit Quellenangabe.</figcaption>\n'
          '    </figure>')
splice(PAGE, '<figure style="margin:28px 0 8px">', '</figure>', FIGURE, 'figure')

patch(PAGE, [
    # --- K1/K2: Lead auf Muenchen/Berlin, gleichbasig, scoped Attribution ---
    ('Wo eine Bestattung wie viel kostet, entscheidet vor allem die kommunale Friedhofssatzung: Beim Sargwahlgrab verlangt die teuerste Großstadt (Mainz, 4.759 € für 30 Jahre) laut Aeternitas fast das Fünffache der günstigsten (Berlin, 964 € für 20 Jahre).',
     'Wo eine Bestattung wie viel kostet, entscheidet vor allem die kommunale Friedhofssatzung: Im auf 20 Jahre vereinheitlichten Vergleich der Landeshauptstädte (Datengrundlage Aeternitas) verlangt die teuerste — München, 4.578 € fürs Sargwahlgrab — fast das Fünffache der günstigsten (Berlin, 964 €).', 1),
    # --- M4: Erfurt-Beispiel streichen ---
    ('aber auch Magdeburg und Erfurt sind teurer als der Schnitt',
     'aber auch Magdeburg liegt über dem Schnitt', 1),
    # --- K6: Grabpflege-Hinweis an der Tabelle ---
    ('Modellierte Kostenspannen (Standard-Szenario, inkl. Grabpflege) — Index verankert an Landeshauptstadt-Gebühren (Aeternitas 2025), keine erhobenen Marktpreise.',
     'Modellierte Kostenspannen (Standard-Szenario) — Index verankert an Landeshauptstadt-Gebühren (Aeternitas 2025), keine erhobenen Marktpreise. Obergrenzen enthalten die volle Grabpflege über die Ruhezeit (Erd ~20, Feuer ~10 Jahre).', 1),
    # --- K8: Zitiervorschlag im Presse-Block ---
    ('Rückfragen: Marie-Therese Bollweg (Betreiberin),',
     'Zitiervorschlag: „Bestattungskosten-Index nach Bundesland 2026, machsruhig.de“ · Rückfragen: Marie-Therese Bollweg (Betreiberin),', 1),
])

# CSV (100er-Rundung)
csv_lines = ['Bundesland;Anker_Landeshauptstadt;Friedhofs_Faktor;Index;Feuerbestattung_min_EUR;Feuerbestattung_max_EUR;Erdbestattung_min_EUR;Erdbestattung_max_EUR']
for r in rows:
    csv_lines.append('%s;%s;%.2f;%d;%d;%d;%d;%d' % (
        r['bl'], r['stadt'], r['f'], r['idx'], r['fe'][0], r['fe'][1], r['er'][0], r['er'][1]))
with io.open('assets/data/bestattungskosten-index-2026.csv', 'w', encoding='utf-8', newline='') as fh:
    fh.write('\n'.join(csv_lines) + '\n')
print('CSV OK')

# Standalone-SVG (100er-Rundung irrelevant fuer Index, aber Konsistenz: regenerieren)
bars = []
for i, r in enumerate(rows):
    y = 70 + i * 28
    w = int(round(r['idx'] / maxidx * 380))
    bars.append('<text x="206" y="%d" text-anchor="end" font-size="13" fill="#2e2620">%s</text>'
                '<rect x="214" y="%d" width="%d" height="16" rx="3" fill="#8a7355"/>'
                '<text x="%d" y="%d" font-size="13" font-weight="700" fill="#2e2620">%d</text>'
                % (y + 13, r['bl'], y, w, 214 + w + 8, y + 13, r['idx']))
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 580" font-family="Arial, Helvetica, sans-serif">\n'
       '<rect width="700" height="580" fill="#faf7f2"/>\n'
       '<text x="20" y="32" font-size="18" font-weight="700" fill="#2e2620">Bestattungskosten-Index nach Bundesland (2026)</text>\n'
       '<text x="20" y="52" font-size="12" fill="#5e5047">100 = bundesweiter Referenzwert · verankert an den Friedhofsgebühren der Landeshauptstädte (Aeternitas 2025)</text>\n'
       + '\n'.join(bars) + '\n'
       '<text x="20" y="562" font-size="11" fill="#5e5047">Modellrechnung machsruhig.de/bestattungskosten-nach-bundesland · keine erhobenen Marktpreise · frei verwendbar mit Quellenangabe (CC BY 4.0)</text>\n'
       '</svg>\n')
with io.open('assets/data/bestattungskosten-index-2026.svg', 'w', encoding='utf-8', newline='') as fh:
    fh.write(svg)
print('SVG OK')

# Methodik: Rundungskonvention
patch('methodik.html', [
    ('die Summen werden auf 50 € gerundet (kaufmännisch mit round half to even).',
     'die Summen werden auf 100 € gerundet (round half to even) — bewusst grob, weil es Modellgrößen sind, keine erhobenen Preise.', 1),
])
print('FERTIG — Werte auf 100 € gerundet, Lead München/Berlin, Erfurt raus')
