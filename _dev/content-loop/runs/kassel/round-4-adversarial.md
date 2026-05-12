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
Kassel adversarial review und schwächen analyse
Friedhöfe und Gebührensatzung in Oldenburg
Friedhöfe in Lübeck: Bestattungen und Gebühren
Rostock: Schwächen und adversariales Scoring
Friedhöfe und Gebührensatzung in Kassel
Oldenburg: Schwächen und adversariale Bewertung
Lübeck adversarial review und schwächen analyse
Rostock: Schwächen und adversariales Scoring
Kassel-Review nach SCORE-Tabelle
Friedhöfe und Bestattungen in Rostock
Kassel-Review nach SCORE-Tabelle
Oldenburg-Review nach SCORE-Tabelle
Lübeck-Review nach SCORE-Tabelle
Rostock-Review nach SCORE-Tabelle
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
Potsdam adversarial review und schwächen analyse
Friedhöfe und Gebührensatzung in Erfurt
Adversarial review of Magdeburg content
Kiel v4 adversarial score evaluation
Kieler Friedhöfe und Bestattungskultur recherchieren
Saarbrücken v3 Adversarial Score Überprüfung
Potsdam v3 adversarial score evaluation
Magdeburg v3 adversarial score überprüfung
Potsdamer Friedhöfe und Bestattungsgesetze recherchieren
Saarbrücken adversarial review und schwächen analyse
Magdeburg v3 adversarial score überprüfung
Alle Chats
B
Bolle
Max Plan
Kassel adversarial review und schwächen analyse
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat C (Adversarial Reviewer).

Du bist Chat C (Adversarial Reviewer). v2 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/kassel/v2-from-chat-A.html

Stadt: Kassel (Hessen). 3 Schwaechen + ADVERSARIAL-SCORE 0-100%.

18:26
Claude hat geantwortet: Ich lade v2 und prüfe adversarial.

Ich lade v2 und prüfe adversarial.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/kassel/v2-from-chat-A.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/kassel/v2-from-chat-A.html

Adversarial: ich suche, was bei Live-Gang knallt. Fakten-Check der härtesten Behauptungen.

ADVERSARIAL-ANALYSE Kassel v2
Schwäche 1 — FAKTUM-RISIKO: "Anteil Urnenbeisetzungen ca. 65 % (Stand 2015)"

Eine 11 Jahre alte Zahl wird im Keyfacts-Block prominent als Stand-Information präsentiert. Adversarial-Frage: Warum nutzt die Redaktion einen Wert von 2015, wenn überall sonst Stand 2025/2026 zitiert wird? Antwort vermutlich: weil keine neuere Zahl verifiziert vorliegt. Das ist verteidigbar — aber dann muss die Datierung deutlich rausgestellt werden, nicht versteckt in Klammern. Außerdem: Bundesdurchschnitt liegt 2024 bei ~78 %, was eine "65 %"-Zahl für eine Großstadt mit Krematorium niedrig erscheinen lässt. Risiko: Leser googelt, findet aktuellere Vergleichswerte, hält die Seite für veraltet. Fix: entweder Zahl mit explizitem Hinweis "letzte öffentlich kommunizierte Zahl, neuere Erhebung nicht veröffentlicht", oder ganz raus aus Keyfacts und in den Krematorium-Absatz mit Kontext.

Schwäche 2 — UNGESICHERTE BEHAUPTUNG: "Mit eigener Bestattungsvorsorge in Trägerschaft des Stadtkirchenkreises"

Letzter Satz im Bestatter-Abschnitt: "Die Kasseler Friedhofsverwaltung selbst bietet nach eigener Auskunft Bestattungsvorsorgeleistungen in Trägerschaft des Evangelischen Stadtkirchenkreises an – ein in der Bundesrepublik selten gewordenes Modell mit kirchlicher Verlässlichkeit." Drei Probleme: (a) "nach eigener Auskunft" ist eine Quellen-Wieselformel ohne Beleg in der Quellenliste — keiner der 17 Belege deckt diese Aussage; (b) "selten gewordenes Modell mit kirchlicher Verlässlichkeit" ist eine Wertung im Werbeton, die in einem neutralen Ratgeber nichts verloren hat — verstößt gegen den Stil der restlichen Seite; (c) rechtliches Risiko: wenn der Stadtkirchenkreis Bestattungsvorsorge anbietet, müsste das nach §§ Bestattungsvorsorgeverträge insolvenzgesichert sein — bevor wir das so behaupten, brauchen wir einen Beleg. Fix: Satz streichen oder durch belegte, neutrale Formulierung ersetzen.

Schwäche 3 — SCHEMA.ORG / SEO-INKONSISTENZ: FAQ-Antworten weichen vom sichtbaren Text ab

Die FAQ im sichtbaren Body ist an mehreren Stellen detaillierter als die FAQPage-Schema-Antworten (Beispiele: Erdbestattungs-Frage nennt sichtbar "rund 4.015 Euro Summe", Schema nicht; Ruhezeit-Frage nennt sichtbar die 5-Jahres-Verlängerung für 217,50 €, Schema nicht; Sterbeurkunde-Frage nennt sichtbar Telefon 0561 115, Schema nicht). Google verlangt seit März 2024, dass FAQ-Schema exakt dem sichtbaren Text entspricht, sonst Rich-Result-Penalty oder gar manuelle Maßnahme. Adversarial: Search Console wirft Warnung, Rich-Result fällt weg, FAQ-Sichtbarkeit kippt auf 0. Fix: Schema-FAQ-Antworten 1:1 an Body-FAQ angleichen — entweder Body kürzen oder Schema erweitern (Schema erweitern ist sicherer).

Bonus-Knackpunkt (sub-blocker)

"Stand: Mai 2026" + "datePublished 2026-05-12" + "dateModified 2026-05-12" — alle drei identisch. Bei einer Seite, die so viele 2025-er Rechtsstandsdaten zitiert, sieht das nach JIT-Generierung aus. Glaubwürdiger: datePublished auf das tatsächliche Erstpublikationsdatum setzen, dateModified auf heute.

ADVERSARIAL-SCORE: 82/100

Begründung: Der Text hält einer harten Prüfung weitgehend stand — Primärquellen vorhanden, §-Zitate konsistent, Friedhöfe verifizierbar, FBG-Stand korrekt. Die drei Schwächen sind vermeidbare Live-Risiken: Schwäche 2 ist ein klares Blocker-Risiko (unbelegte Werbeaussage über Vorsorge-Produkt), Schwäche 3 ist SEO-technisch kritisch (FAQ-Schema-Mismatch kann zu manueller Maßnahme führen), Schwäche 1 ist kosmetisch (alte Zahl prominent platziert). Mit Fix dieser drei Punkte: 90+.

Go-Live-Empfehlung: Nicht ohne Fix von Schwäche 2 und 3. Schwäche 1 darf bleiben, sollte aber transparent datiert werden.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen