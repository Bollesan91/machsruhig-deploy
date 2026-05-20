# Session-Notizen

## Letzte Session
**Datum:** 20. Mai 2026 (FAQ-Schema-Drift-Sweep sitewide + Wuppertal-Gebühren + Sitewide-Audit-Aufräumen)
**Deploy-Status:** Branch `claude/start-ruhig-YetPT` gepusht (6 Commits), nicht in main gemerged — wartet auf Review/Deploy-Freigabe.

## Was wurde gemacht (Session 20.05.2026)

### Stream A: FAQ-Schema-Drift-Sweep + JSON-LD-Hygiene sitewide

**Tool-Suite gebaut (`_dev/audit/`):**
- `faq-schema-drift.py` — auditiert JSON-LD `FAQPage` vs sichtbarem HTML-FAQ-Block über alle Page-Bereiche. Unterstützt drei Markup-Stile (`<details><summary>`, `mr-faq-Wrapper`, `mr-faq__item`/`faq-item`-divs). Filter für Mobile-Nav-`<details>`. Klassifiziert: CLEAN, DRIFT (COUNT/Q_TEXT/A_TEXT), NO_LD, NO_HTML, NO_FAQ.
- `regenerate-faq-jsonld.py` — regeneriert FAQPage-Schema aus sichtbarem HTML als Single-Source-of-Truth. Format-preserving via **Surgical-Replace**: nur das FAQPage-Objekt wird per `JSONDecoder.raw_decode()` byte-genau ersetzt, alle anderen JSON-LD-Nodes bleiben unangetastet. `--dir`/`--city`/`--diff`/`--write`-Argumente.
- `module-heatmap-v2.py` — Modul-Audit (6 Pflicht-Module) mit flexiblen Header-Regex über alle Stadt-Pages.

**Drift-Behebung (Resultat: 0 DRIFT sitewide):**
- bestatter/ (52 Cities): 39 DRIFT → 52 CLEAN
- bestattung-in/ (16 Bundesländer): 11 DRIFT → 16 CLEAN
- vorsorge/ (8 Pages): 8 DRIFT → 8 CLEAN
- tools/ (10): 1 DRIFT (danksagung) → CLEAN; 7 NO_HTML notiert (CSR-React-Issue, separates Ticket)

**Drift-Typen behoben:**
- 4 COUNT-Mismatch (berlin/hamburg LD 4→7, bremen 7→9, rostock 6→7)
- 7 BOTH Q+A-Drift (Augsburg-Vertauschung Q5/Q6, chemnitz, essen, halle, magdeburg, muelheim, darmstadt)
- 44 A_ONLY-Drift (Answer-Text aus HTML übernommen)

**JSON-LD-Quoting-Bugs nebenher gefixt:**
- Münster + Darmstadt hatten unescaped `"` innerhalb von `„…"`-Strings im JSON-LD (verhinderte Parsen). Per Skript-Regex `(„[^„"]*?)"` → `\1"` (U+201D) gefixt.

### Wuppertal Friedhofsgebühren-Tabelle

- Ersetzt: Orientierungsspannen aus NRW-Vergleichsstädten (Düsseldorf/Essen/Solingen/Remscheid) durch 16 verbindliche Sätze des **Christlichen Friedhofsverbandes Wuppertal** (Gebührensatzung 05.12.2023, in Kraft seit 04.03.2024).
- Inkl. Bestattungs-, Kapellen-, Friedhofsunterhaltungs-Gebühren konkret.
- Geltungsbereichs-Hinweis: 34 christliche Friedhöfe + jüdische Friedhöfe und kommunale Grabfelder mit eigenen Sätzen.
- FAQ-Antwort + Quellen-Block (Direkt-Link zu Gebühren- + Friedhofssatzung PDF).
- Daten kamen vom User (PDF in dieser Container-Sandbox per Net-Allowlist nicht erreichbar).

### Stream B: SEO/Content-Audit + Bugfixes

**Broken Internal Links (Sweep-Fix, 17 Vorkommen über 8 Pages):**
- `/bestattung-in/baden-wuerttemberg/` → `/bestattung-in/baden-württemberg/` (12×)
- `/bestattung-in/thueringen/` → `/bestattung-in/thüringen/` (2×)
- `/vorsorge/bestattungsverfuegung/` → `/vorsorge/bestattungsvorsorge/` (3×, Tippfehler)

**OG-Image-Sweep (sitewide, 65 Pages):**
- 13 Pages hatten broken og:image-URLs auf nicht-existente Bilder (`/assets/og/bielefeld-sennefriedhof.png`, `/og/essen.jpg`, `/og/default.jpg`, …)
- 52 Pages hatten og:title/og:url, aber kein og:image (kein Social-Preview-Bild)
- Alle 65 → Default `/assets/og-image.png` (das einzige existierende OG-Image)

**Canonical-Bugs (2):**
- `bestatter/braunschweig/`: `www.machsruhig.de` → `machsruhig.de` (Konsistenz mit anderen Pages)
- `bestatter/muelheim/`: Canonical auf nicht-existentes `/bestatter/muelheim-an-der-ruhr/` → `/bestatter/muelheim/`

### Audit-Befunde (kein Fix, dokumentiert)

- **39 broken internal links insgesamt**, 17 davon gefixt (siehe oben). Verbleibende erfordern Policy-Decision: nicht-existente Cities (Offenbach, Herne, Recklinghausen, Heilbronn, Bremerhaven, Esslingen, Brandenburg-an-der-Havel, …), fehlende Hub-Pages (`/ratgeber/`, `/bestattung-in/`-Index, `/kosten/`, `/wissen/`).
- **7 Tool-Pages mit FAQPage-Schema ohne sichtbaren HTML-Block** (abschiedsbrief, bestattungskosten-rechner, checkliste-todesfall, fristen-radar, kostenrechner, notfallkarte, vorsorge-check) — alle React-CSR. Bekanntes BACKLOG-Item (tool-CSR-Problem). Risiko: Google Structured-Data-Verstoß.
- **Modul-Heatmap V2** (`_dev/audit/module-heatmap-v2.md`): Sitewide-Status nach Sozial-Sweep, robusterer Regex als V1-Heatmap. Lücken: akut 3, kosten 6, sozial 5, quellen 11 — FAQ + Bestwahl jetzt 52/52.
- **Sitemap-Konsistenz**: tatsächlich sauber (Stream-B-Agent hatte URL-Encoding-Naivität-Bug). Umlauts (`baden-württemberg`) sind percent-encoded in Sitemap — best practice.
- **Tel-Link-Audit sitewide**: 0 Probleme. Lib aus Sozial-Sweep blieb sauber.
- **JSON-LD-Validität sitewide**: 0 broken Blocks über ~100 Pages.

### 6 Commits dieser Session

1. `22e3d16` — `[audit]` FAQ-Schema-Drift-Audit-Tool über alle Stadt-Pages
2. `9fabc2d` — `[faq-schema-fix]` FAQ-JSON-LD aus HTML regeneriert (39 Cities + Quote-Fix)
3. `514ddc2` — `[faq-schema-fix]` Gründlicher Audit: Umlaut-Duplikate + Darmstadt-Markup
4. `98f8df1` — `[wuppertal]` Friedhofsgebühren-Tabelle durch offizielle Sätze ersetzt
5. `e2bf34d` — `[faq-schema-fix]` FAQ-Drift sitewide gelöst (Bundesland + Vorsorge + Tools)
6. `90a79df` — `[broken-links]` 17 fehlerhafte interne Links über 8 Pages
7. `7900ce3` — `[og-image + canonical]` Sitewide OG-Image-Fix + 2 Canonical-Bugs

### Methodik-Erkenntnisse

- **Single-Source-of-Truth = HTML** für FAQ-Schema. JSON-LD wird per Skript-Regenerator daraus synchronisiert. Konform zu Google's Structured-Data-Richtlinie ("Content must be present on the page that loads").
- **Surgical-Replace** schlägt full-reserialize: balanced-brace-Suche via `JSONDecoder.raw_decode()` ersetzt nur das gezielte Objekt, andere Nodes bleiben byte-exakt → minimaler Diff-Churn.
- **Format-Preservation pro File** (indent=2 vs minified) detect-bar über `\n` und Erst-Indent-Level.
- **Agent-Halluzinationen erkennen**: Stream-B-Agent behauptete `bestatter/köln/` + `bestatter/münchen/` als Umlaut-Duplikate — falsch. Tatsächlich nur `lübeck/` + `mönchengladbach/`. Findings immer per `ls`/`grep` selbst verifizieren.
- **Network-Allowlist beachten**: Container blockt externe Hosts (`fvwuppertal.de`, `wz.de`, `google.com` → 403). Lokale Audits + User-bereitgestellte Daten als Pfad.

---

## Letzte vor-vorige Session
**Datum:** 19. Mai 2026 (Sozialbestattung-Sweep komplett — 10 Batches, 27 Cities, 12 Bundesländer + Hamburg-Strukturkonsolidierung + Stuttgart-Gebühren 2025)
**Deploy-Status:** content-loop-pipeline → main Final-Merge mit Netlify-Deploy (Ende-Deploy)

## Was wurde gemacht

### Sozialbestattung-Sweep (Modul-Heatmap-Audit → Insert → Re-Review-Loop)

Audit aller deploy-fähigen Stadt-Pages auf 7 Pflicht-Module identifizierte **Sozialbestattung § 74 SGB XII** als größte systemische Lücke (33/52 Cities). Über den Tag verteilt in 10 Batches geschlossen mit Helper-V3-Pipeline (3-Stream-Cadence, Tabs proaktiv nach jeder Phase geschlossen).

**Coverage-Map (27 Cities, 12 Bundesländer):**

| BL | Cities | §-Referenz |
|---|---|---|
| NRW (13) | Bochum, Bonn, Köln, Düsseldorf, Duisburg, Bielefeld, MG, Mülheim, Oberhausen, Hagen, Leverkusen, Wuppertal, Münster | § 8 BestG NRW |
| BW (5) | Heidelberg, Mannheim, Karlsruhe, Freiburg, Stuttgart | § 31 BestattG BW |
| NL (5) | Hannover, Kassel, Braunschweig, Oldenburg, Osnabrück | § 8 Abs. 3 NBestattG |
| HE (1) | Frankfurt | § 13 FBG Hessen |
| HH (1) | Hamburg (Akutbox + Sozial) | § 10/§ 11 HmbBestattG |
| SN (2) | Leipzig, Chemnitz | § 10 Abs. 1 SächsBestG |
| ST (1) | Magdeburg | § 10 BestattG LSA |
| BY (1) | Nürnberg | Art. 15 Bayerisches BestG |
| HB (1) | Bremen | § 4 Abs. 1 Satz 1 Nr. 1 Gesetz über das Leichenwesen (Sonderfall: gleichrangige Pflicht ohne Rangfolge) |
| BB (1) | Potsdam | § 20 BbgBestG |
| MV (1) | Rostock | § 9 Abs. 2 BestattG M-V |
| SH (1) | Kiel | § 13 Abs. 2 BestattG SH |

**Batch-Architektur (10 Batches):**
- Batch 1: Frankfurt/Hannover/Kassel/Bonn (5/19 Mittag — deployed)
- Batch 2: Bochum/Heidelberg/Mannheim/Hamburg (5/19 Mittag — deployed)
- Batch 3: Düsseldorf/Duisburg/Bielefeld (NRW-Trio) — Zwischen-Merge `e65c410`
- Batch 4: Karlsruhe/Freiburg/Stuttgart (BW-Trio) — Zwischen-Merge `e65c410`
- Batch 5: Braunschweig/Oldenburg/Osnabrück (NL) — Zwischen-Merge `e65c410`
- Batch 6: MG/Mülheim/Oberhausen (NRW) — Zwischen-Merge `e65c410`
- Batch 7: Hagen/Leverkusen/Wuppertal (NRW) — Final-Merge
- Batch 8: Leipzig/Chemnitz/Magdeburg (Ost) — Final-Merge
- Batch 9: Nürnberg/Bremen/Potsdam (Multi-BL) — Final-Merge
- Batch 10 FINAL: Münster/Rostock/Kiel — Final-Merge

### Spawn-Tasks parallel abgearbeitet

1. **Hamburg Strukturkonsolidierung** (Spawn nach Batch 2): 3 commits
   - Seebestattung-Doublette konsolidiert (`6f59005`): zwei `<h2>`-Sektionen zu einer zusammengeführt. Widerspruch entfernt: alte Preisspanne „1.200–3.500 €" raus, präzise Reederei-Pakete (1.049/1.646/1.895 €) und Komplettpaket (2.900–5.000 €) bleiben.
   - Bestattungsrecht-Doublette konsolidiert (`e08db75`): Kurzfassung + Fristen-Section zu einer Section zusammengeführt; Stadtstaat-Einordnung + alle Fristen/Sargpflicht/BUKEA + Hint mit Verweis auf BL-Seite erhalten.
   - Orphan `<p>` aus Cross-City-Block ausgegliedert (`f3c3756`): verwaister Friedhofs-Gebühren-Absatz in eigene `<div class="mr-section">` mit h2 „Gebühren & Kostenvoranschläge".
2. **Stuttgart Friedhofsgebühren 2025** (`133c9d9`): Update auf Satzung vom 5.12.2024 (Reihengrab 940→987 €, Bestattungsgebühr 1.010→1.248 €, Urnenreihen 700→735 €, Wahlgrab 1.960→2.142 €, Urnenwahl 1.740→1.890 €, neue Urnenbeisetzung 273 €).

### Re-Reviewer-Qualitätsgate (alle CLEAN nach Hotfixes)

Pro Batch unabhängiger Fact-Checker in fresh Tab. Key Funde + Coordinated Fixes:
- **§ 31 vs § 21 BestattG BW**: Coordinated rollback über 5 BW-Cities (Heidelberg/Mannheim/Karlsruhe/Freiburg/Stuttgart) — § 31 ist die Bestattungspflicht-Reihenfolge in BW, NICHT § 21
- **§ 15 BestV (Bayern)** falsch → **Art. 15 Bayerisches BestG** korrekt (Nürnberg-Fix)
- **§ 10 Abs. 3 SächsBestG** falsch → **§ 10 Abs. 1 SächsBestG** korrekt (Leipzig/Chemnitz-Fix)
- **§ 14 Abs. 3 FBG Hessen** nicht belegt → entfernt (Frankfurt-Hotfix)
- **§ 2 Nr. 12 BestattG SH** existiert nicht → entfernt (Kiel-Hotfix)
- **Tel-Link-Audit**: 4 Cities hatten 1-extra-Digit-Bugs (preventive Audit via Python-regex über alle Pages)
- **Behördennamen-Fix**: Oldenburg „Amt für Soziale Hilfen" (SH-Variante) → korrekt „Amt für Teilhabe und Soziales — Fachdienst Soziale Hilfen"
- **HTML-Struktur**: Frankfurt + Hamburg + Kiel hatten `<section>/</div>`-Mismatches oder nested-section-Bugs → alle gefixt

### Methodik-Erkenntnisse

- **3-Stream-Cadence stabil**: Vom User auf 3 reduziert (vorher 4 mit gelegentlichen Throttling-Issues). Keine Probleme mehr.
- **Tabs proaktiv schließen**: User-Vorgabe mehrfach eingefordert → nach jeder Phase Tabs zu. Kein Tab-Müll mehr beim Sweep-Ende.
- **Independent Reviewer-Pattern bewährt**: Fresh Tabs für Re-Reviewer fanden echte juristische Fehler (§-Numbers, Behördenbezeichnungen, Strukturmängel). Sycophancy-Isolation funktioniert.
- **GitHub raw CDN-Lag**: Cache-Bust-Parameter `?cb=20260519bX` im Fetch-URL der Re-Reviewer um stale-content-FAILs zu vermeiden.
- **Branch-Trick funktioniert**: Pro Iteration nur commit + push auf content-loop-pipeline; main bleibt unangetastet bis Final-Deploy → kein Netlify-Build pro Batch, sparsame Builds.
- **Programmatische Verifikation > WebFetch-Reviewer bei strukturellen Fixes**: Lesson aus Hamburg-Fix — bei DOM-Manipulationen ist `curl + grep <h2>-Counts` verlässlicher als WebFetch-basierte Reviewer (Cache-Lag).
- **Spawn-Tasks für Out-of-Scope-Findings**: Hamburg-Strukturprobleme + Stuttgart-Gebühren-Update wurden als parallel-tasks gespawnt — fertig zur Merge-Zeit ohne den Hauptloop zu unterbrechen.

### Tool-Entwicklung

- `_dev/audit/helper-v3-installer.js` Production Send-Helper (~9KB, 3-Stream-stabil)
- `_dev/audit/insert-sozial-batch{1-10}.py` 10 surgical Python insert-scripts pro Batch
- `_dev/audit/dispatch/dispatch-{city}.js` per-city dispatch artifacts
- `_dev/audit/fix-hamburg-issue{1,2,3}-*.py` aus Spawn-Task
- `_dev/content-loop/runs/{city}/sozial-plan.txt + sozial-rereview.txt` Audit-Trail für jeden Insert

## Pipeline-State (vor Final-Deploy)

- `content-loop-pipeline` HEAD: `4b190fa` (SESSION-NOTES + Dispatch-Tooling)
- `main` HEAD: `9eed27b` (Zwischen-Merge `e65c410` brachte Hamburg + Batch 3-6 live)
- **Dieser Final-Deploy bringt Batches 7-10 + Stuttgart-Gebühren-Update + alle Re-Review-Hotfixes live**

## Nächste Schritte

### Audit-Backlog (nicht in diesem Sweep erledigt)

- **Bulk-FAQ-Schema-Drift-Audit**: ~12 Cities haben JSON-LD vs HTML FAQ-Mismatch
- Wuppertal "nicht-offizielle Gebühren" durch Satzungsdaten ersetzen
- Berlin Quellenmix (Wikipedia → Primärquellen)
- Lübeck Lead-Sprache (noindex bleibt vorerst)
- Münster Bestatter-Wahl-Modul (heatmap 5/7 → war nur Sozial im Scope dieser Session)

### Round 3 Polish (parallel)

- Kostenrechner-CTA in alle Stadt-Pages
- Sitemap-Priority 0.6 → 0.7 für neue Cities
- og-images stadt-spezifisch

## Offene Fragen

- Bulk-FAQ-Schema-Audit jetzt oder beim nächsten Sweep?
- Münster Gold-Template-Upgrade wann?

## Erledigte PBIs (gesamt, Stand 19.05.2026)

1-12, 20-22 + Monetarisierung + Vorsorge-Cluster + 9 Tools + Audit + Roadmap + RP-Elite + Content-Loop-Pilot + Top-5-Stadt-Pages + Welle 2 + Welle 3 Top-Cities + Stadt-Pages-Closeout (15.05.2026) + P0-Fixes Hub/Sitemap/Redirect + Round 2 Full Sweep 25 Cities (18.05.2026) + **Sozialbestattung-Sweep komplett: 27 Cities × 12 Bundesländer + Hamburg-Strukturkonsolidierung + Stuttgart-Gebühren 2025 (19.05.2026)**
