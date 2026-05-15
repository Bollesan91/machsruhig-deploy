Ich hole mir Briefing und v1 und reviewe dann ohne Schönfärberei.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md

Briefing klar. Jetzt die v1 von Bielefeld.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/bielefeld/v1-from-chat-A.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/bielefeld/v1-from-chat-A.html

Wortzahl-Check zuerst, dann systematischer Durchgang.

Sichtbarer Body-Content (ohne Nav/Footer/Sources): grob 1.450–1.550 Wörter — also unter dem 1.500-Minimum, klar unter Ziel-Korridor 2000–2500. Das ist ein harter Punkt.

Jetzt der inhaltliche Durchgang:

Stärken (präzise):

Drei Friedhofs-Porträts mit echten Daten: Sennefriedhof (Eröffnung 15.08.1912, Stapenhorst, Schultz/Meyerkamp, 98 ha, Alte Kapelle 1913, Perathoner, Muggly, 1.343 Kriegsgräber Volksbund-belegt)
Hidden-Gem-Stories durchgängig vorhanden (13 politisch Verfolgte 1945, Arboretum 1,7 ha als Grabstein-Ersatz, Bürgerinitiative 1894 Sudbrack)
Konkrete Gebühren mit Vorher/Nachher (819 € / 682,02 €; 70 € / 58,19 €) und Beschluss-Datum 04.07.2024
Primärquellen verlinkt: Friedhofssatzung + Gebührensatzung PDF, § 28 PStG, Volksbund (2× direkt verlinkt), Stadt Bielefeld Friedhofsverwaltung-Adresse
Schema.org sauber: WebPage, City, Article, 3× Place, BreadcrumbList, FAQPage — alles in @graph

Schwächen (knallhart):

BestG NRW wird genannt, aber kein einziger § zitiert. Im Briefing-Beispiel explizit gefordert. Die Page schiebt ab auf die Bundesland-Seite ("Den ausführlichen Leitfaden … stellt die Bundesland-Seite bereit"). Aber: Aussagen zur Leichenschau, zur zweiten Leichenschau bei Feuerbestattung, zu sargloser Bestattung nach BestG NRW stehen IM Text — ohne §-Verweis. Nur § 28 PStG ist zitiert (Bundesrecht, easy). § 9 BestG NRW (Leichenschau), § 13 (Bestattungsfrist), § 14/15 (Sargpflicht/Ausnahmen) fehlen alle.
Ruhezeiten-Aussage ist butterweich. "typischerweise zwischen 20 und 30 Jahren je nach Bodenverhältnissen und Grabart" — die Friedhofssatzung ist verlinkt, die konkrete Bielefelder Ruhezeit gehört da rein. Aussage ohne Zahl-pro-Grabart ist Floskel.
Kostenliste ist dünn und unvollständig. Drei Bullet-Beispiele:
"Erdbestattung im Erd-Wahlgrab: 819 € Bestattungsgebühr" — das ist NUR die Bestattungsgebühr, nicht das Nutzungsrecht. Eine Erdbestattung im Wahlgrab kostet de facto Bestattungsgebühr + Nutzungsgebühr × Jahre × Fläche. Das wird nicht ausgerechnet. Beispielrechnung "Erdwahlgrab 2-stellig × 25 Jahre = X €" fehlt.
Urnenwahlgrab fehlt komplett, nur Urnenreihengrab genannt
Anonyme Bestattung, Baumbestattung/RuheForst-Optionen in Bielefeld → fehlen
Kosten für Trauerhalle/Kapellennutzung (Sennefriedhof Alte Kapelle, Sudbrack-Kapelle) → fehlen
"Bestatter-Wahl in Bielefeld" ist generisch, nicht bielefeld-spezifisch. Bullet-Punkte zur Auswahl gelten für jede Stadt. Bielefeld-Anker fehlt: konkrete Bestatter-Dichte, Innungs-Mitgliedsbetriebe-Zahl (UNSURE-Kommentar im Code) wurde NICHT aufgelöst — also Aussage fehlt. Wenn keine Zahl, dann zumindest 2-3 namentliche Beispiele für etablierte Bielefelder Bestatter. Nichts davon.
OWL-Bestattungswald wird angeteasert ("Bestattung in einem Bestattungswald in Ostwestfalen-Lippe"), aber NICHT konkretisiert. Welcher? FriedWald Lichtenau? RuheForst? In Bielefeld direkt? Das ist genau der Punkt, an dem die Page Lokalwissen zeigen müsste — und es nicht tut.
Floskel-Detection-Treffer:
"Bemerkenswert ist auch die strenge Reformfriedhof-Idee" — "bemerkenswert" ist Schreibtisch-Adjektiv
"kleinteilige Bürger-Geschichte" — OK, knapp an der Grenze
"in der das Grab keinen Stein hat, sondern wächst, blüht und sich verändert" — poetisch, eher Magazin-Stil; für YMYL-Page eher Friedhofsidylle als Information. Streichkandidat.
"Damit ist Bielefeld die einzige deutsche Stadt, deren Friedhöfe den Award zweimal in Folge gewonnen haben." — Behauptung ohne Quelle und faktisch riskant (Bestattungen.de-Award hat es in vielen Jahren gegeben, "einzige Stadt" ist nicht belegt). Hartes Risiko-Statement.
Lokale Bestattungstraditionen / kulturelle Kontexte fehlen. Briefing fragt explizit: "regionale Bestattungstraditionen, kulturelle Kontexte". OWL/Lippe als Region hat eigene Begräbniskultur (lutherische Prägung, Diakonie-Komplex Bethel direkt nebenan in Gadderbaum/Bielefeld — wird mit keinem Wort erwähnt, obwohl der Johannisfriedhof IN Gadderbaum liegt). Bethel = einer der größten diakonischen Träger Deutschlands, Hospizarbeit, Sarephta-Schwestern, eigener Friedhof? Komplett fehlend.
Pellafriedhof wird genannt als "seit 2017 auslaufend, keine Neuvergabe" — aber das passt zum Bethel-Kontext (Pella = Bethel-nahe Anlage). Auch das wird nicht eingeordnet.
Cross-Links zu Städten / Themen dünn. Nur 4 interne Cross-Links im Body: /bestattung-in/nordrhein-westfalen, /bestattungskosten, /bestattungsarten, /tools/checkliste-todesfall, /tools/vorsorge-check. Keine Stadt-zu-Stadt-Links (z.B. Münster, Köln, Dortmund als andere NRW-Städte). Keine Verlinkung zu /bestattungsarten#baumbestattung o.ä.
Meta-Description nutzt die 160 Zeichen nicht optimal aus — endet mit "Bestatter-Wahl" als Reizthema, aber kein Preisanker, kein "ab 70 €" o.ä. Click-Köder schwach.
OG-Image ist Default /assets/og-image.png — kein Bielefeld-spezifisches OG. Bei den 13 Gold-Pages laut Memory war "98/98 Pages missing OG images" ein Befund; hier wird das Pattern fortgesetzt.
Article-Author = Organization "machsruhig.de" — die anderen Bundesland-Pages nutzen laut Strategie "machsruhig Redaktion" als Autorenmodell. Hier inkonsistent (Author "machsruhig.de", aber Lead-Text "Redaktion machsruhig.de"). Schema sollte Person/Organization mit Name "Redaktion machsruhig.de" sein.
Datum "12. Mai 2026" in datePublished UND dateModified identisch — bei v1-Generierung ok, aber wenn Re-Check geplant ist, sollte dateModified bei v2/v3 mitgepflegt werden. Nur ein Hinweis.
Friedhofsverwaltung-Adresse "Am Stadtholz 24, 33609 Bielefeld" — gut, aber Öffnungszeiten und E-Mail fehlen. Genau das, was Trauernde brauchen.
Keine erkennbaren Service-Boxen für Akut-Hilfe. Bei Trauer-Page sollte oben/seitlich eine Box stehen "Akut: was ist sofort zu tun?". mr-hint-Box wird nur 1× verwendet für "Weitere Friedhöfe" — verschenkt.

SCORE: 68/100

FUNDE:

Wortzahl ~1.450 sichtbar — unter Mindest-1.500, deutlich unter Korridor 2.000–2.500
BestG NRW erwähnt, aber kein § zitiert (§ 9 Leichenschau, § 13 Frist, § 14/15 Sarg/Ausnahmen) — Aussagen zu Leichenschau, zweiter Leichenschau bei Feuerbestattung und sargloser Bestattung stehen im Fließtext ohne Paragraphen
Ruhezeit-Angabe "20–30 Jahre" ohne konkrete Bielefelder Zahlen pro Grabart, obwohl die Friedhofssatzung verlinkt ist
Kostenliste unvollständig: nur Bestattungsgebühr, keine Nutzungsgebühr-Beispielrechnung Wahlgrab; Urnenwahlgrab fehlt; Trauerhallen-/Kapellennutzungsgebühr fehlt; Baumbestattung/anonyme Bestattung in Bielefeld fehlen
"Damit ist Bielefeld die einzige deutsche Stadt, deren Friedhöfe den Award zweimal in Folge gewonnen haben" — Behauptung ohne Quelle, faktisch riskant, raus oder belegen
"Bestatter-Wahl"-Sektion komplett generisch: keine bielefeld-spezifische Bestatter-Dichte-Zahl, keine 2–3 namentlichen Beispiele etablierter Bestatter, Innungs-Aussage als <!-- UNSURE --> offen gelassen
OWL-Bestattungswald angeteasert, nicht konkretisiert (FriedWald/RuheForst-Standort in/bei Bielefeld? Lichtenau?)
Bethel/Diakonie Bielefeld komplett fehlend, obwohl Johannisfriedhof in Gadderbaum direkt im Bethel-Quartier liegt und Pellafriedhof Bethel-nah ist — größter regionaler Trauer-/Hospiz-Kontext der Stadt ignoriert
Floskel-Treffer: "wächst, blüht und sich verändert" (Magazin-Prosa), "bemerkenswert" — entfernen oder durch Fakt ersetzen
Friedhofsverwaltung Am Stadtholz 24 genannt — Öffnungszeiten und E-Mail-Adresse fehlen, genau die für Trauernde wichtigen Service-Daten
OG-Image ist Default /assets/og-image.png statt bielefeld-spezifisch
Article-Author Schema-Inkonsistenz: Author: "machsruhig.de" (Organization) vs. sichtbar "Redaktion machsruhig.de" — sollte einheitlich Person/Organization name: "Redaktion machsruhig.de" werden
Cross-Links dünn: keine NRW-Nachbarstädte (Münster, Dortmund, Köln) verlinkt, keine Deep-Links in /bestattungsarten
Keine sichtbare Service-Box "Akut: was ist jetzt zu tun?" oben — mr-hint-Pattern nur 1× verschwendet für Friedhofs-Liste
Vorgeschichtliche Hügelgräber-Datierung "vermutlich jüngere Steinzeit oder ältere Bronzezeit" — Spanne fast 3.000 Jahre, ohne Quelle. Bodendenkmal-Bescheid der Stadt sollte genauer sein, sonst Aussage straffen

MUST-FIX vor v2:

§§ BestG NRW konkret einsetzen: § 9 (Leichenschau), § 13 (Bestattungsfrist), § 14/15 (Sarg/Ausnahmen, sarglose Bestattung) — mindestens 3 Paragraphen mit Nummer im Fließtext, jeweils mit Link auf recht.nrw.de oder gesetze-im-internet.de
Bielefelder Ruhezeiten konkret: aus Friedhofssatzung Erdwahlgrab/Erdreihengrab/Urnenwahlgrab/Urnenreihengrab als Zahl-pro-Grabart zitieren (Friedhofssatzung 04.07.2024 ist verlinkt — Werte da rausziehen)
Kostenliste auf mind. 6 Positionen erweitern: Erdwahlgrab inkl. Nutzungsrecht × 25 Jahre als Beispielrechnung, Urnenwahlgrab, Urnenreihengrab, anonyme Bestattung, Baumbestattung (falls in Bielefeld angeboten — sonst klar benennen "nicht im kommunalen Bestand"), Trauerhallen-Nutzungsgebühr Alte Kapelle Sennefriedhof
"Einzige deutsche Stadt mit Doppel-Award"-Behauptung streichen oder mit Quelle belegen — sonst Risiko
Bestatter-Wahl-Sektion bielefeld-spezifisch machen: entweder Innungs-Mitgliederzahl recherchieren (Bestatterinnung Westfalen-Lippe Geschäftsstelle anfragen oder Website) oder 2–3 namentliche Beispielbestatter mit Innungs-Mitgliedschaft nennen — sonst hat die Sektion keinen Bielefeld-Bezug
Bethel/Diakonie-Kontext einbauen: eigene Sektion oder Absatz im Johannisfriedhof-Block — Bethel als Hospiz-/Diakonie-Träger in Gadderbaum, Verbindung zu Pellafriedhof, einer der größten regionalen Trauer-Akteure
Bestattungswald OWL konkret nennen: FriedWald oder RuheForst — Standort, Entfernung von Bielefeld, ob auch von Bielefelder Bestattern bedient
Wortzahl auf 2.000+ bringen: durch obige Ergänzungen sollte das automatisch passieren
OG-Image bielefeld-spezifisch generieren (Sparrenburg-Silhouette oder Sennefriedhof-Allee)
Author-Schema konsolidieren: "author":{"@type":"Organization","name":"Redaktion machsruhig.de"} einheitlich
Friedhofsverwaltung-Servicedaten ergänzen: Öffnungszeiten + E-Mail-Adresse, am besten in eigener Service-Box statt im Fließtext
Hügelgräber-Datierung präzisieren oder Aussage auf "vorgeschichtlich, Datierung umstritten" reduzieren — die 3.000-Jahre-Spanne ohne Quelle ist unsauber
Floskel-Sätze raus: "wächst, blüht und sich verändert", "bemerkenswert ist auch die strenge Reformfriedhof-Idee" — durch nüchterne Fakt-Sätze ersetzen
Cross-Links erweitern: mind. 2 NRW-Nachbarstadt-Links (Münster, Dortmund), Deep-Link zu Baumbestattung in /bestattungsarten