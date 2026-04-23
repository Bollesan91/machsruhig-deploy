# CTA-Hierarchie -- machsruhig.de

> Jeder sichtbare Bereich (Viewport) hat genau eine dominante Hauptaktion.
> CTAs folgen einer klaren Hierarchie nach Seitentyp und Scroll-Position.

---

## Grundprinzip

```
Pro sichtbarem Bereich: genau 1 Primaer-CTA
Nie mehr als 3 CTAs gleichzeitig sichtbar (Primaer + Sekundaer + Tertiaer)
Kein CTA ohne vorherigen Mehrwert
```

---

## CTA-Hierarchie nach Seitentyp

### Hub-Seite (/, /bestattungsarten)

| Bereich           | CTA-Typ   | Aktion                          | Darstellung        |
|-------------------|-----------|---------------------------------|--------------------|
| Hero              | Primaer   | Tool starten (z.B. Vorsorge-Check) | Button #7A6B5D  |
| Themen-Kacheln    | Sekundaer | "Mehr erfahren" pro Kachel      | Text-Link          |
| Tool-Teaser       | Primaer   | "Jetzt berechnen"               | Button #7A6B5D     |
| Cross-Sell unten  | Sekundaer | Verwandte Themen                | Text-Links         |

**Regel:** Hub-Seiten sind Wegweiser. Der Primaer-CTA fuehrt immer zum naechsten Schritt (Tool oder Ratgeber), nie direkt zur Conversion.

---

### Tool-Landing-Page (/tools/*)

| Bereich           | CTA-Typ   | Aktion                          | Darstellung        |
|-------------------|-----------|---------------------------------|--------------------|
| Above-the-fold    | Primaer   | "Tool jetzt starten"            | Button #7A6B5D     |
| Tool-Interface    | --        | Kein separater CTA, Interaktion ist der CTA | --        |
| Nach Ergebnis     | Primaer   | "Ergebnis speichern / drucken"  | Button #7A6B5D     |
| Nach Ergebnis     | Sekundaer | Cross-Sell (verwandtes Tool/Ratgeber) | Text-Link / Button transparent |
| Nach Ergebnis     | Tertiaer  | "Vorsorge-Vergleich starten"    | Text-Link (nur wenn thematisch passend) |

**Regel:** Vor dem Tool-Output kein Stufe-3-CTA. Der User muss erst den Mehrwert erleben, bevor eine Conversion angeboten wird.

**Sonderfall Trauerrede-Generator:**
- Nach Ergebnis: "Text kopieren", "Als PDF speichern"
- Cross-Sell: "Kondolenzschreiben verfassen" (Stufe 1)
- KEIN Affiliate oder Lead-Gen -- Trauer-Kontext

---

### Vorsorge-Seite (/vorsorge/*)

| Bereich           | CTA-Typ   | Aktion                          | Darstellung        |
|-------------------|-----------|---------------------------------|--------------------|
| Above-the-fold    | --        | **Content first** -- KEIN CTA   | --                 |
| Nach 30% Scroll   | Sekundaer | Inhaltsverzeichnis / Sprungmarken | Sticky-Nav oder Inline |
| Nach 50% Scroll   | Primaer   | "Vorsorge-Vergleich starten"    | Button #7A6B5D     |
| Seitenende        | Sekundaer | Cross-Sell zu anderen Vorsorge-Themen | Text-Links   |
| Seitenende        | Tertiaer  | "Vorsorge-Ordner herunterladen" | Text-Link          |

**Regel:** Above-the-fold kein CTA. Der User soll erst verstehen, worum es geht. Erst nach substanziellem Content kommt die Conversion-Option.

**Spezifisch pro Vorsorge-Seite:**

| Seite                    | Primaer-CTA (nach 50%)              | Cross-Sell                        |
|--------------------------|--------------------------------------|-----------------------------------|
| Sterbegeldversicherung   | "Anbieter vergleichen*"              | Patientenverfuegung, Testament    |
| Patientenverfuegung      | "Vorlage herunterladen"              | Testament, Vorsorge-Ordner        |
| Testament                | "Testament-Vorlage erstellen"        | Patientenverfuegung, Vorsorge-Ordner |
| Vorsorge-Ordner          | "Vorsorge-Ordner als PDF"            | Sterbegeld, Patientenverfuegung   |

---

### Stadt-Seite (/bestatter/[stadt]/)

| Bereich           | CTA-Typ   | Aktion                          | Darstellung        |
|-------------------|-----------|---------------------------------|--------------------|
| Above-the-fold    | Primaer   | "Bestatter kontaktieren"        | Button #7A6B5D     |
| Bestatter-Liste   | Primaer   | "Anfrage senden" pro Eintrag    | Button #7A6B5D (kleiner) |
| Kosten-Bereich    | Sekundaer | "Kosten berechnen"              | Button transparent |
| Footer-Bereich    | Sekundaer | Andere Staedte                  | Text-Links         |

**Regel:** Stadtseiten sind der direkteste Conversion-Pfad. "Bestatter kontaktieren" ist immer der Primaer-CTA.

---

### Bundesland-Seite (/bestattung-in/[bundesland]/)

| Bereich           | CTA-Typ   | Aktion                          | Darstellung        |
|-------------------|-----------|---------------------------------|--------------------|
| Above-the-fold    | Primaer   | "Stadt waehlen"                 | Dropdown/Suche     |
| Staedte-Uebersicht | Sekundaer | "[Stadt] anzeigen" pro Eintrag | Text-Links         |
| Info-Bereich      | Tertiaer  | "Bestattungskosten berechnen"   | Text-Link          |

---

### Info-Seite (Ratgeber)

| Bereich           | CTA-Typ   | Aktion                          | Darstellung        |
|-------------------|-----------|---------------------------------|--------------------|
| Above-the-fold    | --        | **Content first** -- KEIN CTA   | --                 |
| Im Content        | Tertiaer  | Inline-Links zu verwandten Themen | Text-Links       |
| Nach Hauptinhalt  | Sekundaer | "Passendes Tool nutzen"         | Button transparent |
| Seitenende        | Tertiaer  | Cross-Sell Ratgeber             | Text-Links         |

**Sonderregel Trauer-Ratgeber** (Trauerrede, Kondolenz, Trauersprueche):
- NUR Stufe-1-CTAs
- Kein "Jetzt...", kein Dringlichkeits-Wording
- CTAs als Text-Links, nie als prominente Buttons

---

### Legal-Seite (/impressum, /datenschutz)

| Bereich           | CTA-Typ   | Aktion                          | Darstellung        |
|-------------------|-----------|---------------------------------|--------------------|
| Gesamte Seite     | --        | **Keine CTAs**                  | --                 |

---

## Farb-Referenz

| Hierarchie  | Farbe                              | CSS                                      |
|-------------|------------------------------------|------------------------------------------|
| Primaer     | Warm-Braun auf Creme               | `background: #7A6B5D; color: #fff;`      |
| Sekundaer   | Transparent mit Border             | `background: transparent; border: 1px solid #7A6B5D; color: #7A6B5D;` |
| Tertiaer    | Text-Link                          | `color: #7A6B5D; text-decoration: underline;` |
| Deaktiviert | Grau                               | `background: #d4d0cc; color: #999;`      |

### Button-Specs

```css
/* Primaer */
.btn-primary {
  background-color: #7A6B5D;
  color: #FFFFFF;
  border: none;
  border-radius: 8px;
  padding: 12px 24px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s ease;
}
.btn-primary:hover {
  background-color: #2D2319;
}

/* Sekundaer */
.btn-secondary {
  background-color: transparent;
  color: #7A6B5D;
  border: 1px solid #7A6B5D;
  border-radius: 8px;
  padding: 12px 24px;
  font-family: 'DM Sans', sans-serif;
  font-weight: 500;
  font-size: 1rem;
  cursor: pointer;
}
.btn-secondary:hover {
  background-color: #7A6B5D;
  color: #FFFFFF;
}

/* Tertiaer */
.btn-tertiary {
  background: none;
  border: none;
  color: #7A6B5D;
  text-decoration: underline;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.95rem;
  cursor: pointer;
  padding: 0;
}
```

---

## Anti-Patterns -- Verboten

### 1. Multiple gleichstarke CTAs
```
FALSCH:
[Bestatter kontaktieren]  [Kosten berechnen]  [Vorsorge starten]
                     ^^ Alle gleich prominent

RICHTIG:
[Bestatter kontaktieren]        -- Primaer
 Kosten berechnen               -- Sekundaer (Border)
 Vorsorge planen >              -- Tertiaer (Text-Link)
```

### 2. Dringlichkeits-Wording
```
FALSCH:                          RICHTIG:
"Jetzt sofort handeln!"         "Vorsorge planen"
"Nur noch heute!"               "Anbieter vergleichen"
"Verpassen Sie nicht!"          "Mehr erfahren"
"Letzte Chance!"                "Kostenlos berechnen"
```

### 3. Affiliate als Primaer-CTA
```
FALSCH:
Hero-Bereich: [Sterbegeld-Anbieter vergleichen*]   -- Affiliate ist Primaer

RICHTIG:
Hero-Bereich: "Was ist Sterbegeldversicherung?"     -- Content first
Nach 50%:     [Anbieter vergleichen*]               -- Affiliate als Primaer nach Mehrwert
```

### 4. CTA vor Mehrwert
```
FALSCH:
Seite oeffnet sich -> Sofort: "Bestatter anfragen"  -- User weiss noch nichts

RICHTIG:
Seite oeffnet sich -> Information -> Verstaendnis -> "Bestatter anfragen"
```

### 5. CTA auf Trauerseiten
```
FALSCH:
/trauerrede-schreiben -> [Sterbegeldversicherung vergleichen*]

RICHTIG:
/trauerrede-schreiben -> "Trauerrede-Generator ausprobieren" (Text-Link, Stufe 1)
```

---

## Scroll-basierte CTA-Platzierung

```
 0%  +-----------------------------------------+
     |  Hero / Einleitung                       |
     |  [Primaer-CTA nur bei Tool/Lokal/Hub]    |
     +-----------------------------------------+
25%  |  Hauptinhalt Abschnitt 1                |
     |  (Inline-Links = Tertiaer)              |
     +-----------------------------------------+
50%  |  Hauptinhalt Abschnitt 2                |
     |  [Primaer-CTA bei Vorsorge-Seiten]      |
     +-----------------------------------------+
75%  |  Vertiefung / FAQ                       |
     |  [Sekundaer-CTA: verwandtes Tool]       |
     +-----------------------------------------+
100% |  Cross-Sell / Verwandte Themen          |
     |  (Tertiaer-Links)                       |
     +-----------------------------------------+
```

---

## Checkliste: CTA-Review

Vor Veroeffentlichung jeder Seite pruefen:

- [ ] Genau 1 Primaer-CTA pro sichtbarem Bereich?
- [ ] CTA-Hierarchie klar erkennbar (Primaer > Sekundaer > Tertiaer)?
- [ ] Primaer-CTA nutzt #7A6B5D-Button?
- [ ] Kein Dringlichkeits-Wording?
- [ ] Affiliate-Links gekennzeichnet?
- [ ] Trauer-Seiten ohne Stufe-3-CTAs?
- [ ] Content vor Conversion (kein CTA above-the-fold bei Vorsorge/Info)?
- [ ] Maximal 3 CTAs gleichzeitig sichtbar?
- [ ] Jeder CTA fuehrt zu einer klaren naechsten Aktion?
- [ ] Wording ist respektvoll und nicht draengend?
