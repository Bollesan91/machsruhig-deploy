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
Augsburg Stadt-Page Review für machsruhig.de
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
Bremen Strict Independent Review
Bremen Bestatter Korrektionen: Architektur und Lebensdaten
Hamburg Bestattungsseite: 3 kritische Korrektionen
Berlin Bestattungsgesetz Faktenchecks
Korrektionen Bestattungsgesetz NRW Rangfolge
Strict independent review for Leipzig
Berlin Bestattungsseite: Faktenchecks und Korrektionen
Dresden Bestatter Review Pass 2
Bestatter Essen HTML-Korrektionen
Bremen-Artikel Korrektionen und HTML-Fixes
Dortmund Friedhöfe: Kritische Adress- und Rechtstext-Korrektionen
Dresden Friedhof Schema-Korrektionen
Strenge Überprüfung von Leipzig auf machsruhig.de
Strenge Überprüfung von Berlin-Bestättern
Strict independent review for Bremen
Strenge Überprüfung von Hamburg auf machsruhig.de
Strenge Überprüfung von Essen-Inhalten
Strenge Überprüfung von Berlin-Bestättern
Dortmund Bestatter Review Pass 2
Korrektionen zu Leipziger Friedhofsinformationen
Alle Chats
B
Bolle
Max Plan
Augsburg Stadt-Page Review für machsruhig.de
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetch die Live-Version und prüfe sie.

Ich fetch die Live-Version und prüfe sie.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/augsburg/index.html?cb=1779107742931
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/augsburg/index.html?cb=1779107742931

Ich prüfe die kritischen Faktenpunkte. Schlüsselverdächtige: BayBestG-Paragraph-Referenzen (Art. 14, Art. 15 — stimmt das?), Brecht-Familiengrab (Vater hieß tatsächlich "Berthold Friedrich" oder "Berthold Friedrich" mit "h" vs "Brecht-Vater Berthold Friedrich"), Cross-Link-Konsistenz, FAQ-JSON-LD vs HTML-FAQ.

Web durchsucht
Web durchsucht

Wichtig: Die Page schreibt "Art. 14 BestG, Art. 15 BestG". Laut Rechtsprechung ist die korrekte Norm-Verkettung: Art. 15 Abs. 1 BestG i.V.m. § 15 BestV und § 1 Abs. 1 Satz 2 BestV. Die Page hat das richtig. Allerdings: "Ersatzbestattung nach Art. 14 BestG" stimmt (Art. 14 = Bestattungspflicht der Gemeinde).

Aber: "Art. 15 BestG" als Norm, die die Angehörigen verpflichtet – Art. 15 ist eine Verordnungsermächtigung. Die Page formuliert das aber korrekt als "Art. 15 BestG i.V.m. § 15 BestV". OK.

Jetzt zum Brecht-Vater: Heißt er "Berthold Friedrich Brecht" oder "Berthold Friedrich"? Quick-Check:

Web durchsucht
Web durchsucht

Brecht-Vater "Berthold Friedrich Brecht" und Mutter "Sophie Brecht" — beides korrekt.

Aber: Die Page schreibt "Direktor der Haindl'schen Papierfabrik" — präzise war er kaufmännischer Direktor (ab 1917). Das ist eine Verkürzung, aber nicht falsch genug für MAJOR.

Wichtiger Punkt: Die Page schreibt im FAQ-Schema (JSON-LD) "Familiengrab der Brechts mit Vater Berthold Friedrich Brecht (Direktor der Haindl'schen Papierfabrik)" und im sichtbaren HTML "die Eltern Bertolt Brechts Berthold Friedrich Brecht (Direktor der Haindl'schen Papierfabrik) und Sophie Brecht". Konsistent.

Jetzt: Ludwig von Fischer "rund 34 Amtsjahre" — 8.5.1866 bis 8.1.1900 = knapp 34 Jahre. Stimmt.

Christoph von Schmid (1768–1854) — und der Text sagt "nach Cholera-Tod 1854". Stimmt.

Mathias Kneißl: 1875 geboren, 1902 hingerichtet — soll auf Hermanfriedhof beigesetzt sein. Schnell prüfen:

Web durchsucht
Web durchsucht

MAJOR-Fund: Die Page schreibt Kneißl "geb. 1875" — das ist ungenau aber nicht falsch. Wichtiger: laut Hermanfriedhof.de selbst und Wikipedia: 12. Mai 1875. Page nennt nur "1875" — keine Halluzination, akzeptabel.

Aber: Page sagt "Augsburger JVA hingerichtet" — laut Wikipedia und Hermanfriedhof war es das Landgerichtsgefängnis an der Karmelitengasse, nicht "JVA". Halb-Anachronismus, aber nicht echter Faktenfehler im strikten Sinne (JVA als Sammelbegriff ist vertretbar). Knapp.

Jetzt checke ich noch §-Referenzen Bestattungsfrist:

Page: "§ 19 Abs. 1 BestV" für 8-Tages-Frist ✓ (das ist korrekt für Bayern)
Page: "§ 30 Abs. 1 BestV" für Sargpflicht ✓
Page: "§ 30 Abs. 2 BestV" für sarglose Bestattung ✓

Jetzt FAQ-JSON-LD vs sichtbares HTML:

JSON-LD hat 9 Fragen, HTML hat 9 details. Stimmt zahlenmäßig.
Eine Frage im JSON-LD: "Gilt in Bayern noch Sargpflicht?" → Im HTML: "Gibt es in Augsburg eine Möglichkeit zur sarglosen Erdbestattung?" — unterschiedliche Frageformulierung. Das ist ein FAQ-Schema-Mismatch (Google verlangt, dass JSON-LD-FAQ den sichtbaren Inhalt spiegelt).

Cross-Links:

/bestatter/ → "Bestattung in München" — die URL /bestatter/ ist aber die Bestatter-Hauptseite, nicht München. Dead/falscher Cross-Link: Der Linktext suggeriert München-Seite, der Link führt zur generellen Bestatter-Übersicht. Beim zweiten Vorkommen "<a href="/bestatter/">Münchner Bestatterübersicht</a>" — exakt dasselbe Problem.

Christoph Friedrich Nilson — angeblich "Historienmaler" auf Protestantischem Friedhof. Quick-check:

Web durchsucht
Web durchsucht

OK – Nilson stimmt. Genug Recherche. Ich habe genug für den Review-Bericht.

Zusammenfassung der MAJOR-Funde:

Cross-Link "Bestattung in München" → falscher Anchor: "(siehe <a href="/bestatter/">Bestattung in München</a>)" und "<a href="/bestatter/">Münchner Bestatterübersicht</a>" — der Linktext verspricht eine München-Seite, der Link führt aber zur Bestatter-Hauptübersicht. Dead Cross-Link iSv "geht ins Leere bzgl. Zielseite".
FAQ-Schema vs HTML-Mismatch: JSON-LD FAQ-Frage "Gilt in Bayern noch Sargpflicht?" — im sichtbaren HTML lautet die entsprechende Frage "Gibt es in Augsburg eine Möglichkeit zur sarglosen Erdbestattung?". Google-Richtlinie: FAQ-Schema muss sichtbar im HTML 1:1 vorhanden sein.
YMYL-Risiko Standesamtsgebühr-Beleg: Die Gebühr "12,00 € pro Sterbeurkunde" wird mit "Stadt Augsburg, Urkundenbestellung Standesamt" belegt, aber ohne Stand-Datum. Bei Geldbeträgen verlangt YMYL ein Datum.

Tatsächlich gibt es im Text "seit 1. Januar 2025" für die Friedhofsgebühren (datiert) – aber für die Urkundengebühr fehlt das Datum.

Jetzt der Bericht (max 250 Wörter):

STADT: Augsburg
VERDICT: PASS mit 3 MAJOR

Fund 1 — Cross-Link / falsche Linkziele Wo: Abschnitt "Bestatter in Augsburg auswählen", zwei Stellen. Was: Linktexte "Bestattung in München" und "Münchner Bestatterübersicht" zeigen beide auf /bestatter/ (die generische Bestatter-Hauptseite), nicht auf eine München-Stadt-Page. Wenn /bestatter/muenchen/ nicht existiert, ist der Linktext irreführend. Fix: Entweder Linktext zu "Bestatter-Übersicht" anpassen oder Link auf /bestatter/muenchen/ korrigieren (sofern vorhanden).

Fund 2 — FAQ-Schema ≠ sichtbares HTML Wo: JSON-LD FAQPage vs HTML <details>. Was: JSON-LD-Frage lautet "Gilt in Bayern noch Sargpflicht?", im sichtbaren HTML steht stattdessen "Gibt es in Augsburg eine Möglichkeit zur sarglosen Erdbestattung?". Google verlangt für FAQ-Rich-Results, dass Schema-Fragen wortgleich im sichtbaren Content vorkommen — sonst Rich-Result-Verlust oder manuelle Maßnahme. Fix: Frageformulierung in JSON-LD und HTML angleichen. Beleg: Google Search Central, FAQ structured data Guidelines.

Fund 3 — YMYL: Geldbetrag ohne Stand-Datum Wo: Abschnitt "Bestattungskosten" und "Bestatter auswählen": "Eine beglaubigte Abschrift aus dem Sterberegister kostet beim Standesamt Augsburg 12,00 Euro, jede weitere Ausfertigung 6,00 Euro". Was: Konkrete Gebührenbeträge zitiert ohne Stand-Datum oder Verweis auf Satzung mit Datierung. Die Friedhofsgebühren sind sauber datiert ("seit 1.1.2025"), die Standesamtsgebühren nicht. Fix: "(Stand: [Datum])" oder Verweis auf konkrete Gebührensatzung/PStG-KostV mit Inkrafttreten ergänzen.

(247 Wörter)




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen