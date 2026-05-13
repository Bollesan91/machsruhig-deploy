Ich lese erst Briefing und v1.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Web durchsucht

BRIEFING_OK

SCORE: 72/100

FUNDE (Quellenanker / Faktenfehler / Struktur-Lücken / Marketing):

Quellenanker / Faktenfehler:

§ 9 BestattG Niedersachsen: 10-Tage-Frist wird in der Page als „Erdbestattungen sollen innerhalb von zehn Tagen … erfolgen" zitiert. Tatsächlich ist die Frist im NBestattG meist als „Bestattungen müssen innerhalb von 8 Tagen nach Eintritt des Todes" formuliert (frühere Fassungen sahen 10 Tage vor). Bitte gegen aktuelle Fassung verifizieren – im Zweifel ist hier ein Faktenfehler, der den Audit komplett kippen kann.
§ 11 BestattG als Sargpflicht-Paragraph: Sargpflicht in Niedersachsen ist nicht eindeutig in § 11 verankert – bitte verifizieren, dass § 11 (oder § 12) tatsächlich die Sargpflicht und nicht z.B. Friedhofszwang regelt. Wenn Paragraf falsch, schwere Quellenanker-Verletzung.
§ 8 BestattG (Bestattungspflicht): Reihenfolge in Niedersachsen unklar – das NBestattG nennt typischerweise: Ehegatte/Lebenspartner, volljährige Kinder, Eltern, Großeltern, Geschwister, Enkel. Die Reihenfolge „Großeltern vor Enkeln" muss gegen den Gesetzestext geprüft werden, der Text der Page setzt Geschwister vor Großeltern – das ist verdächtig. Konkret im NBestattG prüfen.
Aussage „zweitgrößter kirchlicher Friedhof Deutschlands" – wird der Friedhofsverwaltung Braunschweig zugeschrieben. Quelle prüfen: Stahnsdorf bei Potsdam wird oft auch als „größter Waldfriedhof" geführt; die Aussage „kirchlicher Friedhof" ist eng. Belastbar?
Magnifriedhof „seit 1720": Die Page sagt einleitend „seit 1720", später aber „Ab 1755 verlegte Braunschweig seine Kirchhöfe nach außerhalb". Widerspruch in der Datierung. Was stimmt?
„Rieseberg-Morde 1933" – Mahnmal seit 6.7.1958: präzise, aber Quelle für dieses Detail fehlt im Quellenverzeichnis (nur Wikipedia Hauptfriedhof).
244 Tote 2. Weltkrieg, 56 Betonkreuze, 201 Zwangsarbeiter, fünf Sintigräber – sehr spezifische Zahlen ohne klar zugeordnete Primärquelle. Wikipedia Katholischer Friedhof ist die mutmaßliche Quelle, aber Wikipedia ≠ Primärquelle. Schwach.
Naumburgstraße 25 als Sozialamt-Adresse: prüfen. Die Stadt-URL ist verlinkt, aber die Adresse direkt extrahiert? Falls falsch, kritischer Fehler für Nutzer.
„§ 651b BGB analog" für Bestatter-Kostenvoranschlag – juristisch fragwürdige Konstruktion. § 651b BGB betrifft Pauschalreiseverträge. Diese Analogie ist nicht etabliert. Streichen oder durch korrekten Verweis (z.B. § 632 BGB Werkvertrag, Vergütungsvereinbarung) ersetzen.

Struktur-Lücken:

Wortzahl: ca. 1.850 Wörter Fließtext (geschätzt). Unter Zielkorridor 2.000–2.500. Aufstocken nötig.
Nur 4 Friedhofsporträts, davon 1 (Welfengruft) explizit „kein Friedhof im klassischen Sinn". Der Stadtfriedhof Braunschweig wird mehrfach erwähnt (kommunaler Träger, konfessionell ungebunden), aber bekommt kein eigenes Porträt. Das ist die größte strukturelle Lücke: drei Friedhofsträger werden in den Kernfakten genannt, aber nur zwei Friedhöfe der Helmstedter Straße porträtiert.
Keine konkreten Bestatter-Empfehlungen, keine Adressen lokaler Bestatter, keine BDB-Mitgliederliste verlinkt.
Keine Verkehrsanbindung-Details außer „Straßenbahn seit 1954" beim Hauptfriedhof. ÖPNV-Linien, Parkplätze fehlen pro Friedhof.
Keine Cross-Links zu anderen Niedersachsen-Städten (Hannover, Osnabrück, Göttingen).
Schema.org: Place für Stadtfriedhof fehlt komplett (passend zur fehlenden Porträt-Sektion).
Hidden-Gems bei Hauptfriedhof: nur „Hermann Blumenau". Bei Katholischem Friedhof nur „Friedenspfad". Das ist eine pro Friedhof – ok, aber bei diesem Friedhof mit dieser Dichte (Büssing, Dedekind, Raabe, Schultze) müssten 2 Stories drin sein (z.B. Norbert Schultze und „Lili Marleen" – die Geschichte des Liedes).
Sozialbestattung: präzise, aber keine Kostenobergrenze genannt. Üblich sind ~3.000–4.000 € in Niedersachsen – das wäre eine konkrete Zahl, die der Nutzer braucht.

Marketing / Floskel-Detection:

Keine harten Floskeln gefunden. Page ist sprachlich diszipliniert.
„Konkurrenzsituation, die für Angehörige Vergleichsmöglichkeiten schafft" – grenzwertig werbliches Framing, aber inhaltlich vertretbar.
„bestattungsgeschichtlich eine der dichtesten Städte Niedersachsens" im Hero – unbelegte Superlativ-Aussage. Quelle oder Streichung.

MUST-FIX vor v2:

§ 9 NBestattG Frist verifizieren (8 oder 10 Tage?) und korrekt zitieren
§ 8 NBestattG Reihenfolge der Bestattungspflichtigen gegen Gesetzestext prüfen, ggf. korrigieren
§ 11 NBestattG als Sargpflicht-Norm verifizieren (oder korrekten § einsetzen)
§ 651b BGB analog streichen – juristisch falsch; durch § 632 BGB oder einfach „schriftlicher Kostenvoranschlag empfohlen" ersetzen
Stadtfriedhof Braunschweig als 5. Friedhofsporträt ergänzen (eigene Adresse, Größe, Eröffnungsjahr, mind. 1 Hidden-Gem oder Besonderheit) und entsprechend Schema.org-Place ergänzen
Magnifriedhof: Widerspruch „seit 1720" vs. „Ab 1755 verlegte Braunschweig seine Kirchhöfe" auflösen
„Zweitgrößter kirchlicher Friedhof Deutschlands": Primärquelle (nicht Wikipedia, nicht Friedhofs-Selbstdarstellung) liefern oder Aussage abschwächen
Hero: Superlativ „bestattungsgeschichtlich eine der dichtesten Städte Niedersachsens" belegen oder streichen
Wortzahl auf 2.000–2.500 ausbauen, primär durch Stadtfriedhof-Porträt und 1–2 zusätzliche Hidden-Gems (z.B. „Lili Marleen"-Story bei Schultze)
Sozialbestattung: konkrete Kostenobergrenze („einfache ortsübliche Bestattung") für Braunschweig recherchieren – Stadt-Vereinbarung mit Bestattern müsste eine Größenordnung nennen
Naumburgstraße 25 Adresse Sozialamt gegen Stadt-Website verifizieren
Cross-Links: mindestens 2 weitere Niedersachsen-Städte (Hannover, Göttingen) verlinken
Schwache Personenzahlen am Katholischen Friedhof (244/56/201/5): Primärquelle (Verein „Braunschweiger Friedhöfe e.V." oder Pfarrgemeinde) im Quellenverzeichnis ergänzen, nicht nur Wikipedia