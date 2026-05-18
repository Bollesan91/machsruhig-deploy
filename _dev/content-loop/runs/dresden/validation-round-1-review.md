Ich lade die Datei und reviewe.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/dresden/index.html?cb=1779091551766

STADT: Dresden

VERDICT: PASS mit 2 MAJOR-Funden

Fund 1 — Selbstwiderspruch Trägerschaft Johannisfriedhof Tolkewitz (MAJOR) Im Schema (Place "Johannisfriedhof Tolkewitz", Description) und im FAQ-Schema/HTML-FAQ "Wer ist Träger…" wird der Johannisfriedhof Tolkewitz als städtischer Hauptfriedhof Dresdens bzw. unter den städtischen Friedhöfen impliziert. Im Fließtext (Sektion "Bestattungsrecht" und "Die vier prägenden Friedhöfe") wird er korrekt als kirchlicher Friedhof in Trägerschaft der "Verwaltung des Elias-, Trinitatis- und Johannisfriedhofes zu Dresden" beschrieben, nur das Krematorium ist kommunal. → Schema-Description und FAQ-Antwort "Wer ist Träger" widersprechen dem Haupttext. Fix: Schema-Description anpassen ("kirchlicher Friedhof in Trägerschaft …, Krematorium kommunal betrieben"); FAQ-Antwort in HTML ist bereits korrigiert, aber FAQ-Schema-JSON listet "Heidefriedhof, Nordfriedhof, Dölzschen, Urnenhain Tolkewitz" als städtisch ohne Johannisfriedhof zu erwähnen → Mismatch HTML-FAQ vs FAQ-Schema (HTML nennt explizit "Verwaltung des Elias-, Trinitatis- und Johannisfriedhofes", Schema nicht).

Fund 2 — FAQ-Schema vs HTML Mismatch "Welches Recht gilt" (MAJOR) FAQ-Schema listet nur "Leichenschau, Friedhofszwang, Sargpflicht" allgemein. HTML-FAQ nennt explizit § 13, § 14, § 18, § 19 SächsBestG. → Antworten weichen inhaltlich ab. Fix: Schema-Antwort an HTML-Wortlaut angleichen (Paragraphen einfügen).

Fund 3 — Sargpflicht §-Nummer prüfen (MAJOR-Verdacht, UNSURE) Seite zitiert § 18 SächsBestG für Sargpflicht und § 19 für Friedhofszwang. Im SächsBestG ist die Sargpflicht tatsächlich in § 18, Friedhofszwang in § 19 — passt. Kein Fund hier, nur Bestätigung.

(232 Wörter)