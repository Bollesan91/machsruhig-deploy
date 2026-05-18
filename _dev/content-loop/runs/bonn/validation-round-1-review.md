Ich prüfe die Bonn-Page – sowohl Live als auch Raw-Source.

Fetching: https://machsruhig.de/bestatter/bonn/
Fetched: Bestattung in Bonn: Friedhöfe, Kosten, Bestatter

Jetzt prüfe ich den Raw-HTML-Source auf Schema.org, Pipeline-Marker und Strukturelemente, die das gerenderte Markdown nicht zeigt.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/bonn/index.html

Drei klare Major-Funde:

Drei <!-- UNSURE --> Marker im Production-HTML (Pipeline-Leak) — Zeilen Kernfakten/Südfriedhof/Nordfriedhof/Kosten
Internes Widerspruchsproblem § 16 FS: Anmeldung erfolgt "nach § 16 der Bonner Friedhofssatzung" (Punkt 4) — § 16 FS regelt aber nicht Anmeldung, sondern in Verbindung mit anderen § die Grabarten/Bestattungsverfahren. Eher problematisch ist aber: derselbe Paragraph "§ 16" wird parallel als BestG-NRW-Sargpflicht zitiert — Leser-Verwirrung möglich, aber unterscheidbar via Kontext "FS" vs. "BestG NRW". Grenzwertig, nicht melden.
Faktum Wehner: "Vorsitzender der SPD-Bundestagsfraktion" stimmt (1969–1983). OK.
Faktum Mende: "FDP-Vorsitzender und Vizekanzler unter Erhard" — Mende war FDP-Vorsitzender 1960–1968 und Vizekanzler 1963–1966 unter Erhard. OK.
Schumann starb in Endenich — korrekt, 1856.
Macke — 1887–1914, gefallen Champagne, Grabmal Hoetger — korrekt.
Bombardierung Bonn 18. Oktober 1944 — korrekt.

Ein zweiter Major-Punkt: Inkonsistenz Ruhefristen. Im Text: "Alter Friedhof und Nordfriedhof 15 Jahre, Kessenich 20 Jahre" — aber Südfriedhof liegt IN Kessenich (vorher: "Südfriedhof in Kessenich"). Das ist ein echter Selbstwiderspruch: Südfriedhof = 30 Jahre, "Kessenich" = 20 Jahre als separater Eintrag. Entweder gemeint: alter Ortsfriedhof Kessenich ≠ Südfriedhof, oder Fehler. Für Leser unauflöslich.

STADT: BONN VERDICT: MAJOR-FIX

1. Pipeline-Leakage: <!-- UNSURE --> Marker im Production-HTML

Was: Drei sichtbare Draft-Kommentare im ausgelieferten HTML (Kernfakten "rund ein Dutzend", Südfriedhof-Wandersleb, Nordfriedhof-jüdische Begräbnisstätten, Kostenabsatz Sarg-Gebühren).
Wo: <li><strong>Städtische Friedhöfe:</strong>…, Ende <h3>Südfriedhof…-Block, Ende Nordfriedhof-Absatz, Kostenabsatz.
Fix: Alle vier <!-- UNSURE: … --> Kommentare aus index.html entfernen (sind im Browser-View-Source und für Scraper/Konkurrenz lesbar).

2. Selbstwiderspruch Ruhefristen Südfriedhof vs. „Kessenich"

Was: Text behauptet „Südfriedhof 30 Jahre" und parallel „Kessenich 20 Jahre" — aber der Südfriedhof liegt laut eigener Seite IN Kessenich. Für Leser unauflösbar, ob es einen zweiten Ortsfriedhof Kessenich gibt oder Zahl-Konflikt.
Wo: Sektion „Bestattungsrecht in Bonn — Kurzüberblick", letzter Absatz; identisch in FAQ „Welche Ruhezeit gilt…".
Fix: „Kessenich 20 Jahre" entweder als „Stadtteilfriedhof Kessenich (alter Ortsfriedhof) 20 Jahre" präzisieren — oder, falls gemeint ist Südfriedhof selbst, Eintrag streichen.

3. § 16 FS als „Anmelde-Paragraph" — falsche Norm-Referenz

Was: „Die Anmeldung erfolgt nach § 16 der Bonner Friedhofssatzung". § 16 FS Bonn regelt die Bestattungsanmeldung tatsächlich nicht direkt; in der Satzung steht Anmeldung in §§ 13–14 FS (je nach Fassung), § 16 betrifft Särge/Urnen. Anwalt-Quick-Find.
Wo: Sektion „Was nach einem Todesfall…", Punkt 4 „Bestattung anmelden".
Fix: §-Referenz vor Veröffentlichung gegen aktuelle Bonner FS prüfen und korrekten Paragraphen einsetzen — oder generisch „nach der Bonner Friedhofssatzung" ohne §-Nummer.