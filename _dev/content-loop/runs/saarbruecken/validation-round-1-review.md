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
Saarbrücken Bestatter-Seite Review
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
Überprüfung Paragraph-Referenzen Chemnitz
Augsburg-Bestatter: Re-Review der Major-Funde
Wixhausen-Eingemeindung Darmstadt überprüfen
Heidelberg Stadt-Page Review für machsruhig.de
Alle Chats
B
Bolle
Max Plan
Saarbrücken Bestatter-Seite Review
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetche die Live-Version und reviewe.

Ich fetche die Live-Version und reviewe.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/saarbruecken/index.html?cb=1779112630724
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/saarbruecken/index.html?cb=1779112630724

Ich verifiziere jetzt die kritischen Paragraph-Referenzen für BestattG Saarland.

Web durchsucht
Web durchsucht

Kritischer Befund: Die Überführungsfrist (36 Stunden) ist in § 22 BestattG Saarland geregelt, nicht in § 29. Die Seite zitiert das mehrfach falsch. Ich verifiziere noch § 31 (Sargpflicht).

Searching the web
Web durchsucht

Befunde sind verifiziert. Hier der Review:

STADT: Saarbrücken VERDICT: PASS mit 2 MAJOR

Fund 1: Falsche Paragraph-Referenz für 36-Stunden-Überführungsfrist (3× im Dokument)

Wo: Section #recht (Absatz 2), Section #todesfall (Schritt 2), FAQ "Wer muss den Sterbefall... anzeigen" (implizit via §29-Block)
Was: Die Seite ordnet die 36-Stunden-Überführungsfrist mehrfach explizit § 29 BestattG Saarland zu („Nach § 29 BestattG Saarland muss die Überführung... innerhalb von 36 Stunden erfolgen"). § 29 regelt aber ausschließlich Bestattungsfristen (48 h / 10 Tage / 3 Monate). Die 36-Stunden-Überführung steht in § 22 Abs. 1 BestattG Saarland (Überführung in Leichenhallen). Das ist ein YMYL-Faktenfehler in einer Kernrechtsangabe und konsistent über drei Stellen.
Fix: Überall „§ 29" → „§ 22 BestattG Saarland" wo es um die 36-h-Überführung geht. § 29 nur noch für 48 h / 10 Tage zitieren. FAQ-JSON-LD-Eintrag „Wie lange dauert es bis zur Bestattung..." entsprechend trennen.

Fund 2: FAQ-Schema vs HTML-FAQ Mismatch bei „Sterbefall anzeigen"

Wo: JSON-LD FAQPage „Wer muss den Sterbefall in Saarbrücken anzeigen?" vs. HTML <details> gleiche Frage.
Was: HTML nennt eine konkrete Reihenfolge der Anzeigepflichtigen (häusliche Gemeinschaft → Wohnungsinhaber → bei Tod Zugegene). Das Schema enthält diese Reihenfolge nicht und sagt stattdessen „In der Praxis übernimmt das beauftragte Bestattungsunternehmen die Anzeige". Inhaltlicher Drift, kein 1:1 Mapping → Google-FAQ-Risiko und PStG-Halbwahrheit (Bestatter ist nicht primär anzeigepflichtig).
Fix: Schema-Answer an HTML-Wortlaut angleichen (Reihenfolge plus Bestatter-Hinweis als Praxis-Zusatz).

Cross-Links (/bestattung-in/saarland/, /bestatter/, /vorsorge/, /bestattungsarten/, /bestattung-in/rheinland-pfalz/) nicht live-geprüft — strukturell konsistent mit deinem Linkschema, kein offensichtlicher Dead-Link. § 5, § 31, BSG-Az., Aeternitas-Werte, 24-Friedhöfe-Claim, jesidisches Grabfeld 2019, Willi-Graf-Grab, URBAN-I, Burbach-Award 2014 — alles plausibel und konsistent zitiert.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
Zu viele Antworten werden gleichzeitig generiert. Du kannst eine Antwort stoppen oder warten, bis eine abgeschlossen ist, und es dann erneut versuchen.
 Claude is active in this tab group  
Open chat
 
Dismiss