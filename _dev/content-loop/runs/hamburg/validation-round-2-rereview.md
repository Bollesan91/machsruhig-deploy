Ich lese die aktuelle Hamburg-Seite.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/hamburg/index.html?cb=1779094870766
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/hamburg/index.html?cb=1779094870766

STADT: Hamburg

VERDICT: CONDITIONAL PASS — Improver-Fixes sitzen (HmbBestattG-Datum/Novelle 2010, Seebestattungs-Staffel 1.049/1.646/1.895 €, Schema author auf #redaktion). Drei MAJOR-Issues bleiben.

FUND 1 — Anonyme-Beisetzung-Math inkonsistent (MAJOR, YMYL) Keyfacts & Tabelle: anonyme Beisetzung 1.250–1.420 € (Friedhof). FAQ „günstige Optionen": 1.250–1.420 € + 1.580–1.945 € Bestatter = 2.830–3.365 €. FAQ-Schema („Was kostet eine Bestattung"): „Eine anonyme Beisetzung ist mit 1.250–1.420 € die günstigste Option." → Schema suggeriert Gesamtkosten, Text sagt nur Friedhofsgebühr. Widerspruch zwischen sichtbarem FAQ und JSON-LD FAQ — Google liest beides. Fix: Schema-Antwort auf „Friedhofsgebühr 1.250–1.420 €, gesamt ca. 2.830–3.365 €" angleichen.

FUND 2 — Erdbestattungsfrist-Vergleich falsch (MAJOR, Faktenfehler) Text: „Schleswig-Holstein: 14 Tage". Das BestattG SH §16 nennt 8 Werktage (nicht 14). Bayern-Angabe „4 Tage" ist ebenfalls schief — BayBestG/BestV nennt 96 Stunden frühestens, 10 Tage spätestens. Falscher Vergleich untergräbt Vertrauen genau dort, wo die Seite Autorität aufbauen will. Fix: Vergleich streichen oder durch verifizierte Werte ersetzen mit §-Quelle.

FUND 3 — Bestatter-Basispreis-Formulierung kaputt (MAJOR, Verständlichkeit) „Erdbestattung: ab 1.945 € (Bestatter-Basispreis, seit Sept. 2024 zzgl. 81,20 €)". Was bedeutet „zzgl. 81,20 €"? Krematoriumsgebühr-Erhöhung? Verwaltungspauschale? Ohne Kontext wirkt das wie Copy-Paste-Artefakt aus Quellrecherche. Fix: entweder erklären (welche Position, warum) oder Wert in den Basispreis einrechnen und Hinweis streichen.