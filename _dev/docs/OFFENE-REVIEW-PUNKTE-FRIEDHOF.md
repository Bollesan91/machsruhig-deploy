# OFFENE-REVIEW-PUNKTE — FRIEDHOF (geklärte False-Positives & bewusste Entscheidungen)

> Schwester zu `OFFENE-REVIEW-PUNKTE.md`, aber für Friedhofseiten (Friedl). Reviewer-Pflicht:
> diese Punkte NICHT erneut als Finding melden (geprüft). Writer-Pflicht: verworfene Findings
> hier nachtragen (Datum, Beleg). Pflichtteil jedes Bau-/Review-Prompts (vgl. `_dev/FRIEDL.md`).

## Geprüfte False-Positives

Aus dem 50/50-Einzel-Review (09.07.2026) — Reviewer irrte, Primärquelle bestätigte UNSEREN Wert. **Nicht erneut melden:**

- **Hagen — Grabnutzung 1.530 + Beisetzung 570 sind KORREKT.** Ein Reviewer meldete 1.465/535/30J als „aktuell". Das war eine ÄLTERE Fassung. Primärquelle `hagen.raw` = VI. Nachtrag (beschlossen 11.12.2025, neuer als die Reviewer-Quelle); pdfplumber-Koordinaten: „4.80 Wahlgrabstätte Sargbestattung = 1.530" + Beisetzung 570 (Grabaushub ab 5. Lj). Reviewer nutzte veraltete Web-Fassung.
- **Potsdam — Beisetzung 767 ist KORREKT für Erwachsene.** Verdacht „767 = Gruft-Sonderfall" ist falsch: 2.1 (384) / 2.2 (767) unterscheiden das ALTER (bis 5 J / über 5 J), NICHT den Grabtyp. „Gruft öffnen und schließen" ist in Potsdam der generische Sammelbegriff für das Öffnen/Schließen JEDER Erdgrabstelle.
- **Saarbrücken — Beisetzung 1.755 ist KORREKT.** Verdacht „1.755 = Tiefgrab-Oberbelegung (2. Körper)" ist falsch: „obere Belegung" = die REGEL-/Standardtiefe; die Zeile (Ziff. II.I Körperbestattung) nennt ausdrücklich das Wahlgrab. Die 1.100 stehen unter Aschebeisetzung (Urne ins Körpergrab) = falsche Zeile für einen Sarg. Untere Belegung (tiefe Erstbelegung Tiefgrab) = 1.925.

## Bewusste Entscheidungen (kein Defekt)

- **Ruhezeit steht nicht in der Gebührenübersicht** (Hamburg AöR): kommt aus Friedhofssatzung/
  Landes-BestattG, separat belegt. Ein target-blinder Reviewer kann sie aus dem GBO-Auszug nicht
  prüfen → seine UNSICHER-Markierung ist erwartbar, kein Defekt (Lektion FRIEDHOF #5).
- **Eine Gebührenübersicht je Träger** deckt mehrere Friedhöfe (Ohlsdorf/Öjendorf/Volksdorf/
  Wohldorf laufen über denselben AöR-Record). Identische Gebührenzahlen auf Schwesterseiten sind
  KEIN Konsistenz-Finding, sondern Single-Source-Prinzip (Lektion FRIEDHOF #1).
- **Hallengebühren je Standort verschieden** trotz gemeinsamer Ordnung (Tarifstellen 3011/3012/3013):
  beabsichtigt, nicht widersprüchlich — die Stufe richtet sich nach dem Standort.
- **München + Nürnberg Ruhezeit = 10 Jahre** (nicht 20): bewusst, so in der Satzung. Jahresmodell × 10 für die 20-J-Normalisierung anpassen — keine „Laufzeit-Fehler"-Meldung.
- **Karlsruhe / Münster / Rostock: KEIN Scope-Zuschlag** (Leichen-/Trauerhalle etc.). Diese Leistungen sind bereits in der Bestattungsgebühr enthalten (Karlsruhe §6 Abs 1; Rostock Anlage A). Sie obendrauf zu rechnen wäre Doppelzählung — kein „fehlende Pflichtgebühr"-Finding.
- **Heidelberg: 2.420 (4.2.3 Einzelgrab 2./3. Reihe)** bewusst als repräsentative Standard-Position gewählt statt 4.2.1 (1. Reihe, 2.750). Beide sind Einzel-Wahlgräber; die günstigere Regel-Lage ist vertretbar.
- **Krefeld: 3.450 (1.6 Zweifachbelegung je Grabstelle)** bewusst als Grabnutzung: ein NEUES Einzel-(Einfachbeleg-)Wahlgrab ist in Krefeld nicht erwerbbar (1.5/2.760 nur Wiedererwerb). Kein „falscher Grabtyp"-Finding — es ist das einzige neu kaufbare Sarg-Wahlgrab.

## Linter-mechanisiert (nicht mehr Reviewer-Thema — `lint-friedhof.py` fängt es)

- **Anführungszeichen-Parität** (Lektion FRIEDHOF #3b): ASCII-`"` als typografisches Schließzeichen
  statt deutsch `„ "` → Gate **F3** (sichtbarer Text + JSON-LD-Werte). Am 23.06. auf Hub + Ohlsdorf
  9× korrigiert (`_dev/audit/fix-friedhof-quotes.py`).
- **Beispielsummen-Arithmetik** → Gate **F1** (Σ der Posten = ausgewiesene Summe, inkl. Multiplikation).
- **Gebühr ≠ verifizierter Träger-Record** → Gate **F9** (Tarifstelle→Betrag-Cross-Check).
- **Standalone-Breadcrumb auf nicht gebauten Hub** (Lektion FRIEDHOF #3a) → Gate **F4**.
- **Provenienz / Stand sichtbar** (gültig-ab + Quelle + „geprüft am") → Gates **F2/F6**.

## Bekannte Linter-Grenzen (bewusst zurückgestellt, niedrige Wahrscheinlichkeit)

Aus dem 2.+3. Review (23.06.) — gefixt: M1–M7/c1/c2/m3/m5 (Welle 2) sowie M2/M3/M6/m9/m10/m12
(Welle 3: Datums-/Record-Crash, Cent-genaue Beträge, `>`-Attribut-Leak, einstellige Daten,
Soll-Zahl vor €). Diese Rest-MINOR bleiben dokumentiert statt gefixt (niedrige Wahrscheinlichkeit,
Konvention-gebunden) — wenn eine künftige Seite sie verletzt, hier nachschlagen statt neu melden:
- **F1**: Posten-Zeile ohne `=` (z. B. mit `:`) wird verworfen → mögliche False-FAIL. Konvention:
  jede Posten-Zeile endet auf `= NNN €`, Summe in `<span class="sum">`.
- **F1**: mehrere Posten in EINER Zeile ohne `<br>` → nur der letzte zählt. Konvention: ein Posten je Zeile.
- **F1**: `.fh-calc`-Box ganz ohne `<span class="sum">` → Arithmetik nicht prüfbar (übersprungen).
- **F3**: ein Zoll-Maß `"` INNERHALB eines korrekten `„…"` (z. B. `„das 2" Rohr"`) kann MISQUOTE
  auslösen. Selten auf Friedhofseiten; im Zweifel deutsche Quotes ohne eingebettetes ASCII-`"`.
- **F7**: Wertungs-Phrasen sind Substring-Treffer — eine Seite, die eine Phrase ausdrücklich
  verneint/zitiert („wir bewerten nicht: …"), würde fälschlich anschlagen. Auf Friedhofseiten unüblich.
- **F9**: mehrere passende Träger-Records für einen Slug → keine Prüfung (nur W2). Slug-Konvention
  ist `…/<friedhof>/index.html`; Flat-File `…/<friedhof>.html` würde nicht matchen.

## Offen (echte Backlogs — Status darf geprüft werden, nicht als „neu" melden)

- **Aktualitäts-Monitoring / Change-Detection je Träger-Satzung** fehlt noch (PDF-Hash brüchig).
  FRIEDL: „nicht in Vollserie gehen, bevor das steht." Bis dahin Q1-Sweep + Verfall-Logik (F6).
- **Aggregationsseiten** `/friedhoefe/<bundesland>/<kreis|ort>/` für Friedhöfe unter dem
  Substanz-Gate (F5) noch nicht gebaut — die meisten der ~32.000 werden Zeile statt eigene URL.
- **Öjendorf/Volksdorf/Wohldorf-Ohlstedt**: im Hamburg-Hub noch Platzhalter (Link → `/bestatter/hamburg/`).
