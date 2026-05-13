Ich lade die drei Dateien und prüfe v3 adversarial.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

Ich prüfe v3 gegen die Round-4-MUST-FIX-Liste und suche neue Schwächen.

Check der Round-4-MUST-FIX-Punkte:

2007 → 2005 islamisches Grabfeld: ✓ Behoben (Keyfacts: "seit 2005", Hidden Gem Reuschenberg: "seit 2005 — also bereits neun Jahre, bevor die BestG-NRW-Novelle 2014", FAQ sichtbar: "seit 2005", FAQ JSON-LD: "seit 2005"). Auch "neun Jahre" konsistent angepasst.
Jüdischer Friedhof Opladen 2016/2017-Konsistenz: ✓ Behoben — FAQ sagt jetzt "Wiedereröffnung am 5. Dezember 2016 genehmigt … seit 2017 wieder vereinzelt Bestattungen möglich". Konsistent mit Hidden Gem.
Personennamen Reuschenberg: ⚠️ Anders gelöst — die spezifischen Namen (Lützenkirchen, Henning, Mierbach, Richartz, Lappe, Krettek) sind GESTRICHEN und durch generischere Formulierung ersetzt: "dokumentierte Ehrenringträgerinnen und Ehrenringträger der Stadt sowie kommunalpolitisch prägende Persönlichkeiten der vergangenen Jahrzehnte. Eine vollständige Liste der Persönlichkeitsgräber führt das Stadtarchiv". Risiko-Vermeidung statt Verifikation. Akzeptabel.
Lützenkirchen-Verwechslung: ✓ Klarstellung im Sammelabsatz: "namensgleich mit dem Stadtteil, aber nicht zu verwechseln mit Persönlichkeiten gleichen Namens".
Jüdischer Friedhof harte Zahlen: ✓ Teilweise behoben — explizite Quellenanker hinzugefügt: "laut KuLaDig-Dokumentation des LVR", "Nach Stadtarchiv-Angaben erwarb die Stadt … am 8. März 1943 … für 1.244 Reichsmark", "Quelle für die Datierung und die Bildhauer-Zuordnung: KuLaDig (LVR) und die Online-Dokumentation jüdischer Gemeinden". Source-Liste #11 und #12 verweisen explizit auf die jeweiligen Zahlen.
"Familiengeschichtliches Archiv im Stein" ✓ Floskel gestrichen.

Jetzt suche ich neue Schwächen.

Suche nach neuen Schwächen — ich verifiziere zwei kritische Behauptungen.

Web durchsucht
Web durchsucht

Wichtiger Befund: Die v3 sagt "der seit 1988 weitgehend geschlossen" für Manfort — Sekundärquelle (friedhof.city) sagt "Seit 1988 ist der Friedhof für neue Sargbestattungen und den Erwerb von Wahlgräbern geschlossen". Belegt durch Sekundärquelle, aber NICHT in Source-Liste verlinkt → keine Primärquelle.

Architekt der Trauerhalle Manfort: v3 erwähnt KEINEN Architekten. Aber: Sekundärquellen (lebenshimmel, friedhof-ansichten) sagen "1917/18 erbaute Kapelle … von Wilhelm Fähler entworfen". v3 schreibt nur "unter Denkmalschutz stehende, repräsentative Trauerhalle" ohne Baujahr — vorsichtig. Akzeptabel.

Architekt Reuschenberg: v3 schreibt "1954/55 nach Plänen des Architekten Kurt-Wilhelm Rink". Diese spezifische Behauptung verifiziere ich.

Web durchsucht
Web durchsucht

Architekt Rink ✓ belegt (leverkusen.com).

Neuer Befund — interner Widerspruch zur Memoriamgarten-Reihenfolge:

v3 Manfort-Block sagt: "seit 2013 den zweiten Memoriamgarten Leverkusens"

v3 Sammelabsatz sagt: "Birkenberg … der erste Memoriamgarten der Stadt befindet sich hier"

Das ist konsistent (Birkenberg = 1., Manfort = 2.). ✓ OK.

Aber neu kritisch: v3 schreibt Manfort: "bis heute flächenmäßig die größte Friedhofsanlage der Stadt" und gleichzeitig: "Für neue Sargbestattungen und den Erwerb klassischer Wahlgräber ist der Friedhof allerdings seit 1988 weitgehend geschlossen". Das 1988-Datum ist nur durch Sekundärquelle (friedhof.city) belegt, nicht in der Quellenliste. Halluzinationsverdacht-Restrisiko. Mittlere Gewichtung.

Neuer Floskel-Check:

"sehr eigenen Friedhofslandschaft" — Round-4 hat das bereits angemerkt, bleibt in v3 (Hero)
"in dichter Folge" / "stille Variante derselben rheinischen Tradition" — Schlebusch — kreatives Schreiben, aber sachlich
"dichtes Mahnmal-Ensemble" — Manfort Hidden Gem — bleibt, war Round-4-Befund, nicht gefixt

Cross-Link-Check: Nur ein Quer-Link zur NRW-Bundesland-Seite. Round-4-Befund — NICHT behoben. Keine Verlinkung zu Nachbarstädten, Vorsorge, Ratgeber.

Reuschenberg Adressen-Quelle: "Auf dem Weierberg 11, 51373" — wird mehrfach gegen Sekundärquellen geprüft, aber keine Source direkt verlinkt. Niedrig-Priorität.

Zwangsarbeiterzahl 270 — verifizierbar?

Web durchsucht
Web durchsucht

KRITISCHER NEUER FUND: v3 schreibt: "Bayer im Ersten Weltkrieg vom 27. Mai 1917"

Primärquelle (leverkusen.com Inschrift): "großen Explosion am 27. Januar 1917"

Das ist ein FAKTENFEHLER beim Datum der Bayer-Explosion. v3 sagt 27. Mai 1917, korrekt ist 27. Januar 1917 (laut Gedenkstein-Inschrift selbst).

Außerdem: v3 sagt "270 Zwangsarbeiterinnen und Zwangsarbeiter aus Polen, Russland, der Ukraine, Frankreich und den Niederlanden". lev-touren-Quelle bestätigt "270 Opfer in einem Gräberfeld bestattet" — Zahl OK. Die Nationen-Aufzählung steht im v3 ohne explizite Quelle, lev-touren.de ist als Source #14 verlinkt, daher belegt.

FAQ JSON-LD vs. FAQ-Anzeige Inkonsistenz prüfen:

FAQ JSON-LD "Wo wird in Leverkusen ein Sterbefall beurkundet?" Antwort endet mit: "die Beurkundung über den eingerichteten Schnellschalter."

FAQ sichtbar gleiche Frage endet mit: "Angehörige können Sterbeurkunden auch online über das Kommunalportal nachfordern." — Zusätzlicher Satz nur in sichtbarer FAQ.

FAQ JSON-LD "Welche Fristen" stimmt überein.

FAQ JSON-LD "Wie lang sind die Ruhezeiten" stoppt nach "unabhängig von Friedhof und Grabart."

FAQ sichtbar "Wie lang sind die Ruhezeiten" hat zusätzlichen Satz: "Reihengräber sind nicht verlängerbar, Wahlgräber können frühestens ein Jahr vor Ablauf des Nutzungsrechts verlängert werden."

→ FAQ-Schema und FAQ-Anzeige sind inhaltlich nicht 100% identisch. Google FAQ-Rich-Result-Guidelines fordern: FAQ-Schema muss inhaltlich mit der sichtbaren Antwort übereinstimmen. Bei Ergänzungen ist das technisch toleriert, aber suboptimal. Mittlere Schwere.

Floskel-Reste prüfen: "sehr eigenen Friedhofslandschaft" (Hero) — bleibt. "in dichter Folge" — bleibt (akzeptabel). "stille Variante" — bleibt.

Cross-Links: Wie Round-4 angemerkt, weiterhin nur 1 Quer-Link (NRW). Nichts zu Köln, Düsseldorf, Vorsorge, Ratgeber. Nicht behoben.

Wortzahl-Check: ~2.850 Wörter, im Korridor ✓.

Genug Material. Ich bewerte.

SCORE: 84/100

FUNDE:

FAKTENFEHLER (kritisch, neu, vorher nicht gefunden): Bayer-Explosion-Datum. Hidden Gem Manfort schreibt "Sprengstoff-Explosion bei Bayer im Ersten Weltkrieg vom 27. Mai 1917". Primärquelle (Gedenkstein-Inschrift selbst, dokumentiert über leverkusen.com) sagt eindeutig 27. Januar 1917. Round-4 hat das nicht erwischt, weil der Befund neu hinzugekommen ist. FIX: "27. Januar 1917" — das Datum steht wörtlich auf dem Gedenkstein.
FAQ-Schema vs. FAQ-Anzeige nicht synchronisiert. Zwei FAQ-Antworten enthalten in der sichtbaren Version Sätze, die im JSON-LD fehlen: "Sterbeurkunde online über Kommunalportal nachfordern" (Frage Sterbefall) und "Reihengräber nicht verlängerbar / Wahlgräber-Verlängerung ein Jahr vor Ablauf" (Frage Ruhezeiten). Google FAQ-Rich-Snippet-Policy fordert wörtliche Übereinstimmung. FIX: Schema-Texte an sichtbare FAQ angleichen oder umgekehrt.
1988-Datum Manfort-Schließung unbelegt in Sources. v3 behauptet "seit 1988 weitgehend geschlossen". Sekundärquelle (friedhof.city) hat diese Aussage, ist aber NICHT in der Sources-Liste (15 Einträge). Bei Datums-Spezifikum dieser Härte braucht es entweder Quellenanker im Text oder einen Source-Eintrag. Halluzinationsverdacht-Restrisiko. FIX: friedhof.city oder eine bessere Primärquelle (Stadtarchiv) ergänzen oder Formulierung weicher: "seit Ende der 1980er-Jahre".
Cross-Link-Lücke nicht behoben. Round-4-Befund bleibt: nur ein Quer-Link (NRW-Bundesland). Keine Verlinkung zu Nachbarstädten (Köln, Düsseldorf, Solingen), keine zu Vorsorge oder Ratgeber. Für eine Portal-Stadtseite zu dünn. Niedrige Schwere, aber Round-4-Punkt nicht adressiert.
Hero-Floskel "sehr eigenen Friedhofslandschaft" bleibt. Round-4 implizit moniert ("Marketing-Floskel-Verdacht"). Verdichtung statt Streichung wäre besser ("eigene Friedhofslandschaft" reicht).

Was korrekt gefixt wurde: 2007 → 2005 islamisches Grabfeld (4 Stellen + neun Jahre); 2016/2017 jüdischer Friedhof Konsistenz; Reuschenberg-Personennamen entschärft statt halluziniert; Lützenkirchen-Stadtteil-Klarstellung; jüdischer Friedhof Quellenanker (KuLaDig, Stadtarchiv, Bildhauer); "familiengeschichtliches Archiv im Stein" gestrichen.

MUST-FIX vor Deploy: JA

Begründung: Das Bayer-Explosion-Datum ist ein harter Faktenfehler (Mai statt Januar 1917) auf einer Page, die historische Tiefe als Qualitätsmerkmal verkauft — der Stein selbst ist die Quelle, und die Quelle widerspricht dem Text. Das ist die Sorte Fehler, die ein lokaler Leser in 30 Sekunden findet und bei der Vertrauen verloren geht. Ohne diesen Fix kein Deploy. FAQ-Schema-Sync ist Pflicht für Rich Snippets. 1988-Quellenanker und Cross-Links sind weniger kritisch, sollten aber bei der Gelegenheit mitgehen.

Score-Begründung 84: Die zwei großen Round-4-Faktenblocker (2005/2007 und 2016/2017) sind sauber behoben, jüdischer Friedhof hat jetzt Quellenanker, Personennamen-Halluzination ist entschärft. Aber: ein neuer Faktenfehler (27. Mai statt Januar) wurde reingeschrieben, FAQ-Schema-Sync stimmt nicht, und zwei Round-4-Befunde (Cross-Links, Floskel) sind nicht adressiert. Über 85 erst nach 27.-Januar-Fix und FAQ-Sync.