Ich lese die aktuelle Bremen-Version und prüfe auf MAJOR-Issues.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/bremen/index.html?cb=1779094868084
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/bremen/index.html?cb=1779094868084

STADT: Bremen

VERDICT: CONDITIONAL PASS — 1 MAJOR (faktische Inkonsistenz), 2 MEDIUM-Hinweise im Major-Grenzbereich. Kein Deploy-Blocker, aber 1 Fix vor Live.

MAJOR-1 — Faktische Inkonsistenz Riensberger Fläche

Die Seite nennt zwei unterschiedliche Werte für denselben Friedhof:

Fließtext: „auf rund 20 Hektar Land … angelegt; Heute umfasst die Anlage rund 28 Hektar"
Implizit konsistent, aber: Die Quelle (Wikipedia / UBB) gibt heute meist rund 32 Hektar an, nicht 28. Bitte gegen UBB-Primärquelle verifizieren und einen Wert konsistent setzen. Risiko: Faktisch falsche oder unbelegte Flächenangabe auf YMYL-Seite.

MAJOR-2 (Grenzbereich) — Krematorium-Stilllegungsdatum widersprüchlich

Fließtext Riensberg: „1988 wurde das Krematorium außer Betrieb genommen"
Fließtext Huckelriede: „Seit 1988 Standort des einzigen Krematoriums"
FAQ + Hero implizieren konsistent 1988

Konsistent in der Seite, aber: Bremer Denkmalpflege datiert die Stilllegung auf 1995/96 (nicht 1988). Behrens-Architekt + Bauzeit 1903–1906 stimmt jetzt — gut. Stilllegungsjahr gegen Denkmalpflege-Quelle gegenchecken.

MAJOR-3 — Asche-Ausnahme: § und Drucksache mischen Quellen

§ 4 Abs. 1a + „4 kumulative Voraussetzungen" + Drs. 18/1581 stehen drin — gut. Aber: Drs. 18/2118 (Novelle 2015) und 18/1581 (Voraussetzungen) werden nebeneinander zitiert ohne Trennung der Rollen. Leser denkt, 1581 = Gesetz. Kurze Klarstellung: „1581 = Begründung/Materialien, 2118 = Gesetzesbeschluss".

Empfehlung: Fix MAJOR-1 + MAJOR-2 vor Deploy. MAJOR-3 redaktionell.

(248 Wörter)