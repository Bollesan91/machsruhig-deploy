Web durchsucht
Web durchsucht

Adversarial-Brille auf. Erst die drei v3-MUST-FIX prüfen, dann unbarmherzig nach neuen Schwächen suchen.

v3-MUST-FIX-Status:

Waldfriedhof Fläche 76 → 67 ha: ERLEDIGT. Hero-Lead („rund 67 Hektar"), Keyfacts („Waldfriedhof (ca. 67 ha)"), H3-Sektion („rund 67 Hektar") und Schema.org-Description („rund 67 Hektar") konsistent auf 67. Alle drei Stellen + Schema.org sauber. ✓
Waldfriedhof Adresse 339/47053/Wedau → 601/47055/Wanheimerort: ERLEDIGT. H3-Sektion („Düsseldorfer Straße 601 in Duisburg-Wanheimerort (47055)") und Schema.org-PostalAddress (streetAddress „Düsseldorfer Straße 601", addressLocality „Duisburg-Wanheimerort", postalCode „47055") korrekt korrigiert. ✓
Hauptfriedhof Sternbuschweg 1881 → 1870: ERLEDIGT. Keyfacts („Hauptfriedhof Sternbuschweg (1870)"), Schema.org-Description („eröffnet 1870") und H3-Body („wurde 1870 als zentraler Stadtfriedhof... eröffnet"). Außerdem geschickt entschärft: „Ein jüdisches Gräberfeld kam 1881 hinzu — eine Datierung, die in älteren Quellen gelegentlich für die Gesamtanlage übernommen wird, aber sich nur auf den jüdischen Teilbereich bezieht." — der Verwechslungs-Mechanismus aus v3 wird transparent erklärt. ✓

Alle drei v3-MUST-FIX sind sauber abgearbeitet — nicht oberflächlich entschärft, sondern faktisch korrigiert und konsistent durchgezogen.

Jetzt aktiv neue Schwächen suchen. Pattern aus v3 war: bei jedem Rewrite kommen neue Zahlen rein, die ungeprüft sind. Also gezielt auf die neu eingeführten oder unveränderten Detail-Zahlen prüfen.

Web durchsucht
Web durchsucht

Volltreffer. Drei harte Fakten zum „Friedhof Ruhrort" in v4 sind falsch — die Page hat den genau gleichen Fehler-Modus wie v3, nur eine Sektion weiter rechts. Jetzt noch einen Cross-Check auf die Hamborn-Eingemeindung 1929, weil das Datum als Story-Anker dient.

Web durchsucht
Web durchsucht

Hamborn 1929 ist sauber belegt. Ruhrort-Eingemeindung 1905 ist auch korrekt (1. Oktober 1905). Aber: Der gesamte „Friedhof Ruhrort"-Abschnitt in v4 ist eine vollständige Halluzination — gleiche Sorte wie die v3-Fehler, nur nicht von v3 nach v4 mitgeschleppt, sondern neu eingeführt oder unkorrigiert übernommen.

SCORE: 71/100

v3-MUST-FIX-Status:

Waldfriedhof Fläche 76 → 67 ha: ERLEDIGT. Konsistent durch Hero, Keyfacts, H3 und Schema.org. Sauber.
Waldfriedhof Adresse 339/47053/Wedau → 601/47055/Wanheimerort: ERLEDIGT. Body und Schema.org-PostalAddress korrekt. Sauber.
Hauptfriedhof Sternbuschweg 1881 → 1870: ERLEDIGT. Plus geschickte transparente Erklärung des v3-Fehlermusters („Ein jüdisches Gräberfeld kam 1881 hinzu — eine Datierung, die in älteren Quellen gelegentlich für die Gesamtanlage übernommen wird"). Vorbildlich aufgearbeitet.

NEUE Schwächen — drei harte Funde, nicht zwei. Score-Senkung gegenüber sauberem v4 ist deshalb gerechtfertigt:

HALLUZINATION #1 — Friedhof Ruhrort: Eröffnungsjahr 1851 ist falsch (korrekt 1845), Adresse Friedrich-Ebert-Straße ist falsch (korrekt Eisenbahnstraße), Fläche 4,5 Hektar ist falsch (korrekt 1,7 Hektar). Das ist der Pipeline-Wiederholungsfehler aus v3 in Reinkultur: drei falsche Detail-Zahlen in einer Sektion, alle drei strukturiert in Schema.org verewigt. Belege durchgängig:

WBD-AöR offiziell (duisburg-friedhof.de): „Der 1845 eingeweihte Friedhof… seine heutige Größe von 1,7 Hektar… Eisenbahnstraße"
WBD Adresse: „Eisenbahnstr. 1, 47119 Duisburg-Ruhrort"
mehrere Sekundärquellen (rheinruhronline, golocal, bestattung-information) bestätigen einhellig 1845 / 1,7 ha / Eisenbahnstraße
Schema.org-Block v4: "streetAddress":"Friedrich-Ebert-Straße", Body v4: „1851 eröffnet", „rund 4,5 Hektar" — alle drei Werte erfunden bzw. mit der Friedrich-Ebert-Brücke verwechselt
der Friedhof heißt im offiziellen Sprachgebrauch auch nicht „Friedhof Ruhrort", sondern „Friedhof Eisenbahnstraße"

Das ist 1:1 dasselbe Schema wie v3 (76/339/1881), nur eine Sektion weiter rechts. MUST-FIX: alle drei Zahlen, die Adresse und idealerweise auch der Friedhofsname auf Eisenbahnstraße / 1845 / 1,7 ha; Schema.org-streetAddress auf „Eisenbahnstraße 1". Bonus-Risiko: der Body referenziert „Reedereien-Familien" — der Friedhof beherbergt tatsächlich Haniel, Liebrecht, de Gruyter, also faktisch korrekt — aber die Zahl der Reeder-Gräber ist nicht belegt und die ikonografische Beschreibung ist wieder geschmacksvoll wolkig.

HALLUZINATION #2 — Inhaltlicher Widerspruch zur eigenen Aussage „älteste innerstädtische": Keyfacts sagen Hauptfriedhof Sternbuschweg (1870) sei der „älteste innerstädtische" — das ist plausibel, weil der ältere Eisenbahnstraße-Friedhof (1845) damals zu Ruhrort gehörte, nicht zu Duisburg. Aber: der Body-Text zum Ruhrort-Abschnitt schreibt selbst: „einer der ältesten erhaltenen kommunalen Friedhöfe Duisburgs" — die WBD-Primärquelle sagt allerdings explizit „Dieser Ruhrorter Friedhof ist der älteste städtische Friedhof in Duisburg auf dem auch heute noch Bestattungen stattfinden". Die Page ist also selbst-inkonsistent: laut Primärquelle ist Eisenbahnstraße/Ruhrort der älteste städtische Friedhof Duisburgs überhaupt (durch Eingemeindung), nicht „einer der ältesten erhaltenen". Das ist nicht so falsifizierbar wie #1, aber ein Schwächen-Vektor für einen Reviewer mit Faktencheck-Reflex. Fix: Formulierung präzisieren oder die WBD-Aussage als Zitat übernehmen.

HALLUZINATION #3 — Zwei Halbsatz-Phantome im selben Abschnitt: Im Hero-Lead steht „Duisburg liegt am Zusammenfluss von Rhein und Ruhr und besitzt mit dem Rheinhafen den größten Binnenhafen Europas." Korrekt: Duisburger Hafen (duisport), nicht „Rheinhafen" — der Rheinhafen ist nur einer der Bestandteile des Duisburger Hafens, der „größte Binnenhafen Europas" ist der Gesamthafen. Kleinerer Befund, aber: in der zweiten Sektion steht „der Duisburger Rheinhafen ist seit dem 19. Jahrhundert der größte Binnenhafen Europas" — der Hafen war im 19. Jahrhundert noch nicht der größte Binnenhafen Europas (er wurde es im Laufe des 20. Jahrhunderts; die heutige Spitzenposition ist erst durch Containerumschlag und Hinterland-Anbindung des späten 20. Jh. entstanden). Beide Phrasen sind YMYL-weich, aber faktisch ungenau und durch Lokalpresse leicht widerlegbar. Niedriger Prio, aber Pattern derselbe wie #1 und v3: ungeprüfte Zuspitzung im Body.

MUST-FIX vor Deploy: JA

Begründung: Befund #1 ist exakt der gleiche Fehler-Modus wie die drei v3-Befunde — drei harte, falsifizierbare Stammdaten eines benannten Friedhofs (Jahr, Adresse, Fläche), zusätzlich strukturiert in Schema.org indexiert. Google wird die falsche PostalAddress „Friedrich-Ebert-Straße" für „Friedhof Ruhrort" indexieren — das ist deutlich schlimmer als ein Body-Fehler, weil es Suchergebnisse vergiftet. Das Korrekturpattern ist erprobt (Chat A hat Waldfriedhof-Adresse und Hauptfriedhof-Datum sauber gefixt) — die Sektion „Friedhof Ruhrort" wurde nur nicht mit dem gleichen Sorgfaltsstandard geprüft, vermutlich weil die v3-Adversarial sich auf die drei Top-Funde konzentrierte. Befund #2 ist Pflicht-Cleanup, Befund #3 ist Mini-Politur.

Pipeline-Lesson für Chat A v5: vor dem nächsten Lauf systematisch jede genannte Adresse, Jahreszahl und Hektar-Zahl gegen duisburg-friedhof.de cross-checken — nicht nur die in der vorherigen Adv-Runde angekreideten. Der Fehler-Modus ist das, was Chat C in v3-Recheck schon notiert hatte: „bei jedem Rewrite verschwinden alte Fehler, neue Zahlen werden eingefügt — ohne dass die neuen Zahlen gegen Primärquellen geprüft werden." In v4 ist exakt das wieder passiert, nur in einer anderen Sektion.