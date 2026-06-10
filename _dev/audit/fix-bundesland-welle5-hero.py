#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welle 5 (2026-06-10) — Helper-V3-R4-Findings ("Substanz GO, Verpackung NO-GO"):
K1 Hero quellen-treu: PM-Originalaussage (Mainz teuerste / Berlin guenstigste
   Grossstadt beim Sargwahlgrab) statt eigener Normierung "laut Aeternitas" |
M2 Grabpflege-Skalierungs-Annahme offengelegt (Methodik + Seiten-Hinweis) |
M3 PM direkt verlinkt | M4 Datierung praezise (PM 04.06.2025) statt "01/2025" |
K5 Rundungskonvention benannt (round half to even) | K6 Index-Formel explizit |
K7 "sechs der dokumentierten Grabarten" | Presse: Standalone-SVG + Methodik-Einzeiler.
"""
import io, sys

PM_URL = 'https://www.aeternitas.de/verein/presse/pressemitteilungen/detail/friedhofsgebuehren-aller-grossstaedte-im-vergleich'
C24_URL = 'https://www.check24.de/sterbegeldversicherung/friedhofsgebuehren-deutschland/'

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

PAGE = 'bestattungskosten-nach-bundesland.html'
patch(PAGE, [
    # --- K1: Hero quellen-treu (PM-Originalvergleich, Ruhezeiten offen) ---
    ('Eine Bestattung kostet in München deutlich mehr als in Berlin — für ein Sargwahlgrab verlangt München laut Aeternitas fast das Fünffache der Berliner Gebühren. Der Treiber sind die kommunalen Friedhofsgebühren, nicht der Sarg. Hier siehst du, wie sich das Kostenniveau über alle 16 Bundesländer verteilt — als modellierte Spanne, verankert an den realen Friedhofsgebühren der Landeshauptstädte.',
     'Wo eine Bestattung wie viel kostet, entscheidet vor allem die kommunale Friedhofssatzung: Beim Sargwahlgrab verlangt die teuerste Großstadt (Mainz, 4.759 € für 30 Jahre) laut Aeternitas fast das Fünffache der günstigsten (Berlin, 964 € für 20 Jahre). Hier siehst du, wie sich das Kostenniveau über alle 16 Bundesländer verteilt — als modellierte Spanne, verankert an den auf 20 Jahre vereinheitlichten Friedhofsgebühren der Landeshauptstädte.', 1),
    # --- M4: Datierung entschaerfen (Reihenfolge: laengere Strings zuerst) ---
    ('Datengrundlage Aeternitas e. V. (Stand 01/2025, vereinheitlicht auf 20 Jahre Nutzungszeit), öffentlich dokumentiert in <a href="' + C24_URL + '" target="_blank" rel="noopener" style="color:var(--mr-primary)">dieser Übersicht</a>',
     'Datengrundlage Aeternitas e. V. (Großstadtvergleich, veröffentlicht 04.06.2025 — <a href="' + PM_URL + '" target="_blank" rel="noopener" style="color:var(--mr-primary)">Pressemitteilung</a>); auf 20 Jahre Nutzungszeit vereinheitlichte Werte nach <a href="' + C24_URL + '" target="_blank" rel="noopener" style="color:var(--mr-primary)">dieser Aufbereitung</a>', 1),
    ('(Aeternitas e.V., Stand 01/2025)', '(Aeternitas e.V. 2025)', 1),
    (', Stand 01/2025)', ' 2025)', 6),
    (' 01/2025)', ' 2025)', 3),
    # --- M2: Grabpflege-Skalierung auf Seite offenlegen ---
    ('für die Feuerbestattung rund 10 Jahre (400–1.500 €).',
     'für die Feuerbestattung rund 10 Jahre (400–1.500 € im Basis-Szenario; im Modell annahmegemäß mit dem Regionalfaktor skaliert).', 1),
    # --- Presse-Block: SVG-Download + Methodik-Einzeiler ---
    ('<a href="/assets/data/bestattungskosten-index-2026.csv" style="color:var(--mr-primary)" download>Rohdaten als CSV</a>',
     '<a href="/assets/data/bestattungskosten-index-2026.csv" style="color:var(--mr-primary)" download>Rohdaten als CSV</a> · <a href="/assets/data/bestattungskosten-index-2026.svg" style="color:var(--mr-primary)" download>Grafik als SVG</a>', 1),
    ('Rückfragen: Marie-Therese Bollweg (Betreiberin), <a href="mailto:kontakt@machsruhig.de" style="color:var(--mr-primary)">kontakt@machsruhig.de</a>',
     'Rückfragen: Marie-Therese Bollweg (Betreiberin), <a href="mailto:kontakt@machsruhig.de" style="color:var(--mr-primary)">kontakt@machsruhig.de</a><br><span style="font-size:12px;color:var(--mr-text-muted)">Methodik in einem Satz: Modellrechnung von machsruhig.de — bundesweites Komponenten-Szenario, regional skaliert über die auf 20 Jahre vereinheitlichten Friedhofsgebühren der Landeshauptstädte (Aeternitas 2025, sechs Grabarten); keine erhobenen Marktpreise.</span>', 1),
    # --- Dataset: SVG als zweite distribution ---
    ('"distribution":{"@type":"DataDownload","encodingFormat":"text/csv","contentUrl":"https://machsruhig.de/assets/data/bestattungskosten-index-2026.csv"}',
     '"distribution":[{"@type":"DataDownload","encodingFormat":"text/csv","contentUrl":"https://machsruhig.de/assets/data/bestattungskosten-index-2026.csv"},{"@type":"DataDownload","encodingFormat":"image/svg+xml","contentUrl":"https://machsruhig.de/assets/data/bestattungskosten-index-2026.svg"}]', 1),
])

patch('methodik.html', [
    # K7 + M3 + M4: Grabarten-Zahl, PM-Link, Datierung
    ('Grundlage sind die von der Aeternitas e. V. erhobenen Gebühren für sechs Grabarten (Stand 01/2025, auf 20 Jahre Nutzungszeit vereinheitlicht, öffentlich dokumentiert in <a href="' + C24_URL + '" target="_blank" rel="noopener" style="color:var(--mr-primary)">dieser Übersicht</a>)',
     'Grundlage sind die von der Aeternitas e. V. erhobenen Gebühren für sechs der dort dokumentierten Grabarten (Großstadtvergleich, veröffentlicht am 04.06.2025 — <a href="' + PM_URL + '" target="_blank" rel="noopener" style="color:var(--mr-primary)">Pressemitteilung</a>; auf 20 Jahre Nutzungszeit vereinheitlichte Tabelle nach <a href="' + C24_URL + '" target="_blank" rel="noopener" style="color:var(--mr-primary)">dieser Aufbereitung</a>)', 1),
    # K6: Index-Formel explizit
    ('Der <strong>Index</strong> der Vergleichsseite ist das Verhältnis der Szenario-Mittelwerte zum Basis-Szenario mal 100; der Mittelwert der 16 Länderwerte liegt bei rund 100.',
     'Der <strong>Index</strong> der Vergleichsseite ist der Mittelwert der Spannen-Mittelpunkte beider Bestattungsarten (Feuer- und Erdbestattung gleich gewichtet), geteilt durch denselben Wert des Basis-Szenarios, mal 100; der Mittelwert der 16 Länderwerte liegt bei rund 100.', 1),
    # K5: Rundungskonvention
    ('die Summen werden auf 50 € gerundet.',
     'die Summen werden auf 50 € gerundet (kaufmännisch mit round half to even).', 1),
    # M2: Grabpflege-Annahme offenlegen
    ('Bestatterleistungen und Sarg-Preise setzen wir bundesweit konstant an — real streuen auch sie etwas, aber deutlich weniger als die Gebühren.',
     'Bestatterleistungen und Sarg-Preise setzen wir bundesweit konstant an — real streuen auch sie etwas, aber deutlich weniger als die Gebühren. Die Grabpflege skalieren wir annahmegemäß mit demselben Faktor wie die Grabgebühren; real hängt sie eher an Gärtner- und Pflanzkosten, die weniger streuen — die Obergrenzen teurer Länder sind dadurch eher konservativ hoch angesetzt.', 1),
    # Faktor-Tabellen-Caption Datierung
    ('Anker: Friedhofsgebühren der Landeshauptstadt (Aeternitas e. V., Stand 01/2025, auf 20 Jahre Nutzungszeit vereinheitlicht).',
     'Anker: Friedhofsgebühren der Landeshauptstadt (Aeternitas e. V. 2025, auf 20 Jahre Nutzungszeit vereinheitlicht).', 1),
    ('(Stiftung Warentest 2023, BDB, Aeternitas e. V., Verbraucherzentralen).',
     '(Stiftung Warentest 2023, BDB, Aeternitas e. V., Verbraucherzentralen).', 1),
])

# Kostenrechner-Kommentar Datierung
patch('tools/bestattungskosten-rechner/index.html', [
    ('(Aeternitas e.V., Stand 01/2025,', '(Aeternitas e.V. 2025,', 1),
])

# ===== Standalone-SVG (Presse-Download) =====
V2 = [('Bayern', 1.76), ('Nordrhein-Westfalen', 1.36), ('Saarland', 1.24),
      ('Sachsen-Anhalt', 1.15), ('Baden-Württemberg', 1.13), ('Niedersachsen', 1.13),
      ('Hamburg', 1.12), ('Hessen', 1.05), ('Thüringen', 0.99), ('Bremen', 0.94),
      ('Mecklenburg-Vorpommern', 0.91), ('Rheinland-Pfalz', 0.91),
      ('Schleswig-Holstein', 0.70), ('Brandenburg', 0.68), ('Sachsen', 0.60), ('Berlin', 0.48)]
ERD_CONST = (2800, 5700); ERD_LOCAL = (2500, 8600)
FEUER_CONST = (2830, 6100); FEUER_LOCAL = (950, 3600)
mid1 = ((FEUER_CONST[0] + FEUER_LOCAL[0] + FEUER_CONST[1] + FEUER_LOCAL[1]) / 2.0 +
        (ERD_CONST[0] + ERD_LOCAL[0] + ERD_CONST[1] + ERD_LOCAL[1]) / 2.0) / 2.0
items = []
for bl, f in V2:
    mid = ((FEUER_CONST[0] + FEUER_LOCAL[0] * f + FEUER_CONST[1] + FEUER_LOCAL[1] * f) / 2.0 +
           (ERD_CONST[0] + ERD_LOCAL[0] * f + ERD_CONST[1] + ERD_LOCAL[1] * f) / 2.0) / 2.0
    items.append((bl, int(round(mid / mid1 * 100))))
items.sort(key=lambda x: (-x[1], x[0]))
maxidx = float(items[0][1])
bars = []
for i, (bl, idx) in enumerate(items):
    y = 70 + i * 28
    w = int(round(idx / maxidx * 380))
    bars.append('<text x="206" y="%d" text-anchor="end" font-size="13" fill="#2e2620">%s</text>'
                '<rect x="214" y="%d" width="%d" height="16" rx="3" fill="#8a7355"/>'
                '<text x="%d" y="%d" font-size="13" font-weight="700" fill="#2e2620">%d</text>'
                % (y + 13, bl, y, w, 214 + w + 8, y + 13, idx))
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 580" font-family="Arial, Helvetica, sans-serif">\n'
       '<rect width="700" height="580" fill="#faf7f2"/>\n'
       '<text x="20" y="32" font-size="18" font-weight="700" fill="#2e2620">Bestattungskosten-Index nach Bundesland (2026)</text>\n'
       '<text x="20" y="52" font-size="12" fill="#5e5047">100 = bundesweiter Referenzwert · verankert an den Friedhofsgebühren der Landeshauptstädte (Aeternitas 2025)</text>\n'
       + '\n'.join(bars) + '\n'
       '<text x="20" y="562" font-size="11" fill="#5e5047">Modellrechnung machsruhig.de/bestattungskosten-nach-bundesland · keine erhobenen Marktpreise · frei verwendbar mit Quellenangabe (CC BY 4.0)</text>\n'
       '</svg>\n')
with io.open('assets/data/bestattungskosten-index-2026.svg', 'w', encoding='utf-8', newline='') as fh:
    fh.write(svg)
print('SVG geschrieben (%d Balken)' % len(items))
print('FERTIG')
