# Friedhofsgebühren — Re-Audit-Status (06.07.2026)

> Zwischenstand einer **unfertigen** Datenbereinigung. NICHT deployen, bis der Finish + das Einzel-Review-Gate durch sind.
> Rohdaten des Audits: `_dev/claims/reaudit-2026-07/` (49 `audit_<slug>.json` + `_merged.json`).

## Auslöser
Die live per-Stadt-Gebühren-Kästen (`friedhoefe/<stadt>/`, aus `_dev/claims/friedhofsgebuehren.json`) hatten einen **systematischen Einheits-Fehler**: Grabtypen gemischt (mal Doppel-/Familiengrab, mal Wahlgrab, mal Reihengrab), Laufzeiten teils falsch. Ursache: **„Einzelstelle" (ein Grab-PLATZ) wurde mit „Einzelbelegung" (eine Beisetzung) verwechselt** — überlebte 2× Verifikation + einen target-blinden Reviewer; erst Bolles Fachauge (Doppelgrab) + Google-Check fingen es.

## Festgelegte Einheit (Bolle 06.07., Variante B)
**Standard Einzel-Erd-Wahlgrab** — frei wählbar/verlängerbar, ERDbestattung, **genau EINE Sargbeisetzung**, **normale Lage**, echte Nutzungsdauer. Grabnutzung + Beisetzung getrennt. Grabtyp je Stadt benannt. Wo kein Einzel-Wahlgrab existiert (nur Doppel/Familie) → günstigstes Erd-Grab mit einer Beisetzung (ggf. Reihengrab), so gekennzeichnet. Reihengrab-Alternative als optionale „günstigste Variante"-Zeile (Daten liegen vor).

## Methode
50 amtliche Satzungen lokal per `pdftotext`/HTML-Extraktion gezogen (WebFetch scheiterte an komprimierten PDFs). Sammel-Skript: scratchpad `collect_satzungen.sh`. Re-Audit: Workflow (47 Agents, je Satzung → Einzel-Erd-Wahlgrab mit Beleg). **Jede Korrektur von Haupt-Claude selbst gegen den Satzungstext verifiziert.**

## PFLICHT-GATE vor Live (Bolle 06.07.): Einzel-Reviews
**Agenten fangen nicht alles.** Beweis: der Workflow flaggte nur 6 Korrekturen und winkte **Bochum** (Familiengrab = Mehrfachbelegung) als „stimmt" durch — erst die Einzelprüfung fing es. Regel: **Vor Live geht JEDE der 50 Städte noch einmal durch einen unabhängigen Einzel-Review** (nicht nur Batch-Agent). Das Batch-Audit ist Rohmaterial, kein Freigabe-Ersatz.

## Bestätigte Korrekturen (verifiziert)
| Stadt | Register (falsch) | Korrekt | Grund |
|---|---|---|---|
| Mainz | 2.827 € / 20 J. (+Beis. 1.887) = 4.714 | Reihengrab 1.172 € / 20 J. + Beis. 1.335 = **2.507** | Doppelgrab; Mainz hat KEIN Einzel-Wahlgrab (Satzung Stand 03.07.2026) |
| Kassel | 1.908 € / 20 J. | 1.908 € / **30 J.** (Wahlgrab 1 Stelle); Reihengrab-Alt 870/20 J. | Laufzeit falsch; Beis. ~2.107 „je nach Leistung" prüfen |
| Mannheim | 1.411 (2 Personen) | Reihengrab **1.035** | 2-Personen-Grab → Einzelbelegung |
| Bonn | 82,20 €/J (Reihengrab) | Wahlgrab **181,67 €/J** | falscher Grabtyp (Einheit B) |
| Mülheim a.d.R. | 2.603 | **2.858** | falscher Tarif (Agent-Fund) |

## Offene Handarbeit (Finish)
- **Bochum** — Register „Familiengrabstätte 2.505" (Mehrfachbelegung); Einzel-Option (Reihengrab-Nutzungsrecht) im Volltext prüfen. Agent-Miss.
- **Köln** — Wahlgrab hält 2 (untere/obere Bestattung), als ein Platz bepreist (1.945) — als Einzelnutzung vertretbar, Kapazität transparent kennzeichnen.
- **Augsburg** — Agent flaggte false + „Familiengrab"; 47 €/J „Grabnutzungsrecht Erdgrabstätten" ist vermutlich der Standard-Einzelgrab → nachprüfen (wahrscheinlich OK).
- **Quelle unlesbar → neu holen/parsen:** Berlin (JS-Ladeseite; + 520 € ist Friedhofsgrundgebühr, NICHT Nutzungsrecht — Nutzungsrecht fehlt, Fassung 2011 stale), Kiel (404-Seite geladen), München (MS-Word-HTML-Tabelle nicht geparst), Wiesbaden (Beisetzung fehlte, ~674 verifizieren).

## Nebenbefund (wertvoll für „günstigste Variante")
Viele Städte haben ein deutlich billigeres Einzel-**Reihengrab** als das Wahlgrab: Aachen 1.527 vs 2.420, Gelsenkirchen 925 vs 2.717, Oberhausen 742 vs 2.098, Dortmund 1.720 vs 2.650, u.a. (Werte in `reaudit-2026-07/`).

## Nächste Schritte (in späterer Sitzung, budgetschonend)
1. Finish der ~6 Handarbeits-Städte (oben).
2. Korrigiertes Register bauen → Live-Boxen regenerieren (`wire-gebuehren-daten.py` re-run) → „Einzelstelle"-Label raus, Grabtyp benannt.
3. Linter (site+friedhof+claims) 0 FAIL.
4. **Einzel-Review-Gate:** jede Stadt einzeln unabhängig prüfen (Pflicht, s.o.).
5. Erst dann Live-Deploy (Bolle-Go).

## Status Index-Idee
**In der Schublade** (Bolle 06.07.). Kein Solo-Live-Index; Wert nur mit institutionellem Ko-Autor. Der `friedhof-lotse`-Branch (Vergleichsseite + Generator) bleibt geparkt.
