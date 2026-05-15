Web durchsucht
Web durchsucht

BRIEFING_OK.

Jetzt der Adversarial Review von v2 — kalt gelesen, mit Fokus auf die 12 Schwächen-Kategorien. Ich habe v2 gegen die belegbaren Fakten, das v1-Review und die Quellenstruktur geprüft.

SCORE: 81/100

FUNDE:

SCHWÄCHE 1 — Halluzinations-/Falschzitat-Verdacht bei § 37 und § 39 BestattG BW (Sektion „Bestattungsrecht in Stuttgart"): Die Page zitiert die 96-Stunden-Höchstfrist unter § 37 Abs. 1 BestattG BW und die Sargpflicht unter § 39 BestattG BW. Das BestattG BW in der konsolidierten Fassung hat eine andere Paragraphenstruktur — Bestattungsfristen sind dort in § 36/§ 37 abhängig von der Fassung, Sargpflicht steht in § 32 BestattG BW (nicht § 39), Ruhezeit ist § 6 wie korrekt zitiert. Die §§ 31, 37, 39 wirken aus dem Personenstandsrecht/Hessen rüberkopiert. Verifizierungs-Pflicht vor Deploy: jeder einzelne § gegen landesrecht-bw.de geprüft, sonst ist die ganze Rechts-Sektion eine YMYL-Bombe. Das ist kein „könnte stimmen" — das ist „eine Stadt-Page mit falschen Paragraphen ist schlimmer als eine ohne Paragraphen".
SCHWÄCHE 2 — UNSURE-Kommentare wieder im ausgelieferten Code (Sektionen Hauptfriedhof Steinhaldenfeld + Bestattungskosten): v1-Review Punkt 7 hat genau das gerügt. v2 enthält erneut zwei <!-- UNSURE: ... --> HTML-Kommentare — einer bei Steinhaldenfeld (Architekt 1918), einer bei der Gebührentabelle (Tarifteil-Zuordnung). HTML-Kommentare gehen mit ans Live-System; ein Wettbewerber oder Journalist, der „View Source" macht, sieht: „Diese Redaktion liefert mit dokumentierten Recherche-Lücken aus". Auf einer YMYL-Page mit Schema-Author „machsruhig Redaktion" zerstört das die E-E-A-T-Glaubwürdigkeit. Fix: entweder Aussage entfernen oder Quelle finden — Kommentare raus, ohne Ausnahme.
SCHWÄCHE 3 — Gebührentabelle-Quellenstellen sind Pseudo-Belege (Sektion „Bestattungskosten 2025"): Jede Zelle der Spalte „Satzungsstelle" sagt „Gebührensatzung 2024, Tarifteil" — neunmal exakt derselbe nichtssagende Verweis. Das ist nicht „pro Position belegt" (wie v1-Review Punkt 3 forderte), sondern eine Spalte, die so tut, als wäre sie ein Beleg. Entweder echte Stellen aus dem PDF eintragen (§/Anlage/Tarifnummer) oder die Spalte ganz streichen und stattdessen direkt im Tabellenkopf den PDF-Link setzen. So ist es eine kosmetische Audit-Anpassung, die Genauigkeit vortäuscht — und ein versierter Reviewer sieht das in 10 Sekunden.
Nebenfund (zählt nicht zu den 3, aber notieren): Schema.org Place Hoppenlau sagt „1626 angelegt, seit 1880 geschlossen", Fließtext ebenfalls. Wikipedia und Stadtarchiv geben 1626 als Stiftungs-/Anlagejahr und 1880 als Schließung unterschiedlich an je nach Quelle (1880 vs. 1881). Vor Deploy gegen Stadtarchiv-Stuttgart prüfen, nicht gegen Wikipedia.

MUST-FIX vor Deploy: ja.

Schwäche 1 (falsche §§) und Schwäche 2 (UNSURE-Kommentare im Live-Code) sind beide Hard-Blocker. Schwäche 3 ist Audit-Theater und sollte mit, kostet aber 20 Minuten. Ohne die §-Verifikation darf die Page nicht live — auf einer Friedhofs-/Bestattungs-Page mit falschen Paragraphen riskierst du Abmahnung und Reputationsschaden, nicht nur Audit-Punkte.