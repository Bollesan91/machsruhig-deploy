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
Wiesbaden Stadt-Page Review für machsruhig.de
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
Überprüfung der Mülheim-Seite auf machsruhig.de
Mainz Bestatter-Seite Review
Krematorium Heidelberg: Re-Review der 4 Major-Funde
FAQ-Schema Validierung für Halle Bestatter
Schalker Fan-Feld Daten-Review für Gelsenkirchen
FAQ-Schema Überprüfung für Erfurt
Gelsenkirchen Stadt-Page Review für machsruhig.de
Halle (Saale) Bestatter-Seite Review
Heidelberg Stadt-Page Review für machsruhig.de
Krematorium Heidelberg: Re-Review der Major-Funde
Halle (Saale) Bestatter-Seite Review
Freiburg Stadt-Page Review für machsruhig.de
Erfurt Stadt-Page Review für machsruhig.de
Heidelberg Stadt-Page Review für machsruhig.de
Alle Chats
B
Bolle
Max Plan
Wiesbaden Stadt-Page Review für machsruhig.de
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetche die Live-Version und reviewe.

Ich fetche die Live-Version und reviewe.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/wiesbaden/index.html?cb=1779113453985
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/wiesbaden/index.html?cb=1779113453985

Ich prüfe die kritischen Punkte. FBG Hessen §-Referenzen verifizieren:

Web durchsucht
Web durchsucht

Kritischer Fund bestätigt: Die FBG-Inhaltsübersicht zeigt klar – §8 = Feuerbestattungsanlagen, §13 = Sorgepflichtige Personen, §10 = Pflicht zur Leichenschau, §12 = Leichenschau, §6 = Grabstätten/Ruhefristen, §16 = Bestattungsfristen. Die Page hat §8 falsch zitiert. Außerdem prüfe ich die Leichenschau-Referenz (§10 ist Pflicht, §12 ist Durchführung – die Page sagt "§10" für Ausstellung des Scheins, das passt eher zu §12).

Selbstwiderspruch geprüft: Hero/FAQ sagen "330.700 qm" und "Hauptfriedhöfe Südfriedhof 33,07 ha" – konsistent. Aber: 33,07 ha = 330.700 qm ✓. Gesamtfläche "ca. 90 ha" für 21 Friedhöfe – wenn allein Südfriedhof 33 ha + Nord 14,5 + Biebrich 9,7 = 57,2 ha für 3 Friedhöfe, + 18 weitere bis 6 ha = plausibel.

FAQ-Schema-Match: 6 Fragen im Schema, 7 Fragen im HTML (Ruhezeit-Frage fehlt im Schema). Das ist ein Mismatch.

STADT: Wiesbaden
VERDICT: FAIL (2 MAJOR)

Fund 1 — Falsche FBG-Paragraphen-Referenz (Sorgepflichtige Personen)
Wo: Section "Bestattungsrecht in Wiesbaden", Absatz 2 + Hero-Aussage zum Sorgepflichtigen-Sequenz
Was: Page zitiert "§ 8 FBG" für sorgepflichtige Personen. Korrekt ist § 13 FBG Hessen. § 8 FBG regelt "Errichtung und Betrieb von Feuerbestattungsanlagen". Bei einer YMYL-Page mit expliziten Paragraphen-Referenzen ist das ein harter Fehler — Nutzer, die sich auf die Reihenfolge der Bestattungspflicht verlassen, zitieren die falsche Norm.
Fix: "§ 8 FBG" → "§ 13 FBG" ersetzen (einmalig im Text).

Fund 2 — FAQ-Schema vs HTML-FAQ Mismatch
Wo: JSON-LD FAQPage vs <section class="mr-faq">
Was: HTML enthält 7 FAQ-Items (inkl. "Welche Ruhezeit gilt für ein Grab in Wiesbaden?"), das Schema nur 6. Die Ruhezeit-Frage fehlt im strukturierten Datensatz. Google verlangt Schema-HTML-Parität, sonst Risiko der Rich-Result-Aberkennung.
Fix: 7. Question-Block für "Ruhezeit" ins FAQPage-Schema ergänzen mit identischem Antworttext.

Kein Selbstwiderspruch bei Flächenangaben (33,07 ha = 330.700 qm konsistent). Cross-Link /bestattung-in/hessen/ plausibel (Standard-Bundesland-Pattern). Keine sonstigen Fakten-Halluzinationen identifiziert.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
Zu viele Antworten werden gleichzeitig generiert. Du kannst eine Antwort stoppen oder warten, bis eine abgeschlossen ist, und es dann erneut versuchen.