#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welle 4b (2026-06-10) — V1-Multiplikator-Claims (Bayern 1,22 / MV 0,78) auf den
restlichen Seiten durch V2-konsistente, quellen-wahre Formulierung ersetzen.
(BY/BE-Faktorverhaeltnis V2: 1,76/0,48 = 3,7 -> "mehr als das Dreifache";
Aeternitas 01/2025, Landeshauptstaedte.)
"""
import io, sys

BOILER_OLD = 'Regionale Multiplikatoren (Bayern 1,22, Mecklenburg-Vorpommern 0,78) verschieben diese Werte erheblich.'
BOILER_NEW = 'Die Friedhofsgebühren vor Ort verschieben diese Werte erheblich — zwischen den Landeshauptstädten liegt laut Aeternitas mehr als das Dreifache (Berlin am günstigsten, München am teuersten); siehe <a href="/bestattungskosten-nach-bundesland" style="color:var(--mr-primary)">Bundesland-Vergleich</a>.'

FILES_BOILER = [
    'bestatter-angebot-pruefen.html', 'bestatter-angebot-vergleichen.html',
    'bestatter-rechnung-pruefen.html', 'bestattungskosten-versteckte-kosten.html',
    'feuerbestattung-angebot-pruefen.html', 'seebestattung-angebot-pruefen.html',
    'was-muss-im-kostenvoranschlag-stehen.html', 'erdbestattung-angebot-pruefen.html',
]

def patch(path, replacements):
    with io.open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()
    for i, (old, new, expect) in enumerate(replacements):
        c = text.count(old)
        if c != expect:
            print('FATAL #%d: %r -> %d (erwartet %d) in %s' % (i, old[:60], c, expect, path)); sys.exit(1)
        text = text.replace(old, new)
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)
    print('%s: %d OK' % (path, len(replacements)))

for f in FILES_BOILER:
    patch(f, [(BOILER_OLD, BOILER_NEW, 1)])

# erdbestattung: FAQ (JSON-LD + DOM identisch) + Prosa
patch('erdbestattung-angebot-pruefen.html', [
    ('In Bayern liegt der Schnitt eher bei 5.500–11.600 € (Multiplikator 1,22), in Mecklenburg-Vorpommern bei 3.500–7.400 € (Multiplikator 0,78).',
     'Wie stark das regionale Niveau variiert, zeigt der Bundesland-Vergleich auf machsruhig.de — zwischen München und Berlin liegen die Friedhofsgebühren der Landeshauptstädte laut Aeternitas mehr als das Dreifache auseinander.', 2),
    ('deren Gebühren regional stark variieren (Bayern 1,22-fach, MV 0,78-fach des Bundes-Mittels).',
     'deren Gebühren regional stark variieren — zwischen den Landeshauptstädten laut Aeternitas mehr als das Dreifache (Details im <a href="/bestattungskosten-nach-bundesland" style="color:var(--mr-primary)">Bundesland-Vergleich</a>).', 1),
])
print('FERTIG')
