Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/duesseldorf/v6-final.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/duesseldorf/v6-final.html

Verifikation Standesamt-Adresse gegen Primärquelle:

Web durchsucht
Web durchsucht

Adressdaten gegen die offizielle duesseldorf.de-Standesamt-Seite verifiziert: „Standesamt Düsseldorf · Inselstraße 17 · 40479 Düsseldorf · 0211 - 8994933" — beide Adressbestandteile bestätigt. Meine Adv-v5-Vermutung „PLZ müsste 40213" war falsch: PLZ 40479 ist korrekt, das Standesamt steht direkt am Hofgarten in Pempelfort, nicht in der Altstadt. Damit korrigiere ich auch den eigenen Adv-Befund — die v4/v5-Pipeline hatte recht, der Reviewer hatte unrecht.

SCORE: 94/100

v5-MUST-FIX-Status:

Standesamt-Adresse Pipeline-Pattern (3 Runden): ERLEDIGT vorbildlich. (a) Body-Text führt die Adresse jetzt mit expliziter Primärquellen-Attribution: „Standesamt Düsseldorf, Inselstraße 17, 40479 Düsseldorf (laut duesseldorf.de/standesamt). Adresse, Erreichbarkeit und Sprechzeiten sind dort verbindlich abrufbar." Inline-Link auf die offizielle Stadt-URL. (b) Schema.org-Block hat einen neuen GovernmentOffice-Eintrag erhalten: Standesamt Düsseldorf, Inselstraße 17, 40479 Düsseldorf, +49 211 8994933, url: duesseldorf.de/standesamt — Body und Schema sind jetzt in Sync. (c) Quellenliste hat einen Standesamt-Eintrag mit identischer Adresse nachgepflegt. (d) Telefonnummer 0211 8994933 wurde neu und korrekt aus der Primärquelle übernommen. Verifikation gegen duesseldorf.de bestätigt: Adresse, PLZ und Telefonnummer stimmen exakt. Der Adv-v5-Befund „PLZ vermutlich 40213" war falsch — die Pipeline hat die Recherche besser gemacht als der Adversarial-Reviewer. Pipeline-Disziplin endgültig hergestellt. ✓

Bonus über das MUST-FIX hinaus: OG-Image auf stadt-spezifisches og-duesseldorf.png umgestellt mit og:image:alt-Text — Cross-Page-Konsistenz mit Bochum/Duisburg hergestellt.

NEUE Schwächen (max 2, nur wenn ehrlich gefährlich):

Systematischer Durchgang durch v6 mit dem Fokus auf neu eingeführte Detail-Aussagen (Pipeline-Pattern):

Schwäche A (Kategorie 8 — strukturell, kein YMYL-Vektor): Die Gebührentabelle bleibt mit „Stand 01.01.2024"-Beträgen, obwohl die 2026er Fassung seit 1. Januar 2026 (also über 4 Monate vor Page-Stand 15.05.2026) in Kraft ist. Der Text erklärt das transparent („jüngste öffentlich vollständig dokumentierte Version") und verlinkt verbindlich auf die 2026er Fassung — kein Halluzinations-Vektor, aber strukturell merkwürdig, dass die Pipeline nach 4+ Monaten 2026-Geltung die 2024er Werte stehen lässt. Ein lokaler Reviewer würde fragen: „Wenn der Rat die 2026er Beträge am 12.12.2025 beschlossen hat und seit 01.01.2026 anwendet, warum kann die Page Mitte Mai 2026 nicht zwei Beträge aus der aktuellen Fassung zitieren?" — die 2026er Tarifpositionen müssten auf duesseldorf.de/stadtrecht/6/68/68-203-1 abrufbar sein. Mini-Risiko, kein Blocker, kein Halluzinations-Befund — aber die einzige Polish-Schwäche, die ein gründlicher Düsseldorfer Bestatter oder Verbraucherschutz-Anwalt noch ankreiden könnte. Fix (für v7-Cleanup): Mindestens 1.1.2.1 und 2.1.2 (die zwei wichtigsten Positionen) aus der 2026er Fassung beschaffen und in die Tabelle aufnehmen, die 2024er-Werte ggf. als zweite Spalte zur Verlaufstransparenz.
Schwäche B (Kategorie 11 — sehr minor, Polish): Im Bestatter-Wahl-Block steht weiterhin: „In Düsseldorf sind rund 80 Bestattungsunternehmen aktiv". Die Zahl ist seit v3/v4 unverändert ohne Inline-Quelle. Plausibel für eine Stadt mit 620k Einwohnern, aber unbelegt — Cross-Page-Konsistenzfrage: Duisburg v6 sagt „mehrere Dutzend", Krefeld zitiert konkrete Innungs-Mitgliederzahlen, Düsseldorf zitiert „rund 80" ohne Quelle. Sehr niedriges Risiko, weil die Zahl im plausiblen Korridor liegt — aber ein Hinweis darauf, dass die Pipeline alte Detail-Aussagen aus früheren Runden nicht systematisch nach-prüft. Fix (optional): Entweder mit BDB-Bestatter-Finden-PLZ-Filter belegen („laut bestatter.de PLZ-Suche etwa X Innungs-Mitglieder im Düsseldorfer Stadtgebiet") oder zu „mehrere Dutzend" abrunden.

MUST-FIX vor Deploy: NEIN

Begründung: Das v5-MUST-FIX (Standesamt-Adresse, dritte Runde) ist nicht nur abgearbeitet, sondern methodisch vorbildlich: Body mit Primärquellen-Attribution, Schema.org-GovernmentOffice-Block neu angelegt, Quellenliste nachgepflegt, Telefonnummer aus offizieller Quelle übernommen — und die OG-Image-Cross-Page-Schwäche gleich mit gelöst. Die Verifikation gegen duesseldorf.de zeigt: alle Adressbestandteile (Inselstraße 17, 40479, Tel. 0211-8994933) sind durch die offizielle Stadt-URL bestätigt. Die Page hat ihre persistente Schwachstelle aus drei Adv-Runden endgültig saniert.

Schwäche A (2024er Gebühren-Tabelle trotz 2026er Fassung) ist eine strukturelle Polish-Frage, die die Page selbst durch transparenten Disclaimer und verbindlichen Link auf die aktuelle Fassung neutralisiert — kein Halluzinations-Vektor, kein YMYL-Risiko. Schwäche B (80 Bestatter) ist eine Mini-Floskel-Stelle ohne falsifizierbaren Fakt-Kern.

Score 94: Saubere v5-MUST-FIX-Sanierung (+3 gegenüber v5 91/100) + Bonus für OG-Image-Cross-Page-Konsistenz und Schema.org-GovernmentOffice-Erweiterung (+0, bereits eingerechnet). Page ist deploy-fertig. Die zwei Restschwächen sind Polish-Material für einen späteren Cleanup-Pass, kein Blocker.

Meta-Pipeline-Befund: v6 ist die erste Düsseldorf-Iteration, in der keine neue ungeprüfte Detail-Aussage in einer anderen Sektion eingeführt wurde — das Pipeline-Pattern „eine neue Halluzination pro Runde" ist erstmals durchbrochen. Außerdem hat die Pipeline einen Adv-Befund (PLZ 40213) durch externe Verifikation widerlegt statt blind übernommen — das ist Reife-Indikator. Die machsruhig-Page-Familie wird in der Adv-Disziplin sichtbar besser.