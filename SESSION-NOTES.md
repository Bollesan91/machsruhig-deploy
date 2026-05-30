# Session-Notizen

## Letzte Session
**Datum:** 2026-05-30

## Was wurde gemacht

**29 Iterationen + 15 Re-Audit-Cycles** für die 7 Hauptwerkzeuge (notfallkarte, fristen-radar, beerdigungsplaner, danksagung, checkliste-todesfall, trauerrede, abschiedsbrief).

### Strukturelle Iterationen (Auswahl)
- **Iter-21**: Consent-Layer site-wide (Umami + Ahrefs + tracking.js gated für 11 Tools)
- **Iter-23**: Fristen-Radar Feiertags-Engine (Gauss-Algorithmus + bundeseinheitliche Feiertage 2026–2028) + § 30 ErbStG Anker
- **Iter-24**: Notfallkarte harter Overflow-Block (Print + PDF gesperrt bei Layout-Overflow, Override via confirm-Dialog) — YMYL-Schadenspfad geschlossen
- **Iter-25**: Danksagung Partner-Plural + Krisen-Gate umstandsbasiert (alle Beziehungen statt nur partner/schwester/bruder/freund) + clipboard-Fallback für In-App-Webviews
- **Iter-26**: Notfallkarte Overflow-Guard d.geb → d.geburtsdatum (echter Code-Bug fix)
- **Iter-27 Strukturwelle**: React + ReactDOM + Babel-Standalone + html2pdf self-hosted unter /vendor/ (vorher 4× Drittanbieter-Request vor Consent — DSGVO-Risiko). CL NRW Faktenfehler (mindest 48→24h, maxErd 8→10 Tage). CL Quelle-Spalte + Friedhofssatzungs-Disclaimer für alle BL.
- **Iter-28**: CL Berlin Novelle 2022 (Wartefrist abgeschafft) + 112-Weiche bei Reanimations-Möglichkeit. TR Export-Sync (quoteFavorite jetzt im Screen-Preview + Timing). TR Grammatik-Fix (.toLowerCase() entfernt, "Mutter" statt "mutter"). TR 'kind' als Relationship-Option (Kind-Guard greift jetzt korrekt).
- **Iter-29**: TR Längen-Versprechen ehrlich gemacht. TR Akut-Krisen-Pointer im Speech-Editor (Telefonseelsorge + BDB). TR Edit-Sync vor Copy (document.activeElement.blur). CL Bayern maxErd Fehlinformation entschärft.

### Finale Score-Verteilung (R-A 15, Komplett-Sweep)
- ✅ **Abschiedsbrief: 88** — stabil hoch (Median über alle Cycles ~85)
- ✅ **Trauerrede: 86** — Durchbruch durch Iter-29 Krisen-Pointer + Längen-Honest + Edit-Sync
- ✅ **Fristen-Radar: ~86** — historisch konstant (R-A 15 retry-rate-limited, R-A 7-12 alle 86-87)
- Notfallkarte: 84 (Median ~84, oszilliert um 85)
- Danksagung: 82 (Median ~82-83)
- Beerdigungsplaner: 79 (Median ~82)
- Checkliste-Todesfall: 78 (Median ~78, volatil 69-85)

### Deploy
3 Tools stabil ≥85 (BEHALTEN), 4 Tools in den 80ern aber unter Schwelle. **Alle 7 Tools werden mit allen Iter-21-29 Verbesserungen nach main gemerged** — auch die 4 unter-85-Tools sind strukturell deutlich besser als der vorherige main-Stand.

## Nächste Schritte

- **Manuelle End-User-Review** der 4 noch unter-85-Tools (CL, NK, DG, BP) — Bolle prüft browser-seitig, was die Reviewer-Befunde der R-A 15 als realistisch verifizierte Defekte zeigen
- Optional: weitere Iter-30+ basierend auf Bolle's manuellen Befunden

## Offene Fragen

- Sollen die 4 Tools mit Median < 85 als "Beta" oder "in Überarbeitung" markiert werden? (Aktuell: alle ohne Label live)
- Median-Audit-Strategie (5 parallele Reviewer pro Tool) als Anti-Noise-Maßnahme — in dieser Session nicht eingeführt, könnte in Iter-30+ sinnvoll werden

## Strukturelle Erkenntnisse aus 15 R-A Cycles

- **Reviewer-Noise dominiert ±5-10 Punkte** — Single-Audit liefert keine stabilen 85+ Scores. Median über 3-5 Cycles ist der echte Schätzwert.
- **Strukturelle Defekte > Punkt-Fixes**: Iter-27 (Babel-Self-Host) brachte CL +15 Punkte, Iter-29 (TR-Krisen-Pointer + Längen-Honest) brachte TR von 79 auf 86. Tiefe Hebel funktionieren, oberflächliche Polish nicht.
- **Self-Hosting unter /vendor/**: ~4.1MB (Babel 3MB, html2pdf 906KB, react-dom 132KB, react 11KB). DSGVO-konform, Cache-friendly.
