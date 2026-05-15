Ich lese erst die drei Dateien, bevor ich bewerte.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

Gelesen. Jetzt v3 streng gegen Adv-v2 prüfen — was wurde gefixt, was bleibt, was ist neu?

Adv-v2-Abgleich (was war Deploy-Blocker):

Wilhelm Engel (1881–1945): Im v3 nicht mehr auffindbar — ✓ entfernt
Keilmann 1973/74 / Trauerhalle Ost / Fritz-Bauer-Forum: Im v3 nicht mehr enthalten — ✓ entfernt
Bestatter-Sektion: Trauerhallen-Liste + Bergmannsbestattung-Mini-Absatz + IG BCE/Knappen-Kontaktebene + PLZ-Filter-Hinweis ergänzt — ✓ adressiert
§-Reihenfolge: bleibt „Ehegatten → Kinder → Eltern → Großeltern → Geschwister → Enkel" (Neben-Fund)
OG-Image: weiterhin /assets/og-image.png (Default, generisch) — nicht behoben
FAQ-Mehrwert: weiterhin hoher Body-Overlap

Jetzt v3 als eigene Page prüfen. Drei substantielle Schwächen suchen — nicht v2-Reste recyceln.

Kategorien-Durchgang:

Niobe-Mosaikwand / Ignatius Geitel 1954 — Sehr spezifische Behauptung („eines der bedeutendsten Mahnmale für die Opfer des Zweiten Weltkriegs in Bochum"), Künstlername Ignatius Geitel + Jahr 1954. In den verlinkten Quellen (Volksbund-Eintrag, ruhrgebiet-industriekultur.de, Wikipedia-Zentralfriedhof) habe ich diese Kombination Geitel+1954+Niobe nicht als gestützt im Text gesehen. Das riecht nach Halluzinations-Verdacht — analog zum „Wilhelm Engel"-Fall in v2. Ein Künstlername mit Jahreszahl auf YMYL-Page ohne explizite Primärquelle ist genau das, was Adv-v2 zum Deploy-Blocker machte.
„Carl Arnold Kortum (1745–1824)" — Lebensdaten check: Kortum war tatsächlich 1745–1824, das stimmt. „Jobsiade" stimmt auch (Wikipedia-bekannt). OK.
Stiepeler Dorfkirche „Kirchengründung 1008, Grabplatten ab 1360" und „Kirchhof Ümmingen mit Grabsteinen ab 1623" — Sehr spezifische Jahreszahlen ohne verlinkte Quelle in der Quellenliste. 1008 für Stiepel ist historisch zwar belegt (Adelheid-Stiftung), aber die Grabplatten-Datierungen 1360 und 1623 sind nicht in der Quellenliste gestützt. Mittlerer Halluzinations-Verdacht.
Zechen-Anzahl „mehr als 30 aktive Schachtanlagen" — Bochum hatte tatsächlich viele Zechen, aber Zahl ohne Quelle, „zeitweise mehr als 30" ist eher vage und vermutlich konservativ. Niedriger Verdacht.
PLZ-Liste 44787–44809 — Stimmt im Wesentlichen, OK.
§ 8 BestG NRW Reihenfolge — Adv-v2 hatte das als Neben-Fund markiert. v3 hat es nicht geprüft (offenbar). Bleibt offener Check. Tatsächlich ist die §-8-Reihenfolge in NRW: Ehegatte/eingetragener Lebenspartner → volljährige Kinder → Eltern → Großeltern → Enkel → Geschwister (Letzteres je nach Fassung). v3 schreibt „Großeltern, Geschwister und Enkel" — das ist die Reihenfolge, die v2 schon hatte. Recht.nrw-Volltext sollte gegengeprüft werden. Aber: das ist ein juristischer Detail-Check, der zwingend vor Deploy stattfinden muss.
OG-Image weiterhin Default — Adv-v2 hat das als Pflicht-vor-Deploy markiert. Nicht behoben. Aber: das ist eher technisches Polish, nicht Content-Schwäche im engeren Sinne.
Trauerhallen-Adressen unvollständig — „Große und Kleine Trauerhalle Hauptfriedhof Freigrafendamm — Immanuel-Kant-Straße, 44803 Bochum" — Hausnummer fehlt, Kapazitäten fehlen (Adv-v2 hat das explizit gefordert). Adressierung also nur halb.
FAQ-Mehrwert — weiterhin hoher Body-Overlap (4 von 7 FAQs sind Body-Recycling mit minimalem Add).
Bestattungsquote 2021 — „666 Erd- vs 2.603 Urnen, ~80%" wird zweimal genannt (Intro + Hauptfriedhof-Sektion). Quelle: „Stadt Bochum" — keine konkrete Veröffentlichung verlinkt. Bei einer so präzisen Zahl (666/2603) wäre die Primärquelle (Statistisches Jahrbuch Bochum, Friedhofsverwaltung-Pressemeldung) Pflicht. Quellen-Lücke.

Drei stärkste Schwächen filtern:

A) Niobe-Geitel-1954 — Halluzinations-Verdacht-Wiederholung, derselbe Fehlertyp wie Engel in v2
B) Bestattungsstatistik 666/2.603 ohne Primärquelle (sehr spezifische Zahl, doppelt zitiert)
C) § 8 BestG NRW Reihenfolge nicht abgeglichen + Stiepeler/Ümmingen-Datierungen ohne Quelle (juristisch/historisch nicht verifiziert)

Plus: OG-Image + FAQ-Mehrwert + Trauerhallen-Hausnummern bleiben Polish-Pflicht.

SCORE: 81/100

FUNDE:

SCHWÄCHE 1 (Halluzinations-Verdacht — Wiederholungs-Fehlertyp): Hauptfriedhof-Sektion, Absatz 3: „Das zentrale Mahnmal mit Hochkreuz und der Niobe-Mosaikwand von Ignatius Geitel (1954) erinnert an die Kriegstoten und ist eines der bedeutendsten Mahnmale für die Opfer des Zweiten Weltkriegs in Bochum." Spezifischer Künstlername + Jahr + Superlativ-Bewertung, aber keine der verlinkten Quellen (Volksbund, ruhrgebiet-industriekultur.de, Wikipedia Zentralfriedhof Bochum, Stadt-Bochum-Erinnerungsorte) belegt diese Kombination im Adv-Lese-Check sichtbar. Das ist exakt der Fehlertyp, der in v2 als „Wilhelm Engel" zum Deploy-Blocker wurde. Ignatius Geitel ist nicht prominent genug, dass eine Falschzuschreibung in einem lokalen Stadtarchiv-Check ungesehen bliebe. — Verbesserung: Primärquelle aus Stadt-Bochum-Erinnerungsorte-Verzeichnis (steht in Quellen) verifizieren und als Inline-Link setzen, oder Künstlername/Jahr/Superlativ streichen und nur „Hochkreuz und Mosaikwand zur Erinnerung an die Kriegstoten" behalten.
SCHWÄCHE 2 (Quellen-Lücke bei spezifischer Statistik, doppelt zitiert): Intro-Sektion + Hauptfriedhof-Sektion nennen beide die Zahl „666 Erdbestattungen / 2.603 Urnenbestattungen 2021, ~80% Feuerbestattung" mit Verweis „Stadt Bochum zählte". Diese Zahl ist auffällig präzise, taucht doppelt auf und ist tragend für die nachfolgende Argumentation („Median-Kostenniveau eher im Urnenbereich", „Gebührenstruktur"). In der Quellenliste taucht aber keine verlinkte Stadt-Bochum-Statistik-Quelle auf — weder ein Geschäftsbericht der Friedhofsverwaltung noch eine Pressemeldung noch das Statistische Jahrbuch. Bei einer Page, die als Gold-Referenz gedacht ist, ist eine Tragendzahl ohne klickbare Primärquelle ein Loch. — Verbesserung: Quelle der Bestattungsstatistik 2021 explizit in der Quellenliste mit Link aufnehmen (Friedhofsverwaltung Bochum Geschäftsbericht oder Pressemeldung); falls die Zahl aus einer Sekundärquelle stammt (z. B. WAZ, Bochumer Tageblatt), entsprechend als „nach Pressebericht XY" kennzeichnen analog zum memovida-Pattern bei den Gebühren.
SCHWÄCHE 3 (Doppel-Defizit: ungeprüfte §-Reihenfolge + ungestützte historische Datierungen): Zwei zusammenhängende Verifikations-Lücken. (a) § 8 BestG NRW Reihenfolge: v3 schreibt „Ehegatten → volljährige Kinder → Eltern → Großeltern, Geschwister und Enkel" — die letzte Triade ist im v2 schon als Neben-Fund markiert worden, in v3 nicht geprüft, obwohl recht.NRW in der Quellenliste verlinkt ist. Die übliche § 8 Abs. 1 BestG NRW-Reihenfolge in NRW lautet: Ehegatte/Lebenspartner → volljährige Kinder → Eltern → Großeltern → Enkel → Geschwister (Enkel vor Geschwister). Falls v3 das gegen den Volltext nicht abgeglichen hat, ist die Reihenfolge potenziell falsch — auf einer YMYL-Page im juristischen Kontext nicht akzeptabel. (b) Harpen-Sektion Schlusssatz: „Stiepeler Dorfkirche (Kirchengründung 1008, Grabplatten ab 1360) und Kirchhof Ümmingen mit Grabsteinen ab 1623." Sehr spezifische Datierungen ohne Quelle in der Quellenliste — gleicher Fehlertyp wie Schwäche 1, nur historisch statt biographisch. — Verbesserung: § 8 Abs. 1 BestG NRW gegen recht.NRW-Volltext abgleichen (5min) und Reihenfolge korrigieren oder bestätigen; Datierungen Stiepel 1008/1360 und Ümmingen 1623 entweder mit Quelle (Stadtarchiv Bochum / Kirchengemeinde Stiepel) inline belegen oder auf vage Formulierung („mittelalterliche Kirchengründung, historische Grabplatten") zurücknehmen.

Neben-Funde (keine Score-Treiber, aber notieren):

OG-Image weiterhin /assets/og-image.png (Default) — Adv-v2 hat es explizit als Pflicht vor Deploy markiert, in v3 nicht adressiert
Trauerhallen-Liste in Bestatter-Sektion: Hausnummer der Immanuel-Kant-Straße fehlt, Kapazitätsangaben (Sitzplätze Große/Kleine TH) fehlen — Adv-v2 hatte „Trauerhallen-Adressen plus Kapazitäten" gefordert, halb erfüllt
FAQ-Mehrwert: 4 von 7 FAQs weiterhin >80% wortgleich mit Body — reicht für Schema, nicht für User
Article-Schema: Author ist „Organization name: machsruhig.de Redaktion" — formal OK, aber kein realer Author-Name. E-E-A-T-mäßig schwächer als Personen-Author.

MUST-FIX vor Deploy: JA.

Begründung: Schwäche 1 (Niobe-Geitel-1954) ist exakt der gleiche Fehlertyp, der in v2 zum Deploy-Blocker wurde — eine spezifische, nicht primärquellengestützte Personenzuschreibung auf einer YMYL-Page im NS-/Erinnerungs-Kontext. Wenn dieser Fehlertyp zwei Runden überdauert, ist das ein systemisches Schreibmuster, das die Page als „Gold-Referenz" disqualifiziert, bis es behoben ist. Schwäche 3a (§ 8-Reihenfolge) ist juristischer Detail-Check mit 5min Aufwand — verzeihlich, wenn vor Deploy erledigt; ungelöst Deploy-Blocker. Schwäche 2 (Statistik-Quelle) ist Polish, aber bei einer Page mit Gold-Anspruch nicht verhandelbar.

Score 81 reflektiert: starker Sprung von 79 (v2→v3 hat die zwei harten Halluzinations-Verdachte aus v2 — Engel, Keilmann — sauber entfernt; Bestatter-Sektion ist substantiell lokalisiert; Trauerhallen-Liste, Bergmannsbestattung-Absatz, IG-BCE/Knappen-Kontaktebene sind ergänzt; PLZ-Bandbreite ist drin), aber neuer Halluzinations-Verdacht (Geitel/Niobe) zieht ~4 Punkte, fehlende Primärquelle für Tragendzahl ~3 Punkte, §-8-Reihenfolge + Datierungs-Trio ungeprüft ~2 Punkte, OG/FAQ/Hausnummern Restpolish ~10 Punkte. Page ist näher dran als v2, aber nicht über der 85-Schwelle.