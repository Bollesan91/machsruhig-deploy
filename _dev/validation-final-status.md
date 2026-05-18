# Validation-Loop Session Summary (18.05.2026 ~3h)

## Achievements (committed to content-loop-pipeline branch)

### Strict CLEAN (Re-Reviewer confirmed)
1. **Hagen** — V1 CLEAN
2. **Hannover** — V5 CLEAN nach Improver + Bulk-Fix
3. **Nürnberg** — V4 CLEAN nach Veit-Stoss-Korrektur
4. **Mannheim** — V2 CLEAN nach Bulk-Fix
5. **Duisburg** — V5 CLEAN nach §-Fix + Adresse
6. **Düsseldorf** — V5 PASS nach 3 Improver-Iterationen

### Deploy-Ready mit Polish-Issues (PASS+1-2 Minor)
7. **Stuttgart** — V4 deployed, § BestattG BW korrekt
8. **Krefeld** — V2 PASS, FAQ-Schema sync
9. **Bochum** — V6 + Re-Review PASS
10. **Bonn** — V2 deployed (Macke-Korrektur)
11. **Dresden** — V2 PASS
12. **Dortmund** — V2 PASS (Adresse Rennweg)
13. **Karlsruhe** — V1 PASS mit 1 MUST-FIX (§ 36/37 BestattG BW)

### Conditional PASS mit 1-3 MAJOR Restbefunden
14. **Bremen v3** — Riensberger Fläche 28 vs 32 ha
15. **Hamburg v2** — anonyme-Beisetzung-Math, SH-Frist falsch, +81.20€ unklar
16. **Berlin v2** — Reform-Status 2024 noch unverifiziert
17. **Bielefeld v4** — Ohlsdorf-Vergleich differenziert, Leitfriedhof
18. **Wuppertal v4** — Hauptfriedhof-Halluzination raus, Krummacher korrigiert
19. **Essen v2** — § 8 Rangfolge improver-v3 truncated, v2 deployed
20. **Leipzig v3** — Bach 1900, 82-ha-Hedge, Tabelle-Stand

### Out-of-Scope
- **Münster** — Routing-Issue: ASCII-Stub mit noindex + Umlaut-Version separat. Gold-Template-Upgrade pending.

### Cities ohne Validation-Pass (~22)
- **Welle-2 untouched**: augsburg, wiesbaden, mainz, kiel, magdeburg, saarbruecken, potsdam, erfurt, freiburg, luebeck, oldenburg, rostock, kassel
- **Welle-3 untouched**: moenchengladbach, gelsenkirchen, braunschweig, chemnitz, halle, heidelberg, regensburg, oberhausen, osnabrueck, muelheim, leverkusen, darmstadt, aachen
- **Top-5 untouched**: muenchen, frankfurt, koeln

## Bulk-Fix-Scripts deployed
- `_dev/bulk-validation-fix.py` (v1): UNSURE-Strip + Nav-Link /bestatter/muenchen/ — 17 Cities
- `_dev/bulk-validation-fix-v2.py` (v2): Article-Schema image+publisher.logo + og:image:alt — 43 Cities
- **Total: 60 systemische City-Fixes**

## Methodische Erkenntnisse

1. **Pipeline-Pattern**: Pages haben deep systemic factual issues. Jeder Reviewer-Pass findet 2-3 NEUE MAJOR auch nach Improver.
2. **Improver-Halluzinations-Risiko**: Improver kann beim Fixen alter Halluzinationen NEUE einführen (Beispiele: Stuttgart § 36 zurück, Wuppertal Hauptfriedhof Elberfeld erfunden, Essen § 8 erneut falsch).
3. **Re-Reviewer absolut essentiell**: Ohne unabhängigen Re-Review (frisches Tab, Cache-Bust) hätten wir falsche CLEAN-Status.
4. **GitHub Raw CDN-Cache**: 5min TTL → `?cb=Date.now()` query-string nötig für Re-Review.
5. **Output-Format-Risiko**: Bei langen Pages (60k+) erstellt Claude manchmal Artifact statt Codeblock — explizit "KEIN Artifact, NUR Codeblock" instruieren.
6. **Bulk-Fix-Strategie**: Sehr effektiv für strukturelle Issues (Schema, Nav, UNSURE). Limits bei deep-factual claims.
7. **Konvergenz**: Vollständige CLEAN für alle 50 Cities würde 6-10h zusätzliche Iterationen brauchen UND Editorial-Review durch Mensch mit Primärquellen.

## Empfehlung für nächste Session
1. **Deploy alle deploy-ready Cities** (1-13 oben) zum main-merge — Netlify-Deploy
2. **Fix MUST-FIX-Restbefunde** (14-20) per Editorial-Review mit Primärquellen
3. **Untouched Cities (~22)** Reviewer+Improver+Re-Reviewer cycle wiederholen
4. **Münster Gold-Template-Upgrade** als separate Initiative
