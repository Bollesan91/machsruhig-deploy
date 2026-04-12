# QA-Gates -- Qualitaetssicherung machsruhig.de

> Jede Seite muss alle 7 Gates bestehen, bevor sie live geht.
> Gate 7 (Pietaet) ist ein harter Blocker -- Durchfallen bedeutet Ueberarbeitung.

---

## Uebersicht der Gates

| Gate | Name                      | Prueft                                        | Blocker? |
|------|---------------------------|-----------------------------------------------|----------|
| 1    | Intent-Fit                | Titel + H1 matchen Suchintention              | Ja       |
| 2    | Utility                   | Konkreter Output oder echte Hilfe             | Ja       |
| 3    | Differenzierung           | Besser oder anders als Konkurrenz             | Nein*    |
| 4    | Conversion-Klarheit       | 1 Primaer-CTA pro sichtbarem Bereich         | Ja       |
| 5    | Brand-Fit                 | Design, Farben, Fonts, Tonalitaet             | Ja       |
| 6    | Programmatic-Sauberkeit   | Keine Platzhalter, keine Fehler               | Ja       |
| 7    | Pietaet-Check             | Angemessener Ton bei Trauerinhalten           | **Ja**   |

Gate 3 ist kein harter Blocker, aber ein Warnsignal. Seiten, die Gate 3 nicht bestehen, sollten priorisiert ueberarbeitet werden.

---

## Gate 1: Intent-Fit

### Frage
> Matchen Titel, H1 und die ersten 100 Woerter die Suchintention des Users?

### Pruefkriterien

| Kriterium                                    | Bestanden                              | Durchgefallen                          |
|----------------------------------------------|----------------------------------------|----------------------------------------|
| Title-Tag enthaelt Haupt-Keyword             | "Bestattungskosten 2024 -- Uebersicht" | "Willkommen auf unserer Seite"         |
| H1 beantwortet die Suchfrage                 | "Was kostet eine Bestattung?"          | "Informationen zu unserem Angebot"     |
| Erster Absatz greift die Intention auf        | "Eine Bestattung kostet..."            | "Wir freuen uns, dass Sie..."          |
| Meta-Description macht klick-wuerdig          | Konkrete Zahl/Fakt + CTA              | Generische Firmenbeschreibung          |

### Checkliste

- [ ] Title-Tag enthaelt das primaere Keyword
- [ ] Title-Tag ist 50-60 Zeichen lang
- [ ] H1 ist einzigartig auf der Seite
- [ ] H1 beantwortet die Suchintention direkt
- [ ] Erster Absatz enthaelt das Keyword natuerlich
- [ ] Meta-Description ist 140-160 Zeichen, enthaelt Keyword + konkreten Nutzen
- [ ] URL-Slug matcht das Thema (keine generischen Slugs wie /seite-1)

### Seitentyp-spezifisch

| Seitentyp | Erwartete Suchintention          | H1-Muster                              |
|-----------|----------------------------------|-----------------------------------------|
| Hub       | Uebersicht / Einstieg            | "[Thema] -- Alles Wichtige im Ueberblick" |
| Tool      | Konkrete Aktion ausfuehren       | "[Tool-Name] -- Jetzt kostenlos nutzen" |
| Info      | Frage beantworten                | "[Frage]?" oder "[Thema] -- Ratgeber"  |
| Vorsorge  | Vorsorge planen                  | "[Vorsorge-Thema] -- Was Sie wissen muessen" |
| Lokal     | Bestatter in Stadt finden        | "Bestatter in [Stadt] finden"          |
| Legal     | Pflichtangaben lesen             | "Impressum" / "Datenschutzerklaerung"  |

---

## Gate 2: Utility

### Frage
> Bekommt der User konkreten Output oder echte Hilfe?

### Pruefkriterien

| Kriterium                                    | Bestanden                              | Durchgefallen                          |
|----------------------------------------------|----------------------------------------|----------------------------------------|
| Konkreter Mehrwert in den ersten 30 Sek.      | Kostenzahl, Checkliste, Tool           | Nur allgemeine Einleitung              |
| Actionable Content (der User kann etwas tun)  | Vorlage, Rechner, Schritt-fuer-Schritt | Nur beschreibender Text                |
| Besser als "einfach googeln"                  | Aggregierte, strukturierte Info        | Wikipedia-Niveau                       |

### Utility-Minimum nach Seitentyp

| Seitentyp | Minimum-Utility                                                    |
|-----------|--------------------------------------------------------------------|
| Tool      | Funktionierendes Tool mit nutzbarem Output (PDF, Text, Ergebnis)   |
| Hub       | Klare Navigation zu mindestens 3 relevanten Unterseiten            |
| Info      | Mindestens 1 konkretes Element: Tabelle, Liste, Vorlage, Beispiel  |
| Vorsorge  | Schritt-fuer-Schritt-Anleitung ODER Vergleich ODER Vorlage         |
| Lokal     | Mindestens 3 Bestatter mit Kontaktdaten ODER Kontaktformular       |
| Legal     | Vollstaendige Pflichtangaben                                       |

### Checkliste

- [ ] Seite liefert konkreten Mehrwert (nicht nur Text)
- [ ] User kann nach Besuch etwas tun, was vorher nicht ging
- [ ] Mindestens 1 interaktives oder herunterladbares Element (bei Tool/Vorsorge)
- [ ] Informationen sind aktuell und korrekt
- [ ] Keine reinen Fuelltext-Abschnitte ohne Mehrwert

---

## Gate 3: Differenzierung

### Frage
> Ist diese Seite besser oder zumindest anders als die Top-3-Suchergebnisse?

### Pruefkriterien

| Kriterium                                    | Bestanden                              | Durchgefallen                          |
|----------------------------------------------|----------------------------------------|----------------------------------------|
| Einzigartiger Blickwinkel oder Daten          | Eigene Kostentabelle, regionaler Bezug | Copy-Paste von Konkurrenz              |
| Bessere Aufbereitung                          | Interaktives Tool statt reinem Text    | Gleicher Text, gleiches Format         |
| Aktuellere Informationen                      | Aktuelle Preise, neue Regelungen       | Veraltete Zahlen                       |
| Zusaetzlicher Nutzen                          | Rechner + Ratgeber + Checkliste        | Nur Ratgeber                           |

### Differenzierungsmerkmale von machsruhig.de

| Merkmal                    | Unser Vorteil                                   |
|----------------------------|--------------------------------------------------|
| Interaktive Tools          | Rechner, Generatoren, Checklisten als Web-Apps   |
| Empathische Tonalitaet     | Respektvoll statt klinisch oder reisserisch      |
| Lokaler Bezug              | 50 Staedte + 16 Bundeslaender                   |
| Vorsorge-Kompetenz         | Gebundeltes Wissen zu allen Vorsorge-Themen      |
| Kein Push-Marketing        | Trust-first statt Conversion-first               |

### Checkliste

- [ ] Top-3-Konkurrenzseiten fuer das Keyword geprueft
- [ ] Mindestens 1 klares Differenzierungsmerkmal identifiziert
- [ ] Kein Content, der 1:1 woanders existiert
- [ ] Bessere UX als Konkurrenz (Ladezeit, Lesbarkeit, Mobile)

---

## Gate 4: Conversion-Klarheit

### Frage
> Gibt es pro sichtbarem Bereich genau 1 dominante Hauptaktion?

### Pruefkriterien

| Kriterium                                    | Bestanden                              | Durchgefallen                          |
|----------------------------------------------|----------------------------------------|----------------------------------------|
| 1 Primaer-CTA pro Viewport                   | [Bestatter kontaktieren]               | [Kontakt] [Rechner] [Vergleich] gleich |
| CTA-Hierarchie erkennbar                      | Primaer > Sekundaer > Tertiaer         | Alle Buttons gleich gross/farbig       |
| CTA-Text beschreibt die Aktion                | "Kosten berechnen"                     | "Hier klicken"                         |
| CTA fuehrt zur erwarteten Seite/Aktion        | Button "Rechner" oeffnet den Rechner   | Button fuehrt woanders hin             |

### Checkliste

- [ ] Maximal 1 Primaer-CTA pro sichtbarem Bereich
- [ ] Primaer-CTA in #7A6B5D, Sekundaer transparent, Tertiaer Text-Link
- [ ] CTA-Text ist beschreibend und aktionsorientiert
- [ ] Kein Dringlichkeits-Wording ("Jetzt sofort!", "Letzte Chance!")
- [ ] Affiliate-CTAs sind gekennzeichnet
- [ ] Trauer-Seiten haben keine Stufe-3-CTAs
- [ ] Maximal 3 CTAs gleichzeitig sichtbar
- [ ] Jeder CTA hat ein klares Ziel (Link oder Aktion)

### CTA-Farb-Check

    Primaer:   bg #7A6B5D, text #FFFFFF    -- CHECK
    Sekundaer: bg transparent, border #7A6B5D, text #7A6B5D -- CHECK
    Tertiaer:  text #7A6B5D, underline     -- CHECK

---

## Gate 5: Brand-Fit

### Frage
> Entspricht die Seite dem Brand von machsruhig.de in Design und Ton?

### Design-Spezifikationen

| Element        | Spezifikation                                         |
|----------------|-------------------------------------------------------|
| Hintergrund    | Creme #faf8f5                                         |
| Primaerfarbe   | Warm-Braun #7A6B5D                                    |
| Dunkel         | Tiefbraun #2D2319                                     |
| Akzent         | Dezent, nie grell                                     |
| Headlines      | Fraunces (Serif)                                      |
| Body-Text      | DM Sans (Sans-Serif)                                  |
| Font-Groesse   | Body: 16-18px, H1: 32-40px, H2: 24-28px              |
| Abstande       | Grosszuegig, Luft lassen, nie gedraengt               |
| Bilder         | Warm, natuerlich, keine Stockfotos mit falschen Laecheln |
| Icons          | Schlicht, einfarbig, passend zur Farbpalette           |

### Tonalitaet

| Eigenschaft     | Richtig                                | Falsch                                 |
|-----------------|----------------------------------------|----------------------------------------|
| Empathisch      | "Wir verstehen, dass..."               | "Sie muessen jetzt handeln!"           |
| Respektvoll     | "In dieser schweren Zeit..."           | "Tod ist ein Geschaeft"                |
| Sachlich        | "Die Kosten betragen durchschnittlich..." | "SCHOCKIEREND: So teuer ist..."     |
| Nie reisserisch | "Was Sie wissen sollten"               | "Die Wahrheit, die Bestatter verschweigen!" |
| Hilfsbereit     | "Wir helfen Ihnen Schritt fuer Schritt" | "Kaufen Sie jetzt"                    |
| Ruhig           | Klare, einfache Saetze                 | Uebertriebene Ausrufezeichen!!!        |

### Checkliste

- [ ] Hintergrundfarbe ist #faf8f5 (Creme)
- [ ] Primaerfarbe ist #7A6B5D (Warm-Braun)
- [ ] Headlines nutzen Fraunces
- [ ] Body-Text nutzt DM Sans
- [ ] Keine grellen Farben, keine Neon-Akzente
- [ ] Genug Whitespace zwischen Abschnitten
- [ ] Bilder sind warm und authentisch (keine unangemessenen Stockfotos)
- [ ] Sprache ist empathisch, respektvoll, sachlich
- [ ] Keine Ausrufezeichen in Headlines (Ausnahme: Tool-CTAs)
- [ ] Keine GROSSBUCHSTABEN-WOERTER im Content
- [ ] Anrede: "Sie" (nicht "du", ausser explizit entschieden)

---

## Gate 6: Programmatic-Sauberkeit

### Frage
> Gibt es technische Artefakte, Platzhalter oder Fehler auf der Seite?

### Pruefkriterien

Dies ist besonders wichtig fuer die programmatisch generierten Seiten (Stadtseiten, Bundesland-Seiten).

| Kriterium                                    | Bestanden                              | Durchgefallen                          |
|----------------------------------------------|----------------------------------------|----------------------------------------|
| Keine Platzhalter im Text                     | "Bestatter in Berlin"                  | "Bestatter in [STADT]"                |
| Keine undefined/null-Werte                    | Alle Felder befuellt                   | "undefined" oder "null" sichtbar       |
| Keine Template-Reste                          | Sauberer HTML-Output                   | Variablen-Syntax im Text sichtbar     |
| Keine leeren Abschnitte                       | Alle Bereiche befuellt                 | Leere Divs, fehlende Inhalte          |
| Keine doppelten Inhalte                       | Einzigartiger Text pro Stadt           | Copy-Paste ohne Anpassung             |
| Links funktionieren                           | Alle internen Links erreichbar         | 404-Fehler bei internen Links          |

### Automatisierte Checks

Platzhalter-Check: Suche nach Template-Resten in HTML-Dateien

    grep -r "[STADT]" --include="*.html"
    grep -r "undefined" --include="*.html" | grep -v "javascript"

### Checkliste

- [ ] Keine [PLATZHALTER] im sichtbaren Text
- [ ] Keine undefined, null, NaN im sichtbaren Text
- [ ] Keine Template-Variablen-Reste
- [ ] Keine leeren Sektionen oder Abschnitte
- [ ] Alle internen Links fuehren zu existierenden Seiten (kein 404)
- [ ] Stadtname korrekt geschrieben (mit Umlauten wo noetig)
- [ ] Bundesland korrekt zugeordnet (Stadt liegt im richtigen Bundesland)
- [ ] Telefonnummern/Adressen sind plausibel (keine Dummy-Daten)
- [ ] Keine doppelten Meta-Tags
- [ ] Canonical-URL ist korrekt gesetzt
- [ ] Schema.org-Markup ist valide (falls vorhanden)
- [ ] Seite laedt in unter 3 Sekunden
- [ ] Mobile-Ansicht ist nutzbar (kein horizontales Scrollen)

---

## Gate 7: Pietaet-Check (NEU)

### Frage
> Ist der Ton dieser Seite angemessen fuer den Kontext Tod, Trauer und Bestattung?

### Warum dieses Gate?

machsruhig.de behandelt eines der sensibelsten Themen ueberhaupt. Viele User befinden sich in einer emotionalen Ausnahmesituation. Jede Seite muss diesem Umstand gerecht werden -- auch Vorsorge-Seiten und Tool-Seiten.

### Pruefkriterien

| Kriterium                                    | Bestanden                              | Durchgefallen                          |
|----------------------------------------------|----------------------------------------|----------------------------------------|
| Kein unangemessener Humor                     | Sachlich, warm, respektvoll            | Wortspiele mit Tod/Sterben             |
| Keine Trivialisierung                         | "In dieser schwierigen Situation..."   | "Ist doch nicht so schlimm"            |
| Keine Angstmacherei                           | "Es kann sinnvoll sein, vorzusorgen"  | "Wenn Sie JETZT nicht handeln..."      |
| Keine Sensationslust                          | Fakten und Hilfe                       | "Schockierende Wahrheit ueber..."      |
| Kein Ausnutzen der Situation                  | Hilfe erst, Monetarisierung spaeter   | Sofort Affiliate nach Trauer-Content   |
| Angemessene Bildsprache                       | Natur, Ruhe, Geborgenheit             | Schockbilder, dramatische Szenen       |
| Kein False Urgency                            | "Wenn Sie bereit sind..."             | "Handeln Sie sofort!"                  |

### Seitentyp-spezifische Pietaet

| Seitentyp  | Pietaet-Level | Anmerkung                                          |
|------------|---------------|-----------------------------------------------------|
| Tool       | Hoch          | Tools zu Trauerthemen (Trauerrede) brauchen besondere Sorgfalt |
| Hub        | Mittel        | Warmherzig, einladend, nie vertrieblich             |
| Info       | Hoch          | Besonders bei Trauerseiten: maximale Sensibilitaet  |
| Vorsorge   | Mittel        | User plant proaktiv, aber Thema bleibt sensibel     |
| Lokal      | Mittel-Hoch   | User braucht konkrete Hilfe, oft in akuter Situation|
| Legal      | Neutral       | Sachlich-juristisch, keine Emotionalitaet noetig    |

### Verbotene Formulierungen

| Verboten                                     | Alternative                                    |
|----------------------------------------------|------------------------------------------------|
| "Profitieren Sie von..."                     | "Nutzen Sie die Moeglichkeit..."               |
| "Angebot sichern"                            | "Mehr erfahren"                                |
| "Countdown" / "Nur noch X Plaetze"           | Keine kuenstliche Verknappung                  |
| "Deal" / "Schnaeppchen"                      | Nicht verwenden                                |
| "Tod" als Clickbait                          | Sachliche Formulierung                         |
| "Bestattungs-Business"                       | "Bestattungswesen" oder "Bestattungsbranche"   |
| "Leiche" (in Marketing-Kontext)              | "Verstorbene/r"                                |
| "Kunden" (fuer Trauernde)                    | "Menschen" oder "Angehoerige"                  |
| "Verkaufen" (Bestatter-Kontext)              | "Beraten" oder "Begleiten"                     |

### Checkliste

- [ ] Kein unangemessener Humor oder Wortspiele zum Thema Tod
- [ ] Keine Trivialisierung von Trauer oder Verlust
- [ ] Keine Angstmacherei oder kuenstliche Dringlichkeit
- [ ] Keine Sensationslust in Headlines oder Teasern
- [ ] Monetarisierung nicht direkt neben Trauer-Content
- [ ] Bildsprache ist angemessen (keine dramatischen/schockierenden Bilder)
- [ ] Sprache ist warm, aber nicht aufgesetzt emotional
- [ ] Kein "False Urgency" (kuenstlicher Zeitdruck)
- [ ] Trauernde werden als "Menschen" oder "Angehoerige" bezeichnet, nicht als "Kunden"
- [ ] Bestatter werden als "Begleiter" positioniert, nicht als "Verkaeufer"

---

## QA-Ablauf

### Schritt 1: Automatisierte Checks (Gate 6)
Vor jeder manuellen Pruefung die automatisierten Checks laufen lassen.

### Schritt 2: Gate 1-5 (Inhalts- und Design-Review)
Jede Seite einzeln durch Gates 1-5 pruefen. Dokumentation in Tabelle:

    | Seite                    | G1 | G2 | G3 | G4 | G5 | G6 | G7 | Status    |
    |--------------------------|----|----|----|----|----|----|----|-----------
    | /bestattungskosten       | OK | OK | OK | OK | OK | OK | OK | LIVE      |
    | /trauerrede-schreiben    | OK | OK | -- | OK | OK | OK | OK | LIVE      |
    | /bestatter/berlin/       | OK | OK | OK | OK | FIX| OK | OK | REVIEW    |

### Schritt 3: Gate 7 (Pietaet) -- Letzter Check
Gate 7 ist der letzte Check vor dem Go-Live. Wenn eine Seite Gate 7 nicht besteht, muss sie ueberarbeitet werden -- auch wenn alle anderen Gates bestanden sind.

### Schritt 4: Stichproben nach Go-Live
Regelmaessig (monatlich) Stichproben auf:
- Funktionieren alle Tools noch?
- Sind Kostenangaben noch aktuell?
- Gibt es neue 404-Fehler?
- Sind Affiliate-Links noch gueltig?
- Wurden programmatische Seiten korrekt aktualisiert?

---

## Gate-Ergebnis-Vorlage

Fuer jede Seite vor Go-Live ausfuellen:

    Seite: ___________________________
    URL:   ___________________________
    Typ:   ___________________________
    Datum: ___________________________

    Gate 1 (Intent-Fit):          [ ] PASS  [ ] FAIL  Anmerkung: ____________
    Gate 2 (Utility):             [ ] PASS  [ ] FAIL  Anmerkung: ____________
    Gate 3 (Differenzierung):     [ ] PASS  [ ] WARN  Anmerkung: ____________
    Gate 4 (Conversion-Klarheit): [ ] PASS  [ ] FAIL  Anmerkung: ____________
    Gate 5 (Brand-Fit):           [ ] PASS  [ ] FAIL  Anmerkung: ____________
    Gate 6 (Programmatic):        [ ] PASS  [ ] FAIL  Anmerkung: ____________
    Gate 7 (Pietaet):             [ ] PASS  [ ] FAIL  Anmerkung: ____________

    Ergebnis: [ ] GO LIVE  [ ] UEBERARBEITEN  [ ] BLOCKIERT
