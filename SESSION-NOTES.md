# Session-Notizen

## Letzte Session
**Datum:** 24. April 2026 (Quality-Pass über alle 12 fertigen BL-Seiten, mit Deploy)
**Deploy-Status:** Mit „ende deploy" gepusht und deployed.

## Was wurde gemacht

### ✅ Vollständige Konsistenz-Prüfung aller 12 fertigen BL-Seiten

**Metrik-Kohärenz (alle 12):**
- Score **85** bei allen
- **0 Issues, 0 Warnungen** bei allen
- **12 interne Links** identisch (Nav byte-identisch, Hash `6531f63e`)
- **Alle JSON-LD-Schemas** identische Typen und valide
- **Wortzahl 1.800–2.400** im Zielkorridor
- **H2-Count 11–12** kohärent
- Canonical-URLs sauber (Umlaute für BW/TH bewusst, externe Links in ASCII korrekt)

### 🟡 3 kleine Drift-Korrekturen (Template-Angleichung)

1. **Baden-Württemberg**: H2 `Auf einen Blick` → `Kernfakten` (ältere Seite angeglichen)
2. **Mecklenburg-Vorpommern**: H2 `Auf einen Blick` → `Kernfakten` (ältere Seite angeglichen)
3. **Brandenburg: Stahnsdorf-Ergänzung** — echter inhaltlicher Gap geschlossen

### 🔴 → 🟢 Echter inhaltlicher Gap geschlossen: Stahnsdorf auf der Brandenburg-Seite

Der Südwestkirchhof Stahnsdorf ist mit 206 Hektar **Deutschlands zweitgrößter Friedhof** nach Ohlsdorf und weltweit einer der zehn größten. Er liegt geografisch in der brandenburgischen Gemeinde Stahnsdorf, wird aber in der öffentlichen Wahrnehmung meist Berlin zugeordnet.

**Vorher:** Brandenburg-Seite erwähnte Stahnsdorf nicht (!). Nur Berlin-Seite hatte es mit korrekter geografischer Präzisierung.

**Jetzt:** Brandenburg-Seite hat einen H3-Block „Südwestkirchhof Stahnsdorf — Deutschlands zweitgrößter Friedhof" mit:
- 206 ha, 1909 von Evangelischer Kirche eingerichtet
- Bedeutung: größter Waldfriedhof Deutschlands, weltweit Top-10
- S-Bahn-Anschluss 1913
- 15.000 Grabstätten-Umbettung bis 1940 wegen „Germania"-Planung
- Prominente: Werner von Siemens, Heinrich Zille, Engelbert Humperdinck, Manfred Krug, Dieter Thomas Heck
- Norwegische Holzkirche im Jugendstil, bekannt aus Netflix „Dark"
- Quellen: suedwestkirchhof.de + Wikipedia (2 neue Einträge in der Quellenliste)

**Brandenburg-Metriken nach Ergänzung:**
- Words: 1.805 → 1.969 (+164)
- External Links: 13 → 15
- Score 85 gehalten

### Querverweis-Logik Berlin ↔ Brandenburg jetzt sauber

Berlin-Seite sagt: „liegt allerdings nicht in Berlin, sondern... in der brandenburgischen Gemeinde Stahnsdorf"  
Brandenburg-Seite sagt: „Eine internationale Besonderheit liegt im Berliner Umland: Der Südwestkirchhof Stahnsdorf..."

Beide Seiten verweisen geografisch korrekt aufeinander und jede bringt ihre eigene Perspektive. **Für SEO:** Beide Seiten ranken jetzt für Stahnsdorf-Queries mit unterschiedlichen Nutzungsszenarien (Berliner, die nach Stahnsdorf suchen — Brandenburger, die ihren BL-Friedhof kennenlernen wollen).

## Status: 12/16 Bundesländer auf Elite-Niveau

**Fertig, alle template-konform, alle primärquellen-belegt:**
BW, MV, LSA, TH, BB, SN, BY, HB, NI, HH, SH, B

**Offen (4):**
| Nächste | Audit | Re-Check Blocker |
|---|---|---|
| Rheinland-Pfalz | 80 | 2 |
| NRW | 78 | 1 |
| Hessen | 80 | 1 |
| Saarland | 71 | 1 |

**Empfehlung nächste Session:** **Rheinland-Pfalz** (2025er Reform mit Aushändigung der Urne, Teilung der Asche, Aschebeisetzung in Flüssen — bisher liberalstes BL Deutschlands, sehr starke Story)

## Workflow-Lehren dieser Session

1. **Umlaute-URLs sind ein Falle für Automatisierung.** Mein erster Audit hatte nur 10 BL gefunden, weil die bash-for-Schleifen ASCII-Namen nutzten. `baden-wuerttemberg` existiert nicht, der Ordner heißt `baden-württemberg`. Das Skript `audit-all-pages.py` fand sie aber, weil es im Dateisystem direkt liest. **Lektion:** Beim Regression-Test IMMER direkt aus der Verzeichnisliste iterieren, nicht aus dem Kopf geraten.

2. **Nav-Byte-Identity-Check als Quality-Gate.** Md5-Hash über den gesamten Nav-Block aller 12 BL verglichen — alle identisch. Das ist der billigste strukturelle Drift-Test, der funktioniert. Sollte als Pre-Commit-Check aufgenommen werden: `python3 _dev/check-nav-consistency.py`.

3. **Cross-Referenz-Gaps zwischen BL-Seiten sind die echten inhaltlichen Drift-Indikatoren.** Die Sachfehler-Blocker fängt das Skript. Aber ein Stahnsdorf, der auf der Berlin-Seite erwähnt wird und auf der Brandenburg-Seite fehlt — das erwischt man nur durch menschliche Inhalts-Prüfung. Nächste Idee: ein Quer-Verweis-Skript, das prüft, ob prominente Städte/Friedhöfe, die in einer BL-Seite genannt werden, auch in der geografisch korrekten BL-Seite vorkommen.

4. **Stufe-2-Check: Metrik-Uniformität als Vertrauenssignal.** Wenn alle 12 Seiten auf Score 85 sind mit 11-12 H2s und 12 Nav-Links und identischen Schemas, ist das ein starkes Signal dafür, dass der Autor-Workflow konsistent lief. Abweichungen würden sofort auffallen.

## Weitere offene Punkte (aus BACKLOG, unverändert)

- **Vorsorge-Ordner:** strategische Entscheidung fällig
- **10 Tool-Seiten** warten auf A.3 Static-Shell-Umbau
- **PRE_LAUNCH_MODE auf False** setzen, sobald Phase F aktiv rollt
- **17 kaputte interne Links sitewide** (Phase D)
- **sitemap.xml stale** (45 noindex-Städte, Phase D)
- **B.2.2 Reviewer-Zeile aktivieren**, wenn Fachpool real
- **D.2.1 Gold-Städte** auf Score ≥ 85 mit FuneralHome-Schema
- **Quer-Verweis-Skript BL-Seiten** (neue Idee aus dieser Session)

## Mail-Infrastruktur (unverändert)

- 🗓️ **08.05.2026:** Migadu-Trial-Ende — Entscheidung Mini ($90/J) vs. Micro ($19/J)
- GMX-IMAP-Einbindung der beiden Mailboxen offen
- DMARC machsleicht.de aktuell `p=none`, langfristig auf `p=quarantine`

## Offene Fragen

Keine aktuell.
