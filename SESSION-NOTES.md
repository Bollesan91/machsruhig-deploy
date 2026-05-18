# Session-Notizen

## Letzte Session
**Datum:** 18. Mai 2026 (Validation-Loop V2 — Round 2 Iteration + Hub-Page + Audit-Fixes)
**Deploy-Status:** main = 5ccd225 (Hub-Page + Sitemap-Erweiterung + Redirect-Fix LIVE)

## Was wurde gemacht

### P0-Fixes nach ChatGPT-Audit (commit 037fac7 -> merge 5ccd225)

| Fix | Status |
|---|---|
| **/bestatter/ Hub-Seite** (47 indexierbare Cities, 16 Bundeslaender-Gruppen) | NEU |
| **Sitemap erweitert** (19 -> 48 Bestatter-URLs, 29 fehlende Cities ergaenzt) | FIX |
| **/bestatter Redirect** (muenchen -> /bestatter/ Hub) | FIX |

### Validation-Loop V2 — Round 2 Batch 1 (5 Cities)

Reviewer->Improver->Re-Reviewer Pipeline auf Round 2 mit 25 zuvor untouched Cities:

| Stadt | Reviewer-Verdict | Status |
|---|---|---|
| **Koeln** | MAJOR-FIX (Selbstwiderspruch muslim 1965/1968, FAQ-Schema=/=HTML, Waldbestattung-Fehler) | dispatched |
| **Frankfurt** | FAIL/3 MAJOR (Rat-Beil 1828/1929, Paragraph 18 vs 19 FBG falsch, dead Cross-Link) | dispatched |
| **Magdeburg** | PASS+1 MAJOR (FAQ-Kapellengebuehr 296Euro fehlt, Cremer-Mauthausen-Halluzination) | dispatched |
| **Potsdam** | MUST-FIX (1866/1867 Eroeffnung, Lenne-Chronologie, Hofgaertner) | dispatched |
| **Rostock** | MAJOR-FIX (Ascheverstreuung 'erste D' unbelegt, FAQ-Schema=/=HTML) | dispatched |
| **Leipzig** (R19) | Bach 1894 vs 1900 + 82-ha Hedge + Friedhofsgebuehren Stand-Datum | commit 55487b3 |
| **Muenster** | FAIL/2 Deploy-Blocker (Babel-JSX, Print-CSS-Bug, noindex) | dokumentiert, kein Fix |

### Validation-Loop-Methodik bewaehrt

- 5 parallele Chrome-Tabs, Reviewer in fresh tabs, Cache-bust ?cb=Date.now() fuer GitHub Raw
- 3-min Wakeup-Cadence
- Improver-Risk bestaetigt: jede Iteration kann neue Halluzinationen einbringen -> Re-Review essential
- Sycophancy-Isolation durch separate Tabs

### Methodik-Erkenntnisse Round 2

1. **AI-Iterations-Konvergenz schlecht**: Tiefe systemische Faktenprobleme (Datums-Widersprueche, FAQ-Schema=/=HTML) brauchen editorial review, nicht weitere AI-Loops
2. **FAQ-Schema-Drift-Pattern**: Koeln 6 vs 5 Fragen, Magdeburg Kapellengebuehr-Drift, Rostock MV-Bestattungsfrist — Schema.org-Audit-Script noetig
3. **Datums-Widersprueche-Pattern**: Bach 1894/1900, Rat-Beil 1828/1929, Potsdam 1866/1867 — Standardliteratur-Cross-Check noetig
4. **Muenster-Architektur-Blocker**: Babel-Client-Side-JSX rendert fuer Googlebot nicht — Gold-Template-Hybrid (statisches Form-Markup) ist die Loesung, dokumentiert in BACKLOG-AUDIT.md

### LIVE-Gesamtstatus

- **50 >=85%-Pipeline-Cities LIVE** (unveraendert seit 15.05.)
- **+3 P0-Fixes** (Hub/Sitemap/Redirect) auf main 5ccd225
- **Round 2: 5/25 Cities reviewed**, 5 Improver dispatched, 20 Cities pending Review

## Naechste Schritte

### Round 2 Continuation (next session)
- Re-Review der 5 dispatched Improver-Outputs (Koeln/Frankfurt/Magdeburg/Potsdam/Rostock)
- Batch 2 — 5 weitere Cities aus Pool: Aachen, Augsburg, Braunschweig, Chemnitz, Darmstadt
- Batch 3 — Erfurt, Freiburg, Gelsenkirchen, Halle, Heidelberg
- Batch 4 — Kassel, Kiel, Leverkusen, Mainz, Muelheim
- Batch 5 — Oberhausen, Oldenburg, Regensburg, Saarbruecken, Wiesbaden

### Muenster-Entscheidung pending
Gold-Template-Upgrade (statisches Lead-Form + Print-CSS-Fix + noindex entfernen) ODER noindex-Akzeptanz. Backlog-Item.

### Systemische Bulk-Fixes erwogen
- FAQ-Schema-vs-HTML Konsistenz-Audit-Script
- Datums-Cross-Check gegen Standardliteratur (manual)
- Friedhofsgebuehren-Tabellen Stand-Datum-Caption-Audit (YMYL)

## Offene Fragen

- Wann Muenster Gold-Upgrade ziehen?
- Bulk-Audit-Script fuer FAQ-Schema-Drift sinnvoll oder per-City editorial?
- Sitemap-Priority-Anpassung (0.6 -> 0.7) fuer neue Cities — Polish

## Erledigte PBIs (gesamt)

1-12, 20-22 + Monetarisierung + Vorsorge-Cluster + 9 Tools + Audit + Roadmap + RP-Elite + Content-Loop-Pilot + Top-5-Stadt-Pages + Welle 2 + Welle 3 Top-Cities + Stadt-Pages-Closeout (15.05.2026) + **P0-Fixes Hub/Sitemap/Redirect + Round 2 Batch 1 Dispatch (18.05.2026)**

## Pipeline-State

- content-loop-pipeline HEAD = 037fac7
- main HEAD = 5ccd225 (Merge enthaelt 037fac7)
- origin/main aligned, Netlify deployed
- Round 2 Improver-Tabs (5) noch offen — bei Continuation re-checken
