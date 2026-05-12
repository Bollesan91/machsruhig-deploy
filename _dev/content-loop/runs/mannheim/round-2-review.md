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
Mannheim-Content Review nach SCORE-Kriterien
HTML-Seite für Bestatter Mannheim erstellen
HTML-Seite für Bestatter in Karlsruhe
HTML-Seite für Bestatter in Münster erstellen
Machsruhig.de Münster Review und Scoring
HTML-Seite für Bestatter in Düsseldorf erstellen
HTML-Seite für Bestatter in Bonn erstellen
HTML-Seite für Bestatter Stuttgart erstellen
Adversarial Review für machsruhig.de Stuttgart
HTML-Seite für Bestatter in Bonn erstellen
HTML-Seite für Bestatter Bielefeld erstellen
HTML-Seite für Bestatter Wuppertal erstellen
HTML-Seite für Bestatter in Bochum erstellen
HTML-Seite für Bestatter in Duisburg erstellen
HTML-Seite für Bestatter Nürnberg erstellen
HTML-Seite für Bestatter Hannover erstellen
HTML-Seite für Bestatter Dresden erstellen
HTML-Seite für Bestatter Bremen erstellen
HTML-Seite für Bestatter Essen erstellen
HTML-Seite für Bestatter in Dortmund erstellen
HTML-Seite für Bestatter Leipzig erstellen
HTML-Page Review für Stuttgart
Machsruhig.de Düsseldorf-Seite reviewen
Machsleicht project setup and priority planning
Admin-Rechte für Microsoft-365-App-Freigaben
💬 Beschreib mir mal den Batch ur…
HTML-Seite für Bestatter Köln erstellen
HTML-Page für Bestatter Hamburg erstellen
Adversarial review für machsruhig.de Köln
HTML-Seite für Bestatter Frankfurt erstellen
HTML-Page für Bestatter Berlin erstellen
Alle Chats
B
Bolle
Max Plan
Mannheim-Content Review nach SCORE-Kriterien
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). Lies das Briefing: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md und dann v1: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/mannheim/v1-from-chat-A.html

Stadt: Mannheim (BW). Review streng nach SCORE-Tabelle (E-E-A-T, Quellen, Friedhof-Tiefe, Recht-Knappheit). Vergib SCORE 0-100% und gib konkrete Fix-Liste fuer v2.

10:37
Claude hat geantwortet: Ich lese das Briefing und v1.

Ich lese das Briefing und v1.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md

Briefing gelesen. Jetzt v1:

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/mannheim/v1-from-chat-A.html

Briefing bestätigt: BRIEFING_OK

SCORE: 76%

GAP:

§-Verweise zum BestattG BW fehlen komplett im Text. Sektion "Bestattungsrecht" nennt nur § 32 BestattG BW (Sargpflicht-Ausnahme) und verweist sonst auf die BW-Landesseite. Für eine Stadtseite mit eigenständigem Recht-Abschnitt müssen mindestens 3-4 § konkret zitiert sein (z.B. § 26 BestattG BW Bestattungsfrist, § 32 Sargpflicht, § 33 Aschen/Friedhofszwang). Aktuell wirkt das wie eine Auslagerung.
Ruhezeit ist mit "UNSURE"-Kommentar als Vermutung markiert ("typischerweise zwischen 20 und 30 Jahren"). Das ist für eine Primärquellen-Page nicht akzeptabel. Entweder Wert aus aktueller Mannheimer Friedhofssatzung beziehen und mit § zitieren, oder Sektion ganz streichen. Aktuell ist es eine unsourced Aussage mit Hedge.
Bestattungskosten-Sektion ist die schwächste der Page: konkrete Mannheimer Beträge fehlen, "vierstelliger Bereich (1.600 bis 2.400 Euro)" ist mit UNSURE markiert und ohne Quelle. Stiftung-Warentest-Verweis hat keinen Link und keinen Stand. Mindestens 1 verifizierter Mannheim-spezifischer Wert (z.B. aktuelle Gebührensatzung-PDF) ist Pflicht — sonst ist die Sektion eine generische Floskel-Aussage in lokalem Mantel.
Wallstadt-Korrektur "nicht in Wallstadt, sondern in Wohlgelegen" ist im Fließtext erklärungsbedürftig: woher kommt die Verwechslung? Wenn kein Kontext geliefert wird, sollte der Satz raus oder mit Quelle versehen. Aktuell wirkt es wie ein internes Memo, das nach außen sichtbar wurde.
Friedhof-Tiefe: 3 Friedhöfe ist erfüllt, aber die Top-7 städtischen Friedhöfe neben Hauptfriedhof + Käfertal werden gar nicht genannt. Bei "10 städtische Friedhöfe" erwartet der Leser mindestens eine Liste/Tabelle der übrigen 8 (Sandhofen, Neckarau, Friedrichsfeld, Rheinau etc.) mit Stadtteil und ggf. Größe. Sonst bleibt die Zahl "10" abstrakt.
Hauptfriedhof-Sektion erschlägt mit Persönlichkeiten-Liste (12 Namen in einem Absatz). Das ist Friedhofs-Folklore, kein Hidden-Gem. Empfehlung: auf 2-3 mit echter Geschichte (Bassermann + Vormärz-Kontext, Sand/Kotzebue-Story) kürzen und den Rest streichen oder als Tabelle "Bedeutende Grabstätten" auslagern.
Hidden-Gem Sand/Kotzebue ist stark, aber die Behauptung "Täter und Opfer auf demselben Friedhof bestattet" braucht eine Quelle. Sand wurde 1820 hingerichtet — vor Eröffnung des Hauptfriedhofs 1842. Wurde er umgebettet? Wenn ja, wann und woher? Ohne diesen Beleg ist die Story angreifbar.
Jüdischer Friedhof: 31 Grabsteine aus F7 (Bastion St. Judas) ist ein konkretes Detail — Quelle dafür fehlt aber in der Quellenliste explizit (nur generischer Wikipedia-Link). Genauso "Vereinbarung von 1839" — primärquellig nicht abgesichert.
Quellen-Liste enthält 4 Wikipedia/Wiki-Links (Wikipedia Hauptfriedhof, Wikipedia Jüdischer Friedhof, Rhein-Neckar-Wiki, HMDB). Das ist für eine Primärquellen-Page zu sekundärquellen-lastig. Mindestens 2 sollten durch echte Primärquellen ersetzt werden: Stadtarchiv Mannheim, Marchivum (Mannheims Stadtarchiv), Eigenbetrieb-PDF zur Friedhofssatzung. Aktuell ist die Page faktisch ein Wikipedia-Rewrite mit lokaler Friedhofsverwaltungs-Garnitur.
Quadratestadt-Sektion (eigener H2-Block) ist tematisch off-topic für eine Bestattungs-Stadtseite. Der Bezug zu Bestattung (Standesamt N1, alter Friedhof F7) ist dünn. Vorschlag: in 2 Sätze in Hauptfriedhof- oder Behörden-Sektion integrieren statt eigener Abschnitt. Aktuell wirkt es wie Stadtmarketing.
FAQ-Schema im JSON-LD hat einen Syntax-Fehler: {"@type":"Question">,"name":... — das > ist ungültiges JSON. Wird beim Schema-Validator (Google Rich Results Test) als Fehler markiert und kann das gesamte FAQPage-Schema invalidieren. Muss vor Deploy korrigiert werden.
HTML-Kommentare <!-- UNSURE: ... --> (3 Stück) sind im ausgelieferten HTML sichtbar — auch wenn sie nicht gerendert werden, sind sie im Quelltext und über View-Source einsehbar. Für eine Produktiv-Page ein No-Go. Müssen vor v2 entweder durch verifizierte Werte ersetzt oder die Aussagen umformuliert/gestrichen werden.
Friedhofs-Highlights: Käfertal-Sektion hat solide Geschichte (Jakob Kramp, 60 Gulden, 22.555 m²), aber die Otto-Siffling-Erwähnung ist sehr knapp. Wenn schon Siffling, dann mit 1 Satz Story: warum 12-facher Nationalspieler? Tod mit 27? Mannheim-Mythos? Aktuell ist es eine Aufzählung.
Trauerhalle Käfertal "67 Sitzplätze, überdachter Vorplatz" — Quelle fehlt. Solche konkreten Werte gehören entweder mit Quelle in den Quellenblock oder müssen raus.
Cross-Links: nur 4 interne Links (BW-Landesseite, Bestattungskosten, Checkliste, Methodik). Bei einer Stadtseite dieser Tiefe erwartet man 6-8 Cross-Links — fehlen u.a. zu /bestattungsarten, /trauerrede-schreiben, /kondolenzschreiben, /tools/vorsorge-check sowie zu Nachbarstädten (Heidelberg, Ludwigshafen — falls vorhanden) oder zur BW-Übersicht.
Wortzahl: ~1.900 Wörter im Body (geschätzt). Liegt im unteren Korridor. Ziel 2000-2500 würde mit den fehlenden Sektionen (übrige 8 Friedhöfe als Tabelle, Bestattungskosten ausgebaut, §-Verweise konkret) erreicht.
Bestatter-Wahl-Sektion: "Bestatterverband Baden-Württemberg" mit UNSURE-Kommentar zum Namen. Der korrekte Name ist "Landesinnung der Bestatter Baden-Württemberg" bzw. "Landesverband der Bestatter Baden-Württemberg" — vor Veröffentlichung verifizieren und UNSURE entfernen.
Footer-Copyright &copy; 2024–2026 — Page selbst trägt Stand "12. Mai 2026", also passt 2026. Aber: kein E-E-A-T-Indikator wie Autorenangabe mit Profil-Link, kein Impressum-Link im Footer sichtbar (nur Methodik). Für YMYL-Thema (Bestattung) ist das ein Vertrauens-Defizit.
Sektion "Bestattungskosten" wiederholt zweimal denselben Punkt ("Friedhofsgebühren regelt die kommunale Friedhofs- und Gebührenordnung"). Redundanz, die für eine eigenständige Cost-Sektion zu wenig Substanz hinterlässt.




Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die Antworten.
Teilen
 Claude is active in this tab group  
Open chat
 
Dismiss