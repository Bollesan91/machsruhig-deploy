Ich lese die zwei Hannover-Dateien.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/hannover/v4-final.html
Web durchsucht

BRIEFING_OK.

v3-MUST-FIX-Status (drei harte Faktenfehler aus v3-Adv):

FIX 1 — Engesohde 30 → 22 ha: v4 schreibt jetzt „rund 22 Hektar (Stadt Hannover; Wikipedia nennt 21,7 ha)" sowohl in der Sektion als auch in den Keyfacts und in der FAQ. Doppelquellen-Konvention sauber. ✓ Behoben.

FIX 2 — Lahe + Hierarchie auf Seelhorst: v4 Keyfacts „Größter (Fläche): Stadtfriedhof Seelhorst (rund 68 ha)" ✓. Lahe-Sektion: „1968 eröffnet und umfasst rund 37 Hektar" ✓. Seelhorst-H3: „flächenmäßig größter Friedhof Hannovers" mit „ab 1919 geplant und 1924 eröffnet, rund 68 Hektar (Denkmalatlas Niedersachsen)" ✓. FAQ: „Flächenmäßig ist der Stadtfriedhof Seelhorst im Süden mit rund 68 Hektar der größte" — Lahe explizit als 37 ha, Engesohde als 22 ha gegenübergestellt ✓. Hierarchie-Korrektur sauber durchgezogen über Keyfacts + Schema.org + Sektion + FAQ. ✓ Behoben.

FIX 3 — Eingangsbau vs. Kapelle Engesohde: v4 trennt jetzt explizit: „Der Eingangsbau im Rundbogenstil stammt aus dem Jahr 1873 und ebenfalls von Ludwig Droste; die heutige Kapelle dagegen wurde erst 1912 von Oskar Barnstorf errichtet — die beiden Bauten trennen rund vier Jahrzehnte." ✓ Behoben mit korrekter Architekten-Zuordnung und expliziter Datenspanne.

Schwitters + Yvonne Georgi (v3-Sekundärbefund): Beide ergänzt, mit Lebensdaten (1887–1948 bzw. 1903–1975) und Werk-Kontext, in Body + FAQ + Schema.org-FAQPage konsistent. ✓ Erledigt.

Alle drei harten v3-MUST-FIX und der zentrale Sekundärbefund sind sauber adressiert. v4 ist über die ganze Page faktentechnisch deutlich präziser. Schema.org-Place-Beschreibungen ziehen die korrigierten Werte mit (Engesohde 22 ha, Seelhorst 68 ha, Lahe 37 ha 1968). Trotzdem finde ich drei substantielle neue Schwächen.

SCORE: 81/100

FUNDE:

SCHWÄCHE 1 (Halluzinations-Verdacht + Quellen-Lücke, Seelhorst-Sektion „Hermann Kube als Stadtgartendirektor"): Der Text schreibt: „Die Anlage geht auf den Stadtgartendirektor Hermann Kube (1874–1953) zurück." Die Lebensdaten 1874–1953 sind sehr konkret und stehen ohne Inline-Anker. Der v3-Adv hatte „Hermann Kube plante ab 1919" als belegt markiert (Denkmalatlas Niedersachsen) — aber die Lebensdaten und die Funktionsbezeichnung „Stadtgartendirektor" sind in v3-Adv nicht verifiziert worden. Recherche-Risiko: Es gab in Hannover mehrere Stadt-Gärtnerei-Funktionen mit ähnlichen Bezeichnungen (Stadtgartendirektor, Gartendirektor, Stadtgärtner). Wenn Hermann Kube tatsächlich „Gartendirektor" oder „Garteninspektor" hieß und nicht „Stadtgartendirektor", ist die Funktionsbezeichnung minimal falsch — ein Konkurrent in 5 Minuten Google-Recherche kann das. Die Lebensdaten 1874–1953 sind plausibel, aber unbelegt. Die Sektion baut auf dieser Person die ganze Genese der Anlage auf — eine Halluzination an dieser Stelle wäre ein YMYL-Glaubwürdigkeits-Treffer.

Zusätzlich: v4 spricht für Engesohde von „Stadtgärtner Ludwig Droste". Für Seelhorst von „Stadtgartendirektor Hermann Kube". Das ist eine Funktionsbezeichnungs-Inkonsistenz innerhalb derselben Page für vergleichbare Rollen — wenn Droste „Stadtgärtner" war und Kube „Stadtgartendirektor", ist das richtig (verschiedene Ära, andere Verwaltungsstruktur), aber dann muss es belegt sein. Stehen beide Bezeichnungen ohne Inline-Anker, ist das Mehrfach-Halluzinations-Verdacht.

Verbesserung: Inline-Anker auf Denkmalatlas Niedersachsen (Seelhorst-Eintrag) oder hannover.de setzen, der Kubes Funktion und Lebensdaten belegt. Falls Lebensdaten nicht belegbar → „Stadtgartendirektor Hermann Kube" ohne Lebensdaten lassen, das reicht für die Aussage. Bei Droste analog prüfen — der ist in v4 auch nur als „Stadtgärtner Ludwig Droste" eingeführt ohne Lebensdaten und ohne Inline-Anker.

SCHWÄCHE 2 (Veraltete Daten + Quellen-Lücke, Bestattungskosten-Sektion): Der Text zitiert „Stiftung Warentest (Finanztest 11/2023): rund 7.000 bis 8.000 Euro" und tut dies an drei Stellen identisch (Body, Schema.org-FAQ, FAQ-Antwort). Mehrere Probleme:

(a) Datenstand 11/2023 — das ist im Mai 2026 fast 2,5 Jahre alt. Stiftung Warentest hat seitdem aktualisierte Erhebungen veröffentlicht (typischerweise im Jahresrhythmus). Wenn eine neuere Finanztest-Ausgabe zu Bestattungskosten existiert, ist 11/2023 nicht mehr der aktuelle Stand und ein Bestatter-Anwalt würde das in 30 Sekunden gegenrecherchieren. Kategorie 3 (Veraltete Daten).

(b) Kein Deep-Link auf den Stiftung-Warentest-Artikel — in der Quellenliste steht nur „Stiftung Warentest — Finanztest 11/2023, ‚Bestattungen: Was sie kosten und wie sich sparen lässt'" ohne URL. Ein Reviewer kann die Quelle nicht prüfen, ohne selbst test.de zu durchsuchen.

(c) Dreifache identische Wiederholung der 7.000–8.000-Euro-Zahl (Body + Schema-FAQ + UI-FAQ) ohne Variation. Wenn die Zahl falsch oder veraltet ist, ist sie dreifach falsch — Google's FAQ-Rich-Snippet würde die veraltete Zahl prominent rendern.

Verbesserung: Prüfen, ob es eine aktuellere Stiftung-Warentest-Erhebung (2024 oder 2025) gibt; falls ja, Datenstand updaten und Deep-Link einfügen. Falls 11/2023 wirklich die aktuellste Erhebung ist, das im Text explizit so deklarieren („nach der zuletzt 2023 veröffentlichten Stiftung-Warentest-Erhebung, neuere Daten liegen redaktionell nicht vor"). Alternativ Aeternitas-Erhebung (typischerweise jährlich aktualisiert) parallel zitieren, das nimmt der Einzelzahl die Solitär-Gewichtung. Quellenliste: Deep-Link auf den test.de-Artikel mit Datum.

SCHWÄCHE 3 (Generischer Satz + Quellen-Lücke + UNSURE-Pipeline-Leakage, BestG-Friedhofszwang-Sektion): Drei Probleme an einer Stelle:

(a) Der Text sagt „Nach dem BestattG Niedersachsen dürfen Verstorbene grundsätzlich nur auf einem öffentlichen Friedhof oder einem genehmigten kirchlichen Friedhof bestattet werden" — ohne konkreten §-Verweis. Im selben Absatz steht ein UNSURE-Kommentar im HTML-Source: <!-- UNSURE: Konkrete §-Zuordnung des Friedhofszwangs im aktuellen BestattG Niedersachsen redaktionell nicht abschließend verifiziert; Verweis auf BL-Page für die vollständige §-Aufstellung. -->. Das ist Pipeline-Leakage — interner Recherchekommentar im ausgelieferten HTML. Für Google nicht sichtbar (Kommentar), aber für jeden Reviewer, der View-Source macht, sofort sichtbar. Bei einer YMYL-Stadtseite mit „alle Inhalte redaktionell geprüft"-Footer ist das ein Credibility-Sweep-Risiko. Außerdem in der Bestattungsrecht-Sektion ein zweiter UNSURE-Kommentar: <!-- UNSURE: Exakte Ruhezeit-Werte je Stadtfriedhof variieren nach Bodengutachten; verbindlich ist die jeweils aktuelle Satzung. --> — gleicher Mechanismus.

(b) Im OG-Image-Bereich ein dritter UNSURE-Kommentar: <!-- UNSURE: Generisches OG-Image; Hannover-spezifisches Motiv folgt sobald Asset-Pipeline verfügbar. -->. Drei UNSURE-Kommentare im finalen HTML.

(c) Der Friedhofszwang ohne §-Verweis ist gleichzeitig eine reale juristische Aussage, die für YMYL belegbar sein muss. v3-Adv hatte das § 12 explizit als Halluzinations-Risiko markiert (deshalb wurde es entfernt) — v4 hat den §-Verweis entfernt, aber keinen verifizierten Ersatz-§ ergänzt. Die NRW-Praxis (BestattG Nds § 8 für Friedhofszwang, § 10 für anonyme/halbanonyme Beisetzungen) wäre nachzuprüfen und entweder mit korrektem § zu zitieren oder generisch ohne § zu belassen — aktueller Stand ist „generisch ohne §, aber mit Pipeline-Kommentar als Selbstanklage".

Verbesserung: Erstens: Alle drei UNSURE-Kommentare aus dem ausgelieferten HTML entfernen — die gehören in das interne BACKLOG / Editor-Kommentare, nicht ins Live-Artefakt. Zweitens: Friedhofszwang-§ entweder gegen voris.niedersachsen.de verifizieren und einsetzen, oder die Aussage auf „nach niedersächsischem Landesrecht" (ohne § generisch) reduzieren — aber ohne Selbstanklage-Kommentar. Drittens: Ruhezeit-Aussage analog: entweder konkrete Werte aus der aktuellen Stadt-Satzung verifizieren oder generisch lassen, ohne Pipeline-Kommentar.

Zusatzbeobachtungen (nicht in den 3er-Quote):

Drei UNSURE-Kommentare als Pipeline-Leakage — wenn das ein wiederkehrendes Pattern in deinen v4-Outputs ist, lohnt ein Pre-Deploy-grep <!-- UNSURE als Hard-Block-Check im bundesland-recheck.py. Krefeld v4 hatte das nicht, Bonn v4 hatte das nicht, Hannover v4 hat es dreifach. Sample size 3 ist klein, aber wenn das nochmal in Halle, Chemnitz, Heidelberg auftaucht, ist es ein systemisches Pipeline-Problem, kein Einzelfall.
Schema.org Article hat „author":{"@type":"Organization","name":"machsruhig.de"} — das weicht von der gespeicherten Locked-Decision ab („Autorenmodell = machsruhig Redaktion"). Bonn v4 und Krefeld v4 schreiben „machsruhig Redaktion" als author.name. Hannover v4 schreibt „machsruhig.de" als author.name UND publisher.name — beide identisch. Das ist Schema-Schwäche: Article.author und Article.publisher sollten nicht identisch sein, Google's structured-data-test wird das toleant durchwinken aber nicht goutieren. Auch der Visible-Text-Author im Body („Redaktion machsruhig.de") weicht von der Bonn/Krefeld-Konvention („machsruhig Redaktion") ab. Kategorie 10 (Schema-Inkonsistenz mit Locked-Decision), nicht show-stoppend, aber Markenpräsenz-Drift.
Cross-Links zu Braunschweig + Hildesheim vorhanden in Quellenliste — Kategorie 9 erfüllt. Gut.
Wortzahl ca. 2.350 — solide, über der Untergrenze.
Floskel-Kontrolle clean — keine „letzte Ruhe", „in dieser schweren Zeit". Kategorie 11 erfüllt.
„Theodor Lessing (1872–1933), Philosoph mit Hannover-Bezug" — der Beisatz „mit Hannover-Bezug" ist sehr vage. Lessing war Hannoveraner Honorarprofessor (Technische Hochschule), 1933 in Marienbad ermordet, dort beerdigt — also formal nicht auf Engesohde, sondern in Marienbad bestattet. Wenn er auf der Liste „Auf Engesohde bestattet" steht, ist das faktisch falsch oder benötigt eine Klarstellung (z.B. „Ehrengrab" / „Gedenkstein"). v3-Adv hat „Umbettung Marienbad → Engesohde" als Halluzination markiert und entfernen lassen — aber Lessing ist in v4 weiter als bestattet-auf-Engesohde-Person gelistet. Potenzielles Halluzinations-Reentry. Falls Engesohde nur einen Gedenkstein/Ehrengrab für Lessing hat, muss das so dastehen. Dies hätte ich beinahe in die 3er-Quote genommen — Tiefe der Verifikation hängt davon ab, ob die Stadt-Hannover-Ehrengrabliste Lessing als „bestattet" oder „Ehrengrab/Gedenkstein" führt. Pre-Deploy-Check empfohlen.
Engesohde 21,7 vs 22 ha Doppelquellen-Lösung ist methodisch elegant — sauberes Pattern für künftige Pages.
Kein direkter Nachbarstadt-Cross-Link im Body — Braunschweig/Hildesheim nur in der Quellenliste. Bonn v4 und Krefeld v4 haben das im Body. Konsistenz-Drift.

MUST-FIX vor Deploy: JA.

Begründung: Schwäche 3 ist ein echtes Hygiene-Versagen — drei Pipeline-Kommentare im ausgelieferten HTML, davon einer („Friedhofszwang § nicht abschließend verifiziert") an einer juristischen YMYL-Stelle. Das ist nicht „könnte besser sein", das ist „darf so nicht live gehen". Selbstanklage-Kommentare im Live-HTML sind das exakte Gegenteil dessen, was der <div class="mr-trust">-Footer verspricht („nach bestem Wissen und auf Basis der zitierten Primärquellen zusammengestellt"). Ein Bestatter-Anwalt oder Konkurrent, der View-Source macht, hat einen Schmiss-Anker.

Schwäche 1 (Kube-Lebensdaten + Funktionsbezeichnung) ist ein 5-Minuten-Verifikations-Fix oder eine 10-Sekunden-Streichung (Lebensdaten raus, „Stadtgartendirektor Hermann Kube" ohne Daten stehen lassen).

Schwäche 2 (Stiftung-Warentest 11/2023) ist ein 10-Minuten-Fix (Recherche aktuellere Quelle ODER explizit als „letzter verfügbarer Stand" deklarieren ODER Aeternitas parallel zitieren) plus Deep-Link in Quellenliste.

Plus der Lessing-Pre-Deploy-Check (Engesohde wirklich bestattet oder nur Ehrengrab/Gedenkstein) — 5 Minuten gegen die Stadt-Hannover-Ehrengrabliste.

Gesamt-Fixzeit für alle drei Schwächen plus Lessing-Check: 30–45 Minuten. Score 81/100 reflektiert: substantieller Fortschritt v3→v4 (drei harte Faktenfehler behoben, Schwitters + Yvonne Georgi ergänzt, Schema.org konsistent gezogen, Doppelquellen-Pattern eingeführt), aber drei substantielle neue Schwächen, davon eine mit Pipeline-Hygiene-Charakter, die deploy-blockiert.