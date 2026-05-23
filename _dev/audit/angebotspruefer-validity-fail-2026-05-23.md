# Validity-FAIL — Angebotsprüfer (tools/angebotspruefer/)

**Datum:** 2026-05-23 · **Methodik:** Helper-V3 Outcome-Validity-Check (erster Einsatz)
**Status Tool:** LIVE seit Welle-B-Deploy (fc13607)

## Verdict: VALIDITY_FAIL (3 von 3 Szenarien)

Drei realistische, seriöse Angebote → Tool schlägt jeweils ROT vor. Gerechnet
gegen exakte Code-Schwellen (computeResult), nicht geschätzt.

| # | Szenario | Inputs | Erwartet | Tatsächlich | Schaden |
|---|---|---|---|---|---|
| 1 | Bezugsgröße: Bestatter-Summe ohne Friedhofsgebühr | Erd/NRW, 2.300 € (Gebühren ~2.800 € separat) | grün / "Gebühren separat?" | −51 % → ROT "Lockangebot" | Misstrauen gg. seriösen Bestatter |
| 2 | Legitime Pauschale | Feuer/BY, 5.900 € (mittig im Rahmen), Posten leer (Anweisung "bei Pauschale leer lassen") | gelb "aufschlüsseln" | Preis grün, aber 9/9 Posten "fehlen" → ROT (criticalMissing) | bestraft Pauschalierung strukturell |
| 3 | Grenzwert/Discounter | Anonyme/MV, 580 € (Direktkremation) | grün, günstig aber plausibel | −50 % → ROT "Lockangebot" | falscher Alarm am unteren Rand |

## Root-Cause (2 Mechanismen)

1. **Preis schaltet allein auf ROT** (−50 %-Regel) auf Basis des groben
   Bundesland-Rahmens — Datenbasis trägt einen Rot-Schluss nicht.
2. **Posten-Check misst Laien-Zuordnung statt echte Vollständigkeit** —
   Erhebungs-Anweisung "im Zweifel leer lassen" erzeugt systematisch False-Positives.

FAIL-Kategorien: Bezugsgröße, Anspruch>Datenbasis, Erhebungs-Bias, verbotene Wertung.

## Fix-Richtung (Writer-Pass, noch offen)

- Summen-Bezugsgröße eindeutig definieren (mit/ohne kommunale Gebühren).
- Preis-Signal abrüsten: nie allein ROT; Vollständigkeit ist der Anker für ROT,
  Preisabweichung max. GELB.
- Posten-Check als *Klärungs-Checkliste* framen, nicht als Vollständigkeits-Audit.
- Legitime Pauschale nicht abstrafen.
- KEIN Stadt/Friedhof-Ausbau (löst das Kernproblem nicht, hoher Aufwand).

## Methodischer Vorbehalt

Selbst-Test (Linse gebaut + selbst angewandt) → kein unabhängiger Sycophancy-Schutz.
Belastbar, weil gegen exakte Code-Schwellen gerechnet. Für wasserdicht: identischer
Run in separatem Tab gegen Live-URL.
