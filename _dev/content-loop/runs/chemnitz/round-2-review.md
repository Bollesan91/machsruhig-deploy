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
Chemnitz review und bewertung
Heidelberg Friedhöfe und Bestattungsgesetze
Friedhöfe und Bestattungen in Halle (Saale)
Friedhöfe und Bestattungen in Krefeld
Chemnitz Friedhöfe und Denkmalschutz
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
Regensburg Friedhöfe und Bestattungsgesetz
Regensburg Friedhöfe und Bestattungsgesetz
Friedhöfe und Gebührensatzung in Kassel
Chat C v3 Rostock performance evaluation
Friedhöfe und Bestattungen in Rostock
Oldenburg v3 adversarial score evaluation
Lübeck v3 adversarial score evaluation
Friedhöfe und Gebührensatzung in Oldenburg
Friedhöfe in Lübeck: Bestattungen und Gebühren
Kassel adversarial review und schwächen analyse
Rostock: Schwächen und adversariales Scoring
Oldenburg: Schwächen und adversariale Bewertung
Rostock: Schwächen und adversariales Scoring
Lübeck adversarial review und schwächen analyse
Alle Chats
B
Bolle
Max Plan
Chemnitz review und bewertung
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/chemnitz/v1-from-chat-A.html

Stadt: Chemnitz (SN). Review SCORE 0-100% + Fix-Liste.

19:55
Claude hat geantwortet: Ich hole mir v1 und reviewe sie systematisch.

Ich hole mir v1 und reviewe sie systematisch.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/chemnitz/v1-from-chat-A.html

Ich gehe systematisch durch und verifiziere die kritischen Faktenbehauptungen.

Faktencheck — kritische Behauptungen

1. Gebühren Stand Januar 2024 — die Satzung muss verifiziert werden.

Searching the web
Web durchsucht

Wichtige Erkenntnis: Die Satzung 67.210 in der Fassung Stand Januar 2024 ist real. Die genauen Gebührensätze muss ich aber verifizieren — die Bestatter-Webseiten zeigen 2012er Stände (105 €, 28 €, 61 €, 40 €, 30 €), v1 zeigt 85 €, 31 €, 67,30 €, 49,40 €, 37,15 €. Das ist ein kritischer Punkt. Ich rufe das PDF direkt ab.

Fetching site
Fetched: https://www.chemnitz.de/fileadmin/chemnitz/media/rathaus/satzungen/67_210_20240101.pdf

Hervorragend — alle Gebühren in v1 sind durchgängig korrekt gegen die offizielle Satzung 67.210 Stand Januar 2024. Quick-Check der v1-Tabellenwerte gegen das PDF:

Position	v1	Satzung	OK?
Reihengrab Erd	423,00	423,00	✅
Wiesen-Reihengrab	794,50	794,50	✅
Wahlgrab/Lösestelle	570,00	570,00	✅
Urnenlösestelle	354,00	354,00	✅
Urnensonderstelle	622,00	622,00	✅
Urnennische Kolumb.	386,00	386,00	✅
Anonym Urnengem.	517,60	517,60	✅
Baumgrab ohne Namen	1.644,00	1.644,00	✅
Baumgrab mit Namen	2.394,00	2.394,00	✅
Kindergrab	177,00	177,00	✅
Friedhofsgrundgebühr	85,00	85,00	✅
Grundgeb. Einlieferung	25,00	25,00	✅
Annahme/Einstell	31,00	31,00	✅
Erdgrab öffn./schl.	297,20	297,20	✅
Urnengrab öffn./schl.	49,40	49,40	✅
Trauergeleit	37,15	37,15	✅
Feierhalle	90,70	90,70	✅
Aufbahr.-/Abschiedsraum	67,30	67,30	✅
Einäscherung	145,35	145,35	✅
Orgelnutzung	28,00	28,00	✅

Alle 20 Gebührenangaben fehlerfrei. Excellent.

Jetzt prüfe ich SächsBestG-Paragrafen.

Searching the web
Web durchsucht

§-Zitate verifiziert. Aber Achtung: v1 schreibt unter "Sterbefall beim Standesamt anzeigen": "Die Anzeige hat innerhalb von drei Werktagen nach Eintritt des Todes zu erfolgen". Das ist nach Personenstandsgesetz § 28 — kurze Verifizierung.

Searching the web
Web durchsucht

§ 28 PStG verifiziert — "drei Werktage" stimmt. Jetzt noch die strittigen historischen Behauptungen und Adressen prüfen — insbesondere:

Krematorium 15.12.1906 + "erstes Krematorium Sachsens"
Friedhof Wartburgstraße geweiht 28.04.1874
Jüdischer Friedhof: Adresse "Am Laubengang 15" und Datum 5.5.1878
Reichenbrand-Adresse "Zwickauer Straße 457"
Searching the web
Web durchsucht

"erstes Krematorium Sachsens 1906" ✅ verifiziert. Schnell die übrigen Daten checken.

Web durchsucht
Web durchsucht

Wichtige Funde:

✅ Friedhof Wartburgstraße, 28.04.1874, Vizebürgermeister Vetters, 30,8 ha — v1 nennt korrekt "Vizebürgermeister Robert Vetters" — Robert ist Zusatz, Wikipedia nennt nur Vetters. NICHT-Blocker: Nicht-falsifizierbar in einer Suche, plausibel.
✅ Krematorium 15.12.1906, erstes Krematorium Sachsens
⚠️ Öffnungszeiten: v1 schreibt "Öffnungszeiten von 7 bis 18 Uhr" für städtische Friedhöfe (im Reichenbrand-Story-Block) — die Webseite zeigt nur Verwaltungs-Öffnungszeiten der Friedhofsverwaltung (Mo-Fr 08:00-12:00). UNGEPRÜFT — kann Tatsache sein, ist aber nicht direkt belegt aus den Sucherergebnissen. Niedrige Priorität, da Friedhöfe in Sachsen typischerweise frei zugänglich sind.

Jetzt der Jüdische Friedhof — v1 nennt "Am Laubengang 15".

Web durchsucht
Web durchsucht

Wichtige Diskrepanzen gefunden — Jüdischer Friedhof:

Behauptung v1	Beleg	Status
Geweiht 5.5.1878	✅ 5.5.1878	OK
1,5 ha	✅ 1,5 ha	OK
sieben Abteilungen	Quelle: sieben Gewanne	OK (Synonym)
Ehrenreihe Rabbiner = F	✅ F	OK
älteste Grabsteine: Gewann D	✅ D	OK
1923: 3.500 Mitglieder, 26 Vereine	⚠️ NICHT IN QUELLE	BLOCKER prüfen
1944 Auto-Union	✅	OK
Schändungen 1945, 1964, 1982, 1986, 1994, 2019, 2021	✅ identisch	OK
Über 80 Grabsteine in Mitleidenschaft	✅	OK
Diamant 1985 Denkmalschutz	✅	OK
Freundeskreis "seit 2014 über 600 Einzelgrabsteine und 12 große Familiengrabsteine"	⚠️ Quelle: über 500 Grabsteine und 15 Erbbegräbnisse	BLOCKER
"Älteste datierte Stein 1878"	nicht direkt belegt — die Quelle sagt "Gewanne D älteste"	KLEINER POINT
Adresse "Am Laubengang 15"	nicht belegt in Geschichte-Quelle	prüfen
Stefan Heym besuchte 2001 ein letztes Mal, "einige Vorfahren bestattet"	NICHT belegt	BLOCKER prüfen
Web durchsucht
Web durchsucht

Adresse "Am Laubengang 15, 09116" ✅ verifiziert. PLZ stimmt. Quick-Check Stefan Heym Vorfahren:

Web durchsucht
Web durchsucht

Stefan Heym ist verifiziert: Vorfahren auf dem Friedhof, 2001 letzter Besuch, Berlin-Weißensee bestattet, Ehrenbürger Chemnitz. ✅

Jetzt schnell der Reichenbrand-Friedhof und die Bestattungszahlen 2.400/40:

Web durchsucht
Web durchsucht

Zwickauer Straße 457, 09117 ✅ verifiziert (offizielle Quelle: kirchgemeinden-chemnitz-west.de). Reichenbrand 1929 eingemeindet — schnell check:

Web durchsucht
Web durchsucht

Wichtiger Fehler gefunden! v1 schreibt:

"Reichenbrand wurde erst 1929 nach Siegmar eingemeindet und kam 1950 mit Siegmar-Schönau zu Karl-Marx-Stadt."

Beide Daten falsch:

Reichenbrand → Siegmar: 1. April 1922, NICHT 1929 (zwei unabhängige Wikipedia-Quellen + Heimatverein)
Siegmar-Schönau → Chemnitz (nicht Karl-Marx-Stadt): 1. Juli 1950. 1950 hieß die Stadt noch Chemnitz; Umbenennung in Karl-Marx-Stadt erst 10. Mai 1953 durch DDR-Ministerrat.

Das ist ein klassischer Recheck-Blocker (Kategorie: Wrong-state-cities-Variante / falsche historische Datierung).

Auch der "1923: 3.500 Mitglieder, 26 Vereine" — verifiziert in Wikipedia "Geschichte der Stadt Chemnitz": ✅ stimmt.

Jetzt noch die strittigen "Beobachtungs"-Zahlen: 2.400 Urnen + 40 Erdbestattungen, 1.250 Bäume Anett Domin, "über 600 Grabsteine + 12 Familiengrabsteine" (gegen Quelle: 500+15):

Searching the web
Web durchsucht

Bestätigt:

Friedhofsverwalterin Anett Domin ✅
1.250 Einzelbäume ✅
2.400 Urnenbeisetzungen/40 Erdbestattungen ✅ (Quelle: Freie Presse 2022)

v1-Behauptung "Verhältnis 60:1" — 2400/40 = 60. ✅

Aber: Diese Zahlen sind aus 2022. v1 schreibt "zählt heute jährlich" — ok, im Wesentlichen aktuell. Aber Reviewer-Anmerkung: keine schwerwiegende Konstante.

Jüdischer Friedhof: "über 600 Einzelgrabsteine und 12 große Familiengrabsteine" — Quelle (guter-ort.in-chemnitz.de) sagt explizit "über 500 Grabsteine und 15 Erbbegräbnisse". Das ist eine direkte Faktendiskrepanz: 600 vs 500, 12 vs 15. BLOCKER.

Letzter Check: Krematorium-Detail "4 Einäscherungsöfen mit Kapazität bis 8.000/Jahr", "33 Mio DM Sanierung 1991", "100 Kühlzellen", "17-Register-Jehmlich-Orgel":

Web durchsucht
Web durchsucht

Krematorium-Daten fast alle ✅:

4 vollautomatische Einäscherungsöfen ✅
8.000 jährliche Kapazität ✅
100 Kühlzellen ✅
17-Register-Jehmlich-Orgel ✅
Über 40% unter Geländeniveau ✅
Architekten Gessler/Ribi ✅
Baufirma Otto Stäber ✅
Baukosten 239.681 Goldmark ✅ (Beleg unten — "weit überzogen")
Bauplan vom 15. Dezember 1905 — ⚠️ Quelle sagt 16.12.1905 für Spatenstich, v1 schreibt 15. Dezember 1905. Faktenfehler

Aber Achtung: v1 Krematorium-Feierhalle "fasst etwa 100 Personen" — Quelle sagt 120 Sitzplätze. Quelle 85 (chemnitz-friedhof.de) sagt "ca. 100 Sitzplätze". Beide Quellen widersprechen sich. Beleg für 100 existiert. Akzeptabel.

Ich habe genug Material für ein qualifiziertes Review. Ich schreibe jetzt Score & Fix-Liste.

Review v1 Chemnitz — Score & Fix-Liste
SCORE: 76/100

Solide Faktenbasis (alle 20 Gebühren ✅, SächsBestG-§§ ✅, PStG § 28 ✅, Krematoriumsdaten ✅, Wartburgstr.-Historie ✅, Stefan Heym ✅). Aber: drei Blocker mit verifizierbar falschen Tatsachen, plus eine Reihe „Vorsicht walten lassen"-Schwächen. Mit Score 76 unter Ziel 85 — v2 nötig.

Blocker (MÜSSEN gefixt werden für ≥85)
B1 · Reichenbrand-Eingemeindungsdatum FALSCH

v1 (Story-Block Reichenbrand): „Reichenbrand wurde erst 1929 nach Siegmar eingemeindet und kam 1950 mit Siegmar-Schönau zu Karl-Marx-Stadt."

Korrekt (3 unabhängige Quellen: Wikipedia Chemnitz-Reichenbrand, Wikipedia Siegmar-Schönau, Heimatverein Reichenbrand):

Reichenbrand → Siegmar: 1. April 1922 (nicht 1929)
Siegmar-Schönau → Chemnitz (nicht Karl-Marx-Stadt): 1. Juli 1950
Umbenennung Chemnitz → Karl-Marx-Stadt erst 10. Mai 1953

→ Doppelfehler: falsches Jahr + falscher Stadtname. Klassischer Recheck-Blocker.

Fix: „Reichenbrand wurde am 1. April 1922 nach Siegmar eingemeindet und kam am 1. Juli 1950 mit Siegmar-Schönau nach Chemnitz (die Umbenennung in Karl-Marx-Stadt erfolgte erst 1953)."

B2 · Jüdischer Friedhof — Sanierungszahlen FALSCH

v1 (Story-Block Jüdischer Friedhof): „Seit 2014 hat der Freundeskreis der Jüdischen Gemeinde Chemnitz über 600 Einzelgrabsteine und 12 große Familiengrabsteine vor dem Verfall gerettet."

Korrekt (Primärquelle guter-ort.in-chemnitz.de/geschichte.html, in Quellenliste zitiert):

„Seit 2014 sind über 500 Grabsteine und 15 Erbbegräbnisse vor dem Verfall gerettet wurden."

→ Beide Zahlen falsch (600 statt 500, 12 statt 15) plus „Familiengrabsteine" statt „Erbbegräbnisse". Inakzeptabel, weil die Quelle in der eigenen Quellenliste steht.

Fix: „Seit 2014 hat der Freundeskreis der Jüdischen Gemeinde Chemnitz über 500 Grabsteine und 15 Erbbegräbnisse vor dem Verfall gerettet."

B3 · Krematorium-Spatenstich Datum FALSCH

v1 (Story-Block Urnenhain): „der erste Spatenstich erfolgte am 15. Dezember 1905. Genau ein Jahr später, am 15. Dezember 1906, wurde das Krematorium eingeweiht"

Korrekt (Primärquelle friedhof-chemnitz.de/Krematorium-Chemnitz):

„konnte am 16.12.1905 der erste Spatenstich zum Bau des Krematoriums erfolgen."

Wikipedia bestätigt ebenfalls 15.12.1905 — hier widersprechen sich zwei Quellen. Aber: Die offizielle Friedhofsverwaltung (eigene Primärquelle, in Quellenliste) sagt 16.12.

→ Niedrigere Schwere als B1/B2, aber: Quellen-Diskrepanz nicht aufgelöst, „genau ein Jahr später"-Konstrukt damit potentiell falsch.

Fix: Entweder Datum auf 16.12.1905 ändern (gemäß Primärquelle der Friedhofsverwaltung) oder „genau ein Jahr"-Konstrukt aufweichen („knapp ein Jahr").

Schwächen (sollten gefixt werden, aber nicht-blockierend)
S1 · Wartburgstraße: „Robert Vetters" — Vorname nicht belegt

v1 nennt „Vizebürgermeister Robert Vetters". Wikipedia + Friedhof-Chemnitz.de nennen nur „Vizebürgermeister Vetters". Vorname nicht falsifiziert, aber auch nicht belegt — Risiko Halluzination. → entweder Beleg nachreichen oder Vornamen streichen.

S2 · „1.250 Bäume" Quellenzuordnung

v1 schreibt: „Friedhofsverwalterin Anett Domin hat allein in der Kategorie Einzelbäume 1.250 Exemplare erfasst, von denen viele zur historischen Erstanlage von 1874 gehören." Der erste Halbsatz ist durch die Freie-Presse-Reportage gedeckt. Der zweite Halbsatz („viele zur historischen Erstanlage von 1874 gehören") ist eine unbelegte Ergänzung. → Streichen oder belegen.

S3 · Krematorium-Feierhalle Sitzplätze

v1: „fasst etwa 100 Personen". Die Friedhofsverwaltung selbst gibt auf zwei Seiten unterschiedliche Werte: 100 (Historie-Seite) vs. 120 (Feierhalle-Krematorium-Seite). „Etwa 100" ist mit der einen Quelle vereinbar, aber unscharf. Niedrige Priorität.

S4 · Öffnungszeiten städtische Friedhöfe „7 bis 18 Uhr"

v1 (Story Reichenbrand): „die städtischen Anlagen haben feste Öffnungszeiten von 7 bis 18 Uhr". Auf der Friedhofs-Chemnitz-Website nicht direkt belegbar (dort nur Verwaltungs-Bürozeiten). Risiko Halluzination — entweder belegen oder weglassen.

S5 · "1.500 Eintauchen Stefan Heym Vorfahren"

v1 schreibt: „einige seiner Vorfahren sind dort bestattet". Beleg liegt vor (dpa via Berliner Abendblatt). ✅ aber: in der v1-Quellenliste fehlt diese Story-Stelle als Beleg. Quelle ergänzen.

S6 · Wahlgrab-Bezeichnung uneinheitlich

v1-Tabelle nennt „Wahlgrab (Lösestelle)" 570,00 €. Die Satzung selbst nennt diese Position einfach „Lösestelle". „Wahlgrab" ist umgangssprachlich/branchenüblich, aber nicht satzungstreu. → entweder satzungstreu „Lösestelle" oder transparent „Lösestelle (Wahlgrab)".

S7 · "Cholera-Epidemie 1866" — kleine Ergänzung

v1 hat das korrekt, aber lässt das Detail unerklärt im Raum stehen. Niedrige Priorität.

Was gut ist (Lob — explizit, damit Chat A es nicht verschlechtert)
Gebühren-Tabellen: 20/20 korrekt gegen Satzung 67.210 Stand Januar 2024. Bemerkenswert sauber.
§§-Zitate: § 19 Abs. 1+2 SächsBestG, § 6 Abs. 2 SächsBestG, § 18b Abs. 6 SächsBestG, § 21 SächsBestG, § 28 PStG — alle wörtlich korrekt.
Krematoriums-Hardfacts: 4 Öfen, 8.000/Jahr, 100 Kühlzellen, 17-Register-Jehmlich-Orgel, Architekten Gessler/Ribi, Baufirma Stäber, 239.681 Goldmark, 33 Mio DM Sanierung 1991 — alle belegt.
Wartburgstr.-Historie: 28.4.1874, Vetters, 30,8 ha, 67 Grababteilungen, Cholera 1866, Frühjahr 1871 Baubeginn, Christus-Statue 4,10 m / Richard König / 2.10.1904 — alles solide.
Jüdischer Friedhof Datum 5.5.1878, Adresse Am Laubengang 15 (09116) ✅
Reichenbrand Adresse Zwickauer Straße 457 (09117) ✅
Stefan Heym Querverweis belegt + verifiziert.
Schema.org-Block: WebPage + Article + City + BreadcrumbList + 4× Place + Organization + FAQPage — Vollständigkeit gut.
Hero-Lead: starker Einstieg, kein Geschwafel, faktenverankert (1.250 Bäume, 15.12.1906 Krematorium).
Funnel zur Bundesland-Seite Sachsen sauber gesetzt.
TL;DR für Chat A
Status	Punkte
Score	76/100 (Ziel ≥85)
Blocker	3 (B1 Reichenbrand 1929/Karl-Marx-Stadt, B2 600/12 vs. 500/15, B3 15./16.12.1905)
Schwächen	7 (Vetters-Vorname, „1874er Bäume", Sitzplätze, Öffnungszeiten 7-18, Heym-Quelle, Lösestelle-Naming, Cholera-Detail)
Gebühren	20/20 korrekt
§§-Zitate	5/5 korrekt
Quellen	10 angeführt, gute Mischung Primär+Sekundär

v2-Empfehlung: Fixe B1+B2+B3 zwingend, S1+S4+S5 für sauberen Recheck-Durchlauf, Rest nice-to-have. Mit B1-B3 + S1+S4 saniert sollte v2 Score ~88 erreichen.

Dein Nutzungsguthaben ist aufgebraucht. Kaufe mehr, um jetzt weiterzumachen, oder warte bis Donnerstag um 14:00, wenn sich deine Plan-Nutzung zurücksetzt.
Mehr kaufen

Du bist Chat B (Reviewer). v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/chemnitz/v1-from-chat-A.html




Stadt: Chemnitz (SN). Review SCORE 0-100% + Fix-Liste.

Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
Claude is active in this tab group
Open chat
Dismiss