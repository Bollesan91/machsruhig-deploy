Ich lade beides und reviewe ehrlich.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Web durchsucht

BRIEFING_OK

SCORE: 74/100

FUNDE (Quellenanker / Faktenfehler / Struktur-Lücken / Marketing):

Faktenfehler / verifikationsbedürftig:

Bruno Taut (1880–1938) ruht laut gängiger Quellen auf dem Südwestkirchhof Stahnsdorf bei Berlin, nicht auf dem Südfriedhof Leipzig. Sehr wahrscheinlich Faktenfehler — muss geprüft und ggf. ersetzt werden.
Max Klinger: Autor hat bereits Unsicherheit markiert (UNSURE-Kommentar). Klinger ist tatsächlich in Großjena beigesetzt — gehört nicht in die Ehrengräberliste ohne Verifikation. Im Fließtext steht die Behauptung trotzdem als Fakt; widersprüchlich zum HTML-Kommentar.
Adam Friedrich Oeser Sterbedatum 1799 prüfen — Oeser starb 1799, ja, aber die Aussage „Grabmal heute ebenfalls in der Lapidariumsanlage" braucht Quellenanker.
Karl Friedrich Zöllner im Fließtext, fehlt in der FAQ-Antwort zum Südfriedhof — Inkonsistenz.
Johann Sebastian Bach / Grabungen 1894: Üblich datiert die Forschung die Grabung auf 1894, die Identifizierung durch Wilhelm His ist publiziert 1895. Stimmt grob, aber „anthropologisch zugeordnet" sollte präziser werden (His-Gutachten).
„Krematorium Leipzig … eines der ersten Krematorien Sachsens" — schwammig. Sachsen hatte ab 1878 das Krematorium Gotha als Pionier (Thüringen), in Sachsen war Chemnitz früher (1907 fertiggestellt, 1908 eröffnet). Die Leipziger Krematoriums-Inbetriebnahme war ca. 1910 — also nicht „eines der ersten", sondern zeitgleich/später. Fakt prüfen oder Aussage entfernen.

Quellenanker — Lücken:

Kein einziger § aus dem SächsBestG wird mit Paragraphennummer zitiert. Sargpflicht, Bestattungsfrist, Friedhofszwang werden erwähnt — Verweis erfolgt nur pauschal auf die Sachsen-Seite. Mindestens § 18 SächsBestG (Bestattungsfrist) und § 19 (Bestattungsart) sollten konkret genannt werden.
Friedhofssatzung Leipzig wird 7× erwähnt, aber nicht verlinkt. Direktlink auf die Satzung in der bürgerservice.leipzig.de oder auf die Gebührenordnung-PDF fehlt komplett.
Ruhezeit „i. d. R. 20 Jahre" in Kernfakten — ohne Quellenverweis und ohne Differenzierung Erd-/Urnenbestattung. Leipziger Satzung muss als Beleg verlinkt sein.
Zweite Leichenschau: „in der Regel im Krematorium durch einen amtlich bestellten Arzt" — Rechtsgrundlage (§ SächsBestG) fehlt.
Israelitischer Friedhof Delitzscher Straße: Eröffnungsjahr fehlt (1928).
Statistische Aussagen wie „über 140 Jahre Belegungsgeschichte" (Ostfriedhof) — ok, aber „gewachsener Altbaumbestand" ist generisch.

Struktur-Lücken:

Wortzahl: Schätzung ~2.000 Wörter — am unteren Ende des Zielkorridors 2.000–2.500, eher Richtung 1.900. Bestattungskosten- und Bestatterwahl-Sektion sind dünn, Bestattungsarten-Sektion ist sehr knapp (2 Absätze).
Bestattungskosten Leipzig: Keine konkreten Leipzig-Zahlen. Nur Bundesdurchschnitt Stiftung Warentest. Eine Tabelle oder Preisspanne für Reihengrab/Wahlgrab/Urnengrab nach Leipziger Gebührenordnung fehlt komplett — das ist die häufigste Suchintention.
Friedhofs-Sektion Nord/Ost: Beide Friedhöfe sind 1881 eröffnet — der Text sagt das zweimal nacheinander, ohne die Reihenfolge oder Hierarchie zu klären. Hektar-Angabe Nordfriedhof fehlt (UNSURE markiert) — muss vor v2 recherchiert sein (Nordfriedhof ~22 ha laut Wikipedia, Ostfriedhof ~17 ha).
Mendelssohn-Absatz in der Johannisfriedhof-Sektion stört den Lesefluss — Mendelssohn war nie dort bestattet, gehört eher in einen separaten „Wer ruht NICHT in Leipzig"-Hinweis oder in die FAQ (wo er bereits steht). Doppelung.
Cross-Links: Nur 4 interne Links (Sachsen, Bestattungsarten, Checkliste, Vorsorge-Check). Verlinkung zu /bestattungskosten, /trauerrede-schreiben, anderen Sachsen-Städten (Dresden, Chemnitz) fehlt.
Schema.org: FAQ enthält 6 Fragen, Mendelssohn-FAQ im HTML aber nicht im JSON-LD. Inkonsistenz — alle sichtbaren FAQ müssen ins Schema.
Place-Schema: Adresse Ostfriedhof zeigt "Oststraße 04103" — 04103 ist Zentrum (Johannisplatz-PLZ), Ostfriedhof liegt in Volkmarsdorf, PLZ 04315 (Oststraße). PLZ-Fehler.

Marketing / Floskeln:

„Hidden Gem" wird viermal verwendet — als Strukturmarker ok, aber tendiert zur Phrase. Variieren (z. B. „Wenig bekannt:", „Besonderheit:").
„bürgerlicher Stadtteilfriedhof" und „hohem Stille-Faktor" (Ostfriedhof) — letzteres ist Marketingsprache. Streichen oder konkretisieren (z. B. Besucherzahlen, falls verfügbar).
„eine Anlage, die ihre Funktion … bis heute behalten hat" — Floskel. Konkretisieren oder streichen.
„in dieser Verbindung von Sepulkralkultur und nationaler Gedenkstätte in Deutschland einzigartig" — starke Behauptung („einzigartig") ohne Quelle. Abschwächen oder belegen.
„Lesezeit: ca. 10 Minuten" passt nicht zu 2.000 Wörtern (das wären ~7–8 min).

MUST-FIX vor v2:

Bruno Taut entfernen oder mit harter Quelle belegen (sehr wahrscheinlich Faktenfehler — Taut ist in Stahnsdorf bestattet).
Max Klinger entfernen aus dem Fließtext (UNSURE-Kommentar im HTML reicht nicht; Aussage steht als Fakt im sichtbaren Text).
§§ SächsBestG mit Paragraphennummern in der Bestattungsrecht-Sektion zitieren (mindestens Bestattungsfrist, Sargpflicht, Friedhofszwang) — nicht nur pauschalverweis auf Sachsen-Seite.
Direktlink auf Leipziger Friedhofssatzung + Gebührenordnung (PDF oder leipzig.de-Unterseite) in Recht- UND Kosten-Sektion einbauen.
Leipzig-spezifische Preisspannen in Kostensektion ergänzen — zumindest Größenordnung Reihengrab / Urnenwahlgrab / Wahlgrab nach Gebührenordnung. Aktuell ist die Sektion eine Allgemein-Page mit Leipzig-Namen.
Nordfriedhof Hektar-Angabe recherchieren und einsetzen (UNSURE-Kommentar auflösen) — analog Ostfriedhof.
PLZ-Fehler Ostfriedhof im Schema.org korrigieren (04103 → 04315).
FAQ-Schema synchronisieren: Mendelssohn-FAQ ist im HTML, fehlt im JSON-LD. 7 sichtbare FAQs vs. 6 im Schema.
Karl Friedrich Zöllner in FAQ-Antwort Südfriedhof ergänzen (Inkonsistenz Fließtext ↔ FAQ).
Krematorium-Aussage entweder belegen oder zu „1910 eröffnet" entschärfen — „eines der ersten Krematorien Sachsens" ist faktisch fragwürdig (Chemnitz war früher).
„Hidden Gem"-Marker variieren — 4× ist zu repetitiv.
„Stille-Faktor" / „bürgerlicher Stadtteilfriedhof" ersetzen oder belegen.
„einzigartig"-Behauptung beim Südfriedhof/Völkerschlachtdenkmal-Areal abschwächen oder Quelle ergänzen.
Mendelssohn-Absatz aus Johannisfriedhof-Sektion entfernen oder als kurzen Hinweisbox darstellen — gehört nicht in die Johannisfriedhof-Beschreibung als 3. Absatz.
Wortzahl auf ~2.300 anheben durch echte Leipzig-Inhalte (Gebühren-Tabelle, Israelitischer Friedhof ausführlicher, Eingemeindete-Ortsteile-Friedhöfe konkret benennen mit Beispielen).
Lesezeit-Angabe auf 7–8 Minuten korrigieren.