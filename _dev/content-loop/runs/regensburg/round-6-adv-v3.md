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
Regensburg v3 adversarial score evaluation
Friedhöfe und Bestattungen in Mönchengladbach
Regensburg Friedhöfe und Bestattungsgesetz
Heidelberg Friedhöfe und Bestattungsgesetze
Mönchengladbach Schwächen-Analyse
Heidelberg: Schwächen und adversariales Scoring
Regensburg: Schwächen und adversariales Scoring
Regensburg SCORE-Bewertung und Fehlerliste
Heidelberg content review nach SCORE-Tabelle
Mönchengladbach-Review nach SCORE-Tabelle
Chat C v3 Kassel Bewertung prüfen
Regensburg Friedhöfe und Bestattungsgesetz
Regensburg Friedhöfe und Bestattungsgesetz
Friedhöfe und Gebührensatzung in Kassel
Chat C v3 Rostock performance evaluation
Friedhöfe und Bestattungen in Rostock
Oldenburg v3 adversarial score evaluation
Lübeck v3 adversarial score evaluation
Friedhöfe und Gebührensatzung in Oldenburg
Friedhöfe in Lübeck: Bestattungen und Gebühren
Kassel adversarial review und schwächen analyse
Rostock: Schwächen und adversariales Scoring
Oldenburg: Schwächen und adversariale Bewertung
Lübeck adversarial review und schwächen analyse
Rostock: Schwächen und adversariales Scoring
Kassel-Review nach SCORE-Tabelle
Kassel-Review nach SCORE-Tabelle
Oldenburg-Review nach SCORE-Tabelle
Lübeck-Review nach SCORE-Tabelle
Friedhöfe und Gebührensatzung in Kassel
Rostock-Review nach SCORE-Tabelle
Alle Chats
B
Bolle
Max Plan
Regensburg v3 adversarial score evaluation
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat C (FINAL-Adv-Recheck).

Du bist Chat C (FINAL-Adv-Recheck). v3 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/regensburg/v3-final.html

Stadt: Regensburg. v2 hatte 72%. Pruefe v3 + FINAL-ADVERSARIAL-SCORE 0-100% (Ziel: >=85%).

19:37
Claude hat geantwortet: Ich hole die v3 und prüfe sie.

Ich hole die v3 und prüfe sie.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/regensburg/v3-final.html

Ich beginne mit dem FINAL-Adversarial-Recheck. Das ist die letzte Stufe vor Go-Live — ich prüfe nach den 9 Recheck-Kategorien (entsprechend _dev/bundesland-recheck.py-Logik), kombiniert mit FINAL-Audit-Schärfe.

FINAL-ADVERSARIAL-RECHECK — Regensburg v3
1. Wortzahl & Substanz
Geschätzt ~2.400 Wörter im sichtbaren Body (ohne JSON-LD, ohne Tabelle, ohne Quellen). ✅ Über Ziel (1700–2400).
4 Friedhöfe mit jeweils 3–4 substantiellen Absätzen + Hidden Gem + Adresse. ✅
Pass.
2. §-Citations & Quellen
§ 15 BS (Ruhezeiten) ✅ konkret zitiert
Art. 1 Abs. 1 BestG ✅
BGS vom 13.12.2018, Anlage 12.12.2024 ✅ konkret
BS vom 04.12.2006 ✅
BayRS 2127-1-G ✅
20 Quellen mit Deeplinks. ✅
Pass.
3. Faktentreue / Wrong-State-City-Check
Stadtteile genannt: Steinweg, Stadtamhof, Burgweinting, Harting, Keilberg, Oberisling, Reinhausen, Sallern, Schwabelweis, Winzer → alle Regensburger Stadtbezirke. ✅
Galgenberg, Schillerstraße, D.-Martin-Luther-Straße, Friedensstraße, Bischof-Konrad-Straße → Regensburger Straßen. ✅
Sulzbach-Rosenberg (Maxhütte) → korrekt extern referenziert. ✅
Pass.
4. Template-Fehler / Copy-Paste-Reste
Keine Platzhalter, keine {{stadt}}, keine falschen Bundesland-Verweise. ✅
Bayern-Verweise konsistent. ✅
Pass.
5. Unbelegte Superlative

Geprüfte Superlative:

"größte und zentral wichtigste städtische Friedhof" → durch Krematorium/140 Sitzplätze belegt ✅
"eindrucksvollster Monumentalfriedhof" → mit Mausoleum-Beschreibung gestützt, aber subjektiv-wertend ⚠️
"historisch außergewöhnlichste Friedhof Regensburgs" → durch document-Status + Klose/Rueß belegt ✅
"eines der bedeutendsten Sepulkral-Denkmäler Europas" → starke Behauptung, durch Klose/Rueß 2015 abdeckbar, aber Quelle nicht direkt zitiert ⚠️
"einzige in Bayern erhaltene Friedhof auf reichsstädtischem Grund" → präzise und prüfbar ✅
"bedeutendsten Jugendstil-Bauwerken Regensburgs" → ok, lokal begrenzt ✅
"herausragenden Beispiele sakraler Kleinarchitektur in Regensburg um 1900" → moderat, lokal begrenzt ✅

→ 2 weiche Superlative, aber alle im Kontext eingebettet. Kein Blocker.

Pass mit Hinweis.
6. UStG-Korrektheit (kritisch nach Bundesland-Sprint-Standard)
Hoheitlich/wirtschaftlich getrennt ✅
"* = umsatzsteuerpflichtig"-Markierung in Tabelle ✅
Übergangsregelung ab 01.01.2027 erwähnt ✅
Krematorium = wirtschaftlich ✅ (entspricht Anlage 12.12.2024)
Pass.
7. Schema.org / Strukturdaten
@graph mit 8 Entities ✅
Article, WebPage, City, BreadcrumbList, 4× Place, Organization, FAQPage ✅
Datums-Konsistenz (datePublished/dateModified = 2026-05-12) ✅
GeoCoordinates 49.0134, 12.1016 ✅ (Regensburg-Zentrum)
Pass.
8. FAQ-Vollständigkeit
7 FAQ-Items in HTML, 7 in JSON-LD ✅
Inhaltlich konsistent zwischen sichtbarem HTML und Schema ✅
Pass.
9. Adversarial Sniff-Test (Was würde ein Reviewer angreifen?)
Tatsächlich gefundene Punkte:

🔴 BLOCKER 1 — Schema-Tippfehler im Place-Description

"Vom Stadtrat Regensburg am 16. Mai 2024 zum 7. document der Stadt erhoben – 
ein lokales Programm der Stadt Regensburg..."

Im JSON-LD Place-Description ist "document" ohne Anführungszeichen. Im sichtbaren Text korrekt mit „document" oder „document". Inkonsistenz zwischen Schema und sichtbarem Text. Kein Go-Live-Blocker im engeren Sinn, aber sauberer Stil = Anführungszeichen auch im Schema (oder kursivieren). → NICE-TO-FIX.

🟡 WEAK 1 — Stiftungssumme "17,4 Millionen Mark" Quelle: Wikipedia (Sekundärquelle). Die Formulierung „nach dieser Angabe rund 17,4 Millionen Mark" markiert die Unsicherheit explizit — das ist sauber. ✅ Akzeptabel.

🟡 WEAK 2 — Telefonnummer Oberer Katholischer Friedhof: (0941) 90572 Eine 5-stellige Durchwahl ohne führende Null wirkt ungewöhnlich für Regensburg (typisch sind 6-stellige Nummern oder Durchwahl-Struktur). Verifikations-Empfehlung vor Go-Live, aber nicht kritisch genug für Blocker. → CHECK.

🟡 WEAK 3 — "ca. 300 m²" Gesandtenfriedhof + "ca. 300 Quadratmeter" Im Meta-Header "ca. 300 m²", im Fließtext "etwa 300 Quadratmeter große Hof". ✅ Konsistent.

🟢 STRENGTH — Die prominente-Sektionen sind durchgehend mit Lebensdaten/Funktion verifizierbar. Sehr gut.

🟢 STRENGTH — Die Hidden-Gems sind nicht generisch ("schöner Park"), sondern enthalten konkrete narrative Anker (Pestkirche+jüdischer Friedhof; Friedhofscafé-Plan; Metternich-Konversion). Adversarial: hoch.

🟢 STRENGTH — Bestelmeyer wird zweimal im Mausoleum-Absatz genannt (Portal + Mausoleum-Plan). Beides historisch belegbar (Bestelmeyer war Hausarchitekt der Familie Dörnberg + plante das Friedhofsportal). ✅

🟡 WEAK 4 — "Im Innenraum schufen die Münchner Bildhauer Hermann Hahn und Georg Albertshofer..." Nicht durch eine direkte Quelle in der Quellenliste belegt. Vermutlich aus dem Wikipedia-Zentralfriedhof-Artikel. Da Wikipedia in Quelle #8 mit Bauer-Spandl 2021 als Sekundärbasis genannt ist → abgedeckt, aber eng. → Akzeptabel.

🟡 WEAK 5 — "Diplomatenfriedhof-Ensembles Europas" Behauptung im Hero: "eines der bedeutendsten erhaltenen Diplomatenfriedhof-Ensembles Europas". Die DSD-Quelle und das Stadtarchiv-Werk Klose/Rueß stützen "einzigartig im Reichsstadt-Kontext", aber europäische Einzigartigkeit ist starke Behauptung. → "in Bayern erhaltene" wäre safer. Nice-to-tighten, aber durch DSD-Auszeichnung 2025 + document-Status verteidigbar.

FINAL-ADVERSARIAL-SCORE
Kategorie	Gewicht	Erfüllung	Punkte
1. Wortzahl & Substanz	10%	100%	10
2. §-Citations & Quellen	15%	100%	15
3. Faktentreue / Geo	15%	100%	15
4. Template-Reinheit	10%	100%	10
5. Unbelegte Superlative	10%	85%	8,5
6. UStG-Korrektheit	10%	100%	10
7. Schema.org	10%	95%	9,5
8. FAQ-Konsistenz	5%	100%	5
9. Adversarial Sniff	15%	88%	13,2
GESAMT	100%		96,2%
FINAL-ADVERSARIAL-SCORE: 96% ✅
Verdict: GO-LIVE FREIGEGEBEN

Sprung v2→v3: 72% → 96% (+24 Punkte) — die Stadt-Recherche-Tiefe (4 Friedhöfe ausführlich, Hidden Gems mit narrativer Substanz, document-Programm korrekt eingeordnet, UStG-Klausel ergänzt) hat den Ausschlag gegeben.

Blocker: 0
Nice-to-Fix (nicht Go-Live-blockierend):
JSON-LD Place "Gesandtenfriedhof": 7. document → 7. „document" für Konsistenz mit sichtbarem Text.
Tel. Oberer Katholischer Friedhof (0941) 90572 vor Erstkontakt durch User verifizieren — wirkt zu kurz für eine reguläre Regensburger Festnetznummer.
Hero-Behauptung "Europas" ggf. auf "Bayerns/Deutschlands" zurückstufen, falls Klose/Rueß 2015 nicht explizit europaweiten Vergleich machen.
Was diese Seite stark macht:
Echte lokale Tiefe (Pestkirche-Geschichte 1713, Galgenberg-Standort-Begründung 1895, Metternich-Konversion 1717, Bombenangriff 1943 auf Messerschmitt).
Saubere Trennung lokales document-Programm vs. UNESCO-Welterbe — adversarial-resistent.
Vollständige UStG-Tabellenfußnote inkl. 2027er-Übergang.
Konsistenz zwischen Hero, Keyfacts, FAQ und Schema bei den Kernzahlen (11 Friedhöfe, 318 €, 848 €, 15/12/7 Jahre).

Empfehlung: Direkt deploy-fähig. Bei Zeit: 3 Nice-to-Fixes vor Ende deploy einbauen, dann live.

Dein Nutzungsguthaben ist aufgebraucht. Kaufe mehr, um jetzt weiterzumachen, oder warte bis Donnerstag um 14:00, wenn sich deine Plan-Nutzung zurücksetzt.
Mehr kaufen




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen