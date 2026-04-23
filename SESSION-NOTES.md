# Session-Notizen

## Letzte Session
**Datum:** 23. April 2026 (Abend, Sprints #3 + #4 Teil 1)
**Deploy-Status:** Sprint #3 + Methodik-Schärfung + Sprint #4 Teil 1 deployed mit "ende deploy".

## Was wurde gemacht

### ✅ Sprint #3 — Über-uns-Seite live (B.1) — ERLEDIGT & deployed

Neue Seite `ueber-uns.html`:
- 353 Zeilen, **1050 sichtbare Wörter**
- **Audit-Score: 75/100**, 0 HTML-Strukturfehler
- Schema.org: **AboutPage + Organization + BreadcrumbList**, mit `foundingDate`, `knowsAbout`, `publishingPrinciples` → `/methodik`
- Inhaltliche Abschnitte: Warum gibt es machsruhig / Wer steht dahinter (Redaktion + Fachpool-Rollen als "im Aufbau" transparent) / Redaktionelle Haltung / Finanzierung / Abgrenzung zu Branchenportalen / Unabhängigkeit / Kontakt & Feedback
- **Begleit-Anpassungen:** Homepage-Footer-Link, Methodik-Querverweis + Footer-Link, `_redirects` (Trailing-Slash-301), sitemap.xml (neuer Eintrag, Priorität 0.6)
- **Sitewide-Entkopplung:** Alle machsleicht/mach's-Familie-Verweise auf ueber-uns.html + methodik.html entfernt (4 Stellen)

Bekannte Nachschärf-Punkte (B.1.1 im BACKLOG) — triggern wenn >50 Besuche/Monat oder Phase D/E-Referenz:
- Redundanz zur Methodik (~40% Überlapp) kürzen
- Title/H1 schärfen
- Fachpool-Cards: Aufbau-Status nach oben ziehen
- Konkurrenz-Abgrenzung mit Belegen unterfüttern
- Floskel-Diät

### ✅ Sprint #4 Teil 1 — Methodik substanziell geschärft + Autoren-Block auf 13 YMYL-Seiten (B.2/B.3 teilweise)

**Methodik-Seite:**
- Lead neu: rechtfertigt die Seite statt Floskel ("Transparenz ist uns wichtig" raus)
- **Quellenhierarchie** als Fließtext (Primär/Sekundär/Erfahrungswerte) mit Inline-Verlinkungen zu Destatis, Stiftung Warentest, Aeternitas, BDB, Verbraucherzentrale
- **Rechtliche Quellen konkret verlinkt:** gesetze-im-internet.de (BGB § 1922, PStG), Bayerisches BestG, NRW BestG
- **Update-Rhythmen als Tabelle** (Sofort/Halbjährlich/Jährlich) mit konkreten Monaten
- **Interessenkonflikts-Regeln** als 4-Punkte-Liste (gelten unabhängig vom Modell-Status)
- **FAQ-Sektion** mit 5 Fragen + ehrlichen Antworten ("Warum nennt ihr keine Reviewer-Namen? — Weil wir noch keine haben.")
- **Änderungslog** sichtbar am Seitenende (zwei Einträge: Erstveröffentlichung + heutige Schärfung)
- Schema erweitert: **FAQPage-Entity** mit allen Q&A strukturiert
- Audit-Score 80→79 (Title/H1-Metrik marginal, substanziell deutlich reicher), 1005→1415 Wörter
- HTML-Altlast gefixt: `</div>` → `</main>` (beide Strukturfehler weg)
- `mr-principle`-Boxen von 10 → 4 reduziert (visueller Overload runter)

**Autoren-Block sitewide (13 Seiten):**

Ziel: E-E-A-T-Block direkt unter der H1 auf allen wichtigen YMYL-Seiten. Format:
> **Redaktion machsruhig.de** · Stand: [Datum]
> [Wie entstehen unsere Inhalte?](/methodik) · Lesezeit: ca. X Minuten

Betroffene Seiten (13):
- 8 Content-Root: beerdigung-planen, bestattungsarten, bestattungskosten, kindern-tod-erklaeren, kondolenzschreiben, trauerrede-schreiben, trauersprueche, vertraege-kuendigen
- 5 Gold-Städte: Berlin, Frankfurt, Hamburg, Köln, München

Einbau in zwei Schritten:
1. `_dev/apply-author-block.py` — ersetzt existierendes `<p class="meta">` durch neuen Block (Dry-Run + Apply, variante-aware)
2. `_dev/apply-author-block-cleanup.py` — entfernt Inline-Styles, fügt zentrale `.mr-article-meta`-CSS-Regel in jeden `<style>`-Block ein

Zusätzlich:
- `.mr-article-meta` auch in `css/machsruhig.css` für Seiten, die diese Datei laden
- **Gold-Städte Schema** erweitert: `Organization`-Knoten + `provider`-Referenz im Service-Block
- **HTML-Altlast:** trauerrede-schreiben.html `</div>` → `</main>` mitgefixt (0 Strukturfehler auf allen 13 Seiten)
- **Stand-Datum:** Nur Berlin trägt "Stand: 23. April 2026" (heute tatsächlich redaktionell angefasst). Alle anderen behalten "April 2026" — ehrlich, kein Pseudo-Review.

Reviewer-Zeile heute bewusst **nicht** eingebaut: Fachpool leer, Platzhalter wäre Selbstschwächung sichtbar auf jeder YMYL-Seite.

## Gesamt-Site-Score-Entwicklung (23.04.2026)

- Session-Start: 59.0
- Nach Sprint #1 (Homepage 80): 59.5
- Nach Sprint #2 (5 Gold-Städte 75): 61.2
- Nach Sprint #3 (Über-uns 75): 61.37
- Nach Sprint #4 Teil 1 (Methodik 79 + 13× Autor-Block): **61.36**

(Die Autoren-Block-Einführung hat keinen Score-Effekt im aktuellen Audit-Skript, weil das Skript noch keinen E-E-A-T-Check hat — die E-E-A-T-Verbesserung ist strukturell real, aber unsichtbar im Score)

## Stufe-1-Quality-Gate: ✅ PASSED (zum ersten Mal heute)

- Alle HTML-Dateien strukturell valide (Altlast trauerrede weg)
- Keine Platzhalter
- Homepage-Score 80 ≥ 75
- OG-Images valide
- Warnungen: 17 kaputte Links (Phase D), Sitemap stale 45 noindex-Städte (Phase D), 3 Deploy-Blocker (Phase A.3 Tool-Shells)

## 🔄 Sprint #4 Teil 2 — offen

Das eigentliche Sprint #4-Ticket sieht 48 YMYL-Seiten vor. Heute sind 13 gemacht (SEO-Impact-Top). Offen:
- **B.2.1:** Autoren-Block auf die restlichen 35 Seiten — 10 Tools, 9 Vorsorge, 16 Bundesländer. Skripte existieren, nur Target-Liste erweitern + Apply. Aufwand ~1.5h.
- **B.2.2:** Reviewer-Zeile aktivieren sobald Fachpool einen ersten Namen hat.

## 🔄 Sprint #5 — noch ausstehend

Sprint #5 — Akutfall-Hauptseite "Erste 24 Stunden" (C.1.1), 6-8h. Geplant für nächste Session oder die danach.

## Offene Punkte für später

- **B.2.1** und **B.2.2** (siehe oben)
- **LocalBusiness/FuneralHome-Schema** für 5 Gold-Städte (Ticket D.2.1)
- **Sitemap.xml stale:** 45 noindex-Städte drin (Phase D)
- **17 kaputte interne Links** (`/bestattung` 16×, `/tools/brief-an-meine-liebsten` 1×)
- **B.1.1** Über-uns-Nachschärfung wenn Traffic kommt
- **Dev-Skripte in `_dev/`:** `apply-author-block.py` + `apply-author-block-cleanup.py` sind committed. Bei zukünftiger Erweiterung auf 35 Seiten: Target-Liste in beiden Skripten parallel halten, oder in `_dev/skills/` dokumentieren.

## PAT-Status

**⚠️ GitHub PAT läuft am 25.04.2026 ab** — in 2 Tagen. Rotation planen, sonst scheitert der nächste Push.

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
+ 23.04.2026 Abend (Mitte): **Sprint #3 Über-uns (B.1, Score 75)** + Backlog-Umklassifizierung Sprint #2 → D.2.1 + sitewide machsleicht-Entkopplung + Deploy
+ 23.04.2026 Abend (spät): **Sprint #4 Teil 1: Methodik geschärft (B.3, Score 79, 1415 Wörter) + Autoren-Block auf 13 YMYL-Seiten (B.2) + trauerrede-Altlast weg + Stufe-1-Quality-Gate erstmals PASSED**
