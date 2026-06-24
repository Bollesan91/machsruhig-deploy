# Friedhof-Übersichten — Top-50-Städte-Loop (Auftrag Bolle 24.06.2026)

> Auftrag: Friedhof-Übersicht je Stadt, Friedl V4, eigener claude.ai-Tab-Reviewer PRO Stadt, Commits gesammelt, bis 3 Städte parallel (einzeln gebaut + reviewt). Keine Rückfragen. Stopp: alle 50 ODER Bolle schreibt.
> Muster je Stadt: Stufe0 WebSearch (offizielle Stadt-Domain: Anzahl städt. Friedhöfe + EINE Gebührensatzung + Träger-Amt + 2 bedeutende) → build Übersicht (Köln-Template) → lint-site+lint-friedhof 0 FAIL → Tab-Review (KOMPAKT-Verdikt, volles Lesen) → Stufe3-Fixes → sammeln → Batch-Push → Live-Verify.
> Linkziele prüfen: /bestatter/<stadt>/ + /bestattung-in/<bl>/ müssen existieren (sonst L1-FAIL).

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
- [~] 11 Bremen — gebaut (13 städt./Umweltbetrieb/Osterholz 1920), Review offen
- [~] 12 Dresden — gebaut (SONDERFALL: nur 4 kommunale/Eigenbetrieb, Mehrheit konfessionell; Heidefriedhof+Johannisfriedhof), Review offen
- [~] 13 Hannover — Stufe0 fertig (19 städt., Fachbereich Umwelt+Stadtgrün, 5 Stadtfriedhöfe: Engesohde 1864/Lahe/Ricklingen 1908/Seelhorst/Stöcken 1891), Build offen
- [ ] 14 Nürnberg
- [ ] 15 Duisburg
- [ ] 16 Bochum
- [ ] 17 Wuppertal
- [ ] 18 Bielefeld
- [ ] 19 Bonn
- [ ] 20 Münster
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
