Ich hole die aktuelle Version und prüfe gezielt auf MAJOR-Issues.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/dortmund/index.html?cb=1779092531774
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/dortmund/index.html?cb=1779092531774

STADT: Dortmund (Pass 2)

VERDICT: PASS mit 1 MAJOR-Restbefund. Improver-Fixes sitzen (Rennweg 65 konsistent, "über 30 Friedhöfe" entschärft, § 16 BestG NRW für 10-Tage-Frist in Prosa, Schritte-Liste und FAQ korrekt durchgezogen). Eine inhaltliche Inkonsistenz ist neu/übersehen.

3 FUNDE:

MAJOR – Widerspruch Krematoriums-Geschichte (Body vs. FAQ/Hidden Gem): Die Seite behauptet an drei Stellen, das Krematorium werde "seit 1924 betrieben" (Hidden Gem, Promi-Absatz Hauptfriedhof, FAQ Krematorium). Gleichzeitig steht im Hero/Hauptfriedhof-Absatz, das Hauptgebäude sei "erst 1924 eingeweiht" worden – und die Stadt Dortmund datiert die Krematoriums-Inbetriebnahme auf 1925/26 (Hauptgebäude 1924, Krematoriumstrakt später). "Seit 1924" ist als Faktum nicht durch die verlinkte Stadtquelle gedeckt und sollte entweder auf "Mitte der 1920er-Jahre" entschärft oder mit Primärquelle (Stadt Dortmund / Wikipedia) belegt werden. YMYL-relevant nicht, aber Vertrauens-relevant – und sitzt in 3 Strukturen (Prosa + Hidden Gem + FAQPage-Schema → wandert in Rich Results).
MINOR-grenzwertig MAJOR – § 13 BestG NRW = Sargpflicht? Inhaltlich korrekt verwendet, aber: § 13 BestG NRW regelt nach aktueller Fassung den Umgang mit der Leiche / Aufbewahrung, die Sargpflicht steht in § 15. Bei Bulk-Fix § 16 wurde § 13 nicht gegengeprüft. Risiko: Wenn dieselbe Verwechslung wie zuvor vorliegt, ist sie an 4 Stellen (Prosa + H3 + 2× FAQ + Schema). Bitte vor Deploy gegen aktuelle BestG-NRW-Fassung verifizieren.
MINOR – Ostfriedhof "im aktiven Betrieb stehen Grabfelder, die für jüdische Beisetzungen reserviert sind" – steht im Hauptfriedhof-Absatz, der Kontext ist aber Hauptfriedhof. Lesefluss-Verwechslung möglich; klarstellen, dass dies den Hauptfriedhof betrifft.

EMPFEHLUNG: Fix 1+2 vor Deploy, dann grünes Licht.