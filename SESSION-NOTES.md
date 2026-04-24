# Session-Notizen

## Letzte Session
**Datum:** 24. April 2026 (Schleswig-Holstein-Sprint, mit Deploy)
**Deploy-Status:** Mit „ende deploy" gepusht und deployed.

## Was wurde gemacht

### ✅ Schleswig-Holstein — 11. von 16 Bundesländer-Seiten auf Elite-Niveau

| Metrik | Vorher | Nachher |
|---|---|---|
| Audit-Score | 79/100 | **85/100** |
| Wortzahl | 366 | **2.040** |
| §-Refs | 0 | **8+** |
| Externe Quellen | 0 | **16** |
| Re-Check Blocker | 2 | **0** |
| Re-Check Warnungen | 4 | **0** |

### 🚨 DER inhaltliche Kerngewinn

Die alte Seite hatte **zwei Standard-Sachfehler** (Sargpflicht: Nein, Mindestfrist 24h). 

**Schleswig-Holsteins ganz neue Story — Reform 13.12.2024 (in Kraft 31.12.2024):**
1. **Sargpflicht-Lockerung** (§ 26 Abs. 4): Bestattung im Leichentuch ist jetzt grundsätzlich erlaubt auf den Willen der verstorbenen Person hin — nicht mehr nur aus religiösen oder weltanschaulichen Gründen.
2. **Asche-Verstreuung auf Friedhöfen** (§ 26 Abs. 3 Nr. 3) neu möglich.
3. **Urnen-Frist auf 3 Monate verlängert** (§ 16 Abs. 3) — vorher 1 Monat.
4. **Strengere Seebestattung** — nur noch durch zugelassene Schiffe.
5. **Reerdigung-Pilotprojekt** (Humus-Transformation in 40 Tagen) auf Grundlage § 15a.

### Schleswig-Holstein-Spezifika belegt
- **BestattG vom 4.2.2005** (GVOBl. Schl.-H. S. 70), Reform 13.12.2024 (in Kraft 31.12.2024), frühere Änderung 29.1.2024
- **§ 16 Abs. 1**: 48h Mindestfrist + 9 Tage Höchstfrist (Soll-Vorschrift)
- **§ 16 Abs. 3** (neu 2024): Urnen 3 Monate nach Einäscherung
- **§ 23 Abs. 1, 2**: Mindestruhezeit durch Friedhofsträger
- **§ 26 Abs. 4**: Sargpflicht-Ausnahme auf Willen
- **§ 26 Abs. 3 Nr. 3**: Asche-Verstreuung auf Friedhöfen neu
- **§ 15a**: Erprobungsklausel (Reerdigung läuft hier)
- **§ 2 Nr. 12**: Reihenfolge Bestattungspflichtige
- **Vorwerker Friedhof Lübeck**: 53 ha, größter der 6 städtischen Lübecker, erstes staatliches Krematorium SH (Verbrennungskirche), in Kiel erst 1916 in Betrieb
- **Lübeck Bestattung im Leichentuch nur Vorwerk und Waldhusen** (Friedhofssatzung)
- Schleswig-Holstein hat den **größten Anteil aller Seebestattungen Deutschlands**

### Korrekturen aus Stufe-1-Gate vor Deploy
1. **Geografie-Fehler:** Rostock (in MV) als SH-Hafen erwähnt — durch Travemünde ersetzt. Gut, dass Re-Check-Skript das fängt.
2. **Lübeck-Ruhefrist „1. Lebensjahr 15 Jahre" entschärft** — die Spezifizierung war geraten, der Friedhofssatzungs-Snippet zeigte zwar „15 Jahre", aber ohne klares Subjekt. Defensive Formulierung: nur noch die Existenz von kürzeren Fristen für Kinder erwähnen, ohne konkrete Zahl.
3. **Title gekürzt** auf 52 Zeichen.
4. **Meta-Description gekürzt** auf 156 Zeichen.

## Status: 11/16 Bundesländer auf Elite-Niveau

**Fertig:** BW, MV, LSA, TH, BB, SN, BY, HB, NI, HH, **SH**

| Nächste | Audit | Re-Check Blocker |
|---|---|---|
| Berlin | 81 | 2 |
| Rheinland-Pfalz | 80 | 2 |
| NRW | 78 | 1 |
| Hessen | 80 | 1 |
| Saarland | 71 | 1 |

**Empfehlung nächste Session:** **Berlin** (Score 81, sollte schnell auf 85 zu bringen sein, Stadtstaat wie HB/HH — Drei-Stadtstaaten-Trilogie wäre dann komplett!) oder **Rheinland-Pfalz** (hat 2025er Reform mit Aushändigung der Urne, Teilung der Asche, Aschebeisetzung in Flüssen — deutlich liberaler als SH; eine starke Story).

## Workflow-Lehren dieser Session

1. **Geografie-Skript fängt Bundesland-Verwechslungen sehr zuverlässig.** Rostock-in-SH fiel sofort auf — wäre ohne das Skript live gegangen. Das Skript ist ein verlässlicher Wächter gegen genau diese Fehlerklasse.
2. **„Stadt-X-Friedhofssatzung sagt..."-Aussagen nur mit hochwertigem Wörtlich-Beleg.** Der Lübeck-Satzungs-Snippet war zu fragmentiert, um den 15-Jahre-Wert sicher dem 1. Lebensjahr zuzuordnen. Defensiv weglassen statt raten.
3. **Bei brandaktuellen Reformen explizit Stand-Datum nennen** (in Kraft seit 31.12.2024) — das gibt dem User Vertrauen und schützt uns gegen veraltete Konkurrenz-Inhalte.

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
