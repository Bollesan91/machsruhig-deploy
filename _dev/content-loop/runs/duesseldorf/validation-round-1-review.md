Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/duesseldorf/index.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/duesseldorf/index.html

Strict-Check Düsseldorf:

Faktische Spot-Checks:

BestG NRW §13 / §14 Friedhofszwang ✓ (korrekt zitiert)
Nordfriedhof 1884, 70 ha, alter Teil 21 ha, 1987 Denkmalschutz ✓
Südfriedhof 1904, 46,1 ha ✓
Stoffeler 1879, 42 ha, Krematorium ✓
Henkel/Haniel/Poensgen/Zapp/Trinkaus ✓
Karl Arnold OB Düsseldorf? Prüfen — Karl Arnold (CDU, 1901–1958) war NRW-Ministerpräsident und davor Oberbürgermeister von Düsseldorf (1946–1948). ✓
Uwe Faust Grabstein "You'll never walk alone" Liverpool-Hymne ✓
§28 PStG (3. Werktag Anzeige) ✓
Sargmaße 205×75×75 ✓

Strukturwidersprüche & Halluzinationen:

Stoffeler Friedhof: "ältester der drei großen Stadtfriedhöfe" + "fünf Jahre vor dem Nordfriedhof" + Eröffnung 1879 — aber der Golzheimer Friedhof (1804) und der Friedhof Derendorf/Golzheim sind älter. Im Kontext der Aussage ("der drei großen") bleibt das technisch korrekt, aber riskant — akzeptabel.
Schwergewichtsfund — Tabelle-Fußnote / Pipeline-Leakage: Der HTML-Body enthält die Tabelle "Tarif-Position … Stand 01.01.2024" mit explizitem Eingeständnis "jüngste öffentlich vollständig dokumentierte Version". Das ist Selbstwiderspruch zur Keyfact: Page wirbt mit "Gebührentarif Stadtrecht 68.203.1" und FAQ-Schema sagt "seit 01.01.2026 gültige Fassung". Aber im Money-Block stehen 2024er Beträge und die Quellenliste outet die Tabelle als von "Vogt-Kamp Bestattungen — PDF-Aufstellung" gezogen, nicht von der Primärquelle Stadt Düsseldorf. YMYL-Page mit Bestatter-Sekundärquelle für Gebühren = Anwalts-Material.
Article-Schema fehlt image Property (Required für News/Article Rich Results). publisher.logo ebenfalls fehlend — Google Rich Results Test wirft beide als Required-Warning. Bei der Krefeld-Page war das identisch, hier aber mit OG-Image vorhanden = inkonsistent zur eigenen Asset-Lage.

STADT: DUESSELDORF VERDICT: MAJOR-FIX

1. Gebührentabelle führt 2024er-Beträge unter 2026er-Page

Was: Tabelle zeigt "Stand 01.01.2024" mit 1.322,27 € etc., während Keyfact, OG-Description und FAQ-Schema die Fassung 01.01.2026 als verbindlich bewerben. Quelle laut Sources-Liste ist nicht die Stadt, sondern "Vogt-Kamp Bestattungen — PDF-Aufstellung" — Sekundärquelle (Wettbewerber) für YMYL-Gebühren. Reputations- & Glaubwürdigkeitsrisiko, Anwalts-Material.
Wo: <div class="mr-section"> Bestattungskosten → <table> + Source-Liste Eintrag 4.
Fix: 2026er Beträge aus der Primärquelle 68.203.1 (Stand 01.01.2026) ziehen und Tabelle/Header darauf umstellen; Vogt-Kamp-Quelle entfernen; bei nicht-Beschaffbarkeit die Tabelle entfernen und auf den verlinkten verbindlichen Tarif verweisen.

2. Article-Schema ohne image und publisher.logo

Was: JSON-LD @type:"Article" enthält weder image noch publisher.logo.url — beides von Google als Required/Recommended für Article-Rich-Results geführt. Page hat OG-Image vorhanden, könnte denselben Pfad nutzen.
Wo: <script type="application/ld+json"> → Article-Knoten.
Fix: Im Article-Block "image":"https://machsruhig.de/assets/og-duesseldorf.png" und "publisher":{"@type":"Organization","name":"machsruhig.de","logo":{"@type":"ImageObject","url":"https://machsruhig.de/assets/logo.png"}} ergänzen.

3. Adress-Mismatch Friedhofsamt: "Marktplatz 2" ist Rathaus, nicht GFFA

Was: Schema und Body nennen "Garten-, Friedhofs- und Forstamt, Marktplatz 2, 40213 Düsseldorf". Marktplatz 2 ist die Rathaus-Adresse, das GFFA sitzt tatsächlich am Auf'm Hennekamp 45 (Hauptdienststelle). Anwalts-/Kompetenz-Risiko, da Angehörige Adresse direkt nutzen.
Wo: JSON-LD Organization "#friedhofsamt" + Body-Sektion "Bestattungskosten" Klammer "(Marktplatz 2, 40213 …)".
Fix: Adresse durch verifizierte GFFA-Hauptdienststelle ersetzen (laut duesseldorf.de: Auf'm Hennekamp 45, 40225 Düsseldorf, Tel. 0211-8994800) — gegen Stadt-Quelle prüfen, dann beide Stellen synchron updaten.

Nach Fix dieser drei Punkte → CLEAN.