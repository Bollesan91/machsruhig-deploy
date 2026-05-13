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
Freiburg Schwächen und adversariales Scoring
v4 HTML-Version mit Adversarial-Fixes
HTML-Version v4 mit Adversarial-Fixes
Chat C final adversarial recheck for Halle
Erfurt v4 adversarial score evaluation
Saarbrücken FINAL-Adv-Recheck v6 Bewertung
HTML-Version mit Review-Fixes liefern
Friedhöfe und Bestattungen in Hagen
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
Chemnitz Schwächen und Adversarial-Bewertung
Heidelberg v4 adversarial score evaluation
Heidelberg v4 adversarial score evaluation
Mönchengladbach Schwächen-Analyse
Heidelberg: Schwächen und adversariales Scoring
Regensburg: Schwächen und adversariales Scoring
Regensburg SCORE-Bewertung und Fehlerliste
Heidelberg content review nach SCORE-Tabelle
Mönchengladbach-Review nach SCORE-Tabelle
Chat C v3 Kassel Bewertung prüfen
Regensburg Friedhöfe und Bestattungsgesetz
Halle review und bewertung
Krefeld review score und fix-liste
Chemnitz review und bewertung
Heidelberg Friedhöfe und Bestattungsgesetze
Heidelberg v3 adversarial score evaluation
Mönchengladbach v3 adversarial score evaluation
Regensburg v3 adversarial score evaluation
Regensburg Friedhöfe und Bestattungsgesetz
Friedhöfe und Bestattungen in Mönchengladbach
Alle Chats
B
Bolle
Max Plan
Freiburg Schwächen und adversariales Scoring
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat C (Adversarial).

Du bist Chat C (Adversarial). v2 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/freiburg/v2-from-chat-A.html

Stadt: Freiburg (BW). 3 Schwaechen + ADVERSARIAL-SCORE.

11:05
Claude hat geantwortet: Ich lade v2 und prüfe adversarial.

Ich lade v2 und prüfe adversarial.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/freiburg/v2-from-chat-A.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/freiburg/v2-from-chat-A.html

Adversarial-Modus. Ich greife v2 hart an — nicht "ist nett". Drei echte Schwächen, die ein kritischer Leser/SEO-Konkurrent/Faktenchecker findet.

Schwäche 1: NICHT-VERIFIZIERTE Gebühren — Glaubwürdigkeits-Risiko

Befund: Die komplette Gebührentabelle (1.795 €, 453 €, 346 €, 568 €, 614 €, 367 €, 74,40 €, 71,70 € etc.) wird mit der Autorität einer Primärquellenrecherche präsentiert ("nach Gebührenverzeichnis als Anlage zur Friedhofssatzung der Stadt Freiburg vom 19. März 2024"). Ich kann nicht prüfen, ob diese Zahlen so im verlinkten PDF stehen — und der Reviewer in Chat B kann es auch nicht. Wenn auch nur eine Zahl falsch ist, ist die gesamte Seite verbrannt: Bestatter zitieren sie, Angehörige planen damit, ein einziger Faktencheck-Treffer von Stiftung Warentest oder Badischer Zeitung erledigt das Vertrauen für die ganze Domain.

Konkrete Risikopunkte:

"Wahlgrab Erdbestattung, je Jahr und Stelle 74,40 €" und "Wahlgrab Erdbestattung Kinder 71,70 €" sowie "Urnenwahlgrab 71,70 €" — Kindergrab teurer pro Jahr als Erwachsenen-Urnenwahlgrab und Erwachsenen-Urnenwahlgrab GLEICH teuer wie Kindergrab? Riecht nach Copy-Paste-Fehler oder Halluzination. Plausibilitätstest gescheitert.
"Wandbeleuchtung Hauptfriedhof (Kerzenwand, 48 Kerzen, Trauerfeier) 109 €" — sehr spezifische Detail-Zahl, die fast nirgends in Satzungen so vorkommt. Klingt nach LLM-Erfindung mit plausiblem Beigeschmack.
"Aufbahrungsraum je angefangener Tag 44 €" — verdächtig rund.

Behebung: Chat A MUSS Gebührenverzeichnis-PDF Seite für Seite verifizieren, jede Zahl mit Satzungsparagraph/Anlagenpunkt belegen, oder Tabelle entfernen. Pseudo-Präzision ist hier gefährlicher als bewusste Abstraktion ("Die Hauptpositionen liegen in der Größenordnung von … — verbindlich die aktuelle Satzung").

Schwäche 2: LEUTWEIN-Passus ist redaktionell unsauber gebaut und SEO-toxisch

Befund: Der Absatz über Theodor Leutwein ist gut gemeint (historische Verantwortung statt unkommentierter Liste), aber handwerklich falsch positioniert und sprachlich problematisch:

Position: Er steht nach der Liste der bestatteten Persönlichkeiten — also wird Leutwein in der "Liste" nicht gelistet, sondern als Sonderfall danach behandelt. Das wirkt wie nachträgliches Reinpressen einer politisch korrekten Pflichtübung. Ein kritischer Leser fragt: Warum dann nicht auch Gallwitz (preußischer General, Heeresgruppenführer 1. WK) oder Gaede (Oberrhein-Front 1914/15) mit Einordnung? Inkonsistent.
Formulierung "einen Völkermord im Sinne der UN-Konvention, an dessen Aufarbeitung bis heute gearbeitet wird": Die deutsche Bundesregierung hat den Herero-Nama-Genozid 2021 offiziell als Völkermord anerkannt — der Halbsatz ist unnötig defensiv. Entweder klare Aussage oder weglassen. Das schwammige "wird gearbeitet" wirkt evasiv.
SEO-Risiko: "Theodor Leutwein" + "Hauptfriedhof Freiburg" + "Völkermord" auf einer Bestattungsplaner-Stadt-Page erzeugt thematische Inkohärenz für Google. Eine Stadt-Page für die Query "Bestatter Freiburg" / "Friedhof Freiburg Gebühren" sollte nicht im Kolonial­geschichts-Cluster ranken. Topical Authority wird verwässert.

Behebung: Entweder Leutwein streichen (nicht jede Person muss erwähnt werden) oder Persönlichkeitsliste komplett rausziehen und in eigene Sub-Seite /bestatter/freiburg/persoenlichkeiten/ auslagern, falls historische Tiefe gewollt ist. Auf Hauptseite gehört Trauerinfrastruktur, nicht Sepulkralhistorie. Empfehlung: Liste der bestatteten Personen radikal kürzen auf max. 3 lokal-relevante (z.B. Rolf Böhme, Gerhard Graf, Wentzinger) ohne militärische Figuren.

Schwäche 3: Unbelegte Schema.org-Property-Claims + fehlende DATUMS-Hygiene

Befund:

Schema.org "Friedhof Bergäcker" Adresse: streetAddress: "Kunzenweg" — ohne Hausnummer. Google validiert Schema.org-Adressen lose, aber LocalBusiness/Place ohne Hausnummer ist ein Quality-Signal-Verlust. Beim Hauptfriedhof steht "Friedhofstraße 8" mit Hausnummer, hier nicht. Inkonsistenz.
datePublished: "2026-05-12" / dateModified: "2026-05-13" vs. Footer "© 2024–2026" vs. "Stand: 13. Mai 2026" im Body — drei verschiedene Datumsangaben über eine Seite verteilt. Für eine "frisch publizierte" Seite plausibel, aber: Wenn die Seite morgen erneut deployt wird, wird sich nur dateModified updaten? Welcher Prozess garantiert das? Risiko: "Stand: 13. Mai 2026" wird statisch im HTML hartcodiert und veraltet ohne Auto-Update.
Unbelegte Behauptung im Fließtext, die nicht in Quellen steht: "In vielen anderen baden-württembergischen Großstädten gelten 20 Jahre" — wird zweimal behauptet (Hinweis-Box + Gebühren-Sektion), aber keine einzige Quelle für diese Vergleichsaussage. Stuttgart, Mannheim, Karlsruhe, Heidelberg haben unterschiedliche Ruhezeiten je nach Friedhof. Pauschalisierung. Faktenchecker-Risiko.
"Über 7.000 bis 8.000 Euro Stiftung Warentest": Der Link geht auf einen Stiftung-Warentest-Artikel — die genaue Zahl 7.000–8.000 € muss im laufend aktualisierten Artikel heute so stehen. Wenn der Artikel inzwischen "6.500 bis 9.000 €" oder "ab 8.500 €" sagt, ist die Behauptung falsch. Bei zweimaliger Erwähnung doppeltes Risiko.

Behebung: (a) Hausnummer Bergäcker recherchieren (Kunzenweg 11? — verifizieren) oder Adresse aus Schema rausnehmen; (b) "Stand"-Datum entweder dynamisch (Build-Hook) oder bewusst weglassen; (c) Pauschalvergleich zu "20-Jahres-Frist" entweder mit 2–3 konkreten Beispielsatzungen belegen (Stuttgart § X, Karlsruhe § Y) oder neutral umformulieren ("liegt am unteren Ende der baden-württembergischen Spanne, die je nach Gemeinde 15–25 Jahre umfasst — verbindlich ist die jeweilige Gemeindesatzung"); (d) Stiftung-Warentest-Zahl entweder live nachprüfen oder durch eine offizielle Quelle ersetzen (z.B. Verbraucherzentrale, Aeternitas-Studie mit Jahresangabe).

ADVERSARIAL-SCORE: 74 / 100

Aufschlüsselung:

Dimension	Punkte	Anmerkung
Faktentreue / Verifizierbarkeit	12 / 20	Gebührentabelle nicht stichprobenfähig prüfbar, Warentest-Zahl unbestätigt, Ruhezeiten-Vergleich pauschal
Lokale Tiefe & Differenzierung	18 / 20	Bergäcker-Details (Parkgrabfeld, Baumurnenfeld, Architekturpreis) sind echt gut
Redaktionelle Sauberkeit	14 / 20	Leutwein-Passus inkonsistent, Persönlichkeitsliste-Logik bricht
SEO / Topical Coherence	14 / 20	Kolonialgeschichts-Drift, Schema-Inkonsistenz Bergäcker, 3 Datumsangaben
Conversion / Funnel-Tauglichkeit	16 / 20	"Keine Empfehlungen"-Position klar, aber die Seite ist primär Enzyklopädie, kaum CTA-Druck zu Vorsorge-Check / Checkliste

Blocker für Go-Live (≥85):

B1: Gebührentabelle muss zeilenweise verifiziert oder entfernt werden (Plausibilitäts-Verdacht bei Wahlgräbern)
B2: Leutwein-Passus + ggf. weitere Militärfiguren entscheiden (drin mit konsistenter Einordnung, oder raus)
B3: Stiftung-Warentest-Zahl 7.000–8.000 € live prüfen oder durch belastbare Quelle ersetzen

Empfehlung an Chat A für v3: Tabelle gegen Original-PDF cross-checken (Seitenzahl im Quellenblock referenzieren), Persönlichkeitsliste auf 3 unkontroverse Namen kürzen, Ruhezeiten-Vergleich konkret machen oder neutral formulieren, Bergäcker-Hausnummer ergänzen.

Dein Nutzungsguthaben ist aufgebraucht. Kaufe mehr, um jetzt weiterzumachen, oder warte bis Donnerstag um 14:00, wenn sich deine Plan-Nutzung zurücksetzt.
Mehr kaufen




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen
Claude is active in this tab group
Open chat
Dismiss