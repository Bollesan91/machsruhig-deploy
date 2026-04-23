# Seitentypen-Zuordnung -- machsruhig.de

> Jede URL ist genau einem Seitentyp zugeordnet.
> Der Seitentyp bestimmt Content-Klasse, CTA-Regeln und Monetarisierungs-Erlaubnis.

---

## Legende

| Seitentyp     | Kuerzel | Content-Klasse | Monetarisierung | CTA-Stufen |
|---------------|---------|----------------|-----------------|------------|
| Hub/Landing   | HUB     | Hub            | Nein            | 1, 2       |
| Tool-LP       | TOOL    | Tool           | Nach Output*    | 1, 2, 3*   |
| Info/Ratgeber | INFO    | Info           | Eingeschraenkt  | 1, 2**     |
| Vorsorge      | VOR     | Vorsorge       | Ja              | 1, 2, 3    |
| Lokal (Stadt) | LOK-S   | Lokal          | Ja (Leads)      | 1, 2, 3    |
| Lokal (BL)    | LOK-BL  | Lokal          | Eingeschraenkt  | 1          |
| Legal         | LEG     | Legal          | Nein            | Keine      |
| Trust/About   | TRUST   | --             | Nein            | Keine      |

\* Tool-LP: Stufe 3 nur nach Output, nicht bei Trauer-Tools.
\** Info: Trauer-Info-Seiten nur Stufe 1.

---

## Vollstaendige URL-Zuordnung

### Startseite

| URL            | Datei          | Seitentyp   | Monetarisierung | Trauer-Schutz |
|----------------|----------------|-------------|-----------------|---------------|
| `/`            | `index.html`   | HUB         | Nein            | --            |

**Funktion:** Zentrale Einstiegsseite. Verlinkt auf alle Hauptbereiche. Kein Affiliate, kein Lead-Gen. Reiner Wegweiser.

---

### Info-Seiten (Ratgeber)

| URL                      | Datei                        | Seitentyp | Monetarisierung   | Trauer-Schutz     |
|--------------------------|------------------------------|-----------|-------------------|--------------------|
| `/bestattungsarten`      | `bestattungsarten.html`      | INFO      | Nein              | --                 |
| `/bestattungskosten`     | `bestattungskosten.html`     | INFO      | Eingeschraenkt    | --                 |
| `/beerdigung-planen`     | `beerdigung-planen.html`     | INFO      | Eingeschraenkt    | --                 |
| `/trauerrede-schreiben`  | `trauerrede-schreiben.html`  | INFO      | **VERBOTEN**      | **Ja -- Trauer**   |
| `/kondolenzschreiben`    | `kondolenzschreiben.html`    | INFO      | **VERBOTEN**      | **Ja -- Trauer**   |
| `/trauersprueche`        | `trauersprueche.html`        | INFO      | **VERBOTEN**      | **Ja -- Trauer**   |

**Anmerkungen:**
- `/bestattungskosten` und `/beerdigung-planen`: Dezenter Cross-Sell zu Tools und Vorsorge erlaubt, kein direkter Affiliate.
- `/bestattungsarten`: Reine Information, keine Monetarisierung.
- Trauer-Seiten: Absoluter Schutz. Kein Affiliate, kein Lead-Gen, keine Cross-Sell zu Monetarisierungs-Seiten.

---

### Tool-Seiten

| URL                               | Verzeichnis                          | Seitentyp | Monetarisierung        | Trauer-Schutz     |
|------------------------------------|--------------------------------------|-----------|------------------------|--------------------|
| `/tools/checkliste-todesfall`      | `tools/checkliste-todesfall/`        | TOOL      | Nach Output (Leads)    | --                 |
| `/tools/bestattungskosten-rechner` | `tools/bestattungskosten-rechner/`   | TOOL      | Nach Output (Affiliate)| --                 |
| `/tools/trauerrede`                | `tools/trauerrede/`                  | TOOL      | **VERBOTEN**           | **Ja -- Trauer**   |
| `/tools/vorsorge-check`            | `tools/vorsorge-check/`              | TOOL      | Nach Output (Cross-Sell)| --                |
| `/tools/beerdigungsplaner`         | `tools/beerdigungsplaner/`           | TOOL      | Nach Output (Leads)    | --                 |
| `/tools/kostenrechner`             | `tools/kostenrechner/`               | TOOL      | Nach Output (Affiliate)| --                 |

**Anmerkungen:**
- `/tools/trauerrede`: Trauer-Tool. Kein Affiliate nach Output. Nur Cross-Sell zu Kondolenz/Trauersprueche (Stufe 1).
- `/tools/kostenrechner`: Variante/Erweiterung des Bestattungskosten-Rechners. Gleiche Regeln.
- Alle Tools: Datenschutz-Hinweis zur lokalen Datenverarbeitung pflichtmaessig.

---

### Vorsorge-Seiten

| URL                                  | Verzeichnis                              | Seitentyp | Monetarisierung       | Trauer-Schutz |
|--------------------------------------|------------------------------------------|-----------|----------------------|---------------|
| `/vorsorge/sterbegeldversicherung`   | `vorsorge/sterbegeldversicherung/`       | VOR       | Affiliate (Vergleich) | --            |
| `/vorsorge/patientenverfuegung`      | `vorsorge/patientenverfuegung/`          | VOR       | Affiliate (Vorlagen)  | --            |
| `/vorsorge/testament`                | `vorsorge/testament/`                    | VOR       | Affiliate (Vorlagen)  | --            |
| `/vorsorge/vorsorge-ordner`          | `vorsorge/vorsorge-ordner/`              | VOR       | Lead-Magnet (PDF)     | --            |

**Anmerkungen:**
- Alle Vorsorge-Seiten: Content first. CTA ab 50% Scroll.
- Sterbegeldversicherung: Primaerer Affiliate-Kanal (Vergleichs-CTA).
- Patientenverfuegung + Testament: Affiliate zu Vorlagen-Portalen.
- Vorsorge-Ordner: Lead-Magnet (E-Mail gegen PDF-Download).

---

### Lokal-Seiten: Staedte (50 Seiten)

| URL                            | Verzeichnis                  | Seitentyp | Monetarisierung        |
|--------------------------------|------------------------------|-----------|------------------------|
| `/bestatter/aachen/`           | `bestatter/aachen/`          | LOK-S     | Leads                  |
| `/bestatter/augsburg/`         | `bestatter/augsburg/`        | LOK-S     | Leads                  |
| `/bestatter/berlin/`           | `bestatter/berlin/`          | LOK-S     | Leads                  |
| `/bestatter/bielefeld/`        | `bestatter/bielefeld/`       | LOK-S     | Leads                  |
| `/bestatter/bochum/`           | `bestatter/bochum/`          | LOK-S     | Leads                  |
| `/bestatter/bonn/`             | `bestatter/bonn/`            | LOK-S     | Leads                  |
| `/bestatter/braunschweig/`     | `bestatter/braunschweig/`    | LOK-S     | Leads                  |
| `/bestatter/bremen/`           | `bestatter/bremen/`          | LOK-S     | Leads                  |
| `/bestatter/chemnitz/`         | `bestatter/chemnitz/`        | LOK-S     | Leads                  |
| `/bestatter/darmstadt/`        | `bestatter/darmstadt/`       | LOK-S     | Leads                  |
| `/bestatter/dortmund/`         | `bestatter/dortmund/`        | LOK-S     | Leads                  |
| `/bestatter/dresden/`          | `bestatter/dresden/`         | LOK-S     | Leads                  |
| `/bestatter/duesseldorf/`      | `bestatter/duesseldorf/`     | LOK-S     | Leads                  |
| `/bestatter/duisburg/`         | `bestatter/duisburg/`        | LOK-S     | Leads                  |
| `/bestatter/erfurt/`           | `bestatter/erfurt/`          | LOK-S     | Leads                  |
| `/bestatter/essen/`            | `bestatter/essen/`           | LOK-S     | Leads                  |
| `/bestatter/frankfurt/`        | `bestatter/frankfurt/`       | LOK-S     | Leads                  |
| `/bestatter/freiburg/`         | `bestatter/freiburg/`        | LOK-S     | Leads                  |
| `/bestatter/gelsenkirchen/`    | `bestatter/gelsenkirchen/`   | LOK-S     | Leads                  |
| `/bestatter/hagen/`            | `bestatter/hagen/`           | LOK-S     | Leads                  |
| `/bestatter/halle/`            | `bestatter/halle/`           | LOK-S     | Leads                  |
| `/bestatter/hamburg/`          | `bestatter/hamburg/`         | LOK-S     | Leads                  |
| `/bestatter/hannover/`         | `bestatter/hannover/`        | LOK-S     | Leads                  |
| `/bestatter/heidelberg/`       | `bestatter/heidelberg/`      | LOK-S     | Leads                  |
| `/bestatter/karlsruhe/`        | `bestatter/karlsruhe/`       | LOK-S     | Leads                  |
| `/bestatter/kassel/`           | `bestatter/kassel/`          | LOK-S     | Leads                  |
| `/bestatter/kiel/`             | `bestatter/kiel/`            | LOK-S     | Leads                  |
| `/bestatter/koeln/`            | `bestatter/koeln/`           | LOK-S     | Leads                  |
| `/bestatter/krefeld/`          | `bestatter/krefeld/`         | LOK-S     | Leads                  |
| `/bestatter/leipzig/`          | `bestatter/leipzig/`         | LOK-S     | Leads                  |
| `/bestatter/leverkusen/`       | `bestatter/leverkusen/`      | LOK-S     | Leads                  |
| `/bestatter/luebeck/`          | `bestatter/luebeck/`         | LOK-S     | Leads                  |
| `/bestatter/magdeburg/`        | `bestatter/magdeburg/`       | LOK-S     | Leads                  |
| `/bestatter/mainz/`            | `bestatter/mainz/`           | LOK-S     | Leads                  |
| `/bestatter/mannheim/`         | `bestatter/mannheim/`        | LOK-S     | Leads                  |
| `/bestatter/moenchengladbach/` | `bestatter/moenchengladbach/`| LOK-S     | Leads                  |
| `/bestatter/muelheim/`         | `bestatter/muelheim/`        | LOK-S     | Leads                  |
| `/bestatter/muenchen/`         | `bestatter/muenchen/`        | LOK-S     | Leads                  |
| `/bestatter/muenster/`         | `bestatter/muenster/`        | LOK-S     | Leads                  |
| `/bestatter/nuernberg/`        | `bestatter/nuernberg/`       | LOK-S     | Leads                  |
| `/bestatter/oberhausen/`       | `bestatter/oberhausen/`      | LOK-S     | Leads                  |
| `/bestatter/oldenburg/`        | `bestatter/oldenburg/`       | LOK-S     | Leads                  |
| `/bestatter/osnabrueck/`       | `bestatter/osnabrueck/`      | LOK-S     | Leads                  |
| `/bestatter/potsdam/`          | `bestatter/potsdam/`         | LOK-S     | Leads                  |
| `/bestatter/regensburg/`       | `bestatter/regensburg/`      | LOK-S     | Leads                  |
| `/bestatter/rostock/`          | `bestatter/rostock/`         | LOK-S     | Leads                  |
| `/bestatter/saarbruecken/`     | `bestatter/saarbruecken/`    | LOK-S     | Leads                  |
| `/bestatter/stuttgart/`        | `bestatter/stuttgart/`       | LOK-S     | Leads                  |
| `/bestatter/wiesbaden/`        | `bestatter/wiesbaden/`       | LOK-S     | Leads                  |
| `/bestatter/wuppertal/`        | `bestatter/wuppertal/`       | LOK-S     | Leads                  |

**Alle Stadtseiten:**
- Primaer-CTA: "Bestatter kontaktieren" (Lead-Gen)
- Sekundaer: Bestattungskosten-Rechner
- Cross-Link: Bundesland-Seite + Nachbar-Staedte

---

### Lokal-Seiten: Bundeslaender (16 Seiten)

| URL                                       | Verzeichnis                              | Seitentyp |
|-------------------------------------------|------------------------------------------|-----------|
| `/bestattung-in/baden-wuerttemberg/`      | `bestattung-in/baden-württemberg/`       | LOK-BL    |
| `/bestattung-in/bayern/`                  | `bestattung-in/bayern/`                  | LOK-BL    |
| `/bestattung-in/berlin/`                  | `bestattung-in/berlin/`                  | LOK-BL    |
| `/bestattung-in/brandenburg/`             | `bestattung-in/brandenburg/`             | LOK-BL    |
| `/bestattung-in/bremen/`                  | `bestattung-in/bremen/`                  | LOK-BL    |
| `/bestattung-in/hamburg/`                | `bestattung-in/hamburg/`                 | LOK-BL    |
| `/bestattung-in/hessen/`                  | `bestattung-in/hessen/`                  | LOK-BL    |
| `/bestattung-in/mecklenburg-vorpommern/`  | `bestattung-in/mecklenburg-vorpommern/`  | LOK-BL    |
| `/bestattung-in/niedersachsen/`           | `bestattung-in/niedersachsen/`           | LOK-BL    |
| `/bestattung-in/nordrhein-westfalen/`     | `bestattung-in/nordrhein-westfalen/`     | LOK-BL    |
| `/bestattung-in/rheinland-pfalz/`         | `bestattung-in/rheinland-pfalz/`         | LOK-BL    |
| `/bestattung-in/saarland/`                | `bestattung-in/saarland/`                | LOK-BL    |
| `/bestattung-in/sachsen/`                 | `bestattung-in/sachsen/`                 | LOK-BL    |
| `/bestattung-in/sachsen-anhalt/`          | `bestattung-in/sachsen-anhalt/`          | LOK-BL    |
| `/bestattung-in/schleswig-holstein/`      | `bestattung-in/schleswig-holstein/`      | LOK-BL    |
| `/bestattung-in/thueringen/`              | `bestattung-in/thüringen/`              | LOK-BL    |

**Alle Bundesland-Seiten:**
- Funktion: Uebersicht der Staedte im Bundesland + regionale Besonderheiten
- Kein eigenes Lead-Gen (nur Weiterleitung auf Stadtseiten)
- Monetarisierung: Eingeschraenkt (nur interne Links)

---

### Legal- und Trust-Seiten

| URL              | Datei              | Seitentyp | Monetarisierung | CTAs   |
|------------------|--------------------|-----------|-----------------|--------|
| `/impressum`     | `impressum.html`   | LEG       | VERBOTEN        | Keine  |
| `/datenschutz`   | `datenschutz.html` | LEG       | VERBOTEN        | Keine  |
| `/methodik`      | `methodik.html`    | TRUST     | VERBOTEN        | Keine  |

**Anmerkungen:**
- `/methodik`: Erklaert die Arbeitsweise der Seite. Trust-Building. Keine Monetarisierung, aber kann intern verlinkt werden.

---

### Sonstige Dateien (keine Content-Seiten)

| Datei/URL         | Funktion                                   |
|-------------------|--------------------------------------------|
| `404.html`        | Fehlerseite -- Link zurueck zur Startseite |
| `robots.txt`      | Crawler-Steuerung                          |
| `sitemap.xml`     | Sitemap fuer Suchmaschinen                 |
| `llms.txt`        | LLM-spezifische Informationen              |
| `_headers`        | Netlify HTTP-Header                        |
| `_redirects`      | Netlify Redirect-Regeln                    |
| `netlify.toml`    | Netlify Konfiguration                      |

---

## Zusammenfassung nach Seitentyp

| Seitentyp     | Anzahl Seiten | Anteil       |
|---------------|---------------|--------------|
| HUB           | 1             | 1%           |
| INFO          | 6             | 7%           |
| TOOL          | 6             | 7%           |
| VOR           | 4             | 5%           |
| LOK-S         | 50            | 57%          |
| LOK-BL        | 16            | 18%          |
| LEG           | 2             | 2%           |
| TRUST         | 1             | 1%           |
| Sonstige      | 1 (404)       | 1%           |
| **Gesamt**    | **87**        | **100%**     |

### Seiten mit Trauer-Schutz (KEINE Monetarisierung)

| URL                      | Seitentyp |
|--------------------------|-----------|
| `/trauerrede-schreiben`  | INFO      |
| `/kondolenzschreiben`    | INFO      |
| `/trauersprueche`        | INFO      |
| `/tools/trauerrede`      | TOOL      |

**Insgesamt: 4 Seiten mit absolutem Trauer-Schutz.**

### Seiten mit Monetarisierungs-Potenzial

| Monetarisierungsform     | Seiten                         | Anzahl |
|--------------------------|--------------------------------|--------|
| Affiliate (Vergleich)    | Sterbegeldversicherung         | 1      |
| Affiliate (Vorlagen)     | Patientenverfuegung, Testament | 2      |
| Lead-Magnet              | Vorsorge-Ordner                | 1      |
| Lead-Gen (Bestatter)     | Stadtseiten                    | 50     |
| Cross-Sell nach Output   | Tool-Seiten (ohne Trauerrede)  | 5      |
| **Gesamt monetarisierbar** |                              | **59** |
