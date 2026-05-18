Ich prüfe die Wuppertal-Seite jetzt.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/wuppertal/index.html

STADT: WUPPERTAL
VERDICT: MAJOR-FIX

1. FAQ-Schema vs HTML Mismatch (§13) Wo: JSON-LD FAQPage, Frage „Welches Bestattungsrecht gilt in Wuppertal?" Was: Schema sagt § 13 (Sargpflicht bei Erdbestattung) — HTML-FAQ sagt § 13 (Sargpflicht bei Erdbestattung **mit Ausnahmen für religiöse Bestattungen**). Inhaltlicher Mismatch zwischen strukturierten Daten und sichtbarem Text. Fix: Schema-Text an HTML-Version angleichen (Ausnahmen-Zusatz ergänzen).

2. Standesamt-Adresse: PLZ-Mismatch Schema vs HTML Wo: FAQ-Schema („Wo wird der Sterbefall angezeigt?") Was: Schema nennt nur Johannes-Rau-Platz 1 (Barmen) ohne PLZ — HTML/FAQ-HTML nennen 42275 Wuppertal-Barmen. Zusätzlich Plausibilitäts-Check empfohlen: Johannes-Rau-Platz 1 liegt laut Stadt Wuppertal 42269 (Barmen), nicht 42275. Bitte mit wuppertal.de gegenprüfen. Fix: Korrekte PLZ verifizieren (vermutlich 42269) und in HTML + Keyfacts + FAQ + FAQ-Schema konsistent setzen.

3. § 8 BestG NRW — Aschebeisetzungs-Frist Wo: Abschnitt „Bestattungsrecht in Wuppertal", § 8 Abs. 1 Was: Behauptung „Aschebeisetzung muss innerhalb von sechs Wochen nach der Einäscherung erfolgen". § 8 BestG NRW kennt diese 6-Wochen-Frist für die Aschebeisetzung in dieser Form nicht als bundeseinheitliche NRW-Regel — sie stammt typischerweise aus Friedhofssatzungen, nicht aus § 8 BestG NRW. Gefahr Halluzination/falsche §-Zuordnung. Fix: Gegen aktuellen BestG-NRW-Volltext prüfen; ggf. Aussage auf „nach Friedhofssatzung" umformulieren oder streichen.

(247 Wörter)