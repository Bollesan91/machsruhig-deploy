Ich lade beides und reviewe.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Web durchsucht

BRIEFING_OK.

Jetzt der Review — schonungslos.

SCORE: 68/100

FUNDE:

Quellenanker / Faktenfehler:

Nordfriedhof-Fläche: Die Kernfakt-Behauptung "rund 70 Hektar" wird viermal wiederholt (Title, Meta, Hero, Keyfacts, Schema), aber kein Beleg verlinkt. Die offizielle Düsseldorfer Friedhofs-Seite gibt die Fläche aller städtischen Friedhöfe zusammen mit ca. 215 ha an — 70 ha allein für den Nordfriedhof ist plausibel, aber unbelegt. Risiko: Wenn der Wert falsch ist, zieht es Title, Meta-Description, H1-Lead, Keyfacts und Schema in einem Rutsch nach unten.
Eröffnungsjahr Nordfriedhof "1884" — keine Quelle verlinkt. Wikipedia nennt 1884, die Stadt selbst formuliert teils anders. Bei einer harten Jahreszahl in H1-Bereich + Schema gehört eine Primärquelle daneben.
Südfriedhof Schema "eröffnet 1904", Stoffeler "eröffnet 1897" — diese Jahreszahlen stehen nur im JSON-LD, im Fließtext werden sie bewusst als UNSURE ausgespart. Das ist ein direkter Widerspruch: Schema behauptet, Text traut sich nicht. Entweder beide raus oder beide rein mit Beleg.
"Krematorium am Nordfriedhof" — wird in Keyfacts, Fließtext und im "Nach einem Todesfall"-Block als Faktum behauptet. Düsseldorf hat das städtische Krematorium tatsächlich am Friedhof Heerdt, nicht am Nordfriedhof. Bitte prüfen und ggf. korrigieren; falls unsicher: Standort offen lassen.
"Bestatterverband Nordrhein-Westfalen als Landesverband im BDB" — der korrekte Name ist Landesinnungsverband des Bestattergewerbes Nordrhein-Westfalen. Bitte verifizieren oder neutral als "BDB-Landesverband NRW" formulieren.
Stiftung-Warentest-Korridor "7.000–8.000 €" wird als konkrete Zahl zitiert, aber test.de wird nur generisch verlinkt (Startseite, kein Artikel). Entweder konkreter Test/Jahr verlinken oder Zahl entschärfen.
§ 28 PStG ist korrekt verlinkt — gutes Beispiel, wie der Rest aussehen müsste.
BestG NRW wird mehrfach genannt, aber recht.nrw.de-Link führt nur auf die Startseite, nicht auf das Gesetz selbst. Keine §-Nummern zu Bestattungsfrist, Sargpflicht, Friedhofszwang (z.B. § 13 BestG NRW Friedhofszwang) — die Page schiebt das komplett auf die Bundesland-Seite ab, was inhaltlich Lücken hinterlässt.

Struktur-Lücken:

Keine konkreten prominenten Gräber genannt. Düsseldorfs Nordfriedhof hat dokumentierte Ehrengräber (u.a. Friedrich Spielhagen, Wilhelm Marx, Heinrich Heppe-Bestatten — bitte Stadt-Liste prüfen). "Persönlichkeiten des Düsseldorfer und rheinischen Lebens" ohne einen einzigen Namen ist Floskel. Briefing fordert ausdrücklich Friedhofs-Highlights mit Geschichte/Hidden-Gem-Story — fehlt komplett.
Ruhezeiten: "20 bis 30 Jahre" generisch für NRW — gehört konkret pro Grabart für Düsseldorf (typisch: 25 Jahre Erdgrab, 20 Jahre Urne). UNSURE-Kommentar erkennt es selbst an.
Friedhofsgebühren: Kein einziger konkreter Betrag. Düsseldorf publiziert die Gebührensatzung öffentlich (Reihengrab, Wahlgrab, Urnenwand etc. mit konkreten €-Werten). Ohne mindestens 2–3 Beispielsätze ist die Kosten-Sektion eine Hülle.
Südfriedhof + Stoffeler: keine eigene Geschichte, keine architektonischen Details mit Substanz, kein Hidden Gem. Im Vergleich zur Nordfriedhof-Sektion deutlich dünner — der Stoffeler-Absatz hat zwei reine Allgemeinplätze ("dichter Baumbestand, engere Wege").
Wortzahl: ca. 1.450 Wörter Fließtext (ohne Keyfacts/FAQ/Quellen). Unter dem 1.500-Minimum, klar unter dem Zielkorridor 2.000–2.500.
Footer-Copyright "2024–2026" — vermutlich Template-Übernahme, aber prüfen ob bewusst.
Datum-Inkonsistenz: Schema datePublished/dateModified = 2026-05-12, Hero zeigt "12. Mai 2026" — okay, aber Page entsteht heute (15. Mai). Wenn das Schema-Datum stehen bleibt, ist die Page schon beim Live-Gang 3 Tage alt.

Marketing / Floskel-Detection:

"Wer die eigene Bestattung zu Lebzeiten regeln möchte, dem hilft der Vorsorge-Check beim Einstieg" — Werbe-Floskel ohne Mehrwert.
"Eine Schritt-für-Schritt-Anleitung für die ersten Tage findet sich in der Checkliste Todesfall" — okay als Cross-Link, aber zweimal in der Page (im Todesfall-Abschnitt + Vorsorge-Block).
"Vorsorge und weiterführende Themen" als Sektion ist ein reiner Link-Stuffing-Absatz (5 interne Links in 3 Sätzen). Wirkt wie Footer-im-Content.
"Trauer braucht Zeit"-Floskeln vermieden — gut. Aber: "im Alltag besuchen möchten" (Stoffeler-Absatz) ist auch nicht stark.

Schema/Technik:

FAQPage Schema enthält 6 Fragen, sichtbarer FAQ-Bereich enthält 7 Fragen (muslimisch/jüdisch zusätzlich). Schema muss vollständig sein, sonst Google-Inkonsistenz.
Schema City-Beschreibung "Landeshauptstadt Nordrhein-Westfalens am Rhein" — Hauptmerkmal ist gleichzeitig auch Hauptstadt-Status, "am Rhein" allein wäre für SEO uninteressant. Okay so.
OG-Image generisch (/assets/og-image.png), nicht stadt-spezifisch — bekanntes Site-weites Problem (98/98 fehlten laut letzter Auditrunde), aber für v2 auch hier flaggen.

MUST-FIX vor v2:

Krematorium-Standort verifizieren: Behauptung "am Nordfriedhof" prüfen. Falls tatsächlich Heerdt → korrigieren in Keyfacts, Fließtext, Todesfall-Absatz.
Nordfriedhof 70 ha + 1884 belegen: Quelle (Stadt Düsseldorf oder Wikipedia-Stadtarchiv) in Fußnote/Link daneben oder Wert weicher formulieren.
Schema-Eröffnungsjahre Süd 1904 / Stoffeler 1897 entscheiden: Entweder mit Beleg in den Fließtext (UNSURE-Kommentare auflösen) oder aus dem Schema raus. Widerspruch Schema↔Text ist nicht haltbar.
3 konkrete Ehrengräber auf dem Nordfriedhof nennen mit Person + Wirkungsfeld + ggf. Feld-Lage. Stadt-Liste der Ehrengräber ist öffentlich.
Friedhofsgebühren konkret: Mindestens 2 Beispielsätze aus der Düsseldorfer Gebührensatzung (z.B. Reihengrab Erdbestattung, Urnenwand). Korridor "7.000–9.000 €" allein reicht nicht.
Ruhezeiten Düsseldorf konkret pro Grabart (Erd-/Urnen-/Kindergrab), nicht "20 bis 30 Jahre NRW-typisch".
§§ BestG NRW nennen: Friedhofszwang (§ 13), Bestattungsfrist (§ 14), Sargpflicht (§ 8) — mit Verlinkung auf den Gesetzestext bei recht.nrw.de, nicht nur Startseite.
Südfriedhof + Stoffeler: je 1 substanzieller Detail-Block (konkrete Trauerhalle/Architektur, Künstler/Grabstätte, lokaler Anker). Aktuell beide deutlich unter Niveau der Nordfriedhof-Sektion.
Stiftung-Warentest-Verweis konkretisieren: Test/Jahr nennen oder Zahl als Branchenkorridor ohne Markenname.
FAQPage Schema: 7. Frage (muslimisch/jüdisch) ergänzen, sonst Konsistenz Schema↔Sichtbares brechen.
Bestatterverband-Name korrigieren (Landesinnungsverband NRW) oder neutral formulieren.
Wortzahl auf ≥ 1.800 erhöhen — primär durch Substanz in Friedhofs-Sektionen + konkrete Gebühren, nicht durch Marketing-Absätze.
Sektion "Vorsorge und weiterführende Themen" entschärfen oder durch lokale Substanz ersetzen (z.B. Düsseldorfer Trauerorte, Trauer-Cafés, kirchliche Beratung).