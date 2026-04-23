# Linklogik -- Interne Verlinkungsstrategie machsruhig.de

> Jeder interne Link hat einen Zweck: den User zum naechsten logischen Schritt fuehren.
> Links folgen definierten Pfaden und einer Cross-Sell-Matrix.

---

## Link-Pfade (User Journeys)

Jeder Link-Pfad beschreibt eine ideale User Journey durch die Seite. Der User bewegt sich von allgemein zu spezifisch, von Information zu Aktion.

### Pfad 1: Bestattung planen

```
/                           Hub/Landing
  |
  v
/bestattungsarten           Info (Uebersicht Bestattungsformen)
  |
  v
/bestatter/[stadt]/         Lokal (konkreter Bestatter vor Ort)
  |
  v
Bestatter-Anfrage           Conversion (Lead-Gen)
```

**Verlinkungsregeln:**
- Startseite verlinkt prominent auf /bestattungsarten
- /bestattungsarten verlinkt auf die naechstgelegene Stadtseite (wenn Standort bekannt) oder auf die Staedte-Uebersicht
- Stadtseite hat Bestatter-Kontaktformular als Primaer-CTA
- Ruecklinks: Stadtseite verlinkt zurueck auf /bestattungsarten (Breadcrumb)

---

### Pfad 2: Vorsorge

```
/                           Hub/Landing
  |
  v
/vorsorge/                  Hub (Vorsorge-Uebersicht, falls vorhanden)
  |                         oder direkt zu Unter-Seiten
  v
/vorsorge/sterbegeld...     Vorsorge (Detail-Ratgeber)
  |
  v
Vergleich-CTA               Conversion (Affiliate)
```

**Verlinkungsregeln:**
- Startseite verlinkt auf Vorsorge-Bereich
- Vorsorge-Seiten verlinken untereinander (Cross-Sell)
- Sterbegeldversicherung hat nach 50% den Vergleichs-CTA
- Patientenverfuegung/Testament/Vorsorge-Ordner verlinken auf externe Vorlagen-Portale (Affiliate)

---

### Pfad 3: Akuter Todesfall

```
/                           Hub/Landing
  |
  v
/beerdigung-planen          Info/Ratgeber (Was tun im Todesfall?)
  |
  v
/tools/checkliste-todesfall Tool (Interaktive Checkliste)
  |
  v
Checkliste drucken          Output (PDF/Druck)
  |
  v
/bestatter/[stadt]/         Cross-Sell (Bestatter vor Ort)
```

**Verlinkungsregeln:**
- /beerdigung-planen ist die wichtigste Einstiegsseite fuer akute Faelle
- Verlinkt direkt und prominent auf /tools/checkliste-todesfall
- Nach Tool-Nutzung: Cross-Sell zu Bestatter-Suche
- KEIN Affiliate oder aggressive CTAs -- der User ist in einer Notsituation

---

### Pfad 4: Trauerrede / Kondolenz

```
/trauerrede-schreiben       Info/Ratgeber
  |
  v
/tools/trauerrede           Tool (Trauerrede-Generator)
  |
  v
Export (Text/PDF)            Output
  |
  v
/kondolenzschreiben         Cross-Sell (verwandter Ratgeber)
```

**Verlinkungsregeln:**
- /trauerrede-schreiben verlinkt auf den Trauerrede-Generator
- Nach Tool-Output: Link zu Kondolenzschreiben als naechsten Schritt
- Kondolenzschreiben verlinkt auf Trauersprueche
- KEINE Monetarisierung in diesem Pfad -- durchgehender Trauer-Kontext

---

### Pfad 5: Kosten verstehen

```
/bestattungskosten          Info/Ratgeber
  |
  v
/tools/bestattungskosten-   Tool (Kostenrechner)
  rechner
  |
  v
Ergebnis                    Output (Kostenschaetzung)
  |
  v
/vorsorge/sterbegeld...     Cross-Sell (Vorsorge)
  |
  +--- oder --->
  |
/bestatter/[stadt]/         Cross-Sell (Bestatter finden)
```

**Verlinkungsregeln:**
- /bestattungskosten verlinkt auf den Kostenrechner
- Nach Ergebnis: Cross-Sell zu Sterbegeldversicherung (logisch: Kosten abdecken)
- Alternativ: Cross-Sell zu Bestatter in der Naehe

---

## Cross-Sell-Matrix

Die Matrix definiert, welche Seiten aufeinander verlinken duerfen und sollen.

### Primaere Cross-Sells (MUSS verlinkt werden)

| Ausgangsseite                    | Verlinkt auf                        | Begruendung                           |
|----------------------------------|-------------------------------------|---------------------------------------|
| Bestattungskosten                | Sterbegeldversicherung              | Kosten absichern                      |
| Checkliste Todesfall             | Bestatter finden (Stadtseite)       | Naechster praktischer Schritt         |
| Trauerrede schreiben             | Trauerrede-Generator                | Tool-Verknuepfung                     |
| Trauerrede-Generator (Output)    | Kondolenzschreiben                  | Verwandter Content                    |
| Kondolenzschreiben               | Trauersprueche                      | Ergaenzender Content                  |
| Vorsorge-Check (Output)          | Patientenverfuegung                 | Empfohlene naechste Schritte          |
| Vorsorge-Check (Output)          | Testament                           | Empfohlene naechste Schritte          |
| Vorsorge-Check (Output)          | Sterbegeldversicherung              | Empfohlene naechste Schritte          |
| Bestatter-Stadtseite             | Bestattungskosten-Rechner           | Kosten einschaetzen                   |
| Bestattungsarten                 | Bestattungskosten                   | Was kostet die gewaehlte Art?         |
| Sterbegeldversicherung           | Vorsorge-Ordner                     | Alle Vorsorge buendeln               |

### Sekundaere Cross-Sells (KANN verlinkt werden)

| Ausgangsseite                    | Verlinkt auf                        | Begruendung                           |
|----------------------------------|-------------------------------------|---------------------------------------|
| Bestattungskosten-Rechner (Out)  | Bestatter-Stadtseite                | Konkretes Angebot einholen            |
| Beerdigung planen                | Bestattungsarten                    | Welche Bestattungsform?               |
| Beerdigung planen                | Bestattungskosten                   | Was kostet es?                        |
| Patientenverfuegung              | Testament                           | Verwandtes Vorsorge-Thema             |
| Testament                        | Patientenverfuegung                 | Verwandtes Vorsorge-Thema             |
| Vorsorge-Ordner                  | Alle Vorsorge-Seiten                | Sammlung aller Dokumente              |
| Beerdigungsplaner (Output)       | Checkliste Todesfall                | Ergaenzende Planung                   |
| Bundesland-Seite                 | Stadtseiten im Bundesland           | Lokale Vertiefung                     |

### Verbotene Cross-Sells

| Ausgangsseite                    | NICHT verlinken auf                 | Begruendung                           |
|----------------------------------|-------------------------------------|---------------------------------------|
| Trauerrede schreiben             | Sterbegeldversicherung              | Trauer-Kontext, keine Monetarisierung |
| Kondolenzschreiben               | Affiliate-Links jeglicher Art       | Trauer-Kontext                        |
| Trauersprueche                   | Bestatter-Anfrage                   | Trauer-Kontext, unpassend             |
| Trauerrede-Generator             | Vorsorge-Vergleich                  | Thematisch unpassend                  |
| Legal-Seiten                     | Jegliche CTAs oder Cross-Sells      | Rechtliche Seiten bleiben neutral     |

---

## Link-Platzierung im Content

### Inline-Links (im Fliesstext)

```markdown
Wenn Sie die [Bestattungskosten](/bestattungskosten) kennen, koennen Sie
besser planen. Nutzen Sie unseren
[Kostenrechner](/tools/bestattungskosten-rechner), um eine erste
Einschaetzung zu erhalten.
```

**Regeln:**
- Maximal 2-3 interne Links pro Abschnitt (ca. 200 Woerter)
- Anchor-Text beschreibt das Ziel, nicht "hier klicken"
- Interne Links vor externen Links

### Cross-Sell-Box (am Abschnittsende)

```
+--------------------------------------------------+
|  Verwandte Themen                                |
|                                                  |
|  > Bestattungskosten berechnen                   |
|  > Sterbegeldversicherung vergleichen            |
|  > Bestatter in Ihrer Naehe finden               |
+--------------------------------------------------+
```

**Regeln:**
- Maximal 3 Links pro Cross-Sell-Box
- Reihenfolge: Thematisch naechster Schritt zuerst
- Nur am Abschnittsende, nie mitten im Content

### Breadcrumb-Navigation

```
Startseite > Vorsorge > Sterbegeldversicherung
Startseite > Tools > Checkliste Todesfall
Startseite > Bestatter > Berlin
Startseite > Bestattung in > Bayern
```

**Regeln:**
- Immer vorhanden (ausser auf Startseite und Legal-Seiten)
- Maximal 3 Ebenen
- Letzte Ebene ist nicht verlinkt (aktuelle Seite)

---

## Verbotene Link-Muster

### 1. Tool zu Tool ohne Output

```
FALSCH:
/tools/vorsorge-check --> /tools/checkliste-todesfall
(User hat den Vorsorge-Check noch nicht benutzt)

RICHTIG:
/tools/vorsorge-check --> [User macht Vorsorge-Check] --> Ergebnis
--> /tools/checkliste-todesfall (als Empfehlung im Ergebnis)
```

Der User muss das erste Tool benutzt haben, bevor er zum naechsten weitergeleitet wird. Sonst entsteht "Tool-Hopping" ohne Mehrwert.

### 2. Externe Links vor internen

```
FALSCH:
"Mehr zur Sterbegeldversicherung bei [externerAnbieter.de]"
... und erst danach: "Unser Ratgeber zur Sterbegeldversicherung"

RICHTIG:
"Lesen Sie unseren [Ratgeber zur Sterbegeldversicherung](/vorsorge/sterbegeldversicherung)"
... und ggf. spaeter: "Anbieter vergleichen bei [externerAnbieter.de]*"
```

Interne Links haben immer Vorrang. Externe Links (besonders Affiliate) kommen erst nach dem internen Content.

### 3. Zirkulaere Verlinkung ohne Mehrwert

```
FALSCH:
/bestattungskosten -> /bestattungsarten -> /bestattungskosten
(Kreisverkehr ohne neuen Inhalt)

RICHTIG:
/bestattungskosten -> /bestattungsarten (einfach, thematisch passend)
/bestattungsarten -> /bestatter/[stadt]/ (naechster Schritt)
```

### 4. Orphan-Links (tote Enden)

```
FALSCH:
Seite hat keinen einzigen ausgehenden internen Link

RICHTIG:
Jede Seite hat mindestens 2 interne Links:
  1. Naechster logischer Schritt
  2. Zurueck zur Uebersicht / verwandtes Thema
```

### 5. Affiliate ohne internen Vorlauf

```
FALSCH:
Erster Link auf der Seite ist ein Affiliate-Link

RICHTIG:
Eigener Content zuerst -> Interne Verlinkung -> dann ggf. Affiliate
```

---

## Linkdichte-Richtwerte

| Seitentyp     | Min. interne Links | Max. interne Links | Externe Links max. |
|---------------|--------------------|--------------------|--------------------|
| Hub           | 5                  | 15                 | 0                  |
| Tool-LP       | 3                  | 6                  | 0-1                |
| Info/Ratgeber | 4                  | 10                 | 1-3                |
| Vorsorge      | 4                  | 8                  | 2-4 (Affiliate)    |
| Lokal (Stadt) | 3                  | 8                  | 0-2                |
| Lokal (BL)    | 5                  | 20                 | 0                  |
| Legal         | 1                  | 3                  | Je nach Bedarf     |

---

## Vollstaendige Link-Map

### Von der Startseite (/)

```
/ -----> /bestattungsarten          "Bestattungsarten im Ueberblick"
/ -----> /bestattungskosten         "Was kostet eine Bestattung?"
/ -----> /beerdigung-planen         "Beerdigung planen"
/ -----> /vorsorge/sterbegeld...    "Vorsorge: Sterbegeldversicherung"
/ -----> /tools/vorsorge-check      "Vorsorge-Check starten"
/ -----> /tools/checkliste-todesfall "Checkliste: Was tun im Todesfall?"
/ -----> /bestatter/[stadt]/        "Bestatter in Ihrer Naehe"
```

### Von Info-Seiten

```
/bestattungskosten -----> /tools/bestattungskosten-rechner
/bestattungskosten -----> /vorsorge/sterbegeldversicherung
/bestattungskosten -----> /bestatter/[stadt]/

/beerdigung-planen -----> /tools/checkliste-todesfall
/beerdigung-planen -----> /bestattungsarten
/beerdigung-planen -----> /bestattungskosten

/trauerrede-schreiben --> /tools/trauerrede
/trauerrede-schreiben --> /kondolenzschreiben

/kondolenzschreiben ----> /trauersprueche
/kondolenzschreiben ----> /trauerrede-schreiben

/trauersprueche --------> /kondolenzschreiben
/trauersprueche --------> /trauerrede-schreiben
```

### Von Tool-Seiten (nach Output)

```
/tools/bestattungskosten-rechner --> /vorsorge/sterbegeldversicherung
/tools/bestattungskosten-rechner --> /bestatter/[stadt]/

/tools/checkliste-todesfall -------> /bestatter/[stadt]/
/tools/checkliste-todesfall -------> /beerdigung-planen

/tools/trauerrede -----------------> /kondolenzschreiben
/tools/trauerrede -----------------> /trauersprueche

/tools/vorsorge-check -------------> /vorsorge/patientenverfuegung
/tools/vorsorge-check -------------> /vorsorge/testament
/tools/vorsorge-check -------------> /vorsorge/sterbegeldversicherung
/tools/vorsorge-check -------------> /vorsorge/vorsorge-ordner

/tools/beerdigungsplaner ----------> /tools/checkliste-todesfall
/tools/beerdigungsplaner ----------> /bestatter/[stadt]/

/tools/kostenrechner --------------> /bestattungskosten
/tools/kostenrechner --------------> /vorsorge/sterbegeldversicherung
```

### Von Vorsorge-Seiten

```
/vorsorge/sterbegeldversicherung --> /vorsorge/vorsorge-ordner
/vorsorge/sterbegeldversicherung --> /vorsorge/patientenverfuegung
/vorsorge/sterbegeldversicherung --> /tools/vorsorge-check

/vorsorge/patientenverfuegung -----> /vorsorge/testament
/vorsorge/patientenverfuegung -----> /vorsorge/vorsorge-ordner

/vorsorge/testament ---------------> /vorsorge/patientenverfuegung
/vorsorge/testament ---------------> /vorsorge/vorsorge-ordner

/vorsorge/vorsorge-ordner ---------> /vorsorge/sterbegeldversicherung
/vorsorge/vorsorge-ordner ---------> /vorsorge/patientenverfuegung
/vorsorge/vorsorge-ordner ---------> /vorsorge/testament
```

### Von Lokal-Seiten

```
/bestatter/[stadt]/ ---------------> /tools/bestattungskosten-rechner
/bestatter/[stadt]/ ---------------> /bestattung-in/[bundesland]/

/bestattung-in/[bundesland]/ ------> /bestatter/[stadt]/ (alle Staedte)
/bestattung-in/[bundesland]/ ------> /bestattungskosten
```
