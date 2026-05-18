Ich lade beide Dateien.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Web durchsucht

BRIEFING_OK

Wortzahl-Schätzung (Body ohne Nav/Footer/FAQ-Schema): ca. 1.250–1.350 Wörter. Damit deutlich unter Korridor 2000–2500.

SCORE: 68/100

FUNDE:

Wortzahl unter Mindestmaß. Body-Content ohne Boilerplate liegt grob bei 1.250–1.350 Wörtern. Briefing fordert min. 1500, Ziel 2000–2500. Allein das zieht die Page strukturell unter Niveau der 13 fertigen Bundesland-Pages.
Keine § -Nummern im Bestattungsrecht-Abschnitt. BestG NRW wird namentlich genannt, aber kein einziger § zitiert. Vergleich: Bundesland-Pages auf 80+-Niveau referenzieren typischerweise §§ zu Bestattungsfrist, Sargpflicht, Leichenschau, Feuerbestattung. Hier nur Verweis auf die NRW-Bundeslandseite — das ist Verweis, nicht Substanz.
Ruhezeit ist Schätzung, nicht Beleg. „typischerweise 25 bis 30 Jahre" mit UNSURE-Kommentar im HTML. Für eine Stadt-Page mit klarem Friedhofsträger (Stadt Wuppertal, Ressort Grünflächen und Forsten) ist das ungenügend — die Wuppertaler Friedhofssatzung ist online abrufbar, exakte Werte je Grabart sind Pflicht.
Null konkrete Eurosätze bei Friedhofsgebühren. Grabarten werden korrekt aufgezählt, aber keine einzige Preisspanne. UNSURE-Kommentar schiebt die Recherche auf später. Vergleich zu 80+-Pages: dort stehen mindestens Spannen wie „Reihengrab Erdbestattung: ca. X–Y € inkl. Y Jahre Nutzungsrecht".
Hauptfriedhof Elberfeld — Fläche fehlt. Geschichte und Topografie sind da, aber keine Hektarangabe, keine Anzahl Gräber, kein Belegungsstand. Der Hauptfriedhof ist laut Stadt Wuppertal eine der größten Anlagen Nordrhein-Westfalens — die konkrete Zahl gehört in den Absatz.
Schwebebahn-Absatz ist Stimmung, kein Inhalt. „silberne Linie zwischen den Häuserzeilen" → schöner Bild-Satz, aber stadt-touristisch, nicht friedhofsrelevant. Wenn die Schwebebahn als Anker dient, dann mit funktionalem Bezug: ÖPNV-Anbindung des Hauptfriedhofs, nächste Station, Erreichbarkeit für Trauergäste. Sonst Floskel-Risiko.
Friedhof Krummacherstraße — keine Fläche, keine Eröffnung, keine Adresse mit Hausnummer. „im Westen Elberfelds", keine PLZ-präzise Lage, kein Eröffnungsjahr. Der Krummacher-Familienbezug ist gut, aber Substanz fehlt. Schema.org gibt nur „Krummacherstraße" ohne Hausnummer — wirkt unsauber.
Friedhof Unterbarmen — kategorisches Schwafeln statt Fakten. Eröffnungsjahr fehlt, Fläche fehlt, Adresse fehlt komplett. Der Engels-Bezug ist historisch richtig, aber Engels selbst ist nicht auf Unterbarmen bestattet (er starb in London, Asche in Eastbourne) — der Absatz weckt falsche Assoziationen, ohne sie aufzulösen. Entweder klärstellen oder Engels rausnehmen.
Jüdische Friedhöfe — Gründungsdaten fehlen. „bis ins 18. und frühe 19. Jahrhundert" ist zu vage. Konkrete Eröffnungsjahre und Größenangaben für Weißenburgstraße und Weinberg gehören rein, sonst ist der Absatz austauschbar.
Floskel: „in der jeweils gültigen Fassung". Reiner Juristen-Pleonasmus, trägt keinen Informationswert. Streichen.
Floskel-Verdacht: „bündelt die Stadt-Perspektive". Lead-Satz. „Stadt-Perspektive" ist Meta-Sprache über die Page, kein Inhalt für den Leser.
Stand-Jahr bei Stiftung Warentest fehlt. „7.000 bis 8.000 Euro" — ohne Jahresangabe nicht belastbar. Briefing fordert: Statistiken mit Stand-Jahr.
Quellen-Link Stiftung Warentest ist Platzhalter-URL. /Bestattung-So-sparen-Sie-Geld-bei-der-Beerdigung-1234567-0/ — die Zahlen 1234567 sehen aus wie ein nicht ersetzter Dummy. Vor v2 unbedingt verifizieren oder Link entfernen.
Cross-Links zu Nachbarstädten fehlen. Solingen, Remscheid (Bergisches Städtedreieck), Düsseldorf, Essen — keine einzige Verlinkung. Briefing nennt Cross-Links zu Städten explizit als Strukturkriterium.
Konfessionelle Friedhöfe nur als Sammelbegriff. „evangelische und katholische Kirchenfriedhöfe" — kein einzelner namentlich. Bei zwei Dutzend kommunalen plus konfessionellen Anlagen wäre mindestens ein evangelisch-konfessionell prominenter Friedhof zu benennen.
Krematorium Wuppertal nicht erwähnt. Bei Feuerbestattung relevant: Gibt es eines in Wuppertal? Falls nein: nächstes Krematorium und Überführungspflicht. Stiller Lücke.
Schema.org Place Krummacherstraße ohne Hausnummer im streetAddress. Validierungsrisiko bzw. Mindest-Qualität nicht erfüllt.
Schema.org Place Unterbarmen ohne streetAddress und ohne postalCode. Schwächer als die anderen beiden Friedhöfe — unsauber.
Kein Kapitel zu Bestattungstraditionen / regionalen Besonderheiten im Sinne „bergische Trauerkultur", protestantisch-reformierte Prägung (wurde im Krummacher-Absatz angerissen, aber nicht als eigenständiges Element ausgeführt). Briefing fordert explizit „lokale Besonderheiten (regionale Bestattungstraditionen, kulturelle Kontexte)".
Datum 12. Mai 2026 vs. tatsächliches heutiges Datum 15. Mai 2026. Marginal, aber im datePublished/dateModified und im sichtbaren Stand-Datum konsistent halten — wenn das die Veröffentlichung sein soll, beim Go-Live nachziehen.

MUST-FIX vor v2:

+700 bis +1.100 Wörter zur Erreichung des 2.000–2.500-Korridors. Erweiterung primär bei: Bestattungsrecht (§-Block), Friedhöfe (Fläche/Eröffnung/Adresse je Anlage), Kosten (konkrete Spannen), neue Sektion „Krematorium und Feuerbestattung in Wuppertal".
§§ aus BestG NRW konkret zitieren im Bestattungsrecht-Abschnitt: Mindestens Bestattungsfrist, Sargpflicht, Friedhofszwang, Aschebeisetzung — jeweils mit § und Absatz.
Wuppertaler Friedhofssatzung und Friedhofsgebührenordnung mit Stand-Jahr zitieren; Ruhezeiten je Grabart konkret (nicht „typischerweise 25–30 Jahre"). UNSURE-Kommentare im HTML auflösen, nicht in v2 weiterschleppen.
Konkrete Eurosätze oder belegbare Spannen für mindestens Reihengrab, Wahlgrab, Urnenreihengrab, Rasengrab — aus der aktuellen Gebührensatzung Wuppertal. Wenn nicht abrufbar: Quelle explizit benennen und Spanne aus vergleichbarer NRW-Stadt mit Verweis.
Hauptfriedhof Elberfeld: Fläche in Hektar, Anzahl Grabstätten, evtl. Belegungsstand ergänzen. Mindestens eine namentlich belegte Persönlichkeit (mit Quelle), sonst Sektion „prominente Bestattete" streichen statt vage halten.
Friedhof Unterbarmen: Adresse, Eröffnungsjahr, Fläche. Engels-Bezug entweder klarstellen (Familie in Barmen, er selbst nicht in Wuppertal bestattet) oder rausnehmen — aktuelle Formulierung ist suggestiv-unsauber.
Friedhof Krummacherstraße: Eröffnungsjahr, Fläche, vollständige Adresse mit Hausnummer; Schema.org streetAddress ergänzen.
Jüdische Friedhöfe: Eröffnungsjahre Weißenburgstraße und Weinberg, Quelle Jüdische Kultusgemeinde Wuppertal oder Stadt Wuppertal.
Krematorium-Absatz ergänzen: Standort, Träger, Überführungsorganisation.
Cross-Links zu Solingen, Remscheid, Düsseldorf, Essen einbauen (Bergisches Städtedreieck + nächste Großstädte).
Stiftung-Warentest-Link verifizieren oder durch funktionierende URL ersetzen; Stand-Jahr der 7.000–8.000-€-Spanne ergänzen.
Floskeln streichen: „in der jeweils gültigen Fassung", „bündelt die Stadt-Perspektive", „silberne Linie zwischen den Häuserzeilen" (oder durch konkreten ÖPNV-Anschluss ersetzen).
Schema.org bereinigen: Unterbarmen streetAddress+postalCode, Krummacherstraße Hausnummer. Validität sicherstellen.
Stand-Datum mit datePublished/dateModified synchronisieren und beim tatsächlichen Go-Live nachziehen.