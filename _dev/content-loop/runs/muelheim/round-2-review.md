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
Mülheim an der Ruhr Review-Bewertung
Friedhöfe und Bestattungen in Leverkusen
Friedhöfe und Bestattungen in Hagen
Friedhöfe und Bestattungen in Leverkusen
Friedhöfe und Bestattungsgesetz in Mülheim an der Ruhr
Friedhöfe in Osnabrück recherchieren und schreiben
Friedhöfe und Bestattungen in Oberhausen
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
Freiburg Schwächen und adversariales Scoring
Friedhöfe und Bestattungen in Oberhausen
Friedhöfe und Bestattungen in Oberhausen
Hagen-Review nach SCORE-Tabelle
Chat C final adversarial recheck for Halle
Erfurt v4 adversarial score evaluation
Saarbrücken FINAL-Adv-Recheck v6 Bewertung
HTML-Version v6 mit BSG-Aktenzeichen-Fixes
HTML-Version mit Review-Fixes liefern
Chat C v3 Halle performance evaluation
Chemnitz v3 adversarial score evaluation
Friedhöfe und Bestattungen in Krefeld
Krefeld v3 adversarial score evaluation
Alle Chats
B
Bolle
Max Plan
Mülheim an der Ruhr Review-Bewertung
Claude hat die Antwort abgeschlossen
Du hast gesagt: Du bist Chat B (Reviewer).

Du bist Chat B (Reviewer). v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/muelheim/v1-from-chat-A.html

Stadt: Muelheim an der Ruhr (NRW). Review SCORE 0-100% + Fix-Liste.

11:42
Claude hat geantwortet: Ich lade v1 und reviewe.

Ich lade v1 und reviewe.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/muelheim/v1-from-chat-A.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/muelheim/v1-from-chat-A.html

Ich gehe in den Reviewer-Modus: Faktencheck gegen Primärquellen, Schema-Check, Honesty-Audit. Ich prüfe gezielt die heikelsten Behauptungen.

Verifikationsläufe:

Fetching: https://de.wikipedia.org/wiki/Hauptfriedhof_M%C3%BClheim_an_der_Ruhr
Fetched: Hauptfriedhof Mülheim an der Ruhr

Mehrere Faktenabweichungen identifiziert. Weiter:

Fetching: https://de.wikipedia.org/wiki/Altstadtfriedhof_(M%C3%BClheim_an_der_Ruhr)
Fetched: Altstadtfriedhof (Mülheim an der Ruhr)

Mehrere kritische Faktenabweichungen bestätigt. Jetzt noch BestG NRW gegenchecken:

Searching the web
Web durchsucht

Genug Daten. Ich habe alles, was ich brauche, um einen sauberen Review zu schreiben. Jetzt strukturiert auswerten:

REVIEW v1 — Mülheim an der Ruhr

Reviewer: Chat B (frischer Kontext, ohne Autoren-Bias) Quellen-Cross-Check: Wikipedia Hauptfriedhof + Altstadtfriedhof, RECHT.NRW (§ 13), Stadt Mülheim, Caritas NRW, Aeternitas.

SCORE: 74 / 100

Solide Grundstruktur, gute Quellenbasis, lokale Texturhinweise (Patenschaftsmodell, muslimisches Grabfeld 1996, Marcks-Mahnmal). Aber: mehrere sachliche Fehler, davon zwei harte Faktenkrater und ein erfundenes "Hidden Gem". Das ist im Live-Honesty-Check nicht go-live-fähig.

BLOCKER (P0) — must-fix vor Deploy
B1. ❌ Theodor Suhnel als Portal-Architekt — Quelle widerspricht eigenem Text

Stelle: Hauptfriedhof-Abschnitt: "Den ersten Preis erhielt der Mülheimer Architekt Theodor Suhnel mit dem Motto […]. Der ausgeführte Entwurf 'Grünumhegt' stammt jedoch von den zweitplatzierten Landschaftsarchitekten Friedrich Bauer und Walter Günther…" Problem: Wikipedia sagt klar: "Das um 1928 von dem Architekten Theodor Suhnel erbaute und 1984–1986 restaurierte Portal steht unter Denkmalschutz." Suhnel hat das Portal (um 1928) gebaut, nicht den Wettbewerb 1915 verloren. Die Wettbewerb-Story mit Motto „Den Toten zur Ruh…" und Fritz Keßler ist nicht in den verlinkten Quellen belegbar — möglicherweise teilweise korrekt aus Hans Weber (1993), aber im jetzigen Text widersprüchlich (Suhnel kann nicht 1915 Erstplatzierter sein und 1928 das Portal bauen, ohne dass das erklärt wird). Fix: Komplett umschreiben auf das, was Wikipedia/Stadt belegen: Anlage 1915 von Bauer/Günther geplant, 1916 eröffnet, Portal um 1928 von Suhnel, 1984–86 restauriert. Wettbewerbsgeschichte streichen, sofern nicht aus Primärquelle (Hans Weber 1993) belegbar. Fritz Keßler / Bäume streichen. 
Wikipedia

B2. ❌ "Hidden Gem" Hauptfriedhof — vermutlich erfunden

Stelle: „Auf dem Hauptfriedhof befindet sich ein von der Familie Thyssen unterhaltenes Grab für 17 Frauen, die am 17. Juli 1917 um 17 Uhr…" Problem: Keine Quelle, keinerlei Beleg. Riecht stark nach Halluzination (zu sauber, zu poetisch, zu spezifisch). Die einzige bekannte Mülheimer Industrie-Explosion mit Frauenopfern ist die Pulverfabrik Empelde — nicht Mülheim/Ruhr. Risiko: wenn falsch, frisst die Story die Glaubwürdigkeit der ganzen Seite auf. Fix: Streichen oder durch belegbares Hidden Gem ersetzen. Belegbare Kandidaten aus Quellen: Karl Ziegler (Nobelpreisträger Chemie, hier bestattet), Erkenntnis aus Buch/Rautenberg/Keil 2021: 311 Wildpflanzenarten = ein Sechstel der NRW-Flora, 1000 m² muslimisches Grabfeld seit 13.06.1996.

B3. ❌ Falsche Pflanzenarten-Zahl Broich

Stelle: "Im Rahmen des LVR-Projekts 'Biodiversität auf Friedhöfen…' wurden 2024 auf dem Friedhof Broich 267 verschiedene Wildpflanzenarten nachgewiesen" Problem: Die 311-Arten-Zahl gehört zum Hauptfriedhof (Buch/Rautenberg/Keil 2021, Jahrbuch 2022), nicht zu Broich. KuLaDig-Quelle für Broich (#15 in der Liste) sollte verifiziert werden — die genaue Zahl 267 ist mit dem aktuellen Quellenstand nicht belegt. Das ist genau das, was der Bundesland-Recheck-Script ("unsourced superlative" / Faktenmix) abfangen würde. Fix: Entweder echte Quelle nennen + Zahl prüfen, oder die Zahl streichen und allgemeiner formulieren ("artenreich", "Magerrasenarten dokumentiert"). Wenn die 311-Zahl gemeint war, dann auf Hauptfriedhof verlagern (B2-Fix).

B4. ❌ Joseph Thyssen Todesort

Stelle: „Joseph Thyssen (Industrieller, Bruder August Thyssens, †1915 in Mülheim)" Problem: Wikipedia listet ihn unter den auf dem Altstadtfriedhof bestatteten Personen — aber bestattet ≠ in Mülheim gestorben. Die Behauptung "†1915 in Mülheim" ist nicht durch die zitierten Quellen gedeckt. Joseph Thyssen starb tatsächlich am 24.04.1915 in Mülheim, das stimmt vermutlich, aber wenn nicht aus zitierter Quelle herleitbar, muss es raus oder mit Quelle versehen. Gleiches gilt für Troost †1830 (nicht im Wiki-Auszug enthalten). Fix: Sterbedaten ohne explizite Quelle streichen — reicht „Joseph Thyssen (Industrieller, Bruder August Thyssens)".

B5. ❌ Zwangsarbeiter-Zahlen Altstadtfriedhof — präzise Zahlen ohne Quelle

Stelle: „389 russische, 11 polnische und ein tschechischer Kriegstoter" Problem: Diese exakten Zahlen sind in keiner der zitierten Quellen auffindbar. Wikipedia spricht nur allgemein von "Gräber der Opfer von Krieg und Gewaltherrschaft – überwiegend russische Zwangsarbeiter die der Gewaltherrschaft der NSDAP 1933–1945 zum Opfer fielen". Auch das Marcks-Mahnmal markiert den Nordteil als Mahnmal für beide Weltkriege, nicht primär den Zugang zum Zwangsarbeitergräberfeld. Fix: Zahlen entfernen oder konkrete Quelle ergänzen (Geschichtsverein-Publikation?). Marcks-Mahnmal korrekt als „Ehrenmal für die Gefallenen beider Weltkriege" (1968) bezeichnen — nicht als Zugang zum Zwangsarbeiter-Feld. 
Wikipedia

P1 — sollte vor Deploy
P1.1 Altstadtfriedhof Bestattungs-Status

Stelle: Im Friedhofs-Block steht „nicht aktiver Bestattungsort" → richtig für Reihen-/Wahlgräber, aber Urnenbestattungen sind seit 1988 wieder möglich (Patenschaftsmodell). Im Text wird das erwähnt, aber die einleitende Liste „8 aktiv für Bestattungen" zählt Altstadt implizit nicht dazu. Das ist inkonsistent: wenn Patenschaft-Urnenbeisetzungen erlaubt sind, ist Altstadt eingeschränkt aktiv. Fix: Klarer trennen: "8 für reguläre Beisetzungen offen + Altstadtfriedhof eingeschränkt über Patenschaftsmodell" — und in FAQ konsistent.

P1.2 § 1 BestG NRW falsch zitiert

Stelle: „Nach § 1 BestG NRW dürfen nur Gemeinden und Religionsgemeinschaften des öffentlichen Rechts Friedhöfe betreiben" Problem: Seit Novellierung kann Trägerschaft auch an gemeinnützige Religionsgemeinschaften übertragen werden (§ 1 Abs. 5 BestG nF), und private Friedhofsträgerschaft ist via Beleihung möglich (§ 1 Abs. 4 BestG nF). Fix: Präzisieren: "primär Gemeinden und Religionsgemeinschaften des öffentlichen Rechts, in Ausnahmefällen Beleihung Privater möglich".

P1.3 Sterbefall-Frist „drei Werktage" / Personenstandsgesetz § 28 ff.

Stelle: „§ 28 ff. Personenstandsgesetz und die örtliche Praxis verpflichten dazu, einen Sterbefall innerhalb von drei Werktagen…" Problem: Sterbefallanzeigefrist ist § 28 PStG („spätestens am dritten auf den Tod folgenden Werktag"). Formulierung ist okay, aber „§ 28 ff." ist unscharf. Außerdem: dass Kliniken/Heime selbst melden, regelt § 30 PStG (Anzeige durch Einrichtungen). Fix: Auf „§ 28 PStG" zuspitzen und § 30 PStG für Einrichtungen ergänzen.

P1.4 Gebührenkorridore (1.285–2.900 €) — UNSURE-Marker im Text

Stelle: HTML-Kommentar: <!-- UNSURE: Einzelpositionen der Satzung 2022 wurden nicht im Volltext eingesehen… --> Problem: Autor gibt selbst zu, die Satzung nicht im Volltext eingesehen zu haben — der Bundesland-Recheck würde das als „Korridor ohne Primärquelle" markieren. Bund-der-Steuerzahler-NRW-Quelle bestätigt zwar „>4.000 € Gesamt", aber die einzelnen Korridore stehen so nicht in den verlinkten Quellen. Fix: Entweder Satzung tatsächlich öffnen und Einzelpositionen zitieren, oder Tabelle entschärfen auf "Gesamtkosten Sargwahlgrab ca. 4.000–5.500 € (BdSt NRW 2024)" ohne Aufspaltung in Grabnutzung/Beisetzung. Den HTML-Kommentar entfernen — der gehört nicht in produktives HTML.

P1.5 Holthausen ≠ Holthausen

Stelle: „Hauptfriedhof an der Zeppelinstraße in Holthausen" Problem: Wikipedia verlinkt von „Mülheim-Holthausen" auf Menden-Holthausen — das ist ein Wiki-Bug, aber der Hauptfriedhof liegt tatsächlich in Holthausen (Mülheim), das stimmt. Der „Holthausener Friedhof" (Röntgenstraße 7–11) liegt ebenfalls in Holthausen aber ist eine separate Anlage. Das ist im Text nicht falsch, aber verwirrend dargestellt: Hauptfriedhof Holthausen vs. „Holthausener Friedhof" geschlossen — zwei Friedhöfe im selben Stadtteil, einer aktiv, einer historisch. Fix: Im Text explizit klarstellen, dass es zwei verschiedene Anlagen in Holthausen sind. Sonst wirken die Aussagen widersprüchlich.

P1.6 Konfessionelle Friedhöfe — Aufzählung

Stelle: „Alt-Katholische Kolumbarium und der jüdische Friedhof" Problem: Nicht durch zitierte Quellen belegt. Existieren beide vermutlich, aber im Quellen-Set nicht nachgewiesen. Fix: Belegen oder allgemeiner formulieren ("konfessionelle Begräbnisstätten der christlichen und jüdischen Gemeinde").

P2 — Polish
„denkmalgeschütztes Portal stammt aus der Zeit um 1928" im Keyfact-Block fehlt → ergänzen, hier ist die Quelle eindeutig.
Karl Ziegler (Nobelpreisträger Chemie, Hauptfriedhof) fehlt komplett in „Bedeutende Bestattete" → drin haben! Stark belegt durch Wikipedia.
Paul Lembke (Oberbürgermeister, Ehrenbürger) ebenfalls erwähnenswert.
Hugo Stinnes wird zweimal genannt mit „starb 1924 in Berlin" — saubere Disambiguierung, gut. Aber Familiengruft enthält Hermann Hugo Stinnes UND Hugo Stinnes (Wiki listet beide). Klarer machen.
„15. April 1916" als Eröffnung: Beleg ✓ (Wikipedia). Datum kann bleiben.
„Wettbewerb 1915" und „70 Entwürfe": keine Quelle in den 16 verlinkten Sources — vermutlich aus Hans Weber 1993, dann müsste die Quelle hinzu. Sonst streichen (siehe B1).
Schema.org: City-Type ist nicht ideal; besser Place mit geo-Koordinaten + containedInPlace. Aber funktional okay.
Author = "machsruhig Redaktion" ✓ (gemäß locked decision 23.04.2026).
Was gut ist
Tonalität: ruhig, sachlich, nicht reißerisch ✓
Patenschaftsmodell Altstadtfriedhof: korrekt beschrieben ✓
Marcks-Mahnmal 1968: ✓
BestG §13-Fristen 24h/10 Tage: ✓ (durch RECHT.NRW direkt belegt)
§ 4a BestG NRW (Grabsteine ohne Kinderarbeit): ✓
7 FAQ-Items + FAQPage-Schema: solide
Kostenwarnung („keine offizielle Tabelle, Plausibilisierung aus der Praxis"): ehrlich ✓
Bestattungsablauf 7 Schritte: vollständig, mit korrekten Kontakten
EMPFEHLUNG

Nicht deployen. Drei harte Faktenfehler (B1 Suhnel-Story, B2 17-17-17-Gem, B3 267-Pflanzen-Zahl) plus präzise Detail-Zahlen ohne Quelle (B4, B5). Die Seite ist strukturell stark, faktisch zu wackelig für Mülheim — eine Stadt mit ausreichend Wikipedia-Belegen, wo Fehler leicht von Lesern entdeckt werden.

Aktion für Chat A (Writer):

B1–B5 vollständig fixen, ohne neue ungeprüfte Details einzufügen
UNSURE-HTML-Kommentar (Gebühren) entfernen — entweder Primärquelle nachreichen oder Korridor entschärfen
Karl Ziegler & Paul Lembke in „Bedeutende Bestattete" aufnehmen
Hidden Gem Hauptfriedhof neu: Vorschlag → Karl Ziegler oder die 311 Wildpflanzenarten = Sechstel der NRW-Flora (Buch/Rautenberg/Keil 2021)

Erwarteter Score nach Fix: 86–90.

Soll ich v2 direkt nachreviewen, sobald Chat A geliefert hat?

Dein Nutzungsguthaben ist aufgebraucht. Kaufe mehr, um jetzt weiterzumachen, oder warte bis Donnerstag um 14:00, wenn sich deine Plan-Nutzung zurücksetzt.
Mehr kaufen

Du bist Chat B (Reviewer). v1 https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/muelheim/v1-from-chat-A.html




Stadt: Muelheim (NRW). Review SCORE 0-100% + Fix-Liste.

Opus 4.7
Claude ist eine KI und kann Fehler machen. Bitte überprüfe die zitierten Quellen.
Teilen
Claude is active in this tab group
Open chat
Dismiss