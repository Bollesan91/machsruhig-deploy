# Session-Notizen

## Letzte Session
**Datum:** 29.05.2026

## Was wurde gemacht

### Iter-15 — Tool-Score-Audit + Phase A+B-Fixes (7 Tools)
- **Phase A Sofort-Fixes** auf 5 Tools nach Helper-V3-Audit:
  - Checkliste-Todesfall: § 1944 BGB als Pflicht-Task in "Monat 1"
  - Notfallkarte: Privacy-Claim (3x) + 112/eGK-Banner
  - Fristen-Radar: Auslandsbezug-Checkbox + § 1944 III + Disclaimer + Titel ehrlich
  - Beerdigungsplaner: Datenschutz präzisiert + Framing ehrlich + Scope-Banner
  - Danksagung: Slash entfernt + ß-Orthografie + Closing-Doppelung + Format-Tipp

- **Phase B Engineering** auf 4 Tools:
  - Notfallkarte: maxlength + Char-Counter + Overflow-Detection mit Warn-Banner
  - Trauerrede: length-Feature (kurz/mittel/lang wirklich wirksam) + hobbies + humorvoll-Guard
  - Abschiedsbrief: Closing-Select + Sender + Datum + Schema-Sync
  - Beerdigungsplaner: localStorage-Persist + Skip-Button + Resume-Banner + Print

- **Konsistenz-Sweeps**:
  - Iter-15c: Privacy-Claims auf 5 weiteren Tools angeglichen (Vorsorge-Check, Kostenrechner, Bestattungskosten-Rechner, Angebotsprüfer, Checkliste)
  - Iter-15d: Fristen-Radar 4 weitere Stellen + Trauerrede Step-5 Privacy
  - A11y: role/aria-live auf 5 Warn-Banner

### Re-Audit-Cycle 1 (gegen SHA c5f56ab)
- 7 parallele Chrome-MCP Audits: Notfallkarte/Fristen-Radar/Beerdigung/Danksagung/Checkliste/Trauerrede/Abschiedsbrief
- Median **78** (vs 64 pre-Iter-15)
- Größte Sprünge: Beerdigungsplaner +28, Trauerrede +25, Abschiedsbrief +18

### Iter-16+16b — Restbefund-Sofort-Fixes
- Beerdigungsplaner value-Property aus track() (Datenschutz-Bug live)
- Trauerrede `${formData.name}`-Literal-Bug in JSX
- Trauerrede "kurz" verdichtet hobbies statt droppen
- Fristen-Radar resolveDeadline + § 193 BGB + taxReturnDeadline (datumsbasiert)
- Abschiedsbrief Plural-Anrede + Praktisches-Header + Entwurf-löschen-Button
- Notfallkarte overflow:hidden → overflow:visible + min-height + Allergien rot
- Danksagung Kindstod-Sensitivity-Hint + VEID-Verweis
- Checkliste Sonderfälle Ausland erweitert + Selbstständig + Erbengemeinschaft

### Iter-17 — Tools auf 90+ (tiefe Engineering)
- Trauerrede tone-guard auch an relationship=kind
- Beerdigungsplaner Gesamtkostenrahmen + Budget-Konflikt-Warnung
- Notfallkarte eGK-Link + Blutgruppen-Disclaimer
- Fristen-Radar ICS-Kalender-Export (VEVENT + VALARM)
- Abschiedsbrief createdAt-State statt heute
- Checkliste Auslandsbezug-Toggle + Tax-Date § 149 AO
- Danksagung Sensitivity-Pfad Partner/Geschwister/Freund

### Re-Audit-Cycle 2 (gegen SHA 6ee65ff)
- Scores: Notfallkarte 82, Fristen-Radar 76, Beerdigungsplaner 64, Danksagung 79, Checkliste 81, Trauerrede 67, Abschiedsbrief 77
- Median 79, Reviewer-Noise ±10 sichtbar (jeder fresh chat findet andere Defekte)

### Iter-18 — Konkrete MUST-FIX
- Fristen-Radar **toter Auslands-Code repariert** (Object.assign in filter griff nicht) — zentralisiert in resolveDeadline mit cfg-Parameter
- Beerdigungsplaner **Gesamtkosten-Aggregation parst jetzt auch o.desc** (Blumen/Musik hatten kein kosten-Feld) + Trauerkaffee × Gäste
- Trauerrede **Fragment-Output weg** + **Religion via unshift statt push** (4 Religionen × 3 Tonebenen) + **quote-Feld verdrahtet** als eigenes quoteFavorite-Segment + **falsche Zitate korrigiert** (Tagore-Schmetterling entfernt, Konfuzius-Zwei-Leben als "Volksweisheit" markiert)
- Notfallkarte maxlength auf alle Felder (60/50/25) + Stand-Datum (MM/YY) auf Karte

### Iter-19 — Critique-driven Refinements
- Danksagung Beziehungen umstrukturiert: Geschwister/Großeltern aufgesplittet in Schwester/Bruder + Großmutter/Großvater (Possessive grammatikalisch korrekt)
- Danksagung Family-Closings differenziert: Kind → "die Eltern", Geschwister → "die Geschwister"
- Checkliste 48h-Pauschal entschärft + Quellen-Hinweis
- Notfallkarte Rückseiten-Overflow-Detection einzelfeld-genau

## Stand
- **Branch `iter-15-audit-fixes` deployed** → Merge in main beim "ende deploy"
- SHA `01b5b84`
- 11 Tools alle privacy-konsistent + a11y-annotiert
- Median Re-Audit-2: 78 (vs 64 pre-Iter-15) — Reviewer-Noise begrenzt weitere Score-Steigerung

## Nächste Schritte
- Nach Netlify-Build: Live-Smoke-Test auf machsruhig.de/tools/...
- Bei Bedarf Iter-20: weitere strukturelle Themen (CSR-Bundle, BL-Quellenprüfung, Consent-Layer für Analytics)
- Strategische Entscheidung Stadt vs Long-Tail-Pillar bleibt offen

## Offene Fragen
- Reviewer-Noise: Tools schwanken ±10 je Audit. Echte Mittelwerte erst nach 3-5 Audit-Cycles + Aggregation aussagekräftig.
- Beerdigungsplaner Lead-Form-Bestatter-Rückruf in Datenschutzerklärung gedeckt? (außerhalb Tool prüfen)
- Abschiedsbrief @babel/standalone-CSR-Risiko Mobil — Precompile-Setup nötig?
