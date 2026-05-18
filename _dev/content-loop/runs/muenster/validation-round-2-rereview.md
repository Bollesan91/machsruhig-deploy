Ich fetche die Datei.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/muenster/index.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/muenster/index.html

STADT: Münster

VERDICT: MAJOR-FIX

Funde (3):

1) Friedhofsnamen halluziniert / Improver-Fix NICHT angewendet

Wo: <table> unter "Friedhöfe und Bestattungsmöglichkeiten" (Zeilen ~Hauptfriedhof/Waldfriedhof/Friedhof Münster Osten)
Was: Listet "Hauptfriedhof Münster", "Waldfriedhof Münster", "Friedhof Münster Osten" — alle drei sind in Münster faktisch falsch. Münster hat Zentralfriedhof (nicht Hauptfriedhof), Waldfriedhof Lauheide (nicht "Waldfriedhof Münster") und Stadtteilfriedhöfe (kein "Münster Osten"). Improver-Korrektur aus Pass 1 wurde nicht übernommen → Halluzination weiterhin live.
Fix: Tabellenzeilen ersetzen durch: Zentralfriedhof Münster / Waldfriedhof Lauheide / Stadtteilfriedhöfe (Sammelzeile).

2) Schema-"None"-Artefakt nicht entfernt

Wo: <script type="application/ld+json"> → Service.description
Was: String enthält "Bestattungsrecht None." — Platzhalter-Artefakt aus Template-Generierung. Improver-Bulk-Fix laut Briefing erledigt, hier aber noch vorhanden → SERP-Sichtbarkeit.
Fix: "None" entfernen, Punkt direkt nach "Bestattungsrecht" setzen.

3) BestG NRW §13 / §8 fehlen komplett

Wo: Abschnitt "Bestattungsrecht und Fristen"
Was: Generischer Platzhaltertext ("richten sich nach den Bestattungsgesetzen des jeweiligen Bundeslandes"), obwohl Münster = NRW. Keine §13 BestG NRW (Bestattungsfrist), keine §8 BestG NRW (Totenfürsorgereihenfolge). Briefing nennt diese als konkretisiert + Bulk-Fix — hier nicht angekommen.
Fix: §13 BestG NRW (Frist Erdbestattung ≤ 8 Werktage, Einäscherung ≤ 6 Wochen) und §8 BestG NRW (Reihenfolge Ehegatte → volljährige Kinder → Eltern → …) einsetzen, analog zu Bochum/Dortmund.

Hinweis: Pass-2-Korrekturen scheinen auf diese Datei nicht angewendet worden zu sein — Pipeline-Check empfohlen, ob Improver auf falschem Branch/File gearbeitet hat.