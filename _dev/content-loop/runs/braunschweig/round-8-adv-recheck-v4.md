Ich lese die drei Dateien parallel und prüfe die MUST-FIX-Punkte konkret im v4-Code.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

Alle drei Dateien gelesen. Jetzt prüfe ich die v3-MUST-FIX systematisch im v4-Code und suche dann frische Schwächen.

MUST-FIX-Check v3 → v4:

Topografie: v4 sagt jetzt durchgängig "in unmittelbarer Nachbarschaft … getrennt durch den Jüdischen Friedhof" (Stadtfriedhof-Absatz) UND "Zwischen Hauptfriedhof und Stadtfriedhof liegt der Jüdische Friedhof" (Jüdischer-Friedhof-Absatz) UND Hero: "in einem zusammenhängenden Strang". → konsistent gefixt ✅
NS-Glättung Schultze: v4 hat das Hidden-Gem komplett umgeschrieben: NSDAP-Mitglied seit 1933, propagandistische Filmmusiken explizit benannt ("Bomben auf Engelland", "Kolberg"), Gottbegnadeten-Liste, Schwarze Liste 1945, zweite Karriere. → ehrlich gefixt ✅
Kosten-Tabelle: Keine "ab"-Angaben mehr, feste Beträge (795 €, 100 €, 32,90 €, 1.582,90 €), 20/25 Jahre Nutzungsrecht explizit. Krematoriumsgebühr ergänzt (200-350 €, Salzgitter/Wolfenbüttel/Hannover). → gefixt ✅

Jetzt adversarial: Wo sind die neuen Schwächen in v4?

SCORE: 87/100

FUNDE:

MUST-FIX v3 alle gefixt — Topografie konsistent, Schultze NS-ehrlich (NSDAP seit 1933, Gottbegnadeten-Liste, Schwarze Liste 1945, zweite Karriere), Kosten ohne "ab" mit Krematorium 200-350 €.
SCHWÄCHE 1 (neu) — FAQ-Rechenfehler "1.800 € realistisch": FAQ sagt "reine Friedhofsgebühren rund 928 € … Krematoriumsgebühr 200-350 € … realistische Gesamtkosten bei etwa 1.800 €". 928 + 350 = 1.278 €, plus Bestatter- und Drittkosten landet realistisch eher bei 2.500-3.500 € (siehe eigene Tabelle: "Urnenbestattung einfach 1.800-3.500 €"). Die 1.800 € sind das untere Ende der eigenen Spanne, aber im FAQ-Text als generelles Niveau dargestellt. Inkonsistent zur eigenen Tabelle und unrealistisch tief, weil reine Bestatterleistung (Sarg/Urne, Überführung, Beratung, Standesamt) in Braunschweig kaum unter 1.000-1.500 € liegt. → Auf 2.500-3.500 € korrigieren oder explizit als "ab"-Wert kennzeichnen.
SCHWÄCHE 2 (neu) — Quellen-Lücke "muslimisches Gräberfeld Abteilung 83": Zweimal verwendet (Recht-Sektion + FAQ Sargpflicht), aber keine Primärquelle hinterlegt. Weder im Quellenblock noch inline verlinkt. Wenn die Abteilungsnummer "83" sachlich falsch oder veraltet ist, hat die Page einen Hard-Fact-Fehler in einer YMYL-Kategorie (religiöse Bestattung). → Verlinkung zur Friedhofsverwaltung-Quelle, die Abteilung 83 explizit ausweist, oder vorsichtigere Formulierung ("in einem eigenen muslimischen Gräberfeld").
SCHWÄCHE 3 (neu) — Halluzinations-Verdacht "Naumburgstraße 25": Keyfacts und Sozialbestattungs-Sektion nennen "Fachbereich Soziales und Gesundheit, Naumburgstraße 25, 38124 Braunschweig" mit konkreten Sprechzeiten (Mo/Mi/Fr 9:00-12:30, Infothek). Die Quelle 8 (braunschweig.de/bestattungskosten) ist verlinkt, aber unklar ob diese spezifische Adresse + Öffnungszeiten dort wirklich so steht oder zusammenkonstruiert ist. Adress-Halluzinationen bei Ämtern sind ein klassischer KI-Failure. → Im Quellenblock explizit "Quelle 8 = Adresse + Sprechzeiten" verifizieren oder Sprechzeiten weglassen und nur auf die Quelle verweisen.
Nachrangig: Quellenblock hat 7 Wikipedia-Einträge bei 22 Quellen — für YMYL grenzwertig viel Sekundärquelle; Hidden-Gem-Details (Blumenau-Umbettung 20.06.1974) hängen an Wikipedia.

MUST-FIX vor Deploy: ja — SCHWÄCHE 1 (FAQ 1.800 € widerspricht eigener Tabelle) und SCHWÄCHE 3 (Adresse/Sprechzeiten verifizieren) sind beide vor Go-Live zu klären. SCHWÄCHE 2 ist Soft-Fix, kann auch nach Deploy nachgezogen werden.