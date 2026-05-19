# Session-Notizen

## Letzte Session
**Datum:** 19. Mai 2026 (Sozialbestattung-Sweep komplett — 10 Batches, 27 Cities, 12 Bundesländer)
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

**Batch-Architektur:**
- Batch 1: Frankfurt/Hannover/Kassel/Bonn (5/19 Mittag — deployed)
- Batch 2: Bochum/Heidelberg/Mannheim/Hamburg (5/19 Mittag — deployed)
- Batch 3: Düsseldorf/Duisburg/Bielefeld (NRW-Trio)
- Batch 4: Karlsruhe/Freiburg/Stuttgart (BW-Trio)
- Batch 5: Braunschweig/Oldenburg/Osnabrück (Niedersachsen)
- Batch 6: MG/Mülheim/Oberhausen (NRW)
- Batch 7: Hagen/Leverkusen/Wuppertal (NRW)
- Batch 8: Leipzig/Chemnitz/Magdeburg (Ost)
- Batch 9: Nürnberg/Bremen/Potsdam (Multi-BL)
- Batch 10: Münster/Rostock/Kiel (FINAL)

### Spawn-Tasks parallel abgearbeitet

1. **Hamburg Strukturkonsolidierung** (Spawn nach Batch 2): 3 commits behoben
   - Doublette Seebestattung-Sections konsolidiert
   - Doublette Bestattungsrecht-Sections konsolidiert
   - Orphan-`<p>` aus Cross-City-Block ausgegliedert
2. **Stuttgart Friedhofsgebühren 2025**: Aktualisierung auf Satzung vom 5.12.2024

### Re-Reviewer-Qualitätsgate (alle CLEAN nach Hotfixes)

Pro Batch unabhängiger Fact-Checker in fresh Tab. Key Funde:
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
- **Branch-Trick funktioniert**: Pro Iteration nur commit + push auf content-loop-pipeline; main bleibt unangetastet bis Final-Deploy → kein Netlify-Build pro Batch, ein einziger Build am Ende.

### Tool-Entwicklung

- `_dev/audit/helper-v3-installer.js` Production Send-Helper (~9KB, 4-Stream-stabil)
- `_dev/audit/insert-sozial-batchN.py` x 8 surgical Python insert-scripts pro Batch
- `_dev/audit/dispatch/dispatch-{city}.js` per-city dispatch artifacts
- `_dev/content-loop/runs/{city}/sozial-plan.txt + sozial-rereview.txt` Audit-Trail für jeden Insert

## Pipeline-State (vor Final-Deploy)

- `content-loop-pipeline` HEAD: `4044ef5` (Final Kiel-Hotfix)
- `main` HEAD: `9eed27b` (zwischenzeitlicher Hamburg+Batch3-6-Merge durch Spawn-Task)
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

1-12, 20-22 + Monetarisierung + Vorsorge-Cluster + 9 Tools + Audit + Roadmap + RP-Elite + Content-Loop-Pilot + Top-5-Stadt-Pages + Welle 2 + Welle 3 Top-Cities + Stadt-Pages-Closeout (15.05.2026) + P0-Fixes Hub/Sitemap/Redirect + Round 2 Full Sweep 25 Cities (18.05.2026) + **Sozialbestattung-Sweep komplett: 27 Cities × 12 Bundesländer (19.05.2026)**
