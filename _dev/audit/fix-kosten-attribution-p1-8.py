# -*- coding: utf-8 -*-
"""P1-8 (Bolle-Entscheid a): eigenes Modell = Single Source.
Satelliten-Seiten attribuieren die EIGENE Modellzahl 6.000-8.000 EUR
faelschlich als "(Stiftung Warentest, 2026)" — SW ist real 7.000-8.000
(Finanztest 11/2023), und das Jahr 2026 ist erfunden. Die Zahl 6.000-8.000
stammt aus dem eigenen Kostenmodell (Kostenrechner: "Bundesweiter
Durchschnitt, alle Arten gemischt"). Also: Zahl bleibt, falsche SW/2026-
Attribution -> eigenes Kostenmodell. NICHT angefasst: BDB-6.000-8.000
(bestattungskosten.html), SW-7.000-8.000-Prosa (BL/Stadtseiten, korrekt),
Kostenrechner-Eigenzahl. Asserts vor dem einzigen Write."""
import os, re

VARIANTS = [
    "6.000–8.000 € (Stiftung Warentest, 2026)",
    "6.000–8.000 € (Stand 2026, Stiftung Warentest)",
]
CANON = "6.000–8.000 € (eigenes Kostenmodell, alle Bestattungsarten gemischt)"

changes = []
total = 0
for root, _, fs in os.walk('.'):
    if os.sep + '_dev' in os.sep + root or '.git' in root or 'node_modules' in root:
        continue
    for f in fs:
        if not f.endswith('.html'):
            continue
        p = os.path.join(root, f)
        s = open(p, encoding='utf-8').read()
        new = s
        for v in VARIANTS:
            new = new.replace(v, CANON)
        if new == s:
            continue
        # ASSERTS vor Write:
        # (a) keine SW-7.000-8.000 auf dieser Datei beruehrt
        assert s.count("7.000–8.000") == new.count("7.000–8.000"), "SW-7000 veraendert: " + p
        # (b) BDB-Zeilen unberuehrt
        assert s.count("Branchenangaben (BDB)") == new.count("Branchenangaben (BDB)"), "BDB veraendert: " + p
        # (c) keine neue erfundene Quelle
        assert "Stiftung Warentest, 2026" not in new, "SW-2026 Rest: " + p
        cnt = sum(s.count(v) for v in VARIANTS)
        total += cnt
        changes.append((p, new, cnt))

print("Dateien:", len(changes), " Fundstellen umattribuiert:", total)
for p, new, cnt in changes:
    open(p, 'w', encoding='utf-8').write(new)
    print("  ", p, cnt)
print("geschrieben.")
