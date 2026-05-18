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
Erfurt Stadt-Page Review für machsruhig.de
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
Köln Bestatter-Seite Qualitätsprüfung
Strict review of Potsdam funeral director content
Strict review protocol for Frankfurt bestatter content
Leipzig Bestatter Korrektionen: Bach-Datum und Flächenangaben
Karlsruhe Bestatter Überprüfung
Hamburg Bestattungsseite: 3 kritische Korrektionen
Berlin Bestattungsgesetz Faktenchecks
Korrektionen Bestattungsgesetz NRW Rangfolge
Berlin Bestatter Review - Hauptprobleme
Hamburg Bestattungsanbieter Überprüfung
Bremen Bestatter Korrektionen: Architektur und Lebensdaten
Bremen Strict Independent Review
Alle Chats
B
Bolle
Max Plan
Erfurt Stadt-Page Review für machsruhig.de
Claude hat die Antwort abgeschlossen
Claude hat geantwortet: Ich fetche die Live-Version und prüfe systematisch.

Ich fetche die Live-Version und prüfe systematisch.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/erfurt/index.html?cb=1779109171346
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/erfurt/index.html?cb=1779109171346

Ich prüfe die kritischen Fakten gegen Primärquellen.

Web durchsucht
Web durchsucht

§ 31 ThürBestG (Ruhezeit) und § 18 (Bestattungspflicht) prüfen. Die Seite nennt § 18 als "Bestattungspflicht mit Rangfolge". Ich prüfe das genauer.

Web durchsucht
Web durchsucht

§ 18 und § 31 ThürBestG passen. Jetzt prüfe ich § 16 (Aufbahrungsfrist 48h) — die Seite schreibt "48 Stunden in Leichenhalle" mit § 16 Abs. 1. Quelle Aeternitas Thüringen sagt aber: "Aufbahrung aus religiösen Gründen § 16 Abs. 2". Das passt. Allerdings: Die Seite behauptet "§ 16 Abs. 1: 48 Stunden". Ich verifiziere das.

Web durchsucht
Web durchsucht

§16 Abs.1 (48h Leichenhalle) und §16 Abs.2 (religiöse Aufbahrung) — bestätigt von Aeternitas. Allerdings: Die Seite nennt im FAQ-Schema § 16 Abs. 1 für die "religiöse Aufbahrung", im sichtbaren FAQ aber korrekt § 1 ThürBestG für die Ehrfurcht. Im sichtbaren Fließtext steht beim Recht-Abschnitt: "längere Aufbahrungen sind aus religiösen oder weltanschaulichen Gründen möglich" — das ist § 16 Abs. 2 (nicht Abs. 1). Im FAQ-Schema: "längere Aufbahrungen aus religiösen oder weltanschaulichen Gründen sind grundsätzlich zulässig, sofern die in § 1 ThürBestG geforderte Ehrfurcht vor den Toten gewahrt bleibt" — das ist nicht falsch, aber unscharf. Kein klarer Fehler.

Ich prüfe einen kritischen Punkt: die Eröffnungsdaten Hauptfriedhof — Schema sagt "1913 angelegt, 1914 geweiht, 1916 offiziell eröffnet". Fließtext: "Eröffnung 8. Juli 1916". Schema-Beschreibung sagt "geweiht 1914" — die Seite (Hero) sagt aber "1916 eröffnet". Schema sagt aber auch "ab 1913 angelegt". Ich check:

Web durchsucht
Web durchsucht

Wichtig: Die offizielle Stadt Erfurt sagt: "erste Beisetzung erfolgte bereits 1914, vor der offiziellen Eröffnung im Jahre 1916." Die Seite ist hier also intern konsistent und mit Quelle vereinbar.

Krematorium Südfriedhof: Die offizielle Quelle erfurt.de sagt das alte Krematorium wurde "1922/23" errichtet und war "noch bis 1977 in Betrieb". Die Page sagt im FAQ "ab 1922/23... bis zur Inbetriebnahme des heutigen Krematoriums [1977] in Nutzung". Konsistent.

Jetzt ein wichtiger Check — § 17 Abs. 3 ThürBestG zur 10-Tage-Frist und 6-Monats-Urnenfrist. Die Seite sagt: "Nach § 17 Abs. 3 ThürBestG müssen Erdbestattung und Einäscherung innerhalb von 10 Tagen erfolgen, die Urne ist binnen 6 Monaten beizusetzen." Aeternitas und Stadtwirtschaft bestätigen das. ✓

Cross-Links prüfen: Die Seite linkt zu /bestatter/weimar/, /bestatter/jena/, /bestatter/gera/. Ich prüfe ob diese existieren.

Web durchsucht, hat einen Befehl ausgeführt
Web durchsucht, hat einen Befehl ausgeführt

403 ist Cloudflare-Bot-Block, kein 404. Ich checke direkt im GitHub-Repo:

3 Befehle ausgeführt
3 Befehle ausgeführt

Domain blockiert. Ich versuche es via web_search/web_fetch:

Fetching: https://machsruhig.de/bestatter/weimar/
Web durchsucht

Keine Treffer für machsruhig.de/bestatter/weimar in Suche — die Stadtseite existiert wahrscheinlich nicht. Aber: Search-Index ist nicht erschöpfend; ein 403 ist nicht definitiv. Gebe diesen Punkt als potenzielles Risiko nur an, wenn ich es klar belegen kann. Da ich es nicht definitiv beweisen kann (kein 404), liste ich es als Hinweis, aber nicht als harten Major-Fund.

Jetzt das Wichtigste — ich prüfe noch FAQ-Schema vs HTML-FAQ-Mismatch:

Im Schema sind 7 Fragen, im HTML sind 8 Fragen (zusätzlich "Was ist beim Besuch des Neuen Jüdischen Friedhofs zu beachten?"). Das ist ein FAQ-Schema vs HTML-FAQ Mismatch — Major.

Zweiter Check: Im Schema sagt das Krematorium-FAQ: "[Krematorium]... wurde nach Plänen des ungarischen Architekten János Szabó in den Jahren 1975 bis 1977 errichtet... Zuvor hatte die Stadt ab 1922/23 ein Krematorium auf dem damaligen Südfriedhof betrieben." Im HTML-FAQ: zusätzlicher Satz "...das nach Schließung des Südfriedhofs noch bis zur Inbetriebnahme des heutigen Krematoriums in Nutzung blieb. Telefonkontakt..." Inhaltliche Erweiterung, kein Widerspruch.

Drittes Detail: Aufbahrung. HTML-FAQ: "längere Aufbahrungen aus religiösen oder weltanschaulichen Gründen sind grundsätzlich zulässig" (kein § genannt für die religiöse Aufbahrung). FAQ-Schema: gleicher Text. Gut.

Aber: Im FAQ-Schema "Was ist eine Sozialbestattung in Erfurt?" hat die Schema-Version mehr Inhalt: "...keine zusätzlichen Wünsche wie aufwendige Grabmale oder Trauerfeiern." Das HTML-FAQ hat das nicht. Kleines Mismatch, aber das HTML-FAQ ist gekürzt → Schema ist legitim umfangreicher. Major-Mismatch ist die fehlende Frage Nr. 8 (Jüdischer Friedhof) im Schema.

Letzter Check: Geldbeträge ohne Stand-Datum (YMYL-Risiko). Die Tabelle nennt "Stammfassung 22.01.2020 (netto)" mit Caption "Seit 01.01.2025 zzgl. 19 Prozent USt". Die Corridor-Angabe "4.500–10.000 Euro" enthält kein Stand-Datum, aber die FAQ-Antwort sagt "inkl. der seit 2025 wirksamen Mehrwertsteuer" → angemessen. Kein klarer YMYL-Verstoß.

Eingemeindung Hochheim: Schema sagt "1938 eingemeindet", Fließtext sagt "1. April 1938", erfurt.de bestätigt 1938. ✓

Jetzt zur formalen Antwort:

STADT: Erfurt VERDICT: PASS mit 1 MAJOR

Fund 1: FAQ-Schema vs sichtbares HTML-FAQ Mismatch

Wo: JSON-LD FAQPage im <head> vs. <section class="mr-faq" id="faq"> im Body
Was: Das JSON-LD enthält 7 Fragen, das sichtbare HTML-FAQ enthält 8 Fragen. Die HTML-Frage "Was ist beim Besuch des Neuen Jüdischen Friedhofs zu beachten?" (Öffnungszeiten, Sabbat-Schließung, Kopfbedeckung, Steine-Brauch) fehlt komplett im Schema. Google's FAQ-Rich-Result-Policy verlangt 1:1-Spiegelung — Mismatch dieser Größe ist ein Strukturfehler, der Rich-Results blockieren oder Manual Action triggern kann.
Fix: Achten Frage als 8. Question-Eintrag ins mainEntity-Array des FAQPage-Blocks aufnehmen, mit Answer-Text aus dem HTML (Werner-Seelenbinder-Str. 3, samstags geschlossen, freitags bis 15 Uhr, Sommer 8–17, Winter bis 16, Männer Kopf bedecken, Steine ablegen, Träger Jüdische Landesgemeinde Thüringen).
Beleg: Google Search Central, FAQ structured data – "the content must be visible to users and match"; erfurt.de bestätigt Datierung 1914 Weihe / 1916 offizielle Eröffnung als korrekt; § 31 Abs. 1 ThürBestG, § 18 und § 16 ThürBestG sind alle korrekt referenziert. 
Erfurt.de + 2

Nebenbefunde unterhalb der MAJOR-Schwelle (nur als Hinweis, nicht Teil des Verdikts): Quelle Nr. 9, 18, 19 im Quellen-Block enden auf .htmc statt .html (Tippfehler in URLs → vermutlich 404 beim Klick). Cross-Links zu /bestatter/weimar/, /jena/, /gera/ konnten in der Stichprobe nicht als existent verifiziert werden, aber auch nicht definitiv als 404 belegt — bitte vor Push manuell prüfen.

(247 Wörter)




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen