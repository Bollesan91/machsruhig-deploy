# Session-Notizen

## Letzte Session
**Datum:** 19. Mai 2026 (Hamburg-Struktur-Fix 3 Issues + Sozial-Sweep Batch 3–6 Merge + Stuttgart-Gebühren-Refresh aus Parallel-Session)
**Deploy-Status:** Hamburg-Fix + Sozial-Batch-3–6 nach main gepusht (Netlify-Deploy ausgelöst). Stuttgart-Refresh aus Parallel-Session ist auf content-loop-pipeline noch nicht gepusht (siehe „Out-of-Scope" unten).

## Was wurde gemacht

### Hamburg — 3 pre-existing strukturelle Issues behoben

Issue-Briefing kam aus `_dev/content-loop/runs/hamburg/akut-sozial-rereview.txt` (Sozialbestattung-Re-Review hatte 3 strukturelle Findings unabhängig vom Sozial-Modul geflaggt).

**1) Seebestattung-Doublette konsolidiert** (Commit 6f59005)
- Zwei <h2>-Sektionen („… leise Tradition" kurz + „… Tradition der Hafenstadt" lang) zu einer Section zusammengeführt.
- Widerspruch entfernt: alte Spanne „1.200–3.500 €" (kurze Section) raus, präzise Reederei-Pakete (1.049/1.646/1.895 €) und Komplettpaket (2.900–5.000 €) aus langer Section bleiben.
- Kultureller Opener aus Section 1 (Hansestadt, Seehafen, Reedereien) bleibt als Einstieg, dann Wie-funktioniert + Orte + Kosten-Tabelle + Vorteile.

**2) Bestattungsrecht-Doublette konsolidiert** (Commit e08db75)
- Zwei <h2>-Sektionen („Kurzfassung" + „Fristen & Regelungen nach HmbBestattG") zu einer Section zusammengeführt.
- Stadtstaat-Einordnung aus #1 + alle Fristen/Sargpflicht/Mindestruhezeit/Besonderheiten/BUKEA aus #2 + Hint mit Verweis auf BL-Seite (`/bestattung-in/hamburg/`) bleibt erhalten.
- Sargpflicht-Doppelung in Besonderheiten-Liste entfernt (war im fließenden Text bereits abgehandelt).

**3) Orphan <p> aus Cross-City-Block ausgegliedert** (Commit f3c3756)
- Verwaister <p> über Friedhofs-Gebühren + Kostenvoranschläge stand innerhalb `<section class="mr-section">` „Bestatter in anderen Städten", aber AUSSERHALB des inneren mr-container — strukturell unsauber + thematisch fremd.
- In eigene `<div class="mr-section">` mit h2 „Gebühren & Kostenvoranschläge — Tipps zur Bestatter-Wahl" ausgegliedert, vor die Cross-City-Section gestellt.

### Sozialbestattung Batch 3–6 mit nach main gepusht

Aus content-loop-pipeline standen 8 weitere Commits aus anderen Sessions an, die im selben Merge nach main mitgeschwommen sind:
- Batch 3 NRW (Düsseldorf/Duisburg/Bielefeld) + Re-Reviews CLEAN
- Batch 4 BW (Karlsruhe/Freiburg/Stuttgart) + § 21 → § 31 BestattG BW Rollback
- Batch 5 NL (Braunschweig/Oldenburg/Osnabrück) + Re-Review-Fixes
- Batch 6 NRW (Mönchengladbach/Mülheim/Oberhausen) + Re-Review-Fixes + Tel-Link-Audit-Fix

Merge-Commit: e65c410 „Merge content-loop-pipeline -> main: Hamburg-Struktur-Fixes + Sozialbestattung Batch 3-6". Standard-Repo-Pattern (letzter Main-Merge bündelte ebenfalls mehrere Batches).

### Methodik & Lessons

- **Surgical Python-Scripts** in `_dev/audit/fix-hamburg-issue{1,2,3}-*.py` (idempotent, Match-Guard, h2-Count-Check post-edit).
- **Branch-Workflow:** Commits einzeln pro Issue auf content-loop-pipeline → push pro Commit → finaler Merge --no-ff nach main.
- **Helper-V3-Re-Reviewer** schlug 2× FAIL — beide Male aufgrund STALE-Cache: WebFetch/CDN lieferte den Vor-Fix-Zustand zurück, auch im fresh Tab mit Cache-Busting-Query. Lesson: bei strukturellen Fixes ist programmatische Verifikation (curl + grep `<h2>`-Counts + grep auf Widerspruchs-Strings) verlässlicher als WebFetch-basierte Reviewer.
- **Anti-Priming:** Zweiter Review-Prompt war non-priming (offene h2-Enumeration statt „prüfe ob zwei wie zuvor"), trotzdem stale Cache-Daten — Cache-Issue, nicht Prompt-Issue.

## Pipeline-State

- **`main`:** HEAD = e65c410 (Hamburg-Fix + Sozial-Batch-3–6 gemerged, Netlify-Deploy läuft)
- **`content-loop-pipeline`:** synchron mit main bis HEAD f3c3756 (vor Merge); danach keine neuen Commits
- **Stash auf content-loop-pipeline:** „stuttgart-wip-unrelated" — Stuttgart-Gebühren-Refresh aus Parallel-Session, NICHT von dieser Session zu committen (siehe unten)

## Out-of-Scope-Find aus Parallel-Session

Während dieser Session existierte eine modifizierte Working-Copy von `bestatter/stuttgart/index.html` mit Stuttgart-Friedhofsgebühren-Refresh auf 2025er-Sätze (940 → 987 €, 1.960 → 2.142 €, 1.010 → 1.248 €, 1.740 → 1.890 €, Urnenreihen 940 → 735 €, neue Bestattungsgebühr Urnenbeisetzung 273 €) + dazugehörige Notiz-Draft in SESSION-NOTES.md.

Diese Änderungen stammen aus einer parallel laufenden Session und wurden bewusst NICHT in diesem „ende" mitgepusht. Stuttgart-Content-Change ist in `git stash@{0}` („stuttgart-wip-unrelated" auf Branch content-loop-pipeline) geparkt; die Stuttgart-Notiz-Draft wurde in diese Datei als Hinweis integriert. Die Parallel-Session kann den Stash poppen, gegenprüfen, und ihrerseits ihre „ende"-Sequence durchziehen.

**Stuttgart-Detail (aus Parallel-Session-Draft):**
- Friedhofsgebührensatzung Landeshauptstadt Stuttgart Fassung 5.12.2024 (Amtsblatt 51/52, 19.12.2024) tritt zum 1.1.2025 in Kraft — Page hatte 2024er-Tarif, 6 Werte überholt, 1 Position fehlte
- Aktualisiert in 4 Block-Ebenen: Keyfacts-Liste (L318), Gebühren-Tabelle (L371-378), JSON-LD FAQPage acceptedAnswer (L191), FAQ-Antwort sichtbar (L438)
- Bewusst nicht angefasst: Krematorium-Einäscherung 605 € (unbestätigt), Sozialbestattungs-Modul (im vorigen Sweep entwertet), Verwaltungsgebühr 92 € + Verlängerungs-Sätze
- Methodik: Surgical Python `/tmp/edit_stuttgart_fees.py` mit 9 exakten Substring-Replacements und Match-Count-Guard
- Post-Edit-Verifikation via `grep`: alle 6 Alt-Werte 0 Treffer im Gebührenkontext, alle 6 Neu-Werte + neue Urnenbeisetzung-Zeile korrekt platziert

## Nächste Schritte

### Hamburg-Page

- Re-Reviewer-Tooling für strukturelle Doppel-Checks neu aufsetzen: WebFetch-Cache-Issue umgehen via Inline-HTML-Paste in Reviewer-Prompt statt URL-Fetch. Oder Programmatic-Verification-Subagent (curl + python `lxml`) als Standard für strukturelle Fixes.
- Hamburg auf vollständige V2-Pipeline-Konformität checken: Module-Heatmap-Audit-Rerun nach diesen Fixes, ob noch andere Gaps offen sind.

### Stuttgart (Parallel-Session)

- Stuttgart-Stash poppen, gegenprüfen, mit `[skip netlify]` auf content-loop-pipeline committen (Parallel-Session-Workflow).
- Krematorium-Einäscherung 605 € via stuttgart.de/medien/ibs/7-3.pdf verifizieren (in deren Notiz-Draft offen).

### Sozialbestattung-Sweep

- ~25 Cities mit fehlendem Sozial-Modul übrig (laut Parallel-Session-Plan): Bochum, Heidelberg, Mannheim, Hamburg-Akutbox (Hamburg-Akutbox bereits in Batch 2 erledigt, Cross-Check), restliche Per-Bundesland-Briefing wiederverwenden mit lokalen Sozialamt-Adressen.

### Audit-Backlog Reste

- Lübeck Lead-Sprache (noindex bleibt vorerst)
- Wuppertal „nicht-offizielle Gebühren" durch echte Satzungsdaten ersetzen
- Berlin Quellenmix (Wikipedia → Primärquellen)

## Offene Fragen

- Re-Reviewer-Cache-Issue: Wie umgehen? Inline-HTML-Paste, dedizierter Programmatic-Subagent, oder eigener Cache-Buster-Proxy?
- Krematorium-Verifikation Stuttgart in nächster Session mit Sozial-Sweep Batch 7 bündeln, oder als Stand-alone Push?

## Erledigte PBIs (gesamt, Stand 19.05.2026)

1-12, 20-22 + Monetarisierung + Vorsorge-Cluster + 9 Tools + Audit + Roadmap + RP-Elite + Content-Loop-Pilot + Top-5-Stadt-Pages + Welle 2 + Welle 3 Top-Cities + Stadt-Pages-Closeout (15.05.2026) + P0-Fixes Hub/Sitemap/Redirect + Round 2 Full Sweep 25 Cities (18.05.2026) + Modul-Heatmap V2 + Sozialbestattung Batch 1 + Sozialbestattung Batch 2 für 4 Cities (19.05.2026) + **Sozialbestattung Batch 3–6 für 12 Cities NRW/BW/NL (19.05.2026, mit Re-Review-CLEAN-Verify und § 21 → § 31-Rollback)** + **Hamburg 3 strukturelle Issues (Seebestattung-Doublette, Bestattungsrecht-Doublette, Cross-City-Orphan) behoben (19.05.2026, content-loop-pipeline → main Merge)**
