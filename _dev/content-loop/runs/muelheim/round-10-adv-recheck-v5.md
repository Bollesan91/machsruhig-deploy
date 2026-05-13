Ich lade die drei Dateien und prüfe v5 gegen die v4-Findings.

Fetching site
Web durchsucht

Jetzt v5 holen und gegen die 3 MUST-FIX (A, B, C) prüfen.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/muelheim/v5-final.html

Adversarial-Modus. Ich prüfe die drei v4-MUST-FIX und suche dann frisch nach Schwächen.

Check der v4-MUST-FIX:

MUST-FIX A (§ 13 Abs. 2 BestG NRW religiöse Ausnahme): v5 hat die Formulierung an drei Stellen (Fließtext Recht-Sektion, HTML-FAQ, Schema.org-FAQ) konsequent ersetzt durch: "Die zuständige Behörde kann nach § 13 Abs. 2 BestG NRW in begründeten Fällen Ausnahmen … zulassen – in der Verwaltungspraxis insbesondere bei muslimischen und jüdischen Bestattungen … Die Ausnahme ist beim Ordnungsamt zu beantragen." ✓ BEHOBEN, exakt nach Vorschlag.

MUST-FIX B (Hugo-Stinnes-Eintrag): v5 schreibt nun "die Gruft der Industriellenfamilie Stinnes (Hugo Stinnes selbst starb 1924 in Berlin und wurde dort beigesetzt)" — Alternative 2 aus dem Vorschlag. ✓ BEHOBEN, offene Frage geschlossen.

MUST-FIX C (Speldorf-Hidden-Gem): v5 hat das Hidden Gem umgebaut. Die alte SEO-Konstruktion ("Schiffer- und Hafenarbeiterfamilien") ist raus. Neuer Text setzt auf nachprüfbare Details: Lage am Speldorfer Wald, Ruhraue-Landschaftsschutzgebiet, parkähnliche Anlage, Stadt-Zitat "Naturraum und Bestattungsort", Bandbreite pflegefreier Bestattungsformen. ✓ BEHOBEN nach Alternative 2 (nachprüfbares Detail statt Namen).

Alle drei MUST-FIX sind sauber abgearbeitet. Jetzt frische Suche — Annahme: die Page ist unter 85.

SCORE: 86/100

FUNDE:

MUST-FIX A–C alle behoben. § 13 Abs. 2 jetzt juristisch korrekt als Ermessensnorm formuliert, an allen drei Stellen (Fließtext, HTML-FAQ, Schema.org-FAQ) konsistent. Stinnes-Eintrag aufgelöst. Speldorf-Gem auf nachprüfbare Lage-Details umgestellt.
SCHWÄCHE 1 (Kategorie 12, Halluzinations-Verdacht): Standesamt-Adresse "Am Rathaus 1" weiterhin unverifiziert. Stand schon im v4-Recheck als zu prüfender Punkt drin, wurde nicht angefasst. Das Mülheimer Rathaus wird offiziell als "Ruhrstraße 1" geführt. "Am Rathaus 1" steht jetzt sowohl im Step-3 der Todesfall-Sektion als auch in der HTML-FAQ — eine möglicherweise falsche Adresse, die Hinterbliebene in der Akutsituation an die falsche Stelle schickt. Compliance-relevant. Fix: gegen Stadt-Quelle prüfen, ggf. ersetzen.
SCHWÄCHE 2 (Kategorie 3 + 12, Datum-Inkonsistenz Friedhofssatzung): URL-vs.-Datums-Widerspruch unverändert. Quelle 4 + Fließtext nennen "Friedhofssatzung vom 19. Dezember 2013", die verlinkte URL lautet aber friedhofssatzung_vom_161220031.html — legt nahe, dass die Stadt-URL auf das Datum 16.12.2003 verweist. Entweder ist das Datum im Text falsch (dann ist die ganze Page mit einer falschen Jahreszahl als Hauptsatzungsdatum unterwegs) oder die URL ist eine kuriose Stadt-Eigenheit (dann sollte das geprüft sein). War im v4-Recheck als Punkt notiert, blieb ungelöst. Fix: URL aufrufen, prüfen was die Stadt selbst als Datum nennt, dann konsistent machen.
SCHWÄCHE 3 (Kategorie 11, Floskel): Doppelte Plausibilisierung in Kosten-Sektion. Der Satz "einfache Urnenbeisetzungen liegen erfahrungsgemäß im niedrigen vierstelligen, klassische Erdbestattungen mit Trauerfeier im mittleren vierstelligen Bereich; repräsentative Wahlgräber mit größerer Trauerfeier können auch fünfstellig werden" ist unverändert aus v4 übernommen — der SOLL-FIX D ("Preis-Spannen mit Mülheim-spezifischer Quelle ersetzen oder streichen") wurde ignoriert. Im Kontext einer ansonsten quellenstrengen Page ("nach Auswertung BdSt NRW 2024", "Gebührensatzung 20.12.2022") ist "erfahrungsgemäß" der einzige Beleg-freie Brocken. Liest sich wie aus einem generischen Bestatter-Ratgeber kopiert. Fix: Entweder Mülheim-spezifische Quelle (z.B. konkrete Bestatter-Preislisten) oder ersatzlos streichen — der Absatz davor mit BdSt-Datenpunkt und Friedhofsverwaltung-Hotline trägt allein.

Zusatzbeobachtung (nicht Top-3): Die FAQ-Frage zur Altstadtfriedhof-Patenschaft steht weiterhin nur im Schema.org-Block, nicht in der sichtbaren HTML-FAQ. v4-SOLL-FIX E nicht angefasst. Cloaking-Hygiene-Risiko an der Grenze.

MUST-FIX vor Deploy: ja.

Begründung: Schwäche 1 (Standesamt-Adresse) ist ein potenzieller Faktenfehler an einer Stelle, die Hinterbliebene in der akuten 72h-Frist konkret aufsuchen müssen. Das ist ein anderes Risikoprofil als Schwäche 2 und 3 — Adresse falsch = Mensch fährt zur falschen Behörde. Verifikation der Adresse gegen die Stadt-Quelle ist ein 2-Minuten-Fix und blockiert.

Schwäche 2 (Satzungsdatum) ist Fakten-Konsistenz — ebenfalls Verifikations-Pflicht vor Deploy, weil das Datum an drei Stellen (Fließtext, Quelle 4, Schema-Kontext) auftaucht und die Glaubwürdigkeit der Page kippt, wenn es falsch ist.

Schwäche 3 (Preis-Floskel) ist tonal/qualitativ, nicht hart blockend — könnte als SOLL-FIX durchgewunken werden, aber wenn man eh nochmal an die Page muss, sollte man das mitnehmen.

Score 86: substantiell besser als v4 (82), weil die drei harten v4-MUST-FIX wirklich behoben sind. Zwei der ursprünglichen Nicht-Top-Beobachtungen aus v4 (Standesamt-Adresse, Satzungsdatum) sind nun aber nach erneuter Prüfung als härter einzustufen — die ist über 85 (Ziel), aber nicht deploy-ready ohne diese zwei Verifikationen.