Ich fetche die Datei und reviewe nur MAJOR-Issues.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/duesseldorf/index.html

STADT: Düsseldorf

VERDICT: MAJOR-FIX (2 Funde)

1. Adress-Widerspruch Friedhofsamt (Schema vs HTML)

Wo: JSON-LD Organization #friedhofsamt (Zeile ~95): "streetAddress": "Marktplatz 2" vs HTML Kosten-Section: Friedhofsamt (Marktplatz 2, 40213 Düsseldorf, Tel. 0211-8991)
Problem: Improver v3 sollte laut Brief auf Auf'm Hennekamp 45 umstellen — beide Stellen zeigen aber noch Marktplatz 2. Entweder Improver hat nur an einer Stelle gefixt und du hast die andere übersehen, oder der Fix wurde gar nicht ausgespielt. Marktplatz 2 ist das Rathaus, nicht der Sitz des Garten-, Friedhofs- und Forstamts.
Fix: Beide Stellen auf Auf'm Hennekamp 45, 40225 Düsseldorf ändern (Schema + HTML-Fließtext).

2. Selbstwiderspruch Gebührentabelle

Wo: Kosten-Section, Tabelle + Einleitungssatz
Problem: Brief sagt Improver v3 = Gebührentabelle 2026. Tabelle zeigt aber weiterhin „Stand 01.01.2024" mit Beträgen 1.322,27 € / 1.185,35 € / 893,07 € / 492,47 €. Der Fließtext sagt explizit „seit 01.01.2026 in Kraft … die folgende Tabelle gibt … die Fassung vom 01.01.2024 wieder". Das ist ein offener Selbstwiderspruch — Leser sieht 2026-Inkrafttreten, aber 2024-Zahlen, mit Hedge-Satz dazwischen. Entweder Tabelle ist real auf 2026 und Überschrift/Hedge wurden vergessen, oder Update wurde nicht eingespielt.
Fix: Klären, welche Variante stimmt — entweder echte 2026-Werte + Überschrift „Stand 01.01.2026" + Hedge-Satz löschen, oder Tabelle als „historische 2024-Referenz" deutlich auszeichnen und nicht mehr als verbindlich anbieten.

HSBC Trinkaus + FAQ-Schema/HTML-Parity + §-Nummern (§13/§14/§8 BestG NRW, §28 PStG, §1/§8/§9 Satzung) + Cross-Links (/bestattung-in/nordrhein-westfalen/, /bestattungskosten, /beerdigung-planen, /tools/checkliste-todesfall, /methodik, /bestatter/): clean.