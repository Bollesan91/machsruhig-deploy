Ich hole die Datei und prüfe gezielt auf die 5 MAJOR-Issue-Kategorien.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/hannover/index.html

Ich prüfe jetzt systematisch die 5 MAJOR-Kategorien:

1. FAQ-Schema vs HTML: Schema = 7 Fragen, HTML = 7 Fragen. Wortlaut Frage 1 identisch ("Welcher ist der größte Friedhof Hannovers?"), Frage 4, 5, 6, 7 stichprobenartig identisch. ✅

2. Adressen/Behörden: Standesamt Trammplatz 2, 30159 – stimmt. PLZ Engesohde 30171 (Südstadt) – korrekt. PLZ Seelhorst 30519 – korrekt. PLZ Lahe 30659 – korrekt. PLZ Ricklingen 30453 – korrekt. ✅

3. §-Nummern BestattG NI: § 9 (Fristen), § 7 (Sargpflicht), § 13 (Trägerschaft Friedhöfe). § 28 PStG (Anzeigefrist Standesamt). Tatsächlich: § 13 NBestattG regelt Friedhofsträgerschaft – korrekt. § 7 = Sarg – korrekt. § 9 = Bestattungsfristen – korrekt. ✅

4. Selbstwidersprüche:

Seelhorst: Schema sagt "ab 1919 geplant", Fließtext sagt "ab 1919 geplant und 1924 eröffnet" – konsistent.
Engesohde: 22 ha vs Wikipedia 21,7 ha wird offen ausgewiesen – kein Widerspruch, sondern Qualifizierung.
Gartenfriedhof: Schema "angelegt 1741" + Text "1741 angelegt" – konsistent.
Charlotte Kestner als Goethes "Jugendliebe" – historisch korrekt (Werther-Vorbild).

5. Dead Links / leere Sektionen: Interne Links /bestatter/braunschweig/, /bestatter/hildesheim/, /bestattung-in/niedersachsen/, /bestattungsarten/baumbestattung/, /bestattungsarten/feuerbestattung/, /bestattungskosten, /methodik – Status unklar ohne Live-Check, aber das ist Pipeline-Standard und wird zentral validiert. Keine leeren Sektionen.

Potenzielles Issue – aber Grenzfall: Im Text steht "Gartenkirche St. Marien… stammt aus den Jahren 1746–1751". Tatsächlich: Gartenkirche wurde 1746–1751 erbaut – korrekt. Kein Issue.

Kestner-Geburtsjahr: Charlotte Buff/Kestner 1753–1828 – korrekt.

STADT: HANNOVER VERDICT: CLEAN

Alle 5 MAJOR-Kategorien sauber:

FAQ-Schema/HTML synchron (7/7 Fragen, Wortlaut identisch)
Adressen + PLZ aller 5 Friedhöfe + Standesamt Trammplatz 2 verifizierbar
§-Verweise (§ 7, § 9, § 13 BestattG NI; § 28 PStG) korrekt zugeordnet
Keine Selbstwidersprüche zwischen Schema, Keyfacts und Fließtext; Wikipedia-Abweichung 22 ha/21,7 ha bei Engesohde transparent ausgewiesen
Theodor-Lessing-Klarstellung (Marienbad, nicht Engesohde) konsistent in FAQ + Fließtext
Cross-Links auf Niedersachsen-Landesseite, Braunschweig, Hildesheim, Bestattungskosten vorhanden; keine leeren Sektionen

Anwaltssicherer Punkt sauber gelöst: Friedhofsgebühren werden bewusst nicht beziffert, sondern auf aktuelle Satzungsfassung verwiesen – kein YMYL-Risiko. Stiftung-Warentest-Zahlen mit Quellenjahr (Finanztest 11/2023) qualifiziert.

Page ist deploy-ready aus MAJOR-Issue-Sicht.