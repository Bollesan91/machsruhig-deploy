Ich fetch die Datei.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/magdeburg/index.html?cb=1779100157782
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/magdeburg/index.html?cb=1779100157782

STADT: Magdeburg

VERDICT: PASS mit 1 MAJOR

FUND 1 — SELBSTWIDERSPRUCH FAQ-Schema vs HTML (FAQPage-Mismatch) Das JSON-LD FAQPage enthält 7 Fragen, das sichtbare HTML-FAQ unter #faq enthält ebenfalls 7 Fragen — aber die Reihenfolge weicht ab:

Schema-Order: Gebühren → Friedhöfe → Ruhezeit → Bestattungsfrist → Standesamt → Sargpflicht → Naturbestattungen
HTML-Order: Gebühren → Friedhöfe → Ruhezeit → Bestattungsfrist → Naturbestattungen → Standesamt → Sargpflicht

Reihenfolgenunterschied ist für Google tolerierbar, ABER: Die Schema-Antwort zu „Welche Friedhofsgebühren fallen in Magdeburg an?" enthält keine Kapellengebühr (296 €), die HTML-Version schon. Inhaltliche Divergenz zwischen Schema-text und sichtbarem Antworttext = Mismatch-Risiko bei Rich-Result-Validierung. Fix: Schema-Answer um „Kapellennutzung (Kategorie I 296 €)" ergänzen, identisch zum HTML.

FUND 2 — HALLUZINATIONS-RISIKO „Mauthausen" Die Cremer-Plastik „O Deutschland, bleiche Mutter" wird als Bronzezweitguss bezeichnet, dessen Original „1961 bis 1965 für die KZ-Gedenkstätte Mauthausen" entstand. Cremers Mauthausen-Mahnmal heißt „Mutter Heimaterde" (1965–67). „O Deutschland, bleiche Mutter" ist ein separates Brecht-Zitat-Werk (1960er), das u. a. auf dem Westfriedhof steht — aber nicht das Mauthausen-Original. Fix: Bezug zu Mauthausen entfernen oder verifizieren über Volksbund-Quelle (steht so nicht in der zitierten Quelle).

FUND 3 — Keiner mit ausreichender Sicherheit. Adressen, §17 BestattG LSA, GewO §14, Standesamt Humboldtstr. 11 plausibel. Cross-Links (/bestattung-in/sachsen-anhalt/, /trauerfeier/, /kosten/, /vorsorge/, /checkliste-todesfall/, /bestattungsarten/) — Status nicht aus dieser Datei prüfbar, kein Fund hier.

(248 Worte)