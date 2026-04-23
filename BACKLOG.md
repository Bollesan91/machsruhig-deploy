# machsruhig.de — BACKLOG (Operativer Masterplan)

> **Operative Tickets** — strategische Grundlagen siehe [STRATEGIE.md](./STRATEGIE.md), Session-Gedächtnis siehe [SESSION-NOTES.md](./SESSION-NOTES.md).
>
> Dieser Plan integriert drei Audits:
> 1. **Internes Vollaudit** (`_dev/audit-all-pages.py`, 714 Zeilen, 98 Seiten, 9 Kategorien, Ø 59.0/100)
> 2. **Substanzanalyse Stadtseiten** (`_dev/stadt-quality-analysis.py`, Tier-Klassifizierung GOLD/SILVER/BRONZE/GENERIC)
> 3. **Externes strategisches Audit** (6,6/10, Schwerpunkt E-E-A-T, Authority vor Leadgen)
>
> Stand: 23. April 2026

---

## Inhalt

0. [🚀 7-Tage-Sprint (ab 24.04.2026)](#-7-tage-sprint-ab-24042026)
1. [Strategische Leitplanken](#strategische-leitplanken)
2. [Status Quo](#status-quo)
3. [Phasen-Roadmap](#phasen-roadmap)
4. [Phase A — Deploy-Blocker entschärfen (AKUT)](#phase-a--deploy-blocker-entschärfen-akut)
5. [Phase B — Trust-Layer sitewide](#phase-b--trust-layer-sitewide)
6. [Phase C — Authority-Content Cluster](#phase-c--authority-content-cluster)
   - C.1 Akutfall · C.2 Kosten · C.3 Recht (Bundesländer) · C.4 Entscheidung
   - C.5 Trauer · C.6 Bürokratie · C.7 Neue Tools · C.8 Vorsorge-Detail
7. [Phase D — Strukturelle SEO-Fixes](#phase-d--strukturelle-seo-fixes)
8. [Phase E — Top-10-Städte auf Gold-Niveau](#phase-e--top-10-städte-auf-gold-niveau)
9. [Phase F — Monetarisierung aktivieren](#phase-f--monetarisierung-aktivieren)
10. [Quality-Gates (vor jedem Go-Live)](#quality-gates-vor-jedem-go-live)
11. [Anti-Patterns](#anti-patterns)
12. [Offene Entscheidungen](#offene-entscheidungen)
13. [Metriken & Akzeptanzkriterien](#metriken--akzeptanzkriterien)
14. [Ticket-Übersicht (komplett)](#ticket-übersicht-komplett)

---

## 🚀 7-Tage-Sprint (ab 24.04.2026)

> Aus Strategie wird Umsetzung. Schluss mit Planen. Diese 5 Tickets sind die Reihenfolge der nächsten 7 Arbeitstage. Klar abgegrenzt von langfristiger Backlog-Pflege.

**Wochenkapazität:** 6-8h (Entscheidung 3 in STRATEGIE.md). Sprint umfasst 5 Tickets mit ~12-18h Aufwand → realistisch in 7 Arbeitstagen, mit Puffer für Pannen und Reviews.

**Reihenfolge ist nicht verhandelbar.** Jedes Ticket entblockiert das nächste.

| # | Ticket | Aufwand | Akzeptanz |
|---:|---|---:|---|
| 1 | **Homepage statisch neu bauen** (A.1) | 4-6h | Audit-Score ≥75, kein @babel/standalone, Lighthouse ≥90, `<main>` sichtbar im View-Source |
| 2 | **5 Gold-Städte statisch ausliefern** (A.2) — **STAGE 1 DONE (23.04.)** | 10-15h | Stage 1 ✅: Score 75, kein JSX-Leak, für Google sichtbar. Stage 2 (Score ≥85 + FuneralHome-Schema) → Ticket **D.2.1** |
| 3 | **Über-uns-Seite live** (B.1) | 3-4h | Haltung sichtbar, Reviewer-Pool-Erwähnung, verlinkt von Homepage + Methodik |
| 4 | **Autorenblock + Methodik-Verlinkung sitewide** (B.2 + B.3) | 4h | "Redaktion machsruhig.de" + "Fachlich geprüft von" auf allen YMYL-Seiten, Methodik-Link prominent |
| 5 | **Akutfall-Hauptseite "Erste 24 Stunden"** (C.1.1) | 6-8h | 2.000+ Wörter, 5+ Gesetzes-Paragrafen, 3+ Quellen, Audit-Score ≥90, Pietät-Gate bestanden |

**Definition Sprint-Ende:**
- Homepage und 5 Gold-Städte sehen für Google nicht mehr aus wie leere SPAs
- Trust-Layer ist sitewide sichtbar
- Erste echte Authority-Seite (Akutfall-Hauptseite) ist Beweis für YMYL-Standard
- Audit-Gesamtscore steigt von 59.0 auf ≥70 (Schätzung)

**Was im Sprint NICHT gemacht wird** (sonst Verzettelung):
- Keine neuen Tools
- Keine weiteren Stadtseiten aufrüsten
- Keine Bundeslandseiten
- Keine Trauer-Cluster-Seiten (außer wenn vor Allerheiligen-Deadline reaktiviert wird)
- Keine Affiliate-Anträge
- Keine Distribution-Kanäle aufsetzen (Newsletter, Pinterest = Phase D-E)
- Keine STRATEGIE.md-Änderungen

**Nach dem Sprint:** Status-Review in SESSION-NOTES.md, dann Übergang zu Phase A.3 (Tool-Static-Shells) und Phase B.4-B.5 (Disclaimer + Stand-Templates).

---

---

## Strategische Leitplanken

Diese Regeln gelten über alle Phasen hinweg. Verstoß = Qualitätsschaden.

1. **Authority vor Leadgen.** Erst Domain-Autorität, dann Monetarisierung aktivieren. Nicht umgekehrt.
2. **Keine weiteren Generic-Template-Seiten.** Jede neue Seite muss Substanz-Kriterien erfüllen (siehe Gold-Template).
3. **YMYL-Standard gilt immer.** Jede Seite mit Gesundheits-/Rechts-/Finanzaussagen braucht: Autor sichtbar, Stand, Quellen, Disclaimer.
4. **Keine CSR-Experimente mehr bei Content-Seiten.** Tools dürfen clientseitig rendern, aber Content-Seiten (= alles was ranken soll) serverseitig/statisch.
5. **Reversibilität bewahren.** `noindex` statt löschen. Änderungen dokumentiert (HTML-Kommentare mit Datum).
6. **Keine Bestatter-Leadgen bauen, bis Authority steht.** Lead-Formulare, Vermittlungs-Funnel etc. bleiben liegen bis Phase F.

---

## Status Quo

### Score-Matrix (98 Seiten)

| Kategorie | Anzahl | Ø Score | Haupt-Problem |
|---|---:|---:|---|
| legal | 4 | 76.2 | (uncritical, eine Seite ohne Canonical) |
| hub | 2 | 66.5 | Affiliate-Integration fehlt (soll so sein, Phase F) |
| vorsorge | 8 | 65.9 | Affiliate-Integration fehlt (Phase F) |
| content | 7 | 64.0 | Schema-Typ-Upgrade |
| bundesland | 16 | 59.4 | Content dünn (373–518 Wörter, Ziel 400–1000) |
| stadt | 50 | 58.8 | 45 Generic-Seiten (noindex), kein LocalBusiness-Schema |
| tool | 6 | 49.7 | CSR-Problem: Google sieht kein H1, keinen Content |
| homepage | 1 | 39.0 | **CSR-Problem auf der Startseite — kritisch** |
| tool-content | 4 | 36.0 | CSR-Problem |

### Die 9 Deploy-Blocker

Seiten, bei denen **Google kein H1 und keinen Content sieht**, weil @babel/standalone clientseitig JSX kompiliert:

1. `index.html` (Homepage, Score 39) — **AKUTESTER FALL**
2. `bestatter/berlin/` (Score 40)
3. `bestatter/frankfurt/` (Score 40)
4. `bestatter/hamburg/` (Score 40)
5. `bestatter/koeln/` (Score 40)
6. `bestatter/muenchen/` (Score 40)
7. `tools/bestattungskosten-rechner/` (Score 40)
8. `tools/danksagung/` (Score 35)
9. `tools/trauerrede/` (Score 40)

**Bemerkenswert:** Die 5 GOLD-Städte (die inhaltlich Gold sind laut Substanzanalyse) werden von Google trotzdem schlecht bewertet, weil der gesamte Gold-Content clientseitig gerendert wird. Das erklärt, warum das externe Audit gesagt hat "München ist knapp am Ziel": Inhalt passt, aber SEO-Sichtbarkeit ist lückenhaft.

### Die Substanz-Realität der Stadtseiten

Aus `stadt-quality.json`:

- **GOLD (5):** Berlin, Frankfurt, Hamburg, Köln, München — 7–9 Friedhofseigennamen, 15–31 Euro-Beträge, 0–1 Floskeln
- **GENERIC (45):** alle exakt 349 Wörter, 3 Friedhofserwähnungen, 0 Euro-Beträge, 4 identische Floskeln — Copy-Paste aus einem Template
- **SILVER/BRONZE:** keine

**→ Schritt A bereits erledigt:** 45 Generic-Städte auf `noindex,follow` gesetzt.

---

## Phasen-Roadmap

```
PHASE A  [AKUT, 1 Session]    Deploy-Blocker entschärfen + Homepage fixen
   ↓
PHASE B  [2 Wochen, parallel] Trust-Layer einziehen (Autor, Methodik, Über uns)
   ↓
PHASE C  [4–6 Wochen]         Authority-Content: Akutfall → Kosten → Recht → Entscheidung
   ↓
PHASE D  [laufend]            Strukturelle SEO-Fixes (OG-Image, Schema, interne Links)
   ↓
PHASE E  [2–4 Wochen]         5 weitere Städte auf Gold-Niveau heben (Top 10 gesamt)
   ↓
PHASE F  [erst wenn A-E solide] Monetarisierung aktivieren, Lead-Funnel, Affiliate
```

**Parallelität:** B und D laufen parallel zu C, weil sie unabhängig sind.

---

## Phase A — Deploy-Blocker entschärfen (AKUT)

**Ziel:** Google muss auf Startseite und den 5 Gold-Städten H1, Content und Struktur sehen können. Derzeit sieht Google bei der Startseite **nur 101 Wörter statischen Text** — alles andere ist React/Babel-Standalone.

### A.1 — Homepage aus CSR-Hölle retten (Score 39 → 75+)

**Problem:**
- `index.html` nutzt `@babel/standalone` mit 29 JSX-Leaks
- Google sieht: 101 Wörter, 1 H1, 1 H2, 3 interne Links, kein Schema, kein `<main>`
- Ziel wäre: ≥600 Wörter, ≥10 interne Links, Schema (`Organization`, `WebSite`), `<main>`-Landmark

**Lösung:**

Statisches HTML-Rewrite der Homepage. Kein React auf der Startseite — ein Nutzer der nach "Bestattung planen" sucht landet auf einer Seite, die Google lesen kann und die in der ersten Sekunde sichtbar ist.

**Pflicht-Bausteine:**

1. **H1 statisch:** "Machs ruhig — Orientierung bei Todesfall, Bestattung und Vorsorge"
2. **H2-Struktur (4–6 Blöcke):**
    - "Im Todesfall — was jetzt zu tun ist" (→ Akutfall-Cluster)
    - "Bestattung planen — Kosten und Ablauf" (→ Kosten-Cluster)
    - "Vorsorge regeln" (→ Vorsorge-Cluster)
    - "Bestatter in deiner Stadt" (→ Gold-Städte)
    - "Kondolieren und trauern" (→ Content-Cluster)
3. **≥10 interne Links** auf Haupt-Cluster-Seiten
4. **Schema.org:** `Organization` + `WebSite` + `SiteNavigationElement`
5. **`<main>`-Landmark** sichtbar im HTML
6. **Über-uns-Teaser** (Trust-Layer-Vorschau)
7. **Keine Monetarisierungs-CTAs** — nur Orientierung (gemäß externem Audit)

**Akzeptanzkriterien:**
- Audit-Score ≥75
- Keine Babel-Standalone-Nutzung
- Kein JSX-Leak
- Lighthouse Performance ≥90
- `<main>` sichtbar im View-Source

**Aufwand:** 4–6h

---

### A.2 — 5 Gold-Städte statisch rendern (Score 40 → 85+)

**Problem:** Berlin, Frankfurt, Hamburg, Köln, München sind **inhaltlich** Gold (siehe Substanzanalyse: 7–9 Friedhöfe, 15–31 Euro-Beträge pro Seite), aber werden clientseitig gerendert. Google sieht fast nichts.

**Lösung:**

Den bereits existierenden Gold-Content **statisch** ausliefern. Entweder:

- **Option A (schnell):** Build-Script, das den React-Output einmal rendert und als statisches HTML speichert (Pre-Rendering)
- **Option B (sauber):** React durch statisches HTML ersetzen, interaktive Elemente (z.B. FAQ-Akkordeon) als Progressive Enhancement

**Empfehlung:** Option B für alle Content-Seiten, Option A nur wenn B zu aufwändig.

**Pflicht-Bausteine pro Stadt (bereits im Content vorhanden, nur statisch rendern):**
- H1 "Bestatter in [Stadt]"
- Einleitung mit konkreten Friedhofsnamen
- Kostentabelle (Erd-/Urnen-/Baum-Bestattung)
- Friedhofs-Übersicht mit Eigennamen und Details
- Bundesland-Rechtsbezug
- FAQ-Sektion
- **NEU:** Schema.org `FuneralHome` oder `LocalBusiness` — die fehlt aktuell!

**Aufwand:** 2–3h pro Stadt, parallelisierbar. Gesamt: 10–15h für alle 5.

**Status (23.04.2026):** Stage 1 abgeschlossen. React + `@babel/standalone` entfernt, statisches HTML mit H1, Content, Kostentabellen, Friedhofs-Übersicht, FAQ, Mobile-Nav als Vanilla-JS, OG-Image als PNG. **Audit-Score pro Stadt: 75.** Für Google vollständig sichtbar.

**Offen (Stage 2, verschoben nach D.2.1):** FuneralHome/LocalBusiness-Schema, H2-Count-Optimierung, Monetarisierungs-Warning (nachdem Lead-Form in Phase F zurückkommt). Ziel: Score ≥85 pro Stadt.

---

### A.3 — Tool-Seiten: Static Shell + Interactive Widget

**Problem:** 9 Tool-Seiten (Score 33–57), alle mit `@babel/standalone`, keine H1, keine H2, Google sieht praktisch nichts. Aus dem externen Audit: "Indexierte Kommt-bald-Seiten sind Ballast."

**Lösung:**

Zweischichtiger Ansatz pro Tool:

1. **Static Shell (SEO-Layer):** H1, Intro-Text (200–400 Wörter), Methodik-Erklärung, Use-Cases, FAQ — alles statisches HTML
2. **Interactive Widget:** Das Tool selbst bleibt React/JSX, aber in einem klar begrenzten `<div id="widget">`

**Pflicht-Bausteine für die Shell:**
- H1 passend zum Tool
- 2–3 H2 (Wie funktioniert das Tool / Wofür / Datenschutz-Hinweis)
- Mindestens 200 Wörter statischer Content
- Schema.org `WebApplication` + `HowTo`
- Links zu verwandten Content-Cluster-Seiten

**Priorität:**
1. `tools/bestattungskosten-rechner/` — wichtigster Entry für Kosten-Suchanfragen
2. `tools/checkliste-todesfall/` — wichtigster Entry für Akutfall
3. `tools/vorsorge-check/` — Vorsorge-Entry
4. Rest nach Bedarf

**Aufwand:** 2–3h pro Tool. 9 Tools = 18–27h.

---

### A.4 — build-Script für Pre-Rendering (optional, aber hilfreich)

Wenn Option A aus A.2 gewählt wird: ein kleines Node-Script, das nach `npm run build` alle React-Komponenten einmal rendert und das Output-HTML speichert. Dadurch wäre das Prerendering automatisch bei jedem Deploy.

**Aufwand:** 3–4h einmalig, spart später viel.

---

## Phase B — Trust-Layer sitewide

**Zeithorizont:** 2 Wochen, parallel zu A und C.

**Warum wichtig:** Das externe Audit hat gesagt: "Fehlende sichtbare Verantwortlichkeit ist bei YMYL-Themen kein Nice-to-have, sondern SEO-Infrastruktur." Bestattung ist YMYL-Kern — ohne Trust-Layer wird jede Content-Arbeit unter Potenzial performen.

### B.1 — "Über uns"-Seite mit Haltung

**Anti-Pattern:** "Wir sind ein Team aus Experten" — das ist Corporate-Blabla.

**Gewünscht:**
- Warum gibt es machsruhig? (z.B.: "Weil die Bestattungsbranche intransparent ist und Betroffene in emotionalen Ausnahmesituationen Orientierung statt Verkaufsdruck brauchen.")
- Wer steht dahinter? (Realperson oder Redaktions-Team mit klarer Verantwortungsstruktur)
- Wie finanziert sich machsruhig? (Ehrlich: Affiliate-Modell, keine Bestatter-Vergütung für Empfehlungen — oder was auch immer die Wahrheit wird in Phase F)
- Was ist die redaktionelle Linie? (Neutral, faktenbasiert, quellengestützt)
- Abgrenzung zu klassischen Bestatter-Portalen / Vergleichsseiten

**URL:** `/ueber-uns` (neu)

**Aufwand:** 3h Text + 1h Bau

**Status (23.04.2026):** Sprint #3 umgesetzt. `ueber-uns.html` live, 1050 Wörter, Score 75, AboutPage+Organization-Schema, Fachpool-Rollen als "im Aufbau" transparent gekennzeichnet, verlinkt von Homepage + Methodik + Sitemap.

**Nachschärfung bei Traffic (B.1.1 — kein akuter Handlungsbedarf):** Die Seite ist solide, hat aber bekannte Qualitätspunkte, die erst bei relevantem Traffic gefixt werden:
- Redundanz zur Methodik-Seite (~40% Überlapp bei Haltung + Finanzierung) — kürzen und auf Methodik verweisen
- Title/H1 schärfen ("Über uns" → "Über machsruhig — unabhängiges Portal für Vorsorge und Bestattung") — löst auch das Audit-Issue "H1/Title keine Keyword-Überlappung"
- Fachpool-Cards: Aufbau-Status VOR die Rollen-Karten ziehen, nicht darunter als small-print
- Konkurrenz-Abgrenzung mit konkreten Namen/Belegen unterfüttern, statt abstrakter Behauptungen
- Eigene Fachpool-Kontaktadresse statt nur Impressum-Verweis
- Floskel-Diät: "Unser Leitsatz"/"Unser Versprechen"/"Wir helfen dir" runterdrehen

**Trigger für Nachschärfung:** Sobald die Seite >50 Besuche/Monat hat oder Phase D/E relevante Referenz-Qualität verlangt.

---

### B.2 — Autoren-/Redaktions-System

**Die unbeantwortete Frage aus der Vorsession:** Wer schreibt unter Klarnamen?

**Optionen:**

**Option 1 — Einzelner Klarname (stärkstes E-E-A-T-Signal):**
- Du selbst als Autor, ggf. mit Bestatter-Netzwerk / Fachberater als Reviewer
- Erfordert: LinkedIn/Xing-Profil verknüpft, evt. Foto, Kurz-Bio
- Nachteil: Personenbindung, rechtliche Angreifbarkeit höher

**Option 2 — Redaktions-Pseudonym mit klarer Struktur:**
- "machsruhig Redaktion" als Autor, aber mit namentlich genannten Reviewern (z.B. Bestatter, Jurist, Seelsorger — Kontakte aufbauen)
- Vorteile: Skalierbar, weniger persönlich exposiert
- Nachteile: Schwächeres E-E-A-T-Signal als echter Einzelautor

**Option 3 — Hybridmodell:**
- Einzelautor "Redakteur: [Name]" pro Artikel, Reviewer aus Fachpool
- Artikel können von Fachleuten geprüft sein (mit Namensnennung)
- Stärkstes Signal, aber aufwändiger

**Pflicht-Elemente unabhängig von der Option:**

Auf jeder YMYL-Seite ein sichtbarer Autoren-Block:

```html
<div class="mr-article-meta">
  <div class="mr-author">
    <img src="/autoren/[slug].jpg" alt="[Name]" />
    <div>
      <strong>[Name]</strong>
      <span>Redaktion machsruhig.de</span>
    </div>
  </div>
  <div class="mr-review">
    Fachlich geprüft von: <a href="/team/[slug]">[Reviewer-Name], [Rolle]</a>
  </div>
  <div class="mr-date">
    Veröffentlicht: [Datum] · Zuletzt geprüft: [Datum]
  </div>
  <a href="/methodik">Wie entstehen unsere Inhalte?</a>
</div>
```

**Plus:**
- `/team` Seite mit Profilen (Kurz-Bio, Qualifikation, ggf. Foto)
- Schema.org `Person` auf jeder Profil-Seite
- Schema.org `author` in `Article`-Schema referenziert die Person-URL

**Entscheidung erforderlich:** Welche Option? (Siehe `Offene Entscheidungen` am Ende)

**Aufwand:** 2h Entscheidung/Aufbau + pro Artikel 5 Min Autor-Block einfügen

---

### B.3 — Methodik prominenter machen

**Status:** `methodik.html` existiert (Score 82), ist aber nur im Footer versteckt verlinkt.

**Aufgaben:**
- Header-Link in Hauptnavigation ergänzen? (Optional, prüfen)
- Auf jeder YMYL-Seite im Autoren-Block direkt verlinken (siehe B.2)
- Methodik-Seite selbst konkretisieren:
  - Quellenhierarchie (Primärquellen → Sekundärquellen)
  - Update-Zyklus (alle 6 Monate, bei Gesetzesänderungen sofort)
  - Unabhängigkeitserklärung
  - Konkret: Welche Gesetze, Behörden, Studien werden zitiert?
  - Konflikt-of-Interest-Statement (falls Affiliate in Phase F aktiv)

**Aufwand:** 2h

---

### B.4 — Einheitlicher Disclaimer-Block

**Problem:** Disclaimer sind über Seiten inkonsistent ("keine Rechtsberatung" — mal ja, mal nein, mal anders formuliert).

**Lösung:** Ein Partial/Include für einheitlichen YMYL-Disclaimer. Standardtext:

> "Die Informationen auf dieser Seite wurden sorgfältig recherchiert, dienen aber ausschließlich der Orientierung und ersetzen im Einzelfall keine Rechts-, Steuer- oder Bestattungsberatung. Bei konkreten rechtlichen Fragen wende dich an einen Fachanwalt oder eine Bestatterkammer."

**Platzierung:**
- Kurz-Version sichtbar am Ende jedes Artikels
- Ausführliche Version in `/methodik`
- Schema.org `disclaimer` property wo möglich

**Aufwand:** 2h Sitewide-Einbau

---

### B.5 — Stand- und Quellen-Konsistenz

**Problem:** "Stand: April 2026" gibt es bei den Gold-Städten, aber nicht einheitlich.

**Ziel:**
- Jede Content-Seite hat oben gut sichtbar: **"Stand: [Monat Jahr]"** oder **"Zuletzt geprüft: [Datum]"**
- Am Ende des Artikels: Quellen-Sektion mit Links zu Primärquellen (Gesetze, offizielle Stellen)
- Mindestens 3 Quellen pro YMYL-Seite

**Aufwand:** 1h Template + laufend bei Content-Arbeit

---

## Phase C — Authority-Content Cluster

**Zeithorizont:** 4–6 Wochen. Reihenfolge nach strategischer Dringlichkeit aus dem externen Audit.

### Cluster C.1 — Akutfall (HÖCHSTE PRIORITÄT)

**Warum zuerst:** Das ist der Entry-Point für Menschen in Krisen. Hier gewinnst oder verlierst du Trust in 10 Sekunden. Gleichzeitig derjenige Punkt, wo das externe Audit mit "Todesfall, was jetzt sofort zu tun ist" ausdrücklich gesagt hat: fehlt auf der Startseite sichtbar.

#### C.1.1 — Hauptseite "Erste 24 Stunden nach dem Tod"

**URL:** `/erste-24-stunden` oder `/todesfall-was-tun`

**Keyword-Targets:**
- "was tun wenn jemand gestorben ist"
- "erste schritte nach todesfall"
- "todesfall checkliste"
- "was tun bei todesfall zu hause"

**Struktur (Content-Gerüst):**

1. **Sofort-Aktionen** (die ersten 2 Stunden)
   - Bei Tod zu Hause: Arzt/Notdienst rufen für Totenschein
   - Bei Tod in Klinik/Pflegeheim: Meist automatisch organisiert
   - Niemanden sofort informieren außer engstem Kreis
   - **Was darf man selbst, was nicht?** Vertraute Handlungen wie Waschen, Umziehen dürfen (siehe § XY BestattG, variiert pro Bundesland)
2. **Totenschein verstehen**
   - Wer stellt ihn aus
   - Warum 1x Original, mehrere Kopien
   - Was steht drin
3. **Bestatter wählen** (aber: nicht übereilen)
   - Drei Kriterien
   - Was ist eine "Abholung" rechtlich
   - Kostenfalle Sofort-Entscheidungen
4. **Standesamt-Anmeldung**
   - Frist (variiert nach Bundesland)
   - Nötige Unterlagen (in eigener Unter-Seite verlinkt)
   - Sterbeurkunden — wie viele bestellen
5. **Die nächsten 24 Stunden — Checkliste**
   - (Cross-Link zu `tools/checkliste-todesfall`)

**Pflicht-Elemente:**
- Mindestens 2.000 Wörter
- 5+ konkrete Gesetzesparagrafen zitiert
- 3+ externe Primärquellen (offizielle Stellen)
- Stand-Angabe, Autor-Block (aus Phase B), Disclaimer
- Schema.org `Article` + `HowTo` + `FAQPage` kombiniert
- 4+ interne Links zu verwandten Cluster-Seiten

**Akzeptanzkriterien:**
- Audit-Score ≥90
- Beim Lesetest: Würde eine Person in Akutsituation das verstehen und Handlungssicherheit gewinnen?
- Keine Floskeln ("Flexible Optionen", "Individuelle Beratung")

**Aufwand:** 6–8h (intensiv Research + Schreiben + Layout)

#### C.1.2 — Entscheidungsbaum "Was ist jetzt sofort zu tun"

**URL:** `/todesfall-situation`

**Konzept:** Interaktiv (oder als verzweigte Statik-Seite), filtert nach Situation:
- Tod zu Hause (erwartet / unerwartet)
- Tod im Krankenhaus
- Tod im Pflegeheim
- Tod im Ausland
- Suizid / Unfall

Jede Situation hat andere erste Schritte (Polizei ja/nein, wer organisiert was, etc.).

**Aufwand:** 4–6h

#### C.1.3 — Unterlagen nach dem Todesfall

**URL:** `/unterlagen-todesfall`

**Content:**
- Komplette Liste aller Dokumente die gebraucht werden
- Sortiert nach: wann gebraucht (sofort / nächste Woche / Monat)
- Wo bekommen (wenn Original verloren)
- Wofür: Standesamt, Rente, Versicherung, Nachlass

**Aufwand:** 4h

#### C.1.4 — Standesamt-Seite

**URL:** `/standesamt-todesfall`

**Content:**
- Anmelde-Pflicht (wer, wann, bis wann)
- Sterbeurkunden: wie viele, wofür, was kosten sie
- Fristen pro Bundesland (Tabelle!)
- Was tun wenn Frist nicht eingehalten werden kann

**Aufwand:** 3h

---

### Cluster C.2 — Kosten

#### C.2.1 — Was kostet eine Erdbestattung wirklich?

**URL:** `/bestattungskosten/erdbestattung` (neu, unter bestehender `/bestattungskosten`)

**Anti-Pattern vermeiden:** "Zwischen X und Y Euro" ohne Kontext.

**Struktur:**
1. Aufgeschlüsselt nach Posten (Bestatter-Grundpreis, Sarg, Friedhofsgebühren, Grabstein, Trauerfeier, Blumenschmuck, Sterbeurkunden, Todesanzeige)
2. Pro Posten: Spanne, Einflussfaktoren, Sparmöglichkeiten
3. Regionale Unterschiede (Bayern teurer als Sachsen, warum)
4. Was ist in Bestatter-Pauschalen drin, was nicht
5. Versteckte Kosten (Grabpflege über 20+ Jahre, Grabsteinwechsel etc.)

**Aufwand:** 5h

#### C.2.2 — Kostenvergleich Bestattungsarten

Tabelle: Erd- vs. Urnen- vs. Baum- vs. See-Bestattung.
Echte Zahlen, bezogen auf die Gold-Städte als Referenz.

**Aufwand:** 3h

#### C.2.3 — Sozialbestattung — wann zahlt das Amt?

**Keyword-Traffic potenziell hoch, wenig Konkurrenz** in der Tiefe.

**Content:**
- § 74 SGB XII im Detail
- Antragsweg, nötige Unterlagen
- Pauschalen pro Bundesland (Übersichts-Tabelle)
- Was ist gedeckt, was nicht
- Was wenn Angehörige "unterhaltsrechtlich verpflichtet" sind aber zahlen sollen
- Schonvermögen bei Erben

**Aufwand:** 4h

#### C.2.4 — Wer zahlt die Beerdigung?

**URL:** `/wer-zahlt-beerdigung`

**Content:**
- Reihenfolge: Erbe → nahe Verwandte → Sozialamt
- Was wenn kein Erbe da ist
- Unterhaltspflichtige Verwandte: wer, wie hoch, Ausnahmen
- Gerichtliche Durchsetzung
- Nachlassverbindlichkeit

**Aufwand:** 3h

#### C.2.5 — Sparoptionen ohne Würdeverlust

- Direktbestattung (was bedeutet das, wo möglich)
- Aussegnung statt Trauerfeier
- Anonymes Grab als Option
- Bestatter-Vergleich (ohne Vergleichsportal sein!)

**Aufwand:** 3h

---

### Cluster C.3 — Recht (Bundesländer fertigstellen)

**Status:** 16 Bundeslandseiten (Ø 59.4 Score, 373–518 Wörter). Ziel: 1000+ Wörter pro Seite, echte rechtliche Tiefe.

**Anti-Pattern-Warnung:** Nicht alle 16 gleichzeitig aufpumpen — das ist der Generic-Fehler nochmal. Reihenfolge: 5 größte Bundesländer (NRW, Bayern, Baden-Württemberg, Niedersachsen, Hessen) zuerst, dann Runde 2.

**Pro Bundesland-Seite:**

1. **Bestattungsgesetz-Überblick** (konkrete Paragrafen-Zitate)
2. **Bestattungsfrist** (z.B. NRW: 4–8 Tage, Bayern: ≤96h nach Totenschein)
3. **Friedhofspflicht ja/nein** (Bremen erlaubt Urnen-Hauptwohnsitz, andere nicht)
4. **Aschestreuung** (wo erlaubt, Ausnahmen)
5. **Sargpflicht** (Ausnahmen für religiöse Gründe)
6. **Sterbegeld** (Sozialhilfe-Richtlinien des Landes)
7. **Tabelle mit Kosten-Beispielen** aus den größten Städten des Bundeslands
8. **Links zu den indexierten Stadt-Seiten** (also: Bayern → München)
9. **Bundesland-spezifische Besonderheiten** (z.B. Seebestattung aus schleswig-holsteinischen Häfen)

**Aufwand pro Bundesland:** 3–4h Research + Schreiben

**Priorität Runde 1 (5 Länder):** NRW, Bayern, BW, Niedersachsen, Hessen → 15–20h
**Priorität Runde 2 (11 Länder):** Rest → 22–33h

---

### Cluster C.4 — Entscheidung

#### C.4.1 — Erd- oder Feuerbestattung?

**Anti-Pattern:** Vor-/Nachteile-Liste.
**Gewünscht:** Entscheidungsleitfaden anhand Lebenssituation:
- Religion / Konfession
- Familien-Wunsch / Individuum-Wunsch
- Örtliche Bindung / keine
- Pflege (wer kümmert sich)
- Kosten (kurz zusammenfassen, Detail in Kosten-Cluster)
- Ökologie (faktenbasiert, nicht ideologisch)

**Aufwand:** 4h

#### C.4.2 — Anonym oder mit Grab?

Trauerpsychologische Dimension ernst nehmen. Studien zu Trauerarbeit zitieren. Entscheidungshilfe ohne Bewertung.

**Aufwand:** 4h

#### C.4.3 — Religion und Bestattung

- Katholisch
- Evangelisch
- Muslimisch
- Jüdisch
- Konfessionslos
- Interreligiös (was wenn Familie uneins)

**Aufwand:** 4h

---

### Cluster C.5 — Trauer (eigener Phase-1-Wachstumshebel)

**Strategischer Hintergrund:** Trauer-Content ist die größte SEO-Goldgrube mit niedrigster Konkurrenz, weil viele Wettbewerber sich nicht an die Pietät trauen oder es zu kommerziell angehen. Gleichzeitig **null Monetarisierung** auf diesem Cluster — siehe Trauer-Schutz in STRATEGIE.md.

**Bestehende Trauer-Seiten:**
- `/trauerrede-schreiben` (Score 64, Info)
- `/tools/trauerrede` (Score 40, CSR-Blocker)
- `/kondolenzschreiben` (Score 64, Info)
- `/trauersprueche` (Score 64, Info)
- `/kindern-tod-erklaeren` (Score 60, Info)

#### C.5.1 — Erstes Jahr nach dem Tod (12-Monats-Begleiter)

**URL:** `/trauer/erstes-jahr`

**Konzept:** Monat-für-Monat-Begleiter. Was Trauer im Monat 1 ist (Funktionieren), Monat 3 (Erschöpfung), Monat 6 (Wellen), Monat 9 (Anniversaries), Monat 12 (Neuanfang). Jeweils mit konkreten Hinweisen, was normal ist, was Hilfe braucht, was Angehörige tun können.

**Keyword-Targets:** "erstes Jahr nach Tod", "Trauer Phasen", "wie lange trauert man"

**Pflicht-Bausteine:**
- 2.000+ Wörter
- Quellen aus Trauerforschung (Kübler-Ross, Bonanno, Worden)
- Keine Pathologisierung — Trauer ist kein Krankheit
- Stichwort: Pietät-Gate 7 (verbindlich)

**Aufwand:** 6h

#### C.5.2 — Zurück zur Arbeit nach Trauerfall

**URL:** `/trauer/zurueck-zur-arbeit`

**Konzept:** Aus Arbeitnehmer-Perspektive (nicht HR). Sonderurlaub, Wiedereingliederung, was sage ich Kollegen, wann ist es zu früh, Rechtliches.

**Keyword-Targets:** "Trauer Arbeitsplatz", "Sonderurlaub Trauerfall", "zurück zur Arbeit nach Tod"

**Aufwand:** 4h

#### C.5.3 — Saisonaler Trauer-Content

Externes Audit-Hinweis: Saisonale Trauer-Suchanfragen explodieren ab Herbst.

| URL | Veröffentlichung | Aufwand |
|---|---|---|
| `/trauer/weihnachten` | Anfang November | 4h |
| `/trauer/silvester` | Mitte Dezember | 3h |
| `/trauer/muttertag` | Anfang Mai | 3h |
| `/trauer/vatertag` | Anfang Juni | 3h |
| `/trauer/totensonntag` | Anfang November | 3h |
| `/trauer/allerheiligen` | Mitte Oktober | 3h |
| `/trauer/jahrestag` | Evergreen | 4h |
| `/trauer/engelsgeburtstag` | Evergreen | 3h |

#### C.5.4 — Beileid digital (WhatsApp, SMS, Mail)

**URL:** `/beileid-whatsapp`

**Konzept:** Wie kondoliert man digital ohne Pietät zu verletzen? Welche Formulierungen funktionieren, was geht gar nicht. Vorlagen für WhatsApp, SMS, E-Mail.

**Keyword-Targets:** "Beileid WhatsApp", "Kondolenz digital", "Beileid SMS"

**Aufwand:** 3h

### Cluster C.6 — Bürokratie & Behörden (Mittelfristig)

**Hintergrund:** Aus content-plan.md — solide SEO-Keywords, mittlere Konkurrenz, klare Utility.

#### C.6.1 — Erbschein beantragen

**URL:** `/erbschein` (neu) — Schritt-für-Schritt mit Kosten, Wann brauche ich einen, wann nicht

**Aufwand:** 4h

#### C.6.2 — Witwenrente beantragen

**URL:** `/witwenrente` — Anleitung + Tool (kleine vs. große Witwenrente, Einkommensanrechnung)

**Aufwand:** 5h (Content + Tool)

#### C.6.3 — Sozialbestattung — eigene Seite

Aus C.2.3 ausgelagert in eigenen Cluster: dies ist ein eigenständiges SEO-Thema, nicht nur ein Kosten-Aspekt.

**URL:** `/sozialbestattung` — Anspruchsprüfung, Antrag, Pauschalen pro Bundesland

**Aufwand:** 4h

#### C.6.4 — Verträge kündigen nach Todesfall

**Status:** `/vertraege-kuendigen` existiert (Score 64). Aufrüsten:
- Musterschreiben pro Vertragsart (Strom, Gas, Telefon, Streaming, Versicherungen)
- Sonderkündigungsrecht-Hinweise mit Fristen
- Tabelle mit Standardfristen pro Anbieter

**Aufwand:** 3h Aufrüstung

#### C.6.5 — Dokumenten-Matrix

**URL:** `/dokumente-matrix` (neu)

**Konzept:** Welche Dokumente brauche ich für welchen Behördengang? Tabellen-Tool, das nach Anliegen filtert (Standesamt, Rente, Bank, Versicherung etc.) und die nötigen Unterlagen anzeigt.

**Keyword-Targets:** "Todesfall Unterlagen", "welche Dokumente nach Todesfall"

**Aufwand:** 5h (Content + simple Filter-Logik)

### Cluster C.7 — Neue Tools (nach Trust-Layer)

Aus content-plan.md, hierher verschoben weil sie Trust-Layer brauchen.

| Tool-URL | Keyword | Unique Angle | Aufwand |
|---|---|---|---|
| `/tools/trauerfeier-planer` | "Trauerfeier planen" | Ablauf-Builder + Musik-Vorschläge | 6h |
| `/tools/sterbeurkunden-rechner` | "wie viele Sterbeurkunden" | Rechner basierend auf Verträgen/Konten | 3h |
| `/tools/erbschaftssteuer-rechner` | "Erbschaftssteuer Rechner" | Steuerklasse + Freibetrag + progressive Sätze | 5h |
| `/tools/witwenrente-rechner` | "Witwenrente Rechner" | Große/kleine Rente + Einkommensanrechnung | 5h |
| `/tools/trauer-tagebuch` | "Trauertagebuch" | 52 Wochen Schreibimpulse als PDF | 4h |
| `/tools/digitaler-nachlass-inventar` | "Digitaler Nachlass" | Online-Konten katalogisieren ohne Passwörter | 5h |

**Wichtig:** Alle neuen Tools als Static Shell + Widget (siehe Phase A.3), kein @babel/standalone mehr.

### Cluster C.8 — Bestehende Vorsorge-Seiten als eigene URLs

Aus content-plan.md Prio B:

#### C.8.1 — Vorsorgevollmacht

**URL:** `/vorsorge/vorsorgevollmacht` (neu, aktuell nur im Vorsorge-Ordner enthalten)

**Aufwand:** 4h

#### C.8.2 — Betreuungsverfügung

**URL:** `/vorsorge/betreuungsverfuegung` (neu)

**Konzept:** Klare Abgrenzung zur Vorsorgevollmacht — viele User wissen den Unterschied nicht.

**Aufwand:** 4h

---

## Phase D — Strukturelle SEO-Fixes

**Parallel zu C laufend.** Kleine Fixes, große Hebel.

### D.1 — OG-Image für alle Seiten (MAX. Hebel, min. Aufwand)

**Problem:** 98/98 Seiten ohne OG-Image. Jeder Social-Media-Share zeigt kein Bild.

**Lösung:**
- Ein Master-OG-Image erstellen: "machs ruhig — Orientierung bei Todesfall, Bestattung und Vorsorge" mit Brand-Farben (1200×630px)
- Plus 4–5 Cluster-spezifische Varianten (Akutfall, Kosten, Recht, Vorsorge)
- Einmal im Build-Prozess per `og:image`-Meta einbinden

**Aufwand:** 2h Design + 1h Einbau = 3h

### D.2.1 — 5 Gold-Städte auf Score ≥85 heben (Stage 2 von A.2)

**Herkunft:** Rest-Arbeit aus Ticket A.2 / Sprint #2. Stage 1 ist am 23.04.2026 abgeschlossen (Score 75, statisch sichtbar). Stage 2 bündelt die restlichen ≥85-Kriterien.

**Betroffen:** Berlin, Frankfurt, Hamburg, Köln, München.

**Was fehlt zu ≥85:**
1. **FuneralHome/LocalBusiness-Schema** pro Stadt (siehe D.2-Matrix unten)
2. **H2-Count** teils unter Ziel — Gliederung nachschärfen
3. **Monetarisierungs-Warning** aufräumen, sobald Lead-Form aus Phase F zurück ist

**Abhängigkeit:** Punkt 3 setzt Phase F-Aktivierung voraus. Punkte 1 + 2 sind jetzt machbar und bringen den Score isoliert auf ~80–82.

**Empfohlene Ausführung:** Gebündelt mit dem Rest von D.2, wenn Phase D drankommt. Nicht isoliert nach Sprint #3 ziehen — Halbarbeit.

**Aufwand:** 3–4h für Punkte 1 + 2 (5 Städte × ~30–40 Min). Punkt 3 kommt automatisch mit Phase F.

**Akzeptanz:** Pro Stadt Audit-Score ≥85, `FuneralHome` oder `LocalBusiness` im Schema-Graph erkennbar, validate-all.sh grün.

---

### D.2 — Schema.org Upgrades pro Kategorie

Basierend auf der Zielmatrix aus `_dev/audit-all-pages.py`:

| Kategorie | Fehlend | Hinzufügen |
|---|---|---|
| homepage (1) | `Organization`, `WebSite` | beide |
| stadt (5 GOLD) | `LocalBusiness` oder `FuneralHome` | auf jede der 5 |
| bundesland (16) | `Place`, `AdministrativeArea` | auf alle 16 |
| content (7) | passt teilweise | gezielt `HowTo` wo Anleitung |
| vorsorge (8) | `Product` für Vorsorge-Dienste | wo relevant |

**Hinweis:** Das existierende Audit-Skript hatte einen Bug (hat `@graph` nicht rekursiv gelesen). Der Bug ist jetzt gefixt. **Schema ist also oft schon da, nur nicht im richtigen Typ.** Pro Seite 15–30 Min Arbeit.

**Gesamt-Aufwand:** 10–15h verteilt

### D.3 — Interne Linkstruktur

**Problem:** Homepage hat 3 interne Links (Ziel 10), Bundesländer meist 4 (Ziel 8).

**Lösung:** Jede Content-Seite bekommt einen einheitlichen "Weiterführend"-Block am Ende mit 5–8 Links zu thematisch verwandten Seiten.

**Aufwand:** 1h Template + pro Seite 5 Min = ~10h gesamt

### D.4 — Title-Längen normalisieren

Aus dem internen Audit: 28 Seiten mit Title >65 Zeichen (teilweise 98!).

**Aufwand:** 1h sitewide (CSV mit aktuellen Titeln → neue Titel → sed-Replace)

### D.5 — Meta-Descriptions normalisieren

Ähnlich — 3 zu lang, mehrere zu kurz. Sitewide-Check.

**Aufwand:** 1h

---

## Phase E — Top-10-Städte auf Gold-Niveau

**Zeithorizont:** erst wenn A, B, C.1+C.2, D solide.

**Kandidaten (nach Einwohnerzahl, Deutschland):**
- [GOLD schon] Berlin, Hamburg, München, Köln, Frankfurt
- [neu GOLD-fähig] Stuttgart, Düsseldorf, Leipzig, Dortmund, Essen

### E.1 — Gold-Template dokumentieren

Aus den existierenden 5 GOLD-Städten ableiten:

**Pflichtkriterien (aus der Substanzanalyse):**
- ≥5 konkrete Friedhofs-Eigennamen mit je 1–2 Sätzen Kontext
- ≥10 Euro-Beträge (Gebühren, Bestatterpreise, Pauschalen)
- Bundesland-Recht verlinkt, 2–3 stadtrelevante Paragrafen zitiert
- Bestattungsfrist des Bundeslands (konkret)
- FAQ mit ≥5 lokal relevanten Fragen
- "Stand: [Datum]" + ≥3 Quellen
- Intro-Text ohne Template-Floskeln (Generic-Check!)
- Schema.org `FuneralHome` (aus Phase D.2)

**Aufwand Template-Dokumentation:** 2h

### E.2 — Pro Stadt: Research + Aufrüstung

Pro neuer Gold-Stadt:
1. Research: Friedhöfe, Gebühren, Bestatter-Landschaft, Besonderheiten
2. Content-Neubau auf Gold-Niveau (Template aus E.1)
3. `noindex` entfernen (wenn Gold erreicht)
4. Audit-Score muss ≥85 sein vor Freigabe
5. Substanzanalyse-Score muss GOLD-Tier sein

**Aufwand pro Stadt:** 4–6h. 5 neue Städte = 20–30h.

**Anti-Pattern:** Nicht alle 45 Generic-Städte mit Research-Agent aufpumpen. Besser 10 echt Gold als 50 halb-Silber.

---

## Phase F — Monetarisierung aktivieren

**Nicht vor Phase E komplett.**

Vorbereitungen können aber früher getroffen werden.

### F.1 — Affiliate-Partner beantragen (KANN PARALLEL LAUFEN)

- DELA (130 €/Sale) — höchste Provision
- SOLIDAR (75 €/Sale)
- Afilio (30 €/Sale)

Beantragung kann sofort starten, da Bearbeitung 2–4 Wochen dauert. Aktivierung erst wenn Domain Authority hat.

**Aufwand:** 2–3h Anträge schreiben

### F.2 — Lead-Formular Backend

**Offene Entscheidung:** Netlify Forms vs. Formspree vs. eigenes Worker-Backend?

Kriterien:
- Kosten: Netlify Forms kostenlos bis 100/Monat, Formspree bis 50 frei
- DSGVO: Netlify in EU? Formspree? Eigene Lösung volle Kontrolle.
- Spam-Schutz
- CRM-Integration für später

**Aufwand:** 4–6h je nach Entscheidung

### F.3 — Bestatter-Vermittlung als Lead-Funnel

Wenn A–E solide:
- Stadt erkannt/ausgewählt
- Anlass (Akut/Vorsorge)
- Bestattungsart / Unsicherheit
- Budget
- Kontaktwunsch
- DSGVO + Vermittlungshinweis
- Routing ins CRM

**Aufwand:** größer, eigenes Ticket zur Zeit X

---

## Quality-Gates (vor jedem Go-Live)

Jede neue Seite muss alle 7 Gates bestehen. Verbindlich. Kompakt-Übersicht hier, Details in [STRATEGIE.md → Quality-Gates](./STRATEGIE.md#quality-gates-vor-jedem-go-live).

| Gate | Name | Blocker? |
|---|---|---|
| 1 | Intent-Fit (Title + H1 matchen Suchintention) | Ja |
| 2 | Utility (konkreter Output oder echte Hilfe) | Ja |
| 3 | Differenzierung (besser als Top-3-Konkurrenz) | Nein* |
| 4 | Conversion-Klarheit (1 Primär-CTA pro Bereich) | Ja |
| 5 | Brand-Fit (Design, Tonalität) | Ja |
| 6 | Programmatic-Sauberkeit (keine Platzhalter, 404-Links) | Ja |
| 7 | **Pietät-Check** | **Ja** |

**QA-Workflow pro Seite:**
1. Automatisierte Checks: `python3 _dev/audit-all-pages.py`
2. Substanzprüfung (bei Stadtseiten): `python3 _dev/stadt-quality-analysis.py`
3. Manuelle Gates 1-5
4. Gate 7 als letzter Check
5. Erst dann `noindex` entfernen / live gehen

**Vorlage pro Seite:**
```
Seite: ___ URL: ___ Typ: ___ Datum: ___
Gate 1 (Intent-Fit):          [ ] PASS  [ ] FAIL
Gate 2 (Utility):             [ ] PASS  [ ] FAIL
Gate 3 (Differenzierung):     [ ] PASS  [ ] WARN
Gate 4 (Conversion-Klarheit): [ ] PASS  [ ] FAIL
Gate 5 (Brand-Fit):           [ ] PASS  [ ] FAIL
Gate 6 (Programmatic):        [ ] PASS  [ ] FAIL
Gate 7 (Pietät):              [ ] PASS  [ ] FAIL
Ergebnis: [ ] GO LIVE  [ ] ÜBERARBEITEN  [ ] BLOCKIERT
```

---

## Anti-Patterns

Diese Entscheidungen ausdrücklich **nicht** treffen, sonst kippt Authority-Phase:

| ❌ Anti-Pattern | ✓ Stattdessen |
|---|---|
| Research-Agent auf 45 Städte loslassen | Händische Arbeit an 5 neuen Gold-Städten |
| Affiliate-CTAs auf jeder Seite maximieren | Trust-Layer komplett, dann selektiv |
| Neue Stadtseiten bauen | Bestehende aufrüsten oder noindexed lassen |
| CSR-Tools klonen | Static Shell + Widget |
| Homepage mit Leadgen-CTAs aufladen | Homepage als Orientierungs-Hub |
| Vergleichsportale (Sterbegeld) angreifen | Nischig bleiben, wo weniger Konkurrenz |
| Template-Floskeln wiederverwenden | Jede neue Seite durch Substanz-Check |

---

## Offene Entscheidungen

3 Entscheidungen wurden am 23.04.2026 getroffen (siehe [STRATEGIE.md → Festgelegte Entscheidungen](./STRATEGIE.md#festgelegte-entscheidungen-23042026)). 3 verbleiben.

### ✅ Entscheidung 1 — Autoren-Modell — ERLEDIGT

Gewählt: **"machsruhig Redaktion" + Fachpool-Reviewer** (Option 2).
Konsequenz: B.2 jetzt umsetzbar (Fachpool aufbauen, Redaktion-Block auf YMYL-Seiten).

### ✅ Entscheidung 2 — CSR-Fix Strategie — ERLEDIGT

Gewählt: **Hybrid (Option C)** — Homepage + Gold-Städte statisch, Tools = Static Shell + Widget.
Konsequenz: A.1, A.2, A.3 jetzt eindeutig umsetzbar.

### ✅ Entscheidung 3 — Realistische Kapazität — ERLEDIGT

Gewählt: **6-8 h/Woche** (machsruhig wird Hauptprojekt).
Konsequenz: Phase A+B realistisch in 7-9 Wochen abgeschlossen, Q4 2026 = Phase F-Aktivierung.

### ⏳ Entscheidung 4 — Gesetzestext-Archiv

- [ ] Brauchen wir eine zentrale `_dev/gesetze/`-Struktur mit Bestattungsgesetzen pro Bundesland, damit nicht jeder Artikel neu recherchiert?

**Empfehlung:** Ja, anlegen sobald C.3 (Bundesländer) startet. Spart Doppelarbeit. Aber **kein Blocker** für Phase A.

### ⏳ Entscheidung 5 — Lead-Backend (F.2)

- [ ] Netlify Forms / Formspree / Eigener Worker

**Empfehlung später:** Erst entscheiden wenn Phase E abgeschlossen ist und Bestatter-Lead-Funnel real wird.

### ⏳ Entscheidung 6 — Monetarisierungs-Antragsstart (F.1)

- [ ] Jetzt schon DELA/SOLIDAR/Afilio beantragen (4 Wochen Bearbeitungszeit nutzen)?

**Empfehlung:** Erst Anträge starten wenn Trust-Layer (Phase B) live und Akutfall-Cluster (C.1) ankommt — nicht früher, weil Affiliate-Programme den Domain-Trust prüfen.

---

## Metriken & Akzeptanzkriterien

### Phase A abgeschlossen wenn:
- Homepage Audit-Score ≥75 (aktuell 39)
- 5 Gold-Städte Audit-Score ≥85 (aktuell 40)
- Keine Deploy-Blocker mehr im Audit-Report
- Lighthouse auf Homepage ≥90

### Phase B abgeschlossen wenn:
- Über-uns-Seite live
- Autor-System auf allen YMYL-Seiten sichtbar
- Methodik verlinkt von jeder YMYL-Seite
- Disclaimer einheitlich

### Phase C abgeschlossen wenn:
- Akutfall-Cluster: 4 Seiten, je ≥1.500 Wörter, je Audit-Score ≥85
- Kosten-Cluster: 5 Seiten, je ≥1.500 Wörter
- Recht-Cluster Runde 1: 5 Bundesländer, je ≥1.000 Wörter
- Entscheidungs-Cluster: 3 Seiten

### Phase D abgeschlossen wenn:
- OG-Image auf ≥95/98 Seiten
- Gold-Städte mit `FuneralHome`-Schema
- Bundesländer mit `Place`-Schema
- Homepage mit `Organization` + `WebSite`

### Phase E abgeschlossen wenn:
- 10 Städte im GOLD-Tier (Substanzanalyse)
- Jede Gold-Stadt Audit-Score ≥85

### Phase F-Freigabe-Kriterium:
- Ø Site-Score ≥80 (aktuell 59.0)
- Kein Cluster unter Ø 75
- Externes Audit-Rating ≥8.0/10 (aktuell 6.6)

---

## Ticket-Übersicht (komplett)

| # | Phase | Ticket | Aufwand | Abhängigkeit |
|---:|---|---|---:|---|
| 1 | A.1 | Homepage statisch neu bauen | 4–6h | — |
| 2 | A.2 | Berlin statisch rendern | 2–3h | A.1 Entscheidung |
| 3 | A.2 | Frankfurt statisch rendern | 2–3h | A.1 Entscheidung |
| 4 | A.2 | Hamburg statisch rendern | 2–3h | A.1 Entscheidung |
| 5 | A.2 | Köln statisch rendern | 2–3h | A.1 Entscheidung |
| 6 | A.2 | München statisch rendern | 2–3h | A.1 Entscheidung |
| 7 | A.3 | Bestattungskosten-Rechner: Static Shell | 2–3h | — |
| 8 | A.3 | Checkliste-Todesfall: Static Shell | 2–3h | — |
| 9 | A.3 | Vorsorge-Check: Static Shell | 2–3h | — |
| 10 | A.3 | Trauerrede-Tool: Static Shell | 2–3h | — |
| 11 | A.3 | Restliche 5 Tools: Static Shell | 10h | — |
| 12 | A.4 | Pre-Rendering Build-Script | 3–4h | optional |
| 13 | B.1 | Über-uns-Seite | 3–4h | Entscheidung 1 |
| 14 | B.2 | Autoren-System implementieren | 2h + Roll-out | Entscheidung 1 |
| 15 | B.3 | Methodik ausbauen | 2h | — |
| 16 | B.4 | Disclaimer-Block einheitlich | 2h | — |
| 17 | B.5 | Stand- und Quellen-Template | 1h | — |
| 18 | C.1.1 | Akutfall-Hauptseite | 6–8h | B.2 |
| 19 | C.1.2 | Entscheidungsbaum | 4–6h | C.1.1 |
| 20 | C.1.3 | Unterlagen-Seite | 4h | — |
| 21 | C.1.4 | Standesamt-Seite | 3h | — |
| 22 | C.2.1 | Erdbestattung-Kosten-Detail | 5h | — |
| 23 | C.2.2 | Kostenvergleich | 3h | C.2.1 |
| 24 | C.2.3 | Sozialbestattung (kurz, in C.6.3 vertieft) | 4h | — |
| 25 | C.2.4 | Wer zahlt? | 3h | — |
| 26 | C.2.5 | Sparoptionen | 3h | — |
| 27 | C.3 | Bundesland NRW | 3–4h | Entscheidung 3 |
| 28 | C.3 | Bundesland Bayern | 3–4h | Entscheidung 3 |
| 29 | C.3 | Bundesland BW | 3–4h | Entscheidung 3 |
| 30 | C.3 | Bundesland Niedersachsen | 3–4h | Entscheidung 3 |
| 31 | C.3 | Bundesland Hessen | 3–4h | Entscheidung 3 |
| 32 | C.3 | Bundesländer Runde 2 (11 Länder) | 22–33h | Runde 1 |
| 33 | C.4.1 | Erd- oder Feuer | 4h | — |
| 34 | C.4.2 | Anonym oder mit Grab | 4h | — |
| 35 | C.4.3 | Religion und Bestattung | 4h | — |
| 36 | C.5.1 | Trauer: Erstes Jahr (12-Monats-Begleiter) | 6h | B.2 |
| 37 | C.5.2 | Trauer: Zurück zur Arbeit | 4h | — |
| 38 | C.5.3 | Trauer-Saisonal: Weihnachten | 4h | timing-kritisch |
| 39 | C.5.3 | Trauer-Saisonal: Silvester | 3h | — |
| 40 | C.5.3 | Trauer-Saisonal: Muttertag | 3h | — |
| 41 | C.5.3 | Trauer-Saisonal: Vatertag | 3h | — |
| 42 | C.5.3 | Trauer-Saisonal: Totensonntag | 3h | timing-kritisch |
| 43 | C.5.3 | Trauer-Saisonal: Allerheiligen | 3h | timing-kritisch |
| 44 | C.5.3 | Trauer-Evergreen: Jahrestag | 4h | — |
| 45 | C.5.3 | Trauer-Evergreen: Engelsgeburtstag | 3h | — |
| 46 | C.5.4 | Beileid digital (WhatsApp/SMS/Mail) | 3h | — |
| 47 | C.6.1 | Erbschein beantragen | 4h | — |
| 48 | C.6.2 | Witwenrente beantragen + Tool | 5h | — |
| 49 | C.6.3 | Sozialbestattung (vertieft) | 4h | C.2.3 |
| 50 | C.6.4 | Verträge kündigen aufrüsten | 3h | — |
| 51 | C.6.5 | Dokumenten-Matrix | 5h | — |
| 52 | C.7 | Tool: Trauerfeier-Planer | 6h | A.3 |
| 53 | C.7 | Tool: Sterbeurkunden-Rechner | 3h | A.3 |
| 54 | C.7 | Tool: Erbschaftssteuer-Rechner | 5h | A.3 |
| 55 | C.7 | Tool: Witwenrente-Rechner | 5h | A.3, C.6.2 |
| 56 | C.7 | Tool: Trauer-Tagebuch (52 Wochen PDF) | 4h | — |
| 57 | C.7 | Tool: Digitaler-Nachlass-Inventar | 5h | A.3 |
| 58 | C.8.1 | Vorsorgevollmacht (eigene Seite) | 4h | — |
| 59 | C.8.2 | Betreuungsverfügung | 4h | C.8.1 |
| 60 | D.1 | OG-Image Master + Varianten | 3h | — |
| 61 | D.2 | Schema.org Upgrades | 10–15h | — |
| 62 | D.3 | Interne Linkstruktur | 10h | — |
| 63 | D.4 | Title-Normalisierung | 1h | — |
| 64 | D.5 | Meta-Description-Normalisierung | 1h | — |
| 65 | E.1 | Gold-Template dokumentieren | 2h | — |
| 66 | E.2 | Stuttgart auf Gold | 4–6h | E.1 |
| 67 | E.2 | Düsseldorf auf Gold | 4–6h | E.1 |
| 68 | E.2 | Leipzig auf Gold | 4–6h | E.1 |
| 69 | E.2 | Dortmund auf Gold | 4–6h | E.1 |
| 70 | E.2 | Essen auf Gold | 4–6h | E.1 |
| 71 | F.1 | DELA/SOLIDAR/Afilio-Anträge | 2–3h | kann parallel |
| 72 | F.2 | Lead-Backend wählen + bauen | 4–6h | Entscheidung 5 |
| 73 | F.3 | Lead-Funnel | groß | F.2 |

**Gesamt-Aufwand (grobe Schätzung):**
- Phase A: 30–45h (AKUT)
- Phase B: 10–15h
- Phase C.1-C.4: 70–110h (Akutfall, Kosten, Recht, Entscheidung)
- Phase C.5: 39h (Trauer-Cluster — niedrige Konkurrenz, hoher Hebel)
- Phase C.6: 21h (Bürokratie & Behörden)
- Phase C.7: 28h (neue Tools)
- Phase C.8: 8h (Vorsorge-Detail-Seiten)
- Phase D: 25–30h
- Phase E: 20–30h
- Phase F: 15–25h + groß F.3

**Kritischer Pfad:** A → B → C.1 → C.2 → C.3 Runde 1 → D parallel → C.5/C.6/C.7 nach Bedarf → E → F

**Saisonale Trigger** (timing-kritisch im Jahresverlauf):
- Mitte Oktober: Allerheiligen-Content live
- Anfang November: Totensonntag + Weihnachten-Content live
- Mitte Dezember: Silvester-Content live
- Anfang Mai: Muttertag-Content live
- Anfang Juni: Vatertag-Content live
