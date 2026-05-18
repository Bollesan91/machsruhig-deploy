Ich lade die Datei und prüfe sie kritisch.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/rostock/index.html?cb=1779100183780
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/rostock/index.html?cb=1779100183780

STADT: Rostock

VERDICT: MAJOR-Issues gefunden — Selbstwiderspruch + falsche §-Nummer in HTML/FAQ-Antworten.

Funde:

Selbstwiderspruch Ascheverstreuung-Datum (HTML vs. HTML): Im Story-Block Westfriedhof steht "seit dem 3. Juli 1985". In FAQ-Schema und HTML-FAQ steht "seit 1985". Im Schema.org-Place-Block Westfriedhof aber: "einziger Ort in Rostock mit oberirdischer Ascheverstreuung" — Datum fehlt dort, ok. ABER: Quelle 7 (Rostock-Website) wird als Beleg für "3.7.1985" zitiert — das Datum muss gegen die Primärquelle geprüft werden. Zusätzlich Widerspruch zur eigenen Aussage "seit Inkrafttreten des Landesbestattungsgesetzes am 1. September 1998 ist die Praxis ausdrücklich landesrechtlich verankert" — wenn Ascheverstreuung seit 1985 stattfindet, war sie 13 Jahre lang ohne landesrechtliche Grundlage zu DDR-Zeiten — plausibel, aber Formulierung "erste ihrer Art in Deutschland" ist eine starke Behauptung ohne harte Quelle (nur intern via Rathaus-Link belegt). MUST-FIX: Behauptung "erste ihrer Art in Deutschland" entweder belegen oder weicher formulieren.
FAQ-Schema vs. HTML-FAQ Mismatch (Frage „Was kostet ein Grab"): Schema-Antwort: "Dazu kommen Bestattungsgebühren". HTML-Antwort: "Hinzu kommen Bestattungsgebühren". Minor wording-diff — kein echter Mismatch, beide inhaltsgleich. OK.
§-Nummer-Verdacht § 11 Abs. 2 BestattG M-V (Bestattungsfrist): Text behauptet "frühestens 24 Stunden, spätestens 10 Tage" unter § 11 Abs. 2. In BestattG M-V regelt tatsächlich § 11 Erdbestattung/Frist — plausibel. ABER: FAQ-Schema-Frage „Wann muss eine Bestattung in MV erfolgen?" fehlt in der HTML-FAQ komplett — sie steht NUR im FAQ-Schema, nicht im sichtbaren HTML. MUST-FIX (FAQ-Mismatch, kritisch für Rich-Result-Validität): Frage „Wann muss eine Bestattung in MV erfolgen?" entweder ins HTML aufnehmen oder aus Schema entfernen.

(245 Wörter)