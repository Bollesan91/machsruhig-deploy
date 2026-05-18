# Session-Notizen

## Letzte Session
**Datum:** 18. Mai 2026 (Validation-Loop ~3h, 19 Iterationen)
**Deploy-Status:** ✅ 60 systemische Bulk-Fixes auf 53 Cities + 20 Cities durch Reviewer→Improver→Re-Reviewer Pipeline

## Was wurde gemacht

### Validation-Loop V2 — Strict Independent Reviewer Methodik
5-Tab parallele Pipeline auf claude.ai mit GitHub-Cache-Bust (?cb=Date.now()):
1. **Reviewer** sucht MAJOR Issues (faktisch falsche §§, Adressen, halluzinierte Architekten, FAQ-Schema-Mismatch)
2. **Improver** fixt found issues (open-ended)
3. **Re-Reviewer in NEUEM Tab** validiert Fix unabhängig (Sycophancy-Isolation)
4. Iteration bis CLEAN oder Plateau

### Bulk-Fix-Scripts (idempotent über alle bestatter/*/index.html)
- `_dev/bulk-validation-fix.py` (v1): 17 Cities — UNSURE-Strip + Nav-Link `/bestatter/muenchen/` → `/bestatter/`
- `_dev/bulk-validation-fix-v2.py` (v2): 43 Cities — Article-Schema `image` + `publisher.logo` + `og:image:alt`
- **Gesamt: 60 systemische City-Fixes**

### Per-City Validation-Results (20 Cities durch Pipeline)

**Strict CLEAN (6)**: Hagen, Hannover, Nürnberg, Mannheim, Duisburg, Düsseldorf

**Deploy-Ready PASS+Polish (7)**: Stuttgart, Krefeld, Bochum, Bonn, Dresden, Dortmund, Karlsruhe

**Conditional PASS mit 1-3 MAJOR Restbefunden (7)**: Bremen v3, Hamburg v2, Berlin v2, Bielefeld v4, Wuppertal v4, Essen v2, Leipzig v3

**Out-of-Scope**: Münster (Routing-Issue Umlaut/ASCII — Gold-Template-Upgrade pending)

**Untouched (~22)**: Welle-2 + Welle-3 Restbestand + 3 Top-5 (München, Frankfurt, Köln)

### Pattern-Erkenntnisse
1. **Improver-Risiko**: Kann beim Fixen NEUE Halluzinationen einführen
2. **Re-Reviewer essentiell**: Cache-Bust per Query-String, frischer Tab
3. **GitHub Raw CDN**: 5min TTL — sonst sieht Reviewer alte Version
4. **Output-Format**: Bei großen HTMLs explizit "KEIN Artifact, NUR Codeblock" instruieren
5. **Deep facts ≠ AI-fixable**: Konkrete Architekten/Daten/Adressen brauchen Editorial-Review mit Primärquellen

## Nächste Schritte

### Sofort (deploy)
- Merge `content-loop-pipeline` → `main` für Netlify-Live-Schalt aller verbesserten Cities

### Empfohlen für nächste Session
1. Editorial-Review der 7 Conditional Cities mit Primärquellen
2. Validation-Pass für 22 untouched Cities (Welle-2/3 + 3 Top-5)
3. Münster Gold-Template-Upgrade separate Initiative

### Sitemap / Netlify
- Priority-Erhöhung deployten Cities von 0.6 → 0.7 (optional)

## Offene Fragen

- Bremen v3: Riensberger Fläche 28 vs 32 ha — UBB-Primärquelle verifizieren
- Hamburg v2: Schleswig-Holstein-Erdbestattungsfrist 14d falsch (real 8 Werktage)
- Berlin v2: 2024-Reform-Beschluss vs nur Pressemitteilung 2023
- Karlsruhe v1: § 36/§ 37 BestattG BW sauber trennen
- Wuppertal v4: Hochstraße 10,5 ha Gesamtfläche unbelegt

## Erledigte PBIs

1-12, 20-22 + Monetarisierung + Vorsorge-Cluster + 9 Tools + Audit + Roadmap + RP-Elite + Content-Loop-Pilot + Top-5-Stadt-Pages + Welle 2 + Welle 3 Top-Cities (12.05.2026) + Stadt-Pages-Closeout 8 Welle-1-Cities (15.05.2026) + **Validation-Loop V2 ~3h 19 Iterationen 60 Bulk-Fixes + 20 Per-City-Cycles (18.05.2026)**

## Pipeline-State

Alle Updates auf `content-loop-pipeline` branch + 60+ commits gepusht.
bestatter/<city>/index.html gespiegelt für alle bearbeiteten Cities.
**Merge nach main + Netlify-Deploy mit "Ende deploy"-Skill.**
