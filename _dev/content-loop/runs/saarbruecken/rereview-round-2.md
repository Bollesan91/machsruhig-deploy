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
Saarbrücken Bestattungsgesetz Review-Validierung
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
Krematorium Heidelberg: Re-Review der Major-Funde
Halle (Saale) Bestatter-Seite Review
Heidelberg Stadt-Page Review für machsruhig.de
Freiburg Stadt-Page Review für machsruhig.de
Erfurt Stadt-Page Review für machsruhig.de
Alle Chats
B
Bolle
Max Plan
Saarbrücken Bestattungsgesetz Review-Validierung
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: I'll fetch the current version and verify both fixes.

I'll fetch the current version and verify both fixes.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/saarbruecken/index.html?cb=1779113454279

Now checking both fixes systematically:

Fund 1 — 36h-Überführung Paragraph-Ref:

Recht-Sektion: "Die Überführung vom Sterbeort hat innerhalb von 36 Stunden zu erfolgen." → kein § genannt (war vorher § 29, jetzt unspezifiziert)
Todesfall-Sektion Step 2: "Nach § 22 Abs. 1 BestattG Saarland muss die Überführung … innerhalb von 36 Stunden erfolgen." → ✓ korrigiert
FAQ-Antwort: "Die Überführung des Verstorbenen in eine Leichenhalle hat nach § 22 Abs. 1 BestattG Saarland innerhalb von 36 Stunden zu erfolgen." → ✓ korrigiert
FAQ-Schema (JSON-LD): "Die Überführung des Verstorbenen in eine Leichenhalle hat nach § 22 Abs. 1 BestattG Saarland innerhalb von 36 Stunden zu erfolgen." → ✓ korrigiert

Fund 2 — FAQ-Schema vs HTML "Sterbefall anzeigen": Schema: "in dieser Reihenfolge: Personen, die mit der verstorbenen Person in häuslicher Gemeinschaft lebten; Personen, in deren Wohnung sich der Sterbefall ereignet hat; sowie Personen, die beim Tod zugegen waren." HTML: identisch. → ✓ 1:1 deckungsgleich

STADT: Saarbruecken
VERDICT: PARTIAL

Fund 1 — 36h-Überführung Paragraph-Ref: ✗ NOT FIXED (teilweise)

✓ Stelle 2 (Todesfall Schritt 2): "Nach § 22 Abs. 1 BestattG Saarland muss die Überführung … innerhalb von 36 Stunden erfolgen."
✓ Stelle 3 (FAQ + FAQ-Schema): "§ 22 Abs. 1 BestattG Saarland … 36 Stunden"
✗ Stelle 1 (Recht-Sektion, Absatz 2): "Die Überführung vom Sterbeort hat innerhalb von 36 Stunden zu erfolgen." — § fehlt komplett. Vorher falsch (§ 29), jetzt unbelegt. Erwartet war Korrektur zu § 22 Abs. 1, nicht Streichung.

Fund 2 — FAQ-Schema vs HTML "Sterbefall anzeigen": ✓ FIXED Schema und HTML jetzt wortgleich mit voller Reihenfolge (häusliche Gemeinschaft → Wohnungsinhaber → Zugegene → Bestatter → Einrichtungsträger). Beweisstelle: JSON-LD FAQPage Block Q5 vs HTML <details> Q5 — Textkörper identisch.

Empfehlung: Recht-Sektion ergänzen: „nach § 22 Abs. 1 BestattG Saarland innerhalb von 36 Stunden". Ohne diese Korrektur bleibt eine YMYL-Rechtsaussage ohne §-Beleg im Fließtext stehen — schwächer als die FAQ-Variante derselben Page.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen