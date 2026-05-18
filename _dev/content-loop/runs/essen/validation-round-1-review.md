Ich lade die Datei.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/essen/index.html?cb=1779091554776

Ich prüfe die wichtigsten MAJOR-Issues durch.

Prüfungen:

1. § 8 BestG NRW Reihenfolge: Text sagt "Ehegatten/Lebenspartner → volljährige Kinder → Eltern → Geschwister → Großeltern → Enkel". Tatsächliche BestG NRW §8 Reihenfolge: Ehegatte/Lebenspartner → volljährige Kinder → Eltern → volljährige Enkelkinder → Großeltern → volljährige Geschwister. Die Reihenfolge im Text scheint nicht korrekt zu sein.

2. Südwestfriedhof - angelegt 1914 vs. Bode-Bauten 1925-29: Konsistent.

3. Parkfriedhof Eröffnung: Text "16. Dezember 1924" — konsistent durchgehend.

4. FAQ HTML vs Schema: 9 FAQs in HTML (inkl. "ALDI-Äquator"), aber nur 8 im FAQPage-Schema (ALDI-Äquator fehlt im JSON-LD). → MISMATCH.

5. Schema-Adresse Ostfriedhof: "45128 Essen" — Südostviertel hat tatsächlich PLZ 45130/45128. Hausnummer fehlt aber im Schema, in HTML steht nur "Saarbrücker Straße" ohne Nummer — konsistent intern.

6. Krematorium PLZ: Schema "45279", HTML "45279 Essen-Freisenbruch". Konsistent. 45279 = Freisenbruch ✓

7. Cross-Links: /bestatter/dortmund/, /duisburg/, /duesseldorf/, /bochum/ — laut Memory existieren Dortmund + Bochum. Düsseldorf/Duisburg unklar.

8. Heinemann OB-Zeit 1945-1949: Korrekt.

9. Schema FAQ #6 Tuchbestattung: zitiert "§ 15 BestG NRW" → Sargregelung. § 15 ist die korrekte Norm in der Fassung von 2003. ✓

STADT: Essen

VERDICT: MUST-FIX (2 MAJOR)

Funde:

§ 8 BestG NRW – falsche Rangfolge. Text: "Ehegatten → Kinder → Eltern → Geschwister → Großeltern → Enkelkinder". Korrekt nach BestG NRW: Ehegatte/Lebenspartner → volljährige Kinder → Eltern → volljährige Enkelkinder → Großeltern → volljährige Geschwister. Geschwister und Enkel/Großeltern stehen in falscher Position. MUST-FIX, da §-zitierte YMYL-Aussage.
FAQ-Schema vs HTML Mismatch. HTML enthält 9 <details>-Blöcke inkl. "Was ist der ALDI-Äquator?" – JSON-LD FAQPage.mainEntity listet nur 8 Fragen, ALDI-Äquator fehlt. Entweder Frage aus HTML entfernen (passt nicht zu YMYL-FAQ) oder in Schema ergänzen. Empfehlung: aus HTML-FAQ raus, ist eher Trivia.
Krematorium-Brennkammern unbelegt. "Drei Brennkammern" steht zweimal (HTML + Schema), aber im Quellenverzeichnis kein Beleg dafür auffindbar – krematorium-essen.de wird zwar verlinkt, Zahl ist nicht primärquellenbasiert. Bei YMYL-Niveau der Seite Risiko: entweder Quelle ergänzen oder Aussage abschwächen ("mehrere Brennkammern").