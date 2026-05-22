# Helper-V3 — Multi-Chat-Dispatch-Methodik

**Stand**: 2026-05-22 · **Projekt**: machsruhig-deploy

Helper-V3 ist die aktuelle Iteration der **Multi-Chat-Pipeline** für parallele Reviewer/Writer-Chats. Sie löst das Grundproblem: Eine einzelne Claude-Session kann sich nicht selbst adversarial kritisieren ohne Sycophancy-Cluster (86%-Score-Falle). Lösung: Mehrere unabhängige claude.ai-Tabs erzeugen, jede mit isoliertem Kontext, parallel arbeiten lassen, Verdicts in der Haupt-Session konsolidieren.

---

## Drei Dispatch-Modi — wann was

Es gibt drei mögliche Wege Arbeit zu delegieren. Verwechsel sie nicht.

### 1. Helper-V3 Chat-Tab-Dispatch (Chrome MCP)
Eigene claude.ai-Tabs als Reviewer/Writer. **Transparent**: Du siehst die Tabs, kannst manuell eingreifen, 240s-Cadence ist observable.

**Lohnt sich für:**
- Komplexe inhaltliche Reviews (Stadt-Page als Ganzes auf Konsistenz prüfen)
- Mehrere Cities parallel adversarial-blind reviewen
- *Gesamteindruck* zählt (Trust-Signale, Lesefluss, Tone)
- Mehrere unabhängige Cities gleichzeitig

### 2. Self-Verify (WebFetch/WebSearch direkt in Haupt-Session)
Die Haupt-Session macht die Verifikation selbst. **Schnellster Pfad**.

**Lohnt sich für:**
- Klare faktische Punkt-Frage (z.B. "Ist § 19 BestV 96h oder 8 Tage?")
- Wenige Stellen zu prüfen (Single-City YMYL-Check)
- Schnell + deterministisch, kein Chrome-MCP-Overhead nötig
- **Default-Modus seit dieser Session** — ~3× schneller als Helper-V3 bei gleicher Qualität für §-Verifikation

### 3. Anthropic-Subagents (Task / Agent-Tool)
Im Background gespawnt, **opak**. Du siehst nicht, was sie denken — nur das Endergebnis.

**LEGITIM für:**
- **Explore-Agent**: "Lies 50 City-HTML-Files und finde alle Vorkommen von § 8 BestG NRW" → mechanisches Lesen, kein Urteil
- **general-purpose-Agent**: Multi-File-Research, "wo wird XY referenziert"
- **Plan-Agent**: Mehrstündige Architektur-Pläne durchdenken
- Genuinely parallele unabhängige Tasks (während Main-Session was anderes macht)

**NIEMALS für (das ist Helper-V3-Use-Case):**
- "Review diese Stadt-Page" → Blackbox-Urteil ohne Anchor-Schutz
- "Score diese Content-Qualität" → Sycophancy unkontrolliert
- "Entscheide ob das ein YMYL-Bug ist" → braucht visible Reasoning
- "Schreibe diese Page neu" → genau wofür Writer-Tabs da sind

### Faustregel — was wo

| Aufgabe | Modus |
|---|---|
| § XY in aktuellem Landesrecht? | Self-Verify (WebFetch) |
| "Wie fühlt sich diese Page an?" | Helper-V3 Tab |
| Score-Vergleich Page-A vs Page-B | Helper-V3 Tab |
| "Wo wird X im Repo referenziert?" | Explore-Subagent oder Grep direkt |
| "Lies 50 Files, finde Pattern" | Explore-Subagent |
| "Plan diese 50h-Migration" | Plan-Subagent |
| "Implementiere den Fix" | Selbst machen, nicht delegieren |
| Multi-City parallel reviewen | Helper-V3 Tabs (3-5 parallel) |

**Kern-Prinzip**: Subagents für *mechanische* Such-/Lese-Tasks. Helper-V3 für *inhaltliche Urteile*. Self-Verify für *Punkt-Fakten*. Never confuse them.

---

## Setup-Pflicht vor Dispatch

### 1. Browser-Identität checken (KRITISCH)

Vor jedem Chrome-MCP-Call:

```
mcp__Claude_in_Chrome__list_connected_browsers
→ Bolle-Office deviceId: 2bee5aa2-fece-43e8-a9e6-ff739861775c
mcp__Claude_in_Chrome__select_browser deviceId=2bee5aa2-fece-43e8-a9e6-ff739861775c
```

**NIE** Hannes-deviceId `a46b8b91-7508-4ac8-9719-cffbe4b626ea` verwenden — das ist ein fremder Account, eskaliert sofort.

### 2. Tab-Hygiene

Vor dem Dispatch: Vorhandene claude.ai-Tabs auflisten. Wenn schon Chat-A/B/C-Tabs offen sind → erst alte schließen, dann neue Tabs aufmachen. **Tabs nach Phase IMMER schließen** — kein Tab-Müll.

### 3. Kein Screenshot-Spam

JPEGs nur wenn echte Unsicherheit. Sonst:
- `mcp__Claude_in_Chrome__javascript_tool` für DOM-Checks
- `mcp__Claude_in_Chrome__tabs_context_mcp` für Tab-State
- `get_page_text` für Inhalts-Lesen

---

## Defaults — Tabs und Cadence

### Default: 3 Streams, 240s Wakeup

Standard-Dispatch ist **3 parallele Chat-Tabs** (Chat-A / Chat-B / Chat-C), **240s Wakeup-Cadence**.

**Warum 3?**
- Cognitive Load: 3 parallel können in einer Wake-up-Phase konsolidiert werden
- Chrome-MCP-Overhead: jedes Tab ist ein eigenes Switch, ab 5 wird's Daten-heavy
- Batch-Size 3 deckt typische "Top-X-Cities"-Reviews (HH/M/B, Stuttgart/Frankfurt/Köln, etc.)
- Dieser Session: Batch 2 Top-3-BL war genau 3 Tabs, sauber konsolidierbar

**Skalierung:**
- 1–2 Streams: Overkill für Helper-V3 — Self-Verify oder Single-Tab
- 3 Streams: Default für Multi-City-Reviewer-Sweep
- 4–5 Streams: Möglich, aber Wake-up dauert länger zum Lesen aller Tabs
- 6+: NICHT machen. Lieber zwei 3er-Batches sequenziell.

**Warum 240s?**
- Reviewer/Writer brauchen ~2–3 min für sinnvolle Output-Tiefe
- Bei <240s liefern sie nur oberflächliche Verdicts
- Bei >300s wird die Prompt-Cache-TTL (5 min) überschritten — teurer
- 240s = Sweet-Spot zwischen Output-Tiefe und Cache-Hit

**Wenn du nur 1 Stream brauchst** (z.B. einzelne Page sehr tief reviewen): Helper-V3 ist Overkill. Mach Self-Verify oder benutz nur 1 Tab ohne den ganzen Dispatch-Loop.

Der Loop wird via Skill `/loop` oder `ScheduleWakeup` getriggert. Pattern:

```
1. Dispatch: Tabs öffnen, Prompt in jedes Tab pasten, abschicken
2. Sleep 240s (Wakeup)
3. Wake-up: Alle Tabs lesen, Verdicts konsolidieren
4. Apply: Fixes deterministisch via Python-Skript anwenden
5. Commit lokal (mit [skip netlify])
6. Nächster Dispatch oder Stop
```

---

## Reviewer vs Writer — Prompt-Struktur

### Reviewer-Prompt (adversarial check)

```
Du bist Reviewer für YMYL-Bestattungs-Content. Prüfe diese Stadt-Page
auf: (1) §-Paragraphen-Korrektheit vs aktuellem Landesrecht,
(2) Faktische Aussagen zu Friedhöfen/Gebühren/Personen,
(3) Logische Konsistenz innerhalb der Page.

URL: https://machsruhig.de/bestatter/{city}/
Quellen für §-Check: recht.{bl}.de, aeternitas.de, dejure.org

Output-Format:
- VERDICT: ALL_PASS | ANY_FAIL
- Issues mit Zeilennummer + Begründung + Quelle
- Optional-Hinweise getrennt (kein FAIL)
```

### Anti-Patterns für Reviewer-Prompts

❌ **Score-Anchoring**: "Die Page ist aktuell bei 84%, prüfe ob 85% erreicht ist"
   → Cluster bei 86%, Sycophancy. **NIE** vorherigen Score oder Ziel-Score nennen.

❌ **Source-Disclosure**: "Anderer Reviewer fand X, prüfe ob das wirklich ein Bug ist"
   → Reviewer wird zustimmen oder widersprechen je nach Phrasing-Hint, nicht je nach Befund.

❌ **Plausible vs Umami Confusion**: Bei machsruhig ist Plausible korrekt (NICHT Umami — das ist machsleicht).

### Writer-Prompt (Re-Generierung nach Reviewer-FAIL)

```
Du bist Writer für eine Stadt-Page. Hier ist der aktuelle Stand:
{HTML}

Diese Issues hat der Reviewer gefunden:
{issues}

Generiere die Page neu mit folgenden Fixes. Behalte Tone + Struktur
gleich. Output: vollständiges HTML.
```

---

## Hamburg-Artifact-Workaround

Bei großen Stadt-Pages (>30 KB) schluckt Claude.ai gelegentlich die letzten 20–30% des HTML-Outputs im Artifact-Viewer. Workaround:

1. Writer-Prompt anweisen: "Output in zwei Teilen — Teil 1 bis Section X, Teil 2 ab Section X+1"
2. Beide Teile lesen via `get_page_text`
3. Lokal zusammenfügen
4. Diff gegen Original vor dem Commit prüfen (nicht blind übernehmen)

Wurde erstmals bei Hamburg-Page nötig (~58 KB).

---

## Adversarial-Fundtypen (was Reviewer typisch finden)

Aus 6+ Helper-V3-Batches dieser Session:

1. **§-Paragraphen-Mis-Attribution** (häufigster YMYL-Bug)
   - z.B. § 22 → § 21 BestattG Saarland (Post-2021-Renumbering)
   - § 3 HmbBestG → § 2 HmbBestG (Reform 2020)
   - § 13 BestG RLP → § 9 BestG RLP (Verantwortlichkeit)

2. **Rangfolge-Vertauschung**
   - Bayern: Großeltern + Enkel VOR Geschwister (Sonderfall)
   - Berlin: Enkel VOR Großeltern (anders als BW/Bayern)
   - BW: Großeltern VOR Geschwister
   - Hessen: keine statutarische Rangfolge (Praxis-Reihenfolge)

3. **Veraltete Fristen**
   - Bayern 96h → 8 Tage (seit 1.4.2021)
   - Hessen 4 Tage → 10 Tage (seit Novelle 30.9.2025)
   - Berlin 48h-Wartefrist abgeschafft (Reform 2024)

4. **Interne Inkonsistenzen**
   - Wiesbaden: "gesetzliche Rangfolge ... gleichrangig" (paradox)
   - Mainz: zwei verschiedene Rangfolgen auf derselben Page

5. **Form-Attribution-Bugs**
   - Plausible `form='bestatter-anfrage'` hardcoded auf 48 Cities, obwohl Lead aus verschiedenen Forms kommt
   - Fix: Dynamic `?source=<form-name>` URL-Param + Parsing auf Success-Page

---

## Fix-Apply-Pattern

Nach Verdict NIE die Stadt-Page manuell mit Edit reparieren wenn ≥3 Stellen betroffen. Stattdessen:

1. **Python-Skript schreiben** in `_dev/audit/fix-ymyl-batchN.py`
2. Skript macht deterministische `text.replace(...)` über alle Stellen + alle Cities
3. Output-Count pro Replace + Anzahl Files modifiziert
4. Lokal ausführen, dann committen
5. Skript bleibt im Repo als Audit-Trail

Vorteil: Reproduzierbar, idempotent, dokumentiert *welche* Strings genau geändert wurden.

---

## Git-Hygiene für Pipeline-Commits

Im `content-loop-pipeline`-Branch arbeiten, NICHT direkt auf `main`:

```bash
git -c user.name="Bollesan91" -c user.email="cbollweg@gmx.de" \
    commit -m "fix(ymyl): § Hamburg/Berlin/München — Round-2 Verdicts [skip netlify]"
```

Pflichten:
- `-c user.name="Bollesan91" -c user.email="cbollweg@gmx.de"` PFLICHT (Sandbox-Bug verschluckt sonst Errors)
- `[skip netlify]` für ALLE pipeline-Commits (Netlify-Builds sparen)
- KEIN `[skip netlify]` beim Merge-Commit auf main
- Co-Author header: `Co-Authored-By: Claude <noreply@anthropic.com>`
- **NIE eigenständig pushen oder deployen** — nur auf explizite User-Anweisung

---

## Anti-Patterns / Lessons-learned

1. **Score-Anchoring** → Reviewer/Writer-Prompts ohne vorherigen Score oder Ziel-Score formulieren
2. **Helper-V3-Overkill für Single-Fact-Checks** → Self-Verify per WebFetch ist 3–5× schneller
3. **Subagent für Reviews missbrauchen** → Background-Task() für "review diese Page" ist ein Anti-Pattern. Subagents sind opak, Helper-V3 Chat-Tabs sind transparent. Subagents NUR für mechanische Such-/Lese-Tasks (Explore, general-purpose). Nicht für inhaltliche Urteile.
4. **Tabs offen lassen** → Wenn Phase fertig, Tabs zumachen
5. **Hannes-Browser** → Vor JEDEM Browser-Use Bolle-deviceId verifizieren
6. **Screenshot-Spam** → Erst JS/get_page_text, dann erst Screenshots wenn nötig
7. **Blind-pushen** → Niemals ohne explizite User-Anweisung pushen/deployen
8. **Strategie-Rückfragen** → "Soll ich auch X?" — Auto-Modus durchziehen, User redirected wenn nötig
9. **Background-Spawn-Trigger-Happy** → Bevor du `Agent()` oder `Task()` callst, prüf: Ist das ein mechanischer Lookup (OK) oder ein Urteil (NOT OK)? Lieber selbst lesen wenn unsicher.

---

## Beispiel-Pipeline-Run (diese Session)

7 Batches §-Verifikation, alle 16 Bundesländer durchgearbeitet:

| Batch | Modus | Cities | Bugs gefunden | Cities clean |
|---|---|---|---|---|
| 1 (Round 1) | Helper-V3 Bulk | NRW (10+) | 1 (Bochum/Essen § 8) | 8+ |
| 2 | Helper-V3 240s | HH/M/B | 6 YMYL-Errors | 0 |
| 3 | Self-Verify | S/F/DD | 3 §-Errors Dresden | Stuttgart, Frankfurt |
| 4 | Self-Verify | H/KI/MZ | Hannover §7→§11, Mainz §13→§9 | Kiel |
| 5 | Self-Verify | HB/L/SB | Saarbrücken §5→§6, §22→§21 | Bremen, Leipzig |
| 6 | Self-Verify | A/MD/EF/P | München-Rangfolge Bayerisch | Augsburg, Magdeburg, Erfurt, Potsdam |
| 7 | Self-Verify | KA/HRO/WI | Wiesbaden Widerspruch | Karlsruhe, Rostock |

**Self-Verify (Batches 3–7) war ~3× schneller** als Helper-V3 (Batch 2) bei gleicher Bug-Findungs-Rate. Helper-V3 lohnt sich primär für Gesamt-Page-Reviews, nicht für faktische Punkt-Checks.

---

## Hand-off für neue Sessions

Wenn du neu in das Projekt einsteigst und Helper-V3 nutzen sollst:

1. Lies erst `memory/multi_chat_pipeline_lessons.md` (V2-Vorgänger-Lessons)
2. Lies `memory/feedback_no_score_anchoring.md`
3. Lies `memory/chrome_browser_devices.md` (Bolle vs Hannes!)
4. Lies dieses File
5. Bei §-Verifikation: **Default Self-Verify**, nicht Helper-V3
6. Bei "Wie fühlt sich die Page an?"-Reviews: Helper-V3 mit 240s
7. Fix-Apply IMMER deterministisch per Python-Skript in `_dev/audit/`
8. Commits mit `[skip netlify]` in `content-loop-pipeline`-Branch
9. Deploy NUR auf explizite User-Anweisung "deploy"

Bei Unsicherheit: User fragen ist okay, aber nicht für jede Triviale-Entscheidung. Auto-Modus durchziehen.
