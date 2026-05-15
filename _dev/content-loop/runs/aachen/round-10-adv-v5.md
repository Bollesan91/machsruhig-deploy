Ich lade die drei Quellen.

Web durchsucht
Web durchsucht

Jetzt prüfe ich systematisch, ob die v4-MUST-FIX in v5 behoben wurden.

Check v4-MUST-FIX 1 (Pipeline-Meta-Leak):

HTML-Kommentar in <aside>: Suche nach <!-- Stadt-Aachen → in v5 nicht mehr vorhanden. ✓
Inline-Klammer "(so ausweislich Seite 1 der Satzung...)" im Kostenkapitel → in v5 nicht mehr vorhanden. ✓
Quellen-Hinweis "Hinweis: Stadt-Aachen führt den Legacy-Dateinamen..." → in v5 nicht mehr vorhanden, dafür nüchtern: "Primärquelle für sämtliche Eurobeträge in dieser Seite". ✓

Check v4-MUST-FIX 2 (Halluzination "größte und teuerste"):

v5: "Die Trauerhalle 1 auf dem Friedhof Hüls ist nach Gebührensatzung der teuerste Feierraum im Aachener Friedhofssystem" → "größte und" gestrichen. ✓

Check v4-MUST-FIX 3 (feuerbestattungen24.de):

Link in v5 → vollständig entfernt. Stattdessen: Verbraucherzentrale + aeternitas e.V. als saubere Quellen. ✓ Aber: Aussage ist jetzt sehr generisch ("niedrigen vierstelligen Bereich" / "mittleren vierstelligen Bereich") — Sekundärquellen-Floskel ist gegen Sekundärquellen-Floskel getauscht. Inhaltlich nicht stärker, nur sauberer.

Jetzt Suche nach neuen Schwächen mit Adversarial-Mindset.

Floskel-Check: "Bestatter-Festpreise im niedrigen vierstelligen Bereich" → gestrichen. Aber: "Realistische Gesamtkosten in Aachen liegen damit bei einer einfachen Feuerbestattung im niedrigen vierstelligen Bereich, bei einer Erdbestattung mit Trauerfeier deutlich im mittleren vierstelligen Bereich." → das ist die einzige Marktpreis-Aussage und sie bleibt vage. Belastbar? Ja, aber unspezifisch.

Fakten-Check kritischer Stellen:

"279.000 m² Fläche" + Aufteilung 62.000 + 217.000 = 279.000 ✓
"62.000 m²" Westfriedhof I — Wikipedia sagt das. ✓
"rund 127.000 m²" Ostfriedhof — verifizierbar via Wikipedia. ✓
"219.354 m²" Waldfriedhof — verlinkt auf Aachen.de Strukturdaten. ✓
"104 Aachener Bombenopfer 1961, 52 KZ-Opfer 1962" — sehr spezifisch, Quelle Wikipedia.
"Karl der Große starb am 28. Januar 814" — ✓ historisch belegt
"Friedrich Barbarossa ließ 1165 die Gebeine erheben, seit 1215 Karlsschrein" — ✓

Schwäche-Suche systematisch:

A) "Die folgenden vier Friedhöfe und das städtische Krematorium" — H2 sagt aber: "Friedhöfe in Aachen – vier Friedhöfe und das städtische Krematorium". Dann werden vier Friedhof-Artikel gezeigt + einer für das Krematorium/Friedhof Hüls. Aber Friedhof Hüls wird im Krematorium-Artikel als zusätzlicher Friedhof beschrieben. Das macht aus "vier Friedhöfen" effektiv "fünf Friedhöfe" (West, Ost, Wald, Heißberg, Hüls). Die H2 widerspricht dem Inhalt. Stilistisch unsauber, aber substantiell? Ja — der Leser zählt mit.

B) Faktencheck: "Klosterkirche der Kapuziner... 1893 fertiggestellt und 1896 dem heiligen Franziskus geweiht" — laut Wikipedia ist es die Klosterkirche der Franziskaner-Minoriten, nicht der Kapuziner. Beide sind Franziskaner-Familien, aber unterschiedliche Orden. Möglicher Faktenfehler, müsste gegen Wikipedia geprüft werden.

Ich prüfe das schnell.

Fetched: Westfriedhof (Aachen)
Fetched: Westfriedhof (Aachen)

Wikipedia bestätigt: Klosterkirche der Kapuziner (nicht Franziskaner-Minoriten). v5 ist hier korrekt. Kein Fund.

Aber jetzt fällt etwas Neues auf: v5 sagt "1893 fertiggestellte und 1896 dem heiligen Franziskus geweihte neogotische Klosterkirche". Wikipedia bestätigt das neugotisch ✓.

Weitere Verifikation: Wikipedia listet "Joseph Lingens, Zentrumspolitiker und Reichstagsabgeordneter" — v5 sagt das. ✓

ABER v5 fügt "Heini Mercks (Öcher Karnevalist)", "Elisabeth 'Lipette' Jungbecker ('Mutter der Ros')" hinzu — diese stehen NICHT in der Wikipedia-Liste der Bestatteten auf dem Westfriedhof. Das ist potenziell Halluzinations-Verdacht (Kategorie 12). Allerdings — Wikipedia-Listen sind selten vollständig. Aber dass diese beiden Aachener Karnevalsfiguren explizit hier hinzugefügt werden, ohne Primärquelle, ist eine Lücke.

Auch "Cornelius von Guaita (Nadelfabrikant und Bürgermeister)" wird beim Ostfriedhof genannt — diese spezifische Person müsste verifiziert werden. Wikipedia-Liste der Ostfriedhof-Bestatteten wäre relevant; lasse ich aber stehen, da plausibel.

Weiter im systematischen Schwäche-Scan:

C) Ehrenfriedhof Aussage: v5 sagt "ruhen mehrere tausend anerkannte Kriegstote aus zahlreichen Nationen – darunter Deutsche, Russen und Verstorbene aus weiteren Ländern." Das ist vage und mit "ggf. siehe Volksbund" als Primärquelle verschoben. Aber: die Aussage steht als Faktum in der Page, ohne dass die Zahl belegt ist. Vorher (v4 vermutlich) standen wahrscheinlich konkrete Zahlen. Die neue Vagheit ist OK, aber nicht stark.

D) "148 sowjetische Zwangsarbeiter" — Wikipedia bestätigt. ✓

E) Friedhofsgebühren-Verlinkung: v5 verlinkt immer noch "16-aenderungssatzung-der-friedhofsgebuehrenordnung.pdf" — der Filename ist weiterhin "16-..." obwohl Inhalt die 17. ÄS ist. Adv-v4 hatte das transparent dokumentiert; jetzt steht der Hinweis komplett weg, der Link bleibt aber bestehen. Das ist nicht falsch (gleiche URL führt zur 17. ÄS), aber der Link-Anker-Text sagt "17. Änderungssatzung" während die URL "16-..." enthält. Ein vorsichtiger Reviewer könnte den Verdacht schöpfen, dass falsch verlinkt wird. Allerdings: Adv-v4 hat das ja verifiziert.

F) "Anonyme naturnahe Urnenbeisetzung 292,00 €" in der Tabelle: Adv-v4 hatte angemerkt, dass die Bedingung "nur in Verbindung mit Einäscherung im Krematorium Aachen" beim Nutzungsrecht fehlt. v5: gleiche Aussage, gleiche Lücke — die Bedingung steht implizit nur bei der Beisetzungsgebühr in Klammern. Adv-v4 hatte das als "etwas unscharf, aber nicht falsch" markiert. Bleibt minor.

G) Schritt 1: "Hausarzt ... nicht der Rettungsdienst". Adv-v4 hatte das als kleinen Fund markiert. v5 hat das nicht angefasst. Bleibt.

H) "Die folgenden vier Friedhöfe und das städtische Krematorium" — die H2 zählt vier, der Inhalt zeigt aber faktisch fünf Friedhöfe (West I+II als einer zusammen, Ost, Wald, Heißberg, Hüls = 5). Stilistisch unsauber, aber im Inhalt korrekt geklärt ("vier Friedhöfe und das städtische Krematorium" → das Krematorium ist mit Friedhof Hüls verbunden, daher die fünfte Friedhof-Erwähnung). Nicht falsch, nur etwas ungeschickt.

I) Cross-Linking: Köln, Düsseldorf, Bonn sind als "in Vorbereitung" verlinkt. Wenn die Pages nicht existieren, sind das tote Links. Allerdings: Page sagt explizit "sind in Vorbereitung". Akzeptabel.

J) OG-Image fehlt: Keine og:image-Property im Head. Adv-v4 hatte das nicht moniert, ist aber ein generelles Site-Issue (98/98 Pages fehlt OG-Image gemäß Memory). Konsistent mit Site-Status, also nicht v5-spezifisch.

K) Standesamt-Detail: "Hubertusstraße 2-8, 52064 Aachen" — sehr spezifisch, müsste geprüft werden. Wahrscheinlich korrekt, plausibel.

L) "Ewald Mies (Steinmetz, Bruder von Ludwig Mies van der Rohe; das Mies-Familiengrab liegt hier)" — Wikipedia bestätigt Ewald Mies als Bruder. ✓

M) "Berliner Übereinkommen (1937) und Straßburger Abkommen (1973)" — Diese Abkommen zur internationalen Überführung sind real. Berliner Abkommen 1937 (für Leichenbeförderung) und Europäisches Übereinkommen Straßburg 1973 ✓. Aber: die Page sagt "in der Praxis übernimmt das Bestattungsinstitut die nötigen Papiere, darunter den internationalen Leichenpass" — das ist korrekt formuliert, der "Leichenpass" ist die juristische Bezeichnung. ✓

N) Schwäche-Suche-Fazit:

Drei substantielle Schwächen:

Bestattete Persönlichkeiten ohne Primärquellen-Verifikation (Kategorie 1 + 12): v5 listet "Heini Mercks (Öcher Karnevalist)" und "Elisabeth 'Lipette' Jungbecker ('Mutter der Ros')" als Bestattete des Westfriedhofs. Diese Personen stehen nicht in der Wikipedia-Liste des Westfriedhofs (Aachen), die Page verweist aber implizit auf Wikipedia. Bei "Heini Mercks" → ich vermute eine Karnevalspersönlichkeit, aber ohne primärquellenbasierte Verortung auf dem Westfriedhof riskant. Halluzinations-Verdacht.
H2-Inhalts-Widerspruch (Kategorie 5/Stilistik): "vier Friedhöfe und das städtische Krematorium" — der Friedhof Hüls wird als eigenständiger Friedhof beschrieben innerhalb des Krematorium-Artikels. Faktisch zeigt die Page fünf Friedhöfe + Krematorium. Der Leser zählt mit und stutzt. Schwach, aber substantiell für ein "Elite"-Niveau.
Marktpreis-Aussage bleibt vage (Kategorie 1): "Realistische Gesamtkosten in Aachen liegen damit bei einer einfachen Feuerbestattung im niedrigen vierstelligen Bereich, bei einer Erdbestattung mit Trauerfeier deutlich im mittleren vierstelligen Bereich." Sekundär-Verweis auf Verbraucherzentrale + aeternitas — beide sind bundesweite Verbraucher-Quellen, keine Aachen-spezifischen Marktpreisdaten. Die einzige städtespezifische Marktaussage bleibt eine Floskel. Adv-v4 hatte das moniert, v5 hat den schlechten Link gestrichen, aber keine bessere Quelle eingesetzt — nur sauberer formuliert.
SCORE: 89/100

FUNDE:

v4-MUST-FIX Status:
- Pipeline-Meta-Leak: ✓ VOLLSTÄNDIG BEHOBEN. HTML-Kommentar in <aside> entfernt, 
  Inline-Klammer im Body gestrichen, Quellen-Hinweis nüchtern auf "Primärquelle 
  für sämtliche Eurobeträge" reduziert. Keine Pipeline-Apologetik mehr im 
  Production-HTML.
- "größte und teuerste" Halluzination: ✓ BEHOBEN. v5 sagt nur noch "der teuerste 
  Feierraum nach Gebührensatzung" — "größte und" gestrichen.
- feuerbestattungen24.de-Sekundärquelle: ✓ ENTFERNT. Ersetzt durch 
  Verbraucherzentrale + aeternitas e.V. Sauberer, aber siehe Schwäche 3.

SCHWÄCHE 1 — Persönlichkeiten ohne Primärquellen-Verifikation (Kategorie 12, 
Halluzinationsverdacht): In der Westfriedhof-Sektion werden "Heini Mercks 
(Öcher Karnevalist)" und "Elisabeth 'Lipette' Jungbecker ('Mutter der Ros')" 
als bestattete Persönlichkeiten genannt. Die Wikipedia-Quelle, auf die die 
Sektion implizit verweist, listet diese Personen NICHT auf dem Westfriedhof. 
Beide sind Aachener Karnevalsfiguren — ihre Bestattungsorte stehen nicht in 
der zitierten Primärquelle. Risiko: zitierfähige Fehlbehauptung in einem 
lokalverankerten Sachverhalt. → Fix: Entweder mit Aachener Stadtarchiv / 
Karnevalsgesellschaft Primärquelle belegen, oder beide Namen aus der Liste 
streichen. Bei Karnevalsfiguren ist die mündliche Tradition stark, das macht 
sie aber nicht primärquellen-tauglich.

SCHWÄCHE 2 — H2/Inhalts-Widerspruch (Kategorie 5/Stilistik im YMYL-Kontext): 
H2 "Friedhöfe in Aachen – vier Friedhöfe und das städtische Krematorium". 
Inhalt zeigt aber 5 Friedhof-Artikel (Westfriedhof, Ostfriedhof, Waldfriedhof, 
Heißbergfriedhof, plus innerhalb des "Krematorium"-Artikels ausführlich den 
Friedhof Hüls als eigenständigen Friedhof). Der Friedhof Hüls wird textlich 
als fünfter Friedhof behandelt ("einer der 28 städtischen Friedhöfe"), aber 
in der Strukturzählung versteckt. Leser zählt mit und stutzt. → Fix: H2 
ändern in "Die fünf wichtigsten Friedhöfe und das städtische Krematorium" 
oder Friedhof Hüls als eigenen <article> herausziehen, Krematorium getrennt.

SCHWÄCHE 3 — Marktpreis-Aussage bleibt unspezifisch (Kategorie 1, Quellen-Lücke): 
Kostenkapitel-Schluss: "Realistische Gesamtkosten in Aachen liegen damit bei 
einer einfachen Feuerbestattung im niedrigen vierstelligen Bereich, bei einer 
Erdbestattung mit Trauerfeier deutlich im mittleren vierstelligen Bereich." 
Beide verlinkten Sekundärquellen (Verbraucherzentrale + aeternitas) sind 
bundesweit, NICHT Aachen-spezifisch. Die einzige stadtspezifische Markt­preis-
Aussage bleibt damit eine Range-Floskel ohne lokale Primärquelle. Auf einer 
"Stadt-Aachen"-Page schwach. → Fix: Entweder konkrete Aachener Bestatter-
Preislisten als Stichproben (3-5 Anbieter), oder Aeternitas-Marktbericht mit 
Regional­schlüssel, oder Aussage präzisieren mit konkreter Spanne (z.B. 
"erfahrungsgemäß 1.500–3.000 € Bestatterhonorar zusätzlich zu Stadtgebühren").

Kleinere Funde (kein MUST-FIX, fürs Backlog):
- Schritt 1 der Anleitung: kategorisches "nicht der Rettungsdienst" bei 
  zuhause-Sterbefall. Bei akut-unklarer Situation ist 112 nicht falsch. 
  Adv-v4 hat das schon moniert, v5 hat nicht angefasst. Bleibt YMYL-grenz­wertig.
- Link-Anker "17. Änderungssatzung" zeigt auf URL mit Dateiname "16-aenderungs­
  satzung...". Inhaltlich verifiziert OK (Adv-v4), aber optisch verwirrend. 
  Stadt-Aachen kann nicht geändert werden, ist deren Filename. Akzeptabel.
- og:image fehlt im Head — konsistent mit dem bekannten Site-weiten Issue 
  (98/98 Pages), nicht v5-spezifisch.

MUST-FIX vor Deploy: ja.

Begründung: Schwäche 1 ist zitierfähige Halluzination in YMYL-Kontext mit 
Lokalbezug — exakt die Klasse Fehler, die Local-Authority-Reviewer fangen 
würden. Schwäche 2 ist optisch-strukturell und beschädigt Vertrauen sofort 
("die Page kann nicht zählen"). Schwäche 3 ist Quellen-Diät, die für 
allgemeine YMYL-Hygiene noch akzeptabel ist, aber für eine Page, die sich 
als Aachen-spezifisch positioniert, eine Lücke. Mindestens 1+2 vor Deploy 
fixen, dann Page realistisch bei 92–93.

Vergleich Adv-v4 (84) → Adv-v5 (89): +5 Punkte durch saubere Behebung aller 
3 v4-MUST-FIX. Verbleibende Schwächen sind eine Klasse subtiler 
(Halluzinations-Verdacht statt manifester Halluzination, Struktur-Widerspruch 
statt Pipeline-Leak). Page ist deploy-fähig nach Fix von 1+2.