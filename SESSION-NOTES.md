# Session-Notizen

## Letzte Session
**Datum:** 2026-06-04

## Iter-11/12/13: Stadt-Nav-Fragmentierung (User-Befund "darmstadt broken")

**Befund:** Die 52 `bestatter/<stadt>/`-Seiten hatten **~7 verschiedene Nav-Templates** (Template-Drift über Zeit), nur 25 kanonisch. Visuell kaputt: unstyled Nav (Bullets, gestackt).

- **iter-11** (Commit f9bcc08): erster Fix, Compat-CSS für die `mr-logo`+`<ul>`-Variante → 16 Städte. **War zu eng** — Scan via `class="mr-logo"` verpasste andere Varianten (BEM `mr-nav__brand`/`mr-nav__menu`, `header.mr-nav`-Wrapper, `mr-nav-brand`).
- **iter-12** (Commit 8e2dbeb): **alle 52 normalisiert** — Haupt-Nav-Wrapper (nav ODER header mit `class="mr-nav"`, balanciert über Verschachtelung) durch kanonisches Berlin-Nav ersetzt + garantiertes Nav-/Breadcrumb-CSS injiziert. Script `_dev/normalize-city-nav-iter12.py`. **Lokal vor Deploy verifiziert** (lokaler http.server + Chrome) — fing 2 Script-Bugs (nested-nav, header-Wrapper). Live bestätigt: je 1 Logo, 0 Orphans.
- **iter-13** (Commit b9d7250): Nav **linksbündig** site-weit (121 Seiten), `.mr-nav-inner` `space-between`→`flex-start`. Script `_dev/nav-leftalign-iter13.py`. Live bestätigt.
- **iter-14** (Commit 0f06dea): **BEM-Compat-CSS** für das alte Stadt-Template. User-Befund: Darmstadt-Kernfakten unlesbar. Audit zeigte: ~29 Städte nutzen ein BEM-Markup (`<dl>`-Kernfakten, `mr-friedhof`-Karten, `mr-faq__item`, `mr-footer__*`, `mr-list`, `mr-hero__*`/`mr-section__*`), dessen Original-Stylesheet (`/assets/css/main.css`) **nie eingecheckt** war (iter-10 entfernte die Referenz). Berlins Inline-CSS stylt nur Block-Klassen, keine BEM-Subelemente. Fix: self-contained Compat-CSS (`_dev/bem-compat-css-iter14.py`) auf alle 52 — Kernfakten-Grid + fette Labels, Friedhof-Karten + Hidden-Gem-Callouts, FAQ-Items, BEM-Footer, Listen (wg. globalem `*{padding:0}`). Lokal vor Deploy an Darmstadt verifiziert, live bestätigt.

**Lessons:** (1) Bei "Pattern?"-Fragen IMMER vollständig klassifizieren statt einen Marker raten — Markup ist heterogener als gedacht (nav vs header, BEM, nested). (2) **Pre-Deploy lokal rendern** (`python3 -m http.server` + Chrome auf `http://127.0.0.1:PORT/...`) statt blind auf N Live-Seiten deployen — hat hier 2 Bugs gefangen. (3) Claude-in-Chrome `navigate` erzwingt `https://` → `file://` geht nicht, `http://127.0.0.1` schon.

- **iter-15** (Commit 93a7f89): Nav **auf 7 Kern-Links verschlankt + ausgerichtet** (site-weit, 121 Seiten). User: Nav überladen/„schwebt"/bricht um. Fix: 12→7 Links (Was tun?/Beerdigung/Kosten/Vorsorge/Bestatter/Trauerrede/Notfallkarte — Kosten+Bestatter neu, waren 0.9-Pillars ohne Nav-Link; `/ratgeber/` verworfen weil 301→Startseite; 5 Text-Tools jetzt via Pillars/Footer). `.mr-nav-inner` `max-width:720px` = Inhaltsbreite → einzeilig (57px) + linke Kante bündig mit Text+Breadcrumb (vorher 120px Versatz, jetzt ~20px). Script `_dev/nav-slim-iter15.py`, balancierter Matcher, lokal vor Deploy verifiziert (Stadt+Pillar).

**Noch offen (nächste Session):**
- **3 alt-Template-Pillars OHNE `mr-nav`**: `was-tun-nach-todesfall.html`, `notfallkarte.html`, `danke-bestatter-anfrage.html` — eigenes altes CSS-System (`<nav class="nav">`/`<header class="site">`), bekamen iter-12/15 NICHT (Matcher findet kein `mr-nav`). Sie haben jetzt eine ANDERE Nav als der Rest = Inkonsistenz. **Wichtig:** `was-tun` + `notfallkarte` sind selbst Nav-Ziele! Redesign/Normalisierung dieser 3 auf das Standard-Template = sinnvoller nächster Schritt.
- Mini-Versatz Nav↔Inhalt 20px (Box-Model nav-inner vs .mr-content-Padding) — kosmetisch, optional pixelgenau machen.
- Tote `.mr-nav-brand{}`/`.mr-nav-links{}`-CSS-Reste auf ein paar Städten (harmlos, optional putzen).

---

## Iter-34 (2026-06-03): Tool-Validity-Audit Danksagung + Injection-Fix

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

### Fix (deployed auf main, 2 Stufen) — betrifft alle 3 KI-Tools (shared `buildUserMessage`)
`netlify/functions/ai-rede.js`:
1. **Prompt-Guard** (15d9fd6 / Merge 4535397): `INJECTION_GUARD` an jeden System-Prompt; User-Message in `<eingaben>…</eingaben>` gekapselt.
   → Live-Test: Prompt-Leak weg, aber **Injection nur teilgeblockt** (Rezept sickerte durch). Prompt-Guard allein reicht auf llama-3.3-70b NICHT.
2. **Strukturelle Input-Bereinigung** (d09c549): kurze Felder (name/relationship/religion/…) einzeilig + auf 70 Zeichen gekappt, Freitext auf 1500.

### Live-Verifikation auf Produktion — BESTANDEN ✅ (03.06.2026)
Direkt-curl gegen `https://machsruhig.de/.netlify/functions/ai-rede` (www→apex-Redirect beachten, curl -L oder apex direkt!):
- Injection im Namensfeld → Modell **verweigert + liefert würdevolle Danksagung**, kein Rezept/BANANE/Prompt-Leak.
- Legit kurz + langer Adelsname (52 Z.) → sauber, Name vollständig erhalten.

## Groq Free-Tier entschieden (03.06.2026)
User bestätigt: **Groq Free-Tier** (keine Karte) → Abuse-Risiko = **Verfügbarkeit** (14.400 req/Tag org-weit), NICHT Kosten. Proportionaler Schutz = **eine Cloudflare-Rate-Limit-Regel** auf `/.netlify/functions/ai-rede` (~20/min/IP) + Bot Fight Mode — User-Aktion im Dashboard. KEIN Turnstile/Origin-Secret (Over-Engineering ohne Geld-Risiko). Erst bei aktiviertem Billing nötig. Detail-Memory: groq_free_tier_decision.

## Trauerrede Re-Audit + Fixes (03.06.2026, deployed)
Welle-2+3-Hero + KI-Integration auditiert. **Validity-Kern PASS** (Iter-33-Defekt behoben: echte KI, Tippfehler-Korrektur, keine Halluzination, 7 Tonarten, kohärent, ehrliche Zitat-Attribution).
**3 Defekte gefunden + gefixt (Commits e3af23d, ca5b956):**
1. Seite hatte **0 `<h1>`** → Hero zu `<h1>`, Ergebnis-Titel zu `<h2>` (1 H1 gesamt). Live ✅
2. Hero sagte **„sechs Tonarten"** → „sieben" (sind 7). Live ✅
3. **Längen-Promise-Gap**: Frontend versprach 400–600/600–1000/1000–1500 W. Live gemessen: kurz ~340, mittel ~627, lang ~598–641 — **mittel≈lang, Modell cappt ~640 W**. Backend-Zielzahl hochsetzen brachte nichts (Modell-Limit, kein Token-Limit; max_tokens trotzdem 2000→4000 als Schutz). Richtige Korrektur = **Frontend ehrlich kalibriert** auf ~350–500/500–700/650–850 W + Backend-Ziele realistisch.

**Trauerrede offene/weiche Funde:**
- Weltlicher Abschluss nutzte mild-religiöses „Seele ruhe in Frieden" trotz religion=nein — nicht gefixt.
- humorvoll liefert bei dünnem Input kaum echten Humor (ununterscheidbar von würdevoll).
- mittel vs. lang real fast identisch — echte Differenzierung bräuchte Multi-Section-Assembly (überzogen für Free-Draft-Tool).
- **Long-Field-Injection (character/memory) bei Trauerrede/Abschiedsbrief NICHT geschlossen** — Clamp greift nur kurze Felder. Auf Free-Tier akzeptiert (Abuse=Verfügbarkeit → Cloudflare-Limit deckt's; Content-Hijack selbstverschuldet).

## Nächste Schritte
- **Cloudflare-Rate-Limit-Regel setzen** (User, Dashboard) — der eine offene Abuse-/Verfügbarkeits-Schutz.
- Injection-Restrisiko (≤70-Z. bei Danksagung; lange Felder bei Trauerrede/Abschiedsbrief) — auf Free-Tier bewusst akzeptiert, dokumentiert.
- Phase 3 Abschiedsbrief KI-Polish-Button (~30 Min, optional).
- Optional: Danksagung Szenario 1 (Vent-Text ceremony) auf neuem Build gegenchecken.
- Branch `fix/ai-injection-guard` gelöscht (gemerged).

## Strukturelle Lessons (kumulativ, neu 2026-06-03)
- **Prompt-Injection ist eine Tool-Validity-Klasse**, die der SEO-Reviewer NIE sieht. Jedes KI-Tool adversarial mit Injection im Freitext-/Namensfeld testen (Zeilen wie "Ignoriere alle Anweisungen…"). Roh interpolierte User-Inputs ohne Daten-Grenze = sofortiger Kaper + Prompt-Leak + Abuse-Vektor (Endpoint als Gratis-LLM-Proxy, nur durch IP-Rate-Limit gedrosselt).
- Server-seitige Netlify-Functions sind **nicht lokal verifizierbar** (Secret-Key liegt in Netlify) — Verifikation braucht Deploy (Branch-Preview oder Produktion).
- machsruhig.de hängt hinter **Cloudflare** → Netlify-Site-Slug von außen nicht ermittelbar; Branch-Preview-URL nur über Netlify-Dashboard.

## Frühere Lessons (Iter-33)
- Helper-V3-SEO-Audit misst Hülle, NICHT Tool-Substanz → Tools brauchen Doppel-Audit (SEO + Tool-Validity).
- JSX-Tools mit in-Browser-Babel: `<br>`/`<hr>`/`<img>` IMMER self-closing. Live-Smoketest nach jedem Deploy Pflicht.
- raw.githubusercontent.com Edge-Cache verfälscht Audits — Live-File-Verification Standard.
