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
Regensburg Stadt-Page Review für machsruhig.de
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
Überprüfung der Mülheim-Seite auf machsruhig.de
Mainz Bestatter-Seite Review
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
Überprüfung Paragraph-Referenzen Chemnitz
Augsburg-Bestatter: Re-Review der Major-Funde
Wixhausen-Eingemeindung Darmstadt überprüfen
Alle Chats
B
Bolle
Max Plan
Regensburg Stadt-Page Review für machsruhig.de
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetche die Live-Version und reviewe.

Ich fetche die Live-Version und reviewe.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/regensburg/index.html?cb=1779112630635
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/regensburg/index.html?cb=1779112630635

STADT: Regensburg
VERDICT: PASS mit 3 MAJOR

Fund 1: Selbstwiderspruch FAQ vs HTML — Friedhofszahl Wo: FAQ-Schema (JSON-LD) Frage 1 vs HTML-FAQ-Detail Frage 1. Was: JSON-LD-FAQ listet nur "Evangelischer Zentralfriedhof und Oberer Katholischer Friedhof" als konfessionelle Friedhöfe. HTML-FAQ ergänzt zusätzlich den Gesandtenfriedhof. Mismatch zwischen Schema und sichtbarem FAQ-Inhalt → Google-Rich-Result-Risiko. Fix: JSON-LD-Answer angleichen, Gesandtenfriedhof mit aufnehmen.

Fund 2: Falsche Paragraph-Referenz BestG Wo: Section "Bestattungsrecht in Regensburg", Absatz 1: „zulässig sind Erd-, Feuer- und Seebestattung (Art. 1 Abs. 1 BestG)". Was: Art. 1 Abs. 1 BayBestG regelt die Bestattungspflicht generell, nicht die Aufzählung der zulässigen Bestattungsarten. Die Zulässigkeit der Feuerbestattung ergibt sich aus Art. 12 BestG (Einäscherung); Seebestattung ist ein Sonderfall ohne expliziten Artikel-Anker im BestG. Falsche Norm-Zuordnung = YMYL-Risiko. Fix: „(Art. 1 BestG i.V.m. Art. 12 BestG)" oder Klammerverweis entfernen und allgemein formulieren.

Fund 3: Faktenfehler Telefonnummer Oberer Katholischer Friedhof Wo: Friedhof-Karte „Oberer Katholischer Friedhof" Verwaltung + Sektion „4. Grabnutzungsrecht": „Tel. 0941 90572" / „Tel. (0941) 90572". Was: Nur 5 Ziffern statt üblicher Regensburger Festnetznummer (Vorwahl 0941 + i.d.R. 6–7 Ziffern, vgl. andere Nummern auf der Seite: 507-2343 etc.). Plausibel abgeschnitten/typo. Bei einer YMYL-Kontaktinfo für Trauerfälle ein No-Go. Fix: Korrekte Nummer der Dompfarreiengemeinschaft / Oberer Katholischer Friedhof verifizieren und ersetzen.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen