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
Re-Review Rostock: Major-Funde Überprüfung
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
Strenge Überprüfung von Berlin-Bestättern
Strict independent review for Bremen
Strenge Überprüfung von Hamburg auf machsruhig.de
Strenge Überprüfung von Essen-Inhalten
Strenge Überprüfung von Berlin-Bestättern
Korrektionen zu Leipziger Friedhofsinformationen
Dortmund Bestatter Review Pass 2
Dresden Bestatter Review Pass 2
Bestatter Essen HTML-Korrektionen
Bremen-Artikel Korrektionen und HTML-Fixes
Dortmund Friedhöfe: Kritische Adress- und Rechtstext-Korrektionen
Dresden Friedhof Schema-Korrektionen
Bestattungsgesetz NRW: Erbfolge und Faktenchecks
Strenge Überprüfung von Leipzig auf machsruhig.de
Alle Chats
B
Bolle
Max Plan
Re-Review Rostock: Major-Funde Überprüfung
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetch die neue Version und prüfe die beiden MAJOR-Funde.

Ich fetch die neue Version und prüfe die beiden MAJOR-Funde.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/rostock/index.html?cb=1779102513387
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/rostock/index.html?cb=1779102513387

STADT: Rostock
VERDICT: CLEAN (2/2 fixed)

Fund 1 — Ascheverstreuung-Superlativ: ✓ FIXED Im HTML-Story-Block Westfriedhof steht jetzt: "Die Streuwiese auf dem Westfriedhof war eine sehr frühe Anlage dieser Art in Deutschland; sie entstand zu DDR-Zeiten und blieb auch nach 1990 in Betrieb." — exakt die geforderte weichere Formulierung. Keine Spur mehr von "erste ihrer Art in Deutschland überhaupt" auf der Seite. Auch in der FAQ und im JSON-LD wird nur noch neutral von "Rostocker Besonderheit" / "ausgewiesenen Fläche des Westfriedhofs seit 1985" gesprochen.

Fund 2 — FAQ-Schema-vs-HTML-Mismatch: ✓ FIXED Beide Listen sind jetzt 1:1 deckungsgleich (6 Fragen in derselben Reihenfolge):

Wie viele kommunale Friedhöfe…
Was kostet ein Grab in Rostock?
Wie lange ist die Ruhefrist in MV?
Wo wird ein Sterbefall in Rostock angezeigt?
Gilt in MV Sargpflicht?
Welche Bestattungsarten gibt es…

Die alte Schema-only-Frage "Wann muss eine Bestattung in MV erfolgen?" ist aus dem JSON-LD entfernt. Die zusätzliche sichtbare HTML-Frage zur Seebestattung steht außerhalb des FAQPage-Schemas, ist also unkritisch (HTML darf mehr enthalten als Schema, nicht umgekehrt).




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen