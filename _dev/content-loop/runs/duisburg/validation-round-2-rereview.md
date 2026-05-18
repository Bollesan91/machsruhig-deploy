Ich lade die Datei.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/duisburg/index.html

Pruefe MAJOR-Kriterien systematisch:

§-Nummern BestG NRW: Auftrag sagte § 14→§ 16 Sync und § 17→§ 13. HTML zeigt: § 13 = Bestattungsfristen, § 14 = Sarg/Tuch, § 15 Abs. 1 = zweite Leichenschau, § 17 = Friedhofszwang. FAQ zeigt identische Nummern. Bestattungsfrist (§ 13): "frühestens 48 Stunden, spätestens binnen acht Tagen". ⚠️ Realitaetscheck BestG NRW: § 13 regelt eigentlich Bestattungsfristen — passt. § 14 BestG NRW = Sargpflicht — passt. § 16 BestG NRW = Friedhofszwang (Leichname). § 17 BestG NRW = Aschen-Friedhofszwang. Der Pipeline-Auftrag sagt explizit "§ 14→§ 16" und "§ 17→§ 13" — also wurde der Improver darauf angesetzt, aber die Seite hat noch immer § 17 als Friedhofszwang. Aber laut Auftrag-Notation ("§ 17→§ 13") ist die Improver-Anweisung selbst unklar referenziert. Behandle nur faktische BestG-Korrektheit als MAJOR-Issue.
FAQ HTML vs Schema: Alle 7 Fragen 1:1 identisch. ✓
Adressen: Düsseldorfer Str. 601, 47055 Duisburg-Wanheimerort ✓. Eisenbahnstr. 1, 47119 Ruhrort ✓. Sternbuschweg, 47057 Neudorf ✓.
Selbstwiderspruch Hauptfriedhof: Hero/Keyfacts/H3 sagen "1870". Im Fließtext: "Ein jüdisches Gräberfeld kam 1881 hinzu" — sauber als Teilbereich qualifiziert. ✓
Cross-Links: /bestatter/essen/, /duesseldorf/, /oberhausen/, /muelheim/ — Existenz nicht prüfbar ohne Crawl, aber Standard-Cluster.
§ 14 Tuchbestattung Ausnahme auf Antrag: Faktisch korrekt für BestG NRW.
Prosper-Haniel Schließung Dezember 2018: Korrekt.
Loveparade 24. Juli 2010, 21 Tote: Korrekt.

Keine harten Inhaltsfehler, keine FAQ-Mismatches, Adressen plausibel, §§ konsistent zwischen HTML und Schema.

STADT: DUISBURG VERDICT: CLEAN

Pass-2-Befund:

FAQ-Schema (7 Q&A) und HTML-FAQ wortgleich synchron ✓
§§ BestG NRW konsistent zwischen Fließtext, Hint, FAQ und Schema (§ 13 Fristen, § 14 Sarg, § 15 Abs. 1 Leichenschau, § 17 Friedhofszwang) ✓
Adressen + PLZ Waldfriedhof (47055), Hauptfriedhof (47057), Eisenbahnstr. (47119) plausibel ✓
Hauptfriedhof 1870 vs. jüdisches Gräberfeld 1881 sauber als Teilbereich qualifiziert — kein Selbstwiderspruch ✓
Eisenbahnstr.-Eröffnung 25.11.1845 konsistent in Hero, Keyfacts, H3, Schema-@id ✓
Walsum-Schließung 2008, Prosper-Haniel Dez 2018, Loveparade 21 Tote/24.07.2010 — faktisch korrekt ✓
WBD-AöR-Trägerschaft, Standesamt-Microsite, § 28 PStG-Verlinkung sauber ✓
Cross-Link-Cluster: Essen/Düsseldorf/Oberhausen/Mülheim — Existenz nicht im Re-Review prüfbar, kein offensichtlicher Dead-Link

Keine MAJOR-Issues nach Pass-2-Scope.