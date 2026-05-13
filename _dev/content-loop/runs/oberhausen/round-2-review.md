Neuer Chat
Ctrl+⇧+O
Suchen
Ctrl+K
Chats
Projekte
Code
Anpassen
Design
Mehr
Zuletzt verwendet
Ausblenden
Oberhausen SCORE-Review und Fix-Liste
Erfurt v5 final adversarial score evaluation
HTML-Version mit Review-Fixes liefern
Friedhöfe und Bestattungen in Hagen
Chat C v5 Halle Adversarial Score Evaluation
Friedhöfe und Bestattungen in Oberhausen
Erfurt v5 final adversarial score evaluation
Erfurt v5 adversarial score evaluation
Hagen-Review nach SCORE-Tabelle
v4 HTML-Version mit Adversarial-Fixes
HTML-Version v4 mit Adversarial-Fixes
Freiburg Schwächen und adversariales Scoring
Friedhöfe und Bestattungen in Oberhausen
Friedhöfe und Bestattungen in Oberhausen
Hagen-Review nach SCORE-Tabelle
Chat C final adversarial recheck for Halle
Erfurt v4 adversarial score evaluation
Saarbrücken FINAL-Adv-Recheck v6 Bewertung
HTML-Version v6 mit BSG-Aktenzeichen-Fixes
HTML-Version mit Review-Fixes liefern
Chat C v3 Halle performance evaluation
Chemnitz v3 adversarial score evaluation
Krefeld v3 adversarial score evaluation
Friedhöfe und Bestattungen in Krefeld
Friedhöfe und Bestattungen in Halle (Saale)
Chemnitz Friedhöfe und Denkmalschutz
Halle adversarial analysis and weaknesses
Krefeld Schwächen und Adversarial-Score
Heidelberg v4 adversarial score evaluation
Heidelberg v4 adversarial score evaluation
Chemnitz Schwächen und Adversarial-Bewertung
Alle Chats
B
Bolle
Max Plan
Oberhausen SCORE-Review und Fix-Liste
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/oberhausen/v1-from-chat-A.html

Stadt: Oberhausen (NRW). Review nach SCORE-Tabelle. SCORE 0-100% + Fix-Liste.

11:23
Claude hat geantwortet: Ich lade v1 und mache den Review.

Ich lade v1 und mache den Review.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/oberhausen/v1-from-chat-A.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/oberhausen/v1-from-chat-A.html

Ich verifiziere kritische Fakten gegen Primärquellen, bevor ich scoree.

Fetching site
Fetched: https://www.oberhausen.de/de/index/rathaus/verwaltung/soziales-gesundheit-wohnen-und-recht/recht/ortsrecht_der_stadt_oberhausen/ortsrecht-material/250101_friedhofsgebuehrensatzung_2025.pdf

Wichtige Funde gegen Primärquelle. Jetzt BestG NRW verifizieren.

Fetching: https://recht.nrw.de/lmi/owa/br_text_anzeigen?v_id=5320141007092133713
Web durchsucht

Wichtige Gesetzes-Verifikationen abgeschlossen. Jetzt das Volksbund-Datum prüfen.

Fetching: https://kriegsgraeberstaetten.volksbund.de/friedhof/oberhausen-westfriedhof
Fetched: Kriegsgräberstätte: Oberhausen, Westfriedhof - Bau, Pflege und Instandsetzung | Volksbund.de

Wichtiger Befund: Volksbund nennt "Gesamtbelegung: 2.192 Tote" oben (Bauwerk-Belegung), aber im Text 2.218 Kriegsopfer auf den Ehrenfeldern. Chat A's "2.218" steht im Text als Gesamtbelegung. Das ist eine numerische Doppeldeutigkeit, die ich im Review erwähnen sollte. Aber prinzipiell ist "2.218 Kriegsopfer" durch die Quelle gedeckt. Jetzt prüfe ich noch das BestG-Datum 17.06.2003 sowie die "1808 GHH" und ein paar weitere Punkte.

Searching the web
Web durchsucht

Wichtige Befunde:

BestG NRW Datum: Chat A schreibt "Stand 01.02.2024" und "geändert durch Gesetz vom 1. Februar 2022" - die korrekte Fassung ist "vom 19.02.2022" (in Kraft getreten am 19. Februar 2022 durch Artikel 71 des Gesetzes vom 1. Februar 2022). Chat A vermischt zwei Daten - der Artikel 71 ist vom 1.2.2022, aber Inkrafttreten 19.02.2022. "Stand 01.02.2024" ist FALSCH - es muss "Stand 19.02.2022" heißen.
GHH Gründung 1808 in Oberhausen: Chat A schreibt "ab 1808 in Oberhausen drei Eisenhütten zusammenführte". Korrekt ist: 1808 wurden die Anteile eingebracht (JHH), aber der 1810er Gesellschaftervertrag gilt als offizielles Gründungsdokument. "Ab 1808" ist vertretbar, aber etwas ungenau.
Volksbund 2.218 vs. 2.192: Volksbund-Seite gibt "Gesamtbelegung: 2.192 Tote" oben an, im Text aber "2.218 Kriegsopfer auf den Ehrenfeldern" – die Differenz erklärt sich vermutlich aus dem Stichtag bzw. Definition. Beide Werte werden auf der Quelle genannt - "2.218" ist also belegt (im Fließtext).
Gebührentabelle: Chat A's Tabelle hat 13 Zeilen, Satzung hat 18 (1.1 bis 1.18). Es fehlen 1.14 (Gemeinschaftsgrab Urne 259€), 1.15 (Stelenkammer 1.658€), 1.16 (Anonym Sarg 683€), 1.17 (Anonym Urne 430€), 1.18 (Verlängerung). Die Tabelle ist UNVOLLSTÄNDIG – speziell die expliziten Anonym-Gebühren (683€/430€) fehlen, obwohl Anonyme Bestattungen prominent erwähnt werden. Das ist ein konkreter Fehler.

Jetzt habe ich genug für das Review.

SCORE-Review v1: Oberhausen

SCORE: 73 / 100

Status: NICHT FREIGEGEBEN für Deploy. Solides Fundament, aber kritische Faktenfehler in BestG-Datierung und unvollständige Gebührentabelle.

Score-Tabelle nach Kategorien
#	Kategorie	Gewicht	Score	Punkte
1	Faktentreue (Primärquellen)	20	60%	12
2	§-Citations & Rechtsbezug	15	85%	12,75
3	Vollständigkeit (Friedhöfe, Kosten, Ablauf)	15	80%	12
4	Quellen-Transparenz	10	90%	9
5	Lokales Kolorit / Hidden Gems	10	90%	9
6	Schema.org & SEO	10	85%	8,5
7	Struktur & Lesbarkeit	10	80%	8
8	Ehrlichkeit (keine unbelegten Superlative)	10	75%	7,5
Summe		100		~73
Blocker (BLOCKER, müssen vor Deploy gefixt werden)
B1 — BestG-NRW-Datum falsch

Problem: Hero, Keyfacts und Fließtext sagen „BestG NRW vom 17.06.2003, Stand 01.02.2024" bzw. „zuletzt durch das Gesetz vom 1. Februar 2022 geänderten Fassung".

Korrekt nach recht.nrw.de: BestG NRW vom 17.06.2003, aktuelle Fassung gültig ab 19.02.2022 (geändert durch Artikel 71 des Gesetzes vom 1. Februar 2022, GV. NRW. S. 122, in Kraft getreten am 19.02.2022). Es gibt keine Änderung von 2024.

Fix: Überall „Stand 01.02.2024" → „Fassung vom 19.02.2022" ersetzen. Betroffen: <meta description> (NICHT betroffen), Keyfacts-DD, §-Recht-Absatz, Quellenverzeichnis Eintrag #1.

B2 — Gebührentabelle unvollständig (relevant für Anonym-Frage)

Problem: Die Tarif-Tabelle zeigt nur 13 Zeilen (1.1–1.13). In der Satzung-Anlage gibt es 18 Tarifstellen (1.1–1.18). Besonders kritisch: Die Seite spricht prominent über anonyme Bestattungen (Hero, Friedhöfe, FAQ, Kostenspanne 2.000–3.000 €), aber die Tabelle enthält die explizite Tarifstelle nicht.

Korrekt laut Satzung:

1.14 Gemeinschaftsgrab Urne — 259 €
1.15 Stelenkammer Urne — 1.658 €
1.16 Anonym Sarg — 683 €
1.17 Anonym Urne — 430 €
1.18 Verlängerung Nutzungsrecht — 1/30 je angefangenes Jahr

Fix: Tabelle um die fehlenden 5 Zeilen ergänzen. Zusätzlich die Kostenspanne „Anonyme Urnenbestattung 2.000–3.000 €" prüfen — mit Tarifstelle 1.17 (430 €) + Grabbereitung 2.17 (397 €) + Pflege 3.18 (295 €) liegt man bei ~1.122 € reinen Friedhofsgebühren; 2.000–3.000 € als Gesamtspanne ist plausibel, aber der Hinweis auf den Stelenkammer-Tarif (1.658 €) fehlt komplett, obwohl es eine reale Bestattungsoption ist.

B3 — „Bund-der-Steuerzahler 2022, 765 €" — Quelle nicht verlinkt/auffindbar

Problem: Chat A behauptet „eine Urnenbeisetzung im Reihengrab lag laut Bund-der-Steuerzahler-Vergleich 2022 mit 765 Euro deutlich unter dem damaligen NRW-Durchschnitt" und „Mit der Neufassung 2025 stiegen die Gebühren ... um rund 21 Prozent ... rund 18 Prozent". Die verlinkte Quelle 7 zeigt aber den BdSt-Vergleich 2025, nicht 2022. Ohne Primärbeleg: unbelegter Superlativ / Datums-Behauptung.

Fix: Entweder (a) konkreten BdSt-2022-Link nachreichen UND die Prozentsätze (21%, 18%) selbst aus alter (22.09.2021) vs. neuer (18.12.2024) Satzung nachrechnen, oder (b) den ganzen Absatz auf eine vorsichtigere Formulierung herunterstufen („Im NRW-Vergleich gehören die Gebühren Oberhausens zu den moderaten Werten, siehe BdSt NRW 2025"). Die alte Satzung 22.09.2021 ist in der neuen explizit als ersetzt referenziert — ein eigener Vergleich ist also methodisch möglich, muss aber ehrlich als „eigene Berechnung Redaktion" gekennzeichnet werden.

Wichtige Mängel (sollten gefixt werden)
W1 — Volksbund-Zahlendiskrepanz nicht erklärt

Chat A nennt 2.218 Kriegsopfer. Die Volksbund-Seite nennt im Header 2.192 als „Gesamtbelegung", im Fließtext 2.218 als „Kriegsopfer auf den Ehrenfeldern". Das ist verteidigbar (Chat A folgt dem Fließtext), aber ein vorsichtiger Reader würde stolpern. Empfehlung: Formulierung schärfen, z.B. „Laut Volksbund Deutsche Kriegsgräberfürsorge ruhen auf den Ehrenfeldern des Westfriedhofs 2.218 Kriegsopfer". Den Aspekt „Volksbund nennt zudem 2.192 als aktuelle Belegung" kann man weglassen — wichtig ist die Zuordnung „Ehrenfelder".

W2 — Ostfriedhof Hidden Gem zu spekulativ

Der <!-- UNSURE: -->-Kommentar in Chat A's Quelltext ist intellektuell ehrlich, aber das verbleibende Hidden-Gem bleibt vage („Schmiedeisengitter, dessen Ornamentik aus der Gründungszeit stammt"). Ohne Beleg zur Gründungszeit ist die Aussage hohl. Fix: Entweder konkretere Recherche (Stadtarchiv Oberhausen, „Eduard Michalides" + Ostfriedhof) oder das Hidden Gem auf den belegten Kern reduzieren („Michalides war Stadtbaumeister Osterfelds Anfang 20. Jh.") und den Gitter-Teil streichen.

W3 — Landwehrfriedhof Adress-Tipp „Landwehr 328"

Der „Hidden Gem" mit dem Tipp, „Landwehr 328 statt 318" zu navigieren, ist eine sehr konkrete Behauptung. Wenn das nicht aus einer dokumentierten Quelle (Forum, lokaler Bestatter-Hinweis, SBO-FAQ) stammt, sondern erfunden ist — streichen. Sonst Quelle nennen oder als „lokaler Erfahrungswert" deutlich relativieren.

W4 — § 13 Abs. 3 BestG NRW Wortlaut-Treue

Chat A schreibt: „Die Einäscherung ist ebenfalls binnen zehn Tagen nach dem Todeseintritt vorgesehen, und die Totenasche muss spätestens sechs Wochen nach der Einäscherung beigesetzt werden (§ 13 Abs. 3 BestG NRW)."

Korrekt nach Gesetzestext: „Erdbestattungen oder Einäscherungen müssen innerhalb von zehn Tagen durchgeführt werden. Die Totenasche ist innerhalb von sechs Wochen beizusetzen." Die 6 Wochen beziehen sich nicht explizit auf den Zeitpunkt nach Einäscherung — das Gesetz lässt das offen, aber die übliche Interpretation (auch nach § 15 Abs. 5: „innerhalb von sechs Wochen nach Aushändigung") stützt Chat A's Formulierung. Empfehlung: Eher mit § 15 Abs. 5 statt § 13 Abs. 3 zitieren, da die 6-Wochen-Frist dort konkreter ist.

W5 — „Bestatter-Meister seit 2003"

Chat A: „geregelter Ausbildungs- und Meisterberuf seit 2003". Tatsächlich: Bestatter ist Ausbildungsberuf seit 2003, geprüfter Bestatter (Fortbildung) gibt es seit längerem, Meister im Bestatterhandwerk wurde erst 2007 eingeführt. Fix: „Ausbildungsberuf seit 2003, Meisterprüfung seit 2007". Quelle: BIBB/Handwerksordnung.

W6 — Ruhezeit-FAQ zu vage

„Üblich sind in Nordrhein-Westfalen 20 bis 30 Jahre für Sargbestattungen und 20 Jahre für Urnenbeisetzungen." — Das ist generisch. Die konkreten Oberhausener Ruhezeiten stehen in der Friedhofssatzung (auch verlinkt in Quelle 3). Chat A hätte die Satzung lesen und konkret zitieren sollen. Fix: Friedhofssatzung § X (Ruhefristen) öffnen und konkrete Werte für Oberhausen einsetzen, oder ehrlich sagen „Konkrete Werte siehe Friedhofssatzung § X, Stadt Oberhausen".

Kleinere Punkte (Nice-to-fix)
K1: Sourcename „Aeternitas" ist Sekundärquelle und für eine NRW-Seite weniger maßgeblich als recht.nrw.de — könnte entfallen oder als „Hintergrund-Übersicht" gekennzeichnet werden.
K2: Die <meta description> listet alle 5 Friedhöfe — das ist 175 Zeichen und damit über dem optimalen 155-Zeichen-Limit für SERPs. Kürzen.
K3: Schema.org Article hat keinen datePublished und dateModified — wichtig für Frische-Signal bei Google.
K4: Im Hero steht „BestG NRW" mit Fassungsdatum 2024; nach Fix B1 dort konsistent halten.
K5: Westfriedhof-Karten-Tipp „Parkplatz an Hamborner Allee" — gut, aber ohne Verifikation aus Primärquelle. Wenn nicht aus eigener Anschauung, dann generischer formulieren.
K6: „Friedhofsverwaltung Sterkrade/Nord" — in Quellen wird die Verwaltungsstruktur SBO nicht so klar in „Nord" und „Süd" geteilt. Bitte gegen SBO-Quelle 4 prüfen.
Was gut ist (zur Bewahrung)

✔ Saubere §-Citations für § 4a (Grabsteine), § 9 (Leichenschau), § 13 (Fristen) — alle korrekt belegt. ✔ Friedhofs-Geschichten (Westfriedhof/GHH, Osterfeld/Bergbau, Styrum/Landwehr) sind inhaltlich stark und ortsspezifisch — kein Template-Schema. ✔ Klare Abgrenzung städtische vs. konfessionelle Friedhöfe. ✔ Ehrliche <!-- UNSURE -->-Kommentare im Quelltext zeigen redaktionelle Selbstkontrolle. ✔ JSON-LD-Schema (WebPage + Article + BreadcrumbList + City + 5× Place + FAQPage) ist sauber strukturiert. ✔ FAQ adressiert echte User-Fragen, kein Filler. ✔ Quellen sind echte Primärquellen (Satzung-PDF, recht.nrw.de, Volksbund, BdSt).

Fix-Liste (priorisiert für Chat A)
B1 (Blocker): BestG-Datum überall auf „Fassung vom 19.02.2022" korrigieren — Hero-Lead, Keyfacts-DD, §-Recht-Absatz, Quelle #1.
B2 (Blocker): Gebührentabelle um Zeilen 1.14, 1.15, 1.16, 1.17, 1.18 ergänzen. Stelenkammer (1.658 €) im Fließtext „Bestattungsangebot" mindestens auf einem Friedhof erwähnen, falls vorhanden.
B3 (Blocker): BdSt-2022-Behauptung und 21%/18%-Prozentsätze entweder belegen ODER zu vorsichtiger Formulierung umbauen.
W1: Volksbund-Formulierung präzisieren (2.218 auf Ehrenfeldern).
W2: Ostfriedhof Hidden Gem entweder belegen oder Gitter-Teil streichen.
W3: Landwehrfriedhof Adress-Tipp belegen oder relativieren.
W4: § 15 Abs. 5 statt nur § 13 Abs. 3 für 6-Wochen-Frist zitieren.
W5: Bestatter-Meister 2007 statt 2003.
W6: Konkrete Oberhausener Ruhezeiten aus Friedhofssatzung nachtragen.
K1–K6: Quick-Wins für nächste Iteration.

Empfehlung an Chat A: Nach Fix von B1–B3 sollte SCORE ≥85 erreichbar sein. Empfohlene Reihenfolge: B1 (5-Minuten-Fix) → B2 (10-Minuten-Fix, Tabelle erweitern) → B3 (15-Minuten-Fix, Formulierung), dann W1–W6 für Politur.

Bereit für v2.

Dein Nutzungsguthaben ist aufgebraucht. Kaufe mehr, um jetzt weiterzumachen, oder warte bis Donnerstag um 14:00, wenn sich deine Plan-Nutzung zurücksetzt.
Mehr kaufen




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen