# Tool-Pre-Build Architektur-Empfehlung

**Helper-V3-Analyse** (22. Mai 2026) zur Frage: Wie 10 React+Babel-in-browser Tools auf indexierbaren/performanten Stand bringen?

## Verworfen

- **Option 2 (Webpack + React)**: Strikt dominiert von Vite. Mehr Komplexität, kein technischer Vorteil. 2026 keine Begründung für Greenfield.
- **Option 3 (Preact ohne Build)**: Bringt FCP/LCP-Verbesserung (~3 KB statt ~45 KB), aber löst Indexing-Kernproblem NICHT. Bleibt CSR — initial HTML leer. Halbe Lösung.

## Empfehlung — gemischt nach Tool-Komplexität

### Tier A — Vanilla HTML/JS Rewrite (Option 4)

**Tools**: bestattungskosten-rechner, kostenrechner, notfallkarte, fristen-radar, checkliste-todesfall (5 simple Form+Berechnungs-Tools)

- **Aufwand**: 2–4h pro Tool = ~15-20h gesamt
- **SEO-Effekt**: BESTE Lösung (HTML im Initial-Response, FCP/LCP optimal, Indexing garantiert)
- **Begründung**: Diese Tools haben Such-Intent ("bestattungskosten rechner") und MÜSSEN ranken. React ist Overhead bei Formular+Calc-Tools.
- **Reihenfolge**: ZUERST starten — schnellster Win, billigste Implementation

### Tier B — Vite + React + SSG (Option 1)

**Tools**: beerdigungsplaner, vorsorge-check (multi-step stateful) + evtl. abschiedsbrief/trauerrede/danksagung (template-based)

- **Aufwand**: 6–12h pro Tool + 10-15h Setup-Initialinvestment
- **SEO-Effekt**: Identisch zu Vanilla bei korrektem SSG-Setup
- **Begründung**: Mehrstufige State-heavy Tools — React-State ist nützlich, Vanilla-Rewrite teuer/bug-anfällig
- **Reihenfolge**: NACH Tier A — Infrastruktur erst aufbauen, wenn Tier A live + ranking-bestätigt

## Vor-Start-Check

Vor Rewrite je Tool kurz prüfen:
- `>~150 Zeilen JSX` oder `>2-3 useState` → Tier B
- Sonst → Tier A

abschiedsbrief/trauerrede/danksagung könnten Tier A ODER B sein — Tool-Code-Inspektion nötig.

## Geschätzter Gesamtaufwand

| Tier | Tools | Stunden |
|---|---|---|
| Tier A | 5 Tools | 15-20h |
| Tier B | 3-5 Tools | 30-50h + 10h Setup |
| Gesamt | 10 Tools | **55-80h** = 1.5-2 Wochen Vollzeit |

## Sofort-Action

Vor Rewrite-Start:
1. Pro Tool: Zeilen-Anzahl JSX zählen
2. `useState`-Vorkommen zählen
3. Tier-Zuordnung finalisieren
4. Tier A: zuerst bestattungskosten-rechner als Proof-of-Concept (höchster Such-Intent)
