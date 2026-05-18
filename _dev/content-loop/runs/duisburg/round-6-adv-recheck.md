Ich lese die drei Dateien.

Web durchsucht
Web durchsucht

BRIEFING_OK.

Grinch-Brille auf. v3 muss die drei harten v2-Funde geschlossen haben (Halluzination Friedrich Thyssen 4/8 1962, leere Gebührentabelle, nicht-belegter Stiftung-Warentest-Wert). Ich prüfe gezielt was reingekommen ist und wo neue Schwächen lauern.

Check 1 — Halluzination Friedrich Thyssen 4/8 1962: In v3 nicht mehr auffindbar. Norden-Sektion erwähnt nur noch generisch "Knappschafts-Grabfelder", "Knappenvereine" — sauber entschärft. ✓

Check 2 — Gebührentabelle: Jetzt mit NRW-typischen €-Korridoren plus Disclaimer "Duisburger Beträge können davon abweichen" und Hinweis auf Wirtschaftsbetriebe. Tabelle hat Substanz. ✓

Check 3 — Stiftung-Warentest-Zahl: In v3 ersetzt durch "Bundesweite Durchschnittsangaben variieren je nach Quelle und Erhebungsmethode" — Zahl ist raus, Phantomquelle ist raus. ✓

Check 4 — Loveparade: Jetzt drin (Sektion "Duisburg als Bestattungsort", 3 Sätze, 21 Tote, Karl-Lehr-Tunnel, Gedenkstätte, 24. Juli). Verlinkt auf duisburg.de Homepage — nicht auf die konkrete Gedenkseite, aber okay. ✓

Check 5 — Superlativ muslimisches Grabfeld: In v3 entschärft auf "größere, zentral verwaltete muslimische Grabanlage". ✓

Check 6 — Sterbefall-Zahl Duisburg: v2-Phantomquelle ("5.500–6.000 Sterbefälle, kommunale Statistik") ist in v3 ersetzt durch IT.NRW-Verweis (226.000 NRW gesamt 2023) plus Open-Data-Duisburg-Link. Beide Quellen real verlinkt. ✓

Soweit die v2-Punkte. Jetzt suche ich neue Schwächen mit dem Mindset "die Page ist unter 85".

Web durchsucht
Web durchsucht

Drei harte Faktenprobleme in v3 gefunden — und das sind neue Fehler, die v2 nicht hatte:

Faktenfehler 1: Fläche Waldfriedhof. v3 sagt zweimal "rund 76 Hektar" (Hero-Lead und H3-Sektion). Sowohl die offizielle WBD-Seite (duisburg-friedhof.de/WBD Friedhöfe) als auch die Wikipedia, mehrere Bestatter-Quellen und der Lokalpresse-Bericht zum 100-jährigen Jubiläum nennen einhellig rund 67 Hektar, nicht 76. Auch im Schema.org-Block wird "76 Hektar" wiederholt. Das ist eine konkrete, falsifizierbare Zahl, die in v1/v2 noch korrekt war (Audit-Verlauf prüft sich da nicht, aber 67 ist die belegte Zahl). Klassischer Zahlendreher 67 ↔ 76, der durch die ganze Page läuft.

Faktenfehler 2: Adresse Waldfriedhof. v3 nennt "Düsseldorfer Straße 339" — sowohl im Schema.org-Block (PostalAddress) als auch im Body-Text ("Düsseldorfer Straße 339 in Duisburg-Wedau"). Die korrekte Adresse ist laut WBD und mehreren Quellen Düsseldorfer Straße 601, 47055 Duisburg. Auch der Stadtteil ist falsch: nicht Wedau, sondern Wanheimerort. Drei Fehler in einer Zeile, alle im strukturierten Datensatz mit drin → falsche PostalAddress in Schema.org wird von Google verarbeitet.

Faktenfehler 3: Eröffnung Hauptfriedhof. v3 sagt zweimal "1881" für den Hauptfriedhof Sternbuschweg (Hero-Lead implizit, Keyfacts-Block "Ältester innerstädtischer: Hauptfriedhof Sternbuschweg (1881)" und Schema.org "eröffnet 1881"). Lasse ich kurz gegenchecken:

Web durchsucht
Web durchsucht

Bestätigt. Der Hauptfriedhof Sternbuschweg wurde 1870 eröffnet, nicht 1881. Sowohl die offizielle WBD-Seite als auch Deutsche Stiftung Denkmalschutz, KuLaDig (LVR) und Stadt-Duisburg-Microsite Neudorf belegen 1870 einhellig. 1881 ist ein Datum aus der Geschichte des Jüdischen Friedhofs (1881-1983 belegt) — möglicherweise wurde das verwechselt.

Damit habe ich genug. Drei substantielle, falsifizierbare Faktenfehler — alle in den ersten 20 Zeilen sichtbar, alle im Schema.org-Block verewigt, alle hätte ein 5-Minuten-Faktencheck gefunden.

SCORE: 68/100

FUNDE:

HALLUZINATION/FAKTENFEHLER #1 — Fläche Waldfriedhof: "rund 76 Hektar" ist falsch, korrekt 67 Hektar. Steht dreimal in der Page: Hero-Lead ("rund 76 Hektar der größte Friedhof"), Keyfacts-Block ("Waldfriedhof (ca. 76 ha)") und H3-Sektion Waldfriedhof ("rund 76 Hektar"). Zusätzlich im Schema.org-Place-Description verewigt. Quellen einhellig: WBD-AöR offiziell (duisburg-friedhof.de: "Fläche von rund 67 Hektar"), Wikipedia ("mit 67 Hektar der größte Friedhof in Duisburg"), Rundschau Duisburg zum 100-jährigen Jubiläum 2023 ("rund 67 Hektar"), Memovida ("67 Hektar"), RuheDirekt ("67 Hektar"). Klassischer Zahlendreher 67↔76 — fatal, weil dreifach reproduziert plus im strukturierten Datensatz. Fix: alle 4 Stellen + Schema.org auf 67 ha korrigieren. MUST-FIX.
HALLUZINATION/FAKTENFEHLER #2 — Adresse + Stadtteil Waldfriedhof falsch. v3 schreibt im H3-Body: "an der Düsseldorfer Straße 339 in Duisburg-Wedau". Korrekt laut WBD-Friedhof.de und Rundschau Duisburg ist Düsseldorfer Straße 601, Stadtteil Wanheimerort (Wedau ist ein anderer Stadtteil im Duisburger Süden). Hausnummer 339 ist im Schema.org-PostalAddress zusätzlich strukturiert verewigt — Google indexiert die falsche Adresse. Zwei harte Fakten in einem Halbsatz falsch. Fix: Düsseldorfer Straße 601, 47055 Duisburg-Wanheimerort. Schema.org streetAddress und postalCode (PLZ ist 47055, nicht 47053) korrigieren. MUST-FIX.
HALLUZINATION/FAKTENFEHLER #3 — Eröffnungsjahr Hauptfriedhof Sternbuschweg: "1881" ist falsch, korrekt 1870. Steht dreimal: Hero-Lead ("Hauptfriedhof am Sternbuschweg der älteste innerstädtische"), Keyfacts ("Hauptfriedhof Sternbuschweg (1881)"), Schema.org Place Description ("eröffnet 1881") und H3-Sektion ("wurde 1881 als zentraler Stadtfriedhof in Duisburg-Neudorf eröffnet"). Belegt: WBD-AöR ("entstand um 1870"), Deutsche Stiftung Denkmalschutz ("wurde 1870 der mit etwa 30 Hektar größte Friedhof der Stadt angelegt"), KuLaDig/LVR ("1870 angelegten neuen kommunalen Friedhof"), Stadt Duisburg/Microsite Neudorf ("entstand um 1870"). 1881 ist das Belegungsbeginn-Datum des jüdischen Teil-Friedhofs (1881–1983) — Verwechslung Gesamtfriedhof ↔ jüdisches Gräberfeld. Damit ist auch die Logik im Body falsch ("ersetzte ältere innerstädtische Begräbnisplätze, die mit dem rasanten Bevölkerungswachstum durch die Industrialisierung an Kapazitätsgrenzen stießen") — die Industrialisierungs-Erzählung ist für 1870 noch konsistent, aber die Behauptung "1881" verschiebt das Bauwerk in eine Spätphase, in der die Stadt schon massiv anders aussah. Fix: alle 4 Stellen + Schema.org auf 1870 korrigieren. MUST-FIX.

Zusatzfunde (nicht in den Top-3, aber notiert):

v3 sagt "Friedhof Ruhrort ... wurde 1851 eröffnet" und "rund 4,5 Hektar" — beide Zahlen sind in v3 neu, weder Bestattungsgesetz noch Stadt Duisburg verlinkt → bei drei bereits belegten Halluzinationen in v3 ist die Wahrscheinlichkeit nicht null, dass auch hier eine sitzt. Mindestens Pflichtcheck.
"Eingemeindung Ruhrorts nach Duisburg 1905" — bitte gegenchecken (Wikipedia nennt 1905, plausibel, aber im Halluzinations-Kontext der Page nochmal sicherheitshalber).
"Hamborn eingemeindet 1929" — laut historischer Quellenlage korrekt, aber im Kontext einer Page mit drei harten Fehlern jedes Datum verifizieren.
"Loveparade 21 Tote" — korrekt belegt (21 starben am Unglückstag bzw. an direkten Folgen), Stand-OK.
Sterbefall-Zahl NRW 2023 (226.000) und IT.NRW-Link — der Link in v3 zeigt auf eine konkrete IT.NRW-Pressemitteilung, gut. Sauber. ✓
Die §-Anker (§ 13, 14, 16 Abs. 2, 17 BestG NRW + § 28 PStG) sind sauber gesetzt und erstmals mit Primärquellen-Link verlinkt — gegenüber v2 deutliche Verbesserung. ✓
Floskel-Risiko: "individuelle Wünsche", "Vorsorge zu Lebzeiten kann viele dieser Fragen entschärfen" — minor Floskel-Verdacht, ignoriere bei 3 harten Fehlern.

MUST-FIX vor Deploy: ja.

Begründung: Drei falsifizierbare Faktenfehler, die jeder durch einen einzigen Klick auf die offizielle WBD-AöR-Seite hätte finden können (76 statt 67 ha, Düsseldorfer Str. 339 statt 601 / Wedau statt Wanheimerort / 47053 statt 47055, 1881 statt 1870). Alle drei sind nicht nur im Body, sondern zusätzlich im Schema.org strukturiert hinterlegt — das bedeutet, dass Google die falschen Daten als strukturierte Stadt-/Place-Information indexiert. Auf einer YMYL-Page mit Anspruch "Primärquellen-zitiert" und mit dem expliziten Versprechen "Stand-Daten aus Friedhofsgebührensatzungen" sind drei Friedhofs-Stammdaten-Fehler ein härterer Vertrauenskiller als die einzelne Bergbau-Halluzination in v2. v2-Probleme (leere Tabelle, Stiftung-Warentest, Phantom-Sterbefallzahl) sind sauber behoben — aber durch das Editieren der Friedhofsabschnitte ist eine neue, schwerwiegendere Faktenebene zerschossen worden. Pattern erkennbar: bei jedem Rewrite verschwinden alte Fehler, neue Zahlen werden eingefügt — ohne dass die neuen Zahlen gegen Primärquellen geprüft werden. Empfehlung über v3-Fix hinaus: Chat A muss in der nächsten Runde jede konkrete Zahl/Jahreszahl in den Friedhof-Sektionen 1:1 gegen die WBD-AöR-Microsite gegenprüfen, bevor sie in den Body geht — nicht aus dem Gedächtnis, nicht aus v2-Vorlage, sondern aus Primärquelle.