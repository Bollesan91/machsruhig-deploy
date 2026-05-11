# Session-Notizen

## Letzte Session
**Datum:** 11. Mai 2026 (Content-Loop Pilot — Saarland + Hessen + NRW via Multi-Chat-Methode)
**Deploy-Status:** Alle 3 Pages mit Deploy gepusht. **16/16 BL fertig.**

## Was wurde gemacht

### 🎯 Content-Loop-Methode (Multi-Chat) erfolgreich validiert + auf 3 BL angewandt

Manueller Pilot der 3-Chat-Architektur (Writer A / Reviewer B / Adversarial C) mit drei Bundesland-Pages durchlaufen — alle drei auf Recheck-grün gebracht, Hessen erreicht das Score-85-Ziel.

| Bundesland | Audit vorher | Audit nachher | Recheck | Tool-Fix-Versuche |
|---|---|---|---|---|
| **Saarland** | 71 + 1 Blocker | **83** | 0/0 ✓ | 4 (Plateau bei 83 — Schönarbeit) |
| **Hessen** | 80 + 1 Blocker | **85** | 0/0 ✓ | 2 (Ziel erreicht ohne Eskalation) |
| **NRW** | 78 + 1 Blocker | **83** | 0/0 ✓ | 2 (Plateau bei 83 — Stopp-Regel akzeptiert) |

**Vorher-Findings:**
- Saarland: Template-Sachfehler „Mindestfrist 24h", 0 §-Refs, 0 Primärquellen
- Hessen: Template-Sachfehler „Sargpflicht: Nein" (laut FBG 2025 FALSCH — Sargpflicht JA mit religiöser Ausnahme § 18 Abs. 2)

### 🎯 Branch-Trick als V2-Methodik-Durchbruch

V1 (Saarland) mit chunked-paste pro Page-Übergabe: ~90 Min Wall-Clock, 12+ Tool-Calls pro Round, 4 Tool-Fix-Versuche → Score 83.

V2 (Hessen) mit Branch-Trick (Files auf `content-loop-pipeline` gepusht, Worker fetcht via raw-URL): ~50 Min Wall-Clock, **0 chunked-Operations**, 2 Tool-Fix-Versuche → Score 85.

Plus: **Quellen-Pack via WebSearch vorab recherchiert** und auf Branch gepusht — eliminiert das Round-1-MISSING-Problem komplett.

### 🎯 Konsistenz-Check + Restruktur-Pattern

Nach erfolgreichem 3-Page-Pilot: Konsistenz-Check über alle 16 BL ergab — **15/16 strukturell konsistent**, Saarland v7 als Outlier (eigene CSS-Klassen statt mr-*, nur 6 H2 statt 11-14, abweichendes Schema-Set Cemetery+GeoCoordinates statt City+ImageObject).

**Restruktur-Pattern entwickelt:** 1 Round, 1 Prompt mit 2 URLs (CONTENT = Saarland v7, LAYOUT = Hessen v5), Worker gießt Inhalt in Standard-Struktur. Resultat **Saarland v8** — 100% strukturell konsistent mit anderen 15 BL, Score bleibt 83 (Plateau). **Effizienz:** 5 Min total statt voller Pipeline-Run.

Status finale Konsistenz:
- 16/16 mit mr-Layout-Klassen ✓
- 16/16 mit identischem Schema-Set (Article, FAQPage, BreadcrumbList, WebPage, Place, City, ImageObject, Organization, PostalAddress, ListItem, Question, Answer) ✓
- 16/16 mit Standard-Sektions-Reihenfolge (Kernfakten → Recht → Fristen → Sargpflicht → Ruhezeiten → Formen → Friedhöfe → Kosten → Hilfe → Was tun → FAQ → Quellen) ✓
- 16/16 mit DM Sans + Fraunces Fonts, skip-link, mr-breadcrumb ✓
- 16/16 Recheck grün (0 Blocker, 0 Warnungen) ✓

### V2-Methodologie als Repo-Doku

Komplette V2-Pipeline-Doku jetzt in `_dev/content-loop/V2-METHODOLOGY.md` — überlebt Memory-Verlust, ist für künftige Pilot-Runs (Stadt-Pages, Tool-Pages) referenzierbar. Enthält: Architektur, Phasen-Workflow, Stopp-Regel „Basics vs Schönarbeit", Konsistenz-Patterns, Restruktur-Pattern, Wakeup-Mechanismen, Token-Effizienz-Daten.

### Hessen-Story (FBG 2025)

- **Neues Friedhofs- und Bestattungsgesetz** vom Hessischen Landtag am 30.09.2025 verabschiedet, GVBl. Nr. 64 (06.10.2025)
- Höchstfrist Erdbestattung: **4 → 10 Tage** (zentrale Reform-Neuerung)
- § 18 FBG regelt Sargpflicht (religiöse Ausnahme nach Abs. 2)
- Friedhofszwang bleibt strikt — Bestattung im Garten ausgeschlossen
- **3 Friedhöfe mit Hidden-Gem-Stories:**
  - Frankfurt Hauptfriedhof 1828, 70 ha, Goethe-„Suleika"/Alzheimer/Schopenhauer/Adorno/Struwwelpeter
  - Kassel Hauptfriedhof 1843, 40 ha + **Künstler-Nekropole** (documenta-Verbindung — einzigartig in Deutschland)
  - Wiesbaden Nordfriedhof 1877, 14,5 ha, Helmut Schön/Volker Kriegel

### Saarland-Status (V1-Methodik, Plateau)

- Sargpflicht nun korrekt: SBestG mit religiöser Ausnahme via Friedhofssatzung
- 2 Friedhöfe Hidden-Gem: Hauptfriedhof Saarbrücken (Memotransfront-Projekt, deutsch-französische Grenzgräber 1870/71 + Weltkriege), Friedhof St. Johann (Willi-Graf-Ehrengrab Weiße Rose)
- FBG-Reform 2021 dokumentiert: Höchstfrist 7→10 Tage, Hermann-Scharf-Zitat zum Friedhofszwang

### 🛠️ Methodik-Findings für V3-Iteration

**Stopp-Regel „Basics vs Schönarbeit":**
- Weiter-iterieren wenn: Recheck-Blocker, Halluzinations-Verdacht, Major Audit-Issues (Schema fehlt, Title falsch, OG fehlt), Score-Gewinn ≥ 3 P pro Versuch
- Akzeptieren wenn: Recheck grün UND Score ≥ 82 UND letzte 2 Versuche < 3 P Gewinn (Plateau)

**Quellen-Pack-Pflicht im Task-Prompt:** ohne vorrecherchierten Pack endet Round 1 in MISSING (so wie Saarland v1).

**Branch-Trick:** für künftige Runs Standard. Erspart Chunking, ermöglicht Cross-File-Referenzen (RP-Page als Stil-Anker, Quellen-Pack, vorherige v-Versionen).

## Status 16/16 Bundesländer auf Elite-Niveau

**FERTIG — alle 16 BL template-konform, alle primärquellen-belegt:**
BW, MV, LSA, TH, BB, SN, BY, HB, NI, HH, SH, B, RP, **Saarland**, **Hessen**, **NRW**

### NRW-Story (§ 4a + Ruhrgebiet)

- BestG NRW vom 17.06.2003, Novelle 01.10.2014, letzte Änderung 01.02.2022
- Höchstfrist Erdbestattung: **10 Tage** (von 8 verlängert), Urnenbeisetzung: 6 Wochen
- **§ 4a BestG NRW** — Grabsteine ohne Kinderarbeit (ILO-Konvention 182), sozialpolitischer Vorreiter
- 3 Friedhöfe Hidden-Gem: **Köln-Melaten** (1810, 43,5 ha, Otto-Motor/Farina/Birgel/Adorno), **Düsseldorf-Nord** (1884, 70 ha, Millionenhügel mit Henkel/Haniel/Poensgen), **Dortmund-Haupt** (1921, **118 ha — einer der größten Deutschlands**, Expressionismus)
- Ruhrgebiet: Bergmanns-Bestattungskultur, Knappschaftsvereine
- Bevölkerungsreichstes BL → höchste Friedhofs/Krematoriumsdichte Deutschlands

## Nächste Schritte

- **Stadt-Pages** in Angriff nehmen (45 Thin-Content-Stadtseiten auf noindex, Top-5 ausbauen)
- **Methodik-V3 codifizieren:** Stopp-Regel „Basics vs Schönarbeit" als Standard für künftige Runs
- **Quellen-Pack-Generator** als Subagent — automatisiert die Vorab-Recherche
- **Auto-Pilot V1 erwägen** — drei API-Conversations statt Browser-Chats für Geschwindigkeit (jetzt ~50 min pro Page, API würde 10 min schaffen)

## Mail-Infrastruktur (unverändert)

- 🗓️ Migadu-Trial: Entscheidung Mini ($90/J) vs. Micro ($19/J) — Entscheidung steht noch aus
- GMX-IMAP-Einbindung der beiden Mailboxen offen
- DMARC machsleicht.de aktuell `p=none`, langfristig auf `p=quarantine`

## Offene Fragen

- Soll NRW direkt im Anschluss laufen, oder erst Methodik-V3 schärfen?
- Branch `content-loop-pipeline` — long-living lassen oder pro Page deleten?

## Erledigte PBIs (gesamt)

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 21, 22
+ Monetarisierung, Vorsorge-Cluster, 9 neue Tools/Seiten
+ Audit + Roadmap „Authority-first" (22.04.2026)
+ RP Elite-Niveau (24.04.2026)
+ **Content-Loop-Pilot Saarland + Hessen** (11.05.2026)
