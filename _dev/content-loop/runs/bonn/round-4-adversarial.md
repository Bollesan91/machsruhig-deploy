Ich lade die drei Dateien.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

BRIEFING_OK.

SCORE: 79/100

FUNDE:

SCHWÄCHE 1: Burgfriedhof-Sektion — Halluzinations-Verdacht und Generik trotz expliziter MUST-FIX-Anweisung. Der Satz „Zu den bekanntesten hier Bestatteten zählt der Schriftsteller Carl Zuckmayer-Umfeld der Bonner Republik" ist erstens grammatisch kaputt (vermutlich AI-Reparatur eines Faktenfehlers — Zuckmayer ist in Saas-Fee/Schweiz begraben, nicht in Bad Godesberg), zweitens inhaltlich nichts-sagend („Umfeld"), drittens reiht sich nahtlos „die Familie der Rheinländer-Maler des 19. Jahrhunderts sowie mehrere Diplomaten der Bonner Jahrzehnte" an — drei Plural-Sammelbegriffe ohne einen einzigen verifizierbaren Namen. Round-2-Review-Punkt 9 forderte explizit Bad Godesberg in eigenen H3 mit belegbarer Bonn-Spezifik — Chat A hat die Sektion erstellt, aber mit genau der Generik gefüllt, die das Briefing rügt. Verbesserung: Zuckmayer-Satz streichen, stattdessen 2–3 verifizierbare Bestattete des Burgfriedhofs (z. B. Christian Bürgers, Hans Iven, Heinrich Lützeler — alle in der Wikipedia-Liste zum Burgfriedhof Bad Godesberg dokumentiert) mit Beruf und Lebensdaten.

SCHWÄCHE 2: Südfriedhof — „Peter Stockhausen" ist mit hoher Wahrscheinlichkeit halluziniert. Der Bonner CDU-Oberbürgermeister hieß Peter Kraemer (1975–1994) bzw. später Bärbel Dieckmann, Jürgen Nimptsch, Ashok-Alexander Sridharan, Katja Dörner. Einen Bonner OB namens „Peter Stockhausen" gibt es in der dokumentierten Liste der Bonner Oberbürgermeister nicht. Round-2-Review-Punkt 4 forderte 2–3 verifizierbare Bestattete — Chat A hat einen Namen erfunden, um das Loch zu stopfen. Das ist im YMYL-Kontext (lokale Stadt-SEO, Vertrauenssignal) ein deploy-blockender Fehler. Hermann Wandersleb bleibt der einzige belastbare Name, und selbst dort ist die Beisetzung auf dem Südfriedhof nicht gegenquellengeprüft im Text. Verbesserung: Stockhausen vollständig streichen; entweder per Wikipedia-Kategorie „Person (Bonn) → gestorben in Bonn" 2 verifizierbare Namen ergänzen oder die Sektion ehrlich als „keine systematische öffentliche Liste, einzelne Persönlichkeiten über Stadtarchiv" belassen und das Hidden-Gem komplett auf die Kriegsgräberstätte verschieben.

SCHWÄCHE 3: Friedhofssatzungs-Paragraphen fehlen weiterhin — MUST-FIX-Punkt 2 nicht erfüllt. Round-2 forderte „Konkrete Bonn-Ruhezeit recherchieren (Friedhofssatzung Bonn § X)". v2 liefert weiterhin nur „in Anlehnung an den Standard nordrhein-westfälischer Großstädte" mit UNSURE-Kommentar. Die Bonner Friedhofssatzung ist als PDF über bonn.de öffentlich verfügbar (§ 13 regelt Ruhezeit, dort steht der konkrete Wert). Dasselbe Muster bei der Gebührensatzung: MUST-FIX-Punkt 3 forderte „mindestens eine konkrete Zahl" — v2 liefert einen NRW-Korridor von Vergleichsstädten, nicht den Bonner Wert. Zwei der zehn MUST-FIX-Punkte sind also nicht erfüllt, sondern mit besser formuliertem UNSURE-Wrapping kaschiert. Verbesserung: Chat A muss die Satzung tatsächlich öffnen (bonn.de → Friedhofssatzung PDF) und mindestens die Ruhezeit-Paragraphennummer + einen Gebühren-Beispielsatz (z. B. Erdreihengrab Nutzungsgebühr) zitieren. Andernfalls bleibt der Score-Sprung von 72 auf 85+ rein kosmetisch.

ZUSATZ (nicht in 3er-Quote, aber Deploy-relevant):

datePublished 12.05.2026 und dateModified 15.05.2026 jetzt korrekt unterschiedlich. ✓
Schema Article hat jetzt image-Property. ✓
Nav-Link-Bug aus Round-2-Review (München als active) ist behoben — Bonn ist jetzt korrekt active. ✓
Floskel-Kontrolle sauber. ✓
Beethoven-Faden ist aufgelöst („Geburts-, nicht Sterbeort", Magnetgrab-Erklärung). ✓
Wortzahl auf rund 2100 Wörter gestiegen — unteres Drittel des Ziels (2200–2400), aber im Korridor.
3 UNSURE-Kommentare im Body — MUST-FIX-Punkt 6 erfüllt (≤3).
Standesamt-Adresse Berliner Platz 2 ist jetzt ohne UNSURE drin. ✓

MUST-FIX vor Deploy: ja.

Begründung: Schwäche 2 (vermutlich erfundener OB-Name) ist ein YMYL-Vertrauensbruch — eine konkrete Personenzuordnung zu einem Friedhof mit erfundenem Namen ist schlimmer als eine ehrlich generische Sektion. Schwäche 1 (Zuckmayer-Fragment + Generik-Plurale) ist die zweite Halluzinations-Front. Schwäche 3 (zwei nicht erfüllte MUST-FIX-Punkte als UNSURE getarnt) zeigt, dass die Pipeline Recherchetiefe-Punkte umetikettiert statt löst. Score 79 spiegelt: Form gut, Halluzinationsrisiko an zwei Stellen, Recherche-Schulden offen. Nicht deploy-ready.