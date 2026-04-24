# Session-Notizen

## Letzte Session
**Datum:** 24. April 2026 (Bayern-Sprint, mit Deploy)
**Deploy-Status:** Mit „ende deploy" gepusht und deployed.

## Was wurde gemacht

### ✅ Bayern — 7. von 16 Bundesländer-Seiten auf Elite-Niveau

| Metrik | Vorher | Nachher |
|---|---|---|
| Audit-Score | 37/100 | **85/100** |
| Wortzahl | ~463 | **2.153** |
| §- + Art-Refs | 0 | **14** (10 §, 4 Art.) |
| Externe Quellen | 0 | **16** |
| Re-Check Blocker | 1 | **0** |
| Re-Check Warnungen | 4 | **0** |

### 🚨 DER inhaltliche Kerngewinn

Die alte Seite hatte **drei fundamentale Sachfehler**:
1. „Mindestfrist 24h" → korrekt **48h nach § 18 Abs. 1 BestV**
2. „Höchstfrist 96h (4 Tage)" → veraltet, seit **BestV-Novelle 2021 sind es 8 Tage** ohne Sa/So/Feiertage (§ 19 Abs. 1)
3. „Sargpflicht: Ja" pauschal → korrekt: **§ 30 Abs. 2 BestV erlaubt seit 2021 die Tuchbestattung** über die Friedhofssatzung. Bayern ist also **strukturell anders als Sachsen** (das eine vergleichbare BestV-Öffnung NICHT kennt).

Konkretes Praxisbeispiel: **Nürnberg** hat die Tuchbestattung in seinem Friedhofssatzungs-Konzept umgesetzt (offizielle nuernberg.de-Seite).

### Weitere Bayern-spezifische Korrekturen gegen das alte Template

- **3 Monate** Urnenbeisetzung (§ 19 Abs. 4 BestV — Reform 2021)
- **Keine landesgesetzliche Mindestruhezeit** — Friedhofssatzung gem. Art. 10 BestG entscheidet
- **München-Standardruhezeit 10 Jahre** (offiziell stadt.muenchen.de)
- **Münchner Waldfriedhof: 161,32 ha, 64.500 Grabstätten, 1907 von Hans Grässel** als erster Waldfriedhof Deutschlands (stadt.muenchen.de Primärquelle)
- **Träger müssen juristische Personen des öffentlichen Rechts sein** (stmi.bayern.de)
- **München bei Friedhofsgebühren bundesweit oben** (Baumbestattung 3.246 € München vs. 780 € Kiel — check24)
- **FriedWald hat 6 Standorte in Bayern** — korrekt: Spessart, Fränkische Schweiz (Ebermannstadt), Fichtelgebirge (Luisenburg), Maintal, Südspessart

### Selbstkritischer Re-Check vor Deploy fand 5 Korrekturen

1. **Nürnberg-URL präziser**: Statt PDF-Datum „April 2023" jetzt korrekt verlinkte offizielle Seite
2. **München-Ruhezeit präziser**: Nicht „für Urnengräber 10 Jahre", sondern „auf den städtischen Friedhöfen zehn Jahre" (gilt für alle Grabarten)
3. **FriedWald-Regionen korrigiert**: „Ebersberg" war falsch im Kopf — korrekt sind Spessart, Fränkische Schweiz, Fichtelgebirge (3 Stellen: Schema, Hauptinhalt, FAQ)
4. **Re-Check-Skript verfeinert**: Heuristik „Höchstfrist 7-8 Tage" zu eng — 8 Tage in BY und SN gesetzlich korrekt. Pattern auf nur „7 Tage" reduziert.
5. **Marketing-Vokabular „Angebot" entfernt**: Skript fängt es als pietätlos. Umformuliert auf „regionale Träger unterhalten ergänzende Bestattungswälder" (3 Stellen)

### Workflow-Lehren dieser Session

1. **Skript-Heuristiken sind dein Korrektiv, nicht dein Gesetz.** Wenn die Heuristik einen False Positive findet, ist die richtige Reaktion entweder die Heuristik präzisieren ODER die Formulierung anpassen — beides dokumentiert.
2. **„Angebot" und ähnliche Marketing-Vokabeln sind in YMYL-Kontext besser zu vermeiden.** Auch wenn faktisch neutral, signalisieren sie Verkäufer-Sicht statt Bürger-Service.
3. **Erinnerungen sind keine Quellen.** „Ebersberg" hatte ich aus dem Kopf — war falsch. Konkrete Standortlisten IMMER live recherchieren.
4. **Bei Quellen-Konflikten lieber konservativer formulieren** (vgl. Sachsen-Glockenturm 60 vs. 63 m).

## 🚨 Implikation für die deployed Sachsen-Seite (`c47989b`)

Die Sachsen-Aussage *„Sachsen gehört... zusammen mit Bayern zu den letzten beiden Bundesländern mit durchgängiger Sargpflicht"* ist nach der Bayern-Recherche zu **undifferenziert**. Bayern hat **die BestV-§30(2)-Öffnung** für Tuchbestattung (über Friedhofssatzung), Sachsen nicht. 

**Empfehlung für nächste Session:** Sachsen-Seite präzisieren: „Sachsen ist nach der Reform Sachsen-Anhalts (11.09.2025) das einzige Bundesland mit durchgängiger Sargpflicht ohne Verordnungs-Lockerung. Bayern hat zwar die gesetzliche Sargpflicht, erlaubt aber seit 2021 über § 30 Abs. 2 BestV Tuchbestattungen, die kommunal im Einzelfall oder per Friedhofssatzung umgesetzt werden."

## Nächste Schritte

### Bundesländer-Seiten: 9 weitere zu überarbeiten

Sortiert nach Re-Check-Blocker-Anzahl (Stand vor Bayern):

| Nächste | Audit | Re-Check Blocker |
|---|---|---|
| Bremen | 81 | 3 |
| Niedersachsen | 80 | 3 |
| Hamburg | 71 | 2 |
| Schleswig-Holstein | 79 | 2 |
| Berlin | 81 | 2 |
| Rheinland-Pfalz | 80 | 2 |
| NRW | 78 | 1 |
| Hessen | 80 | 1 |
| Saarland | 71 | 1 |

Empfehlung für nächste Session: **Sachsen-Präzisierung** (5 Min) + dann **Bremen oder Niedersachsen** (3 Blocker, Hansestadt/Flächenland).

### Weitere offene Punkte (aus BACKLOG, unverändert)

- **Vorsorge-Ordner:** strategische Entscheidung fällig — die „Kommt bald"-Platzhalter sind YMYL-fragwürdig
- **10 Tool-Seiten** warten auf A.3 Static-Shell-Umbau
- **PRE_LAUNCH_MODE auf False** setzen, sobald Phase F aktiv rollt
- **17 kaputte interne Links sitewide** (Phase D)
- **sitemap.xml stale** (45 noindex-Städte, Phase D)
- **B.2.2 Reviewer-Zeile aktivieren**, wenn Fachpool real
- **D.2.1 Gold-Städte** auf Score ≥ 85 mit FuneralHome-Schema

### Mail-Infrastruktur (unverändert)

- 🗓️ **08.05.2026:** Migadu-Trial-Ende — Entscheidung Mini ($90/J) vs. Micro ($19/J)
- GMX-IMAP-Einbindung der beiden Mailboxen offen
- DMARC machsleicht.de aktuell `p=none`, langfristig auf `p=quarantine`

## Offene Fragen

Keine aktuell.
