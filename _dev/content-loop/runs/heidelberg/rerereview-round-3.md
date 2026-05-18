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
Krematorium-Ranking und YMYL-Daten überprüfen
Unbenannt
Wiesbaden Stadt-Page Review für machsruhig.de
Saarbrücken Bestattungsgesetz Review-Validierung
Regensburg Friedhof-Schema Review
Bestattungspflicht-Reihenfolge Oldenburg überprüfen
Wiesbaden Stadt-Page Review für machsruhig.de
Saarbrücken Bestatter-Seite Review
Oberhausen Stadt-Page Review für machsruhig.de
Oldenburg Stadt-Page Review für machsruhig.de
Regensburg Stadt-Page Review für machsruhig.de
Saarbrücken Bestatter-Seite Review
Mülheim Friedhof Re-Review: Major-Funde Überprüfung
Kassel Gebührensatzung: Doppelte Ziffer 1.2 Re-Check
Mülheim Friedhof-Content Review: Major-Funde Überprüfung
FAQ-Schema Überprüfung für Mainz
Kassel Friedhofssatzung: Re-Review der Major-Funde
Überprüfung von Rechtsreferenzen in Leverkusen
Überprüfung von Faktenchecks für machsruhig.de Kiel
Mülheim Friedhof-Content Review: Major-Funde Überprüfung
FAQ-Schema Überprüfung für Mainz
Mainz Bestatter-Seite Review
Überprüfung der Mülheim-Seite auf machsruhig.de
Leverkusen Bestatter-Seite Review
Kassel Stadt-Page Review für machsruhig.de
Kiel Stadt-Page Review für machsruhig.de
FAQ-Schema Überprüfung für Erfurt
Krematorium Heidelberg: Re-Review der Major-Funde
Halle (Saale) Bestatter-Seite Review
Heidelberg Stadt-Page Review für machsruhig.de
Überprüfung der Mülheim-Seite auf machsruhig.de
Mainz Bestatter-Seite Review
Krematorium Heidelberg: Re-Review der 4 Major-Funde
Schalker Fan-Feld Daten-Review für Gelsenkirchen
FAQ-Schema Validierung für Halle Bestatter
Alle Chats
B
Bolle
Max Plan
Krematorium-Ranking und YMYL-Daten überprüfen
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetche die neue Version und prüfe die 4 Fixes.

Ich fetche die neue Version und prüfe die 4 Fixes.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/heidelberg/index.html?cb=1779114251650

STADT: Heidelberg
VERDICT: CLEAN

Fund 1 — Krematorium-Rang: ✓ FIXED

Hero-Lead: "zweitältesten erhaltenen Krematorium Deutschlands (nach Gotha 1878)"
Keyfacts: "in Betrieb seit 22. Dezember 1891 (zweitältestes erhaltenes Krematorium Deutschlands nach Gotha 1878)"
Bergfriedhof-Absatz: "am 22. Dezember 1891 in Betrieb genommen wurde und damit nach der 1878 eröffneten Anlage in Gotha das zweitälteste erhaltene Krematorium Deutschlands ist"
FAQ "Krematorium" + FAQ "historisch interessanteste" (HTML + JSON-LD): beide mit "zweitälteste" + Gotha-Referenz konsistent.

Fund 2 — § 30 raus: ✓ FIXED

Section "Bestattungsrecht": "Sargpflicht und Bestattungsarten (§§ 32, 39 BestattG BW)". § 30 nicht mehr vorhanden. Quellenliste nennt § 32 Abs. 1+2 und § 39 Abs. 3 — sauber.

Fund 3 — FAQ-Mismatch anonyme Bestattung: ✓ FIXED

HTML: "Gesamtkosten beginnen bei rund 1.900 € bis 2.500 € (Stand: Mai 2026)"
JSON-LD: "Die Gesamtkosten beginnen bei rund 1.900 EUR bis 2.500 EUR (Stand Mai 2026)" — Parität gegeben.

Fund 4 — YMYL Stand-Datum Hauptkosten-FAQ: ✓ FIXED

HTML: "(Stand: Mai 2026)" direkt nach erstem Satz, vor den vier Eurobeträgen.
JSON-LD: "Stand: Mai 2026." als Eröffnungssatz vor allen Beträgen. Beides eindeutig YMYL-konform.

Alle 4 MAJOR-Findings behoben. Deploy-freigabefähig.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen