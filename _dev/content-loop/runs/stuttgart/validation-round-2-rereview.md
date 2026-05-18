Ich rufe die Datei ab und prüfe sie.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/stuttgart/index.html

Ich prüfe die kritischen §-Nummern BestattG BW, da hier der größte Risikobereich liegt.

Web durchsucht
Web durchsucht

Kritischer Befund bestätigt. Ich prüfe noch § 37 (Bestattungsfristen) auf die 96h-Behauptung.

Web durchsucht
Web durchsucht

Klarheit ist hergestellt. Damit kann ich das Review schreiben.

Befunde:

§ 31 + § 37 Frist 48h: § 31 BestattG BW verweist auf § 21 Abs. 3 für die Rangfolge — die Seite zählt die Angehörigen direkt unter § 31 auf, ohne § 21 Abs. 3 zu nennen. Wichtiger: Die Behauptung "frühestens 48 Stunden nach Eintritt des Todes" ist falsch — das BestattG BW kennt keine 48h-Wartefrist (das wäre § 36 "Frühester Bestattungszeitpunkt", der aber keine solche Stundenangabe macht). § 37 regelt nur die 96h-Höchstfrist.
§ 13 BestattG BW Leichenschau: Die Leichenschau ist in BW nicht in § 13, sondern in §§ 20 ff. BestattG BW (Erster Teil: Leichenwesen) geregelt. § 13 BestattG BW existiert in anderem Kontext.
Adress-Asymmetrie Hauptfriedhof: Schema/Text sagen einmal "Bad Cannstatt" (HTML), einmal "Steinhaldenfeld" (Schema description + FAQ). Tatsächlich liegt der Hauptfriedhof in Bad Cannstatt, Steinhaldenfeld ist Nachbar-Stadtteil — die Formulierung "im Volksmund nach Steinhaldenfeld benannt" deckt das ab, aber FAQ/Schema bleiben inkonsistent zur korrekten Verortung.

STADT: STUTTGART VERDICT: MAJOR-FIX

1. § 37-Halluzination "frühestens 48 Stunden" Wo: Section "Bestattungsrecht", Absatz § 37. Problem: BestattG BW enthält keine 48h-Mindestfrist. § 37 regelt nur die 96h-Höchstfrist; § 36 ("Frühester Bestattungszeitpunkt") nennt keine Stundenzahl. Erfundene Norm. Fix: 48h-Satz streichen. Korrekt: „§ 37 BestattG BW: Verstorbene, die nicht in Leichenhallen aufgebahrt sind, müssen spätestens 96 Stunden nach Eintritt des Todes bestattet sein."

2. § 31 unvollständig + § 13 falsch Wo: Absatz § 31 + Section "Was nach Todesfall zu tun ist". Problem (a): § 31 BestattG BW listet keine Rangfolge selbst, sondern verweist auf § 21 Abs. 3 ("Für die Reihenfolge gilt § 21 Abs. 3 entsprechend"). Diese Kopplung fehlt. Problem (b): „Rechtsgrundlage ist § 13 BestattG BW" für die Leichenschau ist falsch — Leichenschau ist in §§ 20 ff. BestattG BW geregelt. Fix: § 31 ergänzen um „i.V.m. § 21 Abs. 3 BestattG BW"; § 13 ersetzen durch § 20 BestattG BW.

3. Hauptfriedhof — Schema/FAQ-Inkonsistenz Wo: Schema #hauptfriedhof description + FAQ-Schema „Hauptfriedhof in Stuttgart-Steinhaldenfeld" vs. HTML-Fließtext „in Stuttgart-Bad Cannstatt". Problem: Schema/FAQ verorten ihn in Steinhaldenfeld, HTML korrekt in Bad Cannstatt. Wiki-konsens: Bad Cannstatt. Fix: Schema- und FAQ-Strings auf „Hauptfriedhof in Bad Cannstatt" vereinheitlichen.