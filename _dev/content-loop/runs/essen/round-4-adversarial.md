Ich lade die drei Dateien.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

BRIEFING_OK. Adversarial Review v2:

SCORE: 83/100

FUNDE:

SCHWÄCHE 1: Krematorium-Sektion zitiert § 14 BestG NRW falsch — Der Satz "mit der das Krematorium dann die Sechs-Wochen-Frist nach § 14 BestG NRW überwacht" verortet die Urnenbeisetzungsfrist in § 14 BestG NRW. Tatsächlich ist § 14 BestG NRW das Krematoriumsrecht; die 6-Wochen-Frist für Urnenbeisetzung steht nicht in § 14, sondern ergibt sich aus § 13 Abs. 4 BestG NRW (Bestattungsfristen). Die Page nutzt § 13 BestG NRW an zwei anderen Stellen korrekt für die Erdbestattungsfristen, springt hier aber auf § 14. Halluzinations-Verdacht / falsche §-Zuordnung in einer YMYL-Aussage — kritisch, weil die Page genau auf juristische Genauigkeit setzt. Fix: § 14 entfernen, „nach § 13 Abs. 4 BestG NRW" oder neutral „nach BestG NRW" formulieren.

SCHWÄCHE 2: Parkfriedhof-Daten innerlich widersprüchlich + ungeprüfte Detailzahl — Im Schema.org steht "eröffnet 1924", im Fließtext "Der erste Bauabschnitt wurde 1923 begonnen und bereits am 16. Dezember 1924 vorzeitig in Betrieb genommen" — also Eröffnung 1924, aber die Hidden-Gem-Sektion behauptet "Seit 2019 ergänzt ein Außenkolumbarium das Angebot; auf vier Gräberfeldern liegen 2.045 Opfer des Zweiten Weltkrieges, darunter 213 sowjetische Kriegsgefangene und 52 KZ-Opfer." — die hochspezifischen Zahlen 2.045 / 213 / 52 stehen ohne Inline-Verweis auf Quelle 10 (Volksbund) oder 11. Die Round-2-Kritik forderte konkret die Verifizierung "29.000 Stellen" — diese wurde rausgenommen, aber durch drei neue ungeprüfte Spezialzahlen ersetzt. Halluzinations-Verdacht-Vektor wurde verschoben, nicht behoben. Fix: Entweder Inline-Zitat „(Quelle: Volksbund)" am Satzende, oder Zahlen auf „über 2.000 Kriegsopfer, darunter Hunderte sowjetische Kriegsgefangene und KZ-Opfer" abrunden.

SCHWÄCHE 3: Friedhofsgebührensatzung weiterhin nicht konkret zitiert — MUST-FIX #4 aus Round 2 unerfüllt — Der Review v1 forderte explizit: „Mindestens 3 konkrete Gebührenwerte aus der Friedhofsgebührensatzung der Stadt Essen (Quelle Nr. 3) in die Kostentabelle integrieren oder als belegte Beispiele einzeln nennen — sonst Satzungs-Quelle entfernen." v2 löst das mit einem Ausweichmanöver: ein Hinweis-Absatz nennt drei Positionen, die "direkt im Satzungsdokument geprüft werden" sollten — also: Page sagt dem Leser, er soll selbst nachschlagen. Quelle Nr. 3 bleibt im Quellenverzeichnis, aber kein einziger Euro-Wert stammt nachweislich aus ihr. Die Tabellen-Caption beschreibt sie offen als „Orientierungswerte" / „Marktbeobachtungen". Das ist genau der Vorwurf aus Round 2 (vorgeschobene Quelle), nur höflicher umformuliert. Fix: Entweder echte Euro-Werte aus SR704neu.pdf ziehen (PDF ist verlinkt — Chat A hätte sie fetchen können), oder Quelle Nr. 3 als Hauptquelle für die Gebührentabelle aus der Liste streichen und nur als „weiterführender Beleg" markieren.

Zusatz-Findings (nicht in den 3 Hauptschwächen, aber Notizen):

Parkfriedhof-Adresse "Am Parkfriedhof 33" wird nirgends durch eine Quelle gestützt (Schema.org claimt sie). Plausibel, aber unverifiziert → Halluzinations-Risiko.
"Friedhofssatzung der Stadt Essen vom 27. Juli 2025" — Datum 27. Juli 2025 erscheint dreimal. Quelle Nr. 2 verlinkt SR703neu.pdf, aber das genaue Datum 27.07.2025 wurde im Review-Kontext nicht verifiziert. Bei juristischen Daten ist Pseudo-Präzision riskanter als Vagheit.
Floskel-Restbestände: „bewegt sich zwischen kommunaler Friedhofssatzung, Landesrecht und einer ungewöhnlich dichten Friedhofslandschaft" (Lead) und „Essen hat eine ungewöhnlich tief geschichtete Friedhofslandschaft" — zweimal „ungewöhnlich [adj] Friedhofslandschaft" innerhalb von 200 Wörtern. Stilistisch repetitiv.
FAQ-Schema-Hygiene: v1 forderte den ALDI-Äquator aus dem FAQ-Schema zu entfernen. v2 hat das gemacht (er ist im HTML als <details>, aber NICHT in mainEntity des FAQPage-Schemas) — und kennzeichnet das auch offen im Body („Diese FAQ ist nicht Teil des FAQPage-Schemas, da sie redaktioneller Natur ist."). Diese Meta-Anmerkung im sichtbaren Body ist Page-fremd — interner Redaktions-Kommentar an Leser geleakt. Fix: Satz entfernen.

MUST-FIX vor Deploy: ja — wegen Schwäche 1 (falscher §-Verweis ist YMYL-kritisch und in 5 Minuten zu korrigieren) und Schwäche 3 (Quellen-Lücke aus Round 2 weiterhin offen — die Page beansprucht juristisch-finanzielle Autorität, liefert für die Kostenseite aber keinen einzigen verifizierten Euro-Wert aus der zitierten Satzung). Der Meta-Kommentar im FAQ-Body („Diese FAQ ist nicht Teil des FAQPage-Schemas…") muss zusätzlich vor Deploy raus.

Ehrliche Einschätzung: v2 ist gegenüber v1 (76%) ein echter Sprung — Krematorium-Sektion sitzt, 23 Friedhöfe sind drin, jüdischer Friedhof erwähnt, Cross-Links da, Ruhezeiten ergänzt, ALDI-Äquator-Schema-Hygiene gefixt, Krupp-Privatfriedhof-Disclaimer drin. Aber: die § 14-Falschzuordnung ist neu eingeführt worden (war in v1 nicht da) und die Gebühren-Quellen-Lücke wurde rhetorisch umgangen statt geschlossen. 83/100, Deploy erst nach drei chirurgischen Eingriffen.