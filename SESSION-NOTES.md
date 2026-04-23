# Session-Notizen

## Letzte Session
**Datum:** 23. April 2026
**Deploy:** Ja (Ende der Session mit "ende deploy")

## Sprint-Status

### ✅ Sprint #1 — Homepage statisch neu bauen — ERLEDIGT

**Audit-Score:** 39 → **80/100**
- 642 sichtbare Wörter (vorher 101)
- 1 H1, 4 H2, 15 interne Links
- `<main id="main">`-Landmark
- Schema.org Organization + WebSite + SiteNavigationElement
- Mobile-Nav als Vanilla-JS, kein React, kein @babel/standalone
- OG-Image als PNG eingebunden

### ✅ Sprint #2 — 5 Gold-Städte statisch — ERLEDIGT (teilweise)

**Audit-Score pro Stadt:** 40 → 75
- Berlin: 1766 Wörter
- Frankfurt: 1438 Wörter
- Hamburg: 2189 Wörter
- Köln: 1776 Wörter
- München: 1872 Wörter

**Was gemacht:**
- React + ReactDOM + @babel/standalone entfernt
- Lead-Form durch statischen Trust-Hint-Block ersetzt (Lead-Integration kommt in Phase F)
- Mobile-Nav als Vanilla-JS
- OG-Image-Tags ergänzt (PNG + image:type + image:alt)
- Skip-Link: Inline-Style → CSS-Klasse
- Methodik-Link in Hauptnavigation
- HTML-Strukturfehler behoben: `</div>` → `</main>`

**Akzeptanzkriterium ≥85 noch nicht voll erreicht.** Delta zu 85:
- LocalBusiness/FuneralHome-Schema fehlt noch (geplant Phase D.2)
- Monetarisierungs-Warning (Lead-Form raus, kommt in Phase F zurück)
- H2-Count teils unter Ziel

Die Seiten sind aber **für Google vollständig sichtbar** — das war das Sprint-Ziel. Die Feinarbeit auf ≥85 kommt mit Phase D/E.

### Neu: validate-all.sh Quality Gate (Stufe 1)

6 automatische Checks vor Push:
1. HTML-Syntax-Validität
2. Keine Platzhalter
3. Audit-Score-Prüfung (inkl. Homepage ≥75)
4. Kaputte interne Links
5. Sitemap-Konsistenz
6. OG-Image-Referenzen

3-Stufen-Workflow analog machsleicht:
- Stufe 1: `bash validate-all.sh` → PASSED
- Stufe 2: Elite Check manuell (Content, UX, Pietät, Blast-Radius)
- Stufe 3: "Was habe ich NICHT gecheckt?" explizit benennen

### Neu: Audit-Skript erweitert

Neue Checks im `_dev/audit-all-pages.py`:
- OG-Image-Format-Warning (SVG → Warning, PNG/JPEG bevorzugt)
- @babel/standalone-Warning auf Content-Seiten (auch ohne 5+ Leaks)
- skip-link-Accessibility-Check
- `check_internal_links()`: aggregierte Link-Validität, Ergebnis im JSON-Report

## Gesamt-Site-Score-Entwicklung

- Session-Start: 59.0
- Nach Sprint #1: 59.5
- Nach Sprint #2: **61.2**
- Deploy-Blocker: 9 → 3 (6 entschärft)

## 🔄 Sprint #3-5 — noch ausstehend

| # | Ticket | Aufwand | Priorität |
|---|---|---|---|
| 3 | Über-uns-Seite live | 3-4h | Nächste Session |
| 4 | Autorenblock + Methodik-Verlinkung sitewide | 4h | Nach Sprint #3 |
| 5 | Akutfall-Hauptseite "Erste 24 Stunden" | 6-8h | Nach Sprint #4 |

## Nächste Schritte

**Sprint #3: Über-uns-Seite live**

Konzept:
- URL: `/ueber-uns` (neu)
- Inhalt: Haltung, Redaktion, Reviewer-Pool, Finanzierung, Unabhängigkeit
- Basis: Festgelegte Entscheidung 1 — "machsruhig Redaktion" + Fachpool-Reviewer
- Schema.org AboutPage + Organization
- Prominent verlinkt von Homepage, Footer, Methodik

**Offene Punkte für später:**
- methodik.html + trauerrede-schreiben.html: HTML-Strukturfehler (je 2) — nicht kritisch
- LocalBusiness/FuneralHome-Schema für 5 Gold-Städte (Phase D.2)
- Sitemap.xml stale: hat noch 45 noindex-Städte drin (Phase D)
- 17 kaputte interne Links (`/bestattung` 16×, `/tools/brief-an-meine-liebsten` 1×)

## Saisonale Trigger im Auge behalten

- **Mitte Oktober:** Allerheiligen-Content live
- **Anfang November:** Totensonntag + Weihnachten-Content live
- **Mitte Dezember:** Silvester-Content live

## Verbleibende offene Entscheidungen (kein Blocker)

- **Entscheidung 4:** Gesetzestext-Archiv anlegen? (entscheiden wenn C.3 startet)
- **Entscheidung 5:** Lead-Backend-Tool (entscheiden wenn Phase E abgeschlossen)
- **Entscheidung 6:** Affiliate-Anträge wann starten? (Empfehlung: nach B+C.1)

## Erledigte PBIs (gesamt)

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 21, 22
+ Monetarisierungs-Basis, Vorsorge-Cluster, 9 neue Tools/Seiten (März/April 2026)
+ 23.04.2026 Vormittag: Audit + Backlog + Phase A teilweise (noindex 45 Generic-Städte) + Schema-Parser-Bug-Fix + Doku-Konsolidierung + 3 Schlüssel-Entscheidungen + Markteroberungs-Erweiterung + 7-Tage-Sprint
+ 23.04.2026 Nachmittag: **Sprint #1 Homepage (Score 39→80)** + Audit-Skript-Erweiterung + validate-all.sh + OG-Image als PNG
+ 23.04.2026 Abend: **Sprint #2 5 Gold-Städte (Score 40→75)** + Deploy
