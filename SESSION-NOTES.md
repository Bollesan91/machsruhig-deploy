# Session-Notizen

## Letzte Session
**Datum:** 18. Mai 2026 (Validation-Loop V2 — Round 2 Full Sweep, 25 Cities, ~4h Pipeline)
**Deploy-Status:** Round 2 deploy-ready auf content-loop-pipeline, Merge nach main im Gange

## Was wurde gemacht

### Round 2 — Komplette Validation aller 25 zuvor untouched Cities

| Batch | Cities | Status |
|---|---|---|
| Batch 1 | Koeln/Frankfurt/Magdeburg/Potsdam/Rostock | 5/5 CLEAN |
| Batch 2 | Aachen/Augsburg/Braunschweig/Chemnitz/Darmstadt | 5/5 CLEAN |
| Batch 3 | Erfurt/Freiburg/Gelsenkirchen/Halle/Heidelberg | 5/5 CLEAN (Heidelberg Round-2 noetig) |
| Batch 4 | Kassel/Kiel/Leverkusen/Mainz/Muelheim | 5/5 verified (Kassel PARTIAL bei Gebuehrensatzung — als-ist akzeptiert) |
| Batch 5 | Oberhausen/Oldenburg/Regensburg/Saarbruecken/Wiesbaden | 5/5 CLEAN nach Round-2 |

### Aufgewendete Iterationen

- 25 Reviewer-Tabs (1x pro City), je strict Prompt mit MAJOR-only Filter
- 22 Improver-Anwendungen (3 Cities CLEAN ohne Fix: Braunschweig, Freiburg, Oberhausen)
- 25 Re-Review-Tabs (1x pro Improver-City), in fresh Tabs zur Sycophancy-Isolation
- 5 Round-2-Fixes wo Re-Review noch PARTIAL meldete (Heidelberg/Kassel/Regensburg/Saarbruecken/Mainz)

### Pattern-Erkenntnisse aus 25 Cities

1. **FAQ-Schema-vs-HTML-Mismatch** (~12 Cities betroffen): Haeufigster MAJOR. JSON-LD und HTML driften beim FAQ-Block. Google verlangt 1:1 fuer Rich-Results.
2. **Falsche Paragraph-Referenzen** (~8 Cities): § 30 statt § 32 (Heidelberg), § 7 statt § 4 (Leverkusen), § 12 statt § 1 (Leverkusen), § 18b statt § 18 (Chemnitz), § 29 statt § 22 (Saarbruecken), § 8 statt § 13 (Wiesbaden), Art. 1 statt Art. 12 (Regensburg).
3. **YMYL-Stand-Datum** (~6 Cities): Eurobetraege ohne Datierung — Standesamt-Gebuehren, Friedhofsgebuehren.
4. **Faktenfehler** (~5 Cities): Bach-Umbettung 1894 vs 1900 (Leipzig), Wixhausen-Eingemeindung 1937 vs 1977 (Darmstadt), Eichhof 37/39 ha-Sprung (Kiel), Ostfriedhof Aachen 18.->28.8.1803, Schalke-Fan-Feld 2008 vs Dez 2012 (Gelsenkirchen).
5. **Cross-Link-Fehler** (~3 Cities): Falsche /bestatter/-Anker (Augsburg, Frankfurt), Tote Links auf Ingolstadt/Landshut (Muenchen — bereits gefixt).

### Methodik-Erkenntnisse

- **Python-Surgical-Fix dominant**: schneller, deterministisch, kein AI-Truncation-Risk. 22/25 Cities ueber Python gefixt.
- **AI-Improver nur fuer komplexe Generierung** (Koeln FAQ-Schema-Rewrite). Truncation-Risk bei langen HTML-Outputs (~30k+ chars).
- **claude.ai Concurrency-Cap ~3-4 Streams**: 5-Tab-Cadence triggerte regelmaessig "Zu viele Antworten". 4-Stream-Cadence ab Batch 5 stabiler.
- **Re-Review essential**: Improver fuehrt teilweise neue Issues ein (Frankfurt Dativ-Fehler "Gräber" -> "Gräbern") oder loest nicht vollstaendig (Heidelberg 2/4 PARTIAL).

### Audit-P0/P1 Sofortmassnahmen (parallel zum Round 2)

- /bestatter/ Hub-Route -> /bestatter/ (war fehlerhaft auf muenchen) — gefixt vor Round 2
- Koeln HTML komplett gerendert (37 KB statt 52 Zeilen) — Round 2 Batch 1
- Muenchen Tote Cross-Links auf Ingolstadt + Landshut entfernt (404-Ziele)
- HTTP-Sweep: 47/47 Hub-Cities = HTTP 200 OK. ChatGPT's "41 Cache miss" war Crawler-Artifact.

### Pipeline-State

- `content-loop-pipeline` HEAD nach Round 2: ~24 Commits (00779a3 -> Wiesbaden e36309f)
- `main` aktuell auf 8d6b7a1 (vor Round 2)
- **Merge content-loop-pipeline -> main steht an = Netlify-Deploy**

## Naechste Schritte

### Audit-Backlog (nicht in Round 2 erledigt)

- Luebeck Lead-Sprache aufraeumen (noindex bleibt vorerst)
- Bulk-Audit-Script fuer FAQ-Schema-Drift (systemisch ~12 Cities betroffen) entwickeln
- Wuppertal "nicht-offizielle Gebuehren" durch echte Wuppertal-Satzungsdaten ersetzen (Audit-Hinweis)
- Berlin Quellenmix (Wikipedia raus, Primaerquellen rein) — Audit-Hinweis

### Round 3 Pending (Polish, nicht blockierend)

- Kostenrechner-CTAs in alle deploy-faehigen Stadt-Pages einziehen
- Sitemap-Priority 0.6 -> 0.7 fuer neue Cities
- og-images stadt-spezifisch

## Offene Fragen

- Muenster Gold-Template-Upgrade (Babel-Client-JSX-Architektur) wann?
- Bulk-FAQ-Schema-Audit-Script jetzt oder bei naechstem Sweep?

## Erledigte PBIs (gesamt, Stand 18.05.2026)

1-12, 20-22 + Monetarisierung + Vorsorge-Cluster + 9 Tools + Audit + Roadmap + RP-Elite + Content-Loop-Pilot + Top-5-Stadt-Pages + Welle 2 + Welle 3 Top-Cities + Stadt-Pages-Closeout (15.05.2026) + P0-Fixes Hub/Sitemap/Redirect + **Round 2 Full Sweep 25 Cities (18.05.2026)**
