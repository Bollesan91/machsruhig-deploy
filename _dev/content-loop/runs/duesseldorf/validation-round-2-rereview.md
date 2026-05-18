Ich hole die Datei und prüfe nur Major-Issues.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/duesseldorf/index.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/duesseldorf/index.html

Major-Check durchgegangen. Wichtigste Findings:

STADT: DUESSELDORF VERDICT: MAJOR-FIX

1. Friedhofsamt-Adresse falsch (Hallu-Risiko, schwer) Wo: JSON-LD #friedhofsamt (streetAddress "Marktplatz 2") + Kosten-Sektion-Fließtext ("Friedhofsamt (Marktplatz 2, 40213 Düsseldorf, Tel. 0211-8991)"). Problem: Marktplatz 2, 40213 ist das Rathaus / OB-Sitz, nicht das Garten-, Friedhofs- und Forstamt. Der Improver-Auftrag war explizit GFFA = Auf'm Hennekamp 45, 40225 Düsseldorf — dort sitzt das Amt. Die Telefon-Hauptnummer 0211 8991 ist außerdem die generelle Stadt-Servicenummer, nicht direktes Friedhofsamt. Fix: streetAddress/Fließtext auf Auf'm Hennekamp 45, 40225 Düsseldorf ändern, Telefon entweder entfernen oder durch verifizierte GFFA-Durchwahl ersetzen.

2. Selbstwiderspruch Gebührentabelle vs. Improver-Auftrag Wo: Sektion „Bestattungskosten in Düsseldorf", Tabelle + einleitender Satz. Problem: Auftrag = „Gebührentabelle 2026". HTML zeigt aber weiterhin „Gebühr (Stand 01.01.2024)" mit 2024er-Beträgen und einem ausweichenden Disclaimer („2026er Fassung passt diese Beträge an"). Tabelle widerspricht damit der Sektionsüberschrift und dem H1-Versprechen einer 2026-Seite. Fix: Entweder echte 2026-Tarifbeträge aus 68.203.1 einsetzen — oder Tabelle komplett rausnehmen und durch reinen Verweis auf 68.203.1 ersetzen. Mischzustand ist YMYL-Risiko.

3. Faktencheck Trinkaus / „HSBC Trinkaus" Wo: Nordfriedhof-Absatz Millionenhügel. Problem: Firmiert seit Februar 2022 als HSBC Continental Europe S.A., Germany — Marke „HSBC Trinkaus" ist abgelegt. „später HSBC Trinkaus" ist veraltet/irreführend zum Stand 2026. Fix: Klammer streichen oder auf „später HSBC Trinkaus & Burkhardt, heute HSBC Continental Europe" präzisieren.

FAQ-Schema ↔ HTML-FAQ: 7/7 Fragen 1:1 deckungsgleich, sauber. §-Nummern BestG NRW (§§ 8/13/14): korrekt. Keine leeren Sektionen, Cross-Links intern auflösbar.