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
Chemnitz Stadt-Page Review für machsruhig.de
Chemnitz Stadt-Page Review für machsruhig.de
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
Chemnitz Stadt-Page Review für machsruhig.de
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich hole die Live-Version und prüfe auf MAJOR-Issues.

Ich hole die Live-Version und prüfe auf MAJOR-Issues.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/chemnitz/index.html?cb=1779107743248
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/chemnitz/index.html?cb=1779107743248

Ich prüfe die Schlüsselfakten. Zwei Punkte fallen sofort auf:

Selbstwiderspruch Krematorium-Weihe vs. erste Einäscherung: Im Hero-Text steht "erste sächsische Krematorium, am 15. Dezember 1906 geweiht". Im FAQ-Schema und im Friedhofsprofil heißt es "die ersten beiden Einäscherungen Sachsens am Folgetag" (16.12.1906). Quelle 4 nennt aber explizit: "erste Einäscherung Sachsens 16.12.1906" — konsistent mit dem Text. Kein Widerspruch.
Paragraph-Referenz § 18b Abs. 6 SächsBestG (Friedhofspflicht) — das ist verdächtig. Ich verifiziere kurz.
Web durchsucht
Web durchsucht

Wichtige Erkenntnisse:

§ 19 → tatsächlich § 21: Die im Text als "§ 19 Abs. 1" und "§ 19 Abs. 2" SächsBestG zitierten Fristen (48 Std, 8 Tage, 6 Monate) stehen laut REVOSax und Aeternitas-Quelle nicht in § 19, sondern in § 21 SächsBestG. Allerdings: Die Aeternitas-Quelle, die im Quellenverzeichnis der Chemnitz-Page selbst gelistet ist, schreibt klar "§ 19 Abs. 1 Satz 1 SächsBestG". Das ist eine bekannte Inkonsistenz: ältere Fassungen hatten andere Nummern. Ich verifiziere noch einmal die aktuelle Nummerierung.
Fetched: Sächsisches Bestattungsgesetz
Fetched: Sächsisches Bestattungsgesetz

Bestätigt durch die offizielle REVOSax-Quelle: § 19 SächsBestG = "Fristen für die Bestattung" mit Abs. 1 (48 Std, 8 Tage) und Abs. 2 (6 Monate für Urne). Die Zitate auf der Chemnitz-Page sind korrekt.

Auch § 18b Abs. 6 SächsBestG ("Urne muss innerhalb der Ruhefrist umweltgerecht abbaubar sein") ist korrekt zitiert, aber: die Chemnitz-Page schreibt, dass "die Friedhofspflicht nach § 18b Abs. 6 SächsBestG" gelte. § 18b Abs. 6 regelt jedoch nicht die Friedhofspflicht, sondern die Eigenschaft der Urne (umweltgerecht abbaubar). Die Friedhofspflicht steht in § 18 Abs. 1 Satz 2 SächsBestG. Das ist ein Faktenfehler bei der Paragraph-Zuordnung.

Weitere Prüfungen:

Adresse Jüdischer Friedhof "Am Laubengang 15": Im Volksmund und auch laut Quelle 6 (guter-ort.in-chemnitz.de) heißt der Standort tatsächlich "Am Laubengang". Aktuell offiziell ist "Jüdischer Friedhof am Laubengang". Plausibel.
Krematorium "vier Einäscherungsöfen": Im Hero-Text steht "Heute sind dort vier Einäscherungsöfen in Betrieb" (FAQ-Schema) bzw. "vier vollautomatische Einäscherungsöfen" im Friedhofsprofil. Konsistent.
Reichenbrand Eingemeindung: Page sagt "1. April 1922 nach Siegmar" und "1. Juli 1950 als Ortsteil der Stadt Siegmar-Schönau nach Chemnitz". Das ist verworren — Siegmar-Schönau wurde 1950 nach Chemnitz eingemeindet, nicht Reichenbrand "über" Siegmar-Schönau. Lasse ich als MINOR durchgehen, da es eine plausible Lesart gibt.
FAQ-Schema vs sichtbares HTML-FAQ: Schema hat 7 Fragen, HTML hat 7 sichtbar — die Fragen stimmen inhaltlich überein, mit geringfügigen Erweiterungen im HTML (kein Mismatch der Antworten).
Cross-Links: /bestattung-in/sachsen/ und /bestattung-in/sachsen/#kosten und /vorsorge/ — keine Verweise auf andere Stadt-Pages → keine Dead Cross-Links.
Geldbeträge: Stand "Januar 2024" ist explizit genannt, Hinweis im Footer "Stand der Daten: Mai 2026" → YMYL OK.

STADT: Chemnitz VERDICT: PASS mit 1 MAJOR

Fund 1: Falsche Paragraph-Referenz bei Friedhofspflicht

Wo: Abschnitt "Bestattungsrecht in Chemnitz", Satz: "Eine Aufbewahrung der Urne zu Hause ist nicht zulässig — auch in Chemnitz gilt die Friedhofspflicht nach § 18b Abs. 6 SächsBestG."
Was: § 18b Abs. 6 SächsBestG regelt ausschließlich, dass die Urne "innerhalb der Ruhefrist umweltgerecht abbaubar sein" muss — nicht die Friedhofspflicht. Die Friedhofs-/Bestattungsplatzpflicht steht in § 18 Abs. 1 Satz 2 SächsBestG ("Die Bestattung im Freistaat Sachsen ist nur auf einem in § 1 Abs. 1 bezeichneten Bestattungsplatz zulässig"), die Beisetzungspflicht für Urnen innerhalb 6 Monaten in § 19 Abs. 2 SächsBestG.
Fix-Empfehlung: "§ 18b Abs. 6" → "§ 18 Abs. 1 Satz 2 i.V.m. § 19 Abs. 2 SächsBestG".
Beleg: REVOSax, offizielle Fassung SächsBestG vom 25.05.2018 — § 18b Abs. 6 vs. § 18 Abs. 1 Satz 2.

Alles andere (Krematoriums-Daten, Friedhofsadressen, Gebühren mit Stand Januar 2024, § 6 Ruhezeit, § 19 Fristen, FAQ-Schema/HTML-Konsistenz, Cross-Links) — keine MAJOR-Funde.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
Zu viele Antworten werden gleichzeitig generiert. Du kannst eine Antwort stoppen oder warten, bis eine abgeschlossen ist, und es dann erneut versuchen.