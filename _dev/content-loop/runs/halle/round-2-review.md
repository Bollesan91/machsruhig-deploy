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
Halle review und bewertung
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
Kassel-Review nach SCORE-Tabelle
Kassel-Review nach SCORE-Tabelle
Oldenburg-Review nach SCORE-Tabelle
Lübeck-Review nach SCORE-Tabelle
Rostock-Review nach SCORE-Tabelle
Friedhöfe und Gebührensatzung in Kassel
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
Halle review und bewertung
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/halle/v1-from-chat-A.html

Stadt: Halle (Saale, ST). Review SCORE 0-100% + Fix-Liste.

19:55
Claude hat geantwortet: Ich lese die v1 und prüfe sie.

Ich lese die v1 und prüfe sie.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/halle/v1-from-chat-A.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/halle/v1-from-chat-A.html

Ich prüfe jetzt die kritischen Faktenbehauptungen gegen Primärquellen. Die wichtigsten Verifikationspunkte: Anzahl Friedhöfe (14?), Gertraudenfriedhof-Maße & Geschichte, Südfriedhof-Daten, Stadtgottesacker (Datum 1557, 94 Schwibbögen), Halle-Neustadt-Friedhof, Gebührensatzung 2016 mit den genannten Beträgen, Standesamt-Öffnungszeiten.

Searching the web
Web durchsucht

Wichtiger Fund: Es gibt eine 3. Änderungssatzung vom 26.11.2022 der Gebührensatzung. Die im Artikel angegebenen Gebühren (643 €, 616 €, 609 €) stammen vermutlich aus der alten Fassung 2016 und sind nicht mehr aktuell. Außerdem fehlt Wörmlitz in der Liste der Friedhöfe — die v1 listet "Radewell" und ich sehe Wörmlitz separat. Ich prüfe die aktuelle Gebührensatzung und die Friedhofsliste.

Fetching site
Web durchsucht

Wichtige Erkenntnisse so weit:

Es gibt eine 3. Änderungssatzung vom 26.11.2022 — die Beträge im Artikel sind aus 2016/2019 und veraltet
Ferdinand Fair nennt 2010er-Stand-Beträge, die fast identisch zu den 2016ern sind (617€/608€) — aber die 2022er-Werte sind unklar
Es gibt offenbar einen Friedhof Wörmlitz, der in v1 nicht aufgeführt ist; v1 listet stattdessen "Radewell" — möglicherweise sind das beide separat (oder Radewell heißt offiziell "Radewell & Osendorf")

Ich prüfe Stadtgottesacker-Datierung, Gertraudenfriedhof-Details, Telefonnummer Standesamt:

Searching the web
Web durchsucht

Sehr wichtige Korrekturen für den Stadtgottesacker:

Weihe 1529 ist im Hero-Teil "Geweiht 1529" — aber v1 hat in der Meta-Box "Geweiht 1529, Arkaden 1557–1594" ✓ akzeptabel, allerdings nennt eine Quelle 1557–1590 (nicht 1594). Wikipedia: "1594 entstand der letzte der 94 Bögen" — passt also zu 1557–1594.
31. März 1945 → 31 Bögen zerstört: v1 sagt "31 Grabbögen und der Torturm" — Wikipedia / Heute-macht-der-Himmel-blau sagen 26 Bögen zerstört. → Faktenfehler!
Stifterin "Dr. Marianne Witte 1991": Wikipedia und Friedhofskultur-Halle: "ab 1998 ermöglichte … eine großzügige Privatspende … fast originalgetreue Rekonstruktion" / Lebenshimmel: "Durch die 1997 erfolgte großzügige Stiftung". 1991 ist falsch — "Bauhütte Stadtgottesacker" wurde 1990 eingetragen, die Stifterin wirkte erst ab 1997/1998. → Faktenfehler bzgl. Jahr.
Restaurierung "abgeschlossen 2003": Eine Quelle nennt "Sommer 2007 zum 450. Jahrestag des Baubeginns" als Datum, an dem die Schwibbögen erstmals wieder geschlossen präsentiert wurden. 2003 ist die Gedenktafel-Enthüllung — nicht der Abschluss. → Mögliche Ungenauigkeit / unscharf.
"darunter Marcus Golter, Martin Roedel und Bernd Göbel": Bernd Göbel schuf die Gedenktafel für die Spenderin, nicht die Reliefs der Bögen primär. → Nicht eindeutig falsch, aber unscharf.

Ich prüfe weiter — Gertraudenfriedhof Größe, Wilhelm Jost, Torgau-Urnen, Südfriedhof:

Web durchsucht
Web durchsucht

Sehr wichtige Funde zum Gertraudenfriedhof:

Bauzeit: v1 sagt "1912–1914 unter Leitung Wilhelm Jost" — Friedhofskultur sagt "zwischen 1913 und 1916". Wikipedia/DeWiki: "1912 bis 1914". → Uneinheitlich, aber v1 hat eine zulässige Variante. Erweiterung bis 1916 ist nicht direkt belegt.
Münchner Friedhöfe von Hans Grässel: v1 behauptet, Jost habe sich an Hans Grässel orientiert. → Nicht belegt in der gefundenen Quellenlage. Quelle muss geprüft werden.
"Erste Bestattung am 12.9.1914": v1 OK ✓
Krematorium "1991/92 neu errichtet": v1 sagt "auf dem Friedhofsgelände steht zudem das 1991/92 neu errichtete Krematorium". → Wikipedia sagt das ORIGINAL-Krematorium war von Anfang an dabei (erste Einäscherung 1915). Es gibt Bezeichnungen "Flamarium" für die heutige Anlage des Gemeinnützigen Feuerbestattungsvereins. Datum 1991/92 nicht belegt; ist möglicherweise eine Neueinrichtung/Umnutzung — UNSICHER.
Torgau-Häftlinge: v1 sagt "Anordnung des Ministeriums des Innern", "Urnen ab Juni 1950 verdeckt am Kopfende vorhandener Gräber im Feld 39" — Volksbund: "Gräberfeld 39, Urnen an den Kopfenden bereits vorhandener Gräber". → Bestätigt. "Juni 1950" — nicht direkt belegt, aber Zeitraum 1950-1953 stimmt.
"117 Fälle keine Angehörigen": Volksbund bestätigt 117 ✓
Krystyna Wituska: Diese polnische Widerstandskämpferin — muss verifiziert werden. Sie wurde in Halle hingerichtet 1944, könnte stimmen.
Friedrich August Weineck "Der kleine Trompeter": Verifiziert? Ist der wirklich auf dem Gertraudenfriedhof? Sollte geprüft werden.
Größenangabe v1: "ca. 37 ha (ursprünglich), 47 ha nach Erweiterungen": Die Quellen sind hier widersprüchlich — halle365 sagt 47 ha nach Erweiterung. Wikipedia und Find-a-Grave sagen 37 ha. v1's Formulierung ist eine zulässige Synthese, allerdings ist die "ursprünglich"-Klassifikation der 37 ha ungewöhnlich.

Wichtige Verifikation — Südfriedhof Halle:

Web durchsucht
Web durchsucht

Südfriedhof-Daten sind sehr gut belegt. Eine kleine Anmerkung: v1 sagt "italienische Neo-Renaissance" — die Quellen sagen "italienische Renaissance" (ohne Neo). Aber das ist marginal.

Wichtig: Wikipedia Südfriedhof-Koordinaten: 51.4624 / 11.9761 — v1-Schema sagt 51.466 / 11.962 → Koordinaten verschoben, klein aber falsch.

Ich prüfe noch Standesamt-Daten, BestattG LSA § 17 + § 15 + Halle-Neustadt:

Web durchsucht
Web durchsucht

§ 17 BestattG LSA: vollständig korrekt zitiert ✓ — die Zitate in v1 stimmen.

Wichtig: § 15 BestattG LSA — v1 sagt "§ 15 Abs. 1 BestattG LSA werden Leichen in Särgen bestattet". Die echte Formulierung: "Leichen werden in Särgen, Asche wird in Urnen auf Friedhöfen bestattet". Das ist im FAQ und Recht-Abschnitt korrekt.

Aber ein konkreter Faktencheck-Fehler: v1 nennt im FAQ "Sachsen-Anhalt gehört neben Bayern und Sachsen zu den wenigen Bundesländern, die bislang keine Ausnahme von der Sargpflicht für muslimische Bestattungen … zulassen." Das muss verifiziert werden — denn in den letzten Jahren haben sich die Regelungen mehrfach geändert (NRW, BaWü, etc. haben Ausnahmen, andere haben sie inzwischen auch). Risiko: veraltete Behauptung.

Web durchsucht
Web durchsucht

Wichtiger Befund: Rheinland-Pfalz hat im Oktober 2025 die Sargpflicht aufgehoben! v1's Behauptung "Sachsen-Anhalt gehört neben Bayern und Sachsen zu den wenigen Bundesländern" — RP hat sich verabschiedet. Aktuell sind es Bayern, Sachsen, Sachsen-Anhalt (3 Länder, nicht 4). Außerdem: Die Quellenlage zeigt, dass Bremen ebenfalls eine Sargpflicht hatte, aber Bremen erlaubt Ausnahmen. Die Behauptung im FAQ ist nicht ganz falsch, aber ungenau und potentiell veraltend — denn die Reformdebatte ist im Fluss.

Jetzt noch Standesamt-Daten checken:

Web durchsucht
Web durchsucht

Wichtige Standesamt-Korrektur:

v1 sagt "Telefonisch unter +49 345 2214623" — aktuelle offizielle Quellen sagen: +49 345 2210 (Hauptnummer) und 0345 221-4623 (Servicehotline). v1's Nummer ist also als Servicehotline korrekt, aber nicht die einzige.
v1 sagt "Abgabe von Sterbefallanzeigen ist dienstags und donnerstags ohne Termin möglich" und nennt "Di 09:00–12:00 und 13:00–16:00, Do 09:00–12:00 und 13:00–15:00" → bestätigt durch buerger.sachsen-anhalt.de.
Sterbeurkunden-Preis: v1 sagt im FAQ "Eine Sterbeurkunde kostet 10 €". Das ist tatsächlich der bundesweit übliche Preis, aber muss konkret für Halle nicht 10 € sein — UNGESICHERT.

Jetzt prüfe ich noch Halle-Neustadt-Friedhof:

Web durchsucht
Web durchsucht

Halle-Neustadt-Friedhof — gut belegt. v1 ist hier weitgehend korrekt. Kleine Korrektur: v1 sagt "der Untergrund besteht in weiten Teilen aus Muschelkalk, der einst direkt nebenan im Steinbruch abgebaut wurde". Diese spezifische Behauptung "Muschelkalk + Steinbruch nebenan" ist nicht direkt aus den Quellen belegt — Quellen sprechen nur von "relativ großen Höhenunterschieden und Bodenverhältnissen". UNGESICHERT/SPEKULATIV.

Nun habe ich genug Material. Eine letzte Prüfung — Nordfriedhof: v1 sagt "Nordfriedhof (ab 1850, ca. 14 ha, 12.000 Grabstätten — die zweitälteste Anlage)". Quellen oben bestätigen: 14 ha, 12.000 Grabstätten, ab 1850 ✓.

Aber: Eine Quelle sagt "1851 eröffnet" (siehe Heute-macht-der-Himmel-blau und Wikipedia Südfriedhof). v1 sagt 1850. Differenz: Baubeginn vs. Eröffnung. Akzeptabel.

Nordfriedhof-Adresse: v1 sagt nicht die Adresse, aber Friedhofskultur sagt "Am Wasserturm 12". v1 hat Nordfriedhof in der Liste, aber ohne Adresse — keine direkte Falschangabe.

Jetzt schreibe ich den vollständigen Review.

REVIEW v1 — Halle (Saale)

SCORE: 76 / 100

Solides Fundament, gute Struktur, korrekt zitierte Rechtsnormen (§ 17 BestattG LSA verbatim ✓). Aber: mehrere Faktenfehler bei den Friedhofs-Hidden-Gem-Geschichten, veraltete Gebührenangaben (Stand 2016 statt aktuelle 3. Änderungssatzung 26.11.2022) und eine unvollständige Friedhofsliste (Friedhof Wörmlitz fehlt). Damit ist die Honesty-Schwelle noch nicht erreicht, Audit-Score ≥85 nicht erfüllt.

BLOCKER (must-fix vor go-live)
B1. Gebührensatzung-Stand veraltet (kritisch)
v1 sagt: "Maßgeblich ist die Satzung, die der Stadtrat am 16.12.2015 beschlossen hat und die seit dem 01.01.2016 in Kraft ist"
Realität: Es gibt drei Änderungssatzungen: 25.05.2016, 30.10.2019, 26.11.2022 (veröffentlicht im Amtsblatt 18.11.2022). Aktuelle Lesefassung liegt vor.
Die Beträge 643 €, 616 €, 609 €, 618 €, 610 €, 456 € stammen aus dem 2016er Anlage und sind höchstwahrscheinlich nicht mehr aktuell.
Fix: Aktuelle Lesefassung der Gebührensatzung 2022 fetchen und Tabelle ersetzen. Falls Werte nicht eindeutig verifizierbar → Tabelle entfernen, durch Spannenangabe ersetzen, klar auf "Lesefassung 26.11.2022" verweisen mit Disclaimer "zum jeweils gültigen Stand siehe Satzung". Quelle: SR_708-23_3_Lesefassung_Friedhofsgebuehrensatzung.pdf.
B2. Friedhofsliste unvollständig — Wörmlitz fehlt
v1 nennt 14 Friedhöfe, aber listet konkret nur 13: Gertrauden, Süd, Nord, Stadtgottesacker, Halle-Neustadt, Ammendorf, Büschdorf, Diemitz, Dölau, Giebichenstein, Kröllwitz, Lettin, Radewell, Seeben = 14 (mit Stadtgottesacker als 4. Hauptanlage). Aber: Verein für Friedhofskultur listet Wörmlitz (Anglerstraße 2) als kommunalen Friedhof. Gleichzeitig listet halle-entdecken.de 10 Stadtteilfriedhöfe ohne Wörmlitz. Halle.de selbst nennt nur 14 ohne vollständige Auflistung.
Fix: Über halle.de/leben-in-halle/.../friedhofslexikon/ die vollständige offizielle 14er-Liste verifizieren. Wenn Wörmlitz dazugehört: aufnehmen. Wenn nicht: Quellen-Diskrepanz akzeptieren und die offizielle Stadt-Liste verwenden.
B3. Stadtgottesacker — falsche Zerstörungszahl 1945
v1 sagt: "Nach Bombenabwürfen am 31. März 1945 wurden 31 Grabbögen und der Torturm zerstört oder schwer beschädigt"
Realität: Wikipedia, Heute-macht-der-Himmel-blau, Lebenshimmel und mehrere weitere Quellen: 26 Bögen zerstört. Die Zahl 31 ist nirgends belegbar.
Fix: "26 Bögen wurden bei Bombenangriffen, besonders am 31. März 1945, zerstört" — Torturm: nicht aus den Quellen direkt belegt, Formulierung anpassen.
B4. Stadtgottesacker — falsche Jahreszahl Stiftung Witte
v1 sagt: "Erst eine private Stifterin, Dr. Marianne Witte, ermöglichte 1991 mit umfangreichen Mitteln die Gründung der Stiftung Stadtgottesacker und damit die Restaurierung, die 2003 abgeschlossen wurde."
Realität:
Bauhütte Stadtgottesacker e.V. → eingetragen 1. März 1990 (nicht 1991, und nicht durch Witte)
Witte-Spende → 1997/1998 (nicht 1991)
Schwibbögen geschlossen wieder präsentiert → Sommer 2007 zum 450. Jahrestag (nicht 2003; 2003 war die Gedenktafel-Enthüllung)
Fix: Klare Trennung: "Die 1990 gegründete Bauhütte Stadtgottesacker e.V. und ab 1997/1998 eine großzügige Stiftung von Dr. Marianne Witte (Tochter des Nobelpreisträgers Karl Ziegler) ermöglichten die umfassende Rekonstruktion; zum 450. Jahrestag des Baubeginns 2007 wurden die Schwibbögen wieder geschlossen präsentiert."
B5. Sargpflicht-FAQ veraltet
v1 FAQ: "Sachsen-Anhalt gehört neben Bayern und Sachsen zu den wenigen Bundesländern, die bislang keine Ausnahme von der Sargpflicht für muslimische Bestattungen … zulassen"
Realität (Stand Mai 2026): Rheinland-Pfalz hat im Oktober 2025 die Sargpflicht aufgehoben. Aktuell: Bayern, Sachsen, Sachsen-Anhalt (3 Länder, nicht 4 wie vorher). v1's Aussage ist faktisch korrekt — aber im Recht-Abschnitt steht "Anders als in den meisten anderen Bundesländern" — das ist OK. Aber die FAQ-Liste muss bei nächster Reform (Sachsen-Anhalt-CDU blockiert aktuell) wieder geprüft werden.
Fix: Einfügen "(Stand 2026)" beim Sargpflicht-Punkt. Formulierung verfeinern: "Sachsen-Anhalt gehört zu den wenigen Bundesländern (mit Bayern und Sachsen, Stand 2026), die bislang …". Reform-Hinweis: "Die CDU-Fraktion in Sachsen-Anhalt hat eine Reform bislang blockiert."
MAJOR (sollte vor go-live gefixt werden)
M1. Gertraudenfriedhof — unbelegte "Hans Grässel"-Anspielung
v1: "Jost legte die Wegeführung betont regelmäßig und geradlinig an, in Anlehnung an die Münchner Friedhöfe von Hans Grässel."
Keine der gefundenen Quellen (Friedhofskultur-Halle, Wikipedia, halle365) erwähnt Grässel als Vorbild für Jost. Friedhofskultur sagt nur: "Heimat- und Denkmalschutzbewegung" prägte Jost.
Fix: Anspielung streichen oder Quelle ergänzen. Konservativ: "Jost legte die Wegeführung betont regelmäßig und geradlinig an — typisch für die Friedhofsarchitektur seiner Generation."
M2. Gertraudenfriedhof — Krematorium "1991/92 neu errichtet"
v1: "Auf dem Friedhofsgelände steht zudem das 1991/92 neu errichtete Krematorium, das heute vom Gemeinnützigen Feuerbestattungsverein Halle als Flamarium betrieben wird."
Realität: Wikipedia/halle365: Erste Einäscherung 23.12.1915 (Krematorium war von Anfang an Teil der Anlage). Der Gemeinnützige Feuerbestattungsverein wurde 1990 wieder gegründet. Die Behauptung "1991/92 neu errichtet" ist nicht belegt — es war eher eine Übernahme/Neuausstattung als Neubau.
Fix: "Das Krematorium auf dem Gelände wird heute vom 1990 wiedergegründeten Gemeinnützigen Feuerbestattungsverein Halle e.V. als Flamarium betrieben." Konkretes Datum 1991/92 streichen.
M3. Gertraudenfriedhof — Fläche unscharf formuliert
v1: "ca. 37 ha (ursprünglich), 47 ha nach Erweiterungen"
Realität: Wikipedia, Find-a-Grave, Friedhofskultur: durchweg 37 ha. halle365: "47 ha (nach Erweiterung)". Die Quellenlage ist hier widersprüchlich. Die ursprüngliche Größe als "37 ha" zu klassifizieren und 47 ha als "nach Erweiterungen" wird durch keine Quelle direkt gestützt — könnte aber zutreffen.
Fix: "ca. 37 ha" als Standardangabe nehmen (mehrere belastbare Quellen), 47 ha-Hinweis streichen oder klar als alternative Quellenangabe markieren.
M4. Torgau-Urnen — Datierungspräzision "ab Juni 1950"
v1: "Er ließ die Urnen ab Juni 1950 verdeckt am Kopfende vorhandener Gräber im Feld 39 versenken"
Quellen: Volksbund/Friedhofskultur sprechen vom Zeitraum 1950–1953 insgesamt. "Juni 1950" als Startdatum ist nicht direkt belegt.
Fix: "Er ließ die Urnen zwischen 1950 und 1953 verdeckt am Kopfende vorhandener Gräber im Feld 39 versenken …"
M5. Halle-Neustadt — Muschelkalk-Behauptung unbelegt
v1: "der Untergrund besteht in weiten Teilen aus Muschelkalk, der einst direkt nebenan im Steinbruch abgebaut wurde"
Quellen (Wikipedia, hallelexikon) sprechen nur von "Höhenunterschieden und Bodenverhältnissen" — keine Quelle bestätigt "Muschelkalk + nebengelegener Steinbruch".
Fix: Generische Formulierung: "Aufgrund der erheblichen Höhenunterschiede und der schwierigen Bodenverhältnisse eignet sich fast die Hälfte der Fläche ausschließlich für Urnenbeisetzungen."
M6. Südfriedhof — Koordinaten falsch im Schema.org
v1 JSON-LD: "geo": { "latitude": 51.466, "longitude": 11.962 }
Realität (Wikipedia/Kulturfalter): 51.4624 / 11.9761
Fix: Koordinaten korrigieren auf 51.4624 / 11.9761.
M7. Standesamt-Telefonnummer
v1 nennt mehrfach "+49 345 2214623" als Hauptnummer
Realität: Hauptnummer ist +49 345 2210 (laut halle.de). 0345 221-4623 ist Servicetelefon-Direktwahl.
Fix: Beide Nummern unterscheiden: "Servicetelefon des Standesamts: +49 345 221-4623; allgemeine Standesamts-Hotline: +49 345 2210."
M8. Standesamt-Öffnungszeiten — fehlt: "Mo + Do mit Termin"
v1 sagt: "Die Abgabe von Sterbefallanzeigen ist dienstags und donnerstags ohne Termin möglich." ✓ korrekt
Aber Wochenstruktur unklar dargestellt — Mittwochs und Freitags ist das Standesamt geschlossen, das fehlt. Montags ist nur 9-12 Uhr mit Termin.
Fix: Vollständige Wochenstruktur ergänzen oder Hinweis "Mittwoch und Freitag geschlossen, Termine nur Mo/Di/Do".
MINOR (Politur)
N1. Stadtgottesacker-Datierung Meta-Box
v1: "Eröffnung: Geweiht 1529, Arkaden 1557–1594"
Lebenshimmel sagt "1557 bis 1590" (Bauzeit Arkaden). Wikipedia: "1594 entstand der letzte der 94 Bögen". Beide Datierungen kursieren.
Fix: Beibehalten "1557–1594" mit Verweis auf "über dreißigjährige Bauzeit", oder vorsichtiger: "1557 bis Ende des 16. Jh.".
N2. Stadtgottesacker — Maße "113 × 123 × 129 × 150 m"
Diese spezifischen Maße kommen in keiner der gefundenen Quellen vor. Möglicherweise aus älterer Literatur. UNGESICHERT.
Fix: Maße entfernen, falls keine belastbare Quelle verfügbar.
N3. Südfriedhof — "Neo-Renaissance" vs. "Renaissance"
v1: "Die Ziegelbauten am Eingangsbereich folgen Formen der italienischen Neo-Renaissance"
Quellen sagen einheitlich "italienischen Renaissance" (Friedhofskultur, Wikipedia).
Fix: "Neo-" streichen → "italienische Renaissance" (das ist gemeint, denn es ist ein Bau des späten 19. Jh., der Renaissance-Formen zitiert, also stilistisch Neo-Renaissance — aber die Quellen formulieren es ohne "Neo").
N4. Sterbeurkunden-Preis "10 €" im FAQ
v1: "Eine Sterbeurkunde kostet 10 €, weitere Ausfertigungen ebenfalls je 10 €."
Bundesweit üblich, aber für Halle nicht direkt aus einer Stadt-Halle-Quelle belegt.
Fix: Mit Hinweis "(Stand 2026, siehe Gebührenverzeichnis der Stadt)" oder Preis streichen, falls nicht belastbar verifizierbar.
N5. Reform-Sargpflicht Tonalität
v1 Recht-Abschnitt: "eine in der bundesweiten Reformdebatte regelmäßig diskutierte Besonderheit"
Akzeptable Formulierung, aber: aktueller Reform-Stand in Sachsen-Anhalt (CDU blockiert) könnte einfließen, um Sachverhalt zu schärfen.
N6. Friedrich August Weineck "Der kleine Trompeter"
Verifikation nicht möglich in dieser Review-Runde. Falls Quelle dafür vorhanden, OK. Falls nicht: streichen.
N7. Krystyna Wituska
Polnische Widerstandskämpferin, 1944 in Halle hingerichtet — sehr plausibel, dass auf Gertraudenfriedhof beigesetzt (679 Hingerichtete dort). Aber nicht direkt durch eine Quelle belegt.
Fix: Beibehalten, da plausibel und in Gedenkanlage-Kontext passend. Optional kurze Quellenangabe ergänzen.
N8. "Architekt und Stadtbaurat" Jost
v1 Prominente-Liste: "Wilhelm Jost (Architekt und Stadtbaurat, 1874–1944)" ✓
Sterbedatum: Quellen sagen 6. Juni 1944 in Lohdorf bei Hohensalza. Akzeptabel.
N9. Gertraudenfriedhof — Bauzeit
v1: "Errichtet wurde er zwischen 1912 und 1914" / "Bauzeit 1912–1914, Erweiterung bis 1916"
Friedhofskultur sagt: "Erbaut wurde der Gertraudenfriedhof zwischen 1913 und 1916". Wikipedia: "1912 bis 1914". Beide Angaben kursieren.
Fix: "1912/13–1914" beibehalten, "Erweiterung bis 1916" ggf. nur erwähnen, wenn belastbar belegbar.
N10. "UNSURE"-Kommentar im HTML
Im Kosten-Abschnitt steht <!-- UNSURE: Aktuelle Anpassungen der Gebühren nach 2016 ggf. veröffentlicht; hier nur 2016er Stand belegt -->
Klares Selbst-Eingeständnis von Chat A — das ist exakt der B1-Blocker. Muss bereinigt sein.
POSITIVES (was gut ist, beibehalten)
✓ Saubere HTML-Struktur, vollständiges Schema.org-Markup (Article + BreadcrumbList + WebPage + City + Place ×4 + Organization + FAQPage)
✓ § 17 BestattG LSA exakt zitiert (Abs. 1, 2, 4)
✓ § 15 Abs. 1 BestattG LSA korrekt
✓ § 16 Abs. 2 BestattG LSA korrekt (Wille des Verstorbenen)
✓ § 24 Abs. 1 BestattG LSA korrekt (Umbettungen)
✓ Erste Bestattung Gertraudenfriedhof 12.09.1914 + französischer Kriegsgefangener ✓
✓ Stadtgottesacker: 94 Schwibbögen, Nickel Hoffmann, Camposanto-Vorbild ✓
✓ Südfriedhof: 11.12.1887, Oberbürgermeister Gustav Staude, Lohausen, Bucher, 216.675 Mark 78 Pfennig ✓ (alles 1:1 belegt)
✓ 117 Urnen ohne Angehörige (Torgau-Geschichte) ✓
✓ Adresse Abteilung Friedhöfe Liebenauer Straße 118 ✓
✓ Friedhof Halle-Neustadt: Teutschenthaler Landstraße 16, 11 ha, 7.500 Grabstellen, 1965 Umbettung Passendorf ✓
✓ Sprechzeiten Friedhofsverwaltung Di + Do korrekt
✓ Verweis auf Bundesland-Übersicht (Sachsen-Anhalt) korrekt platziert
✓ Quellen-Apparat vollständig und mit Primärlinks (halle.de, landesrecht-sachsen-anhalt.de)
SCORE-Aufschlüsselung
Kategorie	Punkte	Maximal
Rechtliche Fakten (BestattG LSA)	14	15
Friedhofs-Fakten (Daten, Namen)	11	20
Gebühren / Aktualität	4	10
Behördenwege (Standesamt, Friedhofsamt)	8	10
Vollständigkeit (alle 14 Friedhöfe)	7	10
Hidden-Gems mit Quellenbelegen	6	10
Schema.org / Tech	9	10
Sprache, Lesefluss, Struktur	9	10
Quellenapparat	8	5 (+3)
Summe	76	100
EMPFOHLENE WORKFLOW-ENTSCHEIDUNG

NICHT GO-LIVE READY. Zielwert ≥85 nach Recheck.

Reihenfolge der Fixes:

B1 Gebührensatzung aktualisieren (höchstes Risiko: Faktenfehler bei Geldbeträgen)
B3, B4 Stadtgottesacker-Geschichte korrigieren
B2 Friedhofsliste vervollständigen (Wörmlitz prüfen)
B5 Sargpflicht-FAQ mit "Stand 2026"
M-Punkte abarbeiten
bundesland-recheck.py laufen lassen (besonders Wrong-City-Check für Sachsen-Anhalt-Orte, Unsourced-Superlativ-Check, Template-Error-Check)
Re-Audit; bei ≥85 + Recheck=0 Blocker → Chat A v2

Was an v1 wirklich stark ist: die FAQ-Struktur, die Schema.org-Vollständigkeit und die durchweg saubere §-Zitierung. Mit korrigierten Faktenfehlern und aktualisierter Gebührensatzung wird das eine sehr starke Seite.

Dein Nutzungsguthaben ist aufgebraucht. Kaufe mehr, um jetzt weiterzumachen, oder warte bis Donnerstag um 14:00, wenn sich deine Plan-Nutzung zurücksetzt.
Mehr kaufen




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen