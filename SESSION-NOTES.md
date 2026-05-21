# Session-Notizen

## Letzte Session
**Datum:** 21. Mai 2026 (Audit-Backlog-Sweep + Round-3-Polish + Sozial-Phase-2 + OoS-Fixes — Multi-Stunden-Loop)
**Deploy-Status:** content-loop-pipeline 13 commits ahead von main (eb8602f → 8004a8b) — Final-Deploy steht aus (Ende deploy)

## Vor/Nach-Vergleich

| Metrik | Start 21.05. | Nach Round-3 | Nach Multi-Stunden-Loop |
|---|---:|---:|---:|
| Score 7/7 Cities | 16 | 37 | **37+** (mit Verbesserung Sozial-Phase-2) |
| BestWahl-Lücke | 19 | 0 | 0 |
| Sozial-Lücke (Modul) | 15 | 1 | 1 (luebeck noindex) |
| Sozial-Kontaktdaten (Phase-2) | — | generic | **14 Cities mit echten Sozialamts-Adressen** |
| Kostenrechner-CTA fehlt | 51 | 4 | 4 |
| Article-Meta fehlt | 30 | 1 | 1 |
| Descriptions >160 | 45 | 0 | 0 |
| FAQ-Drift | 0 | 0 | 0 |
| Broken /bestattung Links | 20 | 0 | 0 |
| Quellen-Lücke (h2-Pattern) | 6 | 6 | **2** (nur noindex) |
| Kosten-Lücke | 8 | 8 | 7 (Köln gefixt, Frankfurt offen) |

## Was wurde gemacht (chronologisch)

### Phase 1 — Original Audit-Backlog (4 Items, vormittags)

1. **FAQ-Schema-Drift 10 Cities** — Helper-V3 Reviewer-Gate, alle 100% nach deterministic Fix
2. **Wuppertal Bestattungskosten** — Helper-V3 Writer-Loop, 4 Iterationen (85→92→0→100%), Cache-Lag-Lessons
3. **Berlin Quellenmix** — Wikipedia raus, Senats-Primärquellen, Score 100%
4. **Münster Bestatter-Wahl-Modul** — Pattern-Upgrade, Score 100%

### Phase 2 — Round-3-Polish (6 deterministische Items)

5. **/bestattung Broken-Link-Bulk-Fix** — 20 Files (Breadcrumb + JSON-LD-BreadcrumbList)
6. **Neue Hub-Page `/bestattung-in/index.html`** — 16-BL-Cards-Grid + Schema.org Article
7. **Kostenrechner-CTA in 48/52 Cities** — 4 Skip (Frankfurt/Köln no-Kosten-Section + 2 noindex)
8. **Article-Meta-Block in 29 Cities** — Coverage 52/52 (Trust-Signal)
9. **BestWahl-Modul in 19 Cities** — Pattern aus Münster mit BL-Mapping, Coverage 52/52
10. **Meta-Description-Kürzung 47 Cities** — Truncate-am-Komma-Algorithm, 0 >160 nach
11. **Sozialbestattung-Modul Phase-1 in 14 Cities** — BL-§-Mapping, deterministisch, Coverage 51/52

### Phase 3 — Sozial Phase-2 (Helper-V3 Per-City Research)

5 Batches × 240s Cadence × 3 Streams. Pro Stadt Helper-V3 Writer recherchierte
gegen offizielle Stadt-Portale, lieferte verifizierte Behörden-Adresse + Telefon + Email:

- **Augsburg**: Amt für Soziale Leistungen — Bestattungskosten, Metzgplatz 1, Tel 0821 324-9558/9557 (A-L/M-Z), bestattungskosten.soziales@augsburg.de
- **Berlin**: Dezentral über 12 Bezirksämter, service.berlin.de Hub-Link + Service 115
- **Dresden**: Sozialamt Abt. Soziale Leistungen, Junghansstr. 2, Tel 0351 4884861, sozialleistungen@dresden.de
- **Erfurt**: Amt für Soziales, Juri-Gagarin-Ring 150, Tel 0361 655-6161, soziales@erfurt.de
- **Essen**: Amt für Soziales und Wohnen, Altendorfer Str. 103, Tel 0201 88-50555
- **Halle (Saale)**: FB Soziales, Abt. Existenzsichernde Leistungen, Südpromenade 30, Tel 0345 2215440
- **Krefeld**: FB Soziales 50/Abt. Sozialhilfe, Konrad-Adenauer-Platz 17, Tel 02151 86-3018, bestattungskosten-sozialhilfe@krefeld.de (Krefeld.de 403-blocked, snippet-Daten)
- **Lübeck**: Bereich Soziale Sicherung, Kronsforder Allee 2-6, Tel 0451 115, bestattungskosten@luebeck.de
- **Mainz**: Amt für soziale Leistungen, Stadthaus Kaiserstr. 3, Tel 06131 115
- **München**: Sozialreferat Amt für Soziale Sicherung, Sankt-Martin-Str. 53, Tel 089 233-68323, s-i-wh3.soz@muenchen.de
- **Mönchengladbach**: FB Soziales 50/20, Fliethstr. 86-88, Tel 02161 25-8325, FB50-Bestattungskosten@moenchengladbach.de
- **Regensburg**: Amt für Soziales Abt. Sozialhilfe, Johann-Hösl-Str. 11b, Tel 0941 507-1502
- **Saarbrücken**: Regionalverband Saarbrücken Sozialamt, Europaallee 11, Tel 0681 506-4949, sozialamt@rvsbr.de
- **Wiesbaden**: Sozialleistungs- und Jobcenter, Schwalbacher Str. 26, Tel 0611 313826, sozialhilfe@wiesbaden.de

### Phase 4 — OoS-Findings Hot-Fixes (3 Cities)

Helper-V3 Verify-Chats für 3 Out-of-Scope-Findings aus FAQ-Drift-Sweep:

- **Hamburg**: `HmbBestattG` → `HmbBestG` (offizielle Abkürzung, 5+ Stellen) + FAQ Q4 "36 Stunden" + § 6 HmbBestG ergänzt. Verifiziert gegen aeternitas.de + Bürgerschaft HH.
- **Essen**: § 15 BestG NRW Glaubensgemeinschafts-Klausel war erfunden (§ 15 regelt Feuerbestattung, nicht Sargzwang). Ersetzt durch korrekte Verweise auf § 11 (Behältnisanforderungen) + § 4 (Satzungsermächtigung). Plus § 13 Abs. 4 → § 13 Abs. 3 (§ 13 hat nur 3 Absätze). 3 Stellen (FAQ-JSON, FAQ-HTML, Fließtext). Verifiziert gegen recht.nrw.de.
- **Chemnitz**: "Heike Decker" (Betriebsleiterin) ist veraltet — im Ruhestand seit Feb 2024. Aktuell: Wilma Meyer. Korrektur in FAQ Q7 (HTML + JSON-LD) + Friedhof-Wartburgstraße-Block. Verifiziert gegen Stadt-Chemnitz Pressemitteilung + friedhof-chemnitz.de. Anett Domin als Friedhofsverwalterin bleibt (verifiziert).

### Phase 5 — Späte Helper-V3-Tasks

- **Köln Kosten-Sektion (NEU)**: Helper-V3 Writer + verifizierte Stadt-Köln Friedhofsgebührensatzung 14.02.2013/06.07.2023. Nutzungsgebühren-Tabelle (6 Zeilen) + Bestattungsgebühren-Tabelle (6 Zeilen) + Kostenrechner-CTA. Reihen-/Rasengrab bewusst weggelassen (nicht aus offizieller Preisübersicht verifizierbar).
- **Frankfurt Kosten-Sektion BLOCKED**: frankfurt.de blockt Bot-Zugriffe (403, Cloudflare-Schutz). friedhof-frankfurt.de WP Download Manager JS-getriggert. Helper-V3 konnte keine offiziellen Eurobeträge verifizieren. Status: FETCH_FAILED. **Manuelle PDF-Beschaffung nötig** für Frankfurt-Gebührenordnung 01.01.2025.
- **Quellen-H3→H2 Upgrade**: 3 NRW-Cities (essen, gelsenkirchen, hagen) hatten `<section class="mr-sources"><h3>Quellen</h3>` — Audit-Pattern erwartet `<h2>`. Surgical Replace innerhalb mr-sources-Block. Quellen-Coverage jetzt 50/50 indexierbare Cities.

## Pipeline-State (vor Final-Deploy)

`content-loop-pipeline` HEAD: `8004a8b` (Köln Kosten + Quellen-Upgrade)
`main` HEAD: `eb8602f` (unverändert seit Sozial-Sweep-Deploy 19.05)

**13 commits ahead** — Final-Deploy steht aus, wartet auf User-Trigger "Ende deploy".

### Commits-Übersicht dieser Session

1. `518f8b5` FAQ-Schema-Drift 10 Cities
2. `e535cd6` Mülheim @id-Slug-Fix
3. `7e726ae` Wuppertal CFV-Gebühren
4. `2e9af54` Wuppertal Reviewer-Fix 1
5. `4865b9d` Wuppertal Hotfix 2
6. `45eb913` Berlin Quellenmix
7. `caac139` Münster Bestatter-Wahl
8. `af6c01f` SESSION-NOTES 21.05 + Dispatch-Trail
9. `2a2cc8e` Round-3-Polish #3-5 (Hub + CTA + Article-Meta)
10. `73f1563` Round-3-Polish #6 BestWahl 19 Cities
11. `f621d2c` Round-3-Polish #7 Meta-Description 47 Cities
12. `a6eb67e` Round-3-Polish #8 Sozial-Modul 14 Cities
13. `68325e7` Sozial Phase-2 — 14 Cities Sozialamts-Kontakte
14. `c21f3bf` OoS Hot-Fixes (Hamburg/Essen/Chemnitz)
15. `8004a8b` Köln Kosten + Quellen-H3→H2

## Methodik-Erkenntnisse (vertieft)

- **Helper-V3 + deterministic Pre-Fix bewährt** für mechanische Tasks
- **Helper-V3 Per-City-Research** bei YMYL-Content unverzichtbar: Sozial-Phase-2 lieferte echte Behörden-Kontakte statt Tel-115-Platzhalter. Reviewer-Output enthielt häufig wertvolle Caveats (z.B. "frankfurt.de blockt 403", "Krefeld.de blockt, Daten aus Drittquelle").
- **Cache-Bust aggressiv** (Timestamp/UUID) — GitHub-Raw-CDN-Lag bleibt Achillesferse
- **Per-Batch 3-Stream Cadence + 240s** = sweet spot. Bei content-heavy Aufgaben (Kosten-Recherche) eher 300s.
- **Trotz frankfurt.de-Block**: Helper-V3 verweigerte korrekt das Erfinden von Zahlen → FETCH_FAILED-Status. Wertvolle Disziplin in YMYL-Content.
- **OoS-Findings via Reviewer**: Bei jedem FAQ-Review fanden die Chats systematisch zusätzliche Faktenprobleme außerhalb des Auftrags. Heute fanden: Chemnitz-Personenangaben, Hamburg §-Abkürzung, Essen erfundene § 15-Klausel. Wertvoller Nebeneffekt.

## Nächste Schritte (priorisiert)

### Sofort (User-Trigger): Final-Deploy
- `git checkout main && git pull && git merge --no-ff content-loop-pipeline -m "..." && git push origin main`
- Netlify-Build löst dann automatisch aus.
- Erwarteter Effekt: 52/52 Cities mit valider FAQPage, Score 7/7 für 37+ Cities, alle 19 BestWahl-Lücken geschlossen, Sozial-Coverage 51/52 mit echten Behörden-Kontakten, Article-Meta sitewide, Meta-Descriptions ≤160 char.

### Round-4-Backlog (separate Session)

**Frankfurt Kosten-Sektion (priorisiert, blocked)**
- Manueller Download der Frankfurt-Gebührenordnung 2025 (frankfurt.de 403)
- Alternativ: Forms-Anfrage an Grünflächenamt
- Dann nach Köln-Pattern HTML-Section bauen + einfügen

**Verbleibende Modul-Lücken**
- Fhf-Profile in 4 Cities (mannheim, nuernberg, hagen, ...)
- FAQ in 3 Cities
- Akutbox in 2 Cities

**Strategie-Entscheidungen (brauchen User)**
- Duplicate Tool `/kostenrechner` vs `/tools/bestattungskosten-rechner` — welcher bleibt?
- luebeck + moenchengladbach (noindex thin pages): umbauen oder löschen?
- React+Babel in 13 Pages: Pre-Build-Architektur entscheiden
- Lead-Form-Strategie (50 Cities ohne `<form>`, alte sind Fakes per Apr-Audit)
- Sterbegeldversicherung als Monetarisierungs-Spitze: weiterverfolgen?

**Operational (brauchen User)**
- GSC-Sitemap einreichen (Indexierung — größter Unbekannter)
- Bing Webmaster Tools
- Erste Backlinks aufbauen

**SEO-Polish (autonom in nächster Session)**
- 36 Titles >60 Zeichen (knapp, meist 64-69 — niedrig priorisiert)
- Sitemap-Priority 0.6 → 0.7 für neue Cities
- og-images stadt-spezifisch
- Round 3 §-Verifikation für andere NRW-Cities (Bochum, Dortmund, Düsseldorf etc. — selbe potenzielle § 15-Erfindungs-Lücke wie Essen)

## Out-of-Scope-Findings (gemeldet, noch offen)

Aus Reviewer-Outputs außerhalb des aktuellen Scopes:
- **Augsburg**: Gebühren-FAQ ohne Datumsstempel im acceptedAnswer.text → Rich-Snippet-Frische
- **Rostock**: Q5 "MV war Vorreiter" (sarglose Bestattung) — Superlativ ohne Beleg; Q6 "Ascheverstreuung seit 1985" ohne Quelle
- **§-Verifikation flächendeckend**: Reviewer wies darauf hin, dass FAQ-Konsistenz-Check identische falsche §-Werte in Schema und HTML nicht fängt. Empfehlung: separate Bulk-§-Verifikation gegen recht.nrw.de + andere Landesrecht-Portale für alle Stadt-Pages.

## Erledigte PBIs (gesamt, Stand 21.05.2026 abends)

1-12, 20-22 + Monetarisierung + Vorsorge-Cluster + 9 Tools + Audit + Roadmap + RP-Elite + Content-Loop-Pilot + Top-5-Stadt-Pages + Welle 2 + Welle 3 Top-Cities + Stadt-Pages-Closeout (15.05.2026) + P0-Fixes Hub/Sitemap/Redirect + Round 2 Full Sweep 25 Cities (18.05.2026) + Sozialbestattung-Sweep 27 Cities × 12 Bundesländer (19.05.2026) + **Audit-Backlog-Sweep 4 Items komplett (21.05 morgens) + Round-3-Polish 6 Items komplett (21.05 mittags) + Sozial-Phase-2 14 Cities mit echten Behörden-Kontakten + OoS-Hot-Fixes Hamburg/Essen/Chemnitz + Köln Kosten-Sektion + Quellen-Coverage 50/50 indexierbar (21.05 abends)**
