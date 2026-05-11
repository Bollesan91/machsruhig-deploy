# /loop-Trigger für 45-Städte-Pipeline

## So aktivierst du den autonomen Stadt-Pages-Loop

Im Claude-Code-CLI eintippen:

```
/loop arbeite die naechste unmarkierte Stadt aus _dev/content-loop/STADT-QUEUE.md ab nach _dev/content-loop/MASS-PIPELINE-RECIPE.md. Vollstaendige V2-Pipeline: WebSearch + Quellen-Pack push, Chat A Writer (Branch-Trick), Chat B Review, Chat A v2-Fix, Chat C Adversarial, Chat A v3 Final Fix, v3 nach bestatter/<slug>/index.html, Sitemap update, Status in STADT-QUEUE.md aktualisieren. ScheduleWakeup fuer naechste Stadt (1200s). Stopp wenn alle 45 abgehakt.
```

## Was der /loop macht

1. **Dynamic mode** (kein Intervall) → ich self-pace via ScheduleWakeup
2. **Pro Wakeup**: 1 Stadt komplett (Wallclock ~30-45 min)
3. **ScheduleWakeup**: 1200s nach Push, damit ich vor Cache-Verlust zurückkomme
4. **Stopp**: bei allen 45 abgehakt → KEINE ScheduleWakeup mehr

## Was du als User vorab tun musst

1. **Chrome eingeloggt lassen** auf claude.ai mit Bollesan-Account
2. **Diesen Tab/CLI offen lassen** (oder `/loop` mit cloud-schedule für robust)
3. **Erste Welle 15 Städte** = ~12 Stunden Wallclock
4. **Nach Welle**: ich pause + push main mit Deploy, dann Welle 2

## Welle-Strategie (3 × 15 Städte)

- Nach 15 fertig: main-commit + netlify-deploy
- Nach 30 fertig: dito
- Nach 45 fertig: dito + STADT-Site-Coverage 100%

## Cloud-Schedule-Alternative (empfohlen für robust)

Statt `/loop` mit Session-Bindung:

```
/schedule jede 30 Minuten arbeite die naechste unmarkierte Stadt aus _dev/content-loop/STADT-QUEUE.md ab
```

Das läuft in Anthropic Cloud, auch wenn du den Browser schließt.

## Notfall-Stopp

```
/loop stop
```
oder `TaskStop` für aktive Monitors.
