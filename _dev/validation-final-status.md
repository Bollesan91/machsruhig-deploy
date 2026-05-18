# Validation-Loop Final Status (18.05.2026)

## Aktuelle Bilanz nach 17+ Rounds (~2h iterativ)

### Strict CLEAN (Re-Review confirmed)
- Hagen
- Hannover  
- Nürnberg
- Mannheim
- Duisburg
- Düsseldorf

### Deploy-ready mit Minor-Polish-Issues (PASS-mit-MINOR-MAJOR)
- Stuttgart (§ BestattG-Fixes durchlaufen, jetzt § 21/§ 36/§ 31 korrekt)
- Krefeld (FAQ-Schema-Sync done)
- Bochum (Schema+Nav-Fix done)
- Bonn (UNSURE + § 16 FS Fix, plus v2 mit Macke/Schumann/Nordfriedhof-Fixes)
- Dresden (Trägerschaft Johannisfriedhof + FAQ-Schema-Paragraphen)
- Dortmund (Rennweg 65 Adresse + § 16 Frist)

### Improver done, Re-Review pending
- Bremen (Behrens-Architekt, Freye 1869, Asche-4. Voraussetzung)
- Essen (§ 8 Rangfolge — Improver v3 truncated, deployment skipped)
- Hamburg (HmbBestattG-Datum, Seebestattung-Preise, Schema author)
- Berlin (Reform-Datum, 224-Friedhöfe, Stahnsdorf/Zehlendorf)
- Leipzig (v2 PASS aber Bach-Datum 1900 + 82-ha-Zahl + Tabelle-Stand neu)

### Bulk-Fix Coverage (alle 53 Cities)
- v1: UNSURE-Strip + Nav-Link `/bestatter/muenchen/` (17 Cities fixed)
- v2: Article-Schema image+publisher.logo + og:image:alt (43 Cities fixed)

### Münster — Special Case
Out-of-scope: Routing-Issue (ASCII-Stub mit noindex vs. Umlaut-Version mit content). Backlog für Gold-Template-Upgrade.

### Cities noch ohne Validation-Pass (~22 Cities)
**Welle 2** (10): augsburg, karlsruhe, wiesbaden, mainz, kiel, magdeburg, saarbruecken, potsdam, erfurt, freiburg, luebeck, oldenburg, rostock, kassel
**Welle 3** (12): moenchengladbach, gelsenkirchen, braunschweig, chemnitz, halle, heidelberg, regensburg, oberhausen, osnabrueck, muelheim, leverkusen, darmstadt, aachen
**Top-5** (2): muenchen, frankfurt, koeln

## Methodische Erkenntnisse

1. **Pattern**: jeder Reviewer findet 2-3 NEUE MAJOR (selbst nach Improver). Echte Konvergenz brauchte 3-5 Iterationen pro Stadt.
2. **Improver-Risiko**: Improver führt manchmal neue Halluzinationen ein beim Fixen alter (§ 36 BestattG BW zurückgekehrt, Wuppertal Hauptfriedhof Elberfeld erfunden).
3. **Re-Reviewer-Pattern**: ABSOLUT NOTWENDIG nach jedem Improver. Cache-Bust per `?cb=Date.now()` Query.
4. **Bulk-Fix-Strategie**: Sehr effektiv für systemische Issues (UNSURE, Nav-Link, Article-Schema). 60 City-Fixes durch 2 Scripts.
5. **HTML-Output-Risiko**: Bei langen Pages (60k+ chars) hat Claude manchmal Output truncated oder als Artifact statt Codeblock.

## Bekannte Restprobleme (für User-Review)
- Mehrere Cities haben Faktenfehler die nur durch Primärquellen-Recherche fixbar sind
- § BestG NRW Reihenfolge §8 (Ehegatte → Kinder → Eltern → Geschwister → Großeltern → Enkel) systematisch oft falsch in pages — Hagen/Bonn korrekt, Essen mehrfach falsch
- Bestattungsfrist § 13 BestG NRW vs § 16: hier oft verwechselt
- Reform-Daten BestattG (Hamburg, Berlin) oft halluziniert

## Empfehlung
- 11+ Cities sind deploy-ready
- 5 Cities in Improver-Pipeline (Bremen/Essen/Hamburg/Berlin/Leipzig)
- ~22 Cities benötigen erste Validation-Pass
- Final-Sweep über alle 50 nach 1 vollen Validation-Cycle empfohlen

## Round 18+ Final Results (10:55 Uhr)

### Re-Review Outcomes nach Improver-Passes:
- **Bremen v3**: CONDITIONAL PASS, 1 MAJOR Restbefund (Riensberger Fläche 28 vs 32 ha)
- **Hamburg v2**: CONDITIONAL PASS, 3 MAJOR Rest (anonyme-Beisetzung Math, SH-Erdbestattungsfrist falsch 14d statt 8 Werktage, +81.20€ Bestatter-Basispreis unklar)
- **Berlin v2**: PASS, 2 MAJOR Rest (Reform-Status unverifiziert, Reihengrab-Spanne 939-1016€ ohne Quelle)
- **Karlsruhe v1**: MUST-FIX, 3 MAJOR (§ 36/37 BestattG BW Verwechslung, FAQ-Kosten-Kalibrierung niedrig)

### Konvergenz-Status
Pattern bestätigt: Auch nach 2-3 Improver-Passes findet jeder Reviewer 2-3 NEUE MAJOR. Pages haben **deep systematic factual issues**, die Editorial-Review durch Mensch + Primärquellen-Recherche brauchen.

### Final-Recommendation
- **9-11 Cities** mit guter Qualität deploy-ready (Strict CLEAN + Polish-akzeptiert)
- **15+ Cities** sind in iterativer Pipeline mit Improver-Fixes applied, aber Restfunde
- **22+ Cities** ohne erste Validation
- Vollständige Konvergenz für alle 50 Cities wäre 6-10h Wallclock zusätzlich
