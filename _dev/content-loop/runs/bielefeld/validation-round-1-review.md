Ich review jetzt die Bielefeld-Seite.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/bielefeld/index.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/bielefeld/index.html

Ich gehe systematisch durch die MAJOR-Kriterien.

1. FAQ-Schema vs HTML Mismatch:

Schema hat 8 FAQs, HTML hat 8 FAQs ✓
Reihenfolge weicht ab (Schema: muslim→baum, HTML: baum→muslim) — nicht kritisch für Google
Wortlaut FAQ "Ruhezeit": Schema sagt "Kindern unter sieben Jahren", HTML sagt "Kindern bis zur Vollendung des siebten Lebensjahres" — ❗ inhaltlich identisch, aber Wortlaut-Mismatch

2. Selbstwidersprüche:

Sennefriedhof: Hero sagt "98 Hektar großen Sennefriedhof, einem der drei größten Friedhöfe Deutschlands" + Body "drei größten Friedhöfen Deutschlands — vergleichbare Anlagen finden sich in Hamburg-Ohlsdorf und München-Waldfriedhof" → ❗ FAKTISCHER FEHLER: München-Waldfriedhof ist ~165 ha, Ohlsdorf ~389 ha, aber die Top-3 der größten deutschen Friedhöfe sind Ohlsdorf, München-Waldfriedhof und Sennefriedhof — das passt. ABER: Hamburg-Ohlsdorf ist mit 389 ha deutlich größer, München-Waldfriedhof mit 165 ha auch größer → Sennefriedhof (98 ha) ist NICHT die Nr. 3 in Deutschland. Der Hauptfriedhof Frankfurt (~70 ha), Stahnsdorfer Südwestkirchhof (~206 ha), Friedhof Heerstraße Berlin etc. → Aussage "drei größten" ist riskant. Wikipedia listet Sennefriedhof üblicherweise als "einen der größten", nicht Top-3.

3. Adresse Friedhofsverwaltung: "Am Stadtholz 24, 33609 Bielefeld" — Umweltbetrieb Bielefeld sitzt tatsächlich Am Stadtholz 24, 33609. ✓

4. §-Nummern BestG NRW: §9 Leichenschau, §13 Fristen, §14 Sarg, §16 zweite Leichenschau — passt zum NRW BestG.

5. Bertelsmann auf Johannisfriedhof: Carl Bertelsmann ist tatsächlich auf dem Johannisfriedhof bestattet ✓

STADT: BIELEFELD
VERDICT: MAJOR-FIX

1. Inhaltsfehler "drei größte Friedhöfe Deutschlands"

Wo: Hero-Lead + Sennefriedhof-Absatz ("gehört zu den drei größten Friedhöfen Deutschlands — vergleichbare Anlagen finden sich in Hamburg-Ohlsdorf und München-Waldfriedhof")
Problem: Sennefriedhof (98 ha) ist deutlich kleiner als Ohlsdorf (~389 ha), München-Waldfriedhof (~165 ha) und Stahnsdorfer Südwestkirchhof (~206 ha). Top-3-Behauptung ist faktisch falsch.
Fix: "einer der größten Friedhöfe Deutschlands" (ohne Top-3-Claim) — konsistent mit FAQ-Wortlaut, der bereits korrekt "gehört zu den größten" sagt.

2. FAQ-Schema vs HTML Wortlaut-Drift (Ruhezeit Kinder)

Wo: FAQ-Schema "Kindern unter sieben Jahren" vs. HTML-FAQ + Body "bis zur Vollendung des siebten Lebensjahres"
Problem: Inhaltlich identisch, aber Google flaggt Wortlaut-Mismatch im FAQ-Schema.
Fix: Schema-JSON angleichen an HTML-Wortlaut ("bis zur Vollendung des siebten Lebensjahres").

3. Pellafriedhof — unbelegte Detailbehauptung

Wo: Bethel-Absatz ("Seit 2017 vergibt der Pellafriedhof keine neuen Grabnutzungsrechte mehr")
Problem: Konkrete Jahreszahl 2017 + Stilllegungs-Claim ohne Quelle in Quellenliste (Bethel.de nur generisch verlinkt). Halluzinationsrisiko.
Fix: Entweder Primärquelle (Bethel-Pressemitteilung / OWL-Presse) ergänzen oder Behauptung weicher formulieren ("läuft seit einigen Jahren stillschweigend aus, Neuvergaben sind eingestellt").