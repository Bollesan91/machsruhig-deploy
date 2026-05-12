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
Saarbrücken adversarial review und schwächen analyse
Magdeburger Friedhöfe recherchieren und dokumentieren
Potsdamer Friedhöfe und Bestattungsgesetze recherchieren
Adversarial review of Magdeburg content
Kiel v4 adversarial score evaluation
Saarbrücker Friedhöfe recherchieren und dokumentieren
Kieler Friedhöfe und Bestattungskultur recherchieren
Potsdam content review nach SCORE-Tabelle
Saarbrücken content review nach SCORE-Tabelle
Magdeburg-Review nach SCORE-Tabelle
Kiel v3 Bewertung: Adversarial-Score-Überprüfung
Augsburg v6 Qualitätsprüfung und Adversarial-Scoring
Mainz v3 adversarial review und scoring
Augsburger Friedhöfe und Bestattungsregeln
Wiesbaden v4 adversarial review und scoring
Mainzer Friedhöfe und Bestattungskultur recherchieren
Adversarial review of Kiel briefing materials
Wiesbadener Friedhöfe und Bestattungsgesetze recherchieren
Adversarial review of Mainz content
Augsburg v5 adversarial review und scoring
Kiel-Review nach SCORE-Tabelle
Wiesbaden v3 Compliance-Überprüfung
Mainz content review nach SCORE-Tabelle
Augsburg v4 Bewertung und Adversarial-Score
Adversarial review of Wiesbaden content
Mannheim v4 adversarial quality review
HTML-Seite für Bestatter Mannheim erstellen
Adversarial review v3 Augsburg
Karlsruhe v4 adversarial review und final score
HTML-Seite für Bestatter in Karlsruhe
Alle Chats
B
Bolle
Max Plan
Saarbrücken adversarial review und schwächen analyse
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat C (Adversarial Reviewer).

Du bist Chat C (Adversarial Reviewer). Lies Briefing https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md und v2 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/saarbruecken/v2-from-chat-A.html

Stadt: Saarbruecken (Saarland). 3 Schwaechen + ADVERSARIAL-SCORE 0-100%.

15:14
Claude hat geantwortet: Ich lese beide Dateien.

Ich lese beide Dateien.

Web durchsucht
Web durchsucht

Lese als Adversarial Reviewer. Mindset: die Page ist unter 85. 3 Schwächen finden.

Durchgang im Kopf nach den 12 Kategorien — was springt raus:

Halluzinations-Verdacht "Hauptfriedhof eröffnet 1914": Die Page sagt einerseits "Eröffnet 1914" und in Section #recht "Ab 1916 erfolgten zivile Beisetzungen, 1917 wurden die innerstädtischen Friedhöfe St. Johann und Alt-Saarbrücken offiziell geschlossen". Aber der Hauptfriedhof Saarbrücken wurde tatsächlich 1916 eröffnet (mit Kriegsgräbern angefangen wurde 1914/15, offizielle Eröffnung 1916). Risiko — kann ich nicht zu 100% verifizieren ohne Suche, aber Verdacht.
"bundesweit zweite stationäre Beratungszentrum": Sehr spezifische Behauptung ("bundesweit zweite"), wird mit "nach Angaben der Stadt" abgesichert, aber im Sources-Block kein konkreter URL für diese Aussage — schwacher Quellen-Anker für eine so spezifische Superlative.
Aeternitas-Behauptung in FAQ-Schema: Im FAQ-Schema steht "Ein Erdwahlgrab für 20 Jahre liegt nach Aeternitas-Auswertung bei rund 2.691 Euro" — aber im Sichtbar-Text und in der Tabelle wird derselbe Wert der "Bestatterinnung Saarland" zugeschrieben. Quellen-Widerspruch zwischen Schema und Body.
Sektion Vorsorge sehr kurz: Nur 2 Absätze, kein Cross-Link zur Saarland-Bundeslandseite an der Stelle, wo sie thematisch hingehört.
Cross-Links zu Stadtteilen / anderen Saarland-Städten fehlen: Die Page verweist auf Saarland-Bundesland und Rheinland-Pfalz, aber es gibt keinen Verweis auf andere Saarland-Städte (Völklingen, Neunkirchen, Saarlouis).
"Marktdaten Bestattungsdienstleister": Die Tabelle nennt drei Werte mit der Quelle "Marktdaten Bestattungsdienstleister, 2024/25" — das ist keine identifizierbare Primärquelle. Welcher Dienstleister? Welche URL? Quellen-Lücke für 3 von 6 Tabellenwerten.
"Eröffnet 1914" Hauptfriedhof: Sehr wahrscheinlich falsch — Hauptfriedhof Saarbrücken offiziell 1916. Risikoaussage.
"Bestattungen.de-Award Platz 12, 2014": Wird der Friedhofsdokumentation des Amts zugeschrieben, aber Bestattungen.de selbst ist ein Bestatter-Portal — die Auszeichnung 2014 lässt sich heute schwer verifizieren, kein Link.
Sektion Bestatter-Wahl-Liste: Sehr generisch ("24 Stunden erreichbar", "geprüfte Bestattungsfachkraft") — Floskel-nah, könnte auf jeder Stadt-Page stehen, kein Saarbrücken-Spezifikum.

Die drei stärksten Schwächen:

SCHWÄCHE 1: Tabelle "Bestattungskosten in Saarbrücken" — Quellen-Lücke bei 3 von 6 Werten — Die Werte für Urnen-Wahlgrab (1.240 €), Sarg-Reihengrab (1.620 €) und Sarg-Wahlgrab (2.380 €) werden mit "Marktdaten Bestattungsdienstleister, 2024/25" beschriftet. Das ist keine zitierfähige Primärquelle — kein Anbieter genannt, kein Link, kein Stichtag. Bei einer rechts-/gebührenrelevanten Tabelle ist das in einer 9-Kategorien-Honesty-Prüfung ein klarer Blocker. — Verbesserung: Entweder konkrete Anbieter mit URL und Stand benennen (z.B. "Preisliste Bestatter X, Stand 03/2025") oder die drei Zeilen aus der Tabelle entfernen und stattdessen die Friedhofsgebührensatzung selbst zitieren (§ und Anlage). Halbe Quelle ist schlechter als keine Zeile.

SCHWÄCHE 2: Widerspruch zwischen FAQ-Schema und sichtbarem Body bei der Quellenangabe zum Erdwahlgrab-Preis — Im JSON-LD FAQ-Schema steht "Ein Erdwahlgrab für 20 Jahre liegt nach Aeternitas-Auswertung bei rund 2.691 Euro". Im sichtbaren Body und in der Tabelle wird derselbe Wert (2.691 €) der Bestatterinnung Saarland zugeschrieben. Zwei verschiedene Quellen für dieselbe Zahl — entweder falsch im Schema oder falsch im Body. Search-Engines lesen beides; Inkonsistenz ist auch ein E-A-T-Signal. — Verbesserung: Eine Quelle festlegen (Aeternitas-Pressemitteilung vom 4. Juni 2025 wird ohnehin im Quellen-Block aufgeführt — wahrscheinlich ist Aeternitas die richtige Quelle, "Bestatterinnung Saarland" im Body korrigieren). Tabelle, Body, Schema, FAQ-Body und Quellenliste müssen alle dieselbe Quelle nennen.

SCHWÄCHE 3: Datum "Hauptfriedhof eröffnet 1914" widerspricht der eigenen Body-Aussage — Im mr-cem-meta steht "Eröffnet 1914", aber direkt darunter im Fließtext steht: "diente die Anlage zunächst nur als Begräbnisstätte für gefallene Soldaten des Ersten Weltkriegs. Ab 1916 erfolgten zivile Beisetzungen". Die übliche Datierung des Hauptfriedhofs Saarbrücken ist 1916 (offizielle Inbetriebnahme als regulärer Friedhof; die 1914er-Datierung bezieht sich auf den Beginn der Kriegsgräber-Nutzung). Im Schema.org-Block fehlt zudem ein foundingDate — d.h. der Widerspruch bleibt für Search-Engines im sichtbaren Text. Ein Honesty-Check mit Kategorie "Daten/Fakten-Konsistenz" würde das fangen. — Verbesserung: Meta-Zeile präzisieren: "Eröffnet 1916 (Kriegsgräber-Belegung ab 1914)" oder umgekehrt "Anlage seit 1914, regulärer Bestattungsbetrieb ab 1916". Quelle im Sources-Block ergänzen (saarbruecken.de-Friedhofsdokumentation oder Wikipedia mit Stand).

EHRLICHE %-ZAHL: 76%




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen
Claude is active in this tab group
Open chat
Dismiss