# FRIEDL — Helfer für Friedhofseiten (Skalen-Qualitätssystem)

> Kurzname für „Helfer V4.1 Friedhof". Schwester zu `_dev/HELPER-V4.1.md`; bei Konflikt gilt für Friedhofseiten **Friedl**.
> Zweck: tausende Friedhof-/Träger-Datensätze unter EINHEITLICHEN Kriterien bauen & aktuell halten.
> **Kernumkehr:** Qualität sitzt im **strukturierten Datensatz + Provenienz**, nicht in der Prosa. Seiten werden generiert. Geprüft wird der **Datensatz gegen die Primär-Satzung**. Konsistenz erzwingen Generator + Linter, nicht die Hand.

## Marktreife-Status (ehrlich)
- **Solide / einsetzbar:** das Gate-Gerüst (Stufen 0–3, die 4 Challenge-Dimensionen), Provenienz-Pflicht, Substanz-Gate, Datensatz-Review + Stichprobe.
- **Jetzt ergänzt (war v1-Lücke):** Beschaffungs-Pipeline (Stufe −1), Gebühren-Bündelung pro **Träger**, Standalone = Ausnahme + Aggregationsseiten, §-5-UrhG-Klarstellung, Träger-Typ-Quellenmatrix, konkrete Near-Duplicate-Metrik, Charge-Definition.
- **Weiterhin offen (eigener Design-Schritt vor Vollserie):** das **Aktualitäts-Monitoring** (zuverlässig Satzungs-Änderungen erkennen) — bislang nur Q1-Sweep + Verfall-Logik; eine robuste Change-Detection fehlt noch. **Nicht in Vollserie gehen, bevor das steht.**

---

## Die vier Challenge-Dimensionen

| Dimension | Was bei Skala schiefgeht | Gate |
|---|---|---|
| **Konsistenz** | Seiten driften (Spalten, Vokabular, Disclaimer); Stadt/BL/Geo widersprüchlich | Generierung aus 1 Template + Enums; Linter erzwingt Struktur + Cross-Field |
| **Tiefe** | Thin-/Doorway-Pages; tausend Near-Duplicates → Massen-Deindexierung | Substanz-Gate + Near-Duplicate-Gate; sonst Aggregationszeile statt eigener URL |
| **Recht** | Falsche Gebühr (YMYL/Haftung), falsche Ruhezeit/Fassung, kopierte fremde DB | Provenienz-Pflicht; Ruhezeit aus Satzung∩BestattG; nur amtliche/eigene Quellen |
| **Aktualität** | Satzungen ändern jährlich; veraltete Gebühr = aktiv falsch; bei 1000+ existenziell | Sichtbarer Stand + Gültig-ab; Re-Check-Kadenz; Verfall-Logik; (Monitoring offen) |

---

## Stufe −1 — Beschaffung & Abgrenzung (NEU, der Factory-Eingang)

1. **Discovery der Friedhöfe:** Grundgesamtheit aus **OpenStreetMap / Wikidata** (`amenity=grave_yard`/`landuse=cemetery`, Wikidata `Q39614`) — eigene Erhebung, frei nutzbar; **nie** fremde Verzeichnisse abgreifen (§ 87a UrhG). Liefert Name, Geo, Ort, oft Träger-Hinweis.
2. **Träger-Auflösung:** jedem Friedhof seinen **Träger** zuordnen (Kommune/AöR/Kirchengemeinde/privat). Ein Träger hat **eine** Gebührensatzung für i. d. R. **alle** seine Friedhöfe.
3. **Gebühren-Einheit = Träger-Satzung, nicht Friedhof.** Satzung **einmal pro Träger** ziehen, verifizieren, sichern → alle Friedhöfe dieses Trägers referenzieren denselben Satzungs-Record. (Reduziert Arbeit + Fehlerfläche massiv.)
4. **Standalone-Entscheidung VOR dem Bau (Substanz-Gate, s. Stufe 1):** Die meisten der ~32.000 werden **keine** eigene Seite, sondern eine **Zeile in einer Träger-/Landkreis-Aggregationsseite** (`/friedhoefe/<bundesland>/<kreis|ort>/`). Eigene URL nur für substanzstarke Friedhöfe. Standalone = Ausnahme.
5. **Charge-Einheit:** eine Charge = **ein Träger** (oder ein Landkreis) — Bezugsgröße für Stichprobe, Sign-off, Re-Check.

---

## Der Datensatz (zwei verknüpfte Records)

**A) Träger-Satzungs-Record (trägt die Gebühren, geteilt):**
`traeger_id`, `traeger_name`, `traeger_typ` (Enum: kommunal | AöR | kirchlich-ev | kirchlich-kath | jüdisch | privat | genossenschaftlich), `satzung_titel`, `gueltig_ab`, `quelle_url`, `quelle_typ` (Enum: primaer_satzung | amtsblatt | traeger_website | landesrecht | sekundaer-NUR-discovery), `abruf_datum`, `roh_gesichert` (Pfad), `gebuehren[]` = `{grabart, posten (Grabnutzung|Beisetzung|Trauerhalle|Sonstige), betrag, einheit (je Jahr|je Ruhezeit|pauschal|je m²), tarifstelle}`, `ruhezeit{grabart→jahre}`, `verifiziert_von`, `letzte_pruefung`.

**B) Friedhof-Record (Identität/Substanz, referenziert A):**
`friedhof_id`, `name`, `traeger_id`→A, `typ` (Park|Wald/Ruhewald|Haupt|Stadtteil|konfessionell|historisch), `strasse`,`plz`,`ort`,`bundesland`,`geo`, `osm_id`/`wikidata_id`, `grabarten[]` (kanonisches Enum), `hektar`,`gruendungsjahr`,`grabstellen`/`bestattungen` (wenn belegt), `merkmale[]`, `oeffnungszeiten`,`oepnv`,`verwaltung_kontakt`, `substanz_score`, `standalone` (bool), `reifegrad` (vollständig|teil|datenlücke), `letzte_pruefung`.

---

## Stufe 0 — verhindern (je Träger-Satzung; bei Gebühren/Recht nicht delegierbar)

1. `_dev/docs/LEKTIONEN-FRIEDHOF.md` + `OFFENE-REVIEW-PUNKTE-FRIEDHOF.md` lesen.
2. **Geltende Gebührensatzung als Primärquelle** ziehen, lokal sichern (`_dev/strategie/friedhoefe/<traeger>-gbo-<jahr>-raw.txt`). PDF garbled? → lokal extrahieren (pdfplumber/pdftotext), WebFetch-„unlesbar"-Urteil nicht glauben.
3. **Fassung verifizieren** (Lektion #54): Gültig-ab + Az./Jahr; jährliche Novellen. Zahl gilt nur bei geltender Fassung.
4. **Ruhezeit:** die **Friedhofssatzung des Trägers** setzt den operativen Wert, der das **Mindestmaß des Landes-BestattG** respektieren muss → maßgeblich ist der Satzungswert (≥ Landes-Minimum). Nicht „längere gilt" pauschal.
5. **Quellen-Recht (Vorteil nutzen):** kommunale Gebührensatzungen sind **amtliche Werke (§ 5 UrhG) = gemeinfrei** → Gebühren dürfen 1:1 wiedergegeben werden. **Aber** fremde *Verzeichnis-Zusammenstellungen* bleiben tabu (§ 87a). Kirchliche/private Ordnungen: nicht zwingend gemeinfrei → wörtliche Tabellen sparsam, Fakten + Quellenlink statt Volltext-Kopie.
6. **Datenlücke ehrlich:** Satzung nicht beschaffbar → keine Schätzung. Record `datenlücke`; Seite zeigt „Gebühren beim Träger erfragen" + Kontakt; fällt durchs Substanz-Gate.

---

## Stufe 1 — deterministische Gates (`lint-friedhof.py`, 0 FAIL Pflicht)

- **Substanz-Gate (Tiefe):** Standalone nur bei **≥3 belegten Grabart-Gebühren** (aus dem Träger-Record) **und/oder ≥5 einzigartigen Eigenfakten** des Friedhofs. Sonst → Aggregationszeile, keine eigene URL.
- **Near-Duplicate-Gate (Tiefe/Konsistenz) — konkrete Metrik:** Seite in (Template-Boilerplate) vs. (eindeutige Felder/Fakten/Gebühren) zerlegen; **`unique_tokens / total_tokens ≥ 0,40`** UND **max. 3-Shingle-Jaccard zu jeder Schwesterseite < 0,80**. Darüber → Boilerplate, nicht bauen.
- **Provenienz-Pflicht (Recht):** jede Gebühr/jeder Rechts-Claim → `quelle_url` + `gueltig_ab` + `abruf_datum`. Fehlt → FAIL. Zahl ohne Quelle = FAIL.
- **Aktualitäts-Gate (Aktualität):** `gueltig_ab`-Jahr ≥ Jahr−1 ODER expliziter „geprüft am"-Stempel; `letzte_pruefung` > 12 Mon → WARN, > 18 Mon → FAIL (Verfall-Logik).
- **Arithmetik-Cross-Check (Recht/Konsistenz):** jede Beispielsumme = Σ ihrer belegten Posten (assert). Ruhezeit×Jahresgebühr + Beisetzung + Trauerhalle = ausgewiesene Spanne.
- **Vokabular/Enum + Cross-Field:** Enums geprüft; Ruhezeit ∈ BL-gültige Werte; `bundesland`↔`ort`↔`geo` konsistent; Friedhof→Träger-Referenz existiert.
- **Struktur:** identische Abschnittsfolge/Spalten/Disclaimer (generiert); JSON-LD `Cemetery` valide (ASCII-Quotes); Links + Trailing-Slash kanonisch; Sitemap nur Standalone-Seiten.
- **CTA (dezent, Pflicht):** jede Friedhofseite trägt nach dem Gebühren-Abschnitt einen zurückhaltenden CTA-Block → **Kostenrechner** (primär) + **Angebotsprüfer** (sekundär; speist die Echtangebot-Datenschicht B). Ton hilfreich, nicht werblich (YMYL/Trauer).

> Was der Linter fängt, ist kein Reviewer-Thema. Asserts VOR dem Write.

---

## Stufe 2 — Datensatz-Review + Stichprobe (skaliert)

1. **Datensatz-Review statt Seiten-Review:** target-blinder claude.ai-Tab (Bolle-Device) bekommt **Träger-Record + gesicherte Satzung** und prüft mit Verifikations-Verben: „rechne Beispielsumme nach", „steht Gebühr X in Tarifstelle Y der Satzung?", „ist `gueltig_ab` die geltende Fassung?", „Ruhezeit BL-konform?". Zitatpflicht, MAJOR/MINOR/UNSICHER, kein Score.
2. **Risiko-gewichtete Stichprobe je Charge (=Träger/Kreis):** 1 **Goldstandard je Träger-Typ** vollständig; **10 % Zufall**; **alle Linter-Grenzfälle**. **Stichprobenquote IMMER loggen** (kein Silent-Cap).
3. **Falsifikations-Subagenten (read-only)** für Skalen-Fakten-Checks erlaubt (memory-Carve-out): Record vs. Primärquelle, nur falsifizieren, keine Edits, kein Bewerten (vgl. Lektion #50). Rewrite/Bewerten bleibt Tab/Mensch.
4. WebFetch nie gate-entscheidend.

---

## Stufe 3 — Gate

- **Fertig je Träger-Record** = Linter grün + Provenienz vollständig + Beispielsumme nachgerechnet + (falls Stichprobe/Gold) Review 0 MAJOR.
- **Fertig je Charge** = Stichprobe 0 MAJOR + Aktualitäts-Gate grün + Stichprobenquote dokumentiert + **Sitemap-URL-Diff** (Lektion #46: entfernte URLs = Alarm; lastmod aus Git).
- Findings selbst gegen Primärquelle prüfen (Reviewer irrt beidseitig). Satzungs-Update → **Diff-Re-Check** der geänderten Felder, keine Vollrunde.

---

## Aktualitäts-/Wartungsschicht

- **Sichtbar je Seite:** „Gebühren nach [Satzung], gültig ab [Datum] · von machsruhig geprüft am [Datum]." (Stand = Wahrheits-Claim, nie blind bumpen — Lektion #51.)
- **Kadenz:** Q1-Sweep je Träger (viele Satzungen z. 1.1.); Re-Verifikation vor 12-Monats-WARN.
- **Verfall-Logik** (Lektion #43: Siegel ohne Abgleich = Fassade): Stand > 18 Mon + nicht re-verifiziert → Seite zeigt „Gebühren werden aktualisiert — beim Träger gegenprüfen" statt veralteter Zahlen.
- **OFFEN (vor Vollserie lösen):** robuste **Change-Detection** je Träger-Satzung (PDF-Hash ist brüchig, Pfade wandern). Optionen zu evaluieren: Gültig-ab-Scrape der Satzungs-Indexseite, jährliches Re-Fetch + Inhalts-Diff, Amtsblatt-Watch. Bis dahin: konservativer Q1-Sweep + Verfall-Logik.

---

## Träger-Typ-Quellenmatrix

| Träger-Typ | Gebührenquelle | Rechtsbasis Ruhezeit | Quellen-Recht |
|---|---|---|---|
| kommunal / AöR | kommunale Gebührensatzung (Amtsblatt) | Friedhofssatzung ∩ Landes-BestattG | § 5 UrhG gemeinfrei → 1:1 ok |
| kirchlich (ev/kath) | kirchliche Friedhofs-/Gebührenordnung | kirchl. Ordnung ∩ Landes-BestattG | nicht zwingend gemeinfrei → Fakten + Link, sparsam zitieren |
| jüdisch | Gemeinde-Ordnung | religiöse Vorgaben + Landes-BestattG | wie kirchlich; besondere Sensibilität |
| privat / genossenschaftlich | Preisliste/AGB des Betreibers | Vertrag ∩ Landes-BestattG | urheberrechtlich geschützt → nur Fakten + Quelle |

---

## Datenschicht B: Bestatter-Verzeichnis (Umkreis)

> Zweite Datenschicht neben Friedhof/Gebühren (A): pro Friedhof eine faktische Liste der Bestatter im Umkreis. **Ein kopiertes Verzeichnis ist kein Moat und § 87a-rechtswidrig — wir erheben selbst.**
>
> **Qualität vor Menge — KEIN Auto-Publish.** Reine Sammelskripte produzieren flachen, ungenauen, schwer prüfbaren Datenmüll (Projektlehre Bolle). Das Skript darf nur **erheben + rechnen** (Discovery via OSM, Distanz, Dedup) und einen **Kandidaten**-Satz erzeugen. **Veröffentlicht wird ausschließlich, was einzeln verifiziert ist** (aktiv? Adresse korrekt? real?). Lieber **8 geprüfte** Bestatter als 30 ungeprüfte. Erst wenn die Pro-Record-Qualität + der Prüfaufwand an EINEM Friedhof (Ohlsdorf) bewiesen sind, skalieren — sonst nicht.

**Bestatter-Record:** `bestatter_id`, `name`, `strasse`,`plz`,`ort`,`geo`, `website`, `telefon`, `quelle` (Enum: osm | eigene_recherche | partner-selbstauskunft), `osm_id`, `status` (Enum: aktiv | geschlossen | umgezogen | ungeprüft), `geprueft_am`, `geprueft_via` (google | website | telefon | -). Zuordnung: `{friedhof_id, bestatter_id, distanz_km}` — **distanz_km rechnen wir selbst** (Haversine aus Koordinaten), nie aus fremder Quelle.

**Stufe −1/0 — Erhebung:**
1. **Primär OSM** (`shop=funeral_directors` / `office=funeral_directors`) per Overpass-Radius um die Friedhofs-Koordinaten. Lizenz **ODbL** → speicher-/anzeigbar **mit Nennung „Daten © OpenStreetMap-Mitwirkende"**.
2. **Distanz selbst rechnen. Fremde Verzeichnisse** (bestattungsatlas o. ä.) **nur als Abdeckungs-Gegenprobe** („hat OSM jemanden übersehen?") — NIE als Quelle (§ 87a; ihre Zuordnung + km sind geschützt).
3. **Aktiv-Status verifizieren** per Google/Website/Telefon — zum *Prüfen*, **nicht Google-Daten speichern** (Places-ToS verbietet Speicherung/Anzeige über place_id hinaus). Nur unser Feld `status` + `geprueft_am`.
4. **Anreichern** der „nur Name"-Records (OSM ~⅓) über die eigene Website/Impressum des Bestatters (primär für Adresse/Inhaber).

**Stufe 1 — Gates (lint-friedhof.py erweitern):**
- **Provenienz:** jeder Record `quelle`; bei Anzeige zusätzlich `status` + `geprueft_am`; **ODbL-Attribution** auf jeder Seite mit OSM-Bestattern → sonst FAIL.
- **Aktualität:** nur `status=aktiv` wird *angezeigt*; `ungeprüft`/`geschlossen` nie publik. `geprueft_am` > 12 Mon → Re-Check (Bestatter schließen/ziehen um — gleiche Staleness wie Satzungen).
- **Neutralität (Recht/Firewall):** Reihenfolge **nach Distanz** (oder alphabetisch), **kein Ranking, keine Wertung, keine bezahlte Platzierung** (Listing bleibt gratis — vgl. Geschäftsmodell-Firewall). Keine „Empfehlung"-Sprache.
- **Distanz-Eigenrechnung:** `distanz_km` muss aus `geo` ableitbar sein (Cross-Check), nicht fremdübernommen.
- **Cap + Logging:** „nächste N" (Vorschlag 6–8) bzw. Radius geloggt (Stadt enger, Land weiter) — kein stiller Cap.

**Stufe 2/3:** Stichprobe Aktiv-Status gegen Realität (Google/Website); „geschlossen" raus; Distanz-Stichprobe nachgerechnet.

**Veröffentlichung — Block „Bestatter im Umkreis":** rein **faktisch** (Name, Ort, unsere km, Website-Link), **„automatisch erhoben, ohne Wertung oder Empfehlung"**, sichtbarer **Stand + „Fehler melden"**, **ODbL-Nennung**. Natürlicher Haken: wer transparent auftreten will → **Transparenz-Partner** (Brücke zur Strategie). Erst nach Aktiv-Prüfung anzeigen.

---

## Anti-Patterns

**A (Friedhof):** 1. Thin-/Doorway-Pages → Aggregationszeile. 2. Sekundär-Zahlen als Beleg. 3. Erfundene/interpolierte Gebühren. 4. Fremde Verzeichnis-DB kopieren (§ 87a). 5. Boilerplate-Near-Duplicate. 6. Veraltete Satzung als gültig. 7. „geprüft"-/Siegel-Optik (wir geben amtliche Gebühren wieder, wir bewerten den Friedhof nicht).
**B (Bestatter):** 8. Google-Places-Daten speichern/anzeigen (ToS). 9. Bestatter-Liste mit Ranking/Wertung/bezahlter Platzierung (Neutralität/Firewall). 10. Geschlossene/ungeprüfte Bestatter anzeigen. 11. Fremde km/Zuordnung übernehmen statt selbst rechnen. 12. ODbL-Nennung weglassen.

## Gedächtnis
`_dev/docs/LEKTIONEN-FRIEDHOF.md` (Muster je Träger-Typ/BL: Satzungs-Fundorte, Wahl- vs. Reihengrab, Jahres- vs. Ruhezeit-Gebühr) · `OFFENE-REVIEW-PUNKTE-FRIEDHOF.md` · Mechanisierbares → `lint-friedhof.py`. Beide Docs Pflichtteil jedes Bau-/Review-Prompts.

## Definition of Done — je Friedhof/Träger
- [ ] **Recht:** jede Gebühr aus Primär-Satzung (Tarifstelle + Gültig-ab + Abruf + Rohquelle); Fassung geltend; Ruhezeit = Satzung ≥ Landes-Minimum.
- [ ] **Tiefe:** Substanz-Gate + Near-Duplicate-Gate bestanden.
- [ ] **Konsistenz:** Enums/Struktur/Arithmetik/Cross-Field grün; JSON-LD valide.
- [ ] **Aktualität:** Stand + Gültig-ab sichtbar; `letzte_pruefung` < 12 Mon; in Q1-Sweep.
- [ ] Linter 0 FAIL · (Stichprobe/Gold) Review 0 MAJOR · Beispielsumme nachgerechnet · Sitemap-Diff ok.

## Definition of Done — Bestatter-Verzeichnis (Datenschicht B)
- [ ] **Recht:** OSM-Quelle (ODbL) + Nennung „Daten © OpenStreetMap-Mitwirkende"; keine fremde DB (§ 87a); keine Google-Daten gespeichert; km selbst gerechnet.
- [ ] **Qualität:** jeder ANGEZEIGTE Bestatter einzeln verifiziert (`status=aktiv`, Adresse geprüft); ungeprüfte/geschlossene nicht publik; kein Auto-Publish.
- [ ] **Neutralität:** Sortierung nach Distanz/alphabetisch, kein Ranking/Wertung/bezahlte Platzierung; „ohne Wertung"-Hinweis + „Fehler melden" + Stand sichtbar.
- [ ] **Bewährt vor Skalierung:** Pro-Record-Qualität an Ohlsdorf nachgewiesen.

> Schwellen (vor Serienstart fixieren): Substanz 3 Grabarten ODER 5 Fakten · Aktualität WARN 12 / FAIL 18 Mon · Stichprobe 10 % + Gold je Träger-Typ + alle Grenzfälle · Near-Duplicate unique≥0,40 & Shingle-Jaccard<0,80.
