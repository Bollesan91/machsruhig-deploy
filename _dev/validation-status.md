# Validation-Loop Status

Iterativ: Reviewer → Improver (open-ended) → Re-Reviewer in neuem Tab → bis CLEAN.

## Status

### Welle 1
- [x] bonn — V1 MAJOR-FIX (UNSURE, Kessenich, § 16 FS) → Improver → DEPLOY (16:13)
- [x] hagen — V1 CLEAN ✅
- [ ] krefeld — V1 MAJOR-FIX (FAQ-Schema-Mismatch) → Improver → DEPLOY (16:13) — RE-REVIEW pending
- [x] nuernberg — V2 CLEAN ✅ (nach Improver+Bulk)
- [ ] bochum — V1 MAJOR-FIX (Schema, PLZ, Nav-Link) → Improver → DEPLOY (16:13) — RE-REVIEW pending
- [x] hannover — V2 CLEAN ✅ (nach Improver+Bulk)
- [ ] duisburg — Reviewer streaming (Tab 945)
- [ ] duesseldorf — Reviewer streaming (Tab 947)
- [ ] stuttgart, leipzig, dortmund, essen, bremen, dresden, wuppertal, bielefeld, muenster — pending

### Welle 2
- [x] mannheim — V2 CLEAN ✅ (nach Improver+Bulk)
- [ ] karlsruhe, augsburg, wiesbaden, mainz, kiel, magdeburg, saarbruecken, potsdam, erfurt, freiburg, luebeck, oldenburg, rostock, kassel — pending

### Welle 3
- [ ] moenchengladbach, gelsenkirchen, braunschweig, chemnitz, halle, heidelberg, regensburg, oberhausen, osnabrueck, muelheim, leverkusen, darmstadt, aachen — pending

### Top-5
- [ ] muenchen, frankfurt, berlin, hamburg, koeln — pending

## Systemische Findings (für Bulk-Fix-Final-Pass)
- Generisches OG-Image `/assets/og-image.png` statt city-spezifisch — sehr verbreitet
- FAQ-Schema vs HTML-Mismatch (Krefeld 1 Satz fehlte, Hannover 7 vs 6 Fragen)
- Article-Schema ohne `image` + `publisher.logo` ImageObject
- Nav-Link `/bestatter/muenchen/` auf NRW-/anderen Stadt-Pages
- UNSURE-Kommentare aus Pipeline noch im Production-HTML (Bonn hatte 4)

## Bulk-Fix-Run (18.05.2026)

✅ Script `_dev/bulk-validation-fix.py` lief auf allen 53 bestatter/-Cities:
- 15 Cities: Nav-Link /bestatter/muenchen/ → /bestatter/ (augsburg, berlin, bielefeld, frankfurt, hamburg, karlsruhe, koeln, leipzig, luebeck, mannheim, moenchengladbach, muenster, nuernberg, stuttgart, wuppertal)
- 3 Cities: UNSURE-Kommentare entfernt (münster, rostock, wuppertal)

Diese 2 systemischen Issues sind ab jetzt zentral gefixt — Reviewer flaggt sie nicht mehr.

Verbleibende systemische Findings für mögliche zukünftige Bulk-Fix-Runden:
- Article-Schema ohne `image` + `publisher.logo` (mehrere Cities, JSON-Parsing nötig)
- FAQ-Schema vs HTML-Mismatch (per-city analysis nötig)
- Generic OG-Image-Default (würde neue Asset-Files erfordern)

## Münster Special Case (18.05.2026 R10)
2 Verzeichnisse: bestatter/münster/ (proper, 57k, no noindex) vs bestatter/muenster/ (ASCII stub, 21k, noindex)
Re-Reviewer fetched ASCII-Stub. Routing-Issue separat. Aus Validation-Loop genommen.
