# Session-Notizen

## Letzte Session
**Datum:** 19. Mai 2026 (Modul-Heatmap V2 + Sozialbestattung-Sweep Batch 1)
**Deploy-Status:** content-loop-pipeline → main Merge mit Netlify-Deploy

## Was wurde gemacht

### Modul-Heatmap-Audit (52 Stadt-Pages)

Audit aller deploy-fähigen Stadt-Pages auf 7 Pflicht-Module:
1. Akutbox / Was-tun-bei-Todesfall
2. Bestatter-Wahl-Checkliste
3. Sozialbestattung § 74 SGB XII
4. Kosten-vor-Friedhof
5. FAQ-Block (>= 5 Fragen)
6. Lokales Quellenverzeichnis
7. YMYL-Stand-Datum

Top-Gaps identifiziert:
- **Sozialbestattung-Modul fehlt: 33/52 Cities** (größte systemische Lücke)
- Kosten-vor-Friedhof fehlt: 44/52 Cities
- 4 Cities ≤ 4/7 Module: Köln (4/7), Dresden (4/7), Berlin (5/7), Frankfurt (5/7)

Output: `_dev/audit/module-heatmap.md` (52 Cities × 7 Module Matrix)

### Modul-Insertion (7 Cities Batch 1)

Surgical Python-Insert-Scripts mit Anker-basiertem replace (idempotent). Pro Stadt:
1. Strukturberater-Plan via Helper V3 in fresh Tab (~120s)
2. Python-Insert-Script ausführen → HTML modifiziert
3. Re-Reviewer in zweitem fresh Tab → Fakten-Check, §-Referenz-Verifikation
4. Bei FAIL: Surgical Fix + Re-Verify

| City | Module hinzugefügt | Bestätigte Spezifika |
|---|---|---|
| Köln | Akutbox + Bestatter-Wahl + Sozialbestattung | Standesamt Gülichplatz 1-3, Sozialamt Lindenthal Aachener Str. 220 |
| Dresden | Bestatter-Checkliste + Sozialbestattung | Sozialamt Junghansstr. 2, § 10 Abs. 3 SächsBestG |
| Berlin | Akutbox (Bezirksstandesamt-Logik) | 12 Bezirke + Standesamt I = Auslandsstandesamt |
| Frankfurt | Sozialbestattung | Besonderer Dienst 4, Mainzer Landstr. 291, FBG Hessen § 13 |
| Hannover | Sozialbestattung | Fachbereich Soziales Hamburger Allee 25, NBestattG § 8 Abs. 3 |
| Kassel | Sozialbestattung | Stadt Kassel Sozialamt Obere Königsstr. 8, FBG Hessen § 13 |
| Bonn | Sozialbestattung | Amt für Soziales und Wohnen Hans-Böckler-Str. 5, BestG NRW § 8 |

### Reviewer-Funde (alle gefixt vor Deploy)

- **Berlin Akutbox: § 15 BestattG BE falsch zitiert** — Re-Reviewer fand: § 15 regelt Sarg-Beschaffenheit. Korrekt wäre § 13. Fix: §-Nummer komplett entfernt, konsistent zur existierenden Page.
- **Köln Sozialamt-Adresse-Verifikation** — Bezirksamt Lindenthal Aachener Str. 220 vs. zentrale Adresse — Re-Reviewer bestätigte Bezirksamt korrekt.
- **Dresden § 10 SächsBestG** — Reviewer verifizierte Absatzzitierung Abs. 3.

### Tool-Entwicklung: Helper V3 Send-Helper

`_dev/audit/helper-v3-installer.js` (~9KB Production-Version):
- `window.__mcp.run(prompt, label, opts)` — async dispatch in claude.ai-Tabs
- Lifecycle: sending → streaming → complete | failed
- Auto-Download: `${label}.txt` via Blob+a-tag-click
- Selektor-Update Mai 2026: `[data-testid="action-bar-copy"]` count delta als Completion-Signal (Stop-Button-Selector aus V2 deprecated)
- Retries: 3s → 8s → 20s bei Send-Button disabled

Dispatch-Scripts pro Stadt unter `_dev/audit/dispatch/dispatch-{city}.js` (Helper + Prompt + Label).

### Methodik-Erkenntnisse

- **Independent-Reviewer-Pattern bewährt**: Fresh Tab = eigene Konversation = keine Sycophancy-Bleed. Echte MAJOR-Funde (Berlin §-Fehler).
- **Surgical Python-Insert dominant**: 7/7 Insertions deterministisch via Anker-Match. Kein AI-Truncation-Risk.
- **Branch-Trick funktioniert wie geplant**: 9 Commits auf content-loop-pipeline gesammelt, EIN finaler Merge → main = EIN Netlify-Build.
- **Concurrency-Cap claude.ai ~3-4 Streams**: 4-Stream-Cadence stabil.

## Pipeline-State (vor diesem Deploy)

- `content-loop-pipeline`: HEAD 31ed056 (9 Commits seit letztem main-Merge)
- `main`: d90835e (letzter Merge: Berlin Akutbox)
- **Dieser Deploy bringt Frankfurt + Hannover + Kassel + Bonn Sozialbestattung live**

## Nächste Schritte

### Sozialbestattung-Sweep fortsetzen (29 Cities pending)

Batch 2 vorbereitet (nicht in dieser Session umgesetzt):
- Bochum (5/7, fehlt Bestatter-Wahl + Sozial)
- Heidelberg (5/7, dito)
- Mannheim (5/7, fehlt Sozial)
- Hamburg (5/7, fehlt Akutbox)

Restliche ~25 Cities mit fehlendem Sozial-Modul: Per-Bundesland-Briefing wiederverwenden (NRW/Bayern/Hessen/Sachsen/Niedersachsen/BW), nur Sozialamt-Adresse + Telefon pro Stadt austauschen.

### Round 3 Polish (parallel)

- Kostenrechner-CTA in alle Stadt-Pages
- Sitemap-Priority 0.6 → 0.7 für neue Cities
- og-images stadt-spezifisch

### Audit-Backlog Reste

- Lübeck Lead-Sprache (noindex bleibt vorerst)
- Wuppertal "nicht-offizielle Gebühren" durch echte Satzungsdaten ersetzen
- Berlin Quellenmix (Wikipedia → Primärquellen)

## Offene Fragen

- Bulk-FAQ-Schema-Audit-Script jetzt oder bei nächstem Sweep?
- Münster Gold-Template-Upgrade wann?

## Erledigte PBIs (gesamt, Stand 19.05.2026)

1-12, 20-22 + Monetarisierung + Vorsorge-Cluster + 9 Tools + Audit + Roadmap + RP-Elite + Content-Loop-Pilot + Top-5-Stadt-Pages + Welle 2 + Welle 3 Top-Cities + Stadt-Pages-Closeout (15.05.2026) + P0-Fixes Hub/Sitemap/Redirect + Round 2 Full Sweep 25 Cities (18.05.2026) + **Modul-Heatmap V2 + Sozialbestattung Batch 1 für 7 Cities (19.05.2026)**
