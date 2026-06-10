#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welle 3 (2026-06-10) — Helper-V3-R2-Findings (NO-GO knapp, Blocker-Liste):
K1 Identitaet: Presse-Kontakt benannt (Betreiberin lt. Impressum), Byline bleibt Redaktion |
M2 Ankerzahlen + Komponententabelle Basis-Szenario (aus Kostenrechner-Code, verifiziert) |
M3 Kausal-Claim Friedhofsgebuehren als Literatur-These attribuiert (Lead + FAQ DOM/LD) |
M4 Grabpflege quantifiziert + ohne-Grabpflege-Basiswerte |
M5 methodik JSON-LD dateModified | M6 Datenschutz-Box-Widerspruch |
S8 Index-Definition (Referenzwert 100, Laendermittel ~99) ueberall |
S9 SVG-Opacity vereinheitlicht | S10 CSV + CC-BY-4.0 + Dataset.distribution |
S12 "werbefrei" -> "frei von Display-Werbung"
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

PAGE = 'bestattungskosten-nach-bundesland.html'
patch(PAGE, [
    # --- M3: Lead-Kausal-Claim attribuieren ---
    ('Eine Bestattung kostet in Bayern deutlich mehr als in Mecklenburg-Vorpommern — und das liegt nicht am Sarg, sondern vor allem an den Friedhofsgebühren.',
     'Eine Bestattung kostet in Bayern deutlich mehr als in Mecklenburg-Vorpommern — und das liegt nach übereinstimmender Einschätzung von Aeternitas und Verbraucherzentralen weniger am Sarg als an den kommunalen Friedhofsgebühren.', 1),
    # --- M3: FAQ-Antwort attribuieren, unbelegte Praezision raus (DOM + JSON-LD) ---
    ('Der größte regionale Kostentreiber sind die kommunalen Friedhofsgebühren — sie können von Ort zu Ort um mehrere hundert Prozent schwanken.',
     'Der größte regionale Kostentreiber sind nach den Vergleichen der Aeternitas e. V. die kommunalen Friedhofsgebühren — sie unterscheiden sich zwischen Kommunen teils um ein Vielfaches.', 2),
    # --- S8: Index-Definition Tabellen-Intro ---
    ('Der <em>Index</em> zeigt das relative Kostenniveau — 100 entspricht etwa dem ungewichteten Mittelwert der 16 Bundesländer (nicht dem bevölkerungsgewichteten Bundesdurchschnitt, der wegen der großen teureren Länder höher läge).',
     'Der <em>Index</em> zeigt das relative Kostenniveau — 100 ist der Referenzwert des bundesweiten Basis-Szenarios; der ungewichtete Mittelwert der 16 Länderwerte liegt bei rund 99, ein bevölkerungsgewichteter Bundesdurchschnitt läge wegen der großen teureren Länder höher.', 1),
    # --- S8: figcaption ---
    ('Kostenniveau-Index nach Bundesland (100 ≈ ungewichteter Mittelwert der 16 Länder).',
     'Kostenniveau-Index nach Bundesland (100 = bundesweiter Referenzwert; Ländermittel ≈ 99).', 1),
    # --- S9: SVG-Opacity vereinheitlichen ---
    (' opacity="1"/>', '/>', 8),
    (' opacity="0.72"/>', '/>', 8),
    # --- M4: Grabpflege quantifizieren + ohne-Grabpflege-Anker im Wichtig-Kasten ---
    ('Für eine auf deine Entscheidungen zugeschnittene Schätzung nutze den <a href="/tools/bestattungskosten-rechner/" style="color:var(--mr-primary)">Kostenrechner</a>.',
     'Für eine auf deine Entscheidungen zugeschnittene Schätzung nutze den <a href="/tools/bestattungskosten-rechner/" style="color:var(--mr-primary)">Kostenrechner</a>. Zur Einordnung: In den Werten stecken für die Erdbestattung rund 20 Jahre Grabpflege (1.600–5.000 €), für die Feuerbestattung rund 10 Jahre (400–1.500 €). Ohne Grabpflege liegt das bundesweite Basis-Szenario bei rund 3.400–8.200 € (Feuer) bzw. 3.700–9.300 € (Erd) — das erklärt, warum anderswo zitierte Zahlen oft niedriger ausfallen.', 1),
    # --- M2: Ankerzahlen in Quellen-Box ---
    ('Vollständige Herleitung: <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik</a>.</p>',
     'Vollständige Herleitung: <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik</a>. Bundesweites Basis-Szenario (Index 100): Feuerbestattung ca. 3.800–9.700 €, Erdbestattung ca. 5.300–14.300 € — Komponententabelle in der Methodik.</p>', 1),
    # --- S10 + K1: Presse-Block mit CSV, Lizenz, benannter Kontakt ---
    ('<strong>Für Redaktionen:</strong> Tabelle und Grafik dürfen mit Quellenangabe „machsruhig.de“ frei verwendet werden. Rückfragen: <a href="mailto:kontakt@machsruhig.de" style="color:var(--mr-primary)">kontakt@machsruhig.de</a> · <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik &amp; Herleitung</a>',
     '<strong>Für Redaktionen:</strong> Tabelle und Grafik dürfen mit Quellenangabe „machsruhig.de“ frei verwendet werden (Lizenz: <a href="https://creativecommons.org/licenses/by/4.0/deed.de" target="_blank" rel="noopener" style="color:var(--mr-primary)">CC BY 4.0</a>). <a href="/assets/data/bestattungskosten-index-2026.csv" style="color:var(--mr-primary)" download>Rohdaten als CSV</a> · <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik &amp; Herleitung</a> · Rückfragen: Marie-Therese Bollweg (Betreiberin), <a href="mailto:kontakt@machsruhig.de" style="color:var(--mr-primary)">kontakt@machsruhig.de</a>', 1),
    # --- S10: Dataset-Schema license + distribution ---
    ('"isAccessibleForFree":true,',
     '"isAccessibleForFree":true,"license":"https://creativecommons.org/licenses/by/4.0/deed.de","distribution":{"@type":"DataDownload","encodingFormat":"text/csv","contentUrl":"https://machsruhig.de/assets/data/bestattungskosten-index-2026.csv"},', 1),
])

# ============ methodik.html ============
KOMPONENTEN = '''<div class="bl-scroll" style="overflow-x:auto;margin:16px 0">
    <table style="width:100%;border-collapse:collapse;font-size:14px">
      <caption style="caption-side:top;text-align:left;font-size:12px;color:var(--mr-text-muted);padding:0 0 8px">Basis-Szenario (Index 100): mittlere Ausstattung, Einzelgrab, keine Extras, inkl. Grabpflege. Richtwert-Spannen, redaktionell abgeleitet (Stiftung Warentest 2023, BDB, Aeternitas e. V., Verbraucherzentralen).</caption>
      <thead>
        <tr><th scope="col" style="text-align:left;padding:8px 10px;border-bottom:1px solid var(--mr-border)">Kostenposten</th><th scope="col" style="text-align:right;padding:8px 10px;border-bottom:1px solid var(--mr-border)">Feuerbestattung</th><th scope="col" style="text-align:right;padding:8px 10px;border-bottom:1px solid var(--mr-border)">Erdbestattung</th></tr>
      </thead>
      <tbody>
        <tr><td style="padding:7px 10px;border-bottom:1px solid var(--mr-border)">Bestatterleistungen (Überführung, Versorgung, Behörden)</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">1.800–3.200 €</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">2.000–3.500 €</td></tr>
        <tr><td style="padding:7px 10px;border-bottom:1px solid var(--mr-border)">Sarg (mittlere Qualität)</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">600–1.800 €</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">800–2.200 €</td></tr>
        <tr><td style="padding:7px 10px;border-bottom:1px solid var(--mr-border)">Einäscherung + zweite Leichenschau</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">350–700 €</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">—</td></tr>
        <tr><td style="padding:7px 10px;border-bottom:1px solid var(--mr-border)">Urne</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">80–400 €</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">—</td></tr>
        <tr><td style="padding:7px 10px;border-bottom:1px solid var(--mr-border)">Friedhofsgebühren (Einzel-/Urnengrab, Ruhezeit)</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">300–1.500 €</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">600–2.800 €</td></tr>
        <tr><td style="padding:7px 10px;border-bottom:1px solid var(--mr-border)">Beisetzung</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">250–600 €</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">300–800 €</td></tr>
        <tr><td style="padding:7px 10px;border-bottom:1px solid var(--mr-border)">Grabpflege (Feuer ~10 J. à 40–150 €, Erd ~20 J. à 80–250 €)</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">400–1.500 €</td><td style="text-align:right;padding:7px 10px;border-bottom:1px solid var(--mr-border)">1.600–5.000 €</td></tr>
        <tr><td style="padding:7px 10px;font-weight:700">Summe Basis-Szenario (Index 100)</td><td style="text-align:right;padding:7px 10px;font-weight:700">ca. 3.800–9.700 €</td><td style="text-align:right;padding:7px 10px;font-weight:700">ca. 5.300–14.300 €</td></tr>
      </tbody>
    </table>
    </div>
    <p style="font-size:13px;color:var(--mr-text-muted)">Ohne Grabpflege: ca. 3.400–8.200 € (Feuer) bzw. 3.700–9.300 € (Erd). Spannen = „alle Posten am unteren Rand“ bis „alle Posten am oberen Rand“.</p>'''

patch('methodik.html', [
    # --- M5: JSON-LD dateModified ---
    ('"dateModified": "2026-04-23",', '"dateModified": "2026-06-10",', 1),
    # --- M6: Datenschutz-Prinzip-Box ---
    ('<p>Alle unsere Tools laufen lokal in deinem Browser. Es werden keine Eingaben an unsere Server übermittelt, gespeichert oder ausgewertet. Wenn wir einmal externe Dienste einbinden sollten, weisen wir vorher darauf hin.</p>',
     '<p>Die meisten unserer Tools laufen lokal in deinem Browser — Eingaben werden dort weder an unsere Server übermittelt noch gespeichert. Einzige Ausnahme sind die optionalen KI-Textentwürfe, die deine Angaben zur Texterstellung an einen KI-Dienstleister übermitteln (Details im Abschnitt „Wie unsere Tools funktionieren“ und in der Datenschutzerklärung).</p>', 1),
    # --- M2: Komponententabelle nach Schritt 1 ---
    ('Richtwerten der Verbraucherzentralen und kommunalen Gebührensatzungen.</p>',
     'Richtwerten der Verbraucherzentralen und kommunalen Gebührensatzungen. Für das Standard-Szenario der Vergleichsseite sieht das so aus:</p>\n    ' + KOMPONENTEN, 1),
    # --- S8: Index-Definition Schritt 2 ---
    ('Der <strong>Index</strong> auf der Vergleichsseite ist dieser Faktor mal 100; 100 entspricht etwa dem ungewichteten Mittelwert der 16 Länder (nicht dem bevölkerungsgewichteten Bundesdurchschnitt).</p>',
     'Der <strong>Index</strong> auf der Vergleichsseite ist dieser Faktor mal 100. 100 ist der Referenzwert des bundesweiten Basis-Szenarios; der ungewichtete Mittelwert der 16 Länderwerte liegt bei rund 99 (ein bevölkerungsgewichteter Bundesdurchschnitt läge höher).</p>', 1),
    # --- S12: werbefrei praezisieren ---
    ('Die Informationsseiten und Tools sind und bleiben kostenlos und werbefrei.',
     'Die Informationsseiten und Tools sind und bleiben kostenlos und frei von Display-Werbung.', 1),
    # --- Changelog-Eintrag erweitern ---
    ('Tool-Abschnitt aktualisiert: KI-Textentwürfe als serverseitige Ausnahme transparent gemacht.</p>',
     'Tool-Abschnitt aktualisiert: KI-Textentwürfe als serverseitige Ausnahme transparent gemacht (auch in der Grundsatz-Box). Ergänzt: Komponententabelle des Basis-Szenarios mit Ankerzahlen, Rohdaten-CSV unter CC BY 4.0, präzisierte Index-Definition (Referenzwert 100, Ländermittel ≈ 99).</p>', 1),
])
print('FERTIG')
