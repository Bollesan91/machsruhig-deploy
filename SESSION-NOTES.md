# Session-Notizen

## Letzte Session
**Datum:** 24. April 2026 (Sachsen-Präzisierung + Bremen-Sprint, mit Deploy)
**Deploy-Status:** Mit „ende deploy" gepusht und deployed.

## Was wurde gemacht

### ✅ Sachsen-Präzisierung (5 Min, Folge der Bayern-Recherche)

Die Sachsen-Aussage *„Sachsen + Bayern letzte Sarg-Länder"* war nach der Bayern-Recherche zu undifferenziert. Bayern hat **§ 30 Abs. 2 BestV** als Verordnungs-Öffnung für Tuchbestattung über die Friedhofssatzung — Sachsen kennt keine vergleichbare Ermächtigung.

**3 Stellen aktualisiert** (Sachsen-Seite, Score bleibt 85):
- H2-Sektionsüberschrift: „Sargpflicht in Sachsen: Das einzige Bundesland ohne Verordnungs-Lockerung"
- Hauptinhalts-Absatz: präzisiert mit Verweis auf Bayern-Sondersituation
- FAQ-Box + JSON-LD-Schema: präziser Vergleich Sachsen vs. Bayern

### ✅ Bremen — 8. von 16 Bundesländer-Seiten auf Elite-Niveau

| Metrik | Vorher | Nachher |
|---|---|---|
| Audit-Score | 81/100 | **85/100** |
| Wortzahl | 400 | **2.121** |
| §-Refs | 0 | **15+** |
| Externe Quellen | 0 | **18** |
| Re-Check Blocker | 3 | **0** |
| Re-Check Warnungen | 4 | **0** |

### 🚨 DER inhaltliche Kerngewinn

Die alte Seite hatte **drei fundamentale Fehler**:
1. **Geografie-Fehler:** „Oldenburg" wurde als zu Bremen zugehörig erwähnt — Oldenburg liegt aber in Niedersachsen!
2. „Sargpflicht: Nein" → korrekt: **§ 4 Abs. 2 BestG Bremen** schreibt geschlossenen Sarg vor (Ausnahme nur § 4 Abs. 4 religiös)
3. „Mindestfrist 24h" → korrekt: **48 Stunden** nach § 16 LeichenG

**Bremens Kernknüller jetzt im Mittelpunkt:** Bremen ist nach **§ 4 Abs. 1a** des Bremer Bestattungsgesetzes seit 1.1.2015 **das einzige Bundesland**, in dem die Asche eines Verstorbenen außerhalb von Friedhöfen ausgebracht werden darf — z.B. im eigenen Garten. Strenge Voraussetzungen (Hauptwohnsitz, schriftliche Verfügung, Totenfürsorge, Eigentümerzustimmung, eidesstattliche Versicherung) verhindern „Aschetourismus".

### Bremen-Spezifika belegt
- **GBestattF v. 16.10.1990** (Brem.GBl. S. 303), Reform 2014/In-Kraft 1.1.2015
- **Mindestruhefrist Aschen 20 J., Leichen 25 J.** (§ 5 Abs. 1, transparenz.bremen.de wörtlich)
- **§ 4 Abs. 4**: Sargpflicht-Ausnahme religiös, in Bremen mit Zustimmung Institut für Rechtsmedizin Klinikum Bremen-Mitte
- **Friedhof Osterholz**: 76 ha, 1920, größter Friedhof Bremens (Umweltbetrieb Bremen)
- **Riensberger Friedhof**: 27 ha, 1875, einer der frühesten Parkfriedhöfe Deutschlands (denkmalpflege.bremen.de), Kolumbarium im 1988 stillgelegten Krematorium, 2002 umgebaut
- **Träger**: Umweltbetrieb Bremen (UBB), Eigenbetrieb der Stadtgemeinde Bremen
- **Aschestreuwiesen**: Friedhof Osterholz und Friedhof Blumenthal (UBB-eigene Quelle)

### 3 Korrekturen aus Stufe-1-Gate vor Deploy
1. **§ 5a-Spezifizierung entschärft** — Umweltbestimmung erwähnt, aber ohne konkrete §-Nummer (war nicht 100% durch Primärquelle belegt)
2. **„12 städtische Friedhöfe Bremens"** entfernt (nur durch Sekundärquelle belegt) → defensive Formulierung
3. **„Einäscherungen außerhalb der Stadt"** präzisiert zu „über andere Krematorien in der Region"

### Bonus-Korrektur am Re-Check-Skript
Hamburg-/Berlin-Erwähnung im Vergleichskontext triggerte den „BL-Geografie-Check" als False Positive. Wording umformuliert auf „in der Tradition großer norddeutscher Hauptfriedhöfe" — Skript bleibt streng, Inhalt bleibt sachlich richtig.

## Status: 8/16 Bundesländer auf Elite-Niveau

**Fertig:** BW, MV, LSA, TH, BB, **SN**, **BY**, **HB**

| Nächste | Audit | Re-Check Blocker |
|---|---|---|
| Niedersachsen | 80 | 3 |
| Hamburg | 71 | 2 |
| Schleswig-Holstein | 79 | 2 |
| Berlin | 81 | 2 |
| Rheinland-Pfalz | 80 | 2 |
| NRW | 78 | 1 |
| Hessen | 80 | 1 |
| Saarland | 71 | 1 |

**Empfehlung nächste Session:** **Niedersachsen** (3 Blocker, größtes Flächenland Norddeutschlands, mit Hauptstadt Hannover und vielen Mittelstädten)

## Workflow-Lehren dieser Session

1. **Geografie-Heuristik des Skripts ist scharf — und manchmal zu scharf.** Eine kontextuell saubere Erwähnung anderer Städte (Hamburg/Berlin als Vergleich) wird als Fehler markiert. Lösung: Wording umformulieren, nicht das Skript schwächen.
2. **Bremen war ein gutes Pilot-Beispiel für „die-3-Blocker-und-trotzdem-fast-leerer-Inhalt-Vorlage".** 400 Wörter waren Kernproblem; die Asche-Verstreuung-Story als Hauptinhalt zu identifizieren, brauchte kurze Recherche, dann lief der Rest.
3. **§-Belege defensiv:** Wenn Aeternitas/Sekundärquelle die Absatz-Nummer abschneidet, lieber „§ 16 LeichenG" ohne Absatz schreiben statt eine Nummer zu raten.

## Weitere offene Punkte (aus BACKLOG, unverändert)

- **Vorsorge-Ordner:** strategische Entscheidung fällig — die „Kommt bald"-Platzhalter sind YMYL-fragwürdig
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
