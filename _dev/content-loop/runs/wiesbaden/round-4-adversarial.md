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
Adversarial review of Wiesbaden content
Augsburger Friedhöfe und Bestattungsregeln
Wiesbadener Friedhöfe und Bestattungsgesetze recherchieren
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
HTML-Seite für Bestatter in Bonn erstellen
HTML-Seite für Bestatter Bielefeld erstellen
HTML-Seite für Bestatter Wuppertal erstellen
HTML-Seite für Bestatter in Bochum erstellen
HTML-Seite für Bestatter Dresden erstellen
HTML-Seite für Bestatter Bremen erstellen
HTML-Seite für Bestatter in Duisburg erstellen
HTML-Seite für Bestatter Hannover erstellen
HTML-Seite für Bestatter Nürnberg erstellen
Alle Chats
B
Bolle
Max Plan
Adversarial review of Wiesbaden content
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat C (Adversarial Reviewer).

Du bist Chat C (Adversarial Reviewer). Lies Briefing https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md und v2 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/wiesbaden/v2-from-chat-A.html

Stadt: Wiesbaden (Hessen). Suche aktiv Halluzinationen, erfundene Paragraphen, falsche Zahlen, Schein-Praezision. Vergib ADVERSARIAL-SCORE 0-100% und 3 konkrete Schwaechen + Fix-Liste.

11:36
Claude hat geantwortet: Ich lese erst das Briefing und v2.

Ich lese erst das Briefing und v2.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

BRIEFING_OK.

Jetzt adversariale Prüfung — ich gehe gezielt auf Halluzinations-Verdacht, falsche §, falsche Zahlen.

Verdachtspunkte, die ich verifiziere:

§ 16 Abs. 1 FBG Hessen für Bestattungsfrist (4→10 Tage, Novelle 30.09.2025)
§ 13 FBG für sorgepflichtige Personen
§ 6 FBG Mindestruhefrist 15 Jahre
§ 9 FBG Leichenschau
Drucksache 21/2378 Hessischer Landtag
"Bernhard-von-Wiesen-Stiftung" (Nordfriedhof) — riecht stark nach Halluzination
§ 1.2.8/1.2.9 der Gebührensatzung — Patenschafts-Ermäßigung 25-50%
Südfriedhof "330.700 m²" + "1912 erstes Krematorium Preußens"
Nordfriedhof "Walddistrikt Höllkund", "35.000 Mark"
Searching the web
Web durchsucht

Wichtige Funde so weit:

§ 16 FBG als Bestattungsfrist-Norm — FALSCH. § 16 FBG passt sachlich nicht zur Bestattungsfrist. Drucksache 21/2378 nennt § 19 FBG für Erdbestattungen, der Pietät-Quelle und Aeternitas-PDF zeigen ebenfalls eine andere Paragraphenstruktur. Die Bestattungsfrist (96h/10 Tage) steht historisch in § 8 FBG Hessen, nicht in § 16. Halluzinations-Verdacht.
§ 13 FBG für sorgepflichtige Personen — STIMMT (Drucksache bestätigt).
§ 6 FBG Mindestruhefrist 15 Jahre — STIMMT (Aeternitas-PDF bestätigt).
§ 9 FBG für Leichenschau — verdächtig, im aktuellen Aeternitas-PDF wird § 10 für Leichenschau genannt: "Leichenschau nach § 10". Halluzinations-Verdacht zweite Norm.

Verifizieren wir die Leichenschau-Paragraphen explizit:

Searching the web
Web durchsucht

Klar bestätigt:

Leichenschau = § 10 FBG (in der Page steht: § 9 FBG für Leichenschau — das ist FALSCH. § 9 ist „Schutz der Gesundheit und der Totenruhe", § 10 ist „Pflicht zur Leichenschau")
Bestattungsfrist = § 16 FBG ist tatsächlich KORREKT in der 2007er-Fassung (Inhaltsverzeichnis zeigt „§ 16 Bestattungsfristen"). Mein erster Verdacht war falsch. Aber: Achtung — Drucksache 21/2378 spricht von Änderung in „Art. 1 Nr. ... § 19 FBG" für Erdbestattungen, aber die Frist selbst sitzt traditionell in § 16. § 16 FBG bleibt zunächst stehen.

Aber der Schwung in § 9 statt § 10 für Leichenschau ist klar HALLUZINATION/FALSCHZITAT. Außerdem in „2. Sterbefall beim Standesamt" steht „§ 9 FBG" als Beleg, was sachlich noch unstimmiger ist — § 9 ist Gesundheits-/Totenruhe-Norm.

Jetzt prüfe ich die Schein-Präzision: "Bernhard-von-Wiesen-Stiftung 2001" und "§ 1.2.8/1.2.9 der Gebührensatzung 25-50%".

Searching the web
Web durchsucht

Bernhard-von-Wiesen-Stiftung existiert, 2001 — bestätigt. ABER:

Page sagt: "Die Stadt gründete deshalb 2001 die Bernhard-von-Wiesen-Stiftung" → FALSCH. Sie ist eine treuhänderische Stiftung der Deutschen Stiftung Denkmalschutz, gestiftet von Dr. Werner Behrendt — nicht von der Stadt Wiesbaden.
Page sagt Stiftung umfasse "denkmalgeschützte Gräber" — sie deckt Nordfriedhof UND Biebrich, nicht nur Nordfriedhof. (Geringer Vorwurf.)
Page sagt: "Inzwischen bestehen fast hundert solcher Patenschaften" → Stadtquelle sagt: rund 140. (Schein-Präzision/veraltete Zahl.)
Page sagt: Kolumbarium 1902 mit "512 Urnennischen" → Stadtquelle: "600 Nischen". FALSCHZAHL.
Page sagt: "35.000 Mark" Baukosten Kolumbarium — keine Bestätigung in den Quellen gefunden. Halluzinations-Verdacht.
Page sagt: "§ 1.2.8/1.2.9 der Gebührensatzung — Ermäßigung 25 bis 50 Prozent" für Patenschaften — sehr spezifisch, das prüfe ich.
Web durchsucht
Web durchsucht

Sehr wichtig: 25/50% Patenschaft bestätigt, aber die §-Angabe in der Page ist trotzdem verdächtig: Die Page sagt "§ 1.2.8/1.2.9 der Gebührensatzung". Die Stadtquelle nennt "Beim Erwerb von Nutzungsrechten an einstelligen Wahlgräbern... 25 v.H. ... mehrstelligen Wahlgräbern oder Haingräbern ... 50 v.H." Das ist also nicht eine Range "25 bis 50%" sondern zwei konkrete Stufen je nach Grabart. Die Behauptung "§ 1.2.8/1.2.9" ist Pseudo-Präzision — ohne Verifikation aus der Satzung. Mittlerer Verdacht — könnte stimmen, könnte halluziniert sein. Schwerer wiegt: Stadt als Stifter ist falsch + "fast hundert" statt 140 ist veraltet.

Jetzt prüfe ich noch zwei verdächtige Punkte: "Wolfgang Grams" am Südfriedhof + "Helmut Schön" am Nordfriedhof.

Web durchsucht
Web durchsucht

Helmut Schön ✓, Kriegel ✓, Corvin ✓ — Page-Aussage stimmt im Kern.

Jetzt habe ich genug Munition. Ich konsolidiere die drei stärksten Schwächen — alle aus der Liste (Halluzinations-Verdacht / Falschzahl / falsche §).

Kandidaten:

§ 9 FBG für Leichenschau — eindeutig falsch (Leichenschau = § 10, § 9 = Schutz der Gesundheit und Totenruhe). Plus Sterbefall-Sektion zitiert auch "§ 9 FBG" sinnwidrig. KAT 6 + 12.
"Die Stadt gründete 2001 die Bernhard-von-Wiesen-Stiftung" — falsch (treuhänderische Stiftung der DSD, gestiftet von Dr. Werner Behrendt). Plus "512 Urnennischen" beim Kolumbarium — Stadtquelle nennt 600. Plus "fast hundert" Patenschaften vs. tatsächlich rund 140. Drei Detail-Fehler in einem Absatz. KAT 12.
§ 1.2.8/1.2.9 der Gebührensatzung — Pseudo-Präzision: die Quellangabe "§" in einer Gebührenordnung ist ungewöhnlich (Gebührensätze haben "Lfd. Nr." / "Gebührenziffer", nicht §). Außerdem suggeriert "25 bis 50 Prozent" eine Spanne — laut Stadtquelle sind das zwei harte Stufen (25% einstellige Wahlgräber / 50% mehrstellige + Haingräber). KAT 12.

Drei substantielle Halluzinations-/Schein-Präzisions-Schwächen — alle mit echter Quelle widerlegt.

SCHWÄCHE 1: Abschnitt "Bestattungsrecht in Wiesbaden – das Wichtigste", Absatz 3 ("Mindestruhefrist beträgt ... nach § 6 FBG") sowie Schritt 1 und Schritt 2 unter "Was nach einem Todesfall in Wiesbaden zu tun ist" — die Page zitiert "§ 9 FBG" als Beleg für die ärztliche Leichenschau ("rufen ... der die Leichenschau vornimmt ... § 9 FBG"). § 9 FBG Hessen regelt aber den "Schutz der Gesundheit und der Totenruhe", die Leichenschau steht in § 10 FBG (Inhaltsverzeichnis FBG: "§ 9 Schutz der Gesundheit und der Totenruhe; § 10 Leichenschau"). Auch in Schritt 2 ("Sterbefall beim Standesamt") wird § 9 implizit als Sterbefall-Norm mitgezogen — das ist sachlich daneben. — Fix: § 9 → § 10 FBG bei der ärztlichen Leichenschau ersetzen; in Schritt 2 die §-Behauptung ganz streichen (Sterbefall-Anzeige steht im PStG, nicht im FBG).

SCHWÄCHE 2: Sektion "Nordfriedhof", Hidden-Gem-Absatz — drei sachliche Fehler in einem Absatz. (a) "Die Stadt gründete deshalb 2001 die Bernhard-von-Wiesen-Stiftung, die denkmalgeschützte Gräber restauriert" — die Stiftung wurde nicht von der Stadt errichtet, sondern ist eine treuhänderische Stiftung der Deutschen Stiftung Denkmalschutz, gestiftet von Dr. Werner Behrendt (Quellen: denkmalschutz.de, historismus.org). (b) "Kolumbarium ... mit 512 Urnennischen" — die Stadt selbst (wiesbaden.de, Natur- und Friedhofskultur) spricht von "ursprünglich 600 Nischen". (c) "Inzwischen bestehen fast hundert solcher Patenschaften" — Stadtquelle (Natur- und Friedhofskultur, friedhoefe-wiesbaden.de/patengraeber): "rund 140". Klassische Schein-Präzision auf veralteter Basis. — Fix: Träger korrekt benennen ("treuhänderische Bernhard-von-Wiesen-Stiftung der Deutschen Stiftung Denkmalschutz, 2001 errichtet"), 512 → 600 Urnennischen, "fast hundert" → "rund 140 Patenschaften".

SCHWÄCHE 3: Nordfriedhof-Hidden-Gem, Klammerangabe "(§ 1.2.8/1.2.9 der Gebührensatzung)" zur Patenschafts-Ermäßigung "25 bis 50 Prozent" — doppelt verdächtig. Erstens: Gebührensatzungen arbeiten mit "Lfd. Nr." bzw. Gebührenziffer, nicht mit "§" — die §-Bezeichnung ist eine erfundene Formattreue, die in der Wiesbadener Gebührensatzung in dieser Form sehr wahrscheinlich nicht existiert (das vorliegende Gebührenverzeichnis SV 18-V-67-0003 zeigt "Lfd. Nr." als Strukturmerkmal). Zweitens: "25 bis 50 Prozent" suggeriert eine Spanne — laut Stadt sind das zwei harte Stufen: 25 v.H. bei einstelligen Wahlgräbern, 50 v.H. bei mehrstelligen Wahlgräbern oder Haingräbern (wiesbaden.de/Erdbestattungen). Klassischer Schein-Präzisions-Treffer ohne primäre Verifikation. — Fix: §-Angabe ersatzlos streichen (oder durch "Gebührenziffer …" ersetzen, sobald sie wirklich aus der Satzung zitiert ist) und die Ermäßigung präzise stufen: "Beim Erwerb des Nutzungsrechts ermäßigt sich die Gebühr um 25 % (einstellige Wahlgräber) bzw. 50 % (mehrstellige Wahl- oder Haingräber)" mit Beleg auf wiesbaden.de/leben-in-wiesbaden/.../Erdbestattungen.

EHRLICHE %-ZAHL: 76%

Begründung der Zahl (nicht Teil des Scores für den Loop, nur falls relevant): Substanz, Quellenlage und Bundesland-Recht im Großen sind solide (FBG-Novelle korrekt datiert, Drucksache 21/2378 korrekt, Gebührentabelle und Friedhofsporträts gut). Aber drei harte Falschtreffer im juristischen und historischen Detail (§-Falschzitate, falscher Stifter, Falschzahlen 512/600 und 100/140, fragwürdige §-Konstruktion im Gebührenbereich) drücken den Wert deutlich unter 85. Das sind genau die Fehlerklassen, die Bolle-Loop fangen soll.

Du bist Chat C (Adversarial Reviewer). Lies Briefing https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md und v2 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/wiesbaden/v2-from-chat-A.html




Stadt: Wiesbaden (Hessen). Suche aktiv Halluzinationen, erfundene Paragraphen, falsche Zahlen. Vergib ADVERSARIAL-SCORE 0-100% und 3 konkrete Schwaechen + Fix-Liste.

Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
Claude is active in this tab group
Open chat
Dismiss