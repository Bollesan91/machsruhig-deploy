Ich hole die Datei und prüfe.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/koeln/index.html?cb=1779100151698
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/koeln/index.html?cb=1779100151698

STADT: Köln

VERDICT: MAJOR-FIX

Fund 1 — Selbstwiderspruch muslimische Bestattung (Jahr 1965 vs 1968)

Wo: Oberer Block ("Westfriedhof — Hidden Gem", Hero, Key-Facts, FAQ-Schema, Article-Lead) sagt durchgängig 1965. Unterer Block ("Multikulturalität", FAQ-HTML "Welche islamischen Bestattungsoptionen") sagt 1968.
Fix: Auf 1965 vereinheitlichen (mehrfach belegt im Top-Teil + JSON-LD #westfriedhof description). Beide HTML-FAQ-Stellen ("seit 1968" → "seit 1965") sowie den Fließtext-Abschnitt "Multikulturalität" korrigieren.

Fund 2 — FAQ-Schema vs HTML komplett unterschiedlich

Wo: JSON-LD FAQPage hat 6 Fragen (Friedhöfe in Köln / Kosten / muslimische Bestattung / Sterbeurkunde Standesamt / Bestattungsfrist / Karnevalisten-Bestattung). HTML-FAQ hat 5 völlig andere Fragen (Kosten / Melaten / Schnelligkeit / Wasserbestattung / Islamische Optionen). Nur "Kosten" überlappt thematisch — Antworten weichen aber inhaltlich ab (Schema: 1.500–12.000 €; HTML: 4.000–6.000 € + 2.600 € Urne / 2.900–3.000 € Erdwahl / Trauerhalle 198 €).
Fix: FAQ-Schema an die 5 sichtbaren HTML-Fragen/Antworten angleichen (sonst Schema-Spam-Risiko, Google-Rich-Result-Verlust).

Fund 3 — Dubletten + struktureller Doppelblock

Wo: Sektion "Bestattungsrecht in Köln" (oben, sauber mit § 4a BestG NRW) wird später durch zweite Sektion "Bestattungsrecht in NRW (BestG NRW)" dupliziert — mit abweichendem Stil, "36-Stunden-Überführung" (nicht aus BestG NRW belegt), "Waldbestattung als Ausnahme vom Friedhofszwang" (falsch — Waldbestattung = Friedhof, kein Ausnahmetatbestand), Zuständigkeit "Amt für Landschaftspflege und Grünflächen" (Köln nutzt "Amt für Landschaftspflege und Grün" — Bezeichnung prüfen, oben steht "Friedhofsamt"). Außerdem fehlt das schließende </div> der Westfriedhof-Sektion vor diesem Doppelblock.
Fix: Zweite "BestG NRW"-Sektion löschen, fehlendes </div> schließen, Behördenbezeichnung mit Key-Facts ("Friedhofsamt") konsistent machen.