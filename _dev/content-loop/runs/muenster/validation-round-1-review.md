Ich lade die Datei und reviewe.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/muenster/index.html

STADT: MUENSTER
VERDICT: MAJOR-FIX

1. Halluzination/Erfundene Friedhöfe (Inhaltsfehler) Wo: <div class="mr-section"> Friedhöfe-Tabelle Was: "Hauptfriedhof Münster", "Waldfriedhof Münster", "Friedhof Münster Osten" sind keine offiziellen Bezeichnungen. Münsters Hauptfriedhof heißt Zentralfriedhof (an der Robert-Koch-Straße); zentrale weitere: Waldfriedhof Lauheide (nicht "Waldfriedhof Münster") sowie ca. 13 Stadtteilfriedhöfe (Mauritz, Coerde, Handorf, Hiltrup etc.). "Friedhof Münster Osten" existiert nicht. Fix: Tabelle ersetzen durch Zentralfriedhof + Waldfriedhof Lauheide + 1–2 belegte Stadtteilfriedhöfe mit Quelle stadt-muenster.de.

2. Schema-Artefakt "None" (Inhaltsfehler/Selbstwiderspruch) Wo: JSON-LD Service.description Was: "...Bestattungsrecht None." — String-Templating-Bug, "None" steht wörtlich im strukturierten Daten-Output. Fix: "None" entfernen, korrekten Satz schließen.

3. Bundesland-Verweis ohne Inhalt (leere Sektion / fehlende §-Referenz) Wo: Sektion "Bestattungsrecht und Fristen" Was: Verweist nur generisch auf "Bestattungsgesetze des jeweiligen Bundeslandes" — Münster liegt in NRW, BestG NRW mit konkreten Fristen (§ 13 Bestattungsfrist, § 8 Totenfürsorgeberechtigte) wird nicht genannt. Sektion ist faktisch leer für eine YMYL-Stadtseite. Fix: BestG NRW § 13 (Bestattungsfrist max. 8 Tage nach Eintritt des Todes, Feuerbestattung 6 Wochen) und § 8 Reihenfolge der Totenfürsorgeberechtigten konkret nennen.