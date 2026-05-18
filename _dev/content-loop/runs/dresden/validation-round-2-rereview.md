Ich lade die aktuelle Version und prüfe gezielt auf MAJOR-Issues.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/dresden/index.html?cb=1779092529082

STADT: Dresden

VERDICT: PASS mit 1 MAJOR. Improver-Fixes sitzen (Johannisfriedhof Trägerschaft jetzt sauber kirchlich + kommunales Krematorium; FAQ-Schema §13/14/18/19 aligned; Bulk-Fix konsistent). Re-Check findet 1 substantielle Faktenunschärfe.

FUNDE:

1. MAJOR — Erich Ponto: Begräbnisort falsch Im Annenfriedhof-Abschnitt steht: „Unter den Bestatteten findet sich der Schauspieler und Theaterdirektor Erich Ponto (1884–1957)". Ponto starb zwar in Stuttgart, aber sein Grab liegt nach gängiger biografischer Quellenlage auf dem Waldfriedhof Stuttgart, nicht auf dem Alten Annenfriedhof Dresden. Dresden-Bezug = Wirkungsort (Staatstheater), nicht Grab. Da der Absatz unmittelbar danach Tessenow/Dix als „nicht hier bestattet trotz Dresden-Bezug" abgrenzt, ist die Ponto-Erwähnung in derselben Logik ein Eigentor. Fix: Vor Deploy entweder belastbare Primärquelle für Grab Annenfriedhof beibringen (Friedhofsverwaltung, Grabregister) — oder Ponto streichen und durch belegbare Bestattete ersetzen (z.B. aus Friedhofs-Eigendokumentation).

2. MINOR (nicht blockierend) — Krematorium-Denkmalschutz-Datum „steht seit 1985 unter Denkmalschutz" ist unbelegt im Quellenblock. Wikipedia/Stadt Dresden referenzieren typischerweise DDR-Denkmalliste; Jahresangabe sollte entweder mit Quelle gehärtet oder auf „ist denkmalgeschützt" verallgemeinert werden. Kein Deploy-Blocker.

EMPFEHLUNG: Ponto-Fix vor Deploy. Sonst ist die Seite YMYL-tauglich, Schema sauber, §-Mapping korrekt, Trägerschaft konsistent über Body/FAQ/JSON-LD.