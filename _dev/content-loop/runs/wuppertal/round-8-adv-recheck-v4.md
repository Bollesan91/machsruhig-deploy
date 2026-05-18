Ich lese die drei Dateien parallel.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

Adversarial-Mindset an. v4 hat v3-Befunde adressiert — ich prüfe, ob das sauber gelungen ist, und suche neue Schwächen.

v3-Befunde Check:

❌ Krummacher-Genealogie → jetzt entschärft auf "Theologen-Familie Krummacher" + UNSURE-Kommentar + Verweis auf Stadtarchiv. ✓ Sauber
❌ Ruhezeit 25/20 Jahre → "Kindergräber bis 5. Lebensjahr 20 Jahre" ist komplett raus, nur noch "25 Jahre" + Microsite-Link, plus UNSURE-Kommentar. ✓ Sauber
❌ Bergische Trauerkultur → ersetzt durch deskriptive Aussage ohne Wertvergleich. ✓ Sauber

Jetzt frische adversariale Suche auf v4:

Befund A — Schema.org-Inkonsistenz beim Friedhof Krummacherstraße: Im JSON-LD steht für den Friedhof Krummacherstraße die Adresse "postalCode":"42119","addressLocality":"Wuppertal". PLZ 42119 ist Elberfeld-West/Uellendahl — die Krummacherstraße 35 liegt aber nach Stadtgeografie in Elberfeld (42105 oder 42107). PLZ 42119 ist sachlich wahrscheinlich falsch, im Fließtext steht hingegen korrekt "42119 Wuppertal-Elberfeld". Hier muss verifiziert werden — wenn PLZ 42119 falsch ist, ist es ein Schema.org-Faktenfehler, der bei Google Rich-Results-Test sichtbar wird.

Befund B — Standesamt-PLZ-Inkonsistenz: Hero/Schema/Keyfacts schreiben „Johannes-Rau-Platz 1, Barmen". Im Fließtext und FAQ steht: „Johannes-Rau-Platz 1, 42275 Wuppertal-Barmen". PLZ 42275 ist Wuppertal-Barmen — passt. Aber im FAQ-Schema (Q4) fehlt die PLZ ganz, und im Schema-Block gibt es überhaupt kein GovernmentOffice/Place für das Standesamt. Inkonsistenz zwischen Fließtext-Detail (42275) und Schema-Lücke ist ein E-E-A-T-Befund, sekundär. Wichtiger: Falls PLZ 42275 sachlich falsch ist — Johannes-Rau-Platz 1 ist die Adresse des Wuppertaler Rathauses (Barmen), das ist tatsächlich 42275. ✓ Plausibel, aber Schema sollte konsistent sein.

Befund C — Friedhof Unterbarmen "Engels-Frage" überfrachtet: Der ganze Absatz „Zur Engels-Frage" ist defensiv geschrieben — er reagiert offenbar auf einen früheren Adv-Befund („Engels ist nicht hier bestattet"). Aussage „Auf dem Friedhof Unterbarmen finden sich Gräber anderer Mitglieder der Familie Engels" ist eine konkrete Tatsachenbehauptung ohne Quelle. Welche Engels-Familienmitglieder genau? Das Geburtshaus liegt in Unterbarmen korrekt, aber die Bestattung anderer Engels-Familienmitglieder auf dem Friedhof Unterbarmen ist nicht belegt — das ist ein Halluzinations-Verdacht in Kategorie 12. Verbesserung: Entweder Quelle (Stadtarchiv/Engels-Haus-Museum) oder Aussage streichen / auf „Familie Engels in Barmen ansässig" begrenzen ohne Bestattungsort-Behauptung.

Befund D — Tabelle behauptet implizit Wuppertaler Datenbasis: Die Disclaimer-Sätze rund um die Tabelle sind diesmal sehr klar („keine offiziellen Wuppertaler Sätze, sondern Orientierungsspannen aus … Düsseldorf, Essen, Solingen, Remscheid"). ✓ Sauber. Aber: Die Beisetzungsgebühr 400–900 € und Krematoriumsgebühr 250–400 € stehen ohne den gleichen Disclaimer im Fließtext direkt unter der Tabelle. Lesefluss kann den Disclaimer auf diese zwei Folgesätze nicht automatisch ausdehnen. Sekundär, aber bei strenger Lesart eine Schwachstelle.

Top-3-Auswahl:

SCORE: 87/100

FUNDE:
- SCHWÄCHE 1 (Schema.org Place "Friedhof Krummacherstraße", JSON-LD-Block): PLZ 42119 ist nach Stadtgeografie für die Krummacherstraße 35 Elberfeld zweifelhaft — die Krummacherstraße verläuft in Elberfeld, typische PLZ-Zuordnung 42105/42107. PLZ 42119 ist Uellendahl-Katernberg. Wenn die Schema-PLZ falsch ist, schlägt der Google Rich-Results-Test an und es liegt ein verifizierbarer Faktenfehler in strukturierten Daten vor. Halluzinations-Verdacht Kat. 12 + Schema-Befund Kat. 10. Verbesserung: PLZ über offizielles Wuppertaler Straßenverzeichnis bzw. Google Maps für Krummacherstraße 35 verifizieren und in Schema + Fließtext synchron korrigieren; vermutlich 42105 oder 42107.

- SCHWÄCHE 2 (Sektion "Friedhof Unterbarmen — Erbe der Barmer Industriellen", Engels-Absatz): Die Aussage "Auf dem Friedhof Unterbarmen finden sich Gräber anderer Mitglieder der Familie Engels sowie weiterer Barmer Unternehmerfamilien" ist eine konkrete Tatsachenbehauptung ohne Quelle. Welche Engels-Familienmitglieder? Die Friedrich-Engels-Bestattung wird korrekt als London/Eastbourne verortet, aber die positive Behauptung "andere Engels-Familienmitglieder ruhen hier" ist unbelegt und hat exakt das gleiche Halluzinations-Profil wie die in v2 gestrichene Foerster-Aussage. Kat. 1 (Quellen-Lücke) + Kat. 12 (Halluzinations-Verdacht). Verbesserung: Entweder Beleg über Engels-Haus Wuppertal / Stadtarchiv ergänzen oder Aussage streichen — der Absatz funktioniert auch ohne diesen Halbsatz, der entscheidende Punkt (Engels selbst nicht hier bestattet) bleibt erhalten.

- SCHWÄCHE 3 (Sektion "Bestattungskosten in Wuppertal", direkt unter der Tabelle): Der explizite Orientierungs-Disclaimer steht VOR der Tabelle und bezieht sich textlich auf die Grabarten-Spannen. Die direkt folgenden Zahlenangaben "Beisetzungsgebühren ... 400 bis 900 Euro" und "Krematoriumsgebühr ... rund 250 bis 400 Euro" laufen ohne erneuten Disclaimer — diese Werte werden also implizit als Wuppertal-spezifisch suggeriert, obwohl sie ebenfalls Regionalspannen sind. Schwacher Übergang Kat. 4 + Sektion-Lücke Kat. 8 für eine YMYL-Zahlenaussage. Verbesserung: Halbsatz ergänzen "(ebenfalls Orientierungswerte aus NRW-Großstädten)" oder beide Sätze in den Disclaimer-Block oberhalb der Tabelle integrieren bzw. unter den Tabellen-Fußteil ziehen.

MUST-FIX vor Deploy: ja.

Begründung 87/100: v4 hat alle drei v3-Befunde sauber adressiert (Krummacher entschärft, Kindergräber-Zahl raus, Kultur-Vergleich deskriptiv umgeschrieben). UNSURE-Kommentare im Quelltext zeigen ehrliche Selbstmarkierung. Wortzahl, Schema-Breite, Cross-Links, Tabelle mit Disclaimer, Quellen-Block — alles solide. Punktabzug:

Schwäche 1 (Schema-PLZ) ist ein hartes Faktum, das in 2 Minuten verifizierbar ist und einen sichtbaren Schema-Fehler vermeidet → muss vor Deploy
Schwäche 2 (Engels-Familienmitglieder) ist exakt die Klasse Halluzination, die in v2 mit Foerster schon mal aufgefallen ist — eine Wiederholung des gleichen Musters wäre für eine Gold-Page mit Author-Schema nicht akzeptabel
Schwäche 3 ist ein leichtes Konsistenz-Patzer, isoliert vielleicht Stand-by, aber in Kombination mit 1+2 hebt es die Page nicht über die 88er-Schwelle

Über 85 (klar Gold-Niveau-Substanz, v3→v4 zeigt funktionierenden Loop), unter 90 (zwei Belegrisiken, davon eines mit Halluzinations-Profil). Schwäche 1 ist der harte Must-Fix; Schwäche 2 ist Must-Fix wegen Wiederholungs-Muster; Schwäche 3 ist Should-Fix.