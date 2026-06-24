# OFFENE-REVIEW-PUNKTE — FRIEDHOF (geklärte False-Positives & bewusste Entscheidungen)

> Schwester zu `OFFENE-REVIEW-PUNKTE.md`, aber für Friedhofseiten (Friedl). Reviewer-Pflicht:
> diese Punkte NICHT erneut als Finding melden (geprüft). Writer-Pflicht: verworfene Findings
> hier nachtragen (Datum, Beleg). Pflichtteil jedes Bau-/Review-Prompts (vgl. `_dev/FRIEDL.md`).

## Geprüfte False-Positives

- *(noch keine — Datei neu angelegt 23.06.2026 mit `lint-friedhof.py`)*

## Bewusste Entscheidungen (kein Defekt)

- **Ruhezeit steht nicht in der Gebührenübersicht** (Hamburg AöR): kommt aus Friedhofssatzung/
  Landes-BestattG, separat belegt. Ein target-blinder Reviewer kann sie aus dem GBO-Auszug nicht
  prüfen → seine UNSICHER-Markierung ist erwartbar, kein Defekt (Lektion FRIEDHOF #5).
- **Eine Gebührenübersicht je Träger** deckt mehrere Friedhöfe (Ohlsdorf/Öjendorf/Volksdorf/
  Wohldorf laufen über denselben AöR-Record). Identische Gebührenzahlen auf Schwesterseiten sind
  KEIN Konsistenz-Finding, sondern Single-Source-Prinzip (Lektion FRIEDHOF #1).
- **Hallengebühren je Standort verschieden** trotz gemeinsamer Ordnung (Tarifstellen 3011/3012/3013):
  beabsichtigt, nicht widersprüchlich — die Stufe richtet sich nach dem Standort.

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
