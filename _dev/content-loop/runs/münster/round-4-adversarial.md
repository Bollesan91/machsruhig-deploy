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
Überprüfung von Halluzinationen in Münster-Inhalten
Karlsruhe-Inhalte nach SCORE-Kriterien reviewen
Mannheim-Content Review nach SCORE-Kriterien
HTML-Seite für Bestatter Mannheim erstellen
HTML-Seite für Bestatter in Karlsruhe
HTML-Seite für Bestatter in Münster erstellen
Machsruhig.de Münster Review und Scoring
HTML-Seite für Bestatter in Düsseldorf erstellen
HTML-Seite für Bestatter in Bonn erstellen
HTML-Seite für Bestatter Stuttgart erstellen
Adversarial Review für machsruhig.de Stuttgart
HTML-Seite für Bestatter in Bonn erstellen
HTML-Seite für Bestatter Bielefeld erstellen
HTML-Seite für Bestatter Wuppertal erstellen
HTML-Seite für Bestatter in Bochum erstellen
HTML-Seite für Bestatter in Duisburg erstellen
HTML-Seite für Bestatter Nürnberg erstellen
HTML-Seite für Bestatter Hannover erstellen
HTML-Seite für Bestatter Dresden erstellen
HTML-Seite für Bestatter Bremen erstellen
HTML-Seite für Bestatter Essen erstellen
HTML-Seite für Bestatter in Dortmund erstellen
HTML-Seite für Bestatter Leipzig erstellen
HTML-Page Review für Stuttgart
Machsruhig.de Düsseldorf-Seite reviewen
Machsleicht project setup and priority planning
Admin-Rechte für Microsoft-365-App-Freigaben
Adversarial review für machsruhig.de Köln
HTML-Page für Bestatter Berlin erstellen
HTML-Seite für Bestatter Frankfurt erstellen
💬 Beschreib mir mal den Batch ur…
HTML-Seite für Bestatter Köln erstellen
HTML-Page für Bestatter Hamburg erstellen
Alle Chats
B
Bolle
Max Plan
Überprüfung von Halluzinationen in Münster-Inhalten
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat C (Adversarial Reviewer).

Du bist Chat C (Adversarial Reviewer). Lies das Briefing: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md und dann die zu pruefende v2: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/m%C3%BCnster/v2-from-chat-A.html

Stadt: Muenster (NRW). Suche aktiv nach Halluzinationen: erfundene Paragraphen, Copy-Paste-Quellenschwindel (z.B. NRW-fremde Quellen), falsche Zahlen, Schein-Praezision. Liste jeden Verdacht mit Zitat + Begruendung. Vergib am Ende ADVERSARIAL-SCORE 0-100% und gib konkrete Fixes fuer v3 als Bullet-Liste.

10:42
Claude hat geantwortet: Ich lese erst das Briefing und dann die v2.

Ich lese erst das Briefing und dann die v2.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md

Briefing verstanden. Jetzt die v2.

Web durchsucht
Web durchsucht

BRIEFING_OK.

Jetzt feindlich lesen. Mindset: die Page ist unter 85. Mindestens 3 Schwächen. Ich gehe gezielt auf Halluzinationen, Paragraphen-Sachfehler und Schein-Präzision.

Verdachtsfälle, die ich konkret prüfe:

§ 13 BestG NRW — "Bestattungsfristen" und § 15 BestG NRW — "Feuerbestattung". Im NRW-BestG sind die Fristen tatsächlich nicht in § 13 geregelt (das ist in mehreren anderen Bundesländern so, z. B. Niedersachsen). In NRW stehen die Bestattungsfristen in § 13 Abs. 3 BestG NRW für Erdbestattung — aber Vorsicht: viele Sekundärquellen verwechseln das mit § 14 (Feuerbestattung) oder § 15. Das ist klassisches "Bundesland-fremde-Quelle-Copy-Paste"-Risiko. Auch die "10-Tage-Frist" ist falsch: in NRW gilt für die Bestattung eine Frist von spätestens am achten Tag nach Eintritt des Todes (§ 13 Abs. 3 BestG NRW). Die Page behauptet "innerhalb von zehn Tagen … (Höchstfrist seit der Novelle 2014, zuvor acht Tage)" — das ist genau die Falschdarstellung, die entsteht, wenn man § 16 BestG Niedersachsen oder § 20 BestG Hessen abschreibt.
"§ 8 BestG NRW — Bestattungspflicht … Rangfolge" — die Bestattungspflicht in NRW ist tatsächlich in § 8 BestG NRW geregelt, das stimmt. Aber: die Rangfolge in der Page ("Ehegatten, Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkel") muss mit § 8 Abs. 1 abgeglichen werden — die Reihenfolge in NRW lautet tatsächlich anders, Enkel kommen vor Geschwistern in einigen Versionen.
"§ 9 BestG NRW — Leichenschau" — die Leichenschau ist in NRW in § 9 BestG NRW geregelt, das stimmt grundsätzlich.
"§ 12 BestG NRW" für Bestattungsverfügung/Wille — das ist verdächtig. § 12 BestG NRW regelt soweit ich weiß nicht den "erkennbaren Willen" zur Bestattung.
"§ 4 BestG NRW i. V. m. … § 7 Abs. 2 BestG NRW (Wahrung des religiösen Empfindens)" — extrem spezifisch, klingt erfunden.
"Friedhofsgebührensatzung Stand 2025: Wahlgrab 1.812 €" — sehr präzise Zahl. Muss verifiziert werden.
"Einwohner: 320.728 (31.12.2025)" — Münster hatte zum 31.12.2023 ca. 320.000 Einwohner. 320.728 zum 31.12.2025 ist plausibel, aber die Zitat-URL "newsdetail/zahl-der-gemeldeten-personen-sinkt" klingt nach erfundener Slug.
"34,1 Prozent der Bevölkerung sind zwischen 20 und 39 Jahre alt" — Schein-Präzision ohne Quellen-Verortung.
"Münster Heath War Cemetery … 740 Gräbern britischer Soldaten" — Münster Heath ist tatsächlich ein CWGC-Friedhof, aber er liegt in Heek oder Telgte/Lauheide? Verdächtig — die Zahl 740 ist konkret prüfbar.
"Deutsche Ehrenfriedhof mit 894 Gräbern (darunter 40 Kinder und 215 zivile Bombenopfer der Luftangriffe vom Oktober 1943 und September 1944)" — extreme Schein-Präzision.
"Hilger Hertel der Ältere (1830–1890), seit 1857 Dombaumeister von Münster" — Hertel war tatsächlich Münsteraner Dombaumeister, aber Lebensdaten und "1857" prüfen.
"574 Kriegsgräber … 1.284 münsterschen Bombenopfer" — Schein-Präzision.
"120 Sprengtrichter, alle Mausoleen zerstört" — sehr spezifisch.
"140 Pflanzenarten" kartiert, "100 Vogelarten — davon 47 regelmäßig brütend" — Schein-Präzision.
"1929 für 250.000 Reichsmark ein 104 Hektar großes Gelände" — sehr präzise Zahl.
Wahlgrab "in besonderer Lage" 2.280 € — diese Kategorie existiert auf Lauheide womöglich gar nicht.
"Schöner Friedhof Deutschlands 2014 / Bestattungen-Award" — ich kenne keinen prominenten "Bestattungen-Award 2014" für schönsten Friedhof. Lauheide hat tatsächlich Auszeichnungen, aber die Aussage "vom Bestattungen-Award" und "prominent besetzte Jury" wirkt vage.

Lass mich die kritischsten Punkte aktiv prüfen.

Web durchsucht
Web durchsucht

Sehr wichtiger Befund: § 13 BestG NRW und die 10-Tage-Frist sind korrekt zitiert. Die 24-Stunden-Mindestfrist und die 10-Tage-Höchstfrist (geändert 2014) stimmen. § 14 ist Erdbestattung, § 15 ist Feuerbestattung. Auch der § 7 Abs. 2 BestG NRW (religiöses Empfinden) ist real und passt.

ABER: Die Page schreibt "§ 13 BestG NRW … die Bestattungsfristen" und konkret "Erdbestattung innerhalb von zehn Tagen, Einäscherung ebenfalls binnen zehn Tagen" — das stimmt. Auch "§ 15 BestG NRW Feuerbestattung" stimmt. Hier kein Haupt-Fehler.

Aber: Die Page nennt "§ 8 BestG NRW — Bestattungspflicht … Ehegatten, Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern und volljährige Enkelkinder". Lass mich die tatsächliche Rangfolge in § 8 BestG NRW prüfen.

Web durchsucht
Web durchsucht

§ 8 BestG NRW ist KORREKT zitiert. Die Rangfolge passt exakt. Auch § 13 BestG NRW (24h Mindestfrist, 10 Tage Höchstfrist, 6 Wochen Asche-Beisetzungsfrist) ist korrekt. Auch § 7 Abs. 2 (religiöses Empfinden) und § 4 (Satzungen) sind real und passend zitiert. Das ist juristisch sauber.

Jetzt prüfe ich die historisch-faktischen Schein-Präzisionen, denn DA habe ich den größten Hallu-Verdacht.

Web durchsucht
Web durchsucht

Sehr aufschlussreich. Jetzt habe ich klare Befunde:

Stadt Münster sagt: 82 Hektar. Wikipedia sagt: 84 Hektar. Die Page nimmt 84 — das ist die Wikipedia-Zahl, nicht die Primärquelle. Diskrepanz Primärquelle vs. Sekundärquelle.
Offizielle Eröffnung: Wikipedia sagt klar 10. Oktober 1943 (nicht 1942!). Die Page schreibt: "10. Oktober 1942". Die Stadt Münster sagt "im Oktober 1942 … erster städtischer Friedhof" — möglicherweise ist da etwas verwirrend. Aber Wikipedia ist eindeutig: 10. Oktober 1943. Das ist ein konkreter Faktenfehler in der Page.
"1929 für 250.000 Reichsmark ein 104 Hektar großes Gelände von der Stadt Telgte" — diese präzise Zahl finde ich in keiner Quelle. Wikipedia sagt nichts von 250.000 RM oder 104 ha. Schein-Präzision / mögliche Halluzination.
"Carl Ludwig Schreiber, der ab 1938 das Konzept entwickelte" — Wikipedia bestätigt das. OK.
"100 Vogelarten — davon 47 regelmäßig brütend" — Wikipedia bestätigt das. OK.
"740 Gräber englischer Soldaten" und "894 Gräber, 40 Kinder, 215 zivile Bombenopfer" — Wikipedia bestätigt das. OK.
Award: "Bestattungen.de-Award" — die Page sagt "Bestattungen-Award" (kürzt das ".de" weg). Akzeptabel.
"prominent besetzte Jury" — Wikipedia/Westfalenspiegel sagt "Jury um den früheren Erzbischof Robert Zollitsch". Die Page sagt nur "prominent besetzte Jury" — vage, aber nicht erfunden. Es ist ein Online-Portal-Award, nicht ein offizieller Branchen-Award — die Page verschleiert das durch "prominent besetzte Jury", was sich besser anhört. Aufgewertet/etwas geschönt.

Lass mich noch die Münster Heath War Cemetery und die 1929-Geländekauf-Zahl checken.

Web durchsucht
Web durchsucht

Sehr aufschlussreich! Mehrere klare Befunde:

Wichtig: Stadt-Münster-Primärquelle sagt "Munster Heath Cemetery contains 589 Commonwealth burials of the Second World War. There are also 277 post-war graves." → das macht insgesamt 866, aber davon nur 589 WK2. Die Wikipedia-Zahl "740 Gräber englischer Soldaten" stimmt nicht mit der Primärquelle der Stadt überein! Die Page hat von Wikipedia abgeschrieben statt von der Primärquelle.

Weiter: Die Primärquelle der Stadt sagt eindeutig "894 graves in eight fields (labeled A to H) in the so-called German cemetery" und "More than half of the war graves belong to civilians who died in air raids" — also "mehr als die Hälfte" zivile Opfer, NICHT die Zahlen "40 Kinder und 215 zivile Bombenopfer" wie auf Wikipedia.

Ganz wichtig: Die "250.000 Reichsmark" und "104 Hektar" und "Bauerschaft Verth" sind also tatsächlich in Wikipedia belegt — kein Hallu. Aber: "Hügelgräber aus der Zeit zwischen 2.000 und 1.500 vor Christus" in der Page schreibt "2.000 und 1.500 vor Christus", Wikipedia sagt "2000 bis 1500 Jahre vor Christus". Stimmt im Kern.

Eröffnungsdatum bestätigt: 10. Oktober 1943, NICHT 1942! Die Page schreibt: "Die offizielle Eröffnung erfolgte mitten im Zweiten Weltkrieg am 10. Oktober 1942" — das ist ein klarer Fehler. Wikipedia und mehrere andere Quellen bestätigen 10. Oktober 1943. Auch das Schema.org der Page sagt "1942" konsistent — der Fehler zieht sich durch.

Aber moment, die Stadt Münster sagt im O-Ton selbst auf der Friedhofs-Seite: "Eröffnet im Oktober 1942". Es gibt also Quellen-Konflikt zwischen Stadt (1942) und Wikipedia (10. Oktober 1943). Die Page wählt die Primärquelle 1942 — das ist eigentlich richtig, aber die Page schiebt das präzise Datum "10. Oktober" drüber, das von Wikipedia kommt und dort mit Jahr 1943 verbunden ist. Das ist eine inkonsistente Mischung von Quellen. Verdächtig.

Jetzt noch die letzten kritischen Punkte: Gebühren und Bevölkerung.

Web durchsucht
Web durchsucht

Krasser Fund: Die Stadt-Münster-Primärquelle sagt "Gebühren je Grabstelle und 30 Jahre Nutzungszeit: 1.812 Euro" und Wahlgrab in besonderer Lage: 2.274 Euro (nicht 2.280 Euro wie in der Page!). Die Page hat 2.280 € statt 2.274 €. Allerdings stand 2.280 € in der Bestatter-Sekundärquelle (Haubrich) — die Page hat damit die Sekundärquelle übernommen und nicht die Primärquelle (Stadt Münster).

Also: 1.812 € stimmt mit Primärquelle. 2.280 € ist ein Bestatter-Stand (Haubrich), Primärquelle Stadt sagt 2.274 €. Außerdem: Landschaftsgrab mit 30 m² fehlt in der Gebührentabelle, aber wird im Text genannt — geringer Mangel.

Wichtig nicht erwähnt: Die Page nennt 2.274 € (Landschaftsgrab) nicht — das wäre noch eine relevante Position.

Ich habe jetzt genug. Drei substantielle Schwächen finde ich klar. Zentralfriedhof und Bevölkerungszahl sind noch potentielle vierte/fünfte Schwächen, aber das Briefing verlangt drei substantielle Schwächen. Ich konzentriere mich.

Bisherige Hauptbefunde sortiert nach Schwere:

HALLU/FALSCH-DATUM: Page sagt "offizielle Eröffnung … am 10. Oktober 1942" — Wikipedia: 10. Oktober 1943. Mehrere Quellen bestätigen 1943. Stadt-Friedhofsseite sagt nur unspezifisch "Oktober 1942 … erster städtischer Friedhof" (möglicherweise das Datum, an dem der Friedhof betriebsbereit war / erste Gräber). Das präzise Datum "10. Oktober" ist gekoppelt an 1943 in den belegten Quellen. Faktenfehler.
COPY-PASTE-ZAHLEN aus Sekundärquelle ohne Primärquellen-Abgleich: "Wahlgrab in besonderer Lage 2.280 €" — Stadt Münster sagt aktuell 2.274 € auf ihrer Primär-Seite. Die Page zitiert sich auf die "Friedhofsgebührensatzung Stadt Münster (Stand 2025)" als Quelle — aber die genannte Zahl entspricht nicht der Primärquelle. Außerdem: Bestatter-Sekundärquelle Haubrich nennt 1.830 € statt 1.812 € für Wahlgrab — die Page hat sich entschieden für die Stadt-Primärseite-Variante 1.812, aber für 2.280 die Bestatterseite, Quellen-Mix.
MÜNSTER HEATH WAR CEMETERY — falsche Gräberzahl: Die Page schreibt "740 Gräber britischer Soldaten" (übernommen von Wikipedia). Die Primärquelle Stadt Münster (Stadtarchiv-Seite) sagt aber: "Munster Heath Cemetery contains 589 Commonwealth burials of the Second World War. There are also 277 post-war graves." = 589 WK2 + 277 Nachkriegs. Die Page hat die Wikipedia-Zahl 740 übernommen, die nicht mit der Primärquelle der Stadt übereinstimmt. Auch falsch in der Page: "britischer Soldaten" — die CWGC pflegt Commonwealth, nicht nur britische Gräber (Kanada, Australien etc.). Und die Charakterisierung "die Anfang 1945 bei den Kämpfen im Münsterland ihr Leben verloren" stammt direkt aus Wikipedia — die Stadt-Primärquelle sagt aber sehr deutlich: "the majority of those buried in the cemetery died while serving with the Army of Occupation after the German surrender" — also gerade NICHT im Kampf, sondern nach Kapitulation. Inhaltlicher Widerspruch zur Primärquelle.
Deutscher Ehrenfriedhof — "215 zivile Bombenopfer": Die Stadt-Primärquelle sagt: "More than half of the war graves belong to civilians who died in air raids" (also >447 von 894). Die "215 erwachsene Bürger + 40 Kinder = 255 zivile Opfer" stammt aus Wikipedia und passt zur Stadt-Quelle "mehr als die Hälfte" eher schlecht. Die Page übernimmt blind Wikipedia. Sekundärfehler.
§ 12 BestG NRW und der "erkennbare Wille": Die Page schreibt: "Das BestG NRW (§ 12) und die Hinterbliebenen sind an einen erkennbaren Willen gebunden." § 12 BestG NRW heißt aber "Bestattungsentscheidung" und regelt die Art der Bestattung (Erdbestattung/Feuerbestattung). Der "Wille des Verstorbenen" ist in § 12 mit erfasst, aber das Zitat "an einen erkennbaren Willen gebunden" ist eine inhaltliche Verkürzung, die suggeriert, § 12 wäre eine spezifische Bindungsnorm. Eher mild, aber: "Das BestG NRW (§ 12) und die Hinterbliebenen sind an einen erkennbaren Willen gebunden" ist grammatikalisch außerdem unklar. Eher Stil als Hallu.
Hügelgräber "2.000 und 1.500 vor Christus": OK belegt.
"34,1 Prozent der Bevölkerung sind zwischen 20 und 39 Jahre alt" — Schein-Präzision ohne explizite Quellen-Verortung im Text. Nicht überprüfbar in dem Maße.

Ich habe drei klare, substantielle Schwächen. Format strikt einhalten.

BRIEFING_OK (vorweg zur Bestätigung).

Adversarial Review — Münster v2

SCHWÄCHE 1: Sektion "Waldfriedhof Lauheide", 1. Absatz — Faktenfehler beim Eröffnungsdatum — Die Page schreibt wörtlich: "Die offizielle Eröffnung erfolgte mitten im Zweiten Weltkrieg am 10. Oktober 1942" (und konsistent dazu im Schema.org: "Waldfriedhof Lauheide … 1942 eröffnet" und im Lead: „Waldfriedhof Lauheide (1942, 84 ha)"). Wikipedia und sämtliche belastbaren Quellen nennen den 10. Oktober 1943 als offizielles Eröffnungsdatum. Die Stadt-Münster-Friedhofsseite ist hier mehrdeutig ("Eröffnet im Oktober 1942, war er der erste städtische Friedhof"), aber das präzise Tagesdatum 10. Oktober hängt in den Quellen am Jahr 1943. Die Page hat hier zwei Quellen unsauber zusammengezogen: die Stadt-Vagheit "Oktober 1942" plus den Wikipedia-Tag "10. Oktober" — und produziert daraus ein nicht belegtes Datum. Da der Fehler sich durch Lead, Hauptsektion, Schema.org und FAQ zieht, ist es kein Tippfehler, sondern eine durchgehende Falschangabe. Fix: Datum auf den belegten Stand korrigieren — entweder "offizielle Eröffnung am 10. Oktober 1943" (mit Wikipedia + Westfalenspiegel als Beleg) oder bei Beibehaltung der Stadt-Primärquelle nur "Eröffnung im Oktober 1942" ohne Tagesdatum. Alle vier Vorkommen (Lead, Hauptabsatz, Schema.org, FAQ) müssen synchron geändert werden.

SCHWÄCHE 2: Sektion "Waldfriedhof Lauheide", 3. Absatz — Inhaltlich falsche Charakterisierung des Münster Heath War Cemetery, Wikipedia-Zahl gegen Primärquelle übernommen — Die Page schreibt: „der ‚Englische Friedhof' (Münster Heath War Cemetery) mit 740 Gräbern britischer Soldaten unter Verwaltung der Commonwealth War Graves Commission" — und der Kontext im Text suggeriert Kampfopfer im Münsterland (die Quelle Wikipedia formuliert: "Anfang 1945 bei den Kämpfen im Münsterland"). Die Primärquelle Stadt Münster / Stadtarchiv sagt aber dezidiert anderes: 589 Commonwealth-Bestattungen aus WK2 plus 277 Nachkriegsgräber (= insgesamt 866, nicht 740), und ausdrücklich: "the majority of those buried in the cemetery died while serving with the Army of Occupation after the German surrender" — Mehrheit also Besatzungsarmee-Tote nach Kapitulation, nicht Kampftote. Zweitens: „britische Soldaten" ist sachlich falsch — die CWGC pflegt Commonwealth-Gräber (also auch Kanadier, Australier, Inder, Neuseeländer). Die Page hat hier Wikipedia 1:1 übernommen, obwohl die Stadt Münster eine widersprechende Primärquelle online stellt (stadt-muenster.de/kriegerdenkmale/information-in-english/lauheide), die nicht zitiert wird — und das, obwohl die Quellenliste die nahe verwandte URL stadt-muenster.de/kriegerdenkmale/kriegsgraeberstaetten/kriegsgraeber-zentralfriedhof enthält. Klassischer Wikipedia-Übernahme-Fehler ohne Primärquellen-Abgleich, genau das Anti-Pattern, das der Audit fangen soll. Fix: Zahl korrigieren auf "589 Commonwealth-Bestattungen aus dem Zweiten Weltkrieg sowie 277 Nachkriegsgräber" (mit Stadtarchiv-Primärquelle), "britischer" durch "Commonwealth" ersetzen, Kontext-Aussage zu "Kämpfen im Münsterland" entweder streichen oder qualifizieren ("ein Teil starb in den Kämpfen im Münsterland Anfang 1945, die Mehrheit jedoch erst nach der Kapitulation im Dienst der Besatzungsarmee"). Primärquelle der Stadt in die Quellenliste aufnehmen.

SCHWÄCHE 3: Sektion "Bestattungskosten in Münster", erste Gebührentabelle — Schein-Präzision durch Mix aus Primär- und Sekundärquellen, davon eine falsch — Die Tabelle führt unter "Quelle: Friedhofsverwaltung Stadt Münster, Friedhofsgebührensatzung (Stand 2025)" auf: Wahlgrab 1.812 €, Wahlgrab in besonderer Lage 2.280 €, Urnenwahlgrab 1.350 €, Urnenreihengrab 637 €. Tatsächliche Primärquelle Stadt Münster (stadt-muenster.de/gruen/friedhoefe): Wahlgrab 1.812 € (korrekt), Wahlgrab in besonderer Lage 2.274 € (NICHT 2.280 €), Urnenreihengrab 637 € (korrekt), Landschaftsgrab 2.274 €. Die "2.280 €" stammen sichtbar aus einer Bestatter-Sekundärseite (Bestattungen Haubrich, die parallel 1.830 € für das normale Wahlgrab nennt — die Page hat sich dort selektiv bedient: 1.812 € von der Stadt, 2.280 € von Haubrich). Das ist Quellen-Mix unter einheitlich behaupteter Quelle "Friedhofsverwaltung Stadt Münster" — die Tabellen-Quellenangabe ist also irreführend. Zusätzlich: Die Gebühr für Urnenwahlgrab (1.350 €) und das Landschaftsgrab (Page-Text behauptet "30 m² Umpflanzungsfläche") sind in der Tabelle nicht primärquellengeprüft bzw. fehlen ganz. Der "Stand 2025" ist außerdem nicht hinterlegt — die jüngste belegbare Änderungssatzung ist die 4. Änderungssatzung vom 16.12.2023 (Amtsblatt 2024). Fix: 2.280 € → 2.274 € korrigieren; Landschaftsgrab 2.274 € als eigene Zeile ergänzen (Text spricht davon, Tabelle führt es nicht); Urnenwahlgrab-Wert von der Stadt-Seite gegenprüfen statt nur aus dem FAQ wiederholen; den Stand-Vermerk "Stand 2025" durch das belegte Datum der jüngsten Änderungssatzung ersetzen ("Stand: 4. Änderungssatzung vom 16.12.2023, gültig ab 2024"); Tabellen-Quelle präzisieren ("Stadt Münster, stadt-muenster.de/gruen/friedhoefe, abgerufen 12.05.2026") statt der vagen Berufung auf "Friedhofsgebührensatzung".

EHRLICHE %-ZAHL: 73 %

ADVERSARIAL-SCORE: 73 %

(Begründung in Stichworten, zusätzlich zum strikten Format: drei substantielle, jeweils durch Primärquellen belegbare Schwächen — ein klarer Faktenfehler beim Eröffnungsdatum, eine durch Wikipedia statt Stadt-Primärquelle entstandene inhaltliche Falschdarstellung beim CWGC-Friedhof, ein Quellen-Mix in der Gebührentabelle unter falscher Quellenattribution. Sprache, Schema.org, Wortzahl, Cross-Links und §-Zitate aus dem BestG NRW sind dagegen sauber.)

Konkrete Fixes für v3 (Bullet-Liste für Chat A)
Eröffnungsdatum Lauheide synchron korrigieren (4 Stellen): Lead, Hauptabsatz, Schema.org description, FAQ-Antwort — entweder durchgehend 10. Oktober 1943 (mit Wikipedia + Westfalenspiegel als Quellen-Beleg) oder bei Beibehaltung der Stadt-Münster-Primärquelle ohne Tagesdatum: Eröffnung im Oktober 1942. Mischform aktuell nicht belegt.
Münster Heath War Cemetery: Zahlen + Charakterisierung neu schreiben auf Basis von stadt-muenster.de/kriegerdenkmale/information-in-english/lauheide (Stadt-Primärquelle): „589 Commonwealth-Bestattungen aus dem Zweiten Weltkrieg sowie 277 Nachkriegsgräber"; „britische Soldaten" → „Commonwealth-Soldaten"; Kontext-Aussage zu Kampfopfern qualifizieren (Mehrheit Besatzungsarmee-Tote nach Kapitulation, nicht Kampftote).
Deutscher Ehrenfriedhof: Opferzahlen ebenfalls primärquellengestützt formulieren — Stadt-Münster-Primärquelle sagt „more than half … civilians" (>447 von 894), nicht „215 zivile Bombenopfer + 40 Kinder" (Wikipedia-Zahl, im Konflikt mit der Stadt-Aussage). Entweder Wikipedia-Zahlen mit explizitem Wikipedia-Beleg auszeichnen oder auf Stadt-Aussage umstellen.
Stadt-Münster-Primärquelle zu Kriegsgräbern Lauheide in die Quellenliste aufnehmen: stadt-muenster.de/kriegerdenkmale/information-in-english/lauheide (englische Seite; ggf. deutsche Variante recherchieren).
Gebührentabelle Stadt Münster: 2.280 € → 2.274 € (Stadt-Primärquelle); Landschaftsgrab Lauheide als eigene Zeile aufnehmen (2.274 €, 30 m² Umpflanzungsfläche); Baumurnengrab (1.626 €) ergänzen, weil im Text-Sortiment „Urnenwurzelgrab" angesprochen wird; Tabellen-Caption: Stand 2025 ersetzen durch belegte Fassung („4. Änderungssatzung vom 16.12.2023, gültig ab 2024"); Tabellen-Quelle präziser referenzieren mit URL und Abrufdatum.
Flächenangabe Lauheide klären: Page sagt durchgehend 84 ha (Wikipedia), Stadt-Münster-Friedhofsseite und Westfalenspiegel sagen 82 ha. Inkonsistenz: entweder primärquellenkonform 82 ha oder Wikipedia-Stand 84 ha mit explizitem Hinweis auf abweichende Angabe der Stadt.
Award-Charakterisierung präzisieren: „prominent besetzte Jury beim Bestattungen-Award" ist geschönt — Beleg-Quellen nennen konkret: Bestattungen.de-Award 2014, Jury um Robert Zollitsch (früherer Erzbischof). Faktentreu wäre eine knappe Nennung des Veranstalters (Online-Vergleichsportal Bestattungen.de) und des Jury-Vorsitzes, statt der vagen Aufwertung.
§ 12 BestG NRW-Halbsatz reformulieren: „Das BestG NRW (§ 12) und die Hinterbliebenen sind an einen erkennbaren Willen gebunden" ist grammatikalisch wackelig (Subjekt-Mismatch) und sachlich verkürzt — § 12 regelt die Bestattungsentscheidung. Sauber: „Für Art und Ort der Bestattung ist nach § 12 BestG NRW der Wille der verstorbenen Person maßgeblich; ersatzweise entscheiden die Hinterbliebenen in der Rangfolge des § 8 BestG NRW."
Quellen-Mix in der Gebührentabelle markieren: Wenn beide Träger getrennt aufgeführt werden, jeweils mit eigenständiger Quellenangabe und Abrufdatum — nicht gemeinsam unter „Friedhofsverwaltung Stadt Münster" subsumieren.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
 Claude is active in this tab group  
Open chat
 
Dismiss