# Chrome-Audit-Findings — Komplett (9 Stadt-Pages) — 2026-05-27

## Bilanz
- PASS: München, Stuttgart (2/9)
- FAIL: Köln, Leipzig, Dortmund, Frankfurt, Düsseldorf, Berlin, Hamburg (7/9)

## München — VALIDITY_PASS
Nits: CTA "Vergleicht", Friedhofsteil-Liste-Asymmetrie, Westfriedhof-Chronologie 1898/1897-1902, FBM-Literal in Contact-Card fehlt, § 18 Abs. 1 BestV nicht einzeln gezogen.

## Stuttgart — VALIDITY_PASS
Nits: Gebührenbeträge UNVERIFIED (PDF nicht erreichbar), 116117 in Akutbox als Klartext, "Sozialamt" vs "Amt für Soziales und Teilhabe".

## Köln — VALIDITY_FAIL (3 MUST-FIX)
- MF-1: Willy Birgel Z. 211+231 "1909-1979" → korrekt 1891-1973. 1909-1979 sind Daten Deltgens.
- MF-2: tel:-Link defekt Z. 131 `tel:+492212212556` → korrekt `tel:+4922122125560`
- MF-3: UNSURE-Redaktionskommentar Z. 211 live deployed
- Nit: Napoleon-Dekret-Jahr Z. 209 (1805) vs Z. 224 + FAQ 2× (1804). Korrekt: 1804.

## Leipzig — VALIDITY_FAIL
- MF: Du/man-Register-Bruch Z. 429 + FAQ Z. 544 + JSON-LD Z. 201 + Disclaimer Z. 572

## Dortmund — VALIDITY_FAIL
- MF: JSON-LD-FAQ wortgleich mit HTML synchronisieren (alle 8 Antworten), H1 ggf Subtitle

## Frankfurt — VALIDITY_FAIL (3 MUST-FIX)
- MF-1 (Lens C): FAQ-Drift Q3, Q4, Q6 (JSON-LD ≠ HTML)
  - Q3 Kosten: HTML "…und in einer Urnenkammer bei rund 789 Euro." fehlt in JSON-LD
  - Q4 Recht: JSON-LD "…Details unter /bestattung-in/hessen/." vs HTML "Eine vollständige Übersicht findet sich auf der Seite Bestattung in Hessen."
  - Q6 Behörde: JSON-LD "…betreut 37 kommunale Friedhöfe…" vs HTML "…betreut die 37 kommunalen Friedhöfe Frankfurts…"
- MF-2 (Lens A+B): Rat-Beil-Straße widerspricht sich + faktisch falsch
  - "ab 1929 belegt" (Z.26, 181, 210) vs "bis 1928 in aktiver Nutzung" (Z.26, 181)
  - Primärquelle: 1828-1928 genutzt, letzte Beisetzung 18.09.1928. 1929 geschlossen, Nachfolge Eckenheim.
- MF-3 (Lens A+B): 48h-Frist falsch eingeordnet
  - Z.188 "innerhalb 48h überführt" widerspricht Z.150 "Mindestfrist 48h"
  - Primärquelle: 48h ist Mindestfrist (frühestens), spätestens 10 Tage
- Nits: 36 vs 37 Friedhöfe (Primärquelle 36), Freitag 8-12/13-15 falsch (nur 8-12), "650 Jahre 1272-1828" = 556 Jahre, "Hidden Gem" 4× zu marketing.

## Düsseldorf — VALIDITY_FAIL (2 MUST-FIX)
- MF-1: tel:-Link Z.396 `tel:+4921189911` → korrekt `tel:+492118991` (Anzeige "0211 89-91" korrekt)
- MF-2 (Lens C): FAQ-Wortgleich-Drift in 2/7 — Anführungszeichen-Glyphen
  - Q "Millionenhügel": JSON 'Schreibtisch' vs HTML „Schreibtisch"
  - Q "Tote-Hosen-Grab": JSON 'Wölli' vs HTML „Wölli"
- Nits: Nordfriedhof Stadtteil-Inkonsistenz, Stoffeler 42,36 vs 42 ha, Akutbox ohne tel:-Link, UNVERIFIED-Zahlen

## Berlin — VALIDITY_FAIL (2 MUST-FIX)
- MF-1: Friedrichsfelde halluziniert in Brandenburg (Z.408) — gleichzeitig Tabelle sagt Lichtenberg. "Friedhof Berlin-Friedrichsfelde-Spreebogen-Erweiterung" existiert nicht.
- MF-2: 116 vs 118 evangelische Friedhöfe in 3 Stellen widersprüchlich
  - Z.266 Tabelle 118, Z.287 Akut 118, Z.407 Zahlen 116
  - Summe stimmt nur mit 118: 85+118+9+10=222
- Nits: UNSURE-Kommentar Z.428 live, 116117 ohne tel-Link, München-Karte → /bestatter/ statt /bestatter/muenchen/, Breadcrumb-Slash-Drift, Du/du-Inkonsistenz

## Hamburg — VALIDITY_FAIL (3 MUST-FIX)
- MF-1: AöR-Trägerschaft falsch (Z.160, 290, 362, 365)
  - Page sagt: "Ohlsdorf, Öjendorf, Bergedorf, Harburg" 
  - Primärquelle: AöR betreibt Ohlsdorf, Öjendorf, Volksdorf, Wohldorf-Ohlstedt (+Finkenwerder, Finkenriek, Kirchdorf-Amtshof). Bergedorf+Harburg sind bezirkliche Friedhöfe.
  - Folge: Fehlleitung Angehöriger, tote Deeplinks
- MF-2: Aufgehobenes Gesetz zitiert (Z.402, 588)
  - Page: "HmbBestG vom 14.09.1988 (HmbGVBl. S. 167)" 
  - Aktuell: "BestattG vom 30.10.2019 (HmbGVBl. S. 379)", in Kraft seit 01.03.2020
- MF-3: FAQ #2 falscher Superlativ (JSON-LD Z.119-121, HTML Z.559-560)
  - "Ist Ohlsdorf wirklich der größte Friedhof der Welt? → Ja"
  - Korrekt: größter Parkfriedhof, nicht größter Friedhof (Wadi as-Salam ~917 ha)
- Nits: "Ein Muss für Hamburg!" reißerisch, 116117/112 ohne tel-Link, "10 Tagen" ohne §-Anker, BSG-Zitat UNVERIFIED.

## Bulk-Iter-2 Fix-Plan
### Mechanische Fixes (sicher, kein neuer Inhalt)
- A) Köln tel: `tel:+492212212556` → `tel:+4922122125560`
- B) Köln UNSURE-Kommentar Z.211 raus
- C) Köln Napoleon Z.209: 1805 → 1804
- D) Köln Birgel Z.211+231: 1909-1979 → 1891-1973
- E) Berlin UNSURE-Kommentar Z.428 raus
- F) Berlin 116 → 118 evangelische Friedhöfe (Z.407)
- G) Düsseldorf tel: `tel:+4921189911` → `tel:+492118991`
- H) Düsseldorf FAQ-Anführungszeichen-Sync (JSON-LD straight → „")
- I) Frankfurt FAQ-Drift Q3/Q4/Q6 wortgleich-Sync
- J) Dortmund FAQ-Drift alle 8 Antworten wortgleich-Sync
- K) Leipzig Du/man-Bruch Z.429+544+201+572
- L) Hamburg FAQ #2 Frage umformulieren: "größter Parkfriedhof"

### Inhaltliche Fixes (brauchen Helper-V3 Writer oder User-Review)
- M) Frankfurt Rat-Beil-Straße neu formulieren (1828-1928 + Nachfolge Eckenheim)
- N) Frankfurt 48h-Frist Z.188 umformulieren (Mindestfrist, nicht Überführungspflicht)
- O) Berlin Friedrichsfelde-Brandenburg Halbsatz neu (Friedrichsfelde raus, Stahnsdorf richtig benennen)
- P) Hamburg AöR-Trägerschaft korrigieren (Volksdorf/Wohldorf statt Bergedorf/Harburg) + Deeplinks
- Q) Hamburg Gesetz umstellen (BestattG 2019 statt 1988)
