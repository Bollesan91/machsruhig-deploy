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
AUGSBURG: MAJOR - 47 ist Familiengrab (2 Best.) + fehlende Unterhaltsgeb 34/J. Braucht Neu-Erhebung: Einzel-/Reihengrab-Tarif + Unterhaltsgeb. Reihengrab-Info war 59/J.

## SYSTEMATISCHES SCOPE-THEMA (Einzel-Reviews 06.07.)
Mehrere Städte haben PFLICHT-Zusatzgebühren über Grabnutzung+Beisetzung hinaus, die unser 2-Komponenten-Modell weglässt → unterzeichnet diese Städte:
- Augsburg: Unterhaltsgebühr 34 EUR/Jahr fehlt (real 81/J statt 47).
- Chemnitz: Friedhofsgrundgebühr 85/20J + Einlieferung 25 + Annahme 31 = ~141 EUR fehlen.
- Berlin: Verwaltungsgebühr 52 (jetzt eingerechnet -> 572).
ENTSCHEIDUNG NÖTIG (Bolle): entweder alle Pflicht-Friedhofsgebühren je Stadt aufnehmen (konsistent), ODER Caveat verschärfen ("nur Grabnutzung+Beisetzung; zusätzliche Pflicht-Friedhofsgebühren wie Grund-/Verwaltungsgebühr variieren je Stadt"). Aktuelle Live-Caveat verschweigt das.
Reviewte OK (Original bestätigt): Hamburg, Köln, Düsseldorf, Aachen, Bochum, Chemnitz. Berlin +52. Augsburg MAJOR offen.
Batch5: Duisburg OK (1.838/1.029). Dortmund VERSION-FUND (Maerz-2026-Fassung existiert, 2.650 gegen aktuell pruefen). Dresden NETTO + USt-Frage (924/533 netto; mit 19% 1.100/634 - USt-Behandlung klaeren). Neue globale Themen: Versions-Aktualitaet + Netto/USt.

## GLOBALE ENTSCHEIDUNGEN (Bolle delegiert an Claude, 06.07.)
1. SCOPE: Caveat verschaerfen ("Grabnutzung+Beisetzung; zusaetzliche Pflicht-Friedhofsgebuehren variieren je Stadt") + bekannte Zusatzgebuehren je Stadt notieren (nicht voll neu erheben).
2. USt: Friedhofsgebuehren i.d.R. hoheitlich=USt-frei; nur wo Satzung ausdruecklich netto+USt (Dresden), je Stadt kennzeichnen. Kein pauschales +19%.
3. EINHEIT: Wahlgrab bleibt primaer (B) + Reihengrab als "guenstigste Variante"-Zeile.
4. VERSION: Einzel-Reviews sind der Versions-Check; geflaggte Staedte aktualisieren (Dortmund).

## BATCH 6 (Erfurt/Essen/Frankfurt) — 06.07.
- ERFURT: OK. 870 (Pos 1.1 Erdwahlgrab 20J einstellig) + 1.484 (Pos 6.1 Bestattungsgeb ab 5. Lj) korrekt + versionsaktuell (Fassung 16.03.2026). SCOPE: Pflicht-Friedhofsunterhaltung 506 EUR fehlt (real 2.860 statt 2.354). -> je Decision #1 Note "Friedhofsunterhaltung 506 EUR".
- ESSEN: OK, kein MAJOR. 2.050 (Wahlgrab 25J) + 720 (erste Grabbereitung) korrekt. Version: Gebuehren noch 02/2024 gueltig, 07/2025-Neufassung nur Friedhofssatzung. 720 nur erste Beisetzung (Beibestattung spaeter 765).
- FRANKFURT: OK. 1.855 (Pos 5.1.1.1 Einzelwahlgrab 25J) amtlich exakt + versionsaktuell (GebO 01.01.2025). Beisetzung 1.659 doppelt trianguliert (Doppel 4.630-2.971; Reihe 2.841-1.182) -> sehr wahrscheinlich korrekt; Einzelposten "Bestattungsgeb Erdbest. ab 5.Lj" vor Live im PDF gegenchecken.

## BATCH 8 vorbereitet (Halle/Hamm/Hannover) — Selbstverifikation vorab
- HAMM: MAJOR-Fund (Selbstverifikation). Register 1.166/25J ist FALSCH = Ziffer 1.1.3.5 "25 J im anonymen Rasenfeld, inkl 19% USt". Korrekt = 1.2.1 Wahlgrabstaette je Grabstelle 30 J = 1.482,00. Beisetzung 711 (2.1.2) ok. Zusatz 1.4.1 Unterhaltung 57,83/Wahlgrabstelle. -> Reviewer bestaetigt Batch 8.
- HANNOVER: 2.522 (2.1.1a Standard) + 748 ((1) Erdbeisetzung) beide selbst-verifiziert im Satzungstext. Reihengrab 1.513.
- HALLE: 960 (1.10 Erdbestattungswahlgrab, 20J) + 746. Reihengrab 643. -> Reviewer.

## BATCH 7 (Gelsenkirchen/Hagen/Freiburg) — 06.07.
- GELSENKIRCHEN: OK. 2.717 (A.3.1 Erdwahlgrab 2,50x1,20) + 1.420 (B.7 Erdbestattung) = 4.137, korrekt + versionsaktuell (26. AeS, Kraft 01.01.2026). Single bestaetigt. WICHTIG: alte 25.AeS (2.872/1.320) kursiert noch -> im Tool /2026/01/-Fassung verdrahten. Scope: Grabmal-Aufstellung 112 nur situativ (nicht Pflicht).
- HAGEN: OK -- REVIEWER-FALSE-POSITIVE (selbst widerlegt). Reviewer meldete MAJOR (1.465/535/30J aus alter Fassung). Primaerquelle hagen.raw = VI. Nachtrag (beschl. 11.12.2025, NEUER als Reviewer-Quelle); pdfplumber-Koordinaten-Extraktion: "4.80 Wahlgrabstaette Sargbestattung 1.530" + Beisetzung 570 (Grabaushub ab 5.Lj, Z.135/139). UNSERE 1.530 + 570 KORREKT. Offen MINOR: Nutzungszeit 25 vs 30J (=Ruhezeit lt Friedhofssatzung, nicht Gebuehrensatzung; low impact da 1.530 Flat-Fee bis Ruhezeit-Ablauf).
- FREIBURG: OK. 1.488 (74,40 x20J) + 1.795 bestaetigt (Aeternitas 04.06.2025; Jahresmodell gestuetzt via Doppelgrab 148,80 = 2x74,40). Single bestaetigt (1 Sargplatz; 2. Sarg nur Tieferlegung +336). Scope: Verwaltungsgebuehr Erdbestattung 72,28 = Pflicht obendrauf (real 3.355 statt 3.283).

## BATCH 8 KORREKTUR (Hamm) — meine Hypothese war falsch, Koordinaten-Extraktion korrigiert
ACHTUNG: obige "HAMM MAJOR 1.166 falsch -> 1.482"-Notiz ist FALSCH und aufgehoben. pdfplumber-Koordinaten (hamm.raw):
- 1.2.1 "fuer jede Grabstelle bei einer Nutzungszeit von 30 Jahren" = 1.166,00 -> STANDARD-Wahlgrab = UNSER Wert, KORREKT.
- 1.2.2 = 1.482,00 ist "Erweiterungsteil Bockum, 50 Jahre" (Sonderfall), NICHT Standard.
- 1.1.3.5 anonymes Rasenfeld 25J = 1.209,04 (nicht 1.166 wie geflatteter Text suggerierte).
- Beisetzung: 2.2 "bei einer Wahlgrabstaette" = 711,00 (unser Wert) vs 2.1.2 ab 5.Lj = 596,00.
- Scope: 1.4.1 je Wahlgrabstelle nach 1.2.1 = 38,90 (jaehrl. Unterhaltung?).
ERGEBNIS HAMM: 1.166 + 711 KORREKT. Einziger Fix: Laufzeit 25 -> 30 J. Reviewer bestaetigt Beisetzungs-Zuordnung 711 vs 596.
LEHRE: geflatteter pdftotext hat mich bei Hamm (wie Hagen) getaeuscht -> Koordinaten-Extraktion VOR jeder Register-"Korrektur" (Lektion 15 verschaerft).

## BATCH 9 vorbereitet (Heidelberg/Karlsruhe/Kiel) — Koordinaten-Selbstverifikation
- HEIDELBERG: OK (selbst-verifiziert). 4.2.3 Einzelgrab 2./3. Reihe = 2.420 (guenstigere Standard-Position; 4.2.1 1. Reihe = 2.750) + 2.1 Erdbestattung = 1.190. Beide korrekt. Reviewer: 2./3. Reihe fair vs 1. Reihe?
- KARLSRUHE: OK (selbst-verifiziert). 2.1.1 Erdbestattungswahlgrab an Wegen/Feldern = 100/Jahr + 4.1.1 Erdbestattungsgebuehr = 1.463. Beide korrekt. Jahresmodell wie Freiburg. Reihengrab 1.1.2 = 1.096.
- KIEL: SONDERFALL - lokaler Download war 404-Seite, KEIN Beleg. Reviewer muss aktuelle Kieler Satzung online holen + 1.767,20/654,60 von Grund auf verifizieren/ersetzen.

## BATCH 8 (Halle/Hamm/Hannover) — FINAL 06.07.
- HANNOVER: OK. 2.522 (2.1.1a) + 748 ((1) Erdbeisetzung) versionsaktuell bestaetigt, keine USt (nicht *-markiert), 20 J (§2 Abs 2.1). Trauerhalle 296/30min nur optional. Reihengrab 1.513 = andere Grabart (Info).
- HALLE: MAJOR STALENESS. Lokales PDF = Basisfassung 2015 (SR 7.08-2, KVG-LSA 2014): 1.10=960, 3.1.1 Oeffnen/Schliessen=746. AKTUELL (Reviewer, 2. Aenderung + Lesefassung 2020): Nutzung ~1.005, Beisetzung 916, +FUG 180 Pflicht (Pos 5.1 "Bestandteil aller Grabarten"), Erdreihengrab jetzt 666 (2015: 643). LAUFZEIT: 30 J bestaetigt via MEIN PDF (S.4 "fuer 30 Jahre erhoben", 1.10 im Block) -> unser "20 J" war Eingabefehler. => RE-COLLECT aktuelle Fassung noetig.
- HAMM: Struktur bestaetigt (1.2.1 Standard-Wahlgrab 30J + 2.2 Wahlgrab-Beisetzung). LAUFZEIT 25->30 J (fix, Eingabefehler). EXAKTE WERTE VERSIONS-KONFLIKT: mein hamm.raw = §4-Neufassung m. Bezug GV.NRW 2023 -> 1.2.1=1.166, 2.2=711, 1.4.1=38,90, 1.2.2=1.482. Reviewer (web) -> 1.100/800/36,70/1.427. Richtungen widerspruechlich (Nutzung meins hoeher, Beisetzung seins hoeher) -> kein sauberer Vergleich. => aktuelle Fassung pinnen vor Live.

## ESKALATION: VERSIONS-AKTUALITAET IST GROSSES QUERTHEMA
Nicht nur Dortmund. Betroffen bisher: Halle (2015 base stale), Hamm (2023-ambiguos), Kiel (404 kein Beleg), Dortmund (Maerz-2026 Fassung), Gelsenkirchen (Altfassung 25.AeS kursiert). Muster: viele lokale PDFs sind AeLTERE Fassungen; der live-recherchierende claude.ai-Reviewer ist oft aktueller. KONSEQUENZ fuer Global-Decision #4: vor Live braucht JEDE Stadt einen Live-Fassungs-Abgleich (Datum + Betrag), nicht nur die geflaggten. Das ist ein eigener Arbeitsschritt nach den Einzel-Reviews.

## BATCH 10 vorbereitet (Krefeld/Leipzig/Leverkusen) — Koordinaten-Selbstverifikation
- KREFELD: MAJOR Einheiten-Frage. 2.760 (1.5 Einfachbelegung) ist "NUR WIEDERERWERB UND VERLAENGERUNG" - nicht Ersterwerb. Neu offenbar nur Zweifachbelegung (1.6 = 3.450/Grabstelle) -> wie Mainz evtl. KEIN neues Einzel-Wahlgrab. Beisetzung 1.282 (1.1 Erwachsene ab 6J) bestaetigt. Fassung aktuell (tritt 01.01.2026 in Kraft). Reviewer: korrekter Ersterwerbspreis fuer 1 Sarg? Reihengrab 1.860 als Einzel-Variante?
- LEIPZIG: OK (selbst-verifiziert). 968 (3a Erdwahlgrab einstellig, 20J) + 446 (1a einfache tiefe Bestattung). Reihengrab 415.
- LEVERKUSEN: OK-Werte, DATUM UNKLAR. 164,01/J (1.3 Erdwahlgraeber) + 1.270,98 (2.4 Wahlgraeber Erdbestattung) koordinaten-bestaetigt; "2003" ist nur Gesetzesbezug, Satzungsdatum unklar -> Reviewer versionsaktuell pruefen.

## BATCH 9 (Heidelberg/Karlsruhe/Kiel) — teilweise FINAL 06.07.
- HEIDELBERG: OK. 2.420 (4.2.3 Einzelgrab 2./3. Reihe) + 1.190 (2.1) "sauber belegt und aktuell". SCOPE: Leichenhalle 260 als Regel-Zusatz. EMPFEHLUNG: Reihenlage als Spanne 2.420-2.750 ausweisen (2./3. vs 1. Reihe) statt Fixwert. Reihengrab 1.390 = andere Grabart (18J, Info).
- KARLSRUHE: OK + versionsaktuell (Fassung 01.01.2026). 100/J (2.1.1 an Wegen/Feldern) + 1.463 (4.1.1 Erdbestattung). Single bestaetigt (§5 Abs 1, je Grabstelle). WICHTIG: KEIN Scope-Zuschlag - §6 Abs 1: 1.463 enthaelt BEREITS Leichenhalle+Trauerhalle+Oeffnen/Schliessen+Einsenken (Halle obendrauf = Doppelzaehlung!). Nur situative 4.4.x-Zuschlaege. Ruhezeit-Hinweis: Ortsteile Hohenwettersbach/Stupferich/Wettersbach/Wolfartsweier 25J.
- KIEL: Reviewer laeuft noch (Web-Recherche; 2017er-Merkblaetter veraltet, sucht April-2025-Satzung).

## KIEL — UNRESOLVED (Re-Collect noetig)
Reviewer: Grabtyp-Zuordnung + Version-Logik sauber, aber die 2 Euro-Zahlen (1.767,20 / 654,60) UNBELEGT. Einzige amtliche kiel.de-Zahlen sind 2017 (niedriger). Aktuelle maßgebliche Fassung = "Gebuehrensatzung fuer die Friedhoefe der Landeshauptstadt Kiel, 27.03.2025" (Kieler Ortsrecht, nicht der tote Lokal-Link). TODO: aktuelle 2025-Satzung ziehen + 1.767,20/654,60 Ziffer-gegen-Ziffer nachlesen. Bis dahin Kiel-Werte NICHT freigeben.

## KIEL-FETCH-VERSUCH (06.07.) — gescheitert, => BOLLE-AKTION
WebFetch grabarten.php/service.php = nur JS-Menue (kein Gebuehreninhalt). curl ortsrecht.php = leer (Session/JS-Gate). Kieler amtliche Satzung 27.03.2025 ist ueber Web-Automatik nicht greifbar.
=> BOLLE-AKTION: aktuelle "Gebuehrensatzung fuer die Friedhoefe der LH Kiel, 27.03.2025" aus dem Kieler Ortsrecht manuell laden + in scratch/satzungen/kiel.raw ablegen (oder Link geben), dann Kiel neu reviewen. Bis dahin Kiel-Werte (1.767,20/654,60, Stand unklar) NICHT freigeben.

## BATCH 10 (Krefeld/Leipzig/Leverkusen) — FINAL 06.07.
- KREFELD: KORREKTUR 2.760 -> 3.450. Kein neues Einzel-(Einfachbeleg-)Wahlgrab erwerbbar; 1.5 (2.760) nur Wiedererwerb/Verlaengerung bestehender Graeber. Neu-Erwerb Sarg-Wahlgrab nur 1.6 "Zweifachbelegung je Grabstelle" = 3.450 (einzelne Grabstelle kaufbar, keine Mindestabnahme; man zahlt 2-Sarg-Kapazitaet, belegt 1). Beisetzung 1.282 (I.1.1 Erwachsene ab 6J) OK + versionsaktuell 2026. Reihengrab 1.860 = guenstigste Einzel-Variante (wie Mainz-Muster). Scope quasi-Standard: Verbau von Hand 285 + Abfuhr Erdaushub 171.
- LEIPZIG: Werte OK. 968 (§6 Nr.3a Erdwahlgrab einstellig) + 446 (§9 Nr.1a oeffnen/schliessen einfache tiefe Bestattung) exakt + versionsaktuell (ab 01.09.2024). SCOPE +502 PFLICHT: §8 Nr.1 Friedhofsnutzungs-/-unterhaltungsgebuehr 20J = 420 (Pflicht, grabartunabhaengig) + §9 Nr.2a Grundherstellung Erdgrab = 82 -> Mindestgebuehr 1.916 statt 1.414. Label "oeffnen/schliessen" (Beisetzung=Urne).
- LEVERKUSEN: Werte 164,01/J (1.3) + 1.270,98 (2.4) = Fassung 01.05.2023. 27. Aenderung ab 01.01.2026 existiert (Rat 15.12.2025), exakte neue Saetze UNBESTAETIGT (Ortsrecht-PDF "Stand 01/26" zeigt widerspruechlich noch 2023er-Zahlen) -> VERSION-FLAG: 2026-Saetze pinnen vor Live. Single OK, kein grosser Scope (nur situativ: Trauerhalle 214,51/Matten 17,01/Grabmal 37,80). Reihengrab-Beisetzung waere 2.1 = 1.126,11 (nicht 2.4).

## BATCH 11 vorbereitet (Ludwigshafen/Luebeck/Magdeburg) — Koordinaten-Selbstverifikation
- LUDWIGSHAFEN: 2.469 (1.1 Wahlgrab Erdbest, einstellig) + 1.168 (Beis 1.1 ab 6J) koordinaten-bestaetigt. Fassung 14.12.2020 -> Version pruefen. LAUFZEIT 30 J (unser "20J" falsch, Fix). Abgrenzung 1.7 Partnergrab (2.359).
- LUEBECK: 1.620 (A(1.1) einstellig, Spalte1 v. einstellig/2-neben/2-ueber/Kind) + 928 (=B(1) Bestattung 370 + Grabmachen 2,50m 558) koordinaten-bestaetigt. Fassung 2015 -> Version pruefen. 20 J (Verl. 1/240).
- MAGDEBURG: 1.424 ((2) Erdwahlgrab 20J) + 1.195 (Oeffnen/Schliessen) + Reihengrab 1.230 bestaetigt. Fassung m. Aenderung 2023. Sauber.

## BATCH 12 vorbereitet (Moenchengladbach/Muenchen/Muenster) — Koordinaten/Text-Selbstverifikation
- MOENCHENGLADBACH: 1.659 (1.1.1 Erdgrabstaette einstellig, 25J) + 937 (2.1 Bestattung) koordinaten-bestaetigt. Datum: Aenderungen bis 2020 -> Version pruefen. Premium A3-Feld 1.1.8.1 = 2.413 nicht verwendet (korrekt).
- MUENCHEN: 84/J (Erdgrabstaette Nutzung) + 1.665 (§6 "Beisetzung eines Sarges mit Oeffnen/Schliessen") aus lokalem .txt bestaetigt (muenchen.raw = MS-Word-HTML, aber .txt lesbar). -> Reviewer web-verify versionsaktuell.
- MUENSTER: 1.812 (A.7 Wahlgrab je Grabstelle) + 617 (B.22 Bestattung Wahlgrab) aus amtlichem Tarif AB 01.01.2024 bestaetigt (muenster.raw kein PDF, aber .txt = saubere HTML-Tabelle). Sauber + aktuell. 30J (Verl. 1/30). Reihengrab 956.

## BATCH 11 (Ludwigshafen/Luebeck/Magdeburg) — FINAL 06.07.
- LUEBECK: OK + versionsaktuell. Offizielles Ortsrecht = Fassung 2011 i.d.F. 31.03.2015 (identisch zu unserem PDF, keine neuere). 1.620 (A.1.1 einstellig Vorwerk/Waldhusen) + 928 (=370 B.1a Bestattung + 558 C.1a Oeffnen/Schliessen 2,50m) ALLE DREI bestaetigt - Komposit war exakt richtig. REIHENGRAB-FIX: unser 1.040 war Urnenreihengrab (A.4.1); Sarg-Reihengrab = A.3.1 = 1.280. MINOR: "20 J" steht in Friedhofssatzung (nicht Gebuehrensatzung) - dort gegenpruefen.
- MAGDEBURG: Werte OK + versionsaktuell (Amtsblatt Nr.02 v. 02.02.2024). 1.424 ((2) Erdwahlgrab 20J) + 1.195 (Oeffnen/Schliessen). Single (1 Sarg + bis 2 Urnen). SCOPE MAJOR: Friedhofsunterhaltungsgebuehr 48,90/Jahr (III.) = ~978 ueber 20J (jaehrlich faellig!) + Graburkunde 17 + Antrag 37 + Grabmal 188-239 -> real ~3.650 statt 2.619.
- LUDWIGSHAFEN: VERSION-MAJOR/UNSICHER. 2.469 (1.1 einstellig Wahlgrab) + 1.168 = Fassung Ende 2020 (Anlage 14.12.2020). Stadtrat beschloss 07.11.2022 + Sitzung 11.12.2023 Aenderungen; ob 2.469/1.168 unveraendert = UNBELEGT (Ortsrecht-PDF 7-09 gg. Auto-Abruf gesperrt). NICHT als versionsaktuell ausweisen -> konsolidierte Fassung manuell pruefen. Laufzeit 30 J bestaetigt (unser "20J" war falsch). Single (einstellig, Abgrenzung 1.7 Partnergrab 2.359).

## SCOPE-Sammlung erweitert: Magdeburg +Unterhaltung 48,90/J(~978), Leipzig +502, Erfurt +506, Halle +FUG180, Krefeld +Verbau285, Freiburg +72, Augsburg +34/J, Chemnitz +141, Berlin +52, Heidelberg +Leichenhalle260. -> jaehrliche Unterhaltungsgebuehren (MG 48,90/J, Augsburg 34/J, Hamm ~37/J) sind ein wiederkehrender, grosser blinder Fleck des 2-Komponenten-Modells.

## BATCH 13 vorbereitet (Nuernberg/Oberhausen/Oldenburg) — Koordinaten-Selbstverifikation
- NUERNBERG: 79/J (4.1.1 Wahlgrab einfachtief/einfachbreit) + 1.569 (1.1.2 Beisetzung Erwachsener) bestaetigt. "Reihengrab 99"-Info war Familiengrab 4.2.1 (korrigieren). Datum verify.
- OBERHAUSEN: 2.098 (Wahlgrab 30J) + 1.328 (2.1 Beisetzung Wahlgrab) bestaetigt + VERSIONSAKTUELL 2026 (ab 01.04.2026). Reihengrab Sarg 742+1.172. Sauber.
- OLDENBURG: 1.070 (3.2.3 Wahlgrab ab 5.Lj je Stelle) + 597 (4.2 Beisetzung) bestaetigt + versionsaktuell (ab 01.01.2024). Reihengrab 3.1.2 = 1.002. Moegl. Scope 5.1.2 = 192 (pruefen).

## BATCH 12 (Moenchengladbach/Muenchen/Muenster) — teilweise FINAL 06.07.
- MOENCHENGLADBACH: OK, kein MAJOR. 1.659 (1.1.1, Standard ueber alle 13 Friedhoefe; A3-Feld 2.413 = +45% Sonderlage, korrekt NICHT verwendet) + 937 (2.1). Version: 5. Nachtrag 13.12.2024 (Fassungszitat aktualisieren); 6.-Nachtrag-2026-Restrisiko -> live-PDF vor Go-live pruefen. Trauerhalle 298 situativ.
- MUENSTER: OK. 1.812 (A.7) + 617 (B.22) bestaetigt + versionsaktuell (ab 01.01.2024). Alles ausser Bestattung optional (OVG-Muenster: keine Einheitsgebuehr fuer ungenutzte Leichenzelle/Kapelle). 30J (1.812/30 = 60,40/J Verl.); MINOR: staedt. Merkblatt nennt 1/30-Satz nicht woertlich. Grabmalgenehmigung 54 separat. Sauber.
- MUENCHEN: Reviewer laeuft noch (web-verify Satzung 801, deckt "Gebuehren 2024-2026" -> 84/J + 1.665 plausibel aktuell).

- MUENCHEN (FINAL): 84/J + 1.665 BESTAETIGT versionsaktuell (Satzung ab 01.07.2024, Kalkulation 2024-2026; 84 = Erdgrab 2.+ folgende Reihen §4 Abs.1 I b [2021-23: 68], 1.665 = Basisleistung Erdbestattung inkl. Oeffnen/Schliessen). NUANCEN: (a) 84 ist BILLIGSTE Zeile; Standard 1. Reihe 134/J, Hecke 140, Mauer 160 (+50% moegl.) -> 84 als "guenstigste" vertretbar, aber nicht repraesentativ. (b) RUHEZEIT 10 J (nicht 20!) -> Normalisierung: 84x10=840 + 1.665. (c) -30% moegl. bei echtem Einzelbelegungs-Grab (§4) = 58,80/J, feldabhaengig UNSICHER. (d) Netto/USt: einige 2024er-Positionen auf "Preise + USt" umgestellt.

## BATCH 14 vorbereitet (Osnabrueck/Potsdam/Rostock) — Koordinaten/Text-Selbstverifikation
- OSNABRUECK: 74/J (3.1 Erdwahlgrab je Grabstelle je Jahr) bestaetigt. BEISETZUNG-VERDACHT: unser 450 = "1.1 Bestattung in REIHENgrabstelle"; fuer WAHLgrab gilt 1.2.x (1.2.1 Erdbest ueber 6J = 100?). -> Reviewer korrekte Wahlgrab-Beisetzung klaeren. (osnabrueck.raw ohne Koordinaten-Output; .txt-Struktur genutzt.)
- POTSDAM: 68/J (1.4 Erdeinzelwahlgrabstaette) bestaetigt + aktuell (06.12.2023). BEISETZUNG-VERDACHT: unser 767 = "2.2 GRUFT oeffnen/schliessen"; Sektion 2 listet NUR Gruft (2.1=384, 2.2=767) + Sargtraeger 102. Normale Erd-Sargbestattung unklar -> Reviewer klaeren (384? oder jede Erdbest. = Gruft?).
- ROSTOCK: 940 (A.1 Erdwahlgrab einstellig, 20J) + 560 (Erdgrabstelle oeffnen/schliessen) bestaetigt. Reihengrab C.1 = 940 (gleich). Datum verify. Moegl. Pflege/Unterhaltung-Scope.

## BATCH 13 (Nuernberg/Oberhausen/Oldenburg) — FINAL 06.07.
- NUERNBERG: OK. 79/J (4.1.1 Wahlgrab einfachtief/einfachbreit) + 1.569 (1.1.2 Beisetzung Erwachsener) bestaetigt + versionsaktuell. RUHEZEIT ~10 J (Grabnutzung 79x10=790, nicht 79!). Scope +59 (Annahme). WICHTIG: Wahlgrab 79/J IST guenstigste Option; Reihengrab 99/J TEURER (invertiert; NICHT als Template auf andere Staedte). UNSICHER: exakte Laufzeit Neuerwerb bei Verwaltung gegenchecken.
- OBERHAUSEN: OK. 2.098 (Wahlgrab 30J) + 1.328 (2.1) koordinaten-bestaetigt + versionsaktuell 2026 (ab 01.04.2026). Struktur korrekt (1x Nutzung + 1x Beisetzung). Scope UNSICHER: Verwaltungs-/Genehmigungs-/Einfassungsgebuehr (§19 2025-Satzung) evtl. obendrauf -> Genehmigungen/Verwaltung-Abschnitt pruefen. Reihengrab 742+1.172=1.914.
- OLDENBURG: 1.070 (3.2.3) + 597 (4.2) bestaetigt + versionsaktuell (ab 01.01.2024). SCOPE MAJOR: 5.1.2 Grabumrandung 192 = PFLICHT (§16 Abs 3 Zwangsleistung) -> real 1.070+597+192 = 1.859. 25J bestaetigt (Benutzungssatzung §13). Reihengrab 1.002 nicht relevant.

## BATCH 15 + WIESBADEN vorbereitet (letzte 4) — Koordinaten-Selbstverifikation
- SAARBRUECKEN: 720 (Koerperwahlgrab je Stelle 1 Koerper, 20J) bestaetigt. BEISETZUNG-VERDACHT: unser 1.755 = "obere Belegung je Bestattung" (= TIEFGRAB 2. Koerper); normale Einzelbeisetzung = "Koerpererdgrab je Beisetzung 1.100" -> Reviewer klaeren (1.100 statt 1.755?). Datum 08.12.2020/ab 01.04.2021 -> Version pruefen.
- STUTTGART: 2.142 (B 1.01 Wahlgrab 20J) + 1.248 (A 1.01 Erdbestattung inkl. Oeffnen/Schliessen) bestaetigt + VERSIONSAKTUELL (19.12.2024). Reihengrab 987. Sauber.
- WUPPERTAL: 2.436,83 (3.7 Sargwahlgrab Nutzung 20J) + 815,95 (1.7 Sargwahlgrab Bestattung) bestaetigt. Reihengrab 3.x=1.849,65. Datum verify.
- WIESBADEN: 3.383 (1.2.1 Erdwahlgrab je Grabstelle 30J) + 674 (2.2.1 Bestattung ab 5.Lj) bestaetigt (674 war frueher als "fehlt" geflaggt, ist da). Moegl. Scope 1.3.1 = 112. Datum (Satzung 3. Sept., Jahr?) verify.

## BATCH 14 (Osnabrueck/Potsdam/Rostock) — teilweise FINAL 06.07.
- POTSDAM: OK - VERDACHT WIDERLEGT. 767 ist KORREKT: 2.1(384)/2.2(767) unterscheiden Alter (bis5J / ueber5J), NICHT Grabtyp; beide "Gruft oeffnen/schliessen" = Potsdams generischer Begriff fuer JEDE Erdgrabstelle. Erwachsener = 767. 68/J (1.4 Einzelwahl) + 767 (2.2) bestaetigt + aktuell (06.12.2023). Single.
- ROSTOCK: OK. 940 (A.1 einstellig) + 560 (Erdgrabstelle oeffnen/schliessen) bestaetigt, 1 Sarg exakt (bis 4 Urnen zusaetzl. moegl. +190/260). 20J bestaetigt. KEIN Pflicht-Scope (Unterhaltung + Grabmalgenehmigung anteilig in 940 drin; Feierhalle 150/Aufbewahrung 60 optional). Reihengrab-Info 940 = falsch (nicht verwenden).
- OSNABRUECK: Reviewer laeuft noch (450-Beisetzungsfrage, web-research).

## BATCH 15 (Saarbruecken/Stuttgart/Wuppertal) + Osnabrueck — FINAL 06.07.
- WUPPERTAL: OK + BRANDAKTUELL. 2.436,83 (3.7 Sargwahlgrab) + 815,95 (1.7) bestaetigt gg. Bekanntmachung Nr.48/2025 (18.12.2025, 16. Aenderung, gueltig ab 01.01.2026); 3.2 Sargreihengrab 1.849,65. Konsolidierte Stadtrecht-PDF widerspruechlich, aber Bekanntmachung ist rechtsverbindlich = unsere Werte.
- STUTTGART: OK. 2.142 (B 1.01) + 1.248 (A 1.01 inkl. Oeffnen/Schliessen) bestaetigt + versionsaktuell (19.12.2024). SCOPE: Verwaltungsgebuehr Erdbestattung ~135 -> real ~3.525. Pflegevertrag-Bindung (Gaertner/Steinmetz) = Fremdkosten, nur bei gepflegten Anlagen, im Angebot als Fremdkosten kennzeichnen (nicht Gebuehr). 20J + Reihengrab 987 (andere Grabart).
- OSNABRUECK: MAJOR - VERDACHT BESTAETIGT + Version. Beisetzung 450 = Ziffer 1.1 REIHENgrabstelle = FALSCHE Zeile; Wahlgrab braucht 1.2 Wahlgrabstaette. Parallelvergleich: 1.1.1 (Reihe Erd) = 82 vs 1.2.1 (Wahl Erd) = 100. Exakter 1.2-Wert nicht gg. Primaer-PDF verifizierbar (Stadt-Server bot-blockiert). ZUSAETZLICH: Grabnutzung 74/J x MIN 25 J Ersterwerb = 1.850 (nicht 74!); Ruhezeit 20J. Werte evtl. Altfassung (Rat 03.12.2024/2025) -> gg. 2026-PDF pruefen. => RE-COLLECT wie Kiel (Bolle/manuell: aktuelle Osnabrueck-Satzung, Ziffer 1.2 Wahlgrab-Beisetzung ablesen).

## SAARBRUECKEN + WIESBADEN — FINAL 09.07. (alle 50 durch!)
- SAARBRUECKEN: OK - VERDACHT WIDERLEGT. 1.755 ist KORREKT: "obere Belegung" = Regel-/Standardtiefe (nicht 2. Koerper!); Zeile nennt ausdruecklich Wahlgrab (Ziff II.I Koerperbestattung "Wahl-,...Tiefgrab, obere Belegung je Bestattung 1.755"). Untere Belegung (tiefe Erstbelegung Tiefgrab) = 1.925 (teurer). Die 1.100 = Ziff II.II ASCHEbeisetzung (Urne ins Koerpergrab) = falsche Zeile fuer Sarg. 720 (Koerperwahlgrab) + 1.755 bestaetigt.
- WIESBADEN: OK-Werte, ZITAT-FIX. 3.383 (1.2.1 Erdwahlgrab ausserhalb Reihengraeberabteile 30J) + 674 (2.2.1 Oeffnen/Schliessen) KORREKT + versionsaktuell (Fassung i.d.F. 27.01.2022, 19. Erg.-Lief.). MAJOR nur ZITAT: unser "3. September 1992" = ausser Kraft gesetzte Vor-Euro-Vorgaengerordnung -> Zitat auf 27.01.2022 korrigieren (Werte unveraendert). 1.3.1/112 = KEIN zulaessiger Pflichtaufschlag (Scope-Guess fallengelassen).

## ===== RE-AUDIT KOMPLETT: 50/50 EINZEL-REVIEW DURCH (09.07.2026) =====
3 Beisetzungs-Verdachtsfaelle aufgeloest: Osnabrueck = ECHTER Fehler (450->~100); Potsdam + Saarbruecken = WIDERLEGT (Verdacht war Flattened-Text-Artefakt, Reviewer klaerte). Master-Kategorisierung: _dev/docs/FRIEDHOF-MASTER-SUMMARY.md.
