# CLAUDE.md — Onboarding für Nachsessions

## Was ist machsruhig.de?

Unabhängiges Informationsportal für **Bestattung, Trauer und Vorsorge** in Deutschland. Statische HTML-Site, deployed via Netlify aus diesem Repo. Keine eigene Bestatter-Vermittlung — das ist redaktioneller Content + perspektivisch (Phase F) Affiliate-Partnerschaften für Vorsorge-Themen.

**Strategie:** Authority vor Leadgen (siehe `STRATEGIE.md`).

## Repo-Layout

```
.
├── index.html                  ← Homepage
├── bestattungskosten.html      ← Content-Pages (Root)
├── bestattungsarten.html
├── beerdigung-planen.html
├── kondolenzschreiben.html
├── trauerrede-schreiben.html
├── trauersprueche.html
├── kindern-tod-erklaeren.html
├── vertraege-kuendigen.html
├── methodik.html               ← Trust-Page
├── ueber-uns.html
├── impressum.html, datenschutz.html  ← Legal
├── 404.html
│
├── bestatter/                  ← 50 indexierte + 2 noindex Stadt-Pages
│   ├── index.html              ← Hub (CollectionPage)
│   ├── {city}/index.html       ← 52 Stadt-Pages (3 Markup-Stile)
│   └── (Umlaut-Duplikate: lübeck/, mönchengladbach/ — canonical → ASCII-Variante)
│
├── bestattung-in/              ← 16 Bundesland-Pages
│   ├── index.html              ← Hub (neu in dieser Session)
│   └── {bundesland}/index.html ← Umlaut-Slugs (baden-württemberg/, thüringen/)
│
├── tools/                      ← 10 React-CSR-Tools
│   ├── index.html              ← Hub (neu in dieser Session)
│   ├── bestattungskosten-rechner/, kostenrechner/, beerdigungsplaner/
│   ├── checkliste-todesfall/, fristen-radar/, notfallkarte/, vorsorge-check/
│   └── danksagung/, trauerrede/, abschiedsbrief/
│
├── vorsorge/                   ← 8 Vorsorge-Themen-Pages
│   ├── index.html              ← Hub
│   └── {topic}/index.html      ← bestattungsvorsorge, patientenverfuegung, etc.
│
├── sitemap.xml                 ← 99 URLs, manuell gepflegt
├── robots.txt                  ← AI-Crawler-Policy: GPTBot/ClaudeBot/Perplexity allow, Bytespider deny
├── _redirects                  ← Netlify Pretty-URL-Routing
├── netlify.toml                ← Deploy-Config
├── validate-all.sh             ← Pre-Push Gate (6 Checks, muss STUFE 1 PASSED zeigen)
│
├── _dev/                       ← Audit-Tools, nicht deployed (in robots.txt disallowed)
│   ├── audit-all-pages.py      ← Score-Audit, schreibt AUDIT-REPORT.json
│   ├── audit/
│   │   ├── faq-schema-drift.py        ← FAQ-JSON-LD vs HTML-FAQ-Drift
│   │   ├── regenerate-faq-jsonld.py   ← Surgical JSON-LD-Replace
│   │   ├── module-heatmap-v2.py       ← 6-Module-Audit pro Stadt-Page
│   │   ├── sitewide-health.py         ← JSON-LD + Assets + OG + Schema-Refs
│   │   ├── internal-links-audit.py    ← Broken-Link-Check
│   │   └── meta-length-audit.py       ← Title/Description-Längen
│   └── content-loop/, AUDIT-REPORT.json
│
├── STRATEGIE.md                ← Langfristige strategische Leitplanken
├── BACKLOG.md                  ← Operativer Masterplan (große Datei, mit Phasen A-F)
├── GO-LIVE-CHECKLIST.md        ← Pre-Deploy-Checklist
└── SESSION-NOTES.md            ← Historisches Session-Gedächtnis (CHRONOLOGISCH — neue Sessions oben)
```

## Strategische Leitplanken (NICHT VERHANDELBAR)

Aus `BACKLOG.md` und durch User-Decisions in Sessions etabliert:

1. **Authority vor Leadgen.** Erst Domain-Autorität, dann Monetarisierung. Affiliate/Lead-Forms werden in **Phase F** aktiviert — nicht autonom durch Claude einbauen.
2. **Keine weiteren Generic-Template-Seiten.** Jede neue Stadt-Page muss die 6 Pflicht-Module haben (siehe Modul-Heatmap V2).
3. **YMYL-Standard immer.** Autor sichtbar, Stand, Quellen, Disclaimer auf jeder Page mit Gesundheits-/Rechts-/Finanzaussagen.
4. **Keine CSR-Experimente bei Content-Seiten.** Tools dürfen client-seitig rendern, Content-Pages müssen statisches HTML sein.
5. **Reversibilität bewahren.** `noindex` statt löschen. HTML-Kommentare mit Datum bei Änderungen.
6. **Primärquellen vor Sekundärquellen.** Landesgesetze (recht.nrw.de etc.), kommunale Satzungen, Bundesgesetze (gesetze-im-internet.de). Sekundär: Stiftung Warentest, Verbraucherzentralen.

## Pflicht-Module pro Stadt-Page (Heatmap V2)

Jede Stadt-Page muss 6 H2-Sections haben:

| Modul | Regex-Pattern | Stand 20.05.2026 |
|---|---|---|
| **akut** | `Nach einem Todesfall in X` / `Akutbox` / `ersten 24 Stunden` | 50/52 ✓ |
| **kosten** | `Bestattungskosten in X` / `Kosten einer Bestattung` / `Friedhofsgebühren` | 52/52 ✓ |
| **bestwahl** | `Bestatter in X (auswählen/wählen/finden)` | 52/52 ✓ |
| **sozial** | `Sozialbestattung in X` + `§ 74 SGB XII` | 47/52 (3 echte Lücken: mainz, saarbrücken, wiesbaden) |
| **faq** | `Häufige Fragen` / `FAQ` | 52/52 ✓ |
| **quellen** | `Quellen [und weiterführende Informationen]` | 50/52 ✓ |

Audit: `python3 _dev/audit/module-heatmap-v2.py` → `_dev/audit/module-heatmap-v2.md`.

## FAQ-Schema-Drift-Regel

**Single Source of Truth: HTML.** Wenn FAQ-Inhalt geändert wird (im sichtbaren HTML), muss das JSON-LD `FAQPage` synchronisiert werden. Sonst Google-Penalty-Risiko (Structured-Data-Richtlinie: "Content must be present on the page that loads").

Workflow:
```bash
# 1. Audit ausführen
python3 _dev/audit/faq-schema-drift.py
# → schreibt _dev/audit/faq-schema-drift-report.md

# 2. Bei DRIFT: regenerieren
python3 _dev/audit/regenerate-faq-jsonld.py --dry-run         # zeigt Diff
python3 _dev/audit/regenerate-faq-jsonld.py --write           # alle Cities
python3 _dev/audit/regenerate-faq-jsonld.py --city berlin --write  # einzelne

# 3. Re-Audit zur Verifikation
python3 _dev/audit/faq-schema-drift.py  # → 0 DRIFT erwartet
```

Tool nutzt **Surgical-Replace** via `JSONDecoder.raw_decode()`: nur das `FAQPage`-Objekt wird byte-genau im Original-Text ersetzt, alle anderen Schema-Nodes bleiben unangetastet (minimaler Diff-Churn).

## Pre-Push-Gate: validate-all.sh

Vor jedem Push (oder via PR-CI):

```bash
bash validate-all.sh
```

6 Checks:
1. HTML-Syntax (strict, akzeptiert kein XHTML-Self-Closing `<meta />`)
2. Keine `TODO`/`PLATZHALTER` in Production-Pages
3. Homepage-Audit-Score ≥ 75
4. Interne Links: keine 404-Targets
5. Sitemap-Konsistenz mit Filesystem
6. OG-Image-Existenz

Muss am Ende **STUFE 1 PASSED** zeigen.

## Conventions

- **HTML5** (kein XHTML — keine `/>` an `<meta>`, `<link>`, `<img>`)
- **og:image:** Default ist `/assets/og-image.png` (das einzige existierende OG-Image). Stadt-spezifische sind im Backlog.
- **Canonical:** ohne `www.` (`https://machsruhig.de/...`, nicht `www.machsruhig.de`)
- **Internal Links zu Verzeichnis-Pages:** mit trailing slash (`/bestatter/koeln/`, nicht `/bestatter/koeln`)
- **Robots-Meta:** `index,follow` (ohne Space) für indexable Pages, `noindex,follow` für Generic-Templates
- **External Links:** mit `rel="noopener"` (Tabnabbing-Schutz)
- **Affiliate-Links:** mit `rel="nofollow noopener"`
- **Sitemap:** manuell gepflegt, lastmod sollte mit `dateModified` in JSON-LD übereinstimmen

## Branch-Strategie

- **main:** Deploy-Branch, Netlify baut bei jedem Push automatisch
- **claude/*:** Feature-Branches für Claude-Sessions, kein automatischer Build, Netlify Deploy-Preview pro PR

**Branch-Trick:** Iterativ committen+pushen auf Feature-Branch (kein Netlify-Build pro Commit), Final-Merge zu main triggert Build.

## Network-Allowlist (für Cloud-Container-Sessions)

Dieser Repo läuft in Sandboxen mit Netzwerk-Allowlist. Erreichbar:
- GitHub (push/pull, PR-MCP)
- Anthropic-API (Models)
- WebSearch (Google Snippets, blocked-domains via WebFetch)

**Nicht erreichbar:**
- `fvwuppertal.de`, `wz.de`, deutsche Behörden-Websites, `google.com` direkt → HTTP 403 "Host not in allowlist"

→ Für lokale Recherche-Tasks (z.B. Wuppertal-Gebühren) müssen Daten **vom User beigestellt** werden (Copy-Paste, PDF-Upload).

## Letzter Session-Stand (Mai 2026)

Siehe `SESSION-NOTES.md` (chronologisch, neueste Session oben). Highlights aus Session vom 20.05.2026:

- **FAQ-Schema-Drift sitewide gelöst** (0 DRIFT über 86 Pages)
- **Wuppertal Friedhofsgebühren mit offiziellen Sätzen** (Christlicher Friedhofsverband, Satzung 04.03.2024)
- **Comprehensive Sweep**: 357 rel="noopener" Fixes, 65 OG-Image-Fixes, 17 broken internal links, Bundesland-Crosslinks (15 BL), Kostenrechner-CTA in 50 Cities + 16 BL
- **2 neue Hub-Pages** (`/bestattung-in/`, `/tools/`)
- **Static-SEO-Shell** für alle 9 React-CSR-Tools
- **AI-Crawler-Policy** in robots.txt (GPTBot/ClaudeBot/Perplexity allow, Bytespider deny)

Sitewide Avg-Score (audit-all-pages.py): **70.9** (Stand 20.05.2026).

## Schnellstart für eine neue Session

```bash
# 1. Aktueller Stand
git status
git log --oneline -10
python3 _dev/audit/sitewide-health.py
python3 _dev/audit-all-pages.py

# 2. Pre-Push Gate
bash validate-all.sh

# 3. PR-Stand (wenn vorhanden)
# gh pr list  (oder MCP github-Tools)
```

## Wichtige Don'ts

- ❌ **Kein Affiliate/Lead-Form autonom einbauen** (Phase F, strategisch)
- ❌ **Keine Stadt-Page mit erfundenen Behörden-Adressen oder Gebühren** (Primärquellen-Pflicht)
- ❌ **Kein Force-Push auf main**
- ❌ **Keine BACKLOG.md-Edits autonom** (zu komplex, oft strategische Entscheidungen)
- ❌ **Keine Cities/Hub-Pages anlegen, die User-Decision brauchen** (z.B. neue Stadt-Pages für nicht-existierende verlinkte Cities — erst Policy klären)
