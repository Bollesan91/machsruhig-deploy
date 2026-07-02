# Rollout Phase 2 — Gap-Analyse & MVP-Specs (Stand 19.06.2026)

> Ergebnis der Ist-Stand-Erfassung (Phase 1) + Gap-Analyse. Bau-Mandat erteilt (Loop, V4.1).
> Übergeordnetes Konzept: `transparenz-partner-konzept.md` (v5) · STRATEGIE.md Abschnitt 15.

## A. 7↔15-Schema-Brücke (Fundament-Entscheidung)
Standard (15 Posten) = Erhebungs-Granularität (was Bestatter ausweisen). Modell (7 Komponenten,
`/methodik#kostenmodell`) = Vergleichs-Granularität (was Rechner/Prüfer normalisieren).
Deterministischer Rollup:
- 1 Grundleistung + 2 Überführung + 3 Versorgung + 7 Formalitäten → **Bestatterleistungen** (Pflicht)
- 4 Sarg → **Sarg** (Pflicht) · 8 Krematorium → **Einäscherung + 2. Leichenschau** (Pflicht Feuer)
- 5 Urne → **Urne** (Pflicht Feuer) · 9 Friedhofsgebühren + 10 Grabnutzung → **Friedhofsgebühren**
  (Durchlauf) · Beisetzung → **Beisetzung** (Pflicht)
- 6 Trauerfeier + 11 Grabstein + 12 Deko/Blumen → außerhalb Kern-7 (= Modell-Baseline „ohne
  Grabpflege/Grabmal") = **Optional** · 13 Fremdleistungen → Drittkosten-Sammel (**Durchlauf**)
- 14 USt-Status + 15 Stand-Datum → Meta
Pflicht/Optional/Durchlauf des Standards = exakt die von den Kriterien geforderte Trennung; mappt
1:1 aufs bestehende Modell → Single-Source bleibt (Lektion #43).

## B. Flächendeckende Änderungen (Konsistenz, priorisiert)
- **P1** `fuer-bestatter.html` auf v5 heben (Selbstverpflichtung, Leitsatz, „Zugang nicht Rang",
  Links zu Kriterien + Standard). [inhaltlich → Reviewer]
- **P1** Interne Anbindung „Für Bestatter": Footer-Eintrag + Links aus Stadt-/BL-/Kostenseiten
  (nur 3× verlinkt). [strukturell → Linter+Self+Live-Grep, angekündigt]
- **P1** `was-muss-im-kostenvoranschlag-stehen.html` ↔ `angebotsstandard.html` verknüpfen.
- **P2** `methodik.html#kostenmodell` 7↔15-Brücke als Hinweis + Verweis.
- **P2** Angebotsprüfer-Cluster → Kriterien/Standard verlinken.
- **P3** Terminologie-Sweep (drei kanonische Namen).

## C. Neu-Entwicklung (MVP, Bau-Reihenfolge)
1. **`angebotsstandard.html`** (TRUST/INFO, CTA 1–2, statisch) — 15-Posten-Spec als `mr-cost-table`
   + Erklär-Sektionen + maschinenlesbares JSON-Schema + Redaktion/Quellen/Disclaimer + Crosslinks.
2. **`transparenz-kriterien.html`** (TRUST, CTA 1) — Vergabeprozess · binäre Kriterien · prominent
   „Was NICHT geprüft wird" · Aktualisierung/Entzug · Grenzen · Finanzierung · Beschwerde.
   **Selbstverpflichtung, kein „geprüft/Siegel" bis Anwaltsprüfung.**
3. **`fuer-bestatter.html`** = Partner-werden (Upgrade, siehe B-P1).
4. **Transparenzprofil-Template** `bestatter/[stadt]/[name]/` — GATED bis Hamburg-Pilot-Daten.

## Rollout-Sequenz & Gating
① Standard → B-P1 Anbindung + fuer-bestatter-Upgrade → ② Kriterien → (Hamburg-Pilot) → ④ Profile
→ Radar. **Lead-Aktivierung bleibt Phase F + Anwaltsprüfung.** „Erst der Brunnen, dann die Wasserhähne."

## Stopp-Kriterium des Bau-Loops
MVP ① + B-P1 + ② gebaut/live (Gate je Seite: 0 MAJOR + Linter + Smoke). Profile/Radar gated.
Stopp zusätzlich bei echt harten (Bolle-)Entscheidungen.
