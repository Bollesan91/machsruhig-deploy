Ich lade die drei Dateien und prüfe den MUST-FIX-Status.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

Alle drei Dateien geprüft. Adversariale Analyse von v3 gegen die Adv-v2-Befunde (79%):

MUST-FIX-Status-Check v2 → v3:

MUST-FIX 1 (Gebühren-Tabelle 2021-Sekundärquellen): Tabelle steht weiterhin mit 7 Positionen. Hinzugefügt wurde Spaltenüberschrift "Größenordnung (Sekundärquellen 2024)" und ein Hinweissatz. Aber: Keine Position aus dem aktuellen Gebührentarif 68.203.1 verifiziert. "Urnenbeisetzungsgebühr ca. 390 €" suggeriert weiterhin Genauigkeit. → NICHT vollständig gefixt, nur abgemildert.
MUST-FIX 2 (§§ BestG NRW): Komplett aufgelöst. § 13, § 14 Abs. 1 und § 8 Friedhofssatzung sind jetzt im Fließtext und in der FAQ mit Inhalt zitiert. → GEFIXT.
MUST-FIX 3 (Stiftung Warentest ohne Beleg): Stiftung Warentest komplett entfernt, neutral durch "Aeternitas und Verbraucherzentralen" ersetzt. → GEFIXT.

Nebenbefunde:

Footer-Link München: weiterhin auf /bestatter/muenchen/ (im Nav UND Footer) → NICHT gefixt.
Emma-Burmann UNSURE-Kommentar inkl. sichtbarer Klammer "(in der Wikipedia auch mit Geburtsjahr 1821 angegeben)" → NICHT gefixt.
Datum: dateModified jetzt 2026-05-15, Hero "Stand: 15. Mai 2026" → GEFIXT.

Neue Befunde in v3:

HTML-Kommentar <!-- UNSURE: ... --> ist im ausgelieferten HTML sichtbar (Quelltext) — unprofessionell für Production.
Süd-Adresse: "Am Südfriedhof 14e und 14k" im Text, Schema sagt nur "14e" — kleinere Inkonsistenz.
Bergmann-Skulptur-Provenienz (Gahlen → Grillo → Minidomm → 1994) weiterhin nur Sekundärquellen — von v2 ungefixt.

SCORE: 86/100

FUNDE:

SCHWÄCHE 1: Gebühren-Tabelle (Sektion „Bestattungskosten in Düsseldorf") — Die Tabelle präsentiert 7 €-Positionen mit Cent-Anmutung ("Urnenbeisetzungsgebühr ca. 390 €", "Sargbeisetzungsgebühr ca. 1.100 €"). Spaltenüberschrift "Sekundärquellen 2024" und der erläuternde Satz sind eine Abmilderung, aber keine Lösung — die Zahlen sind weiterhin nicht aus dem verlinkten Tarif 68.203.1 verifiziert, obwohl dieser direkt darunter steht. Bei einer YMYL-Page mit Tabellenformat-Autorität ist das das gleiche Risiko wie in v2: Wenn ein Leser die Beisetzungsgebühr im aktuellen Tarif anders findet, ist die Page angreifbar. Verbesserung: Mindestens 2 Positionen direkt aus dem aktuellen 68.203.1-PDF nachschlagen und mit "Stand 01.01.2026, Position X.Y" auszeichnen; die restlichen 3 Tabellenzeilen entweder gleichbehandeln oder rausnehmen. Eine halb-belegte Tabelle ist schlechter als eine kurze, vollständig belegte.

SCHWÄCHE 2: Sichtbarer Production-Müll im HTML — Im Quelltext steht <!-- UNSURE: Stadt Düsseldorf nennt 1831, Wikipedia 1821 — nicht eindeutig auflösbar. --> plus im Fließtext der sichtbare Halbsatz "(in der Wikipedia auch mit Geburtsjahr 1821 angegeben)". Das ist ein Pipeline-Artefakt aus dem Loop, der nicht in Production gehört — der Nutzer sieht ein unentschiedenes Redaktionsteam. Zusätzlich: Im Nav UND Footer zeigt der Bestatter-Link auf /bestatter/muenchen/ statt auf die Bestatter-Übersicht oder die aktuelle Düsseldorf-Page selbst. Beides war in Adv-v2 als Nebenbefund markiert und ist in v3 nicht gefixt. Verbesserung: Burmann-Datum entscheiden (Stadt-Quelle = 1831 nehmen, Wikipedia-Hinweis und HTML-Kommentar weg) ODER Burmann komplett streichen; Nav- und Footer-Link auf /bestatter/ (Übersicht) ändern.

SCHWÄCHE 3: Bergmann-Skulptur-Provenienz nur durch Blog gedeckt (Sektion Nordfriedhof/Millionenhügel) — Die Kette "ursprünglich Teil des Grabmals von Gahlen, später bei Grillo, dann im Freizeitpark Minidomm, seit 1994 wieder auf dem Friedhof" ist eine sehr spezifische 4-Stationen-Faktenkette mit Jahreszahl, die nur durch den "Public Sculptures"-Wordpress-Blog und ein Top-Magazin-Stück gedeckt ist — keine Primärquelle (Stadtarchiv, Friedhofsverwaltung, denkmalpflegerische Publikation). Bei einer Detailtiefe dieser Art ist das Halluzinations-Risiko real, weil Wordpress-Blogs untereinander zitieren und Fehler weitertragen. Schon in Adv-v2 markiert, in v3 unverändert. Verbesserung: Entweder Provenienz vorsichtiger formulieren ("Die Skulptur soll … gestanden haben") oder den Detailgrad reduzieren ("eine Bergmann-Skulptur, die früher außerhalb des Friedhofs stand und 1994 zurückkehrte") — die genaue Stationenkette ist für den Page-Wert nicht entscheidend.

MUST-FIX vor Deploy: ja.

Begründung: Zwei von drei v2-MUST-FIX sind sauber gelöst (§§ BestG NRW, Stiftung Warentest). Die Gebühren-Tabelle ist nicht gefixt, sondern nur kosmetisch entschärft — bleibt das größte Einzelrisiko. Der HTML-Kommentar plus sichtbarer Wikipedia-Hinweis im Fließtext ist ein Production-Blocker (Pipeline-Artefakt im Live-Text). Der Bestatter-Link auf München in Nav und Footer ist auf einer Düsseldorf-Page peinlich. Score 86: ohne Tabellen-Fix und ohne Burmann/Footer-Putz nicht über 85, mit beiden sauber gelöst klar 89–90.