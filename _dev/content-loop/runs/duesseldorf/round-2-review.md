Claude hat geantwortet: Ich hole mir Briefing und Page.

Ich hole mir Briefing und Page.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Web durchsucht

BRIEFING_OK

SCORE: 68%

GAP:

Friedhofs-Highlights ohne konkrete prominente Gräber. Nordfriedhof-Sektion sagt zwar "Düsseldorfer Oberbürgermeister, Industrielle, Künstler und Wissenschaftler" — nennt aber keinen einzigen Namen. Der Nordfriedhof beherbergt u.a. Wilhelm Marx, Robert Lehr, Heinrich Heine-Verwandte, Friedrich Spielhagen, Robert Pferdmenges, Wim Wenders' Familie etc. Mindestens 3–5 konkrete Namen sind Standard auf vergleichbaren Bundesland-/Stadt-Pages. Das <!-- UNSURE -->-Pattern ist Recherche-Auslagerung an den Reviewer, kein Ergebnis.
§-Verweise zum BestG NRW fehlen komplett. Aussagen zu Leichenschau, Bestattungsfrist, Sargpflicht, Friedhofszwang stehen ohne Paragraphen. Konkret: § 9 BestG NRW (Bestattungsfrist), § 13 BestG NRW (Sargpflicht/Ausnahme), § 17 BestG NRW (Friedhofszwang). Briefing fordert explizit "§-Verweise". Einziger zitierter Paragraph ist § 28 PStG — also Bundesrecht, nicht NRW.
Bestattungskosten ohne konkrete Friedhofsgebührensätze. Die Düsseldorfer Friedhofsgebührensatzung ist öffentlich (Reihengrab Erd ca. X €, Urnenwahlgrab Y €, Verwaltungsgebühr Z €). Die Page nennt nur Gesamtkorridor 7.000–9.000 € und verweist auf "Ortsrecht". Das ist die Auslagerung der Substanz, die hier gefragt ist. Die UNSURE-Notiz bestätigt das selbst.
Ruhezeit Düsseldorf nicht beziffert. "20 bis 30 Jahre typischerweise in NRW" ist generisch. Düsseldorf hat konkrete Ruhezeiten pro Grabart (Reihengrab Erd: meist 25 Jahre, Urnengrab: meist 20 Jahre — je Satzung). Ohne diese Zahl fehlt der entscheidende lokale Datenpunkt.
Südfriedhof + Stoffeler Friedhof bleiben generisch. Beide ohne Eröffnungsjahr (Südfriedhof 1904, Stoffeler 1897 stehen im Schema.org-Block der Page — kommen aber im Body nicht vor!). Beide ohne Fläche in ha. Beide ohne prominenten Bestatteten. Beide ohne historische/architektonische Besonderheit, die über "Landschaftsfriedhof mit altem Baumbestand" hinausgeht.
Schema.org-Body-Inkonsistenz. Im JSON-LD steht "Südfriedhof eröffnet 1904" und "Stoffeler eröffnet 1897" — im sichtbaren Text der Page wird genau bei diesen Daten gesagt, sie seien "laut Auftrag nicht beziffert". Das ist ein direkter Widerspruch innerhalb derselben Datei.
Quellen-Liste hat 10 Einträge, aber 0 davon ist die Düsseldorfer Friedhofsgebührensatzung direkt verlinkt. Es wird auf /ortsrecht verwiesen — das ist das Inhaltsverzeichnis. Direktlink zum PDF/Satzungstext fehlt.
Stiftung-Warentest-Zitat ohne Stand-Jahr und ohne Direktlink. "Stiftung Warentest nennt Korridor 7.000–8.000 €" — welche Untersuchung, welches Jahr? Link geht nur auf test.de-Homepage, nicht zur Quelle.
Wortzahl im Body ca. 1.500 Wörter. Unteres Limit des Briefings, deutlich unter Ziel-Korridor 2.000–2.500. Die fertigen Bundesland-Pages liegen bei 1.700–2.400. Für eine Stadt-Page in dieser Größenordnung (Landeshauptstadt, 3 Friedhöfe) wäre 2.000+ angemessen — der fehlende Substanz-Stoff (Namen, Paragraphen, konkrete Gebühren) würde das automatisch füllen.
Krematorium Nordfriedhof nur einsatzig erwähnt. Inbetriebnahmejahr, Lage, Bedeutung für die Region — fehlt komplett. Das UNSURE-Kommentar legt offen, dass nicht recherchiert wurde.
Kriegsgräberfelder ohne Zahlen. Nordfriedhof + Stoffeler werden beide als Kriegsgräberstätte genannt — aber ohne Anzahl Gräber, ohne Schlachten/Hintergrund, ohne Volksbund-Direktlink zur jeweiligen Stätte. Verlinkt ist die Volksbund-Hauptseite.
Cross-Links zu NRW-Städten sind tote Links auf der eigenen Domain. /bestatter/koeln/, /bestatter/essen/, /bestatter/dortmund/ — falls diese Pages noch nicht existieren, ist das ein Re-Check-Blocker. (Anmerkung an Pilot/Owner: gegen-prüfen.)
Floskel "letzte Ruhe / individuelle Wünsche" vermieden — aber: "wichtigster Erinnerungsort", "großzügige Wegeführungen", "prägen das Bild" sind generische Friedhofs-Topoi ohne lokalen Anker. Funktioniert auch für Hamburg-Ohlsdorf oder Berlin-Stahnsdorf, also kein Düsseldorf-Spezifikum.
Author-Modell uneinheitlich. Im Body: "Redaktion machsruhig.de". Im Schema.org Article: "author":{"@type":"Organization","name":"machsruhig.de"} — der Fachpool-Reviewer aus dem locked-decision-Setup ("machsruhig Redaktion + Fachpool-Reviewer") taucht weder im Body noch im JSON-LD auf.




