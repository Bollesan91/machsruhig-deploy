# Rollout-Prompt — Datentransparenz-Strategie umsetzen (Stand 19.06.2026)

> Zum Einfügen in eine neue Session. Ziel: das besprochene Konzept erfassen, planen und umsetzen —
> bestehendes Design, Seitenstruktur und Content-Niveau konsistent auf hohem Niveau halten.

---

Du arbeitest am Projekt **machsruhig.de**. Setze die **Datentransparenz-Strategie** um (Angebots-
standard / Transparenz Partner / Kostenradar). Oberster Maßstab: **bestehendes Design, Seiten-
struktur und Content-Stärke konsistent und auf hohem Niveau halten** — nichts verwässern, nichts
fremdkörpern.

## 0. Zuerst lesen (Pflicht — Stufe 0, nicht delegierbar)
- `STRATEGIE.md` (besonders **Abschnitt 15 Datentransparenz-Strategie** + Content-Klassen,
  CTA-Hierarchie, Monetarisierung, Trauer-Schutz, Quality-Gates, Leitplanken).
- `_dev/strategie/transparenz-partner-konzept.md` (v5 — das operative Konzept).
- `_dev/docs/LEKTIONEN.md` + `_dev/docs/OFFENE-REVIEW-PUNKTE.md` (Findings-Gedächtnis + geklärte
  False-Positives).
- `_dev/HELPER-V4.1.md` (Qualitätssystem) und die Memory `datenstrategie-echte-angebote`.
- Arbeitsumgebung: Clone `C:/Users/Bolle/AppData/Local/Temp/machsruhig-deploy`, Repo
  `Bollesan91/machsruhig-deploy`, Netlify-Deploy auf Push `main`, PAT-Setup nach Clone,
  Git-Identität `-c user.name="Bollesan91" -c user.email="cbollweg@gmx.de"`.

## 1. Phase 1 — Livestand VOLLSTÄNDIG erfassen (read-only, keine Änderung)
1. **Seiten-Inventar** nach Content-Klasse/Seitentyp (STRATEGIE Abschnitt 4): alle HTML, je Typ
   (Hub/Info/Tool/Vorsorge/Lokal-Stadt/Lokal-BL/Legal/Trust).
2. **Design-System extrahieren:** Markenfarben, Fonts, und die wiederkehrenden Komponenten —
   Header/Nav, Footer, Hero, Karten, FAQ-Akkordeon, Tabellen, Ampel, CTA-Buttons,
   Redaktions-/Autor-Block, Methodik-/Quellen-Block, Disclaimer. WO sind sie definiert
   (CSS-Datei/Inline/Partial-Muster)? Halte die exakten CSS-Klassen/Strukturen fest.
3. **Konzept-Berührungspunkte kartieren:** Angebotsprüfer (Logik + UI), Kostenrechner,
   `/methodik#kostenmodell` (15-Posten-Schema), Stadt-/BL-Seiten (Kostendarstellung + Bestatter-
   Bezug), Footer „Bestatter finden", bestehende Bestatter-/Lead-Strukturen.
4. **Linter-Baseline** `python _dev/scripts/lint-site.py` (0 FAIL festhalten); lokal rendern, um
   Design-Patterns real zu sehen (predeploy_local_render_check beachten — mobile lokal nicht prüfbar).
5. **Output:** strukturierte Ist-Stand-Karte (Tabelle: Bereich · Datei(en) · Komponente/Pattern ·
   Relevanz fürs Konzept).

## 2. Phase 2 — Gap-Analyse: was muss flächendeckend geändert + was neu entwickelt
**A) Flächendeckende Änderungen am Bestehenden (Konsistenz-getrieben):**
- Terminologie/Claims auf die **drei kanonischen Namen** + den Leitsatz ausrichten („verständlichster
  statt günstigster"). KEINE neuen Namen.
- Das **15-Posten-Schema** als gemeinsame Sprache zwischen Kostenmodell, Kostenrechner,
  Angebotsprüfer und (künftig) Angebotsstandard prüfen und angleichen — Drift = YMYL-Defekt
  (Single-Source-Prinzip, Lektion #43).
- Interne Verlinkung + Nav/Footer: wo Standard/Partner/Radar eingebunden werden — **respektiert
  CTA-Hierarchie + Trauer-Schutz + Phase-F-Gating**.
- Angebotsprüfer: die Transparenz-Kriterien als lebenden Check spiegeln — nur wenn ohne Substanzbruch.
**B) Neu entwickeln (Concept-MVP, in Bau-Reihenfolge):**
1. **Angebotsstandard-Spec-Seite** (+ maschinenlesbares Eingabe-Schema) — Fundament, keine PII,
   kein Backend, keine Rechtshürde; sofortiger SEO-/Autoritäts-Anker.
2. **Öffentliche Kriterienseite** (Vergabeprozess · Kriterien · Aktualisierung · Entzug · Grenzen
   der Prüfung · Finanzierung · Hinweis-/Beschwerdefunktion).
3. **„Transparenz Partner werden"-Seite** (+ Partnerbrief-Tonalität).
4. **Transparenzprofil-Template** je Bestatter („keine Qualitätsbewertung" prominent).
5. Später (gated): Kostenradar/Stadt-Integration, Transparenz-Karte, Anbieter-Cockpit.
- Je neue Seite **vorab zuweisen:** Content-Klasse + Seitentyp + CTA-Stufen (STRATEGIE), Layout aus
  Bestandskomponenten, Pflicht-Bausteine (Redaktion/Autor, Stand, Quellen, Disclaimer, Schema.org),
  interne Links.

## 3. WIE ES AUSSEHEN MUSS (Konsistenz + Niveau — der eigentliche Auftrag)
- **Design:** ausschließlich bestehendes System (Markenfarben `#7A6B5D` / `#FAF8F5` / `#2D2319` /
  `#73655A` / `#866E45`, **Fraunces**-Headings / **DM Sans**-Body, vorhandene Komponenten/CSS-Klassen).
  KEINE neue Designsprache, kein Fremd-Framework. Mobil sauber.
- **Seitenstruktur:** jede neue Seite genau **eine** Content-Klasse; **statisches HTML** (Leitplanke
  4 — kein CSR für Content), Schema.org, interne-Link-Dichte nach STRATEGIE-Tabelle, **ein** Primär-
  CTA je sichtbarem Bereich.
- **Content-Stärke:** gleiche Substanz-Latte wie die besten Bestandsseiten — echte Zahlen,
  Primärquellen, Redaktions-/Autor-Block, Stand-Datum, Disclaimer, Methodik-Verlinkung. KEIN dünner
  Template-Klon (Leitplanke 2: Friedhofsnamen/€-Beträge/Quellen).
- **Konzepttreue:** je Baustein den **Vier-Faktoren-Filter** (Vertrauen · Daten · Beziehung · SEO/PR)
  nachweisen; **Drei-Namen-Disziplin**; **Trust-Leitplanken** (Selbstverpflichtung NICHT „Siegel";
  kein Pay-to-Rank; redaktionelle Mauer zwischen Benchmark und Lead-Geschäft); **Phasenmodell**
  (Standard/Spec jetzt = Authority-Hebel; Lead-Aktivierung = Phase F + Anwaltsprüfung).
- **Pietät/Trauer-Schutz + Quality-Gates 1–7** gelten unverändert (Gate 7 harter Blocker).

## 4. Verbote (damit nichts kaputtgeht)
- Monetarisierung/Lead-Aktivierung NICHT scharf schalten (bleibt Phase F).
- Kein „geprüft"/Siegel-Claim vor anwaltlicher Prüfung (UWG/BGH).
- Keine erzwungenen Badge-Backlinks (Google-Risiko) — Badge optional, neutraler Anchor.
- Keine leeren Radar/Report-Dashboards vor echten Daten („erst der Brunnen, dann die Wasserhähne").
- Keine neuen Produktnamen, keine neue Designsprache, keine CSR-Content-Seiten.
- Trauerseiten unangetastet (kein CTA, keine Monetarisierung — absolut).

## 5. Arbeitsweise (Helfer V4.1)
- **Stufe 0:** jede Norm/Zahl mit Rechts-/Geldfolge VOR dem Schreiben primärverifizieren
  (gesetze-im-internet.de / amtliche Landesportale / amtliche Stadt-Satzungen; Sekundärquellen nie
  Beleg; Fassungs-/Jahresstand prüfen — Lektion #54).
- **Stufe 1:** Linter `python _dev/scripts/lint-site.py` = **0 FAIL** vor jedem Commit/Deploy.
- **Stufe 2:** für JEDE inhaltliche/YMYL-Seite ein **unabhängiger target-blinder Reviewer-Tab**
  (claude.ai via Chrome-MCP, NUR Bolle-Device `2bee5aa2-fece-43e8-a9e6-ff739861775c`); für rein
  strukturelle/Design-Arbeit reicht Linter + Self-Verify + Live-Grep, aber **ausdrücklich ankündigen**.
- **Stufe 3:** jedes Finding selbst gegen die Primärquelle prüfen (Reviewer irrt in beide
  Richtungen), Diff-Re-Check seitenweit, **Gate = 0 offene MAJOR + Linter grün + Live-Smoke**.
- **Deploy-Disziplin:** Branch-Trick bei Review-Schleifen (SHA-raw-URL), `[skip netlify]` bei
  Doc-only, Builds bündeln; nach Sitemap-Änderung an GSC-Re-Submit erinnern; Pushes gefiltert
  (Remote-URLs nicht ausgeben).
- **Gedächtnis:** `LEKTIONEN.md` (Muster) + `OFFENE-REVIEW-PUNKTE.md` (False-Positives) +
  `SESSION-NOTES.md` fortschreiben.

## 6. Erwartete Lieferung (in dieser Reihenfolge; bei großen Schritten erst bestätigen lassen)
1. **Ist-Stand-Karte** (Phase 1).
2. **Flächendeckende Änderungsliste** — priorisiert, exakte Dateien, je mit Begründung „warum /
   welche Konsistenz".
3. **Neu-Entwicklungs-Spec je MVP-Seite** — Zweck · Content-Klasse/Seitentyp · Layout aus
   Bestandskomponenten · Abschnitte (Wireframe-Ebene) · Pflicht-Bausteine · interne Links ·
   Vier-Faktoren-Nachweis · Mockup-Beschreibung (wie es konkret aussieht).
4. **Sequenzierter Rollout-Plan** — Phasenmodell-konform, Standard zuerst, Gating beachtet.
5. **Konkreter erster Baustein:** Angebotsstandard-Spec-Entwurf, ready to build.

**Nordstern für ALLES:** Vertrauen + Daten + Beziehung + SEO/PR gleichzeitig — und bestehendes
Design / Seitenstruktur / Content-Niveau konsistent auf hohem Niveau halten. Im Zweifel:
Substanz und Konsistenz vor Tempo.
