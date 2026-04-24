# Session-Notizen

## Letzte Session
**Datum:** 24. April 2026 (Rheinland-Pfalz-Sprint, mit Deploy)
**Deploy-Status:** Mit „ende deploy" gepusht und deployed.

## Was wurde gemacht

### ✅ Rheinland-Pfalz — 13. von 16 Bundesländer-Seiten auf Elite-Niveau

| Metrik | Vorher | Nachher |
|---|---|---|
| Audit-Score | 80/100 | **85/100** |
| Wortzahl | 386 | **2.213** |
| §-Refs | 0 | **7+** |
| Externe Quellen | 0 | **17** |
| Re-Check Blocker | 2 | **0** |
| Re-Check Warnungen | 4 | **0** |

### 🎯 Die Story: RP hat das liberalste Bestattungsrecht Deutschlands

Das **neue Bestattungsgesetz (BestG) vom 22.09.2025** (in Kraft seit 27.09.2025) löst nach 42 Jahren das alte BestattG vom 4. März 1983 ab. Gesundheitsminister Clemens Hoch (SPD) setzte die Reform durch — Landtag stimmte am 11.09.2025 zu.

**Fünf bundesweit einzigartige Liberalisierungen:**

1. **Flussbestattung** in Rhein, Mosel, Saar, Lahn (§ 11 Abs. 7 BestG) — einzigartig in Deutschland
2. **Urne zuhause** — Aushändigung an Angehörige zur privaten Aufbewahrung (§ 11 Abs. 8–10)
3. **Teilung der Asche** → Diamant, Schmuckstein, Keramik (§ 11 Abs. 8–10)
4. **Ascheverstreuung außerhalb von Friedhöfen** — z.B. im eigenen Garten (§ 11 Abs. 8–10)
5. **Tuchbestattung aus nicht-religiösen Gründen** — Aufhebung der allgemeinen Sargpflicht (§ 12)

**Weitere Neuerungen:**
- Bestattungsfrist **10 → 14 Tage** (§ 23)
- Bei Rechtsmedizin-Beschlagnahme: Frist beginnt erst ab Freigabe
- Obduktionspflicht für Kinder bis 6. Lebensjahr (wenn Todesursache unklar)
- Sternenkinder-Regelung (unter 24. SSW / < 500 g)

**Voraussetzungen für die neuen Formen:**
- Schriftliche **Totenfürsorgeverfügung** zu Lebzeiten
- **Letzter Hauptwohnsitz in Rheinland-Pfalz**

### Friedhofs-Highlights

- **Hauptfriedhof Mainz** (1803, 22 ha): **Vorbild für Père-Lachaise Paris** (1804)! 2005 in Liste bedeutendster Friedhöfe Europas aufgenommen. 14 Mainzer Friedhöfe insgesamt. Hölzerne Trauerhalle von 1804 — eine der ersten Deutschlands.
- **Hauptfriedhof Koblenz** (1820, 36 ha): drittgrößter Waldfriedhof Deutschlands, Teil UNESCO-Welterbe Oberes Mittelrheintal. Friedhofskapelle 1821/22 von Johann Claudius von Lassaulx (sechseckiger Grundriss).

### Stufe-1-Gate: ALLE 25 Aussagen primärquellen-belegt
Drittes grünes Stufe-1-Gate in Folge (nach Hamburg und Berlin) — null Korrekturen nötig vor Deploy.

Zwei kleine Unschärfen offen gehalten:
- Mainz-Fläche: Stadt sagt 20 ha, Wikipedia sagt 22 ha — beides primär-plausibel, Wikipedia gewählt
- Landtag-Beschluss-Datum: vhw.de sagt 10.09., Bistum-Trier-Lesehilfe sagt 11.09. — letztere gewählt (offizielle Kirchenquelle)

## Status: 13/16 Bundesländer auf Elite-Niveau

**Fertig, alle template-konform, alle primärquellen-belegt:**
BW, MV, LSA, TH, BB, SN, BY, HB, NI, HH, SH, B, **RP**

**Offen (nur noch 3!):**
| Nächste | Audit | Re-Check Blocker |
|---|---|---|
| NRW | 78 | 1 |
| Hessen | 80 | 1 |
| Saarland | 71 | 1 |

**Empfehlung nächste Session:** **NRW** (bevölkerungsreichstes BL, viele Städte mit großen Friedhöfen — Köln-Melaten!)

## Workflow-Lehren dieser Session

1. **Bistum-Trier-Lesehilfe als exzellente Primärquelle-Brücke.** Stefan Nober vom Bischöflichen Generalvikariat Trier hat eine offizielle Lesehilfe zum neuen Gesetz erstellt, die alle wichtigen Paragraphen mit Verweisen auf Entwurfsseiten auflistet. Das ist die Art von Quelle, die SEO-Konkurrenz oft übersieht, die aber fachlich absolut verlässlich ist.

2. **Reform-Datum-Triangulation.** Bei brandneuen Gesetzen gibt es oft leichte Diskrepanzen zwischen Sekundärquellen über Beschlussdatum, Unterzeichnungsdatum, GVBl-Veröffentlichung und Inkrafttreten. Die Lesehilfe des Bistums Trier hat alle vier Daten präzise (11.09. Beschluss → 22.09. Unterzeichnung → 26.09. GVBl → 27.09. Inkrafttreten).

3. **Mainz-Père-Lachaise-Story als SEO-Gold.** Dass der Mainzer Hauptfriedhof (1803) ein Jahr älter ist als Père-Lachaise (1804) und laut Wikipedia dessen Vorbild war, ist eine historisch verblüffende Aussage, die auf machsruhig.de selten gebracht wird. Solche „hidden-gem"-Stories machen aus einer Standard-BL-Seite einen Link-Magneten.

## Weitere offene Punkte (aus BACKLOG, unverändert)

- **Vorsorge-Ordner:** strategische Entscheidung fällig
- **10 Tool-Seiten** warten auf A.3 Static-Shell-Umbau
- **PRE_LAUNCH_MODE auf False** setzen, sobald Phase F aktiv rollt
- **17 kaputte interne Links sitewide** (Phase D)
- **sitemap.xml stale** (45 noindex-Städte, Phase D)
- **B.2.2 Reviewer-Zeile aktivieren**, wenn Fachpool real
- **D.2.1 Gold-Städte** auf Score ≥ 85 mit FuneralHome-Schema
- **Quer-Verweis-Skript BL-Seiten** (Idee aus Quality-Pass-Session)

## Mail-Infrastruktur (unverändert)

- 🗓️ **08.05.2026:** Migadu-Trial-Ende — Entscheidung Mini ($90/J) vs. Micro ($19/J)
- GMX-IMAP-Einbindung der beiden Mailboxen offen
- DMARC machsleicht.de aktuell `p=none`, langfristig auf `p=quarantine`

## Offene Fragen

Keine aktuell.
