Ich lade die Datei und prüfe Pass 2.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/wuppertal/index.html

Prüfe die Major-Punkte systematisch:

1. FAQ-Schema vs HTML Mismatch (§ 13 Sync-Check):

Schema § 13: "Sargpflicht bei Erdbestattung" (knapp)
HTML § 13: "Sargpflicht bei Erdbestattung mit Ausnahmen für religiöse Bestattungen"
→ Leichte Asymmetrie, aber nicht widersprüchlich. Akzeptabel.

2. § 8 Aschebeisetzung-Sync:

Schema § 8: "Bestattungsfristen" ✓
Schema § 14: "Aschebeisetzung auf einem Friedhof, Friedhofszwang" ✓
HTML § 14: "Friedhofszwang, Aschebeisetzung" ✓
HTML-FAQ § 14: "Friedhofszwang, auch für Aschen" ✓
→ Konsistent.

3. PLZ-Check:

Standesamt Johannes-Rau-Platz 1: HTML sagt 42275 Wuppertal-Barmen
Memory-Vorgabe war "PLZ 42269" – aber: Tatsächliche PLZ Johannes-Rau-Platz 1 ist 42275 (Barmen-Mitte/Werth). 42269 ist Oberbarmen/Wichlinghausen.
→ HTML hat 42275 – das ist korrekt. Memory-Trigger "PLZ 42269" war offenbar der Improver-Auftrag, der korrekt umgesetzt wurde (oder Bolle hatte den Trigger falsch im Kopf). HTML-Wert 42275 ist faktisch richtig.

4. § 28 PStG Werktag-Klausel:

HTML: "spätestens am dritten Werktag … Samstag gilt nicht als Werktag"
§ 28 PStG sagt: "spätestens am dritten auf den Tod folgenden Werktag". Samstag-Ausschluss ist eine zusätzliche Behauptung – tatsächlich gilt Samstag standesamtlich nicht als Werktag (§ 193 BGB-Analog wird angewendet bei geschlossenen Ämtern). Vertretbar.

5. Krummacher-Postleitzahl:

Schema + HTML: Krummacherstraße 35, 42119 Wuppertal-Elberfeld
Tatsächliche PLZ Krummacherstr. 35: 42115 (Elberfeld-Mitte/Brill). 42119 ist Elberfeld-West/Cronenberg-Grenze.
→ MÖGLICHER PLZ-FEHLER – Check nötig.
Searching the web
Web durchsucht

Schwere Funde:

Friedhof Krummacherstraße ADRESSE FALSCH – HTML/Schema sagt "Krummacherstraße 35, 42119" – korrekt ist Krummacherstr. 25, 42115 Wuppertal. Beide Komponenten (Hausnummer + PLZ) sind falsch. Schema-Block + HTML-Hero. 
Fvwuppertal
Friedhof Krummacherstraße INHALTSFEHLER (Halluzination) – HTML beschreibt ihn als "reformiert-protestantische" Anlage, "Begräbnisplatz der reformierten Gemeinde Elberfelds … im 19. Jahrhundert angelegt", "Theologen-Familie Krummacher" namensgebend. Realität: "Der Friedhof Krummacherstraße, auch Friedhof Varresbeck genannt, wurde 1902 eröffnet. Er ist parkähnlich nach dem Vorbild des Ohlsdorfer Friedhofs in Hamburg angelegt." Träger ist der Evangelische Friedhofsverband Wuppertal (uniert, nicht reformiert-spezifisch), Gründung 1902 (nicht 19. Jh.), Vorbild Ohlsdorf. Das ist eine massive narrative Halluzination. 
Fvwuppertal
Friedhof Unterbarmen – HTML: "Lönsstraße 65, 42283". Tatsächlicher Unterbarmer Friedhof liegt an der Unterdörnen / Lönsstraße; PLZ 42283 ist Barmen – plausibel, aber Hausnummer 65 nicht verifiziert. Niedrigere Priorität.

STADT: Wuppertal VERDICT: MAJOR-FIX

Fund 1 — Friedhof Krummacherstraße: Adresse falsch (Schema + HTML)

Wo: JSON-LD #friedhof-krummacher + H3-Block "Friedhof Krummacherstraße"
Ist: "Krummacherstraße 35, 42119"
Fix: Krummacherstraße 25, 42115 Wuppertal-Elberfeld (Quelle: fvwuppertal.de)

Fund 2 — Friedhof Krummacherstraße: Halluzinierte Narrative (Inhaltsfehler)

Wo: H3 "Friedhof Krummacherstraße — Gedächtnis der reformierten Bürgerschaft" + Schema-Description
Ist: "im 19. Jahrhundert als Begräbnisplatz der reformierten Gemeinde Elberfelds angelegt", "reformiert-protestantische Tradition", Krummacher-Familie als Namensgeber suggeriert
Fix: Faktisch ist es der Friedhof Varresbeck, eröffnet 1902, evangelisch (Friedhofsverband Wuppertal), parkartig nach Ohlsdorfer Vorbild. Reformiert-Narrativ + 19.-Jh.-Datierung streichen. Section komplett umschreiben oder durch faktentreuen Block ersetzen.

Fund 3 — Krummacher-PLZ in Hero-Anlauftext implizit

Wo: Lead-Paragraph "Friedhof Krummacherstraße bewahrt das Erbe der reformiert-protestantischen Bürgerschaft Elberfelds"
Fix: Aussage synchron mit Fund 2 entschärfen (evangelisch, nicht reformiert-spezifisch).

Hinweis: PLZ-Trigger "42269" aus Auftrag = nicht im File präsent; Standesamt steht korrekt mit 42275 (sachlich richtig). FAQ-Schema/HTML synchron für § 8/§ 13/§ 14. Krummacher ist das einzige, aber harte Problem — Deploy-Blocker.