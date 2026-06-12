# Helfer V4.1 — lernendes Qualitätssystem mit Tab-Reviewern

> **Gilt ab 12.06.2026 für machsruhig (und sinngemäß machsleicht). Ersetzt Helfer-V3 als Standard-Verfahren; `_dev/HELPER-V3.md` bleibt als Referenz (Linsen-Tabelle + Prompt-Baukasten werden hier weiterverwendet).**
> Herkunft: Erbenradar-„Helfer v4" (Bolle-Freigabe 11.06.2026), angepasst nach Bolle-Entscheid 12.06.: **claude.ai-Tab-Reviewer und Scores bleiben** — mit den Leitplanken aus der Loop-Nacht 10./11.06. (12+ Review-Runden, Befunde dokumentiert in `docs/LEKTIONEN.md`).
> Ziel: gleiche oder bessere Aufdeckungsleistung bei 2–3 Anfass-Runden pro Seite statt ~10 — hohe Qualität UND Tempo.

## Stufe 0 — VOR dem Schreiben (verhindert statt findet)

1. **`_dev/docs/LEKTIONEN.md` lesen** — destilliertes Findings-Gedächtnis aller Reviews. Pflicht-Input für jeden Schreibenden (Haupt-Claude).
2. **Jede Norm/Zahl mit Rechtsfolge primärverifizieren, BEVOR sie geschrieben wird**: gesetze-im-internet.de / Landesrecht-Portale / amtliche Satzungen via WebFetch oder Chrome-Volltext. Sekundärquellen (Kanzlei-Blogs, Bestatter-Seiten, auch eigene Strategie-Doks) sind nie Beleg. Kanonische Kostenspannen NUR aus `/methodik#kostenmodell`.
3. Verifizierte Wortlaute/Werte notieren → gehen als **„heute primärverifiziert — dazu keine Findings nötig"-Block** in den Review-Prompt.

## Stufe 1 — Deterministische Gates (Sekunden, keine Sycophancy)

- **`python _dev/scripts/lint-site.py`** vor jedem Review und jedem Deploy. **0 FAIL ist Pflicht.** Prüft (v1): tote interne Links, FAQ-sichtbar↔JSON-LD-Parität, €-Beträge im JSON-LD die im sichtbaren Text fehlen, verbotene Strings (`_dev/config/lint-verboten.txt` — wächst aus LEKTIONEN), Umami-Mehrfacheinbindung, `var(--mr-*)` ohne Fallback auf Standalone-Seiten, verschachtelte `@media`, doppelte IDs, JSON-LD-Parsebarkeit.
- Bei Fix-Skripten zusätzlich (bewährt): alle Asserts (Tag-Balance, Soll-Reihenfolge, JSON-LD-Parse) **VOR** dem Datei-Write; ein Write am Ende.
- **Was der Linter fangen kann, ist kein Reviewer-Thema mehr** — und kein zulässiger Reviewer-Befund (steht im Prompt).

## Stufe 2 — EINE breite Review-Welle (Tab-Reviewer, scharfer Prompt)

- **Reviewer = frischer claude.ai-Tab** (Chrome-MCP, Bolle-Device `2bee5aa2-…`, starkes Modell), target-blind, kennt weder Autor noch Vorgeschichte. Subagents bleiben für Review/Rewrite verboten (Memory-Stand; Aufhebung nur nach dem gepaarten Experiment, s. unten).
- **Branch-Trick, gehärtet — wann welcher Modus:**
  - **Mehr-Runden-Inhaltsarbeit** (Seiten-Rework, neue Seiten, Daten-Assets, alles mit Review-Schleifen): eigener Arbeits-Branch (`verdichtung/…` bzw. `content-loop-pipeline`), Commits mit `[skip netlify]`. Reviewer liest die **Commit-SHA-raw-URL** (`raw.githubusercontent.com/<user>/<repo>/<sha>/<pfad>`) — **nie Branch-URLs**, der Edge-Cache (~5 min) serviert sonst alte Stände (belegt: R3-Daten-PR). Merge auf main erst bei Gate-grün → spart Netlify-Builds, hält main deploybar, und Zwischenstände erreichen nie die Live-Site.
  - **Doc-/Tooling-only** (LEKTIONEN, Linter, Specs, SESSION-NOTES): direkt main mit `[skip netlify]` — kein Review-Zyklus nötig, Branch wäre Overhead.
  - **Mehrere fertige Artefakte im Loop**: lokal auf main sammeln, EIN Push am Ende (Builds bündeln — Memory feedback_batch_main_push), sofern kein Zwischen-Live-Verify nötig ist.
  - Bei Trust-/Matrix-Claims zusätzlich die Tool-Code-URLs unter demselben SHA mitgeben.
- **Prompt = maßgeschneidert + super scharf** (Bolle-Direktive 11.06., Baukasten in HELPER-V3.md): Ist-Analyse + Stellen-Inventar vorab; Rolle + reale Fallhöhe; kanonische Referenzen MITGEBEN; nummerierter Winkel-Katalog (alle typ-relevanten Linsen in EINER Welle — Recht, Zahlen-Konsistenz übers ganze Inventar, Nutzerführung, Struktur/Schema, YMYL-Ton); **Verifikations-Verben** („rechne nach", „recherchiere das Az.", „prüfe Links gegen den Repo-Baum", „diffe FAQ vs. JSON-LD"); **expliziter Recherche-Auftrag** (die wertvollsten Funde der Loop-Nacht kamen aus Reviewer-Websearch).
- **Reviewer-Pflichten im Prompt:** wörtliches Zitat je Finding (ohne Zitat zählt es nicht) · Kategorien **MAJOR / MINOR / UNSICHER** (bei Norm-Zweifel UNSICHER statt raten) · „heute primärverifiziert"-Block respektieren · dokumentierte False-Positives aus `_dev/docs/OFFENE-REVIEW-PUNKTE.md` nicht erneut melden · Linter-Themen nicht melden.
- **Score: ja, als Telemetrie.** Score 0–100 + Einzeiler im Verdikt. Drei Leitplanken: kein Ziel-/Vor-Score im Prompt (Anti-Anchoring) · vergleichbar NUR innerhalb derselben Review-Konversation · **der Score entscheidet nie** — das Gate ist maschinell (Stufe 3). Fortschritt wird primär als **Befund-Tabelle** berichtet (MAJOR/MINOR/UNSICHER gefunden → verifiziert → gefixt → offen, Score als letzte Spalte).
- Parallelität: Standard **1 Tab** pro Artefakt; nur bei Hochrisiko (Daten-Asset, Engine/Tool-Validity, Pressetext) 2–3 parallele Linsen-Tabs; max. 3 Streams (Rate-Limit). **Tempo-Regel: Während ein Review läuft, arbeitet Haupt-Claude am nächsten Artefakt weiter** (Pipeline statt Warten — so lief die Loop-Nacht).

## Stufe 3 — Verifikation, Fix, Diff-Re-Check, maschinelles Gate

1. **Haupt-Claude verifiziert JEDES Finding selbst gegen die Primärquelle**, bevor gefixt wird — Reviewer irren in beide Richtungen (belegt: „toter PM-Link" war 200; SH-Frist-Korrektur war korrekt). Verworfene Findings → `OFFENE-REVIEW-PUNKTE.md`.
2. Fixes deterministisch (Python-Skript in `_dev/audit/` bei ≥3 Stellen; Asserts vor Write). Danach Linter erneut.
3. **Re-Review nur auf den Diff** (Mini-Prompt im selben Tab: „Stichprobe auf diese N Stellen genügt — GO/NO-GO?"). Fix-induzierte Fehler sind die häufigste MAJOR-Quelle späterer Runden — nie ungeprüft eine neue Vollrunde drehen.
4. **Gate „fertig" (maschinell entscheidbar):** 0 offene MAJORs **+** Linter grün **+** Browser-Smoke (DOM/JSON-LD/Tool-Durchlauf end-to-end mit Sichtbarkeits-Asserts vor jedem Klick). Tools zusätzlich: Doppel-Audit (SEO + Live-Validity) bleibt Pflicht.
5. Volle Site-Wellen (alle Seiten, mehrere Runden) nur als Meilenstein vor einem Launch — nicht je Iteration.

## Gedächtnis (das lernende Element)

- Nach jeder Welle: neue Findings-**Muster** (nicht Einzelfälle) → `_dev/docs/LEKTIONEN.md`; verworfene False-Positives → `_dev/docs/OFFENE-REVIEW-PUNKTE.md`; mechanisierbare Muster → neuer Linter-Check bzw. `lint-verboten.txt`-Eintrag. Beide Docs sind Pflichtteil jedes Schreib- UND Review-Prompts — so wird Seite 12 besser als Seite 1.

## Schreib-Agents

- **YMYL-Texte (machsruhig komplett, Erbenradar-Recht): Haupt-Claude schreibt selbst.** Stufe-0-Verifikation ist nicht delegierbar.
- Subagents erlaubt nur: read-only Explore, Recherche-Sammlung (Rohmaterial, kein Beleg), Plan ohne Code-Generierung. (Schreib-Agents für Nicht-YMYL: offen, Bolle-Entscheid steht aus — machsleicht-Verbot gilt bis dahin.)

## Loop-Betrieb (autonome Abarbeitung mehrerer Artefakte)

Bewährt in der Loop-Nacht 10./11.06. (13 Ränge unbeaufsichtigt):

- **Aktivierung:** Bolle beauftragt einen Loop („Loop starten", `/loop`). Stopp-Kriterium IMMER vorab fixieren (Ziel erreicht ODER Bolle schreibt). Vor einem autonomen Stopp: PushNotification mit Einzeiler-Ergebnis.
- **Taktung (zweigleisig):** Primäres Wecksignal = Background-Sleep (`sleep 180–260 && echo MARKER`, run_in_background → task-notification). **Zusätzlich IMMER ScheduleWakeup als Fallback** (Sentinel `<<autonomous-loop-dynamic>>`), Delay ~270 s während aktiver Reviews — bewusst unter dem 300-s-Prompt-Cache-Fenster. Bei Leerlauf/reinem Warten: 1200–1800 s.
- **Pipeline-Regel:** Während ein Tab-Review läuft, arbeitet Haupt-Claude am nächsten Artefakt (Ist-Analyse, Fix-Skripte, Linter) — nie idle warten.
- **Pro abgeschlossenem Artefakt:** Befund-Tabelle + SESSION-NOTES-Zeile, Review-Tabs schließen, Branch gemäß Branch-Trick-Matrix mergen/sammeln, Live-Verify nach Deploy (curl-Greps auf neue + entfernte Strings).
- **Reviews lesen:** Tab-Status per JS (`data-is-streaming`, letzter `font-claude-response`-Block), URLs/Sonderzeichen vor Ausgabe strippen (Privacy-Filter). Senden: `execCommand('insertText')` + separater Send-Klick — nie Ctrl+V (Diktiermodus).

## Offenes Experiment (entscheidet die Reviewer-Frage empirisch)

Gepaarter Test auf denselben 2–3 Artefakten: Tab-Reviewer vs. Recherche-befugte, zitatpflichtige Fable-Subagents. Metrik: **verifizierte MAJORs pro Welle** (+ Wandzeit, Token). Gewinner wird Stufe-2-Standard; erst danach werden die Subagent-Verbots-Memories angefasst.

## YMYL-Verschärfung (unverändert)

- Jede Zahl mit Rechtsfolge braucht vor Veröffentlichung einen Primärquellen-Treffer.
- Kostenspannen: einzige Quelle ist das kanonische Modell (`/methodik#kostenmodell`); jede Seite, die Spannen nennt, verlinkt dorthin.
