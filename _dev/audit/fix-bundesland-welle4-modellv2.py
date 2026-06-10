#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welle 4 (2026-06-10) — Modell V2 ausrollen (User-Entscheid: gruendliche Rekalibrierung).
Herleitung: _dev/audit/bundesland-modell-v2.py (Aeternitas-Landeshauptstadt-Gebuehren 01/2025).
KANONISCH sind die auf 2 Dezimalen gerundeten Faktoren — alle veroeffentlichten
Zahlen (Index, Spannen, CSV, Kostenrechner) werden hier daraus berechnet,
damit die publizierte Faktor-Tabelle die Werte exakt reproduziert.
Aenderungen: Kostenrechner-JS (Faktor nur ortsgebundene Posten) + BL-Seite
(Tabelle/SVG/Keyfacts/FAQ/JSON-LD/CSV/Prosa) + Methodik (Faktor-Tabelle, Quellen).
"""
import io, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
os.chdir(ROOT)

# ===== Kanonische V2-Faktoren (2 Dezimalen) + Anker-Staedte =====
V2 = [
    ('Bayern', 'München', 1.76), ('Nordrhein-Westfalen', 'Düsseldorf', 1.36),
    ('Saarland', 'Saarbrücken', 1.24), ('Sachsen-Anhalt', 'Magdeburg', 1.15),
    ('Baden-Württemberg', 'Stuttgart', 1.13), ('Niedersachsen', 'Hannover', 1.13),
    ('Hamburg', 'Hamburg', 1.12), ('Hessen', 'Wiesbaden', 1.05),
    ('Thüringen', 'Erfurt', 0.99), ('Bremen', 'Bremen', 0.94),
    ('Mecklenburg-Vorpommern', 'Schwerin', 0.91), ('Rheinland-Pfalz', 'Mainz', 0.91),
    ('Schleswig-Holstein', 'Kiel', 0.70), ('Brandenburg', 'Potsdam', 0.68),
    ('Sachsen', 'Dresden', 0.60), ('Berlin', 'Berlin', 0.48),
]
SLUG = {
    'Bayern': 'bayern', 'Baden-Württemberg': 'baden-wuerttemberg', 'Hamburg': 'hamburg',
    'Berlin': 'berlin', 'Hessen': 'hessen', 'Bremen': 'bremen',
    'Nordrhein-Westfalen': 'nordrhein-westfalen', 'Niedersachsen': 'niedersachsen',
    'Rheinland-Pfalz': 'rheinland-pfalz', 'Schleswig-Holstein': 'schleswig-holstein',
    'Saarland': 'saarland', 'Sachsen': 'sachsen', 'Brandenburg': 'brandenburg',
    'Thüringen': 'thueringen', 'Mecklenburg-Vorpommern': 'mecklenburg-vorpommern',
    'Sachsen-Anhalt': 'sachsen-anhalt',
}
ERD_CONST = (2800, 5700); ERD_LOCAL = (2500, 8600)
FEUER_CONST = (2830, 6100); FEUER_LOCAL = (950, 3600)

def r50(x): return int(round(x / 50.0)) * 50
def de(n): return '{:,}'.format(n).replace(',', '.')

rows = []
mid1 = ((FEUER_CONST[0] + FEUER_LOCAL[0] + FEUER_CONST[1] + FEUER_LOCAL[1]) / 2.0 +
        (ERD_CONST[0] + ERD_LOCAL[0] + ERD_CONST[1] + ERD_LOCAL[1]) / 2.0) / 2.0
for bl, stadt, f in V2:
    fe = (r50(FEUER_CONST[0] + FEUER_LOCAL[0] * f), r50(FEUER_CONST[1] + FEUER_LOCAL[1] * f))
    er = (r50(ERD_CONST[0] + ERD_LOCAL[0] * f), r50(ERD_CONST[1] + ERD_LOCAL[1] * f))
    mid = ((FEUER_CONST[0] + FEUER_LOCAL[0] * f + FEUER_CONST[1] + FEUER_LOCAL[1] * f) / 2.0 +
           (ERD_CONST[0] + ERD_LOCAL[0] * f + ERD_CONST[1] + ERD_LOCAL[1] * f) / 2.0) / 2.0
    rows.append({'bl': bl, 'stadt': stadt, 'f': f, 'idx': int(round(mid / mid1 * 100)),
                 'fe': fe, 'er': er})
rows.sort(key=lambda r: (-r['idx'], r['bl']))

idx_top, idx_low = rows[0]['idx'], rows[-1]['idx']
spread = int(round((float(idx_top) / idx_low - 1) * 100))
mittel = sum(r['idx'] for r in rows) / 16.0
# Plausibilitaets-Anker fuer die Texte unten:
assert rows[0]['bl'] == 'Bayern' and rows[1]['bl'] == 'Nordrhein-Westfalen' and rows[2]['bl'] == 'Saarland', [r['bl'] for r in rows[:3]]
assert rows[-1]['bl'] == 'Berlin' and rows[-2]['bl'] == 'Sachsen' and rows[-3]['bl'] == 'Brandenburg' and rows[-4]['bl'] == 'Schleswig-Holstein'
assert 99.0 <= mittel <= 101.5, mittel
print('Index: %s ... %s | Spread %d%% | Mittel %.1f' % (idx_top, idx_low, spread, mittel))

def idx_cls(i):
    return 'bl-hi' if i >= 110 else ('bl-lo' if i <= 86 else 'bl-mid')

def patch(path, replacements):
    with io.open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()
    for i, (old, new, expect) in enumerate(replacements):
        c = text.count(old)
        if c != expect:
            print('FATAL #%d: %r -> %d Treffer (erwartet %d) in %s' % (i, old[:70], c, expect, path))
            sys.exit(1)
        text = text.replace(old, new)
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)
    print('%s: %d Ersetzungen OK' % (path, len(replacements)))

def splice(path, start_marker, end_marker, new_block, label):
    with io.open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()
    i = text.find(start_marker)
    j = text.find(end_marker, i)
    if i < 0 or j < 0 or text.count(start_marker) != 1:
        print('FATAL splice %s: marker nicht eindeutig (%d/%d)' % (label, i, j)); sys.exit(1)
    text = text[:i] + new_block + text[j + len(end_marker):]
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)
    print('%s: splice %s OK' % (path, label))

PAGE = 'bestattungskosten-nach-bundesland.html'

# ===== Tabelle (tbody) =====
tb = []
for r in rows:
    tb.append('        <tr><td><a href="/bestattung-in/%s/">%s</a></td><td><span class="bl-idx %s">%d</span></td><td class="num">%s–%s €</td><td class="num">%s–%s €</td></tr>' % (
        SLUG[r['bl']], r['bl'], idx_cls(r['idx']), r['idx'],
        de(r['fe'][0]), de(r['fe'][1]), de(r['er'][0]), de(r['er'][1])))
TBODY = '<tbody>\n' + '\n'.join(tb) + '\n      </tbody>'

# ===== SVG =====
maxidx = float(idx_top)
svg_rows = []
for i, r in enumerate(rows):
    y = 8 + i * 28
    w = int(round(r['idx'] / maxidx * 380))
    svg_rows.append(
        '<text x="186" y="%d" text-anchor="end" font-size="13" fill="var(--mr-text,#2e2620)">%s</text>'
        '<rect x="194" y="%d" width="%d" height="16" rx="3" fill="var(--mr-primary,#8a7355)"/>'
        '<text x="%d" y="%d" font-size="13" font-weight="700" fill="var(--mr-text,#2e2620)">%d</text>'
        % (y + 13, r['bl'], y, w, 194 + w + 8, y + 13, r['idx']))
FIGURE = ('<figure style="margin:28px 0 8px">\n'
          '      <svg viewBox="0 0 660 460" role="img" aria-label="Balkendiagramm: Kostenniveau-Index der 16 Bundesländer, von Bayern (%d) bis Berlin (%d)" style="width:100%%;height:auto;font-family:inherit">\n'
          '        %s\n'
          '      </svg>\n'
          '      <figcaption style="font-size:12px;color:var(--mr-text-muted);margin-top:8px">Kostenniveau-Index nach Bundesland (100 = bundesweiter Referenzwert; verankert an den Friedhofsgebühren der Landeshauptstädte, Aeternitas 01/2025). Eigene Modellrechnung machsruhig.de, Stand Juni 2026 — Grafik frei verwendbar mit Quellenangabe.</figcaption>\n'
          '    </figure>' % (idx_top, idx_low, '\n        '.join(svg_rows)))

splice(PAGE, '<tbody>', '</tbody>', TBODY, 'tbody')
splice(PAGE, '<figure style="margin:28px 0 8px">', '</figure>', FIGURE, 'figure')

patch(PAGE, [
    # --- Lead ---
    ('Eine Bestattung kostet in Bayern deutlich mehr als in Mecklenburg-Vorpommern — und das liegt nach übereinstimmender Einschätzung von Aeternitas und Verbraucherzentralen weniger am Sarg als an den kommunalen Friedhofsgebühren. Hier siehst du, wie sich das Kostenniveau über alle 16 Bundesländer verteilt, als modellierte Spanne für ein Standard-Szenario.',
     'Eine Bestattung kostet in München deutlich mehr als in Berlin — für ein Sargwahlgrab verlangt München laut Aeternitas fast das Fünffache der Berliner Gebühren. Der Treiber sind die kommunalen Friedhofsgebühren, nicht der Sarg. Hier siehst du, wie sich das Kostenniveau über alle 16 Bundesländer verteilt — als modellierte Spanne, verankert an den realen Friedhofsgebühren der Landeshauptstädte.', 1),
    # --- Keyfacts ---
    ('<li>Teuerstes Bundesland (Modell): <strong>Bayern</strong> — Index 122</li>',
     '<li>Teuerstes Bundesland (Modell): <strong>Bayern</strong> — Index %d (Anker: München)</li>' % idx_top, 1),
    ('<li>Günstigste Bundesländer (Modell): <strong>Mecklenburg-Vorpommern &amp; Sachsen-Anhalt</strong> — Index 78</li>',
     '<li>Günstigstes Bundesland (Modell): <strong>Berlin</strong> — Index %d</li>' % idx_low, 1),
    ('<li>Teuerstes Land liegt im Modell rund <strong>56 %</strong> über dem günstigsten</li>',
     '<li>Teuerstes Land liegt im Modell rund <strong>%d %%</strong> über dem günstigsten</li>' % spread, 1),
    ('<li>Die Zahlen sind <strong>Modell-Schätzungen</strong>, keine erhobenen Marktpreise</li>',
     '<li>Die Zahlen sind <strong>Modell-Schätzungen</strong>, verankert an Aeternitas-Gebührendaten (Stand 01/2025) — keine erhobenen Marktpreise</li>', 1),
    # --- Tabellen-Intro ---
    ('Der <em>Index</em> zeigt das relative Kostenniveau — 100 ist der Referenzwert des bundesweiten Basis-Szenarios; der ungewichtete Mittelwert der 16 Länderwerte liegt bei rund 99, ein bevölkerungsgewichteter Bundesdurchschnitt läge wegen der großen teureren Länder höher. Die Euro-Spannen sind aus diesem Index abgeleitet und bewusst gerundet; jede Spanne reicht von „alle Posten am unteren Rand“ bis „alle Posten am oberen Rand“ — sie ist eine Bandbreite, kein Einzelpreis. Sortiert vom teuersten zum günstigsten Bundesland.',
     'Der <em>Index</em> zeigt das relative Kostenniveau — 100 ist der Referenzwert des bundesweiten Basis-Szenarios (der Mittelwert der 16 Länderwerte liegt bei rund 100). Der Regionalfaktor jedes Landes ist an den Friedhofsgebühren seiner Landeshauptstadt verankert (Aeternitas, Stand 01/2025) und skaliert nur die ortsgebundenen Posten — Bestatterleistungen und Sarg sind bundesweit konstant angesetzt. Jede Spanne reicht von „alle Posten am unteren Rand“ bis „alle Posten am oberen Rand“ — eine Bandbreite, kein Einzelpreis. Sortiert vom teuersten zum günstigsten Bundesland.', 1),
    # --- caption ---
    ('Modellierte Kostenspannen (Standard-Szenario, inkl. Grabpflege) — aus dem Index abgeleitet, keine erhobenen Marktpreise.',
     'Modellierte Kostenspannen (Standard-Szenario, inkl. Grabpflege) — Index verankert an Landeshauptstadt-Gebühren (Aeternitas 01/2025), keine erhobenen Marktpreise.', 1),
    # --- Prosa: Modell-Satz ---
    ('Im Modell bilden wir das vereinfacht über einen Regionalfaktor je Bundesland ab — wie genau, steht in unserer <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik</a>.</p>',
     'Im Modell skaliert deshalb ein Faktor je Bundesland nur diese ortsgebundenen Posten — verankert an den realen Gebühren der jeweiligen Landeshauptstadt (Aeternitas, Stand 01/2025). Wie genau, steht in unserer <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik</a>.</p>', 1),
    # --- Prosa: Ballungsraum-These ersetzen ---
    ('<p>Bundesländer mit vielen teuren Ballungsräumen (Bayern, Baden-Württemberg, Hamburg) liegen deshalb im Modell oben, dünner besiedelte ostdeutsche Länder (Mecklenburg-Vorpommern, Sachsen-Anhalt, Brandenburg) unten. <strong>Wichtig:</strong> Das ist ein Durchschnitt über das ganze Land — innerhalb jedes Bundeslandes gibt es zwischen Stadt und Land noch einmal große Spannen.</p>',
     '<p>Dabei folgt das Gefälle keinem einfachen Ost-West- oder Stadt-Land-Muster: München und Düsseldorf liegen oben, aber auch Magdeburg und Erfurt sind teurer als der Schnitt — während Berlin als größte Stadt des Landes die günstigsten Gebühren aller Landeshauptstädte hat. Friedhofsgebühren sind kommunalpolitische Entscheidungen, keine Geografie. <strong>Wichtig:</strong> Der Landeswert ist an der Landeshauptstadt verankert — zwischen Stadt und Land gibt es innerhalb jedes Bundeslandes noch einmal große Spannen.</p>', 1),
    # --- FAQ A1 (DOM + LD) ---
    ('Nach unserem Kostenmodell liegt das Niveau in Bayern am höchsten, gefolgt von Baden-Württemberg und Hamburg. Ausschlaggebend sind vor allem die hohen Friedhofsgebühren in den dortigen Ballungsräumen. Das sind modellierte Schätzungen, keine erhobenen Marktpreise.',
     'Nach unserem Kostenmodell liegt das Niveau in Bayern am höchsten (Anker: München), gefolgt von Nordrhein-Westfalen und dem Saarland. Ausschlaggebend sind die Friedhofsgebühren der jeweiligen Landeshauptstadt (Aeternitas, Stand 01/2025). Das sind modellierte Schätzungen, keine erhobenen Marktpreise.', 2),
    # --- FAQ A2 (DOM + LD) ---
    ('Am niedrigsten liegt das modellierte Niveau in Mecklenburg-Vorpommern und Sachsen-Anhalt, dicht gefolgt von Brandenburg, Thüringen und Sachsen. Zwischen dem teuersten und dem günstigsten Bundesland liegt nach dem Modell rund 56 % Unterschied.',
     'Am niedrigsten liegt das modellierte Niveau in Berlin — die Hauptstadt hat laut Aeternitas die günstigsten Friedhofsgebühren aller Landeshauptstädte. Dahinter folgen Sachsen, Brandenburg und Schleswig-Holstein. Zwischen dem teuersten und dem günstigsten Bundesland liegt im Modell rund %d %% Unterschied.' % spread, 2),
    # --- FAQ A4 (DOM + LD) ---
    ('Es sind Modell-Schätzungen auf Basis regionaler Kostenfaktoren für ein Standard-Szenario, keine erhobenen Marktpreise.',
     'Es sind Modell-Schätzungen für ein Standard-Szenario, verankert an den realen Friedhofsgebühren der Landeshauptstädte (Aeternitas, Stand 01/2025) — keine erhobenen Marktpreise.', 2),
    # --- FAQ A5 (DOM + LD) ---
    ('Nein — der Index ist ein Durchschnitt über das gesamte Bundesland. Innerhalb eines Landes liegen Großstadt und ländliche Gemeinde oft weit auseinander.',
     'Nein — der Index ist an den Friedhofsgebühren der Landeshauptstadt verankert. Ländliche Gemeinden im selben Bundesland liegen oft deutlich günstiger, einzelne Städte auch höher.', 2),
    # --- Dataset-Beschreibung ---
    ('"description":"Modellierter Kostenniveau-Index (78-122) und abgeleitete Kostenspannen für Feuer- und Erdbestattung in allen 16 deutschen Bundesländern. Eigene Modellrechnung von machsruhig.de auf Basis von Richtwerten (BDB, Stiftung Warentest, Aeternitas e.V., Verbraucherzentralen) — keine erhobenen Marktpreise."',
     '"description":"Modellierter Kostenniveau-Index (%d–%d) und abgeleitete Kostenspannen für Feuer- und Erdbestattung in allen 16 deutschen Bundesländern. Regionalfaktoren verankert an den Friedhofsgebühren der Landeshauptstädte (Aeternitas e.V., Stand 01/2025); Komponentenspannen als Richtwerte (BDB, Stiftung Warentest, Verbraucherzentralen) — eigene Modellrechnung, keine erhobenen Marktpreise."' % (idx_low, idx_top), 1),
    # --- Quellen-Box: Kalibrierquelle ergaenzen ---
    ('<li><a href="https://www.aeternitas.de/" target="_blank" rel="noopener" style="color:var(--mr-primary)">Aeternitas e.V.</a>: Friedhofsgebühren-Vergleiche</li>',
     '<li><a href="https://www.aeternitas.de/" target="_blank" rel="noopener" style="color:var(--mr-primary)">Aeternitas e.V.</a>: Friedhofsgebühren-Vergleiche und Gebührendatenbank</li>\n      <li>Kalibrierbasis der Regionalfaktoren: Friedhofsgebühren der 16 Landeshauptstädte, Datengrundlage Aeternitas e. V. (Stand 01/2025, vereinheitlicht auf 20 Jahre Nutzungszeit), öffentlich dokumentiert in <a href="https://www.check24.de/sterbegeldversicherung/friedhofsgebuehren-deutschland/" target="_blank" rel="noopener" style="color:var(--mr-primary)">dieser Übersicht</a></li>', 1),
])

# ===== CSV =====
csv_lines = ['Bundesland;Anker_Landeshauptstadt;Friedhofs_Faktor;Index;Feuerbestattung_min_EUR;Feuerbestattung_max_EUR;Erdbestattung_min_EUR;Erdbestattung_max_EUR']
for r in rows:
    csv_lines.append('%s;%s;%.2f;%d;%d;%d;%d;%d' % (
        r['bl'], r['stadt'], r['f'], r['idx'], r['fe'][0], r['fe'][1], r['er'][0], r['er'][1]))
with io.open('assets/data/bestattungskosten-index-2026.csv', 'w', encoding='utf-8', newline='') as fh:
    fh.write('\n'.join(csv_lines) + '\n')
print('CSV: 17 Zeilen geschrieben')

# ===== Kostenrechner =====
KR = 'tools/bestattungskosten-rechner/index.html'
mult_lines = []
for chunk_start in range(0, 16, 4):
    part = ', '.join("'%s': %.2f" % (bl, dict((b, f) for b, s, f in V2)[bl]) for bl in
                     [v[0] for v in sorted(V2)][chunk_start:chunk_start + 4])
    mult_lines.append('    ' + part)
NEW_MULT = ('// Modell V2 (2026-06-10): Friedhofs-Faktor je Bundesland, verankert an den\n'
            '  // Friedhofsgebuehren der Landeshauptstadt (Aeternitas e.V., Stand 01/2025,\n'
            '  // 20 Jahre Nutzungszeit, Mittel ueber 6 Grabarten, spaltennormiert).\n'
            '  // Wirkt NUR auf ortsgebundene Posten (s. LOCAL_FEE_KEYS) — Herleitung:\n'
            '  // /methodik#kostenmodell + _dev/audit/bundesland-modell-v2.py\n'
            '  var REGIONAL_MULTIPLIERS = {\n' + ',\n'.join(mult_lines) + '\n  };\n'
            "  var LOCAL_FEE_KEYS = {friedhofsgebuehr:1, friedhofsgebuehr_urne:1, friedhofsgebuehr_anonym:1, beisetzung:1};")
OLD_MULT = """  var REGIONAL_MULTIPLIERS = {
    'Baden-Württemberg': 1.20, 'Bayern': 1.22, 'Berlin': 1.15, 'Brandenburg': 0.80,
    'Bremen': 1.05, 'Hamburg': 1.20, 'Hessen': 1.15, 'Mecklenburg-Vorpommern': 0.78,
    'Niedersachsen': 1.02, 'Nordrhein-Westfalen': 1.05, 'Rheinland-Pfalz': 0.95,
    'Saarland': 0.90, 'Sachsen': 0.82, 'Sachsen-Anhalt': 0.78, 'Schleswig-Holstein': 0.95,
    'Thüringen': 0.80
  };"""
patch(KR, [
    (OLD_MULT, '  ' + NEW_MULT.strip(), 1),
    ('      var min = Math.round(cost.min * multiplier * qualityMult);\n      var max = Math.round(cost.max * multiplier * qualityMult);',
     '      // V2: Regionalfaktor nur auf ortsgebundene Posten (Friedhof/Beisetzung)\n      var regMult = LOCAL_FEE_KEYS[key] ? multiplier : 1.0;\n      var min = Math.round(cost.min * regMult * qualityMult);\n      var max = Math.round(cost.max * regMult * qualityMult);', 1),
])

# ===== Methodik =====
fac_rows = []
for r in rows:
    fac_rows.append('        <tr><td style="padding:7px 10px;border-bottom:1px solid var(--mr-border)">%s</td><td style="padding:7px 10px;border-bottom:1px solid var(--mr-border)">%s</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">%.2f</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">%d</td></tr>' % (
        r['bl'], r['stadt'], r['f'], r['idx']))
FAKTOR_TABELLE = '''<div class="bl-scroll" style="overflow-x:auto;margin:16px 0">
    <table style="width:100%;border-collapse:collapse;font-size:14px">
      <caption style="caption-side:top;text-align:left;font-size:12px;color:var(--mr-text-muted);padding:0 0 8px">Regionalfaktoren und Index je Bundesland — Anker: Friedhofsgebühren der Landeshauptstadt (Aeternitas e. V., Stand 01/2025, auf 20 Jahre Nutzungszeit vereinheitlicht).</caption>
      <thead>
        <tr><th scope="col" style="text-align:left;padding:8px 10px;border-bottom:1px solid var(--mr-border)">Bundesland</th><th scope="col" style="text-align:left;padding:8px 10px;border-bottom:1px solid var(--mr-border)">Anker-Stadt</th><th scope="col" style="text-align:right;padding:8px 10px;border-bottom:1px solid var(--mr-border)">Friedhofs-Faktor</th><th scope="col" style="text-align:right;padding:8px 10px;border-bottom:1px solid var(--mr-border)">Index</th></tr>
      </thead>
      <tbody>
''' + '\n'.join(fac_rows) + '''
      </tbody>
    </table>
    </div>'''

patch('methodik.html', [
    # §2 neu + Faktor-Tabelle
    ('<p><strong>2. Regionalfaktor je Bundesland:</strong> Jedes Bundesland erhält einen Faktor zwischen 0,78 (Mecklenburg-Vorpommern, Sachsen-Anhalt) und 1,22 (Bayern). Dieser Faktor ist unsere redaktionelle Einschätzung des regionalen Kostenniveaus — gestützt vor allem auf Friedhofsgebühren-Vergleiche und den Anteil teurer Ballungsräume. Der <strong>Index</strong> auf der Vergleichsseite ist dieser Faktor mal 100. 100 ist der Referenzwert des bundesweiten Basis-Szenarios; der ungewichtete Mittelwert der 16 Länderwerte liegt bei rund 99 (ein bevölkerungsgewichteter Bundesdurchschnitt läge höher).</p>',
     '<p><strong>2. Regionalfaktor je Bundesland:</strong> Jedes Bundesland erhält einen Friedhofs-Faktor zwischen 0,48 (Berlin) und 1,76 (Bayern). Er ist an den realen Friedhofsgebühren der jeweiligen <strong>Landeshauptstadt</strong> verankert: Grundlage sind die von der Aeternitas e. V. erhobenen Gebühren für sechs Grabarten (Stand 01/2025, auf 20 Jahre Nutzungszeit vereinheitlicht, öffentlich dokumentiert in <a href="https://www.check24.de/sterbegeldversicherung/friedhofsgebuehren-deutschland/" target="_blank" rel="noopener" style="color:var(--mr-primary)">dieser Übersicht</a>). Jede Grabart-Spalte wird auf ihren Mittelwert über alle 16 Städte normiert, dann wird je Stadt über die verfügbaren Grabarten gemittelt. Der Faktor wirkt <strong>nur auf die ortsgebundenen Posten</strong> (Friedhofsgebühren, Beisetzung, Grabpflege) — Bestatterleistungen, Sarg/Urne und Einäscherung bleiben bundesweit konstant. Der <strong>Index</strong> der Vergleichsseite ist das Verhältnis der Szenario-Mittelwerte zum Basis-Szenario mal 100; der Mittelwert der 16 Länderwerte liegt bei rund 100.</p>\n    ' + FAKTOR_TABELLE, 1),
    # §3 anpassen
    ('<p><strong>3. Spannen je Bundesland:</strong> Die Euro-Spannen der Vergleichsseite sind die Summe der Komponenten-Spannen eines definierten Standard-Szenarios, multipliziert mit dem Regionalfaktor und gerundet. Sie sind also <em>vollständig aus dem Index abgeleitet</em> — es sind keine 16 unabhängigen Erhebungen.</p>',
     '<p><strong>3. Spannen je Bundesland:</strong> Die ortsgebundenen Posten des Standard-Szenarios werden mit dem Friedhofs-Faktor multipliziert, die übrigen Posten bleiben konstant; die Summen werden auf 50 € gerundet. Die Spannen sind damit aus Basis-Szenario und Faktor-Tabelle <em>vollständig reproduzierbar</em> — es sind keine 16 unabhängigen Erhebungen.</p>', 1),
    # Vereinfachungen neu
    ('<p>Das Modell verwendet <strong>einen</strong> Faktor je Bundesland für alle Kostenposten. In der Realität streuen vor allem die kommunalen Friedhofsgebühren stark, während Bestatterleistungen und Sarg-Preise deutlich weniger regional gespreizt sind — der einheitliche Faktor ist eine Näherung für das Gesamtniveau. Innerhalb jedes Bundeslandes liegen Großstadt und ländliche Gemeinde zudem weit auseinander; der Landeswert ist ein Durchschnitt.</p>',
     '<p>Der Faktor ist an der <strong>Landeshauptstadt</strong> verankert — sie steht stellvertretend für ihr Land, obwohl ländliche Gemeinden meist günstiger und einzelne andere Städte teurer liegen. Die Aeternitas-Daten sind auf 20 Jahre Nutzungszeit vereinheitlicht; für München und Potsdam fehlen einzelne Grabarten, dort mitteln wir über die verfügbaren Spalten. Bestatterleistungen und Sarg-Preise setzen wir bundesweit konstant an — real streuen auch sie etwas, aber deutlich weniger als die Gebühren.</p>', 1),
    # Einordnung praezisieren
    ('Index und Spannen sind eine Modellrechnung von machsruhig.de. Sie werden von BDB, Stiftung Warentest, Aeternitas oder den Verbraucherzentralen <strong>nicht bestätigt</strong>',
     'Index und Spannen sind eine Modellrechnung von machsruhig.de auf Basis öffentlich dokumentierter Aeternitas-Gebührendaten. Die Modellrechnung selbst wird von BDB, Stiftung Warentest, Aeternitas oder den Verbraucherzentralen <strong>nicht bestätigt</strong>', 1),
    # Changelog erweitern
    ('Ergänzt: Komponententabelle des Basis-Szenarios mit Ankerzahlen, Rohdaten-CSV unter CC BY 4.0, präzisierte Index-Definition (Referenzwert 100, Ländermittel ≈ 99).</p>',
     'Ergänzt: Komponententabelle des Basis-Szenarios mit Ankerzahlen, Rohdaten-CSV unter CC BY 4.0. Modell V2: Regionalfaktoren neu hergeleitet — statt redaktioneller Schätzung jetzt verankert an den Friedhofsgebühren der 16 Landeshauptstädte (Aeternitas e. V., Stand 01/2025); der Faktor wirkt nur noch auf ortsgebundene Posten. Faktor-Tabelle veröffentlicht, Kostenrechner auf dasselbe Modell umgestellt.</p>', 1),
])

print('FERTIG — Spread: %d %%, Index %d–%d, Mittel %.1f' % (spread, idx_low, idx_top, mittel))
