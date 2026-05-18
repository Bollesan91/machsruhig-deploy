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
Gelsenkirchen Stadt-Page Review für machsruhig.de
Wixhausen-Eingemeindung Darmstadt überprüfen
Augsburg-Bestatter: Re-Review der Major-Funde
Überprüfung Paragraph-Referenzen Chemnitz
Ostfriedhof Aachen: Re-Review der Major-Funde
Wixhausen-Eingemeindung Darmstadt überprüfen
Aachen Stadt-Page Review für machsruhig.de
Chemnitz Stadt-Page Review für machsruhig.de
Darmstadt Stadt-Page Review für machsruhig.de
Braunschweig Stadt-Page Review für machsruhig.de
Augsburg Stadt-Page Review für machsruhig.de
Aachen Stadt-Page Review für machsruhig.de
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
Hamburg Bestattungsseite: 3 kritische Korrektionen
Berlin Bestattungsgesetz Faktenchecks
Korrektionen Bestattungsgesetz NRW Rangfolge
Berlin Bestatter Review - Hauptprobleme
Hamburg Bestattungsanbieter Überprüfung
Bremen Bestatter Korrektionen: Architektur und Lebensdaten
Bremen Strict Independent Review
Alle Chats
B
Bolle
Max Plan
Gelsenkirchen Stadt-Page Review für machsruhig.de
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: I'll fetch the live version and review it for major issues.

I'll fetch the live version and review it for major issues.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/gelsenkirchen/index.html?cb=1779109172155

Ich prüfe jetzt systematisch auf MAJOR-Issues. Lass mich kritische Fakten gegenchecken.

Web durchsucht
Web durchsucht

Wichtige Funde: Die Schalke04.de-Quelle sagt klar "Seit Dezember 2012" für die Eröffnung des Schalke Fan-Felds. Die SFCV-Quelle von 2008 spricht zwar von Grundsteinlegung Juli 2008 + Einweihung Oktober 2008, aber die offizielle Vereinsquelle widerspricht das. Auch BAUWELT nennt 4000 m² statt 3.600 m². Und Olly Olschewski starb laut taz Januar 2013 (nicht 2013 generell — Beisetzung 9. März 2013). Lass mich noch §13 BestG NRW checken.

Web durchsucht
Web durchsucht

§ 13 BestG NRW Frist (10 Tage) und § 8 (Rangfolge) sind korrekt. Jetzt prüfe ich noch die Cross-Links und die Schalker Daten genauer — da gibt es ein ernsthaftes Datums-Problem.

Kritischer Fund: Die offizielle Quelle schalke04.de schreibt eindeutig "Seit Dezember 2012 können königsblaue Fans ... auf dem Schalke Fan-Feld" — das ist die wahrscheinlich tatsächliche Eröffnung. Die Seite behauptet aber durchgängig Einweihung 2008 (Hero, FAQ, Cemetery-Block, Sources). Die taz-Quelle von 2013 berichtet auch über die erste Beisetzung im März 2013. Bauwelt sagt 4000 m² (nicht 3.600). Allerdings sagt SFCV-Quelle Grundsteinlegung 27.7.2008 + Einweihung Oktober 2008 — was vermutlich eine ANDERE Anlage war (auf "Friedhof Gelsenkirchen-Horst", nicht Beckhausen-Sutum). Das ist ein gewichtiger Hinweis auf Konfusion zwischen zwei Schalker Grabfeldern.

Lass mich kurz die Cross-Links für tote Links checken.

Web durchsucht
Web durchsucht

Cross-Link Herne wurde nicht im Suchindex gefunden — kann Hinweis auf fehlende Page sein, aber ohne klare Bestätigung kein definitiver MAJOR-Fund (ich notiere als möglich). Genug Material. Ich schreibe den Review.

STADT: Gelsenkirchen
VERDICT: FAIL — 2 MAJOR-Funde

Fund 1: Selbstwiderspruch / mögliches Datumsproblem Schalker Fan-Feld Wo: Cemetery-Block "Schalker Fan-Feld", FAQ-Schema und Hero Was: Seite behauptet durchgängig "eingeweiht Oktober 2008" bzw. "war 2008 der erste Themenfriedhof". Die offizielle Vereinsquelle schalke04.de schreibt jedoch eindeutig: "Seit Dezember 2012 können königsblaue Fans ihrem Herzensverein auch über den Tod hinaus verbunden bleiben: auf dem Schalke Fan-Feld, einem Gemeinschaftsgrabfeld auf dem Friedhof Beckhausen-Sutum". Die SFCV-Quelle von 2008 (auf der die Seite fußt) bezieht sich vermutlich auf eine andere/Vorgänger-Anlage in Gelsenkirchen-Horst (Thema Bergbau/Zeche), nicht auf Beckhausen-Sutum. Auch die taz berichtet erste Beisetzung März 2013, kompatibel mit Eröffnung Dez 2012. Fix: Datum auf "Dezember 2012" korrigieren (alle Stellen: Hero, Cemetery-Meta, FAQ-Schema, FAQ-HTML, Kostenblock, Sources-Annotation). "Erster Themenfriedhof 2008" prüfen — taz-Beleg möglich, aber Eröffnungsjahr stimmt nicht. Quelle: schalke04.de Inside-Interview mit Ulupinar. 
Schalke 04

Fund 2: Selbstwiderspruch Flächenangabe Fan-Feld Wo: Cemetery-Block "Schalker Fan-Feld" + FAQ Was: Seite nennt "3.600 m²" (SFCV-Quelle von 2008). Bauwelt (Architekturfachpresse, beruht auf Faru Architekten) nennt jedoch "Auf rund 4000 Quadratmetern finden 1904 Gräber Platz". Fix: Auf "rund 4.000 m²" ändern oder beide Angaben sauber qualifizieren (3.600 m² Planung 2008 / 4.000 m² Realisierung laut Architekten). 
Bauwelt

Hinweis (kein MAJOR): § 8 BestG NRW, § 13 Abs. 3 BestG NRW, § 28 PStG, § 74 SGB XII — alle korrekt referenziert. Gebührensatzung mit Stand 01.01.2025 sauber datiert.

(247 Wörter)




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen