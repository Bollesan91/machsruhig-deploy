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
Kassel Stadt-Page Review für machsruhig.de
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
Kassel Stadt-Page Review für machsruhig.de
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetch die Live-Version und prüfe.

Ich fetch die Live-Version und prüfe.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/kassel/index.html?cb=1779110750012
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/kassel/index.html?cb=1779110750012

Ich prüfe die kritischen Punkte. FAQ-Schema vs HTML-FAQ: Beide haben 8 Fragen — match. Paragraphen: § 16 FBG (Bestattungsfristen), § 30 FBG (kirchliche Träger), § 17 FBG (Sargpflicht), § 10 FBG (Leichenschau), § 13 FBG (Bestattungspflicht), § 20 Abs. 3 FBG (Friedhofszwang Urnen) — das sind die hessischen FBG-Nummern, plausibel. § 28 PStG korrekt.

Selbstwiderspruch: Tabelle "Friedpark-Wahlgrabstätte 30 J, 1 Stelle = 4.032 €" UND "Parkartige Wahlgrabstätte Abt. 6+11, doppelte Grundfläche = 4.032 €" — beide Ziffer 1.2, identischer Preis bei unterschiedlicher Fläche. Verdächtig, aber ohne Satzungstext nicht hart verifizierbar → UNSURE → nicht melden.

Faktencheck: Hauptfriedhof eröffnet 1843 ✓. Ludwig Emil Grimm 1790–1863 ✓. Scheidemann 1865–1939 ✓. Arnold Bode 1900–1977 ✓. Spohr 1784–1859 ✓.

Cross-Links: /bestatter/frankfurt/, /wiesbaden/, /darmstadt/, /offenbach/ — keine Möglichkeit zu prüfen ohne Repo-Check.

Web durchsucht
Web durchsucht

Cross-Links nicht testbar — als UNSURE behandeln, nicht melden.

Echter Fund: Keyfacts sagt "Friedhofssatzung 9.06.08, Beschluss 13.12.2024, geltend ab 12.04.2025; zweite Fassung beschlossen 22.08.2025". Quelle 2 sagt aber: "Satzung … in der Fassung der Änderung vom 13. Dezember 2024, geltend ab 12. April 2025" — KEINE zweite Fassung 22.08.2025 erwähnt. Die 22.08.2025-Änderung gehört zur Gebührensatzung 9.06.09, nicht zur Friedhofssatzung 9.06.08. Selbstwiderspruch / Faktenfehler in Keyfacts.

Zweiter Punkt: Wahlgrab Ziffer 1.1 = 1.908 € (30 J., 1 Stelle). Friedpark-Wahlgrab Ziffer 1.2 = 4.032 € (30 J., 1 Stelle). Beim Westfriedhof wird die "Parkartige Wahlgrabstätte Abt. 6+11, doppelte Grundfläche" mit Ziffer 1.2 / 4.032 € angegeben — und zugleich "Friedpark-Wahlgrabstätte 30 J, 1 Stelle" ebenfalls mit Ziffer 1.2 / 4.032 €. Identische Ziffer für zwei verschiedene Grabtypen ist mindestens unklar, möglicher Faktenfehler.

YMYL: Alle Geldbeträge mit Stand 22.08.2025 / Fassung 06.12.2025 versehen, Hero-Meta "Stand: Mai 2026" ✓.

STADT: Kassel
VERDICT: PASS mit 2 MAJOR

Fund 1 — Datums-Selbstwiderspruch Friedhofssatzung 9.06.08 Wo: Keyfacts-Box, Zeile "Friedhofssatzung". Was: Behauptet "9.06.08, Beschluss 13.12.2024, geltend ab 12.04.2025; zweite Fassung beschlossen 22.08.2025, geltend ab 06.12.2025". Die eigene Quelle 2 listet 9.06.08 nur "in der Fassung der Änderung vom 13. Dezember 2024, geltend ab 12. April 2025" — die 22.08.2025/06.12.2025-Änderung gehört nachweislich zur Gebührensatzung 9.06.09 (Quelle 1), nicht zur Friedhofssatzung. Datum vermischt zwei verschiedene Satzungen. Fix: Zweiten Halbsatz in der Friedhofssatzung-Zeile streichen. Nur belassen: "9.06.08, Änderung vom 13.12.2024, geltend ab 12.04.2025".

Fund 2 — Doppelte Belegung Ziffer 1.2 / 4.032 € Wo: Westfriedhof-Box ("Gebührenrelevante Besonderheiten") und Kostentabelle. Was: "Parkartige Wahlgrabstätte Abt. 6+11, doppelte Grundfläche" und "Friedpark-Wahlgrabstätte, 1 Stelle" werden beide als Ziffer 1.2 mit identisch 4.032,00 € geführt. Doppelte Fläche = gleicher Preis wie eine Stelle Friedpark ist intern widersprüchlich, eine der beiden Ziffern-Zuordnungen ist falsch. Fix: Gegen Gebührensatzung 9.06.09 verifizieren, welche Ziffer welche Grabart abdeckt; vermutlich gehört "Parkartige Wahlgrab, doppelte Grundfläche" zu einer anderen Unter-Ziffer (z.B. 1.2.2) mit eigenem Preis. Falsche Zeile korrigieren.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen