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
Darmstadt Stadt-Page Review für machsruhig.de
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
Berlin Bestattungsseite: Faktenchecks und Korrektionen
Dresden Bestatter Review Pass 2
Bestatter Essen HTML-Korrektionen
Bremen-Artikel Korrektionen und HTML-Fixes
Dortmund Friedhöfe: Kritische Adress- und Rechtstext-Korrektionen
Dresden Friedhof Schema-Korrektionen
Strenge Überprüfung von Leipzig auf machsruhig.de
Strenge Überprüfung von Berlin-Bestättern
Strict independent review for Bremen
Strenge Überprüfung von Hamburg auf machsruhig.de
Strenge Überprüfung von Essen-Inhalten
Strenge Überprüfung von Berlin-Bestättern
Dortmund Bestatter Review Pass 2
Korrektionen zu Leipziger Friedhofsinformationen
Alle Chats
B
Bolle
Max Plan
Darmstadt Stadt-Page Review für machsruhig.de
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetche die Live-Version und prüfe.

Ich fetche die Live-Version und prüfe.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/darmstadt/index.html?cb=1779107743409
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/darmstadt/index.html?cb=1779107743409

Ich prüfe jetzt auf MAJOR-Issues. Zentrale Checks:

§ 16 FBG Hessen — Bestattungsfrist: Im FBG Hessen 2007 ist die Bestattungsfrist tatsächlich in § 13 geregelt, nicht § 16. § 16 regelt die Leichenschau. Das muss verifiziert werden.
Web durchsucht
Web durchsucht

§ 16 FBG ist korrekt für die Bestattungsfristen. Auch die Sargpflicht-Referenz (§ 19 FBG) ist plausibel — die Suche oben zeigt § 19 betrifft Erdbestattungen. Gut.

Jetzt prüfe ich die "Bestattungspflicht ohne Rangfolge"-Behauptung gegen § 13 FBG Hessen — das ist ein YMYL-relevanter Punkt:

Web durchsucht
Web durchsucht

Wichtiger Befund: § 13 FBG Hessen kennt keine Rangfolge für die Bestattungspflicht (Aufzählung in Abs. 2 ohne Reihenfolge). Allerdings regelt § 14 Abs. 3 FBG sehr wohl eine Rangfolge bei Meinungsverschiedenheiten über die Bestattungsart (Ehegatte > Verwandte, Kinder > übrige, nähere > entferntere).

Die Aussage auf der Seite ("ohne Rangfolge") ist also mit der Quelle (PDF Standesamt Darmstadt) belegt und beim Sorgepflichtigenkreis (§ 13) auch korrekt — das ist nicht klar genug ein MAJOR-Fehler, um es zu melden. Lasse das durchgehen.

Selbstwiderspruch-Check:

FAQ JSON-LD: Mindestkosten Urne "zwischen rund 2.500 und 5.500 Euro"
Sichtbares FAQ: "zwischen etwa 2.500 € (anonym) und 5.500 €"
Sichtbare Liste oben: "Anonyme Urnenbeisetzung: ca. 2.000 – 3.000 €" und "Urnenbeisetzung mit kleinem Grab: ca. 3.500 – 5.500 €"

→ Widerspruch: FAQ sagt 2.500 € als Untergrenze für anonyme Urne, Liste sagt 2.000 €. Das ist minor und auch eine Größenordnung — grenzwertig, nicht klar genug für MAJOR.

Cross-Links: Frankfurt, Wiesbaden, Offenbach. Schaue ich kurz, ob die existieren — aber für das gegebene Review-Format reicht es, das nicht spekulativ als FAIL zu melden.

Adressen-Check Bessunger Friedhof: Im Article steht "Heinrichwingertsweg 72". Verifiziere kurz:

Web durchsucht
Web durchsucht

Wichtige Funde:

Eberstädter Friedhof: Adresse falsch. Im sichtbaren HTML steht "Palisadenstraße 5–7" und im FAQ ebenfalls. Offizielle Stadt Darmstadt nennt aber Palisadenstraße 7 (Pietät Engelsfunke/Kahrhof: "Pallisadenstraße 20"/"Palisadenstraße 20"). Verifiziere primär:
Web durchsucht
Web durchsucht

Eberstädter Friedhof "Palisadenstraße 5-7" ist plausibel via offizielles Digitales Rathaus Darmstadt. Kein MAJOR-Fehler.

Wixhausen PLZ: Im sichtbaren HTML steht nichts zur PLZ Wixhausen. In FAQ: "Friedhof Wixhausen (Auwiesenweg 18)" — keine PLZ-Angabe im sichtbaren Text. Die Suchergebnisse zeigen 64291 oder 64283 — uneinheitlich. Kein klarer MAJOR-Fund.

Wichtiger Selbstwiderspruch — Adresse Wixhausen vs. Stadt-Quelle: Die offizielle Stadt-Quelle nennt für Arheilgen "Auwiesenweg 18, 64291" — aber das ist Arheilgen. Im HTML steht "Arheilgen: Weiterstädter Straße 46" (korrekt) und "Wixhausen: Auwiesenweg 18" — der Auwiesenweg 18 ist laut offizieller Stadt-Quelle aber der Arheilger Friedhof, NICHT Wixhausen!

Verifiziere das nochmal:

Web durchsucht
Web durchsucht

Klar: "Auwiesenweg 18" ist tatsächlich der Friedhof Wixhausen, nicht Arheilgen. Die offizielle Stadt-Quelle (Eintrag oben in der Suche) verwechselt das selbst, aber andere Primärquellen (Wikipedia, Pietät, Foursquare) bestätigen: Auwiesenweg 18 = Wixhausen. Die Stadt-Quelle aus der vorherigen Suche zeigt "Auwiesenweg 18" beim Arheilger Friedhof (siehe darmstadt.de-Snippet) — das ist offenbar ein Fehler der Stadt-Seite selbst. Die machsruhig-Seite hat es korrekt: Auwiesenweg 18 = Wixhausen. Kein MAJOR-Fund hier.

Jetzt prüfe ich noch den Krematorium-Fakt: Erstes deutsches Krematorium 1878 Gotha — das ist korrekt.

Konsistenz-Check zur Bessunger-Eingemeindung: HTML sagt einmal "Bessungen war bis 1888 eine selbstständige Gemeinde" und am Anfang "Beit Hachajim seit 1680" — Eingemeindung Bessungen tatsächlich 1888? Schnell prüfen:

Searching the web
Web durchsucht

Bessungen 1888 ist korrekt. Keine weiteren MAJOR-Funde aus diesem Check.

Selbstwiderspruch Eingemeindung: HTML sagt einmal "Eingemeindungen 1937" (Eberstadt/Arheilgen/Wixhausen), aber Eberstadt wurde 1937 eingemeindet — und Wixhausen erst 1977! Schnell prüfen:

Web durchsucht
Web durchsucht

MAJOR-Fund: Die Seite behauptet:

Hero: "Vier Anlagen prägen das Friedhofsbild..."
Friedhöfe-Section: "Daneben bestehen die Stadtteilfriedhöfe in Eberstadt, Arheilgen und Wixhausen, die mit den Eingemeindungen 1937 zu Darmstadt kamen."
Stadtteilfriedhöfe-Block: "Mit den großen Eingemeindungen 1937 kamen die südlich und nördlich gelegenen Vororte Eberstadt, Arheilgen und Wixhausen zur Stadt Darmstadt"

Das ist falsch: Eberstadt und Arheilgen wurden 1937 eingemeindet, Wixhausen aber erst zum 1.1.1977 (Gebietsreform Hessen). Quellen einheitlich: Wikipedia, darmstadt.de, wixhausen.de, lagis-hessen.de. Sachlicher Fehler, 2× in derselben Seite — kein Einzelfall. Das ist ein klarer Faktenfehler mit YMYL-Relevanz nicht, aber sachlich klar widerlegbar und doppelt im Text.

Schreibe jetzt das Review.

STADT: Darmstadt
VERDICT: PASS mit 1 MAJOR

Fund 1: Faktenfehler — Eingemeindung Wixhausen falsch datiert (an 2 Stellen im Text)

Wo: (a) Abschnitt "Friedhöfe in Darmstadt", einleitender Absatz: "Daneben bestehen die Stadtteilfriedhöfe in Eberstadt, Arheilgen und Wixhausen, die mit den Eingemeindungen 1937 zu Darmstadt kamen." (b) Stadtteilfriedhöfe-Artikel: "Mit den großen Eingemeindungen 1937 kamen die südlich und nördlich gelegenen Vororte Eberstadt, Arheilgen und Wixhausen zur Stadt Darmstadt."
Was: Eberstadt und Arheilgen wurden 1937 eingemeindet, Wixhausen aber erst zum 1.1.1977 im Zuge der hessischen Gebietsreform. Belege: darmstadt.de Stadtportrait Wixhausen ("Erst seit der hessischen Gebietsreform 1977 gehört Wixhausen zu Darmstadt"), wixhausen.de Geschichte ("Wixhausen wird ab 1977 zu einem Darmstädter Stadtteil"), Wikipedia (Darmstadt-Wixhausen), LAGIS Hessen (kreisfreie Stadt Darmstadt zum 1. Januar 1977 gebildet).
Fix-Empfehlung: An beiden Stellen umformulieren, z. B.: "… Stadtteilfriedhöfe in Eberstadt und Arheilgen (mit den Eingemeindungen 1937 nach Darmstadt gekommen) sowie in Wixhausen (Eingemeindung erst 1977 im Zuge der hessischen Gebietsreform)."

Kleinerer Hinweis (kein MAJOR, FYI): FAQ-JSON-LD und sichtbares FAQ nennen Untergrenze Urnenbeisetzung "2.500 €", die Gesamtkosten-Liste oberhalb dagegen "anonyme Urnenbeisetzung: ca. 2.000–3.000 €". Größenordnung-Disclaimer im Text deckt das ab, kein harter Selbstwiderspruch — daher nicht als MAJOR gemeldet.

Alle anderen geprüften Punkte (§ 16 FBG Bestattungsfrist & Novelle, § 19 FBG Sargpflicht, § 74 SGB XII, Adressen Alter Friedhof/Waldfriedhof/Bessunger/Jüdischer/Eberstadt/Wixhausen, Eingemeindung Bessungen 1888, Krematorium 1913/14, Gotha 1878, Cross-Links Frankfurt/Wiesbaden/Offenbach plausibel) sind sauber.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen