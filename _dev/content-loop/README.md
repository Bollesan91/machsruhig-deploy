# Content-Loop Test-Run für machsruhig.de

## Ziel dieses Tests

**Einmal** den Multi-Chat-Loop manuell durchspielen mit Saarland. Sehen, ob die Methode inhaltlich funktioniert, bevor wir Auto-Pilot bauen.

**Dies ist KEIN nächtlicher Auto-Run.** Das ist ein Live-Test mit Bolle dabei, gesteuert von Claude Code.

## Was hier gebaut ist

```
_dev/content-loop/
├── README.md                       (diese Datei)
├── PILOT-INSTRUCTIONS.md           ← Claude Code Anleitung für den Test
├── briefings/
│   ├── A-writer.md                 → Chat A System-Prompt
│   ├── B-reviewer.md               → Chat B System-Prompt (fremder Reviewer)
│   └── C-adversarial.md            → Chat C System-Prompt (feindlicher Reviewer)
├── prompts/
│   ├── 01-task-saarland.md         Round 1 in Chat A
│   ├── 02-review-as-stranger.md    Round 2 in Chat B
│   ├── 03-fix-with-external-feedback.md  Round 3 in Chat A
│   ├── 04-adversarial-review.md    Round 4 in Chat C
│   ├── 05-final-fix.md             Round 5 in Chat A
│   ├── 06-tool-fix.md              Round 6 (Versuch 1+2) in Chat A
│   ├── 06b-escalation.md           Round 6 (Versuch 3) in Chat A
│   └── 06c-last-chance.md          Round 6 (Versuch 4) in Chat A
├── runs/
│   └── saarland/                   ← wird beim Test angelegt
│       ├── chats.yaml              URL-Tabelle der 3 Chats
│       ├── v1-from-chat-A.html
│       ├── round-2-review.md
│       ├── v2-from-chat-A.html
│       ├── round-4-adversarial.md
│       ├── v3-from-chat-A.html
│       ├── round-6-recheck.txt
│       ├── round-6-audit.txt
│       └── RUN-REPORT.md           ← der wichtigste Output
└── logs/                           später für Auto-Pilot
```

## Die 3-Chat-Architektur (warum)

Round 2 (Self-Score) und Round 4 (Adversarial) sind die kritischen Bewertungs-Runden. Im selben Chat wie die Schreibrunde (A) verteidigt der Worker unbewusst sein eigenes Werk → Sycophancy → schlechte Bewertung. 

Lösung: **Bewertung in fremdem Chat ohne Schreib-Kontext.**

- Chat A schreibt (v1, v2, v3, alle Tool-Fixes)
- Chat B bewertet v1 als Fremder (Round 2)
- Chat C bewertet v2 als feindlicher Reviewer (Round 4)

Jede Bewertung ist sycophancy-frei. Jedes Schreiben hat den Kontext der vorherigen Iterationen.

## Wie der Test abläuft

Bolle sagt zu Claude Code: „Lies PILOT-INSTRUCTIONS.md und mach den Saarland-Test."

Claude Code:
1. Liest die Anleitung + alle Briefings + Prompts
2. Liest die aktuelle Saarland-Page + RP-Page als Vergleich
3. Liest recheck.py + audit-all-pages.py um Tool-Outputs zu verstehen
4. Sagt: „Ready für Test-Run, Bolle dran"

Bolle:
1. Öffnet Chat A in Chrome, paste Briefing A, paste Task
2. Notiert URL in chats.yaml
3. Kopiert Output an Claude Code, der speichert in v1-from-chat-A.html
4. Öffnet Chat B, paste Briefing B, paste v1 als Review-Task
5. Notiert URL, kopiert Output → round-2-review.md
6. Zurück zu Chat A → Round 3 → v2
7. Chat C → Round 4 → adversarial.md
8. Chat A → Round 5 → v3
9. Claude Code: copy v3 ins Target, run Tools
10. Bei rot: Round 6 Fix-Loop (max 4)
11. Bei grün: Commit (kein Push)
12. Claude Code schreibt RUN-REPORT.md

## Was wir aus dem Test lernen wollen

- Funktioniert die Multi-Chat-Methode inhaltlich? Ist Round 2 in Chat B wirklich strenger als Round 2 im selben Chat A?
- Erreichen wir Score 85+ ohne dass Bolle inhaltlich nachbessert?
- Wo stolpert die Methode? An welchen Stellen muss Bolle eingreifen, die wir später automatisieren müssten?
- Wie viel Zeit / Token kostet ein Run?
- Welche Briefings/Prompts sind zu vage, zu eng, zu lang?

Dieser Test ist die Grundlage für die V2-Entscheidung: lohnt sich Auto-Pilot überhaupt? Wenn die Methode bei 1 Page schon hakt, würde Auto-Pilot nichts retten.

## Was der Test NICHT ist

- Kein Auto-Pilot
- Keine Browser-Automatisierung
- Keine Nacht-Maschine
- Kein Push auf live
- Keine Skalierung auf andere Bundesländer / Städte / Tools

## Nächste Schritte je nach Ergebnis

**Wenn Test grün:** 
- RUN-REPORT auswerten
- Briefings/Prompts iterieren wo nötig
- Hessen + NRW als zweiter manueller Test (anderer Tag)
- Erst dann Auto-Pilot diskutieren

**Wenn Test gelb (knapp gescheitert):**
- Diagnose: war es die Methode oder Saarland-spezifisch?
- 1-2 Briefings/Prompts schärfen, nochmal Saarland

**Wenn Test rot:**
- Methode überdenken
- Eventuell Round-Anzahl reduzieren
- Eventuell Single-Chat-Modus mit besserem Adversarial-Prompt testen
