Ich lade die drei Dokumente und reviewe ohne Schönfärberei.

Web durchsucht
Web durchsucht

BRIEFING_OK

Jetzt adversarial. Annahme: v2 ist unter 85, mindestens 3 echte Schwächen drin. Lese gezielt auf das, was v1-Review NICHT abgedeckt hat oder was Chat A in v2 neu eingebracht hat.

SCORE: 78/100

FUNDE:

SCHWÄCHE 1: Halluzinations-Verdacht beim Lehrpfad „Zukunftsbäume mit über 50 Stationen" (Hauptfriedhof-Block, 3. Absatz) — Diese sehr spezifische Zahl ("über 50 Stationen") taucht im gesamten Quellenapparat nicht auf. dortmund.de erwähnt einen „Lehrpfad" nur generisch; die „50 Stationen" sind Erfindung oder ungeprüft übernommen. Genauso die „Schafe auf der Talwiese" — kein Quellen-Anker im Apparat. Bei einer YMYL-Page, die in Round 2 ausdrücklich auf Primärquellen-Disziplin getrimmt wurde, ist das ein Rückfall. Fix: entweder Quelle (Stadt Dortmund Pressestelle / Tiefbauamt) nachliefern oder beide Details streichen — Hidden Gem trägt sich auch ohne diese Spezifika über Platane + Kolumbarium-Öfen.

SCHWÄCHE 2: Gebührentabelle 2019 ist ein Deploy-Blocker, nicht ein Caveat — und der Review-Hinweis aus Round 2 wurde nur halb umgesetzt — Round-2-Review hat klar gesagt: „entweder mit Werten aus der aktuellen Gebührensatzung (2025/2026) ersetzen ODER mit deutlichem Hinweis markieren ODER Tabelle entfernen". Chat A hat Option 2 gewählt (Caveat), aber damit bleibt das Kernproblem: Ein Nutzer in akuter Trauerfall-Situation sieht eine Tabelle mit konkreten EUR-Werten und nimmt diese als Orientierung, auch wenn drüber steht „Erhöhungen bis 2025 nicht eingerechnet". Das ist bei einem YMYL-Thema (Geld in akuter Notlage) ein Vertrauens- und Conversion-Killer beim ersten Faktencheck durch einen Hinterbliebenen. Bei einer Page, die Bestatter-Leads für 150–300 € verkaufen soll, ist eine 6 Jahre alte Preistabelle kein „indikativer Korridor" sondern Risikomaterial. Fix: Tabelle löschen und durch Prosa-Korridor ersetzen ("Friedhofsgebühren in Dortmund liegen je nach Grabart zwischen XXX und XXX EUR; verbindlich ist die aktuelle Satzung — Link") ODER aktuelle Werte aus der 2025er Satzung nachziehen. Halbgar lassen ist schlechter als beides.

SCHWÄCHE 3: Quellen-Lücke beim LSG-NRW-Urteil — Sekundärquelle (Aeternitas) bei juristischer Aussage, statt Originalurteil — Der Absatz zur Sozialbestattung zitiert das LSG NRW Urteil vom 23.05.2024 (Az. L 9 SO 49/23) mit konkreter Rechtsaussage („Sozialamt darf Übernahme nicht ohne Weiteres auf eine pauschale Summe begrenzen"). Verlinkt ist aber Aeternitas, ein Vereinsblog. Das ist exakt der „Wikipedia-bei-juristischer-Aussage"-Antipattern aus dem Briefing (Kategorie 1). Bei einer Aussage mit konkretem Az., konkretem Datum und konkretem Inhalt MUSS die Primärquelle (NRWE-Rechtsprechungsdatenbank, justiz.nrw.de) verlinkt sein — sonst ist die Beweisführung im Glashaus. Zusätzlich: Aussage „Eheleute / konfessionelle Bestattung" als Beispiele für „besondere Umstände" stammt aus dem Aeternitas-Text, nicht aus dem Urteil selbst — wenn das LSG das so nicht gesagt hat, ist es eine sekundär-paraphrasierte Auslegung, die hier als Urteilsinhalt verkauft wird. Fix: Primärlink zu NRWE/openjur ergänzen, Aussage gegen Originalurteil verifizieren, ggf. die „besonderen Umstände" weicher fassen.

Weitere belastbare Mängel (nicht in den Top-3, aber Deploy-relevant):

Ostfriedhof-Block: „Henriette Davidis" als „Kochbuch-Ikone des 19. Jahrhunderts, ihr 'Praktisches Kochbuch' erschien ab 1845 in über 70 Auflagen" — Round-2-Hinweis wurde übernommen, ABER: die „über 70 Auflagen"-Zahl ist nicht im Quellenapparat belegt. Wikipedia nennt das, Stadt Dortmund nicht. Bei YMYL-Disziplin: Quelle oder weicher.
„Schalkenmehren"-Fix war notwendig, ist jetzt „Schaufenster der Stadtgeschichte und Ruheort der BVB-Gründer" — funktioniert, aber „Schaufenster der Stadtgeschichte" ist generisch und passt nicht zum eigentlichen Hidden Gem (Franz Jacobi/BVB). Die H3 verspricht zwei Dinge, der Block liefert eines. Substanz im Südfriedhof-Block bleibt insgesamt der dünnste der vier — nur Franz Jacobi konkret + Weltkriegs-Gedenkstätte als Mini-Erwähnung. Im Vergleich zu Haupt-/Ost-/Nordfriedhof fällt der Südfriedhof ab. Briefing-Kategorie 8 (Sektion zu dünn) trifft hier zu.
Wortzahl-Check: Sichtbarer Content nach grober Schätzung ca. 2.300 Wörter — okay, aber Südfriedhof-Block trägt davon vielleicht 150 Wörter. Asymmetrie zwischen den vier Friedhöfen ist auffällig.
„ersten Etagen-Einäscherungsöfen aus dem Jahr 1924" im Hauptfriedhof Hidden Gem — Aussage ist sehr stark („deutschlandweit erste"? oder „die ersten dieses Krematoriums"?). Formulierung ist mehrdeutig. Wenn „erste Etagen-Öfen Deutschlands" gemeint: Beleg fehlt. Wenn nur „erste dieses Krematoriums": trivial und kein Hidden Gem.
Schema.org @graph ist sauber gemacht — FAQPage, Article, BreadcrumbList, Place-Knoten für alle vier Friedhöfe. Kein Mangel hier. Wenn überhaupt: Author beim Article ist „Organization machsruhig Redaktion" — bei YMYL wäre eine Person plus Qualifikation E-E-A-T-stärker. Aber kein Blocker.
UNSURE-Kommentare im HTML-Output sichtbar gelassen — <!-- UNSURE: ... --> Kommentare sind im finalen HTML nicht produktionsreif. Sind zwar HTML-Kommentare und für Nutzer unsichtbar, aber: ein neugieriger Wettbewerber/Journalist sieht den Source und bekommt eine Liste eurer Unsicherheiten frei Haus. Vor Deploy raus.

MUST-FIX vor Deploy: JA.

Begründung: 2 von 3 substantiellen Schwächen (Gebührentabelle 2019 als Vertrauenssignal-Risiko + LSG-Urteil mit Sekundärquelle) sind bei einer YMYL-Page mit Lead-Gen-Absicht nicht akzeptabel. Hinzu kommen die UNSURE-Kommentare im HTML-Output, die schlicht ein Build-Hygiene-Versäumnis sind und in 2 Minuten gefixt werden können. Halluzinations-Verdacht beim Lehrpfad ist heilbar durch Streichung. Score 78 ist substantieller Fortschritt gegenüber v1 (74) — aber unter dem 85er-Threshold.

EHRLICHE %-ZAHL: 78%