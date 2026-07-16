# machsruhig.de — STRATEGIE

> Single Source of Truth für alle strategischen Entscheidungen.
> Operative Tickets liegen in [BACKLOG.md](./BACKLOG.md).
> Quellmaterial im Archiv unter `_dev/archiv/`.

**Stand:** 23.04.2026
**Letzte Konsolidierung:** Inhalte aus 7 _dev/docs Dokumenten + Audit-Befunden + externem strategischen Audit (6,6/10) zusammengeführt.
**Update 18.06.2026:** Neue strategische **Hauptsäule — Datentransparenz-Strategie** (Abschnitt 15). Detail-Konzept: `_dev/strategie/transparenz-partner-konzept.md` (v5). Vereint und hebt Kronjuwel 2 + M.5-Moats (Friedhofsgebühren-DB, Tool-Nutzungssignale) zur tragenden Geschäfts- und Autoritätssäule.

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
13. [Festgelegte Entscheidungen (23.04.2026)](#festgelegte-entscheidungen-23042026)
14. [Markteroberungs-Erweiterung (Roadmap für Phase D-E)](#markteroberungs-erweiterung-roadmap-für-phase-d-e)
    - M.1 Off-Page-SEO & PR · M.2 Distribution (Newsletter + Pinterest)
    - M.3 Kronjuwelen · M.4 Markt-KPIs · M.5 Moats
15. [Datentransparenz-Strategie — neue Hauptsäule (18.06.2026)](#datentransparenz-strategie-strategische-hauptsäule-ab-18062026)

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
> **Erweiterung 18.06.2026:** Die Kern-Monetarisierung entwickelt sich zur **transparenten Lead-Vermittlung** (Bestatter-Leads, aber *Zahlung kauft Zugang, nicht Rang* + redaktionelle Mauer zum Benchmark) plus **B2B-Daten-Reports** — siehe Abschnitt 15. Aktivierung bleibt Phase F; Authority-/Standard-Bausteine bauen schon vorher.

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

## Festgelegte Entscheidungen (23.04.2026)

Drei strategische Entscheidungen, die Folgearbeit blockierten, sind jetzt gefällt. Diese gelten verbindlich.

### Entscheidung 1 — Autorenmodell: "machsruhig Redaktion" + Fachpool-Reviewer

**Gewählt:** "machsruhig Redaktion" als Autor-Identität auf allen YMYL-Seiten, ergänzt durch namentlich genannte Reviewer aus einem Fachpool (zu rekrutieren: Bestatter, Jurist, Trauerbegleiter, Seelsorger).

**Begründung:**
- Sicheres Modell ohne persönliche Exposition (keine LinkedIn/Foto-Pflicht)
- Skalierbar — neue Inhalte brauchen keinen neuen Klarnamen
- Rechtliche Angreifbarkeit bleibt im Rahmen (Impressum führt rechtlich verantwortliche Person)
- Reviewer-Namen liefern E-E-A-T-Signal trotz Pseudonym-Autor

**Konsequenz für Implementierung:**
- Sichtbarer Block auf jeder YMYL-Seite mit "Redaktion machsruhig.de" + ggf. "Fachlich geprüft von: [Name], [Rolle]"
- `/team`-Seite mit Reviewer-Profilen (Kurz-Bio, Qualifikation)
- Schema.org `author` referenziert "Organization machsruhig.de"
- Schema.org `reviewedBy` referenziert Person-URLs

**Aufgabe Fachpool aufbauen** — siehe BACKLOG B.2.

### Entscheidung 2 — CSR-Fix-Strategie: Hybrid (Static Content + Widget für Tools)

**Gewählt:** Homepage und 5 Gold-Städte werden komplett statisch ausgeliefert. Die 9 Tool-Seiten bekommen eine Static Shell (H1, Intro 200-400 Wörter, Methodik, FAQ als statisches HTML) plus das React-Widget in einem klar abgegrenzten Container.

**Begründung:**
- Pre-Rendering (Option A) hätte Babel-Standalone im Bundle behalten — Performance bleibt schlecht, Build-Pipeline aufwändig
- Komplett-Rewrite (Option B) wäre 30-50h Arbeit, hätte Phase B blockiert
- Hybrid passt zur Leitplanke 4: Content statisch, Interaktion clientseitig

**Konsequenz für Implementierung:**
- Homepage: React/Babel-Standalone raus, statisches HTML mit echten H1/H2/Content/Schema/Internal-Links
- 5 Gold-Städte: bestehender Gold-Content statisch ausliefern, ggf. FAQ-Akkordeon als Progressive Enhancement
- 9 Tools: jeweils 200-400 Wörter statische Shell oben drüber/drumherum, Widget bleibt in `<div id="widget">`
- Build-Script (Phase A.4) optional, nur wenn nötig

### Entscheidung 3 — Realistische Kapazität: 6-8 h/Woche (machsruhig wird Hauptprojekt)

**Gewählt:** 6-8 Stunden pro Woche dediziert für machsruhig.de. Damit wird machsruhig zum priorisierten Projekt neben Advergy und vor machsleicht-Wachstumsfeatures.

**Konsequenz für Zeitplanung:**

Bei 7h/Woche Mittelwert:
- **Phase A (30-45h):** ca. **5-7 Wochen** (Mai bis Mitte Juni 2026)
- **Phase B (10-15h):** ca. **2 Wochen**, parallel zu A
- **Phase C.1+C.2 (50-60h):** ca. **8-9 Wochen** (Juni-August 2026)
- **Phase D (25-30h):** parallel laufend, plus 4 Wochen konzentriert
- **Phase C.5 saisonale Trauer-Seiten:** Allerheiligen-Content muss bis 10.10. live sein → harte Deadline
- **Phase E (20-30h):** ca. **3-4 Wochen** (September 2026)
- **Phase F (15-25h):** Aktivierung Oktober/November 2026

**Realistische Marker für 2026:**
- Q2 (Mai-Juni): Phase A + B fertig, Authority-Cluster begonnen
- Q3 (Juli-September): Phase C läuft, saisonaler Trauer-Content rechtzeitig live, Phase E gestartet
- Q4 (Oktober-Dezember): Phase F-Aktivierung, erste Affiliate-Erträge

**Pufferregel:** Bei Verzögerungen wird Skalierung (Phase E) zugunsten Authority (Phase C) verschoben — niemals umgekehrt.

---

## Markteroberungs-Erweiterung (Roadmap für Phase D-E)

> Hinweis: Die folgenden Sektionen sind **strategischer Vorlauf für Phase D-E**, nicht Bedingung für den Start in Phase A. Sie ergänzen den defensiven Authority-Plan um die offensive Markt-Komponente.
>
> Hintergrund: Eine externe strategische Bewertung sah den Plan als 8,2/10 für Authority-Aufbau, aber nur 6,8/10 für aktive Markteroberung. Die folgenden 5 Sektionen schließen diese Lücke — werden aber **erst nach Phase A+B operationalisiert**.

### M.1 — Off-Page-SEO & PR (Aktivierung Phase D)

**Ziel:** 30-50 verlinkende qualitativ relevante Domains aufbauen, plus Brand-Erwähnungen ohne Link.

**Ziel-Kategorien für Outreach:**

| Kategorie | Beispiele | Outreach-Ansatz |
|---|---|---|
| Verbraucherportale | Verbraucherzentrale (Bundesländer), Stiftung Warentest, Aeternitas e.V. | Faktencheck-Dossiers anbieten |
| Hospize & Trauerbegleitung | Deutscher Kinderhospizverein, Bundesverband Trauerbegleitung, lokale Hospize | Tool-Empfehlungen (Trauer-Tagebuch etc.) |
| Kirchen & Seelsorge | EKD, Caritas, Diakonie, einzelne Bistümer | Kondolenz-Ratgeber, Trauer-Begleitung |
| Bestatterkammern | Bundesverband Deutscher Bestatter (BDB), Landesinnungsverbände | Kosten-Transparenz, Wahl-Hilfe für Verbraucher |
| Behörden | Standesämter, Versorgungsämter (Sozialbestattung) | Anleitungen, FAQ-Verlinkung |
| Anwalts-/Notarverzeichnisse | Anwaltsauskunft DAV, Notar-Suche | Erbrecht-Themen, Patientenverfügung |
| Medien (Lokal- & Fachpresse) | Lokalzeitungen, Bestattungswelt, ZE Bestattungen | Datenstories aus Audit (Bestattungskosten-Vergleich) |
| Frauen-/Familien-Portale | Mama-Blogs, Familien-Magazine | "Kindern Tod erklären"-Cluster |

**Outreach-Formate:**
- Datenstory-Pitches (z.B. "Bestattungskosten 2026 nach Bundesland")
- Tool-Demonstrationen (Erbschaftssteuer-Rechner für Anwaltsblogs)
- Gastbeiträge (sehr selektiv, max. 3-5 pro Jahr)
- Faktenchecks für Redaktionen
- Saisonale PR-Anlässe (Totensonntag, Allerheiligen, Weihnachten)

**KPI:** 20+ Referring Domains bis Q4 2026, 50+ bis Q2 2027.

### M.2 — Distribution außerhalb Google: Newsletter + Pinterest

**Bewusste Beschränkung auf 2 Kanäle.** Nicht TikTok, nicht YouTube, nicht Reddit — solo-machbar nicht.

#### M.2.1 — Newsletter

**Warum:** Trauer-Begleitung ist mehrwöchig (siehe C.5.1 "Erstes Jahr"). Newsletter ist das einzige Format, das Mehrwochen-Begleitung leistet, ohne dass User ständig zurück auf die Seite müssen.

**Format:** Wöchentlich, aber Subscriber wählen Pfad ("Begleitung im 1. Jahr nach Verlust" / "Vorsorge-Roadmap" / "Akutfall-Checklisten").

**Lead-Magnets als Eintritt:**
- "Vorsorge-Ordner als PDF" (vorhandene Seite)
- "52 Wochen Trauerbegleitung" (Trauer-Tagebuch-Tool, geplant in C.7)
- "Bestattungskosten-Spickzettel" (1-Pager PDF aus Kosten-Cluster)

**Tool:** ConvertKit oder Mailerlite (DSGVO-tauglich, niedrigschwellig).

**KPI:** 500 Subscriber bis Q4 2026, 2000 bis Q2 2027.

#### M.2.2 — Pinterest

**Warum:** Trauersprüche/Trauerzitate dominieren Pinterest. Visuelle Pinnable-Cards zu Quotes plus Verlinkung zur Quelle = großer Traffic-Hebel mit wenig Aufwand. Funktioniert auch für Vorsorge-Checklisten und Akutfall-Anleitungen.

**Format:** Pin-Vorlagen in Markenfarben + Fraunces-Schrift erstellen. Pro Trauersprüche-Kategorie (Tod Mutter, Tod Vater, Tod Kind, Tod Partner) eigene Pinnwand.

**Cadence:** 5-10 neue Pins pro Woche in den ersten 3 Monaten, danach 3-5/Woche.

**Tool:** Pinterest Business Account + ggf. Tailwind für Scheduling.

**KPI:** 10k Monthly Viewers bis Q4 2026, 50k bis Q2 2027. **Wichtig:** Pinterest-Traffic gilt nicht als Backlink-Signal, aber als Brand-Search-Treiber.

**Anti-Pattern:** Keine Trauer-Pins mit dramatischen Bildern. Keine Schockbilder. Keine "10 Sätze die jeden Trauernden trösten"-Clickbait. Pietät-Gate gilt auch hier.

### M.3 — Kronjuwelen (3 Assets, die unverhältnismäßig viel ziehen sollen)

**Definition:** Drei Seiten/Tools, in die überproportional viel Energie fließt, weil sie maximale Backlinks, Brand-Searches und Empfehlungen generieren sollen.

#### Kronjuwel 1 — Akutfall-Hauptseite "Erste 24 Stunden" (`/erste-24-stunden`)

**Warum:** Höchster emotionaler Hebel + höchste Empfehlungsrate. Wer in akuter Krise echte Hilfe bekommt, empfiehlt das radikal. Gleichzeitig: SERP-Lücke zwischen Bestatter-Verkaufsseiten und trockenen Behörden-PDFs.

**Standard:** *Der* deutsche Notfall-Guide. 3.000+ Wörter, mit allen Bundesland-Frist-Unterschieden, Quellen aus Bestattungsgesetzen, eingebettetem PDF-Download für Akutsituationen, Audio-Version für Menschen die in Schock nicht lesen können (in Phase E).

**Backlink-Hooks:**
- PDF "Erste-24-Stunden-Checkliste" zum Drucken (Verbraucherzentrale, Hospize verlinken)
- Audio-Version (Barrierefreiheit, Verbände verlinken)
- Datenstory: "Bestattungsfristen pro Bundesland" als Tabelle (Medien zitieren)

**KPI:** Top-3 für "was tun wenn jemand stirbt" und "todesfall checkliste" bis Q4 2026.

#### Kronjuwel 2 — Bestattungskosten-Rechner mit echter regionaler Datenbank

**Warum:** Kostenrechner sind das meistverlinkte Tool-Format in der Bestattungsbranche. Die existierenden sind alle generisch oder Bestatter-getrieben. Wenn machsruhig **echte regionale Friedhofsgebühren** in einer Datenbank hat (50 Städte als Anfang), wird das Tool zur Standard-Referenz.

**Standard:** Eingabe (Stadt, Bestattungsart, Sarg/Urne, Zeremoniewunsch) → Aufschlüsselung nach Posten mit echten Zahlen aus der Stadt-Datenbank. **Datenbank ist der Moat.**

**Backlink-Hooks:**
- "Bestattungskosten-Rechner machsruhig.de" als verlinkbares Tool (Lokalzeitungen, Verbraucherportale)
- Quartals-Studie "Wo ist Bestatten am teuersten/günstigsten?" mit Daten aus der Datenbank (PR-Anlass)
- Embed-Code für Bestatterkammer-Websites (langfristig)

**KPI:** Top-3 für "bestattungskosten rechner" bis Q1 2027.

#### Kronjuwel 3 — Trauerrede-Generator (KI-gestützt, mit Pietät-Gate)

**Warum:** Trauerreden sind eine massive Schmerz-Suchanfrage ("trauerrede vorlage", "rede beerdigung"). Existierende Tools sind generisch oder schlechte KI-Outputs. Mit Pietät-Gate-Validierung und thematischer Personalisierung (Beziehung zum Verstorbenen, kurze Erinnerung, Charakter) wird das ein Tool, das Menschen nach dem Nutzen *teilen*.

**Standard:** Chat-artige Eingabe ("Wer war diese Person für Sie?" → 3-4 Folgefragen) → fertige Rede in 2 Stilen (formal/persönlich), Export als PDF/Text/WhatsApp-Share-Karte.

**Backlink-Hooks:**
- WhatsApp-Share-Karte: "Ich habe meine Trauerrede mit machsruhig erstellt" (organische Social-Verbreitung)
- Hospize, Trauerbegleiter empfehlen das Tool
- Bestatter empfehlen es Angehörigen (selbst wenn sie eigene Bestatter-Reden haben)

**KPI:** 1000 Tool-Nutzungen pro Monat bis Q1 2027.

**Wichtig:** Pietät-Gate 7 ist hier **harter Blocker** — Output muss durch Pietät-Filter, der Floskeln und Trivialisierungen rauswirft.

### M.4 — Markt-KPIs (zusätzlich zu Build-KPIs)

**Build-KPIs** (bereits in Backlog) misst Code-Qualität. **Markt-KPIs** misst tatsächliche Marktposition.

| KPI | Q3 2026 | Q4 2026 | Q2 2027 | Q4 2027 |
|---|---:|---:|---:|---:|
| Organischer Traffic / Monat | 5k | 15k | 50k | 150k |
| Top-3-Rankings (Kern-Keywords) | 5 | 15 | 40 | 100 |
| Top-10-Rankings | 25 | 60 | 150 | 300 |
| Referring Domains | 10 | 25 | 60 | 150 |
| Domain Rating (Ahrefs) | DR 8 | DR 15 | DR 25 | DR 35 |
| Brand Search / Monat | 50 | 200 | 1.000 | 5.000 |
| Newsletter-Subscriber | 100 | 500 | 2.000 | 8.000 |
| Pinterest Monthly Viewers | 1k | 10k | 50k | 200k |
| Affiliate-Umsatz / Monat | — | — | 2.000 € | 12.000 € |
| Lead-Conversions / Monat | — | — | 50 | 300 |

**Tracking-Setup:**
- Google Search Console (kostenlos)
- Ahrefs Lite oder Ubersuggest für Backlinks und Domain Rating
- Plausible Analytics (DSGVO, bereits installiert)
- ConvertKit/Mailerlite für Newsletter-KPIs
- Pinterest Business Analytics (kostenlos)

**Cadence:** Quartalsweise Review im SESSION-NOTES.md, OKR-Anpassung wenn Werte 30%+ unter Ziel.

**Definition Markt-Erfolg (Q4 2027):**
- 150k organische Visits/Monat = Top-3 unter den DACH-Bestattungs-Info-Portalen (geschätzt nach SimilarWeb-Vergleichen)
- 100+ Top-3-Rankings = thematische Autorität für YMYL-Bestattung in DE

### M.5 — Moats (was wird monatlich uneinholbarer)

Moats sind die Aktiva, die mit jedem Monat schwerer kopierbar werden. Aktuell hat machsruhig **null harte Moats**. Diese sind aufzubauen:

| Moat | Wie aufbauen | Ab Phase | Schwer kopierbar weil |
|---|---|---|---|
| **Friedhofsgebühren-Datenbank** | Pro Stadt-Aufrüstung in Phase E die offiziellen Gebühren-Daten kuratieren, in strukturierter DB ablegen | E | Wettbewerber müsste 50+ Städte einzeln recherchieren |
| **Newsletter-Liste** | Lead-Magnets aus Phase B+C, Begleitformate aus C.5 | B fortlaufend | Vertrauensbasis ist nicht mit Geld kaufbar |
| **Reviewer-Fachpool** | Bestatter, Juristen, Trauerbegleiter aus Outreach (M.1) für Reviews gewinnen, mit Names sichtbar machen | B fortlaufend | Persönliche Beziehungen, schwer abzuwerben |
| **Bundesland-Recht-Wissen** | Aus Phase C.3 strukturierte Datenbank zu Bestattungsfristen, Sargpflicht, Aschestreuung etc. pro Bundesland | C.3 | Gesetze ändern sich ständig, Pflege-Aufwand schreckt Kopisten ab |
| **Tool-Nutzungssignale** | Anonymisierte Aggregat-Daten ("Was rechnen User in Stadt X für Bestattung aus?") zur Content-Verbesserung | C.7 | Datennetzwerk-Effekt: je mehr Nutzer, desto besser die Aggregate |
| **Saisonaler Trauer-Content (C.5)** | Allerheiligen, Totensonntag, Weihnachten etc. — jährlich gepflegt, Backlinks akkumulieren | C.5 | Pinterest- und Backlink-Stock ist erst nach Jahren skalierbar |
| **Brand-Stärke "machsruhig"** | Konsequente Tonalität, kein Push, Empfehlung durch Hospize/Bestatter | A-F | Brand-Building ist Jahre-Investment, nicht Monate |
| **YMYL-Compliance-History** | Konsequente Quality-Gates über Jahre = Google-Vertrauen | A fortlaufend | Trust ist linear-zeitabhängig, nicht beschleunigbar |

**Strategische Konsequenz:** Moats sind das, was Wettbewerber mit 500k Euro **nicht** kopieren können. Du baust sie unbewusst durch konsequente Phase-A-bis-F-Umsetzung — aber wenn du sie **bewusst** aufbaust (z.B. Datenbank von Anfang an strukturiert, nicht nur in HTML), wird Phase F um Faktoren wertvoller.

**Update 18.06.2026:** Friedhofsgebühren-DB + Tool-Nutzungssignale (Datennetzwerk-Effekt) + Kronjuwel-2-Datenbank sind in der **Datentransparenz-Strategie (Abschnitt 15)** zu *einer* tragenden Säule vereint — „Datenbank von Anfang an strukturiert" wird dort zum *maschinenlesbaren Angebotsstandard*.

---

## Datentransparenz-Strategie (strategische Hauptsäule, ab 18.06.2026)

> Detail-Konzept mit operativer Tiefe: `_dev/strategie/transparenz-partner-konzept.md` (v5).
> Diese Sektion ist die strategische Einordnung in den Gesamtplan.

**Die These.** machsruhig wird **der Transparenzstandard für Bestatter-Angebote** — nicht das größte Verzeichnis, nicht der billigste Vergleich, sondern der Ort, an dem Angehörige verstehen, ob ein Angebot nachvollziehbar aufgebaut ist, und an dem transparente Bestatter sichtbar werden. **Leitsatz: belohnt nicht den günstigsten Bestatter, sondern den verständlichsten.** Geprüft wird Transparenz der Darstellung, **nicht das Preisniveau**.

**Warum das die Evolution dieses Papiers ist, kein Fremdkörper.** Es vereint drei bereits angelegte Fäden zu einer zentralen Säule: Kronjuwel 2 (Kostenrechner mit echter Datenbank — „Datenbank ist der Moat"), M.5 Friedhofsgebühren-Datenbank und M.5 Tool-Nutzungssignale (Datennetzwerk-Effekt). Aus „ein Moat unter vielen" wird die tragende Geschäfts- und Autoritätssäule.

**Nordstern (Aufnahme-Kriterium für jeden Baustein):** muss *gleichzeitig* erzeugen — **Vertrauen** (Nutzer) · **Daten** (uns) · **Beziehung** (Bestatter) · **SEO/PR**.

**Das Rückgrat — EIN Schema, drei Oberflächen (nur diese drei Namen):**
1. **machsruhig Angebotsstandard** — freiwillige, *maschinenlesbare* Definition, wie ein verständliches Bestatter-Angebot aufgebaut ist (15 Posten, deckungsgleich mit dem Kostenmodell); als offene Spezifikation + Eingabe-Formular. *Das Fundament und der eigentliche Moat: wer Angebote in unserem Format ausgibt, dessen Schienen besitzen wir.*
2. **machsruhig Transparenz Partner** — wer nach dem Standard offenlegt, bekommt ein öffentliches Transparenzprofil. Start als *Selbstverpflichtung* (nicht „Siegel" — UWG/BGH-Risiko), binäre objektive Kriterien, kostenlos, neutral. Prominent: „Was NICHT geprüft wird" (keine Qualitätsbewertung).
3. **machsruhig Kostenradar** — aggregierte, anonymisierte Preisspannen pro Stadt + seriöser Jahresreport (PR-Arm). Streng gated bis genug Daten da sind. Die jährliche Partner-Bestätigung = longitudinale Echtpreis-Zeitreihe (granular — was Aeternitas/Destatis-Makrotrends nicht haben).

**Geschäftsmodell — beides, transparent.** machsruhig ist Transparenz-Plattform UND Lead-Vermittler. Das Gift war nie Lead-Gen, sondern *intransparentes Pay-to-Rank*. Drei gesunde Erlöslinien:
- **Transparente Lead-Vermittlung (Kern):** Bestatter zahlen für **Zugang** zum Lead-Pool, **nicht für Rang**; Auswahl nach neutralen, offengelegten Kriterien; für den Nutzer als Vermittlung erkennbar; nur Transparenz Partner im Pool. **Partner-Status = Eintrittskarte für Leads** → Transparenz wird Geschäfts-Anreiz statt Bitte (löst „warum sollte ein Bestatter mitmachen?").
- **B2B-Markt-Reports** (anonymisiert/aggregiert) — skalierte zweite Linie (Bestatter, Versicherer); Zeitreihe wird jährlich wertvoller.
- **Optionale Bestatter-Komfort-Tools** — Ranking bleibt neutral.

Vier Trust-Regeln tragen das „beides": (a) als Vermittlung erkennbar; (b) Zahlung kauft Zugang, nicht Rang; (c) nur Partner im Pool; (d) **redaktionelle Mauer** zwischen Kostenradar/Benchmark und Lead-Geschäft. **Genau diese Mauer können die Pay-to-Rank-Incumbents nicht ziehen — das ist der USP.** Trust ist hier Profit-Center, nicht Kostenstelle.

**Einordnung ins Phasenmodell (Leitplanke „Authority vor Leadgen" bleibt gültig).** *Standard + offene Spec* (keine PII, kein Backend, keine Rechtshürde) sind sofort baubar und zahlen auf die **Authority-Phase** ein (Original-Daten/Spec = Backlink-Magnet → adressiert das Cold-Start-Indexierungsproblem). Die **Lead-Aktivierung** bleibt an Phase F + anwaltliche Prüfung gebunden (Leitplanke 7). Reihenfolge: Standard → reibungsloses Onboarding → **Hamburg-Pilot** (Funnel 30→10→5→3→1) → Radar/Reports. Regel: **erst der Brunnen, dann die Wasserhähne** (keine leeren Dashboards vor Daten).

**Wettbewerb (Ergänzung zur Tabelle in Abschnitt 10).** Lead-Gen-Vergleichsportale (bestatter-preisvergleich.de: 18 J., ~131k Angebote) haben mehr Rohdaten, aber **kein Benchmark** — ihr Pay-to-Rank-Modell verbietet ehrliche Transparenz (Innovator's Dilemma). Online-Bestatter (mymoria/Emmora–Ahorn) verkaufen eigene Preise. Aeternitas besitzt nur Makro-Trends. Der granulare, posten-/regions-scharfe Trust-First-Benchmark ist **frei** — der Moat ist Geschäftsmodell/Positionierung + Tempo, **nicht** Datenvolumen.

**Trust-Leitplanken (nicht verhandelbar):** Status nicht käuflich; keine Nutzerdaten-Verkäufe, nie personenbezogene Sterbefalldaten (DSGVO: Anbieter-Preise = Geschäftsdaten = der einfache Strom, zuerst angehen); Kriterien/Vergabeprozess/Finanzierung öffentlich; vor großer Kommunikation **anwaltliche Prüfung** (UWG/Prüfzeichen).

**Bewusst außerhalb dieser Säule** (Detail im Konzept-Doc): Consumer-Tool-Features (Fragenliste, Auftrag-Check, „Angebot des Monats") → allgemeine Tool-/Content-Roadmap; spätere Stufen (Transparenz-Karte, Anbieter-Cockpit) erst ab Partner-Masse; **abgelehnt:** Transparenz-Score (Qualitätsurteil-Tabu → bleibt binär), Verbands-Co-Creation der Kriterien (Capture-Risiko).

**Status-Nachtrag 13.07.2026 — der „Brunnen" ist real.** Das Friedhofsgebühren-Register hat den vollen Härtetest hinter sich: ein systematischer Einheiten-Fehler (Einzelstelle ≠ Einzelbelegung; „teuerste Stadt Mainz 4.714 €" war falsch → korrekt Reihengrab 2.507 €) wurde gefunden, alle **50 Städte einzeln reviewt und 49 primär gegen die amtliche Satzung gepinnt** (nur Kiel wartet auf manuellen Satzungs-Abruf). Die per-Stadt-Boxen sind mit Einheit-B-Labels, Pflicht-Zusatzgebühren (13 Städte) und USt-Kennzeichnung regeneriert (Branch, vor Deploy). Konsequenzen: (a) die Datenbasis ist **studien- und partnerfest** — die Ko-Autor-Ansprache (M.1/Spur A) kann sich auf primär-verifizierte Daten stützen; (b) Lehre fürs Datenmodell: **jährliche Unterhaltungs-/Grundgebühren sind der größte blinde Fleck** von 2-Komponenten-Preismodellen — der Angebotsstandard (Oberfläche 1) muss solche Pflicht-Nebenposten als eigenes Feld führen; (c) Erhebungs-Playbook etabliert (Koordinaten-Extraktion, Primär-Pinning, Einzel-Review-Gate) → wiederverwendbar für den Kostenradar. Operativer Stand: `_dev/strategie/FAHRPLAN.md`.

---

## Verweise

- **Operative Tickets:** [BACKLOG.md](./BACKLOG.md)
- **Session-Gedächtnis:** [SESSION-NOTES.md](./SESSION-NOTES.md)
- **Audit-Tools:** `_dev/audit-all-pages.py`, `_dev/stadt-quality-analysis.py`
- **Audit-Reports:** `_dev/AUDIT-REPORT.json`, `_dev/stadt-quality.json`
- **Strategie-Quellmaterial (Archiv):** `_dev/archiv/`
