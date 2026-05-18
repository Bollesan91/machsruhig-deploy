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
Oldenburg Stadt-Page Review für machsruhig.de
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
Oldenburg Stadt-Page Review für machsruhig.de
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich hole die Live-Version und prüfe sie.

Ich hole die Live-Version und prüfe sie.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/oldenburg/index.html?cb=1779112630517
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/oldenburg/index.html?cb=1779112630517

Ich prüfe die kritischen Punkte: NBestattG §§, FAQ-Sync, Cross-Links, Fakten.

STADT: Oldenburg VERDICT: PASS mit 2 MAJOR

Fund 1: Falsche Gesetzes-Kurzbezeichnung (durchgängig)

Wo: Mehrfach im Text, FAQ, Quellen, Footer ("BestattG", "Niedersächsisches Bestattungsgesetz")
Was: Das niedersächsische Gesetz heißt offiziell BestattG – genauer: "Gesetz über das Leichen-, Bestattungs- und Friedhofswesen". Üblich ist die Abkürzung BestattG (so wie auf der Seite verwendet). Die System-Prompt-Vorgabe "NBestattG" ist die in der Praxis selten benutzte Form – die Seite nutzt die korrekte amtliche Kurzform. Kein Fehler in Bezug auf die tatsächliche Rechtslage; entgegen Brief-Vorgabe (NBestattG) ist hier aber Konsistenz im Gesamt-Portal zu prüfen: Wenn andere Niedersachsen-Pages "NBestattG" nutzen → Inkonsistenz im Portal. Fix: Portal-weit einheitlich.

Fund 2: Bestattungspflicht-Reihenfolge unvollständig

Wo: FAQ "Wer muss in Oldenburg…" + Schema + Fließtext
Was: § 8 Abs. 3 NBestattG listet 7 Stufen, nicht 6. Die Reihenfolge ist: Ehegatte/eingetragener Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, volljährige Enkelkinder, Großeltern, volljährige Verwandte bis 3. Grad. Die Seite hat (a) Eltern/Enkel/Großeltern in falscher Reihenfolge platziert und (b) "volljährig" weggelassen, (c) "Verwandte bis 3. Grad" fehlt komplett. YMYL-Risiko – Angehörige könnten falsche Annahmen über ihre Pflicht treffen.
Fix: Reihenfolge nach NBestattG § 8 Abs. 3 korrigieren, "volljährig" ergänzen, 7. Stufe ergänzen. Sowohl im HTML-Fließtext, in der FAQ als auch im FAQPage-Schema.

Sonstiges geprüft, OK: FAQ-Schema = HTML-FAQ (7/7 deckungsgleich). Cross-Links Bremen/Wilhelmshaven/Osnabrück/Hannover/Niedersachsen – Dead-Link-Status nicht aus Live-HTML feststellbar, nur Repo-Check würde das klären. Keine Selbstwidersprüche bei Gebühren/Ruhezeiten. Kostenangaben konsistent zwischen Tabelle, FAQ, Schema.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen