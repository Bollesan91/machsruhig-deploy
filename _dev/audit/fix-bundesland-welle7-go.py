#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welle 7 (2026-06-10) — R6-GO-Pflichtkorrekturen (GO 85, 3 Pflicht-Fixes vor Versand):
M1 Headline-Zahl explizit attribuiert (Aeternitas-Daten, check24-Aufbereitung) |
M2 Datenstand sichtbar (Gebuehrenbasis Anfang 2025, Modellierung Juni 2026) |
M3 Obergrenzen-Rahmung defensiver ("tendenziell zu hoch" statt "konservativ hoch") |
K4 Halbsatz trennt 4,75x (Sargwahlgrab) von 81% (Gesamt-Index).
"""
import io, sys

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
    # M1 + K4: Lead — explizite Attribution + Trennung der zwei Spread-Zahlen
    ('Im auf 20 Jahre vereinheitlichten Vergleich der Landeshauptstädte (Datengrundlage Aeternitas) verlangt die teuerste — München, 4.578 € fürs Sargwahlgrab — fast das Fünffache der günstigsten (Berlin, 964 €). Hier siehst du,',
     'Im Vergleich der Landeshauptstädte (Aeternitas-Gebührendaten, auf 20 Jahre vereinheitlicht in der check24-Aufbereitung) verlangt die teuerste — München, 4.578 € fürs Sargwahlgrab — fast das Fünffache der günstigsten (Berlin, 964 €). Aufs gesamte Bestattungs-Szenario gerechnet schrumpft der Abstand: Im Modell liegt das teuerste Bundesland rund 81 % über dem günstigsten. Hier siehst du,', 1),
    # M2: Datenstand-Keyfact
    ('<li>Die Zahlen sind <strong>Modell-Schätzungen</strong>, verankert an Aeternitas-Gebührendaten (Stand 2025) — keine erhobenen Marktpreise</li>',
     '<li>Die Zahlen sind <strong>Modell-Schätzungen</strong> — keine erhobenen Marktpreise. Gebührenbasis: Aeternitas, Anfang 2025; Modellierung: Juni 2026</li>', 1),
    # M3: Caption defensiver
    ('Obergrenzen enthalten die volle Grabpflege über die Ruhezeit (Erd ~20, Feuer ~10 Jahre).',
     'Obergrenzen enthalten die volle Grabpflege über die Ruhezeit (Erd ~20, Feuer ~10 Jahre) und fallen dadurch tendenziell eher zu hoch als zu niedrig aus.', 1),
])

patch('methodik.html', [
    # M3: "konservativ hoch" praezisieren
    ('die Obergrenzen teurer Länder sind dadurch eher konservativ hoch angesetzt.',
     'die Obergrenzen teurer Länder fallen dadurch tendenziell zu hoch aus — diese bewusste Überschätzung nehmen wir in Kauf, statt Präzision vorzutäuschen.', 1),
])
print('FERTIG')
