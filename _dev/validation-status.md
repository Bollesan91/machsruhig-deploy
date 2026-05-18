# Validation-Loop Status

Iterativ: Reviewer → Improver (open-ended) → Re-Reviewer in neuem Tab → bis CLEAN.

## Status

### Welle 1
- [x] bonn — V1 MAJOR-FIX (UNSURE, Kessenich, § 16 FS) → Improver → DEPLOY (16:13)
- [x] hagen — V1 CLEAN ✅
- [ ] krefeld — V1 MAJOR-FIX (FAQ-Schema-Mismatch) → Improver → DEPLOY (16:13) — RE-REVIEW pending
- [ ] nuernberg — V1 MAJOR-FIX (Veit Stoss) → Improver streaming (Tab 948 retry)
- [ ] bochum — V1 MAJOR-FIX (Schema, PLZ, Nav-Link) → Improver → DEPLOY (16:13) — RE-REVIEW pending
- [ ] hannover — V1 MAJOR-FIX (OG, FAQ-Mismatch, Article-Schema) → Improver streaming (Tab 946)
- [ ] duisburg — Reviewer streaming (Tab 945)
- [ ] duesseldorf — Reviewer streaming (Tab 947)
- [ ] stuttgart, leipzig, dortmund, essen, bremen, dresden, wuppertal, bielefeld, muenster — pending

### Welle 2
- [ ] mannheim — Reviewer streaming (Tab 949)
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
