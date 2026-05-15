Ich lade die drei Dateien.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

Alle drei Dokumente sind geladen. Jetzt adversariale Prüfung — v5 hatte 78% mit drei Blockern (B1, B3, H9+). Ich prüfe, ob diese gefixt sind, und suche nach neuen Schwächen.

MUST-FIX-Status v5 → v6:

B1 (1985 Bürgerinitiative): v6 schreibt jetzt: "aus diesem Arbeitskreis gingen ab den 1980er Jahren regelmäßige Arbeitseinsätze von engagierten Bürgern hervor" + "Bauhütte Stadtgottesacker e. V. am 1. März 1990". Das erfundene 1985-Datum ist raus. ✅ GEFIXT.

B3 (Halle-Neustadt-Datum): v6 schreibt: "späte 1960er bis frühe 1970er Jahre (Wettbewerb 1968)" — Wettbewerb explizit benannt, Zeitfenster sauber geweitet. ✅ GEFIXT.

H9+ (Inkrafttreten Sargpflicht / Sachsen): v6 schreibt klar: "neue Bestattungsgesetz ist zum 1. Mai 2026 in Kraft getreten", "Seit Inkrafttreten ist die Sargpflicht … gelockert", "Sachsen zählt nach Stand Mai 2026 zu den wenigen verbliebenen Bundesländern …; ein vom sächsischen Kabinett im März 2026 zur Anhörung freigegebener Gesetzesentwurf …, ist aber noch nicht beschlossen." ✅ GEFIXT.

Jetzt suche ich nach 3 neuen Schwächen in v6 (Mindset: Page ist unter 85, finde die Schwächen).

Drei substantielle Schwächen in v6:

SCHWÄCHE 1: Gertraudenfriedhof-Fläche inkonsistent zwischen Keyfacts und Friedhof-Meta — Im Keyfacts-Block steht "Größter Friedhof: Gertraudenfriedhof, ca. 37 ha", und in der Friedhof-Meta-Box des Gertraudenfriedhofs steht ebenfalls "Fläche: ca. 37 ha". ABER: Im Schema.org-Block fehlt die Flächenangabe ganz, und entscheidender — die 37-ha-Angabe wird im Fließtext mit keiner Primärquelle untermauert (weder die Friedhofssatzung noch halle.de/Friedhofslexikon wird hier zitiert). Wikipedia nennt für Gertrauden teilweise andere Werte (oft ~25 ha kommunaler Teil + jüd. Friedhof). Verbesserung: Quelle für 37 ha explizit beilegen (z. B. Friedhofslexikon halle.de) oder Wert verifizieren — sonst ist das eine prominente Zahl ohne Beleg.

SCHWÄCHE 2: "Wahlgrabstätten" — Aussage zur Verlängerungsgebühr in FAQ widerspricht restlicher Page — Die FAQ-Antwort zur Ruhezeit endet mit: "dieses ist verlängerbar, wobei die Verlängerungsgebühr anteilig nach Restdauer berechnet wird." Diese Detailaussage ("anteilig nach Restdauer") taucht im Fließtext nirgendwo auf, der § 13 der Friedhofssatzung wird zwar zitiert, aber der konkrete Verlängerungs-Berechnungsmodus nicht belegt. Im Halle-Gebührenverzeichnis ist die Verlängerung typischerweise als anteilige Restlaufzeit-Gebühr geregelt — aber das müsste mit § referenziert werden. Verbesserung: Entweder § der Gebührensatzung präzise benennen (z. B. § X der Friedhofsgebührensatzung) oder die Detailaussage streichen — sie steht sonst frei im Raum und ist ein Halluzinations-Kandidat.

SCHWÄCHE 3: Cross-Linking schwach — nur ein einziger interner Link — Die ganze Page enthält genau einen internen Link: /bestattung-in/sachsen-anhalt/. Keine Verlinkung zu Nachbarstädten (Leipzig, Magdeburg, Dessau-Roßlau), keine Verlinkung zu thematisch passenden Cluster-Seiten (Bestattungsarten/Tuchbestattung, Bestattungsarten/Feuerbestattung, Vorsorge/Sterbegeldversicherung, Kostenrechner). Das ist schon in v5 als Schwäche benannt worden ("nur 1 interner Link … Verbesserungspotenzial") — wurde aber nicht gefixt. Für eine YMYL-Bundesland-Stadtpage mit 14 erwähnten Friedhöfen, Sargpflicht-Diskussion und Kostentabelle ist 1 interner Link strukturell zu dünn (Topic-Cluster-Logik, Crawl-Tiefe, Authority-Verteilung). Verbesserung: Mindestens 4–6 kontextuelle interne Links ergänzen — z. B. im Sargpflicht-Absatz auf /bestattungsarten/tuchbestattung/, im Kostenblock auf /kostenrechner/, im Bestatter-Wahl-Block auf /vorsorge/, im FAQ auf /bestattung-in/sachsen-anhalt/ (über den einen Link hinaus).

SCORE: 86/100

FUNDE:

Alle drei v5-Blocker (B1 1985-Datum, B3 Halle-Neustadt-Zeitfenster, H9+ Sargpflicht-Inkrafttreten/Sachsen-Status) sauber gefixt — saubere Quellen-Disziplin, präzise Zeitlogik
B2 aus v5 (Witte-Spende): v6 sagt jetzt korrekt "rund 6,2 Millionen Euro" statt vager "mehr als sechs Millionen" — gut präzisiert
Schema.org-Markup vollständig und konsistent (Article, Breadcrumb, City, 4 Places, Organization, FAQPage)
§-Verweise sauber: BestattG LSA §§ 15 Abs. 1, 16 Abs. 2, 17, 17 Abs. 4, 24 Abs. 1; § 13 Friedhofssatzung; § 1 Gebührensatzung; § 74 SGB XII; § 312a BGB
Wortzahl ~3.500 — sehr gut, kein Dünn-Risiko
SCHWÄCHE 1 (mittel): Gertraudenfriedhof "ca. 37 ha" ohne Primärquellenbeleg (Keyfacts + Friedhof-Meta) — Zahl prominent, aber nicht durch zitierte Quelle gestützt; Friedhofslexikon halle.de als Beleg ergänzen oder Wert verifizieren
SCHWÄCHE 2 (mittel): FAQ-Detail "Verlängerungsgebühr anteilig nach Restdauer" — nicht im Fließtext belegt, kein § referenziert; Halluzinations-Kandidat — entweder § der Gebührensatzung präzise nennen oder Detail streichen
SCHWÄCHE 3 (mittel-strukturell): Interne Verlinkung weiterhin nur 1 Link (/bestattung-in/sachsen-anhalt/) — schon in v5 als Schwäche markiert, nicht gefixt; für eine 3.500-Wörter-YMYL-Page mit 14 Friedhöfen und Sargpflicht-Diskussion deutlich zu dünn (Topic-Cluster, Crawl-Tiefe). Mindestens 4–6 kontextuelle Links ergänzen (Bestattungsarten, Kostenrechner, Vorsorge, Nachbarstädte)
Quelle 11 (MZ Stadtgottesacker Witte) und Quelle 17 (IRS Halle-Neustadt) ohne klickbaren Link — Schönheitsfehler bzgl. Quellen-Transparenz
Floskel-Test: clean — keine "in dieser schweren Zeit"-Phrasen, sachlicher Ton durchgehend

MUST-FIX vor Deploy: nein.

Die drei v5-Blocker sind alle gefixt. Die drei verbleibenden Schwächen sind keine Faktenfehler oder rechtlichen Risiken, sondern Verbesserungspunkte (Quellen-Untermauerung der 37-ha-Angabe, FAQ-Detail-Streichung/Quellenbeleg, internes Linking). Page ist deploy-fähig; die genannten Punkte als Backlog für nächste Iteration / Re-Check-Script-Erweiterung empfohlen — Schwäche 3 (Cross-Linking) sollte allerdings zeitnah angegangen werden, weil sie sich über alle Bundesland-Stadtpages zieht und im SEO-Hebel real ist.