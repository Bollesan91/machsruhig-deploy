# Session-Notizen

## Letzte Session
**Datum:** 23. April 2026

## Was wurde gemacht

### Triple-Audit durchgeführt (intern + Substanz + extern)

- **Bestehendes Audit-Skript** `_dev/audit-all-pages.py` (714 Zeilen, 9 Kategorien) gelaufen
- **Bug-Fix:** `jsonld_types()` las @graph-Wrapper nicht rekursiv → Schema-Werte waren fälschlich leer. Nach Fix: Gesamt-Score 54.7 → 59.0
- **Neue Substanz-Analyse** `_dev/stadt-quality-analysis.py` — misst echte lokale Tiefe (Friedhofs-Eigennamen, Eurozahlen, Generic-Floskeln)
- **Externes strategisches Audit** (6,6/10) integriert

### Harte Erkenntnisse

- **Gesamt-Score 59.0/100** (98 Seiten)
- **Bimodale Stadt-Qualität:** 5 GOLD (Berlin, Frankfurt, Hamburg, Köln, München) + 45 GENERIC (identisches Template, 349 Wörter, 0 Euro-Zahlen, 4 Floskeln)
- **9 Deploy-Blocker:** @babel/standalone rendert JSX clientseitig → Google sieht praktisch keinen Content. Betroffen: Homepage (Score 39!), 5 Gold-Städte (Score 40!), 3 weitere Tools
- **Bitterste Pointe:** Die 5 Gold-Städte sind inhaltlich Gold, aber SEO-unsichtbar wegen CSR. Das erklärt, warum externes Audit "München nur knapp am Ziel" sagte
- **OG-Image fehlt auf 98/98 Seiten**
- **Schema.org: vorhanden, aber falsche Typen** für Stadtseiten (haben FAQPage/Service, fehlt LocalBusiness/FuneralHome)

### Phase A teilweise umgesetzt

- **45 Generic-Stadtseiten auf `noindex,follow` gesetzt** (alle außer Berlin, Frankfurt, Hamburg, Köln, München)
- Jede Seite mit HTML-Kommentar dokumentiert (Datum + Verweis auf BACKLOG.md)
- Reversibel via sed
- **Noch offen in Phase A:** Homepage + 5 Gold-Städte + 9 Tools aus CSR-Hölle retten

### Doku-Konsolidierung (NEU am Ende der Session)

Doppelte/parallele Strategie-Dokumente waren entstanden. Nach Vorbild machsleicht aufgeräumt:

**Vorher:**
- 7 separate Strategie-Dokumente in `_dev/docs/` (content-klassen, seitentypen, cta-hierarchie, linklogik, monetarisierung, qa-gates, content-plan)
- Plus alter `.claude/session-notiz.md` (01.04.2026, stale)
- Plus `BACKLOG.md` im Root (837 Zeilen, neu)

**Nachher (gemäß Doku-Regel analog machsleicht):**
- `STRATEGIE.md` (Root, 472 Zeilen) — synthetisiert die 7 _dev/docs Dokumente + externe Audit-Erkenntnisse
- `BACKLOG.md` (Root, 1.055 Zeilen) — erweitert um Cluster C.5 Trauer, C.6 Bürokratie, C.7 neue Tools, C.8 Vorsorge-Detail
- `SESSION-NOTES.md` (Root) — Session-Gedächtnis
- `_dev/archiv/` — alle 7 originalen Strategie-Dokumente plus README.md mit Konsolidierungs-Mapping
- `.claude/session-notiz.md` gelöscht (stale)

**Backlog wuchs von 49 auf 73 Tickets** durch Integration der content-plan-Inhalte:
- Trauer-Cluster (Erstes Jahr, Zurück zur Arbeit, 8 saisonale Seiten, Beileid digital) = 11 Tickets
- Bürokratie (Erbschein, Witwenrente, Sozialbestattung vertieft, Verträge kündigen, Dokumenten-Matrix) = 5 Tickets
- Neue Tools (Trauerfeier-Planer, Sterbeurkunden-Rechner, Erbschaftssteuer, Witwenrente, Trauer-Tagebuch, Digitaler-Nachlass-Inventar) = 6 Tickets
- Vorsorge-Detail (Vorsorgevollmacht, Betreuungsverfügung als eigene Seiten) = 2 Tickets
- Quality-Gates-Sektion ergänzt (vorher fehlte das im Backlog)

### Aufräumarbeiten Detail

- Alte Roadmap-Dateien entfernt (von BACKLOG.md ersetzt)
- Dupliziertes Audit-Skript im Root entfernt (canonisch: `_dev/audit-all-pages.py`)
- Stadt-Quality-Tools nach `_dev/` verschoben
- 7 Strategie-Dokumente von `_dev/docs/` nach `_dev/archiv/` verschoben
- Stale `.claude/session-notiz.md` gelöscht
- Root jetzt sauber: nur `BACKLOG.md` + `STRATEGIE.md` + `SESSION-NOTES.md`

## Nächste Schritte

**Höchste Priorität — Phase A (Deploy-Blocker):**

1. **Homepage statisch neu bauen** (aktuell Score 39, nur 101 Wörter für Google sichtbar) — 4-6h
2. **5 Gold-Städte statisch rendern** (aktuell Score 40, Content existiert aber unsichtbar) — 10-15h
3. **9 Tool-Seiten mit Static Shell versehen** (H1, Intro, FAQ als statisches HTML, Tool als Widget) — 18-27h

**Parallel Phase B — Trust-Layer:**

4. Über-uns-Seite mit Haltung — blockiert durch Entscheidung 1 (Autoren-Modell)
5. Autoren-System sitewide einführen — blockiert durch Entscheidung 1
6. Methodik prominenter, Disclaimer einheitlich — 4h

**Quick-Wins aus Phase D:**

7. OG-Image für alle 98 Seiten (Master + 4-5 Varianten) — 3h
8. LocalBusiness/FuneralHome-Schema für 5 Gold-Städte — 2-3h

**Saisonale Trigger im Auge behalten:**

- **Mitte Oktober:** Allerheiligen-Content live
- **Anfang November:** Totensonntag + Weihnachten-Content live
- **Mitte Dezember:** Silvester-Content live

## Offene Fragen (blockieren Folge-Arbeiten)

1. **Autoren-Modell:** Klarname (du) / Redaktions-Pseudonym / Hybrid? → blockiert Phase B
2. **Content-Kapazität:** Stunden pro Woche realistisch? Research selbst oder Agent?
3. **Gesetzestext-Archiv:** Zentrale `_dev/gesetze/`-Struktur anlegen?
4. **CSR-Fix-Strategie:** Pre-Rendering (Build-Script) / Static Rewrite / Hybrid?
5. **Lead-Backend:** Netlify Forms / Formspree / eigener Worker?
6. **Affiliate-Anträge:** Jetzt starten (4 Wochen Bearbeitungszeit) oder warten?

## Erledigte PBIs (gesamt)

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 21, 22
+ Monetarisierungs-Basis, Vorsorge-Cluster, 9 neue Tools/Seiten (März/April 2026)
+ Audit + Backlog + Phase A teilweise (noindex 45 Generic-Städte) + Schema-Parser-Bug-Fix (23.04.2026)
+ Doku-Konsolidierung: STRATEGIE.md + BACKLOG erweitert + _dev/docs archiviert (23.04.2026)
