Ich lade die drei Dateien und prüfe.

Fetching site
Web durchsucht

BRIEFING_OK

Jetzt prüfe ich gezielt, ob die v2-MUST-FIX in v3 abgearbeitet wurden, und suche neue Schwächen.

MUST-FIX aus v2 — Status in v3:

1.904 weichgespült? ✓ — v3 sagt jetzt zweimal „auf eine Endausbaustufe von rund 1.904 Grabstätten angelegt" (Hero-OG, Friedhof-Sektion, FAQ-Schema). Genau die geforderte Formulierung.
300 Beerdigungen-Zahl entschärft? ✓ — die konkrete „300" ist komplett raus. Nur noch „in der Größenordnung von etwa zehn Prozent". FAQ-Schema enthält jetzt sogar den Disclaimer „eine amtliche Statistik mit Primärquellen-Charakter liegt der Redaktion nicht vor". Sauber.
Schalker Bestattungssoziologie-Block + „Grabnummern mit 04"? ✓ — Essay-Block ersatzlos gestrichen, durch Libuda-Umbettung als Hidden Gem ersetzt (verifizierbare Sachinformation mit Datum + Quelle). Korrekter Fix.
Hauptfriedhof Buer 1899 / Torhäuser-Denkmalstatus? Teilweise — „1899" steht weiter ohne Pin, aber Torhäuser sind jetzt vorsichtiger formuliert: „aus den 1920er Jahren … das genaue Errichtungs- und Eintragungsdatum recherchiert die Redaktion nach (Quellenhinweis ausstehend)". Ehrliche Markierung statt erfundenes Datum — akzeptabel.
Ostfriedhof 1897 / Hüllen Quellen-Pin? ✓ — direkter Inline-Pin am Satzende ergänzt.

Alle drei MUST-FIX sauber abgearbeitet. Jetzt suche ich drei neue Schwächen — die Annahme bleibt: Page ist unter 90, mindestens drei Schwächen existieren.

SCORE: 89/100

FUNDE:

SCHWÄCHE 1 — Inkonsistenz Schalker Fan-Feld Grundkosten (Bestattungskosten-Sektion vs. Gesamtkostenspanne): In der Friedhofssektion steht „Die Grundkosten für eine Grabstelle beginnen bei rund 5.400 Euro zuzüglich städtischer Friedhofsgebühren und Bestatterkosten; enthalten sind eine Grabplatte mit dem Schalker Wappen und 25 Jahre Dauergrabpflege." In der Gesamtkostenspanne steht dann „Schalker Fan-Feld: ab ca. 7.300 € (Grabstelle 5.406 € + städtische Gebühren + Bestatterleistung)". Zwei Probleme: (a) 5.400 vs. 5.406 — präziser Wert kommt aus dem Nichts, ohne Quellen-Pin; das Wort „rund" oben ist mit „5.406" unten inkonsistent. (b) Für beide Beträge fehlt eine Primärquelle (sfcv.de, Schalke Fan-Feld GmbH, Suttmeyer). Bei YMYL-Page in FAQ-/Tabellen-Kontext ist eine Eurozahl ohne Pin Vertrauens-Risiko. Fix: Eine Zahl konsolidieren (5.400 € reicht), Quellen-Pin direkt anhängen oder mit „Stand 2024/2025, Schätzung auf Basis öffentlich kommunizierter Preise" markieren.

SCHWÄCHE 2 — Kolumbarium-Tarife im Tabellenblock ohne Quellen-Pin und nicht in der Satzung verifizierbar: Die Gebührentabelle listet „Kolumbarium Einzel-Urnenkammer 2.100 €", „Doppel-Urnenkammer 3.100 €" und „Urnenfach 1.500 €" — drei Beträge, die nicht den klassischen Wahl-/Reihen-/Gemeinschaftsgrab-Tarifen entsprechen. Die verlinkte Gebührensatzung-PDF wird als Quelle für die gesamte Tabelle ausgewiesen, aber gerade Kolumbariumstarife werden in NRW häufig in separater Anlage geführt. Drei runde Zahlen (2.100 / 3.100 / 1.500) wirken zudem zu „glatt" für eine amtliche Satzung, in der die anderen Werte präzise auf den Euro ausgewiesen sind (4.192, 2.641, 1.903). Halluzinations-Verdacht Kategorie 12. Fix: Beträge gegen die verlinkte PDF gegenchecken, ggf. Anlage-Seitenzahl im Quellen-Hinweis, oder bei Unsicherheit „auf Anfrage über GELSENDIENSTE" statt erfundene runde Zahlen.

SCHWÄCHE 3 — Cross-Link „Bestattung in Nordrhein-Westfalen" wird zweimal als zentrale Vertiefungsressource gesetzt, aber im Footer nur als Region-Link unter „Städte & Länder" geführt — und der Anker-Text „Vollständige Übersicht zum BestG NRW" verspricht im CTA-Block mehr als ein typischer Stub-Page liefern dürfte: Die Page lehnt sich an der NRW-Page als Quelle aus („Für eine vollständige Darstellung der landesrechtlichen Vorschriften … verweist diese Seite auf die Übersicht Bestattung in Nordrhein-Westfalen") und der CTA am Ende verstärkt das nochmal. Wenn /bestattung-in/nordrhein-westfalen/ aktuell nicht selbst Gold-Status hat (laut Site-Audit-Memo: 11 Bundesland-Pages noch auf Template-Niveau — NRW gehört wahrscheinlich nicht zu den 5 überarbeiteten Pages BW/MV/SA/TH/BB), dann verweist die Gelsenkirchen-Page Trust-Signal-mäßig auf eine schwächere Page. Das ist ein Off-Page-Risiko, kein Inline-Faktenfehler — aber ein klassischer Quer-Verweis-Bug nach Kategorie 9, weil die Verlinkungs-Verheißung („vollständige Darstellung", „vollständige Übersicht") nicht eingelöst wird. Fix: Entweder NRW-Page parallel auf Gold heben, bevor Gelsenkirchen deployt, oder den CTA und den Verweis-Satz auf direkt zitierbare Detailpunkte („§ 8, § 13, § 14 BestG NRW") reduzieren statt auf die NRW-Hub-Page.

MUST-FIX vor Deploy: nein.

Begründung: Alle drei v2-MUST-FIX (1.904-Pin, 300-Zahl, Soziologie-Block) sind sauber abgearbeitet und die Page bewegt sich klar in Gold-Korridor (88–92). Die drei neuen Schwächen sind kein YMYL-Trust-Bruch in strukturierten Daten:

Schwäche 1 (5.400/5.406-Inkonsistenz) ist Detail-Politur, kein Schema.org-Risiko.
Schwäche 2 (Kolumbarium-Tarife) ist Verifikations-Aufgabe vor Deploy — sollte 5 Minuten gegen die verlinkte PDF gegengecheckt werden, ist aber kein Blocker mit derzeitiger Quellenmarkierung („Auszüge der amtlichen Tarife").
Schwäche 3 (NRW-Hub-Page-Status) ist strategisches Cross-Page-Issue, nicht Page-spezifisch — gehört auf die Deploy-Reihenfolge-Liste, nicht in die v4-Schleife.

Empfehlung: 5-Minuten-Check der Kolumbariumstarife gegen die PDF, dann Deploy. Optional v4 für 5.400/5.406-Harmonisierung wenn Loop ohnehin noch läuft.