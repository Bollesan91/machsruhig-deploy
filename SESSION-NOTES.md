# Session-Notizen

## Letzte Session
**Datum:** 24. April 2026 (Sachsen-Sprint, mit Deploy)
**Deploy-Status:** Mit „ende deploy" gepusht und deployed.

## Was wurde gemacht

### ✅ Sachsen — 6. von 16 Bundesländer-Seiten auf Elite-Niveau

| Metrik | Vorher | Nachher |
|---|---|---|
| Audit-Score | 37/100 | **85/100** |
| Wortzahl | ~321 | **2.250** |
| §-Referenzen | 0 | **19** |
| Externe Quellen | 0 | **22** |
| Re-Check Blocker | 3 | **0** |
| Re-Check Warnungen | 4 | **0** |

### 🚨 DER inhaltliche Kerngewinn

Die alte Seite log mit „Sargpflicht: Nein" — Sachsen gehört in Wahrheit
zusammen mit **Bayern** zu den letzten beiden Bundesländern mit
**durchgängiger Sargpflicht** (LSA-Reform 11.09.2025 hat den dritten
Sarg-Staat raus). Belegt mit drei Paragraphen:
- § 18a SächsBestG (Erdbestattung nur in Särgen)
- § 20 Abs. 1 Satz 4 SächsBestG (Einäscherung nur im umweltverträglichen Sarg)
- § 16 Abs. 1 SächsBestG (Einsargung zur Beförderung)

### Weitere Sachsen-spezifische Korrekturen gegen das alte Template

- **8 Werktage** Höchstfrist (nicht „8 Tage" — § 19 Abs. 1, von Dresden.de bestätigt)
- **6 Monate** Urnenbeisetzung (§ 19 Abs. 2, sanktioniert via § 23 Abs. 1 Nr. 16)
- **20 Jahre auch für Aschen** (§ 6 Abs. 2 Satz 2 — Sachsen-spezifisch, in Brandenburg z.B. nur 15 J.)
- Friedhofsdaten Dresden: 58 Friedhöfe, 4 kommunale (dresden.de Primärquelle)
- Heidefriedhof 54 ha, 1936 (Wikipedia)
- Johannisfriedhof 1881, 2011 „Schönster Friedhof Deutschlands" (Denkmalfort)
- Trinitatisfriedhof als historischer Seuchenfriedhof
- Leipzig Südfriedhof 78 ha (leipzig.de Primärquelle)
- Krematorium Leipzig 14.01.1910 als 18. dt. Krematorium (leipzig.de wörtlich)
- Chemnitz: Eigenbetrieb der Stadt (NICHT GmbH — friedhof-chemnitz.de Primärquelle)

### Selbstkritischer Re-Check vor Deploy

Bolle hat „check alles nochmal" angeordnet — der ehrliche Stufe-1-Gate
hat 6 Korrekturen gefunden:

1. **Mathematik:** „13 andere Bundesländer" → „die übrigen 14" (16 - SN - BY = 14)
2. **Tippfehler:** „fünfgrößten" → „fünftgrößten" Friedhof
3. **Sachfehler Chemnitz:** „GmbH" → korrekt „Eigenbetrieb"
4. **Falsch attribuierte Höhe:** Glockenturm „63 m laut Wikipedia" raus
   (Wikipedia sagt 60 m, andere 63 m — Quellen-Konflikt) →
   konservativer formuliert ohne Höhenangabe
5. **6-Monats-Frist:** schwammigen Vergleich ersetzt durch Dresden-Beleg
   + § 23 Abs. 1 Nr. 16 (Ordnungswidrigkeit)
6. **Aschenruhezeit-Vergleich:** „manche andere BL" → präzises
   Brandenburg-Beispiel (15 J.)

## Workflow-Lehren dieser Session

1. **Mathematische Plausibilitätsprüfung gehört in den Re-Check.**
   „13 von 16 minus 2" hätte ich vorher rechnen sollen.
2. **Quellen-Konflikte explizit notieren.** Beim Glockenturm gab es
   60 m vs. 63 m — saubere Lösung war, die Zahl rauszunehmen, statt
   eine Quelle willkürlich zu wählen.
3. **Rechtsformen niemals raten.** „GmbH" hatte ich im Chemnitz-Absatz
   reflexhaft gesetzt — der Eigenbetrieb-Status hätte direkt geprüft
   werden müssen.

## Nächste Schritte

### Bundesländer-Seiten: 10 weitere zu überarbeiten

Sortiert nach Re-Check-Blocker-Anzahl (Stand vor Sachsen):

| Nächste | Audit | Re-Check Blocker |
|---|---|---|
| Bremen | 81 | 3 |
| Niedersachsen | 80 | 3 |
| Hamburg | 71 | 2 |
| Schleswig-Holstein | 79 | 2 |
| Berlin | 81 | 2 |
| Rheinland-Pfalz | 80 | 2 |
| NRW | 78 | 1 |
| Bayern | 81 | 1 |
| Hessen | 80 | 1 |
| Saarland | 71 | 1 |

Empfehlung für nächste Session: **Bremen oder Niedersachsen** (3
Blocker, Hansestadt-Besonderheiten) — oder **Hamburg/Schleswig-Holstein**
(Bolles Region, also persönlicher Bezug).

**Bayern interessant nach Sachsen:** Beide letzten Sarg-Länder, Sachsen
hat jetzt einen sauberen Rahmen — Bayern könnte direkt auf die gleiche
Argumentationslinie aufgesetzt werden.

### Weitere offene Punkte (aus BACKLOG, unverändert)

- **Vorsorge-Ordner:** strategische Entscheidung fällig — die
  „Kommt bald"-Platzhalter sind YMYL-fragwürdig
- **10 Tool-Seiten** warten auf A.3 Static-Shell-Umbau
- **PRE_LAUNCH_MODE auf False** setzen, sobald Phase F aktiv rollt
- **17 kaputte interne Links sitewide** (Phase D)
- **sitemap.xml stale** (45 noindex-Städte, Phase D)
- **B.2.2 Reviewer-Zeile aktivieren**, wenn Fachpool real
- **D.2.1 Gold-Städte** auf Score ≥ 85 mit FuneralHome-Schema

### Mail-Infrastruktur (aus Mail-Session 24.04.)

- 🗓️ **08.05.2026:** Migadu-Trial-Ende — Entscheidung Mini ($90/J)
  vs. Micro ($19/J)
- GMX-IMAP-Einbindung der beiden Mailboxen offen
- DMARC machsleicht.de aktuell `p=none`, langfristig auf `p=quarantine`

## Offene Fragen

Keine aktuell.
