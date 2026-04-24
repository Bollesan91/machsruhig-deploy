# Session-Notizen

## Letzte Session
**Datum:** 24. April 2026 (Niedersachsen-Sprint, mit Deploy)
**Deploy-Status:** Mit „ende deploy" gepusht und deployed.

## Was wurde gemacht

### ✅ Niedersachsen — 9. von 16 Bundesländer-Seiten auf Elite-Niveau

| Metrik | Vorher | Nachher |
|---|---|---|
| Audit-Score | 80/100 | **85/100** |
| Wortzahl | 352 | **1.967** |
| §-Refs | 0 | **9** |
| Externe Quellen | 0 | **18** |
| Re-Check Blocker | 3 | **0** |
| Re-Check Warnungen | 4 | **0** |

### 🚨 DER inhaltliche Kerngewinn

Die alte Seite hatte **drei fundamentale Fehler**:
1. **Geografie-Fehler:** „Bremen" als Region in Niedersachsen erwähnt — Bremen ist eigenes Bundesland (Stadtstaat)
2. „Sargpflicht: Nein" → korrekt: **§ 11 Abs. 1 BestattG** Sargpflicht (Ausnahme über untere Gesundheitsbehörde nach § 11 S. 2)
3. „Mindestfrist 24h" → korrekt: **48 Stunden** nach § 9 Abs. 1

### Niedersachsen-Spezifika belegt
- **BestattG vom 8.12.2005** (Nds. GVBl. S. 381), zuletzt geändert 23.02.2022 (in Kraft 02.03.2022)
- **§ 9 Abs. 1**: 48h Mindestfrist
- **§ 9 Abs. 2**: 8 Tage Höchstfrist (Soll-Vorschrift, gemeindefreie Tage zählen nicht mit)
- **§ 9 Abs. 2 S. 4**: Urne 1 Monat
- **§ 11 Abs. 1**: Sargpflicht-Volltext + Ausnahmemöglichkeit
- **§ 14**: Mindestruhezeit 20 Jahre (für alle Bestattungen, untere Gesundheitsbehörde kann ändern)
- **§ 13a Abs. 2**: Naturstein-Klausel (keine Kinderarbeit, ILO-182-Bezug) — eine soziapolitische Besonderheit
- **Stadtfriedhof Engesohde**: 1864 als erster kommunaler Großfriedhof, 21,7 ha, Eingangsbau Droste 1873, Kapelle Barnstorf 1910 (Wikipedia)
- **Stadtfriedhof Stöcken**: 1891 eröffnet, 55 ha, ~170.000 Bestattungen seit 1891, Bauabschnitt Rowald + Narten 1889–1892
- **Stadtfriedhof Seelhorst**: 1920 eröffnet, **63 ha (Stadt Hannover) bzw. 68,5 ha (Wikipedia)** — Quellenkonflikt explizit erwähnt
- **Seelwald**: erster städtischer Bestattungswald in Hannover, 2005
- **Friedhofsmuseum**: seit 2006 im alten Krematorium, 300 m²
- **5 große + 14 kleinere städtische Friedhöfe** in Hannover (hannover.gov.de offiziell)
- **FriedWald**: 15 Standorte in Niedersachsen (friedwald.de offiziell)
- **Träger**: Fachbereich Umwelt und Stadtgrün der Landeshauptstadt Hannover

### Korrekturen aus Stufe-1-Gate vor Deploy
1. **„Beverstedt" als FriedWald-Standort entfernt** — nicht durch Primärquelle belegt. Korrekt: 15 FriedWald-Standorte mit Bramsche (erster), Hasbruch, Lüneburger Heide etc. — verifiziert über friedwald.de offiziell.
2. **Quellenkonflikt Seelhorst-Fläche explizit erwähnt** — Stadt Hannover sagt 63 ha, Wikipedia 68,5 ha; ich erkläre die Differenz mit späteren Erweiterungen.
3. **Title gekürzt** auf 59 Zeichen (vorher 68).

## Status: 9/16 Bundesländer auf Elite-Niveau

**Fertig:** BW, MV, LSA, TH, BB, SN, BY, HB, **NI**

| Nächste | Audit | Re-Check Blocker |
|---|---|---|
| Hamburg | 71 | 2 |
| Schleswig-Holstein | 79 | 2 |
| Berlin | 81 | 2 |
| Rheinland-Pfalz | 80 | 2 |
| NRW | 78 | 1 |
| Hessen | 80 | 1 |
| Saarland | 71 | 1 |

**Empfehlung nächste Session:** **Hamburg** (Stadtstaat, Score am niedrigsten 71, Ohlsdorf als größter Friedhof Deutschlands wäre eine starke Story) oder **Berlin** (Score schon 81, geht schneller).

## Workflow-Lehren dieser Session

1. **Erinnerungen sind keine Quellen — Wiederholungslektion.** „Beverstedt" hatte ich auswendig im Kopf — friedwald.de hat es nicht; Bramsche, Hasbruch sind die wirklichen Pionier-Standorte. Konkrete Standorte IMMER live recherchieren, NIE aus dem Kopf zitieren.
2. **Quellenkonflikte transparent machen.** Bei Seelhorst-Fläche habe ich die Stadt-Hannover-PDF und Wikipedia direkt nebeneinander zitiert — das ist ehrlicher und User-freundlicher als willkürliche Auswahl.
3. **Title-Länge ist ein einfacher Score-Hebel.** Mit „Recht & Friedhöfe" statt „Recht, Fristen & Friedhöfe" auf <60 Zeichen kommen.

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
