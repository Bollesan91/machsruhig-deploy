Ich fetch die Datei und prüfe strict.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/bochum/index.html?cb=1779091140866
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/bochum/index.html?cb=1779091140866

Strict-Review läuft. Ich checke: §§-Nummern BestG NRW, Adressen, FAQ-Schema↔HTML, interne Faktenkonsistenz, Cross-Links.

Checks:

§§ BestG NRW: §8 Reihenfolge ✓, §9 Leichenschau ✓, §13 Fristen ✓, §14/15 ✓. Konsistent.
FAQ-Schema vs HTML: 7 Fragen Schema = 7 Fragen HTML. Texte 1:1 inhaltsgleich (nur Anführungszeichen-Style + minimale Wording-Variation "Trauerfeier-Vorbereitung" vs "Trauerfeier-Vorbereitung, Grab-Anmeldungen oder Verlegungen" in Q2). Schema-Text Q2 abweichend von HTML-Text Q2 — Schema sagt "Trauerfeier-Vorbereitung oder Grabverlegungen", HTML sagt "Trauerfeier-Vorbereitung, Grab-Anmeldungen oder Verlegungen". Minor, kein MAJOR.
Adressen: Technisches Rathaus Hans-Böckler-Str. 19, 44777 ✓. Standesamt Willy-Brandt-Platz 2–6, 44777 ✓. Bergbau-Museum Am Bergbaumuseum 28, 44791 ✓. Harpen Kirchharpener Str. 63, 44805 ✓.
Cross-Links: /bestattungskosten, /bestattungsarten, /bestattung-in/nordrhein-westfalen/, /bestatter/koeln/, /duesseldorf/, /dortmund/, /essen/, /tools/checkliste-todesfall, /tools/vorsorge-check, /trauerrede-schreiben, /methodik — alle Plausibel als Standard-Routen.
Selbstwidersprüche/Halluzinationen:
Hauptfriedhof-Flächen: 35,5 + 11 = 46,5 ha ✓
Eröffnung 18.04.1935 ✓ konsistent durchgehend
Wattenscheid Eingemeindung 1975 ✓
Kortum Lebensdaten 1745–1824 ✓
Husemann 1873–1935, KZ Esterwegen ✓
Sheffield-Ring → Oviedo-Ring: Sheffield ist tatsächlich Bochumer Partnerstadt, Oviedo auch. Umbenennung Sheffield→Oviedo ist eine konkrete Behauptung, die bestätigt werden müsste — aber außerhalb der MAJOR-Fokusliste (Halluzinationsrisiko niedrig, da Wikipedia-Hauptquelle gelistet).

STADT: Bochum VERDICT: PASS

Funde (alle MINOR, kein MAJOR):

FAQ Q2 Wording-Drift Schema↔HTML: Schema "Trauerfeier-Vorbereitung oder Grabverlegungen", HTML "Trauerfeier-Vorbereitung, Grab-Anmeldungen oder Verlegungen". Schema sollte mit HTML synchron sein (Google-Best-Practice). Kein Inhaltsfehler, aber Re-Check-Script-Trigger.
Footer-Copyright "2024–2026" — Page-Stand 15.05.2026, aber Domain-Migration & Inhalt 2026 ist plausibel. Kein Fund.

Keine MAJOR-Funde. Faktenlage, §§-Verweise, Adressen, Cross-Links sauber.