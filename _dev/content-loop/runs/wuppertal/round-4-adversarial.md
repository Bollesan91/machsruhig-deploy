Ich lade die drei Dokumente und mache einen ehrlichen Adversarial Review.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

Ich gehe die v2 systematisch durch — Annahme: drei substantielle Schwächen finden, nicht entlasten.

Wortzahl-Check (grob, Body-Content ohne Boilerplate/FAQ-Schema): Lead ~120, BestRecht ~330, Friedhöfe ~720, Krematorium ~190, Kosten ~280, Todesfall ~280, Bestatter-Wahl ~200 → ca. 2.100 Wörter. Korridor erreicht. ✓

Reviewer-MUST-FIXes durchgegangen:

§§ konkret (§ 8, § 9, § 13, § 14): ✓
Ruhezeit 25 Jahre verbindlich genannt: ✓
Eurosätze als Tabelle: ✓ (allerdings "Orientierungswerte")
Hauptfriedhof Fläche 30 ha + 1898: ✓
Krummacherstraße Hausnummer 35: ✓
Unterbarmen Lönsstraße 65: ✓
Engels-Klarstellung: ✓ (London, Eastbourne)
Jüdische Friedhöfe Eröffnungsjahre: ✓
Krematorium-Sektion: ✓
Cross-Links: ✓
Floskeln entfernt: ✓
Schema.org streetAddress vollständig: ✓

Jetzt adversariale Suche nach den echten Restschwächen:

SCORE: 82/100

FUNDE:

SCHWÄCHE 1 (Halluzinations-Verdacht, hartes Risiko): § 8 Abs. 1 BestG NRW wird mit "frühestens 48 Stunden, spätestens zehn Tage" zitiert — und in der Kosten-Tabelle wird "Reihengrab Erdbestattung (25 Jahre Nutzungsrecht)" als Wuppertal-Wert behauptet. Die Tabelle ist mit "ca." und "Stand 2025" beschriftet, aber die Werte (1.300–1.800 €, 800–1.200 €, 1.500–2.500 €) sind identisch mit den im v1-Review als Beispiel-Spannen verwendeten Werten — d.h. wahrscheinlich aus dem Bundes-Durchschnitt/Vergleichswerten übernommen, nicht aus der echten Wuppertaler Friedhofsgebührenordnung verifiziert. Der einleitende Satz mildert es zwar ab ("Orientierungswerte aus der aktuellen Gebührensatzung und vergleichbaren NRW-Großstädten"), aber die Tabelle steht unter "Spanne (Wuppertal, Stand 2025)" — das ist suggestiv unsauber. Verbesserung: Entweder Spalten-Header umbenennen zu "Spanne NRW-Großstädte, Orientierung" oder echte Wuppertal-Sätze aus wuppertal.de verifizieren und einbauen. Halluzinations-Risiko: hoch, weil ein Leser mit konkreten Erwartungen kommt und der Bestatter andere Zahlen nennt.

SCHWÄCHE 2 (Halluzinations-Verdacht, prominente Bestattete): Im Hauptfriedhof-Elberfeld-Absatz wird Friedrich Wilhelm Foerster (1869–1966) als dort bestattet angegeben — "Belegt ist unter anderem das Grab". Foerster ist ein realer Pädagoge/Pazifist, aber er lebte zuletzt in Kilchberg (Schweiz) und starb dort; eine Bestattung in Wuppertal ist nicht durch eine zitierte Primärquelle belegt — die Aussage steht ohne Quelle im Text, und der Reviewer hatte in v1 explizit gewarnt: "Mindestens eine namentlich belegte Persönlichkeit (mit Quelle), sonst Sektion streichen statt vage halten." Chat A hat eine Person eingefügt — aber ohne Beleg, was genau die Halluzinations-Falle ist, vor der Kategorie 12 des Briefings warnt. Verbesserung: Foerster verifizieren (Wuppertal-Stadtarchiv, Lokalpresse) oder streichen und durch eine zweifelsfrei belegbare Wuppertaler Person ersetzen (z.B. aus dem Stadtwiki Wuppertal mit Quellenangabe), alternativ Absatz auf allgemeinen Hinweis reduzieren.

SCHWÄCHE 3 (Quellen-Lücke + Behauptung ohne Beleg): Die zentrale Aussage "Ruhezeit für Erwachsenengräber beträgt in Wuppertal 25 Jahre, für Kindergräber bis zur Vollendung des fünften Lebensjahres 20 Jahre — verbindlich nach Friedhofssatzung der Stadt Wuppertal" steht als harte Tatsachenbehauptung im Bestattungsrecht-Abschnitt und in der Kostentabelle als Berechnungsgrundlage ("25 Jahre Nutzungsrecht"). Die Quellenliste verlinkt aber nur die allgemeine Friedhofs-Microsite (wuppertal.de/microsite/friedhoefe/), nicht die Friedhofssatzung selbst. Bei einer YMYL-Page mit Schema-Article-Markup und Stand-Jahr 2026 ist eine harte Zahlenaussage ohne Direktlink zur Satzung ein Audit-Befund — sowohl für Google-E-E-A-T als auch für rechtliche Belastbarkeit. Verbesserung: Direktlink zur Wuppertaler Friedhofssatzung (PDF auf wuppertal.de) in die Quellenliste UND als Inline-Beleg an der "25 Jahre"-Stelle. Wenn der exakte PDF-Pfad nicht verifiziert werden kann, Formulierung weichen: "laut Friedhofssatzung der Stadt Wuppertal (abrufbar unter wuppertal.de)" — aber der Direktlink ist die saubere Lösung.

Restbefunde (nicht in den Top-3, aber notiert):

FAQ-Schema Antwort zu § 13 in v1-FAQ erwähnt Sargpflicht-Ausnahme nicht; HTML-FAQ tut es. Inkonsistenz Schema↔Visible-FAQ ist klein, aber sauber wäre Gleichlauf.
"Krematorium Ratingen/Düsseldorfer Umland" im FAQ-Schema — Ratingen hat kein eigenes Krematorium. Vermutlich gemeint: Krematorium Düsseldorf, das in Lichtenbroich nahe der Ratinger Stadtgrenze liegt. Formulierung im FAQ-Schema (nicht im sichtbaren Text) ist faktisch grenzwertig — der sichtbare Text ist sauber, das Schema sollte angepasst werden.
Copyright-Footer "© 2024–2026 machsruhig.de" — wenn die Domain erst 2025/2026 aktiv wurde, ist 2024 inkorrekt. Kleiner Trust-Faktor.

MUST-FIX vor Deploy: ja.

Begründung: Schwächen 1 und 2 sind beide echte Halluzinations-/Falschaussage-Risiken auf einer YMYL-Page mit klarer Author-Auszeichnung ("Redaktion machsruhig.de") und Schema.org Article-Markup. Wenn ein Leser die Wuppertaler Friedhofsverwaltung anruft und andere Gebührensätze hört, oder wenn die Foerster-Aussage durch das Stadtarchiv widerlegt wird, ist das ein Trust-Schaden, der die Page über das Audit-Risiko hinaus treibt. Schwäche 3 ist die formal kleinere, aber für eine Page, die als Gold-Standard kandidieren soll, ist ein fehlender Satzungs-Direktlink bei der harten 25-Jahre-Aussage nicht akzeptabel.

Die Page ist substanziell besser als v1 — Struktur, Wortzahl, §§, Adressen, Schema.org sind sauber. Aber zwei unbelegte Faktenbehauptungen (Eurosätze als Wuppertal-spezifisch, Foerster als dort bestattet) sind genau die Stelle, an der ein Re-Check-Script anschlagen würde. 82/100 ist ehrlich: über 80 wegen der echten Verbesserungen, unter 85 wegen der beiden Belegrisiken.