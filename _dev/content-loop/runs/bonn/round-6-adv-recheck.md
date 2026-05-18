Ich lese die drei Dateien parallel.

Fetching site
Web durchsucht

BRIEFING_OK.

Ich gehe v3 gegen die 12 Kategorien und die offenen Adv-v2-Funde durch. v3 hat sichtbar nachgebessert: Stockhausen ist weg, Zuckmayer ist weg, §-Nummern stehen drin (§§ 17 ff, § 20, § 26, § 32, § 24, § 25, § 29, § 31), konkrete Gebühren-Beispiele sind da (848,40 €, 1.132,80 €, 1.018,80 €). Aber ich finde drei substantielle neue Schwächen.

SCORE: 82/100

FUNDE:

SCHWÄCHE 1 (Halluzinations-Verdacht, Burgfriedhof-Sektion): Die Sektion ist nach Stockhausen/Zuckmayer-Streichung jetzt das Gegenteil — komplett namenlos. Drei Absätze über den Burgfriedhof, kein einziger Bestatteter wird konkret genannt. Stattdessen: „Künstler, Wissenschaftler und Persönlichkeiten des öffentlichen Lebens", „einer kosmopolitischen Schicht aus Wissenschaft, Kultur und Verwaltung", „einzelne Persönlichkeiten — etwa Bonner Universitätsprofessoren und Künstler des Rheinlands". Das ist exakt Kategorie 5 (Friedhofs-Highlights ohne Story) plus Kategorie 2 (Generische Sätze). Die Wikipedia-Liste zum Burgfriedhof Bad Godesberg führt verifizierbare Namen (z. B. Heinrich Lützeler, Hans Iven, Familie Dahm) — Chat A hat den umgekehrten Fehler zu v2 gemacht: statt einen erfundenen Namen zu droppen, jetzt 0 Namen. Adv-v2 Schwäche 1 forderte explizit „2–3 verifizierbare Bestattete mit Beruf und Lebensdaten" — nicht erfüllt. Verbesserung: mindestens 2 Wikipedia-belegte Bestattete des Burgfriedhofs mit Lebensdaten + 1 Satz Biografie einsetzen, sonst rechtfertigt die Sektion ihre Existenz als eigene H3 nicht.

SCHWÄCHE 2 (Halluzinations-Verdacht / Quellen-Lücke, Nordfriedhof „Sterntalerfeld" mit § 31): Die Aussage „§ 31 (3) Reihengrabanlage mit bis zu 14 sterblichen Überresten" ist verdächtig spezifisch ohne Primärquellen-Link. Der Text gibt § 31 der Bonner Friedhofssatzung als Quelle an, inkl. Maßen 1,00 × 0,50 m und Ruhefrist 10 Jahre. Aber: In der Quellen-Liste ist die Friedhofssatzung verlinkt — der Text müsste das auch im Body anchor-verlinken, tut es aber nicht. Und „bis zu 14 sterbliche Überreste gemeinschaftlich" ist eine sehr ungewöhnliche, konkrete Zahl — wenn das aus der Satzung stammt, lässt es sich belegen; wenn nicht, ist es Halluzinations-Kategorie 12. Bei einem YMYL-Thema (Tot-/Fehlgeburten-Grabfeld, höchst emotional) ist die Hürde für solche Zahlen höher als anderswo. Verbesserung: entweder Inline-Anchor auf den konkreten § 31 der Satzung (Anker oder PDF-Seite), oder die Zahl 14 raus und stattdessen die allgemeinere Aussage „Gemeinschaftsbestattung in einem ausgewiesenen Reihengrabfeld" belassen.

SCHWÄCHE 3 (Quellen-Lücke + Generischer Satz, Kosten-Sektion): „Stiftung Warentest 7.000–8.000 Euro" ist ohne konkrete Quelle, ohne Jahr, ohne Studientitel. Der Satz erscheint dreimal (Body, FAQ, Schema FAQ-Snippet) und ist jeweils nur „nach Stiftung Warentest". Die Quellenliste verlinkt pauschal auf test.de-Startseite — das ist Sekundärquellen-Niveau und für eine YMYL-Preisaussage zu dünn. Stiftung Warentest hat mehrere Bestattungs-Untersuchungen veröffentlicht; ohne Jahr/Studie ist die Zahl nicht prüfbar und potentiell veraltet (Kategorie 3). Gleichzeitig: Die Spanne 7.000–8.000 € deckt sich mit dem bundesweiten Durchschnittsbereich der letzten Jahre, ist also plausibel — aber „plausibel" ist nicht „belegt". Verbesserung: entweder Studientitel + Jahr ergänzen („Stiftung Warentest, test 06/2024" o.ä.) und Deep-Link auf den Artikel, oder die Zahl als „je nach Erhebungen verschiedener Verbraucherorganisationen" relativieren und auf die eigene /bestattungskosten-Seite als Hauptbeleg verlagern.

Zusatzbeobachtungen (nicht in den 3er-Quote, aber relevant):

Wortzahl ca. 2.050 — im Korridor, aber nahe der Untergrenze. Burgfriedhof-Sektion ist mit ~200 Wörtern dünn (Kategorie 8).
Reformjahr BestG NRW „2014" steht im Text, aber die NRW-Reform war 2014 mit weiteren Änderungen 2022 — kurz prüfen, ob 2014 noch der aktuelle Stand ist (Kategorie 3, Verdacht, nicht Beweis).
2 UNSURE-Kommentare im Body — sauber unter 3.
Schema, OG-Tags, Author-Org, Breadcrumb, FAQPage, BreadcrumbList vollständig.
Cross-Links zu Köln/Düsseldorf vorhanden — Kategorie 9 erfüllt.
Floskel-Kontrolle clean — keine „letzte Ruhe", „in dieser schweren Zeit".
Stockhausen-Halluzination aus v2 → behoben ✓
Zuckmayer-Fragment aus v2 → behoben ✓
§-Paragraphen MUST-FIX → erfüllt (mehrfach mit konkreten §-Nummern) ✓
Konkrete Gebühren-Zahl MUST-FIX → erfüllt (3 Beispielwerte mit Berechnung) ✓

MUST-FIX vor Deploy: ja.

Begründung: Schwäche 1 ist die direkte Nicht-Erfüllung eines Adv-v2-MUST-FIX (Burgfriedhof verifizierbare Namen). Schwäche 2 ist Halluzinationsrisiko an einer pietätssensiblen Stelle. Schwäche 3 ist YMYL-Quellendünne bei einer prominent platzierten Zahl. Score 82 spiegelt: substantielle Fortschritte gegenüber v2 (79), aber zwei der drei Schwächen sind 30-Minuten-Fixes (Wikipedia-Lookup Burgfriedhof + Satzungs-Anker setzen + Studientitel ergänzen) — kein Grund, sie auf v4 zu vertagen.