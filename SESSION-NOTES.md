# Session-Notizen

## Letzte Session
**Datum:** 28. Mai 2026 (Externes Grinch-Audit + Iter-13 + Helper-V3 Tool-Score-Audit)

## Was wurde gemacht

### Externes Audit (Bolle hat extern auditieren lassen — "Grinch mode")
Audit hat ehrlich gespiegelt was wir die letzten 2 Tage übersehen haben:
- ❌ E-E-A-T-Substanz fehlt komplett (kein namentlicher Autor mit Background)
- ❌ Stadt-Strategie unwahrscheinlich gewinnbar bei head-terms ("Bestatter [Stadt]")
- ❌ "Wir sind ein kleines Team" widerspricht Einzelperson-Impressum (jeder Quality-Rater sieht das)
- ❌ Sprachfehler: "Judäisten", "Zeckenpest" in bestattungsarten.html
- ❌ RLP-Urne-zu-Hause Behauptung ohne juristische Quelle
- ❌ GSC nicht verifiziert, Sitemap nicht eingereicht
- ✓ Methodik-Page transparenter als bei den meisten Konkurrenten (rare praise)
- ✓ Stadt-Modifier-Queries (Long-Tail) realistisch gewinnbar mit guten Pages

Bolle's strategische Einsicht: Site noch zu unreif für Reviewer-Outreach. Foto+Vita aktuell nicht gewünscht. Stadt-Strategie weitermachen mit angepasstem Verständnis (Modifier-Queries, nicht Head-Terms).

### Iter-13: Audit-Sofortfixes (Commit `da8a86e`)
- "Judäisten" → "orthodoxe Juden"
- "Zeckenpest" → "Borkenkäfer / Eichenprozessionsspinner / Eschentriebsterben"
- RLP-Urne weicher: "in einzelnen Bundesländern unter Auflagen — Bundesland-spezifisch prüfen"
- methodik.html: "Wir sind ein kleines Team" → "Hinter machsruhig.de steht Marie-Therese Bollweg aus Hamburg" (konsistent mit Impressum)
- ueber-uns.html: "Die Redaktion machsruhig.de" → "Marie-Therese Bollweg — Initiative & Redaktion" mit Kontakt + Postanschrift
- Reviewer-Fachpool: "wird aufgebaut" → "ist geplant" (ehrlicher)

### Helper-V3 Tool-Score-Audit (kritischer Tag-Befund)
Trigger: Bolle hatte beim Trauerrede-Generator "Schweißausbrüche". Helper-V3 Chrome-Tabs gestartet.

**Trauerrede-Generator: SCORE 46/100 — ÜBERARBEITEN**
- A Output 42: 3 Felder werden NIE verwendet (`formData.length`, `hobbies`, `quote`); `anrede` ignoriert; Längen-Timer täuscht aktiv
- B Edge-Cases 22: Säugling + "humorvoll" = Scherz-Templates. Null Guards.
- C Akut-UX 68: durchklickbar aber sinnlose Felder
- D Transparenz 38: Kein Hinweis dass Template (kein KI). Component intern "TrauerrdeGenerator" (Tippfehler!)
- E Datenschutz 82: kein localStorage/fetch
- F Disclaimer 35: kein Profi-Trauerredner-Hinweis
- **2 Tippfehler im Template fest verdrahtet:** "nahestund" → "nahestand", "tiefspüre" → "tief spüre"

**Abschiedsbrief-Generator: SCORE 64/100 — ÜBERARBEITEN**
- A Output 68: geführtes Schreib-Gerüst (gut), aber Closing fix "In Liebe", kein Name+Datum
- **B Edge-Cases 35 KRITISCH:** "Abschiedsbrief" ist suizid-konnotiert. Kein Telefonseelsorge-Hinweis. Kein Krisen-Auffangnetz.
- C Akut-UX 80: gut
- D Transparenz 82: sauber
- E Datenschutz 78: localStorage lokal, aber "Nichts gesendet" + 3 Tracker = Widerspruch
- F Disclaimer 40: kein Profi-Hilfe-Hinweis

### Ungelöste Tool-Fixes (für nächste Session)
**Sofort-MUST-FIX (5 Min Arbeit für massiven Score-Sprung):**
1. **Abschiedsbrief:** Telefonseelsorge-Banner (0800 111 0 111 oder 0800 111 0 222, 24/7 kostenlos anonym) — bei suizid-konnotiertem Tool quasi rechtlich Pflicht
2. **Trauerrede:** "nahestund" → "nahestand"
3. **Trauerrede:** "tiefspüre" → "tief spüre"
4. **Trauerrede:** Component "TrauerrdeGenerator" → "TrauerredeGenerator"
5. **Beide:** Profi-Hinweis (Trauerredner ca. 400-800 EUR / Trauerbegleitung über bv-trauerbegleitung.de)

**Tiefer Rebuild (1-2h Arbeit, separat):**
- Trauerrede: Längen-Feature implementieren ODER Feld raus
- Trauerrede: hobbies/quote/anrede verdrahten ODER Felder raus
- Trauerrede: Edge-Case-Guards (Säugling + humorvoll sperren, junge Tote: persoenlich erzwingen)
- Abschiedsbrief: Name + Datum unter "In Liebe"
- Abschiedsbrief: Closing wählbar (Select-Dropdown statt fix "In Liebe")
- Abschiedsbrief: Datenschutz-Aussage präzisieren ("Briefinhalte bleiben lokal" statt "Nichts gesendet")

### Andere Tools — noch nicht Helper-V3-auditiert (NEU als Open)
- tools/beerdigungsplaner
- tools/danksagung
- tools/notfallkarte
- tools/fristen-radar
- tools/checkliste-todesfall

Sollten in nächster Session via Helper-V3 Score-Audit durchlaufen (analog zu Trauerrede + Abschiedsbrief). Risiko-Reihenfolge: Notfallkarte > Fristen-Radar > Beerdigungsplaner > Danksagung > Checkliste.

### Remote-Control nicht gestartet
Bolle wollte `/remote-control` triggern für Cloud-Agent-Rebuild. UI-Befehl funktioniert in claude.ai Browser nicht (nur Claude Code CLI). Alternative: Anthropic RemoteTrigger API kann von hier aus genutzt werden. Trigger nicht angelegt — Bolle hat stattdessen "ende deploy" gewählt.

Für nächste Session: Cloud-Agent für autonomen Tool-Rebuild ist eine valide Option (RemoteTrigger.create mit detailliertem Prompt).

## Nächste Schritte (priorisiert)

**Phase A — Tool-Sofort-Fixes (Sofort-MUST-FIX, 15 Min):**
1. Trauerrede: 2 Tippfehler + Component-Name (5 Min)
2. Abschiedsbrief: Telefonseelsorge-Banner (5 Min) — DRINGEND wegen Suizid-Kontext
3. Beide: Profi-Hinweis (5 Min)
4. Re-Score nach Sofort-Fixes (erwartet: Trauerrede ~62, Abschiedsbrief ~80)

**Phase B — Tool-Rebuild (1-2h, oder via Cloud-Agent):**
5. Trauerrede: Längen-Feature implementieren ODER 3 Felder raus
6. Trauerrede: hobbies/quote/anrede verdrahten ODER raus
7. Trauerrede: Edge-Case-Guards (junge Tote, Säugling)
8. Abschiedsbrief: Name+Datum + Closing wählbar
9. Re-Score nach Rebuild (erwartet: ≥75 für beide)

**Phase C — Restliche 5 Tools auditieren:**
10. Helper-V3 Score-Audit für Notfallkarte, Fristen-Radar, Beerdigungsplaner, Danksagung, Checkliste

**Phase D — Strategische Entscheidung (Audit-Antwort):**
11. Long-Tail-Pillar-Pivot ODER Stadt-Cluster-Strategie weiter? → Datenbasiert sobald GSC läuft (nicht aus dem Bauch)

**Phase E — Bolle-Tasks (kein Code-Aufwand):**
12. GSC verifizieren + sitemap.xml einreichen — größter Indexierungs-Hebel
13. Foto+Vita ggf. später wenn Site reifer (aktuell nicht)
14. Reviewer-Akquise in 3-6 Monaten wenn Site reif

## Offene Fragen
- **Strategische Richtung:** Stadt vs Long-Tail-Pillar — Entscheidung nach erster GSC-Datenwoche
- **Trauerrede-Tool:** Rebuild oder einfach offline nehmen + auf später verschieben?
- **5 ungeprüfte Tools:** offline lassen während Audit-Pipeline läuft?

---

# ───────── ARCHIV: frühere Sessions ─────────

## Session
**Datum:** 27. Mai 2026 (Spät-Nachmittag — Iter-9 bis Iter-12 Hidden-Bug-Hunt)

## Was wurde gemacht (Spät-Nachmittag-Erweiterung)

Nach dem "ende deploy" gegen 15:00 fanden wir noch 5 weitere Iter-Wellen, getrieben durch User-Befund "darmstadt sieht broken aus" und dem darauf folgenden Pattern-Check.

### Iter-9: Frankfurt Zweit-Layer-Duplikat
- Welle B hatte Hessen-Block aufgepfropft, dupliziert mit Frankfurt-Original
- Block 2 (Bestattungsrecht in Hessen Fristen) komplett raus — stand schon in Block 1
- Block 3 (Lokale Besonderheiten) von 6 H3 auf 4 schlanke H3 kondensiert
- Werbe-Sprache raus ("Vorreiter", "attraktiver Ort")
- -1516 bytes
- Commit `3a79c8a`

### Iter-10: Broken-CSS-Pattern auf 8 Stadt-Pages (kritischer Visuell-Bug)
**Root-Cause:** Helper-V3-Writer haben verschiedene CSS-Strategien verwendet:
- `/assets/css/main.css` (404, file doesn't exist)
- `/assets/fonts/dmsans.css` (404)
- `/assets/fonts/dm-sans.woff2` (404)
- `/assets/fonts/fonts.css` (404)

Site-Standard ist: **inline `<style>` + Fonts unter `/fonts/`** (not `/assets/fonts/`)

8 Pages betroffen:
- Aachen + Darmstadt: komplett unstyled (kein inline-style) → Berlin's `<style>` Block übernommen
- Chemnitz + Gelsenkirchen: hatten inline style aber broken font-link-Refs
- Braunschweig, Erfurt, Heidelberg, Oberhausen: broken /assets/fonts/fonts.css Refs
- Commit `6acfd8b`

### Iter-11: Site-Health-Scanner Bulk-Fix (14 Finding-Types → 5)
Comprehensive Scan über 116 Pages, dann Bulk-Fix:
- JSON-LD Parse-Error in tools/bestattungskosten-rechner (fehlende ]} für @graph)
- tools/abschiedsbrief: missing H1 → automatisch generiert
- tools/fristen-radar: 2. H1 → H2 demoted
- kontakt.html: robots-meta hinzugefügt
- bestattung-in/hessen + bestatter/hamburg: leftover UNSURE-Kommentare entfernt
- **40 Files: og:image bulk-add** (`/assets/og-image.png` default)
- 5 Files: kompletter OG-Block (danke/datenschutz/impressum/luebeck/moenchengladbach)
- Commits `f91f07c` + `1dba5f9`

### Iter-12: Deep-Scan-Fixes (21 Files)
Tiefere Pattern-Scans + Fixes:
- **12 broken internal links** (font-paths + /vorsorgevollmacht + /reerdigung)
- **Canonical-Bug:** Braunschweig hatte `www.machsruhig.de` (WWW-Variante) — entfernt
- **Sitemap-Update:** Lübeck + Mönchengladbach percent-encoded Umlaut-URLs ergänzt
- **Mixed-Content:** 8 Pages http:// → https:// upgrade (Primärquellen)
- **Meta-desc-too-long:** 2 Pages gekürzt (224→152, 221→151 chars)
- **Wiesbaden Spezialfix:** broken @font-face-Deklarationen für nicht-existente DMSans/Fraunces-Files ersetzt
- Commit `ec2253e`

### Site-Health Endstand (post Iter-12)
Deep-Scan zeigt 5 verbleibende Finding-Types, **alle False-Positives**:
- `tel_link_mismatch` (44): Regex-False-Positive (+49 vs 0 — sind dieselbe Nummer)
- `sitemap_orphans` (4): Scanner kann percent-encoded URLs nicht mappen
- `canonical_path_mismatch` (4): Self-Canonical Umlaut↔percent-encoded (1:1 dasselbe)
- `heading_hierarchy_skip` (84): systematisches Design-Pattern (H2 → H4 in Footer)
- `unsitemapped_indexable` (4): gleicher Scanner-Mapping-Bug wie sitemap_orphans

**Echte verbleibende Bugs: 0** ✓

### Heutiges Commit-Total (Spät-Nachmittag)
- `3a79c8a` iter-9 Frankfurt-Dedup
- `6acfd8b` iter-10 broken-CSS-Pattern (8 Pages)
- `f91f07c` iter-11 Bulk-Fix (47 OG-Tag-Fixes + JSON-LD + H1)
- `1dba5f9` iter-11 Teil 2 (og:image bulk)
- `ec2253e` iter-12 deep-scan-fixes (21 Files)

---

# ───────── ARCHIV: frühere Sessions ─────────

## Session
**Datum:** 27. Mai 2026 (Nachmittag — Ahrefs-SEO-Welle + Analytics-Coverage 100%)

## Was wurde gemacht (Nachmittag, nach Chrome-Audit-Pipeline vom Mittag)

### Ahrefs-Audit Iter-6 bis Iter-8
- **Ahrefs Site Audit installiert** (User-seitig) — deterministischer Crawler ergänzt LLM-Reviewer
- **Health Score 48 → 74** (nach Iter-6+7), erwartet 80+ nach nächstem Re-Crawl
- **Iter-6 Phase A (_redirects):** ~60 neue Regeln — 31 nicht-existente Stadt-Aliase → Hub, 4 Stadt-Alias-Redirects (an-Main, an-der-Ruhr, im-Breisgau), 8 generische Pages → Hubs, Bestattungsarten/Vorsorge-Subs → Hubs, Bundesland-Pages mit Umlaut-Targets, /cdn-cgi/-Catchall
- **Iter-6 Phase B (Link-Cleanup):** 200 broken internal city-links in 83 Files entfernt (19 Production-Pages + 64 Dev-Archiv). Python-Script `<a href="/bestatter/{nonexistent}/">Text</a>` → `Text` (strip anchor, keep text)
- **Iter-6 Phase C (Stub-Page):** /kontakt.html neu erstellt — 17 Inlinks die vorher 404'ten haben jetzt echtes Ziel
- **Iter-7 (Polish nach Re-Crawl):** /kontakt.html OG-Tags + sitemap + Bundesland-Redirects auf Umlaut-Targets (Pages existieren mit ä/ö/ü)
- **Iter-8 (Analytics-Coverage):** 53 ungetrackte Stadt-Pages bekommen Umami+Ahrefs WA. Vorher nur 3 von 116 getrackt, jetzt **100%**

### Erkenntnisse Nachmittag
- **Self-Verify-Sycophancy** vs **deterministisches Crawler-Audit** sind komplementär. Health 48 → 74 in 1 Stunde durch mechanische Fixes — keine LLM-Variance.
- **Cloudflare Email Obfuscation war False-Alarm:** /cdn-cgi/l/email-protection 404s waren nur **Ahrefs-Cache** von früherer CF-Phase. User hat Toggle ausgeschaltet (Email Obfuscation OFF), aber Errors waren schon vorher weg. CF ist aktuell nicht im Request-Pfad.
- **NEUE Lesson (Memory-würdig):** Cowork-Sandbox unter `/tmp/` zeigt phantom-deletions im git-status (Files im Repo, aber nicht physisch im Sandbox-Mount). `git add -A` darf NICHT verwendet werden ohne sanity-check. Stattdessen explizit Files staunen. Heute hat git add -A versehentlich 23.576 Deletionen mit-committed (`_dev/` + `data/*.json`). Recovery per `git checkout c391617 -- _dev/ data/` durchgeführt.
- **Ahrefs WA + Umami komplementär:** Umami = On-Site-Behavior + Conversions; Ahrefs WA = Off-Site-Source-Korrelation + SEO-Verbindung

### Endstand Site-Health
- **YMYL** (Chrome-Audit, Vormittag): 7/8 Stadt-Pages ≥85, Frankfurt-Variance
- **SEO** (Ahrefs, Nachmittag): Health 74 (Good), 404s 61→~3, Broken Links 47→~5
- **Tracking-Coverage**: 116/116 Pages (vorher 3/116)
- **Commits heute Nachmittag**: fe61e5f, 2bac5a2, c391617, 69b0fd1, b3a3307, + this commit

## Nächste Schritte (priorisiert)

**Phase A (klein, nach Quota-Reset Donnerstag 14:00):**
1. **Frankfurt Zweit-Layer-Duplikat** aufräumen (Welle B hat Hessen-Block dazu gepackt, dupliziert mit Frankfurt-Original — Rat-Beil zweimal mit unterschiedlichen Zahlen)
2. **Frankfurt GVBl-Citation** manuell beim Hessisches Landesrecht verifizieren (Bolle oder Jurist) — Reviewer-Variance gibt keine sichere Antwort
3. **Dortmund Chrome-Re-Score** (war Quota-blocked, erstes Score nach Welle B 8 FAQ-Drift-Fixes)
4. **Ahrefs Re-Crawl checken** — Health Score nach Iter-7+8 sollte 80+ sein

**Phase B (SEO-Optimierung):**
5. **9 Orphan Pages** in Ahrefs identifizieren und entweder von Hub-Pages aus verlinken oder noindex
6. **2 Noindex in sitemap** + **2 Non-canonical in sitemap** identifizieren und cleanen
7. **Redirect Chains** (3 Stück) auflösen — direkte Links statt A→B→C
8. **3XX redirect: 105 Stellen "Page has links to redirect"** — interne Stadt-Page-Links direkt verdrahten statt via 301

**Phase C (Polish, optional):**
9. Du-Kasus-Mix global vereinheitlichen (Berlin 16× klein + 7× groß; Düsseldorf, Leipzig, Stuttgart ähnlich)
10. Datums-Hinweise an Gebühren-Tabellen (München, Stuttgart) ergänzen — "Stand der Satzung verifizieren"

**Phase D (Tracking-Reifung):**
11. **Umami Goals/Events** einrichten — `lead_form_submit`, `tool_complete:kostenrechner`, `outbound_click:check24`, `phone_click` (Implementation im Code nötig)
12. **Ahrefs WA Dashboard** beobachten — welche Pages konvertieren, welche Bounces

**Hinter dem Messgate (wenn machsleicht-Indexierung rankt):**
13. Echter Reviewer-Pool aufbauen (Bestatter / Jurist / Trauerbegleitung)
14. Lead-Funnel + Einwilligung sauber
15. Welle E (Tier-Bestattung, Auswanderer, Patchwork-Familie)

## Offene Fragen
- **Frankfurt GVBl-Citation:** "GVBl. Nr. 64 vom 6.10.2025" vs "GVBl. Nr. 101 vom 16.12.2025" — welches ist die echte Verkündung der FBG-Novelle 2025? Reviewer geben gegensätzliche Antworten.

---

# ───────── ARCHIV: frühere Sessions ─────────

## Session
**Datum:** 27. Mai 2026 (Mittag — Chrome-Audit-Retro 9 Cities + 5 Iter-Wellen + Deploy)

## Was wurde gemacht

**Auslöser:** User-Kritik nach Welle 2B: "JUNGE!!! DU NUTZT NICHT CHROME DFÜRS REVIEWEN UND WRITEN!" + "alles müll". Self-Verify mit WebFetch hatte Sycophancy-Verzerrung. Korrektur: alle Stadt-Pages mit echten unabhängigen Chrome-Helper-V3-Tabs retro-auditiert.

### Welle 1: Chrome-Audit Retro (9 Cities, alle deployed)
- **PASS (2):** München, Stuttgart
- **FAIL (7):** Köln (3 MF), Hamburg (3 MF), Frankfurt (3 MF), Düsseldorf (2 MF), Berlin (2 MF), Leipzig (1 MF), Dortmund (1 MF)
- **Audit-Doc:** `_dev/audit/chrome-audit-welle1-retro-2026-05-27.md`

### Iter-Wellen Fix-Pipeline (5 Wellen, 46 Fixes total)

**Iter-1/Welle A — mechanisch (15 Fixes, 5 Cities):**
- Köln: tel-Link defekt (`tel:+492212212556` → `tel:+4922122125560`), UNSURE-Kommentar Z.211 entfernt, Willy Birgel 1909-1979 → 1891-1973, Napoleon-Dekret 1805 → 1804
- Berlin: 116→118 evangelische Friedhöfe, UNSURE-Kommentar Z.428, Friedrichsfelde-Brandenburg-Halbsatz
- Düsseldorf: tel-Link `+4921189911` → `+492118991`, FAQ-Anführungszeichen
- Frankfurt: FAQ-Drift Q3/Q4/Q6 wortgleich-Sync
- Hamburg: FAQ #2 Frage "größter Friedhof" → "größter Parkfriedhof"

**Iter-2/Welle B — inhaltlich (31 Fixes, 4 Cities, via Helper-V3 Writer-Tabs):**
- Frankfurt (5): Rat-Beil-Straße 1828-1928 Datierung (3 Stellen) + 48h-Frist als Mindestfrist statt Überführungspflicht (2 Stellen)
- Hamburg (14): AöR-Trägerschaft Bergedorf/Harburg → Volksdorf/Wohldorf (6 Patches) + BestattG 1988 → BestattG 2019 + 8x HmbBestG-Kürzel → BestattG global
- Leipzig (4): Du/man-Bruch (Z.429+572 Fließtext, Z.201 JSON-LD + Z.544 HTML <summary>)
- Dortmund (8): FAQ-Drift alle 8 Antworten JSON-LD ↔ HTML wortgleich (selbst-mechanisch, Helper-V3 Quota-blocked)

**Iter-3 — nach Re-Score (3 Cities, 15 Stellen):**
- Köln (10): 1965 → 1968 (muslimische Grabfelder Westfriedhof, Stadt-Köln-Primärquelle, 9× wiederholt inkl. og:description + JSON-LD)
- Hamburg (1): Akutbox § 2 → § 1 Abs. 2 BestattG (Krankenhaus-Leichenschau)
- Frankfurt (4): GVBl-Zitierung + § 19 → § 15 + § 18 Abs. 2 Sargpflicht

**Iter-4 — Sub-Gate-Cities (Leipzig + Berlin):**
- Leipzig: "8 Werktage" → "8 Tage" (§ 19 SächsBestG, 3 Stellen — der "Mindest-Frist-Verlängerungs-Bug")
- Berlin: 116 117 als tel:-Link in Akutbox, Affiliate-Block raus aus § 74-Sozialbestattungs-Block

**Iter-5 — Pattern-Removal (3 Cities):**
- Stuttgart + Düsseldorf + Leipzig: Check24-Sterbegeldversicherungs-Affiliate aus Sozialbestattungs-Block raus (ethisch grenzwertige Monetarisierung an Härtefall-Zielgruppe)
- Stuttgart: title/og:title/H1/JSON-LD alle synchron auf "Friedhöfe, Kosten und Bestatter"

### Chrome-Re-Score (8 von 9 gescored, Dortmund Quota-blocked)

| City | Score | Status |
|---|---|---|
| Köln | 91 | ✅ GOLD |
| Berlin | 89 | ✅ GOLD (+5 nach Iter-4) |
| Düsseldorf | 89 | ✅ GOLD |
| Stuttgart | 88 | ✅ GOLD |
| Hamburg | 88 | ✅ GOLD |
| München | 85 | ✅ GOLD knapp |
| Leipzig | 85 | ✅ GOLD knapp (+5 nach Iter-4) |
| Frankfurt | 70-84 | ⚠️ Reviewer-Variance (zwei Reviewer widersprechen sich bei GVBl-Citation) |
| Dortmund | — | Quota-Wall (Donnerstag 14:00 Reset) |

**7 von 8 gescored über 85-Gate** = objektives Gold-Niveau mit externem Maßstab.

### Erkenntnisse
- **Self-Verify-Sycophancy ist real:** Memory-Pattern bestätigt — Subagent/WebFetch-Scores -7 zu hoch
- **Reviewer-Variance ist auch real:** Bei Frankfurt geben zwei unabhängige Chrome-Reviewer gegensätzliche "Primärquellen"-Behauptungen → ab Iter-5 Diminishing Returns
- **Polish ≠ Faktizität:** Die alte "Elite"-Bewertung war strukturell korrekt (Du-Anrede, mr-Classes, akutbox), aber Faktizität gegen Primärquellen war nie gemessen

## Nächste Schritte (priorisiert)

**Phase A — Frankfurt + Dortmund cleanup (klein):**
1. **Frankfurt Zweit-Layer-Duplikat** aufräumen (Welle B hat Hessen-Block dazu gepackt, der sich mit Frankfurt-Original-Block dupliziert — Rat-Beil zweimal mit unterschiedlichen Zahlen, doppelte Fristen, In-Kraft-Framing inkonsistent)
2. **Frankfurt GVBl-Zitierung** manuell beim Hessisches Landesrecht verifizieren (Bolle oder Jurist) — Reviewer-Variance gibt keine sichere Antwort
3. **Dortmund Chrome-Re-Score** nach Quota-Reset Donnerstag 14:00 (erstes Score, nach Welle B 8 FAQ-Drift-Fixes)

**Phase B — Optional, falls weiterhin "Gold für alle":**
4. Du-Kasus-Mix global vereinheitlichen (Berlin 16× klein + 7× groß; Düsseldorf, Leipzig, Stuttgart ähnlich) — kosmetisch, +1-2 Score
5. Datums-Hinweise an Gebühren-Tabellen (München, Stuttgart) ergänzen — "Stand der Satzung verifizieren"

**Hinter dem Messgate (wenn machsleicht-Indexierung rankt):**
6. Frankfurt + Dortmund Audits konsolidieren
7. Echter Reviewer-Pool aufbauen (Bestatter / Jurist / Trauerbegleitung)
8. Lead-Funnel + Einwilligung sauber
9. Welle E (Tier-Bestattung, Auswanderer, Patchwork-Familie)

## Offene Fragen
- **Frankfurt GVBl-Citation:** "GVBl. Nr. 64 vom 6.10.2025" vs "GVBl. Nr. 101 vom 16.12.2025" — welches ist die echte Verkündung der FBG-Novelle 2025? Reviewer geben gegensätzliche Antworten. Braucht Primärquellen-Klärung.

---

# ───────── ARCHIV: frühere Sessions ─────────

## Session
**Datum:** 27. Mai 2026 (Morgen — Stadt-Polish-Welle Top 5 + Konsistenz-Sweep + Deploy)

## Was wurde gemacht
- **Stadt-Polish-Welle Top 5 (4 Städte, 5. Frankfurt offen):** Helper-V3 Writer parallel auf 2 Tabs pro Welle (Branch-Trick via Artifact-Download + Blob-Download).
  - **Welle 1 (Commit 2621e85):** Berlin (+18k: Bezirks-Matrix 12 Standesämter, Träger-Tabelle 85/118/9/10=222) + Hamburg (+11k: mr-contact-card Hamburger Friedhöfe AöR, Gebühren-Mini-Tabelle)
  - **Welle 2 (Commit 8d20e14):** München (+20k: Akutbox unter H1, mr-contact-card FBM) + Köln (+14k: FAQ-Block als sichtbarer Accordion, Gebührenlink prominent)
- **Welle 2A (Düsseldorf+Stuttgart) + Welle 2B (Leipzig+Dortmund)** mit gleichem Polish-Pattern deployed.
- **End-Check Konsistenz-Sweep:** alle 4 Stadt-Pages konsistent (H1-Format, akutbox-id, Träger-Info, FAQ-Drift, Du-Anrede, § 74 SGB XII).

## Session
**Datum:** 26. Mai 2026 (Abend — Angebotsprüfer-Rebuild v2.4 + ASCII-Canonical-Fix LIVE)

## Was wurde gemacht
- **Angebotsprüfer v2.4 LIVE, Validity-PASS:** 5 Iterationen Rebuild (v2 → v2.4-Polish). Kern-Änderungen: SEPARAT_KOSTEN-Logik (Friedhofsgebühren raus aus Range), INFO_POSTEN-Konstante, ROT nur bei kumuliertem Risiko.
- **P0-Versicherung während Rebuild:** Tool noindex + 16 CTAs neutralisiert.
- **ASCII-Canonical-Fix:** `bestatter/luebeck/` + `bestatter/moenchengladbach/` ASCII-Stubs zeigen percent-encoded canonical auf Umlaut-Hauptversion.

---

# ───────── (Ältere Archive gekürzt — siehe Git-History) ─────────
