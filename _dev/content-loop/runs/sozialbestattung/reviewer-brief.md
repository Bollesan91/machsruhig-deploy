# Chat B Reviewer-Brief — Sozialbestattung Pillar v1
## (Helper-V3 fresh tab, kein Anchoring auf Writer-Tab)

Adversarial-Audit einer YMYL-Content-Page (Bestattungsrecht/Sozialhilfe).

## KONTEXT
Eine neue Pillar-Page wurde geschrieben für https://machsruhig.de/sozialbestattung — Thema: Kostenübernahme der Bestattung durch das Sozialamt nach § 74 SGB XII. Der Writer hatte ein Quellen-Pack als Grundlage; aber: WebSearch und Reviewer-Output können trotz Pack noch halluzinieren.

**Page-HTML** (zum Adversarial-Lesen):
[HIER WIRD HTML EINGEFÜGT IM CHAT — komplett von DOCTYPE bis /html]

**Quellen-Pack als Verifikations-Anker:**
https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/_dev/content-loop/runs/sozialbestattung/quellen-pack.md

## DEIN AUFTRAG — 5 Linsen

### Linse 1: YMYL-Rechtspräzision (HAUPTRISIKO)
Pro §-Aussage prüfen:
- Ist der § korrekt zitiert? (§ 74 SGB XII — Kostenübernahme; § 1968 BGB — Erbenhaftung; § 195 BGB — Verjährung; § 632 BGB — ortsüblicher Preis; ggf. andere)
- Verifiziere gegen Primärquelle (gesetze-im-internet.de oder dejure.org), NICHT nur gegen Reviewer-WebSearch-Ergebnis (Sycophancy-Falle: Reviewer kann WebSearch falsch interpretieren — passiert beim Plan-Reviewer der vorigen Session mit §649/§650-Verwechslung)
- Sind die Rechtsfolgen konjunktivisch ("kann übernommen werden") statt absolut ("wird automatisch erstattet")?
- Bundesland-Bezug bei landesabhängigen Aussagen genannt?
- Sind erfundene Fristen drin? (Verjährung 3 Jahre § 195 BGB OK; "Reklamationsfrist X Tage" = Hallu)

### Linse 2: Promise-Delivery
H1 verspricht: was lernt ein User mit konkretem Anlass (Bestattung steht an, Geld reicht nicht)? Wird das Page-Promise im Body eingelöst?
Pro Sektion: Beitrag zur Antrags-Entscheidung? Oder Backfill/Filler?

### Linse 3: Faktentreue gegen Quellen-Pack
Stichproben gegen Quellen-Pack-Punkte:
- Anspruchsreihenfolge (Erben → Bestattungspflichtige → Sozialamt) — Page korrekt?
- "Erforderliche Kosten" als "einfach, würdig, ortsüblich" — Page korrekt?
- KEINE Pauschal-Begrenzung (BSG/VG-Rechtsprechung) — Page erwähnt das?
- Schonvermögen + 8.700–10.500 € VG-Urteile — Page erwähnt?
- Bargeldfreibetrag 10.000 € SGB XII — Page erwähnt?
- Sozialbestattung vs Ordnungsamtsbestattung-Abgrenzung — Tabelle/Erklärung sauber?
- Zuständiges Sozialamt: am Sterbeort (nicht Wohnort Antragsteller) — Page korrekt?

### Linse 4: Mythen-Adressierung
Quellen-Pack listet 5 häufige Mythen. Werden die in der Page adressiert (entweder explizit oder implizit durch korrekte Darstellung)?
1. "Sozialamt zahlt nur 800 €" → gekippte Pauschal-Begrenzung
2. "Erst Erbschaft annehmen" → falsch
3. "Sozialbestattung = anonyme Feuerbestattung" → falsch (das ist Ordnungsamt)
4. "Antrag VOR Bestattung Pflicht" → falsch
5. "Bestattungsvorsorge muss aufgelöst werden" → falsch (Schonvermögen)

### Linse 5: Pietät + Brand-Standard
- Sprache neutral, keine Marketing-Floskeln? (Memory: kein "Lockangebot"-Wording, kein Angstmarketing)
- Disclaimer da (keine Rechtsberatung, sondern Orientierung)?
- Quellenbox am Ende mit Verlinkungen zu Primärquellen?
- Crosslinks zu BL-Pages / Stadt-Pages / bestattungskosten?
- JSON-LD FAQ wortgleich zu HTML-FAQ? (Rich-Result-Risiko)

## RÜCKGABE
- Pro Linse: PASS / TUNE / RE-OPEN + konkrete Findings (Zitate)
- Top-3 Critical-Fixes (was MUSS vor Deploy noch geändert werden)
- Liste der nicht-blockierenden Polish-Punkte
- Methodische Eigen-Kritik (was hast du NICHT prüfen können?)

Antwortlänge: strukturiert kompakt, max 2500 Worte.
