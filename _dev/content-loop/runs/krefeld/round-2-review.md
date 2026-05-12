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
Krefeld review score und fix-liste
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
Krefeld review score und fix-liste
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/krefeld/v1-from-chat-A.html

Stadt: Krefeld (NRW). Review SCORE 0-100% + Fix-Liste.

19:55
Claude hat geantwortet: Ich lade die v1 und reviewe sie systematisch.

Ich lade die v1 und reviewe sie systematisch.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/krefeld/v1-from-chat-A.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/krefeld/v1-from-chat-A.html

Jetzt führe ich systematisch den Review durch. Ich prüfe die heiklen Faktenbehauptungen gegen Primärquellen.

Faktencheck — kritische Behauptungen
Searching the web
Web durchsucht

Wichtiger Fund: Wikipedia widerspricht der Behauptung des Erwerbsdatums 1864 (nicht 1867 als Eröffnung). Aber 1867/1891 stimmt als Eröffnungsdaten. Krefeld-Entdecken sagt: Anton Rumpen ist Architekt, 1911-1920 entstanden die Bauten — vs. 1913-1916 in mehreren anderen Quellen.

Jetzt prüfe ich die Krematorium-Behauptung "erstes im Rheinland, fünftes in Preußen":

Searching the web
Web durchsucht

Wichtige Erkenntnisse:

"16-Meter-Kuppel" — wird in den Quellen nicht erwähnt; v1 spricht in der Trauerhalle-Beschreibung von „Halbkreis mit Kuppeldach" (Stadt Krefeld) — der Wert 16m ist NICHT QUELLENGEDECKT
Krematorium-Architekt: Anton Rumpen, Baujahr 1914/1915 (laut Denkmalbehörde), nicht "1913-1916" wie v1 schreibt — die v1-Zahl bezieht sich auf das Ensemble Trauerhalle+Krematorium
"fünftes in Preußen" — bestätigt durch Stadt Krefeld
Trauerhalle ist halbkreisförmig mit Kuppeldach — nicht 16-Meter-Kuppel
Heinz von der Way bestätigt

Jetzt prüfe ich die Gebührensatzung-Zahlen (die wichtigsten Risikoaussagen):

Searching the web
Web durchsucht

Wichtig: Es gibt bereits eine 2025er Gebührensatzung, nicht nur 2024. v1 zitiert die 2024er. Ich muss die Original-PDF prüfen, um die Tabellen-Zahlen zu verifizieren:

Fetching site
Fetched: https://cdn0.scrvt.com/4d6b554b585982c1c18f4b712976e98b/2ac282b4d9f54e18/570c3dee41f1/Friedhofsgebuehrensatzung-2024.pdf

KRITISCHE FUNDE in der Gebühren-Tabelle:

v1-Behauptung	Satzung 2024 (echt)	Status
Reihengrab Sarg "25 Jahre"	Satzung nennt keine 25 Jahre, nur "Reihengrabstätte 1.860 €"	⚠️ Nutzungszeit unbelegt
Urnenreihengrab 1.860 €	1.680 € (Pos. 2.3)	❌ FALSCH
Urnenwahlgrab 2.700 €	2.700 € (Pos. 2.6)	✅
Baumgrabstätte 5.040 €	5.040 € (Pos. 2.7)	✅
Anonyme Urnen 2.100 €	2.100 € (Pos. 2.2)	✅
Anonyme Ascheeinbringung 2.640 €	2.640 € (Pos. 2.1)	✅
Urnenkammer 400 €	10.170 € (Pos. 2.8)	❌ MASSIV FALSCH (Faktor 25!)
Erdwahlgrabstätte 8.250 €	"Parkgrabstätte zur Zweifachbelegung je Grabstelle 8.250 €" (Pos. 1.7)	⚠️ Bezeichnung nicht "Erdwahlgrab", sondern "Parkgrabstätte" — und es ist pro Grabstelle bei min. 2 Stellen = ggf. doppelt
Sargbestattung "1.021 €" auf Hauptfriedhof	Sargbestattung 1.283 € (Pos. 1.1) — 1.021 € ist "Urnen-Ausbettung+Wiederbeerdigung" (Pos. 2.1/2.2 Umbettungen)	❌ FALSCH
Grabmalgenehmigung stehend 211 €	211 €	✅
FAQ: Ruhezeit "25 Jahre" für Urnen	Satzung-Text liefert keine direkte Aussage hier; "Ruhezeit 25" ist in v1 inkonsistent (Hero sagt "25", FAQ sagt "20")	⚠️ Widerspruch im Dokument
5-Jahres-Verlängerung max. 30 Jahre	Stimmt (Pos. 3.2)	✅
Pflege jährlich 51 € + Verwaltung 23 €	Stimmt	✅

Drei harte Faktenfehler in der zentralen Gebührentabelle. Das ist ein Killer.

Jetzt prüfe ich noch das Schloss-Linn / jüdischer Friedhof Linn:

Web durchsucht
Web durchsucht

Linn-Belegung 1751-1936, 64 Grabsteine 1792-1936 — v1-Aussagen stimmen. Aber: v1 sagt "Es ist einer der ältesten erhaltenen jüdischen Bestattungsplätze am unteren Niederrhein" — das ist eine Wertung ohne Quelle.

Auch hier: v1 schreibt "der jüdische Friedhof Am Strathhof" — die Hauptliste der JG Krefeld nennt jedoch Klever Straße als ältesten, Heideckstraße (im Hauptfriedhofs-Areal von 1758 oder, wie Wikipedia sagt, "Begräbnisstätte ... 1723 angelegt") — v1 spricht im Hauptfriedhof-Absatz von "jüdischer Friedhof von 1723". JG Krefeld nennt aber 1758. Inkonsistenz/Faktenrisiko.

Web durchsucht
Web durchsucht

OK — die Aussage "jüdischer Friedhof von 1723" stimmt (Anlage), die Belegungszeit ist 1758-1938. v1 ist also korrekt mit "1723".

Aber: v1 schreibt im FAQ "jüdischer Friedhof Am Strathhof" als separat erwähnt — das ist korrekt.

Jetzt checke ich noch das Standesamt Krefeld (Adresse) und die Hüls-Behauptung mit dem "Schluff" / Uerdinger Linie:

Web durchsucht
Web durchsucht

MASSIVER FAKTENFEHLER: Standesamt Krefeld ist an der Rheinstraße 138, nicht "Von-der-Leyen-Platz 1". Die Adresse Von-der-Leyen-Platz 1 ist das Rathaus / die Stadtverwaltung allgemein. Das Standesamt befindet sich in einem separaten Gebäude an der Rheinstr. 138. Dieser Fehler erscheint in v1 dreimal: Keyfacts, Schritt 3, FAQ.

Ich habe genug Material für ein fundiertes Review. Ich verzichte auf weitere Detailprüfung (Hülser Schluff Sankt Tönis, Cornelius de Greiff Lebensdaten — letztere stimmen laut Wikipedia 1781-1863), da die kritische Faktendichte schon klar ist.

REVIEW v1 Krefeld
SCORE: 62/100

Verdict: NICHT freigabefähig. Drei harte Faktenfehler in zentralen, suchrelevanten Aussagen (Gebührentabelle, Standesamt-Adresse). Stilistisch und strukturell hochwertig, inhaltlich dicht und Schema gut — aber die Fehler sind genau jene, bei denen ein Angehöriger sich blamiert / falsche Wege geht / falsche Summen erwartet. Das ist exakt der Fall, den machsruhig vermeiden muss.

BLOCKER (müssen vor Deploy fixiert sein)
B1 — Standesamt-Adresse FALSCH (3x im Dokument)
v1: "Standesamt Krefeld im Rathaus, Von-der-Leyen-Platz 1"
Korrekt: Standesamt Krefeld, Rheinstraße 138, 47798 Krefeld (Quelle: krefeld.de Serviceportal, Standesamt.com, Stadt Krefeld direkt)
Von-der-Leyen-Platz 1 = Anschrift der Stadtverwaltung allgemein, nicht des Standesamts
Fix-Stellen: Keyfacts, Steps Pos. 3, FAQ "Wo wird beurkundet"
B2 — Urnenreihengrab-Gebühr FALSCH
v1 Tabelle: "Urnenreihengrabstätte (incl. Einfassung) 1.860,00 €"
v1 FAQ: "Urnenreihengrabstätte (20 Jahre, inkl. Einfassung) 1.860,00 €"
v1 Schema FAQ: "Urnenreihengrab 1.860 €"
Korrekt laut Satzung 2024 Pos. 2.3: 1.680,00 €
1.860 € ist die Sarg-Reihengrabstätte (Pos. 1.2), nicht die Urne
B3 — Urnenkammer-Gebühr KATASTROPHAL FALSCH
v1 Tabelle: "Urnenkammer 20 Jahre 400,00 €"
Korrekt laut Satzung 2024 Pos. 2.8: 10.170,00 € (Faktor 25!)
400 € ist die "Reihengrabstätte für Kinder bis 6 Jahre" (Pos. 1.1)
Das ist der gefährlichste Fehler: Angehörige planen mit 400 € und stehen vor 10.170 €
B4 — Sargbestattungsgebühr FALSCH zitiert
v1 Callout: "Sargbestattung 1.021 € auf dem Hauptfriedhof"
Korrekt laut Satzung Pos. 1.1: 1.283 € (Sargbestattung Erwachsene)
1.021 € ist die Gebühr für Urnen-Ausbettung+Wiederbeerdigung (Pos. IV.2.1/2.2) — völlig andere Leistung
B5 — Erdwahlgrab-Begriff irreführend
v1: "Erdwahlgrabstätte, mindestens 2 Stellen, 25 Jahre, 8.250 €"
Korrekt: Satzung Pos. 1.7 nennt "Parkgrabstätte zur Zweifachbelegung je Grabstelle 8.250 €" — d.h. pro Stelle, also bei 2 Stellen real 16.500 €
Es gibt auch Pos. 1.6: "Wahlgrabstätte zur Zweifachbelegung je Grabstelle 3.450 €" — günstigere Variante
v1 stellt die teuerste Variante als "die" Erdwahlgrab-Option dar, ohne Einfachbelegung/Zweifachbelegung-Unterscheidung; und ohne Hinweis auf "pro Stelle"
B6 — Nutzungszeit-Widerspruch im Dokument
v1 Tabelle: Reihengrab Sarg "25 Jahre"
v1 FAQ Ruhezeit: Erwachsene 25 Jahre, Urnen 20 Jahre
v1 Hero-FAQ Schema: "Ruhezeit 25 Jahre, bei Urnen ebenfalls 25 Jahre üblich"
v1 Steps: keine Angabe
Die Satzung selbst nennt explizite Nutzungsrechte: Sarg-Reihengrab keine Angabe in Pos. III.1.2 (nur Kinder: 20 J), Urnen-Reihen: nicht explizit, Kinder-Reihen: 20 J. Die Friedhofssatzung 2016 müsste hier konsultiert werden.
Action: Friedhofssatzung 27.04.2016 §§ ziehen oder die widersprüchliche Aussage rausnehmen. Schema-FAQ "Urnen 25 Jahre üblich" widerspricht der nüchternen FAQ-Antwort ("20 Jahre") — inkonsistent.
MAJOR (sollte vor Deploy fixiert werden)
M1 — "16-Meter-Kuppel" der Trauerhalle nicht quellengedeckt
v1: "Trauerhalle mit ihrer 16-Meter-Kuppel" (2x: Hauptfriedhof-Porträt, Step 5)
Quellenlage: Stadt Krefeld beschreibt: "repräsentatives, halbkreisförmiges Gebäude mit Kuppeldach"; Denkmalbehörde-PDF spricht von "Zentralbau ... Backstein-Rundbau mit Zeltdach". Keine 16-Meter-Angabe findbar.
Action: Wert streichen oder als "markante Kuppel" / "imposante Kuppelhalle" weichformulieren.
M2 — Krematorium-Datierung "1913 bis 1916" ungenau
v1: "errichtet in den Jahren 1913 bis 1916"
Korrekt laut Denkmalbehörde: Krematorium Baujahr 1914/1915 (Architekt Anton Rumpen); Stadtverordnetenbeschluss 9.11.1911; Inbetriebnahme Oktober 1915
1913–1916 ist die Bauzeit des Ensembles Trauerhalle + Leichenhalle + Krematorium (laut Stadt Krefeld); falls v1 dieses Ensemble meint, dann ok — sonst korrigieren
Action: präziser machen: "Trauerhalle, Leichenhalle und Krematorium entstanden zwischen 1913 und 1916; das Krematorium nahm im Oktober 1915 den Betrieb auf"
M3 — "Ehrengrab Feld C, Nr. 65–88" für Cornelius de Greiff
v1 nennt Position spezifisch; Wikipedia "Cornelius de Greiff" sollte vor Deploy nochmal verifiziert werden (war in Sources verlinkt — wurde nicht geprüft)
Action: vor Deploy in Wikipedia-Artikel Cornelius_de_Greiff verifizieren, sonst Felder-Nennung entfernen.
M4 — Unbelegte Wertungen / "Superlative ohne Quelle"
"übertrifft den Krefelder Stadtwald (52 ha) flächenmäßig" — Stadtwald-Fläche ungeprüft; Krefelder-entdecken.de und andere geben für Stadtwald variierende Werte (typisch ~52 ha lt. einigen Quellen, andere 60+). Quelle setzen oder Vergleich streichen.
"zu den Vorreitern Preußens" in der grünen Friedhofsgestaltung — die Stadt-Krefeld-Quelle stützt das im Kern ("zählte Krefeld zu den Vorreitern"). OK, aber präziser zitieren.
"eine der ältesten jüdischen Begräbnisstätten am Niederrhein" (Hauptfriedhof-jüdisch 1723) — möglich, aber ohne Quelle. Linn 1751 ist jünger. Klever Straße ist 17. Jh. (älter!). Aussage überprüfen oder weicher formulieren.
"Es ist einer der ältesten erhaltenen jüdischen Bestattungsplätze am unteren Niederrhein" (Linn) — ähnlich: belastbar? Klever Straße Hüls ist älter (17. Jh.).
M5 — "Streuwiesen auf dem Hauptfriedhof"
v1: "Solche Flächen existieren in Krefeld derzeit auf dem Hauptfriedhof in Form von Streuwiesen"
Quellenlage: Im Material wurde keine direkte Bestätigung gefunden, dass Krefeld eine Aschestreuwiese anbietet. KBK-Übersicht prüfen, sonst Aussage streichen oder konditional formulieren ("Erfragen Sie die Möglichkeiten bei der KBK-Friedhofsverwaltung"). Das ist ein NRW-allgemeines Recht, ob die Stadt das umsetzt, ist eine andere Frage.
M6 — "Gebührensatzung 2024" — bereits Stand 2025 verfügbar
v1: zitiert durchgehend die Fassung 2024 (5. Änderungssatzung 14.12.2023)
Realität: Es gibt bereits eine Friedhofsgebührensatzung 2025 auf der KBK-Website (gefunden im Suchergebnis)
Action: Satzung 2025 ziehen, Tabelle mit aktuellen Werten überarbeiten; sonst ist die Seite zum Launch schon veraltet.
M7 — "Bestattungspflicht (§ 8 BestG NRW)" — Paragraphen-Nummer prüfen
v1 verweist auf "§ 8 BestG NRW" für Bestattungspflicht. Im NRW-BestG ist die Bestattungspflicht in § 8 BestG NRW kodifiziert. ✅ vermutlich ok, aber im Recheck verifizieren.
"§ 4 BestG NRW" für Ruhezeiten (FAQ) — die Friedhofssatzung beruht auf § 4 BestG NRW. ✅ plausibel, aber gegen Originalgesetz checken.
"§ 13 BestG NRW" für Bestattungsfristen — korrekt zugeordnet, auch wenn die genauen Absätze (Abs. 1, 2, 3) im Original verifiziert werden sollten.
M8 — "novelliert 01.10.2014" mehrfach erwähnt — Quelle/Datum verifizieren
Wird im Body als Faktum genutzt. Das Datum könnte 1.9.2014 sein oder ein anderes Inkrafttreten. MAGS-NRW-FAQ konsultieren, ggf. exakt zitieren.
MINOR (Polish)
m1 — FAQ-Antworten teils widersprüchlich zum Body
FAQ "Welche Bestattungsfrist": Schema-Antwort sagt "10 Tage", aber im Body und Schema-FAQ ist die 6-Wochen-Frist für Asche-Beisetzung erwähnt. Konsistent.
FAQ "Wie viele Friedhöfe": Body listet 11 Friedhöfe (Hauptfriedhof, Uerdingen, Linn, Hüls + 7 weitere = 11 ✅). Aber Schema-FAQ + Body wiederholen sich; FAQ "11 städtische" steht in Konkurrenz zu "jüdischer Friedhof Am Strathhof" als zusätzlich genannter. Klarstellen: Am Strathhof ist Hülser jüdischer Friedhof, nicht "Klever Straße". → präziser: "Am Strathhof" gehört zur jüdischen Gemeinde, nicht zum KBK-Verbund. OK so, aber: JG Krefeld nennt 5 jüdische Friedhöfe — eine kurze Erwähnung der jüdischen Gemeinde-Friedhöfe würde Vollständigkeit erhöhen.
m2 — Schema.org Inkonsistenz
Zeitstempel datePublished = dateModified = "2026-05-12" → für eine neue Seite ok
Im FAQ-Schema steht "Ruhezeit von 25 Jahren, bei Urnenbestattungen sind ebenfalls 25 Jahre üblich" — widerspricht dem Body-FAQ ("20 Jahre"). HARTER Inkonsistenz-Trigger im JSON-LD.
m3 — Cornelius de Greiff Lebensdaten
v1: "1781–1863" — Wikipedia bestätigt das.
Aber: "Reichsfinanzminister 1848/49" für Hermann von Beckerath — kurz verifizieren, das stimmt aber laut historischer Literatur (kurze Amtszeit in der Frankfurter Reichsregierung).
m4 — "FC Uerdingen 05" → "Bayer 05 Uerdingen" / "KFC Uerdingen 05"
v1 schreibt "FC Uerdingen 05 (gegründet 1905, zeitgleich mit dem Friedhof)" — der Verein heißt heute KFC Uerdingen 05, gegründet 1905. Die Aussage "Gründungsmitglieder hier bestattet" — unbelegt, Spekulation. Streichen oder belegen.
m5 — Dujardin Weinbrennerei
"Verbindungen zur Weinbrennerei Dujardin" — Uerdingen, ok. Aber wiederum unbelegt, ob Familienmitglieder auf dem Uerdinger Friedhof liegen. Konditional formulieren ("vermutlich" / "wahrscheinlich" / im Quellenverzeichnis belegen).
m6 — "Architekt Dahmen" / "Gartenbauinspektor Rocholl" Hüls
v1: "geplant vom Architekten Dahmen, gärtnerisch gestaltet vom Gartenbauinspektor Rocholl"
Action: prüfen — ich konnte das im Material nicht direkt verifizieren; bei aufmerksamen Lesern in Hüls problematisch, wenn falsch.
m7 — "Schluff" Strecke Sankt Tönis zum Hülser Berg
Der Schluff fährt heute Krefeld – Hülser Berg (vom Bahnhof Krefeld-Nord, nicht Sankt Tönis). Historisch ging die Strecke teilweise weiter. Prüfen / korrigieren.
m8 — Uerdinger Linie / "Hüls ek"
Die Uerdinger Linie ist eine maken-machen Sprachgrenze, nicht ek/ich. Die ek/ich-Grenze ist die Benrather Linie. v1 vermischt das. Klassischer linguistischer Fehler. Streichen oder korrekt formulieren ("Hüls liegt im niederfränkischen Sprachraum nördlich der Uerdinger Linie ...").
m9 — Sozialbestattung § 74 SGB XII Adresse
"Fachbereich Soziales, Wirtschaft und Gesundheit, Konrad-Adenauer-Platz 17" — Anschrift im Recheck verifizieren.
m10 — DIN EN 15017
Korrekter Verweis. ✅
Aber: "TÜV Rheinland" als Prüfer — verifizieren; manche Quellen nennen verschiedene Zertifizierer. Markenzeichen ist eine Kollektivmarke; die Audits werden BDB-organisiert. Präziser formulieren.
m11 — Memoriam-Garten seit 2016
✅ Stadt Krefeld bestätigt das. Aber: "gemeinsame Anlage mit Stelen, Mauerarrangements und Rasenflächen" — das Bild stimmt.
m12 — Trauerhalle Verberg
v1 listet "Kapellen auf den Friedhöfen Uerdingen, Fischeln, Linn und weiteren Standorten." Die Satzung Pos. II.4 nennt Trauerhalle Verberg mit speziellem Tarif (94 €) — also gibt es eine Verberger Trauerhalle. Erwähnung möglich, aber kein Blocker.
m13 — Markenzeichen Nummer 39614008
"Kollektivmarke unter der Nummer 39614008 beim Deutschen Patent- und Markenamt" — Nummer verifizieren (DPMA-Register).
STRUKTUR / SEO / FORM (positiv)
✅ Schema.org @graph mit WebPage, Article, BreadcrumbList, City, mehreren Place, Organization, FAQPage — vollständig
✅ Wortzahl ~2.300 (im Korridor 1700-2400)
✅ Klares H1/H2/H3-Schema, Hero, Keyfacts, Tabelle, Steps, FAQ, Quellen, Footer
✅ Mobile-responsive CSS
✅ Breadcrumb-Schema korrekt
✅ Canonical-Tag gesetzt
✅ Quellenverzeichnis mit 15 Belegen, viele Primärquellen
✅ Hidden Gems sind erzählerisch stark (Fahrstuhl-Krematorium, Schluff-Akustik, Sprachgrenze, Uerdinger Sonderweg)
✅ Tonalität sachlich-würdevoll, keine kommerzielle Anbiederung
⚠️ FAQ-Inkonsistenz im Schema.org-Block (Ruhezeit) → muss synchron zum Body-FAQ sein
FIX-PRIORITÄTSREIHENFOLGE
Sofort (Blocker): B1 (Standesamt-Adresse), B2 (Urnenreihen 1.680 €), B3 (Urnenkammer 10.170 €), B4 (Sargbestattung 1.283 €), B5 (Erdwahlgrab-Tabelle differenzieren), B6 (Ruhezeit-Konsistenz Schema vs. Body)
Vor Deploy (Major): M1 (16m-Kuppel raus), M2 (Krematoriumsdaten), M4 (Superlative entschärfen), M5 (Streuwiesen verifizieren), M6 (auf Satzung 2025 ziehen)
Polish: m4 (KFC Uerdingen), m6 (Hüls-Architekten), m7 (Schluff-Strecke), m8 (Uerdinger Linie ≠ ek/ich), m13 (Markenzeichen-Nummer)
EMPFEHLUNG FÜR CHAT A (V2)
Tabelle komplett neu aus Original-PDF Gebührensatzung 2024 (oder besser 2025) übernehmen, per Copy-Paste verifizieren
Standesamt: ein einziges Mal Adresse zentral als Variable definieren ("Standesamt Krefeld, Rheinstr. 138, 47798 Krefeld"), dann an alle 3 Stellen einsetzen
Schema.org FAQ-Block aus dem Body-FAQ generieren (DRY-Prinzip), keine doppelte Wahrheitsquelle
Alle "ältesten / größten / ersten" Superlative gegen Quelle prüfen, sonst entschärfen
Uerdinger Linie / Benrather Linie linguistisch differenzieren oder Absatz streichen

Bei v2 ohne diese Fixes: Score bleibt unter 75. Mit allen Blocker + M-Fixes: 87-92 erreichbar.

Dein Nutzungsguthaben ist aufgebraucht. Kaufe mehr, um jetzt weiterzumachen, oder warte bis Donnerstag um 14:00, wenn sich deine Plan-Nutzung zurücksetzt.
Mehr kaufen




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
 Claude is active in this tab group  
Open chat
 
Dismiss