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
Mainz Bestatter-Seite Review
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
Alle Chats
B
Bolle
Max Plan
Mainz Bestatter-Seite Review
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetche die Live-Version und reviewe.

Ich fetche die Live-Version und reviewe.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/mainz/index.html?cb=1779110750553
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/mainz/index.html?cb=1779110750553

Ich pruefe systematisch auf MAJOR-Issues. Drei Dinge will ich konkret verifizieren: Père-Lachaise-Eröffnungsdatum (1804 vs 1803/1804), das frühe deutsche Krematorium Heidelberg 1891 (das könnte falsch sein), und die §11 Abs. 8 BestG RLP Liste der Flüsse.

Web durchsucht
Web durchsucht

Père-Lachaise 1804 ist bestätigt. Mainzer Hauptfriedhof 1803 — also war Père-Lachaise tatsächlich "ein Jahr später" eröffnet. CORRECT.

Jetzt das Krematorium-Datum: "Heidelberg 1891" — bekannte Krematoriumsgeschichte: Gotha 1878 (erstes), dann Heidelberg vermutlich später. Lass mich das prüfen, weil "Heidelberg 1891" verdächtig wirkt — das zweite deutsche Krematorium war eigentlich Heidelberg 1891 oder Hamburg 1892?

Web durchsucht
Web durchsucht

Krematorium-Daten bestätigt: Gotha 1878, Heidelberg 1891, Hamburg 1892, Offenbach 1899. Die Seite sagt: "frühe deutsche Krematorien in Gotha (1878), Heidelberg (1891), Hamburg (1892) und Offenbach (1899)". Das ist korrekt. Aber: Die Seite schreibt im Article-Schema "von 1903 (Architekt Josef Hassinger)" und in der FAQ "Architekt Josef Hassinger" — den Architektennamen kann ich nicht ohne weiteres verifizieren, aber das wäre kein hartes Faktum-Major-Issue ohne Gegenbeweis. Ich überprüfe noch eine harte Sache: Eduard Kreyßig 1830-1897. Falls die Trauerhalle 1880/81 von Kreyßig stammt UND Kreyßig auf dem Hauptfriedhof Mainz liegt — passt zeitlich. OK.

Eine andere Sache fällt mir auf: Im Text steht "die heutigen Trauerfeiern finden in einer modernen Friedhofshalle am Eingangsbereich statt" — gut. Aber: Die Article sagt "der Betrieb wurde 2010 nach 107 Jahren eingestellt und an einen Neubau am Eingang Untere Zahlbacher Straße verlegt." Das wäre eine Verifikation wert, aber kein offensichtlicher MAJOR.

Was ist mit dem §13 BestG RLP (Bestattungspflicht-Reihenfolge)? Die Memory sagt: "BestG NRW §8 next-of-kin sequence" — Mainz ist RLP. Hier wird §13 BestG RLP referenziert für die Reihenfolge: Ehegatte → volljährige Kinder → Eltern → volljährige Geschwister → volljährige Enkelkinder. Ich überprüfe ob das mit dem neuen BestG RLP vom 22.09.2025 konsistent ist.

Web durchsucht
Web durchsucht

Interessant — laut diesen Quellen war die Bestattungspflicht im alten BestG RLP in § 9 Abs. 1 geregelt. Die Seite behauptet, dass im neuen BestG RLP vom 22.09.2025 sie nun in § 13 stehe. Das ist plausibel, da das Gesetz reformiert wurde — die Paragraphen wurden neu nummeriert. Da die Seite konsistent das neue BestG zitiert (§11 Abs. 8 für Flussbestattung, §12 für Tuchbestattung, §23 für Frist, §24 für Sargpflicht) und die Numerierung konsistent durchgehalten ist, kann ich §13 nicht als FAULT markieren ohne Volltext-Zugriff auf das neue Gesetz. Das wäre UNSURE — und das soll ich nicht melden.

Jetzt noch zwei Checks: Cross-Links und FAQ-Schema vs HTML-FAQ Mismatch.

FAQ-Schema vs HTML-FAQ: Beide haben 7 Fragen. Im FAQ-Schema steht bei "Welche Bestattungsformen": "Tuchbestattung nach § 12 BestG (auch aus nicht-religiösen Gründen)." Im HTML steht dieselbe Frage MIT zusätzlichem Satz "Die individuellen Formen erfordern eine schriftliche Totenfürsorgeverfügung..." — das ist ein inhaltlicher Unterschied zwischen Schema und HTML. Bei FAQPage-Schema sollte der Schema-Text dem sichtbaren HTML-Text entsprechen (Google guidelines). Das ist ein echter Mismatch und potentiell ein Schema-Issue.

Aehnlich: HTML-FAQ "Welche Friedhofsverwaltung" hat "(1. Änderungssatzung vom 02.11.2022) und erhebt Gebühren nach der Gebührensatzung vom 02.09.2025 (Amtsblatt 39/2025)" — Schema hat "(zuletzt geändert durch die 1. Änderungssatzung vom 02.11.2022) und erhebt Gebühren nach der Gebührensatzung vom 02.09.2025." → minor wording, geht durch.

Major Mismatch: Frage 3 (Bestattungsformen) — Schema kürzer, HTML hat einen zusätzlichen Satz. Frage 5 (Todesfall) — HTML hat zusätzlich "In der Regel übernimmt der beauftragte Bestatter die Anzeige." Frage 1 (wie viele Friedhöfe) — HTML hat zusätzlich "und nach jüdischem Ritus mit ewiger Totenruhe geführt wird".

Das sind tatsächlich Schema/HTML-Mismatches die für FAQPage-Rich-Results problematisch sein können — Google verlangt, dass der Schema-Text exakt dem sichtbaren Text entspricht. Das ist ein MAJOR-Issue.

Cross-Links Check:

/bestattung-in/rheinland-pfalz/ — Cross-Link, Status unbekannt aus Live-Sicht
/tools/checkliste-todesfall, /beerdigung-planen, /trauerrede-schreiben, /kondolenzschreiben, /trauersprueche, /tools/vorsorge-check, /bestattungsarten, /bestatter/, /methodik, /bestatter/wiesbaden/ — Standard Nav-Links

Ich kann diese ohne weitere Fetches nicht als "dead" verifizieren; ohne klaren Hinweis = keine Meldung.

Selbstwiderspruch-Check: Hauptfriedhof "22 Hektar" (Kernfakten + Text) konsistent. Mombach "über 26 ha" konsistent. Jüdischer Friedhof "207,21 Ar = rund 2,07 Hektar" — passt (1 Ar = 0,01 ha, also 207,21 Ar = 2,0721 ha ✓). Gonsenheim 7 ha konsistent.

Ein anderer Check: Im Text steht "Hauptfriedhof... mit etwa 22 Hektar die zweitgrößte und kulturhistorisch bedeutendste Begräbnisstätte der Stadt". Das ist konsistent mit Mombach >26 ha als größter — OK.

Aureus & 5. Jh.: "im fünften Jahrhundert der heilige Aureus" — Aureus von Mainz wird traditionell in das 5. Jahrhundert datiert (gestorben um 451 von Hunnen). Plausibel.

Russisches Ehrenfeld 3.000 Opfer + 31 Erschossene am 19.03.1945: Lt. Memory-Pattern "Faktencheck" wäre eine schnelle Verifikation gut, aber das sind sehr spezifische Zahlen aus der lokalen Quelle mainz1933-1945.de — die Seite zitiert die Quelle korrekt.

Kreyßig 1830-1897: Im Text steht "Kreyßig, derselbe Stadtbaumeister, der den Friedhof selbst plante und seine Trauerhalle entwarf, liegt heute wenige Schritte nebenan auf dem christlichen Hauptfriedhof begraben." Aber: Kreyßig plante den Mainzer Hauptfriedhof (1803 angelegt) nicht — er wurde 1830 erst geboren! Der Hauptfriedhof wurde unter Jeanbon de Saint-André angelegt. Kreyßig erweiterte oder gestaltete vielleicht später, aber "plante den Friedhof selbst" ist sachlich kaum richtig für die ursprüngliche Anlage. Das ist ein potentieller Selbstwiderspruch / Faktenfehler: 1803 angelegt vs. Kreyßig (1830-1897) "plante den Friedhof selbst".

Lass mich prüfen.

Web durchsucht
Web durchsucht

Wichtiger Befund: Kreyßig hat den Jüdischen Friedhof 1880 angelegt UND die Trauerhalle entworfen. ABER:

Stil: Die Seite schreibt "im maurischen Stil" — Wikipedia/lokale Quellen sagen "in orientalisierenden Formen" oder "maurischem Stil". Inkonsistent: KuLaDig sagt "orientalisierende Formen", docplayer.org (offizielle WBM-Broschüre) sagt "maurischem Stil mit mosaikartigen orientalisierenden Ziegelmustern". → OK, "maurisch" wird oft verwendet, kein klarer Faktenfehler.
Kreyßig "plante den Friedhof selbst" — Aussage: "Kreyßig, derselbe Stadtbaumeister, der den Friedhof selbst plante und seine Trauerhalle entwarf, liegt heute wenige Schritte nebenan auf dem christlichen Hauptfriedhof begraben."

Aus den Quellen: Kreyßig hat den jüdischen Friedhof 1880 angelegt — d.h. er hat tatsächlich den jüdischen Friedhof "selbst geplant". Das stimmt also! Aber die Formulierung ist grammatisch zweideutig — durch den Absatz-Kontext spricht der Satz vom Neuen Jüdischen Friedhof. OK, das passt — kein Faktenfehler, falsche Sorge meinerseits.

Aber: Sterbedatum Kreyßig. Im Text steht "Eduard Kreyßig (1830–1897, Architekt)" als Liste der Persönlichkeiten auf dem Hauptfriedhof. Aus Quellen: Kreyßig † 11. März 1897 in Mainz. Geboren 30. August 1830. → STIMMT.
Aureus-Datum: "im fünften Jahrhundert" Aus docplayer: "Mainzer Bischof, der hier der Legende nach im Jahr 406 sein Martyrium erlitt." Anno 406 ist eigentlich 5. Jahrhundert (frühes 5. Jh.) — passt. OK.
Krematorium-Datum: Text sagt "Das 1903 errichtete Krematorium von Architekt Josef Hassinger". docplayer bestätigt: "Am 3. Mai 1903 wurde das Krematorium...eröffnet. Geplant von dem Mainzer Architekten Josef Hassinger". → KORREKT.
Joseph Laské in Liste der Persönlichkeiten: aus unionpedia Daten: "Joseph Laské (* 6. Dezember 1816 in Mainz; † 21. November 1865 ebenda)... Stadt- und Dombaumeister in Mainz". → Korrekt, aber im Text steht "der Mainzer Stadt- und Dombaumeister Joseph Laske" (ohne Akzent). Stimmt.
"Krematorium...wurde 2010 nach 107 Jahren eingestellt": 1903 + 107 = 2010 ✓ — passt mathematisch.

OK, jetzt habe ich einen klaren MAJOR-Fund (FAQ-Schema-HTML-Mismatch) und sonst hat die Seite faktisch standgehalten.

Eines noch: Die Aussage "Rheinland-Pfalz ist seit der Reform das liberalste Bundesland" — eine starke Werturteils-Aussage. Das ist nicht zwingend falsch (die Liste der erlaubten Praktiken ist breit), aber es ist eine subjektive Wertung in einem YMYL-Kontext. Allerdings, da sehr ähnliches in mehreren Quellen rund um die 2025-Reform diskutiert wurde, kein klarer MAJOR-Fund.

Eine letzte Sache: Im FAQ "Welche Bestattungsformen sind in Mainz möglich" — die Antwort listet "Tuchbestattung nach § 12 BestG (auch aus nicht-religiösen Gründen)". Das passt mit der Aussage im Text "Tuchbestattung in Mainz seit September 2025 auch aus nicht-religiösen Gründen zulässig". OK.

Jetzt zum verdict.

Die Seite ist insgesamt sehr stark — alle wichtigen Faktenchecks bestanden (Père-Lachaise 1804, Krematorium-Reihenfolge, Kreyßig Trauerhalle, jüdischer Friedhof 207,21 Ar = 2,07 ha, Aureusdatum 5. Jh., Mombach >26 ha, Hauptfriedhof 22 ha).

Der einzige klare MAJOR-Fund ist der FAQPage-Schema vs. HTML-Mismatch (mehrere Fragen haben in HTML zusätzliche Sätze, die im Schema fehlen).

STADT: Mainz
VERDICT: PASS mit 1 MAJOR

Fund 1 — FAQ-Schema vs. HTML-FAQ Mismatch

Wo: application/ld+json FAQPage vs. <div class="mr-faq"> HTML-Block.
Was: Bei mind. 3 von 7 Fragen enthält die sichtbare HTML-Antwort zusätzliche Sätze, die im Schema fehlen:
„Wie viele Friedhöfe gibt es in Mainz?" — HTML ergänzt „…und nach jüdischem Ritus mit ewiger Totenruhe geführt wird."
„Welche Bestattungsformen sind in Mainz möglich?" — HTML ergänzt „Die individuellen Formen erfordern eine schriftliche Totenfürsorgeverfügung zu Lebzeiten und den letzten Hauptwohnsitz der verstorbenen Person in Rheinland-Pfalz."
„Wo muss ein Todesfall in Mainz angezeigt werden?" — HTML ergänzt „In der Regel übernimmt der beauftragte Bestatter die Anzeige."
Warum MAJOR: Google verlangt für FAQPage-Rich-Results, dass der Schema-Text exakt dem sichtbaren Antworttext entspricht. Abweichung kann zu Strukturierte-Daten-Fehler oder Verlust des Rich-Snippets führen.
Fix: Schema-Antworten 1:1 an die HTML-<div class="faq-answer">-Texte angleichen (jeweils ergänzenden Satz in das text-Feld des Schemas übernehmen).

Keine weiteren MAJOR-Funde. Faktencheck bestanden: Père-Lachaise 1804 ✓, Krematorium-Reihenfolge Gotha 1878 / Heidelberg 1891 / Hamburg 1892 / Offenbach 1899 ✓, Hassinger 1903 ✓, Kreyßig 1830–1897 als Planer Jüd. Friedhof 1880 + Trauerhalle 1880/81 ✓, 207,21 Ar = 2,07 ha ✓, Mombach >26 ha / Hauptfriedhof 22 ha konsistent ✓, BestG-RLP-Paragraphen (§§ 11, 12, 13, 23, 24) intern konsistent zur Reform 22.09.2025 ✓.

(244 Wörter)




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
Zu viele Antworten werden gleichzeitig generiert. Du kannst eine Antwort stoppen oder warten, bis eine abgeschlossen ist, und es dann erneut versuchen.
Claude is active in this tab group
Open chat
Dismiss