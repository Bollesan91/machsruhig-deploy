# Friedhof-Übersichten — Top-50-Städte-Loop (Auftrag Bolle 24.06.2026)

> Auftrag: Friedhof-Übersicht je Stadt, Friedl V4, eigener claude.ai-Tab-Reviewer PRO Stadt, Commits gesammelt, bis 3 Städte parallel (einzeln gebaut + reviewt). Keine Rückfragen. Stopp: alle 50 ODER Bolle schreibt.
> Muster je Stadt: Stufe0 WebSearch (offizielle Stadt-Domain: Anzahl städt. Friedhöfe + EINE Gebührensatzung + Träger-Amt + 2 bedeutende) → build Übersicht (Köln-Template) → lint-site+lint-friedhof 0 FAIL → Tab-Review (KOMPAKT-Verdikt, volles Lesen) → Stufe3-Fixes → sammeln → Batch-Push → Live-Verify.
> Linkziele prüfen: /bestatter/<stadt>/ + /bestattung-in/<bl>/ müssen existieren (sonst L1-FAIL).

## NEUE PRIO (Bolle 25.06.): Islam + Überführung — geht VOR weiteren Stadt-Übersichten
Bolle-Impuls: muslimische Friedhöfe/Grabfelder fehlen komplett; Überführung ins Ausland (Türken/Ex-Jugoslawen/Afghanen) = großer unterversorgter Bedarf. Stufe-0 schon primär verifiziert (25.06.):
- **Islam-Fakten:** ~127 islamische Grabfelder in DE (meist Abteilungen AUF kommunalen Friedhöfen, nicht eigene Friedhöfe). Ältestes = Columbiadamm Berlin (Türkischer Friedhof) 1866; Hamburg-Öjendorf (seit 1978, neues Feld 2008) = zweitältestes. Sargpflicht/Tuchbestattung je Bundesland gelockert ABER widersprüchliche Sekundärquellen → je Land am Landes-Bestattungsgesetz PRIMÄR prüfen (gesetze-im-internet/Landesrecht), NICHT aus Sekundärquelle übernehmen. Ewiges Ruherecht vs. Ruhefristen = echter Konflikt. Ausrichtung Mekka, rituelle Waschung, Bestattung binnen 24h.
- **Überführung-Fakten:** Türkei Sarg-Überführung ~4.000–7.000€ (Bestatter DE + Zinksarg + Einbalsamierung + Dokumente + Flug + Empfang); Balkan per Straße günstiger; Afghanistan teurer/komplexer. Leichenpass beim Gesundheitsamt 20–120€; Konsulat des Ziellandes; internationale Sterbeurkunde. KOSTENHEBEL = Sterbekassen/Bestattungsfonds (DİTİB + türk./balkan. Vereine), Mitgliedschaft deckt Überführung günstig/kostenlos.
- FORTSCHRITT 25.06.: (a) Pillar `ueberfuehrung-ausland.html` GEBAUT + REVIEWT + GEFIXT + DEPLOY. Brutaler claude.ai-Review (Score 78) fand 1 MAJOR + 3 Minors, alle gefixt: MAJOR = DİTİB-Fonds 1.500€ gilt NUR bei Tod im Drittland (nicht DE-Bestattung); bei DE-Bestattung Transport+Beisetzung ohne Grab; Beitrag ~50€ + einmalige Eintrittsgebühr 60–500€; „nur Türkei" = nur ÜberführungsZIEL. Minors: Türkei-Kosten ab ~3.500€ statt 4.000€ + „zzgl. Grab/Beisetzung im Zielland"; sarglos „wo Kommune zulässt, kein Rechtsanspruch"; Zinksarg „i.d.R.". Abkommen/Leichenpass/Islam-Konflikt KORREKT. lint-site 169 S./0 FAIL (FAQ↔JSON-LD-Parität ok). (b) Islam-Vollständigkeit: Berlin (Columbiadamm-Card) + Hamburg („ein muslimischer") benennen Muslime SCHON → Lücke nur in später gebauten Städten (Welle 1–9). Eigener Muslim-Grabfeld-Pass nötig (Detektor-Grep + je Stadt: welches kommunale Grabfeld ist islam.), analog jüd.
- FORTSCHRITT 25.06. (b2): Pillar `islamische-bestattung.html` GEBAUT (Ablauf Ghusl/Kafan, Sarg-vs-Tuch-Rechtslage je Land, Ruhefrist-Konflikt, ~127 Grabfelder/Columbiadamm 1866, Überführungs-Querverweis, 7 FAQ) → L1-FAIL `/friedhoefe/` (kein Hub) gefixt → /berlin/ → lint-site 170 S./0 FAIL → brutaler Review LÄUFT (Tab 693). NOCH NICHT committet. Offen danach: Islam-Grabfeld-Pass für später gebaute Städte; ggf. Inlinks von bestattungsarten/bestattungskosten zu den 2 neuen Pillars.
- **Bauplan (Friedl, je eigener Review):** (1) Pillar „Überführung ins Ausland" ZUERST (Ablauf + ehrliche Kosten + Sterbekassen + Dokumenten-Checkliste). (2) Pillar „Islamische Bestattung in Deutschland" (Sargpflicht-je-Land-Tabelle primär verifiziert + Ruherecht-Konflikt + Grabfeld finden + Querverweis Pillar 1). (3) Islam-Vollständigkeit in Übersichten: Columbiadamm/Berlin + Öjendorf/Hamburg + pro Stadt islam. Grabfeld benennen (wie jüd.). Quellen Pillar 1: Auswärtiges Amt, Gesundheitsämter-Merkblätter, Konsulate, DİTİB.

## REMEDIATION (Bolle 25.06.): Welle 5–9 BRUTAL nachprüfen
KOMPAKT-Parallel-Reviewer (Welle 5–9) hatte blinden Fleck bei VOLLSTÄNDIGKEIT (fehlende Friedhöfe) + Namens-Ambiguität — Fakten hielten aber stand. Bolle-Entscheid: alle 15 mit adversarischem A/B/C-Prompt (Träger-Falle + Fehler-Pflicht + Lücken-Check) neu prüfen, fixen, neu deployen. Ab Stadt 32 generell dieser Prompt.
- [x] Wiesbaden — re-reviewt brutal: sauber, KEIN FEHLER
- [x] Mannheim — re-reviewt brutal: Fakten ok; LÜCKE jüd. Friedhof Mannheim → ergänzt (noch nicht committet)
- [x] Bonn — Nordfriedhof 22/27ha relativiert; jüd. Friedhöfe (Schwarzrheindorf 1623 + Römerstr.) ergänzt
- [x] Bielefeld — Alter Friedhof 1808/Friedhofs GmbH ergänzt (Karte); Johannisfriedhof Lage Gadderbaum korrigiert; jüd. Friedhof ergänzt
- [x] Wuppertal — „nur einer kommunal"→wenige (Ronsdorf/Schöller/Cronenberg); „drei jüdische"→VIER (Krummacherstr. 2008 aktiv)
- [x] Münster (Score 86) — Amtsname „Umwelt und" gefixt; Zentralfriedhof (kirchl.) + jüd. Einsteinstr./Hohe-Ward ergänzt
- [x] Karlsruhe (Score 80→fix) — „eingeweiht 1874"→eröffnet 1874/eingeweiht 1876; Kremat. 1903/04; jüd. orthodox+liberal (1873) ergänzt
- [x] Augsburg (Score 80→fix) — kirchl. Träger erweitert (3); jüd. Haunstetter Str. 1867 + Kriegshaber ergänzt
- [x] Mönchengladbach (85) — jüd. Friedhof Rheydt/Eifelstr. ergänzt
- [x] Gelsenkirchen (84) — jüd. Friedhof Wanner Str. 1874 ergänzt
- [x] Aachen (77) — „28"→„rund 28" (operativ 27); jüd. Friedhof Lütticher Str. 1822 ergänzt
- [x] Braunschweig (82) — jüd. Friedhöfe Hamburger Str. 1797 + Helmstedter Str. 1914 ergänzt
- [x] Kiel (83) — jüd. Friedhof Michelsenstr. 1852 + Grabfelder Alter Urnenfriedhof ergänzt
- [x] Chemnitz (80) — jüd. Friedhof Am Laubengang/Altendorf ergänzt; Städt. Friedhof = 3 Standorte/40,4 ha (statt 1×31)
- [x] Halle (84) — Krematorium Gertraudenfriedhof = privater Betreiber klargestellt; jüd. Friedhof Dessauer Str. 1929 ergänzt
- ✅ WELLE 5–9 KOMPLETT BRUTAL NACHGEPRÜFT (15/15). Scores 77–86. Hauptmuster: jüdische Friedhöfe waren überall ungenannt. Jetzt benannt.
- SYSTEMATISCHE LÜCKE entdeckt: ALLE Übersichten hatten generische „Jüdische Friedhöfe"-Zeile OHNE Namen → bei jeder Stadt die konkreten jüd. (+ wichtigen kirchl.) Friedhöfe nachtragen.
- ✅ WELLE 1–4 + ORIGINALE jüdisch-Lücke GESCHLOSSEN (25.06., Qualitäts-Nacharbeit, kein Speed-Alleingang): Detektor-Grep „getragen von der jüdischen Gemeinde, mit eigenen Vorgaben." fand 9 pur-generische + dresden (nur „einen jüdischen Friedhof") + hannover (gar keine jüd. Erwähnung). 11 Städte primär-verifiziert ergänzt (Commit fb3154d): Dortmund (Wickede 1891 + Hauptfriedhof), Essen (Segeroth 1885), Duisburg (Sternbuschweg 1882), Bochum (Wasserstr. 1918), Düsseldorf (Ulmenstr. 1877 + Nordfriedhof), Leipzig (Alter/Neuer Israelit. 1864/1928), Nürnberg (Schnieglinger Str. 1910 + Bärenschanzstr. 1864), Bremen (Deichbruchstr./Hastedt 1796), Wiesbaden (Platter Str. 1891), Dresden (Pulsnitzer Str. 1751 + Fiedlerstr. 1867), Hannover (An der Strangriede 1864 + Bothfeld 1924). München/Köln/Frankfurt/Stuttgart hatten bereits benannte jüd. Friedhöfe ✓; Bonn/Bielefeld in Welle-5-9-Remediation erledigt.
- ✅ 3-TAB-FAKTEN-REVIEW DURCH (eigene Web-Recherche je Stadt, Scores 74/~/~). 2 echte FEHLER + 3 Minors gefunden + alle selbst primär-verifiziert + gefixt: (1) **Dortmund** FEHLER — Wickede „seit 1938 Gedenkstätte" falsch (1938 zerstört, seit 1946 Gedenkstätte) + bedeutendster ist jüd. Teil Ostenfriedhof (erste Beisetzung 1885) → ersetzt; (2) **Hannover** FEHLER (Lücke) — ältester erhaltener jüd. Friedhof Norddeutschlands Oberstraße (~1550, Heine-Vorfahren) fehlte → ergänzt; (3) Bochum 1917 angelegt/1918 erste Bestattung; (4) Leipzig „geweiht 1928"→„belegt seit 1927"; (5) Bremen „Stadtteil Hastedt"→„in Hastedt" (Ortsteil v. Hemelingen). Essen/Duisburg/Düsseldorf/Nürnberg/Wiesbaden/Dresden = KORREKT. Linter grün. DEPLOY-bereit.
- STANDALONE-Kandidaten (vergessene wichtige Friedhöfe → eigene Seite + Review, Bolle 25.06.): Stadtgottesacker Halle (Renaissance-Denkmal) ★, Alter Friedhof Bielefeld (1808), jüd. Friedhof Schwarzrheindorf Bonn (ältester, 1623)
  - [x] Stadtgottesacker Halle — GEBAUT + BRUTAL REVIEWT (Score 78). 2 MAJOR gefixt: (a) „vollendet 1594"→um 1590 (Fachquellen einig, Wikipedia falsch); (b) Nickel Hoffmann NICHT dort bestattet — nur Reliefporträt über innerem Eingang, Begräbnisort unbekannt → Bestattungsbehauptung entfernt. Alle 5 prominenten Gräber (Francke/Thomasius/R.Franz/Niemeyer/Wucherer) + Lebensdaten vom Reviewer bestätigt. Linter grün. DEPLOY.
- (Essen war Welle 2/sequenziell, bonus-brutal geprüft: hielt stand)

## Status
- [x] 1 Berlin — live (Übersicht + Weißensee + Dorotheenstädtischer)
- [x] 2 Hamburg — live (Übersicht + Ohlsdorf + Öjendorf + jüd. Altona)
- [x] 3 München — live (Übersicht + Alter Südlicher Friedhof)
- [x] 4 Köln — live (Übersicht + Melaten)
- [x] 5 Frankfurt am Main — reviewt (5 MAJOR Rat-Beil/Westhausen gefixt), deploy-bereit
- [x] 6 Stuttgart — reviewt (5 MAJOR Hauptfriedhof≠Steigfriedhof gefixt), deploy-bereit
- [x] 7 Düsseldorf — reviewt (Stoffeln-MINOR gefixt), deploy-bereit
- [x] 8 Leipzig — reviewt (0 Fix)
- [x] 9 Dortmund — reviewt (5 MAJOR Westfriedhof→Südwestfriedhof gefixt)
- [x] 10 Essen — reviewt (0 Fix)
- [x] 11 Bremen — reviewt (Riensberg-Lage→Schwachhausen MINOR gefixt)
- [x] 12 Dresden — reviewt (0 Fix; SONDERFALL-Framing 4 kommunal/Mehrheit konfessionell korrekt)
- [x] 13 Hannover — reviewt (0 Fix)
- [x] 14 Nürnberg — reviewt (0 Fix; Johannis/Rochus kirchlich, Süd 62ha städtisch)
- [x] 15 Duisburg — reviewt (Sternbuschweg-Lage MAJOR→Neudorf gefixt)
- [x] 16 Bochum — reviewt (0 Fix)
- [x] 17 Wuppertal — reviewt parallel (SONDERFALL: faktisch nur 1 kommunal = Friedhof Ronsdorf/Lohsiepenstr.; „wenige"→„nur einer" gefixt)
- [x] 18 Bielefeld — reviewt parallel (Brackwede ist kirchlich→Schildesche MAJOR gefixt)
- [x] 19 Bonn — reviewt parallel (Alter Friedhof 1715 statt 1787 MAJOR gefixt)
- NEU: 3-Tab-Parallel-Review funktioniert! navigate akzeptiert tabId → 3 Reviews gleichzeitig. Ausleser: Block mit Stadt-Term+VERDIKT-Keyword (kleinster), NICHT ^N:-Regex.
- [x] 20 Münster — reviewt parallel (2 MAJOR: kein „Zentralfriedhof" + Hörster aufgelassen → 6 echte Namen: Lauheide/Wolbeck/Angelmodde/Hohe Ward/Albachten/Nienberge)
- [x] 21 Mannheim — reviewt parallel (0 MAJOR; Käfertal Nordosten MINOR)
- [x] 22 Karlsruhe — reviewt parallel (Krematorium 1903 NICHT „früheste" MAJOR gefixt; Stadtteilfriedhof-Zahl präzisiert: FBA 11, gesamt ~28)
- [x] 23 Augsburg — reviewt parallel (Protestantischer Friedhof ist kirchlich MAJOR gefixt; Westfriedhof 1874)
- [x] 24 Wiesbaden — reviewt parallel (0 Fix; Südfriedhof „über 30 ha")
- [x] 25 Mönchengladbach — reviewt parallel (0 Fix; Hauptfriedhof 49ha/Rheydt 22ha)
- [x] 26 Gelsenkirchen — reviewt parallel (Friedhof Buer = Hauptfriedhof, MAJOR → Beckhausen)
- [x] 27 Aachen — reviewt parallel (Westfriedhof NICHT größter/kein Krematorium dort, MAJOR gefixt; Krematorium auf Hüls)
- [x] 28 Braunschweig — reviewt parallel (0 Fix; SONDERFALL: Hauptfriedhof evangelisch, kommunal = Stadtfriedhof 1914 + 16 Ortsteil)
- [x] 29 Kiel — reviewt parallel (Teil-Sonderfall: Parkfriedhof Eichhof+Südfriedhof kirchlich; kirchliche „mehrere" statt 6)
- [x] 30 Chemnitz — reviewt parallel (Nikolaifriedhof ist kirchlich/ev. MAJOR umsortiert; Krematorium am Urnenhain)
- [x] 31 Halle — reviewt parallel (0 Fix; 14 kommunal, Gertraudenfriedhof 37ha, Stadtgottesacker Renaissance 1557)
- [ ] 32 Magdeburg · 33 Freiburg · 34 Krefeld · 35 Mainz · 36 Lübeck · 37 Oberhausen · 38 Erfurt · 39 Rostock · 40 Kassel · 41 Hagen · 42 Potsdam · 43 Saarbrücken · 44 Hamm · 45 Ludwigshafen · 46 Mülheim a.d.R. · 47 Oldenburg · 48 Osnabrück · 49 Leverkusen · 50 Heidelberg
  - 32 Magdeburg STUFE-0 SCHON RECHERCHIERT (24.06., primär): 16 städtische Friedhöfe, Träger = Eigenbetrieb Stadtgarten und Friedhöfe Magdeburg (LH Magdeburg), EINE gemeinsame Friedhofsgebührensatzung; Westfriedhof = Hauptfriedhof + zentrale Friedhofsverwaltung (Kapelle), dazu Südfriedhof; jüdisch: Israelitischer Friedhof Magdeburg, gegründet 1816 (Fermersleber Weg/Sudenburger Feldmark), ~2.300 Gräber/15.500 m², einer der größten Ostdeutschlands außer Berlin, klassizist. Grabmale, Träger Synagogengemeinde zu Magdeburg. → NÄCHSTER TICK: Übersicht bauen (Köln-Template), jüd. benannt, lint, eigener brutal+Score-Tab-Review.
- [x] 32 Magdeburg — REVIEWT (Score 84) + 3 Fixes: Südfriedhof 20→18ha (zweitgrößter); islam. Grabfeld Westfriedhof 2009→2004 (offizielle Stadtquelle); LÜCKE Neuer Jüd. Friedhof Königstr./Groß Ottersleben 2018 (aktive Beisetzungen) ergänzt. Träger/16/Westfriedhof 62,5ha-größter/Schoch/jüd.1816 KORREKT. lint grün.
- [x] 33 Freiburg — REVIEWT (Score 91, KEIN Kernfakt-Fehler) + 2 Fixes: islam. Grabfeld St. Georgen (nach Mekka) ergänzt; „Gebührensatzung"→„Friedhofssatzung nebst Gebührenordnung". Träger/17-8/Hauptfriedhof 1.11.1872-27ha-Brühl/Alter Friedhof denkmal/jüd.1870-900Steine KORREKT. lint grün.
- STANDING (Bolle 25.06.): 2 Städte parallel nebenbei zu Pillars, je eigener claude.ai-Reviewer, brutal A/B/C/D+Score. Islam-Grabfeld pro Stadt proaktiv mitbenennen (verifiziert).
- [x] 34 Krefeld — REVIEWT (Score 95, KEIN Fehler) + Fix: islam. Grabfeld Hauptfriedhof Heideckstr. ergänzt (KBK: nach Mekka, sarglos, Waschräume). Träger KBK AöR/11/54ha/1867/1891/jüd.1758-1938+1903 alle KORREKT. lint grün.
- [x] 35 Mainz — REVIEWT (Score 82) + 4 Fixes: „14 städt."→13 (WBM-Eigenbeleg, jüd. sind 7 separate); Waldfriedhof Mombach (26ha, GRÖSSTER, fehlte!) als Card+Liste ergänzt; islam. Grabfeld Mombach (seit 1970er, Gasilhane 2011) ergänzt; „sieben jüdische Friedhöfe" benannt. Hauptfriedhof 1803/Jeanbon/Ehrenhof + Judensand UNESCO 27.7.2021/~1700 + Neuer 1881 KORREKT. lint grün.
- [x] 36 Lübeck — REVIEWT (Score 88, kein MAJOR) + Fix: islam. Grabfeld Friedhof Waldhusen/Kücknitz ergänzt (primär verifiziert). 5 städt.+Namen/Vorwerker 53ha/Moisling größter SH alle KORREKT (Reviewer: „6" in Wikipedia ist Quellenfehler, unsere 5 stimmt). lint grün.
- [x] 37 Oberhausen — REVIEWT (Score 78) + 3 Fixes selbst primär verifiziert: griech.-orthod. Grabfeld liegt am WESTFRIEDHOF (Lirich), NICHT Nordfriedhof (muslim. Grabfeld korrekt am Nordfriedhof); Westfriedhof (35ha, größter, multikonf.) als Card ergänzt; Holten „letzte Beisetzung 1924" entfernt (Quellenkonflikt 1924/1931). Träger SBO/5/Namen/Satzung 2026 KORREKT. lint grün.
- [x] 38 Erfurt — REVIEWT (Score 74) + 4 Fixes (selbst primär verifiziert): Alter Cyriakstr.-Träger = Stadt Erfurt/Gedenkfläche (nicht Landesgemeinde); **Neuer Jüd. Friedhof 1878 = einziger aktiver Thüringens ergänzt**; islam. Grabfeld Hauptfriedhof seit 2000 ergänzt; „~70"→„zahlreiche" Steine (umstritten). Hauptfriedhof 57ha/53 Grabfelder/25 Ortsteil + UNESCO 2023 KORREKT. lint grün.
- [x] 39 Rostock — REVIEWT + 3 Fixes: Reviewer-„nur 3 Friedhöfe" WIDERLEGT (rathaus-Liste = 4: Neuer Friedhof, Westfriedhof, Neuer Friedhof Warnemünde, RuheForst — meine 4 bleibt); **aktiver jüd. Friedhof Westfriedhof 1996/2018 + muslim. Gräberfeld Westfriedhof ergänzt** (Lindenpark nur historisch). Neuer Friedhof 44ha/1912 KORREKT. lint grün.
- [x] 40 Kassel — REVIEWT (Score 84, SONDERFALL bestätigt, KEIN harter Fehler!) + Fix: islam. Grabfeld Westfriedhof (Heinrich-Schütz-Allee, seit 1986, nach Mekka, Waschraum, ~570 Bestattete) ergänzt. Keine kommunalen Friedhöfe/Ev. Stadtkirchenkreis/Hauptfriedhof Tannenheckerweg 40ha/jüd. Bettenhausen KORREKT. lint grün.
- [x] 41 Hagen — REVIEWT (Score 80) + 3 Fixes (primär verifiziert): „älterer jüd. Friedhof Delstern" FALSCH→Böhmerstraße (ab 1820, 1966 aufgelassen→Umbettung Eilpe); Waldfriedhof Loxbaum (flächengrößter, 1976) ergänzt; jüd. Elsey/Hohenlimburg ergänzt. WBH/10/Delstern 10,7ha/islam. Vorhalle+Waschhaus/jüd. Eilpe 1920 KORREKT. lint grün.
- [x] 42 Potsdam — REVIEWT + 2 Fixes (primär verifiziert): jüd. Pfingstberg „bis heute belegt"→präzisiert (noch nach Ritus möglich ABER historisch weitgehend belegt, letzte Beisetzung 2003); islam. Grabfeld Neuer Friedhof ergänzt. 15 städt./Neuer 26ha/Bornstedter Sonderfall UNESCO/Pfingstberg 1743 UNESCO 1999 KORREKT. lint grün.
- [x] 43 Saarbrücken — REVIEWT + 2 Fixes (primär verifiziert): St. Johann „1917 geschlossen"→heute wieder aktiv (Urnenfeld U9); Waldfriedhof Burbach (zweitgrößter, 1875, 28,5ha) ergänzt. 24 städt./165ha/Hauptfriedhof 61ha größter SW-DE/islam. Grabfeld 1997+Bektaschi 2013/jüd. Goldene Bremm KORREKT. lint grün.
- [x] 44 Hamm — REVIEWT (Score 90, KEIN Faktenfehler!) + 3 Ergänzungen (primär verifiziert): muslim. Grabfeld Parkfriedhof Herringen seit 1994; **Birkenallee = Deutschlands ERSTES Hindu-Grabfeld 2015** (+ größter Friedhof Hamms); „ältester"→„ältester bestehender". 12 städt./Ostenfriedhof 1.7.1800 multikonf./jüd. seit 1825 KORREKT. lint grün. (/bestatter/hamm/ fehlt → Hub.)
- [x] 45 Ludwigshafen — REVIEWT (Score 88) + 2 Fixes: „Waschräume in Trauerhalle" = unbelegt → entfernt (nur Gebetstisch); „wird erweitert" entfernt. 9 städt./Hauptfriedhof 1855/56 >10.000 größter/islam. Grabfeld nach Mekka/jüd. 1858 KORREKT. lint grün (F3 gefixt). (/bestatter/ludwigshafen/ fehlt → Hub.)
- SCORE-NACHTRAG (auf Bolle-Nachfrage komplettiert): 39 Rostock 64, 42 Potsdam 80, 43 Saarbrücken 83 (waren vorher nur als „reviewt" notiert). Volle Score-Tabelle siehe unten.
- Nächste 2: 46 Mülheim a.d.R. + 47 Oldenburg.
- [ ] 21 Mannheim
- [ ] 22 Karlsruhe
- [ ] 23 Augsburg
- [ ] 24 Wiesbaden
- [ ] 25 Mönchengladbach
- [ ] 26 Gelsenkirchen
- [ ] 27 Aachen
- [ ] 28 Braunschweig
- [ ] 29 Kiel
- [ ] 30 Chemnitz
- [ ] 31 Halle (Saale)
- [ ] 32 Magdeburg
- [ ] 33 Freiburg im Breisgau
- [ ] 34 Krefeld
- [ ] 35 Mainz
- [ ] 36 Lübeck
- [ ] 37 Oberhausen
- [ ] 38 Erfurt
- [ ] 39 Rostock
- [ ] 40 Kassel
- [ ] 41 Hagen
- [ ] 42 Potsdam
- [ ] 43 Saarbrücken
- [ ] 44 Hamm
- [ ] 45 Ludwigshafen
- [ ] 46 Mülheim an der Ruhr
- [ ] 47 Oldenburg
- [ ] 48 Osnabrück
- [ ] 49 Leverkusen
- [ ] 50 Heidelberg

## Befunde je Welle (Kurz)
- Welle 1 (FFM/S/D): Stufe0 — FFM 36 städt. (Grünflächenamt, Friedhofs-+Bestattungsgebührenordnung, Hauptfriedhof 1828 + jüd. Battonnstraße); Stuttgart 41 (Garten-/Friedhofs-/Forstamt, Gebührensatzung Stadtrecht 7/3 geänd. 05.12.2024, Pragfriedhof/Waldfriedhof); Düsseldorf 13 auf 263 ha (Garten-/Friedhofs-/Forstamt, Gebührensatzung Stadtrecht 68.203, Nordfriedhof 1884 ~70 ha/Südfriedhof).
