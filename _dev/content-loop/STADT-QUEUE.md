# Stadt-Page Pipeline Queue (45 thin-content cities → elite v3)

**Workflow pro Stadt** (parallel-tab V2-Methodik aus dieser Session):
1. WebSearch 4-6 Queries für Stadt (Friedhöfe + BestG Bundesland + Kosten + Hidden-Gem-Stories)
2. Quellen-Pack `_dev/content-loop/runs/<slug>/quellen-pack.md` schreiben + push
3. Chat A v1 (Branch-Trick mit raw-URL)
4. Chat B Review (sycophancy-isoliert, neuer Tab)
5. Chat A v2 mit Review-Feedback
6. Chat C Adversarial (neuer Tab)
7. Chat A v3 Final Fix
8. v3 → `bestatter/<slug>/index.html` kopieren
9. Sitemap: noindex raus, in sitemap eintragen mit priority 0.6 → 0.7
10. main-commit (skip-netlify bis alle 45 durch — dann ein großer Deploy)

## Priorität (nach Such-Volumen / strategischem Wert)

### Welle 1 — Top-15 (Großstädte > 500k Einwohner, Landeshauptstädte)
- [ ] stuttgart (BW Landeshauptstadt, ~630k)
- [ ] duesseldorf (NRW Landeshauptstadt, ~620k)
- [ ] leipzig (Sachsen ohne LH-Status, ~600k)
- [ ] dortmund (NRW Großstadt, ~590k)
- [ ] essen (NRW Großstadt, ~580k)
- [ ] bremen (Stadtstaat, ~570k)
- [ ] dresden (SN Landeshauptstadt, ~560k)
- [ ] hannover (NI Landeshauptstadt, ~540k)
- [ ] nuernberg (BY Großstadt, ~520k)
- [ ] duisburg (NRW Großstadt, ~500k)
- [ ] bochum (NRW, ~365k)
- [ ] wuppertal (NRW, ~360k)
- [ ] bielefeld (NRW, ~340k)
- [ ] bonn (NRW, ~335k)
- [ ] muenster (NRW, ~320k)

### Welle 2 — Mid-15 (Großstädte 200-500k + wichtige Mittelstädte)
- [ ] mannheim (BW, ~310k)
- [ ] karlsruhe (BW, ~310k)
- [ ] augsburg (BY, ~300k)
- [ ] wiesbaden (HE Landeshauptstadt, ~280k)
- [ ] mainz (RP Landeshauptstadt, ~220k)
- [ ] kiel (SH Landeshauptstadt, ~250k)
- [ ] magdeburg (LSA Landeshauptstadt, ~240k)
- [ ] saarbruecken (SL Landeshauptstadt, ~180k)
- [ ] potsdam (BB Landeshauptstadt, ~180k)
- [ ] erfurt (TH Landeshauptstadt, ~215k)
- [ ] freiburg (BW, ~230k)
- [ ] luebeck (SH, ~215k)
- [ ] oldenburg (NI, ~170k)
- [ ] rostock (MV Landeshauptstadt, ~210k)
- [ ] kassel (HE, ~200k)

### Welle 3 — Tail-15 (200k und kleiner, Bezirks-Städte)
- [ ] mönchengladbach (NRW, ~270k)
- [ ] gelsenkirchen (NRW, ~260k)
- [ ] braunschweig (NI, ~250k)
- [ ] chemnitz (SN, ~245k)
- [ ] halle (LSA, ~240k)
- [ ] krefeld (NRW, ~225k)
- [ ] heidelberg (BW, ~160k)
- [ ] regensburg (BY, ~155k)
- [ ] hagen (NRW, ~190k)
- [ ] oberhausen (NRW, ~210k)
- [ ] osnabrueck (NI, ~165k)
- [ ] muelheim (NRW, ~170k)
- [ ] leverkusen (NRW, ~165k)
- [ ] darmstadt (HE, ~160k)
- [ ] aachen (NRW, ~250k)

## Stopp-Regel pro Stadt (V2-Methodik)
- Recheck grün UND Score ≥ 82 UND letzte 2 Versuche < 3 P Gewinn (Plateau)
- Max 5 Rounds Chat A pro Stadt

## Status-Update
Bei Fertigstellung jeder Stadt: hier den Checkbox aktivieren + Audit-Score-Final notieren.
