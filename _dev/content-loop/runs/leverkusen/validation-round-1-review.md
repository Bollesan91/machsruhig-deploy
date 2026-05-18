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
Leverkusen Bestatter-Seite Review
Krematorium Heidelberg: Re-Review der 4 Major-Funde
FAQ-Schema Validierung für Halle Bestatter
Schalker Fan-Feld Daten-Review für Gelsenkirchen
FAQ-Schema Überprüfung für Erfurt
Krematorium Heidelberg: Re-Review der Major-Funde
Halle (Saale) Bestatter-Seite Review
Heidelberg Stadt-Page Review für machsruhig.de
Erfurt Stadt-Page Review für machsruhig.de
Freiburg Stadt-Page Review für machsruhig.de
Gelsenkirchen Stadt-Page Review für machsruhig.de
Halle (Saale) Bestatter-Seite Review
Heidelberg Stadt-Page Review für machsruhig.de
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
Re-Review Frankfurt Friedhof und Bestattungsrecht
Rostock Bestatter Review auf machsruhig.de
Magdeburg Bestatter Review - Qualitätskontrolle
Re-Review Rostock: Major-Funde Überprüfung
Magdeburg-Überprüfung: MAJOR-Funde validieren
Überprüfung der Köln-Seite auf behobene Major-Fehler
Potsdam-Friedhof: Überprüfung der MUST-FIX-Korrektionen
Alle Chats
B
Bolle
Max Plan
Leverkusen Bestatter-Seite Review
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetche die Live-Version und prüfe systematisch auf MAJOR-Issues.

Ich fetche die Live-Version und prüfe systematisch auf MAJOR-Issues.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/leverkusen/index.html?cb=1779110750301

Ich prüfe systematisch auf MAJOR-Issues. Drei Punkte fallen auf, die ich verifizieren muss:

§ 7 Abs. 2 BestG NRW als Sargpflicht-Verweis — das ist die kritische Paragraphen-Referenz
Volksbund-Link: "Waldfriedhof" — Reuschenberg ist Friedhof, nicht Waldfriedhof
Kriegstote Reuschenberg: "acht deutsche" — Volksbund-Daten prüfen
Web durchsucht
Web durchsucht

Bestätigung der MAJOR-Issues abgeschlossen:

§ 7 BestG NRW = "Totenwürde, Gesundheitsschutz" — regelt KEINE Sargpflicht/Tuchbestattung. Satzungs-Ermächtigung steht in § 4. Damit ist die FAQ-Aussage "Friedhofssatzung nach § 7 Abs. 2 BestG NRW" eine falsche Paragraph-Referenz — und § 7 Abs. 2 regelt "Berücksichtigung des Empfindens der Glaubensgemeinschaft", nicht Tuchbestattung-Satzungsbefugnis.
§ 12 Abs. 1, § 14 Abs. 1, § 15 Abs. 5 BestG NRW als Friedhofszwang-Verweis: § 12 ist "Bestattungsentscheidung" (Erd/Feuer) — kein Friedhofszwang. § 14 Abs. 1 = Erdbestattung auf Friedhof ✓. § 15 Abs. 5 = Aschen auf Friedhof/See ✓. Der § 12 Abs. 1-Verweis ist falsch — richtig wäre § 1 Abs. 1 (Gewährleistungsauftrag der Gemeinden, Bezug zu Friedhof).
Rangfolge Bestattungspflichtige § 8 Abs. 1: HTML erwähnt § 8 nur in der Bestatter-Schritt-Liste-Verweisung — keine explizite Reihenfolge zur Prüfung. Skip.
Volksbund-Eintrag: HTML zitiert "Leverkusen-Reuschenberg-Waldfriedhof". Im Text steht "Kriegsgräberstätte mit acht deutschen Kriegstoten". Zahl unbestätigt, aber nicht eindeutig falsch — skip als MAJOR.
FAQ-Schema vs HTML-FAQ: Identisch (beides 7 Fragen, gleicher Wortlaut). ✓
Cross-Links: /bestattung-in/nordrhein-westfalen/, /bestatter/, /vorsorge/, /ratgeber/ — Standard-Sitemap-Pfade, nicht prüfbar ohne Live-Site. Skip.
Selbstwiderspruch Manfort: "größte Friedhofsanlage" + gleichzeitig "seit Ende der 1980er weitgehend geschlossen für neue Sargbestattungen" — kein Widerspruch, aber spannungsreich. Skip.

STADT: Leverkusen
VERDICT: PASS mit 2 MAJOR

Fund 1: Falsche Paragraph-Referenz (Sargpflicht/Tuchbestattung) Wo: FAQ "Gilt in Leverkusen eine Sargpflicht?" + HTML-Recht-Sektion implizit Was: Verweis auf "§ 7 Abs. 2 BestG NRW" als Rechtsgrundlage für Satzungsregelung zu Tuchbestattungen. § 7 BestG NRW regelt "Totenwürde, Gesundheitsschutz" (Abs. 2 = Glaubensgemeinschaftsberücksichtigung), NICHT Satzungsbefugnis. Die Satzungsermächtigung steht in § 4 BestG NRW. Fix: Ersetze "nach § 7 Abs. 2 BestG NRW" durch "nach § 4 Abs. 1 BestG NRW" (Satzungsregelung von Art, Umfang und Durchführung der Bestattung).

Fund 2: Falsche Paragraph-Referenz (Friedhofszwang) Wo: Recht-Sektion, Absatz 2: "Nach § 12 Abs. 1, § 14 Abs. 1 und § 15 Abs. 5 BestG NRW müssen Leichen auf einem Friedhof beigesetzt werden, Urnen auf einem Friedhof oder auf See." Was: § 12 Abs. 1 regelt die Bestattungsentscheidung (Erd- vs. Feuerbestattung, Wille der Verstorbenen) — NICHT den Friedhofszwang. Korrekte Grundlage für den Gewährleistungsauftrag ist § 1 Abs. 1 BestG NRW. Fix: Ersetze "§ 12 Abs. 1" durch "§ 1 Abs. 1" — § 14 Abs. 1 (Leichen) und § 15 Abs. 5 (Aschen) bleiben korrekt.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen