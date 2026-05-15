Ich lade die drei Dateien und prüfe v2 adversarial.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

Ich gehe v2 jetzt adversarial durch. Drei Schwächen, keine Sycophancy.

Was mir beim Lesen sofort auffällt:

Schema.org FAQ "Ruhezeit" sagt: "Wahlgräber können auf Antrag in Schritten von mindestens 5 Jahren, maximal bis zu 30 Jahre, verlängert werden." — Das ist die Verlängerungs-Spanne, nicht die Ruhezeit. Die eigentliche Ruhezeit wird im Schema-Antworttext überhaupt nicht beantwortet. Body-FAQ nennt "Mindestruhezeit 15 Jahre in NRW" — Schema-FAQ nennt sie nicht. Das ist genau der Schema-vs-Body-Inkonsistenz-Trigger, den der v1-Review explizit als Blocker markiert hat.
Uerdinger Linie / ek-eck vs. esch-isch — der v1-Review (m8) hat ausdrücklich darauf hingewiesen: "Die Uerdinger Linie ist eine maken-machen Sprachgrenze, nicht ek/ich. Die ek/ich-Grenze ist die Benrather Linie." v2 hat das nicht korrigiert, sondern den Fehler vertieft: "Während südlich der Linie […] die Form 'esch/isch' gilt, gebraucht das Hölsch Plott die Form 'eck/ek'." Linguistisch falsch. Die Uerdinger Linie trennt ik/ich (maken/machen-Linie), nicht eck/esch.
HTML-Kommentar im Live-Code sichtbar — im Cornelius-de-Greiff-Listenpunkt steht <!-- UNSURE: Feldangabe C, Nr. 65–88 stammt aus Wikipedia/dewiki, ohne sie in v2 zu wiederholen, da Reviewer eine Primärquellen-Bestätigung verlangt -->. Das ist Autoren-Metakommentar, der versehentlich im ausgelieferten HTML steht. Sichtbar im Quelltext, peinlich vor Deploy, möglicherweise von Crawlern gelesen.
Mindestruhezeit "15 Jahre in NRW" — Body-FAQ behauptet das als Faktum. § 4 BestG NRW gibt aber keine bundesweit gültige NRW-Mindestruhezeit vor; das BestG NRW überträgt die Festsetzung an die Friedhofsträger. Die Zahl "15 Jahre" wird ohne Primärquelle (Krefelder Friedhofssatzung § X) genannt. Halluzinationsverdacht laut Briefing-Kategorie 12.
§-Verweis Sargpflicht falsch verortet — v2 schreibt: "Bei der Erdbestattung gilt nach § 13 Abs. 4 der Krefelder Friedhofssatzung Sargpflicht". § 13 BestG NRW regelt die Bestattungsfristen, nicht die Sargpflicht. Die Krefelder Friedhofssatzung hat ihre eigene Paragraphen-Zählung — Abs. 4 des § 13 dort ohne Beleg gesetzt. Riecht nach Paragraphen-Konfusion (§ 13 BestG vs. § 13 Satzung).
Floskel-Treffer: "sachliche Orientierung" (3×), "in der Seidenstadt am linken Niederrhein" — Briefing-Kategorie 11.

Drei substantielle Schwächen pflichtgemäß plus Bonus:

SCHWÄCHE 1: Im ausgelieferten HTML steht ein Autoren-Metakommentar <!-- UNSURE: Feldangabe C, Nr. 65–88 stammt aus Wikipedia/dewiki, ohne sie in v2 zu wiederholen, da Reviewer eine Primärquellen-Bestätigung verlangt --> im Prominente-Bestattete-Listenpunkt zu Cornelius de Greiff — Prozess-Notiz von Chat A, die nicht entfernt wurde. — Fix: HTML-Kommentar ersatzlos löschen vor jedem Deploy; Chat-A-Workflow um End-Sweep auf <!-- UNSURE / <!-- TODO ergänzen.

SCHWÄCHE 2: Uerdinger-Linie-Passage im Hidden-Gem Hüls ist linguistisch falsch — die Uerdinger Linie trennt ik/ich ("maken/machen"-Linie), nicht "esch/isch" gegen "eck/ek". Die eck/ich-Grenze ist die Benrather Linie, weiter südlich. v1-Review m8 hat exakt diesen Fehler markiert, v2 hat ihn nicht korrigiert sondern mit konkreten falschen Beispielwörtern verfestigt. — Fix: Entweder neu formulieren ("Hüls liegt nördlich der Uerdinger Linie, die das Niederfränkische vom Mittelfränkischen scheidet — 'maken' nördlich, 'machen' südlich") oder den Absatz streichen. Wikipedia-Artikel "Uerdinger Linie" als Primärquelle einsetzen.

SCHWÄCHE 3: Schema.org-FAQ "Wie lange ist die Ruhezeit auf Krefelder Friedhöfen?" beantwortet die Frage nicht — die Antwort beschreibt ausschließlich die Verlängerungs-Spanne (5/30 Jahre) für Wahlgräber. Die eigentliche Ruhezeit (Body nennt "15 Jahre Mindestruhezeit NRW") fehlt im Schema komplett. Damit Schema ↔ Body inkonsistent — derselbe Blocker-Typ wie in v1 (B6), nur jetzt durch Auslassung statt Widerspruch. Zusätzlich: Die Body-Aussage "Mindestruhezeit beträgt in NRW 15 Jahre" hat keine Primärquelle (BestG NRW überträgt die Festsetzung an Träger; pauschale 15-Jahre-Aussage für NRW ist nicht belegt). — Fix: Schema-FAQ-Antwort um konkrete Ruhezeit nach Krefelder Friedhofssatzung ergänzen (Sarg/Urne separat). Body-Aussage "15 Jahre in NRW" durch Krefelder Satzungs-§ ersetzen, Primärquelle in Sources nachziehen.

EHRLICHE %-ZAHL: 78%

SCORE: 78/100

FUNDE:

HTML-Kommentar <!-- UNSURE: ... --> im Live-Code (Chat-A-Prozessnotiz vergessen)
Uerdinger-Linie linguistisch falsch (esch/eck statt maken/machen) — v1-Hinweis m8 nicht umgesetzt, sogar verschärft
Schema-FAQ "Ruhezeit" beantwortet Frage nicht (nur Verlängerung) → Schema↔Body-Inkonsistenz
"Mindestruhezeit 15 Jahre in NRW" ohne Primärquelle, sachlich fragwürdig
"§ 13 Abs. 4 Krefelder Friedhofssatzung" für Sargpflicht — § konfundiert mit § 13 BestG NRW, ohne Beleg
Floskel "sachliche Orientierung" 3× + "Seidenstadt am linken Niederrhein" (Kategorie 11)
"Reichsfinanzminister 1848/49" für Hermann von Beckerath — korrekt ist Finanzminister im Reichsministerium der provisorischen Zentralgewalt; Begriff "Reichsfinanzminister" anachronistisch

MUST-FIX vor Deploy: ja

Begründung Must-Fix: HTML-Kommentar im Live-HTML ist nicht verhandelbar (peinlich, indexierbar). Uerdinger-Linie-Fehler war im v1-Review markiert und blieb stehen — wenn Loop-Output v1-Findings nicht abräumt, ist der Loop-Mechanismus selbst beschädigt. Schema-FAQ-Lücke triggert dieselbe Klasse Inkonsistenz, die in v1 schon Blocker war.