# Content-Loop V2 — Methodologie

**Validiert mit Saarland, Hessen, NRW (11.05.2026).** Alle 16 Bundesland-Pages auf Elite-Niveau, strukturell konsistent.

---

## Architektur: 3 Chats + Branch-Trick

Drei separate **claude.ai-Browser-Tabs** (nicht Subagents, nicht API):

- **Chat A — Writer:** schreibt v1, v2, v3, alle Tool-Fixes. Hat Memory der eigenen Iterationen.
- **Chat B — Reviewer:** bewertet v1 als fremder Reviewer. Keine Schreib-Memory → kein Sycophancy-Effekt.
- **Chat C — Adversarial:** sucht 3 Schwächen in v2 als feindlicher Reviewer. Frischer Context.

Trennung **verhindert Sycophancy** — wir haben den Score-Drift zwischen Chat A's Selbsteinschätzung und Chat B/C-Bewertung mehrfach beobachtet (Hessen v1: Chat B 78% → Chat C 81%; Saarland v1: Chat B 72% → Chat C 79%). Same-Chat würde diese Strenge verlieren.

### Branch-Trick (KERN der V2-Methodik)

Statt langer chunked-paste-Operationen (V1-Methode) bekommt jeder Chat eine **raw-URL** zum aktuellen Page-Stand. Worker fetcht via Web-Search/Fetch selbständig.

**Pro Round:**

1. Worker liefert HTML → lokal speichern als `runs/<slug>/v<N>-from-chat-A.html`
2. Commit + Push auf branch `content-loop-pipeline`
3. Raw-URL ist sofort verfügbar: `https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/<slug>/v<N>-from-chat-A.html`
4. Nächster Chat bekommt **kurzen Prompt mit URL** (statt 30k-Zeichen chunked-paste)

**Effekt:** ~50 Min pro Page statt ~90 Min, kein chunked-paste-Drama, Worker kann zudem die RP-Page oder Hessen-Page als Niveau-Anker selbst fetchen.

---

## Pipeline-Workflow

### Phase 0: Pilot-Vorbereitung (~10 Min, vor Round 1)

1. **WebSearch parallel** (4–6 Queries) für:
   - Aktuelles Bestattungsgesetz mit Paragraphen-Nummern
   - 2–3 bedeutende Friedhöfe mit Geschichte/Architektur/Fläche
   - Bestattungskosten + Friedhofsgebühren-Satzungen
   - Lokale Besonderheiten / Hidden-Gem-Stories
2. **Quellen-Pack** als markdown nach `runs/<slug>/quellen-pack.md` schreiben — verifizierte §-Nummern, Friedhofs-Daten mit Quellen, Hidden-Gem-Stories, alle als kopierbare URLs
3. **Branch sicherstellen:** auf `content-loop-pipeline` (von main abgezweigt), **niemals auf main pushen während Pipeline läuft**
4. Quellen-Pack push → raw-URL prüfen

### Phase 1: WRITE (Chat A, Round 1)

1. Briefing A pasten (siehe `_dev/content-loop/briefings/A-writer.md`)
2. Worker antwortet `BRIEFING_OK`
3. **Task-Prompt mit zwei URLs:**
   - Quellen-Pack-URL
   - Referenz-Page-URL (z.B. Hessen v5 als Stil-Anker, da auf Score 85 + alle mr-Klassen)
4. Worker fetcht beide, schreibt v1 (~3-5 Min Streaming)
5. v1 lokal speichern → commit/push → URL

### Phase 2: SCORE (Chat B, Round 2)

1. Neuer Tab, Briefing B pasten
2. `BRIEFING_OK`
3. Prompt mit v1-URL → Worker fetcht, gibt `SCORE: NN%` + `GAP:` Liste
4. Review als markdown speichern → commit/push → URL

### Phase 3: FIX (Chat A, Round 3)

1. Prompt mit Review-URL → Worker fetcht, schreibt v2
2. v2 speichern → commit/push

### Phase 4: ADVERSARIAL (Chat C, Round 4)

1. Neuer Tab, Briefing C pasten
2. `BRIEFING_OK`
3. Prompt mit v2-URL → Worker liefert 3 Schwächen + `EHRLICHE %-ZAHL: NN%`
4. Adversarial-Review speichern → push

### Phase 5: FINAL FIX (Chat A, Round 5)

1. Prompt mit Adversarial-URL → v3
2. v3 speichern → push

### Phase 6: TOOL-VALIDATION + FIX-LOOP

1. v3 ins Target kopieren: `cp runs/<slug>/v3.html bestattung-in/<slug>/index.html` (lokal, **nicht commit**)
2. `python3 _dev/bundesland-recheck.py bestattung-in/<slug>/index.html`
3. `python3 _dev/audit-all-pages.py` → AUDIT-REPORT.json → Score extrahieren
4. Decision per **Stopp-Regel** (siehe unten)

Bei Bedarf bis zu 4 Tool-Fix-Versuche mit Worker, jeweils via raw-URL.

### Phase 7: Promotion auf main (mit Deploy)

1. Wenn akzeptiert: Page kopieren von Pipeline-Branch → main-Branch (lokal)
2. SESSION-NOTES.md updaten
3. Commit + Push origin main → Netlify-Deploy

---

## Stopp-Regel „Basics vs Schönarbeit"

Verhindert verschwendete Tool-Fix-Versuche bei Score-Plateaus.

### Weiter-iterieren (Basics)

- Recheck hat Blocker oder Warnungen
- Halluzinations-Verdacht (erfundene §-Nummer, nicht-verifiziertes Zitat, ungeprüfte Statistik)
- Major Audit-Issues:
  - Schema fehlt (BreadcrumbList, Place, Article)
  - Title outside 50–60 Zeichen
  - OG-Image fehlt oder als SVG
  - Cross-Links zu thematischen Hubs = 0
  - skip-link fehlt
- Score-Gewinn ≥ 3 P pro Versuch → Methode trägt noch

### Akzeptieren (Schönarbeit)

- Recheck grün ✓ UND
- Audit-Score ≥ 82 UND
- letzte 2 Versuche < 3 P Gewinn (Plateau erkannt)
- Wortzahl innerhalb ±50 vom Ziel-Korridor (z.B. 2516 statt 2500 → akzeptabel)

**Lehre aus Saarland (V1):** 4 Tool-Fix-Versuche bei Plateau 83 waren Verschwendung. Hessen (V2) erreichte 85 in 2 Versuchen, NRW (V2) bei 83 nach 2 Versuchen akzeptiert.

---

## Konsistenz-Patterns (alle 16 BL nutzen jetzt)

### Layout (mr-Stil)

CSS-Klassen aus dem machsruhig-Standard-System:

- `mr-nav` — sticky Navigation oben
- `mr-content` — Hauptcontainer (max-width 720px)
- `mr-hero` — Hero-Sektion mit H1 + Lead
- `mr-breadcrumb` — Brotkrumen-Navi
- `mr-keyfacts` — Kernfakten-Box mit ul
- `mr-section` — Inhalts-Sektion
- `mr-faq` — FAQ-Bereich (Schema.org-konform)
- `mr-sources` — Quellen-Block am Ende
- `mr-footer` — Footer
- `skip-link` — Accessibility-Sprungmarke

Fonts: **DM Sans** (Sans-Serif) + **Fraunces** (Serif für H1/H2).

### Schema.org-Set

Alle 16 BL haben dasselbe JSON-LD-Set:
`Article, FAQPage, BreadcrumbList, WebPage, Place, City, ImageObject, Organization, PostalAddress, ListItem, Question, Answer`

Article muss enthalten: `author, publisher, datePublished, dateModified, inLanguage, mainEntityOfPage`.

### Sektions-Reihenfolge

1. Kernfakten (mr-keyfacts ul)
2. Bestattungsgesetz [BL] (mit § und Reform-Story falls aktuell)
3. Bestattungsfristen
4. Sargpflicht (mit religiöser Ausnahme)
5. Mindestruhezeiten / Friedhofszwang
6. Bestattungsformen in [BL]
7. Wichtige Friedhöfe (2–3 mit Hidden-Gem-Story)
8. Bestattungskosten (mit konkreten Spannen)
9. Bestatter und lokale Hilfe (Cross-Links zu Stadtseiten)
10. Was Sie konkret tun müssen (Handlungsanleitung)
11. Häufige Fragen (FAQ Schema.org-konform)
12. Quellen (alle Primärquellen verlinkt)

---

## Restruktur-Pattern (für bereits inhaltlich solide Pages mit Layout-Abweichung)

**1 Round, 1 Prompt, 1 Output** — kein Multi-Chat nötig.

Neuer Chat (frischer Context), Prompt mit zwei URLs:
- **CONTENT-Quelle:** existierende Page (alle Inhalte/Quellen bleiben)
- **LAYOUT-Template:** Hessen-Page oder andere Standard-Page (mr-Klassen, Schema-Set, Sektions-Reihenfolge)

Worker übernimmt alle Inhalte aus CONTENT, gießt in LAYOUT-Struktur. Funktioniert in einem Schuss — Saarland v8 (07.05.2026) als Proof: nicht-konformes Saarland v7 → 100% konformes v8 in ~5 Min.

**Anwendungsfall:** wenn alte Pages strukturell von neuem Standard abweichen, Inhalt aber gut ist.

---

## Wakeup-Mechanismen bei langen Streams

**WICHTIG:** `ScheduleWakeup` funktioniert **nur im `/loop dynamic mode`** — nicht in normaler Konversation.

### Optionen für lange Streaming-Phasen (>3 Min)

**A) `/loop` Skill aktivieren** vor Pipeline-Start
- User triggert `/loop <prompt>`, dann ist `ScheduleWakeup` verfügbar
- Beste Wahl für längere autonome Runs
- Cache-Strategie: 60–270s = Cache warm, 1200–1800s = Cache miss aber ok bei langen Wartephasen

**B) `Bash run_in_background` mit `Monitor`-Tool**
- Background-Task pollt, Notification weckt Claude
- Für sehr lange Wartephasen / parallele Operationen

**C) Klassisch: sequenzielle `wait`-Loops**
- `mcp__Claude_in_Chrome__computer wait` (max 10s pro Aufruf)
- Standard für kurze Wartephasen (<3 Min)
- Verbraucht Tokens pro Polling-Schritt

Pragmatisch: bei sehr langen Phasen (>5 Min) Option A oder B, sonst C.

---

## Token-Effizienz (gemessen)

| Methode | Wall-Clock | Plan-Token-Verbrauch | Hinweis |
|---|---|---|---|
| V1 (chunked-paste) | ~90 Min | hoch (viele Chunks + Wait-Loops) | Saarland-Erstrun |
| V2 (Branch-Trick) | ~50 Min | mittel | Hessen, NRW |
| V2 + Restruktur | ~5–10 Min | niedrig (1 Round) | Saarland v8 |

---

## Hard-Stops während eines Runs

Sofort an User melden und stoppen wenn:
- Worker antwortet nicht mit `BRIEFING_OK` nach Briefing-Paste (max 1× neu versuchen)
- Output von Round 1 offensichtlich kaputt (kein HTML, <800 Zeilen, massive Halluzinationen)
- Worker stellt mehrfach Rückfragen statt zu liefern
- `recheck.py` oder `audit-all-pages.py` crashen (Tool-Fehler ist kein Worker-Problem)
- User sagt „Stop"

---

## Was die V2-Methodik NICHT ist

- Kein Auto-Pilot (User-Steuerung pro Round-Wechsel)
- Keine Subagent-Pipeline (würde die echte separate-Chat-Architektur kollabieren lassen)
- Keine API-Migration (würde funktionieren, aber kostet ~$3-25 pro Page; aktuell Plan-Tokens)

---

## Nächste Schritte für V3

- **Quellen-Pack-Generator als Subagent** — würde Pilot-Vorbereitungszeit von 10 Min auf 2 Min reduzieren, ohne Multi-Chat-Architektur zu beeinträchtigen
- **Anwendung auf Stadt-Pages** (45 Thin-Content-Pages sind aktuell noindex, Top-5 könnten via dieser Methodik aufgelevelt werden)
- **Anwendung auf Tool-Pages** (tool-content-Kategorie hat Score-Mittel 36/100 — größtes Optimierungspotenzial)

---

## Referenz-Implementierungen

- `runs/hessen/` — vollständiger V2-Run, Score 85 in 2 Tool-Fix-Versuchen
- `runs/saarland/` — V1 (chunked) → v7 Score 83, V2-Restruktur → v8 strukturell konsistent
- `runs/nrw/` — V2-Run, Score 83 (Plateau, akzeptiert nach Stopp-Regel)
- `briefings/A-writer.md`, `briefings/B-reviewer.md`, `briefings/C-adversarial.md` — die drei Chat-Briefings
- `prompts/01-task-saarland.md` ff. — Round-Prompts als Templates
