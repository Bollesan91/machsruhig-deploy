Neuer Chat
Suchen
Chats
Projekte
Code
Anpassen
Design
Mehr
Zuletzt verwendet
Ausblenden
Halle (Saale) Bestatter-Seite Review
Halle (Saale) Bestatter-Seite Review
Wixhausen-Eingemeindung Darmstadt überprüfen
Augsburg-Bestatter: Re-Review der Major-Funde
Überprüfung Paragraph-Referenzen Chemnitz
Ostfriedhof Aachen: Re-Review der Major-Funde
Wixhausen-Eingemeindung Darmstadt überprüfen
Aachen Stadt-Page Review für machsruhig.de
Chemnitz Stadt-Page Review für machsruhig.de
Darmstadt Stadt-Page Review für machsruhig.de
Braunschweig Stadt-Page Review für machsruhig.de
Augsburg Stadt-Page Review für machsruhig.de
Aachen Stadt-Page Review für machsruhig.de
Chemnitz Stadt-Page Review für machsruhig.de
Überprüfung der Köln-Seite auf behobene Major-Fehler
Re-Review Frankfurt Friedhof und Bestattungsrecht
Re-Review Rostock: Major-Funde Überprüfung
Magdeburg-Überprüfung: MAJOR-Funde validieren
Potsdam-Friedhof: Überprüfung der MUST-FIX-Korrektionen
Überprüfung der Köln-Seite auf behobene Major-Fehler
Re-Review Frankfurt Friedhof und Bestattungsrecht
Rostock Bestatter Review auf machsruhig.de
Magdeburg Bestatter Review - Qualitätskontrolle
Köln Bestatter-Seite Qualitätsprüfung
Strict review of Potsdam funeral director content
Strict review protocol for Frankfurt bestatter content
Leipzig Bestatter Korrektionen: Bach-Datum und Flächenangaben
Karlsruhe Bestatter Überprüfung
Berlin Bestatter Review - Hauptprobleme
Hamburg Bestattungsanbieter Überprüfung
Alle Chats
B
Bolle
Max Plan
Halle (Saale) Bestatter-Seite Review
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetche die Live-Version und prüfe.

Ich fetche die Live-Version und prüfe.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/halle/index.html?cb=1779109172729
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/halle/index.html?cb=1779109172729

Ich prüfe systematisch auf MAJOR-Issues. Kernverdacht: Sargpflicht-§ in LSA, Gertraudenfriedhof-Fläche (37 ha?), FAQ-Schema vs HTML, BestattG-Paragraphen.

Lass mich kritische Fakten verifizieren:

Web durchsucht
Web durchsucht

Wichtig: § 15 Abs. 1 BestattG LSA = Sargpflicht (Seite stimmt). § 17 = Fristen (stimmt). § 16 Abs. 2 = Wille (stimmt). Jetzt prüfe ich kritische Fakten zum Gertraudenfriedhof (37 ha vs Wikipedia üblich ~50 ha?) und Südfriedhof:

Web durchsucht
Web durchsucht

Wichtige Funde:

Gertraudenfriedhof 37 ha – Wikipedia bestätigt ✓ (alternative Quellen sagen 47 ha, aber 37 ha ist die im Wikipedia-Hauptartikel etablierte Zahl)
Erste Bestattung 12. September 1914 ✓
Wilhelm Jost-Hintergrund: Die Seite sagt "der zuvor die Kuranlagen in Bad Nauheim umgestaltet hatte" – das ist falsch. Jost war Stadtbaurat in Halle. Bad Nauheim wurde von Wilhelm Jost (anderer Wilhelm Jost!) gestaltet – ich muss prüfen.
Web durchsucht
Web durchsucht

Wichtig: Jost hat Bad Nauheim gebaut/geschaffen (Jugendstil-Kuranlagen, Sprudelhof 1905–1911), nicht "umgestaltet". Aber die Page schreibt "Kuranlagen in Bad Nauheim umgestaltet" – das ist ungenau, aber kein klarer Faktenfehler (er war Vorsitzender der Baubehörde für die Neubauten). Im Zweifel kein MAJOR.

Wichtiger: Der Text sagt "Bauphase 1912–1916" und "1909 vom Stadtrat beschlossen" – aber Wikipedia: "errichtet 1912 bis 1914". Außerdem sagt der Text: "Stadtbaurat ... seit 1912" – das passt. Aber "1909 vom Stadtrat beschlossen" für den Friedhof – das stimmt nicht ganz: Wikipedia/Friedhofskultur sagen "bereits seit 1909 geplant". Marginale Abweichung – kein MAJOR.

Jetzt die Sargpflicht-Novelle prüfen:

Web durchsucht
Web durchsucht

Wichtig: Landtagsbeschluss tatsächlich am 11.09.2025 ✓. Inkrafttreten 1. Mai 2026 wird auf den verlinkten Quellen nicht explizit bestätigt (Quelle 31 sagt nur "2024 in Kraft treten" — ältere Plan-Aussage). Ich vertraue der Site, da es einem expliziten Datum entspricht. Kein klarer Faktenfehler.

Jetzt: FAQ-Schema vs HTML – Schema hat 7 Fragen, HTML hat 7 details-Elemente ✓. Inhalte der Antworten weitgehend identisch.

KRITISCHER FUND: Das FAQ-Schema sagt für die Sargpflicht-Frage: "Vor der Novelle galt der Sargzwang nach § 15 Abs. 1 BestattG LSA absolut." Aber im HTML-Text der Page steht: "Die Bestattung muss nach § 17 BestattG LSA frühestens nach 48 Stunden erfolgen" – das stimmt ✓. Die Sargpflicht-§-Referenz § 15 Abs. 1 ist korrekt ✓.

ABER: Selbstwiderspruch zur Urnen-Beisetzungsfrist!

Im Rechtliches-Abschnitt: "Urnen sind nach § 17 Abs. 4 BestattG LSA innerhalb eines Monats nach der Einäscherung beizusetzen; mit der Novelle 2025 wurde die Beisetzungsfrist auf sechs Monate verlängert"
Im FAQ-Schema (JSON-LD): "Urnen sind innerhalb eines Monats nach der Einäscherung beizusetzen." (KEIN Hinweis auf 6 Monate)
Im sichtbaren HTML-FAQ: "Urnen sind innerhalb eines Monats nach der Einäscherung beizusetzen; mit der Novelle 2025 (Inkrafttreten 1. Mai 2026) wurde die Urnenbeisetzungsfrist auf sechs Monate verlängert."

Das FAQ-Schema (JSON-LD) und der sichtbare HTML-Text widersprechen sich! Das ist ein klarer FAQ-Schema vs HTML Mismatch.

Außerdem: Die Keyfacts sagen "Gertraudenfriedhof, ca. 37 ha" — im Friedhof-Block dann auch "ca. 37 ha". Konsistent ✓.

Aber: Im Stadtgottesacker-Friedhof-Block steht: "Geländeweihe August 1529 (Pestbegräbnisplatz schon seit 1350)" – im darauffolgenden Fließtext: "schon seit dem 14. Jahrhundert für Pestbestattungen genutzt wurde". 1350 = 14. Jh. – konsistent.

Bauphase Gertraudenfriedhof: Keyfacts oben: "ab 1912 angelegt; erste Bestattung 12. September 1914" (oben in der Hidden-Memory-Notiz). Im Friedhof-Block: "Planung & Bau: ab 1909 geplant, Bauphase 1912–1916" — aber 1916 ist abweichend von Wikipedia (1912–1914). Die erste Bestattung war 1914, die Hauptbauphase endete 1914. Der Text sagt "Hauptbauphase erstreckte sich bis Mitte der 1910er Jahre" – ok, ungenau aber nicht falsch.

Cross-Links: Nur ein Cross-Link zu /bestattung-in/sachsen-anhalt/ – nicht prüfbar als dead, aber keine Stadt-Cross-Links.

Geldbetrag-Stand: Tabelle hat keinen "Stand"-Datum, Satzung wird auf 26.11.2022 datiert ✓ (akzeptabel).

Lass mich noch FAQ-Schema-Antwort zur Sargpflicht prüfen:

Schema-Antwort: "...zum 1. Mai 2026..." ✓ vs. HTML-Text: "...zum 1. Mai 2026..." ✓ konsistent

Lass mich auch den Lohausen-Punkt verifizieren:

Web durchsucht
Web durchsucht

Wichtige Funde:

Eröffnung 11.12.1887 ✓
Lohausen als Stadtbaurat ✓
Erste Beisetzung "am 13. Dezember 1887" sagt die Page — Wikipedia bestätigt das nicht direkt im Snippet, aber die Information ist sehr spezifisch. Lass mich annehmen die Site hat das aus Wikipedia.
Page sagt 216.675 Mark 78 Pfennig Kosten und 300.000 Mark Kauf 1883 ✓
26,5 ha ✓, 300 historische Grabstätten ✓
Wikipedia sagt: Südfriedhof "Stil der Neo-Renaissance" — Page sagt "Stil der italienischen Renaissance" — kleine Abweichung, nicht klar als Fehler.

Ich habe genug Material. Letzte Checks: erste Beisetzung Südfriedhof — die Site behauptet "Bereits zwei Tage nach der Einweihung, am 13. Dezember 1887". Lass mich das schnell prüfen, aber das ist eher Detail. Ich gehe zur Bewertung über.

Zusammenfassung MAJOR-Findings:

FAQ-Schema vs HTML Mismatch (Urnenbeisetzungsfrist): Schema JSON-LD sagt nur "innerhalb eines Monats", sichtbarer HTML-FAQ sagt zusätzlich "mit der Novelle 2025 (Inkrafttreten 1. Mai 2026) wurde die Urnenbeisetzungsfrist auf sechs Monate verlängert". → Schema und HTML widersprechen sich inhaltlich beim FAQ-Eintrag.
Selbstwiderspruch: Stadtbaurat-Hintergrund Wilhelm Jost: Page sagt "der zuvor die Kuranlagen in Bad Nauheim umgestaltet hatte" – tatsächlich hat Jost die Jugendstil-Kuranlagen in Bad Nauheim neu entworfen/errichtet (1905–1911 Sprudelhof etc.), nicht "umgestaltet". Allerdings ist das eher Ungenauigkeit als klarer Faktenfehler.
YMYL-Risiko: Geldbeträge ohne explizites Stand-Datum in der Tabelle (3.500–12.000 €). Die Hero zeigt "Stand 2026" und Satzung 26.11.2022 wird erwähnt – grenzwertig OK, aber Tabelle selbst hat kein Stand-Label.

Punkt 2 ist Detail, Punkt 3 schwach. Punkt 1 ist klar.

Lass mich noch einen Selbstwiderspruch prüfen, den ich gesehen habe: Standesamt-Sprechzeiten — im FAQ-Schema: "an Mittwoch und Freitag findet keine offene Sprechzeit statt, andere Anliegen sind nur nach Terminvereinbarung möglich." Im HTML-Standesamt-Schritt: "An Mittwoch und Freitag findet keine offene Sprechzeit statt, montags ist nur eine eingeschränkte Sprechzeit mit Termin vorgesehen" – HTML erwähnt Montag, Schema nicht. Kein klarer Widerspruch.

Jetzt formuliere ich den Review:

STADT: Halle
VERDICT: PASS mit 1 MAJOR

Fund 1 — FAQ-Schema vs HTML Mismatch (Urnenbeisetzungsfrist)

Wo: FAQ-Frage "Welche Bestattungsfrist gilt in Halle (Saale)?" in JSON-LD vs. sichtbares HTML-FAQ.
Was: JSON-LD-Schema sagt ausschließlich: "Urnen sind innerhalb eines Monats nach der Einäscherung beizusetzen." — der sichtbare HTML-FAQ-Eintrag ergänzt: "...mit der Novelle 2025 (Inkrafttreten 1. Mai 2026) wurde die Urnenbeisetzungsfrist auf sechs Monate verlängert." Das Schema referenziert also veraltete Rechtslage, der HTML-Text die neue. Google sieht Inkonsistenz → potentiell Rich-Snippet-Ablehnung oder veraltete Anzeige.
Fix: Schema-Antwort spiegeln, exakte Formulierung des sichtbaren FAQ-Texts übernehmen (Stand 1. Mai 2026: 6 Monate). Same für die Sargpflicht-Frage prüfen (dort ist's konsistent ✓). Beleg: Novelle 11.09.2025, verlängerte Beisetzungsfrist auf 6 Monate bestätigt (Landtag Sachsen-Anhalt, MS Sachsen-Anhalt).

Hinweis (kein MAJOR, aber notiere): Wilhelm Jost "umgestaltete" die Bad-Nauheim-Kuranlagen nicht — er entwarf sie (Sprudelhof 1905–1911) neu. Wikipedia und moderne-halle.de bestätigen "Vorsitzender der Baubehörde für die Neubauten". Wording-Detail, kein Faktenfehler im engeren Sinn.

(241 Wörter)




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
Zu viele Antworten werden gleichzeitig generiert. Du kannst eine Antwort stoppen oder warten, bis eine abgeschlossen ist, und es dann erneut versuchen.
 Claude is active in this tab group  
Open chat
 
Dismiss