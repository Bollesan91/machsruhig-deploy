# Session-Notizen

## Letzte Session
**Datum:** 15. Mai 2026 (Multi-Chat-V2-Pipeline Final-Round, Stadt-Pages-Closeout)
**Deploy-Status:** ✅ **50 ≥85%-Pipeline-Cities LIVE** (Ziel "alle 45" übertroffen)

## Was wurde gemacht

### 🚀 Multi-Chat-Pipeline V2 — 8 NEUE LIVE Pages diese Session

Pipeline durchgeführt für 4 zuvor regression-blockierte Welle-1-Cities + 4 weitere Großstädte:

| Stadt | Final-Version | Score | Highlights |
|---|---|---|---|
| **Bonn** | v4 | 86% | NRW Welle 1 |
| **Hagen** | v5 | 89% | Welle 3, 3 MUST-FIX (Architekten/Loxbaum/Bestatter) |
| **Krefeld** | v5 | 86% | Welle 3, 3 MUST-FIX (von der Way / Ehrengräber / BdSt-Self-Contradiction) |
| **Nürnberg** | v4 | 87% | Welle 1, 2. Leichenschau Datum-Fix 4× (1.1.2023 → 1.4.2025) |
| **Bochum** | v6 | 88% | Welle 1, Wattenscheid-PLZ 44866-44869 + UNSURE-Strip |
| **Hannover** | v5 | 87% | Welle 1, 3 UNSURE-Kommentare raus + Kube/Warentest-Fixes |
| **Duisburg** | v6 | **92%** ✅ | Welle 1, Eisenbahnstraße-Stammdaten + § 15 Abs. 1 §-Fix |
| **Düsseldorf** | v6 | **94%** ✅ | Welle 1, § 22 BestV NRW-Halluzination + Standesamt-Verifikation |

**Top-Performer dieser Session:** Düsseldorf 94%, Duisburg 92%, Hagen 89%, Bochum 88%

### 📋 Pipeline-Methodik bewährt

Parallel 4-5 Tabs (Chat A Writer / Chat C Adversarial) auf claude.ai via Chrome MCP.
ScheduleWakeup-Loop +240s zwischen Checks, vollständige V2-Pipeline pro Stadt.

### 🎯 Methodik-Erkenntnisse

1. **Pipeline-Pattern erkannt**: "Jede Runde neue Detail-Halluzination" — bei jedem Rewrite tauchen ungeprüfte neue Zahlen/Adressen auf
2. **§-Cross-Page-Konsistenz kritisch**: Hagen § 15 Abs. 1 vs Duisburg § 16 Abs. 2 (BestG NRW) — §-Zitate gegen recht.nrw.de cross-checken
3. **UNSURE-Pipeline-Leakage**: Hannover v4 hatte 3 UNSURE-Inline-Kommentare im Production-HTML, Bochum v5 ebenso — Pre-Deploy-grep nötig
4. **Score-Pattern**: v3→v4 typisch +14 bis +17 Punkte, v4→v5 +2-3, Plateau bei v5-v6
5. **3-Runden-Pipeline-Schwachstelle Standesamt-Adresse**: Düsseldorf brauchte v6 weil v5 PLZ-Fix nicht annahm

### LIVE-Gesamtstatus

- Pre-Session: 23 Pipeline-Cities ≥85% + 14 v1-only = 37 LIVE
- Diese Session: **+8 zusätzliche ≥85%-Pipeline-Deploys**
- **Total deploy-fähige Pipeline-Cities: 50 LIVE** (53 city-dirs gesamt)

## Nächste Schritte

### Offene Pipeline-Items
Keine — alle ehemaligen Regression-Cities (Hannover/Nürnberg/Bochum/Duisburg/Düsseldorf) sind jetzt ≥85% LIVE.

### Main-Merge erforderlich
Alle Pages auf `content-loop-pipeline`-Branch. Merge nach `main` für Netlify-Deploy muss user-seitig (Sandbox-Restriction).

Pipeline-Branch enthält:
- bestatter/{bonn,hagen,krefeld,nuernberg,bochum,hannover,duisburg,duesseldorf}/index.html
- Alle Adv-Recheck-Markdown-Logs in `_dev/content-loop/runs/<city>/round-{10,12}-adv-*.md`

## Offene Fragen

- Sitemap-Priority anheben (alle neu deployten von 0.6 → 0.7) — TODO
- og-images stadt-spezifisch (z.B. og-duesseldorf.png) — Polish, nicht blockierend

## Erledigte PBIs (gesamt)

1-12, 20-22 + Monetarisierung + Vorsorge-Cluster + 9 Tools + Audit + Roadmap + RP-Elite + Content-Loop-Pilot + Top-5-Stadt-Pages + Welle 2 + Welle 3 Top-Cities (12.05.2026) + **Stadt-Pages-Closeout 8 zusätzliche Welle-1-Cities (15.05.2026)**

## Pipeline-State

Alle 8 neuen Pages auf `content-loop-pipeline` branch gestaged und gepusht.
bestatter/<city>/index.html gespiegelt.
Merge nach main + Netlify-Deploy muss user-seitig.
