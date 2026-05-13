Neuer Chat
Ctrl+⇧+O
Suchen
Ctrl+K
Chats
Projekte
Code
Anpassen
Design
Mehr
Zuletzt verwendet
Ausblenden
Erfurt v5 final adversarial score evaluation
HTML-Version mit Review-Fixes liefern
Friedhöfe und Bestattungen in Hagen
Chat C v5 Halle Adversarial Score Evaluation
Friedhöfe und Bestattungen in Oberhausen
Erfurt v5 final adversarial score evaluation
Erfurt v5 adversarial score evaluation
Hagen-Review nach SCORE-Tabelle
v4 HTML-Version mit Adversarial-Fixes
HTML-Version v4 mit Adversarial-Fixes
Freiburg Schwächen und adversariales Scoring
Friedhöfe und Bestattungen in Oberhausen
Friedhöfe und Bestattungen in Oberhausen
Hagen-Review nach SCORE-Tabelle
Chat C final adversarial recheck for Halle
Erfurt v4 adversarial score evaluation
Saarbrücken FINAL-Adv-Recheck v6 Bewertung
Heidelberg Friedhöfe und Bestattungsgesetze
Heidelberg v3 adversarial score evaluation
Mönchengladbach v3 adversarial score evaluation
Regensburg v3 adversarial score evaluation
Friedhöfe und Bestattungen in Mönchengladbach
Regensburg Friedhöfe und Bestattungsgesetz
Mönchengladbach Schwächen-Analyse
Heidelberg: Schwächen und adversariales Scoring
Regensburg: Schwächen und adversariales Scoring
Regensburg SCORE-Bewertung und Fehlerliste
Heidelberg content review nach SCORE-Tabelle
Mönchengladbach-Review nach SCORE-Tabelle
Chat C v3 Kassel Bewertung prüfen
HTML-Version v6 mit BSG-Aktenzeichen-Fixes
HTML-Version mit Review-Fixes liefern
Chat C v3 Halle performance evaluation
Chemnitz v3 adversarial score evaluation
Krefeld v3 adversarial score evaluation
Friedhöfe und Bestattungen in Krefeld
Friedhöfe und Bestattungen in Halle (Saale)
Chemnitz Friedhöfe und Denkmalschutz
Halle adversarial analysis and weaknesses
Krefeld Schwächen und Adversarial-Score
Heidelberg v4 adversarial score evaluation
Heidelberg v4 adversarial score evaluation
Chemnitz review und bewertung
Krefeld review score und fix-liste
Halle review und bewertung
Chemnitz Schwächen und Adversarial-Bewertung
Heidelberg v4 adversarial score evaluation
Alle Chats
B
Bolle
Max Plan
Erfurt v5 final adversarial score evaluation
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat C (FINAL-Adv-Recheck).

Du bist Chat C (FINAL-Adv-Recheck). v5 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/erfurt/v5-final.html

Stadt: Erfurt. v4 hatte 83%. FINAL-ADVERSARIAL-SCORE 0-100% (Ziel: >=85%).

11:22
Claude hat geantwortet: Ich lade die v5-Datei und führe das adversariale Recheck durch.

Ich lade die v5-Datei und führe das adversariale Recheck durch.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/erfurt/v5-final.html

Ich führe das adversariale Recheck durch. Lass mich systematisch durchgehen mit verschärftem Anti-Sycophancy-Modus.

FINAL-Adversarial-Recheck Erfurt v5
1. § ThürBestG-Verweise — auf Korrektheit geprüft
§ im Text	Behauptung	Plausibilität
§ 1 Abs. 1	Ehrfurcht/Totenwürde/Totenruhe als Ziele	✓ üblich für ThürBestG
§ 4	Ärztliche Leichenschau	⚠️ unklar — in vielen Landesgesetzen ist Leichenschau in §§ 5-6
§ 15	Totenschein	⚠️ Paragraph-Nummer verdächtig nah an § 16
§ 16 Abs. 1	48h Überführung Leichenhalle	✓ plausibel
§ 17 Abs. 1	Erd-/Feuerbestattung gleichberechtigt	⚠️
§ 17 Abs. 3	10 Tage Bestattungsfrist, 6 Monate Urne	⚠️
§ 18	Bestattungspflicht/Rangfolge	✓
§ 19 Abs. 1+2	Wille Verstorbener	✓
§ 20 Abs. 1	48h-Frühestbestattung	⚠️
§ 21 Abs. 1	Zweite Leichenschau vor Feuerbestattung	⚠️
§ 31 Abs. 1	20/15 Jahre Ruhezeit	⚠️

Ich muss das primär verifizieren — denn falsche §-Verweise sind das Killerkriterium.

Web durchsucht
Web durchsucht

Jetzt habe ich die volle ThürBestG-Verifizierung. Lass mich systematisch jeden §-Verweis prüfen:

§-Check ThürBestG — Verifizierung gegen Primärquelle
§ im v5	Behauptung	Primärquelle sagt	Status
§ 1 Abs. 1	Ehrfurcht/Totenwürde/Totenruhe/Totenehrung	✓ exakt so	KORREKT
§ 4	Ärztliche Leichenschau	§ 4 = "Veranlassung der ärztlichen Leichenschau"	KORREKT
§ 15	Totenschein	§ 15 = "Totenschein und Sektionsschein"	KORREKT
§ 16 Abs. 1	48h Überführung in Leichenhalle	✓ "innerhalb von 48 Stunden ... in eine Leichenhalle zu überführen"	KORREKT
§ 17 Abs. 1	Erd-/Feuerbestattung gleichberechtigt	⚠️ § 17 Abs. 1 = "Jede Leiche muss bestattet werden" — Bestattungsarten sind in § 19 Abs. 1 geregelt!	FEHLER
§ 17 Abs. 3	10 Tage / 6 Monate Urne	✓ "Erdbestattung oder Einäscherung innerhalb von zehn Tagen ... Asche innerhalb von sechs Monaten"	KORREKT
§ 18	Bestattungspflicht/Rangfolge	✓ § 18 = "Bestattungspflichtige" mit Rangfolge	KORREKT
§ 18 Abs. 1	Rangfolge Ehepartner→Kinder→Eltern→Geschwister	⚠️ Tatsächliche Reihenfolge: 1. Ehegatte, 2. Lebenspartner, 3. Kinder, 4. Eltern, 5. Geschwister, 6. Enkel, 7. Großeltern, 8. nichtehel. Partner — v5 lässt Lebenspartner und Enkel/Großeltern weg, ohne dies kenntlich zu machen ("und so weiter" deckt das gerade so ab)	UNGENAU/grenzwertig
§ 19 Abs. 1	Erd-/Feuerbestattung gleichberechtigt	✓ "Die Bestattung kann als Erdbestattung oder als Feuerbestattung..."	KORREKT
§ 19 Abs. 2	Wille Verstorbener vorrangig	✓ "Die Art und der Ort der Bestattung richten sich nach dem Willen des Verstorbenen"	KORREKT
§ 20 Abs. 1	48h-Frühestbestattung	✓ "Bestattung ... nur zulässig, wenn seit Eintritt des Todes 48 Stunden verstrichen sind"	KORREKT
§ 21 Abs. 1	Zweite Leichenschau vor Feuerbestattung	✓ "Feuerbestattung ist nur zulässig, wenn durch eine zweite Leichenschau bestätigt..."	KORREKT
§ 31 Abs. 1	20/15 Jahre Ruhezeit	✓ "bei Erdbestattungen mindestens 20 Jahre, bei Urnenbeisetzungen mindestens 15 Jahre"	KORREKT

Kritischer Fund: Der Verweis "§ 17 Abs. 1 und § 19 Abs. 1 ThürBestG" für die Gleichberechtigung von Erd- und Feuerbestattung ist falsch: § 17 Abs. 1 sagt nur "Jede Leiche muss bestattet werden". Die Gleichrangigkeit steht ausschließlich in § 19 Abs. 1. Dieser Fehler tritt zweimal auf (im Recht-Abschnitt und im Todesfall-Abschnitt).

2. Sozialbestattung § 74 SGB XII
Web durchsucht
Web durchsucht

§ 74 SGB XII korrekt zitiert ("erforderliche Kosten einer Bestattung werden übernommen"). ✓

3. Erfurter Friedhofsgebührensatzung verifizieren
Web durchsucht
Web durchsucht

KRITISCHER BEFUND zur Friedhofsgebührensatzung:

Die Linke-Pressemitteilung sagt explizit: "Die Stadtverwaltung will die Friedhofsgebühren zum 1. Januar 2025 um 19 Prozent durch den Aufschlag der Umsatzsteuer erhöhen. Bisher waren diese Gebühren umsatzsteuerfrei. Die Kommunen sind aber erst ab 2027 gesetzlich verpflichtet, diese Umsatzsteuer auch zu erheben." 
Die-linke-erfurt

Die Linke-Quelle ist eine Pressemitteilung VOR der Beschlussfassung (datiert Oktober 2024, Stadtrat sollte am 6.11.2024 entscheiden). Die Beschluss-Nr. 1261/24 vom 06.11.2024 wurde laut Erfurt.de aber tatsächlich gefasst — Geltung ab 01.01.2025 ist bestätigt durch die Satzungs-PDF. Der v5-Text behauptet das korrekt.

Aber: Ich finde eine wichtige Nuance:

v5 sagt: "Die in der untenstehenden Übersicht aufgeführten Beträge entsprechen der Stammfassung 2020; die ab 2025 geltenden Endbeträge liegen je nach Position etwa 19 Prozent höher."
Dies steht im Widerspruch zur Tabelle, die mit "(netto)" gekennzeichnet ist. Frage: Sind die 2020er Beträge tatsächlich Netto-Beträge gewesen, auf die jetzt 19% MwSt aufgeschlagen werden? Oder waren es Bruttobeträge, die nun um 19% erhöht wurden?

Die Linke-Quelle sagt klar: "Bisher waren diese Gebühren umsatzsteuerfrei" → die alten Beträge waren also weder netto noch brutto im klassischen Sinne, sondern USt-frei. Die Klassifikation "netto" in der Tabelle ist daher technisch ungenau — sollte korrekter heißen "umsatzsteuerfrei nach Stammfassung 2020" oder ähnlich. Das ist ein kleiner aber realer Präzisionsmangel. 
Die-linke-erfurt

4. Faktenchecks Friedhöfe & Geschichte
Web durchsucht
Web durchsucht

Faktencheck Hauptfriedhof:

v5: "1907 hatte Gartendirektor Otto Linne in einer Bedarfsberechnung 55 Hektar Gräberfläche für 100 Jahre veranschlagt" → ✓ "Gartendirektor Otto Linne bereits im Jahr 1907 Berechnungen angestellt: Bei Setzung von 200.000 Einwohnern ermittelte er für 100 Jahre eine Gräberfläche von 55 ha" 
Erfurt.de
v5: "1912 schlug Stadtgartendirektor Hermann Bromme dem Erfurter Rat vor" → ✓
v5: "reichsweiten Ideenwettbewerb von 1912/13" — der Wettbewerb wurde am 8.7.1912 ausgeschrieben, Ergebnis 1913 → ✓
v5: "Hennigs (Hannover) und Meißner (Darmstadt) als Sieger" — Erfurt.de schreibt "Hennigs", Wikipedia "Hennings/Paul Meißner". Erfurt.de ist Primärquelle → v5 ist konsistent mit erfurt.de. ✓ aber Vorname Meißners nicht erwähnt — keine Bewertung erforderlich
v5: "Stadtgartendirektor Hermann Braband setzte den überarbeiteten Entwurf ab 1913 baulich um" → ✓ "Stadtgartendirektor Hermann Braband ab Mitte 1913 den Aufbau ... in Angriff" 
Erfurt.de
v5: "ersten 18 Hektar wurden 1914 fertiggestellt, die offizielle Eröffnung folgte am 8. Juli 1916" → ⚠️ Erfurt.de: "1914 als Friedhof durch den Domprobst Feldkamm und Senior Fischer zum Friedhof geweiht". Wikipedia: "1916 eröffnet". Die Trennung Weihe 1914 / Eröffnung 1916 ist plausibel und konsistent → KORREKT
v5: "57 Hektar und gliedert sich in über 50 Grabfelder" → ✓ Erfurt.de: "53 Grabfelder und Sonderanlagen"
v5: "Hauptfriedhof = 57 ha, drei Feierhallen mit 40, 45 und 95 Sitzplätzen" — muss verifiziert werden
Web durchsucht
Web durchsucht

Faktencheck Hauptfriedhof:

✓ 57 ha — bestätigt durch erfurt.de: "Fläche des Friedhofes: 57 ha Anzahl der Grabfelder: 54 Anzahl der Grabanlagen: 43 800 Sitzplätze in den Feierhallen: 40, 45, 95" 
Erfurt.de
✓ Drei Feierhallen mit 40, 45, 95 Sitzplätzen
⚠️ v5 sagt "über 50 Grabfelder" + "mehreren zehntausend Grabanlagen" — Erfurt.de: 54 Grabfelder, 43.800 Grabanlagen. v5 ist deutlich unspezifischer. "Über 50" ist nicht falsch, aber lasch — "53/54 Grabfelder" wäre präziser. "Mehrere zehntausend" ist OK für 43.800.
✓ Krematorium-Architektur (Szabó, 1975-1977, 2 Baukörper, breite Freitreppen, Metallrelief "Das Leben" von Günter Reichert) — bestätigt
⚠️ v5 sagt: "von Mark Escherich im Architekturführer Thüringen als bedeutendster Krematoriumsneubau der DDR eingeordnet" — erfurt-web.de schreibt aber: "Sörries wies auch darauf hin, dass es sich bei dem Veranstaltungsort um den bedeutendsten Krematorium-Neubau der DDR-Zeit handelt" — also Reiner Sörries, nicht Mark Escherich! Das ist eine falsche Zuschreibung. Mark Escherich schreibt zwar im Architekturführer Thüringen über das Krematorium, aber die Bewertung als "bedeutendster DDR-Krematoriumsneubau" kommt von Sörries. 
Erfurt-web

Lass mich das nochmal genauer prüfen:

Web durchsucht
Web durchsucht

KRITISCHER BEFUND (Faktenfehler): Erfurt-web.de schreibt klar: "Mark Escherich unterstreicht im „Architekturführer Thüringen" ebenfalls dessen Bedeutung" — also Escherich erwähnt es AUCH, aber die zentrale Aussage "bedeutendster Krematorium-Neubau der DDR-Zeit" stammt von Reiner Sörries. 
Erfurt-web

Im v5 steht: "von Mark Escherich im Architekturführer Thüringen als bedeutendster Krematoriumsneubau der DDR eingeordnet". Das bleibt eine Verzerrung — Escherich unterstreicht die Bedeutung, aber die zugespitzte Formulierung "bedeutendster" stammt von Sörries. Dies ist ein substanzieller Faktenfehler in der Quellenzuschreibung.

5. Hochheim, Eingemeindung 1938
Web durchsucht
Web durchsucht

Faktencheck Hochheim:

v5: "Hochheim wurde am 1. April 1938 nach Erfurt eingemeindet (1936: 2.750 Einwohner)" ✓ — beides bestätigt
v5: "heute leben in dem ... rund 2.850 Menschen" — Wikipedia (2016): 2.799 Einwohner. Erfurt.de: "ca. 2700 Menschen". → leichte Diskrepanz: v5 sagt 2.850, Erfurt.de sagt 2.700, Wikipedia (2016) sagt 2.799. Quelle für 2.850 unklar — möglich, aber nicht aus Quellen 5–12 belegt. Grenzwertig, nicht direkt falsch.
v5: "8.800 Quadratmetern und rund 643 Grabanlagen" ✓ "Fläche des Friedhofes: 0,88 ha Anzahl der Grabanlagen: 643 Sitzplätze in der Feierhalle: ca. 45" 
Erfurt.de
v5: "etwa 45 Trauergäste" ✓
v5 sagt aber: "ist beheizbar und verfügt über eine öffentliche Toilette" — Erfurt.de: "großzügig angelegten Trauerhalle und der öffentlichen Toilette bietet Raum für 40 bis 50 Trauergäste und ist beheizbar". ✓ 
Erfurt.de
v5: "Seit 2005 besteht die Möglichkeit der Beisetzung in einem Urnengemeinschaftsgrab mit Namensnennung" ✓
v5: "Schule in der Nachbarschaft" ✓
v5: "evangelische Johanneskirche, 1883 im neugotischen Stil erbaut" ✓
v5: "katholische Bonifatius-Kirche" ✓

⚠️ v5 sagt zur Adresse: "Am Angerberg" — Lass mich verifizieren:

Web durchsucht
Web durchsucht

Befund: Adresse "Am Angerberg, 99094 Erfurt-Hochheim" — Korrekt ✓. v5 hat aber Bus-Linie nicht erwähnt (Bus 51, 170, Haltestelle Hochheim) — Erfurt.de listet das. Aber das ist nicht zwingend erforderlich; v5 lässt den Verkehrsanschluss nur weg.

Aber: v5 sagt im JSON-LD-Schema:

"address":{"@type":"PostalAddress","streetAddress":"Am Angerberg","postalCode":"99094","addressLocality":"Erfurt"}

Im Text aber: "99094 Erfurt-Hochheim". → kleine Inkonsistenz aber technisch egal, Erfurt mit PLZ 99094 ist OK.

6. Neuer Jüdischer Friedhof Erfurt
Searching the web
Web durchsucht

Faktencheck Neuer Jüdischer Friedhof:

v5: "1,4 Hektar, ca. 1.000 Grabstellen" ✓ "Fläche des Friedhofes: 1,40 ha Anzahl der Grabanlagen: ca. 1000" 
Erfurt.de
v5: "eröffnet 10. September 1878" ✓ "Am 10. September 1878 wurde er feierlich eröffnet" 
Wikipedia
v5: "Trauerhalle von Hugo Hirsch (1894)" ✓ "Die Halle wurde von dem Architekten Hugo Hirsch geplant ... Das Gebäude ... wurde 1894 eingeweiht" 
Wikipedia
v5: "Kulturdenkmal seit 1994" ✓
v5: "1871 fand sich südlich des Stadtzentrums, an der heutigen Thüringenhalle, ein geeignetes Areal" ✓
v5: "Bürgerschützenkorps als Nachbar versuchte ... Beschwerde beim Magistrat" ✓
v5: "1939 ein Areal an das Bürgerschützenkorps abtreten, das dort bis 1942 die Thüringenhalle baute" ⚠️ — bisher nicht direkt geprüft

Wichtigerer Punkt: v5: "Säulen aus thüringischem Sandstein" — Wikipedia/Erfurt.de erwähnt "thüringischem Sandstein". puffbohne.de spezifiziert "Seeberger Sandstein" (was thüringisch ist). ✓

Aber: v5 sagt "Mazewa" (Singular) — korrekte Bezeichnung wäre Mazewa (Singular) / Mazewot (Plural). Hidden Gem-Titel "Hans Walthers Mazewa" ist linguistisch OK.

⚠️ v5: "Östlich der Trauerhalle standen bis 2009 außerdem 28 Grabsteine, die vom zerstörten Friedhof in der Cyriakstraße gerettet werden konnten" — diese Zahl 28 Grabsteine bis 2009 — muss verifiziert werden:

Web durchsucht
Web durchsucht

Faktencheck Alter Jüdischer Friedhof:

✓ v5: "12. auf den 13. März 1926 verwüsteten Mitglieder des „Wiking-Bundes" den Friedhof und zerstörten 95 Grabsteine" — muss noch geprüft werden. Wikipedia: "Zerstörungen des Friedhofs fanden 1926 durch jugendliche Mitglieder des Wiking-Bundes statt" — bestätigt das Wiking-Bund-Vandalismus 1926. Aber die genaue Anzahl 95 Grabsteine und das Datum 12./13. März finde ich nicht direkt in den primären Quellen, sehe es aber auf juedisches-leben.erfurt.de impliziert. Plausibel, aber nicht 100% verifiziert. 
Wikipedia
v5: "Am 6. April 1939 musste die jüdische Gemeinde das Grundstück unentgeltlich an die Stadt abtreten" — eine andere Quelle sagt allgemein "1939", das spezifische Datum 06.04.1939 ist plausibel, aber nicht in meinen Recherche-Quellen direkt aufgetaucht.
v5: "1944 ließ die Stadtverwaltung die Grabsteine abräumen" ✓ "1944 wurden die Grabsteine entfernt" 
Wikipedia
v5: "1996 wurde ein erster Gedenkstein aufgestellt" ✓
v5: "2007 wurden die Garagen abgerissen" ✓ "An einer „Sichtbarmachung" des Friedhofes wird seit 2007 gearbeitet" 
Wikipedia

⚠️ Verbesserungsbedarf: v5 sagt "1944 ließ die Stadtverwaltung die Grabsteine abräumen", während Wikipedia und Jüdische Gemeinden Online sagen "1944 eingeebnet" und "1944 entfernt". v5 ist konsistent.

7. § 1968 BGB Erben-Verweis

v5 sagt: "Die Bestattungspflicht ist nicht identisch mit der Kostentragungspflicht — diese trifft nach § 1968 BGB die Erben." ✓ — bestätigt durch BGB.

8. Schema.org JSON-LD Konsistenz

Im JSON-LD steht:

WebPage, Article, City, Place (×4), BreadcrumbList, FAQPage, Organization — alle korrekt strukturiert.
City "Erfurt" mit PLZ "99084" — das ist die zentrale Erfurter PLZ (Bürgeramt) — OK
City-geo: "50.9787,11.0328" — passt für Erfurt-Zentrum
Hauptfriedhof: lat 50.9750, lon 10.9806 — plausibel (Bindersleben/Marbacher Straße im Westen)
Telephone Hauptfriedhof: "+49 361 655-5711" ✓
E-Mail: hauptfriedhof.gartenamt@erfurt.de — überprüfen
Web durchsucht
Web durchsucht

✓ E-Mail-Adresse, Telefon-Nummer, Adresse, Öffnungszeiten alle bestätigt.

9. Standesamt Erfurt — Bürgermeister-Wagner-Straße 1
Web durchsucht
Web durchsucht

✓ Standesamt-Adresse "Bürgermeister-Wagner-Straße 1, 99084 Erfurt" bestätigt. Telefon 0361 655-7654 für Urkundenstelle bestätigt.

10. Honesty-Check via Bolle-Recheck-Skript (mental)

Lass mich die 9-Kategorien-Checks gegen die v5 durchgehen:

1. Template-Fehler (Saarland/anderes Bundesland erwähnt?) — keine. ✓ 2. Falsche Städtenamen (nicht in Thüringen) — keine erkennbar. ✓ 3. Unsourced Superlatives — "einziger noch aktiver jüdischer Friedhof Thüringens" ✓ belegt; "bedeutendster Krematorium-Neubau der DDR" ⚠️ falsche Quellenzuschreibung (Escherich statt Sörries). 4. §-Verweise: § 17 Abs. 1 zur Bestattungsart ist FEHLERHAFT (Doppelfehler im Text) 5. Datum-Konsistenz: 1.1.2025 / 01.01.2025 / 06.11.2024 / 04.12.2024 — alles konsistent. 6. Adressen/Telefon: alle ✓ 7. Tote Verweise (Wikipedia-Sätze unbelegt): Hauptsächlich konsolidiert. "1924 Denkmal von Max Standfuß" ✓ Wikipedia. 8. Gewichtung & Balance: Vier Friedhöfe ausführlich beschrieben, zwei davon (Alter + Neuer Jüd.) sehr ausführlich → gut. 9. Trichter / Konversionsbedingungen: Aufbau Logik→Friedhöfe→Kosten→Todesfall→Bestatterwahl→FAQ — ✓

11. Echte Verbesserungen gegenüber v4 (Self-check)

Da v4 mit 83% bewertet wurde, war Sycophancy-Drift ausgeschlossen — v5 muss Substanz haben:

✓ "Bolle-Loop"-Architektur sichtbar in der inhaltlichen Tiefe
⚠️ Ich finde aber keinen Hinweis, dass v5 substanziell besser ist als das, was ein guter v4 wäre. Die meisten Befunde (Architektur, Daten, Quellen) sind übernommen. Die zwei realen Fehler (Escherich/Sörries; § 17 vs. § 19) könnten in v4 unentdeckt geblieben sein und wären hier nicht behoben.
FINAL-Adversarial-Score
Befundtabelle
#	Befund	Schwere	Punktabzug
1	§ 17 Abs. 1 ThürBestG zur Gleichberechtigung Erd-/Feuerbestattung ist falsch zitiert (doppelt im Text) — korrekt ist § 19 Abs. 1 alleine	Substanzieller §-Fehler	-4
2	Zuschreibung "bedeutendster Krematorium-Neubau der DDR" an Mark Escherich falsch — stammt von Reiner Sörries; Escherich unterstreicht es nur	Quellenfehler	-3
3	Tabellen-Klassifikation "netto" für Stammfassung 2020 ungenau — die Beträge waren umsatzsteuerfrei, nicht "netto"	Präzision	-1.5
4	Hochheim-Einwohner "rund 2.850" — Erfurt.de sagt "ca. 2700", Wikipedia 2.799 (2016). Quelle unklar	Präzision	-1
5	"Über 50 Grabfelder" / "mehrere zehntausend Grabanlagen" Hauptfriedhof — Erfurt.de hat präzise Zahlen 54 / 43.800	Lasch, nicht falsch	-1
6	§ 18 Rangfolge-Liste verkürzt ("und so weiter") — Lebenspartner, Enkelkinder, Großeltern, nichteh. Partner ausgelassen	Knapp grenzwertig	-1
7	"12./13. März 1926" und "95 Grabsteine" Vandalismus alter jüd. Friedhof — Wikipedia hat nur "1926", die spezifischen Zahlen finde ich nicht direkt belegt	Behauptung ohne klare Primärquelle	-1
8	"06.04.1939" exaktes Datum der Abtretung des alten jüd. Friedhofs — wieder spezifisch, ohne direkte Belegquelle in der Recherche	Behauptung ohne klare Primärquelle	-0.5
9	Mehrwertsteuer-Erläuterung im Text korrekt, aber die Tabelle hilft Lesern nicht, die tatsächlich heute geltenden Brutto-Beträge zu sehen	UX-Schwäche	-1

Punktstand: 100 - 14 = 86%

Pluspunkte (nicht abzugsfähig, aber qualitätstragend):
Saubere §-Verweise auf ThürBestG (mit den oben genannten Ausnahmen)
Vollständige Quellen-Liste (21 Einträge)
Saubere Schema.org-JSON-LD
Realistische Kostenangaben mit Spannweite 4.500–10.000 €
Klare Trennung städtische Gebühren vs. Bestatterleistungen
Vier Friedhöfe substantiell und unterscheidbar beschrieben
Aufmerksamkeit für Sozialbestattung mit § 74 SGB XII
Hidden Gems gut platziert und nicht generisch
Sozial- und sensibel-thematisch sauber
FINAL-ADVERSARIAL-SCORE: 86%

Ziel >=85% — erreicht, aber knapp.

Empfehlung für Go-Live

Vor Deploy zwingend zu fixen (Blocker):

§-Fehler korrigieren (zwei Stellen im Text):
Statt: "Erdbestattung und Feuerbestattung sind nach § 17 Abs. 1 und § 19 Abs. 1 ThürBestG gleichberechtigt zulässig"
Richtig: "Erdbestattung und Feuerbestattung sind nach § 19 Abs. 1 ThürBestG gleichberechtigt zulässig"
Die zweite Stelle steht im "Todesfall"-Abschnitt mit derselben Formulierung.
Escherich → Sörries korrigieren:
Statt: "von Mark Escherich im Architekturführer Thüringen als bedeutendster Krematoriumsneubau der DDR eingeordnet"
Vorschlag: "Reiner Sörries vom Museum für Sepulkralkultur Kassel hat den Bau 2014 als bedeutendsten Krematoriumsneubau der DDR-Zeit eingeordnet; Mark Escherich unterstreicht die Bedeutung im Architekturführer Thüringen."

Empfohlen (kein Blocker): 3. Tabellen-Klassifikation: "netto" → "(Stammfassung 2020, vor MwSt-Aufschlag)" 4. Hochheim-Einwohner: "rund 2.850" → "rund 2.700" oder Quelle dafür liefern 5. Hauptfriedhof: "über 50 Grabfelder" → "54 Grabfelder"; "mehrere zehntausend" → "rund 43.800" 6. § 18 Rangfolge vollständiger nennen oder explizit auf Verkürzung hinweisen

Nach Fix der Blocker 1+2 würde der Score auf ca. 92–93% steigen. Erst dann "Ende deploy" — bis dahin [skip netlify].

Dein Nutzungsguthaben ist aufgebraucht. Kaufe mehr, um jetzt weiterzumachen, oder warte bis Donnerstag um 14:00, wenn sich deine Plan-Nutzung zurücksetzt.
Mehr kaufen




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
Zu viele Antworten werden gleichzeitig generiert. Du kannst eine Antwort stoppen oder warten, bis eine abgeschlossen ist, und es dann erneut versuchen.
Zu viele Antworten werden gleichzeitig generiert. Du kannst eine Antwort stoppen oder warten, bis eine abgeschlossen ist, und es dann erneut versuchen.
Claude is active in this tab group
Open chat
Dismiss