Ich lese die drei Dateien und bewerte v4 adversarial.

Fetching site
Web durchsucht

Adversarial Review. Ich gehe die 4 MUST-FIX-Punkte aus dem 78%-Recheck durch und suche dann eigene neue Schwächen.

MUST-FIX-Check aus round-6 (78%):

Tarif-Tabelle entfernt? ✅ Ja — die ganze Tabelle ist raus, ersetzt durch Hinweiskasten + Tarifgruppen-Beschreibung + Spannen. Sauber gelöst.
Westfriedhof: "über 2.000" → 2.218 + "15 Kriegsgräberstätten"? ✅ Beides drin, beides mit Volksbund-Beleg.
PLZ-Widerspruch transparent? ✅ Fußnote [1] mit Erklärung 46145 vs. 46042, sowohl im Fließtext als auch in FAQ.
Tarifstelle 1.15 "Stelenkammer 1.658 €" verifizieren? ✅ Hinfällig durch Tabellen-Entfernung.

Alle 4 Blocker behoben. Jetzt suche ich neue Schwächen — die Page ist NICHT bei 90%, also drei substantielle Schwächen müssen drin sein.

SCORE: 87/100

FUNDE:

SCHWÄCHE 1 — Fachverband Bestattungsgewerbe NRW: nicht verifiziert, möglicherweise falscher Name (Section "Bestatter wählen", Punkt 1 der Indikatoren-Liste): v4 nennt den "Fachverband Bestattungsgewerbe NRW" als Qualitätsindikator. Der korrekte Name des NRW-Landesverbandes des BDB ist nach meiner Recherche "Bestatterverband Nordrhein-Westfalen e.V." bzw. "Landesverband NRW im Bundesverband Deutscher Bestatter". "Fachverband Bestattungsgewerbe NRW" ist als organisatorische Bezeichnung nicht primärquellenbelegt. Halluzinations-Verdacht (Kategorie 12 im Briefing). Fix: Entweder gegen Primärquelle des Landesverbands verifizieren und korrekten Namen einsetzen, oder generischer formulieren ("Mitgliedschaft im BDB-Landesverband NRW").
SCHWÄCHE 2 — FAQ "Ruhezeit": Quellen-Trick verschleiert Lücke (FAQ-details "Wie lang ist die Ruhezeit"): Die Antwort schreibt zunächst "geregelt in § 11 der Friedhofssatzung der Stadt Oberhausen (aktuelle Fassung vom 31.03.2026)" — und dann kommen konkrete Zahlen (25/30 Jahre, 15/20 Jahre, 20 Jahre Aschen) ausdrücklich aus der Vorgängerfassung 18.12.2024. Die Aussage "die Systematik ist gegenüber der Vorgängerfassung weitgehend unverändert" ist eine Vermutung, nicht belegt. Eine Bundesland-Page, die für eine konkrete Stadt veröffentlicht wird und die Ruhezeiten-Frage stellt, sollte die aktuelle Satzung gelesen haben. Im selben Atemzug zu sagen "verbindlich ist die Friedhofsverwaltung" ist eine Cop-out-Formulierung. Audit-Risiko: das Honesty-Check-Script flaggt "Zahlen aus 18.12.2024 in einer Page, die 31.03.2026 als gültig deklariert". Fix: § 11 der aktuellen Satzung 31.03.2026 öffnen, exakte Ruhezeiten zitieren. Wenn diese identisch zur Vorgängerfassung sind: das aussagen statt vermuten. Wenn anders: korrigieren.
SCHWÄCHE 3 — Bund-der-Steuerzahler-Aussage ist intern widersprüchlich (Section "Bestattungskosten", erster Absatz): v4 schreibt: "gehörte Oberhausen zu den Großstädten mit moderaten Friedhofsgebühren — gleichzeitig zählte Oberhausen zu den Städten mit den deutlichsten Erhöhungen zum Jahreswechsel 2025". "Moderat" UND "deutliche Erhöhung" im selben Satz wirkt wie ein hingeschriebener Kompromiss, nicht wie eine belegte Aussage. Welche Position genau im BdSt-Ranking? Wie hoch war die Erhöhung in %? Welche Friedhofsgebühren konkret stiegen am stärksten (Erdbestattung Wahlgrab? Urne Reihengrab?)? Ohne diese Zahlen ist die Aussage rhetorisch unscharf — und die verlinkte BdSt-Quelle (Quelle 9) wird nicht spezifisch zitiert. Fix: Konkrete Position/Rang nennen ("Platz X von 23 Großstädten") und die Erhöhungs-Größenordnung als %-Angabe — oder den Satz streichen und nur den Verweis auf die Studie als Hintergrundlektüre stehen lassen.
SCHWÄCHE 4 (bonus) — datePublished = dateModified = 2026-05-13 (Schema-Block): Bleibt unverändert seit Round-6. Page wurde nachweislich durch mehrere Iterationen geschrieben; bei einem Article-Schema mit identischem datePublished/dateModified am selben Tag wie der Recheck-Lauf signalisiert man Frische. Bei späteren Edits (z. B. wenn echte 2026er-Tarife nachkommen) muss dateModified hochgesetzt werden, datePublished bleibt 2026-05-13 fix. Aktuell akzeptabel, aber als Workflow-Hinweis: nach Deploy datePublished einfrieren.

MUST-FIX vor Deploy: ja.

Konkret:

Fachverband-Name verifizieren (gegen Webseite des NRW-Bestatterverbands) oder in "BDB-Landesverband Nordrhein-Westfalen" generalisieren. Falscher Verbandsname auf einer Page, die als Trust-Signal Verbandsmitgliedschaften nennt, ist eigenes Eigentor.
§ 11 der aktuellen Friedhofssatzung 31.03.2026 öffnen und Ruhezeiten verifizieren — wenn unverändert, das aktiv aussagen ("Die Ruhezeiten in der Fassung 31.03.2026 entsprechen denen der Vorgängerfassung"); wenn geändert, korrigieren. So wie es jetzt steht, ist die FAQ-Antwort eine vermutende Aussage.
BdSt-Satz schärfen oder streichen. "Moderat + deutliche Erhöhung" ohne Zahlen ist Phrase. Entweder konkrete Rang-/Prozent-Angaben aus der BdSt-Studie 2025, oder Satz weg.

Die übrigen Punkte (datePublished-Hygiene) sind Workflow-Hinweis, kein Deploy-Blocker.

Page ist deutlich besser als v3 — die 78%→87%-Verbesserung ist real, primär durch das saubere Lösen der Tarif-Tabellen-Frage. Aber nicht deploy-fertig: zwei der drei Schwächen oben sind faktische Risiken, nicht Stilfragen.