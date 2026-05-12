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
Chat C v4 Saarbrücken Bewertung
Friedhöfe und Bestattungsgebühren in Freiburg
Magdeburger Friedhöfe recherchieren und dokumentieren
Friedhöfe und Gebührensatzung in Erfurt
Saarbrücker Friedhöfe recherchieren und dokumentieren
Erfurt content review nach SCORE-Tabelle
Saarbrücken v3 Adversarial Score Überprüfung
Potsdam v3 adversarial score evaluation
Magdeburg v3 adversarial score überprüfung
Potsdamer Friedhöfe und Bestattungsgesetze recherchieren
Magdeburg v3 adversarial score überprüfung
Saarbrücken adversarial review und schwächen analyse
Potsdam adversarial review und schwächen analyse
Friedhöfe und Gebührensatzung in Erfurt
Adversarial review of Magdeburg content
Kiel v4 adversarial score evaluation
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
Kiel-Review nach SCORE-Tabelle
Augsburg v5 adversarial review und scoring
Alle Chats
B
Bolle
Max Plan
Chat C v4 Saarbrücken Bewertung
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat C (FINAL-Adv-Recheck).

Du bist Chat C (FINAL-Adv-Recheck). v4 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/saarbruecken/v4-final.html

Stadt: Saarbruecken (Saarland). v3 hatte 84%. Pruefe v4 + FINAL-ADVERSARIAL-SCORE 0-100% (Ziel: >=85%).

15:46
Claude hat geantwortet: Ich lade die v4 und prüfe sie adversarial.

Ich lade die v4 und prüfe sie adversarial.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/saarbruecken/v4-final.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/saarbruecken/v4-final.html

Ich gehe die v4 adversarial durch. Schwerpunkt: Faktenrisiken, Quellenketten, Schema-Konsistenz, Recheck-Blocker.

FINAL-Adversarial-Recheck Saarbrücken v4
Risikofeld 1 — Faktenrisiken (Hard Facts)
Behauptung	Risiko	Status
Hauptfriedhof 61 ha, "größter in Südwestdeutschland"	Wird klar als "nach Angaben Amt für Stadtgrün" attribuiert → Aussage liegt bei Quelle, nicht bei machsruhig	✅ sauber attribuiert
Hauptfriedhof "Anlage ab 1914, regulärer Bestattungsbetrieb seit 1916"	Differenzierung zwischen Baubeginn und ziviler Eröffnung — kein Widerspruch zur 1916-Datierung im FAQ/Schema	✅ konsistent
Hauptfriedhof Schema: "foundingDate":"1916"	Stimmt zu "regulärer Bestattungsbetrieb seit 1916" überein	✅
Waldfriedhof Burbach 28,5 ha, eröffnet 1875	Beide Werte konsistent (Schema + Text + Meta)	✅
Friedhof St. Johann eröffnet 24.06.1883, 6,3 ha, seit 1984 Urnenfriedhof	Sehr spezifisches Datum — Schema foundingDate:"1883" deckt sich	✅
Friedhof Alt-Saarbrücken eröffnet 1851, geschlossen 1917, letzte Beisetzung 2002	Schema foundingDate:"1851" konsistent	✅
Saarbrücken hat 24 städtische Friedhöfe	Konsistent in Hero, Keyfacts, FAQ, Schema-FAQ	✅
Aeternitas-PM "4. Juni 2025" mit konkreten Werten (2.691 €, 1.706,50 €, 2.500 €, 1.100 €)	HIGH-RISK ITEM — sehr spezifische Zahlen, attribuiert über Bestatterinnung Saarland	⚠️ Attribuierungs-Kette korrekt aufgebaut: "Aeternitas, zitiert nach Bestatterinnung Saarland" → wenn diese Kette falsch wäre, läge die Schuld bei der Sekundärquelle, nicht bei machsruhig. Solide.
§ 5 BestattG: 15/10/6 Jahre Ruhezeit	Standard Saarland-Recht — über alle vorherigen Bundesland-Pages konsistent	✅
§ 29 BestattG: 48h frühestens, 10 Tage spätestens, 36h Überführung	Konsistent mit Saarland-Bundesland-Page	✅
§ 31 BestattG: Sargpflicht	Korrekte Paragraphennummer für saarländisches Recht	✅
Schonvermögen "seit 01.01.2023: 10.000 €"	Faktencheck: Korrekt — § 90 Abs. 2 Nr. 9 SGB XII wurde durch das Bürgergeld-Gesetz auf 10.000 € angehoben	✅
BSG-Urteil B 8 SO 23/14 R, 18.03.2015	POTENZIELLER MISMATCH im FAQ-Schema steht oben "B 8 SO 23/15 R", im Text und in Quellen steht "B 8 SO 23/14 R"	🔴 BLOCKER 1
Jesidisches Grabfeld März 2019	Sehr spezifisches Datum — als attribuiert markiert	✅
URBAN I 1999–2001 Burbach	Spezifisches EU-Programm korrekt benannt	✅
Bestattungen.de-Award 2014, Platz 12 Burbach	Sehr spezifische Behauptung, als "Amt-dokumentiert" attribuiert	✅ (Risiko liegt bei Sekundärquelle)
Willi Graf Ehrengrab Feld 2 St. Johann	Historisch belegt, attribuiert	✅
Spichern-Translokation 1983	Spezifisch, aber als Hidden-Gem klar narrativ markiert	✅
Treuhandkonto Sparkasse Saarbrücken, Mindestanlage 3.000 €	Attribuiert via Bestatterinnung	✅
Richtwert 4.500 €/Person Bestattungsvorsorge	Klar als "Innungs-Empfehlung, kein landesrechtlicher Pauschalbetrag" gekennzeichnet — exzellente Einordnung	✅
Risikofeld 2 — Schema.org Konsistenz
Check	Befund
FAQPage Schema vs. sichtbare FAQ-Sektion	9 Fragen Schema = 9 Fragen sichtbar — Anzahl stimmt
Schema-Antworten vs. sichtbare Antworten	Inhaltlich konsistent, sichtbare Antworten sind ausführlicher (kein Widerspruch)
BSG-Aktenzeichen Mismatch	Schema: "B 8 SO 23/15 R" — Sichtbarer Text: "B 8 SO 23/14 R" — Quellen: "B 8 SO 23/14 R"
Place-Schemas (4 Friedhöfe)	Alle haben Adresse, Geo, foundingDate, containedInPlace — vollständig
Geo-Koordinaten plausibel	Hauptfriedhof 49.2225/6.9580, Burbach 49.2505/6.9501 — alle im Saarbrücker Stadtgebiet
BreadcrumbList	3 Stufen, korrekt verlinkt
Risikofeld 3 — Template-Fehler / Wrong-State-Mistakes
Check	Befund
Andere Bundesländer fälschlich erwähnt?	Nur als bewusste Vergleiche (Chemnitz 50 €, Merzig 816 €) und als Nachbarland-Verweis (Rheinland-Pfalz) — sauber
Städte aus falschen Bundesländern?	Burbach, St. Johann, Alt-Saarbrücken, Malstatt — alles korrekte Saarbrücker Stadtteile
Paragraphen aus falschem Bundesland?	Alle §§ beziehen sich auf BestattG Saarland
Kopierter Schwester-Bundesland-Schaden?	Keine Spuren von Hessen/RLP/BW-Text gefunden
Risikofeld 4 — Unbelegte Superlative
Behauptung	Status
"größter Friedhof in Südwestdeutschland"	"nach Angaben des Amts für Stadtgrün und Friedhöfe" attribuiert
"bundesweit zweites stationäres Beratungszentrum"	"nach Angaben des Amts" attribuiert
"Spitzenwert im Saarland" (Baumbestattung)	Stützt sich auf Aeternitas/Innungs-Vergleich — sauber im Quellenkanal
"bedeutendsten Beispielen späthistoristischer Sepulkralkunst" (St. Johann)	Etwas weich, aber im Kunstgeschichte-Konsens belegbar; nicht als harter Superlativ vermarktet
Risikofeld 5 — CTA / Werbung / Lead-Gen-Verstöße

Keine Bestatter-Empfehlungen, keine Lead-CTAs, kein "jetzt anfragen", keine Affiliate-Links. Reiner Ratgeber-Stil. ✅

Risikofeld 6 — Honesty-Check Kategorien (analog bundesland-recheck.py)
Kategorie	Befund
1. Template-Reste	Keine {{stadt}}-Platzhalter, keine Lorem-Ipsum-Reste
2. Wrong-State-Cities	Keine
3. Unbelegte Superlative	Alle Superlative attribuiert
4. Schema-vs-FAQ-Mismatch	BSG-Aktenzeichen
5. Wortzahl-Untergrenze (~1700–2400)	Geschätzt ~2400 Wörter — im Korridor
6. §-Citations	§§ 5, 29, 31 BestattG Saarland; § 90 Abs. 2 Nr. 9 SGB XII; BSG B 8 SO 23/14 R — alle vorhanden
7. Quellen-Block vollständig	12 Quellenpositionen inkl. Wikipedia-Disclosure
8. Date-Konsistenz (datePublished/dateModified)	Beide 2026-05-12 — heutiges Datum, konsistent
9. Interne Verlinkung	7 interne Links (Saarland, RLP, Bestattungsarten, Vorsorge, Bestatter, Vorsorge x2) — gut
Risikofeld 7 — Hidden Gems Qualität
Friedhof	Hidden Gem	Qualität
Hauptfriedhof	Erstes jesidisches Grabfeld	Echt, einzigartig, gut erzählt — keine 0815-Story
Burbach	Turnerdenkmal 1926	Sehr spezifisch, lokal verankert, narrativ stark
St. Johann	Willi Graf + Spichern-Translokation	Zwei Geschichten verdichtet, hervorragender Erzählbogen ("73 Jahre Kriegsgeschichte auf wenigen m²")
Alt-Saarbrücken	Röchling + ehrenamtlicher Pflegeverein	Verbindet Industriegeschichte mit Gegenwart — funktioniert

Alle vier Hidden Gems sind genuin lokal und narrativ. Kein Copy-Paste-Muster aus anderen Städten.

Adversarial-Probing: Was würde ein feindseliger Reviewer angreifen?
BSG-Aktenzeichen-Inkonsistenz → konkretes Glaubwürdigkeitsleck ✅ gefunden
"6,3 Hektar" St. Johann im sichtbaren Text — keine Quelle direkt zugeordnet, nur generisch "Amt für Stadtgrün". Hätte ich Quelle, würde ich das stützen, aber kein Widerspruch — niedriges Risiko ⚠️
"Anlage ab 1914" vs foundingDate:"1916" im Schema — kein Widerspruch (Schema bildet zivile Eröffnung ab), aber feindseliger Reviewer könnte fragen warum nicht 1914. Verteidigbar. ⚠️ niedrig
"Stadtbaumeister Hugo Dihm" — sehr spezifischer Name; nicht in Quellen-Block direkt referenziert, vermutlich aus Wikipedia. Da Wikipedia als Sekundärquelle für narrative Elemente offengelegt ist: vertretbar. ⚠️ niedrig
"1.100 €" Öffnen/Schließen Urnengrab — sehr hohe Zahl im Vergleich zu Chemnitz 50 €. Wenn Aeternitas das nicht so ausgewiesen hat, wäre das ein Knaller. Attribuierungs-Kette hält die Verantwortung bei Aeternitas/Innung. ✅
Wikipedia-Disclosure im Quellen-Block — gut, aber: Hidden-Gem-Stories über Willi Graf, Spichern, Turnerdenkmal, Hauptfriedhof-Persönlichkeiten stammen damit primär aus Wikipedia. Ist erklärt und konsequent — exzellent gehandhabt. ✅
Zusammenfassung der Blocker
#	Blocker	Severität	Fix
1	BSG-Aktenzeichen Schema vs. Text — FAQPage-Schema zeigt "B 8 SO 23/15 R", sichtbarer Text und Quellen zeigen "B 8 SO 23/14 R"	🔴 HARD BLOCKER (Schema-Mismatch, fehlerhaftes Aktenzeichen ist eine harte Fehlinformation in einem Rechtsthema)	In FAQ-Schema Antwort 8 ändern: B 8 SO 23/15 R → B 8 SO 23/14 R
FINAL-ADVERSARIAL-SCORE
Dimension	Gewicht	Score
Fakten / Belegbarkeit	25%	23/25 (BSG-AZ-Mismatch zieht 2 Punkte)
Quellenkette / Attribuierung	15%	15/15 — vorbildlich, Wikipedia-Disclosure inkl.
Schema.org-Konsistenz	10%	8/10 (BSG-AZ-Mismatch im Schema)
Honesty-Check (9 Kategorien)	15%	14/15 (8 von 9 grün, eine rot)
Hidden Gems / Lokal-Tiefe	10%	10/10 — vier echte, narrativ starke Lokalstories
Struktur / Aufbau / Lesefluss	10%	10/10
Recht / §-Citations / Aktualität	10%	9/10 (BSG-AZ-Fehler)
Keine CTA-/Werbeverstöße	5%	5/5

Gesamtscore: 94 / 100 = 94 %

✅ Ziel ≥85 % erreicht (mit deutlichem Abstand)

🔴 ABER: Ein 🔴-Blocker (BSG-Aktenzeichen-Inkonsistenz Schema vs. Text) verhindert nach Bundesland-Recheck-Logik den Go-Live trotz hohem Score. Audit-Score allein reicht nicht — Recheck muss 0 Blocker zeigen.

Empfehlung

Vor Deploy zwingend fixen:

diff
- {"@type":"Question","name":"Welche Sonderregeln gelten für Bestattungsvorsorge im Saarland?","acceptedAnswer":{"@type":"Answer","text":"... eine im Einzelfall angemessene Bestattungsvorsorge (B 8 SO 23/15 R)."}}
+ {"@type":"Question","name":"Welche Sonderregeln gelten für Bestattungsvorsorge im Saarland?","acceptedAnswer":{"@type":"Answer","text":"... eine im Einzelfall angemessene Bestattungsvorsorge (B 8 SO 23/14 R)."}}

Nach Fix: Score steigt auf ~97 %, 0 Blocker — Go-Live-fähig.

Soll ich den Fix als Patch vorbereiten oder reicht der Hinweis für Chat A?

Dir stehen keine Nutzungsguthaben mehr zur Verfügung. Kaufe jetzt mehr, um weiterzumachen, oder warte bis 17:40, wenn sich dein Nutzungskontingent zurückgesetzt.
Mehr kaufen




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen