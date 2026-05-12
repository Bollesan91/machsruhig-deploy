Neuer Chat
Suchen
Chats
Projekte
Code
Anpassen
Design
Mehr
Zuletzt verwendet
Ausblenden
Mönchengladbach-Review nach SCORE-Tabelle
Regensburg Friedhöfe und Bestattungsgesetz
Friedhöfe und Bestattungen in Mönchengladbach
Heidelberg Friedhöfe und Bestattungsgesetze
Chat C v3 Kassel Bewertung prüfen
Regensburg Friedhöfe und Bestattungsgesetz
Regensburg Friedhöfe und Bestattungsgesetz
Friedhöfe und Gebührensatzung in Kassel
Chat C v3 Rostock performance evaluation
Friedhöfe und Bestattungen in Rostock
Oldenburg v3 adversarial score evaluation
Lübeck v3 adversarial score evaluation
Friedhöfe und Gebührensatzung in Oldenburg
Friedhöfe in Lübeck: Bestattungen und Gebühren
Kassel adversarial review und schwächen analyse
Rostock: Schwächen und adversariales Scoring
Oldenburg: Schwächen und adversariale Bewertung
Lübeck adversarial review und schwächen analyse
Rostock: Schwächen und adversariales Scoring
Kassel-Review nach SCORE-Tabelle
Kassel-Review nach SCORE-Tabelle
Oldenburg-Review nach SCORE-Tabelle
Lübeck-Review nach SCORE-Tabelle
Rostock-Review nach SCORE-Tabelle
Friedhöfe und Gebührensatzung in Kassel
Magdeburg v4 performance evaluation
Friedhöfe und Bestattungsgebühren in Freiburg
Magdeburger Friedhöfe recherchieren und dokumentieren
Erfurt content review nach SCORE-Tabelle
Saarbrücken v3 Adversarial Score Überprüfung
Friedhöfe und Gebührensatzung in Erfurt
Saarbrücker Friedhöfe recherchieren und dokumentieren
Lübecks Friedhöfe und Bestattungsregeln
Freiburg content review nach SCORE-Tabelle
Chat C v4 Saarbrücken Bewertung
Erfurt Schwächen-Analyse mit Adversarial Review
Alle Chats
B
Bolle
Max Plan
Mönchengladbach-Review nach SCORE-Tabelle
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). Lies Briefing https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md und v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/moenchengladbach/v1-from-chat-A.html

Stadt: Moenchengladbach (NRW). Review nach SCORE-Tabelle. SCORE 0-100% + Fix-Liste.

18:58
Claude hat geantwortet: Ich lese zuerst Briefing und v1.

Ich lese zuerst Briefing und v1.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md

Briefing gelesen. Jetzt v1.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/moenchengladbach/v1-from-chat-A.html

BRIEFING_OK

Wortzahl-Check und Detailprüfung:

~2.150 Wörter Fließtext (geschätzt im Korridor)
4 Friedhöfe ausführlich, 9 weitere kurz erwähnt
4 Hidden Gems
§-Verweise präsent (§ 13 Abs. 2/3 BestG NRW, § 14, § 6, § 10, § 27 Friedhofssatzung)
Quellen-Liste mit 8 Einträgen
FAQ Schema.org vorhanden, 7 Fragen
1 zitierter "rund 702 €" Preis (BdSt NRW 2022), Tabelle mit 4 Tarifzeilen
CSS-Bug: --mr-accent-soft:#e8efe c; (Leerzeichen im Hex-Code)

SCORE: 76%

GAP:

CSS-Syntaxfehler in :root: --mr-accent-soft:#e8efe c; enthält ein Leerzeichen im Hex-Wert und ist damit ungültig — die Variable fällt zurück auf "unset", wodurch Keyfacts-Box, Tabellen-Header und FAQ-Akzentfarbe ihre Hintergrundfarbe verlieren. Muss zu 
#e8efec (oder gewünschtem Wert) korrigiert werden.
Statistik-Zahl ohne klare Stand-Angabe in Tabelle: Die Gebühren-Tabelle (1.620 €, 1.700 €, 2.175 €) trägt keinen Stand-Hinweis direkt am Tisch — nur "Erster Nachtrag 2018" im Vorlauftext. Bei einer Quelle aus 2018 in einer 2026-Seite muss der Stand prominent in Caption oder Zeile stehen ("Stand: 2018, Erster Nachtrag"), sonst wirkt der Tarif aktueller als er ist.
702-€-Quelle wird zweimal genannt, aber nie verlinkt: "Bund der Steuerzahler NRW, Friedhofsgebührenvergleich 2022" erscheint im Fließtext und im FAQ, aber Quelle 6 verlinkt nur generisch auf steuerzahler.de — nicht auf die konkrete Studie/PDF. Direktlink zur 2022er Studie fehlt.
Geo-Fehler "viertgrößte Stadt NRW": Im Bestatter-Abschnitt steht "Mönchengladbach ist mit über 260.000 Einwohnern die viertgrößte Stadt Nordrhein-Westfalens". Tatsächlich ist Mönchengladbach in NRW etwa Platz 7–8 (nach Köln, Düsseldorf, Dortmund, Essen, Duisburg, Bochum, Wuppertal). Faktencheck nötig — entweder auf "siebt-/achtgrößte" korrigieren oder Aussage rausnehmen.
Friedhof Giesenkirchen ohne Hidden Gem-Story zum Ort selbst: Die Giesenkirchen-Hidden-Gem dreht sich um die allgemeine Reststreifen-Regelung des § 10 Abs. 2 — das ist eine satzungsweite Eigenheit, kein Giesenkirchen-Spezifikum. Echter lokaler Anker (Geschichte, Architektur, Besonderheit des Friedhofs Giesenkirchen) fehlt — z. B. Eröffnungsjahr, Trauerhalle, charakteristische Anlage.
"Bekannte Bestattete" beim Friedhof Rheydt leer: Formulierung "Bekannte Bestattete sind unter anderem ehemalige Borussen-Spieler … aufgrund der Persönlichkeitsrechte werden Einzelnamen nicht öffentlich publiziert" ist eine Floskel-Ausflucht. Entweder konkrete, öffentlich dokumentierte Person nennen (z. B. ggf. ehemalige Vereinsfunktionäre, deren Grab öffentlich begangen wird) oder Satz streichen. Bei Hauptfriedhof funktioniert das ja (Franz Meyers, Hermann Piecq, Joseph Kämpf).
Cross-Links zu Nachbarstädten/anderen MG-Themen fehlen: Es gibt nur einen Link zur Bundesland-Page NRW. Cross-Links zu vergleichbaren NRW-Städten (z. B. Krefeld, Düsseldorf, Köln — falls existent) oder zum Ratgeber-Bereich (Bestattungsvorsorge, Trauerhilfe) fehlen. Der Bestatter-Abschnitt verspricht "Ratgeber-Bereich von machsruhig", verlinkt aber nicht.
§ 6 Friedhofssatzung wird zitiert (Wahlgrab/Vorsorge), § 10 Abs. 1 und Abs. 2, § 27 Abs. 5, § 14 BestG NRW — aber § 13 wird nur als Abs. 2/3 zitiert, Abs. 1 (Todesbescheinigung) wird im "Was tun"-Abschnitt erwähnt, aber nicht eindeutig als Rechtsgrundlage referenziert. Konsistente Vollzitate (§ Absatz BestG NRW / Friedhofssatzung) durchgehend nötig — besonders bei der Sargpflicht: keine Sargpflicht-Aussage mit § zu finden, obwohl in NRW relevant.
Keine Bestatterzahl/Marktdaten: Aussage "Preisspreizung zwischen Mönchengladbacher Bestattern liegt erfahrungsgemäß bei 1.000 bis 2.000 Euro" ist unbelegt ("erfahrungsgemäß"). Entweder mit Stiftung-Warentest- oder Verbraucherzentrale-Quelle absichern oder als "branchenüblich" mit Verweis auf Bundesverband Deutscher Bestatter formulieren.
Krematorium-Standort fehlt: Mönchengladbach hat selbst kein Krematorium — Einäscherungen erfolgen i. d. R. in Krefeld oder Düsseldorf. Diese praktisch wichtige Info (welches Krematorium fährt der Bestatter an, Auswirkung auf Frist und Kosten) wird nicht genannt, obwohl Krematoriumsgebühr mehrfach erwähnt wird.
Telefonnummer mags 02161 256892: Nummer steht ohne Quellenverweis. Falls aus mags.de übernommen → in Quelle 4 implizit, aber Telefonnummern verändern sich — Stand/Datum am Telefon-Eintrag wünschenswert oder explizit aus mags.de/kontakt verlinken.
OG-Image fehlt: Open-Graph-Tags vorhanden, aber og:image fehlt — beim Teilen in WhatsApp/Facebook/LinkedIn erscheint kein Vorschaubild. Für eine Bundesstadt-Page mit Hidden-Gem-Storys (Borussia-Kolumbarium!) Pflicht.
mr-hero h2-Hierarchie: Erste h2 ist "Kernfakten auf einen Blick" in einem <aside>, nicht im Hauptcontent. Davor steht direkt unter h1 nur ein lead-paragraph ohne thematische Zwischenüberschrift. Logischer wäre, "Bestattungsrecht in Mönchengladbach" als erste inhaltliche h2 zu positionieren und Keyfacts als aside ohne h2 (oder mit h3) zu klassifizieren — sonst läuft der Screen-Reader-Outline durcheinander.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen
Claude is active in this tab group
Open chat
Dismiss