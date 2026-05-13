Neuer Chat
Ctrl+⇧+O
Suchen
Ctrl+K
Chats
Projekte
Code
Anpassen
Design
Mehr
Zuletzt verwendet
Ausblenden
Osnabrück review und bewertung
Friedhöfe und Bestattungen in Leverkusen
Friedhöfe und Bestattungen in Hagen
Friedhöfe und Bestattungen in Leverkusen
Friedhöfe und Bestattungsgesetz in Mülheim an der Ruhr
Friedhöfe in Osnabrück recherchieren und schreiben
Friedhöfe und Bestattungen in Oberhausen
Oberhausen SCORE-Review und Fix-Liste
Erfurt v5 final adversarial score evaluation
Freiburg adversarial score evaluation v3
Hagen NRW Schwächen und Adversarial-Bewertung
HTML-Version mit Review-Fixes liefern
Chat C v5 Halle Adversarial Score Evaluation
Erfurt v5 final adversarial score evaluation
Erfurt v5 adversarial score evaluation
Hagen-Review nach SCORE-Tabelle
v4 HTML-Version mit Adversarial-Fixes
HTML-Version v4 mit Adversarial-Fixes
Freiburg Schwächen und adversariales Scoring
Friedhöfe und Bestattungen in Oberhausen
Friedhöfe und Bestattungen in Oberhausen
Hagen-Review nach SCORE-Tabelle
Chat C final adversarial recheck for Halle
Erfurt v4 adversarial score evaluation
Saarbrücken FINAL-Adv-Recheck v6 Bewertung
HTML-Version v6 mit BSG-Aktenzeichen-Fixes
HTML-Version mit Review-Fixes liefern
Chat C v3 Halle performance evaluation
Chemnitz v3 adversarial score evaluation
Friedhöfe und Bestattungen in Krefeld
Krefeld v3 adversarial score evaluation
Alle Chats
B
Bolle
Max Plan
Osnabrück review und bewertung
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/osnabrueck/v1-from-chat-A.html

Stadt: Osnabrueck (NDS). Review SCORE 0-100% + Fix-Liste.

11:42
Claude hat geantwortet: Ich lade v1 und reviewe sie.

Ich lade v1 und reviewe sie.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/osnabrueck/v1-from-chat-A.html

Ich reviewe v1 systematisch. Zuerst prüfe ich kritische Faktenbehauptungen gegen die Primärquellen.

Searching the web
Web durchsucht

Wichtige Befunde. Ich prüfe noch einige weitere kritische Fakten.

Searching the web
Web durchsucht

Wichtige Diskrepanz gefunden: Johannisfriedhof-Kapelle. v1 sagt "1874 begonnen, 1875 fertiggestellt" — Quelle sagt nur "1875". Außerdem: Letzte Beisetzungen 1995, aber Stadt-Quelle sagt für Johannisfriedhof "seit 1. Januar 1996 nicht mehr". Ich prüfe noch das Krematorium und Niedersächsisches Bestattungsgesetz Fristen.

Searching the web
Web durchsucht

Mehrere Diskrepanzen bestätigt. Eine letzte Prüfung: Standesamt-Adresse und Krematorium-Adresse.

Searching the web
Web durchsucht

Eine letzte kritische Faktenprüfung: Sterbeurkunde-Folgepreis (v1 sagt 7,50€, das wäre die Hälfte von 15€ — bestätigt durch Standesamt.com). NOW prüfe ich noch §-Verweise im Nds. BestattG (Sargpflicht §11, Krematorium §12, Fristen §9).

Searching the web
Web durchsucht

Wichtig: Seit 01.01.2019 lautet § 9 Abs. 2 Satz 4 nicht mehr "sollen", sondern "sind innerhalb eines Monats ... beizusetzen" (verschärft, verbindlich). Auch: Mindestruhezeit ist nach § 14 BestattG mindestens 20 Jahre - das v1 sagt "20 bis 25 Jahre üblich" – das stimmt für die Praxis, aber die Mindestpflicht ist 20.

Jetzt habe ich genug Material. Ich schreibe das Review.

REVIEW v1 Osnabrück (Chat B / Reviewer)
SCORE: 78/100

Verdict: Solide, gut recherchierte Hauptseite. Audit-Score-Niveau wahrscheinlich ≥85 erreichbar nach Fixes. Aber: 6 sachliche Blocker müssen vor Deploy korrigiert werden. Drei Falschangaben sind nicht nachsourcebar (Wettbewerb 1927, Kapelle 1874 begonnen, Geschoeller). Eine Behauptung widerspricht dem aktuellen Stand des Nds. BestattG (Urnenfrist).

🔴 BLOCKER (müssen weg)
#	Stelle	Fehler	Korrektur (mit Quelle)
B1	Heger Friedhof, Absatz 1	"Geplant nach 1. WK auf Grundlage eines städtischen Architektenwettbewerbs aus dem Juni 1927; die Eröffnung fand bereits 1925 statt, der Wettbewerb betraf vor allem die spätere bauliche Ausgestaltung."	Logisch inkonsistent. Der Architektenwettbewerb 1927 betraf die Trauerhalle/Krematorium (nicht "1925 eröffnete Friedhof"). Wikipedia: Wettbewerb 1927 → Entwurf "Campo Santo" → aber erst 1935 erneuter Wettbewerb, gewonnen von Springer/Lemke/Brinckmann (Hannover) → Einweihung Trauerhalle+Krematorium 10.10.1937. v1 hat hier zwei Wettbewerbe vermischt und 1936 als Errichtungsjahr behauptet. Fix: "Friedhof eröffnet 1925. Der Architektenwettbewerb für die Trauerhalle wurde 1927 ausgeschrieben (1. Preis: Spannmacher/Wende), tatsächlich umgesetzt wurde aber der Siegerentwurf eines zweiten Wettbewerbs 1935 (Springer, Lemke, Brinckmann, Hannover). Einweihung Trauerhalle und Krematorium am 10. Oktober 1937."
B2	Heger Friedhof, "Stille Sondersituation"	"Die ursprüngliche Anlage aus zwei Öfen wurde 1993–1995 um einen modernen Anbau mit zwei zusätzlichen Öfen ergänzt"	Falsch. Stadt Osnabrück: "ein neues Krematorium mit moderner Filtertechnik und zwei Öfen angebaut" — das war ein Ersatz des Originals, nicht eine Ergänzung. Die Anlage hatte danach nicht 4 Öfen, sondern weiterhin 2. Erst 2026 ging die dritte Ofenlinie in Betrieb (Quelle: staerkt.osnabrueck.de Februar 2026). Fix: "Anfang der 1990er Jahre wurde neben den ursprünglichen Anlage ein neues Krematorium mit moderner Filtertechnik und zwei Öfen angebaut; das alte System wurde dadurch ersetzt. 2008/2009 erfolgte eine Modernisierung wegen verschärfter Umweltauflagen, 2023 entstand ein weiterer Anbau für Kühl- und Untersuchungsräume. Anfang 2026 ging eine dritte Ofenlinie in Betrieb."
B3	Heger Friedhof, "Lage" Krematorium	"versorgt aufgrund seiner geographischen Lage auch das gesamte südliche Niedersachsen und Teile des angrenzenden Münsterlands"	Unsourced superlative / falsche Geografie. Osnabrück liegt im Westen Niedersachsens, nicht im Süden. Das Krematorium versorgt die Region NW-Niedersachsen + Münsterland. "Südliches Niedersachsen" wäre Göttingen/Hannover-Süd — die haben eigene Krematorien. Fix: Entweder Quelle bringen für "Versorgt Region X" oder streichen und nur sagen "ist das einzige Krematorium im Großraum Osnabrück".
B4	Johannisfriedhof, Absatz 2	"Die Friedhofskapelle aus Sandstein im Stil der Neugotik wurde 1874 nach Plänen des Maurermeisters Wilhelm Propfe begonnen und 1875 fertiggestellt."	Nicht sourcebar. Stadt-Quelle nennt nur "1875" als Errichtungsjahr; Wikipedia: "Kapelle aus dem Jahre 1875". Name "Propfe" und Jahr "1874" tauchen in keiner der bekannten Quellen auf. Fix: "Die Kapelle aus Sandstein im Stil der Neugotik wurde 1875 errichtet." (Architekt nur nennen, wenn Quelle verifiziert — sonst weglassen.)
B5	Rechtsabschnitt, § 9 Abs. 2 Satz 4	"Urnen müssen innerhalb eines Monats nach der Einäscherung beigesetzt werden."	Halb richtig, halb falsch. Bis 2018 war es eine "Soll-Vorschrift". Seit 01.01.2019 lautet die geltende Fassung: "Urnen sind innerhalb eines Monats nach der Einäscherung beizusetzen." Das ist eine verbindliche Pflicht, nicht nur eine "Soll-Vorschrift". Das nachfolgende OVG-Zitat von 2006 betrifft die alte Rechtslage und ist heute weniger einschlägig als der neue Wortlaut. Fix: Wortlaut zitieren ("sind ... beizusetzen", § 9 Abs. 2 Satz 4 BestattG i.d.F. seit 1.1.2019). Die OVG-Entscheidung von 2006 kann erwähnt bleiben als historische Abgrenzung.
B6	Prominente Bestattete Hasefriedhof	"Felix Hermann Maria Schoeller († 1907, Papierfabrikant)"	Unsourced / wahrscheinlich falsch. In den verifizierten Listen für den Hasefriedhof (Wikipedia, hasefriedhof-johannisfriedhof.de) taucht kein "Felix Hermann Maria Schoeller" auf. Die Familie Schoeller ist eine Düren-/Aachen-Familie; Felix Heinrich Schoeller († 1907) war Papierfabrikant in Düren, nicht in Osnabrück. Wahrscheinlich Verwechslung. Fix: Streichen.
🟡 MAJOR (sollten gefixt werden, blockieren aber nicht zwingend)
#	Stelle	Issue	Empfehlung
M1	Johannisfriedhof, Absatz 4	"Wie der Hasefriedhof wurde auch der Johannisfriedhof 1995 für aktive Beisetzungen geschlossen"	Stadt-Quelle: Beisetzungen auf Johannisfriedhof "bereits seit 1. Januar 1996 nicht mehr". Hasefriedhof: 1995. Differenzieren.
M2	Adresse Heger Friedhof Schema.org	streetAddress: "Rheiner Landstraße 168"	Krematorium-Anmeldung Stadt-Quelle: "Rheiner Landstraße 170". FAQ-Text in v1 verwendet auch 170. Schema.org & Hero-Box konsistent auf 170 setzen (oder verifizieren, welche Hausnummer offiziell ist — vermutlich 168 für Friedhofs-Haupteingang, 170 für Krematorium-Empfang).
M3	Reerdigung-Status	"Reerdigung ist in Niedersachsen derzeit gesetzlich nicht zulässig"	Stand 2026 prüfen: Seit der Bundestagsanhörung 2024 gibt es politische Bewegung. Aktuell (Mai 2026) trifft "in Niedersachsen nicht zugelassen" zu, aber Formulierung "Bislang hat ausschließlich Schleswig-Holstein eine Rechtsgrundlage geschaffen" sollte ggf. mit Datum versehen werden ("Stand Mai 2026").
M4	Hellern, Eröffnung	"1929 für die damalige Gemeinde Hellern eingerichtet" + "ca. 26.000 m²" + "Lengericher Landstraße"	1929 + 26.000m² ist bestätigt. Aber: Adresse "Lengericher Landstraße" ist nicht aus den verifizierten Quellen — bitte gegen offizielle Stadt-Adresse prüfen.
M5	Atter Friedhof Fläche	"ca. 8.000–10.000 m²"	Stadt-Quelle eindeutig: "rund 8.000 qm". Spanne ist falsch. Fix: "ca. 8.000 m²".
M6	UNSURE-Kommentar Dodeshaus	<!-- UNSURE: Detail zu konkretem Baumgrab-Angebot Dodeshaus aus den verfügbaren Quellen nicht eindeutig bestätigt -->	HTML-Kommentar in Output lassen ist OK für Review-Phase, muss aber vor Deploy raus. Stattdessen Aussage präziser machen oder streichen.
M7	Story-Tag Hasefriedhof	Erwähnung "adventure-hasefriedhof.de" als Hidden Gem	Verifiziert (existiert), aber: WebApp ist laut eigener Aussage "in Testphase". Eventuell Hinweis "(Stand 2025/2026 noch in Testphase)" ergänzen oder Erwähnung weniger werbend gestalten.
M8	Doppelung "Quadratmeter"	"270.000 Quadratmetern" mehrfach im Heger-Absatz wiederholt	Stilistisch: einmal in den Kernfakten, einmal im Fließtext reicht.
🟢 MINOR (Polish)
#	Stelle	Hinweis
N1	FAQ Anonyme Bestattung	Antwort sagt "übrigen sieben kommunalen Friedhöfen" — bei 8 aktiven minus Heger = 7. Stimmt. ✓
N2	Tabelle Kosten	Untergrenze Urnengrab 990€ + Sarggrab 1.220€ konsistent zu Lead. ✓ Aber: keine direkte Quelle in der Tabellenfußnote. "Stand 2026" + Verweis auf Friedhofsgebührensatzung 9.12.2025 ist ok, müsste aber präziser sein wenn jemand nachfragt: "ungefähre Spannen basierend auf typischer Bandbreite vergleichbarer Kommunen in Niedersachsen — verbindlich ist die Gebührensatzung der Stadt."
N3	Kernfakten	"Friedhofsgebührensatzung vom 9. Dezember 2025" — diese spezifische Behauptung sollte gegen das Osnabrücker Ortsrecht verifizierbar sein. Wenn nicht direkt verifizierbar, dann weicher formulieren ("aktuell gültige Friedhofsgebührensatzung der Stadt").
N4	Ablauf-Liste Schritt 2	"§ 8 Abs. 3 BestattG (Ehe-/Lebenspartner, volljährige Kinder, Eltern, …)" — verifizieren gegen aktuelles Nds. BestattG, da die Reihenfolge der Bestattungspflichtigen länderspezifisch variiert.
N5	Doppelte Trauerhalle-Erwähnung	Heger Friedhof: "rund 30 Trauergäste" für alte Kapelle — Stadt-Quelle bestätigt "etwa 30". Stadt-Quelle erwähnt auch "12 Sitzplätze" Verabschiedungsraum (2006), das fehlt in v1. Nice-to-have.
N6	OG-Bild & Twitter Card	Schema.org gut, aber <meta property="og:image"> fehlt. Wenn machsruhig.de generisches OG-Bild hat, hinzufügen für Social-Sharing.
N7	Sitemap-/Hreflang-Tag	<link rel="canonical"> ist da. Gut. Kein hreflang nötig, da nur DE. ✓
N8	Headlines-Hierarchie	Eine <h2> (Kernfakten) in <aside> ist semantisch grenzwertig. Wenn Audit-Tool strict ist, könnte das einen Punktabzug geben. Alternative: <h3> in der aside-Box.
📋 ZUSAMMENFASSUNG für Chat A

Pflicht-Fixes (B1–B6):

Wettbewerb 1927 vs. 1935 + Einweihung 10.10.1937 trennen
Krematorium: 1993–95 Ersatz nicht Ergänzung, 3. Ofenlinie erst 2026
"Südliches Niedersachsen" → "Region Osnabrück" (oder Quelle)
Johannisfriedhof-Kapelle: nur 1875, kein "Propfe"
Urnenfrist § 9 Abs. 2 S. 4 BestattG aktuelle Fassung ("sind … beizusetzen")
Schoeller streichen

Sollte zusätzlich (M1, M2, M5):

Johannisfriedhof letzte Beisetzung 1996 (nicht 1995)
Hausnummer Heger (168 vs. 170) konsistent
Atter ca. 8.000 m² (nicht Spanne)
HTML-UNSURE-Kommentar raus

Erwartung nach Fix: Audit-Score ≥85 sehr wahrscheinlich. Honesty-Recheck-Blocker werden insbesondere B1 und B6 sein (template error + unsourced person).

Gut gemacht:

Recht-Block mit echten §-Verweisen, OVG-Zitat
"Neues Leben zwischen alten Gräbern" + finnische Jäger als echte Hidden Gems (verifiziert)
Kostenstruktur differenziert (Spanne nicht Punktwerte)
Quellen-Block sauber, Schema.org sauber
Lokalkolorit (Möser/napoleonisches Dekret 1804) ist historisch korrekt

Bereit für v2.

Dein Nutzungsguthaben ist aufgebraucht. Kaufe mehr, um jetzt weiterzumachen, oder warte bis Donnerstag um 14:00, wenn sich deine Plan-Nutzung zurücksetzt.
Mehr kaufen




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
 Claude is active in this tab group  
Open chat
 
Dismiss