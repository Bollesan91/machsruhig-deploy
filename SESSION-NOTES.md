# Session-Notizen

## Letzte Session
**Datum:** 11. Mai 2026 (Content-Loop Pilot — Saarland + Hessen via Multi-Chat-Methode)
**Deploy-Status:** Saarland + Hessen mit Deploy gepusht.

## Was wurde gemacht

### 🎯 Content-Loop-Methode (Multi-Chat) erfolgreich validiert

Manueller Pilot der 3-Chat-Architektur (Writer A / Reviewer B / Adversarial C) mit zwei Bundesland-Pages durchlaufen — beide Pages auf Recheck-grün gebracht, Hessen erreicht das Score-85-Ziel.

| Bundesland | Audit vorher | Audit nachher | Recheck | Tool-Fix-Versuche |
|---|---|---|---|---|
| **Saarland** | 71 + 1 Blocker | **83** | 0/0 ✓ | 4 (Plateau bei 83 — Schönarbeit, nicht Substanz) |
| **Hessen** | 80 + 1 Blocker | **85** | 0/0 ✓ | 2 (Ziel erreicht ohne Eskalation) |

**Vorher-Findings:**
- Saarland: Template-Sachfehler „Mindestfrist 24h", 0 §-Refs, 0 Primärquellen
- Hessen: Template-Sachfehler „Sargpflicht: Nein" (laut FBG 2025 FALSCH — Sargpflicht JA mit religiöser Ausnahme § 18 Abs. 2)

### 🎯 Branch-Trick als V2-Methodik-Durchbruch

V1 (Saarland) mit chunked-paste pro Page-Übergabe: ~90 Min Wall-Clock, 12+ Tool-Calls pro Round, 4 Tool-Fix-Versuche → Score 83.

V2 (Hessen) mit Branch-Trick (Files auf `content-loop-pipeline` gepusht, Worker fetcht via raw-URL): ~50 Min Wall-Clock, **0 chunked-Operations**, 2 Tool-Fix-Versuche → Score 85.

Plus: **Quellen-Pack via WebSearch vorab recherchiert** und auf Branch gepusht — eliminiert das Round-1-MISSING-Problem komplett.

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

## Status 15/16 Bundesländer auf Elite-Niveau

**Fertig (alle template-konform, alle primärquellen-belegt):**
BW, MV, LSA, TH, BB, SN, BY, HB, NI, HH, SH, B, RP, **Saarland**, **Hessen**

**Offen (nur noch 1!):**
- NRW (Audit 78, 1 Recheck-Blocker)

## Nächste Schritte

- **NRW** als finale BL-Page → Score-Ziel 85+. Mit V2-Methodik (Branch-Trick + Quellen-Pack vorab).
- **Methodik-V3:** Stopp-Regel „Basics vs Schönarbeit" einbauen — verhindert die 4 Versuche, die bei Saarland nur 2 P Gewinn pro 2 Versuche brachten.

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
