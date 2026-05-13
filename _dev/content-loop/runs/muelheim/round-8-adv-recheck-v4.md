Ich lade die drei Dateien und prüfe v4 adversarial.

Fetching site
Web durchsucht

Jetzt die v4-Final.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/muelheim/v4-final.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/muelheim/v4-final.html

Adversarial-Modus. Ich prüfe gegen die 3 MUST-FIX aus Round 6, dann separat 3 neue Schwächen.

Round-6-MUST-FIX-Check:

NS-Verkürzung Altstadtfriedhof → v4: "ruhen nach Angaben der Stadt Mülheim 440 überwiegend russische Kriegsgefangene und Zwangsarbeiter aus beiden Weltkriegen". ✓ BEHOBEN (wörtlich Stadt-Quelle).
Marcks-Aussage → v4: "Marcks gehörte zu den bedeutendsten deutschen Bildhauern des 20. Jahrhunderts; ihm ist das Gerhard-Marcks-Haus in Bremen als eigenes Künstlermuseum gewidmet." Floskel "selten beachtetes Werk" und "Hauptarbeiten in Bremen und Köln" sind raus. Gerhard-Marcks-Haus Bremen in Quellen verlinkt. ✓ BEHOBEN.
Hauptfriedhof-Planung (Suhnel-Siegerentwurf) → v4: "Siegerentwurf „Den Toten zur Ruh" vom Mülheimer Architekten Theodor Suhnel stammte; der zweitplatzierte Entwurf „Grünumhegt" der Magdeburger Landschaftsarchitekten Friedrich Bauer und Walter Günther wurde mit dem Suhnel-Entwurf vereinigt... Bauleitung lag bei Fritz Keßler aus Leipzig." ✓ BEHOBEN.

Alle 3 MUST-FIX sauber abgearbeitet. Jetzt suche ich neue Schwächen — Annahme: die Page ist unter 85.

Adversarial-Funde v4:

SCHWÄCHE 1 — § 13 Abs. 2 BestG NRW religiöse Ausnahme (Kategorie 6 + 12, juristische Ungenauigkeit nicht behoben): Die Page sagt sowohl im Fließtext als auch in FAQ und in Schema.org: "§ 13 Abs. 2 BestG NRW erlaubt aus religiösen Gründen Ausnahmen von der 24-Stunden-Wartefrist". Das stand schon als SOLL-FIX 4 im Round-6-Recheck und wurde nicht angefasst. § 13 Abs. 2 BestG NRW enthält die 24h-Frist und eine generische Ausnahmebefugnis "in begründeten Fällen" — keine pauschale "religiöse" Ausnahme. Die Page erweckt fälschlich den Eindruck einer automatischen religiösen Ausnahme. Im Bestattungs-Compliance-Kontext (muslimische/jüdische Familien lesen die Page!) ist das nicht nur unscharf, sondern potenziell schadensstiftend, weil falsche Erwartungen geweckt werden. Fix: "Die Behörde kann nach § 13 Abs. 2 BestG NRW in begründeten Fällen Ausnahmen von der 24-Stunden-Wartefrist zulassen — in der Verwaltungspraxis insbesondere bei muslimischen und jüdischen Bestattungen, bei denen eine zeitnahe Beisetzung Glaubensritus ist. Die Genehmigung ist beim Ordnungsamt zu beantragen."

SCHWÄCHE 2 — Hugo-Stinnes-Gruft bleibt halb-erklärt (Kategorie 5 + 12): v4 schreibt "die Familiengruft Hugo Stinnes – Hugo Stinnes selbst starb 1924 in Berlin, in der Mülheimer Gruft ruhen aber weitere Familienmitglieder". Das war im Round-6-Recheck als ungelöst markiert ("HUGO STINNES UNGEKLÄRT"). Es ist immer noch ein erzählerischer Kurzschluss: Wenn er selbst nicht dort ruht, warum heißt sie "Familiengruft Hugo Stinnes"? Welche Familienmitglieder? Keine Namen, kein Datum, keine Quelle. Der Leser bleibt mit der Frage stehen. Entweder belegen (Stadt-Quelle Altstadtfriedhof listet Namen) oder anders einleiten ("die Gruft der Industriellenfamilie Stinnes mit Bestattungen aus der Generation vor Hugo Stinnes — er selbst starb 1924 in Berlin und wurde dort beigesetzt").

SCHWÄCHE 3 — Speldorf-Hidden-Gem ohne Substanz (Kategorie 2 + 5): Auch der war als SOLL-FIX 5 markiert und ist unverändert in v4: "Auf dem Friedhof finden sich Wahlgräber von Schiffer- und Hafenarbeiterfamilien aus der ersten Hafen-Generation Anfang des 20. Jahrhunderts." Kein einziger Name, keine Quelle. Bei genauer Lektüre ist das pure SEO-Konstruktion — ein generischer Satz, der über fast jeden Industriestadtteil-Friedhof in Deutschland geschrieben werden könnte ("hier finden sich Gräber von Arbeiterfamilien aus der Wachstumszeit"). Im Vergleich zum Altstadt-Hidden-Gem (Marcks, konkrete 440 Tote, Stadt-Quelle) und Hauptfriedhof-Gem (Ziegler, Daten, Nobelpreis) fällt Speldorf qualitativ deutlich ab. Fix: Entweder mindestens einen konkret recherchierten Namen/Reederei nennen oder die Behauptung tonal entschärfen ("vermutlich", "die Stadtgeschichte legt nahe") und stattdessen ein nachprüfbares anderes Detail nutzen (z.B. Trauerhallen-Architekt, Lage am Speldorfer Wald, konkrete Pflanzenwelt).

Zusätzliche Beobachtungen (nicht Top-3, aber für Vollständigkeit):

Preis-Spannen "niedrig/mittel/fünfstellig vierstellig" stehen unverändert drin (SOLL-FIX 6 nicht angefasst). Plausibilisierungs-Floskel ohne Mülheim-Bezug. Schwächer als der Rest der Page.
Datum-Konsistenz Friedhofssatzung: Quelle 4 nennt "Friedhofssatzung vom 19. Dezember 2013", die URL heißt aber friedhofssatzung_vom_161220031.html (legt 16.12.2003 nahe). Das ist Stadt-URL-Kuriosität, nicht unbedingt Faktenfehler — aber sollte gegengeprüft sein.
Standesamt-Adresse: "Am Rathaus 1" — schnell-check empfehlenswert, da das Mülheimer Rathaus offiziell als "Ruhrstraße 1" geführt wird. (Nicht hier verifiziert, aber als Recheck-Punkt notiert.)
JSON-LD FAQ duplicate vs. HTML-FAQ: Die FAQ steht im Schema.org-Block UND im HTML — Google-konform, aber ein Eintrag (Patenschaft Altstadtfriedhof) erscheint nur im Schema, nicht in der sichtbaren FAQ. Das ist Cloaking-Verdacht-Grenze (sichtbare vs. nur-Schema-FAQ-Antworten). Sollte gespiegelt werden.
OUTPUT

SCORE: 82/100

FUNDE:

MUST-FIX 1–3 aus Round 6 alle sauber behoben. NS-Formulierung jetzt wörtlich Stadt-Quelle, Marcks-Floskel raus + Gerhard-Marcks-Haus belegt, Suhnel als Siegerentwurf-Architekt korrekt eingeordnet inkl. Bauer/Günther und Fritz Keßler. Substanzieller Fortschritt gegenüber v2.
§ 13 Abs. 2 BestG NRW religiöse Ausnahme weiterhin juristisch ungenau — Page suggeriert automatische religiöse Ausnahme, real ist § 13 Abs. 2 eine generische Ermessensnorm "in begründeten Fällen". Im Bestattungs-Compliance-Kontext für muslimische/jüdische Hinterbliebene besonders heikel. War in Round 6 als SOLL-FIX markiert, nicht angefasst.
Hugo-Stinnes-Gruft bleibt narrativ-unaufgelöst — Page nennt "Familiengruft Hugo Stinnes" + Hinweis, dass er selbst nicht dort liegt, aber keine Mitglieder mit Namen/Datum/Quelle. Der Leser hat eine offene Frage am Ende. Round-6-Befund nicht aufgenommen.
Speldorf-Hidden-Gem ist pure SEO-Konstruktion — "Schiffer- und Hafenarbeiterfamilien aus der ersten Hafen-Generation" ohne einen einzigen Namen, ohne Quelle, ohne nachprüfbares Detail. Qualitativ deutlich schwächer als Altstadt-Gem (Marcks + 440 Tote belegt) oder Hauptfriedhof-Gem (Ziegler komplett belegt). Round-6-SOLL-FIX 5 nicht behoben.
Preis-Plausibilisierung "niedrig/mittel/fünfstellig vierstellig" unverändert ohne Mülheim-Quelle. Tonaler Bruch zur ansonsten quellenbasierten Page.
FAQ-Schema enthält Antwort zur Altstadtfriedhof-Patenschaft, die in der sichtbaren HTML-FAQ fehlt — formal Cloaking-Verdacht-Grenze, sollte gespiegelt werden.

MUST-FIX vor Deploy: ja.

MUST-FIX A: § 13 Abs. 2 BestG NRW religiöse Ausnahme präzisieren. Aktuelle Formulierung an drei Stellen (Fließtext Recht-Sektion, FAQ HTML, FAQ Schema.org) ersetzen durch: "Die zuständige Behörde kann nach § 13 Abs. 2 BestG NRW in begründeten Fällen Ausnahmen von der 24-Stunden-Wartefrist zulassen — in der Verwaltungspraxis insbesondere bei muslimischen und jüdischen Bestattungen. Die Ausnahme ist beim Ordnungsamt zu beantragen." Begründung: Compliance-Risiko für die kritischste Lesergruppe (Familien mit zeitkritischer religiöser Bestattung).
MUST-FIX B: Hugo-Stinnes-Eintrag auflösen. Entweder konkrete Familienmitglieder mit Daten aus Stadt-Altstadtfriedhof-Quelle nachtragen oder umformulieren zu "Gruft der Industriellenfamilie Stinnes (Hugo Stinnes selbst starb 1924 in Berlin)". Aktuell hängt der Leser in einer offenen Frage.
MUST-FIX C: Speldorf-Hidden-Gem entweder mit mindestens einem konkret-recherchierten Schiffer-/Reederei-Namen belegen ODER auf nachprüfbares Detail umstellen (Trauerhalle, Pflanzenwelt analog zu Broich, konkrete Lage am Mülheimer Hafen). Aktuell qualitatives Loch im Friedhofs-Quartett.

SOLL-FIX D (nicht-Blocker, aber empfohlen): Preis-Spannen mit Mülheim-spezifischer Quelle (z.B. bestattung-information.de nennt konkrete Beträge) ersetzen oder streichen — sonst tonaler Bruch zur sonst quellenbasierten Page.

SOLL-FIX E: FAQ-Frage zur Altstadtfriedhof-Patenschaft aus Schema.org auch in HTML-FAQ spiegeln (Cloaking-Hygiene).

Begründung Score 82: Substantielle Verbesserung gegenüber v2 (Round-6-MUST-FIX alle behoben), aber drei Round-6-SOLL-FIX-Punkte ungelöst geblieben. Davon ist mindestens MUST-FIX A (juristische Ungenauigkeit § 13 Abs. 2 mit Lesergruppen-Risiko) ein neuer harter Blocker, der vor Deploy gefixt werden muss. Page-Substanz solide, drei Detail-Lücken kosten 18 Punkte.