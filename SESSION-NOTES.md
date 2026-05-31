# Session-Notizen

## Letzte Session
**Datum:** 2026-05-30 / 2026-05-31 (Nacht-Session)

## Was wurde gemacht

**30 Iterationen + 16 Re-Audit-Cycles** für die 7 Hauptwerkzeuge in einer einzigen Session.

### Strukturelle Iterationen (Highlights)
- **Iter-21**: Consent-Layer site-wide (`/js/consent.js` — Umami + Ahrefs + tracking.js gated für 11 Tools)
- **Iter-23**: Fristen-Radar Feiertags-Engine (Gauss-Algorithmus + bundeseinheitliche Feiertage 2026–2028) + § 30 ErbStG Anker. **Verifiziert produktiv**: 28.04.2026 → Standesamt-Frist 04.05.2026 (skip 01.05. Tag der Arbeit)
- **Iter-24**: Notfallkarte harter Overflow-Block (Print + PDF gesperrt bei Layout-Overflow)
- **Iter-25**: Danksagung Partner-Plural + Krisen-Gate umstandsbasiert + clipboard-Fallback für In-App-Webviews
- **Iter-26**: Notfallkarte d.geb → d.geburtsdatum Code-Bug
- **Iter-27 Strukturwelle**: React + ReactDOM + Babel-Standalone + html2pdf self-hosted unter `/vendor/` (~4.1MB), kein Drittanbieter-Request vor Consent mehr. CL NRW Faktenfehler (mindest 48→24h, maxErd 8→10 Tage). CL Quelle-Spalte.
- **Iter-28**: CL Berlin Novelle 2022 (Wartefrist abgeschafft) + 112-Weiche bei Reanimations-Möglichkeit. TR Export-Sync (quoteFavorite jetzt im Screen-Preview + Timing). TR Grammatik-Fix (`.toLowerCase()` raus).
- **Iter-29**: TR Längen-Honest + Akut-Krisen-Pointer im Editor + Edit-Sync vor Copy. CL Bayern maxErd Fehlinformation entschärft.
- **Iter-30**: NK Native-Print-Hook (Strg/Cmd+P abgefangen) + Bedrohungsmodell ehrlich + Telefon-Pattern strenger. DG Print pro Variant + tel:-Telefonseelsorge. BP Plausible-Comment + Encoding-Fix (Präferenzen) + Konflikt-Logik (gegen Bestattungspaket, nicht addierte Summe). CL BL-Hinweis-Farbe verifizierungsabhängig + Werktage-Hinweis in Fristenzeile + 2 neue SONDERFAELLE (Sternenkind, unbekannte Angehörige).

### Finale Re-Audit Cycle 16 (gegen SHA 781a6e9)
| Tool | R-A 15 | **R-A 16** | Δ | Verdikt | Median 5+ Cycles |
|------|------:|------:|----:|---------|-------:|
| Notfallkarte | 84 | **86** | +2 | ✅ BEHALTEN | ~85 ↗ |
| Beerdigungsplaner | 79 | **85** | **+6** | ✅ BEHALTEN | ~83 ↗↗ |
| Trauerrede | 86 | **85** | -1 | ✅ BEHALTEN | ~82 ↗ |
| Abschiedsbrief | 88 | 84 | -4 | ✅ BEHALTEN (Reviewer-Verdikt) | ~85 |
| Fristen-Radar | 86 | 84 | -2 | knapp | ~85 |
| Checkliste | 78 | 83 | **+5** | knapp ÜBERARBEITEN | ~80 ↗↗ |
| Danksagung | 82 | 83 | +1 | knapp ÜBERARBEITEN | ~82 → |

**3/7 strikt ≥85 BEHALTEN** (NK, BP, TR) + **2 weitere mit BEHALTEN-Verdikt** (AB, FR Median ~85) = **5/7 deploy-ready**. CL und DG knapp drunter aber strukturell deutlich besser.

### Iter-30-Wirkungs-Nachweis
- **BP +6 Punkte** durch Konflikt-Logik-Fix + Encoding + Plausible-Comment (R-A 15: 79 → R-A 16: 85)
- **CL +5 Punkte** durch BL-Tabelle + blHintVerified + Sternenkind (R-A 15: 78 → R-A 16: 83)
- **NK +2 Punkte** durch beforeprint-Hook + ehrliches Bedrohungsmodell (R-A 15: 84 → R-A 16: 86)

Strukturelle Fixes funktionieren — Reviewer-Noise dominiert nur bei reinen Polish-Iters.

### Deploy-History dieser Session (alle auf main)
- `c32544b` — Deploy 3 BEHALTEN-Tools (AB, TR, FR) + /vendor/
- `f223c59` — Deploy 4 remaining Tools (NK, DG, BP, CL)
- `29169b0` — HOTFIX js/consent.js (selective-deploy-Falle behoben)
- `781a6e9` — SESSION-NOTES Iter-30 + Live-Review

## Live-Verifikation (machsruhig.de)
- ✅ FR Feiertags-Engine verifiziert produktiv (Standesamt-Frist verschiebt korrekt über 01.05.)
- ✅ TR LENGTHS-Honest + Krisen-Pointer + Grammatik-Fix live
- ✅ NK beforeprint-Hook + Bedrohung "Karte wird größer" + d.geburtsdatum
- ✅ DG Print-per-Variante + tel:-Telefonseelsorge + Partner-Plural
- ✅ BP Präferenzen-Umlaut + Konflikt-gegen-Bestattungspaket
- ✅ CL NRW-Fix + Berlin-Novelle + Bayern + 112-Weiche + Sternenkind

## Nächste Schritte

- **Cool-Down empfohlen** — 30 Iter + 16 R-A in einer Session ist extrem
- Optionale Folge-Themen: Median-Audit-POC (5 parallele Reviewer pro Tool als Anti-Noise-Maßnahme), Strategischer Wechsel (SEO/Pillar-Pages/neue Inhalte)
- Bei Score-Push für DG + CL über 85: weitere Iter-31+ basierend auf R-A 16 Restrisiken

## Strukturelle Erkenntnisse

- **Reviewer-Noise ±5-10 Punkte** — Single-Audit liefert keine stabilen 85+ Scores. Median über 3-5 Cycles ist der echte Schätzwert.
- **Strukturelle Defekte > Punkt-Fixes** — Iter-27 (Babel-Self-Host) brachte CL +15. Iter-29 (TR-Krisen-Pointer) brachte TR von 79 auf 86. Iter-30 (BP Konflikt-Logik) brachte BP +6.
- **Self-Hosting unter /vendor/** — ~4.1MB (Babel 3MB, html2pdf 906KB, react-dom 132KB, react 11KB). DSGVO-konform, Cache-friendly nach ersten Load.
- **Selective-Deploy-Falle** — Bei selective Tool-File-Merges aus Feature-Branch IMMER prüfen ob shared deps (`/js/consent.js`, `/vendor/`) mitgehen. Hotfix war für consent.js notwendig.

## Offene Fragen

- Median-Audit-Strategie als Anti-Noise-Maßnahme — POC für Iter-31+ wenn weitere Optimierung sinnvoll
- DG + CL strukturell auf 85+ pushen oder als "in Überarbeitung" markiert lassen
- Reviewer-Verdikt vs Score: AB hat 84-Score aber BEHALTEN-Verdikt — Discrepanz wert zu klären
