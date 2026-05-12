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
Lübeck-Review nach SCORE-Tabelle
Friedhöfe und Gebührensatzung in Kassel
Friedhöfe und Gebührensatzung in Oldenburg
Friedhöfe und Bestattungen in Rostock
Friedhöfe in Lübeck: Bestattungen und Gebühren
Friedhöfe und Gebührensatzung in Kassel
Friedhöfe und Gebührensatzung in Erfurt
Saarbrücker Friedhöfe recherchieren und dokumentieren
Lübecks Friedhöfe und Bestattungsregeln
Freiburg content review nach SCORE-Tabelle
Erfurt Schwächen-Analyse mit Adversarial Review
Chat C v4 Saarbrücken Bewertung
Magdeburg v4 performance evaluation
Friedhöfe und Bestattungsgebühren in Freiburg
Magdeburger Friedhöfe recherchieren und dokumentieren
Erfurt content review nach SCORE-Tabelle
Saarbrücken v3 Adversarial Score Überprüfung
Potsdam v3 adversarial score evaluation
Magdeburg v3 adversarial score überprüfung
Potsdamer Friedhöfe und Bestattungsgesetze recherchieren
Magdeburg v3 adversarial score überprüfung
Saarbrücken adversarial review und schwächen analyse
Potsdam adversarial review und schwächen analyse
Friedhöfe und Gebührensatzung in Erfurt
Adversarial review of Magdeburg content
Kiel v4 adversarial score evaluation
Kieler Friedhöfe und Bestattungskultur recherchieren
Potsdam content review nach SCORE-Tabelle
Saarbrücken content review nach SCORE-Tabelle
Kiel v3 Bewertung: Adversarial-Score-Überprüfung
Magdeburg-Review nach SCORE-Tabelle
Alle Chats
B
Bolle
Max Plan
Lübeck-Review nach SCORE-Tabelle
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). Lies Briefing https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md und v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/luebeck/v1-from-chat-A.html

Stadt: Luebeck (Schleswig-Holstein). Review nach SCORE-Tabelle. SCORE 0-100% + Fix-Liste.

17:57
Claude hat geantwortet: Ich lade Briefing und v1.

Ich lade Briefing und v1.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Web durchsucht

BRIEFING_OK

SCORE: 74%

GAP:

§ 16 BestattG SH falsch zitiert. Im Text steht „§ 16 Abs. 1: 48-h-Frist; § 16 Abs. 3: Urnenfrist 1 Monat" — das BestattG SH regelt die Bestattungsfristen tatsächlich in § 16 (Bestattungsfristen), die 48-Stunden-Wartefrist steht aber in § 16 Abs. 2, nicht Abs. 1. Absatz-Nummern müssen am Primärtext (juris-Link in Quelle 4) verifiziert werden, sonst kippt der Honesty-Check.
„§ 15 BestattG SH = Sargpflicht" ist falsch verortet. § 15 BestattG SH regelt die Bestattungsarten/Bestattungsorte; die Sargpflicht für Erdbestattungen ergibt sich aus § 14 (Anforderungen an Särge und Urnen) bzw. dem Kontext der Bestattungsarten. FAQ und Fließtext sagen beide „§ 15 = Sargpflicht" — das ist eine Wiederholung desselben Fehlers an zwei Stellen und für die Honesty-Check-Kategorie „Unsourced legal claim with wrong paragraph" ein Blocker.
Reerdigung-Behauptung „seit 2024 als erstes Bundesland" nicht belegt. Die Aussage taucht 2× auf (Fließtext + FAQ), in den Quellen findet sich aber kein Beleg dafür, dass das BestattG SH 2024 entsprechend novelliert wurde. Entweder konkreten Änderungsnachweis (Datum, GVOBl-Fundstelle) ergänzen oder Aussage entschärfen.
§ 10 Abs. 1 BestattG SH zu „36-Stunden-Überführung in Leichenraum" prüfen. Diese Frist und der Paragraph stehen ohne Querverweis zur Primärquelle im Schritte-Block. Wahrscheinlich korrekt, aber Recheck-Script wird das markieren — § und Absatz an juris verifizieren.
Floskel/Werbe-Sprache „Lübecker Bucht / RuheForst / Alvarien". Im Bestatter-Wahl-Block: „Reerdigung in einem der schleswig-holsteinischen Alvarien" — „Alvarien" ist kein etabliertes deutsches Wort für Reerdigungsstätten (gemeint vermutlich „Alvarium" der Firma Meine Erde, aber das ist ein Produktname/Markenbegriff, nicht eine Anlagengattung). Entweder konkret „in der Reerdigungsanlage in Mölln (Meine Erde)" oder Begriff streichen.
Burgtorfriedhof Ehrengräber-Zahl widersprüchlich. Im Meta-Block steht „131 Ehrengräber", im Fließtext „13 Ehrengrabstätten und vier Kriegsgräber … 2018 kam eine 14. hinzu". 131 vs. 14 ist ein Faktor-10-Widerspruch innerhalb derselben Sektion. Eine der beiden Zahlen ist falsch.
St. Jürgen Kapellen-Datum inkonsistent. Meta sagt „Kapelle von 1646", Fließtext sagt „zuletzt 1645 an die heutige Stelle … Einweihung am 31. August 1646". OG-Description sagt „St. Jürgen (1645/1904)". 1645 (Versetzung) und 1646 (Einweihung) sind beide korrekt, aber die Inkonsistenz zwischen Meta/OG/Fließtext muss im Recheck als „date_mismatch" durchgehen — alle drei Stellen auf eine Form vereinheitlichen.
Marianne Bachmeier Faktencheck. Text sagt „erschoss 1981 im Lübecker Landgericht den mutmaßlichen Mörder ihrer Tochter Anna". Tochter hieß Anna, ja — aber der Tatort war das Landgericht Lübeck (korrekt), Jahr 1981 (korrekt). Aussage „Mutter und Tochter liegen seit 2017 wieder unter einer gemeinsamen Grabplatte" braucht Beleg (welche Quelle? Wikipedia Burgtorfriedhof? Lübecker Nachrichten?). Aktuell unsourced.
Friedhofsgebühren-Tabelle ohne Stand-Jahr und Satzungsverweis pro Zeile. „ca. 1.280 – 4.950 €" ist eine Spanne, aber ohne expliziten Hinweis „Stand: Friedhofsgebührensatzung vom 31.03.2015 i.d.F. von [letzter Änderung]". Wenn die letzte Änderung 2023 oder 2024 war, gehört das in die Tabellen-Caption — sonst wirkt die Spanne wie geschätzt, nicht zitiert.
„Niederländische Ehrengräberstätte 2.678 Kriegsgräber" — Zahl verifizieren. Volksbund (Quelle 10) ist verlinkt, gut. Aber die Zahl 2.678 sollte mit Stand-Jahr versehen sein, und „elf Nationen" ist sehr konkret — wenn Volksbund eine andere Zahl nennt, kippt der Recheck.
Cross-Links dünn. Genau ein Cross-Link auf /bestattung-in/schleswig-holstein/. Keine Links zu anderen SH-Städten (Kiel, Flensburg, Neumünster — falls vorhanden) und keine Links auf Themen-Seiten (z.B. Seebestattung, Reerdigung, Vorsorge). Die anderen Bundesland-/Stadt-Pages haben typischerweise 3–5 Cross-Links.
Verwaltungs-Öffnungszeiten ohne Quelle. „montags, dienstags und donnerstags 8–14 Uhr, mittwochs und freitags 8–12 Uhr" — kein Link, kein Stand. Öffnungszeiten ändern sich; entweder mit luebeck.de-Direktlink oder weglassen und auf die Verwaltungs-URL verweisen.
Wortzahl knapp unter Ziel-Korridor. Grob geschätzt ca. 1900–2000 Wörter Fließtext (ohne Tabelle, FAQ, Quellen). Liegt am unteren Rand des 2000–2500-Korridors. Ausbau-Kandidaten: Bestattungskosten-Sektion (Bestatterleistungen aufschlüsseln), Bestatter-Wahl-Sektion (konkrete Innungs-Mitgliedsbetriebe-Statistik SH), Reerdigung in SH eigener Absatz mit Quelle.
Hidden Gem Waldhusen ist die schwächste der vier. „Einer der schönsten Friedhöfe Norddeutschlands" ist ein Zitat ohne klare Quelle (welche Stelle der Hansestadt-Darstellung sagt das wörtlich?). Die anderen drei Hidden Gems (Kriegsgräber, Familie Mann, Lillie-Klassizismus) sind faktisch dicht — Waldhusen ist nur ein Lob-Zitat ohne Anker. Entweder konkretes Detail (welche Baumart prägt? wer pflegt? welcher Soldatenfriedhof-Block?) oder Hidden Gem entfernen.
Schema.org Place ohne geo-Koordinaten. Alle vier Friedhof-Place-Einträge haben PostalAddress, aber kein geo: { latitude, longitude }. Für Local-SEO ein vermeidbares Loch — die anderen Bundesland-Pages auf machsruhig haben Geo-Koordinaten in Place-Entities.
Title-Tag und H1 nicht parallel zu anderen Stadt-Pages prüfen. Title: „Bestattung in Lübeck — Friedhöfe, Kosten, Recht | machsruhig" — gut. Aber ist das das verwendete Title-Muster bei den anderen Stadt-Pages (Hamburg, Kiel etc.)? Wenn dort z.B. „Bestattung Lübeck: …" steht, muss Lübeck dem Muster folgen.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen
 Claude is active in this tab group  
Open chat
 
Dismiss