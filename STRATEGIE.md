# machsruhig.de — STRATEGIE

> Single Source of Truth für alle strategischen Entscheidungen.
> Operative Tickets liegen in [BACKLOG.md](./BACKLOG.md).
> Quellmaterial im Archiv unter `_dev/archiv/`.

**Stand:** 23.04.2026
**Letzte Konsolidierung:** Inhalte aus 7 _dev/docs Dokumenten + Audit-Befunden + externem strategischen Audit (6,6/10) zusammengeführt.

---

## Inhalt

1. [Vision & Mission](#vision--mission)
2. [Phasenmodell (Authority vor Leadgen)](#phasenmodell-authority-vor-leadgen)
3. [Content-Architektur](#content-architektur)
4. [Content-Klassen & Seitentypen](#content-klassen--seitentypen)
5. [CTA-Hierarchie](#cta-hierarchie)
6. [Linklogik & User Journeys](#linklogik--user-journeys)
7. [Monetarisierungsstrategie](#monetarisierungsstrategie)
8. [Trauer-Schutz (verbindlich)](#trauer-schutz-verbindlich)
9. [Quality-Gates (vor jedem Go-Live)](#quality-gates-vor-jedem-go-live)
10. [Wettbewerb & USP](#wettbewerb--usp)
11. [Tonalität & Pietät](#tonalität--pietät)
12. [Strategische Leitplanken](#strategische-leitplanken)

---

## Vision & Mission

machsruhig.de ist die **deutschsprachige Orientierungshilfe rund um Tod, Bestattung und Vorsorge**. Drei Lebensphasen werden abgedeckt:

1. **Vorsorge** — vor dem Todesfall
2. **Akutfall** — unmittelbar danach
3. **Trauer** — langfristige Bewältigung

**USP:** Die einzige deutsche Seite, die alle drei Phasen mit hoher Substanz abdeckt. Kein Wettbewerber macht alle drei gut (siehe Wettbewerb).

**Mission:** Menschen in einer der sensibelsten Situationen ihres Lebens orientieren — ohne Verkaufsdruck, ohne Sensationslust, mit echter Hilfe.

**Markenversprechen:** Trust first, Conversion folgt. Wir liefern erst Mehrwert, dann Monetarisierung — niemals umgekehrt.

---

## Phasenmodell (Authority vor Leadgen)

Strategische Reihenfolge nach externem Audit (6,6/10): erst Domain-Autorität, dann Skalierung. Sechs Phasen, dokumentiert im BACKLOG.md mit operativen Tickets.

```
PHASE A  [AKUT]              Deploy-Blocker entschärfen (Homepage + Gold-Städte aus CSR-Hölle)
   ↓
PHASE B  [parallel]          Trust-Layer (Über uns, Autoren, Methodik, Disclaimer)
   ↓
PHASE C  [4-6 Wochen]        Authority-Content (Akutfall → Kosten → Recht → Entscheidung)
   ↓
PHASE D  [laufend]           Strukturelle SEO (OG-Image, Schema-Typen, interne Links)
   ↓
PHASE E  [2-4 Wochen]        Top-10-Städte auf Gold-Niveau
   ↓
PHASE F  [erst wenn A-E]     Monetarisierung aktivieren (Affiliate, Lead-Funnel)
```

**Kritischer Punkt:** Monetarisierungs-Strukturen (Affiliate-Hooks, Bestatter-Leads) bleiben vorbereitet, aber **nicht aktiv ausgebaut** bis A-E solide sind. Die ursprüngliche Monetarisierungs-Roadmap aus _dev/docs/monetarisierung.md ist als Phase F im BACKLOG hinterlegt — chronologisch nach hinten verlagert.

---

## Content-Architektur

### Die drei Phasen-Cluster

| Cluster | URL-Präfix | Beispielseiten | Status |
|---|---|---|---|
| **Vorsorge** | `/vorsorge/*` | Hub, Bestattungsvorsorge, Sterbegeldversicherung, Patientenverfügung, Testament, Vorsorge-Ordner, Sorgerechtsverfügung, Digitaler Nachlass, Ohne Vorsorge | 9 Seiten live |
| **Akutfall** | `/`, `/beerdigung-planen`, `/tools/checkliste-todesfall` etc. | Beerdigung planen, Checkliste, Bestattungsarten, Bestattungskosten | erweiterungsbedürftig (Phase C.1) |
| **Trauer** | `/trauerrede-*`, `/kondolenz*`, `/trauer-*` | Trauerrede, Kondolenz, Trauersprüche, Kindern Tod erklären | live, weitere geplant |

### Lokale Architektur

| Typ | Anzahl | URL-Präfix |
|---|---|---|
| Stadtseiten (alle) | 50 | `/bestatter/[stadt]/` |
| Stadtseiten indexiert (Gold-Tier) | 5 | Berlin, Frankfurt, Hamburg, Köln, München |
| Stadtseiten noindex (Generic) | 45 | Rest |
| Bundesländer | 16 | `/bestattung-in/[bundesland]/` |

Begründung noindex: 45 Stadtseiten sind Copy-Paste-Klone (349 Wörter, 0 Eurozahlen, 4 Floskeln). Externes Audit warnt vor Generic-Massen-Templates. Indexierung würde Domain-Autorität schwächen. Reversibel via Backlog Phase E.

---

## Content-Klassen & Seitentypen

Jede Seite ist genau einer **Content-Klasse** und einem **Seitentyp** zugeordnet. Klasse + Typ bestimmen Aufbau, CTA-Stufen, Monetarisierungs-Erlaubnis.

### Übersicht

| Klasse | Typ | Beispiel | CTA-Stufen | Monetarisierung |
|---|---|---|---|---|
| Tool | TOOL | Bestattungskosten-Rechner | 1, 2, 3* | Nur nach Output, nicht bei Trauer-Tools |
| Hub | HUB | `/`, `/bestattungsarten` | 1, 2 | Nein |
| Info | INFO | `/bestattungskosten`, `/beerdigung-planen` | 1, 2** | Eingeschränkt, nicht bei Trauer-Info |
| Vorsorge | VOR | `/vorsorge/*` | 1, 2, 3 | Ja (in Phase F) |
| Lokal Stadt | LOK-S | `/bestatter/[stadt]/` | 1, 2, 3 | Ja, Bestatter-Leads (in Phase F) |
| Lokal Bundesland | LOK-BL | `/bestattung-in/[bl]/` | 1 | Nur interne Verlinkung |
| Legal | LEG | `/impressum`, `/datenschutz` | Keine | Nein |
| Trust | TRUST | `/methodik`, `/ueber-uns` (Phase B) | Keine | Nein |

\* Tool: Stufe 3 nur nach Output.
\** Info: Trauer-Info nur Stufe 1.

### CTA-Stufen

**Stufe 1 — Orientierung.** Text-Link oder dezenter Button. Beispiele: "Mehr zum Thema", "Tool starten", "Weiterlesen".

**Stufe 2 — Unterstützung.** Sekundär-Button. Beispiele: "Checkliste drucken", "Ergebnis speichern", "Per E-Mail senden".

**Stufe 3 — Conversion.** Primär-Button #7A6B5D, weiße Schrift. Beispiele: "Vorsorge-Vergleich starten", "Bestatter anfragen". **Pflicht:** Affiliate-Kennzeichnung. **Nicht aktiv bis Phase F.**

### Verbindliche Regeln

1. Jede Seite gehört genau einer Klasse an. Keine Mischformen.
2. CTA-Stufen sind aufsteigend. Stufe 3 setzt Stufe 1 + 2 voraus.
3. Pro sichtbarem Bereich maximal 1 Primär-CTA.
4. Trauerseiten: keine Stufe-3-CTAs, keine Monetarisierung. Verbindlich.
5. Affiliate-Links immer mit "*" gekennzeichnet, Hinweis im Footer.
6. Tool-Seiten brauchen Datenschutz-Hinweis zur lokalen Datenverarbeitung.
7. Kostenangaben brauchen Disclaimer "Alle Angaben sind Richtwerte".

### Anti-Patterns (verboten)

- Multiple gleichstarke CTAs ("Bestatter kontaktieren | Kosten berechnen | Vorsorge starten" alle gleich prominent)
- Dringlichkeits-Wording ("Jetzt sofort handeln!", "Nur noch heute!", "Letzte Chance!")
- Affiliate als Primär-CTA above-the-fold
- CTA vor Mehrwert (Seite öffnet → sofort "Bestatter anfragen" ohne Information)
- Pop-ups, Exit-Intent-Overlays, Countdown-Timer

---

## CTA-Hierarchie

Pro Seitentyp definiert. Vollständige Tabellen siehe `_dev/archiv/cta-hierarchie.md`. Kurzform:

### Hub (/, /bestattungsarten)
- Hero: Stufe 1 oder 2 (Tool starten, mehr erfahren) — kein direkter Sales-CTA
- Themen-Kacheln: Sekundär ("Mehr erfahren")
- **Regel:** Wegweiser, keine Conversion

### Tool-LP (/tools/*)
- Above-the-fold: Stufe 1 ("Tool starten")
- Nach Ergebnis: Stufe 2 ("Speichern", "Drucken")
- Nach Ergebnis: Stufe 3 nur wenn thematisch passt
- **Sonderfall Trauerrede:** kein Affiliate, kein Lead-Gen

### Vorsorge-Seite (/vorsorge/*)
- Above-the-fold: kein CTA — Content first
- Nach 50% Scroll: Stufe 3 (Vorsorge-Vergleich) — aber **erst in Phase F aktiviert**
- Seitenende: Cross-Sell zu anderen Vorsorge-Themen

### Stadt-Seite (/bestatter/[stadt]/)
- Above-the-fold: Stufe 3 ("Bestatter kontaktieren") — **erst in Phase F aktiviert**
- Bestatter-Liste: Stufe 3 pro Eintrag
- **Aktuell:** Sekundärer Pfad, weil 45/50 noindex und Phase F nicht aktiv

### Bundesland-Seite
- Above-the-fold: Stufe 1 ("Stadt wählen")
- Kein eigenes Lead-Gen, nur Weiterleitung

### Info-Ratgeber
- Above-the-fold: kein CTA
- Inline: Tertiär-Links zu verwandten Themen
- Seitenende: Sekundär-Link zu passendem Tool
- **Trauer-Ratgeber:** ausschließlich Stufe 1

### Legal
- Keine CTAs jeglicher Art

---

## Linklogik & User Journeys

### Die 5 Hauptpfade

**Pfad 1 — Bestattung planen:**
`/` → `/bestattungsarten` → `/bestatter/[stadt]/` → Bestatter-Anfrage *(letztes nur Phase F)*

**Pfad 2 — Vorsorge:**
`/` → `/vorsorge/` → `/vorsorge/sterbegeldversicherung` → Vergleich *(nur Phase F)*

**Pfad 3 — Akuter Todesfall:**
`/` → `/beerdigung-planen` → `/tools/checkliste-todesfall` → Checkliste drucken → `/bestatter/[stadt]/`

**Pfad 4 — Trauerrede / Kondolenz:**
`/trauerrede-schreiben` → `/tools/trauerrede` → Export → `/kondolenzschreiben` (kein Affiliate auf gesamtem Pfad)

**Pfad 5 — Kosten verstehen:**
`/bestattungskosten` → `/tools/bestattungskosten-rechner` → Ergebnis → Cross-Sell zu Vorsorge oder Bestatter

### Cross-Sell-Regeln

**Pflicht-Cross-Sells** (siehe vollständig in `_dev/archiv/linklogik.md`):
- Bestattungskosten → Sterbegeldversicherung
- Checkliste Todesfall → Bestatter (Stadt)
- Trauerrede schreiben → Trauerrede-Generator
- Vorsorge-Check (Output) → Patientenverfügung, Testament, Sterbegeld

**Verbotene Cross-Sells:**
- Trauerrede → Sterbegeldversicherung
- Kondolenzschreiben → Affiliate jeder Art
- Trauersprüche → Bestatter-Anfrage
- Legal-Seiten → CTAs

### Linkdichte-Richtwerte

| Seitentyp | Min. interne Links | Max. interne Links | Externe Links max. |
|---|---|---|---|
| Hub | 5 | 15 | 0 |
| Tool-LP | 3 | 6 | 0-1 |
| Info/Ratgeber | 4 | 10 | 1-3 |
| Vorsorge | 4 | 8 | 2-4 (Affiliate) |
| Lokal Stadt | 3 | 8 | 0-2 |
| Lokal BL | 5 | 20 | 0 |
| Legal | 1 | 3 | je nach Bedarf |

### Anti-Patterns

- Tool-Hopping ohne Output (User muss erst Ergebnis sehen)
- Externe Links vor internen
- Zirkuläre Verlinkung ohne Mehrwert
- Orphan-Pages ohne ausgehende interne Links
- Affiliate-Link als allererster Link auf einer Seite

---

## Monetarisierungsstrategie

> **Aktueller Stand:** Vorbereitet, aber nicht aktiviert. Aktivierung in Phase F.

### Grundprinzipien

1. **Respekt vor der Situation** — Trauer-Kontext darf nie monetarisiert werden.
2. **Trust vor Umsatz** — Mehrwert zuerst, Conversion folgt.
3. **Vorsorge ist monetarisierbar** — proaktive Planer sind offen für Lösungen.
4. **Trauer ist tabu** — keine Ausnahme, keine Diskussion.
5. **Transparenz immer** — Affiliate sichtbar gekennzeichnet.

### Tier 1 — Aktivierbar in Phase F

#### 1.1 Sterbegeldversicherung-Affiliate
- Plattform: `/vorsorge/sterbegeldversicherung`
- Modell: CPL (5-15 €) oder CPA (30-80 €)
- Empfohlene Partner: **DELA (130 €/Sale), SOLIDAR (75 €/Sale), Afilio (30 €/Sale)**
- Anträge können in Phase F.1 vorbereitet werden (4 Wochen Bearbeitungszeit)

#### 1.2 Bestatter-Leads
- Plattform: 50 Stadtseiten
- Modell: CPL 10-30 € (Akut > Vorsorge)
- Voraussetzung: 5 Gold + 5 weitere Top-10-Städte aufgerüstet (Phase E)
- Backend-Optionen: Netlify Forms / Formspree / eigener Worker

#### 1.3 Vorsorge-Dokumente Affiliate
- Plattform: `/vorsorge/patientenverfuegung`, `/vorsorge/testament`, `/vorsorge/vorsorge-ordner`
- Partner-Optionen: smartlaw, Formblitz, Arag, AfterLife
- Modell: CPS 5-15% vom Preis

### Tier 2 — Mittelfristig (Monat 6+)

- Eigener Bestattungsvorsorge-Vergleich (3-6 Monate Entwicklung)
- Premium Vorsorge-Ordner als Lead-Magnet (E-Mail gegen PDF)
- Bestatter-Verzeichnis Freemium (29-149 €/Monat pro Bestatter)

### Tier 3 — Langfristig (12-24 Monate)

- Online-Bestattungsvorsorge-Plattform
- Bestatter-Bewertungssystem
- Newsletter / Trauer-Begleitung

### Umsatz-Prognose (konservativ)

**Tier 1 (ab Monat 1-3 nach Phase-F-Start):** 1.375 - 8.450 €/Monat
**Skaliert (ab Monat 6-12):** 9.900 - 41.000 €/Monat

Quelle: Detailrechnung in `_dev/archiv/monetarisierung.md`. Zahlen abhängig von organischem Traffic.

### Verbindliche Monetarisierungs-Regeln

| Seitentyp | Monetarisierung erlaubt? | Bedingung |
|---|---|---|
| Trauer-Info & Trauer-Tools | **VERBOTEN** | absolut, keine Ausnahme |
| Vorsorge | Ja | nur in Phase F, mit Trust-Layer |
| Tool-Seiten (nicht Trauer) | Ja, nach Output | erst nach Mehrwert |
| Stadtseiten | Ja, Bestatter-Leads | nur Gold-Tier, in Phase F |
| Bundesländer | Eingeschränkt | nur interne Verlinkung |
| Legal | **VERBOTEN** | absolut |
| Hub | Nein | nur Wegweiser |

---

## Trauer-Schutz (verbindlich)

**4 Seiten haben absoluten Trauer-Schutz:**

| URL | Typ | Begründung |
|---|---|---|
| `/trauerrede-schreiben` | INFO | Akuter Trauerfall-Kontext |
| `/tools/trauerrede` | TOOL | Generator für Trauerrede |
| `/kondolenzschreiben` | INFO | Beileid an Trauernde |
| `/trauersprueche` | INFO | Trauernde suchen Worte |

**Plus:** alle künftigen `/trauer/*`-Seiten (Erstes Jahr, Weihnachten, Feiertage etc.) — siehe Backlog.

**Was bedeutet absoluter Trauer-Schutz:**

- Keine Affiliate-Links jeglicher Art
- Kein Lead-Gen
- Keine gesponserten Inhalte
- Keine prominenten Buttons (nur Text-Links)
- Keine Cross-Sells zu monetarisierten Seiten
- Keine Bilder, die dramatisch oder bedrückend wirken
- Tonalität: warm, respektvoll, zurückhaltend, nie drängend

---

## Quality-Gates (vor jedem Go-Live)

Jede neue Seite muss alle 7 Gates bestehen. Gate 7 (Pietät) ist harter Blocker.

| Gate | Name | Prüft | Blocker? |
|---|---|---|---|
| 1 | Intent-Fit | Title + H1 matchen Suchintention | Ja |
| 2 | Utility | Konkreter Output oder echte Hilfe | Ja |
| 3 | Differenzierung | Besser/anders als Konkurrenz | Nein* |
| 4 | Conversion-Klarheit | 1 Primär-CTA pro sichtbarem Bereich | Ja |
| 5 | Brand-Fit | Design, Farben, Fonts, Tonalität | Ja |
| 6 | Programmatic-Sauberkeit | Keine Platzhalter, Template-Reste, 404-Links | Ja |
| 7 | **Pietät-Check** | Angemessener Ton bei Trauerinhalten | **Ja** |

\* Gate 3: kein harter Blocker, aber Warnsignal.

### Gate 7 — Pietät (harter Blocker)

**Verbotene Formulierungen:**

| Verboten | Stattdessen |
|---|---|
| "Profitieren Sie von..." | "Nutzen Sie die Möglichkeit..." |
| "Angebot sichern" | "Mehr erfahren" |
| "Countdown" / "Nur noch X Plätze" | Keine künstliche Verknappung |
| "Deal" / "Schnäppchen" | Nicht verwenden |
| "Tod" als Clickbait | Sachliche Formulierung |
| "Bestattungs-Business" | "Bestattungswesen" oder "Bestattungsbranche" |
| "Leiche" (Marketing) | "Verstorbene/r" |
| "Kunden" (für Trauernde) | "Menschen" oder "Angehörige" |
| "Verkaufen" (Bestatter-Kontext) | "Beraten" oder "Begleiten" |

**Pietät-Level pro Seitentyp:**

| Seitentyp | Pietät-Level | Anmerkung |
|---|---|---|
| Tool | Hoch | besonders Trauerrede-Tool |
| Hub | Mittel | warmherzig, einladend, nie vertrieblich |
| Info | Hoch | Trauer-Info: maximale Sensibilität |
| Vorsorge | Mittel | proaktiv, aber Thema bleibt sensibel |
| Lokal | Mittel-Hoch | oft akute Situation |
| Legal | Neutral | sachlich-juristisch |

### Vollständige QA-Checklist

Detaillierte Prüfkriterien pro Gate inkl. PASS/FAIL-Beispiele in `_dev/archiv/qa-gates.md`.

### QA-Ablauf

1. Automatisierte Checks (Gate 6) — `_dev/audit-all-pages.py`
2. Gate 1-5 — manuelle Inhalts-/Design-Review
3. Gate 7 — letzter Check, harter Blocker
4. Stichproben monatlich nach Go-Live

---

## Wettbewerb & USP

| Wettbewerber | Stärke | Unsere Differenzierung |
|---|---|---|
| **November.de** | Full-Service Bestatter | Wir sind unabhängig, kein Verkauf |
| **Mymoria** | Online-Buchung | Wir sind kostenlos, ohne Anmeldung |
| **bestattungen.de** | Großes Verzeichnis | Wir haben bessere Tools + Content |
| **Afilio** | Vorsorge-Dokumente | Wir sind breiter (Trauer + Vorsorge + Akut) |
| **Gedenkseiten.de** | Memorial Pages | Wir verlinken statt konkurrieren |
| **Verivox / Check24** | Sterbegeld-Vergleich | Nicht angreifen — chancenlose SERP |

### Unser USP

Die EINZIGE deutsche Seite, die alle drei Phasen abdeckt:

1. **Vorsorge** (vor dem Todesfall)
2. **Akutfall** (unmittelbar danach)
3. **Trauer** (langfristige Bewältigung)

Kein Wettbewerber macht alle drei gut. Das ist der strategische Hebel.

### Differenzierungsmerkmale

| Merkmal | Vorteil |
|---|---|
| Interaktive Tools | Rechner, Generatoren, Checklisten als Web-Apps |
| Empathische Tonalität | Respektvoll statt klinisch oder reißerisch |
| Lokaler Bezug | 50 Städte + 16 Bundesländer (5 Gold-Städte indexiert) |
| Vorsorge-Kompetenz | Gebündeltes Wissen zu allen Vorsorge-Themen |
| Kein Push-Marketing | Trust-first statt Conversion-first |

---

## Tonalität & Pietät

### Grundton

**Sachlich, warm, respektvoll.** Nicht klinisch, nicht reißerisch, nicht drängend.

Vergleich:

| Falsch | Richtig |
|---|---|
| "Schockierende Wahrheit über Bestattungskosten!" | "Bestattungskosten 2026 — was Sie wissen sollten" |
| "Wenn Sie JETZT nicht handeln..." | "Es kann sinnvoll sein, frühzeitig vorzusorgen" |
| "Profitieren Sie von unserem Angebot" | "Nutzen Sie diese Möglichkeit" |
| "Ist doch nicht so schlimm" | "In dieser schwierigen Situation..." |

### Bildsprache

- **Erlaubt:** Natur, Ruhe, Geborgenheit, gedämpfte Farben
- **Verboten:** Schockbilder, dramatische Szenen, Friedhof-Atmosphäre als Schauerelement

### Markenfarben

| Farbe | Hex | Verwendung |
|---|---|---|
| Primär (warm-braun) | `#7A6B5D` | Buttons, Akzente |
| Hintergrund (creme) | `#FAF8F5` | Body |
| Text dunkel | `#2D2319` | Primärtext |
| Text gedämpft | `#73655A` | Sekundärtext |
| Accent | `#866E45` | Hervorhebungen |

WCAG-AA-Kontraste auf allen 88 HTML-Seiten validiert (April 2026).

### Schriften

- **Headings:** Fraunces (Serif, warm)
- **Body:** DM Sans (Sans-Serif, gut lesbar)
- Self-hosted in `/fonts/`

---

## Strategische Leitplanken

Diese Regeln gelten über alle Phasen. Verstoß = Qualitätsschaden.

1. **Authority vor Leadgen.** Erst Domain-Autorität, dann Monetarisierung aktivieren.
2. **Keine weiteren Generic-Template-Seiten.** Substanz-Kriterien (Friedhofsnamen, €-Beträge, Quellen) müssen erfüllt sein.
3. **YMYL-Standard immer.** Autor, Stand, Quellen, Disclaimer auf jeder gesundheits-/rechts-/finanz-relevanten Seite.
4. **Keine CSR-Experimente bei Content-Seiten.** Tools dürfen clientseitig rendern, Content-Seiten serverseitig/statisch.
5. **Reversibilität bewahren.** `noindex` statt löschen. Änderungen mit HTML-Kommentaren dokumentieren.
6. **Trauer-Schutz absolut.** Keine Diskussion, keine Ausnahme.
7. **Keine Bestatter-Leadgen bauen, bis Authority steht.** Lead-Funnel bleibt liegen bis Phase F.
8. **Gold-Standard vor Skalierung.** 10 echt gute Stadtseiten > 50 mittelmäßige.

---

## Verweise

- **Operative Tickets:** [BACKLOG.md](./BACKLOG.md)
- **Session-Gedächtnis:** [SESSION-NOTES.md](./SESSION-NOTES.md)
- **Audit-Tools:** `_dev/audit-all-pages.py`, `_dev/stadt-quality-analysis.py`
- **Audit-Reports:** `_dev/AUDIT-REPORT.json`, `_dev/stadt-quality.json`
- **Strategie-Quellmaterial (Archiv):** `_dev/archiv/`
