# Session-Notizen

## Letzte Session
**Datum:** 23. April 2026

## Sprint-Status

### ✅ Sprint #1 — Homepage statisch neu bauen — ERLEDIGT

**Audit-Score:** 39 → **80** (Ziel war ≥75)
**Issues:** 5 Crit/High → **0**
**Warnings:** 7 → **0**
**Wins:** 4 (lang-Attribut, Content-Tiefe passend, Schema, Monetarisierungs-Element)

**Was umgebaut wurde:**
- React + @babel/standalone komplett raus
- Statisches HTML mit echtem Hero, 8 Topic-Cards, "Drei Phasen"-Sektion, Trust-Block, "Wofür wir nicht da sind"-Sektion
- 642 Wörter sichtbarer Content (vorher 101)
- 1 H1, 4 H2, 15 interne Links
- `<main id="main">`-Landmark sichtbar
- Schema.org Organization + WebSite + SiteNavigationElement (publisher, inLanguage, mehr Properties)
- Mobile-Nav als 25-Zeilen-Vanilla-JS (kein React-Overhead)
- Inline-Styles als CSS-Klassen extrahiert
- Methodik-Link in Hauptnavigation prominent (Vorbereitung für Sprint #4)

**OG-Image neu erstellt:**
- `assets/og-image.svg` (1200×630, machsruhig-Branding mit Brand-Farben)
- Eingebunden via og:image, twitter:image, Schema.org logo
- Erstes OG-Image überhaupt im Repo (war 0/98 Seiten ohne)

**Title + Meta:**
- Title: "mach's ruhig — Vorsorge, Trauer & Bestattung. Wenn es soweit ist." (65c, perfekt)
- Description: 136c (im 120-165 Sweet-Spot)
- H1/Title-Keyword-Match jetzt OK (beide haben "Vorsorge, Trauer, Bestattung" + "Mach's ruhig")

### 🔄 Sprint #2-5 — noch ausstehend

| # | Ticket | Aufwand | Status |
|---|---|---|---|
| 2 | 5 Gold-Städte statisch ausliefern | 10-15h | Nächste Session |
| 3 | Über-uns-Seite live | 3-4h | Nach Sprint #2 |
| 4 | Autorenblock + Methodik-Verlinkung sitewide | 4h | Nach Sprint #3 |
| 5 | Akutfall-Hauptseite "Erste 24 Stunden" | 6-8h | Nach Sprint #4 |

## Gesamt-Site-Score-Entwicklung

- **23.04.2026 morgens:** 54.7 (vor Audit-Bug-Fix)
- **23.04.2026 mittags:** 59.0 (nach Bug-Fix)
- **23.04.2026 abends:** **59.5** (nach Sprint #1)

**Erwartete Ziele:**
- Nach Sprint #2 (5 Gold-Städte ≥85): Gesamt-Score ~63-65
- Nach Sprint #3-4 (Trust-Layer): ~67-70
- Nach Sprint #5 (Akutfall-Seite): ~70-72

## Nächste Schritte

**Sprint #2 — 5 Gold-Städte statisch ausliefern**

Aktueller Stand der 5 Gold-Städte (Berlin, Frankfurt, Hamburg, Köln, München):
- Score 40/100 jeweils
- Inhaltlich Gold (7-9 Friedhofsnamen, 15-31 Eurozahlen, kuratierte Inhalte)
- Aber: Komplett CSR via @babel/standalone → Google sieht praktisch nichts
- Schema vorhanden, aber LocalBusiness/FuneralHome fehlt

**Vorgehen Sprint #2 (analog zu Sprint #1):**
1. Pro Stadt: bestehender Gold-Content statisch ausliefern
2. React/Babel raus, Vanilla-Mobile-Nav rein
3. FuneralHome-Schema ergänzen
4. OG-Image-Verweis ergänzen
5. Audit-Score ≥85 pro Stadt

Templates sind über alle 5 Städte identisch — Pattern ist nach 1. Stadt repeatable.

## Saisonale Trigger im Auge behalten

- **Mitte Oktober:** Allerheiligen-Content live
- **Anfang November:** Totensonntag + Weihnachten-Content live
- **Mitte Dezember:** Silvester-Content live

## Verbleibende offene Entscheidungen (kein Blocker für Sprint)

- **Entscheidung 4:** Gesetzestext-Archiv anlegen? (entscheiden wenn C.3 startet)
- **Entscheidung 5:** Lead-Backend-Tool (entscheiden wenn Phase E abgeschlossen)
- **Entscheidung 6:** Affiliate-Anträge wann starten? (Empfehlung: nach B+C.1)

## Erledigte PBIs (gesamt)

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 21, 22
+ Monetarisierungs-Basis, Vorsorge-Cluster, 9 neue Tools/Seiten (März/April 2026)
+ 23.04.2026: Audit + Backlog + Phase A teilweise (noindex 45 Generic-Städte) + Schema-Parser-Bug-Fix + Doku-Konsolidierung + 3 Schlüssel-Entscheidungen + Markteroberungs-Erweiterung + 7-Tage-Sprint
+ 23.04.2026: **Sprint #1 — Homepage statisch neu gebaut (Score 39→80)** + erstes OG-Image (assets/og-image.svg)
