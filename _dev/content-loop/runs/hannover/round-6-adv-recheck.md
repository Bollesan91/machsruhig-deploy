Ich lade die drei Dateien und prüfe.

Fetching site
Web durchsucht

Ich prüfe die drei MUST-FIX-Punkte aus v2 gegen v3.

MUST-FIX 1 — Marschner-Halluzination am Gartenfriedhof: Volltextsuche „Marschner" in v3 → kein Treffer. Gartenfriedhof-Persönlichkeiten in v3: Charlotte Kestner und Laves. Marschner ist raus. ✓ Behoben.

MUST-FIX 2 — Lessing „umgebettet": Volltextsuche „umgebettet" in v3 → kein Treffer. Lessing-Eintrag in v3: nur „1872–1933, Philosoph mit Hannover-Bezug". Keine Marienbad/Umbettungs-Behauptung mehr. ✓ Behoben.

MUST-FIX 3 — § 12 BestattG für Friedhofszwang: v3 schreibt „Nach dem BestattG Niedersachsen dürfen Verstorbene grundsätzlich nur auf einem öffentlichen Friedhof…" — der §-Verweis ist entfernt, durch generischen Gesetzesverweis ersetzt, plus UNSURE-Kommentar dazu. ✓ Behoben (Risiko entschärft).

Jetzt prüfe ich, ob v3 neue Schwächen eingeführt hat oder bekannte Sekundärbefunde noch substantiell offen sind.

Web durchsucht
Web durchsucht

Substantielle neue Funde aus der Quellenrecherche:

Engesohde: v3 schreibt „rund 30 Hektar". Stadt Hannover (Primärquelle, hannover.de) sagt: 22 Hektar, 1864 eröffnet. Wikipedia: 21,7 Hektar, 52 Abteilungen. Auch visit-hannover.com nennt 21,7 Hektar. 30 ha ist faktisch falsch — ca. 35% zu hoch. Das ist eine substanzielle Zahlenfehlerangabe in v3, die in v2 als „Wikipedia ~30 ha" eingeführt wurde, aber Wikipedia sagt selbst 21,7. Halluzination. 
Hannover.de + 2

Lahe: v3 schreibt „Anfang der 1960er Jahre" + „rund 75 Hektar". Visit-Hannover sagt: 1968 eröffnet, 37 Hektar. v3 ist sowohl beim Jahr (1968, nicht „Anfang 1960er") als auch bei der Fläche (37 statt 75 ha) deutlich daneben. Zweite substantielle Zahlenfehlerangabe. 
visit-hannover

Seelhorst: v3 schreibt „rund 56 Hektar, 1924 eröffnet, Hermann Kube". Denkmalatlas Niedersachsen sagt: heute mit 68 Hektar Fläche größter Friedhof der Stadt, Hermann Kube plante ab 1919. Also: Seelhorst ist mit 68 ha größer als Lahe (37 ha) — v3 behauptet das Gegenteil („Lahe flächenmäßig größter"). Das ist ein strukturelles Problem: die ganze Hierarchie-Argumentation („Lahe = größter Waldfriedhof") ist falsch. 
Niedersachsen

Gartenfriedhof-Schließung: Stadt Hannover sagt: Zum gleichen Zeitpunkt wurden einige kleine innerstädtische Anlagen wie der Gartenfriedhof und der Nicolai-Friedhof aufgelassen — also 1864 ist tatsächlich belegt. ✓ Hier war der Sekundärbefund aus v2 falsch. 
hannover

Eingangsbau Engesohde: v3 schreibt „Kapelle aus den frühen 1870er Jahren". Wikipedia: Eingangsbau 1873 von Droste. Stadt Hannover: Kapelle 1912 eingeweiht. Die Kapelle ist also nicht aus den 1870ern, sondern aus 1910/1912 — v3 verwechselt Eingangsbau (1873) mit Kapelle (1912). Drittes Faktenproblem. 
Wikipedia
Hannover.de

Score-Begründung: v3 hat alle 3 MUST-FIX aus v2 sauber behoben (Marschner raus, Lessing-Umbettung raus, § 12 raus). Dafür gibt es Verbesserung. ABER: bei der Recherche fallen drei neue, harte Zahlenfehler auf, die ein YMYL-Reviewer in 10 Min mit hannover.de + Wikipedia gegencheckt — die hätten in v2 schon auffallen müssen und sind in v3 ungeprüft drin geblieben. Das ist Halluzinations-Risiko-Kategorie und Deploy-Blocker.

BRIEFING_OK

SCORE: 74/100

FUNDE:

SCHWÄCHE 1 — Flächenangabe Engesohde „rund 30 Hektar" ist faktisch falsch (Engesohde-Sektion + FAQ). Stadt Hannover (hannover.de) nennt 22 Hektar, Wikipedia 21,7 Hektar. v3 liegt ca. 35% zu hoch — das ist keine Rundungsunschärfe, sondern ein Halluzinations-Treffer. Die Zahl wandert zusätzlich in die FAQ („rund 30 Hektar") und wird damit doppelt gepflanzt. Verbesserung: Auf 22 Hektar korrigieren (Primärquelle hannover.de), Wikipedia parallel zitieren, in FAQ identisch ziehen.

SCHWÄCHE 2 — Lahe-Größe und Eröffnungsjahr beide falsch, und Hierarchie-Aussage „flächenmäßig größter" damit hinfällig (Lahe-Sektion + Keyfacts + FAQ). v3: „Anfang der 1960er, rund 75 Hektar". Visit-Hannover/Stadt: 1968 eröffnet, 37 Hektar. Denkmalatlas Niedersachsen nennt Seelhorst mit 68 Hektar als größten Friedhof der Stadt — nicht Lahe. v3 baut Keyfacts („Größter Fläche: Lahe"), FAQ („Lahe mit rund 75 Hektar der größte") und Sektions-Headline („Lahe — der flächenmäßig größte Waldfriedhof") komplett auf der falschen Hierarchie auf. Das ist nicht eine Zahl falsch, sondern eine Struktur-Aussage falsch, die sich durch drei Stellen zieht. Verbesserung: Lahe = 1968, ~37 ha. Seelhorst neu als „flächenmäßig größter" mit 68 ha einsetzen. Keyfacts, Sektions-H3 und FAQ-Antwort konsistent ziehen. Primärquelle: denkmalatlas.niedersachsen.de + hannover.de.

SCHWÄCHE 3 — Verwechslung Eingangsbau / Kapelle Engesohde (Engesohde-Sektion). v3: „Kapelle aus den frühen 1870er Jahren". Wikipedia: Eingangsbau 1873 von Droste. Stadt Hannover: Kapelle 1912 eingeweiht (von Oskar Barnstorf). v3 verschiebt damit das prägende Architekturmerkmal um 40 Jahre und ordnet es dem falschen Architekten zu. Verbesserung: Trennen — „Eingangsbau im Rundbogenstil 1873 von Ludwig Droste, Kapelle 1912 von Oskar Barnstorf". Beleg: hannover.de + Wikipedia.

Sekundärbefunde (kein Blocker, aber erwähnenswert):

v3 nennt Wilhelm Busch, Lessing, Hase, Kopf als Engesohde-Promis. Kurt Schwitters (Dadaist) und Yvonne Georgi (Tänzerin) fehlen — beide werden von visit-hannover und green-hannover als prägende Engesohde-Gräber genannt. Schwitters ist eine offensichtliche Lücke für eine YMYL-Page mit Anspruch.
„Hannover ca. 545.000 Einwohner" — aktuelle Zahl der LSN liegt eher bei ~545k bis ~552k je nach Stand; nicht falsch, aber Stichtag fehlt.
Sargpflicht-Aussage: § 7 BestattG ist plausibel, sollte aber gegen die aktuelle Fassung auf voris.niedersachsen.de gegengeprüft werden — das war auch in v2 schon offen.

MUST-FIX vor Deploy: ja.

Begründung: v3 hat die drei v2-MUST-FIX sauber erledigt (Marschner, Lessing-Umbettung, § 12) — das ist anzuerkennen. Aber bei der Faktenprüfung gegen die offensichtlichsten Primärquellen (hannover.de, Denkmalatlas Niedersachsen, Visit-Hannover) fallen sofort drei harte Zahlenfehler auf: Engesohde 30 statt 22 ha, Lahe 75 statt 37 ha + 1960er statt 1968, Kapelle 1870er statt 1912. Besonders der Lahe-Fehler ist strukturell — die ganze „flächenmäßig größter"-Argumentation ist auf falschen Zahlen aufgebaut und zieht sich durch Keyfacts, Sektions-H3 und FAQ. Das ist exakt das Muster, das eine YMYL-Page nicht produzieren darf. Behebbar in 30–45 Min. Score 74/100, nicht 79 — weil v2-Befunde behoben wurden, aber neue substantielle Faktenprobleme aufgedeckt sind, die in v2 schon dringewesen wären, wenn der Adversarial sie gegen Primärquellen geprüft hätte.