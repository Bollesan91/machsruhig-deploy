Ich lade die Dateien.

Fetching site
Web durchsucht

Ich prüfe v3 strikt gegen die vier MUST-FIX-Punkte aus dem v2-Adversarial-Review und gehe parallel die 12 Schwächen-Kategorien durch.

BRIEFING_OK — ich habe die Page nicht geschrieben, ich suche Schwächen.

MUST-FIX-Check aus v2-Review (81%):

MF1 (Grab-Stückzahlen „Stand 2024"): ✅ ERLEDIGT. Die spezifischen Zahlen „18.000 Gräber", „26.000 Gräber", „47 Gräberfelder Stand 2024" sind in v3 vollständig entfernt. Riensberg nennt nur noch 28 ha; Osterholz nennt „mehrere zehntausend Verstorbene" — vage, aber nicht angreifbar.
MF2 (Drs. 18/2118 ohne Link auf Drucksache): ✅ ERLEDIGT. Eigener Link auf bremische-buergerschaft.de/index.php?id=222&...laufende_nummer=2118&wahlperiode=18 ist inline am Satz „Drucksache 18/2118".
MF3 (Hugo Wagner ohne Beleg): ⚠️ HALB ERLEDIGT. Inline-Link auf Wikipedia-Riensberg ist jetzt direkt am Architekten-Namen mit Formulierung „Architekt nach Wikipedia-Artikel zum Riensberger Friedhof: Hugo Wagner". Die Unsicherheit ist transparent gemacht (Wikipedia als Sekundärquelle deklariert), das ist akzeptabel.
MF4 (Kostentabelle ohne Quellen-Anker): ✅ ERLEDIGT. Inline-Link auf UBB-Gebührenordnungs-PDF (Dezember 2020) ist im Einleitungssatz UND in der Tabellen-Fußnote. Die Zahlen sind explizit als „Größenordnungen aus Marktbeobachtungen 2025/2026, abgeleitet aus" entschärft.

Alle vier MUST-FIX-Punkte aus v2 sind adressiert. Jetzt suche ich neue Schwächen in v3.

SCORE: 86/100

FUNDE:

SCHWÄCHE 1 (Halluzinations-Verdacht / „66 Gräber bedeutender Persönlichkeiten"): Sektion Riensberg, Hidden Gem — der Satz „Unter den rund 66 Gräbern bedeutender Persönlichkeiten findet sich das eines Sioux-Angehörigen..." nennt eine sehr konkrete Zahl (66), die in keiner der drei am Absatz verlinkten Quellen (Spurensuche, Wikipedia-Riensberg, UBB-Riensberg) als solche auftaucht, jedenfalls nicht ohne weiteres prüfbar. Das ist exakt das Muster, vor dem das Briefing warnt: spezifische Zahl ohne erkennbaren Beleg-Anker direkt am Satz. Wenn die 66 aus Wikipedia stammt, dann gehört der Wikipedia-Link an genau dieses Zahlwort, nicht erst zwei Halbsätze später am Sioux-Verweis. Verbesserung: Inline-Anker direkt an „rund 66 Gräbern" auf den konkreten Wikipedia-Abschnitt (#Persönlichkeiten) oder Zahl auf „rund 60 Gräber bedeutender Bremer Persönlichkeiten" vagisieren — der Punkt der Aussage ist die Liste der Namen darunter, nicht die Stückzahl.

SCHWÄCHE 2 (Faktenfehler-Verdacht / Paul Freye Geburtsjahr): Sektion Osterholz — „Den Architektenwettbewerb gewann mit dem zweiten Preis der Berliner Gartenarchitekt Paul Freye (1896–1958) gemeinsam mit dem Architekten Franz Seeck". Der Osterholzer Friedhof wurde am 1. Mai 1920 eröffnet. Ein 1896 geborener Gartenarchitekt hätte den Wettbewerb mit 23–24 Jahren gewonnen — möglich, aber ungewöhnlich für einen Friedhof dieser Größenordnung. Verdacht: Geburtsjahr ist verwechselt mit einem anderen Freye, oder es war ein älterer Paul Freye. Wikipedia-Osterholzer-Friedhof ist im Quellenblock, aber nicht inline am Namen. Wenn das Geburtsdatum nicht aus einer prüfbaren Primärquelle stammt (Adressbuch, Architektenkammer-Eintrag, Friedhofs-Eigeneintrag „selbst beigesetzt"), gehört es entweder belegt oder gestrichen — „der Berliner Gartenarchitekt Paul Freye gemeinsam mit Franz Seeck" reicht inhaltlich. Verbesserung: Wikipedia-Anker inline an Freye, ODER Lebensdaten entfernen, ODER prüfen.

SCHWÄCHE 3 (Sektion „Was nach einem Todesfall in Bremen zu tun ist" — Faktenfehler bei Standesämtern): Die Sektion nennt „Standesämter Mitte, Nord, Süd, Ost und West sowie die Stadtteilbüros". Bremen hat tatsächlich ein zentrales Standesamt Bremen (Hauptstandesamt, Hollerallee) plus dezentrale Stadtteilbüros — die Aufzählung „Mitte/Nord/Süd/Ost/West" entspricht der Bremer Bezirks-/Ortsamtsstruktur, aber nicht zwingend einer Standesamts-Aufteilung mit diesen exakten Namen. Das ist ein klassisches LLM-Muster: plausibel klingende Verwaltungs-Topographie wird aus der Stadtgliederung generiert, ohne dass die zuständige Behörde so heißt. Kein inline-Link auf eine konkrete Bremen.de-Standesamt-Übersicht direkt am Aufzählungs-Satz — nur generisch auf das Bürgerservice-Portal. Verbesserung: Konkrete bremen.de-Seite zum Standesamt Bremen inline verlinken ODER Aufzählung neutralisieren („die Standesämter der Stadt Bremen") — Letzteres ist sicher, das Erstere wäre besser.

SCHWÄCHE 4 (Cross-Link-Inkonsistenz / Verwirrung Stadt vs. Bundesland): Die Page verlinkt mehrfach „Bestattung in Bremen (Bundesland)" als /bestattung-in/bremen/. Gleichzeitig steht die Stadt-Page selbst auf /bestatter/bremen/. Im Hero-Lead wird die Bundeslandseite nicht erwähnt, obwohl die ganze Einleitung der nächsten Sektion („Diese Stadtseite behandelt ausschließlich die Stadtgemeinde Bremen; ... auf der Bundeslandseite dokumentiert") implizit verspricht, dass es sie gibt. Wenn die Bundeslandseite real existiert, fehlt der frühe Hinweis im Hero („Für das Landesrecht siehe die Bundeslandseite Bestattung in Bremen"). Wenn sie noch nicht live ist, sind drei Inline-Links plus FAQ-Verweis tote Links. Das ist ein deploy-blockierender Punkt, der nicht im Page-Content selbst lösbar ist — er hängt am Site-Status. Verbesserung: Vor Deploy verifizieren, dass /bestattung-in/bremen/ existiert und mindestens Bestattungsfristen § 13 + Sargpflicht § 11 behandelt. Andernfalls Inline-Links entfernen und Hinweis umformulieren auf „auf einer separaten Landesrechts-Übersicht (in Vorbereitung)".

MUST-FIX vor Deploy: ja.

Begründung: Page ist substanziell besser als v2 (81 → 86), alle vier alten MUST-FIX-Punkte sind sauber adressiert. ABER:

Schwäche 1 (66 Gräber) und Schwäche 2 (Freye 1896) sind genau das Muster, das v2 schon hatte und das die Loop verhindern soll: spezifische Zahlen ohne direkten Beleg-Anker. Schnell fixbar (5–10 Min), aber Pflicht für YMYL.
Schwäche 4 (Bundeslandseite) ist deploy-kritisch unabhängig vom Content: tote interne Links auf einer Stadt-Page killen die Re-Check-Logik und sind nach der Bundesland-Recheck-Skript-Doktrin ein harter Blocker.
Schwäche 3 (Standesämter) ist weniger kritisch, aber im YMYL-Kontext „was muss ich nach einem Todesfall tun" zählt jede Behördenangabe.

Page wäre bei 89–90, wenn die vier Punkte gefixt sind. Aktueller Stand 86 ist über deinem 85-Schwellwert, aber die Halluzinations-Verdachtsmomente bei Zahlen sind genau das Risiko, das nicht durch einen Score-Cut-off durchgewunken werden sollte. Quick-Fix-Runde empfohlen, dann Re-Check, dann Go-Live.