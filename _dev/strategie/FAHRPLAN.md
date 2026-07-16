# machsruhig — Fahrplan (Stand 13.07.2026)

> Dein eine-Seite-Überblick. Wenn du den Faden verlierst: hier reinschauen. Einfache Sprache.
> Vorversion (30.06.) ist durch den Friedhof-Re-Audit überholt — dieser Stand ersetzt sie komplett.

## Wo stehen wir — in 4 Sätzen
1. Die Website ist **gebaut und sauber** (~196 Seiten, Linter 0 FAIL); Google indexiert langsam mehr (26→45 Seiten Mitte Juni), aber **Cold-Start-Autorität bleibt DAS Engpass-Problem** — der Fix ist geliehene Glaubwürdigkeit (Institution + Fach-Reviewer), nicht mehr Content.
2. Das **Friedhofsgebühren-Daten-Asset ist jetzt echt belastbar**: Nach Fund eines systematischen Einheiten-Fehlers (Einzelstelle ≠ Einzelbelegung — „Mainz 4.714" war falsch!) wurden alle **50 Städte einzeln reviewt und 49 primär gegen die amtliche Satzung gepinnt**; die Live-Boxen sind korrigiert regeneriert (Branch, noch nicht deployed).
3. Der **Friedhof-Lotse/Index bleibt in der Schublade** bis ein institutioneller Ko-Autor steht — als Solo-Publikation zu schwach, als gemeinsame Studie der Backlink-Hebel.
4. Geld-These unverändert: **Vorsorge-Marge + Transparenz-Partner-Modell** (Lead-Zugang statt Pay-to-Rank) — wartet auf anwaltliche Prüfung, Hamburg-Pilot danach.

---

## Drei Spuren

### Spur A — wartet auf DICH (nichts erzwingen; wenn erledigt, kurz Bescheid sagen)
- [ ] **Kiel-Satzung hochladen** (5 Min): „Gebührensatzung Friedhöfe LH Kiel, 27.03.2025" aus kiel.de/Ortsrecht im Browser laden → mir geben. Automatisiert nachweislich nicht greifbar (404-Gate). Dann sind **50/50** gepinnt.
- [ ] **Deploy-Go Friedhof-Boxen** (nach Kiel + Review-Findings): Merge auf main → lastmod-Befehl → GSC-Re-Submit.
- [ ] **Anwalt** klären: (1) UWG/Prüfzeichen fürs Transparenz-Partner-Modell, (2) DSGVO spätere Nutzer-Daten, (3) §34d/Tippgeber Vorsorge, (4) Bestattungsrecht-Anwalt als benannter Fach-Reviewer.
- [ ] **Partner ansprechen** (Verbraucherzentrale/Aeternitas-Umfeld) — Exposé fertig in `PARTNER-OUTREACH.md`. Jetzt stärker: das Daten-Asset ist primär-verifiziert. Mensch-zu-Mensch, KEIN Funnel-Gimmick.
- [ ] **Über-uns** vertiefen (dein offener Punkt) · Presse-Telefonnummer.

### Spur B — Daten & Friedhof (fast fertig, wartet nur auf A-Punkte)
1. ✅ **Re-Audit komplett (09.–13.07.):** 50/50 Einzel-Review + Koordinaten-Selbstverifikation; 49/50 primär gepinnt (nur Kiel offen). Korrekturen: Mainz→2.507 (Reihengrab), Krefeld→3.450, Dortmund→2.700/25J, Hamm→1.100/800, Osnabrück-Beisetzung→100, 4× Laufzeit. Version-Staleness-Runde: 8/8 aufgelöst außer Kiel. Scope: 13 Städte mit benannten Pflicht-Zusatzgebühren.
2. ✅ **Live-Boxen regeneriert** (Branch `friedhof-lotse`): Grabtyp je Stadt statt „Einzelstelle", Pflicht-Zusatz-Zeilen, USt-Hinweise, Berlin-Sonderfall, verschärfter Caveat. Linter 0 FAIL + Smoke grün. Stufe-2-Review-Welle gelaufen (Findings → OFFENE-REVIEW-PUNKTE).
3. ⏳ **Deploy** = Spur A (Kiel + Go). Ein Befehl bumpt lastmod ehrlich (`update-sitemap-lastmod.py --apply --commit`).
4. 🗄️ **Lotse/Index geparkt** — Re-Aktivierung nur mit Ko-Autor (dann: Studie = PR-Hebel).
5. ⏳ **Studien-Publikation**: braucht Ko-Autor (A) + finale Methodik-Review. Datenbasis ist jetzt studienfest.

### Spur C — Content & Akquise (nächste Bau-Themen, brauchen weder Anwalt noch Partner)
- [ ] **Islam-Pillar + Überführung ins Ausland** (Prio seit 25.06., vor Städte 32–50): nutzt direkt die Friedhof-Daten (muslimische Grabfelder). Der inhaltlich nächste große Build.
- [ ] **Brieffunnel-Bestatter-Akquise (Idee 13.07., vielversprechend):** physischer persönlicher Brief + QR → ECHTE personalisierte Transparenz-Analyse (unser frisch verifizierter Gebühren-Datensatz als Payload) als Einstieg ins Transparenz-Partner-Programm, Hamburg-Pilot. Vorher: Ton (Chance statt Scham — Bestatter-Würde!) + UWG-Check (→ Spur A Anwalt). NICHT für Aeternitas (Institution = Beziehung, kein Funnel).
- [ ] Digitaler-Nachlass-Ratgeber + Erbschafts-Erklärinhalte (Nischen-Recherche 30.06., nachrangig).

---

## Der nächste konkrete Schritt
**Du:** Kiel-PDF (5 Min) + wenn du magst das Deploy-Go.
**Ich:** Review-Findings der Stufe-2-Welle einarbeiten → dann steht der Friedhof-Deploy schussbereit; parallel Islam-Pillar-Konzept (Spur C) anfangen.

---

## Alle Details (musst du nicht im Kopf haben)
- `_dev/docs/FRIEDHOF-MASTER-SUMMARY.md` — Re-Audit-Gesamtsicht (Korrekturen/Version/Scope je Stadt).
- `_dev/docs/FRIEDHOF-REAUDIT-STATUS.md` — Voll-Protokoll aller Batches + Pinning.
- `GAMECHANGER-AUDIT-2026-06.md` — der Befund (Trust=Backlink=ein Problem).
- `PARTNER-OUTREACH.md` — Exposé + Zielliste Ko-Autor. · `transparenz-partner-konzept.md` — Partner-Modell (v5).
- `_dev/claims/friedhofsgebuehren.json` — das Register (kanonisch, 49/50 primär-verifiziert, Audit-Trail je Stadt).
- Lektionen: `_dev/docs/LEKTIONEN-FRIEDHOF.md` (u.a. Koordinaten-Extraktion schlägt Flattened-Text; Reviewer irren in beide Richtungen) + `LEKTIONEN.md` (Windows-Temp-Cleanup frisst Klon → `git ls-files --deleted` Pflicht-Check).
