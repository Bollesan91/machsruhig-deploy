# Content-Klassen -- machsruhig.de

> Jede Seite auf machsruhig.de gehoert genau einer Content-Klasse an.
> Die Klasse bestimmt Aufbau, CTA-Stufe, Tonalitaet und Monetarisierungs-Erlaubnis.

---

## Uebersicht der Klassen

| Klasse   | Zweck                              | Beispiele                                                    | CTA-Stufen erlaubt |
|----------|------------------------------------|--------------------------------------------------------------|--------------------|
| Tool     | Interaktive Werkzeuge              | Bestattungskosten-Rechner, Trauerrede-Generator, Vorsorge-Check, Checkliste Todesfall, Beerdigungsplaner | 1, 2, 3*           |
| Hub      | Uebersichts- und Einstiegsseiten   | Bestattungsarten, Vorsorge, Bestatter finden                 | 1, 2               |
| Info     | Eigenstaendige Ratgeber            | Bestattungskosten, Trauerrede schreiben, Kondolenzschreiben, Trauersprueche | 1, 2**             |
| Vorsorge | Vorsorge-Content                   | Sterbegeldversicherung, Patientenverfuegung, Testament, Vorsorge-Ordner | 1, 2, 3            |
| Lokal    | Stadt- und Bundesland-Seiten       | Bestatter in Berlin, Bestattung in Bayern                    | 1, 2, 3            |
| Legal    | Rechtliche Pflichtseiten           | Impressum, Datenschutz                                       | Keine               |

\* Tool-Seiten: Stufe 3 nur nach Output (Ergebnis-Anzeige), nie vorher.
\** Info-Seiten zu Trauerinhalten (Trauerrede, Kondolenz, Trauersprueche): Ausschliesslich Stufe 1.

---

## Klasse: Tool

### Definition
Interaktive Seiten, auf denen der User aktiv etwas tut: Eingaben machen, Ergebnisse erhalten, Dokumente generieren.

### Seiten
| URL                              | Tool-Name                    |
|----------------------------------|------------------------------|
| `/tools/bestattungskosten-rechner` | Bestattungskosten-Rechner    |
| `/tools/trauerrede`              | Trauerrede-Generator         |
| `/tools/vorsorge-check`          | Vorsorge-Check               |
| `/tools/checkliste-todesfall`    | Checkliste Todesfall         |
| `/tools/beerdigungsplaner`       | Beerdigungsplaner            |
| `/tools/kostenrechner`           | Kostenrechner (Variante)     |

### Aufbau
1. **Headline + Kurzbeschreibung** -- Was macht das Tool, fuer wen ist es?
2. **Tool-Interface** -- Eingabefelder, Schritte, Interaktion
3. **Ergebnis-Bereich** -- Ergebnis, Zusammenfassung, Export-Optionen
4. **Kontext-Content** -- Erklaerungen, Hintergrundinformationen zum Thema
5. **Cross-Sell** -- Verwandte Tools oder Ratgeber

### CTA-Verhalten
- **Vor Nutzung (Stufe 1):** "Tool jetzt starten", "Kostenlos berechnen"
- **Nach Ergebnis (Stufe 2):** "Ergebnis als PDF speichern", "Checkliste drucken", "Ergebnis per E-Mail senden"
- **Nach Ergebnis (Stufe 3):** Cross-Sell zu Vorsorge-Vergleich, Bestatter-Anfrage -- nur wenn thematisch passend

### Pflicht-Hinweise
- Datenschutz-Hinweis: "Ihre Daten werden nicht gespeichert und ausschliesslich lokal verarbeitet." (wenn zutreffend)
- Kostenangaben: Disclaimer "Alle Angaben sind Richtwerte und koennen regional abweichen."

---

## Klasse: Hub

### Definition
Uebersichtsseiten, die als Einstieg in ein Themengebiet dienen. Sie verlinken auf Detail-Seiten und Tools.

### Seiten
| URL                 | Hub-Thema                |
|---------------------|--------------------------|
| `/` (index.html)    | Hauptseite / Landing     |
| `/bestattungsarten` | Bestattungsarten-Uebersicht |

### Aufbau
1. **Hero-Bereich** -- Emotionale Ansprache, Kernversprechen
2. **Themen-Kacheln** -- Verlinkung zu den wichtigsten Unterseiten
3. **Tool-Teaser** -- Kurzvorstellung der interaktiven Tools
4. **Trust-Elemente** -- Unabhaengigkeit, Qualitaetsversprechen
5. **Sekundaere Navigation** -- Weitere Themen, Stadtseiten

### CTA-Verhalten
- **Primaer (Stufe 1):** "Mehr erfahren", "Zum Ratgeber", "Tool starten"
- **Sekundaer (Stufe 2):** "Checkliste herunterladen", Seiten-interne Navigation
- **Kein Stufe-3-CTA** auf Hub-Seiten

---

## Klasse: Info

### Definition
Eigenstaendige Ratgeber-Artikel, die ein Thema umfassend behandeln. Der User sucht Information, nicht Interaktion.

### Seiten
| URL                      | Thema                     | Trauer-Kontext |
|--------------------------|---------------------------|----------------|
| `/bestattungskosten`     | Bestattungskosten-Ratgeber | Nein           |
| `/beerdigung-planen`     | Beerdigung planen Ratgeber | Nein           |
| `/trauerrede-schreiben`  | Trauerrede schreiben       | **Ja**         |
| `/kondolenzschreiben`    | Kondolenzschreiben         | **Ja**         |
| `/trauersprueche`        | Trauersprueche-Sammlung    | **Ja**         |

### Aufbau
1. **Headline + Einleitung** -- Empathische Einfuehrung, Suchintention aufgreifen
2. **Inhaltsverzeichnis** -- Sprungmarken zu Abschnitten
3. **Hauptinhalt** -- Strukturierte Abschnitte mit Zwischenueberschriften
4. **Praktische Hilfe** -- Vorlagen, Beispiele, Formulierungshilfen
5. **Weitergehende Links** -- Verwandte Ratgeber, passende Tools

### CTA-Verhalten
- **Trauer-Seiten (Trauerrede, Kondolenz, Trauersprueche):**
  - NUR Stufe 1: "Mehr zum Thema", "Tool ausprobieren", "Weitere Vorlagen"
  - KEINE Stufe-2- oder Stufe-3-CTAs
  - KEINE Monetarisierung
- **Nicht-Trauer-Seiten (Bestattungskosten, Beerdigung planen):**
  - Stufe 1 + 2 erlaubt
  - Stufe 3 nur als dezenter Hinweis am Seitenende

---

## Klasse: Vorsorge

### Definition
Content rund um Vorsorge-Planung. Der User handelt proaktiv und ist offen fuer konkrete Loesungen. Hier ist Monetarisierung erlaubt und sinnvoll.

### Seiten
| URL                                 | Thema                     |
|-------------------------------------|---------------------------|
| `/vorsorge/sterbegeldversicherung`  | Sterbegeldversicherung    |
| `/vorsorge/patientenverfuegung`     | Patientenverfuegung       |
| `/vorsorge/testament`               | Testament                 |
| `/vorsorge/vorsorge-ordner`         | Vorsorge-Ordner           |

### Aufbau
1. **Headline + Problem-Statement** -- Warum ist Vorsorge wichtig?
2. **Erklaerung** -- Was ist das Thema, wie funktioniert es?
3. **Praktische Schritte** -- Was muss der User tun?
4. **Vergleich/Empfehlung** -- Optionen, Anbieter-Vergleich (bei Sterbegeld)
5. **CTA-Bereich** -- Vergleich starten, Vorlage herunterladen
6. **FAQ** -- Haeufige Fragen

### CTA-Verhalten
- **Above-the-fold:** Content first -- kein CTA im Sichtbereich oben
- **Nach ca. 50% Scroll:** Stufe-3-CTA "Vorsorge-Vergleich starten" oder "Anbieter vergleichen"
- **Am Seitenende:** Cross-Sell zu anderen Vorsorge-Themen

---

## Klasse: Lokal

### Definition
Stadtseiten und Bundesland-Seiten mit lokaler Bestatter-Information. Kombination aus Information und Lead-Generierung.

### Seiten
- **50 Stadtseiten:** `/bestatter/berlin/`, `/bestatter/muenchen/`, `/bestatter/hamburg/` etc.
- **16 Bundesland-Seiten:** `/bestattung-in/bayern/`, `/bestattung-in/nordrhein-westfalen/` etc.

### Aufbau Stadtseite
1. **Headline** -- "Bestatter in [Stadt] finden"
2. **Kurzinfo** -- Bestattung in [Stadt]: Besonderheiten, Friedhoefe
3. **Bestatter-Liste** -- Lokale Bestatter mit Kontaktdaten
4. **Kontaktformular** -- Anfrage an lokale Bestatter
5. **Kosten-Info** -- Bestattungskosten in [Stadt]
6. **Verwandte Staedte** -- Nearby-Staedte als Links

### Aufbau Bundeslandseite
1. **Headline** -- "Bestattung in [Bundesland]"
2. **Regionale Besonderheiten** -- Landesspezifische Regelungen
3. **Staedte-Uebersicht** -- Links zu allen Stadtseiten im Bundesland
4. **Allgemeine Kosten** -- Regionale Kostenspanne

### CTA-Verhalten
- **Primaer (Stufe 3):** "Bestatter kontaktieren", "Kostenlose Anfrage senden"
- **Sekundaer (Stufe 1):** "Bestattungskosten-Rechner nutzen", "Weitere Staedte"

---

## Klasse: Legal

### Definition
Rechtlich vorgeschriebene Seiten. Kein Marketing, keine CTAs, keine Monetarisierung.

### Seiten
| URL              | Inhalt        |
|------------------|---------------|
| `/impressum`     | Impressum     |
| `/datenschutz`   | Datenschutz   |

### Regeln
- Keine CTAs jeglicher Art
- Keine internen Werbe-Links
- Sachlicher, juristischer Ton
- Vollstaendige rechtliche Pflichtangaben

---

## CTA-Stufen im Detail

### Stufe 1 -- Orientierung
> Ziel: User auf der Seite halten, zum naechsten Schritt fuehren.

| CTA-Text                  | Einsatz                          |
|---------------------------|----------------------------------|
| "Mehr zum Thema"          | Am Ende eines Abschnitts         |
| "Tool starten"            | Teaser auf Tool-Seite            |
| "Weiterlesen"             | Verknuepfung zu Ratgebern        |
| "Zum Ratgeber"            | Hub-Seite zu Info-Seite          |

- **Darstellung:** Text-Link oder dezenter Button
- **Farbe:** Text-Link in #7A6B5D oder transparent Button mit Border

### Stufe 2 -- Unterstuetzung
> Ziel: User bekommt konkreten Mehrwert zum Mitnehmen.

| CTA-Text                  | Einsatz                          |
|---------------------------|----------------------------------|
| "Checkliste drucken"      | Nach Tool-Nutzung                |
| "Ergebnis speichern"      | Nach Berechnung                  |
| "Als PDF herunterladen"   | Vorsorge-Dokument                |
| "Per E-Mail senden"       | Ergebnis-Export                  |

- **Darstellung:** Button, sekundaer
- **Farbe:** Transparent mit #7A6B5D Border

### Stufe 3 -- Conversion
> Ziel: Monetarisierung -- Affiliate, Lead-Gen, Vergleich.

| CTA-Text                       | Einsatz                          |
|--------------------------------|----------------------------------|
| "Vorsorge-Vergleich starten"   | Vorsorge-Seiten                  |
| "Bestatter anfragen"           | Stadtseiten                      |
| "Anbieter vergleichen*"        | Sterbegeld-Seite                 |
| "Kostenlose Beratung anfragen" | Nach Tool-Ergebnis               |

- **Darstellung:** Primaer-Button, prominent
- **Farbe:** #7A6B5D Hintergrund, weisse Schrift
- **Pflicht:** Affiliate-Kennzeichnung bei Affiliate-Links

---

## Verbindliche Regeln

### Grundsaetzlich
1. **Jede Seite gehoert genau einer Klasse an.** Keine Mischformen.
2. **CTA-Stufen sind aufsteigend.** Stufe 3 setzt voraus, dass Stufe 1 und 2 bereits vorhanden sind.
3. **Pro sichtbarem Bereich maximal 1 Primaer-CTA.** Keine CTA-Ueberflutung.

### Trauerseiten-Schutz
4. **Keine Stufe-3-CTAs auf Trauerseiten.** Trauerrede, Kondolenzschreiben, Trauersprueche sind geschuetzte Bereiche.
5. **Keine Monetarisierung auf Trauerseiten.** Kein Affiliate, kein Lead-Gen, keine Werbung.
6. **Tonalitaet auf Trauerseiten:** Empathisch, respektvoll, zurueckhaltend. Niemals draengend.

### Transparenz
7. **Affiliate-Links immer kennzeichnen.** Sichtbar mit "Werbung" oder "*" plus Erklaerung im Footer.
8. **Tool-Seiten brauchen Datenschutz-Hinweis.** Wo werden Daten verarbeitet? Werden sie gespeichert?
9. **Kostenangaben brauchen Disclaimer.** "Alle Angaben sind unverbindliche Richtwerte."

### Marketing-Grenzen
10. **KEIN Push-Marketing.** Keine Pop-ups, keine Exit-Intent-Overlays, keine countdown-basierten CTAs.
11. **Tonalitaet muss respektvoll und empathisch bleiben.** Keine reisserischen Ueberschriften, kein Druck.
12. **Trust vor Conversion.** Erst Mehrwert liefern, dann (dezent) monetarisieren.
