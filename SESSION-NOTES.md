# Session-Notizen

## Letzte Session
**Datum:** 2026-06-10 (Session B: Datenschutz-KI)

## Session 2026-06-10 B: Datenschutz-KI-Luecke geschlossen (3 Helper-V3-Runden bis GO)

**Anlass:** Task-Chip aus Session A — datenschutz.html erwaehnte die KI-Verarbeitung (Groq/USA) der drei Tools trauerrede/danksagung/abschiedsbrief nicht (0 grep-Treffer fuer groq|ai-rede|kuenstliche intelligenz).

**Ergebnis: Branch `datenschutz-ki-abschnitt` (HEAD c15c0ff), Helper-V3 GO — NICHT auf main gemergt, wartet auf User-Freigabe.**

**Was drin ist (3 Commits, alle [skip netlify]):**
1. **datenschutz.html**: Neuer **§7 „KI-gestuetzte Textentwuerfe"** — Zweck, Empfaenger Groq Inc. (USA) via Netlify-Function ai-rede, Llama 3.3, Opt-in/Freiwilligkeit, keine Speicherung bei uns, IP nur In-Memory-Rate-Limit, **Art. 6 I a + Art. 49 I a DSGVO** mit USA-Risikohinweis, Groq-Retention vorsichtig („nach eigenen Angaben", Default bis 30 Tage Abuse-Logs, kein Training laut DPA). §2/§6 behaupteten faelschlich „Trauerrede-Generator laeuft vollstaendig im Browser" — korrigiert. Abschnitte umnummeriert (1–12), Stand Juni 2026.
2. **Alle 3 Tool-Seiten** (Review-R1-Pflichtkorrekturen): „einmalig an Groq" → „bei jeder Generierung" (jede Regeneration = neuer Call!), **echter Widerrufs-Button** an `window.mrAI.revokeConsent()` in den Privacy-Notices (vorher Phantom-Opt-out — Art. 7 III!), „Opt-in vor jeder Generierung" → „beim ersten Mal, danach direkt", „laut Privacy-Policy" → „nach eigenen Angaben" (Quelle ist das DPA).
3. **Abschiedsbrief-FAQ** (Review-R2): „Werden meine Worte gespeichert?" — sichtbare FAQ + JSON-LD wortgleich um KI-Ausnahme ergaenzt, JSON-LD validiert.

**Fix-Skripte:** `_dev/audit/fix-ki-datenschutz-konsistenz.py` + `-r2.py` (exakte String-Matches, kein Multi-Line-Regex auf JSON-LD). Lokal gerendert + getestet: Babel fehlerfrei, Revoke-Button funktioniert end-to-end (Consent-Key ist `mr-ai-consent-v1`, NICHT `mr-ai-consent` wie der Kommentar in mr-ai.js behauptet).

**Review-Kette** (claude.ai-Tab „Datenschutzerklaerung-Audit fuer KI-Tools", Opus 4.8, kein Anchoring, Reviewer verifizierte selbst gegen ai-rede.js + Groq-Doku): R1 NO-GO (5 Pflichtkorrekturen, wichtigster: „ausschliesslich zur Erstellung der Antwort" staerker als Groqs Default) → R2 NO-GO (uebersehene Abschiedsbrief-FAQ in 2 Stellen) → **R3 GO, keine neuen Widersprueche**.

**methodik.html** war schon korrekt (Session A) — der dortige Verweis auf die Datenschutzerklaerung laeuft jetzt nicht mehr ins Leere.

**OFFEN (User, nicht Code):**
- **Merge `datenschutz-ki-abschnitt` → main** (= Deploy der DSGVO-Texte; solange nicht gemergt, fehlt §7 live!)
- **Zero-Data-Retention in Groq-Console aktivieren** (Data Controls) — dann strenger als §7 verspricht
- AV-Vertraege Groq + Netlify pruefen (Reviewer B-1)
- Langfristig: Fachanwalt ueber §7 + Consent-Mechanik (YMYL)

---

## Session 2026-06-10: Daten-PR-Seite presse-fest (Modell V2 + 6 Helper-V3-Runden bis GO 85)

**Anlass:** Review der neuen /bestattungskosten-nach-bundesland (Daten-PR-Asset fuer Backlink-Phase).

**Ablauf (7 Wellen auf Branch fix/bundesland-quickfixes, am Ende gemerged + deployed):**
1. **Quickfixes:** Site-weiter FAQ-Doppelmarker-Fix (site.css hatte ::before UND ::after "+" — 87 Seiten betroffen), Quellen verlinkt, Lesezeit ehrlich, CTA-H3, CSS-Bust v20260612.
2-3. **Helper-V3 R1/R2** (claude.ai-Tabs, Opus, kein Anchoring): Methodik-Herleitung fehlte, Spannen als Index-Ableitung reverse-engineert, Presse-Apparat fehlte → Kostenmodell-Sektion in /methodik, Komponententabelle, CSV (CC BY 4.0), Presse-Block, SVG-Chart, Dataset-Schema.
4. **R3 fand den Kern-Defekt:** V1-Regionalfaktoren (redaktionell geschaetzt) widersprachen der selbst zitierten Aeternitas-Quelle (Berlin Index 115, real guenstigste Grossstadt; 56%-Hook durch Einheitsfaktor aufgeblaeht). **User-Entscheid: gruendliche Rekalibrierung.**
5. **Modell V2** (_dev/audit/bundesland-modell-v2.py): Friedhofs-Faktor je BL aus den Aeternitas-Landeshauptstadt-Gebuehren (01/2025, 6 Grabarten, spaltennormiert; via check24-Aufbereitung), wirkt NUR auf ortsgebundene Posten (Friedhof/Beisetzung/Grabpflege). Index 75 (Berlin) bis 136 (Bayern), Spread 81%, Mittel 100,4. **Kostenrechner auf dasselbe Modell umgestellt** (LOCAL_FEE_KEYS) + end-to-end verifiziert. V1-Faktor-Claims auf 8 weiteren Seiten ersetzt. Faktor-Tabelle in /methodik veroeffentlicht → komplette Zahlenkette reproduzierbar.
6-7. **R4-R6:** Hero-Attribution geschaerft (Muenchen 4.578 vs Berlin 964, beide 20J, exakt auf den verlinkten Datensatz gescoped), 100-EUR-Rundung, Datenstand sichtbar, Grabpflege-Annahme offengelegt. **R6: GO, Score 85, keine kritischen Befunde** — Reviewer hat alle 96 Werte + 16 Indizes + Faktoren selbst reproduziert.

**Score-Verlauf:** Self-Verify 81 → 68 → 71 → 62 → 68 → 72 → GO 85. Sycophancy-Pattern erneut bestaetigt.

**Strukturelle Lessons (auch in memory/multi_chat_pipeline_lessons.md):**
- Reviewer-URLs IMMER mit Commit-SHA (Branch-raw-URLs cachen ~5 min — R3 prüfte veralteten Stand).
- Reviewer-recherchierte Fakten selbst verifizieren + Claims exakt auf den verlinkten Datensatz scopen (Mainz-Falle R4→R5).
- Daten-Assets: Reproduzierbarkeits-Auftrag in den Review-Prompt; GO erst, wenn ein Reviewer alles nachrechnen kann.

**Nebenbefunde gefixt:** /methodik behauptete "Eingaben verlassen nie deinen Computer" (seit KI-Tools falsch) — korrigiert (Tools-Sektion + Grundsatz-Box).

**Nachtrag Welle 8/8b (gleiche Session, deployed f44adea):** Externes SEO-Review (8,1/10) triagiert — Schema/Presse-Block/GSC waren schon erledigt (Reviewer sah Cache). Umgesetzt: Hauptseite /bestattungskosten an Modell V2 harmonisiert (Muenchen-Gebuehren 1.500-2.500 -> 4.578 EUR, Berlin-als-teuer-Fehler raus, check24-Attribution), Steuer-FAQ-Faktenfehler korrigiert (pauschales "Nein" -> Par. 33 EStG, BMF-verifiziert), FAQ-LD der Hauptseite programmatisch aus DOM regeneriert (Paritaet), "kein echter Landesdurchschnitt" sichtbar, Embed-Code im Presse-Block, Rueckverlinkung 18 BL-Hubs (personalisierte Index-Box) + Rechner. Review: GO 84. Bewusst NICHT umgesetzt: CTA-Verschaerfung (Konflikt mit Presse-Neutralitaet), 16 Mini-Sektionen + Above-fold-BL-Auswahl (eigenes Paket, Kannibalisierungs-Risiko mit Hubs beachten), fachlicher Reviewer (User-Akquise).

**OFFEN:**
- ~~**Datenschutz erwaehnt die KI-Verarbeitung (Groq/US) NICHT**~~ → **ERLEDIGT in Session 2026-06-10 B** (Branch `datenschutz-ki-abschnitt`, GO, wartet auf Merge).
- Presse-Block: Telefonnummer? (R5: Redaktionen verifizieren telefonisch) — User-Entscheid.
- Optional: chart-spezifisches og:image (PNG).
- Pressetext fuer Lokalredaktionen (naechster Schritt der Backlink-Phase) — Seite ist jetzt GO dafuer.
- Cloudflare-Rate-Limit-Regel fuer ai-rede (User, Dashboard) — weiterhin offen.

---


## Iter-11/12/13: Stadt-Nav-Fragmentierung (User-Befund "darmstadt broken")

**Befund:** Die 52 `bestatter/<stadt>/`-Seiten hatten **~7 verschiedene Nav-Templates** (Template-Drift über Zeit), nur 25 kanonisch. Visuell kaputt: unstyled Nav (Bullets, gestackt).

- **iter-11** (Commit f9bcc08): erster Fix, Compat-CSS für die `mr-logo`+`<ul>`-Variante → 16 Städte. **War zu eng** — Scan via `class="mr-logo"` verpasste andere Varianten (BEM `mr-nav__brand`/`mr-nav__menu`, `header.mr-nav`-Wrapper, `mr-nav-brand`).
- **iter-12** (Commit 8e2dbeb): **alle 52 normalisiert** — Haupt-Nav-Wrapper (nav ODER header mit `class="mr-nav"`, balanciert über Verschachtelung) durch kanonisches Berlin-Nav ersetzt + garantiertes Nav-/Breadcrumb-CSS injiziert. Script `_dev/normalize-city-nav-iter12.py`. **Lokal vor Deploy verifiziert** (lokaler http.server + Chrome) — fing 2 Script-Bugs (nested-nav, header-Wrapper). Live bestätigt: je 1 Logo, 0 Orphans.
- **iter-13** (Commit b9d7250): Nav **linksbündig** site-weit (121 Seiten), `.mr-nav-inner` `space-between`→`flex-start`. Script `_dev/nav-leftalign-iter13.py`. Live bestätigt.
- **iter-14** (Commit 0f06dea): **BEM-Compat-CSS** für das alte Stadt-Template. User-Befund: Darmstadt-Kernfakten unlesbar. Audit zeigte: ~29 Städte nutzen ein BEM-Markup (`<dl>`-Kernfakten, `mr-friedhof`-Karten, `mr-faq__item`, `mr-footer__*`, `mr-list`, `mr-hero__*`/`mr-section__*`), dessen Original-Stylesheet (`/assets/css/main.css`) **nie eingecheckt** war (iter-10 entfernte die Referenz). Berlins Inline-CSS stylt nur Block-Klassen, keine BEM-Subelemente. Fix: self-contained Compat-CSS (`_dev/bem-compat-css-iter14.py`) auf alle 52 — Kernfakten-Grid + fette Labels, Friedhof-Karten + Hidden-Gem-Callouts, FAQ-Items, BEM-Footer, Listen (wg. globalem `*{padding:0}`). Lokal vor Deploy an Darmstadt verifiziert, live bestätigt.

**Lessons:** (1) Bei "Pattern?"-Fragen IMMER vollständig klassifizieren statt einen Marker raten — Markup ist heterogener als gedacht (nav vs header, BEM, nested). (2) **Pre-Deploy lokal rendern** (`python3 -m http.server` + Chrome auf `http://127.0.0.1:PORT/...`) statt blind auf N Live-Seiten deployen — hat hier 2 Bugs gefangen. (3) Claude-in-Chrome `navigate` erzwingt `https://` → `file://` geht nicht, `http://127.0.0.1` schon.

- **iter-15** (Commit 93a7f89): Nav **auf 7 Kern-Links verschlankt + ausgerichtet** (site-weit, 121 Seiten). User: Nav überladen/„schwebt"/bricht um. Fix: 12→7 Links (Was tun?/Beerdigung/Kosten/Vorsorge/Bestatter/Trauerrede/Notfallkarte — Kosten+Bestatter neu, waren 0.9-Pillars ohne Nav-Link; `/ratgeber/` verworfen weil 301→Startseite; 5 Text-Tools jetzt via Pillars/Footer). `.mr-nav-inner` `max-width:720px` = Inhaltsbreite → einzeilig (57px) + linke Kante bündig mit Text+Breadcrumb (vorher 120px Versatz, jetzt ~20px). Script `_dev/nav-slim-iter15.py`, balancierter Matcher, lokal vor Deploy verifiziert (Stadt+Pillar).

- **iter-16** (Commit fd7567b): `was-tun-nach-todesfall` (alt-Template-Pillar, Nav-Ziel) auf Standard-7-Link-Nav gegraftet. Body war schon konsistent (Fraunces etc.), nur Nav alt → alte `<header class="site">`-Nav durch `mr-nav` ersetzt + Nav-CSS mit Fallback-Farben (Seite hat keine `--mr-`-Vars). Lokal+live verifiziert. Damit ist die **Nav site-weit einheitlich**. — `notfallkarte.html` bleibt unangetastet (VERWAIST: `/notfallkarte → /tools/notfallkarte/`, nicht ausgeliefert); `danke-bestatter-anfrage.html` ok (minimale mr-* Danke-Seite ohne Nav by design).

- **iter-17** (Commit 525c5ef): Nav linke Kante **bündig zum Inhalt** gemacht (Polsterung von `.mr-nav` → `.mr-nav-inner`, identisches Box-Model wie `.mr-content`/`.mr-breadcrumb`). 122 Seiten + was-tun (`max-width:var(--maxw)`=760). Logo/H1/Breadcrumb alle bündig (lokal verifiziert).

- **iter-18** (Commit 9be7401): Mobile-Nav = **Hamburger**. Bug: auf Mobile alle 7 Links vertikal gestapelt (kein Einklappen; `.mr-nav-toggle` da, aber Mobile-CSS/JS fehlte — Template-Altlast). Fix 122 Seiten: `@media(max-width:760px)` Links aus + Hamburger an + `.mr-nav.open` Spalte; Toggle-JS vor `</body>`. JS-Toggle lokal verifiziert; Mobile-Render lokal nicht prüfbar (Umgebung fix 1920px).

**Noch offen (nächste Session):**
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

## Verdichtung-2-Loop (10.06.2026, autonomer Roadmap-Loop)
Mandat: Top-10 der `_dev/ROADMAP-verdichtung-2.md` autonom abarbeiten (Bolle: „Vertraue dir da"). Modus je Rang: Branch → Fix-Skript in `_dev/audit/` → unabhängiger Review (claude.ai-Tab, ohne Score-Anchoring) → GO → Merge auf main (Netlify-Build) → Live-Verify.

**Stand: Top-10 + R11 (Bestattungsarten) + SH-Frist-Fix. Loop läuft weiter (Bolle 11.06.), als Nächstes Rang 12 (Bestatter-Städteübersicht).** Backlog: Hamburg-Extern-Verifikationen, Consent-Vereinheitlichung (eigener Block), Fristen-MITTEL 4-6 (§30-III-Testament-Satz, FAQ-Q6-Beweislast, Sicherungsmaßnahmen-Hinweis), tracking.js-Plausible-Header.

| Rang | Seite | Kern-Maßnahmen | Review | Commit/Merge |
|---|---|---|---|---|
| 1 | Angebotsprüfer | Intro-Landing, Beispiel-Ampel (#ap-beispiel 3.600–9.000 NRW Feuer), Warnsignale, Ergebnis=Fragenliste, Nav „Angebot prüfen"; **renderStep4-Bug gefixt** (condBA-Posten nie sichtbar — Validity-Audit-Fund) | Doppel-Audit SEO+Validity | deployed |
| 2 | Startseite | Hero-CTAs, Kartenreihenfolge (Prüfer/Rechner/Checkliste zuerst), Trust-Strip, „So funktioniert"-Steps, „alle Eingaben im Browser"-Claim korrigiert (KI-Ausnahme) | GO | deployed |
| 3 | Bestattungskosten (Money) | Dreiteilung+Badges, 3-Stufen-Beispiel (1.000–2.200/3.400–8.200/5.300–14.300), §74-konforme Sozialbestattung, Direktkremation-Zeile, Quellenbox | 3 Runden bis GO 84 | deployed |
| 4 | Kostenrechner | CAT_META-Badges+Sparhebel je Block, Basis-Einordnung; **R4b**: Einordnung mathematisch geschlossen (Komponentensumme ohne Grabpflege, de-regionalisiert, Schwellen ±15/+30 % in Methodik) | NO-GO 64 → R4b → GO | deployed |
| 5 | Was-tun-nach-Todesfall | Schutz-Boxen „Bevor du einen Bestatter beauftragst" (+Rechner/Prüfer-CTAs, data-track) + „Was du heute nicht entscheiden musst", Sternenkind §31-PStV-präzise, Fristen-Radar-Link | GO 84 | 4dac4a9, live-verifiziert |
| 6 | Hamburg-Stadtseite | R6: Quickhelp eigenständig, Gesamtkosten-Box, Historie nach unten; R6b nach NO-GO 54: Kostenkonsistenz (anonym 2.830–3.365 überall, Typisch ab 5.000, Einäscherung 300–550), Tourismus-Ton raus, Affiliate aus Sozialblock, Email-Pflicht, Service-Schema weg, Faktenfixes (30 J., Vor-1877-Gräber raus, Kisdorf SH), Telefonseelsorge | NO-GO 54 → GO 82 auflagenfrei | 49276aa |

| 7 | Sozialbestattung | Schnell-Check "Zahlt das Sozialamt?", druckbare Unterlagen-Checkliste (Print-CSS), Stand-Konsistenz; R7b nach NO-GO 79: Trauerredner BSG-konform (B 8 SO 20/22 R — auch Hamburg-§74-Block gefixt!), Bayern-Beispiel ersetzt (SH/Nds. Lebensgemeinschaft, Bayern Gegenbeispiel Art. 15 BestV), SGB II gleichrangig, Schonvermögen 7.000–10.500 (OVG NRW 12 A 2454/18 + VG Münster 6 K 4230/17, beide selbst verifiziert), Lead entschärft, formloser Antrag + Stundung/Direktabrechnung | NO-GO 79 → GO 90 (+R7c-Folge-Commit → ~95) | Branch r7 |

| 8 | Methodik + Datenschutz | Tool-Datenschutz-Matrix (byteweise identisch auf beiden Seiten), Cluster-Prüfdaten, Danksagung-Umami-Falschsatz; R8b nach NO-GO 64: **Checkliste-localStorage implementiert** (Matrix/FAQ versprachen Persistenz, Code hatte keine — Reviewer-Code-Audit-Fund; Klick→Reload→Restore lokal verifiziert), §6 auf Matrix gestützt, §9 Doppel-Regime ehrlich deklariert, §8 Tool-Formulare+Netlify-Speicherung, §2 zwei Ausnahmen, Matrix-Fußnote; R8c: „einzige Ausnahme"→zwei Ausnahmen (3 Stellen) | NO-GO 64 → GO 87 | Branch r8 |

| 9 | Beerdigung planen | Entscheidungsnavigator (jetzt/warten/Kostentreiber), Angebotsprüfer prominent (war komplett unverlinkt!), Kosten auf kanonische Komponentensummen, 48h-"alle Bundesländer"-Fehler (Hamburg-Widerspruch); R9b: Berlin/Brandenburg aus Fristen-Beispielen (Berlin hat keine Höchstfrist), Feuer-Spanne kanonisch qualifiziert, JSON-LD Q1/Q3 angeglichen; R9c: Keyfact "meist", Kolumbarium-Qualifikator | NO-GO 72 → GO (Stichprobe, 1 Auflage erfüllt) | Branch r9 |

| 10 | Fristen nach Todesfall | Übersichtstabelle Frist/ab-wann/was-tun/wer-hilft (aus belegten Sektionen); R10b: §573d-Kette korrigiert (Abs. 2 definiert Frist allein), staler Opt-In-Kommentar entfernt, Stand-Daten vereinheitlicht | GO 86 mit Auflagen (erfüllt) | Branch r10 |

| 11 | Bestattungsarten | Vergleichstabelle kanonisiert (Baum war Faktor ~2 daneben!), Spalten Zeit/Aufwand, Direktkremation-Zeile, Entscheidungshilfe 4 Leitfragen + 3 Konstellationen; R11b nach NO-GO 52: **Naturbestattungs-Rechtsfehler** (Bayern/BW erlauben KEINE Verstreuung — Anbieter CH/AT), 9 Prosa-Spannen kanonisiert, FAQ günstigste=Direktkremation, Diamant-Rechtslage DE, Umbettungs-FAQ, 70%→drei Viertel; R11c: Religion-Leitfrage, Anonym-Alternativen | NO-GO 52 → GO 86 | Branch backlog-1 |

**Nebenfunde gefixt:** Rechner-Spartipps hatten letzten „Erben zu arm"-§74-Fehler site-weit + Pseudo-Betrag „1.500–2.500 €" → §74-konform (cccd800); Icon-Inkonsistenz Step-0 🤐→🕊.
**Kostenrechner-Live-Validity: PASS.** Reviewer-Sandbox kam nicht an machsruhig.de (Egress-Whitelist) → Option 2: Szenarien mit sichtbarkeits-assertierten echten DOM-Klicks gefahren, Ergebnis-DOM-Dumps geliefert (Erd-Default NRW 6.204–17.396, Erd-Max Bayern 10.438–30.173, See 2.850–6.200). Pflicht-Nachtest See+Grabstein: Summe unverändert (kein Garbage-in), aber Zusammenfassung behauptete "Grabstein: mittel" → P2-Fixes (4efd6f1): Extras modellgetrieben je Art ausblenden + State-Reset, Blocklabel Seebestattung/Waldbestattung statt Friedhof, Spartipps szenariospezifisch. Smoke aller 5 Arten danach grün (Baum exakt 3.050–7.000 = Komponentensumme).
**Offen beim User:** Pressetext-Versand, Groq-ZDR, AV-Verträge, Cloudflare-Rate-Limit, Presse-Telefonnummer, Fachanwalt §7.

### Hamburg-Backlog aus GO-82-Review (nicht deploy-blockierend)
1. Feuerbestattungs-Gesamtzeile in die Hamburg-Kostenbox (billigster Fix, größter Nutzerwert) — Zahlen erst sauber herleiten (Urnenwahlgrab 2.000–2.230 + Bestatter ab 1.580 + Einäscherung).
2. Extern-Verifikationen nächster Fakten-Check: jüdisches Sonderfeld auf Ohlsdorf, SH-14-Tage-Frist, §-6-BestattG-Zitat (36 h), Jüdischer Friedhof Altona „geschlossen 1877".
3. FAQ 5 „ggf." präzisieren; Standesamt-Adressen Altona/Bergedorf ergänzen; 2026er-Gebührenordnung der AöR prüfen; mainEntityOfPage Trailing-Slash; Footer-Claim „immer aktuell" (site-weit).
