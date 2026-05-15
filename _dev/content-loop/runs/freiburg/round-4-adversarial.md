Ich lade die drei Dateien.

Fetching site
Web durchsucht

Drei Dateien gelesen. Briefing-Mindset: Annahme = Page hat mindestens 3 Schwächen. Ich gehe die 12 Kategorien durch und prüfe gezielt, ob v2 die v1-Kritik wirklich behoben hat oder ob neue Schwächen entstanden sind.

Kritische Prüfpunkte v1→v2:

v1-Kritik §§20 ff. für Leichenschau: v2 zitiert weiterhin §§ 20–22 BestattG BW für Leichenschau. Das war der zentrale §-Fehler der v1-Review. Prüfung: BestattG BW (vom 21.7.1970) — Leichenschau ist in BW im § 5 BestattG BW geregelt (Pflicht, Veranlassung, Durchführung). § 20 betrifft Bestattungseinrichtungen / Friedhofsträger. v2 hat den §-Fehler aus v1 nicht korrigiert, sondern doppelt belegt: in der <ul> der Sektion, in der FAQ, im JSON-LD und in der Hero. Das ist ein Halluzinations-/Faktenfehler quer durch die Page.
v1-Kritik § 31 Reihenfolge (Großeltern vor Geschwistern): v2 hat das identisch übernommen: „Ehegatte/Lebenspartner, volljährige Kinder, Eltern, Großeltern, volljährige Geschwister, Enkel". Originaltext § 31 BestattG BW reiht Geschwister vor Großeltern. Faktenfehler weiterhin drin.
v1-Kritik „kürzere Ruhezeit wegen günstiger Bodenverhältnisse": v2 hat den unbelegten Begründungssatz entfernt — gut.
v1-Kritik Leutwein unkommentiert: v2 hat ausführliche Einordnung ergänzt — sauber gelöst.
v1-Kritik UNSURE-Kommentar Max Meckel: in v2 nicht mehr vorhanden — gut.
Footer München-Link: in v2 nicht vorhanden, Cross-Cluster zeigt korrekt auf BW-Städte — gut.
Bestatter-Sektion: v2 begründet explizit die Nicht-Nennung („keine namentlichen Empfehlungen") und liefert Qualitätsindikatoren — vertretbar gelöst, nicht mehr dünn.

Weitere Funde:

Stiftung Warentest 7.000–8.000 €: v2 schreibt jetzt „laufend aktualisierter Ratgeber" statt Jahresangabe. Das ist eine Verschleierung, kein Beleg. Konkrete Stiftung-Warentest-Ratgeber haben Stand-Datum. Wenn beim Klick auf den Link kein Betrag in dieser Spanne erscheint, ist die Aussage nicht belegt.
JSON-LD Cemetery als additionalType: "additionalType":"https://schema.org/Cemetery" ist semantisch unscharf. Es gibt schema.org/Cemetery nicht als ratifizierten Type — das ist eine erfundene URL. Validatoren werden das ignorieren oder als Warnung melden. Statt additionalType mit nicht-existierender URL sollte der Place ohne diesen Pseudo-Type stehen, oder als LandmarksOrHistoricalBuildings/Place mit keywords.
JSON-LD City als Type: schema.org/City existiert nicht; korrekt wäre Place mit address oder AdministrativeArea. Zweiter Schema-Validierungsfehler.
Maßeinheit „Ar": „82,61 Ar" für Jüdischen Friedhof ist eine ungewöhnliche, fast antiquierte Einheit (1 Ar = 100 m²). Für Verständlichkeit sollte die Umrechnung in m² oder ha mitgegeben werden (0,83 ha bzw. 8.261 m²). Sonst Stolperstein für Leser.
Bombenangriff 10. Mai 1940: v2 hat einen Quellenanker („Stadtarchiv Freiburg sowie Kalchthaler 1997") ergänzt — gut. Aber: Die Sektion zum Gräberfeld der Fliegerangriff-Toten ist sehr lang (Engelmann-Figur, Schneider-Inschrift, Zimber-Neugestaltung, Datum 27. November 1958, OB Brandel) und entfernt sich vom Page-Thema „Bestattung in Freiburg" Richtung Friedhofs-Geschichts-Essay. YMYL-Fokus leidet.

Jetzt die drei substantiellen Schwächen pro Briefing-Format:

SCHWÄCHE 1 (Halluzinations-Verdacht / falscher §):
Stelle: Sektion „Bestattungsrecht — der kurze Überblick mit Paragraphen", erster Bullet
("§§ 20–22 BestattG BW — Leichenschau"), gleicher Fehler in FAQ-Antwort 3 und im 
JSON-LD FAQPage. Außerdem in der ersten Hauptsektion Sektion "Was nach einem Todesfall 
zu tun ist", Punkt 1.
Problem: In BestattG BW (21.7.1970) wird die ärztliche Leichenschau in § 5 geregelt 
(Leichenschaupflicht, Veranlassung, Vornahme), nicht in §§ 20–22. §§ 20 ff. regeln 
andere Materie (Friedhofsträger/Bestattungseinrichtungen). Diese §-Verwechslung war 
bereits in der v1-Review als Honesty-Check-Blocker markiert, ist in v2 unverändert
drin und jetzt sogar dreifach verankert (Body + FAQ + Schema). Das ist der schwerste 
Fund und blockt go-live.
Verbesserung: Vor jedem weiteren Schritt §§ im Volltext des BestattG BW gegenprüfen 
(Landesrecht-BW-Link ist bereits in den Quellen) und § 5 BestattG BW exakt zitieren. 
Alle vier Vorkommen (Sektion 1, Sektion „Was zu tun ist", FAQ-Antwort 3, JSON-LD 
FAQPage) synchron korrigieren. Re-Check-Script vorher mit aktualisierter 
§-Whitelist laufen lassen.

SCHWÄCHE 2 (Halluzinations-Verdacht / Reihenfolge §31):
Stelle: Sektion „Bestattungsrecht", Bullet zu § 31 BestattG BW
("Reihenfolge der Angehörigen (Ehegatte/Lebenspartner, volljährige Kinder, Eltern, 
Großeltern, volljährige Geschwister, Enkel)") und identisch in Sektion 
„Was nach einem Todesfall zu tun ist", Punkt 1.
Problem: Die Reihenfolge nach § 31 BestattG BW reiht Geschwister vor Großeltern. 
Die Page führt Großeltern vor Geschwistern — gleicher Fehler wie in v1, in v2 
nicht behoben. Damit hat die Page zwei §-Fehler in derselben Sektion, beide bereits 
in v1 markiert, beide übernommen. Bei YMYL-Themen ist eine falsche 
Bestattungspflichtigen-Reihenfolge praxisrelevant — Angehörige könnten daraus 
falsche Rechtsfolgen ableiten.
Verbesserung: § 31 BestattG BW Volltext laden, exakte Reihenfolge einfügen 
(Ehegatte/eingetragener Lebenspartner, Kinder, Eltern, Geschwister, Großeltern, 
Enkel — Original-Wortlaut gegenprüfen, inkl. Volljährigkeitsbedingung exakt 
übernehmen). Beide Stellen synchron korrigieren.

SCHWÄCHE 3 (Schema.org-Fehler mit Pseudo-URLs):
Stelle: JSON-LD im <head>, vier Place-Einträge mit 
"additionalType":"https://schema.org/Cemetery" sowie der "City"-Eintrag 
("@type":"City").
Problem: schema.org/Cemetery existiert nicht als ratifizierter Type — das ist 
eine konstruierte URL, die kein Schema-Validator als gültiges additionalType 
akzeptiert. Gleiches gilt für "@type":"City" — schema.org kennt nur Place, 
LocalBusiness, AdministrativeArea, GovernmentBuilding etc., aber keinen 
City-Type. Beide Pseudo-Types sind in der Rich-Result-/Schema-Validation 
Warnungen oder Ignorierungen und untergraben den SEO-Vorteil, den das 
Schema-Markup leisten soll. Da das Briefing explizit Schema.org als 
Qualitätskriterium nennt und v2 hier ambitioniert vorgeht, fällt der Fehler 
besonders ins Gewicht.
Verbesserung: "@type":"City" ersetzen durch "@type":"Place" oder 
"AdministrativeArea". "additionalType":"https://schema.org/Cemetery" 
entfernen, stattdessen z. B. Place mit "keywords":"Friedhof, Cemetery" oder 
"@type":"LandmarksOrHistoricalBuildings" — auf jeden Fall keine 
nicht-existenten Schema-URLs konstruieren. Anschließend via Google 
Rich-Results-Test und schema.org/validator durchlaufen lassen.

EHRLICHE %-ZAHL: 71%

SCORE: 71/100

FUNDE:

Leichenschau-§§ falsch (§§ 20–22 statt § 5 BestattG BW) — 4× im Dokument, war v1-Blocker, in v2 unverändert.
§ 31 Reihenfolge falsch (Großeltern vor Geschwistern) — 2× im Dokument, war v1-Blocker, in v2 unverändert.
Schema.org-Markup nutzt nicht-existente Types (City) und Pseudo-URL-additionalType (schema.org/Cemetery).
Stiftung-Warentest-Zahl ohne konkretes Stand-Datum (v1-Kritik nur kosmetisch entschärft).
Maßeinheit „82,61 Ar" ohne Umrechnung für durchschnittlichen Leser unverständlich.
Gräberfeld-Fliegerangriff-Sektion driftet von Bestattungsthema in Friedhofsgeschichte ab (Länge unverhältnismäßig).

Positiv (nicht Teil der Schwächen, aber zur Einordnung): Leutwein-Kontext, UNSURE-Kommentar weg, Footer-München-Link weg, Bestatter-Sektions-Begründung, Bombenangriff-Quelle — alle behoben.

MUST-FIX vor Deploy: ja.

Die beiden §-Fehler (Schwäche 1 + 2) sind YMYL-Halluzinationen, die das Re-Check-Script per Definition blocken müssen. Das Schema.org-Problem (Schwäche 3) ist kein Honesty-Blocker, aber technisch falsch und sollte im selben Zug mitfixiert werden. Ohne Korrektur ist die Page nicht go-live-fähig — gleicher Grund wie nach v1.