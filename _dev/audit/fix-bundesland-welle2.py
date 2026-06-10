#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welle 2 (2026-06-10) — Helper-V3-Reviewer-Findings Daten-PR-Seite einarbeiten.
Verdict-Quelle: claude.ai-Review (NO-GO als PR-Asset). Befunde:
K1 Methodik-Herleitung fehlt | M1 Spannen=Index-Ableitung offenlegen |
M2 Index-Definition praezisieren | M3 "ueberregional aehnlich" abschwaechen |
M4 Grabpflege-Einschluss prominent | M5 Spannen-Charakter erklaeren |
M6 Visual (SVG-Chart) + Dataset-Schema + Article-Schema-Felder |
M7 Presse-Block | M8 CTA reduzieren | Klein: scope=col, twitter/og:locale |
Methodik: Kostenmodell-Sektion neu + veralteter "nie an Server"-Tool-Claim korrigiert.
"""
import io, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
os.chdir(ROOT)

def patch(path, replacements):
    with io.open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    for i, (old, new, expect) in enumerate(replacements):
        c = text.count(old)
        if c != expect:
            print('FATAL #%d: %r -> %d Treffer (erwartet %d) in %s' % (i, old[:70], c, expect, path))
            sys.exit(1)
        text = text.replace(old, new)
    with io.open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)
    print('%s: %d Ersetzungen OK' % (path, len(replacements)))

# ============ SVG-Chart (M6) ============
IDX = [("Bayern",122),("Baden-Württemberg",120),("Hamburg",120),("Berlin",115),
       ("Hessen",115),("Bremen",105),("Nordrhein-Westfalen",105),("Niedersachsen",102),
       ("Rheinland-Pfalz",95),("Schleswig-Holstein",95),("Saarland",90),("Sachsen",82),
       ("Brandenburg",80),("Thüringen",80),("Mecklenburg-Vorpommern",78),("Sachsen-Anhalt",78)]
rows = []
for i, (name, idx) in enumerate(IDX):
    y = 8 + i * 28
    w = int(round(idx / 122.0 * 380))
    rows.append(
        '<text x="186" y="%d" text-anchor="end" font-size="13" fill="var(--mr-text,#2e2620)">%s</text>'
        '<rect x="194" y="%d" width="%d" height="16" rx="3" fill="var(--mr-primary,#8a7355)" opacity="%s"/>'
        '<text x="%d" y="%d" font-size="13" font-weight="700" fill="var(--mr-text,#2e2620)">%d</text>'
        % (y + 13, name, y, w, '1' if idx >= 100 else '0.72', 194 + w + 8, y + 13, idx))
SVG = ('\n\n    <figure style="margin:28px 0 8px">\n'
       '      <svg viewBox="0 0 660 460" role="img" aria-label="Balkendiagramm: Kostenniveau-Index der 16 Bundesländer, von Bayern (122) bis Sachsen-Anhalt (78)" style="width:100%;height:auto;font-family:inherit">\n'
       '        ' + '\n        '.join(rows) + '\n'
       '      </svg>\n'
       '      <figcaption style="font-size:12px;color:var(--mr-text-muted);margin-top:8px">Kostenniveau-Index nach Bundesland (100 ≈ ungewichteter Mittelwert der 16 Länder). Eigene Modellrechnung machsruhig.de, Stand Juni 2026 — Grafik frei verwendbar mit Quellenangabe.</figcaption>\n'
       '    </figure>')

PAGE = 'bestattungskosten-nach-bundesland.html'
patch(PAGE, [
    # --- Meta-Head: twitter:card + og:locale (Klein) ---
    ('<meta property="og:url" content="https://machsruhig.de/bestattungskosten-nach-bundesland">',
     '<meta property="og:url" content="https://machsruhig.de/bestattungskosten-nach-bundesland">\n'
     '<meta property="og:locale" content="de_DE">\n'
     '<meta name="twitter:card" content="summary_large_image">\n'
     '<meta name="twitter:title" content="Bestattungskosten nach Bundesland — der regionale Vergleich 2026">\n'
     '<meta name="twitter:image" content="https://machsruhig.de/assets/og-image.png">', 1),
    # --- Article-Schema: image + mainEntityOfPage + dateModified (M6c) ---
    ('"publisher":{"@type":"Organization","name":"machsruhig.de"},"datePublished":"2026-06-09","dateModified":"2026-06-09"}',
     '"publisher":{"@type":"Organization","name":"machsruhig.de"},"image":"https://machsruhig.de/assets/og-image.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://machsruhig.de/bestattungskosten-nach-bundesland"},"datePublished":"2026-06-09","dateModified":"2026-06-10"}', 1),
    # --- Dataset-Schema vor FAQPage (M6b) ---
    ('{"@type":"FAQPage","mainEntity":[',
     '{"@type":"Dataset","name":"Bestattungskosten-Index nach Bundesland 2026","description":"Modellierter Kostenniveau-Index (78-122) und abgeleitete Kostenspannen für Feuer- und Erdbestattung in allen 16 deutschen Bundesländern. Eigene Modellrechnung von machsruhig.de auf Basis von Richtwerten (BDB, Stiftung Warentest, Aeternitas e.V., Verbraucherzentralen) — keine erhobenen Marktpreise.","url":"https://machsruhig.de/bestattungskosten-nach-bundesland","creator":{"@type":"Organization","name":"machsruhig.de","url":"https://machsruhig.de/"},"dateModified":"2026-06-10","spatialCoverage":"Deutschland","isAccessibleForFree":true,"variableMeasured":["Kostenniveau-Index (100 = ungewichteter Mittelwert der 16 Bundesländer)","Modellierte Kostenspanne Feuerbestattung (EUR)","Modellierte Kostenspanne Erdbestattung (EUR)"]},{"@type":"FAQPage","mainEntity":[', 1),
    # --- Sichtbares Stand-Datum ---
    ('<span>Stand: 9. Juni 2026</span>', '<span>Stand: 10. Juni 2026</span>', 1),
    # --- Keyfact M3 ---
    ('<li>Überregional ähnlich: Bestatterleistungen, Sarg/Urne</li>',
     '<li>Weniger regional gespreizt: Bestatterleistungen, Sarg/Urne</li>', 1),
    # --- Tabellen-Intro: M2 + M1 + M5 + M4 ---
    ('Der <em>Index</em> zeigt das relative Kostenniveau (100 = Bundesdurchschnitt-nah). Sortiert vom teuersten zum günstigsten Bundesland.</p>',
     'Der <em>Index</em> zeigt das relative Kostenniveau — 100 entspricht etwa dem ungewichteten Mittelwert der 16 Bundesländer (nicht dem bevölkerungsgewichteten Bundesdurchschnitt, der wegen der großen teureren Länder höher läge). Die Euro-Spannen sind aus diesem Index abgeleitet und bewusst gerundet; jede Spanne reicht von „alle Posten am unteren Rand“ bis „alle Posten am oberen Rand“ — sie ist eine Bandbreite, kein Einzelpreis. Sortiert vom teuersten zum günstigsten Bundesland.</p>\n    <p><strong>Die Werte enthalten die Grabpflege über die gesamte Ruhezeit — der wesentliche Grund, warum die Obergrenzen über vielen anderswo zitierten Bestattungskosten liegen.</strong></p>', 1),
    # --- caption ---
    ('Modellierte Kostenspannen (Standard-Szenario) — keine erhobenen Marktpreise.',
     'Modellierte Kostenspannen (Standard-Szenario, inkl. Grabpflege) — aus dem Index abgeleitet, keine erhobenen Marktpreise.', 1),
    # --- th scope (Klein) ---
    ('<tr><th>Bundesland</th><th>Index</th><th class="num">Feuerbestattung ca.</th><th class="num">Erdbestattung ca.</th></tr>',
     '<tr><th scope="col">Bundesland</th><th scope="col">Index</th><th scope="col" class="num">Feuerbestattung ca.</th><th scope="col" class="num">Erdbestattung ca.</th></tr>', 1),
    # --- SVG-Chart nach Tabelle (M6a) ---
    ('    </table>\n    </div>\n\n    <div class="mr-hint" style="margin-top:16px">\n      <strong>Wichtig — so sind diese Zahlen zu lesen:</strong>',
     '    </table>\n    </div>' + SVG + '\n\n    <div class="mr-hint" style="margin-top:16px">\n      <strong>Wichtig — so sind diese Zahlen zu lesen:</strong>', 1),
    # --- Friedhofsgebühren-Prosa: M3-Satz + Modell-Transparenz ---
    ('<p>Ein Sarg kostet in Rostock ungefähr so viel wie in München. Was den regionalen Unterschied macht, sind die',
     '<p>Ein Sarg kostet in Rostock nicht dramatisch mehr oder weniger als in München. Was den großen regionalen Unterschied macht, sind vor allem die', 1),
    ('was eine ländliche Gemeinde verlangt.</p>',
     'was eine ländliche Gemeinde verlangt. Im Modell bilden wir das vereinfacht über einen Regionalfaktor je Bundesland ab — wie genau, steht in unserer <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik</a>.</p>', 1),
    # --- M8: zweiten CTA-Block in Textlink falten ---
    ('prüfe ihn Posten für Posten.</p>\n  </section>\n\n  <div class="mr-cta-block no-print">\n    <h3>Bestatter-Angebot prüfen</h3>\n    <p>In drei Minuten gegen die regionale Spanne abgleichen: Ampel-Einschätzung, Liste der Klärungspunkte und konkrete Fragen für den Bestatter.</p>\n    <a href="/tools/angebotspruefer/" class="cta-primary" data-track="cta">Angebot prüfen</a>\n    <span class="cta-sub">Kostenlos · 3 Minuten · Ohne Anmeldung</span>\n  </div>',
     'prüfe ihn Posten für Posten — der <a href="/tools/angebotspruefer/" style="color:var(--mr-primary)" data-track="cta">Angebotsprüfer</a> gleicht ihn in drei Minuten gegen die regionale Spanne ab (kostenlos, ohne Anmeldung).</p>\n  </section>', 1),
    # --- FAQ M3: DOM + JSON-LD identisch (Paritaet!) ---
    ('Bestatterleistungen und Sarg-Preise sind dagegen überregional ähnlich. Deshalb macht vor allem der Friedhof den Unterschied.',
     'Bestatterleistungen und Sarg-Preise sind dagegen deutlich weniger regional gespreizt. Deshalb macht vor allem der Friedhof den Unterschied.', 2),
    # --- K1b: Modell-Abgrenzung in Quellen-Box + M7 Presse-Block ---
    (' Friedhofsgebühren-Vergleiche</li>\n    </ul>\n  </div>',
     ' Friedhofsgebühren-Vergleiche</li>\n    </ul>\n    <p style="font-size:13px;color:var(--mr-text-muted);margin-top:10px">BDB, Stiftung Warentest, Aeternitas und die Verbraucherzentralen liefern die Richtwerte, auf denen unser Modell aufsetzt. <strong>Index und Spannen sind eine eigene Modellrechnung von machsruhig.de</strong> und werden von diesen Stellen nicht bestätigt. Vollständige Herleitung: <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik</a>.</p>\n  </div>\n\n  <div class="mr-hint no-print" style="margin:16px 0">\n    <strong>Für Redaktionen:</strong> Tabelle und Grafik dürfen mit Quellenangabe „machsruhig.de“ frei verwendet werden. Rückfragen: <a href="mailto:kontakt@machsruhig.de" style="color:var(--mr-primary)">kontakt@machsruhig.de</a> · <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik &amp; Herleitung</a>\n  </div>', 1),
])

# ============ methodik.html ============
KM = '''  <!-- Regionales Kostenmodell -->
  <section class="mr-section" id="kostenmodell">
    <h2>Das regionale Kostenmodell (Bundesland-Index)</h2>
    <p>Unser Kostenrechner und die Vergleichsseite <a href="/bestattungskosten-nach-bundesland" style="color:var(--mr-primary)">Bestattungskosten nach Bundesland</a> beruhen auf einer eigenen Modellrechnung. Damit jeder nachvollziehen kann, was diese Zahlen sind — und was nicht —, legen wir die Herleitung hier offen.</p>
    <h3>So entsteht das Modell</h3>
    <p><strong>1. Bundesweites Komponentenmodell:</strong> Für jeden Kostenposten einer Bestattung (Bestatterleistungen, Sarg/Urne, Friedhofsgebühren, Beisetzung, Trauerfeier, Grabpflege u. a.) führen wir eine bundesweite Richtwert-Spanne (von–bis). Diese Spannen sind redaktionell abgeleitet aus den oben genannten Kostenquellen — Erhebungen der Stiftung Warentest, Daten des BDB, Friedhofsgebühren-Vergleichen der Aeternitas e. V., Richtwerten der Verbraucherzentralen und kommunalen Gebührensatzungen.</p>
    <p><strong>2. Regionalfaktor je Bundesland:</strong> Jedes Bundesland erhält einen Faktor zwischen 0,78 (Mecklenburg-Vorpommern, Sachsen-Anhalt) und 1,22 (Bayern). Dieser Faktor ist unsere redaktionelle Einschätzung des regionalen Kostenniveaus — gestützt vor allem auf Friedhofsgebühren-Vergleiche und den Anteil teurer Ballungsräume. Der <strong>Index</strong> auf der Vergleichsseite ist dieser Faktor mal 100; 100 entspricht etwa dem ungewichteten Mittelwert der 16 Länder (nicht dem bevölkerungsgewichteten Bundesdurchschnitt).</p>
    <p><strong>3. Spannen je Bundesland:</strong> Die Euro-Spannen der Vergleichsseite sind die Summe der Komponenten-Spannen eines definierten Standard-Szenarios, multipliziert mit dem Regionalfaktor und gerundet. Sie sind also <em>vollständig aus dem Index abgeleitet</em> — es sind keine 16 unabhängigen Erhebungen.</p>
    <h3>Was das Modell bewusst vereinfacht</h3>
    <p>Das Modell verwendet <strong>einen</strong> Faktor je Bundesland für alle Kostenposten. In der Realität streuen vor allem die kommunalen Friedhofsgebühren stark, während Bestatterleistungen und Sarg-Preise deutlich weniger regional gespreizt sind — der einheitliche Faktor ist eine Näherung für das Gesamtniveau. Innerhalb jedes Bundeslandes liegen Großstadt und ländliche Gemeinde zudem weit auseinander; der Landeswert ist ein Durchschnitt.</p>
    <div class="mr-hint">
      <strong>Einordnung:</strong> Index und Spannen sind eine Modellrechnung von machsruhig.de. Sie werden von BDB, Stiftung Warentest, Aeternitas oder den Verbraucherzentralen <strong>nicht bestätigt</strong> und sind keine erhobenen Marktpreise. Das Modell taugt für den Richtungsvergleich zwischen Regionen — nicht als Preisauskunft für den Einzelfall. Verbindlich sind nur die Gebührensatzung der jeweiligen Kommune und konkrete Bestatter-Angebote.
    </div>
  </section>

'''
patch('methodik.html', [
    ('  <!-- Update-Zyklus -->', KM + '  <!-- Update-Zyklus -->', 1),
    ('<p>Alle interaktiven Tools auf machsruhig.de — der Kostenrechner, die Checkliste, der Trauerrede-Generator — laufen vollständig in deinem Browser (clientseitig). Das bedeutet konkret:</p>\n    <p>Deine Eingaben verlassen nie deinen Computer. Es wird nichts an unsere Server gesendet. Es werden keine Cookies für Tracking gesetzt. Die Tools funktionieren auch offline, sobald die Seite einmal geladen ist.</p>\n    <p>Wenn ein Tool in Zukunft eine serverseitige Komponente benötigen sollte (z. B. für eine AI-gestützte Funktion), werden wir das vorher klar kommunizieren und deine Einwilligung einholen.</p>',
     '<p>Die meisten interaktiven Tools auf machsruhig.de — etwa der Kostenrechner und die Checkliste — laufen vollständig in deinem Browser (clientseitig): Deine Eingaben verlassen deinen Computer nicht, und es werden keine Cookies für Tracking gesetzt.</p>\n    <p><strong>Ausnahme sind die KI-gestützten Textentwürfe</strong> (Trauerrede, Danksagung, Abschiedsbrief): Wenn du dort auf „Generieren“ klickst, werden die von dir eingegebenen Angaben zur Texterstellung an unsere Server-Funktion und von dort an einen KI-Dienstleister übermittelt. Die Nutzung ist freiwillig — ohne Klick auf „Generieren“ wird nichts übertragen. Details regelt die <a href="/datenschutz" style="color:var(--mr-primary)">Datenschutzerklärung</a>.</p>', 1),
    ('      <div style="margin-bottom:20px">\n        <div style="font-size:13px;color:var(--mr-primary);font-weight:600;margin-bottom:4px">23. April 2026</div>',
     '      <div style="margin-bottom:20px">\n        <div style="font-size:13px;color:var(--mr-primary);font-weight:600;margin-bottom:4px">10. Juni 2026</div>\n        <p style="font-size:14px;margin:0;line-height:1.6">Neuer Abschnitt „Das regionale Kostenmodell (Bundesland-Index)“: Herleitung von Index und Kostenspannen offengelegt (Komponentenmodell, Regionalfaktor, bewusste Vereinfachungen). Tool-Abschnitt aktualisiert: KI-Textentwürfe als serverseitige Ausnahme transparent gemacht.</p>\n      </div>\n      <div style="margin-bottom:20px">\n        <div style="font-size:13px;color:var(--mr-primary);font-weight:600;margin-bottom:4px">23. April 2026</div>', 1),
    ('<strong>Stand:</strong> 23. April 2026', '<strong>Stand:</strong> 10. Juni 2026', 1),
])
print('FERTIG')
