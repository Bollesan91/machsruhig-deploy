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
Oldenburg-Review nach SCORE-Tabelle
Friedhöfe und Gebührensatzung in Kassel
Friedhöfe und Gebührensatzung in Oldenburg
Friedhöfe und Bestattungen in Rostock
Friedhöfe in Lübeck: Bestattungen und Gebühren
Friedhöfe und Gebührensatzung in Kassel
Friedhöfe und Gebührensatzung in Erfurt
Saarbrücker Friedhöfe recherchieren und dokumentieren
Lübecks Friedhöfe und Bestattungsregeln
Freiburg content review nach SCORE-Tabelle
Erfurt Schwächen-Analyse mit Adversarial Review
Chat C v4 Saarbrücken Bewertung
Magdeburg v4 performance evaluation
Friedhöfe und Bestattungsgebühren in Freiburg
Magdeburger Friedhöfe recherchieren und dokumentieren
Erfurt content review nach SCORE-Tabelle
Saarbrücken v3 Adversarial Score Überprüfung
Potsdam v3 adversarial score evaluation
Magdeburg v3 adversarial score überprüfung
Potsdamer Friedhöfe und Bestattungsgesetze recherchieren
Magdeburg v3 adversarial score überprüfung
Saarbrücken adversarial review und schwächen analyse
Potsdam adversarial review und schwächen analyse
Friedhöfe und Gebührensatzung in Erfurt
Adversarial review of Magdeburg content
Kiel v4 adversarial score evaluation
Kieler Friedhöfe und Bestattungskultur recherchieren
Potsdam content review nach SCORE-Tabelle
Saarbrücken content review nach SCORE-Tabelle
Kiel v3 Bewertung: Adversarial-Score-Überprüfung
Magdeburg-Review nach SCORE-Tabelle
Alle Chats
B
Bolle
Max Plan
Oldenburg-Review nach SCORE-Tabelle
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). Lies Briefing https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md und v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/oldenburg/v1-from-chat-A.html

Stadt: Oldenburg (Niedersachsen). Review nach SCORE-Tabelle. SCORE 0-100% + Fix-Liste.

17:57
Claude hat geantwortet: Ich lese beide Dateien.

Ich lese beide Dateien.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Web durchsucht

BRIEFING_OK

SCORE: 78%

GAP:

HTML-Fehler im St. Gertruden-Kirchhof Block: Das <div class="hidden-gem"> wird mit </p> statt </div> geschlossen (Zeile mit „aus einem Ableger des ursprünglichen Baumes erwachsen.</p></div>"). Bricht die DOM-Struktur, alle nachfolgenden Elemente liegen ungewollt im Hidden-Gem-Container.
Schema.org-Inkonsistenz beim St. Gertruden-Kirchhof: JSON-LD nennt „Gertrudenkapelle und herzogliches Mausoleum" und Adresse „Kirchhofstraße, 26121", Fließtext spricht aber von „nördlich des Pferdemarkts" und gibt im Meta-Block „zwischen Alexanderstraße und Nadorster Straße" als Lage an. Beide Lageangaben sind nicht deckungsgleich – eine Adresse muss verbindlich gewählt und in Meta-Block, JSON-LD und Fließtext identisch sein.
Lage-Widerspruch unaufgelöst: Die Behauptung „nördlich des Pferdemarkts" + „zwischen Alexanderstraße und Nadorster Straße" als ein Friedhof passt geografisch nicht zusammen (Pferdemarkt liegt südlich, Alexanderstraße/Nadorster bilden ein Gebiet weiter nördlich). Muss faktisch geprüft und korrigiert werden – Verdacht auf Verwechslung mit dem Gertrudenfriedhof an der Alexanderstraße (das ist ein anderer/erweiterter Standort).
Fläche städtische Friedhöfe widerspricht sich: Keyfacts nennen „insgesamt rund 26 Hektar", Parkfriedhof Bümmerstede wird mit 16 ha angegeben, Waldfriedhof Ofenerdiek mit 10 ha – das sind 26 ha. Plausibel, aber Quelle 11 (NWZ) wird als Beleg für „16 ha" beim Waldfriedhof zitiert, nicht beim Parkfriedhof. Quellenzuordnung im Quellenblock prüfen und Fläche pro Friedhof mit jeweils eigener Quelle hinterlegen.
Waldfriedhof Ofenerdiek: „Mary Kehl, regional bekannte Persönlichkeit, deren Grab heute zu den meistbesuchten der Anlage zählt" – unbelegte Superlativ-Aussage („meistbesuchten") ohne Quelle. Mary Kehl ist nicht über etablierte Quellen als prominent verifizierbar. UNSURE-Kommentar zeigt eigene Unsicherheit des Autors – Eintrag sollte entweder mit harter Quelle belegt oder gestrichen werden.
St. Gertruden-Kirchhof: „2.176 belegte Gräber" – sehr spezifische Zahl ohne Quellenverweis. Stand-Jahr fehlt. Muss entweder mit Primärquelle (Kirchengemeinde / Stadtmuseum) belegt oder als ca.-Angabe gerundet werden.
Hidden-Gem Bümmerstede zur Hochwasserlage 5. Januar 2024: spezifisches Datum, Behauptung „einer von wenigen deutschen Friedhöfen, die durch mobile Deichsysteme aktiv vor einer Flut geschützt werden mussten" – Superlativ („einer von wenigen") ohne Beleg. Quelle (NWZ-Bericht oder Stadt Oldenburg) muss in Sources-Block aufgenommen werden, sonst Aussage entschärfen.
Bestattungspflicht-Reihenfolge falsch zitiert: § 8 Abs. 3 BestattG Niedersachsen listet die Reihenfolge anders (nach Eheangaben sind Kinder, dann Eltern, dann Geschwister, dann Großeltern, dann Enkelkinder folgt einer anderen Logik). Die Aufzählung „Ehegatte … Kinder, Enkelkinder, Eltern, Großeltern, Geschwister" muss anhand des aktuellen Gesetzestexts verifiziert werden. Im Zweifel direkt aus § 8 Abs. 3 Nds. BestattG zitieren.
Anzeigefrist beim Standesamt widersprüchlich: Fließtext sagt „spätestens am dritten Werktag nach dem Todestag", FAQ-Antwort und FAQ-JSON-LD sagen „innerhalb des nächsten Werktags". § 28 PStG kennt 3. Werktag – die FAQ-Aussage „nächster Werktag" ist falsch. Dringend angleichen.
Schema.org Place-Adresse St. Gertruden-Kirchhof gibt PLZ „26121", Fließtext im Meta-Block gibt keine PLZ aber andere Straße. Schema-Adresse („Kirchhofstraße, 26121") und Fließtext-Adresse müssen identisch sein.
Bestatter-Wahl-Sektion enthält sachlichen Fehler: „Der Bundesverband privater Versicherer (kein Bestatter-Verband, sondern Pflichtversicherer)" – verwirrend und sachlich schief; gemeint ist vermutlich der Bundesverband Bestattungsbedarf oder eine Bestatter-Innung. Aussage entweder konkretisieren oder streichen.
Niedersächsisches Bestattungsgesetz: Korrekte Kurzbezeichnung ist BestattG, nicht „BestattG" als universelle Abkürzung – Schreibweise wird im Text verwendet, aber das Gesetz wird in Niedersachsen als „BestattG" oder „NBestattG" zitiert. Eine konsistente Schreibweise wählen (in BW etabliert ist „BestattG"; Bremen/Niedersachsen-Pages verwenden meist „BestattG"). Konsistenz mit den anderen Bundesland-Pages prüfen.
Frachtdichte Kostentabelle ist gut, aber: Verlängerungsgebühren für die Nutzungszeit fehlen in der Tabelle (im Fließtext werden „38 € Urne / 43 € Erd" genannt). In Tabelle aufnehmen oder als separate Mini-Tabelle, damit Vergleichbarkeit mit anderen Pages gegeben ist.
Cross-Links zu Nachbarstädten fehlen: Nur Bundesland-Niedersachsen-Page wird verlinkt. Cross-Links zu Bremen (Nachbarstadt, kurze Distanz), Wilhelmshaven oder Osnabrück würden Audit-Score heben und sind in anderen Bundesland-Pages Standard.
Wortzahl: liegt geschätzt bei ~1.700–1.800 Wörtern – im unteren Korridor des Ziels 2000–2500. Tiefe in der Friedhofs-Sektion (besonders Willehad – nur 1 Absatz) und in der Bestatter-Wahl-Sektion ausbaufähig.
Floskel-Treffer im Hero-Block: „spart Zeit, Geld und unnötige Telefonate" – Marketing-Floskel, unpräzise. Stattdessen konkreter Nutzen: was genau wird durch Strukturkenntnis gespart?
Floskel-Treffer in der Friedhofs-Einleitung: „Oldenburg hat in seinen Friedhöfen mehr Geschichte versammelt als viele größere Städte" – unbelegter Vergleichs-Superlativ. Streichen oder konkret machen.
FAQ-Antwort „Gibt es ein Krematorium": Im JSON-LD steht nur „286 € zzgl. Umsatzsteuer", in der HTML-FAQ steht zusätzlich „Auch Verstorbene, die nicht in Oldenburg beigesetzt werden, können hier kremiert werden." – beide Antworten müssen wortgleich sein, sonst Inkonsistenz zwischen sichtbarer Antwort und Rich-Snippet.
Quellenblock: Quelle 3 („Niedersächsisches Gesetz … – Landtag Niedersachsen") ohne URL. Direkter Deeplink ins niedersächsische Vorschrifteninformationssystem (voris.niedersachsen.de) muss ergänzt werden – sonst nicht überprüfbar.
Quelle 12 („Bürgerverein Ofenerdiek, Stadtteilhistorie") ohne URL und ohne konkrete Publikation. So nicht zitierfähig. Entweder konkretisieren (Titel, Datum, Link) oder streichen und die darauf beruhende Hidden-Gem-Aussage zur Munitionsfabrik anderweitig belegen.
Lokaler Anker: Bestattungstraditionen / regionale Besonderheiten Oldenburgs (z.B. plattdeutsche Trauerkultur, Friesische Einflüsse im Nordwesten, niedersächsische Trauerredner-Tradition) fehlen komplett. Andere Pages haben einen Abschnitt zu regionalen Besonderheiten – hier wäre Platz für 1–2 Absätze.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen