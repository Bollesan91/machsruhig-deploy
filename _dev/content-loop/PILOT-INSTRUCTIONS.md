# Test-Run Anleitung für Claude Code

**Ziel:** Einmal den Multi-Chat-Loop manuell durchspielen mit **Saarland** als Testkandidat. Du steuerst, Bolle beobachtet. Kein Auto-Pilot, kein Watchdog. Wir wollen sehen ob die Methode inhaltlich funktioniert.

**Aufgabe:** Saarland-Bundesland-Page von Audit-Score 71 + 1 Recheck-Blocker auf Score ≥ 85 + 0 Blocker bringen.

---

## Vorbereitung (du, ohne Browser)

1. `git status` prüfen — sauber? Wenn nicht: `git stash` und melde dich.
2. `git pull` auf `main`.
3. Lies einmal komplett: 
   - `_dev/content-loop/briefings/A-writer.md`
   - `_dev/content-loop/briefings/B-reviewer.md`
   - `_dev/content-loop/briefings/C-adversarial.md`
   - `_dev/content-loop/prompts/` (alle 5 Files)
4. Lies die aktuelle Saarland-Page: `bestattung-in/saarland/index.html`
5. Lies eine fertige Vergleichspage zur Kalibrierung: `bestattung-in/rheinland-pfalz/index.html` — das ist das Ziel-Niveau
6. Lies `_dev/bundesland-recheck.py` — du musst verstehen was die ausgibt
7. Lies `_dev/audit-all-pages.py` — du musst Score auf einzelne Datei beziehen können

Wenn alles gelesen: melde Bolle „Ready für Test-Run". **Stelle keine Architektur-Fragen mehr — wir haben das durchdiskutiert.**

---

## Ablauf: 3 Chats, 6 Runden

Wir nutzen **drei separate claude.ai-Chats** für die kritische Trennung von Schreiben und Bewerten.

### Chat A — der Autor (öffnet Bolle in Chrome)

1. Bolle öffnet `https://claude.ai/new`
2. Bolle paste den **kompletten Inhalt** von `briefings/A-writer.md` als ersten Prompt
3. Worker antwortet idealerweise mit `BRIEFING_OK` (oder ähnlich)
4. **URL des Chats notieren** in `_dev/content-loop/runs/saarland/chats.yaml` (siehe Template unten)
5. Bolle paste **Saarland-Task-Prompt** (siehe `prompts/01-task-saarland.md`)
6. Worker schreibt komplette HTML-Page in einer Antwort
7. **Bolle kopiert den Output** in `_dev/content-loop/runs/saarland/v1-from-chat-A.html`

### Chat B — der Reviewer (frischer Chat, Round 2)

1. Bolle öffnet **neuen** `claude.ai/new` Tab
2. Briefing aus `briefings/B-reviewer.md` einfügen
3. Worker bestätigt
4. URL in chats.yaml notieren
5. Bolle paste Prompt aus `prompts/02-review-as-stranger.md` mit dem v1-HTML als Anhang
6. Worker liefert SCORE + GAP
7. Bolle kopiert die Antwort in `runs/saarland/round-2-review.md`

### Chat A — Round 3 (FIX)

1. Bolle wechselt zurück zu Chat A (URL aus chats.yaml)
2. Paste Prompt aus `prompts/03-fix-with-external-feedback.md` + Round-2-Review von Chat B
3. Worker liefert v2 als HTML
4. Bolle kopiert in `runs/saarland/v2-from-chat-A.html`

### Chat C — Round 4 (Adversarial, frischer Chat)

1. Bolle öffnet **neuen** Chat
2. Briefing aus `briefings/C-adversarial.md` einfügen
3. Worker bestätigt
4. URL notieren
5. Paste Prompt aus `prompts/04-adversarial-review.md` mit v2-HTML
6. Worker liefert 3 SCHWÄCHEN + ehrliche %-Zahl
7. Kopieren in `runs/saarland/round-4-adversarial.md`

### Chat A — Round 5 (FINAL_FIX)

1. Bolle zurück zu Chat A
2. Paste Prompt aus `prompts/05-final-fix.md` + Round-4-Schwächen von Chat C
3. Worker liefert v3
4. Bolle kopiert v3 in `runs/saarland/v3-from-chat-A.html`

### Round 6 — External Validation (du, Claude Code)

1. v3 ins Target kopieren: `cp runs/saarland/v3-from-chat-A.html bestattung-in/saarland/index.html`
2. `python3 _dev/bundesland-recheck.py bestattung-in/saarland/index.html` ausführen, Output speichern in `runs/saarland/round-6-recheck.txt`
3. `python3 _dev/audit-all-pages.py` (oder Single-File-Variante) ausführen, Score für Saarland aus `_dev/AUDIT-REPORT.json` extrahieren, in `runs/saarland/round-6-audit.txt`
4. **Entscheidungs-Logik:**
   - 0 Blocker UND Score ≥ 85 → Erfolg, weiter zu Commit-Schritt
   - Sonst → Round 6 Fix-Loop (siehe unten)

### Round 6 Fix-Loop (max 4 Versuche)

Wenn die Tools rot sind:

1. Bolle zurück zu Chat A
2. Paste Prompt aus `prompts/06-tool-fix.md` mit dem **rohen Tool-Output** drin
3. Worker liefert v4 (oder vN)
4. Du copy ins Target, run Tools nochmal
5. Versuche zählen. Bei Versuch 3: nimm `prompts/06b-escalation.md` (zwingt Diagnose). Bei Versuch 4: `prompts/06c-last-chance.md` (zwingt Kürzung).
6. Wenn nach Versuch 4 immer noch rot → Reject. Letzten Output in `runs/saarland/REJECTED-vN.html` archivieren, `bestattung-in/saarland/index.html` aus git wiederherstellen (`git checkout bestattung-in/saarland/index.html`).

### Commit (nur wenn grün)

1. `git diff bestattung-in/saarland/index.html` zeigen — Bolle review kurz
2. `git add bestattung-in/saarland/`
3. Commit mit Message-Template:
```
[content-loop test] Saarland: Audit 71→XX, Recheck-Blocker 1→0

Test-Run der Multi-Chat-Loop-Methode.
Round-2-Score: NN%
Round-4-Score (adversarial): NN%
Last-Fix-Loops: N
[skip netlify]
```
4. **NICHT pushen.** Bolle entscheidet später per „Ende deploy".

### Run-Log

Nach allem Schreib einen Bericht in `_dev/content-loop/runs/saarland/RUN-REPORT.md` (siehe Template unten). Der ist der wichtigste Output dieses Tests — daraus lernen wir.

---

## chats.yaml Template

Speichern unter `runs/saarland/chats.yaml`:

```yaml
task: saarland
started_at: 2026-MM-DD HH:MM
chats:
  A_writer:
    url: https://claude.ai/chat/<uuid>
    role: schreibt v1, v2, v3, alle Fixes
    opened_at: HH:MM
  B_reviewer:
    url: https://claude.ai/chat/<uuid>
    role: Round 2 SCORE als fremder Reviewer
    opened_at: HH:MM
  C_adversarial:
    url: https://claude.ai/chat/<uuid>
    role: Round 4 ADVERSARIAL als feindlicher Reviewer
    opened_at: HH:MM
```

---

## RUN-REPORT.md Template

```markdown
# Test-Run Saarland — YYYY-MM-DD

## Ergebnis
- Status: completed | rejected | abort
- Final Audit-Score: NN
- Final Recheck-Blocker: N
- Last-Fix-Loops: N
- Commit: <hash> (oder "kein Commit, rejected")

## Round-by-Round

### Round 1 (WRITE in Chat A)
- Dauer: MM Minuten (Worker-Schreibzeit)
- Output-Länge: NN Zeilen, ~NN Wörter
- Auffälligkeiten: …

### Round 2 (SCORE in Chat B — kritisch)
- Score: NN%
- GAP-Punkte: N (1: ..., 2: ..., 3: ...)
- War der Score ehrlich/niedrig? Vergleich mit Bolle-Erwartung
- Hat der fremde Reviewer wirklich Schwächen gefunden, die ein Same-Chat-Selbst-Review verschluckt hätte?

### Round 3 (FIX in Chat A)
- Wurden alle GAP-Punkte adressiert?
- Verschlechterungen anderswo?

### Round 4 (ADVERSARIAL in Chat C — kritisch)
- 3 Schwächen geliefert? Welche?
- Ehrliche Score: NN%
- War Score ≤ Round-2-Score? (Drift-Check)

### Round 5 (FINAL_FIX in Chat A)
- Schwächen umgesetzt?
- Gefühlt: ist die Page jetzt 85+?

### Round 6 (TOOL VALIDATION)
- Recheck Output: …
- Audit Score: …
- Anzahl Fix-Loops bis grün: N
- Welcher Eskalations-Prompt nötig: 06 / 06b / 06c

## Lessons Learned

### Was hat überraschend gut funktioniert
- ...

### Was war schwächer als erwartet
- ...

### Konkrete Fehler / Bugs / Inkonsistenzen
- ...

### Empfehlungen für V2 der Methode
- Briefing-Änderungen: ...
- Prompt-Änderungen: ...
- Workflow-Änderungen: ...

### Token-Verbrauch (geschätzt aus Antwortlängen)
- Chat A: ~NN.000 Token
- Chat B: ~NN.000 Token
- Chat C: ~NN.000 Token
- Total: ~NN.000 Token

### Zeitaufwand
- Total Wall-Clock: NN Minuten
- Davon Bolle-aktiv: NN Minuten
- Davon Worker-rechnet: NN Minuten
```

---

## Hard-Stops während des Runs

Sofort an Bolle melden und stoppen wenn:
- Worker antwortet nicht mit `BRIEFING_OK` nach Briefing-Paste (max 1x neu versuchen)
- Output von Round 1 ist offensichtlich kaputt (kein HTML, oder < 800 Zeilen, oder massive Halluzinationen)
- Worker stellt mehrfach Rückfragen statt zu liefern
- recheck.py oder audit-all-pages.py crashen (Tool-Fehler ist kein Worker-Problem)
- Bolle sagt „Stop"

---

## Was wir NICHT tun

- Nicht autonom durchlaufen — bei jedem Round-Wechsel kurzer Check mit Bolle
- Nicht pushen
- Nicht andere Files anfassen als `bestattung-in/saarland/` und `_dev/content-loop/runs/`
- Nicht Saarland-Page aus git verändern bevor v3 final ist (bestehende Version bleibt als Fallback)
