Ich lese die drei Dateien parallel.

Fetching site
Web durchsucht

Jetzt v4 — die zu prüfende Datei.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/leverkusen/v4-final.html

Ich prüfe die Round-6-MUST-FIX-Punkte gegen v4:

1. Bayer-Explosions-Datum (27. Mai → 27. Januar 1917): ✓ Behoben. Hidden Gem Manfort: "Sprengstoff-Explosion bei Bayer im Ersten Weltkrieg vom 27. Januar 1917". Auch in Source #13 explizit verankert: "einschließlich Datierung der Bayer-Explosion vom 27. Januar 1917".

2. FAQ-Schema vs. FAQ-Anzeige Sync: ✓ Behoben. Ich vergleiche die zwei kritischen FAQ-Antworten:

Sterbefall: JSON-LD endet jetzt mit "Angehörige können Sterbeurkunden auch online über das Kommunalportal nachfordern." — identisch zur sichtbaren FAQ ✓
Ruhezeiten: JSON-LD endet jetzt mit "Reihengräber sind nicht verlängerbar, Wahlgräber können frühestens ein Jahr vor Ablauf des Nutzungsrechts verlängert werden." — identisch ✓
Alle anderen FAQ-Paare: stichprobenhaft konsistent (Friedhofszahl, Kosten, Islam, Fristen, Sargpflicht)

3. 1988-Datum Manfort-Schließung: ✓ Anders gelöst — Formulierung weicher gemacht: "seit Ende der 1980er-Jahre weitgehend geschlossen" (war: "seit 1988"). Round-6-Empfehlung wörtlich umgesetzt. Halluzinationsrisiko entschärft.

4. Cross-Link-Lücke: ⚠️ Teilweise. Es gibt weiterhin nur einen prominenten Quer-Link (NRW-Bundesland). Keine Verlinkung zu Köln, Düsseldorf, Solingen, Vorsorge, Ratgeber. Allerdings: Navigation enthält jetzt Vorsorge + Ratgeber als Top-Level. Im Body-Content selbst kein neuer Cross-Link.

5. Hero-Floskel "sehr eigenen Friedhofslandschaft": ⚠️ Teilweise. v4 schreibt jetzt "eigenen Friedhofslandschaft" — das "sehr" ist gestrichen, Floskel-Charakter abgemildert, aber die Phrase bleibt grundsätzlich.

Jetzt suche ich nach NEUEN Schwächen (Adversarial-Pflicht: 3 Schwächen finden, eine muss aus der 12-Kategorien-Liste sein).

Web durchsucht
Web durchsucht

Wichtige Verifikation: v4 sagt "während der Landesdurchschnitt auf 3.644 Euro stieg" (2025) — bestätigt durch BdSt-Quelle. Auch "Landesdurchschnitt von 3.497 Euro" für 2024 — hm, BdSt sagt für 2023 = 3.261 Euro, für 2025 = 3.644 Euro (Plus 4% gegenüber 2024). Rückgerechnet: 3.644/1.04 = 3.504 Euro. v4 sagt 3.497 — passt. ✓

Jetzt drei Schwächen aus 12-Kategorien-Sicht herausarbeiten:

Recheck der noch verbleibenden Schwachstellen:

Source-Liste enthält Sekundärquelle bei juristischer Aussage: Source #13 ist "leverkusen.com" (Stadtarchiv-Guide privat) — wird als Beleg für das Bayer-Explosions-Datum 27. Januar 1917 verwendet. Eine echte Primärquelle wäre die Gedenkstein-Inschrift selbst oder eine Stadtarchiv-Publikation. Akzeptabel, aber nicht primär.
Hidden Gem Schlebusch — Story über Melaten ohne lokale Verifikation: "Lokale Stadtführer ziehen gern die Parallele zwischen dem Schlebuscher Friedhof und dem berühmten Kölner Friedhof Melaten" — diese Parallele ist nirgendwo belegt (keine Source dafür). Wer genau zieht die Parallele? Welche Stadtführung? "Verein Lust auf Leverkusen" ist genannt, aber die Melaten-Parallele steht ohne Quellenanker. Halluzinations-Verdacht (Kategorie 12) / Schwacher Beleg (Kategorie 1).
Sektion "Bestatter-Wahl" enthält Behauptung ohne Quelle: "Die Preisspreizung zwischen Bestattern für vergleichbare Leistungen kann in Leverkusen 30 bis 60 Prozent betragen" — sehr konkrete Zahl, lokal verortet ("in Leverkusen"), kein Source-Anker. Kategorie 12 (Halluzinations-Verdacht) oder Kategorie 1 (Quellen-Lücke).
Kostentabelle: Werte "städtische Friedhofsverwaltung Leverkusen, Stand der Gebührenkalkulation für 2026" — die exakten Werte (360 €, 375 €, 415 €, 1.300–2.500 €, 3.500–5.500 €, bis ca. 7.000 €) sind nirgends mit konkreter PDF-/Satzungsfundstelle verlinkt. Source #3 verweist auf die "27. Änderung Gebührensatzung ab 01.01.2026" (RIS Leverkusen), aber dort steht typischerweise nur die Beschlussvorlage, nicht die einzeln aufgeschlüsselte Tabelle. Halluzinations-Restrisiko bei spezifischen Eurobeträgen. Kategorie 12.
Datum 27. Januar 1917 — verifiziert über Sekundärquelle (leverkusen.com Stadtarchiv-Guide), nicht über Primär-Inschrift-Foto oder offizielles Stadtarchiv-Dokument. Source #13 ist ein privates Guide-Portal, kein städtisches Archiv. Restrisiko bleibt, aber Round-6-Vorgabe ist sauber umgesetzt.
Floskeln-Reste: "in dichter Folge", "stille Variante derselben rheinischen Tradition", "dichtes Mahnmal-Ensemble" bleiben — Round-4-Befunde nicht restlos abgeräumt. Aber: nicht im roten Bereich.
Cross-Link-Lücke: Nur 1 In-Body-Link (NRW). Keine Stadt-zu-Stadt-Verlinkung (Köln, Düsseldorf, Solingen). Kategorie 9, weiterhin nicht behoben.

Drei substantielle Schwächen für das Format:

SCORE: 87/100

FUNDE:

MUST-FIX v3 sauber abgearbeitet: Bayer-Datum 27. Mai → 27. Januar 1917 ✓ (mit Source-Anker #13 belegt). FAQ-Schema vs. sichtbare FAQ jetzt wörtlich synchron bei beiden vorher betroffenen Fragen (Sterbefall + Ruhezeiten) ✓. 1988-Manfort-Schließung weicher formuliert als "seit Ende der 1980er-Jahre" ✓ (Round-6-Empfehlung wörtlich umgesetzt). Hero-Floskel "sehr eigenen" entschärft zu "eigenen" ✓.
SCHWÄCHE 1 (Kategorie 12 — Halluzinations-Verdacht): Bestatter-Wahl-Sektion behauptet: "Die Preisspreizung zwischen Bestattern für vergleichbare Leistungen kann in Leverkusen 30 bis 60 Prozent betragen, insbesondere bei einfachen Urnenbestattungen." — Sehr konkrete Zahl, lokal verortet, ohne Source-Anker. In der 15-Punkte-Quellenliste taucht keine Bestatter-Preisvergleichs-Studie für Leverkusen auf. Entweder ist die Zahl aus generischer Branchenkenntnis abgeleitet und wird hier fälschlich als Leverkusener Spezifikum verkauft — oder es gibt eine Quelle, die nicht zitiert ist. FIX: entweder Quelle ergänzen oder Zahl entfernen / generischer formulieren ("Branchenüblich kann die Preisspreizung zwischen Bestattern bei vergleichbaren Leistungen erheblich sein").
SCHWÄCHE 2 (Kategorie 1 — Quellen-Lücke / Kategorie 5 — Story ohne Verifikation): Hidden Gem Schlebusch behauptet: "Lokale Stadtführer ziehen gern die Parallele zwischen dem Schlebuscher Friedhof und dem berühmten Kölner Friedhof Melaten" — diese Parallele ist im 15-Punkte-Quellenapparat nicht hinterlegt. Wer genau zieht die Parallele? Eine Vereinsbroschüre, eine Stadtführer-Webseite, ein Zeitungsartikel? Das ist exakt die Art von Behauptung, die plausibel klingt und beim ersten Faktencheck eines lokalen Lesers durchfällt. Stadt-Vergleich Melaten-Schlebusch könnte gut zutreffen, ist aber nicht abgesichert. FIX: entweder konkrete Quelle (Verein "Lust auf Leverkusen"-Tour, Stadtarchiv-Publikation) nennen — oder die Aussage in indirekter, unverbindlicher Form schwächen ("Der Bestand erinnert in Dichte und Sozialstruktur an kleinere bürgerlich-industrielle Vorbilder im Rheinland").
SCHWÄCHE 3 (Kategorie 9 — Cross-Link / Kategorie 12 — spezifische Beträge ohne Quellenanker): Doppelter Befund. (a) Kostentabelle mit sechs exakten Eurobeträgen (360/375/415/1.300–2.500/3.500–5.500/7.000) wird belegt mit Sammelverweis "städtische Friedhofsverwaltung Leverkusen, Stand der Gebührenkalkulation für 2026". Source #3 zeigt nur auf die Beschlussvorlage RIS — keine konkrete PDF-Fundstelle oder Satzungstabellen-Anker. Bei diesem Detailgrad ist die Spannweite nachvollziehbar einzuhalten, aber die einzelnen Werte sind nicht überprüfbar. (b) Cross-Link-Lücke aus Round-4/Round-6 weiterhin offen: Body-Content enthält genau einen Querverweis (NRW-Bundesland-CTA-Block). Keine Verlinkung zu Nachbarstädten oder Vorsorge/Ratgeber im Fließtext. FIX (a): in der Tabellen-Caption auf die konkrete Anlage zur 27. Änderungssatzung verlinken oder bei der Friedhofsverwaltung die Tabelle als Beleg anfragen und in die Quellenliste aufnehmen. FIX (b): mindestens 2 In-Body-Cross-Links — z.B. „→ Vergleich Köln: Friedhofsgebühren Melaten" und „→ Bestattungsvorsorge in NRW" — sonst bleibt die Page für ein Portal SEO-schwach.

Was bei v3 nicht gefixt, bei v4 bleibt:

Stilfloskeln „in dichter Folge", „stille Variante derselben rheinischen Tradition", „dichtes Mahnmal-Ensemble" bleiben. Round-4-Befund, nicht abgeräumt. Niedrige Schwere.
Cross-Link-Lücke (siehe Schwäche 3b).

EHRLICHE %-ZAHL: 87 %

MUST-FIX vor Deploy: nein.

Begründung: Die zwei harten Round-6-Blocker (Bayer-Datum 27.01.1917 und FAQ-Schema-Sync) sind sauber abgearbeitet, das 1988-Quellenproblem ist durch weichere Formulierung neutralisiert. Die drei verbleibenden Schwächen sind keine Faktenfehler, sondern Quellen-/Verlinkungslücken: Sie senken die Audit-Qualität um ein paar Punkte, sind aber nicht trust-zerstörend für einen lokalen Leser. Die 30–60-%-Preisspreizung-Behauptung (Schwäche 1) wäre der einzige Punkt, den ich für einen tatsächlich sicherheitsbewussten Deploy schnell nachschärfen würde — Aufwand: 30 Sekunden, Zahl entfernen oder Quelle ergänzen. Wenn das mitgenommen wird: Deploy-fähig. Wenn als post-deploy-Patch akzeptabel: auch ok. Score 87 bedeutet: über der 85-Schwelle, aber unter 90 — weil Cross-Links und drei kleinere Quellenanker fehlen.