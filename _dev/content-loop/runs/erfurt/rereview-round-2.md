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
FAQ-Schema Überprüfung für Erfurt
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
Re-Review Rostock: Major-Funde Überprüfung
Magdeburg-Überprüfung: MAJOR-Funde validieren
Potsdam-Friedhof: Überprüfung der MUST-FIX-Korrektionen
Überprüfung der Köln-Seite auf behobene Major-Fehler
Re-Review Frankfurt Friedhof und Bestattungsrecht
Rostock Bestatter Review auf machsruhig.de
Magdeburg Bestatter Review - Qualitätskontrolle
Strict review of Potsdam funeral director content
Köln Bestatter-Seite Qualitätsprüfung
Alle Chats
B
Bolle
Max Plan
FAQ-Schema Überprüfung für Erfurt
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist strikter Re-Reviewer fuer machsruhig.

Du bist strikter Re-Reviewer fuer machsruhig.de. Vorherige Reviewer-Runde fand 1 MAJOR-Fund in Erfurt.

ORIGINAL-MAJOR-FUND:
1. FAQ-Schema vs HTML-Mismatch: JSON-LD FAQPage enthielt 7 Fragen, sichtbares HTML-FAQ enthielt 8 Fragen. Die HTML-Frage 'Was ist beim Besuch des Neuen Juedischen Friedhofs zu beachten?' (Oeffnungszeiten, Sabbat-Schliessung, Kopfbedeckung, Steine-Brauch) fehlte komplett im Schema. Erwartet: Achte Frage als 8. Question-Eintrag im mainEntity-Array ergänzt, mit Answer-Text aus dem HTML.

NEUE VERSION (fetch jetzt):
https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/erfurt/index.html?cb=1779110000179

Format:
STADT: Erfurt
VERDICT: CLEAN | PARTIAL (0/1 fixed) | FAIL
✓ FIXED oder ✗ NOT FIXED + Beweisstelle.
Max 200 Worte.

Mehr anzeigen
15:13
Claude hat geantwortet: I'll fetch the new version and verify the fix.

I'll fetch the new version and verify the fix.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/erfurt/index.html?cb=1779110000179
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/erfurt/index.html?cb=1779110000179

STADT: Erfurt
VERDICT: CLEAN (1/1 fixed)

✓ FIXED — FAQ-Schema vs HTML-Mismatch behoben.

Beweisstelle Schema (JSON-LD FAQPage, mainEntity, 8. Eintrag):

"@type": "Question",
"name": "Was ist beim Besuch des Neuen Jüdischen Friedhofs zu beachten?",
"acceptedAnswer": {
  "@type": "Answer",
  "text": "Der Neue Jüdische Friedhof in der Werner-Seelenbinder-Straße 3 ist samstags und an jüdischen Feiertagen geschlossen, freitags nur bis 15 Uhr geöffnet. Im Sommer gelten Öffnungszeiten von 8 bis 17 Uhr, im Winter bis 16 Uhr. Männliche Besucher sollten den Kopf bedecken; das Hinterlassen kleiner Steine auf Grabmälern ist Brauch und drückt die Erinnerung aus. Träger ist die Jüdische Landesgemeinde Thüringen."
}

Beweisstelle HTML (<section class="mr-faq">, 8. <details>): Frage „Was ist beim Besuch des Neuen Jüdischen Friedhofs zu beachten?" mit inhaltsgleicher Antwort (Werner-Seelenbinder-Straße 3, Samstag/Feiertage geschlossen, Fr bis 15 Uhr, Sommer 8–17/Winter bis 16 Uhr, Kopfbedeckung, Steine-Brauch, Trägerin).

Count-Abgleich: 8 Questions im Schema ↔ 8 <details> im HTML. Reihenfolge und Antwortinhalte konsistent. Keine neuen Diskrepanzen.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen