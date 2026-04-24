# Session-Notizen

## Letzte Session
**Datum:** 24. April 2026 (Hamburg-Sprint, mit Deploy)
**Deploy-Status:** Mit „ende deploy" gepusht und deployed.

## Was wurde gemacht

### ✅ Hamburg — 10. von 16 Bundesländer-Seiten auf Elite-Niveau

| Metrik | Vorher | Nachher |
|---|---|---|
| Audit-Score | 71/100 | **85/100** |
| Wortzahl | 346 | **2.067** |
| §-Refs | 0 | **6+** |
| Externe Quellen | 0 | **18** |
| Re-Check Blocker | 2 | **0** |
| Re-Check Warnungen | 4 | **0** |

### 🚨 DER inhaltliche Kerngewinn

Die alte Seite hatte **zwei fundamentale Fehler**:
1. „Sargpflicht: Nein" → korrekt: **Sargpflicht ja**, Ausnahmen für muslimische Bestattungen möglich
2. „Mindestfrist 24h" → **Hamburg hat überhaupt keine starre 48h-Mindestfrist** (Sondersituation!)

**Hamburgs Doppel-Story:**
1. **Mensch-Tier-Bestattung** (seit 1.3.2020 in Kraft) — Hamburg ist das **erste Bundesland** Deutschlands mit dieser gesetzlichen Regelung. Erstes Grabfeld auf Ohlsdorf, bis zu 1 Hektar. Tier muss in Tierkrematorium eingeäschert werden.
2. **Friedhof Ohlsdorf** — der **größte Parkfriedhof der Welt** (389 ha), Deutschlands größter Friedhof, weltweit Platz 4 nach dem Wadi as-Salam in Nadschaf/Irak (917 ha).

### Hamburg-Spezifika belegt
- **BestattG vom 30.10.2019** (HmbGVBl. Nr. 42, S. 379), Stand 1.2.2024 — komplette Modernisierung des Vorgängergesetzes von 1988
- **§ 10 Abs. 1**: 10-Tages-Anzeigepflicht statt starrer Höchstfrist
- **§ 6**: Überführung in Leichenhalle innerhalb 36h
- **KEINE explizite 48h-Mindestfrist** im Hamburger BestattG (anders als in den meisten BL!)
- **Hamburger Friedhöfe – Anstalt öffentlichen Rechts** (HFG vom 8.11.1995): betreibt Ohlsdorf, Öjendorf, Volksdorf, Wohldorf + Finkenwerder (alt+neu), Finkenriek, Kirchdorf-Amtshof
- **Hamburger Krematorium GmbH** (100%-Tochter): Krematorien Ohlsdorf + Öjendorf
- **Ohlsdorf**: 1.7.1877 eröffnet, 389 ha (größte Ausdehnung 1930: 400 ha), 235.000 Grabstellen, 1,4 Mio Beisetzungen seit Gründung, 4.500/Jahr; Architekt Wilhelm Cordes; 1900 Grand Prix Pariser Weltausstellung; 2015 Nutzfläche reduziert auf 200 ha; 36.000 Bäume, 450 Gehölzarten, 800 Skulpturen, 15 Teiche
- **Öjendorf**: 14.07.1966 eröffnet, 98,7 ha, zweitgrößter Hamburger Parkfriedhof, seit 1978 separate islamische Grabanlagen
- **Volksdorf**: 1959-2012 vom Bezirksamt Wandsbek verwaltet, ab 2013 unter Hamburger Friedhöfe AöR
- **Lutz Rehkopf** ist Sprecher der Hamburger Friedhöfe (mehrfach in Quellen belegt)

### 2 Korrekturen + 1 technischer Fix
1. **Marketing-Vokabel „Angebot" entfernt** — Re-Check-Heuristik fängt das in YMYL-Kontext zurecht. „Spektrum" als pietätsneutrale Alternative.
2. **JSON-LD Anführungszeichen-Konflikt:** `„Hamburger Friedhöfe"` im Schema-Text brach das JSON, weil das `"` als String-Ende interpretiert wurde. Defensiv: deutsche Anführungszeichen entfernt im JSON-LD (im sichtbaren HTML-Text bleiben sie). Schema-Test: PARSE_ERROR → grün.
3. **Title gekürzt** auf 52 Zeichen.

## Status: 10/16 Bundesländer auf Elite-Niveau

**Fertig:** BW, MV, LSA, TH, BB, SN, BY, HB, NI, **HH**

| Nächste | Audit | Re-Check Blocker |
|---|---|---|
| Schleswig-Holstein | 79 | 2 |
| Berlin | 81 | 2 |
| Rheinland-Pfalz | 80 | 2 |
| NRW | 78 | 1 |
| Hessen | 80 | 1 |
| Saarland | 71 | 1 |

**Empfehlung nächste Session:** **Schleswig-Holstein** (geografisch direkter Nachbar Hamburgs, Synergien bei Recherche; oder Berlin, ist Score-mäßig nahe an 85)

## Workflow-Lehren dieser Session

1. **Deutsche Anführungszeichen im JSON-LD-Schema sind ein Fallstrick.** Wenn das geschlossene `"` (ASCII) in einem JSON-Strinng-Wert steht, bricht das JSON. Entweder als HTML-Entity codieren ODER deutsche Sonderzeichen ganz weglassen im Schema (im sichtbaren HTML-Text bleiben sie). Sollte ich automatisch im Skript prüfen können.
2. **„Angebot" / „bietet" / „leistet" sind pietätsensibel** in YMYL-Bestattungs-Kontext. Re-Check fängt das automatisch — gut. Mein Wording-Fix: „Spektrum", „umfasst", „verfügbar".
3. **Hamburg hat KEINE 48h-Mindestfrist im Gesetz** — das ist eine echte Sondersituation, die ich selbst nicht erwartet hatte. Sekundärquellen widersprechen sich (anwalt-Plattform sagt richtig „keine starre Frist", Bestattungs-Aggregator sagt fälschlich „48h für alle 16"). **Lokale Bestattungs-Quelle ist immer näher dran** als überregionale Aggregator-Seiten.
4. **Stufe-1-Gate war diesmal komplett grün ohne Korrekturen.** Saubere Recherche zahlt sich aus — alle 26 Behauptungen wörtlich primärquellen-belegt.

## Weitere offene Punkte (aus BACKLOG, unverändert)

- **Vorsorge-Ordner:** strategische Entscheidung fällig
- **10 Tool-Seiten** warten auf A.3 Static-Shell-Umbau
- **PRE_LAUNCH_MODE auf False** setzen, sobald Phase F aktiv rollt
- **17 kaputte interne Links sitewide** (Phase D)
- **sitemap.xml stale** (45 noindex-Städte, Phase D)
- **B.2.2 Reviewer-Zeile aktivieren**, wenn Fachpool real
- **D.2.1 Gold-Städte** auf Score ≥ 85 mit FuneralHome-Schema

## Mail-Infrastruktur (unverändert)

- 🗓️ **08.05.2026:** Migadu-Trial-Ende — Entscheidung Mini ($90/J) vs. Micro ($19/J)
- GMX-IMAP-Einbindung der beiden Mailboxen offen
- DMARC machsleicht.de aktuell `p=none`, langfristig auf `p=quarantine`

## Offene Fragen

Keine aktuell.
