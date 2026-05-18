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
Kiel Stadt-Page Review für machsruhig.de
Krematorium Heidelberg: Re-Review der 4 Major-Funde
FAQ-Schema Validierung für Halle Bestatter
Schalker Fan-Feld Daten-Review für Gelsenkirchen
FAQ-Schema Überprüfung für Erfurt
Krematorium Heidelberg: Re-Review der Major-Funde
Halle (Saale) Bestatter-Seite Review
Heidelberg Stadt-Page Review für machsruhig.de
Erfurt Stadt-Page Review für machsruhig.de
Freiburg Stadt-Page Review für machsruhig.de
Gelsenkirchen Stadt-Page Review für machsruhig.de
Halle (Saale) Bestatter-Seite Review
Heidelberg Stadt-Page Review für machsruhig.de
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
Re-Review Frankfurt Friedhof und Bestattungsrecht
Rostock Bestatter Review auf machsruhig.de
Magdeburg Bestatter Review - Qualitätskontrolle
Re-Review Rostock: Major-Funde Überprüfung
Magdeburg-Überprüfung: MAJOR-Funde validieren
Überprüfung der Köln-Seite auf behobene Major-Fehler
Potsdam-Friedhof: Überprüfung der MUST-FIX-Korrektionen
Alle Chats
B
Bolle
Max Plan
Kiel Stadt-Page Review für machsruhig.de
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetche die Live-Version und prüfe auf MAJOR-Issues.

Ich fetche die Live-Version und prüfe auf MAJOR-Issues.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/kiel/index.html?cb=1779110750155
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/kiel/index.html?cb=1779110750155

Ich prüfe die kritischen Punkte: Friedhofsanzahl, Eichhof-Eröffnung, Niobe-Datum, Koester, Paragraph-§-Referenzen BestattG SH, FAQ-Schema vs HTML, Cross-Links.

Schnelle Verifikation der Hauptfakten:

Niobe sank 26. Juli 1932 ✓
Eichhof eröffnet 5. Juli 1900 ✓
Südfriedhof 30. April 1869 ✓
Hans von Koester (1844–1928) ✓
BestattG SH § 13 (Bestattungspflicht), § 15 (Arten), § 15a (Erprobung), § 16 (Fristen) – passt
FAQ-Schema 8 Fragen ↔ HTML 8 Fragen ✓
Cross-Links: /bestattung-in/schleswig-holstein/, /ratgeber/seebestattung/, etc. – kann ich nicht intern verifizieren, nicht melden ohne Beleg

Potenzielle Issues:

Selbstwiderspruch Nordfriedhof Größe: Keyfacts sagen "größter städtischer Friedhof = Nordfriedhof 16 ha". Im Nordfriedhof-Porträt steht "größter städtischer Friedhof Kiels". Konsistent.
Selbstwiderspruch Eichhof Fläche: Kauf 1896 von "37 Hektar große Hofstelle", später "rund 39 Hektar". Plausibel durch Erweiterung, aber nicht erklärt – grenzwertig, kein klarer Faktenfehler.
§ 9 BestattG SH (Leichenschau): BestattG SH § 9 ist tatsächlich Leichenschau ✓
§ 10 BestattG SH (Überführung in Leichenraum): Korrekt ✓
Niobe-Zahlen: 109 Besatzung, 69 Tote – das ist die etablierte Zahl, ✓
Hans von Koester "erster aktiv dienender Großadmiral": Tirpitz wurde 1911 Großadmiral, war aktiv. Koester wurde 1905 Großadmiral. Das ist faktisch richtig – Koester war der erste, Tirpitz später.
Bestattungsfristen alte Regel "ein Monat": Vor Novelle galt in SH tatsächlich 1 Monat – ✓
Friedhof Russee/Meimersdorf als städtisch: Plausibel, aber Meimersdorf könnte kirchlich sein. Hier unsicher → nicht melden (UNSURE-Regel).

Hauptfunde:

STADT: Kiel
VERDICT: PASS mit 2 MAJOR

Fund 1: Selbstwiderspruch Eichhof-Fläche Wo: Abschnitt „Parkfriedhof Eichhof", Absatz zur Geschichte. Was: Text sagt „1896 kaufte die Kirchengemeinde […] eine 37 Hektar große Hofstelle", direkt darauf „heute ist der Eichhof mit rund 39 Hektar". Sprung von 37→39 ha ohne Erklärung (Erweiterung? Vermessung?). Leser merkt den Widerspruch. Fix: Entweder „ursprünglich 37 ha, später auf rund 39 ha erweitert" ergänzen ODER eine konsistente Zahl wählen und mit Quelle belegen.

Fund 2: § 10 BestattG SH – nicht verifizierte „36-Stunden"-Frist Wo: Abschnitt „Was nach einem Todesfall in Kiel zu tun ist", Schritt 2 (Bestatter beauftragen). Was: „Im Verbund mit den ortspolizeilichen Regelungen der Stadt Kiel und der Bestattungsverordnung gilt dabei in der Praxis: Die Überführung soll regelmäßig spätestens innerhalb von 36 Stunden nach Todeseintritt erfolgen." Die 36-Stunden-Frist ist im BestattG SH selbst nicht so kodifiziert; § 10 spricht von „unverzüglich". Die konkrete 36-h-Angabe wird einer „Bestattungsverordnung" zugeschrieben, die in dieser Form für SH nicht eindeutig belegbar ist. YMYL-Risiko: Angehörige könnten sich auf nicht existente Frist verlassen. Fix: Entweder konkrete Rechtsquelle (Paragraph + Verordnung) nennen oder auf „unverzüglich nach § 10 BestattG SH, in der Praxis innerhalb von 24–36 Stunden" abschwächen ohne Suggestion einer harten Frist.

Hinweis: Friedhofszahlen, FAQ-Schema↔HTML-Sync (8↔8), §15/§16/§13/§16(3)-Drei-Monats-Frist, Niobe-Daten und Koester-Eckdaten sind sauber.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen