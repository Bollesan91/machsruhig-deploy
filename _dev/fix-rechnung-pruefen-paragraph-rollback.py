# YMYL-CRITICAL Rollback: § 650 BGB → § 649 BGB in bestatter-rechnung-pruefen.html
#
# Plan-Reviewer-Hallu: behauptete §650 sei korrekter Kostenanschlags-Paragraph.
# Re-Audit-Reviewer + dejure.org/gesetze-im-internet.de bestätigt:
# - § 649 BGB n.F. (2026) = Kostenanschlag (mit Anzeigepflicht in Abs. 2)
# - § 650 BGB = Werklieferungsvertrag (falsch für unseren Use-Case)
# - § 648 BGB = freie Kündigung (war historisch § 649 a.F.)
#
# Konjunktivische Formulierung BLEIBT (Plan-Reviewer hatte hier recht).
# § 280 BGB Schadensersatz-Hebel BLEIBT (auch korrekt).
# § 195 BGB Verjährung BLEIBT (auch korrekt).
# § 632 BGB ortsüblich BLEIBT (auch korrekt).

import os, sys
sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(ROOT, "bestatter-rechnung-pruefen.html")

# Reine Norm-Korrekturen § 650 → § 649
FIXES = [
    ("§ 650 Abs. 2 BGB", "§ 649 Abs. 2 BGB"),
    ("§ 650 BGB", "§ 649 BGB"),
]

with open(TARGET, "r", encoding="utf-8") as f:
    text = f.read()
original = text
total = 0
for old, new in FIXES:
    count = text.count(old)
    if count:
        text = text.replace(old, new)
        total += count
        print(f"  x{count}: {old} → {new}")

if text != original:
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\nRollback: {total} Norm-Referenzen korrigiert.")
else:
    print("Keine Treffer.")
