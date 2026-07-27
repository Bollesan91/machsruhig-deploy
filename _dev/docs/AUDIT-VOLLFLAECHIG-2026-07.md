# Vollflächiges Audit machsruhig.de (extern, 07/2026) — Triage & Abarbeitung

> Externes Gesamt-Audit (Vertrauen 7/10, YMYL-Absicherung 5,5/10, „Risiko durch skalierte Stadtseiten: hoch").
> V4.1-Stufe-3: jedes Finding gegen Live/Primärquelle geprüft. Bolle-Mandat: „alles was ohne mich geht umsetzen und fixen", Schwieriges mit Helfer.

## Umgesetzt & deployed (ohne Bolle machbar)

### Autorenschaft / E-E-A-T — Findings #1, #2, #17, #26 (kritisch)
Institutionelle Byline → **namentliche Verantwortung + ehrliches Status-Label**, site-weit, mit Helfer-Rigor (Parse+Walk-Skript `_dev/audit/fix-authorship.py`, Asserts-vor-Write, Linter 0-FAIL, JSON-LD-Reparse-Gate, Browser-Smoke).

Die Byline lebte in **6+ Oberflächen** (Lesson 16 in groß):
1. JSON-LD `author` inline (`Organization` „machsruhig Redaktion" / „Redaktion machsruhig.de" / „machsruhig.de Redaktion")
2. JSON-LD `author` als `@id`-Referenz auf eine `#redaktion`-Entität
3. JSON-LD `reviewedBy`-Knoten (4 Seiten — falscher Review-Implikat) → **entfernt**
4. sichtbar `<strong>…</strong>` in `mr-article-meta` (84×)
5. `<meta name="author">`, `<p class="stand">…Recherche:…`, `<p class="meta">…` Klartext (Legacy)
6. Prosa („von der machsruhig Redaktion erstellt") + kiel-`mr-author`-Block + darmstadt-Hero

**Ergebnis (live):** 51 Seiten JSON-LD `author` = `Person` **Marie-Therese Bollweg** (url /ueber-uns); 90 Seiten sichtbares Label **„redaktionell recherchiert, nicht extern fachlich geprüft"**; Byline site-weit „Redaktion: Marie-Therese Bollweg". Rest-Strings „machsruhig Redaktion"/„Redaktion machsruhig.de"/„Fachpool-Reviewer"/„reviewedBy" = **0**.

### Falsche Fachpool-Behauptung entfernt — Finding #1 (kritisch)
3 Legacy-Seiten (darmstadt/kiel/regensburg) behaupteten sichtbar + im JSON-LD einen **„Bestattungsfachpool"-Review**, den es nicht gibt (über-uns sagt selbst: Fachpool „erst geplant"). Alle entfernt/ehrlich ersetzt. methodik/ueber-uns nennen den Fachpool weiterhin **als geplant** (ehrlich) — unangetastet; das neue Label erfüllt genau deren Zusage „noch nicht extern geprüfte Inhalte werden gekennzeichnet".

### Beispielprofil — Finding #27 (hoch)
`transparenzprofil-beispiel.html`: `robots` → **noindex,follow** + **aus Sitemap entfernt** (188 URLs). Trägt kein LocalBusiness/Review-Schema (nur Article+Breadcrumb) → nichts zu entfernen; „fiktiv"-Kennzeichnung war schon da.

## Bereits erledigt / False Positive (mit Live-Beleg)
- **#8 §649 BGB** — schon gefixt (Hotfix 16.07.): alte „Mindestangaben"-Formulierung 0×, neue live. Auditor sah Vor-Hotfix-Stand.
- **#22 robots.txt/sitemap** — HTTP 200, valide (Auditor-Tool hatte Bot-Gate-403). Sitemap jetzt 188 URLs.
- **#15 KI-Datenschutz** — Groq/USA am Tool schon offengelegt.
- **methodik „3 Ausnahmen"** — schon konsistent.

## Braucht Bolle (organisatorisch — kein Code löst das; = der eigentliche Engpass)
Deckt sich mit PARTNER-OUTREACH / GAMECHANGER-AUDIT (Cold-Start-Autorität):
- **#1** echte externe Fachprüfung / Ko-Autor → dann Label je Seite auf „fachlich geprüft (Name, Datum)" hochstufen (Label-System steht jetzt bereit).
- **#5** „So wählen wir Bestatter aus"-Seite (reales Auswahlverfahren) + #6/#7 Pilot-Marker/„Bestätigt heißt ausschließlich…" (Partner-Programm noch nicht live → nachrangig).
- **#16** Sterbegeldversicherung: wirtschaftliche Neutralität ausbauen (Gegenüberstellung, wann nachteilig) — YMYL-Content, Haupt-Claude schreibt selbst nach Bolle-Go.
- **#17/#18** Bio/Qualifikation/Erfahrung, #30 Telefon + Beschwerdeweg, #19 Rollen-Trennung Info vs. Vermittlung.
- **#3/#23** Stadtseiten-Skalierung drosseln + Quality-Gate (Policy) — Audit-Kernrat.
- **#11** Titel „Bestattungskosten nach Bundesland" ggf. entschärfen (Klick vs. Präzision) — Bolle-Entscheidung.
- **#14** Datenschutz direkt am Bestatter-Anfrageformular (sobald Vermittlung live).

## Nicht umgesetzt (bewusst)
- Automatische Datums-Aktualisierung (#25): machen wir ohnehin nicht — lastmod = echtes Commit-Datum.
- Volle Quellen-Matrix je Stadtseite (#10): Aufwand hoch, nachrangig; Provenienz-Gates F2/F6 decken das Nötigste.
