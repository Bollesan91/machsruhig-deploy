Ich hole die Seite und prüfe.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/dortmund/index.html?cb=1779091636766

STADT: Dortmund

VERDICT: PASS mit Vorbehalt – inhaltlich solide, drei MAJOR-Issues blockieren aber Veröffentlichung.

MAJOR 1 – Falsche Adresse Hauptfriedhof (Faktencheck-Risiko, YMYL-kritisch) Die Seite gibt durchgehend „Am Gottesacker 25, 44143 Dortmund" für Hauptfriedhof + Krematorium an (Hero, Schema.org #hauptfriedhof, Kontakttabelle, FAQ, Keyfacts). Die offizielle Adresse des Hauptfriedhofs Dortmund lautet jedoch Rennweg 65, 44143 Dortmund. „Am Gottesacker" ist nach dortmund.de nicht die Anschrift – das ist im Sterbefall ein Navigationsfehler mit echten Folgen. Auch PLZ 44149 für Sozialamt Hospitalstraße 2-4 ist zu verifizieren (Innenstadt-PLZ tendenziell 44135/44137).

MAJOR 2 – „32 städtische Friedhöfe" mehrfach unbelegt zitiert Zahl steht in Keyfacts, Hero, FAQ und Quellen, der verlinkte Stadt-Dortmund-Link bestätigt sie aber nicht sichtbar im Seitentext. Da diese Zahl ein zentrales Authority-Signal ist (FAQ-Schema → Rich Result), muss sie entweder über einen sekundären Beleg (Statistikportal Stadt Dortmund) abgesichert oder weichgespült werden („über 30"). Sonst Abstrahlung auf Trust der Gesamtseite.

MAJOR 3 – §-Referenz BestG NRW §13 Bestattungsfrist ist falsch zitiert Text: „Bestattungsfristen (Erd- und Aschebeisetzung innerhalb von zehn Tagen) in §13". Tatsächlich regelt §13 BestG NRW die Sargpflicht; Bestattungsfristen stehen in §16 BestG NRW. Die Sargpflicht-Aussage in der FAQ verweist korrekt auf §13 – aber die Frist-Zuordnung ist sachlich falsch. Bei YMYL + zitierter Norm = harter MUST-FIX.

Reihenfolge §8 next-of-kin korrekt. Gebühren-Disclaimer sauber gelöst. Hidden Gems gut.