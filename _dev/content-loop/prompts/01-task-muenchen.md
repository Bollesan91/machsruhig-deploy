# Round 1 — München WRITE-Task (in Chat A) · Stadt-Page-Variante

Du schreibst jetzt die **erste komplette HTML-Version** der Münchner Stadt-Page.

---

## Target-Pfad

`bestatter/muenchen/index.html`

---

## Niveau-Anker (LAYOUT-Quelle, mr-Klassen, Schema-Set)

Fetche die Hessen-BL-Page als Layout-Vorbild — sie nutzt alle Standard-mr-Klassen, das Standard-Schema-Set, die Standard-Sektions-Reihenfolge:

**LAYOUT-URL:**
```
https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/hessen/v5-from-chat-A.html
```

Übernimm die mr-CSS exakt (inline-style-Block). Schema-Set: Article, FAQPage, BreadcrumbList, WebPage, Place, City, ImageObject, Organization, PostalAddress, ListItem, Question, Answer.

**Anpassen** an Stadt-Kontext:
- BreadcrumbList: Start → Bestatter-Verzeichnis → München (3-stufig statt 4-stufig)
- Place-Schema: `name: "München"`, `containedInPlace: City "München" / State "Bayern"`
- Jeder Friedhof als eigenes `Place` mit `address` und ggf. `geo`

---

## Quellen-Pack (FACT-Quelle, Pflicht zu fetchen)

**Quellen-URL:**
```
https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/muenchen/quellen-pack.md
```

Enthält:
- Verifizierte Daten zur Münchner Friedhofs-Verwaltung (28 städt. Friedhöfe, FBM, Friedhofsgebührensatzung Nr. 801)
- Vier Hauptfriedhöfe mit Hidden-Gem-Stories: Alter Südfriedhof (1563), Waldfriedhof Großhadern (1907), Nordfriedhof (1884), Ostfriedhof (1900)
- Hans-Grässel-Leitmotiv (3 von 4 Friedhöfen)
- Kostenkorridor 2025-2026 mit konkreten Zahlen
- Bestatter-Wahl-Hinweise

---

## Stadt-Page-spezifische Anforderungen München

### 1. Bestattungsrecht KURZ halten

Nur 3-4 Absätze zum Recht. Stichworte:
- Bayerisches Bestattungsgesetz (BestG) + Bestattungsverordnung (BestV)
- Sargpflicht-Lockerung seit 2021 über Friedhofssatzung
- Mindestfrist 48h, Höchstfrist Erdbestattung 96h
- Münchner Friedhofssatzung: Ruhezeit 10 Jahre Erdbestattung / 10 Jahre Urne, Wahlgräber verlängerbar

**Verweis-Link:** `Vollständige rechtliche Übersicht: <a href="/bestattung-in/bayern/">Bestattung in Bayern</a>`

### 2. Friedhofs-Sektion = Hauptfokus (60% der Wortzahl)

Vier Friedhöfe je 250-400 Wörter:
- **A. Alter Südlicher Friedhof** — 1563 Pestfriedhof, Campo Santo nach Friedrich von Gärtner 1840, „Walhalla der Wissenschaft" (Spitzweg, Fraunhofer, Liebig, Klenze, Kaulbach, Schwanthaler)
- **B. Waldfriedhof Großhadern** — 1907 erster Waldfriedhof Deutschlands, Hans Grässels Pionier-Konzept, Heisenberg/Stuck/Wedekind/Ende. (Achtung: NICHT mit Waldfriedhof Solln verwechseln)
- **C. Nordfriedhof Schwabing** — 1884, Hans Grässels achteckige Aussegnungshalle 1896-99 in warmen Gelbtönen, Thomas Manns „Tod in Venedig"-Schauplatz, Heesters
- **D. Ostfriedhof Obergiesing** — 1900 von Hans Grässel, **einziges Münchner städtisches Krematorium** (1929 eröffnet, denkmalgeschützt), Moshammer-Mausoleum, Löwitsch/Gildo/Kronawitter

**Narrativer Bogen Hans Grässel:** durchgängige Klammer von 3 der 4 Friedhöfe — kann als wiederkehrendes Motiv die Page tragen.

Schema.org `Place` pro Friedhof mit `name`, `address`, optional `geo`.

### 3. Kostenkorridor München

Tabelle mit Friedhofsgebühren laut Satzung 801 (Wahlgrab 1.588 €, Hecken-Nutzung 114 € p.a., Urnenreihen 1.880 €) PLUS Gesamtkosten-Korridor (Feuerbestattung 1.161-5.547 €, Erdbestattung 2.232-8.000 €).

Hinweis: München gehört zu den teuersten Großstädten DE wegen Grabplatz-Knappheit.

### 4. Was tun nach Todesfall in München

Konkrete Adressen:
- Standesamt München, Pacellistraße 5, 80333 München
- Städtische Friedhöfe / FBM, Damenstiftstraße 8, 80331 München
- Sozialreferat für Sozialbestattung § 74 SGB XII

### 5. Bestatter-Wahl in München

- Münchner Bestatterinnung als Indikator
- VDB-Mitgliedschaft, TÜV-Zertifikat
- 2-3 Kostenvoranschläge einholen
- Spezialitäten: muslimische Bestattung (Westfriedhof-Feld), jüdische Bestattung (IKG München), anonyme Beisetzung, Seebestattung-Vermittlung

### 6. FAQ — 6 Fragen

Mind. enthalten:
1. Welche Bestattungsfristen gelten in München / Bayern?
2. Wie hoch sind die Friedhofsgebühren in München?
3. Welche Friedhöfe sind in München besonders bedeutend?
4. Wie finde ich einen guten Bestatter in München?
5. Was kostet eine Beerdigung in München durchschnittlich?
6. Gibt es in München ein städtisches Krematorium?

---

## Title / Meta

- **Title (max 60 chars):** „Bestattung in München: Friedhöfe, Kosten, Bestatter | machsruhig"
- **Meta-description (max 160 chars):** Stadt-spezifisch, mit 3 Such-Hooks: München + Friedhof + Kosten/Bestatter

---

## Aktuelle Stadt-Page (Kontext, NICHT als Vorlage benutzen)

Es gibt eine alte `bestatter/muenchen/index.html` mit 2659 Wörtern. Sie hat schon eine sinnvolle Sektion-Struktur, aber zu kurz und ohne Hidden-Gem-Stories. **Schreibe komplett neu**, übernimm aus der alten Version nichts wortwörtlich. Wenn du sie sehen willst:

**OPTIONAL bestehende Stadt-Page:**
```
https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/muenchen/index.html
```

Nur einzelne Stadt-Insights daraus übernehmen, NICHT die Struktur kopieren.

---

## Format der Antwort

Komplette HTML-Datei `<!DOCTYPE html>` bis `</html>`. Inline-Style-Block mit allen mr-CSS-Klassen wie in der Hessen-Page. JSON-LD im Head. **Nur HTML, keine Erklärung.**

Liefere jetzt die Münchner Stadt-Page.
