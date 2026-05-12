Neuer Chat
Suchen
Chats
Projekte
Code
Anpassen
Design
Mehr
Zuletzt verwendet
Ausblenden
Wiesbaden-Review nach SCORE-Tabelle
HTML-Seite für Bestatter in Karlsruhe
Augsburger Friedhöfe und Bestattungsregeln
Karlsruhe v3 adversarial review und final-score
Adversarial review v3 Mannheim
Wiesbadener Friedhöfe und Bestattungsgesetze recherchieren
HTML-Seite für Bestatter Mannheim erstellen
Adversarial review of Augsburg content
Adversarial review v3 Münster content check
Adversarial review of Karlsruhe content
Augsburg-Content Review nach SCORE-Tabelle
Adversarial review of Mannheim content
HTML-Seite für Bestatter in Münster erstellen
Überprüfung von Halluzinationen in Münster-Inhalten
Karlsruhe-Inhalte nach SCORE-Kriterien reviewen
Mannheim-Content Review nach SCORE-Kriterien
Machsruhig.de Münster Review und Scoring
HTML-Seite für Bestatter in Düsseldorf erstellen
HTML-Seite für Bestatter in Bonn erstellen
HTML-Seite für Bestatter Stuttgart erstellen
Adversarial Review für machsruhig.de Stuttgart
HTML-Seite für Bestatter in Bonn erstellen
HTML-Seite für Bestatter Bielefeld erstellen
HTML-Seite für Bestatter Wuppertal erstellen
HTML-Seite für Bestatter in Bochum erstellen
HTML-Seite für Bestatter in Duisburg erstellen
HTML-Seite für Bestatter Nürnberg erstellen
HTML-Seite für Bestatter Hannover erstellen
HTML-Seite für Bestatter in Dortmund erstellen
HTML-Seite für Bestatter Leipzig erstellen
HTML-Seite für Bestatter Dresden erstellen
HTML-Seite für Bestatter Essen erstellen
HTML-Seite für Bestatter Bremen erstellen
Alle Chats
B
Bolle
Max Plan
Wiesbaden-Review nach SCORE-Tabelle
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). Lies Briefing https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md und v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/wiesbaden/v1-from-chat-A.html

Stadt: Wiesbaden (Hessen). Review streng nach SCORE-Tabelle. Vergib SCORE 0-100% und gib konkrete Fix-Liste fuer v2.

11:23
Claude hat geantwortet: Ich lese erst das Briefing und dann v1.

Ich lese erst das Briefing und dann v1.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md

Jetzt v1:

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/wiesbaden/v1-from-chat-A.html

Wortzahl-Check und Floskel-Detection durchlaufen. Quellen-Substanz wirkt stark (§-Verweise, konkrete Gebühren mit SV-Nummer), aber drei Punkte stechen heraus, die ich verifizieren muss: (1) FBG-Novelle 2025 mit 10-Tage-Frist, (2) §-Zuordnung (§ 9, § 13, § 16, § 20 FBG), (3) Krematorium 1912 als „erstes Preußens".

Searching the web
Web durchsucht

FBG-Novelle bestätigt (30.09.2025 verabschiedet, in Kraft Oktober 2025, § 16 Abs. 1: 48h–10 Tage). § 16 als Bestattungsfrist ist korrekt. Aber: v1 ordnet die Sorgepflichtigen-Reihenfolge § 13 zu — und behauptet § 9 sei „Leichenschau". Schnell-Check: laut Aeternitas-FBG-Dokument (Index 5) ist § 9 tatsächlich Leichenschau, § 13 Sorgepflichtige, § 16 Bestattungsfristen, § 20 Feuerbestattung. Dann ist § 20 Abs. 3 als Quelle für „Urne zu Hause" verdächtig — § 20 regelt Feuerbestattung, nicht Aufbewahrung. Bei Aeternitas Index 11 steht explizit „Unklar ist, ob auch Ausnahmen von der Urnenpflicht zugelassen werden können. (§ 20 Abs. 3 FBG)". Also: § 20 Abs. 3 ist nur möglicherweise Rechtsgrundlage und nicht eindeutig — v1 stellt das aber als sichere Genehmigungsfähigkeit dar. Das ist eine Überdehnung.

Krematorium 1912 schnell prüfen:

Searching the web
Web durchsucht

Krematorium 1912 ist „eine der ersten" Preußens — laut Stadt Wiesbaden sogar „erste". v1 nutzt beide Formulierungen leicht inkonsistent ("eine der ersten Feuerbestattungsanlagen in Preußen" im Fließtext, "erste Krematorium Preußens" im Keyfacts/Box). Beides ist durch Quellen gedeckt, aber Inkonsistenz. Wichtiger Punkt: Krematorium war 1997 abgelöst — v1 schreibt aber „Im Mittelpavillon der Eingangsgebäude wurde 1912 das Krematorium in Betrieb genommen" und später „Bis 1997 wurde dort eingeäschert, dann ersetzte eine neue Anlage am nördlichen Rand". Quellen sagen aber: Krematorium war im Untergeschoss/Keller der Trauerhalle (Mittelbau), nicht „Mittelpavillon der Eingangsgebäude". Kleiner Fakt-Drift.

Jetzt habe ich genug für ein ehrliches Review. Ich bewerte streng. Wortzahl visuell überschlagen: ~2.300-2.500 Wörter. Liegt im Ziel-Korridor.

SCORE: 78%

GAP:

§ 20 Abs. 3 FBG wird als sichere Rechtsgrundlage für die private Urnen-Aufbewahrung dargestellt („genehmigungsfähig", „Ausnahmen von der Urnenbeisetzungspflicht zulassen"). Tatsächlich regelt § 20 Feuerbestattung; Aeternitas bezeichnet es ausdrücklich als „unklar, ob auch Ausnahmen von der Urnenpflicht zugelassen werden können". v1 muss diese Unsicherheit benennen statt zu glätten — sonst ist es eine juristisch zu weit gehende Aussage in einem rechtssensiblen Kontext.
FBG-Novelle: Datum unscharf. „novelliert 2025" / „Herbst 2025" reicht nicht. Beschluss 30.09.2025, Verkündung GVBl. Nr. 64 vom 06.10.2025, Inkrafttreten Tag nach Verkündung. Diese drei Daten sollten konkret rein, gerne mit Drucksache 21/2378.
Krematorium-Verortung falsch: v1 schreibt „Im Mittelpavillon der Eingangsgebäude wurde 1912 das Krematorium in Betrieb genommen". Laut Stadt Wiesbaden und Wikipedia lag das Krematorium in den Untergeschossen (Keller) der Trauerhalle / des Mittelbaus, nicht in einem Pavillon. Faktenfehler.
Inkonsistenz: Hero+Keyfacts+Tabelle-Caption sagen „erstes Krematorium Preußens", Fließtext Südfriedhof sagt „eine der ersten Feuerbestattungsanlagen in Preußen". Beides durch Quellen belegbar (Stadt Wiesbaden = „erste", Wikipedia = „eine der ersten") — aber innerhalb einer Page muss eine Formulierung gewählt und durchgezogen werden.
§ 13 Abs. 3 FBG-Behauptung „Hessen ist das einzige Bundesland, in dem auch Krankenhäuser, Pflegeheime oder ähnliche Einrichtungen bestattungspflichtig werden" — das ist eine starke Alleinstellungs-Aussage ohne Quelle. Bei den anderen 15 Bundesländern gibt es subsidiäre Bestattungspflichten der Ordnungsbehörden; ob diese Konstellation wirklich einzigartig ist, muss belegt oder die Aussage entschärft werden auf „Hessen kennt eine ausdrückliche subsidiäre Bestattungspflicht von Einrichtungen (§ 13 FBG)".
Nur 3 Friedhofs-Highlights (Nord, Süd, Russisch) + 1 Wald. Für eine 21-Friedhöfe-Stadt mit Stadtteilcharakter ist Friedhof Biebrich namentlich genannt, aber nicht ausgearbeitet. Mindestens ein vierter klassischer Friedhof sollte mit eigener Tiefe (Geschichte, Fläche, Besonderheit) vorkommen — Biebrich, Alter Friedhof Platter Straße oder jüdischer Friedhof am Nordfriedhof. Die jüdischen Friedhöfe Wiesbadens sind nur in einem Halbsatz erwähnt, das ist für eine Kurstadt mit substanzieller jüdischer Geschichte zu dünn.
Bernhard-von-Wiesen-Stiftung: Das Gründungsjahr 2001 wird ohne Quelle behauptet, ebenso die konkrete Ermäßigung „25 bis 50 Prozent" mit dem § 1.2.8/1.2.9-Verweis auf die Gebührensatzung. § 1.2.8/1.2.9 ist keine übliche §-Notation für eine Satzung — das wirkt wie eine Position aus dem Gebührenverzeichnis, nicht ein Paragraph. Formatierung klären (Pos. 1.2.8 statt § 1.2.8) oder Quelle anhängen.
Schema.org: City-Knoten enthält keine containedInPlace als verlinktes State-Objekt mit @id, sondern nur inline. Konsistent mit den 13 fertigen Bundesland-Pages? Bitte gegen Sachsen oder Berlin abgleichen — falls die State-Verlinkung dort ausgebaut ist, hier nachziehen.
FAQ-Schema: Die Frage „Welche Bestattungsfrist gilt in Hessen?" verweist auf „§ 16 Abs. 1 FBG". Korrekt. Aber die HTML-FAQ-Antwort sagt zusätzlich „eine der längsten Bestattungsfristen im Bundesvergleich" — das stimmt nicht. 10 Tage ist der Standard in NRW, RLP und mehreren weiteren Ländern (siehe Aeternitas-Stellungnahme: „Angleichung an die Rechtslage in den meisten anderen Bundesländern"). Damit ist die Aussage faktisch falsch und sollte ersetzt werden durch „liegt nun im Bundesländer-Durchschnitt".
Cross-Links zu anderen Städten/Bundesländern: Nur 1 Link zur Hessen-Übersicht. Keine Cross-Links zu Frankfurt, Darmstadt, Kassel, Offenbach trotz expliziter Nennung dieser Städte im Bestatter-Abschnitt. Für interne Verlinkung und SEO ungenutzt.
„Bei Sterbefällen außerhalb eines Krankenhauses kann ein bevollmächtigtes Bestattungsinstitut die Anzeige übernehmen" — die Logik ist umgekehrt. Bei Krankenhaus zeigt das Krankenhaus an (§ 9 PStG), bei Sterbefällen außerhalb muss durch Angehörige oder bevollmächtigten Bestatter angezeigt werden. Im FAQ-Schema steht dasselbe verkehrt. Bitte aufdröseln und korrekt formulieren.
Marktpreis-Spannen „3.500–5.500 Euro" (Urne) und „8.000–15.000 Euro" (Erdbestattung mit Wahlgrab) ohne Quellenangabe. Aeternitas oder Verbraucherzentrale als Beleg ergänzen — sonst bleibt das eine unsubstantiierte „Erfahrungswert"-Aussage.
Wortzahl: Etwa 2.300–2.450 Wörter geschätzt. Im Ziel-Korridor, aber am unteren Ende. Mit einem vierten Friedhof, mehr jüdischer Geschichte und einer Sektion zu „Bestattungstraditionen in Wiesbaden" (Kurstadt, Belle Époque, internationale Klientel als regionale Besonderheit) wäre der Korridor 2400–2600 stabiler getroffen.
„Hidden Gem"-Überschriften wirken als Marker formelhaft — bei drei Friedhöfen identisch „Hidden Gem: …". Eine Variation der Überschriften (etwa „Geschichte hinter der Anlage", „Was diesen Ort besonders macht") würde Floskel-Wahrnehmung reduzieren.
Adresse Russisch-Orthodoxer Friedhof: Schema.org-Block hat „Christian-Spielmann-Weg 1" — Quellen-Check mit der offiziellen Adresse der Kirche/Friedhof Neroberg fehlt. Bitte verifizieren oder durch „Neroberg, 65193 Wiesbaden" ersetzen, das auch im Meta-Bereich des Friedhof-Blocks steht — Inkonsistenz Schema vs. sichtbarer Meta-Eintrag.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen