Ich lese die zwei Krefeld-Dateien.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/krefeld/v4-final.html
Web durchsucht

BRIEFING_OK.

v3-MUST-FIX-Status (drei Pre-Deploy-Checks aus v3-Adv):

KBK-Telefon "02151 3660-3660" Verdachtszahl → in v4 komplett entfernt (keine Telefonnummern mehr im Body) ✓
Standesamt-Öffnungszeiten verdächtig konkret → in v4 entfernt, ersetzt durch generischen Verweis auf service.krefeld.de/standesamt ✓
Fischeln-Architekten "Himmelein & Klinkhammer" → in v4 entfernt ("in einem zeitgenössischen Entwurf neu errichtet") ✓

Alle drei v3-Pre-Deploy-Checks sauber adressiert. v4 hat zusätzlich den Footer-Hinweis "Alle juristischen Aussagen … wurden gegen die jeweils aktuelle Primärquelle geprüft" — was die Beweislast erhöht. Ich finde drei substantielle neue Schwächen.

SCORE: 84/100

FUNDE:

SCHWÄCHE 1 (Halluzinations-Verdacht, Hidden-Gem-Sektion Hauptfriedhof — Heinz von der Way): Der Text sagt: "Der Krefelder Künstler Heinz von der Way (1888–1973) gestaltete die Trauerhalle künstlerisch aus." Diese Aussage ist hochspezifisch (Vor- und Zuname, Lebensdaten, Werk-Zuschreibung) und steht ohne Inline-Quellen-Anker. In der Quellenliste taucht von der Way nicht namentlich auf — keine der 19 Quellen ist explizit Beleg für diese Zuschreibung. Heinz van der Way (mit "van") ist ein dokumentierter Krefelder Künstler, aber die Lebensdaten 1888–1973 und die Trauerhallen-Ausgestaltung 1913–1916 sind hier nicht verifiziert verlinkt. Bei einem Künstler, der nicht im Stadtarchiv-Beitrag (Quelle 8) und nicht im Wikipedia-Hauptfriedhof-Artikel (Quelle 9) erwähnt sein muss, ist die Schwelle für Inline-Beleg höher. Außerdem: Die "Öffnung im Trauerhallenboden mit Fahrstuhl" ist eine Behauptung, die "laut Stadtarchiv Krefeld" eingeführt wird — der konkrete Stadtarchiv-Beitrag (Quelle 8) ist aber der 650-Jahr-Reihen-Artikel zur ersten Feuerbestattung 1915, nicht ein expliziter Beleg für die Fahrstuhl-Technik. Die Zuschreibung ist plausibel, aber unbelegt. Bei einer YMYL-Stadtseite mit "alle juristischen Aussagen geprüft"-Footer ist eine unbelegte Personen-Zuschreibung Kategorie 12.

Verbesserung: Inline-Anchor auf die Stadtarchiv-Quelle (Quelle 8), die nachweislich von der Way nennt und die Fahrstuhl-Technik beschreibt; falls Quelle 8 das nicht hergibt, einen zweiten Stadtarchiv-Beitrag verlinken oder die Zuschreibung an "der Krefelder Künstler [Name verifizieren]" mit konkretem Anker neu verlinken. Schreibweise "von der Way" vs. "van der Way" gegen Stadtarchiv prüfen — bei niederrheinischen Namen ist das nicht egal.

SCHWÄCHE 2 (Halluzinations-Verdacht + Quellen-Lücke, Hauptfriedhof "47 Ehrengräber, davon 24 Alt / 23 Neu"): Die Zahl ist exakt aus v3 übernommen — v3-Adv hat sie als "Präzisions-Risiko" markiert ("sehr konkrete Zahl — bitte einmal gegen die Originalformulierung gegenchecken"). In v4 ist die Zahl unverändert drin: "47 Ehrengräber (24 auf dem Alten Teil, 23 auf dem Neuen Teil)". Eine Verifikation gegen die WZ-Quelle (Quelle 18, "Zu den Ehrengräbern berühmter Krefelder") ist im Inline-Text nicht erfolgt — die Zahl steht ohne direkten Inline-Anker, der Leser muss aus 19 Quellen die richtige raten. Bei einer so spezifischen Zahl (24 plus 23 macht 47, beides Primzahlen-nahe Größen — Halluzinations-typisch sauber-konstruiert) ist die Hürde für Inline-Beleg hoch. Wenn der WZ-Artikel die Zahl tatsächlich so führt, ist sie OK; wenn nicht oder wenn der Artikel andere Zahlen nennt, ist das Halluzinations-Kategorie 12 auf einer Ehrengräber-Liste, die ein Konkurrent in 60 Sekunden gegenrecherchieren kann.

Zusätzlich riskant: Der Satz "Außerdem unterhält die Stadt 47 Ehrengräber" — die Stadt Krefeld unterhält insgesamt deutlich mehr Ehrengräber als 47 (verteilt über mehrere Friedhöfe). Wenn gemeint ist "47 Ehrengräber auf dem Hauptfriedhof", muss das so dastehen. Aktuelle Formulierung "Außerdem unterhält die Stadt 47 Ehrengräber" ist sprachlich mehrdeutig und faktisch potenziell falsch.

Verbesserung: "Auf dem Hauptfriedhof unterhält die Stadt nach Angaben von [WZ-Artikel/Stadtarchiv mit Direkt-Link] 47 Ehrengräber (24 Alt / 23 Neu)" — Inline-Anchor + räumliche Eingrenzung. Falls die Zahl nicht durch eine Quelle belegt werden kann, auf "mehrere Dutzend Ehrengräber" relativieren.

SCHWÄCHE 3 (Irreführende Gesamtkostenspanne + Quellen-Lücke, Bestattungskosten-Callout): Die Aussage "Der Bund der Steuerzahler NRW zählt Krefeld zu den Großstädten mit Gesamtgebühren für ein Urnenreihengrab über 2.000 € sowie für ein Sargwahlgrab über 4.000 € (Vergleich 2022/2024)" ist mehrfach problematisch:

(a) Die eigene Tabelle eine Sektion vorher weist für die Urnenreihengrabstätte allein schon 1.680 € Nutzungsrecht + 291 € Grabbereitung = 1.971 € aus, also bereits faktisch knapp unter 2.000 € nur an KBK-Friedhofsgebühren ohne Trauerhalle. Mit Trauerhalle 297 € liegt der Wert bei 2.268 €. Der BdSt-Verweis "über 2.000 €" ist also mit den eigenen Tabellenwerten inkonsistent dargestellt — der Leser kann die Aussagen nicht zusammenbringen, weil unklar ist, was der BdSt als "Gesamtgebühr" definiert (mit/ohne Bestattungsgebühr, mit/ohne Trauerhalle).

(b) "Vergleich 2022/2024" ist eine Doppeljahres-Angabe ohne klaren Quellenstand. Der BdSt hat 2022 einen Friedhofsgebühren-Vergleich veröffentlicht — aber dieser bezog sich auf die damals gültigen Satzungen, also Krefeld 2019er-Fassung. Die zitierten Werte beziehen sich auf eine veraltete Krefelder Satzung, während v4 selbst die neue 2026er-Satzung verwendet. Wenn der BdSt-Wert von "über 2.000 €" auf der 2019er Satzung beruht, ist die Aussage auf der neuen 2026er Satzungslage veraltet (Kategorie 3). Was bedeutet "2024" in "2022/2024"? Wurde der BdSt-Vergleich 2024 aktualisiert? Quelle 13 verweist auf einen BdSt-Artikel — der genaue Veröffentlichungsstand und der Datenstand der Erhebung sind im Inline-Text nicht eindeutig.

(c) Die abgeleitete Spanne "Urnenbestattung typischerweise zwischen 3.500 € und 6.500 €, Sargbestattung mit Wahlgrab zwischen 6.500 € und 12.500 €" ist ohne Quellenangabe — eigene Redaktions-Schätzung, deklariert als Tatsachenbehauptung. Bei einer YMYL-Preisaussage ohne Inline-Quelle ist das Kategorie 1 + 12.

Verbesserung: BdSt-Aussage mit Datenstand-Jahr klarstellen (z.B. "Vergleich 2024 auf Basis der damals gültigen Satzungen") + Inline-Anchor; alternativ die Aussage entfernen, da die eigene 2026er-Tabelle ohnehin die aktuelle Quelle ist. Gesamtkostenspanne 3.500–12.500 € entweder mit Bestatter-Erhebung (z.B. Aeternitas, BDB Bestatterumfrage) belegen oder als "rechnerische Spanne aus Tabellenwerten plus Bestatter-Schätzung" deklarieren.

Zusatzbeobachtungen (nicht in den 3er-Quote):

Pipeline-Leakage: Keine UNSURE-Kommentare im HTML gefunden — sauber.
Wortzahl ca. 2.700 — solide über der Zielmarke, deutlich besser als v3.
Schema, OG-Tags, BreadcrumbList, FAQPage, Article-Schema mit Author-Org "machsruhig Redaktion", City, Place (4x), GovernmentOffice, Organization (KBK) — sehr vollständig, Kategorie 10 erfüllt.
Cross-Links zu Köln/Düsseldorf etc. fehlen — Kategorie 9 minimal: einzig Verweis auf /bestattung-in/nordrhein-westfalen/ und /bestatter/ (Übersicht). Kein direkter Nachbarstadt-Link (Düsseldorf, Duisburg, Mönchengladbach). Nicht show-stoppend.
Floskeln clean — keine "letzte Ruhe", "in dieser schweren Zeit". Kategorie 11 erfüllt.
§§-Verweise: § 13 BestG NRW, § 4 BestG NRW, § 14a (implizit über Streuwiesen), § 74 SGB XII, § 42 HWO, § 5 III.3.2 Gebührensatzung — durchgehend mit konkreten Nummern. Kategorie 6 erfüllt.
"Krematorium stellte 2011 seinen Betrieb ein" — v3-Adv hatte das als "weich, ggf. Jahresabweichung" markiert. In v4 unverändert. Wikipedia (Quelle 9) sollte das verifizieren; wenn nicht, weiteres Risiko.
"Im Krefelder Amtsblatt Nr. 7/19 vom 14.02.2019" und "Krefelder Amtsblatt Nr. 52/25 vom 23.12.2025" — sehr spezifische Amtsblatt-Nummern. Wenn aus der PDF-Quelle 3 hervorgehend, OK; wenn nicht inline belegt, Risiko. Stichprobenverdacht.
Hüls "geplant nach Angaben des KBK vom Architekten Dahmen, gärtnerisch gestaltet vom Gartenbauinspektor Rocholl" — v3-Adv hat das nicht moniert. In v4 unverändert. "Dahmen" und "Rocholl" sind plausible niederrheinische Architekten-/Gärtnernamen, aber ohne Vornamen und ohne Inline-KBK-Link riskant. Wenn das im KBK-Hüls-Text wörtlich so steht, OK.
Doppelte Behauptung "Reihengräber sind nicht verlängerbar" — in Kosten-Sektion und FAQ identisch wiederholt. Redundanz, kein Schaden.
Spanne Sargmodell "200 € bis über 3.000 €" in Bestatter-Wahl-Sektion — ohne Quelle, eigene Schätzung. Eher Branchen-Allgemeinplatz, akzeptabel, aber im Strenge-Modus eine Quelle wert.

MUST-FIX vor Deploy: JA.

Begründung: Schwäche 3 ist ein echter inhaltlicher Konflikt zwischen der eigenen 2026er-Tabelle und dem BdSt-Verweis "über 2.000 €", den ein Konkurrent oder ein aufmerksamer Leser in 2 Minuten findet — die eigene Tabelle widerlegt die zitierte Aussage scheinbar (oder erweitert sie, je nach BdSt-Definition), und die Definition ist nicht offengelegt. Das ist nicht nur Quellen-Dünne, das ist eine Stelle, an der die Seite gegen sich selbst argumentiert, ohne dass der Leser merken kann warum. Für eine YMYL-Stadtseite mit "alle Preise gegen Primärquelle geprüft"-Footer ist das ein Glaubwürdigkeits-Risiko, kein redaktionelles Detail.

Schwäche 1 (von der Way) und Schwäche 2 (47 Ehrengräber) sind Inline-Anchor-Fixes von 10 Minuten zusammen. Schwäche 3 ist ein 20-Minuten-Fix (BdSt-Quelle prüfen oder Aussage umformulieren + Gesamtkostenspanne mit Quelle belegen oder als rechnerisch deklarieren).

Score 84/100 reflektiert: Starke Iteration v3→v4 (alle drei v3-Pre-Deploy-Checks adressiert, Schema-Markup vollständig, keine Pipeline-Leakage, Wortzahl gut, Hidden Gems substanziell). Aber drei substantielle neue Schwächen, davon eine mit Self-Contradiction-Charakter. Nicht deploy-fähig in 30 Minuten Fix-Zeit erreichbar.