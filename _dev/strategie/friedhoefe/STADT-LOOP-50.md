# Friedhof-Übersichten — Top-50-Städte-Loop (Auftrag Bolle 24.06.2026)

> Auftrag: Friedhof-Übersicht je Stadt, Friedl V4, eigener claude.ai-Tab-Reviewer PRO Stadt, Commits gesammelt, bis 3 Städte parallel (einzeln gebaut + reviewt). Keine Rückfragen. Stopp: alle 50 ODER Bolle schreibt.
> Muster je Stadt: Stufe0 WebSearch (offizielle Stadt-Domain: Anzahl städt. Friedhöfe + EINE Gebührensatzung + Träger-Amt + 2 bedeutende) → build Übersicht (Köln-Template) → lint-site+lint-friedhof 0 FAIL → Tab-Review (KOMPAKT-Verdikt, volles Lesen) → Stufe3-Fixes → sammeln → Batch-Push → Live-Verify.
> Linkziele prüfen: /bestatter/<stadt>/ + /bestattung-in/<bl>/ müssen existieren (sonst L1-FAIL).

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
