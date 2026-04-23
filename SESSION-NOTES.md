# Session-Notizen

## Letzte Session
**Datum:** 23. April 2026

## Zusammenfassung dieser Session

Aus Audit wurde Strategie wurde Plan. **Drei strategische Entscheidungen gefällt, 7-Tage-Sprint definiert, Markteroberungs-Komponente ergänzt.** Bereit für Umsetzung ab nächster Session.

## Festgelegte Entscheidungen (verbindlich)

### Entscheidung 1 — Autorenmodell
**"machsruhig Redaktion" + Fachpool-Reviewer.**
Kein Klarname. Sicheres Modell, skalierbar, E-E-A-T-Signal über namentliche Reviewer (Bestatter, Jurist, Trauerbegleiter, Seelsorger). Aufgabe: Fachpool aufbauen.

### Entscheidung 2 — CSR-Fix-Strategie
**Hybrid:** Homepage + 5 Gold-Städte komplett statisch ausliefern, 9 Tools als Static Shell + React-Widget im Container. Babel-Standalone raus aus Content-Seiten, bleibt nur in Tool-Widgets.

### Entscheidung 3 — Wochenkapazität
**6-8 h/Woche.** machsruhig wird Hauptprojekt. Realistische Marker:
- Q2 2026 (Mai-Juni): Phase A + B fertig
- Q3 2026: Phase C läuft, saisonaler Trauer-Content rechtzeitig
- Q4 2026: Phase F-Aktivierung (Affiliate, Lead-Funnel)

## Was passierte in dieser Session

### Triple-Audit + Bug-Fix
- Internes Vollaudit mit Bug-Fix (jsonld_types() las @graph nicht rekursiv) → Score 54.7 → 59.0
- Substanzanalyse Stadtseiten: 5 GOLD + 45 GENERIC, bimodal, kein Mittelbau
- Externes strategisches Audit (6,6/10) integriert
- 9 Deploy-Blocker identifiziert: Homepage Score 39, 5 Gold-Städte Score 40, 3 weitere Tools — alle wegen @babel/standalone CSR

### Phase A teilweise umgesetzt
- 45 Generic-Stadtseiten auf `noindex,follow` gesetzt
- HTML-Kommentar mit Datum + Verweis auf BACKLOG.md
- Gold-Städte (Berlin, Frankfurt, Hamburg, Köln, München) bleiben indexiert

### Doku-Konsolidierung
- 7 _dev/docs Dokumente nach `_dev/archiv/` verschoben + README mit Mapping
- STRATEGIE.md (Master-Strategie) im Root erstellt
- BACKLOG.md (operative Tickets) im Root erweitert
- Stale .claude/session-notiz.md gelöscht
- Doku-Regel analog machsleicht: nur STRATEGIE.md + BACKLOG.md + SESSION-NOTES.md im Root

### Backlog-Erweiterung
- Cluster C.5 Trauer (11 Tickets, inkl. saisonale Seiten)
- Cluster C.6 Bürokratie (5 Tickets)
- Cluster C.7 Neue Tools (6 Tickets)
- Cluster C.8 Vorsorge-Detail (2 Tickets)
- Quality-Gates-Sektion im Backlog
- Saisonale Trigger-Liste

### Bewertungs-Diskurs (intern + ChatGPT)
- Erste Bewertung: 6,5/10 für Markteroberung — Plan zu defensiv
- Zweite Bewertung: 8,2/10 für Authority-Aufbau, 6,8/10 für Markteroberung — fairer Frame
- ChatGPT: "Jetzt loslegen, aber 3 Entscheidungen vorher festzurren"
- Ergebnis: 5 Markteroberungs-Sektionen ergänzt (M.1 Off-Page, M.2 Distribution, M.3 Kronjuwelen, M.4 Markt-KPIs, M.5 Moats) — als Vorlauf für Phase D-E, nicht als Blocker für Start

### 7-Tage-Sprint definiert
Erstes Element im BACKLOG. Klare Reihenfolge:
1. Homepage statisch neu bauen (4-6h)
2. 5 Gold-Städte statisch ausliefern (10-15h, parallel)
3. Über-uns-Seite live (3-4h)
4. Autorenblock + Methodik-Verlinkung sitewide (4h)
5. Akutfall-Hauptseite "Erste 24 Stunden" (6-8h)

Gesamt: 12-18h sinnvoll arbeitbar. Bei 6-8h/Woche realistisch in 7 Arbeitstagen mit Puffer.

## Nächste Schritte (in Reihenfolge)

**Diese Session beendet.** Nächste Session ist Umsetzung Sprint-Item #1.

1. **Sprint #1: Homepage statisch neu bauen** — 4-6h
   - React/Babel-Standalone raus
   - H1 statisch, ≥4 H2-Blöcke, ≥10 interne Links
   - Schema.org Organization + WebSite + SiteNavigationElement
   - `<main>`-Landmark sichtbar
   - Akzeptanz: Audit-Score ≥75, Lighthouse ≥90

2. **Sprint #2: 5 Gold-Städte statisch** — 10-15h, kann parallel
   - Bestehender Gold-Content statisch ausliefern
   - FuneralHome-Schema ergänzen
   - Akzeptanz: Score ≥85 pro Stadt

3-5: Über-uns-Seite, Autorenblock, Akutfall-Hauptseite (siehe BACKLOG → 7-Tage-Sprint)

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
