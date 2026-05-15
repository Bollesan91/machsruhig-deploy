Ich lese mir alle drei Dokumente durch.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

Jetzt die v3, in der die MUST-FIX umgesetzt sein sollen.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/nuernberg/v3-final.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/nuernberg/v3-final.html

Adversarial Mode an. Ich gehe die v3 systematisch durch und prüfe (a) ob die drei v2-MUST-FIX umgesetzt sind, (b) was Chat A in v3 neu eingeführt hat, und (c) wo unabhängig davon noch Schwächen sind.

MUST-FIX-Status aus v2:

§-Verweise / 8-Tage-Frist: Fließtext zitiert jetzt korrekt § 18 BestV (Frühest, 48h) und § 19 Abs. 1 BestV (Spätest, 8 Tage, ohne Samstage/Sonn-/Feiertage), nennt explizit den Rechtswechsel zum 01.04.2021 mit GVBl.-Fundstelle, und die zweite Leichenschau wird sauber als § 17 Abs. 1 Satz 1 Nr. 2 BestV (seit 01.01.2023) zitiert. Art. 16 BestG wird korrekt als Verordnungsermächtigung eingeordnet. FAQ-Antworten konsistent. Erledigt. ✓
Friedhofssatzung/Gebührensatzung als Deeplink: Drei direkte PDF-Links eingebaut (Bestattungs-/Friedhofssatzung, BFGebS, Anlage gültig ab 01.04.2026). Erledigt. ✓
Konkrete Nürnberg-Zahlen in Kosten: Tabelle mit fünf Grabarten und € (Reihengrab 650 €, Wahlgrab 50 €/Jahr, Kindergrab 425 €, Familiengrab 70 €/Jahr) eingebaut. Erledigt. ✓

Damit sind die drei v2-MUST-FIX abgearbeitet. Aber: neue Schwächen.

Neue Prüfung — substantielle Schwächen in v3:

Was mich beim Lesen stutzig macht: Chat A hat aus „erfahrungsgemäß"-Zahlen plötzlich harte Tabellenwerte gemacht (650 € Reihengrab, 50 €/Jahr Wahlgrab, BFGebS § 5). Das ist genau die Halluzinations-Falle aus Round 2 — diesmal nicht beim Rechtsteil, sondern bei den Gebühren. Zwei Indizien: (a) Die Links zur Gebührensatzung sind generisch (PDF-URLs, ich kann sie nicht abrufen), (b) die Zahlen sind sehr glatt und „typisch", (c) der Quellenverweis im Tabellenkopf ist „BFGebS § 5" — § 5 ist in deutschen Gebührensatzungen oft die Allgemein-Vorschrift, nicht der Gebührentarif (der steht meist in der Anlage). Ich prüfe das.

Web durchsucht
Web durchsucht

Treffer und Differenzierung:

Gebühren-Check (Quelle: docplayer-Mirror der BFGebS, Stand 2017-Änderung):

Reihengrab Erwachsene: 650 € ✓ (Page korrekt)
Reihengrab Kinder: 425 € ✓
Familiengrab: 70 €/Jahr ✓
Wahlgrab Erwachsene: 50 €/Jahr (Page) vs. 31 €/Jahr (älterer Stand 2010) / 50 €/Jahr (Stand 2017) — die Page hat 50 €, das ist der aktuellere Wert ✓
Wahlgrab Kinder: 13 €/Jahr ✓
§-Verweis „BFGebS § 5" ✓ — § 5 ist tatsächlich „Grabarten" in der BFGebS, das stimmt.

Damit ist die Gebührentabelle korrekt — der erste Halluzinations-Verdacht löst sich auf. Gut für Chat A.

Aber: Die Sache mit „Anlage zur Gebührensatzung, gültig ab 1. April 2026" — wo kommt das her? Ich finde Anlage-Versionen für 2010, 2023, 2024 — aber explizit „ab 1. April 2026" wird nicht durch meine Suche bestätigt. Das ist ein Halluzinations-Risiko (sehr spezifisches Datum, könnte erfunden sein).

Web durchsucht
Web durchsucht

„Anlage zur Gebührensatzung, Preise gültig ab 01.04.2026" ist auf nuernberg.de tatsächlich so verlinkt — Treffer 17 bestätigt das wörtlich. Damit ist die Datumsangabe korrekt und keine Halluzination. Sehr gut.

Aber — und das ist relevant — Treffer 16 sagt: „Vor einer Einäscherung schreibt der Freistaat seit dem 1. April 2025 verbindlich eine zweite Leichenschau…". Die Page schreibt aber „seit dem 1. Januar 2023". Beide Daten kursieren — was stimmt wirklich? Das ist neu im Widerspruch und potenziell relevant.

Web durchsucht
Web durchsucht

Klarer Treffer und das ist ein harter inhaltlicher Fehler in v3:

Die Page schreibt vier Mal: „seit dem 1. Januar 2023" für die zweite Leichenschau (Rechtsteil, „Was nach Todesfall zu tun ist", FAQ „Wo wird eingeäschert", Schema.org-FAQ).

Tatsächlich gilt die Pflicht in Bayern seit dem 1. April 2025 (BayMBl. 2025 Nr. 99; Aeternitas; Friedhofsverwaltung Nürnberg eigenes Merkblatt „Informationen zur Einführung der 2. Leichenschau ab 1.4.2025"). Der ursprüngliche Termin 1.1.2023 wurde mehrfach verschoben — zuerst auf 1.7.2024, dann auf das Frühjahr 2025, schließlich Inkrafttreten 1.4.2025. Round 2 hatte das Datum 1.1.2023 vermutet, Chat A hat es übernommen, ohne zu prüfen.

Das ist wieder genau die Halluzinations-Klasse aus Round 2: Datum klingt plausibel, ist aber überholt. Auf YMYL-Niveau und im Schema.org-FAQ doppelt schwer.

Außerdem fällt mir beim Querlesen auf: Die Keyfacts oben sagen BestG Bayern + BestV (§ 18 Frühest-, § 19 Spätest-Frist) — aber § 19 Abs. 1 BestV wird im Fließtext und in der FAQ richtig zitiert. In den Keyfacts fehlt der „Abs. 1"-Zusatz. Marginal.

Und die OG-Image-URL https://machsruhig.de/assets/og-image.png ist generisch — das ist genau ein Punkt aus dem v0/v1-Audit (98/98 Seiten fehlten OG-Images). Falls dieses File nicht existiert oder generisch ist, ist es kein deploy-Blocker, aber ein Quality-Issue.

Genug Vorarbeit. Drei substantielle Schwächen:

BRIEFING_OK

SCORE: 71/100

FUNDE:

SCHWÄCHE 1 (Halluzination/veraltetes Datum — Deploy-Blocker): Falsches Inkrafttretensdatum der zweiten Leichenschau, viermal wiederholt. Die Page schreibt an vier Stellen: Rechtsteil („Seit dem 1. Januar 2023 verlangt § 17 Abs. 1 Satz 1 Nr. 2 BestV vor jeder Feuerbestattung eine zweite Leichenschau"), Abschnitt „Was nach einem Todesfall zu tun ist", FAQ „Wo wird eingeäschert" sowie identisch im Schema.org-FAQ-Markup („Vor jeder Einäscherung ist seit dem 1. Januar 2023…"). Falsch. Die Pflicht zur zweiten Leichenschau wurde in Bayern mehrfach verschoben und gilt tatsächlich erst seit dem 1. April 2025 (BayMBl. 2025 Nr. 99 mit Inkrafttreten 17.03.2025 für die Muster, § 17 Abs. 5 Satz 3 BestV i.d. ab 1.4.2025 geltenden Fassung). Die Friedhofsverwaltung Nürnberg veröffentlicht selbst ein Merkblatt mit dem Titel „Informationen zur Einführung der 2. Leichenschau ab 1.4.2025". Der Ursprungstermin 1.1.2023 wurde 2022/23 auf 1.7.2024 und dann auf Frühjahr 2025 verschoben — Chat A hat den überholten Termin offenbar aus älteren Quellen übernommen, ohne zu prüfen. Das ist exakt die Fehlerklasse aus Round 2 (falsche §/Datum-Zitate auf YMYL-Seite), nur eine Ebene weiter. Fix: „seit 1. April 2025" an allen vier Stellen, Schema.org-FAQ konsistent ändern, Quelle BayMBl. 2025 Nr. 99 und das Friedhofsverwaltungs-Merkblatt in die Quellenliste.

SCHWÄCHE 2 (UNSURE-Verarbeitung inkonsistent — Quellen-Lücke + Floskel-Verdacht): „Mehr als 30.000 dokumentierte Begräbnisse" und „125 Hektar / 5.000 Bestattungen jährlich" ohne Quelle. Im St.-Johannis-Abschnitt steht: „Die Belegung … umfasst nach Angaben des Stadtarchivs deutlich mehr als 30.000 dokumentierte Begräbnisse über mehr als fünf Jahrhunderte" — mit Berufung auf das Stadtarchiv, aber ohne Fundstelle (kein konkreter Bestand, keine PDF-Seite, keine Veröffentlichung). Im Rechtsabschnitt steht: „zehn Friedhöfe mit knapp 90.000 Gräbern und ca. 125 Hektar Fläche und führt jährlich über 5.000 Bestattungen durch" — auch das ohne Beleg. Drei harte Zahlen, eine attributierte Sekundärquelle („Stadtarchiv"), null überprüfbare Primärquelle. Auf einer YMYL-Page, die in Schwäche 1 schon ein Datums-Problem hat, ist das ein zweites Vertrauensthema: Wo kommen die Zahlen her? Wenn Chat A sie nicht plausibilisieren kann, gehören sie raus oder mit konkretem Beleg versehen (z.B. Stadtarchiv-Findbuch, Pressemitteilung der Friedhofsverwaltung, Geschäftsbericht). „Nach Angaben des Stadtarchivs" ohne Link/Bestandsnummer ist im Briefing-Sinne die Kategorie „Aussage ohne Primärquelle, nur mit Sekundärverweis". Fix: Entweder konkrete Quelle (URL/Findbuch/Pressemitteilung mit Datum) oder Zahl streichen und durch belegbare Größenordnung ersetzen.

SCHWÄCHE 3 (Generischer Block / Floskel — wiederholte Round-2-Schwäche): „Bestatterleistungen / Grabstein / Trauerfeier"-Korridore weiter ohne Nürnberg-Bezug. Der Abschnitt „Weitere Kostenkomponenten" enthält genau die Zahlen, die Round 2 als „deutschlandweite Boilerplate" gerügt hatte: „Bestatterleistungen … rund 2.500 bis 4.500 Euro. Grabstein und Inschrift: 1.500 bis 4.000 Euro je nach Material und Bearbeitung. Trauerfeier, Trauerdruck und Bewirtung: 500 bis 1.500 Euro." Keine Quelle, kein Stand, kein Nürnberg-Anker. Zwar wurden die Friedhofsgebühren in einer separaten Tabelle nachgerüstet (gut, MUST-FIX erledigt) — aber direkt darunter steht weiter die deutschland-generische Aufschlüsselung ohne Quelle. Chat A hat den Round-2-Befund nur teilweise behoben: harte städtische Gebühren ✓, aber den Korridor-Block hat er weitergeführt. Mindestens eine der drei Positionen sollte mit Quelle belegt sein (Stiftung Warentest, BdSt-Erhebung, Branchen-Statistik des Bundesverbands Bestatter) — sonst bleibt es der Floskel-Vorwurf aus Round 2. Fix: Quelle pro Korridor (z.B. „Branchendurchschnitt laut Bundesverband Deutscher Bestatter 2024" mit Link) oder die Aussage relativieren („typische Spannweiten, regional stark abweichend, konkrete Beträge nur über schriftliche Kostenvoranschläge").

Was Chat A in v3 sehr gut umgesetzt hat (nur zur Pipeline-Transparenz, kein Pluspunkt):

§ 18 / § 19 Abs. 1 BestV / 8-Tage-Frist / GVBl. 2021 S. 138 sauber im Fließtext, FAQ und Schema.org konsistent ✓
Gebührensatzungs-PDFs als Deeplinks (drei Stück, inkl. Anlage gültig ab 01.04.2026) ✓ — und die Anlage 01.04.2026 ist gegen die Friedhofsverwaltungs-Seite verifiziert, also kein Halluzinations-Verdacht
Gebührentabelle mit konkreten € (Reihengrab 650 €, Wahlgrab 50 €/Jahr etc.) — Werte stimmen mit BFGebS § 5 überein ✓
Konkrete Cross-Links Bayern + Städte ✓, Schema.org mit Place-Entities und GeoCoordinates ✓

Was unverändert von v2 her schwach bleibt (nicht in Top-3, aber zur Vollständigkeit):

Keyfacts „§ 18 Frühest-, § 19 Spätest-Frist" — der Abs.-1-Zusatz fehlt, Fließtext und FAQ haben ihn (Inkonsistenz)
Muslimische Gemeinden „in Nürnberg" weiterhin ohne konkreten Namen/Adresse — Round 2 hatte „konkrete Adressen" gefordert; v3 sagt nur „eine der muslimischen Gemeinden". Teilerfüllt, nicht erfüllt.
OG-Image ist generisches /assets/og-image.png (98/98-Problem aus dem Audit) — ist aber keine YMYL-Frage, keine Halluzination

MUST-FIX vor Deploy: ja.

Schwäche 1 ist allein Deploy-Blocker — falsches Inkrafttretensdatum einer YMYL-Pflichtregelung, viermal wiederholt und auch im Schema.org-FAQ-Markup. Die Friedhofsverwaltung Nürnberg selbst dokumentiert 1.4.2025; Pipeline-extern überprüfbar in zwei Klicks. Wenn die Seite mit „seit 1.1.2023" live geht, ist das ein konkret nachweisbar falsches Statement zu einer ärztlichen Pflichtregelung — größeres Risiko als nur Trust-Verlust, weil Bestatter und Angehörige die Page als Referenz nutzen könnten. Schwächen 2 und 3 sind „nice-to-fix für Score >80", aber Schwäche 1 ist hart.

Score-Begründung: v2 lag bei 64 wegen falschem Rechtsteil; Chat A hat den Rechtsteil sehr ordentlich saniert (+10), Quellen-Deeplinks ergänzt (+3), Gebührentabelle eingezogen (+4), aber ein neues YMYL-Datums-Falsum eingeführt (−5) und zwei Round-2-Schwächen nur teilbehoben (−5). Netto: 71.