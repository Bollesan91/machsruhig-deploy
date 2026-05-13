Neuer Chat
Ctrl+⇧+O
Suchen
Ctrl+K
Chats
Projekte
Code
Anpassen
Design
Mehr
Zuletzt verwendet
Ausblenden
Osnabrück Schwächen und adversariales Scoring
Friedhöfe und Bestattungen in Oberhausen
Leverkusen review score und fix-liste
Friedhöfe in Osnabrück recherchieren und schreiben
Friedhöfe und Bestattungsgesetz in Mülheim an der Ruhr
Chat C Hagen adversarial score evaluation
Leverkusen review und fix-liste
Osnabrück review und bewertung
Mülheim an der Ruhr Review-Bewertung
Oberhausen Schwächen und Adversarial-Score
Friedhöfe und Bestattungen in Hagen
Friedhöfe und Bestattungen in Leverkusen
Friedhöfe und Bestattungen in Leverkusen
Oberhausen SCORE-Review und Fix-Liste
Erfurt v5 final adversarial score evaluation
Freiburg adversarial score evaluation v3
Hagen NRW Schwächen und Adversarial-Bewertung
HTML-Version mit Review-Fixes liefern
Chat C v5 Halle Adversarial Score Evaluation
Erfurt v5 final adversarial score evaluation
Erfurt v5 adversarial score evaluation
Hagen-Review nach SCORE-Tabelle
v4 HTML-Version mit Adversarial-Fixes
HTML-Version v4 mit Adversarial-Fixes
HTML-Version v6 mit BSG-Aktenzeichen-Fixes
HTML-Version mit Review-Fixes liefern
Chat C v3 Halle performance evaluation
Chemnitz v3 adversarial score evaluation
Krefeld v3 adversarial score evaluation
Friedhöfe und Bestattungen in Krefeld
Freiburg Schwächen und adversariales Scoring
Friedhöfe und Bestattungen in Oberhausen
Friedhöfe und Bestattungen in Oberhausen
Hagen-Review nach SCORE-Tabelle
Chat C final adversarial recheck for Halle
Saarbrücken FINAL-Adv-Recheck v6 Bewertung
Erfurt v4 adversarial score evaluation
Alle Chats
B
Bolle
Max Plan
Osnabrück Schwächen und adversariales Scoring
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat C (Adversarial).

Du bist Chat C (Adversarial). v2 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/osnabrueck/v2-from-chat-A.html

Stadt: Osnabrueck (NDS). 3 Schwaechen + ADVERSARIAL-SCORE.

11:54
Claude hat geantwortet: Ich lade v2 und prüfe adversarial.

Ich lade v2 und prüfe adversarial.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/osnabrueck/v2-from-chat-A.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/osnabrueck/v2-from-chat-A.html

Adversarial-Modus. Ich greife die wundesten Punkte an — nicht Stil, sondern Substanz, die einen Audit-Reviewer triggern würde.

🔴 Adversarial Review: v2 Osnabrück
Schwäche 1: Friedhofsgebührensatzung vom 9.12.2025 — Quellenbeleg fehlt komplett

Du zitierst dreimal eine "Friedhofsgebührensatzung der Stadt Osnabrück (Ortsrecht 2.15), Stand 9. Dezember 2025 für das Wirtschaftsjahr 2026" — in Kernfakten, im Recht-Abschnitt und in den FAQ. Im Quellenverzeichnis #6 steht sie als Eintrag, aber ohne Link/URL. Alle anderen 15 Quellen haben anklickbare Belege. Diese eine nicht.

Das ist ein Adversarial-Killshot: Ein Reviewer fragt: "Beweise das Datum 9.12.2025." Du kannst es nicht. Entweder hast du es aus einer Quelle, die du nicht offenlegst, oder du hast es konfabuliert. Beides ist tödlich für Trust.

Verschärfend: Das exakte Datum "9. Dezember 2025" ist hochspezifisch. Wenn das nicht stimmt — z.B. die Sitzung war am 16.12., oder die Satzung gilt erst ab 2027, oder es gibt sie gar nicht in dieser Form — dann zerschlägt eine einzige Faktencheck-Mail an die Stadt die gesamte Glaubwürdigkeit der Seite. Hoch-spezifische unbelegte Daten sind schlimmer als gar keine Daten.

Fix: Entweder URL nachreichen + verifizieren, oder Datum entfernen und durch "die jeweils aktuelle Friedhofsgebührensatzung" ersetzen.

Schwäche 2: Preisspannen im Kosten-Block sind nicht aus der genannten Quelle ableitbar

Du nennst konkrete Spannen:

Grabnutzungsrecht Erdgrab 20 J.: 1.220 – 4.500 €
Urnengrab 20 J.: 990 – 4.300 €
Bestattungsgebühr: 400 – 900 €
Krematoriumsgebühr Heger: 250 – 450 €
Trauerhalle: 180 – 380 €

Diese Zahlen sind ungewöhnlich präzise (1.220, nicht 1.200; 990, nicht 1.000). Das suggeriert: "Ich habe das aus der Gebührensatzung." Aber die Satzung ist nicht verlinkt (siehe Schwäche 1), und in keiner anderen Quelle stehen diese Beträge.

Adversarial-Frage: Woher kommen 1.220 €? Wenn ein Nutzer auf staerkt.osnabrueck.de die echte Gebührensatzung findet und dort steht 1.180 € oder 1.350 €, dann ist die Seite faktisch falsch — nicht nur "veraltet". Das ist Recheck-Blocker Kategorie 3: unsourced specific numerical claims.

Verstärker: Die Caption der Tabelle sagt zwar "Verbindlich sind ausschließlich die Beträge der jeweils aktuellen Friedhofsgebührensatzung" — aber das ist ein Disclaimer, kein Beleg. Honesty-Check würde das als "Hedging um unbelegte Konkretzahlen herum" flaggen.

Fix: Entweder echte Beträge aus der verlinkten Satzung übernehmen, oder Spannen drastisch breiter machen ("ab ca. 1.000 €" / "1.000 – 5.000 €") und im Text klar als "marktübliche Größenordnung in vergleichbaren niedersächsischen Städten" kennzeichnen.

Schwäche 3: "Atter Friedhof" taucht plötzlich auf — widerspricht der eigenen 8er-Liste

In den Kernfakten und der FAQ steht: "acht aktive kommunale Friedhöfe" — namentlich genannt: Heger, Hellern, Lüstringer, Nahner, Pyer, Schinkel, Sutthausen, Dodeshaus. Das sind 8.

Im Fließtext nach Dodeshaus listest du dann zusätzlich:

"sowie der Atter Friedhof (1913 gegründet, rund 8.000 m², kleinster Friedhof der Stadt, im Leyer Holz)"

Und einen Satz später:

"bis zum 1876 eröffneten Eversburger Friedhof an der Kirchstraße."

Das sind plötzlich 10 Friedhöfe, nicht 8. Entweder:

(a) Atter und Eversburg sind unter einem der 8er-Namen subsumiert (dann fehlt die Erklärung)
(b) Sie sind eigenständig (dann ist die "8"-Zahl in Kernfakten + FAQ + JSON-LD FAQPage falsch)
(c) Sie sind nicht-kommunal (dann fehlt der Hinweis, dass sie kirchlich/privat sind)

Adversarial-Killshot: Die FAQ-Antwort im JSON-LD steht 1:1 in den Rich Results bei Google. Wenn dort "8 aktive kommunale Friedhöfe" + namentliche Liste steht, aber im selben Dokument 10 Namen auftauchen, ist das ein internes Widerspruchs-Pattern — genau das, was der bundesland-recheck.py Schritt 4 ("interne Konsistenz") fängt.

Verschärfend: "Eversburger Friedhof an der Kirchstraße" — taucht nirgends sonst im Text auf, kein Schema.org Eintrag, kein Place-Block. Wirkt wie ein eingestreuter Satz ohne Faktenfundament.

Fix: Entweder die "8" auf die tatsächliche Anzahl korrigieren und Liste vereinheitlichen (Kernfakten = Fließtext = FAQ = JSON-LD), oder Atter/Eversburg als "ehemalige Gemeindefriedhöfe, heute Teil von …" klar einordnen.

ADVERSARIAL-SCORE: 68/100

Berechnung:

Dimension	Punkte	Begründung
Quellen-Integrität	11/20	Drei Hochrisiko-Claims (Satzungsdatum, Preisspannen, "8 Friedhöfe") ohne sauberen Beleg. Sonst 15 ordentliche Quellen.
Interne Konsistenz	10/15	Atter/Eversburg-Widerspruch zur 8er-Zahl. JSON-LD und Fließtext divergieren.
§-Präzision & Recht	14/15	§ 11, § 12, § 9 Abs. 2 BestattG sauber. OVG-Beschluss 21.11.2006 korrekt eingeordnet als "alte Rechtslage". Stark.
Lokalkolorit / Substanz	14/15	Sepp Spannmacher, Campo-Santo-Wettbewerb, finnische Jäger, Ruppmann-Etagenöfen — echte Tiefe, keine Floskeln.
Schema.org / Tech-SEO	9/10	@graph sauber, BreadcrumbList korrekt, FAQ-Antworten erben aber den 8-er Widerspruch.
Sprachliche Substanz	10/10	Keine Superlativ-Lyrik, keine "renommierten" Floskeln, keine Pseudo-Tradition.
Honesty-Check (recheck.py-Logik)	0/15	Würde Blocker werfen: Kategorie "unsourced specific numerical claims" (Preise) + "internal contradiction" (Friedhofszahl) + "unverified date specificity" (9.12.2025).

= 68/100

Verdikt: Unter Audit-Ziel ≥85. Drei harte Blocker, alle in einem Pass mit überschaubarem Aufwand fixbar (URL nachliefern + Zahlen weichzeichnen + Friedhofsliste vereinheitlichen). Substanz und Lokalkolorit sind dagegen Premium-Niveau — schade um die handwerklichen Schnitzer bei den Belegen.

Empfehlung für Chat A (Writer-Revision v3): Fix in dieser Reihenfolge: (1) Friedhofsanzahl resolven (Quelle: staerkt.osnabrueck.de listet die kommunalen Friedhöfe vollständig) → (2) Satzungsdatum verifizieren oder generalisieren → (3) Preisspannen ehrlich machen oder belegen.

Dein Nutzungsguthaben ist aufgebraucht. Kaufe mehr, um jetzt weiterzumachen, oder warte bis Donnerstag um 14:00, wenn sich deine Plan-Nutzung zurücksetzt.
Mehr kaufen




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen
Claude is active in this tab group
Open chat
Dismiss