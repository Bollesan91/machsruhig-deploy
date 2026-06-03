# Session-Notizen

## Letzte Session
**Datum:** 2026-06-03

## Was wurde gemacht (Iter-34: Tool-Validity-Audit Danksagung + Injection-Fix)

### Doppel-Pflicht-Audit Danksagung nach Welle-2+3-Deploy
Welle 2+3 (Commit 8b4f729: Hero-Block + Auto-Generate-All-3) live verifiziert via Chrome-MCP (Bolle-Device).

**Funktionaler Smoketest — PASS:**
- `#app` rendert (Hotfix `<br/>` hält), keine weiße Seite
- Keine Babel/JSX/React-Console-Errors (nur Extension-Noise)
- Wizard 3 Schritte OK, Personalisierung (Name+Beziehung) korrekt
- Auto-Generate aller 3 Varianten (formal/persönlich/kurz) funktioniert
- Live-KI bestätigt: `POST /.netlify/functions/ai-rede` → 200, kein Template-Fallback
- "✨ Neu generieren" liefert frischen, abweichenden Text

**Tool-Validity-Audit (adversariale Bedienung) — FAIL → gefixt:**
- Szenario 1 (Garbage-in, Vent-Text im Detailfeld): Schulden/"langweilig" gefiltert, ABER weicher Leak — Var. 3 schrieb "Trotz der nicht immer einfachen Beziehung…" in die öffentliche Karte.
- Szenario 2 (Prompt-Injection im **Namensfeld**): HARTER FAIL — Injection kaperte alle 3 Varianten komplett (Output = Pfannkuchen-Rezept) + **voller System-Prompt-Leak** ("REGELN:…").

### Fix (deployed auf main, Commit 15d9fd6 / Merge 4535397)
`netlify/functions/ai-rede.js` — betrifft **alle 3 KI-Tools** (trauerrede/danksagung/abschiedsbrief, shared `buildUserMessage`):
- `INJECTION_GUARD` an jeden System-Prompt angehängt (Daten-≠-Anweisung-Grenze, Rollen-Lock, kein Prompt-Leak, keine Übernahme negativer Angaben)
- User-Message in `<eingaben>…</eingaben>` gekapselt
- Node-Syntax-Check OK

## Nächste Schritte
- **Live-Verifikation auf Produktion** nach Deploy-Build: Injection-Test (Pfannkuchen-Szenario) gegen www.machsruhig.de erneut fahren → muss jetzt würdevolle Danksagung statt Rezept liefern. **Noch offen, falls Build bei Session-Ende nicht fertig war.**
- Branch `fix/ai-injection-guard` kann nach erfolgreicher Verifikation gelöscht werden.
- Phase 3 Abschiedsbrief KI-Polish-Button (~30 Min, optional)

## Strukturelle Lessons (kumulativ, neu 2026-06-03)
- **Prompt-Injection ist eine Tool-Validity-Klasse**, die der SEO-Reviewer NIE sieht. Jedes KI-Tool adversarial mit Injection im Freitext-/Namensfeld testen (Zeilen wie "Ignoriere alle Anweisungen…"). Roh interpolierte User-Inputs ohne Daten-Grenze = sofortiger Kaper + Prompt-Leak + Abuse-Vektor (Endpoint als Gratis-LLM-Proxy, nur durch IP-Rate-Limit gedrosselt).
- Server-seitige Netlify-Functions sind **nicht lokal verifizierbar** (Secret-Key liegt in Netlify) — Verifikation braucht Deploy (Branch-Preview oder Produktion).
- machsruhig.de hängt hinter **Cloudflare** → Netlify-Site-Slug von außen nicht ermittelbar; Branch-Preview-URL nur über Netlify-Dashboard.

## Frühere Lessons (Iter-33)
- Helper-V3-SEO-Audit misst Hülle, NICHT Tool-Substanz → Tools brauchen Doppel-Audit (SEO + Tool-Validity).
- JSX-Tools mit in-Browser-Babel: `<br>`/`<hr>`/`<img>` IMMER self-closing. Live-Smoketest nach jedem Deploy Pflicht.
- raw.githubusercontent.com Edge-Cache verfälscht Audits — Live-File-Verification Standard.
