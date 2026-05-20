# FAQ-Schema-Drift-Audit

**Stand:** faq-schema-drift.py — alle Stadt-Pages

## Zusammenfassung

- **Total Cities:** 50
- **CLEAN:** 9
- **DRIFT:** 39
- **NO_LD (HTML ohne JSON-LD FAQPage):** 1
- **NO_HTML (JSON-LD ohne HTML-Block):** 0
- **NO_FAQ (gar keine FAQ):** 1

## DRIFT (JSON-LD ≠ HTML)

### aachen  (LD=7, HTML=7)

- **A_TEXT[0]** — Wie viele Friedhöfe gibt es in Aachen?
  - LD:   `Der Aachener Stadtbetrieb verwaltet 28 aktive städtische Friedhöfe und sechs reine Gedenkstätten sowie das Krematorium auf der Hüls. Daneben existiert der konfessionell jüdische Friedhof an der Lüttic…`
  - HTML: `<p>Der Aachener Stadtbetrieb verwaltet 28 aktive städtische Friedhöfe und sechs reine Gedenkstätten sowie das Krematorium auf der Hüls. Daneben existiert der konfessionell jüdische Friedhof an der Lüt…`
- **A_TEXT[1]** — Welche Bestattungsfristen gelten in Aachen?
  - LD:   `Es gilt das Bestattungsgesetz NRW (BestG NRW). Erdbestattungen dürfen frühestens 24 Stunden nach dem Tod erfolgen (§ 13 Abs. 2 BestG NRW). Erdbestattungen und Einäscherungen müssen innerhalb von zehn …`
  - HTML: `<p>Es gilt das Bestattungsgesetz NRW. Erdbestattungen dürfen frühestens 24 Stunden nach dem Tod vorgenommen werden (<strong>§ 13 Abs. 2 BestG NRW</strong>). Erdbestattungen und Einäscherungen müssen i…`
- **A_TEXT[2]** — Was kostet eine Bestattung in Aachen?
  - LD:   `Nach der 17. Änderungssatzung der Friedhofsgebührenordnung der Stadt Aachen (Stand: 17.12.2025) kostet das Nutzungsrecht an einem Reihengrab zur Sargbeisetzung (Erwachsene) für die Ruhefrist 1.527,00 …`
  - HTML: `<p>Nach der 17. Änderungssatzung der Aachener Friedhofsgebührenordnung (Stand 17.12.2025) kostet das Nutzungsrecht an einem Reihengrab zur Sargbeisetzung 1.527,00 € für die Ruhefrist, ebenso ein Urnen…`
- **A_TEXT[3]** — Wer übernimmt die Bestattungskosten, wenn kein Geld vorhanden ist?
  - LD:   `Nach § 74 SGB XII übernimmt der Sozialhilfeträger – in Aachen die StädteRegion Aachen, organisatorisch über den Fachbereich Soziales und Integration der Stadt Aachen – die erforderlichen Kosten einer …`
  - HTML: `<p>Nach § 74 SGB XII übernimmt der Sozialhilfeträger – in Aachen die StädteRegion Aachen, organisatorisch über den Fachbereich Soziales und Integration der Stadt Aachen – die erforderlichen Kosten ein…`
- **A_TEXT[4]** — Besteht in Aachen Sargpflicht?
  - LD:   `Das BestG NRW kennt seit 2003 keine pauschale Sargpflicht mehr. Die Friedhofssatzung der Stadt Aachen regelt Einzelheiten zu Sarg und Urne; für Erdbestattungen ist in der Regel ein Sarg vorgeschrieben…`
  - HTML: `<p>Das BestG NRW kennt seit der Novelle von 2003 keine gesetzliche Sargpflicht mehr. Die Friedhofssatzung der Stadt Aachen schreibt für Erdbestattungen auf den kommunalen Friedhöfen jedoch ein geeigne…`
- **A_TEXT[5]** — Welche Ruhezeit gilt auf Aachener Friedhöfen?
  - LD:   `Die Ruhezeit ist in der Friedhofssatzung der Stadt Aachen geregelt und beträgt je nach Friedhof 20, 25 oder 30 Jahre. Auf Westfriedhof, Waldfriedhof und Friedhof Hüls liegt sie typischerweise bei 20 J…`
  - HTML: `<p>Die Ruhezeit ist in der Friedhofssatzung geregelt und richtet sich nach den Bodenverhältnissen. Auf dem Westfriedhof, Waldfriedhof und Friedhof Hüls gilt eine Ruhezeit von 20 Jahren, auf dem Friedh…`
- **A_TEXT[6]** — Wo wird der Sterbefall in Aachen beurkundet?
  - LD:   `Zuständig ist das Standesamt Aachen im Verwaltungsgebäude Marschiertor, Hubertusstraße 2-8, 52064 Aachen. Die Anzeige des Todes muss nach § 28 PStG spätestens am dritten auf den Tod folgenden Werktag …`
  - HTML: `<p>Zuständig ist das Standesamt Aachen im Verwaltungsgebäude Marschiertor, Hubertusstraße 2-8, 52064 Aachen. Die Anzeige des Todes muss nach <strong>§ 28 PStG</strong> spätestens am dritten auf den To…`

### augsburg  (LD=9, HTML=9)

- **A_TEXT[0]** — Wie viele Friedhöfe gibt es in Augsburg?
  - LD:   `Auf dem Stadtgebiet Augsburgs liegen 14 Friedhöfe. Neun davon werden städtisch verwaltet (Westfriedhof, Nordfriedhof, Alter und Neuer Ostfriedhof, Alter und Neuer Friedhof Haunstetten sowie die Friedh…`
  - HTML: `<p>Auf dem Stadtgebiet liegen 14 Friedhöfe. Neun davon werden städtisch verwaltet – Westfriedhof, Nordfriedhof, Alter und Neuer Ostfriedhof, Alter und Neuer Haunstetter Friedhof sowie die Friedhöfe Gö…`
- **Q_TEXT[1]**
  - LD:   `Was kostet eine Bestattung in Augsburg?`
  - HTML: `Was kostet eine Bestattung auf einem städtischen Friedhof in Augsburg?`
- **A_TEXT[1]** — Was kostet eine Bestattung in Augsburg?
  - LD:   `Auf städtischen Friedhöfen beträgt die reine Bestattungsgebühr seit 1. Januar 2025 für eine Erdbestattung ab dem 12. Lebensjahr 940 Euro, für eine Urnenbeisetzung 532 Euro (Satzung 7511 der Stadt Augs…`
  - HTML: `<p>Seit 1. Januar 2025 beträgt nach Satzung 7511 die Bestattungsgebühr für eine Erdbestattung ab dem 12. Lebensjahr 940 Euro, für eine Urnenbeisetzung 532 Euro. Auf zehn Jahre Ruhezeit summieren sich …`
- **A_TEXT[2]** — Wie lange ist die Bestattungsfrist in Bayern?
  - LD:   `Seit der Neufassung der Bayerischen Bestattungsverordnung zum 1. April 2021 müssen Verstorbene spätestens acht Tage nach Feststellung des Todes bestattet oder eingeäschert sein (§ 19 Abs. 1 BestV). So…`
  - HTML: `<p>Seit 1. April 2021 müssen Verstorbene spätestens acht Tage nach Feststellung des Todes bestattet oder eingeäschert sein (§ 19 Abs. 1 BestV). Sonntage, gesetzliche Feiertage und Samstage werden nich…`
- **A_TEXT[3]** — Wie lang ist die Ruhezeit auf Augsburger Friedhöfen?
  - LD:   `Die Ruhezeit beträgt auf den meisten Augsburger Friedhöfen zehn Jahre. Auf Wahlgrabstätten kann das Nutzungsrecht für 10, 15 oder mehr Jahre erworben und in der Regel verlängert werden. Bei Kindern bi…`
  - HTML: `<p>Auf den meisten Augsburger Friedhöfen beträgt die Ruhezeit zehn Jahre, bei Kindern bis zum vollendeten fünften Lebensjahr fünf Jahre. Auf Wahlgrabstätten lassen sich Nutzungsrechte mit 10, 15 oder …`
- **A_TEXT[4]** — Gibt es in Augsburg eine Möglichkeit zur sarglosen Erdbestattung?
  - LD:   `Grundsätzlich ja. § 30 Abs. 1 BestV schreibt für Erdbestattungen Särge aus leicht abbaubarem Vollholz vor. Seit der BestV-Novelle 2021 darf der Friedhofsträger nach § 30 Abs. 2 BestV jedoch sargfreie …`
  - HTML: `<p>Grundsätzlich gilt in Bayern Sargpflicht (§ 30 Abs. 1 BestV, Vollholzsarg). § 30 Abs. 2 BestV erlaubt dem Friedhofsträger jedoch seit 2021, sarglose Bestattungen im Leichentuch aus religiösen oder …`
- **Q_TEXT[5]**
  - LD:   `Wo wird der Sterbefall in Augsburg gemeldet?`
  - HTML: `Wer trägt die Bestattungskosten in Augsburg?`
- **A_TEXT[5]** — Wo wird der Sterbefall in Augsburg gemeldet?
  - LD:   `Zuständig ist das Standesamt Augsburg in der Maximilianstraße 69, 86150 Augsburg. Die Sterbefall-Abteilung ist unter 0821 324-3848 oder -3867 erreichbar, per E-Mail unter sterbefall@augsburg.de. In de…`
  - HTML: `<p>Bestattungspflichtig sind nach Art. 15 BestG in Verbindung mit § 15 BestV und § 1 Abs. 1 Satz 2 Nr. 1 BestV die Angehörigen in folgender, durch den Verordnungstext exakt festgelegter Reihenfolge: a…`
- **Q_TEXT[6]**
  - LD:   `Wer trägt die Bestattungskosten in Augsburg?`
  - HTML: `Wo wird ein Sterbefall in Augsburg gemeldet?`
- **A_TEXT[6]** — Wer trägt die Bestattungskosten in Augsburg?
  - LD:   `Bestattungspflichtig sind nach Art. 15 BestG in Verbindung mit § 15 BestV und § 1 Abs. 1 Satz 2 Nr. 1 BestV die Angehörigen in folgender, durch die Verordnung festgelegter Reihenfolge: a) Ehegatte ode…`
  - HTML: `<p>Beim Standesamt Augsburg in der Maximilianstraße 69, 86150 Augsburg. Die Sterbefall-Abteilung ist telefonisch unter 0821 324-3848 oder -3867 erreichbar, per E-Mail unter sterbefall@augsburg.de. Zus…`
- **A_TEXT[7]** — Gibt es in Augsburg ein Krematorium?
  - LD:   `Ja. Das Krematorium der Stadt Augsburg liegt auf dem Westfriedhof in der Stadtberger Straße 80a und gehört zu den älteren Feuerbestattungsanlagen Bayerns. Es wurde im Rahmen der großen Neubaumaßnahmen…`
  - HTML: `<p>Ja. Das Krematorium der Stadt Augsburg liegt auf dem Westfriedhof in der Stadtberger Straße 80a. Es wurde im Rahmen der großen Neubaumaßnahmen von 1913 bis 1915 errichtet – zusammen mit der Aussegn…`
- **A_TEXT[8]** — Ist Bertolt Brecht auf einem Augsburger Friedhof beigesetzt?
  - LD:   `Nein. Brecht selbst ist 1956 auf dem Dorotheenstädtischen Friedhof in Berlin beigesetzt worden. Auf dem Protestantischen Friedhof Augsburg liegt jedoch das Familiengrab der Brechts mit Vater Berthold …`
  - HTML: `<p>Nein. Bertolt Brecht selbst ist 1956 auf dem Dorotheenstädtischen Friedhof in Berlin beigesetzt worden, direkt neben dem Haus in der Chausseestraße 125, in dem er seine letzten Jahre verbrachte. Au…`

### berlin  (LD=4, HTML=7)

- **COUNT-Mismatch:** JSON-LD hat 4 Q/A, HTML hat 7
- **A_TEXT[0]** — Was kostet eine Bestattung in Berlin?
  - LD:   `Die Kosten in Berlin sind günstiger als in anderen Großstädten. Urnengräber kosten etwa 450–1.200 € (20 Jahre), Erdgräber 1.000–3.500 € (25–30 Jahre). Bestatterleistungen kommen hinzu (ca. 1.200–2.500…`
  - HTML: `Berlin hat im Bundesvergleich relativ günstige Friedhofsgebühren. Beispiele für landeseigene Friedhöfe: Reihengrab (Erdbestattung) ca. 939–1.016 € (20 Jahre), Urnengrab 450–1.200 €, anonyme Beisetzung…`
- **A_TEXT[1]** — Wie viele Friedhöfe gibt es in Berlin?
  - LD:   `Laut Berlin.de (Senatsverwaltung für Mobilität, Verkehr, Klimaschutz und Umwelt) gibt es in Berlin insgesamt 222 Friedhöfe, davon 182 geöffnet. Das Land Berlin verwaltet davon 85 Friedhöfe, der Rest i…`
  - HTML: `Laut Berlin.de (Senatsverwaltung für Mobilität, Verkehr, Klimaschutz und Umwelt) gibt es im Land Berlin <strong>222 Friedhöfe</strong>, von denen 182 geöffnet sind. 85 davon werden vom Land Berlin ver…`
- **Q_TEXT[2]**
  - LD:   `Was hat sich durch die Reform des Berliner Bestattungsgesetzes 2024 geändert?`
  - HTML: `Wurde die 48-Stunden-Wartefrist in Berlin abgeschafft?`
- **A_TEXT[2]** — Was hat sich durch die Reform des Berliner Bestattungsgesetzes 2024 geändert?
  - LD:   `Mit der Reform 2024 wurde die bisherige 48-Stunden-Wartefrist vor einer Bestattung (vormals § 21 BestattG BE) abgeschafft. Damit können insbesondere muslimische und jüdische Bestattungen, die nach rel…`
  - HTML: `Ja. Mit der Reform des Berliner Bestattungsgesetzes 2024 wurde die bisherige Mindestwartefrist von 48 Stunden nach Eintritt des Todes (vormals § 21 BestattG BE) abgeschafft. Der Senat hatte die Reform…`
- **Q_TEXT[3]**
  - LD:   `Gibt es naturnahe Bestattungen in Berlin?`
  - HTML: `Kann ich in Berlin ohne Sarg bestattet werden?`
- **A_TEXT[3]** — Gibt es naturnahe Bestattungen in Berlin?
  - LD:   `Ja. Innerhalb Berlins bieten u.a. der Waldfriedhof Zehlendorf und der Waldfriedhof Heerstraße naturnahe Bestattungen in Waldlage. Zusätzlich nutzen viele Berliner Familien den Südwestkirchhof Stahnsdo…`
  - HTML: `Grundsätzlich besteht in Berlin Sargpflicht. Auf vom Friedhofsträger bestimmten Grabfeldern können Verstorbene jedoch aus religiösen Gründen in einem Leichentuch ohne Sarg bestattet werden — relevant …`

### bielefeld  (LD=8, HTML=8)

- **A_TEXT[2]** — Was kostet eine Bestattung in Bielefeld?
  - LD:   `Gesamtkosten in Deutschland liegen laut Stiftung Warentest bei rund 7.000 bis 8.000 Euro. Die Friedhofsgebühren in Bielefeld wurden 2024 um 20 Prozent angehoben. Eine Erdbestattung im Erd-Wahlgrab kos…`
  - HTML: `Gesamtkosten in Deutschland liegen laut Stiftung Warentest bei rund 7.000 bis 8.000 Euro. Die Friedhofsgebühren in Bielefeld wurden 2024 um 20 Prozent angehoben — eine Erdbestattung im Erd-Wahlgrab ko…`
- **A_TEXT[3]** — Wie lange ist die Ruhezeit auf Bielefelder Friedhöfen?
  - LD:   `Nach der Friedhofssatzung der Stadt Bielefeld (Fassung 04.07.2024) gilt eine Ruhezeit von 25 Jahren für Erdbestattungen Erwachsener, 20 Jahren für Erdbestattungen von Kindern unter sieben Jahren und 2…`
  - HTML: `Nach der Friedhofssatzung der Stadt Bielefeld (Fassung 04.07.2024) gilt eine Ruhezeit von 25 Jahren für Erdbestattungen Erwachsener, 20 Jahren für Erdbestattungen von Kindern bis zur Vollendung des si…`
- **A_TEXT[5]** — Wer ist auf dem Johannisfriedhof bestattet?
  - LD:   `Auf dem Johannisfriedhof ruhen unter anderem der Backpulver-Erfinder August Oetker (1862–1918), Vertreter der Bielefelder Unternehmerfamilien Delius, Bertelsmann und Kisker sowie der Reformjurist Alfr…`
  - HTML: `Auf dem Johannisfriedhof ruhen unter anderem der Backpulver-Erfinder August Oetker (1862–1918), Vertreter der Bielefelder Unternehmerfamilien Delius, Bertelsmann und Kisker sowie der Reformjurist Alfr…`
- **A_TEXT[7]** — Gibt es Baumbestattungen in oder bei Bielefeld?
  - LD:   `Auf den kommunalen Friedhöfen Bielefelds werden Baumgrabfelder als Naturgrabbereiche angeboten; die Beisetzung erfolgt dort biologisch abbaubar. Klassische FriedWald-Bestattungen außerhalb von Friedhö…`
  - HTML: `Auf den kommunalen Friedhöfen Bielefelds werden Baumgrabfelder als Naturgrabbereiche angeboten; die Beisetzung erfolgt dort biologisch abbaubar. Klassische FriedWald-Bestattungen außerhalb von Friedhö…`

### bochum  (LD=7, HTML=7)

- **A_TEXT[1]** — Wo befindet sich der Hauptfriedhof Bochum und wann ist er erreichbar?
  - LD:   `Der Hauptfriedhof Bochum (Friedhof Freigrafendamm) liegt an der Immanuel-Kant-Straße im Stadtteil Altenbochum, rund zwei Kilometer östlich der Innenstadt. Der Friedhof ist täglich rund um die Uhr bege…`
  - HTML: `Der Hauptfriedhof Bochum (Friedhof Freigrafendamm) liegt an der Immanuel-Kant-Straße im Stadtteil Altenbochum, rund zwei Kilometer östlich der Innenstadt. Der Friedhof ist täglich rund um die Uhr bege…`
- **A_TEXT[2]** — Gibt es in Bochum einen West- und einen Ostfriedhof?
  - LD:   `Nein, offizielle städtische Friedhöfe mit diesen Namen gibt es in Bochum nicht. Häufig wird mit Westteil und Ostteil die Zweiteilung des Hauptfriedhofs Freigrafendamm gemeint, die durch den Oviedo-Rin…`
  - HTML: `Nein, offizielle städtische Friedhöfe mit diesen Namen gibt es in Bochum nicht. Häufig wird mit „Westteil" und „Ostteil" die Zweiteilung des Hauptfriedhofs Freigrafendamm gemeint, die durch den <stron…`
- **A_TEXT[3]** — Welche Friedhofsgebühren gelten in Bochum?
  - LD:   `Friedhofsgebühren regelt die Stadt Bochum in der Gebührensatzung für die städtischen Friedhöfe; verbindlich ist allein die jeweils gültige Fassung. Die Stadt veröffentlicht jährlich die Broschüre 'Bes…`
  - HTML: `Friedhofsgebühren regelt die Stadt Bochum in der Gebührensatzung für die städtischen Friedhöfe; verbindlich ist allein die jeweils gültige Fassung. Die Stadt veröffentlicht jährlich die Broschüre „Bes…`
- **A_TEXT[4]** — Welche Rolle spielt die Bergbau-Tradition für die Bochumer Friedhöfe?
  - LD:   `Bochum war über ein Jahrhundert Bergbaustadt mit zeitweise mehr als 30 aktiven Schachtanlagen; die Trauerkultur trägt das Erbe sichtbar weiter. Auf dem Hauptfriedhof Freigrafendamm liegt unter anderem…`
  - HTML: `Bochum war über ein Jahrhundert Bergbaustadt mit zeitweise mehr als 30 aktiven Schachtanlagen; die Trauerkultur trägt das Erbe sichtbar weiter. Auf dem Hauptfriedhof Freigrafendamm liegt unter anderem…`

### bonn  (LD=8, HTML=8)

- **A_TEXT[3]** — Welche prominenten Persönlichkeiten sind auf dem Burgfriedhof Bad Godesberg bestattet?
  - LD:   `Auf dem Burgfriedhof Bad Godesberg sind unter anderem der SPD-Politiker und Bundestagsabgeordnete Herbert Wehner (1906–1990, Ehrengrab der Stadt Bonn), der FDP- und spätere CDU-Politiker Erich Mende (…`
  - HTML: `Auf dem Burgfriedhof Bad Godesberg sind unter anderem der SPD-Politiker und Bundestagsabgeordnete Herbert Wehner (1906–1990, Ehrengrab der Stadt Bonn), der FDP- und spätere CDU-Politiker und Vizekanzl…`
- **A_TEXT[5]** — Welche Ruhezeit gilt auf den Bonner Friedhöfen?
  - LD:   `Die Ruhezeit ist in Anlage 2 der Bonner Friedhofssatzung je Friedhof einzeln festgelegt. Für Urnen und Grabkammersysteme gilt einheitlich 15 Jahre auf allen Friedhöfen. Bei Sargbestattungen variiert d…`
  - HTML: `Die Ruhezeit ist in Anlage 2 der Bonner Friedhofssatzung je Friedhof einzeln festgelegt. Für Urnen und Grabkammersysteme gilt einheitlich 15 Jahre auf allen Bonner Friedhöfen. Bei Sargbestattungen var…`

### braunschweig  (LD=7, HTML=7)

- **A_TEXT[0]** — Wie lange darf man in Niedersachsen mit der Bestattung warten?
  - LD:   `Nach § 9 Abs. 2 BestattG Niedersachsen sollen Leichen innerhalb von acht Tagen seit Eintritt des Todes bestattet oder eingeäschert worden sein. Urnen sollen innerhalb eines Monats nach der Einäscherun…`
  - HTML: `<p>Nach § 9 Abs. 2 BestattG Niedersachsen sollen Leichen innerhalb von acht Tagen seit Eintritt des Todes bestattet oder eingeäschert worden sein. Urnen sollen innerhalb eines Monats nach der Einäsche…`
- **A_TEXT[1]** — Was kostet eine einfache Urnenbestattung auf dem Hauptfriedhof Braunschweig?
  - LD:   `Die reinen Friedhofsgebühren betragen rund 928 € (Urnenwahlgrabstätte 795 € + Fertigung Urnengruft inkl. Beisetzung 100 € + Verwaltungsgebühr 32,90 €). Hinzu kommen die Krematoriumsgebühr von erfahrun…`
  - HTML: `<p>Die reinen Friedhofsgebühren betragen rund 928 € (Urnenwahlgrabstätte 795 € + Fertigung Urnengruft inkl. Beisetzung 100 € + Verwaltungsgebühren 32,90 €). Hinzu kommen die Krematoriumsgebühr von erf…`
- **A_TEXT[3]** — Ist eine Bestattung ohne Sarg in Braunschweig möglich?
  - LD:   `Grundsätzlich gilt nach § 11 Abs. 1 BestattG Sargpflicht. Die untere Gesundheitsbehörde kann Ausnahmen zulassen, wenn in der zu bestattenden Person ein wichtiger Grund vorliegt und ein öffentlicher Be…`
  - HTML: `<p>Grundsätzlich gilt nach § 11 Abs. 1 BestattG Sargpflicht. Die untere Gesundheitsbehörde kann Ausnahmen von der Sargpflicht zulassen, wenn in der zu bestattenden Person ein wichtiger Grund vorliegt …`
- **A_TEXT[4]** — Wo ist Heinrich der Löwe begraben?
  - LD:   `Heinrich der Löwe und seine zweite Frau Mathilde von England sind im Braunschweiger Dom St. Blasii beigesetzt. Das Grabmal aus Muschelkalk im Mittelschiff stammt aus der Zeit um 1230/1250. Die separat…`
  - HTML: `<p>Heinrich der Löwe und seine zweite Frau Mathilde von England sind im Braunschweiger Dom St. Blasii beigesetzt. Das gemeinsame Grabmal aus Muschelkalk im Mittelschiff stammt aus der Zeit um 1230/125…`
- **A_TEXT[5]** — Kann man auf dem Magnifriedhof in der Innenstadt noch bestattet werden?
  - LD:   `Ja. Der Magnifriedhof wurde 2020 als Stadtteilfriedhof reaktiviert. Möglich sind Urnenbeisetzungen an Einzelbäumen und an einer Urnenwand; Erdbestattungen sind für Gemeindemitglieder der Magni-Gemeind…`
  - HTML: `<p>Ja. Der Magnifriedhof wurde 2020 als Stadtteilfriedhof reaktiviert. Möglich sind Urnenbeisetzungen an Einzelbäumen sowie an einer Urnenwand; Erdbestattungen sind für Gemeindemitglieder der Magni-Ge…`
- **A_TEXT[6]** — Welcher Friedhof in Braunschweig hat die niedrigste Konfessionshürde?
  - LD:   `Der städtische Stadtfriedhof an der Helmstedter Straße ist konfessionell ungebunden und steht allen Bürgerinnen und Bürgern offen. Auch Hauptfriedhof und Katholischer Friedhof nehmen Bestattungen ohne…`
  - HTML: `<p>Der städtische Stadtfriedhof an der Helmstedter Straße ist konfessionell ungebunden und steht allen Bürgerinnen und Bürgern offen. Auch der Hauptfriedhof und der Katholische Friedhof nehmen Bestatt…`

### bremen  (LD=7, HTML=8)

- **COUNT-Mismatch:** JSON-LD hat 7 Q/A, HTML hat 8
- **A_TEXT[1]** — Darf in Bremen die Asche zuhause aufbewahrt oder im Garten verstreut werden?
  - LD:   `Bremen kennt eine bundesweit seltene Ausnahme zum Friedhofszwang. Nach § 4 Abs. 1a des Bremer Friedhofs- und Bestattungsgesetzes kann die Asche unter engen Voraussetzungen außerhalb von Friedhöfen auf…`
  - HTML: `Bremen kennt eine bundesweit seltene Ausnahme zum Friedhofszwang. Nach § 4 Abs. 1a des Bremer Friedhofs- und Bestattungsgesetzes (Novelle 2015) kann die Asche unter engen Voraussetzungen außerhalb von…`

### chemnitz  (LD=7, HTML=7)

- **A_TEXT[0]** — Wie viele Friedhöfe gibt es in Chemnitz?
  - LD:   `Die Stadt Chemnitz betreibt drei kommunale Friedhofsanlagen: den Friedhof Wartburgstraße, den Urnenhain an der Reichenhainer Straße und den Friedhof am Richterweg für Opfer von Krieg und Gewaltherrsch…`
  - HTML: `<div>Die Stadt Chemnitz betreibt drei kommunale Friedhofsanlagen: den Friedhof Wartburgstraße, den Urnenhain an der Reichenhainer Straße und den Friedhof am Richterweg für Opfer von Krieg und Gewalthe…`
- **A_TEXT[1]** — Wie lange ist die Ruhezeit auf Chemnitzer Friedhöfen?
  - LD:   `Nach § 6 Abs. 2 SächsBestG gilt eine Regelruhezeit von 20 Jahren. Für Kinder, die vor Vollendung des zweiten Lebensjahres verstorben sind, beträgt sie 10 Jahre. Die Friedhofssatzung der Stadt Chemnitz…`
  - HTML: `<div>Nach § 6 Abs. 2 SächsBestG gilt eine Regelruhezeit von 20 Jahren. Für Kinder, die vor Vollendung des zweiten Lebensjahres verstorben sind, beträgt sie 10 Jahre. Die Friedhofssatzung der Stadt Che…`
- **A_TEXT[2]** — Was kostet eine Urnenbeisetzung in Chemnitz?
  - LD:   `Die reinen Friedhofsgebühren für eine Urnenlösestelle auf den Städtischen Friedhöfen Chemnitz liegen laut Gebührensatzung der Stadt Chemnitz (Stand Januar 2024) bei 354,00 Euro Grabnutzungsgebühr für …`
  - HTML: `<div>Die reinen Friedhofsgebühren für eine Urnenlösestelle auf den Städtischen Friedhöfen liegen laut Gebührensatzung 67.210 (Stand Januar 2024) bei 354,00 € Grabnutzungsgebühr für 20 Jahre, zuzüglich…`
- **Q_TEXT[3]**
  - LD:   `Wann muss eine Bestattung in Chemnitz erfolgen?`
  - HTML: `Welche Fristen gelten nach einem Todesfall?`
- **A_TEXT[3]** — Wann muss eine Bestattung in Chemnitz erfolgen?
  - LD:   `Nach § 19 Abs. 1 SächsBestG darf eine Erdbestattung oder Einäscherung frühestens 48 Stunden nach Feststellung des Todes erfolgen und muss innerhalb von acht Tagen durchgeführt werden. Eine Urne ist na…`
  - HTML: `<div>Nach § 19 Abs. 1 SächsBestG darf eine Erdbestattung oder Einäscherung frühestens 48 Stunden nach Feststellung des Todes erfolgen und muss innerhalb von acht Tagen durchgeführt werden (Wochenenden…`
- **A_TEXT[4]** — Welcher Friedhof in Chemnitz hat das Krematorium?
  - LD:   `Das Krematorium der Stadt Chemnitz befindet sich am Urnenhain an der Reichenhainer Straße, gegenüber dem Friedhof Wartburgstraße. Die Weihe fand am 15. Dezember 1906 statt, die ersten beiden Einäscher…`
  - HTML: `<div>Das Krematorium befindet sich am Urnenhain an der Reichenhainer Straße, gegenüber dem Friedhof Wartburgstraße. Die Weihe fand am 15. Dezember 1906 statt, die ersten beiden Einäscherungen Sachsens…`
- **Q_TEXT[5]**
  - LD:   `Gibt es in Chemnitz Baumbestattungen?`
  - HTML: `Ist eine Baumbestattung in Chemnitz möglich?`
- **A_TEXT[5]** — Gibt es in Chemnitz Baumbestattungen?
  - LD:   `Ja. Auf dem Friedhof Wartburgstraße werden Baumbestattungen sowohl mit als auch ohne Namensnennung angeboten. Die Variante ohne Namensnennung kostet 1.644 Euro für 20 Jahre, die Variante mit Namenskis…`
  - HTML: `<div>Ja. Auf dem Friedhof Wartburgstraße werden Baumbestattungen sowohl mit als auch ohne Namensnennung angeboten. Die Variante ohne Namensnennung kostet 1.644 € für 20 Jahre, die Variante mit Namensk…`
- **A_TEXT[6]** — Wer ist Träger der Städtischen Friedhöfe Chemnitz?
  - LD:   `Träger ist der Friedhofs- und Bestattungsbetrieb der Stadt Chemnitz, ein Eigenbetrieb mit Sitz in der Wartburgstraße 47, 09126 Chemnitz. Die Verwaltung ist werktags von 8 bis 15 Uhr telefonisch erreic…`
  - HTML: `<div>Träger ist der Friedhofs- und Bestattungsbetrieb der Stadt Chemnitz, ein Eigenbetrieb der Stadt mit Sitz in der Wartburgstraße 47, 09126 Chemnitz. Betriebsleiterin ist Heike Decker. Die Verwaltun…`

### dortmund  (LD=8, HTML=8)

- **A_TEXT[0]** — Wie viele Friedhöfe gibt es in Dortmund?
  - LD:   `Die Stadt Dortmund betreibt über 30 städtische Friedhöfe. Zusätzlich existieren zahlreiche konfessionelle Friedhöfe in Trägerschaft katholischer und evangelischer Kirchengemeinden sowie jüdische Fried…`
  - HTML: `<p>Die Stadt Dortmund betreibt über 30 städtische Friedhöfe (Eigenbetrieb Friedhöfe Dortmund). Hinzu kommen zahlreiche konfessionelle Friedhöfe in Trägerschaft katholischer Kirchengemeinden (z. B. St.…`
- **A_TEXT[1]** — Welcher ist der größte Friedhof in Dortmund?
  - LD:   `Der Hauptfriedhof in Brackel zählt mit rund 118 Hektar (nach Angaben der Stadt Dortmund) zu den größten Friedhöfen Deutschlands und ist die größte zusammenhängende Grünfläche der Stadt.…`
  - HTML: `<p>Der Hauptfriedhof in Brackel zählt nach Angaben der Stadt Dortmund mit rund 118 Hektar zu den größten Friedhöfen Deutschlands und ist zugleich die größte zusammenhängende Grünfläche Dortmunds.</p>…`
- **A_TEXT[2]** — Wie lange ist die Ruhezeit auf Dortmunder Friedhöfen?
  - LD:   `Die Ruhezeiten ergeben sich aus der Satzung für die Friedhöfe der Stadt Dortmund und richten sich nach den jeweiligen Bodenverhältnissen. Erd- und Aschebeisetzungen haben nach § 4 Abs. 2 BestG NRW gle…`
  - HTML: `<p>Die genauen Ruhezeiten ergeben sich aus der Friedhofssatzung der Stadt Dortmund. Nach § 4 Abs. 2 BestG NRW müssen die Friedhofsträger für Erd- und Aschebeisetzungen <em>gleich lange</em> Grabnutzun…`
- **A_TEXT[3]** — Was kostet eine Bestattung in Dortmund?
  - LD:   `Die Gesamtkosten setzen sich aus Bestatterleistung, Friedhofsgebühren und Fremdleistungen zusammen. Eine einfache Urnenbeisetzung beginnt bei rund 2.500 Euro, eine klassische Erdbestattung im Wahlgrab…`
  - HTML: `<p>Die Gesamtkosten setzen sich aus Bestatterleistung, Friedhofs- und Krematoriumsgebühren sowie Fremdleistungen (Steinmetz, Trauerredner, Floristik) zusammen. Eine einfache anonyme Urnenbeisetzung be…`
- **A_TEXT[4]** — Wer trägt die Kosten, wenn Hinterbliebene zahlungsunfähig sind?
  - LD:   `Bei nachgewiesener Zahlungsunfähigkeit übernimmt das Sozialamt Dortmund auf Antrag die erforderlichen Bestattungskosten gemäß § 74 SGB XII. Zuständig ist die Bestattungskostenhilfe im Sozialamt, Hospi…`
  - HTML: `<p>Bei nachgewiesener Zahlungsunfähigkeit übernimmt das Sozialamt Dortmund auf Antrag die erforderlichen Bestattungskosten gemäß § 74 SGB XII. Zuständig ist die Bestattungskostenhilfe im Sozialamt, Ho…`
- **A_TEXT[5]** — Gibt es in Dortmund ein Krematorium?
  - LD:   `Das städtische Krematorium befindet sich auf dem Hauptfriedhof, Rennweg 65, 44143 Dortmund. Die Anlage wird seit 1924 betrieben, 1999 wurde ein Neubau mit drei Etagen-Einäscherungsöfen errichtet. Es w…`
  - HTML: `<p>Ja. Das städtische Krematorium befindet sich auf dem Hauptfriedhof, Rennweg 65, 44143 Dortmund. Es wird seit 1924 betrieben (zunächst mit Etagen-Einäscherungsöfen im Untergeschoss der Urnenhalle); …`
- **A_TEXT[6]** — Welche Bestattungsarten sind in Dortmund möglich?
  - LD:   `Möglich sind klassische Erdbestattungen im Reihen- oder Wahlgrab, Urnenbeisetzungen, Urnennischen im historischen Kolumbarium des Hauptfriedhofs, anonyme Urnenbeisetzungen, Ascheverstreuung im dafür e…`
  - HTML: `<p>Zulässig sind klassische Erdbestattungen im Reihen- oder Wahlgrab, Urnenbeisetzungen, Urnennischen im historischen Kolumbarium des Hauptfriedhofs (für bis zu zwei Aschekapseln in einer Schmuckurne)…`
- **A_TEXT[7]** — Sind muslimische oder jüdische Bestattungen in Dortmund möglich?
  - LD:   `Auf dem Hauptfriedhof Dortmund gibt es einen historischen jüdischen Teil sowie Grabfelder für muslimische Beisetzungen. Die Sargpflicht regelt § 13 BestG NRW; eine sarglose Bestattung kann auf Antrag …`
  - HTML: `<p>Auf dem Hauptfriedhof Dortmund existiert ein historisch gewachsener jüdischer Teil; muslimische Beisetzungen werden auf dafür ausgewiesenen Grabfeldern städtischer Friedhöfe ermöglicht. Die Sargpfl…`

### dresden  (LD=7, HTML=7)

- **A_TEXT[1]** — Wer ist Träger der Dresdner Friedhöfe?
  - LD:   `Die meisten historischen innerstädtischen Friedhöfe in Dresden sind kirchliche Friedhöfe, getragen von einzelnen evangelisch-lutherischen Kirchgemeinden der Evangelisch-Lutherischen Landeskirche Sachs…`
  - HTML: `Die meisten historischen innerstädtischen Friedhöfe sind kirchliche Friedhöfe, getragen von einzelnen evangelisch-lutherischen Kirchgemeinden bzw. von der Verwaltung des Elias-, Trinitatis- und Johann…`
- **A_TEXT[2]** — Was kostet eine Bestattung in Dresden?
  - LD:   `Die Gesamtkosten liegen — wie im Bundesdurchschnitt — typischerweise zwischen 7.000 und 8.000 Euro. Konkrete Friedhofsgebühren auf städtischen Friedhöfen (Friedhofsgebührensatzung der Landeshauptstadt…`
  - HTML: `Die Gesamtkosten liegen — wie im Bundesdurchschnitt — typischerweise zwischen 7.000 und 8.000 Euro. Konkrete Friedhofsgebühren auf städtischen Friedhöfen (Friedhofsgebührensatzung Dresden vom 16.11.20…`
- **A_TEXT[3]** — Welches Recht gilt für Bestattungen in Dresden?
  - LD:   `In Dresden gilt das Sächsische Bestattungsgesetz (SächsBestG), insbesondere § 13 (ärztliche Leichenschau), § 14 (zweite Leichenschau vor Einäscherung), § 18 (Sargpflicht bei Erdbestattungen, mit Ausna…`
  - HTML: `In Dresden gilt das Sächsische Bestattungsgesetz (SächsBestG), insbesondere § 13 (Leichenschau), § 14 (zweite Leichenschau bei Einäscherung), § 18 (Sargpflicht) und § 19 (Friedhofszwang, auch für Asch…`
- **A_TEXT[5]** — Wo wird in Dresden eingeäschert?
  - LD:   `Das Krematorium auf dem Johannisfriedhof Tolkewitz, erbaut 1909–1911 nach Plänen von Fritz Schumacher, gilt als einer der bedeutendsten frühen Reformbauten der Sepulkralarchitektur in Deutschland und …`
  - HTML: `Das Krematorium auf dem Johannisfriedhof Tolkewitz, erbaut 1909–1911 nach Plänen von Fritz Schumacher, gilt als einer der bedeutendsten frühen Reformbauten der Sepulkralarchitektur in Deutschland und …`

### duesseldorf  (LD=7, HTML=7)

- **A_TEXT[3]** — Was ist der Millionenhügel auf dem Nordfriedhof?
  - LD:   `Der Millionenhügel ist die höchste Erhebung im denkmalgeschützten alten Teil des Nordfriedhofs und Standort besonders aufwändiger Familiengrabanlagen Düsseldorfer Industriellen- und Bankiersfamilien. …`
  - HTML: `Der Millionenhügel ist die höchste Erhebung im denkmalgeschützten alten Teil des Nordfriedhofs und Standort besonders aufwändiger Familiengrabanlagen Düsseldorfer Industriellen- und Bankiersfamilien. …`
- **A_TEXT[6]** — Was ist beim Tote-Hosen-Grab auf dem Südfriedhof zu beachten?
  - LD:   `Die Düsseldorfer Punkrock-Band Die Toten Hosen hat im Jahr 2001 auf dem Südfriedhof ein Gemeinschaftsgrabfeld erworben. Beigesetzt sind dort bislang Roadie Uwe Faust, Schlagzeuger Wolfgang 'Wölli' Roh…`
  - HTML: `Die Düsseldorfer Punkrock-Band Die Toten Hosen hat im Jahr 2001 auf dem Südfriedhof ein Gemeinschaftsgrabfeld erworben. Beigesetzt sind dort bislang Roadie Uwe Faust, Schlagzeuger Wolfgang „Wölli" Roh…`

### erfurt  (LD=8, HTML=8)

- **A_TEXT[0]** — Welche Friedhöfe gibt es in Erfurt?
  - LD:   `Die Landeshauptstadt Erfurt betreibt den Hauptfriedhof als Zentralfriedhof sowie 25 kommunale Ortsteilfriedhöfe in den eingemeindeten Stadtteilen. Hinzu kommen evangelische und katholische Friedhöfe i…`
  - HTML: `<div>
      <p>Die Landeshauptstadt Erfurt betreibt den Hauptfriedhof als Zentralfriedhof sowie 25 kommunale Ortsteilfriedhöfe — darunter Hochheim, Hochstedt, Dittelstedt, Gispersleben und Gottstedt. …`
- **A_TEXT[1]** — Wie lange ist die Ruhezeit auf den Erfurter Friedhöfen?
  - LD:   `Nach § 31 Abs. 1 Thüringer Bestattungsgesetz beträgt die Ruhezeit bei Erdbestattungen mindestens 20 Jahre, bei Urnenbeisetzungen mindestens 15 Jahre. Auf den städtischen Friedhöfen in Erfurt gilt nach…`
  - HTML: `<div>
      <p>Nach § 31 Abs. 1 Thüringer Bestattungsgesetz beträgt die Ruhezeit bei Erdbestattungen mindestens 20 Jahre, bei Urnenbeisetzungen mindestens 15 Jahre. Auf den städtischen Friedhöfen in E…`
- **A_TEXT[2]** — Was kostet eine Bestattung auf dem Erfurter Hauptfriedhof?
  - LD:   `Die kommunalen Gebühren ergeben sich aus der Friedhofsgebührensatzung FriedhGebSEF in der Fassung der 1. Änderung vom 06.11.2024 (Beschluss-Nr. 1261/24), in Kraft seit 01.01.2025. Mit dieser Änderung …`
  - HTML: `<div>
      <p>Die kommunalen Gebühren ergeben sich aus der Friedhofsgebührensatzung FriedhGebSEF in der Stammfassung vom 22. Januar 2020, geändert durch die 1. Änderungssatzung vom 06.11.2024 (in Kra…`
- **A_TEXT[3]** — Wo muss ein Sterbefall in Erfurt angezeigt werden?
  - LD:   `Sterbefälle werden beim Standesamt der Landeshauptstadt Erfurt, Urkundenstelle im Bürgeramt, Bürgermeister-Wagner-Straße 1, 99084 Erfurt, beurkundet. Die Urkundenstelle ist telefonisch unter 0361 655-…`
  - HTML: `<div>
      <p>Zuständig ist das Standesamt der Landeshauptstadt Erfurt — Urkundenstelle im Bürgeramt, Bürgermeister-Wagner-Straße 1, 99084 Erfurt, telefonisch erreichbar unter 0361 655-7654. In der R…`
- **A_TEXT[4]** — Was ist eine Sozialbestattung in Erfurt?
  - LD:   `Wenn die nach Thüringer Bestattungsgesetz bestattungspflichtige Person die Kosten nicht tragen kann, übernimmt nach § 74 SGB XII der Sozialhilfeträger die erforderlichen Bestattungskosten. Zuständig i…`
  - HTML: `<div>
      <p>Wenn die nach Thüringer Bestattungsgesetz bestattungspflichtige Person die Kosten nicht tragen kann, übernimmt nach § 74 SGB XII der Sozialhilfeträger die erforderlichen Bestattungskost…`
- **A_TEXT[5]** — Gibt es in Erfurt ein Krematorium?
  - LD:   `Ja. Das städtische Krematorium befindet sich auf dem Hauptfriedhof und wurde nach Plänen des ungarischen Architekten János Szabó in den Jahren 1975 bis 1977 errichtet. Es gilt als bedeutendster Kremat…`
  - HTML: `<div>
      <p>Ja. Das städtische Krematorium befindet sich auf dem Hauptfriedhof und wurde nach Plänen des ungarischen Architekten János Szabó in den Jahren 1975 bis 1977 errichtet. Es gilt als bedeu…`
- **A_TEXT[6]** — Wie lange darf ein Verstorbener in Erfurt zu Hause aufgebahrt werden?
  - LD:   `Nach § 16 Abs. 1 Thüringer Bestattungsgesetz ist ein Leichnam innerhalb von 48 Stunden nach Eintritt des Todes in eine Leichenhalle zu überführen. In dieser Frist ist eine Hausaufbahrung rechtlich zul…`
  - HTML: `<div>
      <p>Nach § 16 Abs. 1 Thüringer Bestattungsgesetz ist ein Leichnam innerhalb von 48 Stunden nach Eintritt des Todes in eine Leichenhalle zu überführen. Innerhalb dieser Frist ist eine Hausau…`

### essen  (LD=8, HTML=8)

- **A_TEXT[0]** — Welche Bestattungsfrist gilt in Essen?
  - LD:   `In Essen gelten die landesrechtlichen Fristen aus dem BestG NRW: Erdbestattungen dürfen frühestens 24 Stunden nach Eintritt des Todes erfolgen und müssen innerhalb von zehn Tagen durchgeführt werden. …`
  - HTML: `<div class="mr-faq-body">In Essen gelten die landesrechtlichen Fristen aus dem BestG NRW: Erdbestattungen dürfen frühestens 24 Stunden nach Eintritt des Todes erfolgen und müssen innerhalb von zehn Ta…`
- **A_TEXT[1]** — Wie viele kommunale Friedhöfe gibt es in Essen?
  - LD:   `Die Stadt Essen verwaltet 23 kommunale Friedhöfe, die von Grün und Gruga Essen unterhalten werden. Zu den vier größten zählen der Parkfriedhof in Huttrop, der Südwestfriedhof in Fulerum, der Ostfriedh…`
  - HTML: `<div class="mr-faq-body">Die Stadt Essen verwaltet 23 kommunale Friedhöfe, die von Grün und Gruga Essen unterhalten werden. Heute prägen vier große Zentralfriedhöfe (Parkfriedhof Huttrop, Südwestfried…`
- **Q_TEXT[2]**
  - LD:   `Was kostet eine Bestattung in Essen?`
  - HTML: `Was kostet eine Bestattung in Essen realistisch?`
- **A_TEXT[2]** — Was kostet eine Bestattung in Essen?
  - LD:   `Die Gesamtkosten setzen sich aus Friedhofsgebühren der Stadt Essen (Grabnutzungsrecht plus Bestattungsgebühr) und den Bestatterleistungen zusammen. Realistisch liegt die Spanne für eine einfache Feuer…`
  - HTML: `<div class="mr-faq-body">Eine einfache Feuerbestattung mit Urnenreihengrab liegt in Essen bei etwa 3.000 bis 4.500 €, eine Erdbestattung mit Sargwahlgrab bei rund 5.000 bis 8.000 €. Mit Grabstein, Dau…`
- **A_TEXT[3]** — Wer übernimmt die Kosten bei Mittellosigkeit – Sozialbestattung in Essen?
  - LD:   `In Essen prüft das Amt für Soziales und Wohnen Anträge auf Übernahme der Bestattungskosten nach § 74 SGB XII. Der Antrag wird möglichst vor der Beisetzung gestellt; die Mitgliedsbetriebe des Stadtverb…`
  - HTML: `<div class="mr-faq-body">In Essen prüft das Amt für Soziales und Wohnen Anträge auf Übernahme der Bestattungskosten nach § 74 SGB XII. Der Antrag wird möglichst vor der Beisetzung gestellt; die Mitgli…`
- **A_TEXT[5]** — Ist auf den Essener Friedhöfen eine Tuchbestattung möglich?
  - LD:   `Das BestG NRW enthält keinen ausdrücklichen allgemeinen Sargzwang; nach § 15 BestG NRW können bestimmte Glaubensgemeinschaften die Bestattung ohne Sarg vorsehen. Maßgeblich für die kommunalen Friedhöf…`
  - HTML: `<div class="mr-faq-body">Das BestG NRW enthält in § 15 keinen ausdrücklichen allgemeinen Sargzwang; die Vorschrift sieht vor, dass Mitgliedern bestimmter Glaubensgemeinschaften eine sarglose Bestattun…`
- **A_TEXT[6]** — Wo werden Sterbefälle in Essen beurkundet?
  - LD:   `Sterbefälle werden beim Standesamt der Stadt Essen beurkundet. Die Sterbeurkunde wird in der Regel über das beauftragte Bestattungsunternehmen oder direkt durch Angehörige angefordert; sie wird für Re…`
  - HTML: `<div class="mr-faq-body">Sterbefälle werden beim Standesamt der Stadt Essen im Rathaus, Porscheplatz 1, 45121 Essen, beurkundet. Die Anzeige erfolgt in der Regel über das beauftragte Bestattungsuntern…`

### frankfurt  (LD=6, HTML=6)

- **A_TEXT[2]** — Was kostet eine Bestattung in Frankfurt am Main?
  - LD:   `Die Friedhofsgebühr der Stadt Frankfurt liegt 2025 für eine Erdbestattung bei rund 1.596 Euro, für eine Urnenbeisetzung im Erdgrab bei rund 1.006 Euro. Inklusive Bestatter-Leistungen, Sarg, Trauerfeie…`
  - HTML: `Die Friedhofsgebühr der Stadt Frankfurt liegt 2025 für eine Erdbestattung bei rund 1.596 Euro, für eine Urnenbeisetzung im Erdgrab bei rund 1.006 Euro und in einer Urnenkammer bei rund 789 Euro. Inklu…`
- **A_TEXT[3]** — Welches Bestattungsrecht gilt in Frankfurt?
  - LD:   `Es gilt das hessische Friedhofs- und Bestattungsgesetz (FBG) vom 5. Juli 2007 in der Fassung der Novelle vom 30. September 2025. Die Höchstfrist für Erdbestattungen beträgt seither zehn Tage statt vie…`
  - HTML: `Es gilt das hessische Friedhofs- und Bestattungsgesetz (FBG) vom 5. Juli 2007 in der Fassung der Novelle vom 30. September 2025. Die Höchstfrist für Erdbestattungen beträgt seither zehn Tage statt vie…`
- **A_TEXT[5]** — Welche Behörde verwaltet die Frankfurter Friedhöfe?
  - LD:   `Das Grünflächenamt der Stadt Frankfurt, Abteilung Friedhofsangelegenheiten. Service-Telefon 069 212-36480 (Montag bis Freitag 8 bis 12 und 13 bis 15 Uhr). Die Abteilung betreut 37 kommunale Friedhöfe …`
  - HTML: `Das Grünflächenamt der Stadt Frankfurt, Abteilung Friedhofsangelegenheiten. Service-Telefon 069 212-36480 (Montag bis Freitag 8 bis 12 und 13 bis 15 Uhr). Die Abteilung betreut die 37 kommunalen Fried…`

### freiburg  (LD=7, HTML=7)

- **A_TEXT[1]** — Wer ist Friedhofsträger in Freiburg?
  - LD:   `Träger der städtischen Friedhöfe in Freiburg ist der Eigenbetrieb Friedhöfe der Stadt Freiburg im Breisgau. Maßgeblich ist die Friedhofssatzung der Stadt Freiburg vom 19. März 2024, in Kraft seit 1. M…`
  - HTML: `Träger der städtischen Friedhöfe in Freiburg ist der Eigenbetrieb Friedhöfe der Stadt Freiburg im Breisgau (Friedhofstraße 8, 79106 Freiburg). Maßgeblich ist die Friedhofssatzung vom 19. März 2024, in…`
- **A_TEXT[2]** — Welche Paragraphen des BestattG BW gelten in Freiburg?
  - LD:   `In Freiburg gilt das Bestattungsgesetz Baden-Württemberg vom 21. Juli 1970. Zentrale Paragraphen sind §§ 20–22 (Leichenschau), § 30 (Bestattungspflicht), § 31 (Bestattungspflichtige), § 32 (Bestattung…`
  - HTML: `In Freiburg gilt das Bestattungsgesetz Baden-Württemberg vom 21. Juli 1970. Zentrale Paragraphen sind §§ 20–22 (Leichenschau, Veranlassung, Vornahme), § 30 (Bestattungspflicht), § 31 (Bestattungspflic…`
- **A_TEXT[3]** — Wie lange dauert die Ruhezeit auf dem Hauptfriedhof Freiburg?
  - LD:   `Nach § 14 Abs. 1 der Freiburger Friedhofssatzung beträgt die Ruhezeit für Särge und Aschenurnen 15 Jahre. Bei Kindern, die vor Vollendung des zehnten Lebensjahres verstorben sind, beträgt die Ruhezeit…`
  - HTML: `Nach § 14 Abs. 1 der Freiburger Friedhofssatzung beträgt die Ruhezeit für Särge und Aschenurnen 15 Jahre, bei Kindern vor Vollendung des zehnten Lebensjahres zehn Jahre. Damit liegt Freiburg am untere…`
- **A_TEXT[4]** — Was kostet eine Bestattung in Freiburg?
  - LD:   `Nach dem Gebührenverzeichnis zur Freiburger Friedhofssatzung (in Kraft seit 1. Mai 2024): Grundgebühr Erdbestattung 1.795 €, Beisetzen einer Urne 453 €. Reihengrab Erwachsene 346 €, Rasenreihengrab Er…`
  - HTML: `Nach dem Gebührenverzeichnis zur Freiburger Friedhofssatzung (Stand 1. Mai 2024): Grundgebühr Erdbestattung 1.795 €, Beisetzen einer Urne 453 €. Reihengrab Erwachsene 346 €, Rasenreihengrab 568 €, Urn…`
- **A_TEXT[5]** — Welche Bestatter sind in Freiburg vertreten?
  - LD:   `In Freiburg sind Mitgliedsbetriebe des Bundesverbands Deutscher Bestatter (BDB) sowie unabhängige Häuser tätig. Der BDB bietet eine Suche nach Postleitzahl. Der Eigenbetrieb Friedhöfe der Stadt Freibu…`
  - HTML: `In Freiburg sind Mitgliedsbetriebe des Bundesverbands Deutscher Bestatter (BDB) sowie unabhängige Häuser tätig. machsruhig.de gibt bewusst keine namentlichen Empfehlungen. Eine Freiburger Besonderheit…`
- **A_TEXT[6]** — Gibt es einen jüdischen Friedhof in Freiburg?
  - LD:   `Ja. Die 1863 rechtlich konstituierte Jüdische Gemeinde Freiburg legte 1870 an der Ecke Elsässer Straße/Rosbaumweg einen eigenen Friedhof an. Er umfasst 82,61 Ar und rund 900 Grabsteine, ist denkmalges…`
  - HTML: `Ja. Die 1863 rechtlich konstituierte Jüdische Gemeinde Freiburg legte 1870 an der Ecke Elsässer Straße/Rosbaumweg einen eigenen Friedhof an. Er umfasst 82,61 Ar und rund 900 Grabsteine, ist denkmalges…`

### gelsenkirchen  (LD=8, HTML=8)

- **A_TEXT[0]** — Wie lange darf eine Bestattung in Gelsenkirchen aufgeschoben werden?
  - LD:   `Nach § 13 Abs. 3 BestG NRW müssen Erdbestattungen und Einäscherungen innerhalb von zehn Tagen nach dem Todesfall durchgeführt werden. Die Totenasche ist innerhalb von sechs Wochen beizusetzen. Auf Ant…`
  - HTML: `<div class="answer">
      <p>Nach § 13 Abs. 3 BestG NRW müssen Erdbestattungen und Einäscherungen innerhalb von zehn Tagen nach dem Todesfall durchgeführt werden. Die Totenasche ist innerhalb von sec…`
- **A_TEXT[1]** — Wer trägt in Gelsenkirchen die Bestattungspflicht?
  - LD:   `§ 8 BestG NRW regelt die Rangfolge: Ehegatten und Lebenspartner, dann volljährige Kinder, dann Eltern, volljährige Geschwister, Großeltern und volljährige Enkelkinder. Ist niemand der Genannten verfüg…`
  - HTML: `<div class="answer">
      <p>§ 8 BestG NRW regelt die Rangfolge: Ehegatten und Lebenspartner, dann volljährige Kinder, dann Eltern, volljährige Geschwister, Großeltern und volljährige Enkelkinder. Is…`
- **A_TEXT[2]** — Was kostet ein einfaches Urnenreihengrab auf einem städtischen Friedhof in Gelsenkirchen?
  - LD:   `Nach der Friedhofsgebührensatzung der Stadt Gelsenkirchen, gültig ab 01.01.2025, kostet das Nutzungsrecht inklusive Grabbereitung für eine Urnen-Reihengrabstätte 1.903 Euro. Hinzu kommen die Leistunge…`
  - HTML: `<div class="answer">
      <p>Nach der Friedhofsgebührensatzung der Stadt Gelsenkirchen, gültig ab 01.01.2025 (Fassung vom 18.12.2024), kostet das Nutzungsrecht inklusive Grabbereitung für eine Urnen-…`
- **A_TEXT[3]** — Gibt es in Gelsenkirchen einen Themenfriedhof?
  - LD:   `Ja. Auf dem städtischen Friedhof Beckhausen-Sutum, in Sichtweite der Veltins-Arena, liegt das Schalker Fan-Feld — ein als Stadion angelegtes Gemeinschaftsgrabfeld, angelegt auf eine Endausbaustufe von…`
  - HTML: `<div class="answer">
      <p>Ja. Auf dem städtischen Friedhof Beckhausen-Sutum, in Sichtweite der Veltins-Arena, liegt das Schalker Fan-Feld — ein als Stadion angelegtes Gemeinschaftsgrabfeld, angele…`
- **A_TEXT[4]** — Übernimmt das Sozialamt in Gelsenkirchen Bestattungskosten?
  - LD:   `Ja, nach § 74 SGB XII. Wenn der Bestattungspflichtige die Kosten nicht aufbringen kann, übernimmt der Fachbereich Soziales der Stadt Gelsenkirchen die erforderlichen Kosten. Der Antrag muss zeitnah, m…`
  - HTML: `<div class="answer">
      <p>Ja, nach § 74 SGB XII. Wenn der Bestattungspflichtige die Kosten nicht aufbringen kann, übernimmt der Fachbereich Soziales der Stadt Gelsenkirchen die erforderlichen Kost…`
- **A_TEXT[5]** — Welche Bestattungsarten bieten die städtischen Friedhöfe Gelsenkirchen?
  - LD:   `Wahl- und Reihengrabstätten für Sarg und Urne, Gemeinschaftsgräber, dauergrabgepflegte Gemeinschaftsgräber, Friedhain (Baumgrab), Naturgrabstätten in Wiesenfeldern sowie auf dem Hauptfriedhof Buer sei…`
  - HTML: `<div class="answer">
      <p>Wahl- und Reihengrabstätten für Sarg und Urne, Gemeinschaftsgräber, dauergrabgepflegte Gemeinschaftsgräber, Friedhain (Baumgrab), Naturgrabstätten in Wiesenfeldern sowie …`
- **A_TEXT[6]** — Wo wird der Sterbefall in Gelsenkirchen beurkundet?
  - LD:   `Zuständig ist das Standesamt der Stadt Gelsenkirchen im Hans-Sachs-Haus, Ebertstraße 11, 45879 Gelsenkirchen. Der Sterbefall ist nach § 28 PStG spätestens am dritten auf den Tod folgenden Werktag dort…`
  - HTML: `<div class="answer">
      <p>Zuständig ist das Standesamt der Stadt Gelsenkirchen im Hans-Sachs-Haus, Ebertstraße 11, 45879 Gelsenkirchen. Der Sterbefall ist nach § 28 PStG spätestens am dritten auf …`
- **A_TEXT[7]** — Wo finde ich Trauerbegleitung und Hospizdienste in Gelsenkirchen?
  - LD:   `Trauerbegleitung in Gelsenkirchen leistet unter anderem der Ambulante Hospizdienst Gelsenkirchen sowie der Caritasverband und das Diakoniewerk Gelsenkirchen-Wattenscheid mit Trauergruppen und Einzelge…`
  - HTML: `<div class="answer">
      <p>Trauerbegleitung in Gelsenkirchen leistet unter anderem der Ambulante Hospizdienst Gelsenkirchen, der Caritasverband sowie das Diakoniewerk Gelsenkirchen und Wattenscheid…`

### hagen  (LD=7, HTML=7)

- **A_TEXT[6]** — Welche Stelle führt die zweite Leichenschau vor einer Feuerbestattung in Hagen durch?
  - LD:   `Vor jeder Einäscherung im Eduard-Müller-Krematorium ist nach § 15 Abs. 1 BestG NRW eine weitere ärztliche Leichenschau erforderlich. Veranlasst wird sie durch die untere Gesundheitsbehörde des Sterbe-…`
  - HTML: `<p>Vor jeder Einäscherung im Eduard-Müller-Krematorium ist nach § 15 Abs. 1 BestG NRW eine weitere ärztliche Leichenschau erforderlich. Veranlasst wird sie durch die untere Gesundheitsbehörde des Ster…`

### halle  (LD=7, HTML=7)

- **A_TEXT[0]** — Wie viele Friedhöfe gibt es in Halle (Saale)?
  - LD:   `Die Stadt Halle (Saale) unterhält 14 kommunale Friedhöfe. Sie sind in § 1 der Friedhofsgebührensatzung abschließend benannt: Gertraudenfriedhof, Südfriedhof, Nordfriedhof, Friedhof Neustadt, Kröllwitz…`
  - HTML: `<p>Die Stadt Halle (Saale) unterhält 14 kommunale Friedhöfe. Sie sind in § 1 der Friedhofsgebührensatzung abschließend benannt: Gertraudenfriedhof, Südfriedhof, Nordfriedhof, Friedhof Neustadt, Kröllw…`
- **A_TEXT[1]** — Welche Bestattungsfrist gilt in Halle (Saale)?
  - LD:   `Nach § 17 BestattG LSA dürfen Leichen frühestens 48 Stunden nach Todeseintritt bestattet werden. Erdbestattung oder Einäscherung sollen innerhalb von zehn Tagen nach Todeseintritt erfolgen. Urnen sind…`
  - HTML: `<p>Nach § 17 BestattG LSA dürfen Leichen frühestens 48 Stunden nach Eintritt des Todes bestattet werden. Erdbestattung oder Einäscherung sollen innerhalb von zehn Tagen nach Todeseintritt vorgenommen …`
- **A_TEXT[2]** — Was kostet ein Reihengrab in Halle (Saale)?
  - LD:   `Die Grabnutzungsgebühren für Reihen- und Urnenreihengräber in Halle bewegen sich nach der städtischen Friedhofsgebührensatzung (Lesefassung vom 26.11.2022) im niedrigen bis mittleren dreistelligen Ber…`
  - HTML: `<p>Die Grabnutzungsgebühren für Reihen- und Urnenreihengräber in Halle bewegen sich nach der städtischen Friedhofsgebührensatzung (Lesefassung vom 26.11.2022) für eine Nutzungszeit von 20 Jahren im ni…`
- **A_TEXT[3]** — Gilt in Sachsen-Anhalt Sargpflicht?
  - LD:   `Nicht mehr uneingeschränkt. Mit der vom Landtag am 11. September 2025 verabschiedeten Novelle des BestattG LSA wurde die allgemeine Sargpflicht aus religiösen oder weltanschaulichen Gründen gelockert.…`
  - HTML: `<p>Nicht mehr uneingeschränkt. Der Landtag verabschiedete die Novelle des BestattG LSA am 11. September 2025; das neue Gesetz ist zum 1. Mai 2026 in Kraft getreten. Seit Inkrafttreten ist die allgemei…`
- **A_TEXT[4]** — Wo wird die Sterbeurkunde in Halle ausgestellt?
  - LD:   `Zuständig ist die Abteilung Standesamt der Stadt Halle (Saale), Marktplatz 1, 06108 Halle. Die Abgabe von Sterbefallanzeigen ist dienstags (9–12 und 13–16 Uhr) und donnerstags (9–12 und 13–15 Uhr) ohn…`
  - HTML: `<p>Zuständig ist die Abteilung Standesamt der Stadt Halle (Saale), Marktplatz 1, 06108 Halle. Die Abgabe von Sterbefallanzeigen ist dienstags (9–12 und 13–16 Uhr) und donnerstags (9–12 und 13–15 Uhr) …`
- **Q_TEXT[5]**
  - LD:   `Wie lange ist die Ruhezeit auf Halleschen Friedhöfen?`
  - HTML: `Wie lange ist die Ruhezeit auf halleschen Friedhöfen?`
- **A_TEXT[5]** — Wie lange ist die Ruhezeit auf Halleschen Friedhöfen?
  - LD:   `Die Ruhezeit wird in § 13 der Friedhofssatzung der Stadt Halle (Saale) festgelegt. Reihen- und Urnenreihengräber sowie Urnengemeinschaftsanlagen werden in Halle mit einer Nutzungszeit von 20 Jahren ve…`
  - HTML: `<p>Die genaue Ruhezeit wird in § 13 der Friedhofssatzung der Stadt Halle (Saale) festgelegt. Reihen- und Urnenreihengräber sowie Urnengemeinschaftsanlagen werden in Halle mit einer Nutzungszeit von 20…`
- **A_TEXT[6]** — Können Urnen auf dem Stadtgottesacker bestattet werden?
  - LD:   `Ja. Nach einem längeren Verbot von Beisetzungen sind Urnenbestattungen innerhalb der Friedhofsmauern des Stadtgottesackers heute wieder möglich. Der Stadtgottesacker zählt zu den 14 kommunalen Friedhö…`
  - HTML: `<p>Ja. Nach einem längeren Verbot von Beisetzungen sind Urnenbestattungen innerhalb der Friedhofsmauern des Stadtgottesackers heute wieder möglich. Der Stadtgottesacker zählt zu den 14 kommunalen Frie…`

### hamburg  (LD=4, HTML=7)

- **COUNT-Mismatch:** JSON-LD hat 4 Q/A, HTML hat 7
- **Q_TEXT[0]**
  - LD:   `Was kostet eine Bestattung in Hamburg?`
  - HTML: `Was kostet eine Bestattung in Hamburg — Gesamtbudget?`
- **A_TEXT[0]** — Was kostet eine Bestattung in Hamburg?
  - LD:   `Die Friedhofsgebühren für ein Sargwahlgrab liegen bei 2.800–3.195 € (25 Jahre). Ein Urnenwahlgrab kostet 2.000–2.230 €. Hinzu kommen Bestatterleistungen (1.200–2.500 €). Eine anonyme Beisetzung ist mi…`
  - HTML: `Die Gesamtkosten setzen sich aus mehreren Positionen zusammen: Friedhofsgebühren (z.B. Sargwahlgrab 2.800–3.195 €) + Bestatterleistungen (Erdbestattung ab 1.945 €, Feuerbestattung ab 1.580 €) + eventu…`
- **Q_TEXT[1]**
  - LD:   `Ist der Ohlsdorf offen für Besucher?`
  - HTML: `Ist der Ohlsdorf wirklich der größte Friedhof der Welt?`
- **A_TEXT[1]** — Ist der Ohlsdorf offen für Besucher?
  - LD:   `Ja, der Ohlsdorf ist ein öffentlicher Friedhof und eine beliebte Parkanlage. Viele Hamburger besuchen ihn zum Spazieren und zur Grabpflege. Es gibt Führungen und Informationszentren.…`
  - HTML: `Ja, der Ohlsdorf ist mit 389 Hektar (zum Vergleich: Central Park NY = 341 ha) der weltgrößte Parkfriedhof. Er wurde 1877 gegründet und ist nicht nur Begräbnisort (202.000 Grabstellen, 1,4 Mio. Bestatt…`
- **A_TEXT[2]** — Kann man in Hamburg eine Seebestattung durchführen lassen?
  - LD:   `Ja, Hamburg bietet Seebestattungen an. Die Urne wird von einem Schiff aus in Nord- oder Ostsee beigesetzt. Eine unbegleitete Seebestattung beginnt ab 1.049 € (Paketpreis). Begleitete Fahrten kosten ca…`
  - HTML: `Ja, Seebestattungen sind in Hamburg eine Tradition und völlig legal. Die Urne wird von einem speziellen, behördlich genehmigten Schiff aus in die Nord- oder Ostsee beigesetzt (vor Helgoland, in der Lü…`
- **A_TEXT[3]** — Wie lange habe ich Zeit, eine Bestattung zu organisieren?
  - LD:   `Die Überführung muss innerhalb von 36 Stunden erfolgen. Eine Erdbestattung muss spätestens nach 10 Tagen durchgeführt sein. Das gibt mehr Zeit zur Organisation als in anderen Bundesländern.…`
  - HTML: `Nach dem Todesfall: Überführung in Leichenhalle innerhalb 36 Stunden (gesetzlich verpflichtend). Erdbestattung muss spätestens nach 10 Tagen erfolgen — dies gibt der Familie ausreichend Zeit (mehr als…`

### heidelberg  (LD=9, HTML=9)

- **A_TEXT[0]** — Wie lange ist die Ruhezeit auf Heidelberger Friedhöfen?
  - LD:   `Nach § 6 Abs. 1 BestattG BW beträgt die Mindestruhezeit für Erwachsene 15 Jahre, für Kinder unter 10 Jahren 10 Jahre und für Kinder unter 2 Jahren 6 Jahre. Diese Mindestruhezeiten gelten auch für Asch…`
  - HTML: `<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">Nach § 6 Abs. 1 BestattG BW beträgt die Mindestruhezeit für Erwachsene 15 Jahre, für Kinder unte…`
- **A_TEXT[1]** — Bis wann muss in Heidelberg bestattet werden?
  - LD:   `Nach § 37 Abs. 1 BestattG BW muss ein Verstorbener spätestens 96 Stunden nach Todeseintritt bestattet oder auf den Transportweg gebracht werden. Tage, an denen nicht bestattet wird, bleiben unberücksi…`
  - HTML: `<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">Nach § 37 Abs. 1 BestattG BW muss ein Verstorbener, der nicht in einer Leichenhalle aufgebahrt i…`
- **A_TEXT[2]** — Kann in Heidelberg eine anonyme Bestattung erfolgen?
  - LD:   `Anonyme Bestattungen sind auf mehreren Heidelberger Friedhöfen möglich, in der Regel als Urnenbeisetzung in einem gesonderten Grabfeld. Nicht jeder Friedhof bietet diese Form an; auf dem Friedhof Hand…`
  - HTML: `<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">Anonyme Bestattungen sind auf mehreren Heidelberger Friedhöfen möglich — in der Regel als Urnenb…`
- **A_TEXT[3]** — Gibt es in Heidelberg ein muslimisches Gräberfeld?
  - LD:   `Ja, sogar zwei unterschiedliche Angebote. Der Friedhof Pfaffengrund am Diebsweg ist der einzige Heidelberger Friedhof mit nach Mekka ausgerichteten Gräbern für strenggläubige muslimische Bestattungen.…`
  - HTML: `<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">Ja, sogar zwei unterschiedliche Angebote. Der Friedhof Pfaffengrund am Diebsweg ist der einzige …`
- **A_TEXT[4]** — Gibt es in Heidelberg ein Krematorium?
  - LD:   `Ja. Auf dem Bergfriedhof an der Rohrbacher Straße steht das am 22. Dezember 1891 in Betrieb genommene Krematorium der Stadt Heidelberg, nach dem 1878 in Gotha eröffneten Krematorium das zweitälteste e…`
  - HTML: `<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">Ja. Auf dem Bergfriedhof an der Rohrbacher Straße steht das am 22. Dezember 1891 in Betrieb geno…`
- **A_TEXT[5]** — Wo wird der Sterbefall in Heidelberg angezeigt?
  - LD:   `Beim Standesamt Heidelberg in der Bergheimer Straße 69, 69115 Heidelberg. Anzeigepflichtig sind in der Regel Angehörige oder das beauftragte Bestattungsunternehmen. Mitzubringen sind Totenschein, Pers…`
  - HTML: `<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">Beim Standesamt Heidelberg in der Bergheimer Straße 69, 69115 Heidelberg. Zuständig ist das Stan…`
- **A_TEXT[6]** — Was kostet eine Bestattung in Heidelberg insgesamt?
  - LD:   `Stand: Mai 2026. Eine anonyme Feuerbestattung beginnt bei rund 1.900 € bis 2.500 €. Eine Feuerbestattung mit Urnen-Reihengrab und Trauerfeier liegt bei 3.500 € bis 5.500 €. Eine Erdbestattung mit Wahl…`
  - HTML: `<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">Die Gesamtkosten hängen stark von Bestattungsart und Grabwahl ab (Stand: Mai 2026). Eine einfach…`
- **A_TEXT[7]** — Ist eine Seebestattung von Heidelberg aus möglich?
  - LD:   `Ja, aber nicht im Neckar. Nach § 32 Abs. 2 BestattG BW ist eine Seebestattung als Beisetzung einer Urne auf Hoher See zulässig; in oberirdischen Binnengewässern wie Bodensee oder Neckar ist sie nicht …`
  - HTML: `<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">Ja, aber nicht im Neckar. Nach § 32 Abs. 2 BestattG BW ist eine Seebestattung als Beisetzung ein…`
- **A_TEXT[8]** — Welcher Heidelberger Friedhof ist der historisch interessanteste?
  - LD:   `Eindeutig der Bergfriedhof. Dort ruhen unter anderem Friedrich Ebert, Robert Bunsen, Max Weber, Wilhelm Furtwängler und Felix Wankel. Die Anlage ist als Gartendenkmal nach Johann Metzger erhalten, beh…`
  - HTML: `<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
      <p itemprop="text">Eindeutig der Bergfriedhof. Dort ruhen unter anderem Reichspräsident Friedrich Ebert, der Chemik…`

### karlsruhe  (LD=7, HTML=7)

- **A_TEXT[4]** — Was kostet eine Bestattung in Karlsruhe?
  - LD:   `Nach der Karlsruher Friedhofgebührensatzung (Stand 01.01.2026): Erdbestattungsreihengrab 877 €, Urnenreihengrab 791 €, Erdbestattungswahlgrab 2.000–3.080 €, Urnenwahlgrab 1.860 €, Kolumbariennische 1.…`
  - HTML: `Nach der Karlsruher Friedhofgebührensatzung (Stand 1. Januar 2026): Erdbestattungsreihengrab 877 €, Urnenreihengrab 791 €, Erdbestattungswahlgrab 2.000–3.080 €, Urnenwahlgrab 1.860 €, Kolumbariennisch…`

### kiel  (LD=8, HTML=8)

- **A_TEXT[0]** — Wie viele Friedhöfe gibt es in Kiel?
  - LD:   `In Kiel sind zwölf größere Friedhöfe in Betrieb: fünf städtische unter Trägerschaft der Stadt Kiel (Nordfriedhof, Ostfriedhof, Urnenfriedhof, Friedhof Russee, Friedhof Meimersdorf) sowie sieben kirchl…`
  - HTML: `<p>In Kiel sind nach Angaben der Landeshauptstadt zwölf größere Friedhöfe in Betrieb: fünf städtische unter Trägerschaft der Stadt Kiel (Nordfriedhof, Ostfriedhof, Urnenfriedhof, Friedhof Russee, Frie…`
- **A_TEXT[1]** — Welcher Friedhof in Kiel ist der größte?
  - LD:   `Der Parkfriedhof Eichhof mit rund 39 Hektar, eröffnet 1900, ist der größte Friedhof Kiels und gehört zu den größten Friedhöfen in Schleswig-Holstein. Der größte rein städtische Friedhof Kiels ist der …`
  - HTML: `<p>Der Parkfriedhof Eichhof mit rund 39 Hektar Fläche, eröffnet am 5. Juli 1900, ist der größte Friedhof Kiels und gehört zu den größten Friedhöfen in Schleswig-Holstein. Innerhalb des Kieler Stadtgeb…`
- **A_TEXT[2]** — Was kostet eine Bestattung in Kiel insgesamt?
  - LD:   `Eine einfache Feuerbestattung mit Urnenreihengrab kostet in Kiel rund 3.500 bis 5.000 Euro. Eine Erdbestattung mit Trauerfeier liegt typischerweise bei 5.500 bis 8.500 Euro zuzüglich Grabstein. Anonym…`
  - HTML: `<p>Eine einfache Feuerbestattung mit Urnenreihengrab kostet in Kiel insgesamt rund 3.500 bis 5.000 Euro inklusive Bestatter-, Krematoriums- und Friedhofsgebühren. Eine klassische Erdbestattung mit Tra…`
- **A_TEXT[3]** — Wie lange ist die Ruhezeit auf Kieler Friedhöfen?
  - LD:   `Die Ruhezeit beträgt für Särge in der Regel 25 Jahre, für Urnen 20 Jahre und für Kindersärge 15 Jahre, festgelegt in den Friedhofssatzungen der Stadt Kiel und des Kirchenkreises Altholstein.…`
  - HTML: `<p>Auf den Kieler Friedhöfen beträgt die Ruhezeit für Särge in der Regel 25 Jahre, für Urnen 20 Jahre und für Kindersärge 15 Jahre. Diese Fristen sind in der Friedhofssatzung der Stadt Kiel bzw. des K…`
- **A_TEXT[4]** — Innerhalb welcher Frist muss in Schleswig-Holstein eine Urne beigesetzt werden?
  - LD:   `Seit der Novelle des Bestattungsgesetzes Schleswig-Holstein vom 13. Dezember 2024 (in Kraft seit 31. Dezember 2024) gilt nach § 16 Absatz 3 BestattG SH eine Frist von drei Monaten ab der Einäscherung.…`
  - HTML: `<p>Seit der Novelle des Bestattungsgesetzes Schleswig-Holstein vom 13. Dezember 2024 (in Kraft seit 31. Dezember 2024) gilt nach § 16 Absatz 3 BestattG SH eine Frist von drei Monaten ab der Einäscheru…`
- **A_TEXT[5]** — Wo befindet sich das zuständige Standesamt für die Sterbeanzeige in Kiel?
  - LD:   `Zuständig ist das Standesamt der Landeshauptstadt Kiel, Fleethörn 9, 24103 Kiel im Rathaus. In der Regel übernimmt der beauftragte Bestatter die Anzeige des Sterbefalls im Auftrag der Angehörigen inne…`
  - HTML: `<p>Zuständig ist das Standesamt der Landeshauptstadt Kiel, Fleethörn 9, 24103 Kiel (Rathaus). Im Regelfall übernimmt der beauftragte Bestatter die Anzeige des Sterbefalls im Auftrag der Angehörigen, s…`
- **A_TEXT[6]** — Ist eine Seebestattung in der Kieler Förde möglich?
  - LD:   `Ja. Seebestattungen sind in Schleswig-Holstein nach § 15 BestattG SH zulässig und werden von mehreren Kieler Bestattern in der westlichen Ostsee – meist vor Laboe und in der Kieler Bucht – durchgeführ…`
  - HTML: `<p>Ja. Seebestattungen sind in Schleswig-Holstein nach § 15 BestattG SH zulässig und werden von mehreren Kieler Bestattern in der westlichen Ostsee – meist in den ausgewiesenen Beisetzungsgebieten vor…`
- **A_TEXT[7]** — Wer trägt die Bestattungskosten, wenn keine Angehörigen vorhanden sind?
  - LD:   `Sind keine Angehörigen vorhanden oder verweigern diese die Bestattung, übernimmt nach § 13 BestattG SH die Gemeinde – in Kiel die Landeshauptstadt – die Bestattung als Ersatzvornahme und fordert die K…`
  - HTML: `<p>Nach § 13 BestattG SH sind in Schleswig-Holstein zunächst die nahen Angehörigen bestattungspflichtig. Sind keine Angehörigen vorhanden oder verweigern diese die Bestattung, übernimmt die Gemeinde –…`

### koeln  (LD=5, HTML=5)

- **A_TEXT[0]** — Was kostet eine Bestattung in Köln?
  - LD:   `Die Friedhofsgebühren der Stadt Köln liegen bei ca. 2.600 € für pflegefreie Urnengräber (20 Jahre) und 2.900–3.000 € für Erdwahlgräber (25–30 Jahre). Hinzu kommen Bestatterleistungen (1.200–2.500 €), …`
  - HTML: `Die Friedhofsgebühren der Stadt Köln sind stabil und liegen bei ca. 2.600 € für pflegefrei Urnengräber (20 Jahre) und 2.900–3.000 € für Erdwahlgräber (25–30 Jahre). Hinzu kommen Bestatterleistungen (1…`
- **A_TEXT[1]** — Was ist das Besondere am Melaten-Friedhof?
  - LD:   `Der Melaten (gegründet 29.6.1810) ist einer der ältesten und schönsten Friedhöfe Deutschlands und ein Kulturdenkmal. Nach Napoleons Dekret 1804 wurde er nach dem Pariser Père-Lachaise gestaltet. Hier …`
  - HTML: `Der Melaten (gegründet 29.6.1810) ist einer der ältesten und schönsten Friedhöfe Deutschlands und ein Kulturdenkmal. Nach Napoleons Dekret 1804 wurde er nach dem Pariser Père-Lachaise gestaltet. Hier …`

### krefeld  (LD=7, HTML=7)

- **A_TEXT[0]** — Wie viele Friedhöfe gibt es in Krefeld?
  - LD:   `In Krefeld werden elf städtische Friedhöfe vom Kommunalbetrieb Krefeld AöR (KBK) betrieben, mit einer Gesamtfläche von rund 130 Hektar. Der Hauptfriedhof an der Heideckstraße ist mit 54 Hektar der grö…`
  - HTML: `<div class="answer">
        <p>In Krefeld werden elf städtische Friedhöfe vom Kommunalbetrieb Krefeld AöR (KBK) betrieben: Hauptfriedhof, Uerdingen, Linn, Hüls, Bockum, Fischeln, Stratum, Traar, Verb…`
- **A_TEXT[1]** — Was kostet ein Urnenreihengrab in Krefeld?
  - LD:   `Nach der Krefelder Friedhofsgebührensatzung 2026 (6. Änderungssatzung vom 18.12.2025, Inkrafttreten 01.01.2026) kostet das Nutzungsrecht an einer Urnenreihengrabstätte inkl. Einfassung 1.680,00 €. Hin…`
  - HTML: `<div class="answer">
        <p>Nach der Krefelder Friedhofsgebührensatzung 2026 (Inkrafttreten 01.01.2026, 6. Änderungssatzung vom 18.12.2025) kostet das Nutzungsrecht an einer Urnenreihengrabstätte …`
- **A_TEXT[2]** — Wie lange ist die Ruhezeit auf Krefelder Friedhöfen?
  - LD:   `Die konkrete Ruhezeit legt die Krefelder Friedhofssatzung vom 18.12.2025 fest; das BestG NRW gibt mit § 4 die Ermächtigung zum Satzungserlass, schreibt jedoch keine landesweit einheitliche Ruhezeit nu…`
  - HTML: `<div class="answer">
        <p>Die konkrete Ruhezeit wird durch die Krefelder Friedhofssatzung vom 18.12.2025 festgelegt; das BestG NRW gibt mit § 4 die Ermächtigung zum Satzungserlass, schreibt jedo…`
- **A_TEXT[3]** — Welche Bestattungsfrist gilt in Krefeld?
  - LD:   `Nach § 13 BestG NRW dürfen Erdbestattungen frühestens 24 Stunden nach Eintritt des Todes erfolgen. Sowohl Erdbestattung als auch Einäscherung müssen innerhalb von 10 Tagen vorgenommen werden. Die Beis…`
  - HTML: `<div class="answer">
        <p>Das BestG NRW schreibt in § 13 vor: Erdbestattungen dürfen frühestens 24 Stunden nach Eintritt des Todes erfolgen. Sowohl Erdbestattungen als auch Einäscherungen müssen…`
- **A_TEXT[4]** — Gibt es in Krefeld einen Friedhofszwang?
  - LD:   `Ja. In Nordrhein-Westfalen gilt grundsätzlich Friedhofszwang — die Totenasche darf nur auf einem Friedhof beigesetzt werden. NRW erlaubt allerdings — abweichend von strengeren Bundesländern — eine Asc…`
  - HTML: `<div class="answer">
        <p>Ja, in Nordrhein-Westfalen und damit auch in Krefeld gilt grundsätzlich Friedhofszwang. Sowohl Erdbestattung als auch Urnenbeisetzung müssen auf einem öffentlichen oder…`
- **A_TEXT[5]** — Wo findet man qualifizierte Bestatter in Krefeld?
  - LD:   `Der Bestatterverband NRW e.V. unterhält einen Stadtverband Krefeld. Innungsmitglieder mit dem Markenzeichen "Bestatter — vom Handwerk geprüft" des Bundesverbands Deutscher Bestatter (Kollektivmarke, z…`
  - HTML: `<div class="answer">
        <p>Der Bestatterverband NRW e.V. mit Sitz in Düsseldorf unterhält einen Stadtverband Krefeld. Eine Bestatter-Suche nach Postleitzahl ist über bestatter-nrw.de möglich. Emp…`
- **A_TEXT[6]** — Wo wird in Krefeld der Sterbefall beurkundet?
  - LD:   `Zuständig ist das Standesamt Krefeld, Rheinstraße 138, 47798 Krefeld. Der Sterbefall muss spätestens am dritten auf den Tod folgenden Werktag gemeldet werden. Aktuelle Telefonnummern, Sprechzeiten und…`
  - HTML: `<div class="answer">
        <p>Zuständig ist das Standesamt Krefeld, Rheinstraße 138, 47798 Krefeld. Der Sterbefall muss spätestens am dritten auf den Tod folgenden Werktag gemeldet werden. Aktuelle …`

### leipzig  (LD=7, HTML=7)

- **A_TEXT[2]** — Wo ist Johann Sebastian Bach in Leipzig bestattet?
  - LD:   `Johann Sebastian Bach wurde 1750 zunächst auf dem Alten Johannisfriedhof beigesetzt. Im Oktober 1894 wurde sein vermuteter Sarg im Zuge des Kirchen-Neubaus geborgen; die feierliche Beisetzung der Gebe…`
  - HTML: `Bach wurde 1750 zunächst auf dem Alten Johannisfriedhof beigesetzt. Am 22. Oktober 1894 wurde sein vermuteter Sarg im Zuge des Kirchen-Neubaus geborgen; die feierliche Beisetzung der Gebeine in der ei…`
- **A_TEXT[3]** — Welches Bestattungsrecht gilt in Leipzig?
  - LD:   `In Leipzig gilt das Sächsische Gesetz über das Friedhofs-, Leichen- und Bestattungswesen (SächsBestG). Insbesondere § 18 SächsBestG enthält die allgemeinen Vorschriften zur Bestattung einschließlich d…`
  - HTML: `In Leipzig gilt das Sächsische Gesetz über das Friedhofs-, Leichen- und Bestattungswesen (SächsBestG). § 18 SächsBestG enthält die allgemeinen Vorschriften zur Bestattung einschließlich des Friedhofsz…`
- **A_TEXT[6]** — Wo wurde Felix Mendelssohn Bartholdy bestattet?
  - LD:   `Felix Mendelssohn Bartholdy starb 1847 in Leipzig, wurde aber auf eigenen Wunsch nach Berlin überführt und auf dem Dreifaltigkeitsfriedhof I beigesetzt. In Leipzig erinnern das Mendelssohn-Haus, das D…`
  - HTML: `Mendelssohn starb 1847 in Leipzig, wurde aber auf eigenen Wunsch nach Berlin überführt und auf dem Dreifaltigkeitsfriedhof I beigesetzt. In Leipzig erinnern das Mendelssohn-Haus, das Denkmal vor der T…`

### magdeburg  (LD=7, HTML=7)

- **A_TEXT[0]** — Welche Friedhofsgebühren fallen in Magdeburg an?
  - LD:   `Nach der Friedhofsgebührensatzung der Landeshauptstadt Magdeburg vom 18.01.2024 kostet eine Erdreihengrabstätte 1.230 € für 20 Jahre, eine Urnenreihengrabstätte 1.053 €. Hinzu kommen Bestattungs- und …`
  - HTML: `<div class="mr-faq-answer">Nach der seit 1. Februar 2024 geltenden Friedhofsgebührensatzung kostet eine Erdreihengrabstätte für 20 Jahre 1.230 €, eine Urnenreihengrabstätte 1.053 €. Hinzu kommen Besta…`
- **A_TEXT[1]** — Wie viele kommunale Friedhöfe gibt es in Magdeburg?
  - LD:   `Der Eigenbetrieb Stadtgarten und Friedhöfe Magdeburg bewirtschaftet 16 kommunale Friedhöfe im Stadtgebiet. Der größte ist mit rund 62,5 Hektar der Westfriedhof, gefolgt vom Südfriedhof mit 18 Hektar u…`
  - HTML: `<div class="mr-faq-answer">Der Eigenbetrieb Stadtgarten und Friedhöfe Magdeburg bewirtschaftet 16 kommunale Friedhöfe. Der größte ist mit rund 62,5 ha der Westfriedhof, gefolgt vom Südfriedhof (18 ha)…`
- **A_TEXT[2]** — Wie lange ist die Ruhezeit in Magdeburg?
  - LD:   `Die Friedhofsgebührensatzung der Landeshauptstadt Magdeburg setzt die Nutzungsdauer der Grabstätten regelmäßig auf 20 Jahre fest. Das BestattG LSA schreibt eine Mindestruhezeit von 15 Jahren vor (10 J…`
  - HTML: `<div class="mr-faq-answer">Die Magdeburger Gebührensatzung legt die Nutzungsdauer für Grabstätten regelmäßig auf 20 Jahre fest und liegt damit über der landesgesetzlichen Mindestruhezeit nach BestattG…`
- **Q_TEXT[4]**
  - LD:   `Wo wird der Sterbefall in Magdeburg beurkundet?`
  - HTML: `Gibt es in Magdeburg Naturbestattungen?`
- **A_TEXT[4]** — Wo wird der Sterbefall in Magdeburg beurkundet?
  - LD:   `Zuständig ist das Standesamt Magdeburg, Humboldtstraße 11, 39112 Magdeburg. Die Sterbeurkunde wird vom registerführenden Standesamt ausgestellt.…`
  - HTML: `<div class="mr-faq-answer">Auf dem Südfriedhof gibt es seit 2015 ein Naturgrabfeld, das den Trend zur Waldbestattung in den städtischen Raum überträgt. Die Gebühr beträgt 3.027 € für 20 Jahre inklusiv…`
- **Q_TEXT[5]**
  - LD:   `Gilt in Sachsen-Anhalt eine Sargpflicht?`
  - HTML: `Wo wird der Sterbefall in Magdeburg beurkundet?`
- **A_TEXT[5]** — Gilt in Sachsen-Anhalt eine Sargpflicht?
  - LD:   `Ja. Sachsen-Anhalt ist eines der wenigen Bundesländer, in denen weiterhin eine durchgängige Sargpflicht besteht. Eine Ausnahme von der Sargpflicht – etwa für muslimische Bestattungen im Leichentuch – …`
  - HTML: `<div class="mr-faq-answer">Beim Standesamt Magdeburg, Humboldtstraße 11, 39112 Magdeburg. Telefon Sterberegister: 0391 540 4216, E-Mail: sterbe@std.magdeburg.de. Die Sterbeurkunde kostet nach aktuelle…`
- **Q_TEXT[6]**
  - LD:   `Gibt es in Magdeburg Naturbestattungen?`
  - HTML: `Gilt in Sachsen-Anhalt eine Sargpflicht?`
- **A_TEXT[6]** — Gibt es in Magdeburg Naturbestattungen?
  - LD:   `Auf dem Südfriedhof existiert seit 2015 ein Naturgrabfeld. Die Gebühr beträgt nach der Satzung 3.027 € für 20 Jahre einschließlich Anlagenunterhaltung. Eine klassische Waldbestattung außerhalb von Fri…`
  - HTML: `<div class="mr-faq-answer">Ja, durchgängig. Sachsen-Anhalt gehört zu den wenigen Bundesländern, in denen das Bestattungsgesetz keine Ausnahme von der Sargpflicht – etwa für muslimische Bestattungen im…`

### mainz  (LD=7, HTML=7)

- **A_TEXT[5]** — Welche Friedhofsverwaltung ist zuständig?
  - LD:   `Träger aller kommunalen Friedhöfe in Mainz ist der Wirtschaftsbetrieb Mainz - Anstalt des öffentlichen Rechts (WBM), Industriestraße 70, 55120 Mainz, Telefon 06131-9715-0. Der WBM verwaltet die Friedh…`
  - HTML: `Träger aller kommunalen Friedhöfe in Mainz ist der Wirtschaftsbetrieb Mainz - Anstalt des öffentlichen Rechts (WBM), Industriestraße 70, 55120 Mainz, Telefon 06131-9715-0. Der WBM verwaltet die Friedh…`
- **A_TEXT[6]** — Ist eine Patenschaft für historische Gräber in Mainz möglich?
  - LD:   `Ja. Der WBM bietet auf dem Hauptfriedhof Patenschaften für denkmalgeschützte Grabstätten an. 19 Gräber tragen seit dem Projektstart ein grünes Patenschaftsschild. Paten verpflichten sich zur Pflege un…`
  - HTML: `Ja. Der WBM bietet auf dem Hauptfriedhof Patenschaften für denkmalgeschützte Grabstätten an. 19 Gräber tragen seit dem Projektstart ein grünes Hinweisschild. Paten verpflichten sich zur Pflege und Erh…`

### muelheim  (LD=7, HTML=7)

- **Q_TEXT[0]**
  - LD:   `Wie viele städtische Friedhöfe gibt es in Mülheim an der Ruhr?`
  - HTML: `Wie viele städtische Friedhöfe gibt es in Mülheim?`
- **A_TEXT[0]** — Wie viele städtische Friedhöfe gibt es in Mülheim an der Ruhr?
  - LD:   `Die Stadt Mülheim an der Ruhr verwaltet zehn städtische Friedhöfe. Auf acht davon finden reguläre Beisetzungen statt. Der Altstadtfriedhof ist seit 1967 für reguläre Bestattungen geschlossen, lässt ab…`
  - HTML: `<p>Die Stadt verwaltet zehn städtische Friedhöfe. Auf acht davon finden Beisetzungen statt: sieben für reguläre Bestattungen (Hauptfriedhof, Broich, Dümpten I (Schildberg), Dümpten II (Oberheidstraße)…`
- **Q_TEXT[1]**
  - LD:   `Kann man auf den Mülheimer Friedhöfen pflegefreie Gräber wählen?`
  - HTML: `Welche Bestattungsfristen gelten in Mülheim?`
- **A_TEXT[1]** — Kann man auf den Mülheimer Friedhöfen pflegefreie Gräber wählen?
  - LD:   `Ja, auf mehreren Friedhöfen – darunter Broich, Speldorf und Hauptfriedhof – werden pflegefreie Urnengemeinschaftsanlagen und Hainbestattungen angeboten. Bei diesen Grabarten ist eine einmalige Pauscha…`
  - HTML: `<p>Es gilt das Bestattungsgesetz NRW. Nach § 13 Abs. 2 BestG NRW dürfen Erdbestattungen frühestens 24 Stunden nach Eintritt des Todes vorgenommen werden, nach § 13 Abs. 3 müssen sie innerhalb von zehn…`
- **Q_TEXT[2]**
  - LD:   `Welche Bestattungsfristen gelten in Mülheim an der Ruhr?`
  - HTML: `Wo wird der Sterbefall in Mülheim angezeigt?`
- **A_TEXT[2]** — Welche Bestattungsfristen gelten in Mülheim an der Ruhr?
  - LD:   `Es gilt das Bestattungsgesetz Nordrhein-Westfalen (BestG NRW). Erdbestattungen dürfen nach § 13 Abs. 2 frühestens 24 Stunden nach Eintritt des Todes vorgenommen werden und müssen nach § 13 Abs. 3 inne…`
  - HTML: `<p>Beim Standesamt Mülheim an der Ruhr spätestens am dritten auf den Tod folgenden Werktag (§ 28 PStG). Adresse: Am Rathaus 1, 45468 Mülheim, postalisch Postfach 10 19 53, 45419 Mülheim, Telefon 0208 …`
- **Q_TEXT[3]**
  - LD:   `Wo wird der Sterbefall in Mülheim angezeigt?`
  - HTML: `Was kostet ein Grab in Mülheim an der Ruhr?`
- **A_TEXT[3]** — Wo wird der Sterbefall in Mülheim angezeigt?
  - LD:   `Die Anzeige erfolgt beim Standesamt Mülheim an der Ruhr spätestens am dritten auf den Tod folgenden Werktag (§ 28 PStG). In der Praxis übernimmt das beauftragte Bestattungsunternehmen die Formalitäten…`
  - HTML: `<p>Die Friedhofsgebühren richten sich nach der Gebührensatzung der Stadt vom 20. Dezember 2022. Eine Auswertung des Bundes der Steuerzahler NRW vom Oktober 2024 ordnet Mülheim den NRW-Städten mit Gesa…`
- **Q_TEXT[4]**
  - LD:   `Was kostet ein Grab in Mülheim an der Ruhr?`
  - HTML: `Kann man auf den Mülheimer Friedhöfen pflegefreie Gräber wählen?`
- **A_TEXT[4]** — Was kostet ein Grab in Mülheim an der Ruhr?
  - LD:   `Mülheim gehört nach Auswertung des Bundes der Steuerzahler NRW (2024) zu den Städten mit Gesamtgebühren von über 4.000 Euro für ein Sargwahlgrab. Die genauen Einzelbeträge richten sich nach der Gebühr…`
  - HTML: `<p>Ja, auf mehreren Friedhöfen – darunter Broich, Speldorf und Hauptfriedhof – werden pflegefreie Urnengemeinschaftsanlagen und Hainbestattungen angeboten. Bei diesen Grabarten ist eine einmalige Paus…`
- **Q_TEXT[5]**
  - LD:   `Kann man die Asche eines Verstorbenen in Mülheim außerhalb eines Friedhofs verstreuen?`
  - HTML: `Welche Religionsgemeinschaften haben in Mülheim eigene Bestattungsmöglichkeiten?`
- **A_TEXT[5]** — Kann man die Asche eines Verstorbenen in Mülheim außerhalb eines Friedhofs verstreuen?
  - LD:   `Nach § 14 und § 15 BestG NRW ist die Verstreuung der Totenasche auf eigens dafür ausgewiesenen Flächen zulässig. Auf den Mülheimer Friedhöfen werden hierfür anonyme Urnengemeinschaftsfelder angeboten.…`
  - HTML: `<p>Neben den städtischen Friedhöfen gibt es konfessionelle Begräbnisstätten der katholischen, evangelischen und jüdischen Gemeinden. Auf dem Hauptfriedhof besteht seit dem 13. Juni 1996 ein etwa 1.000…`
- **Q_TEXT[6]**
  - LD:   `Welche Religionsgemeinschaften haben in Mülheim eigene Bestattungsmöglichkeiten?`
  - HTML: `Kann man die Asche eines Verstorbenen in Mülheim außerhalb eines Friedhofs verstreuen?`
- **A_TEXT[6]** — Welche Religionsgemeinschaften haben in Mülheim eigene Bestattungsmöglichkeiten?
  - LD:   `Neben den städtischen Friedhöfen gibt es konfessionelle Begräbnisstätten der katholischen, evangelischen und jüdischen Gemeinden. Auf dem Hauptfriedhof besteht seit dem 13. Juni 1996 ein etwa 1.000 Qu…`
  - HTML: `<p>Nach § 14 und § 15 BestG NRW ist die Verstreuung der Asche grundsätzlich an dafür ausgewiesenen Orten zulässig. In Mülheim werden diese Möglichkeiten in anonymen Urnengemeinschaftsanlagen umgesetzt…`

### oberhausen  (LD=7, HTML=7)

- **A_TEXT[0]** — Welche Friedhöfe gehören zur Stadt Oberhausen?
  - LD:   `Die Stadt Oberhausen verwaltet fünf städtische Friedhöfe: Westfriedhof (Lirich), Nordfriedhof (Königshardt), Ostfriedhof (Osterfeld), Landwehrfriedhof (Styrum) und Alstadener Friedhof. Die Gesamtfläch…`
  - HTML: `<div>
      <p>Die Stadt Oberhausen verwaltet fünf städtische Friedhöfe: Westfriedhof (Lirich), Nordfriedhof (Königshardt), Ostfriedhof (Osterfeld), Landwehrfriedhof (Styrum) und Alstadener Friedhof. …`
- **A_TEXT[1]** — Was kostet eine Bestattung auf einem Oberhausener Friedhof?
  - LD:   `Die Friedhofsgebühren sind in der Friedhofsgebührensatzung der Stadt Oberhausen vom 31.03.2026 (Amtsblatt Nr. 6/2026) festgelegt; aktuelle Tarifstellen sind auf der SBO-Seite abrufbar. Die Gesamtkoste…`
  - HTML: `<div>
      <p>Die Friedhofsgebühren sind in der Friedhofsgebührensatzung der Stadt Oberhausen vom 31.03.2026 (Amtsblatt Nr. 6/2026) festgelegt. Die rechtsverbindlichen Tarifstellen sind auf der Seite…`
- **A_TEXT[2]** — Wie lang ist die Ruhezeit in Oberhausen?
  - LD:   `Die Ruhezeiten sind in § 11 der Friedhofssatzung der Stadt Oberhausen geregelt (aktuelle Fassung vom 31.03.2026). Nach der Vorgängerfassung galten im Regelfall 25 Jahre (Verstorbene bis 5 Jahre) und 3…`
  - HTML: `<div>
      <p>Die Ruhezeiten sind in § 11 der Friedhofssatzung der Stadt Oberhausen geregelt (aktuelle Fassung vom 31.03.2026; die Systematik ist gegenüber der Vorgängerfassung 18.12.2024 weitgehend …`
- **A_TEXT[3]** — Gibt es in Oberhausen anonyme Bestattungen?
  - LD:   `Ja, anonyme Urnenbeisetzungen werden ausschließlich auf dem Westfriedhof und dem Nordfriedhof angeboten. Die Beisetzung erfolgt unter Ausschluss der Öffentlichkeit; die Grabstelle wird nicht namentlic…`
  - HTML: `<div>
      <p>Ja. Anonyme Urnenbeisetzungen werden in Oberhausen ausschließlich auf dem Westfriedhof (Lirich) und dem Nordfriedhof (Königshardt) angeboten. Die Trauerfeier kann in der Friedhofskapell…`
- **A_TEXT[4]** — Wie lange dauert es nach dem Tod, bis die Bestattung stattfinden muss?
  - LD:   `Nach § 13 Abs. 2 BestG NRW darf eine Erdbestattung frühestens 24 Stunden nach Eintritt des Todes erfolgen. Erdbestattungen und Einäscherungen müssen innerhalb von zehn Tagen durchgeführt sein (§ 13 Ab…`
  - HTML: `<div>
      <p>Nach § 13 Abs. 2 BestG NRW darf eine Erdbestattung frühestens 24 Stunden nach Eintritt des Todes erfolgen. Erdbestattungen und Einäscherungen müssen innerhalb von zehn Tagen durchgeführ…`
- **A_TEXT[5]** — Wo wird der Sterbefall in Oberhausen beurkundet?
  - LD:   `Beim Standesamt Oberhausen im Technischen Rathaus, Bahnhofstraße 66, 46145 Oberhausen (Gebäude C, 3. Etage). Kontakt: sterbefaelle@oberhausen.de, Tel. 0208 825-2612 / -2569 / -2692. Eine Sterbeurkunde…`
  - HTML: `<div>
      <p>Beim Standesamt Oberhausen im Technischen Rathaus, Bahnhofstraße 66, 46145 Oberhausen (Gebäude C, 3. Etage), E-Mail sterbefaelle@oberhausen.de, Telefon 0208 825-2612, -2569 oder -2692. …`
- **A_TEXT[6]** — Gibt es ein muslimisches oder griechisch-orthodoxes Grabfeld in Oberhausen?
  - LD:   `Ja, auf den städtischen Friedhöfen Oberhausens sind ein muslimisches und ein griechisch-orthodoxes Grabfeld eingerichtet (das griechisch-orthodoxe laut SBO auf dem Westfriedhof). Welcher Friedhof welc…`
  - HTML: `<div>
      <p>Ja. Auf den städtischen Friedhöfen Oberhausens sind ein muslimisches und ein griechisch-orthodoxes Grabfeld eingerichtet (das griechisch-orthodoxe Grabfeld ist laut SBO auf dem Westfrie…`

### oldenburg  (LD=7, HTML=7)

- **A_TEXT[1]** — Was kostet ein Grab in Oldenburg?
  - LD:   `Auf den städtischen Friedhöfen kostet eine Urnenreihengrabstelle 590 €, ein Urnenwahlgrab 767 €, ein Erdwahlgrab 1.070 € je Stelle. Hinzu kommt jeweils eine Beisetzungsgebühr (Urne 199 €, Erdbestattun…`
  - HTML: `<p>Auf den städtischen Friedhöfen kostet eine Urnenreihengrabstelle 590&nbsp;€, ein Urnenwahlgrab 767&nbsp;€, ein Erdwahlgrab 1.070&nbsp;€ je Stelle. Hinzu kommt jeweils eine Beisetzungsgebühr (Urne 1…`
- **A_TEXT[4]** — Wer muss in Oldenburg die Bestattung organisieren?
  - LD:   `Die Bestattungspflicht regelt § 8 Abs. 3 des Niedersächsischen Bestattungsgesetzes (BestattG). Die nummerierte Rangfolge lautet: 1. Ehegattin/Ehegatte oder eingetragene Lebenspartnerin/Lebenspartner, …`
  - HTML: `<p>Die Bestattungspflicht regelt § 8 Abs. 3 des Niedersächsischen Bestattungsgesetzes (BestattG). Die nummerierte Rangfolge lautet: 1. Ehegattin oder Ehegatte oder eingetragene Lebenspartnerin/Lebensp…`

### osnabrueck  (LD=7, HTML=7)

- **A_TEXT[0]** — Wie viele Friedhöfe gibt es in Osnabrück?
  - LD:   `Die Stadt Osnabrück unterhält zehn aktive kommunale Friedhöfe: Heger Friedhof, Atter Friedhof, Friedhof Eversburg, Friedhof Hellern, Lüstringer Friedhof, Nahner Friedhof, Pyer Friedhof, Friedhof Schin…`
  - HTML: `<p>Die Stadt Osnabrück unterhält zehn aktive kommunale Friedhöfe: Heger Friedhof, Atter Friedhof, Friedhof Eversburg, Friedhof Hellern, Lüstringer Friedhof, Nahner Friedhof, Pyer Friedhof, Friedhof Sc…`
- **A_TEXT[1]** — Welcher Friedhof in Osnabrück hat ein Krematorium?
  - LD:   `Das einzige Krematorium der Stadt befindet sich auf dem Heger Friedhof an der Rheiner Landstraße 170. Es wurde 1936/1937 errichtet, 1993 durch einen Neubau ersetzt und 2023 um moderne Räumlichkeiten e…`
  - HTML: `<p>Das einzige Krematorium der Stadt befindet sich auf dem Heger Friedhof an der Rheiner Landstraße 170. Die ursprüngliche Anlage wurde 1936/1937 errichtet, 1993 durch ein neues Krematorium mit modern…`
- **A_TEXT[2]** — Wie lange ist die Ruhezeit in Osnabrück?
  - LD:   `Die konkrete Ruhezeit ergibt sich aus der Friedhofssatzung der Stadt Osnabrück. Üblich sind 20 bis 25 Jahre für Erd- und Urnenbestattungen. Maßgeblich ist die jeweils aktuelle Friedhofssatzung; das Ni…`
  - HTML: `<p>Die konkrete Ruhezeit ergibt sich aus der Friedhofssatzung der Stadt Osnabrück. Üblich sind 20 bis 25 Jahre für Erd- und Urnenbestattungen. Maßgeblich ist die jeweils aktuelle Friedhofssatzung; das…`
- **A_TEXT[3]** — Was kostet eine Bestattung in Osnabrück?
  - LD:   `Die Gesamtkosten in Osnabrück bewegen sich für eine einfache Feuerbestattung in der Größenordnung von rund 3.500 bis 6.000 Euro, für eine klassische Erdbestattung mit Trauerfeier bei 6.000 bis 12.000 …`
  - HTML: `<p>Die Gesamtkosten bewegen sich für eine einfache Feuerbestattung in der Größenordnung von rund 3.500 bis 6.000 Euro, für eine klassische Erdbestattung mit Trauerfeier bei 6.000 bis 12.000 Euro. Dies…`
- **A_TEXT[4]** — Wo wird in Osnabrück der Sterbefall angezeigt?
  - LD:   `Zuständig ist das Standesamt Osnabrück am Natruper-Tor-Wall 2, 49076 Osnabrück. Die Anzeige erfolgt spätestens am dritten auf den Tod folgenden Werktag. Bei Sterbefällen in Krankenhaus oder Pflegeeinr…`
  - HTML: `<p>Zuständig ist das Standesamt Osnabrück am Natruper-Tor-Wall 2, 49076 Osnabrück, Telefon 0541 323-0, E-Mail standesamt@osnabrueck.de. Die Anzeige erfolgt spätestens am dritten auf den Tod folgenden …`
- **A_TEXT[5]** — Gibt es in Osnabrück eine anonyme Bestattung?
  - LD:   `Ja, ausschließlich auf dem Heger Friedhof. Dort werden anonyme Urnenbeisetzungen auf einem gemeinschaftlichen Feld ohne Namenskennzeichnung angeboten. Auf den übrigen neun kommunalen Friedhöfen ist di…`
  - HTML: `<p>Ja, ausschließlich auf dem Heger Friedhof. Dort werden anonyme Urnenbeisetzungen auf einem gemeinschaftlichen Feld ohne Namenskennzeichnung angeboten. Diese Bestattungsform richtet sich an Menschen…`
- **A_TEXT[6]** — Ist eine Reerdigung in Osnabrück möglich?
  - LD:   `Nein. Die Reerdigung – die Umwandlung des Körpers in Erde mithilfe pflanzlicher Substrate – ist in Niedersachsen nach aktuellem Stand (Mai 2026) gesetzlich nicht zugelassen. Eine Rechtsgrundlage beste…`
  - HTML: `<p>Nein. Die Reerdigung – die Umwandlung des Körpers in Erde mithilfe pflanzlicher Substrate innerhalb von rund 40 Tagen – ist in Niedersachsen nach aktuellem Stand (Mai 2026) gesetzlich nicht zugelas…`

### potsdam  (LD=8, HTML=8)

- **A_TEXT[1]** — Welcher Friedhof in Potsdam ist UNESCO-Welterbe?
  - LD:   `Sowohl der Bornstedter Friedhof als auch der Jüdische Friedhof am Pfingstberg gehören als Teil der Berlin-Potsdamer Parklandschaft seit 1999 zum UNESCO-Welterbe. Beide stehen unter Denkmalschutz.…`
  - HTML: `<div><p>Sowohl der Bornstedter Friedhof als auch der Jüdische Friedhof am Pfingstberg gehören als Teil der Berlin-Potsdamer Parklandschaft seit 1999 zum UNESCO-Welterbe. Beide stehen unter Denkmalschu…`
- **A_TEXT[2]** — Wie lange ist die Ruhezeit in Potsdam?
  - LD:   `Nach § 32 Abs. 1 Brandenburgisches Bestattungsgesetz beträgt die Mindestruhezeit 20 Jahre für Leichen und 15 Jahre für Aschen. Die Stadt Potsdam setzt im Erdreihengrab 25 Jahre und im Urnenreihengrab …`
  - HTML: `<div><p>Nach § 32 Abs. 1 Brandenburgisches Bestattungsgesetz beträgt die Mindestruhezeit 20 Jahre für Leichen und 15 Jahre für Aschen. Die Landeshauptstadt Potsdam setzt im Erdreihengrab eine Ruhezeit…`
- **A_TEXT[3]** — Was kostet ein Urnengrab in Potsdam?
  - LD:   `Auf den kommunalen Friedhöfen kostet ein Urnenreihengrab für 20 Jahre 969 Euro, ein Urnengrab in der Urnengemeinschaftsanlage ebenfalls für 20 Jahre 918 Euro. Eine Urnenwahlgrabstelle wird mit 49 Euro…`
  - HTML: `<div><p>Auf den kommunalen Friedhöfen kostet ein Urnenreihengrab für 20 Jahre 969 Euro, ein Urnengrab in der Urnengemeinschaftsanlage ebenfalls für 20 Jahre 918 Euro. Eine Urnenwahlgrabstelle wird mit…`
- **A_TEXT[5]** — Wo wird der Sterbefall in Potsdam angezeigt?
  - LD:   `Beim Standesamt Potsdam in der Friedrich-Ebert-Straße 79–81, 14469 Potsdam (Tel. 0331 289-0). Die Anzeige sollte innerhalb von drei Werktagen erfolgen.…`
  - HTML: `<div><p>Beim Standesamt Potsdam in der Friedrich-Ebert-Straße 79–81, 14469 Potsdam (Tel. 0331 289-0). Die Anzeige sollte innerhalb von drei Werktagen erfolgen. Die ausgestellte Sterbeurkunde wird für …`
- **A_TEXT[6]** — Welche Bestattungsfristen gelten in Brandenburg?
  - LD:   `Nach § 22 Abs. 1 BbgBestG ist eine Bestattung frühestens 48 Stunden nach Eintritt des Todes zulässig. Nach § 19 Abs. 3 BbgBestG muss die Erd- oder Feuerbestattung spätestens innerhalb von zehn Tagen n…`
  - HTML: `<div><p>Brandenburg kennt zwei Fristen: Nach § 22 Abs. 1 BbgBestG ist eine Bestattung frühestens 48 Stunden nach Eintritt des Todes zulässig. Nach § 19 Abs. 3 BbgBestG muss die Erd- oder Feuerbestattu…`
- **A_TEXT[7]** — Gibt es in Potsdam Baum- oder Waldbestattungen?
  - LD:   `Auf den kommunalen Friedhöfen sind Baumgrabstätten für Urnen verfügbar. Klassische FriedWald- oder RuheForst-Anlagen außerhalb von Friedhöfen liegen im Umland, etwa der FriedWald Nuthetal-Parforceheid…`
  - HTML: `<div><p>Auf den kommunalen Friedhöfen sind Baumgrabstätten für Urnen verfügbar. Klassische FriedWald- oder RuheForst-Anlagen außerhalb von Friedhöfen liegen im Umland; auf Potsdamer Stadtgebiet existi…`

### regensburg  (LD=7, HTML=7)

- **A_TEXT[0]** — Wie viele städtische Friedhöfe gibt es in Regensburg?
  - LD:   `Die Stadt Regensburg betreibt elf städtische Friedhöfe: Am Dreifaltigkeitsberg (mit Krematorium), Burgweinting, Harting, Keilberg, Oberisling, Reinhausen, Sallern, Schwabelweis, Stadtamhof, Steinweg u…`
  - HTML: `<div class="answer">Die Stadt Regensburg betreibt elf städtische Friedhöfe: Am Dreifaltigkeitsberg (mit Krematorium), Burgweinting, Harting, Keilberg, Oberisling, Reinhausen, Sallern, Schwabelweis, St…`
- **A_TEXT[1]** — Was kostet eine Bestattung in Regensburg?
  - LD:   `Auf städtischen Friedhöfen liegen die reinen kommunalen Gebühren laut Bestattungsgebührensatzung der Stadt Regensburg (BGS, Anlage vom 12.12.2024) für eine Urnenbeisetzung im Erdgrab bei 318 € zuzügli…`
  - HTML: `<div class="answer">Auf städtischen Friedhöfen liegen die kommunalen Gebühren laut Bestattungsgebührensatzung (BGS, Anlage 12.12.2024) für eine Urnenbeisetzung im Erdgrab bei 318 € zuzüglich Grabnutzu…`
- **A_TEXT[2]** — Wo muss ein Sterbefall in Regensburg angezeigt werden?
  - LD:   `Der Sterbefall wird beim Standesamt Regensburg im Bürger- und Verwaltungszentrum, D.-Martin-Luther-Straße 3, 93047 Regensburg, beurkundet. Telefon (0941) 507-1346 für den Bereich Sterbefall. Die Anzei…`
  - HTML: `<div class="answer">Der Sterbefall wird beim Standesamt Regensburg im Bürger- und Verwaltungszentrum, D.-Martin-Luther-Straße 3, 93047 Regensburg, beurkundet. Telefon (0941) 507-1346 für den Bereich S…`
- **A_TEXT[3]** — Gilt in Regensburg die Sargpflicht?
  - LD:   `Ja. Nach Bayerischem Bestattungsgesetz (BestG) und der Bayerischen Bestattungsverordnung (BestV) gilt die Sargpflicht. Seit Oktober 2019 ist die Beisetzung im Leichentuch unter bestimmten religiösen V…`
  - HTML: `<div class="answer">Ja. Nach Bayerischem Bestattungsgesetz (BestG) und Bayerischer Bestattungsverordnung (BestV) besteht Sargpflicht. Seit Oktober 2019 ist die Beisetzung im Leichentuch unter bestimmt…`
- **A_TEXT[4]** — Welche Friedhöfe in Regensburg sind besonders sehenswert?
  - LD:   `Der Gesandtenfriedhof an der Dreieinigkeitskirche – seit dem Stadtratsbeschluss vom 16. Mai 2024 das 7. document der Stadt Regensburg und einziges erhaltenes Diplomatenfriedhof-Ensemble im ehemaligen …`
  - HTML: `<div class="answer">Der Gesandtenfriedhof an der Dreieinigkeitskirche – seit dem Stadtratsbeschluss vom 16. Mai 2024 das 7. „document" der Stadt Regensburg (lokales Programm der Stadt für authentische…`
- **A_TEXT[5]** — Wie wähle ich einen Bestatter in Regensburg?
  - LD:   `Angehörige sollten mindestens zwei Kostenvoranschläge einholen. Zertifizierungen sind ein Qualitätsindikator: Mitgliedschaft im Bundesverband Deutscher Bestatter (BDB) oder Markenzeichen RAL-GZ 749. D…`
  - HTML: `<div class="answer">Angehörige sollten mindestens zwei Kostenvoranschläge einholen. Zertifizierungen sind ein Qualitätsindikator: Mitgliedschaft im Bundesverband Deutscher Bestatter (BDB) oder das RAL…`
- **A_TEXT[6]** — Wie lange ist die Ruhezeit in Regensburg?
  - LD:   `Nach § 15 der Bestattungssatzung der Stadt Regensburg vom 04.12.2006 beträgt die Ruhezeit auf allen elf städtischen Friedhöfen einheitlich: 15 Jahre für Leichen (Sargbestattungen), 12 Jahre für Ascher…`
  - HTML: `<div class="answer">Nach § 15 der Bestattungssatzung der Stadt Regensburg vom 04.12.2006 beträgt die Ruhezeit auf allen elf städtischen Friedhöfen einheitlich: <strong>15 Jahre für Leichen</strong> (S…`

### rostock  (LD=6, HTML=7)

- **COUNT-Mismatch:** JSON-LD hat 6 Q/A, HTML hat 7
- **A_TEXT[1]** — Was kostet ein Grab in Rostock?
  - LD:   `Nach der Friedhofsgebührensatzung der Hansestadt Rostock kostet das Nutzungsrecht für eine Erdwahlgrabstätte (20 Jahre) 940 Euro, eine Urnenwahlgrabstätte bis zwei Urnen 455 Euro und eine Urnenstelle …`
  - HTML: `<div><p>Nach der Friedhofsgebührensatzung der Hansestadt Rostock kostet das Nutzungsrecht für eine Erdwahlgrabstätte (20 Jahre) 940 Euro, eine Urnenwahlgrabstätte bis zwei Urnen 455 Euro und eine Urne…`
- **A_TEXT[2]** — Wie lange ist die Ruhefrist in Mecklenburg-Vorpommern?
  - LD:   `Nach § 15 BestattG M-V beträgt die gesetzliche Mindestruhefrist 20 Jahre für Erd- und Urnenbestattungen. Eine Verkürzung ist nur aus wichtigem Grund möglich.…`
  - HTML: `<div><p>Nach § 15 BestattG M-V beträgt die gesetzliche Mindestruhefrist 20 Jahre – sowohl für Erd- als auch für Urnenbestattungen. Eine Verkürzung ist nur aus wichtigem Grund möglich; der Friedhofsträ…`
- **A_TEXT[3]** — Wo wird ein Sterbefall in Rostock angezeigt?
  - LD:   `Sterbefälle werden beim Standesamt Rostock, Hinter dem Rathaus 5, 18055 Rostock angezeigt. Nach § 28 Personenstandsgesetz (PStG) muss die Anzeige spätestens am dritten auf den Tod folgenden Werktag er…`
  - HTML: `<div><p>Zuständig ist das Standesamt Rostock, Hinter dem Rathaus 5, 18055 Rostock (Tel. Sterbefall 0381 381-1476). Nach § 28 PStG muss die Anzeige spätestens am dritten auf den Tod folgenden Werktag e…`
- **A_TEXT[4]** — Gilt in Mecklenburg-Vorpommern Sargpflicht?
  - LD:   `§ 10 BestattG M-V regelt seit der Novelle 2021, dass eine Erdbestattung ohne Sarg erfolgen kann, wenn dies dem Willen des Verstorbenen entspricht. MV war hier Vorreiter: Religiöse Gründe müssen nicht …`
  - HTML: `<div><p>§ 10 BestattG M-V regelt seit der Novelle 2021, dass eine Erdbestattung ohne Sarg erfolgen kann, wenn dies dem Willen des Verstorbenen entspricht. MV war hier Vorreiter: Religiöse Gründe müsse…`
- **A_TEXT[5]** — Welche Bestattungsarten gibt es auf den Rostocker Friedhöfen?
  - LD:   `Die kommunalen Friedhöfe bieten Reihen- und Wahlgrabstätten für Erd- und Urnenbestattungen, Urnengemeinschaftsanlagen (anonym oder mit Namensplatte), Urnenstelen, das Kolumbarium auf dem Neuen Friedho…`
  - HTML: `<div><p>Die kommunalen Friedhöfe bieten Reihen- und Wahlgrabstätten für Erd- und Urnenbestattungen, Urnengemeinschaftsanlagen (anonym oder mit Namensplatte), Urnenstelen, das Kolumbarium auf dem Neuen…`

### saarbruecken  (LD=9, HTML=9)

- **A_TEXT[0]** — Welche Friedhöfe gibt es in Saarbrücken?
  - LD:   `Die Landeshauptstadt Saarbrücken betreibt 24 städtische Friedhöfe in den Stadtteilen. Der Hauptfriedhof (Südfriedhof) ist mit rund 61 Hektar der größte. Weitere bedeutende Anlagen sind der Waldfriedho…`
  - HTML: `<p>Das Amt für Stadtgrün und Friedhöfe der Landeshauptstadt betreibt 24 städtische Friedhöfe in den verschiedenen Stadtteilen. Der Hauptfriedhof (Südfriedhof) ist mit rund 61 Hektar der größte und nac…`
- **A_TEXT[1]** — Wie hoch sind die Friedhofsgebühren in Saarbrücken?
  - LD:   `Die Gebühren richten sich nach der Friedhofsgebührensatzung der Landeshauptstadt Saarbrücken (37. Änderungssatzung, gültig seit 1. April 2021). Nach einer von der saarländischen Bestatterinnung zitier…`
  - HTML: `<p>Die Gebühren richten sich nach der Friedhofsgebührensatzung der Landeshauptstadt Saarbrücken (37. Änderungssatzung, gültig seit 1. April 2021). Nach der Aeternitas-Auswertung 2025 liegen die Saarbr…`
- **A_TEXT[2]** — Welche Ruhezeit gilt im Saarland?
  - LD:   `Nach § 5 BestattG Saarland beträgt die Mindestruhezeit für Erwachsene 15 Jahre. Für Kinder unter 10 Jahren gelten 10 Jahre, für Kinder unter 2 Jahren 6 Jahre. Die Ruhezeit für Asche ist ebenfalls mind…`
  - HTML: `<p>Nach § 5 BestattG Saarland beträgt die Mindestruhezeit für Erwachsene 15 Jahre. Für Kinder, die vor Vollendung des zehnten Lebensjahres verstorben sind, gilt eine Mindestruhezeit von 10 Jahren, für…`
- **A_TEXT[3]** — Besteht in Saarbrücken eine Sargpflicht?
  - LD:   `Ja. Nach § 31 BestattG Saarland gilt für Erdbestattungen grundsätzliche Sargpflicht. Friedhofssatzungen können Ausnahmen für Verstorbene zulassen, deren religiöse Glaubensüberzeugung eine Sargbestattu…`
  - HTML: `<p>Ja. § 31 BestattG Saarland schreibt für Erdbestattungen die Sargpflicht vor. Die Friedhofsträger können in ihren Satzungen Ausnahmen für Verstorbene aufnehmen, deren religiöse Glaubensüberzeugung e…`
- **A_TEXT[5]** — Wie lange dauert es bis zur Bestattung und welche Fristen gelten?
  - LD:   `Nach § 29 BestattG Saarland darf eine Bestattung frühestens 48 Stunden nach Eintritt des Todes erfolgen. Erdbestattungen müssen spätestens zehn Tage nach dem Tod vorgenommen sein. Die Überführung des …`
  - HTML: `<p>Nach § 29 BestattG Saarland darf eine Bestattung frühestens 48 Stunden nach Eintritt des Todes erfolgen. Eine Erdbestattung muss spätestens zehn Tage nach dem Tod vollzogen sein. Die Überführung de…`
- **A_TEXT[6]** — Welche Bestattungsformen sind in Saarbrücken möglich?
  - LD:   `Auf den Saarbrücker Friedhöfen sind Erdbestattung im Reihen-, Wahl- oder Rasengrab, Urnenbeisetzung in zahlreichen Varianten (Reihen-, Wahl-, Baum-, Rabatten-, Gemeinschafts- und Pyramidengrab) sowie …`
  - HTML: `<p>Auf den städtischen Friedhöfen Saarbrückens sind Erdbestattungen im Reihen-, Wahl- oder Rasengrab, Urnenbeisetzungen in Reihen-, Wahl-, Baum-, Rabatten-, Urnenwand-, Pyramiden- oder Gemeinschaftsgr…`
- **A_TEXT[7]** — Welche Sonderregeln gelten für Bestattungsvorsorge im Saarland?
  - LD:   `Die saarländische Bestatterinnung (Fachinnung Holz und Kunststoff Saar) bietet ein Treuhand-Festgeldkonto bei der Sparkasse Saarbrücken an, Mindestanlage 3.000 Euro. Nach Angaben der Bestatterinnung S…`
  - HTML: `<p>Die saarländische Bestatterinnung (Fachinnung Holz und Kunststoff Saar) bietet als Treuhänder ein Festgeldkonto bei der Sparkasse Saarbrücken an — Mindestanlage 3.000 Euro. Das gesetzliche Schonver…`
- **A_TEXT[8]** — Wo finden Angehörige in Saarbrücken Beratung zu Bestattung und Grabpflege?
  - LD:   `Am Haupteingang des Saarbrücker Hauptfriedhofs an der Metzer Straße betreibt das Amt für Stadtgrün und Friedhöfe ein stationäres Informations- und Beratungszentrum, in dem Fragen zu Bestattung und Gra…`
  - HTML: `<p>Am Haupteingang des Saarbrücker Hauptfriedhofs an der Metzer Straße betreibt das Amt für Stadtgrün und Friedhöfe ein stationäres Informations- und Beratungszentrum — nach Angaben des Amts das bunde…`

### stuttgart  (LD=7, HTML=7)

- **A_TEXT[1]** — Was kostet eine Bestattung in Stuttgart?
  - LD:   `Die Gesamtkosten für eine Bestattung in Stuttgart liegen nach Erfahrungswerten aus Bestatter-Voranschlägen üblicherweise in einer Spanne von etwa 3.000 bis über 11.000 Euro; eine separate Stuttgart-St…`
  - HTML: `Eine separate Stuttgart-Studie aus einer belastbaren Verbraucherquelle liegt nicht vor. Erfahrungswerte aus Bestatter-Voranschlägen deuten auf eine grobe Spanne von etwa 3.000 Euro (einfache Feuerbest…`
- **A_TEXT[2]** — Gibt es in Stuttgart muslimische Grabfelder?
  - LD:   `Ja. Der Hauptfriedhof in Stuttgart-Bad Cannstatt unterhält seit 1985 ein dauerhaft gewidmetes muslimisches Grabfeld sowie seit 1944 ein armenisches Grabfeld. Sarglose Tuchbestattungen sind nach § 39 B…`
  - HTML: `Ja. Der Hauptfriedhof in Stuttgart-Bad Cannstatt unterhält seit 1985 ein dauerhaft gewidmetes muslimisches Grabfeld sowie laut Wikipedia seit 1944 ein armenisches Grabfeld. Sarglose Tuchbestattungen s…`
- **A_TEXT[3]** — Welche Ruhezeit gilt auf Stuttgarter Friedhöfen?
  - LD:   `Die Ruhezeit wird in Baden-Württemberg nach § 6 BestattG BW vom Friedhofsträger über die jeweilige Friedhofssatzung festgelegt. Die Stuttgarter Friedhofssatzung sieht in der Praxis 25 Jahre für Erdbes…`
  - HTML: `Die Ruhezeit wird nach § 6 BestattG BW vom Friedhofsträger über die Friedhofssatzung festgelegt. Die Stuttgarter Friedhofssatzung sieht in der Praxis 25 Jahre für Erdbestattungen Erwachsener und 20 Ja…`
- **A_TEXT[4]** — Wo befindet sich das Krematorium Stuttgart?
  - LD:   `Das städtische Krematorium liegt auf dem Pragfriedhof in Stuttgart-Nord. Das Jugendstil-Gebäude wurde 1905 bis 1907 von Architekt Wilhelm Scholter errichtet und gilt als eines der frühen Krematorien S…`
  - HTML: `Das städtische Krematorium liegt auf dem Pragfriedhof in Stuttgart-Nord. Das Jugendstil-Gebäude wurde 1905 bis 1907 von Architekt Wilhelm Scholter errichtet und zählt zu den frühen Krematorien Süddeut…`
- **A_TEXT[6]** — Was unterscheidet die Stadt-Seite von der Bundesland-Seite?
  - LD:   `Diese Seite konzentriert sich auf Stuttgart-spezifische Themen: die vier Hauptfriedhöfe mit ihrer Geschichte, die städtische Friedhofsgebührensatzung und Stadt-Adressen für den Todesfall. Das vollstän…`
  - HTML: `Diese Seite konzentriert sich auf Stuttgart-spezifische Themen: die vier Hauptfriedhöfe mit ihrer Geschichte, die städtische Friedhofsgebührensatzung und Stadt-Adressen für den Todesfall. Das vollstän…`

### wiesbaden  (LD=7, HTML=7)

- **A_TEXT[0]** — Wie viele Friedhöfe gibt es in Wiesbaden?
  - LD:   `Die Landeshauptstadt Wiesbaden unterhält 21 städtische Friedhöfe mit insgesamt rund 90 Hektar Fläche sowie den Bestattungswald Terra Levis in Frauenstein. Hinzu kommen sieben jüdische Friedhöfe und de…`
  - HTML: `<p>Die Landeshauptstadt unterhält 21 städtische Friedhöfe mit insgesamt rund 90 Hektar Fläche sowie den Bestattungswald Terra Levis in Frauenstein. Hinzu kommen sieben jüdische Friedhöfe – wovon nur d…`
- **A_TEXT[1]** — Was kostet ein Reihengrab in Wiesbaden?
  - LD:   `Nach der Friedhofsgebührensatzung kostet ein Erdreihengrab mit 30 Jahren Nutzungsrecht 1.517 Euro, ein Urnenreihengrab mit 20 Jahren 812 Euro. Hinzu kommen Bestattungsgebühren (Erdbestattung 418 Euro …`
  - HTML: `<p>Nach der Friedhofsgebührensatzung kostet ein Erdreihengrab mit 30 Jahren Nutzungsrecht 1.517 Euro, ein Urnenreihengrab mit 20 Jahren 812 Euro. Hinzu kommen Bestattungsgebühren (Erdbestattung 418 Eu…`
- **A_TEXT[2]** — Welche Bestattungsfrist gilt in Wiesbaden?
  - LD:   `Mit der Novelle des Friedhofs- und Bestattungsgesetzes Hessen, beschlossen am 30. September 2025, wurde die Höchstfrist von vier auf zehn Tage nach Todeseintritt verlängert. Die Mindestfrist bleibt be…`
  - HTML: `<p>Mit der am 30. September 2025 beschlossenen FBG-Novelle wurde die Bestattungshöchstfrist von vier auf zehn Tage nach Todeseintritt verlängert. Die Mindestfrist beträgt weiterhin 48 Stunden (§ 16 Ab…`
- **A_TEXT[3]** — Welcher Friedhof Wiesbadens ist der größte?
  - LD:   `Der Südfriedhof am Siegfriedring 25 ist mit 330.700 Quadratmetern der größte Friedhof Wiesbadens. Er entstand 1908/1909 und beherbergt das 1912 eröffnete erste Krematorium Preußens sowie das Familieng…`
  - HTML: `<p>Der Südfriedhof am Siegfriedring 25 ist mit 330.700 Quadratmetern der größte Friedhof Wiesbadens. Er entstand 1908/1909 und beherbergt das 1912 eröffnete erste Krematorium Preußens sowie das Famili…`
- **A_TEXT[4]** — Wo wird ein Sterbefall in Wiesbaden angezeigt?
  - LD:   `Der Sterbefall wird beim Standesamt Wiesbaden im Alten Rathaus, Marktstraße 16, 65183 Wiesbaden angezeigt. Bei Sterbefällen außerhalb eines Krankenhauses kann ein bevollmächtigtes Bestattungsinstitut …`
  - HTML: `<p>Das Standesamt Wiesbaden im Alten Rathaus, Marktstraße 16, 65183 Wiesbaden, ist zuständig. Bei Sterbefällen außerhalb eines Krankenhauses übernimmt ein bevollmächtigtes Bestattungsinstitut die Anze…`
- **A_TEXT[5]** — Gibt es in Wiesbaden eine Baumbestattung?
  - LD:   `Ja, im Frauensteiner Stadtwald wurde 2013 der Bestattungswald Terra Levis eingerichtet. Rund 540 Bäume auf etwa 25 Hektar Fläche stehen für Urnenbeisetzungen zur Verfügung, das Nutzungsrecht beträgt 9…`
  - HTML: `<p>Ja. Der Bestattungswald Terra Levis im Frauensteiner Stadtwald wurde 2013 eröffnet und umfasst rund 25 Hektar mit etwa 540 ausgewählten Bäumen. Das Nutzungsrecht beträgt 99 Jahre. Zusätzlich bietet…`

### wuppertal  (LD=7, HTML=7)

- **A_TEXT[1]** — Wie hoch sind die Bestattungskosten in Wuppertal?
  - LD:   `Die Gesamtkosten einer Bestattung liegen in Deutschland nach Erhebungen der Verbraucherzentrale und der Stiftung Warentest (Stand 2024) im Bereich von etwa 7.000 bis 8.000 Euro. In Wuppertal kommen Fr…`
  - HTML: `Die Gesamtkosten einer Bestattung liegen in Deutschland nach Erhebungen der Verbraucherzentrale und der Stiftung Warentest (Stand 2024) im Bereich von etwa 7.000 bis 8.000 Euro. In Wuppertal kommen Fr…`
- **A_TEXT[2]** — Welches Bestattungsrecht gilt in Wuppertal?
  - LD:   `In Wuppertal gilt das Bestattungsgesetz Nordrhein-Westfalen (BestG NRW). Maßgeblich sind unter anderem § 8 (Bestattungsfristen: Erdbestattung frühestens 48 Stunden, spätestens 10 Tage nach Feststellun…`
  - HTML: `In Wuppertal gilt das Bestattungsgesetz Nordrhein-Westfalen (BestG NRW). Maßgeblich sind unter anderem § 8 (Bestattungsfristen: Erdbestattung frühestens 48 Stunden, spätestens 10 Tage nach Feststellun…`
- **A_TEXT[3]** — Wo wird der Sterbefall in Wuppertal angezeigt?
  - LD:   `Die Anzeige des Sterbefalls erfolgt beim Standesamt Wuppertal am Johannes-Rau-Platz 1 (Barmen) und ist nach § 28 PStG spätestens am dritten Werktag nach dem Tod vorzunehmen. In der Regel übernimmt der…`
  - HTML: `Die Anzeige des Sterbefalls erfolgt beim Standesamt Wuppertal am Johannes-Rau-Platz 1, 42275 Wuppertal-Barmen, und ist nach § 28 PStG spätestens am dritten Werktag nach dem Tod vorzunehmen. In der Reg…`
- **A_TEXT[6]** — Was sollten Angehörige bei der Bestatter-Wahl in Wuppertal beachten?
  - LD:   `Empfehlenswert sind mindestens drei Kostenvoranschläge im Vergleich. Auf eine Mitgliedschaft im Bundesverband Deutscher Bestatter beziehungsweise im Landesverband Nordrhein-Westfälischer Bestatter, Tr…`
  - HTML: `Empfehlenswert sind mindestens drei Kostenvoranschläge im Vergleich. Auf eine Mitgliedschaft im Bundesverband Deutscher Bestatter bzw. im Landesverband Nordrhein-Westfälischer Bestatter, Transparenz d…`

## NO_LD (HTML-FAQ ohne JSON-LD FAQPage)

- muenster (HTML=7)

## NO_FAQ (keine FAQ-Sektion)

- darmstadt

## CLEAN

duisburg, hannover, kassel, leverkusen, luebeck, mannheim, moenchengladbach, muenchen, nuernberg
