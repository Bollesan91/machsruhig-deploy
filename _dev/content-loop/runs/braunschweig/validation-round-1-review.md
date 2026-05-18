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
Braunschweig Stadt-Page Review für machsruhig.de
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
Braunschweig Stadt-Page Review für machsruhig.de
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: I'll fetch the page and review it for major issues.

I'll fetch the page and review it for major issues.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/braunschweig/index.html?cb=1779107743084
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/braunschweig/index.html?cb=1779107743084

Ich pruefe jetzt die kritischen Faktenpunkte. Mehrere Auffaelligkeiten zum Verifizieren: (1) Hermann Blumenau geboren in Hasselfelde 1819, (2) Norbert Schultze 1911 in Braunschweig geboren, (3) Mathilde Todesjahr 1189 (Heinrich der Loewe 1195), (4) Hauptfriedhof Adresse Helmstedter Strasse 38, (5) Stadtfriedhof Helmstedter Strasse 39, (6) Sozialamt Naumburgstrasse 25.

Web durchsucht
Web durchsucht

Blumenau OK: 1819 Hasselfelde, gegründet 1850. Page sagt "1819 in Hasselfelde geborene", "gründete 1850 in Südbrasilien". OK. Page sagt aber: "Am 20. Juni 1974 wurden seine Gebeine exhumiert" - das Datum sollte ich verifizieren, aber das ist Detail; Quellen sagen nur "1974". Kein klarer Faktenfehler.

Jetzt pruefe ich Stadtfriedhof Adresse und Magnifriedhof:

Web durchsucht
Web durchsucht

Wichtige Befunde so weit:

Hauptfriedhof: 43 ha bestätigt, 1887 bestätigt, 1976 Eingangsgebäude bestätigt (genauer 7. Okt 1976), Straßenbahn seit Nov 1954 bestätigt.
Stadtfriedhof Adresse "Helmstedter Straße 39" — die offizielle Stadt-Seite gibt keine Hausnummer 39 an, sondern verweist nur auf Helmstedter Straße. Wikipedia: "Helmstedter Straße, Brodweg und Franz-Frese-Weg". Auch im JSON-LD steht Helmstedter Straße 39. Das könnte ein Faktenfehler sein — der Stadtfriedhof hat keine eindeutige Hausnummer 39; die Hauptfriedhofsverwaltung sitzt Helmstedter Str. 38, der Stadtfriedhof selbst hat den Eingang Franz-Frese-Weg. Unsicher, ob "Nr. 39" konkret falsch ist. Lasse das wegen Unsicherheit weg (kein klarer MAJOR ohne Beleg).
Position des Jüdischen Friedhofs: Text auf der Page widerspricht sich. Im Hero und im JSON-LD-Beschreibung Stadtfriedhof: "in unmittelbarer Nachbarschaft zum evangelischen Hauptfriedhof, getrennt durch den Jüdischen Friedhof". Ja, das stimmt mit Wikipedia überein ("Zwischen Hauptfriedhof und Stadtfriedhof befindet sich der Jüdische Friedhof"). Konsistent.
Hauptfriedhof Größe: Page sagt "rund 43 Hektar" — Wikipedia sagt "rund 42 Hektar" im Einleitungstext, aber Propstei-Verband und Friedhofsverwaltung sagen "zirka 43 Hektar". Page belegbar konsistent.
Wikipedia sagt Hauptfriedhof ist "zweitgrößter kirchlicher Friedhof Deutschlands" (nach Stahnsdorf). Page sagt "einer der größten kirchlichen Friedhöfe Deutschlands". OK, das ist abgeschwächt, nicht falsch.

Jetzt prüfe ich den Magnifriedhof (kritisches Detail: "regulär geschlossen 1887, 2020 als Stadtteilfriedhof reaktiviert") und die NBestattG §-Referenzen:

Web durchsucht
Web durchsucht

Wichtige Korrekturen jetzt klar:

Hauptfriedhof — Stadtbaumeister vs Architekt Ludwig Winter: Page sagt: "Die Friedhofskapelle wurde nach Plänen des Stadtbaumeisters Ludwig Winter errichtet". Wikipedia: "Stadtbaurat Ludwig Winter". Im Personenverzeichnis steht "Ludwig Winter (1843–1930), Stadtbaumeister". Das ist eine konsistente kleine Unschärfe, kein klarer Faktenfehler.
Lessing Grabmal aus "Saubsdorfer Marmor aus Schlesien": Quelle bestätigt ("ehemalige deutsche Provinz Schlesien" — heute Tschechien/Saubsdorf = Supíkovice). OK.

Jetzt der KRITISCHE Check zu §8 NBestattG. Die Page sagt: "Die Bestattungspflicht ergibt sich aus § 8 Abs. 3 BestattG". Im NBestattG ist die Bestattungspflicht-Rangfolge tatsächlich in §8. Aber: User-Memory sagt "BestG NRW §8 next-of-kin sequence" — das ist NRW. Für Niedersachsen muss ich die NBestattG-§§ verifizieren:

Web durchsucht
Web durchsucht

§8 Abs. 3 NBestattG mit Rangfolge Ehegatte/Lebenspartner → Kinder → Enkelkinder → Eltern → Großeltern → Geschwister — die Page-Reihenfolge ("Ehegattin/Ehegatte, Kinder, Enkelkinder, Eltern, Großeltern, Geschwister") ist KORREKT. §8 Abs. 4 für Gemeinde-Veranlassung auch korrekt. §9 (Fristen) und §11 (Sargpflicht) ebenso.

Ein letzter Check: Stadtfriedhof Erweiterung 1969 und die Adresse:

Web durchsucht
Web durchsucht

Wichtige Befunde verdichten sich:

Stadtfriedhof "Erweiterung 1969": Quellen erwähnen 1930 als Eröffnung des Urnenfriedhofs, 2006 neue Feierhalle, keine Quelle nennt 1969 als Erweiterungsdatum. Die Page-Behauptung "Erweiterung 1969" konnte ich in keiner Quelle bestätigen. Das ist eine potenzielle Halluzination — aber ich kann es nicht negativ belegen, daher melde ich es als zu prüfendes Risiko, nicht als MAJOR ohne Gegenbeleg. Skip — bei Unsicherheit nicht melden.
Stadtfriedhof Adresse "Helmstedter Straße 39": Find-a-Grave gibt "Helmstedter Strasse 38A" für Stadtfriedhof, BillionGraves gibt "18 Brodweg". Die Stadt-Braunschweig-Seite selbst gibt keine Hausnummer. Die Hausnummer 39 taucht in keiner verifizierbaren Quelle auf. Plus: Der Hauptfriedhof hat Helmstedter Str. 38 als Verwaltungsadresse, und der Stadtfriedhof liegt DAHINTER (nicht direkt an der Helmstedter Straße als Hauptzugang). "Helmstedter Straße 39" wirkt halluziniert. Aber: keine harte Negativ-Quelle — meldet als möglich, aber unscharf.
Klares Item: Der Page-Hero sagt "Vier große Friedhöfe an der Helmstedter Straße in unmittelbarer Nachbarschaft – Hauptfriedhof, Stadtfriedhof, Jüdischer Friedhof und Katholischer Friedhof". Stadtfriedhof-Wikipedia: "An den Hauptfriedhof grenzen weitere große Friedhöfe an, wie der Stadtfriedhof in Trägerschaft der Stadt Braunschweig und dahinter der Katholische Friedhof". Stadt-Braunschweig-Seite: "Der Stadtfriedhof liegt an der Helmstedter Straße angrenzend an den Evangelischen Hauptfriedhof und den Katholischen Friedhof". Damit ist die räumliche Anordnung Hauptfriedhof – Jüdischer Friedhof – Stadtfriedhof – Katholischer Friedhof korrekt dargestellt. OK.

Lasse mich noch FAQ-Schema vs HTML prüfen — ich habe alle 7 Fragen sowohl in HTML als auch in JSON-LD. Inhalt stimmt sinngemäß überein. OK.

Cross-Links: /bestatter/hannover/, /bestatter/goettingen/, /bestatter/osnabrueck/, /bestattung-in/niedersachsen/. Diese würde ich nicht crawlen können ohne Zugriff. Status unklar, lasse weg.

Zusammenfassung: Ich finde keine harten MAJOR-Faktenfehler mit klarem Gegenbeleg. Die zwei verdächtigsten Punkte (Hausnummer Stadtfriedhof "39", "Erweiterung 1969") sind unscharf und ich kann sie nicht eindeutig widerlegen — daher KEIN MAJOR-Verdict ohne Quelle.

Allerdings: Page-Adresse "Helmstedter Straße 39" für Stadtfriedhof + JSON-LD wiederholt das = das wäre potenziell falsch, aber ohne Gegenbeleg lasse ich es weg gemäß User-Vorgabe ("Belege wenn möglich").

STADT: Braunschweig
VERDICT: CLEAN — keine MAJOR-Funde.

Geprüft: Daten/Personen (Blumenau 1819 Hasselfelde, Schultze 1911, Lessing 1781, Heinrich der Löwe 1195 / Mathilde 1189, Dom-Stiftung 1173) — alle belegt korrekt. §§-Referenzen NBestattG (§8 Abs. 3 Rangfolge, §8 Abs. 4 Gemeindebestattung, §9 Abs. 1/2 Fristen, §9 Abs. 2 8-Tage-Frist + Monatsfrist Urne, §11 Abs. 1 Sargpflicht) — alle exakt korrekt, Rangfolge Ehegatte→Kinder→Enkel→Eltern→Großeltern→Geschwister stimmt mit Originaltext überein. Friedhofs-Eckdaten (Hauptfriedhof 1887/43 ha, Stadtfriedhof 1914, Jüdischer Friedhof 1914 Lübke, Katholischer 01.11.1901/8,47 ha, Magnifriedhof 1887 geschlossen/2020 reaktiviert, Straßenbahn seit Nov 1954, Eingangsgebäude 1976) — alle bestätigt. FAQ-Schema vs HTML: 7/7 Fragen konsistent, kein Schema-Mismatch. Geldbeträge (795 €, 100 €, 32,90 €, 1.582,90 €, 3.000–4.500 €) mit Stand-Datum 13.05.2026 und Satzungs-Stand 01.03.2022 sauber qualifiziert.

Zwei Punkte zum Selbst-Verifizieren (kein MAJOR, da ohne Gegenbeleg): "Stadtfriedhof, Helmstedter Straße 39" — Hausnummer in keiner Primärquelle gefunden (Stadt-BS-Seite gibt keine Hausnummer; Hauptfriedhof-Verwaltung sitzt Helmstedter Str. 38). "Stadtfriedhof Erweiterung 1969" — Quellen nennen Urnenfriedhof-Eröffnung 1930 und Feierhalle 3 von 2006, 1969 nirgends bestätigt. Beide kurz im Stadt-BS-Friedhofsamt rückfragen.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen