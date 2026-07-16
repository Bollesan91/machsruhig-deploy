# Externes YMYL-Live-Audit 16.07.2026 — Triage & Abarbeitung

> Quelle: von Bolle eingereichtes externes Audit (Score 67/100, 16 Findings, 72h/30d/90d-Plan).
> V4.1-Stufe-3: jedes Finding selbst gegen die Primärquelle verifiziert — Reviewer irren in beide Richtungen.
> Score = Telemetrie eines fremden Systems, nicht vergleichbar mit unseren Wellen.

## Triage-Tabelle (72h-Liste — alle abgearbeitet 16.07.2026)

| # | Finding | Verifikation | Status |
|---|---------|--------------|--------|
| 1 | „Gesetzliche Mindestangaben eines Kostenvoranschlags (§ 649 BGB)" | **BESTÄTIGT.** § 649 BGB (heute primärverifiziert) regelt den Kostenanschlag: keine Gewähr + Anzeigepflicht bei wesentlicher Überschreitung — er definiert KEINE Mindestangaben/Pflichtinhalte. | ✅ GEFIXT: `angebotsstandard.html` (4 Stellen), `was-muss-im-kostenvoranschlag-stehen.html` (FAQ-Frage+Antwort, sichtbar + JSON-LD) |
| 2 | Falsches § 5 PAngV-Zitat (Preisverzeichnis-Pflicht) | **BESTÄTIGT.** § 5 PAngV 2022 = „Mengeneinheit für die Angabe des Grundpreises" (gesetze-im-internet.de, 16.07. verifiziert). Preisverzeichnisse für Leistungen regelt **§ 12** — und der nimmt gerade „Leistungen, die üblicherweise aufgrund von schriftlichen Angeboten oder schriftlichen Voranschlägen erbracht werden, die auf den Einzelfall abgestellt sind" AUS (typisch Bestattung). Das alte Zitat war ein Alt-PAngV-Relikt (vor 2022 war § 5 „Leistungen"). | ✅ GEFIXT: `bestatter/nuernberg` (Satz + Quellen-Link → § 12), Pauschal-Sätze entschärft auf `bonn`, `regensburg`, `duesseldorf` (inkl. Streichung „auf Verbraucherwunsch zu schriftlichen KV verpflichtet" — steht nicht in der PAngV), `rostock` („vgl. PAngV" als Beleg für Posten-Aufschlüsselung entfernt) |
| 3 | „Die Kosten tragen die Angehörigen — und zwar sofort" zu pauschal | **BESTÄTIGT.** Kostentragung differenziert: § 1968 BGB (Erben), vertragliche Auftraggeberhaftung, landesrechtliche Bestattungspflicht, § 74 SGB XII (Sozialamt). | ✅ GEFIXT: `vorsorge/index.html` |
| 4 | Digitaler Nachlass: BGH-2018-Pauschalisierung („alle Konten, Plattformen müssen Zugang gewähren") | **BESTÄTIGT.** BGH III ZR 183/17 betraf den Nutzungsvertrag eines sozialen Netzwerks; kein pauschaler technischer Zugriffs-Freibrief für jede Kontoart. | ✅ GEFIXT: `vorsorge/digitaler-nachlass` — beide Pauschal-Sätze gescopet (je 2×: sichtbar + JSON-LD) |
| 5 | Digitaler Nachlass: fehlende Warnung vor eigenmächtiger Nutzung von Onlinebanking-Zugangsdaten | **BESTÄTIGT** (Risiko real: Erbstreit, unberechtigter Zugriff). | ✅ GEFIXT: mr-hint „Wichtig bei Bank- und Zahlungskonten" nach dem Gesetzes-Abschnitt eingefügt (Weg über die Bank mit Erbnachweis/Vollmacht) |
| 6 | Methodik vs. Datenschutz: „zwei vs. drei Ausnahmen" widersprüchlich | **FALSE POSITIVE.** `methodik.html` sagt bereits „Drei Ausnahmen" (Z. 142 + 300), konsistent mit Datenschutz. | ❌ verworfen, dokumentiert |
| 7 | „Anonyme Datenspende" ist zum Sendezeitpunkt nicht anonym | **TEILWEISE BESTÄTIGT.** Die Offenlegung (Datenschutz 6a) war bereits ehrlich und präzise: Netlify-IP-Logging, 30–60-Tage-Trennung, EG-26-Begründung, Widerrufsfenster. ABER Button/Labels behaupteten „anonym" zum Klick-Zeitpunkt — laut eigenem Text tritt Anonymität erst NACH der Trennung ein. | ✅ GEFIXT: Wording konsistent — Button „Eckdaten spenden", Labels „ohne Namen und ohne Angaben zu deiner Person" (`tools/angebotspruefer` 5 Stellen, `datenschutz.html` 4, `methodik.html` 1). Substanz/Verfahren unverändert. |
| 8 | Bremen: Gebühren auf 2020er-Stand | **BESTÄTIGT für `bestatter/bremen/`** (die `friedhoefe/bremen/`-Seite war aktuell). Aktuelle Gebührenordnung = Ortsgesetz 16.12.2025 (Brem. GBl. Nr. 154), heute per pdfplumber-Koordinaten primär erhoben. | ✅ GEFIXT: Tabelle komplett neu (6 Positionen mit Gebührenziffern: 00.00=998, 00.01=1.149, 00.09.00=1.333, 00.09.02=1.502, 00.05.02 Kolumbarium=3.183, 00.05.00 Anonym=975), Verlängerungs-Logik aus Ziffer 09.00 (nur Wahlgräber, 1/20 je Jahr), Quellen-Link auf verkündetes PDF |
| 9 | 112/116117-Logik inkonsistent | **BESTÄTIGT für 4 von ~30 Seiten.** Kanonische Regel (`was-tun-nach-todesfall.html`, korrekt): erwarteter Tod → Hausarzt/116117; 112 NUR wenn unklar ob die Person lebt / gerade zusammengebrochen (Reanimation). Falsch waren: `bochum` („nachts → 112"), `duisburg` (112 als gleichwertige Leichenschau-Alternative), `regensburg` („bei akutem Sterben → 116117"), `muenchen` (112-Reanimationsfall fehlte, direkter 110-Rat). Übrige ~25 Seiten gescannt: Logik korrekt („bei unklarer Lage 112"). | ✅ GEFIXT (4 Seiten) |
| 10 | Saarbrücken zitiert § 649 falsch | **FALSE POSITIVE.** „649" auf der Seite ist Teil einer Telefonnummer. | ❌ verworfen, dokumentiert |
| 11 | Indexierte „Kommt bald"-Seite (vorsorge-ordner) mit „rechtlich geprüft"-Claim | **TEILWEISE FALSE POSITIVE.** Seite hatte bereits `noindex,follow` und stand NICHT in der Sitemap. Aber die FAQ-Antwort suggerierte Rechtskonformität eines unveröffentlichten Produkts. | ✅ GEFIXT: FAQ-Antwort ehrlich („in Arbeit, noch nicht anwaltlich geprüft"), sichtbar + JSON-LD |

## 30d/90d-Punkte (brauchen Bolle — unverändert offen)

- Externer Jurist: Voll-Prüfung der Rechtsaussagen (→ Spur A Anwalt, deckt sich mit bestehendem Backlog)
- Benannter Bestattungsfachmann / Fach-Reviewer + Prüferprofile (→ Partner-/Reviewer-Strategie, GAMECHANGER-AUDIT)
- Medizinische Freigabe der Sterbebegleitungs-Inhalte
- Sterbegeld-Affiliate-Interessenkonflikt kennzeichnen (redaktionelle Entscheidung Bolle)
- Löschfristen-Übersicht im Datenschutz vervollständigen
- ZDR Groq-Console + AV-Verträge (bekannt, liegt beim User)
- Templated-City-Pages-Kritik: bewusste Architektur-Entscheidung (Register-getrieben, Substanz-Gate) — kein 72h-Defekt, ggf. Differenzierung im Zuge Verdichtung 2.0

## Lehren

- **Alt-Normzitate überleben Novellen:** § 5 PAngV a.F. („Leistungen") wurde 2022 zu § 12; unser Text zitierte noch die alte Nummer mit Link auf die NEUE Fassung — der Link „belegte" damit das Falsche. Normzitat + Fassung IMMER zusammen pinnen (Stufe 0).
- **Ein externes Audit ist ein Reviewer wie jeder andere:** 3 von 11 72h-Findings waren ganz oder teilweise False Positives (§-649-Saarbrücken, Zwei-Ausnahmen, vorsorge-ordner-Index) — Stufe-3-Selbstverifikation bleibt Pflicht.
