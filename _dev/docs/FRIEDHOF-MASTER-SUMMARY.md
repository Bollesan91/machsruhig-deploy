# Friedhofsgebühren Re-Audit — Master-Summary (50 Städte, Einzel-Review abgeschlossen)

> Ergebnis der stadtweisen Einzelprüfung (claude.ai-Friedl-Reviewer) + Koordinaten-Selbstverifikation gegen die amtlichen Satzungs-PDFs.
> Einheit B: günstigstes reguläres Einzel-Erd-Wahlgrab, EINE Sargbeisetzung, echte Nutzungsdauer. Grabnutzung + Beisetzung getrennt.
> Detail je Stadt: FRIEDHOF-REAUDIT-STATUS.md (Batch-Sektionen). Stand: 09.07.2026.

## A. WERT-KORREKTUREN (Register war/ist falsch → ändern)
| Stadt | Register (falsch) | Korrekt | Grund |
|---|---|---|---|
| Mainz | 4.714 (Doppelgrab) | Reihengrab 1.172/20J + 1.335 = 2.507 | kein Einzel-Wahlgrab; Doppelgrab |
| Kassel | 1.908 / 20 J | 1.908 / **30 J** (+ Beis. prüfen) | Laufzeit falsch |
| Mannheim | 1.411 (2 Pers.) | Reihengrab 1.035 | 2-Personen-Grab |
| Krefeld | 2.760 (Ersterwerb) | **3.450** (1.6 Zweifachbeleg. je Grabstelle) | kein neues Einzel-Wahlgrab; 2.760 nur Wiedererwerb |
| Osnabrück | Beis. 450 (Reihengrab-Zeile) | **100** (1.2.1 Wahlgrab) + Grabnutzung 74/J×**25J** | 450 war Ziffer 1.1 Reihengrab — PRIMÄR bestätigt (pdftotext-layout) |
| Dortmund | 2.650 / 950 / 20 J | **2.700 / 960 / 25 J** | Amtsblatt 9/2026 (primär) — Altfassung ersetzt |
| Hamm | 1.166 / 711 | **1.100 / 800** | 8. Änderung 2024 (primär) — lokales PDF war stale, Reviewer hatte recht |

*(Saarbrücken 720+1.755 & Potsdam 68/J+767: mein Beisetzungs-Verdacht widerlegt — Werte stimmen, s. Sektion F.)*

## B. LAUFZEIT-FIXES (Wert ok, Nutzungsdauer im Register falsch)
| Stadt | Register | Korrekt |
|---|---|---|
| Hamm | 25 J | **30 J** (1.166 + 711 Werte ok) |
| Halle | 20 J | **30 J** (+ Staleness, s.u.) |
| Ludwigshafen | 20 J | **30 J** (2.469 + 1.168) |

## C. VERSION / STALENESS — Pinning-Runde 09.07. (6/8 PRIMÄR-VERIFIZIERT)
| Stadt | Status | Ergebnis (Primärquelle) |
|---|---|---|
| Dortmund | ✅ PINNED | Amtsblatt 9/2026 → korrigiert 2.700/960/25J |
| Hamm | ✅ PINNED | 8. Änderung 2024 → korrigiert 1.100/800 (mein PDF war stale) |
| Halle | ✅ PINNED | Live SR_708-2 → 960/746 aktuell + FUG 210 (Reviewer-Zahlen waren Fehl-Aufteilung) |
| Osnabrück | ✅ PINNED | Ortsrecht II_2-15 (curl+layout) → 74/J + 100 bestätigt |
| Leverkusen | ✅ PINNED | Amtsblatt 47/2025 → 164,01/1.270,98 unverändert |
| Wiesbaden | ✅ PINNED | FGO 7-5.3 2022 → 3.383/674 + Zitat gefixt |
| **Kiel** | 🔴 OFFEN (STALE) | 404-Gate; **BOLLE: Satzung 27.03.2025 hochladen** |
| **Ludwigshafen** | 🟠 OFFEN (VERIFY) | 7-09.pdf hart hinter Redirect-Gate; 2.469/1.168 nicht primär bestätigbar |
| Gelsenkirchen / MG | ✓ OK_NOTE | Werte ok; nur aktuelle Quelle verdrahten (kosmetisch) |

## D. SCOPE — Pflicht-Zusatzgebühren, die das 2-Komponenten-Modell weglässt
(Global-Decision #1: Caveat verschärfen + bekannte Zusatzgebühren je Stadt notieren)
| Stadt | Fehlender Pflicht-Posten | Größe |
|---|---|---|
| Magdeburg | Friedhofsunterhaltung 48,90/Jahr | ~978 / 20 J |
| Leipzig | §8 Friedhofsnutzung 420 + §9 Grundherstellung 82 | +502 |
| Erfurt | Friedhofsunterhaltung | +506 |
| Halle | FUG "Bestandteil aller Grabarten" | +180 |
| Oldenburg | Grabumrandung 192 (§16 Zwangsleistung) | +192 |
| Krefeld | Verbau von Hand 285 + Erdaushub 171 | +456 (quasi-Std) |
| Freiburg | Verwaltungsgebühr Erdbestattung | +72 |
| Augsburg | Unterhaltsgebühr 34/Jahr | ~680 / 20 J |
| Chemnitz | Grund-/Einlieferung/Annahme | +141 |
| Berlin | Verwaltungsgebühr | +52 (eingerechnet) |
| Heidelberg | Leichenhalle | +260 |
| Nürnberg | Annahme | +59 |
| Stuttgart | Verwaltungsgebühr Erdbestattung | +135 |
> Muster: **jährliche Unterhaltungsgebühren** (MG 48,90/J, Augsburg 34/J, Hamm ~37/J) sind der größte blinde Fleck.
> Gegenbeispiel Karlsruhe/Münster/Rostock: KEIN Scope-Zuschlag (Hallen etc. bereits in der Bestattungsgebühr → nicht doppelt zählen!).

## E. EINHEITEN-SONDERFÄLLE (kein reguläres Einzel-Wahlgrab)
- Mainz: kein Einzel-Wahlgrab → Reihengrab.
- Krefeld: neues Einzel-Wahlgrab nicht erwerbbar → 3.450 (Zweifachbeleg.) oder Reihengrab 1.860.
- Augsburg: 47/J war Familiengrab → Neu-Erhebung Einzel-/Reihengrab-Tarif offen.

## F. REVIEWER-FALSE-POSITIVES (Selbstverifikation hat Reviewer widerlegt — unser Wert stimmt)
- Hagen: Reviewer meldete 1.465/535 (alte Fassung); Koordinaten-Extraktion aus VI. Nachtrag (Dez 2025) = 1.530 + 570 KORREKT.
- Potsdam: mein Beisetzungs-Verdacht 767 widerlegt (767 korrekt für Erwachsene; "Gruft" = generischer Begriff für jede Erdgrabstelle).
- Saarbrücken: mein Beisetzungs-Verdacht 1.755 widerlegt ("obere Belegung" = Regeltiefe, nicht 2. Körper; 1.100 = Urnen-Zeile).

## G. BESTÄTIGT OK (Wert + Version, keine Änderung außer ggf. Scope-Note)
Hamburg, Köln, Düsseldorf, Aachen, Bochum, Chemnitz, Duisburg, Erfurt, Essen, Frankfurt, Hannover, Gelsenkirchen, Freiburg, Heidelberg, Karlsruhe, Leipzig, Lübeck, Magdeburg, München, Münster, Nürnberg, Oberhausen, Oldenburg, Potsdam, Rostock, Stuttgart, **Wuppertal** (ab 01.01.2026), **Saarbrücken** (720+1.755), **Wiesbaden** (3.383+674, nur Zitat auf 27.01.2022 fixen), Bielefeld, Bonn (revert), Mülheim (revert), Dresden (Netto/USt-Frage)

**Alle 50 Städte durch die Einzelprüfung (09.07.2026).**

## OFFENE ENTSCHEIDUNGEN / NÄCHSTE SCHRITTE
1. Osnabrück + Saarbrücken Beisetzungs-Zeile final klären (Reviewer läuft).
2. Version-Pinning-Runde (Kategorie C) = eigener Arbeitsschritt vor Live. Kiel braucht Bolle-Upload.
3. Scope-Umsetzung je Global-Decision #1 (Caveat + Notes), NICHT alle Gebühren neu erheben.
4. München/Nürnberg: Ruhezeit 10 J (nicht 20) in der Normalisierung berücksichtigen.
5. Erst danach: korrigiertes Register bauen → Live-Boxen regenerieren → Linter → Deploy (Bolle-Go).
