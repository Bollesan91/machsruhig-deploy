Ich fetche die drei Dokumente und mache dann den Adversarial Review.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

Alle drei Dokumente liegen vor. Adversarial Review v3-Final:

SCORE: 78/100

FUNDE:

Heger-Friedhof Eröffnungsdatum 1925 vs. Wettbewerbsablauf intern inkonsistent. Im Fließtext steht: „Geplant wurde die Anlage nach dem Ersten Weltkrieg, eröffnet 1925." Direkt im Anschluss: „1927 schrieb die Stadt einen Architektenwettbewerb für die künstlerische Ausgestaltung aus … lediglich eine kleine Trauerhalle entstand. Erst 1935 erfolgte ein zweiter, beschränkter Wettbewerb." Plus: „Die ältere [Kapelle] stammt aus dem Eröffnungsjahr 1925, wurde 2008 vollständig saniert." Widerspruch: Wenn der Wettbewerb erst 1927 ausgeschrieben wurde, kann eine Kapelle nicht „aus dem Eröffnungsjahr 1925" stammen — es sei denn, sie ist ein Vorgängerbau vor dem Wettbewerb. Recheck.py Kategorie 4 (interne Konsistenz) würde anschlagen.
Heger-Friedhof Fläche 270.000 m² vs. „27 Hektar" — Rechenfehler bzw. Inkonsistenz. Kernfakten und Schema.org listen 270.000 m². Fließtext: „Mit einer Fläche von 27 Hektar". 27 ha = 270.000 m² ✓ rechnerisch korrekt — aber: keine der vorhandenen Quellen (Wikipedia Heger Friedhof, staerkt.osnabrueck.de) belegt diese exakte Zahl im verlinkten Quellenapparat. Recherchier-Falle: Wikipedia nennt für Heger meist ~27 ha rund — die exakte Punktzahl 270.000 wirkt fabriziert-präzise. Adversarial-Frage: Wo ist die m²-Zahl aus der Quelle 11 (Wikipedia Heger Friedhof) belegt?
„Sinnspruch über dem Krematoriumseingang" — Quelle fehlt. Zitat: „Flamme löse das Vergängliche, befreit ist das Unsterbliche". Hochspezifischer Wortlaut, in Anführungszeichen, ohne Beleg. Wenn der Spruch nicht exakt so dort steht (Wortlautvarianten existieren in der Feuerbestattungsbewegung), ist das eine wörtliche Falschzitation. Quelle 11 (Wikipedia Heger Friedhof) müsste das belegen — wenn ja, ist die Zuordnung ok; wenn nein, ist es ein Halluzinations-Verdacht (Briefing-Kategorie 12).
Anna Siemsen auf Hasefriedhof — Todesjahr fehlt, alle anderen haben es. Prominente-Liste Hase: „Justus Friedrich August Lodtmann († 1808)", „Bernhard Möllmann († 1897)" usw. — durchgehend mit Sterbedatum. Nur „Anna Siemsen (Pädagogin und Politikerin)" ohne Datum. Anna Siemsen starb 1951 in Hamburg — Beisetzung auf Hasefriedhof Osnabrück müsste belegbar sein. Inkonsistenz im Detail + möglicher Faktenfehler (Hasefriedhof war 1951 zwar noch aktiv bis 1995, aber war Siemsen tatsächlich dort beigesetzt?). Ohne Quelle riskant.
„Niedersächsisches Bestattungsgesetz seit dem 1. Januar 2006 in Kraft … 2018 umfassend novelliert." Quellenangabe 1 nennt „vom 8. Dezember 2005, zuletzt geändert durch Gesetz vom 20. Juni 2018 (in Kraft 01.01.2019)". Inkonsistenz: Die Novelle trat zum 01.01.2019 in Kraft, nicht „2018 umfassend novelliert" (kann man so formulieren, aber der spätere Satz „Mit der Novelle von 2018 wurde die Frist … Seit dem 1. Januar 2019 lautet § 9 Abs. 2 Satz 4" macht das ok). Marginalia — aber: „§ 8 BestattG (Reihenfolge der bestattungspflichtigen Angehörigen)" — in Niedersachsen ist die Bestattungspflicht in § 8 BestattG geregelt, das passt. Aber: Die genannte Reihenfolge „Ehe-/Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder" — Großeltern vor Enkelkindern? Im niedersächsischen § 8 Abs. 3 BestattG ist die Reihenfolge: 1. Ehegatten/Lebenspartner, 2. volljährige Kinder, 3. Eltern, 4. volljährige Geschwister, 5. Großeltern, 6. volljährige Enkelkinder — das passt tatsächlich so. Aber zur Verifikation: die Liste muss 1:1 dem Gesetzestext entsprechen, sonst Compliance-Problem.
Schwacher Übergang: „Die vier ausführlich beschriebenen Häuser umfassen die wichtigsten aktiven sowie die kulturhistorisch bedeutsamsten Friedhöfe." Das ist redaktioneller Meta-Satz, kein Übergang. Briefing-Kategorie 4.
Marketing-Floskel in Bestatterwahl-Sektion: „Die Wahl des Bestatters ist die wichtigste Einzelentscheidung beim Bestattungsablauf – sowohl wirtschaftlich als auch atmosphärisch." „Atmosphärisch" ist weich/marketing-nah. Recheck Kategorie „unsourced superlatives": „die wichtigste Einzelentscheidung" — nach welchem Maßstab? Marketing-Behauptung.
„Eine günstige Online-Feuerbestattung ohne Trauerfeier ist in Niedersachsen bereits ab rund 1.100 Euro … erhältlich." Konkrete Preisangabe ohne Beleg. Keine Quelle in der Liste deckt das. Briefing-Kategorie 1 + 12.
Quelle 16 (OVG-Beschluss) ohne Link/Fundstelle. Alle anderen Quellen verlinkt, diese eine nur als Textreferenz. Wiederholt das Pattern aus Adv-Vorrunde („eine Quelle ohne Link") in milder Form — Reviewer-Auge bleibt hängen.

MUST-FIX vor Deploy: ja.

Präzise:

Heger 1925/1927/1935-Widerspruch auflösen — entweder „eröffnet 1925" entfernen oder die „ältere Kapelle aus 1925" als Vorgängerbau (vor dem Hauptwettbewerb) klar einordnen mit Quelle.
Heger-Fläche 270.000 m² entweder mit konkreter Quellenfundstelle untermauern oder weichzeichnen („rund 27 Hektar").
Krematoriumsspruch „Flamme löse das Vergängliche…" verifizieren in Quelle 11 oder Anführungszeichen entfernen und paraphrasieren.
Anna Siemsen Todesjahr + Beisetzungsort Hasefriedhof belegen oder aus der Liste streichen.
„Online-Feuerbestattung ab 1.100 €" belegen oder generalisieren („deutlich günstiger als klassische Bestattung").
Bestatter-Sektion entfloskeln: „wichtigste Einzelentscheidung … atmosphärisch" durch sachliche Formulierung ersetzen.
OVG-Beschluss Quelle 16 mit Aktenzeichen-Fundstelle (z. B. Niedersächsisches Justizportal/openJur) verlinken — sonst gleiche Schwäche wie Vorrunde.
§ 8 BestattG Reihenfolge durch direkten Wortlaut-Abgleich mit Gesetzestext (Quelle 2 PDF) bestätigen oder § 8 Abs. 3 zitieren.

Der v2→v3-Sprung hat die alten Killshots (Satzungsdatum 9.12.2025, Phantasie-Preisspannen 1.220/990, 8-vs-10-Friedhöfe) sauber bereinigt — das ist deutlich. Aber v3 hat neue Substanz-Risiken eingeführt (Heger-Datierungskonflikt, unbelegte wörtliche Zitate, Einzelpreisbehauptung 1.100 €), die ein Auditor in der zweiten Lesung findet. 78/100 ehrlich, nicht 85+.