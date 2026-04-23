# Session-Notizen

## Letzte Session
**Datum:** 23. April 2026 (Abend, Sprint #3)
**Deploy:** Ja (mit "ende deploy")

## Was wurde gemacht

### ✅ Sprint #3 — Über-uns-Seite live (B.1) — ERLEDIGT

Neue Seite `ueber-uns.html`:
- 353 Zeilen, **1050 sichtbare Wörter**
- **Audit-Score: 75/100**
- 0 HTML-Strukturfehler
- Schema.org: **AboutPage + Organization + BreadcrumbList**, mit `foundingDate`, `knowsAbout`, `publishingPrinciples` → `/methodik`
- Vanilla-JS Mobile-Nav, OG-Image als PNG, Skip-Link als CSS-Klasse, sauberes `</main>`-Closing (kein Copy-Paste-Fehler aus Methodik-Vorlage)
- Print-Styles vorhanden

Inhaltliche Abschnitte:
- Warum gibt es machsruhig (Branchenkritik + Haltung)
- Wer steht dahinter (Redaktion + Fachpool-Rollen als "im Aufbau" transparent gekennzeichnet)
- Redaktionelle Haltung (4 Prinzipien-Cards)
- Finanzierung (Bestatter-Vermittlung + Vorsorge + "Was wir nicht tun")
- Abgrenzung zu Branchenportalen
- Unabhängigkeit
- Kontakt & Feedback

### Begleitende Anpassungen

- **index.html:** Footer-Link auf `/ueber-uns` als erster Eintrag im "Über uns"-Block
- **methodik.html:** Inhaltlicher Querverweis auf `/ueber-uns` im "Wer wir sind"-Abschnitt + Footer-Link ergänzt
- **_redirects:** Trailing-Slash-Normalisierung `/ueber-uns/` → `/ueber-uns` 301
- **sitemap.xml:** Neuer Eintrag für `/ueber-uns` (Priorität 0.6, changefreq monthly)

### Sitewide-Änderung: machsleicht-Verbindung entfernt

Entscheidung in dieser Session: **Keine sichtbare Verbindung zwischen machsruhig und machsleicht auf der Seite.** Vier Stellen bereinigt:
- ueber-uns.html Unabhängigkeits-Abschnitt (umformuliert zu "eigenständiges Projekt")
- ueber-uns.html Footer ("Unabhängiges Informationsportal" statt "Projekt der mach's-Familie")
- methodik.html "Wer wir sind"-Absatz (Schwestermarke-Satz entfernt)
- methodik.html Footer (analog)

### Backlog-Aufräumen (davor in dieser Session)

- **Sprint #2** von "teilweise ERLEDIGT" auf **STAGE 1 DONE** umklassifiziert
- Neues Ticket **D.2.1** angelegt: "5 Gold-Städte auf Score ≥85 heben (Stage 2 von A.2)" — gebündelt mit Phase D.2 Schema-Upgrades
- **B.1** um Status-Block + Nachschärf-Notizen (B.1.1) ergänzt: Redundanz zur Methodik kürzen, Title/H1 schärfen, Fachpool-Cards-Reihenfolge, Floskel-Diät — Trigger: wenn >50 Besuche/Monat oder Phase D/E

## Gesamt-Site-Score-Entwicklung

- Session-Start: 61.2
- Nach Sprint #3: **61.37** (leichter Anstieg durch neue Seite mit Score 75)

## 🔄 Sprint #4-5 — noch ausstehend

| # | Ticket | Aufwand | Priorität |
|---|---|---|---|
| 4 | Autorenblock + Methodik-Verlinkung sitewide (B.2 + B.3) | 4h | Nächste Session |
| 5 | Akutfall-Hauptseite "Erste 24 Stunden" (C.1.1) | 6-8h | Nach Sprint #4 |

## Nächste Schritte

**Sprint #4: Autorenblock + Methodik-Verlinkung sitewide**

Konzept:
- "Redaktion machsruhig.de" + ggf. "Fachlich geprüft von: [Name], [Rolle]" als sichtbarer Block auf allen YMYL-Seiten
- Methodik-Link prominent auf jeder Content-Seite
- Schema.org `author` referenziert "Organization machsruhig.de"
- Schema.org `reviewedBy` referenziert Person-URLs (sobald Fachpool existiert)

## Offene Punkte für später

- **methodik.html + trauerrede-schreiben.html: HTML-Strukturfehler** (je 2) — vorbekannt, nicht kritisch, nicht in Sprint #3 adressiert
- **LocalBusiness/FuneralHome-Schema** für 5 Gold-Städte (Ticket D.2.1)
- **Sitemap.xml stale:** hat noch 45 noindex-Städte drin (Phase D)
- **17 kaputte interne Links** (`/bestattung` 16×, `/tools/brief-an-meine-liebsten` 1×)
- **B.1.1 Über-uns-Nachschärfung** wenn Traffic kommt (siehe BACKLOG)

## PAT-Status

**⚠️ GitHub PAT läuft am 25.04.2026 ab** — in 2 Tagen. Rotation planen bevor's beim nächsten Push scheitert.

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
+ 23.04.2026 Abend (früh): **Sprint #2 5 Gold-Städte (Score 40→75)** + Deploy
+ 23.04.2026 Abend (spät): **Sprint #3 Über-uns (B.1, Score 75)** + Backlog-Umklassifizierung Sprint #2 → D.2.1 + sitewide machsleicht-Entkopplung + Deploy
