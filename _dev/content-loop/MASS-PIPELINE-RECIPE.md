# Mass-Pipeline Recipe (45 thin-content cities → elite)

**Verwendung im /loop dynamic mode:**
```
/loop arbeite die naechste unmarkierte Stadt aus _dev/content-loop/STADT-QUEUE.md ab nach diesem Recipe. Stopp wenn alle 45 abgehakt.
```

## Stadt-Pipeline-Phasen (1 Stadt = ~1h Wallclock im /loop)

### Phase A: Recherche (5 Min)
1. Lies STADT-QUEUE.md → erste unmarkierte Stadt = `<slug>`
2. WebSearch parallel (4-6 Queries):
   - "<slug> Hauptfriedhof Geschichte prominente Gräber"
   - "Friedhöfe <slug> Anzahl städtisch Friedhofsamt Gebühren"
   - "Bestattungskosten <slug> 2025 Erdbestattung Feuerbestattung"
   - "<Bundesland> Bestattungsgesetz Paragraphen Höchstfrist Sargpflicht" (nur falls BL-Page nicht existiert)
3. Quellen-Pack nach `_dev/content-loop/runs/<slug>/quellen-pack.md` schreiben
4. Push auf content-loop-pipeline
5. Status: Quellen-Pack live → raw-URL für Pipeline verfügbar

### Phase B: Pipeline (Chrome-MCP, ~45 Min Wallclock parallel)
6. Tab-Setup (4 neue Tabs):
   - Tab A: Chat A Writer
   - Tab B: Chat B Reviewer
   - Tab C: Chat C Adversarial
   - Tab D: ggf. Verify/Reserve
7. Chat A v1: konsolidierter Prompt mit Brief-URL + Task-URL via JS insertText
8. Background-Sleep 240s
9. v1 extrahieren (`<pre code>` oder Artifact-Codeblock), push
10. Chat B Review (Branch-Trick raw-URL)
11. Background-Sleep 180s
12. Review extrahieren, push
13. Chat A v2 mit Review-URL
14. Background-Sleep 240s
15. v2 extrahieren, push
16. Chat C Adversarial mit v2-URL
17. Background-Sleep 180s
18. Adversarial extrahieren, push
19. Chat A v3 Final Fix mit Adversarial-URL
20. Background-Sleep 240s
21. v3 extrahieren, push

### Phase C: Deploy-Prep (5 Min)
22. `cp _dev/content-loop/runs/<slug>/v3-from-chat-A.html bestatter/<slug>/index.html`
23. Sitemap update: `<slug>` von priority 0.6 → 0.7, lastmod heute
24. Robots-meta in bestatter/<slug>/index.html: `noindex` → `index,follow`
25. STADT-QUEUE.md: Checkbox [x] + finalen Score notieren
26. Push content-loop-pipeline + main mit `[skip netlify]`
27. ScheduleWakeup für nächste Stadt (Verzögerung 60s)

### Phase D: Pause + Re-trigger
28. Wenn Stadt erfolgreich abgeschlossen: ScheduleWakeup mit gleichem /loop-Prompt
29. delaySeconds: 1200-1800 (cache-bewusst)
30. Wenn alle 45 abgehakt → KEINE ScheduleWakeup mehr → /loop endet
31. Bei 5-Pages-Block: `git push main` mit Netlify-Deploy (Welle 1/2/3 jeweils 15 Pages → 3 Deploys)

## Anti-Patterns (vermeiden)
- ❌ Sequentiell ohne parallele Tabs → zu langsam
- ❌ Artifact-Modus für Hamburg-ähnliche Stadtstaaten → bitte „kein Artifact, nur Codeblock" im Prompt
- ❌ Chat B im selben Konversations-Chat für 2 Städte → Sycophancy-Risiko → neuer Tab pro Stadt
- ❌ Quellen-Pack > 4 KB → zu viel Tokens → kompakt halten
- ❌ Stopp-Regel ignorieren → Plateau bei Score 83 ist OK

## Rate-Limit Handling
- Max 4 parallel Streams pro Anthropic-Account
- Bei „Zu viele Antworten gleichzeitig" → 60s warten, dann queued Tab erneut absenden
- Tab-Anzahl im Browser im Auge behalten — alle paar Städte ältere Tabs schließen

## Deploy-Welle-Strategie
- Nach Welle 1 (15 Städte): main commit + netlify deploy → 15 neue Pages live
- Nach Welle 2 (30 Städte): netto +15 Pages live
- Nach Welle 3 (45 Städte): finaler netto +15
- Jede Welle: SESSION-NOTES.md auf main mit Audit-Scores aller 15

## Memory-Update
- Nach jedem deploy: Memory `feedback_*.md` falls neue Erkenntnisse über Pipeline (z.B. Hamburg-Artifact-Issue, Frankfurt-Quellen-Schwindel-Pattern)
