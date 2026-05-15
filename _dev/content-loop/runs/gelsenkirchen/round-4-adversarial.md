Ich lese die drei Dateien.

Fetching site
Web durchsucht

BRIEFING_OK

Jetzt prüfe ich v2 gezielt: Wurden v1-Fehler gefixt? Welche neuen Schwächen gibt es? Ich gehe nicht „insgesamt", ich gehe Stelle für Stelle.

Prüfung der v1-Fixes:

Hero „weltweit" → korrigiert zu „in Deutschland erste" ✓
Gebührensatzung „18.12.2024" ✓
HTML-Kommentar weg ✓
Libuda-Jahr konsolidiert auf Januar 2022 ✓
BestG NRW Datierung gefixt (jetzt „zuletzt geänderte Fassung") ✓
Hassel/Papst gestrichen ✓
Cross-Links Ruhrgebiet (Essen/Bochum/Herne/Recklinghausen) ✓
Krematorium-Hinweis ergänzt ✓
Schätzungen markiert ✓
Potofski-Sterbedatum redaktionell zurückgehalten ✓

Solide gefixt. Aber: ich finde drei neue Schwächen.

SCORE: 84/100

FUNDE (Faktenfehler / unbelegte Claims / Marketing):

SCHWÄCHE 1 — Halluzinations-Verdacht „1.904 Plätze" Schalker Fan-Feld (Friedhöfe-Sektion + FAQ): Die Page behauptet zweifach „1.904 Plätzen — in Anspielung auf das Gründungsjahr 1904". Die zitierte taz-Quelle und sfcv.de belegen die Stadion-Form und das Gründungsjahr-Motiv, aber nicht die konkrete Zahl 1.904. Recherchierbare Quellen (Wikipedia Schalker Fan-Feld, Berichte zur Einweihung) nennen üblicherweise rund 1.904 Grabstätten als Endausbaustufe, aber die Eröffnungs-Belegung war deutlich kleiner. Die Page präsentiert „1.904" wie eine Hardfact-Kapazität. Halluzinations-Risiko: § 7 der Kategorienliste (zu spezifische Zahl ohne erkennbaren Primärquellen-Pin). Fix: Entweder Zahl mit Direktquelle anpinnen (sfcv.de/Stadt-PM zur Einweihung) oder weicher formulieren („auf eine Endausbaustufe von rund 1.904 Grabstätten angelegt").

SCHWÄCHE 2 — Unbelegte Zahl + Cross-Reference-Fehler bei Ordnungsamtsbestattungen: Die Page sagt dreimal „etwa zehn Prozent / rund 300 Beerdigungen jährlich" mit Quelle „FriedhofsGEschichte(n) — Westfriedhof" (friedhoefe-gelsenkirchen.de). Das ist ein Geschichts-Storytelling-Artikel, keine statistische Primärquelle der Friedhofsverwaltung. Selbst die Page-Autorin markiert es als „Schätzung der Friedhofsverwaltung" — aber wiederholt die exakte Zahl 300 dreimal als wäre sie verbindlich. Bei rund 2.700–3.000 Sterbefällen/Jahr in GE (statistisches Landesamt NRW) ist 10 % rechnerisch plausibel, aber die Zahl 300 hängt an einer Story-Seite und steht dreifach in Schema.org-FAQ → wird als verbindlich von Google indexiert. Fix: Entweder echte Primärquelle (Stadt GE Soziales, Jahresbericht GELSENDIENSTE) oder die Zahl auf „etwa 300" reduzieren und in FAQ-Schema den Schätzwert-Disclaimer einbauen.

SCHWÄCHE 3 — „Schalker Bestattungssoziologie" Hidden-Gem ist Wertungs-Prosa, kein Hidden Gem: Der Block „Das Fan-Feld ist mehr als ein kurioser Themenfriedhof: Es funktioniert als Spiegel der Schalker Identität im Strukturwandel. Wer hier liegt, hat sich selbst zugeordnet — über alle Konfessionen und gesellschaftlichen Schichten hinweg." → Das ist Essay-Färbung, keine Sachinformation. Kategorie 11 (Floskeln) und Kategorie 5 (Hidden Gem ohne harten Story-Anker). Im Gegensatz zum Libuda-Hidden-Gem (klare Story mit Datum/Quelle) und Ungarische-Jüdinnen-Hidden-Gem (klare Story mit Volksbund-Anker) liefert dieser Block keine neue verifizierbare Tatsache — er interpretiert. Außerdem die Behauptung „Reservierungen tragen Grabnummern, die mit 04 enden" → kein Quellen-Pin, klingt wie Halluzination/Marketing-Folklore. Fix: Block streichen oder durch eine verifizierbare Konkretsache ersetzen (z.B. Anzahl belegter Gräber Stand 2025 mit sfcv-Quelle).

Zusätzlich (kleiner, aber nennenswert):

Hauptfriedhof Buer „Eröffnet 1899": Volksbund-Quelle ist gesetzt für die Flächenangabe, aber das Eröffnungsjahr 1899 hängt ohne direkten Quellen-Pin im Fließtext. Bitte verifizieren oder mit Stadtarchiv-Quelle anpinnen.
„1923 errichteten Torhäuser … seit 1993 in der Denkmalliste": Keine Denkmalliste-Quelle verlinkt. Bei Architektur-Detailaussagen schwach.
Ostfriedhof „Eröffnet 1897 auf Initiative der damaligen Gemeinde Hüllen": Direkter Quellen-Pin am Satzende fehlt, GG-Wiki ist nur weiter unten verlinkt.

MUST-FIX vor Deploy: ja — aber knapp.

Begründung: Die 1.904-Zahl und die 300-Beerdigungen-Zahl sind in FAQ-Schema.org verankert und werden damit potenziell als Google-Featured-Snippet ausgespielt. Eine als verbindlich präsentierte Zahl ohne Primärquelle in strukturierten Daten ist YMYL-Risiko (Trust-Signal-Beschädigung). Die Schalke-Bestattungssoziologie ist kein Deploy-Blocker, aber drückt die Page unter Elite-Niveau.

Realistisch: Wenn 1.904 + 300 schnell verifiziert/abgesoftened werden und der Soziologie-Block raus oder hart ersetzt wird → deploy-ready bei ~88-90.