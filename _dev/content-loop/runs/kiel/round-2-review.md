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
Kiel-Review nach SCORE-Tabelle
Mainzer Friedhöfe und Bestattungskultur recherchieren
Augsburger Friedhöfe und Bestattungsregeln
Wiesbadener Friedhöfe und Bestattungsgesetze recherchieren
Mainz content review nach SCORE-Tabelle
Kieler Friedhöfe und Bestattungskultur recherchieren
Augsburg v4 Bewertung und Adversarial-Score
Adversarial review of Wiesbaden content
Mannheim v4 adversarial quality review
HTML-Seite für Bestatter Mannheim erstellen
Adversarial review v3 Augsburg
Karlsruhe v4 adversarial review und final score
HTML-Seite für Bestatter in Karlsruhe
Wiesbaden-Review nach SCORE-Tabelle
Karlsruhe v3 adversarial review und final-score
Adversarial review v3 Mannheim
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
Alle Chats
B
Bolle
Max Plan
Kiel-Review nach SCORE-Tabelle
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). Lies Briefing https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md und v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/kiel/v1-from-chat-A.html

Stadt: Kiel (Schleswig-Holstein). Review streng nach SCORE-Tabelle. Vergib SCORE 0-100% und Fix-Liste fuer v2.

11:55
Claude hat geantwortet: Ich lade beide Dateien und führe das Review durch.

Ich lade beide Dateien und führe das Review durch.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md

Hinweis: Das Briefing erwartet eigentlich Bestätigung mit "BRIEFING_OK" und dann separate Lieferung. Da du beides in einem Schritt willst (Stadt Kiel) und v1 bereits referenziert ist, lade ich jetzt die v1.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/kiel/v1-from-chat-A.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/kiel/v1-from-chat-A.html

Briefing und v1 gelesen. Wortzahl grob ~2200 Wörter, vier Friedhofsporträts mit Hidden Gems, FAQ + Schema + Quellen vorhanden. Jetzt strenge Prüfung gegen die SCORE-Tabelle (Quellen-Substanz, Tiefe, Floskeln, Struktur).

SCORE: 72%

GAP:

Kiel hat laut Hero "vier städtische Anlagen", der Kostenabschnitt listet aber sieben städtische Friedhöfe auf (Nordfriedhof, Urnenfriedhof am Krematorium, Ostfriedhof, Russee, Meimersdorf, Elmschenhagen, Pries). Das ist ein direkter Widerspruch im eigenen Text. Die FAQ ("vier städtische") wiederholt den Fehler. Recherche bei kiel.de muss klären, wie viele städtische Friedhöfe es tatsächlich gibt, und alle drei Stellen (Hero, Kernfakten, Kostenabschnitt, FAQ) müssen konsistent sein.
Trägerzuordnung Elmschenhagen / Pries / Friedrichsort ist intern widersprüchlich. Im Kostenabschnitt stehen Elmschenhagen und Pries unter "städtisch", in der FAQ unter "kirchlich (Kirchenkreis Altholstein)". Eine der beiden Aussagen ist falsch — vor Veröffentlichung über kiel.de bzw. friedhof-kiel.de eindeutig klären.
§-Verweise zum BestattG SH sind teilweise unbelegt oder falsch zugeordnet. § 16 (Fristen 48h / 9 Tage / 1 Monat Urne) muss gegen die aktuelle Fassung 2025 verifiziert werden — nach der Reform zum 01.01.2025 wurden Paragraphennummern teils verschoben. Auch § 15 (zulässige Bestattungsarten) und § 13 (Bestattungspflicht) sowie § 10 (36-Stunden-Frist zur Überführung in den Leichenraum) gegen die geltende Fassung prüfen. § 15a (Erprobung neuer Bestattungsarten) ist eine starke Behauptung — Primärquelle (Landesnorm gesetze-rechtsprechung.sh.juris.de) im Quellenblock fehlt; aeternitas.de ist Sekundärquelle.
Friedhofsgebühren sind ohne Stand-Jahr und ohne konkrete Satzungsfundstelle. Der Satz "Stand der zuletzt öffentlich dokumentierten Friedhofsgebührensatzung" ist eine Floskel-Variante und genau das, was die Recheck-Skripte als unsourced markieren. Jede Zeile in der Gebührentabelle braucht: Stand-Jahr + § der Friedhofsgebührensatzung Kiel oder klare Kennzeichnung "Richtwert, Stand prüfen". Aktuell sind die Beträge nicht nachprüfbar.
Hidden Gem Südfriedhof ("verwachsene Trauerbuchen auf Grabfeld E als ein denkmalgeschützter Baum"): sehr spezifische Behauptung, keine Quelle. Falls nicht aus Arnold/Fischer 2019 oder einer Friedhofsführungs-Broschüre belegbar, gestrichen oder entschärft. Solche unverifizierten "botanischen Unikate" sind genau das Risiko, das die Bundesland-Recheck-Logik erkennen würde.
Hidden Gem Eichhof ("über 430 Gehölzarten, japanische Kuchenbäume, kalifornische Fuchsschwanzkiefern, ~80 Singvogelarten"): Zahlen ohne Quelle. Eichhof-Broschüre des Kirchenkreises Altholstein oder NABU/Naturschutz-Erhebung als Beleg ergänzen, sonst weiche Formulierung.
Esmarch-Grab "Backstein-Kapelle als Grabmal": Die Esmarch-Mausoleum-Beschreibung ist verbreitet als Backsteinbau bekannt, aber die Formulierung "Backstein-Kapelle als Grabmal" ist ungenau (Mausoleum ≠ Kapelle). Sauber: "Mausoleum aus rotem Backstein, Architekt …" mit Quelle.
Bevölkerungszahl 1860 = "rund 17.500": Stadtarchiv-Quelle bzw. Statistisches Landesamt SH zitieren, sonst Zahl nur als "rund 20.000 Mitte 19. Jh." angeben. Aktuell unbelegt.
"Erster vollständig durchgestalteter Parkfriedhof Deutschlands ... Jahre vor dem bekannteren Ohlsdorfer Friedhof": Ohlsdorf wurde 1877 eröffnet, Südfriedhof Kiel 1869 — das stimmt zeitlich. Trotzdem ist die Superlativ-Aussage "erster vollständig durchgestalteter Parkfriedhof Deutschlands" eine harte fachliche Behauptung, die mindestens eine Sekundärquelle (Arnold/Fischer 2019 reicht, wenn explizit als Beleg-Anker im Fließtext referenziert) erfordert. Aktuell nur am Ende im Quellenblock — der Recheck markiert das als "Superlativ ohne Inline-Quelle".
Niobe-Unglück: "1932 vor Fehmarn ... 69 Marinesoldaten": Datum 26. Juli 1932 und 69 Tote sind die Standardangaben. Eine Inline-Quelle (Volksbund oder Stadtarchiv Kiel) fehlt aber, und die Zahl variiert in der Literatur (manche Quellen 69, andere 71). Klären und festschreiben.
Hans von Koester ist im Text mehrfach als "erster Admiral der Kaiserlichen Marine" bezeichnet — das ist nicht korrekt. Koester war Großadmiral und Chef der Hochseeflotte, aber nicht "erster Admiral". Faktcheck und Korrektur.
Kirchenkreis Altholstein "sieben kirchliche Friedhöfe": Die FAQ listet sieben namentlich auf (Eichhof, Südfriedhof, Holtenau, Elmschenhagen, Pries, Friedrichsort, Neumühlen-Dietrichsdorf). Das überschneidet sich mit den "städtischen" im Kostenabschnitt. Liste über friedhof-kiel.de validieren und Doppelnennungen auflösen.
Deutsche Rentenversicherung Nord, Ziegelstraße 150, 23556 Lübeck: Adresse prüfen, ggf. ist Hauptverwaltung in Lübeck Travemünder Allee. Falsche Adresse in Behörden-Listing ist ein typischer Recheck-Treffer ("Adresse mit falscher Straße/Stadt").
Friedwald Kisdorf: Es gibt einen FriedWald in Kisdorf (Kreis Segeberg) — verifizieren, ob er wirklich der "nächste" für Kieler ist (alternativ Bordesholm/Daldorf/Aukrug prüfen; RuheForst-Standorte sind teils näher).
Floskel-Detection — drei Treffer:
"eine eigene Sprache der Trauer" (Friedhofs-Übersicht, Einleitung) — generisch, streichen oder konkret machen.
"eine andere Sprache der Trauer als wenige Meter weiter" (Nordfriedhof Hidden Gem) — wiederholt die gleiche Floskel.
"ein Geflecht, das Angehörige verstehen sollten" (Hero) — leerformelartig.
"viele Friedhöfe bieten" / "die meisten Kieler Bestatter": zweimal im Bestatter-Abschnitt verwendet ("Die meisten Kieler Bestatter übernehmen die Koordination …", "mehrere im Bundesverband freier Trauerredner organisiert"). Generisch, ohne konkrete Verbandszahl/Quote. Entweder Zahl ("X von Y Mitgliedsbetrieben in Kiel") oder neutral umformulieren.
Cross-Links sind dünn: Nur ein Link zur Landesseite Schleswig-Holstein und ein Hinweiskasten. Die fertigen 13 Bundesland-Pages haben typischerweise zusätzliche Verlinkungen zu Themen-Ratgebern (Seebestattung, Friedwald, Vorsorge, Patientenverfügung). Mindestens 2–3 thematische Cross-Links ergänzen — Seebestattung als Ratgeber-Anker wäre für Kiel naheliegend.
Author-Block fehlt im sichtbaren Text: Schema sagt "machsruhig Redaktion" — gut, aber kein sichtbares Autor-/Datum-/Review-Element auf der Seite. Bei der locked decision vom 23.04.2026 ("Author-Modell = machsruhig Redaktion + Fachpool-Reviewer") muss das auch sichtbar werden. Aktuell nur in JSON-LD.
Bundesverband-Doppelung: Im Bestatter-Abschnitt werden "Bundesverband Deutscher Bestatter e.V." und "Bundesverband der Deutschen Bestattungsunternehmen e.V. (BDB)" als zwei separate Verbände genannt. Der BDB ist real (kleinerer Verband), aber die Formulierung "auch der BDB ist in Kiel vertreten" ist nicht belegt. Mitgliedernachweis für Kiel oder Aussage entfernen.
Wortzahl ~2200: liegt im Zielkorridor, ist aber näher an der Untergrenze. Mit den nötigen Quellen-Ergänzungen, einem konkreten lokalen Trauer-/Bestattungskultur-Absatz (Seebestattungs-Tradition, Norddeutsche Trauerkultur, Marinetradition als kulturelles Element) und einem kurzen "Vorsorge in Kiel"-Anker würde das Niveau der Bundesland-Pages besser erreicht.
Lokale Besonderheit "Seebestattung in der Kieler Förde" ist unter-ausgespielt. Kiel ist einer der wichtigsten Seebestattungs-Häfen Deutschlands — neben Hamburg und Cuxhaven. Dazu gehört: zugelassene Reedereien (z. B. Reederei Adler-Schiffe / Förde-Reederei Seetouristik / kleinere Anbieter), grobe Preisspanne anonym vs. begleitet, Beisetzungszone westliche Ostsee, Standard-Anbieter. Aktuell nur eine FAQ-Frage — das ist für Kiel zu wenig.
Quellen-Block: Wikipedia als Beleg für Friedhofsdaten gelistet. Für ein Audit-Niveau ≥85 sollten die Primärquellen direkt verlinkt sein (kiel.de-Friedhofsseiten, friedhof-kiel.de, Volksbund-Eintrag Nordfriedhof, Stadtarchiv Kiel "Erinnerungstage" pro Friedhof, Denkmalliste SH). Wikipedia-Pauschalverweis durch konkrete Einzel-URLs ersetzen oder als "Hintergrund" markieren.

Du bist Chat B (Reviewer). Lies Briefing https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md und v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/kiel/v1-from-chat-A.html




Stadt: Kiel (SH). Review streng nach SCORE-Tabelle. Vergib SCORE 0-100% und Fix-Liste fuer v2.

Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen
Claude is active in this tab group
Open chat
Dismiss