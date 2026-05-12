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
Potsdam content review nach SCORE-Tabelle
Magdeburger Friedhöfe recherchieren und dokumentieren
Saarbrücker Friedhöfe recherchieren und dokumentieren
Kieler Friedhöfe und Bestattungskultur recherchieren
Saarbrücken content review nach SCORE-Tabelle
Magdeburg-Review nach SCORE-Tabelle
Potsdamer Friedhöfe und Bestattungsgesetze recherchieren
Kiel v3 Bewertung: Adversarial-Score-Überprüfung
Augsburg v6 Qualitätsprüfung und Adversarial-Scoring
Mainz v3 adversarial review und scoring
Augsburger Friedhöfe und Bestattungsregeln
Wiesbaden v4 adversarial review und scoring
Mainzer Friedhöfe und Bestattungskultur recherchieren
Adversarial review of Kiel briefing materials
Wiesbadener Friedhöfe und Bestattungsgesetze recherchieren
Adversarial review of Mainz content
Augsburg v5 adversarial review und scoring
Kiel-Review nach SCORE-Tabelle
Wiesbaden v3 Compliance-Überprüfung
Mainz content review nach SCORE-Tabelle
Augsburg v4 Bewertung und Adversarial-Score
Adversarial review of Wiesbaden content
Mannheim v4 adversarial quality review
HTML-Seite für Bestatter Mannheim erstellen
Adversarial review v3 Münster content check
Adversarial review of Karlsruhe content
Augsburg-Content Review nach SCORE-Tabelle
Adversarial review of Mannheim content
HTML-Seite für Bestatter in Münster erstellen
Überprüfung von Halluzinationen in Münster-Inhalten
Adversarial review v3 Augsburg
Karlsruhe v4 adversarial review und final score
HTML-Seite für Bestatter in Karlsruhe
Wiesbaden-Review nach SCORE-Tabelle
Karlsruhe v3 adversarial review und final-score
Adversarial review of Augsburg content
Adversarial review v3 Mannheim
Alle Chats
B
Bolle
Max Plan
Potsdam content review nach SCORE-Tabelle
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). Lies Briefing https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md und v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/potsdam/v1-from-chat-A.html

Stadt: Potsdam (Brandenburg). Review streng nach SCORE-Tabelle. Vergib SCORE 0-100% + Fix-Liste.

15:00
Claude hat geantwortet: Ich lese beide Dateien und führe das Review durch.

Ich lese beide Dateien und führe das Review durch.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Web durchsucht

BRIEFING_OK

Ich habe v1 systematisch geprüft. Wortzahl ca. 1.750 (im unteren Zielkorridor). Vier Friedhöfe mit Geschichte, Architektur, Fläche, Hidden Gem — gute Substanz. Drei §-Verweise (§ 17, § 19, § 20, § 32 BbgBestG). Gebührentabelle mit 10 Positionen aus Primärquelle. Trotzdem mehrere konkrete Schwachstellen, vor allem juristische Genauigkeit, Floskeln im Bestatter-Abschnitt und Lücken bei lokalen Besonderheiten.

SCORE: 76%

GAP:

§ 21 BbgBestG wird im FAQ als Beleg für sarglose Erdbestattung zitiert, ist aber laut Briefing-Standard nicht verifiziert. Im Brandenburgischen Bestattungsgesetz regelt § 20 BbgBestG die Bestattungsart (inkl. sargloser Bestattung in ausgewiesenen Feldern). § 21 BbgBestG behandelt typischerweise einen anderen Sachverhalt. Hier droht ein Honesty-Recheck-Blocker — §-Nummer gegen bravors.brandenburg.de verifizieren oder Paragraph durch eine korrekte Norm ersetzen.
§ 20 BbgBestG wird im Fließtext als Norm für die Reihenfolge der bestattungspflichtigen Angehörigen genannt. In der Praxis steht diese Reihenfolge in § 10 BbgBestG (Bestattungspflicht). §-Nummer zwingend gegen Primärquelle verifizieren — falsche Paragraphennummern sind ein klassischer Honesty-Recheck-Blocker.
Sektion "Bestatter in Potsdam wählen" enthält keinen einzigen lokalen Anker. Sätze wie "mehrere Dutzend Bestattungsunternehmen", "alteingesessene Familienbetriebe", "Mitgliedschaft im Bundesverband Deutscher Bestatter" sind 1:1 auf jede andere Stadt übertragbar. Mindestens 2-3 konkrete Potsdamer Bestatter mit Adresse oder Stadtteil-Anker (Babelsberg, Innenstadt, Drewitz) einbauen — oder Sektion auf Bestatter-Bewertungslogik mit Potsdam-Bezug fokussieren (z. B. Hinweis auf BDB-Landesgruppe Brandenburg mit Sitz in Potsdam/Umland).
"Markenzeichen Geprüfter Bestatter" und "Markenzeichen-Bestatter-Siegel" werden ohne Quelle und in unklarer Beziehung zueinander genannt. Entweder Markenzeichen Bestattungen GmbH korrekt benennen + verlinken oder die Passage straffen.
Brandenburger Besonderheit "Bestattungsfrist 10 Tage" wird genannt, aber ein zentrales Brandenburg-Spezifikum fehlt: Brandenburg ist eines der Bundesländer mit der kürzesten Mindestfrist von 48 Stunden vor Bestattung (§ 19 BbgBestG, Frühestbestattung). Das ist für Angehörige praktisch relevant — fehlt komplett.
Kosten-Sektion: Die Aussage "erste Gebührenerhöhung seit 2003" ist eine starke historische Behauptung und steht ohne Inline-Quellenverweis. Tagesspiegel-Artikel 22.09.2023 ist zwar in Quellenliste, aber Fußnoten/Ankerlink im Fließtext fehlt. UNSURE-Kommentar im HTML ist gut, sollte aber auch sichtbar für Nutzer als "geschätzt"-Hinweis kommuniziert werden, nicht nur im HTML-Kommentar.
Konfessionelle Friedhöfe (12 Anlagen, ein Drittel des Gesamtangebots) werden nur in Kernfakten und beim Bornstedter Friedhof gestreift. Es fehlt: Welche Konfessionen? Gibt es jüdische Friedhöfe in Potsdam (Pfingstberg-Friedhof — historisch sehr bedeutsam, 1743 angelegt)? Mindestens ein Absatz oder eine kurze Liste der wichtigsten konfessionellen Anlagen.
Brandenburg-spezifisch fehlt der Jüdische Friedhof am Pfingstberg (angelegt 1743, einer der ältesten erhaltenen jüdischen Friedhöfe Brandenburgs). Für eine Potsdam-Page mit Anspruch auf Vollständigkeit ist das eine bemerkenswerte Lücke. Mindestens Erwähnung mit Adresse und historischem Kontext.
FAQ-Sektion hat 7 Fragen, aber Schema.org-FAQPage im Head hat ebenfalls 7 — Konsistenz prüfen: Die FAQ-Frage "Was kostet ein Urnengrab in Potsdam?" im sichtbaren HTML ist nicht im Schema.org-FAQPage enthalten (dort: "Was kostet eine Bestattung auf einem kommunalen Friedhof in Potsdam?"). Schema.org und sichtbare FAQ müssen sich entsprechen, sonst Google-Rich-Result-Risk.
Cross-Links: Nur ein einziger interner Link zur Bundesland-Page Brandenburg. Es fehlen Links zu Nachbarstädten (Berlin, Brandenburg an der Havel) oder Themen-Pages (Vorsorge, Trauerfeier, Sterbegeldversicherung). Mindestens 3-4 Cross-Links für SEO und Nutzerführung.
Floskel-Risiko in der Ablauf-Sektion: "in den ersten Tagen drei Anlaufstellen relevant" — generisch. Statt drei abstrakten Schritten konkrete Potsdamer Telefonnummern und Wegezeiten zwischen Standesamt, Krankenhäusern und Friedhofsverwaltung anbieten.
Die Behauptung "Kurt von Plettenberg, der einzige Widerstandskämpfer des 20. Juli 1944, der eine ordentliche Beerdigung erhielt" ist eine starke, exklusive Aussage ohne Inline-Quelle. Entweder mit Quelle absichern oder abschwächen ("einer der wenigen…").
Gillis Grafström wird als "vierfacher Olympiasieger" bezeichnet — korrekt sind drei Olympiasiege (1920, 1924, 1928) plus eine Silbermedaille 1932. Faktencheck zwingend, sonst Honesty-Recheck-Blocker.
Wortzahl bei 1.750 — im unteren Korridor. Für Score 85+ wäre Erweiterung auf 2.000-2.200 sinnvoll, vor allem: konfessionelle Friedhöfe inkl. jüdischer Friedhof, lokale Bestatter-Sektion, ergänzende Brandenburg-Spezifika (Frühestbestattung 48h, Feuerbestattung-Voraussetzungen § 22 BbgBestG).
Image-Meta zeigt auf /og/potsdam.jpg — Datei vorhanden? Wenn nicht, OG-Bild bei Social Sharing kaputt.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen
Claude is active in this tab group
Open chat
Dismiss