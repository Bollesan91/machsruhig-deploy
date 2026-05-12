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
Augsburg-Content Review nach SCORE-Tabelle
HTML-Seite für Bestatter in Münster erstellen
Adversarial review of Mannheim content
HTML-Seite für Bestatter in Karlsruhe
Augsburger Friedhöfe und Bestattungsregeln
HTML-Seite für Bestatter Mannheim erstellen
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
HTML-Seite für Bestatter Dresden erstellen
HTML-Seite für Bestatter Bremen erstellen
HTML-Seite für Bestatter Essen erstellen
HTML-Seite für Bestatter in Dortmund erstellen
HTML-Seite für Bestatter Leipzig erstellen
HTML-Page Review für Stuttgart
Machsruhig.de Düsseldorf-Seite reviewen
Machsleicht project setup and priority planning
💬 Beschreib mir mal den Batch ur…
Admin-Rechte für Microsoft-365-App-Freigaben
Alle Chats
B
Bolle
Max Plan
Augsburg-Content Review nach SCORE-Tabelle
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). Lies das Briefing: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md und v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/augsburg/v1-from-chat-A.html

Stadt: Augsburg (Bayern). Review streng nach SCORE-Tabelle. Vergib SCORE 0-100% und gib konkrete Fix-Liste fuer v2.

10:56
Claude hat geantwortet: Ich lese erst Briefing und v1, dann reviewe ich streng nach SCORE-Tabelle.

Ich lese erst Briefing und v1, dann reviewe ich streng nach SCORE-Tabelle.

Fetching site
Web durchsucht

BRIEFING_OK

Jetzt prüfe ich systematisch gegen den Maßstab. Wortzahl-Check über den sichtbaren Body-Content ist mir wichtig – die Page wirkt eher knapp.

Skeptische Prüfung:

Wortzahl: Sichtbarer Body-Content (ohne FAQ-Antworten, Quellen, Navigation) liegt grob bei ~1.500–1.700 Wörtern. Mit FAQ kommt man auf ~2.000. Das ist im unteren Korridor, nicht im Zielkorridor 2.000–2.500 Hauptcontent.
Friedhofs-Highlights: 4 Friedhöfe ausführlich (Protestantischer, Hermanfriedhof, Westfriedhof, Jüdischer Kriegshaber). Das ist mehr als das Minimum (2–3). Tiefe ist überwiegend stark – mit konkreten Daten, Architekten, Geschichte, Hidden Gems mit echtem lokalem Anker (Brecht-Eltern, Mathias Kneißl, Schießplatz-Anekdote, Holzer-Jugendstil-Argument).
§-Verweise BestG/BestV: Vorhanden – § 19 Abs. 1 BestV (Frist), § 19 Abs. 4 BestV (Urnenfrist), § 30 Abs. 1+2 BestV (Sargpflicht), Art. 1 Abs. 1 BestG, Art. 14 BestG, § 3 BestV (Leichenschau), § 15 BestV (Bestattungspflicht). Aber: § 15 BestV ist ein klassischer Stolperstein – die Bestattungspflicht der Angehörigen steht in Art. 15 BestG, nicht in der BestV. Das muss ich markieren – wenn das eine falsche Zitierung ist, ist es ein Blocker für den Recheck.
Kosten: Konkrete Preisspannen, Tabelle aus städtischer Gebührensatzung, Gesamtkorridor 4.500–9.000 €. Stark.
Lokale Besonderheiten: Reichsstadt-Erbe (konfessionelle Friedhofstrennung), muslimisches Grabfeld Ostfriedhof, rituelle Waschungen Göggingen, Krematorium am Westfriedhof. Gut verankert.
Floskeln: Beim Drüberlesen finde ich keine "letzte Ruhe", "schwere Zeit", "individuelle Wünsche". Sehr sauber.
Struktur/Schema.org: H1, sinnvolle H2-Sektionen, FAQ-Schema mit 7 Fragen, BreadcrumbList, Article, City, Place (4 Friedhöfe), Organization. Sehr vollständig.
Cross-Links: Nur 2 (Bayern-Übersicht, Bestattungsvorsorge). Keine Stadt-zu-Stadt-Verlinkung (z.B. München, Nürnberg) – das ist auf anderen Bundesland-Pages oft vorhanden, hier ist es aber eine Stadt-Page innerhalb Bayern, also weniger zwingend. Aber: Kein Cross-Link zum FAQ-Eintrag aus Hauptcontent, kein Link auf eine Augsburg-spezifische Bestatter-Liste.
Sterbeurkunden-Gebühr: 12 € genannt – plausibel, aber ohne §-Quelle (PStV/PStG).
„Naturfriedhof" beim Westfriedhof: Schwammig. Augsburg hat tatsächlich einen Naturfriedhof, aber meines Wissens den Naturfriedhof Wittelsbacher Land außerhalb / oder den Bestattungswald-Bereich. Die Formulierung "innerhalb des Westfriedhofs gibt es heute auch einen Naturfriedhof" – das ist faktisch zu prüfen. Recheck-Risiko.
„rund 70.000 Grabplätze" – keine Einzelquelle in der Sources-Liste, die das stützt. Sourcing-Lücke.
„Klaus Müller Oberbürgermeister 1947–1964" – das stimmt nicht ohne Weiteres mit meinem Wissen überein; Augsburger Nachkriegs-OB war u.a. Klaus Müller? Das muss faktisch verifiziert werden. Faktrisiko.
„Christoph von Schmid ... Verfasser des Weihnachtsliedes ‚Ihr Kinderlein kommet" – Schmid ist tatsächlich der Textdichter, gestorben in Augsburg 1854. Plausibel, aber Begräbnisort prüfen (Hermanfriedhof? Bin nicht 100% sicher).
Eltern Brechts Sterbedaten/Zusatz – im FAQ steht „trägt die Namen und Sterbedaten sowie für den Vater den Zusatz Fabrikdirektor" – plausibel und konsistent zwischen Hauptcontent und FAQ.
Standesamt-Zuständigkeit Stadtteile: Liste der früher selbstständigen Orte (Bergheim, Göggingen, Haunstetten...) – plausibel, aber ohne Primärquelle direkt verlinkt.
Quellen: 17 Quellen, davon viele Primärquellen (städtische Satzung, Gesetze, Bayerische Verordnung). Stark. Aber: Wikipedia 3x als Quelle – kein echter Blocker, aber Primärquellen wären sauberer.
„Bestatterkrematorium am Westfriedhof" – Augsburg hat tatsächlich ein städtisches Krematorium, das müsste am Westfriedhof sein. Plausibel.
Anzahl Friedhöfe: Im Hauptcontent „rund 15", im FAQ wird die Aufzählung von 9 städtischen + 4 konfessionellen = 13 genannt + „zwei jüdische Friedhöfe" – das passt zu 15. Aber: Im Schema.org-Aufzählung der Places fehlt der Westfriedhof als jüdischer Friedhof; und im FAQ ist von „Friedhof Kriegshaber / Hooverstraße und Haunstetter Straße" die Rede, im Schema steht nur Kriegshaber. Inkonsistenz Schema vs. Text.

Zwischenfazit: Inhaltlich überdurchschnittlich gut. Tiefe, Sourcing-Substanz und Floskel-Vermeidung sind im oberen Korridor. Aber:

§ 15 BestV vs. Art. 15 BestG ist potenziell falsche Zitation (Recheck-Blocker)
Naturfriedhof-Aussage Westfriedhof ist faktisch unsicher
"70.000 Grabplätze" unsourced
Klaus-Müller-OB-Datum ist überprüfbedürftig
Schema.org listet nur 4 Friedhöfe (zweiter jüdischer Friedhof fehlt)
Wortzahl-Hauptcontent eher 1.700, nicht 2.000+
Cross-Links dünn (nur 2)
Sterbeurkunde 12 € ohne §-Quelle

Skeptisch gewertet, mit Sorge um die §-Zitation und unverifizierte Fakten:

SCORE: 78%

GAP:

§ 15 BestV-Zitation für Bestattungspflicht der Angehörigen ist mit hoher Wahrscheinlichkeit falsch. Die Bestattungspflicht der Angehörigen ist in Bayern in Art. 15 BestG (Bayerisches Bestattungsgesetz) geregelt, nicht in § 15 BestV. Vor v2 mit Primärquelle gesetze-bayern.de gegenprüfen und korrigieren – sonst Recheck-Blocker (Kategorie „§-Falschzitation").
„Naturfriedhof innerhalb des Westfriedhofs" ist unklar belegt. Augsburg hat den Naturfriedhof Wittelsbacher Land (außerhalb), und der Westfriedhof bietet Baumgräber – das ist nicht dasselbe wie ein „Naturfriedhof". Aussage präziser formulieren („Baumgrabfeld als alternative Bestattungsform") oder mit Quelle vom Amt für Grünordnung belegen.
„Rund 70.000 Grabplätze" hat keine Quelle. Die Zahl steht ohne Verweis. Entweder mit Augsburg-Stadtbericht/Stadtlexikon-Quelle belegen oder streichen.
Klaus Müller als OB 1947–1964 ist verifizierungsbedürftig. Augsburger Nachkriegs-OBs waren u.a. Hugo Rasch, Wolfgang Pepper, Klaus Müller – das Datum 1947–1964 sollte gegen Stadtlexikon Augsburg gegengeprüft werden. Bei Falschangabe = Faktblocker.
Schema.org-Inkonsistenz: nur 4 Friedhöfe als Place-Entitäten. Im Text werden 9 städtische + 4–5 konfessionelle genannt, im JSON-LD stehen nur Protestantischer, Hermanfriedhof, Westfriedhof und Jüdischer Kriegshaber. Mindestens Nord-, Ostfriedhof und das zweite jüdische Friedhofs-Areal (Haunstetter Straße) ergänzen, sonst springt das Schema-Audit an.
Sterbeurkunde 12 € ohne §-Quelle. Gebühr ist plausibel, aber Primärquelle (PStG/PStV bzw. Kostensatzung Augsburg) fehlt im Quellenapparat.
Wortzahl Hauptcontent liegt geschätzt bei 1.700, nicht im Zielkorridor 2.000–2.500. Aufstocken um eine eigene kleine Sektion „Friedhof Göggingen / Neuer Ostfriedhof" (muslimisches Grabfeld bereits erwähnt, aber kein eigener Block mit Adresse/Fläche/Geschichte) oder eine Sektion „Krematorium Augsburg" mit Geschichte, Adresse und Gebühren.
Cross-Links zu dünn (nur 2). Es fehlen Links zu Nachbarstädten (München, Nürnberg, sobald vorhanden), zur Ratgeber-Seite Trauerfeier, zu Erbschein/Nachlassgericht. Mindestens 4–5 interne Links für SEO-Linkstruktur.
Westfriedhof-Sektion hat keine Belegungszahl/Fläche. Bei den anderen drei Friedhöfen ist die Fläche genannt (6 ha, 4,5 ha, 9.400 m²), beim Westfriedhof fehlt sie – obwohl er als „größte städtisch verwaltete Friedhofsanlage" bezeichnet wird. Konkrete ha-Angabe + Grabstellenanzahl mit Quelle nachtragen.
FAQ deckt Krematorium und muslimische/sarglose Bestattung doppelt ab, aber keine Frage zu „Wer trägt die Bestattungskosten?" Standardfrage fehlt – Bestattungspflichtige nach Art. 15 BestG, Sozialbestattung nach § 74 SGB XII.
Quellen Wikipedia 3x statt Primärquelle. Für Protestantischen Friedhof und Hermanfriedhof gibt es jeweils eine offizielle Webseite, die schon in Quelle 8 und 10 verlinkt ist – Wikipedia-Einträge (Quellen 9 und 11) könnten gestrichen oder durch Stadtlexikon/Wißner-Quelle ersetzt werden.
Friedhofsgebührensatzung-Bezug uneinheitlich. Im Text „Anlage zu Satzung 7511", in der Quelle steht „Satzung 7511" und „7511_ANL". Sinnvoll: Im Fließtext einmal vollständige Satzungsnummer + Bekanntmachungsdatum nennen statt nur „seit 1. Januar 2025".

Du bist Chat B (Reviewer). Lies das Briefing: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md und v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/augsburg/v1-from-chat-A.html




Stadt: Augsburg (Bayern). Review streng nach SCORE-Tabelle. Vergib SCORE 0-100% und gib konkrete Fix-Liste fuer v2.

Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen
Claude is active in this tab group
Open chat
Dismiss