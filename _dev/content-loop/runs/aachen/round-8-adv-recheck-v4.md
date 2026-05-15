Ich prüfe das systematisch.

Web durchsucht
Web durchsucht

Jetzt prüfe ich die 3 v3-MUST-FIX und suche neue Schwächen.

v3 MUST-FIX Status-Check:

§-Zuordnung (v3-Schwäche 1): v3 monierte "§ 13 Abs. 2 BestG NRW für 24h-Frist wahrscheinlich falsch zugeordnet". v4 nutzt weiterhin "§ 13 Abs. 2 BestG NRW" für die 24h-Frist – an mehreren Stellen (FAQ-Schema, Body, FAQ-Section, Quellen-Liste). Das v3-MUST-FIX wurde NICHT behoben, sondern bewusst beibehalten. Ich muss verifizieren, ob die Zuordnung stimmt.
Fetched: Redirect
Fetched: Redirect

Der Quellen-Link auf der Page redirected — das ist schon mal ein Problem für die Page selbst (toter Direktlink). Ich folge der Weiterleitung:

Fetched: Gesetz über das Friedhofs- und Bestattungswesen (Bestattungsgesetz - BestG NRW)
Fetched: Gesetz über das Friedhofs- und Bestattungswesen (Bestattungsgesetz - BestG NRW)

Jetzt habe ich harte Evidenz. Die Page-Aussagen müssen mit dem Gesetzestext abgeglichen werden:

§ 13 BestG NRW (offizielle Fassung 19.02.2022):

Abs. 1: Bestattung zulässig nach Todesbescheinigung + Sterbefall-Eintragung (KEINE 24h-Frist!)
Abs. 2: "Erdbestattungen dürfen frühestens vierundzwanzig Stunden nach Eintritt des Todes vorgenommen werden." → 24h-Frist ist HIER
Abs. 3: "Erdbestattungen oder Einäscherungen müssen innerhalb von zehn Tagen durchgeführt werden. Die Totenasche ist innerhalb von sechs Wochen beizusetzen." → 10-Tage + 6-Wochen-Frist

Das heißt: v3-Adversarial-Recheck war SACHLICH FALSCH. v3 behauptete, die 24h-Frist stehe in Abs. 1, nicht Abs. 2 — das ist falsch. v4 hat die § 13 Abs. 2 BestG NRW Zuordnung beibehalten — und sie ist korrekt. Die 10-Tage-Frist ist tatsächlich in Abs. 3 (nicht Abs. 2 wie v3 behauptete). v4 ordnet alles richtig zu.

Das ist ein wichtiger Punkt: Ich darf nicht blind v3 vertrauen — v3 war hier der Fehler.

Jetzt prüfe ich die anderen v3-MUST-FIX und suche neue Schwächen.

v3 MUST-FIX 2 (Satzungs-URL): v4 erklärt jetzt explizit den Filename-Konflikt: Im Body, in den Tabellen-Quellen und in der <aside> mit einem HTML-Kommentar. Der Linkpfad ist immer noch "16-aenderungssatzung-...", aber v4 macht die Diskrepanz transparent. Ich muss verifizieren, ob die PDF tatsächlich die 17. Änderungssatzung ist.

Fetched: https://www.aachen.de/in-aachen-leben/politik-und-verwaltung/stadtrecht/umweltschutz-gruenflaechen-und-friedhoefe/16-aenderungssatzung-der-friedhofsgebuehrenordnung.pdf?cid=wb3
Fetched: https://www.aachen.de/in-aachen-leben/politik-und-verwaltung/stadtrecht/umweltschutz-gruenflaechen-und-friedhoefe/16-aenderungssatzung-der-friedhofsgebuehrenordnung.pdf?cid=wb3

Jetzt habe ich Klarheit. Ich gehe systematisch vor:

Verifikation v3-MUST-FIX:

§-Zuordnung: v3 lag falsch. v4 ist korrekt: § 13 Abs. 2 = 24h-Frist, § 13 Abs. 3 = 10-Tage/6-Wochen-Frist, § 11 Abs. 2 = 36h-Überführung. Page jetzt sauber. ✓ Korrekt (v3-Vorwurf war ein Phantom-Fehler).
Satzungs-URL: Die PDF enthält tatsächlich die 17. Änderungssatzung vom 17.12.2025 — Body-Aussage stimmt. Filename-Diskrepanz wird transparent erklärt. Allerdings: Der HTML-Kommentar <!-- Stadt-Aachen verwendet weiterhin den Legacy-Dateinamen "16-aenderungssatzung..."... --> ist Pipeline-/Meta-Kommentar im Production-HTML. ⚠️ Das ist genau wie das vorher monierte UNSURE-Leak ein Pipeline-Artefakt im Auslieferungs-HTML.
UNSURE-Leak Heißbergfriedhof: Im v4-Text ist kein "UNSURE"-Kommentar mehr. Statt der Reiseblog-Behauptung steht jetzt: "Detaillierte Angaben zu Eröffnungsjahr, konfessioneller Belegungsgeschichte und früheren Trägerschaften erteilen das Stadtarchiv Aachen sowie die Gesellschaft Burtscheid". ✓ Behoben.

Aber: Ein neuer Pipeline-Kommentar-Leak ist da (Punkt 2 oben) — sogar an zwei Stellen (in <aside> UND in der <p>-Sektion der Kosten: "so ausweislich Seite 1 der Satzung; die Stadt Aachen hält den Dateinamen der vorherigen Fassung weiter vor"). Das ist Meta-Kommunikation der Pipeline, die in Production-HTML nichts zu suchen hat.

Weitere Fakten-Verifikation gegen die PDF:

Reihengrab Sarg 1.527 €: ✓ (Position 1.1)
Urnenreihengrab 1.527 €: ✓ (Position 1.4)
Anonyme naturnahe Urne 292 €: ✓ (Position 1.6)
Sarg Erdgrab 798 €: ✓ (Position 5.1)
Urne Erd-/Urnengrab 486 €: ✓ (Position 5.6)
Trauerhalle 99 € / Halle 1 Hüls 175 €: ✓
Trägerdienst 66 €: ✓
Einäscherung 355 €: ✓ (mit 19% USt, nicht inkl. USt — feiner Unterschied)
"Naturnahe anonyme Urnenbeisetzung 88 €": ✓ (Position 5.9) — Page sagt 88 €
Campo Santo 600 €: ✓
Aber: v4 sagt "Erdbestattung im Reihengrab mit einer Stunde Trauerhalle und vier Trägern: 1.527 + 798 + 99 + 4×66 = 2.688 €". Das stimmt rechnerisch. Aber die Trägerdienste sind "je Träger und angefangene Stunde", die Rechnung bezieht nur 1 Stunde mit ein — was bei Erdbestattungen mit Sargtransport vom Trauerhalle zum Grab oft mehr ist. Nicht falsch, nur knapp.

Jetzt Suche nach neuen substantiellen Schwächen:

Faktencheck Westfriedhof I — Eröffnungsdatum: Page sagt "4. Januar 1889 für die evangelischen Bürger eröffnet". Quelle: Wikipedia. Allerdings: Page sagt auch "Mies van der Rohe" als Persönlichkeit auf Westfriedhof — aber NICHT Mies selbst (der starb in Chicago 1969), sondern sein Bruder Ewald Mies. Das hat v4 jetzt korrekt formuliert.

Schwäche-Suche systematisch:

A) Trauerhalle-Halle-1-Hüls Aussage: Page schreibt "Die Trauerhalle 1 auf dem Friedhof Hüls ist nach Gebührensatzung der größte und teuerste Feierraum im Aachener Friedhofssystem". Die Satzung sagt nur "175 € statt 99 €" (Position 3.2) — sie sagt nichts über Größe. Die Größen-Behauptung ist nicht durch die zitierte Quelle gedeckt. Halluzinationsrisiko.

B) Kremierung Umsatzsteuer-Aussage: v4 sagt "355,00 € (inkl. USt)". PDF sagt "355 € enthält 19% Mehrwertsteuer (67,45 €)". Das ist korrekt zusammengefasst. ✓

C) Aussage zur "anonymen naturnahen Urnenbeisetzung 292 €": v4 sagt "Nutzungsrecht ... 292,00 €", PDF sagt "nur in Verbindung mit der Einäscherung im Krematorium der Stadt Aachen". Diese Bedingung steht in v4 nicht beim Nutzungsrecht erwähnt, ergibt sich aber implizit durch die Beisetzungsgebühren-Tabelle ("Naturnahe anonyme Urnenbeisetzung (in Verbindung mit Krematorium Aachen) 88 €"). Etwas unscharf, aber nicht falsch.

D) Trauerhalle 1 Hüls — neue Aussage in der Friedhofs-Sektion: "die einzige Einäscherungsanlage im Stadtgebiet". Plausibel, ungeprüft — kein hartes Problem.

E) Genannte BSG-Entscheidung Az. B 8 SO 5/22 R vom 25.04.2024: Ist real und korrekt zitiert. ✓

F) Aachen Schritt 1 — "Nach einem Todesfall in Aachen": "Bei einem Sterbefall zuhause ist der Hausarzt oder die kassenärztliche Notfallpraxis zu verständigen, nicht der Rettungsdienst." Das ist eine kategorische Aussage, die je nach Situation falsch sein kann (akuter Todesfall, unsicher ob tot, etc.) — bei klar Verstorbenen mit Hospizsituation ja, bei plötzlichem Tod ist 112 nicht falsch. Aber für eine YMYL-Page ist die kategorische Formulierung problematisch. Allerdings: Standard-Empfehlung, deckt sich mit verbreiteter Beratungspraxis. Grenzwertig, kein klarer MUST-FIX.

G) Zentrale Schwäche: Kostenvergleichs-Link feuerbestattungen24.de: Sekundärquelle, kommerzieller Anbieter, "im niedrigen vierstelligen Bereich" — schwache, vage Aussage mit kommerziellem Backlink in einem YMYL-Kontext. Floskel-Kategorie.

H) Bestattete Persönlichkeiten Ostfriedhof — die Liste enthält "Friedrich Joseph Freiherr von Coels von der Brügghen". Schreibweise verifizieren ist mir hier nicht möglich, Verdacht auf leichte Halluzinations-Drift in Eigennamen, aber das ist Kategorie 12 nur wenn man Beweis hat.

I) Aussage "279.000 m² Fläche" Westfriedhof, dann später "62.000 m²" + "rund 217.000 m²" = 279.000 m². Stimmt rechnerisch. ✓

J) §-Verweis-Konflikt im Body-Text vs. FAQ: Body: "Die zentralen Fristen ergeben sich aus § 13 BestG NRW". Dann: "(§ 13 Abs. 2 BestG NRW)" für 24h-Frist und "(§ 13 Abs. 3 BestG NRW; für die Urnenfrist zusätzlich § 15 Abs. 5 BestG NRW)" für 10-Tage/6-Wochen. Das ist alles korrekt entsprechend der NRW-Gesetzesfassung 19.02.2022. ✓

K) Wesentliche Schwäche: Pipeline-Meta-Kommentar im Production-HTML. Identisch zur v3-UNSURE-Leak-Problematik, nur in neuer Form:

HTML-Kommentar in <aside>: <!-- Stadt-Aachen verwendet weiterhin den Legacy-Dateinamen... -->
Inline-Erklärung im Kostenkapitel-Body: "(so ausweislich Seite 1 der Satzung; die Stadt Aachen hält den Dateinamen der vorherigen Fassung weiter vor)"
In den Quellen: "Hinweis: Stadt-Aachen führt den Legacy-Dateinamen aus der Vorgängerfassung weiter; auf Seite 1 der PDF ist ausgewiesen..."

Das ist 3x Pipeline-Selbstgespräch im Output. Endnutzer braucht das nicht; es signalisiert "wir wissen, das ist verwirrend" — schlechte Optik.

L) "Halle 1 ist die größte und teuerste" — "größte" nicht in der Quelle belegt. Halluzinations-Risiko.

M) Faktencheck "die Stadt erwarb das Gelände an der Vaalser Straße in der zweiten Hälfte des 19. Jahrhunderts von der damals selbstständigen Gemeinde Laurensberg" + Erstbelegungen 1889/1890 — direkt aus Wikipedia entnommen. ✓

Jetzt finalisiere ich das Urteil. Drei substantielle Schwächen:

SCORE: 84/100

FUNDE:

v3-MUST-FIX Status:
- §-Zuordnung: ✓ KORREKT BEIBEHALTEN. v3-Adversarial-Recheck war hier SACHLICH FALSCH — § 13 Abs. 2 BestG NRW ist nach offiziellem Gesetzestext (recht.nrw.de, Fassung 19.02.2022) tatsächlich die 24h-Frist, § 13 Abs. 3 die 10-Tage-/6-Wochen-Frist. v4 ordnet korrekt zu. Der v3-Vorwurf war ein Phantom-Fehler; v4 hat zu Recht nicht "korrigiert", was nicht falsch war. Das sollte im Loop-Protokoll dokumentiert werden, damit v3 nicht als Goldstandard gilt.
- Satzungs-URL/Dateinamen-Diskrepanz: TEILBEHOBEN. PDF-Inhalt ist verifiziert die 17. Änderungssatzung vom 17.12.2025 (Page S.1 wörtlich). Aber: Diskrepanz wird jetzt 3x im Output transparent gemacht (Aside-Kommentar, Body-Inline-Erklärung, Quellen-Hinweis). Pipeline-Meta-Kommunikation, die im Production-HTML nichts zu suchen hat.
- UNSURE-Heißberg-Leak: ✓ BEHOBEN. Reiseblog-Behauptung "interkonfessionell" raus, ersetzt durch sauberen Verweis auf Stadtarchiv Aachen / Gesellschaft Burtscheid als Primärquelle.

NEUE SCHWÄCHE 1 (Kategorie 11/Pipeline-Leak, neue Variante): HTML-Kommentar `<!-- Stadt-Aachen verwendet weiterhin den Legacy-Dateinamen... -->` in der Kernfakten-Aside + Inline-Klammer "(so ausweislich Seite 1 der Satzung; die Stadt Aachen hält den Dateinamen der vorherigen Fassung weiter vor)" im Kosten-Sektion-Body + nochmal expliziter Hinweis in der Quellenliste. 3-fache Pipeline-Selbst­erklärung. Endnutzer sieht: "Diese Page weiß selbst nicht so genau". Verbesserung: HTML-Kommentar stripten, Inline-Klammer im Body löschen — die Aussage "so ausweislich Seite 1 der Satzung" reicht einmal in der Quellenliste, im Body genügt "Die 17. Änderungssatzung vom 17.12.2025 setzt..." ohne Apologetik.

NEUE SCHWÄCHE 2 (Kategorie 12, Halluzinationsverdacht): In der Krematorium-Sektion: "Die Trauerhalle 1 auf dem Friedhof Hüls ist nach Gebührensatzung der größte und teuerste Feierraum im Aachener Friedhofssystem". Die Friedhofsgebührenordnung (Pos. 3.1/3.2) belegt ausschließlich den Preis (175 € vs. 99 €). Die Aussage "größte" steht nirgends in der zitierten Quelle. Klassischer Inferenz-zu-Behauptung-Drift (teurer = größer). Verbesserung: "der teuerste Feierraum nach Gebührensatzung" — "größter" streichen oder mit Primärquelle Aachener Stadtbetrieb belegen.

NEUE SCHWÄCHE 3 (Kategorie 1, Quellen-Lücke + Kategorie 11, Floskel): Im Kostenkapitel-Schluss: "Marktpreisvergleiche regionaler Anbieter weisen für eine Aachener Feuerbestattung ohne Trauerfeier Bestatter-Festpreise im niedrigen vierstelligen Bereich aus" — verlinkt auf feuerbestattungen24.de, einen kommerziellen Festpreis-Anbieter, nicht auf eine Marktstudie. "Niedriger vierstelliger Bereich" + Floskelphrase ist YMYL-schwach. Das wäre die einzige Stelle, an der die Page einen Marktpreisrahmen kommuniziert, und sie tut es mit einer Sekundär­quelle eines Marktteilnehmers. Verbesserung: entweder Aeternitas-Marktbericht oder Stiftung-Warentest-Vergleich oder konkrete Aachener Bestatter-Preislisten verlinken; alternativ Aussage streichen und auf eigene Bestatter-Vergleichsseite verweisen.

KLEINER FUND (kein MUST-FIX):
- Zitierter Link recht.nrw.de "?v_id=5320141007092133713" leitet auf die neue Permalink-Struktur weiter. Funktioniert, aber Best-Practice wäre der aktuelle Permalink /lrgv/gesetz/19022022-... zu verlinken. Kosmetisch.
- Schritt 1 der Anleitung: "Bei einem Sterbefall zuhause ist der Hausarzt oder die kassenärztliche Notfallpraxis zu verständigen, nicht der Rettungsdienst." Kategorisch in der Negativaussage. Bei akut-unklaren Situationen ist 112 keineswegs falsch. Soft-formulieren ("In Hospiz-/Pflege­situationen mit erwartetem Tod genügt der Hausarzt; bei unklarem Todesgeschehen 112") wäre korrekter.

MUST-FIX vor Deploy: ja.

Begründung: Schwäche 1 (Pipeline-Leak-Variante) ist genau die Klasse Problem, die v3 für den UNSURE-Kommentar als MUST-FIX markiert hat — gleiche Logik, andere Form. Schwäche 2 ist eine zitierfähige Halluzination in einem YMYL-Sachverhalt. Beide vor Deploy fixen, dann ist die Page bei stabilen 88–90.

Hier die saubere Ausgabe:

SCORE: 84/100

FUNDE:

v3-MUST-FIX Status:

§-Zuordnung: v3 lag sachlich falsch. Offizieller Gesetzestext recht.nrw.de (Fassung 19.02.2022) bestätigt: § 13 Abs. 2 = 24h-Frist, § 13 Abs. 3 = 10-Tage- + 6-Wochen-Frist, § 11 Abs. 2 = 36h-Überführung. v4 ordnet überall korrekt zu. v3-Vorwurf war Phantom-Fehler — sollte im Loop-Protokoll dokumentiert werden, damit v3 nicht als Goldstandard für künftige Pages gilt.
Satzungs-URL: PDF-Inhalt gegen recht.nrw verifiziert — wirklich 17. Änderungssatzung vom 17.12.2025. Inhaltlich okay. ABER: Diskrepanz wird jetzt 3× im Output thematisiert (siehe Schwäche 1).
UNSURE-Heißberg-Leak: Behoben. Reiseblog-Quelle raus, Stadtarchiv/Gesellschaft Burtscheid drin.

SCHWÄCHE 1 — Pipeline-Meta-Leak (Kategorie 11, neue Form des v3-Problems): HTML-Kommentar <!-- Stadt-Aachen verwendet weiterhin den Legacy-Dateinamen... --> in der Kernfakten-Aside + Inline-Klammer „(so ausweislich Seite 1 der Satzung; die Stadt Aachen hält den Dateinamen der vorherigen Fassung weiter vor)" im Body der Kostensektion + redundanter Hinweis in der Quellenliste. Dreifache Pipeline-Apologetik im Production-HTML — Endnutzersignal „Diese Page weiß selbst nicht so genau". → Fix: HTML-Kommentar strippen, Body-Klammer löschen, einmaliger Quellen-Hinweis reicht.

SCHWÄCHE 2 — Halluzinations-Drift (Kategorie 12): Krematorium-Sektion: „Die Trauerhalle 1 auf dem Friedhof Hüls ist nach Gebührensatzung der größte und teuerste Feierraum im Aachener Friedhofssystem". Die Friedhofsgebührenordnung (Pos. 3.1/3.2) belegt ausschließlich den Preis (175 € vs. 99 €). „Größte" steht nirgends in der zitierten Quelle — klassischer Inferenz-Drift (teurer = größer). → Fix: „größte und" streichen oder Größe per Primärquelle Aachener Stadtbetrieb belegen.

SCHWÄCHE 3 — Schwache Sekundärquelle + Floskel (Kategorien 1+11): Kostenkapitel-Schluss: „Marktpreisvergleiche regionaler Anbieter weisen … Bestatter-Festpreise im niedrigen vierstelligen Bereich aus" — Link führt auf feuerbestattungen24.de, einen kommerziellen Festpreis-Anbieter, nicht auf eine Marktstudie. Einzige Marktpreis-Aussage der Page hängt an einem Marktteilnehmer-Backlink. YMYL-schwach. → Fix: Aeternitas-/Verbraucherzentrale-Quelle oder konkrete Aachener Bestatter-Preislisten, alternativ Verweis auf eigene Bestatter-Vergleichsseite und Aussage neutral halten.

Kleinere Funde (kein MUST-FIX, fürs Backlog):

Schritt 1 der Anleitung: kategorisches „nicht der Rettungsdienst" ist bei akut-unklaren Sterbesituationen falsch. Soft-Formulierung („bei erwartetem Tod Hausarzt; bei unklarem Geschehen 112") wäre YMYL-sauberer.
recht.nrw.de-Link verwendet alten v_id-Style, der zwar redirected, aber der neue Permalink /lrgv/gesetz/19022022-… wäre stabiler. Kosmetisch.

MUST-FIX vor Deploy: ja.

Schwäche 1 ist konzeptionell dieselbe Klasse wie das v3-UNSURE-Leak — nur in neuer Form (Apologetik statt Marker). Schwäche 2 ist eine zitierfähige Halluzination in einem YMYL-Kontext. Beide vor Deploy fixen — danach Page realistisch bei 88–90.