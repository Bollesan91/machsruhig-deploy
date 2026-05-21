# Session-Notizen

## Letzte Session
**Datum:** 21. Mai 2026 (Audit-Backlog-Sweep — FAQ-Drift + Wuppertal + Berlin + Münster)
**Deploy-Status:** content-loop-pipeline 7 commits ahead von main — Final-Deploy steht aus (Ende deploy)

## Was wurde gemacht

### Item 1 — Bulk-FAQ-Schema-Drift-Audit (10 Cities, alle 100%)

Discovery-Audit (`_dev/audit/audit-faq-drift.py`) fand 10 Cities mit FAQPage JSON-LD vs HTML FAQ-Mismatch:
- augsburg, chemnitz, essen, muelheim: Q-Texte unterschiedlich (Schema stale gegenüber Content-Refinements)
- berlin, hamburg: Schema deutlich unterversorgt (4 vs 7 Qs)
- bremen, rostock: 1 Q in Schema fehlend
- darmstadt, muenster: KEIN FAQPage in JSON-LD (komplett fehlend)

Strategie: HTML ist die Wahrheit. Schema deterministisch aus HTML regeneriert (`_dev/audit/fix-faq-drift.py`).

**Pre-existing JSON-LD-Parse-Bug** in darmstadt + muenster behoben (`fix-jsonld-quotes.py`):
- `„text"` mit straight U+0022 als Closing-Quote → JSON-Parser-Bruch
- Beide JSON-LD-Blöcke waren bisher ungültig → von Google ignoriert
- Fix: U+0022 → U+201D (typografisches Closing)

Helper-V3 Reviewer-Chats in 4 Batches (3+3+3+1, 240s Cadence):
- Augsburg/Berlin/Bremen: 3× CLEAN @ 100%
- Chemnitz/Darmstadt/Essen: 3× CLEAN @ 100%
- Hamburg/Muelheim/Muenster: 3× CLEAN @ 100%
- Rostock: 1× CLEAN @ 100%

Drift-Audit post-fix: **0/52 Cities mit Drift, 52/52 mit valider FAQPage**.

**Mülheim @id-Hotfix** nach Reviewer-Flag: FAQPage @id war `/muelheim/#faq`, alle anderen @ids nutzen kanonischen Slug `/muelheim-an-der-ruhr/`. Fix angewendet. (Bug-Quelle: fix-faq-drift.py nutzte Directory-Name für @id-Konstruktion — sollte WebPage-@id-Slug erben für Cities mit abweichendem kanonischen Slug.)

### Item 2 — Wuppertal Bestattungskosten (4 Iterationen → 100%)

Vorher: Cost-Table mit "Orientierungsspannen aus vergleichbaren NRW-Großstädten" (Düsseldorf/Essen/Solingen/Remscheid) — Reviewer-Backlog flaggte als "nicht-offizielle Gebühren".

Web-Fetched: **Friedhofsgebührensatzung des CFV Wuppertal vom 05.12.2023, gültig ab 04.03.2024** (PDF mit pdftotext extrahiert).

Neue Struktur:
- § 4 Nutzungsgebühren: 15 Zeilen (Reihen-/Wahl-/Reihengemeinschafts-/Wahlgemeinschaftsgrabstätten, Rasenfeld-Produkte, Innenraum- + Außenkolumbarien) — alle mit Ruhezeit und exaktem Euro-Betrag aus der Satzung
- § 6 Bestattungsgebühren: 6 Zeilen (Erd/Urne/Kolumbarium + Friedhofskapelle)
- Fließtext: 235€/155€ gärtnerische Grundausstattung, 79€/67€ Verlängerung je Jahr, Friedhofsliste § 4(7)

Iterations-Verlauf:
- v1 (deterministisch): Score 85% — Reviewer flaggte 2 MUST-FIX (Auftragsverwaltungs-Behauptung + Rasenfeld-Labels)
- v2 (Hotfix 1): Score 92% — Reviewer flaggte 2 Drift (klassisches Grabfeld + Kirchhofstr/Erbhöfen waren in CFV § 1)
- v3 (Hotfix 2): Score 0% (Reviewer hatte stale GitHub-Raw-Cache erwischt)
- v4 (aggressiver Cache-Bust): Score 100% — A/B-Strings beide präsent, alle Beträge exakt aus PDF

**Lesson:** GitHub-Raw-CDN-Lag kann auch mit Cache-Bust-Parameter weiter stale-Inhalte zurückgeben. Aggressiver Cache-Bust (Timestamp oder unique-ID) ist Pflicht.

### Item 3 — Berlin Quellenmix (1 Iteration → 100%)

Vorher (Line 351 "Friedhofslandschaft in Zahlen"):
- "221 Friedhöfe" / "1.147 ha gesamt" / "575 ha landeseigen" — aus "Wikipedia-Übersicht"
- Widersprach Rest der Seite: FAQ/Hero/Schema sagten einheitlich 222 / 580 ha

Neu (Primärquellen statt Wikipedia):
- 222 Friedhöfe aus offizieller `liste_friedhoefe.pdf` (Stand 31.12.2024)
- 580 ha landeseigen aus amtlicher Broschüre `broschuere_fhinberlin.pdf`
- 116 evangelisch / 9 katholisch — Counts aus PDF-Liste verifiziert
- Wikipedia-Referenz ersatzlos gestrichen, 411 ha ev (unverifizierbar) raus
- 79 Gartendenkmäler + 23/14 geschlossen-Sätze raus (nicht aus Senats-Liste belegbar)

Reviewer: 0 Wikipedia-Treffer, 0× "1.147" / "575 ha", 8× "222", 3× "580 ha/Hektar". VERDICT CLEAN @ 100%.

### Item 4 — Münster Bestatter-Wahl-Modul (1 Iteration → 100%)

Vorher: Sektion "Bestatter in Münster — Auswahl und Qualitätsindikatoren" als 3 Fließtext-Absätze. Heatmap-Pattern erkannte das nicht als vollwertiges Modul (Score 5/7).

Neu (entspricht Wuppertal/Düsseldorf-Standard):
- H2: "Bestatter-Wahl in Münster — Qualitätskriterien"
- `<ul>` mit 6 strukturierten Kriterien: BDB-Mitgliedschaft, RAL-Gütezeichen, Preisliste, Kostenvoranschlag, Sonderformen (mit Münster-Bezug Lauheide muslimisch + Hohe Ward jüdisch), Vorsorgevertrag
- Cross-Links zu Nachbarstädten (Osnabrück, Dortmund, Bielefeld, Essen)

Reviewer: 6/6 Kriterien-Coverage, alle Strukturchecks PASS. VERDICT CLEAN @ 100%.

## Out-of-Scope-Findings (durch FAQ-Reviewer entdeckt, separat zu behandeln)

Die FAQ-Reviewer haben mehrfach Fakten-Probleme außerhalb des FAQ-Konsistenz-Scopes gemeldet:

- **Berlin** (Batch A): Fließtext-Abschnitt "Berliner Friedhofslandschaft" hatte 221 vs überall sonst 222, 1.147 ha als Einzelwert. → **erledigt in Item 3**
- **Chemnitz** (Batch B):
  - Q7 nennt "Heike Decker" als Betriebsleiterin, Wartburgstraße-Block nennt "Anett Domin" — zwei verschiedene Personen, zwei Rollen. YMYL-Risiko bei Personenangaben.
  - Krematorium-FAQ datiert FeuerbestattungsG auf 29.05.1906, Urnenhain-Block legt ersten Spatenstich auf 16.12.1905 (Bau vor Rechtsgrundlage — historisch plausibel, aber prüfen).
  - Gebühren "Stand Januar 2024" bei Footer "Stand Mai 2026" → Aktualitäts-Frage.
- **Hamburg** (Batch C): F4 "Überführung in Leichenhalle innerhalb 36 Stunden (gesetzlich verpflichtend)" — § 17 HmbBestG bitte gegen Primärquelle prüfen.
- **Essen** (Batch B): §-Verweise auf BestG NRW (Q1/Q6/Q8: 24h / 10 Tage / § 13 / § 15) sind im Schema und HTML identisch zitiert — Konsistenz-Check würde identisch-falsche Werte nicht fangen. Empfohlen: separate §-Verifikation gegen recht.nrw.de.
- **Augsburg** (Batch A): Gebühren-FAQ (#2, #8) trägt keinen Datumsstempel im acceptedAnswer.text — für isoliertes Rich-Snippet könnte Zeitbezug fehlen.
- **Rostock** (Batch D): Q5 "MV war Vorreiter" (sarglose Bestattung) — Superlativ ohne Beleg. Q6 "Ascheverstreuung seit 1985" ohne sichtbare Quelle.

## Pipeline-State

- `content-loop-pipeline` HEAD: `caac139` (Münster Bestatter-Wahl)
- `main` HEAD: `eb8602f` (unverändert seit Sozialbestattung-Sweep-Deploy am 19.05.2026)
- **7 commits ahead — Final-Deploy steht noch aus** (User-Trigger "Ende deploy" erwartet)

Commits in dieser Session:
1. `518f8b5` FAQ-Schema-Drift behoben: 10 Cities synchronisiert
2. `e535cd6` Mülheim FAQPage @id Slug-Inkonsistenz
3. `7e726ae` Wuppertal: NRW-Spannen → offizielle CFV-Satzung
4. `2e9af54` Wuppertal Reviewer-Fix 1: Auftragsverw. + Rasenfeld-Labels
5. `4865b9d` Wuppertal Hotfix 2: klassisches Grabfeld + Kirchhofstr/Erbhöfen
6. `45eb913` Berlin: Wikipedia-Quelle raus, Senats-Primärquellen
7. `caac139` Münster: Bestatter-Wahl-Modul Pattern-Upgrade

## Methodik-Erkenntnisse

- **Helper-V3 + deterministic Pre-Fix bewährt**: Mechanische Schema-Korrekturen erst per Python, dann Reviewer-Loop zur Qualitätssicherung — spart 90% Reviewer-Iterationen vs. Multi-Chat-Writer-Loop für mechanische Tasks.
- **Reviewer findet OoS-Issues**: Bei jedem FAQ-Drift-Review fanden die Chats zusätzliche Fakten-Probleme außerhalb des Auftrags (z.B. Berlin 221/222). Wertvoller Nebeneffekt — auch wenn nicht im Score.
- **Cache-Bust ist Pflicht-Disziplin**: Selbst bei `?cb=20260521b1` kann GitHub-Raw stale-cached. Aggressiver, unique Cache-Bust-Token pro Iteration (z.B. `cb=fresh$(date +%s)`).
- **240s Cadence funktioniert**: Helper-V3-Chats laufen meist in 150-250s durch. 240s ist guter Puffer — kürzer geht (~120s), aber dann häufiger 1× Nachschauen nötig.
- **Score-Threshold 85%**: Pragmatischer Cut-off. Wuppertal v1 traf 85% genau und hatte 2 echte MUST-FIX — auch über Threshold lohnen sich die letzten 1-2 Iterationen.

## Nächste Schritte (priorisiert)

### Sofort (User-Trigger): Final-Deploy
- `git checkout main && git merge --no-ff content-loop-pipeline -m "..." && git push origin main`
- Netlify-Build löst dann automatisch aus.

### Round 3 Polish (separate Session)
- **OoS-Findings abarbeiten** (Chemnitz Personenangaben, Hamburg § 17, Essen §-Verifikation, Augsburg Datumsstempel, Rostock Vorreiter-Behauptung).
- **Kostenrechner-CTA** in alle Stadt-Pages.
- **Sitemap-Priority 0.6 → 0.7** für neue Cities.
- **og-images stadt-spezifisch**.
- **fix-faq-drift.py @id-Slug-Bug:** WebPage-@id-Slug erben statt Directory-Name (Mülheim-Lessons-learned).

### Audit-Backlog komplett abgeräumt (Stand 21.05.2026)
- ✓ Bulk-FAQ-Schema-Drift-Audit
- ✓ Wuppertal nicht-offizielle Gebühren
- ✓ Berlin Quellenmix
- ✓ Münster Bestatter-Wahl-Modul

## Offene Fragen (für nächste Session)

- Bulk-§-Verifikation gegen recht.nrw.de für alle 13 NRW-Cities? (Lücke aus FAQ-Konsistenz-Check)
- Chemnitz: Personenangaben in YMYL-Content beibehalten oder neutralisieren?
- Hamburg: § 17 HmbBestG Überführungsfrist gegen Primärquelle (Hamburg.de hat aktuellen Volltext).
- Round 3 Polish jetzt oder nach Indexierung (GSC-Sitemap-Submit als Priorität)?

## Erledigte PBIs (gesamt, Stand 21.05.2026)

1-12, 20-22 + Monetarisierung + Vorsorge-Cluster + 9 Tools + Audit + Roadmap + RP-Elite + Content-Loop-Pilot + Top-5-Stadt-Pages + Welle 2 + Welle 3 Top-Cities + Stadt-Pages-Closeout (15.05.2026) + P0-Fixes Hub/Sitemap/Redirect + Round 2 Full Sweep 25 Cities (18.05.2026) + Sozialbestattung-Sweep 27 Cities × 12 Bundesländer (19.05.2026) + **Audit-Backlog-Sweep 4 Items komplett (21.05.2026)**
