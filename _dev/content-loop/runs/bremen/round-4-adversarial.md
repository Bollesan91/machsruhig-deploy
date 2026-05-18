Ich hole mir die drei Dateien.

Fetching site
Web durchsucht

BRIEFING_OK

Jetzt zerlege ich v2. Ich gehe die 12 Schwächen-Kategorien im Kopf durch und gleiche v2 gegen v1-Review ab.

SCORE: 81/100

FUNDE:

SCHWÄCHE 1 (Halluzinations-Verdacht / Zahl-zu-spezifisch ohne Quelle): Sektion Riensberg — „etwa 18.000 Gräber" auf „rund 28 Hektar" und in Osterholz „rund 26.000 Gräber" auf „47 Gräberfeldern (Stand 2024)". Diese sehr spezifischen Zahlen tauchen in keiner der im Quellenblock verlinkten UBB-Seiten oder Wikipedia-Artikel ersichtlich auf — der UBB nennt typischerweise Hektar, aber keine Grab-Stückzahlen mit „Stand 2024". Insbesondere „47 Gräberfelder" wird sonst in der Bremer Friedhofsliteratur als deutlich höhere Zahl geführt (Osterholz hat traditionell mehr Felder). Verbesserung: Entweder konkrete Drucksache/UBB-Pressemitteilung mit Stand-Datum verlinken (Drs. 21/571 S ist im Quellenblock — wenn Zahl von dort, dann inline-Anker direkt am Satz) oder Zahl streichen. „Stand 2024" ohne Fundstelle ist ein klassischer Halluzinations-Marker, weil Stand-Angaben Belege verlangen.

SCHWÄCHE 2 (Quellen-Lücke an juristischer Schlüsselstelle): Sektion „Bremer Bestattungsrecht" — die Novelle wird jetzt mit „17. November 2015 (Brem.GBl. 2015, S. 540, Drs. 18/2118)" zitiert. Die Drucksachen-Angabe ist neu in v2 und löst MUST-FIX-Punkt aus v1, ABER: der Link dahinter führt nicht auf das Brem.GBl. oder die Drucksache 18/2118 selbst, sondern wieder nur auf das Transparenzportal-Gesetzes-Inhaltsverzeichnis. Wer die Drucksache prüfen will, klickt ins Leere. Bei der für die ganze Seite tragenden Aussage („bundesweit nahezu einmalig") ist das die Stelle, wo ein Reviewer mit Jurist-Brille zuerst klickt. Verbesserung: Eigener Link auf die Drucksache 18/2118 der Bremischen Bürgerschaft (bremische-buergerschaft.de) ODER auf die konkrete Fundstelle im Brem.GBl. 2015 S. 540. Sonst riecht die spezifische Drs.-Nummer wie eine Halluzination, die nicht gegengeprüft wird.

SCHWÄCHE 3 (Faktenfehler / Architekten-Widerspruch unaufgelöst): Sektion Riensberg — v1-Review hatte explizit als MUST-FIX angemahnt: Architekt des Riensberg-Krematoriums (1907) prüfen, Behrens vs. Wagner. v2 schreibt jetzt „Hugo Wagner". Das ist plausibel und entspricht dem v1-Vorschlag — ABER: Wagner gilt in der Bremer Architekturgeschichte primär als Theater- und Verwaltungsbau-Architekt, nicht als Krematoriumsspezialist. Die Quelle dafür ist nicht inline verlinkt (weder UBB noch Wikipedia direkt am Satz). Wenn v1 bereits unsicher war und v2 einfach von „Behrens" auf „Wagner" wechselt ohne Belegspur, ist das ein Loop-Risiko: Chat A könnte Halluzination gegen Halluzination getauscht haben. Verbesserung: Inline-Anker auf Wikipedia-Riensberg oder UBB-Riensberg-Seite direkt am Architekten-Namen, oder UNSURE-Kommentar im Backend-Loop-Log (NICHT im HTML). Aktuell steht es als harte Tatsachenbehauptung ohne nachvollziehbare Quellenkette.

SCHWÄCHE 4 (Strukturelle Schwäche — Bestattungskosten-Sektion fact-light): Die Kostentabelle nennt sechs Zeilen mit „ab"-Preisen (870 € / 1.240 € / 1.620 € / 2.380 € / 690 €), aber NULL davon ist inline auf die UBB-Gebührenordnung verlinkt. Der Hinweissatz davor sagt „verbindlich ist ausschließlich die aktuelle Gebührenordnung des UBB" mit Link — aber die konkreten Eurozahlen schweben quellenlos darüber. Schlimmer: Diese „ab"-Werte sind die Zahlen, wegen denen User die Seite überhaupt anklicken (Money-Keyword Bestattungskosten Bremen), und sie tragen kein einziges Belegankerchen. Wenn ein UBB-Mitarbeiter oder ein Mitbewerber die Seite prüft und die Gebührenordnung 2025 andere Werte ausweist, ist die Seite sofort angreifbar. Verbesserung: Entweder konkrete UBB-Gebührenordnung-PDF (das 2020er PDF ist im Quellenblock — wenn Werte daher, dann inline-Anker pro Zeile oder mindestens am Tabellen-Kopf) oder Zahlen entschärfen („Größenordnungen laut UBB-Gebührenordnung 2020, aktualisiert 2025: …"). Das ist YMYL-Geld-Inhalt ohne Primärquellen-Anker.

MUST-FIX vor Deploy: ja.

Schwäche 1 (Grab-Stückzahlen mit „Stand 2024" ohne Beleg) und Schwäche 4 (Kostentabelle ohne inline-Anker auf UBB-Gebührenordnung) sind beide Show-Stopper für eine YMYL-Seite. Schwäche 2 (Drs. 18/2118 ohne Link auf Drucksache selbst) ist Pflicht, weil v2 genau diesen v1-MUST-FIX adressieren sollte und nur halb erledigt hat. Schwäche 3 (Wagner-Beleg) ist Pflicht nach Re-Check-Logik, weil v1 explizit UNSURE markiert hatte und v2 die Unsicherheit kommentarlos in eine Tatsachenbehauptung verwandelt hat — genau das Muster, das die Bolle-Loop-Architektur verhindern soll.

Page ist deutlich besser als v1 (74 → 81), aber 81 ist nicht 85+, und die vier Punkte sind alle in der konkreten Stelle verortet, alle innerhalb von 30 Minuten fixbar.