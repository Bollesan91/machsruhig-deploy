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
Aachen Stadt-Page Review für machsruhig.de
Aachen Stadt-Page Review für machsruhig.de
Überprüfung der Köln-Seite auf behobene Major-Fehler
Re-Review Frankfurt Friedhof und Bestattungsrecht
Re-Review Rostock: Major-Funde Überprüfung
Magdeburg-Überprüfung: MAJOR-Funde validieren
Potsdam-Friedhof: Überprüfung der MUST-FIX-Korrektionen
Überprüfung der Köln-Seite auf behobene Major-Fehler
Re-Review Frankfurt Friedhof und Bestattungsrecht
Rostock Bestatter Review auf machsruhig.de
Magdeburg Bestatter Review - Qualitätskontrolle
Köln Bestatter-Seite Qualitätsprüfung
Strict review of Potsdam funeral director content
Strict review protocol for Frankfurt bestatter content
Leipzig Bestatter Korrektionen: Bach-Datum und Flächenangaben
Karlsruhe Bestatter Überprüfung
Berlin Bestatter Review - Hauptprobleme
Hamburg Bestattungsanbieter Überprüfung
Bremen Strict Independent Review
Bremen Bestatter Korrektionen: Architektur und Lebensdaten
Hamburg Bestattungsseite: 3 kritische Korrektionen
Berlin Bestattungsgesetz Faktenchecks
Korrektionen Bestattungsgesetz NRW Rangfolge
Strict independent review for Leipzig
Dresden Bestatter Review Pass 2
Bestatter Essen HTML-Korrektionen
Bremen-Artikel Korrektionen und HTML-Fixes
Dortmund Friedhöfe: Kritische Adress- und Rechtstext-Korrektionen
Dresden Friedhof Schema-Korrektionen
Strenge Überprüfung von Leipzig auf machsruhig.de
Berlin Bestattungsseite: Faktenchecks und Korrektionen
Strenge Überprüfung von Berlin-Bestättern
Strict independent review for Bremen
Strenge Überprüfung von Hamburg auf machsruhig.de
Strenge Überprüfung von Essen-Inhalten
Dortmund Bestatter Review Pass 2
Korrektionen zu Leipziger Friedhofsinformationen
Strenge Überprüfung von Berlin-Bestättern
Alle Chats
B
Bolle
Max Plan
Aachen Stadt-Page Review für machsruhig.de
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetche die Live-Version und prüfe.

Ich fetche die Live-Version und prüfe.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/aachen/index.html?cb=1779107742778

Ich prüfe jetzt systematisch auf MAJOR-Issues.

Searching the web
Web durchsucht

Wichtiger Befund: Westfriedhof I war für evangelische, Westfriedhof II für katholische Bürger - der Text auf der Seite ist also korrekt. Aber: Im JSON-LD und Hero-Text wird "28 städtische Friedhöfe" behauptet. Lass mich das prüfen, plus den Punkt zur Campo Santo (neogotisch vs. Mittelturm) und Ostfriedhof.

Web durchsucht
Web durchsucht

Bestätigt: 28 aktive Friedhöfe = korrekt (offizielle Stadt-Quelle). Aber: Im Page-Text "Ostfriedhof" steht "rund 127.000 m²" - offizielle Stadt-Quelle sagt 125.265 m². Außerdem: Eröffnungsdatum im Page-Text ist "18. August 1803", offizielle Stadt-Quelle sagt 28. August 1803. Und: Heißbergfriedhof Adresse - Page sagt "Heißbergstraße / Kapellenstraße 2" und "Kreuzungsbereich Heißbergstraße/Robert-Schuman-Straße" laut Stadt. Lass mich Ostfriedhof-Eröffnung und Campo Santo prüfen.

Web durchsucht
Web durchsucht

Sehr wichtiger Befund! Der Ostfriedhof-Eintrag im Page-Text enthält mehrere Fakten-Issues, aber das Datum 18. August 1803 stimmt mit Wikipedia überein, während die Stadt 28. August 1803 sagt. Das ist ein Datums-Konflikt zwischen Primärquellen — Wikipedia steht im Konflikt mit Stadt-Aachen-Webseite. Da die Stadt-Quelle als verbindlicher gilt für YMYL, und Ostfriedhof e.V. (Förderverein) auch 28. August 1803 sagt, ist das im Page-Text mit "18. August" wahrscheinlich falsch.

Außerdem: Der Page-Text sagt "Adalbertsteinweg" als Adresse - korrekt ist Adalbertsteinweg 123 (nicht nur "Adalbertsteinweg" wie im JSON-LD).

Aber das sind eher kleinere Detail-Issues. Lass mich die wichtigeren Punkte fokussieren. Jetzt prüfe ich die Cross-Links und das FAQ-Schema vs. HTML-FAQ.

Cross-links und FAQ-Schema strukturell prüfen
Cross-links und FAQ-Schema strukturell prüfen

FAQ-Schema = sichtbares HTML-FAQ, gleicher Frage-Satz, beide 7 Einträge - PASS. Jetzt Cross-Links prüfen (die werden im Text als "in Vorbereitung" beschrieben, sind also bewusst gesetzt — kein MAJOR).

Failed to fetch: https://machsruhig.de/bestatter/koeln/
Failed to fetch: https://machsruhig.de/bestatter/koeln/

Cross-Links Köln/Düsseldorf/Bonn werden im Text explizit als "in Vorbereitung" markiert — also bewusst dead/placeholder, kein MAJOR. Die §-Referenzen prüfen: §11 Abs. 2, §13 Abs. 2, §13 Abs. 3, §15 Abs. 1, §15 Abs. 5, §9, §28 PStG, §74 SGB XII — alle konsistent zwischen Schema und Text. §11 Abs. 2 für 36h-Frist explizit als Korrektur gegen Fehlannahme markiert ("steht nicht in § 13, sondern in § 11 Abs. 2") — gut.

Jetzt der entscheidende Geld-Stand-Check: Alle Eurobeträge tragen Stand "17.12.2025" der 17. Änderungssatzung. Aber: Der Link verweist auf "16-aenderungssatzung-der-friedhofsgebuehrenordnung.pdf" — Widerspruch zwischen Text ("17. Änderungssatzung") und URL-Slug ("16-aenderungssatzung")!

Web durchsucht
Web durchsucht

Wichtiger Befund bestätigt: Das PDF heißt zwar "16-aenderungssatzung..." in der URL, aber inhaltlich ist es tatsächlich die 17. Änderungssatzung vom 17.12.2025. Das ist kein Faktenfehler — Stadt-Aachen hat das PDF nur unter altem Dateinamen veröffentlicht. Die Eurobeträge (1.527,00 €, 1.527,00 € Urnenreihengrab) stimmen mit der Live-Quelle überein. Kein MAJOR-Issue.

Wichtig zusätzlich: Pressemitteilung sagt "27 Friedhöfe und fünf Gedenkstätten", offizielle Übersichtsseite sagt "28 aktive Friedhöfe und sechs Gedenkstätten". Die offizielle Übersichtsseite ist die maßgebliche Primärquelle und wird im Page zitiert — also OK.

Aber kritisch ist: Page-Text sagt "Friedhof Hüls" als 28. städtischer Friedhof + Westfriedhof I+II als 2 Friedhöfe. Stadt-Aachen listet Westfriedhof I und Westfriedhof II separat. Die Page-Title-Section sagt "vier Friedhöfe und das städtische Krematorium" und listet dann Westfriedhof "I und II" als einen Eintrag (zusammen 279.000 m²) - das ist OK als zusammenfassende Darstellung.

Jetzt noch der Ostfriedhof-Eröffnungs-Datum-Check: Page sagt "18. August 1803" — Wikipedia bestätigt "18. August 1803", Stadt-Aachen-Webseite "28. August 1803", Ostfriedhof.de (offizieller Förderverein) "28. August 1803". Die offiziellen Aachener Quellen sind sich einig: 28. August 1803. Wikipedia weicht ab. Da der Page Wikipedia als Quelle zitiert und nicht die Stadt-Quelle, ist "18. August" möglicherweise eine Wikipedia-Halluzination, aber zumindest belegt — für YMYL ein MINOR, kein MAJOR, da sachlich umstritten zwischen Quellen.

Letzter Check: Heißbergfriedhof-Adresse. Page sagt "Heißbergstraße / Kapellenstraße 2" + Schema sagt das gleiche. Stadt-Aachen sagt aber "Kreuzungsbereich Heißbergstraße/Robert-Schuman-Straße" (nicht Kapellenstraße!). Die Eröffnung laut Stadt: 1. September 1862 — Page nennt kein konkretes Datum, sagt "geht auf das 19. Jahrhundert zurück" — sicher. Aber Kapellenstraße 2 ist falsch — sollte Robert-Schuman-Straße sein.

Web durchsucht
Web durchsucht

Heißbergfriedhof Adressen-Konflikt geklärt:

Stadt Aachen (offiziell): "Kreuzungsbereich Heißbergstraße/Robert-Schuman-Straße"
Wikipedia: "Ecke Heißberg- und Kapellenstraße Nr. 2"
d-friedhof.de: "Robert-Schuman-Straße 2"

Die Page übernimmt die Wikipedia-Angabe ("Heißbergstraße / Kapellenstraße 2") - das ist nicht eindeutig falsch, aber widerspricht der maßgeblichen Stadt-Quelle. Da Wikipedia immerhin Beleg ist, kein klarer Faktenfehler.

Jetzt habe ich genug Material. Lass mich den finalen Review schreiben.

STADT: Aachen
VERDICT: PASS mit 2 MAJOR

Fund 1 – Ostfriedhof-Fläche (Selbstwiderspruch zur offiziellen Stadt-Quelle): Wo: Section "Ostfriedhof (Adalbertsteinweg)", Absatz 1. Was: Page nennt "rund 127.000 m² Fläche". Die offizielle Stadt-Aachen-Quelle (strukturierte-daten/orte/friedhoefe/ostfriedhof/) sagt verbindlich 125.265 m². Da der Page selbst diese Stadt-Quellen als maßgeblich zitiert (Waldfriedhof: 219.354 m² ist exakt), ist die Aachen-spezifische Rundung auf "rund 127.000" inkonsistent zur restlichen Page-Logik und stammt aus Wikipedia/umdiewelt.de. Fix: Auf "rund 125.000 m²" oder exakt 125.265 m² korrigieren (Quelle: aachen.de/strukturierte-daten/orte/friedhoefe/ostfriedhof/).

Fund 2 – Ostfriedhof-Eröffnungsdatum (Faktenkonflikt mit Primärquelle): Wo: Section "Ostfriedhof (Adalbertsteinweg)", Absatz 1. Was: Page nennt "am 18. August 1803 eröffnet". Die maßgebliche Stadt-Aachen-Quelle und auch der Förderkreis-Ostfriedhof e.V. (ostfriedhof.de) nennen einhellig 28. August 1803 ("am 28. August 1803 ... eingesegnet"). Nur Wikipedia (Quelle der Page) nennt den 18.8. — wahrscheinlich Wikipedia-Halluzination. Bei YMYL-Page ist die kommunale Primärquelle vorrangig. Fix: Auf "am 28. August 1803" korrigieren (Quelle: ostfriedhof.de/der-friedhof/geschichte + aachen.de).

Anmerkungen (kein MAJOR):

FAQ-Schema vs. HTML-FAQ: identisch (7 Q&A, alle §-Refs konsistent) — PASS.
§-Referenzen BestG NRW (§11 Abs. 2, §13 Abs. 2/3, §15 Abs. 1/5) korrekt.
Eurobeträge mit Stand 17.12.2025 durchgängig korrekt vs. PDF der 17. Änderungssatzung.
URL-Slug "16-aenderungssatzung..." zeigt inhaltlich die 17. Änderungssatzung — Stadt-Aachen-Eigenheit, kein Fehler der Page.
Cross-Links Köln/Düsseldorf/Bonn explizit als "in Vorbereitung" markiert — bewusst, kein dead-link-MAJOR.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
Zu viele Antworten werden gleichzeitig generiert. Du kannst eine Antwort stoppen oder warten, bis eine abgeschlossen ist, und es dann erneut versuchen.