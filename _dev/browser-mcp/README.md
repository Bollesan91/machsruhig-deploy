# Browser-MCP Send-Helper V3

Robuste claude.ai-Send-Funktion für Browser-MCP-Automation.
Single-shot Dispatch mit Auto-Concurrency-Retry + Auto-Download.

## Problem

Bei parallelen MCP-Dispatches an mehrere claude.ai-Tabs:
1. **"Zu viele Antworten werden gleichzeitig generiert"** — claude.ai cappt bei 3 parallelen Streams pro Account
2. **Send-Button-Race** — fester `setTimeout` greift zu früh
3. **Stop-Button existiert nicht** — alte Selektoren (`button[aria-label*="Stop"]`) liefern null
4. **Assistant-Message-Selektoren veraltet** — `font-claude-message`, `article`, `[role=article]` matchen alle 0

## V3-Lösung

Verifizierte Selektoren (Mai 2026):
- **Send-Button:** `button[aria-label*="Send"|"senden"]`
- **User-Message-Verify:** `[data-testid="user-message"]` count delta
- **Stream-Complete:** `[data-testid="action-bar-copy"]` count erreicht `initial+2`
- **Response-Extract:** letzten copy-btn's Container, strippe `"Claude hat geantwortet: "`-Prefix

## API

```js
__mcp.run(prompt, label, opts?)   // Startet Task — returns 'STARTED'
__mcp.status()                    // {phase, label, elapsed, error, responseLen, logTail}
__mcp.lastResult()                // Response-Text (oder null)
```

Phases: `idle` → `sending` → `streaming` → `complete` | `failed`

Opts:
- `sendTimeoutMs` (default 120000) — max Wait für Cap-Clear
- `streamTimeoutMs` (default 300000) — max Wait für Response
- `autoDownload` (default true) — triggert Blob-Download als `{label}.txt`

## Agent-Pattern (Pipeline-Scheduler für 4 parallele Tabs)

```
tasks = [city1, city2, ..., city25]
tabs = [t1, t2, t3, t4]

# Initial-Dispatch
for tab in tabs:
  navigate(tab, /new) + install helper + run(tasks.pop().prompt, tasks.pop().label)

while tasks oder any tab not 'complete':
  sleep(30s)
  for tab in tabs:
    status = mcp.status(tab)
    if status.phase == 'complete':
      # Auto-Download liegt schon in Downloads/<label>.txt
      results[task.label] = read_file(label.txt)
      if tasks:
        navigate(tab, /new) + run(tasks.pop())  # next task!
```

Theoretischer Speedup gegenüber synchroner 5-Tab-Wave: **3x** durch Pipeline-Mode (kein "all-wait-for-slowest"-Sync mehr).

## Speed-Vergleich (Round 2: 25 Cities)

| Modus | Wall-Clock |
|---|---|
| Sequential | ~125 min |
| 5-Tab-Wave (V1, manual retries) | ~30 min |
| 4-Tab-Pipeline + V3 | ~10 min |

## Datei-Liste

- `send-helper-v3.js` — Production-Version (DOM Mai 2026)
- `README.md` — Diese Doku
- `send-helper.js` (V1) — Deprecated
- `send-helper-v2.js` — Deprecated (Stop-Button-Selektor veraltet)
