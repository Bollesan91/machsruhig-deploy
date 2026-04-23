# Monetarisierungsstrategie -- machsruhig.de

> Trust first. Erst Mehrwert liefern, dann monetarisieren.
> Trauerseiten bleiben IMMER frei von Monetarisierung.

---

## Grundprinzipien

1. **Respekt vor der Situation.** Viele User sind in einer emotionalen Ausnahmesituation. Monetarisierung darf das niemals ausnutzen.
2. **Trust vor Umsatz.** Qualitaetscontent und nuetzliche Tools schaffen Vertrauen. Monetarisierung folgt dem Vertrauen, nie umgekehrt.
3. **Vorsorge ist monetarisierbar.** Wer proaktiv vorsorgt, ist offen fuer Loesungen und Produkte. Das ist der Hauptkanal.
4. **Trauer ist tabu.** Trauerrede, Kondolenz, Trauersprueche -- diese Seiten werden niemals monetarisiert. Keine Ausnahme.
5. **Transparenz immer.** Jeder Affiliate-Link, jede bezahlte Empfehlung wird sichtbar gekennzeichnet.

---

## Tier 1 -- Sofort umsetzbar (Affiliate + Lead-Gen)

### 1.1 Sterbegeldversicherung-Vergleich

**Modell:** Affiliate (CPA oder CPL)

**Funktionsweise:**
1. User liest Ratgeber `/vorsorge/sterbegeldversicherung`
2. Nach 50% Content: CTA "Anbieter vergleichen"
3. User gibt Alter + Wunschsumme ein (einfaches Formular)
4. Empfehlung wird angezeigt mit Affiliate-Link zum Anbieter
5. Bei Abschluss: Provision

**Platzierung:**
- Nur auf `/vorsorge/sterbegeldversicherung`
- Als Cross-Sell nach Tool-Output (Bestattungskosten-Rechner, Vorsorge-Check)
- NICHT auf Trauerseiten
- NICHT auf der Startseite als Primaer-CTA

**Kennzeichnung:**
```html
<p class="affiliate-hinweis">
  * Werbung: Wir erhalten eine Provision, wenn Sie ueber diesen Link
  abschliessen. Fuer Sie entstehen keine Mehrkosten.
</p>
```

**Geschaetztes Potenzial:**
- CPL (Lead): 5-15 EUR pro qualifiziertem Lead
- CPA (Abschluss): 30-80 EUR pro Abschluss
- Conversion Rate geschaetzt: 1-3% der Seitenbesucher

---

### 1.2 Bestatter-Leads

**Modell:** Lead-Generierung (CPL)

**Funktionsweise:**
1. User besucht Stadtseite `/bestatter/[stadt]/`
2. Kontaktformular: Name, E-Mail, Telefon, Art der Bestattung, Zeitrahmen
3. Lead wird an lokale Bestatter in der Stadt weitergeleitet
4. Bestatter zahlt pro qualifiziertem Lead

**Platzierung:**
- Auf allen 50 Stadtseiten als Primaer-CTA
- Als Cross-Sell nach Bestattungskosten-Rechner
- Als Cross-Sell nach Checkliste Todesfall

**Formular-Felder:**
| Feld              | Typ       | Pflicht | Hinweis                        |
|--------------------|----------|---------|--------------------------------|
| Name               | Text     | Ja      |                                |
| E-Mail             | E-Mail   | Ja      |                                |
| Telefon            | Tel      | Nein    | "Fuer Rueckruf"                |
| Stadt              | Select   | Ja      | Vorbelegt aus URL              |
| Art der Bestattung | Select   | Nein    | Erd/Feuer/See/Baum/Unbekannt   |
| Zeitrahmen         | Select   | Nein    | Akut/1-4 Wochen/Vorsorge       |
| Nachricht          | Textarea | Nein    |                                |

**Datenschutz:**
- DSGVO-konformes Opt-in erforderlich
- Hinweis: "Ihre Daten werden ausschliesslich an Bestattungsunternehmen in [Stadt] weitergeleitet."
- Link zur Datenschutzerklaerung

**Geschaetztes Potenzial:**
- CPL: 10-30 EUR pro Lead (je nach Stadt und Zeitrahmen)
- "Akut"-Leads wertvoller als "Vorsorge"-Leads
- 50 Staedte x ca. 5-20 Leads/Monat = 250-1.000 Leads/Monat

---

### 1.3 Vorsorge-Dokumente (Affiliate)

**Modell:** Affiliate (CPS)

**Funktionsweise:**
1. User liest Ratgeber zu Patientenverfuegung, Testament
2. Am Ende des Ratgebers: "Rechtssichere Vorlage erstellen"
3. Link zu Vorlagen-Portal (smartlaw, Formblitz, Arag o.ae.)
4. User erstellt dort Dokument, wir erhalten Provision

**Partner-Optionen:**
| Partner      | Produkt                    | Provision geschaetzt |
|--------------|----------------------------|----------------------|
| smartlaw     | Patientenverfuegung-Vorlage | 5-15% vom Preis     |
| Formblitz    | Testament-Vorlagen          | 5-10% vom Preis     |
| Arag         | Online-Rechtsberatung       | CPL 5-20 EUR        |
| AfterLife    | Digitaler Nachlass          | CPL/CPS variabel    |

**Platzierung:**
- `/vorsorge/patientenverfuegung` -- Link zu Vorlagen-Erstellung
- `/vorsorge/testament` -- Link zu Testament-Generator
- `/vorsorge/vorsorge-ordner` -- Links zu allen Vorlagen

**Kennzeichnung:**
- Immer mit "*" und Affiliate-Hinweis
- Nie als redaktionelle Empfehlung tarnen

---

## Tier 2 -- Mittelfristig (Premium + Tools)

### 2.1 Bestattungsvorsorge-Vergleich (eigenes Tool)

**Modell:** Affiliate + Premium-Platzierung

**Funktionsweise:**
1. Eigenes Vergleichstool fuer Bestattungsvorsorge-Vertraege
2. User gibt Wuensche ein (Art, Umfang, Budget)
3. Tool zeigt passende Vorsorge-Vertraege verschiedener Anbieter
4. Klick auf Anbieter = Affiliate-Link
5. Premium-Platzierung fuer Anbieter (bezahlt)

**Voraussetzungen:**
- Recherche: Bestattungsvorsorge-Anbieter und deren Konditionen
- Datenbank: Anbieter, Tarife, Leistungen
- Technik: Vergleichsrechner-Logik
- Rechtlich: Keine Beratung, nur Vergleich

**Zeitrahmen:** 3-6 Monate Entwicklung

**Geschaetztes Potenzial:**
- CPL: 20-50 EUR pro qualifiziertem Lead
- CPA: 50-200 EUR pro Abschluss
- Vorsorge-Markt waechst stetig

---

### 2.2 Premium Vorsorge-Ordner (Lead-Magnet)

**Modell:** Lead-Magnet (E-Mail gegen PDF)

**Funktionsweise:**
1. User besucht `/vorsorge/vorsorge-ordner`
2. CTA: "Kompletten Vorsorge-Ordner als PDF herunterladen"
3. User gibt E-Mail-Adresse ein
4. Erhaelt PDF mit allen Vorsorge-Checklisten und Vorlagen
5. Follow-up E-Mails: Vorsorge-Tipps + Affiliate-Angebote

**Inhalt des Vorsorge-Ordners (PDF):**
- Checkliste: Vorsorge-Status pruefen
- Vorlage: Patientenverfuegung-Entwurf
- Vorlage: Testament-Entwurf
- Checkliste: Wichtige Dokumente sammeln
- Uebersicht: Sterbegeldversicherung-Vergleich
- Kontaktliste: Wichtige Ansprechpartner

**Datenschutz:**
- DSGVO-konformes Double-Opt-in
- Abmeldelink in jeder E-Mail
- Keine Weitergabe der E-Mail an Dritte

**Geschaetztes Potenzial:**
- E-Mail-Liste: Wertvoller Kanal fuer langfristige Monetarisierung
- Conversion zu Affiliate: 5-10% der E-Mail-Empfaenger
- Lead-Nurturing ueber Monate moeglich

---

### 2.3 Bestatter-Verzeichnis (Freemium)

**Modell:** Freemium (Basis-Eintrag gratis, Premium kostenpflichtig)

**Funktionsweise:**

| Tier     | Leistung                                     | Preis/Monat     |
|----------|-----------------------------------------------|-----------------|
| Basis    | Name, Adresse, Telefon                        | Kostenlos       |
| Standard | + Logo, Oeffnungszeiten, 3 Fotos, Link       | 29-49 EUR       |
| Premium  | + Bewertungen anzeigen, Top-Platzierung, Badge | 79-149 EUR     |

**Voraussetzungen:**
- Bestatter-Datenbank aufbauen (Start: 50 Staedte, je 3-10 Bestatter)
- CMS fuer Bestatter-Profile
- Verifizierungs-Prozess
- Vertrieb: Bestatter ansprechen

**Zeitrahmen:** 6-12 Monate

---

## Tier 3 -- Langfristig (Plattform)

### 3.1 Online-Bestattungsvorsorge

**Modell:** Plattform (Transaktionsgebuehr oder SaaS)

**Vision:**
- Kompletter digitaler Vorsorge-Prozess auf machsruhig.de
- User konfiguriert Bestattungswuensche online
- Bekommt verbindliches Angebot von Partner-Bestattern
- Schliesst Vorsorge-Vertrag digital ab

**Zeitrahmen:** 12-24 Monate
**Voraussetzungen:** Bestatter-Netzwerk, rechtliche Pruefung, sichere Zahlungsabwicklung

---

### 3.2 Bestatter-Bewertungen

**Modell:** Bewertungsportal (Reichweite + Premium-Listings)

**Vision:**
- User koennen Bestatter bewerten (nach Erfahrung)
- Bewertungen auf Stadtseiten anzeigen
- Bestatter mit guten Bewertungen erhalten mehr Anfragen
- Premium-Bestatter koennen auf Bewertungen antworten

**Zeitrahmen:** 12-18 Monate
**Voraussetzungen:** Moderations-System, Verifizierung, Rechtsabklaerung (Bewertungsrecht)

---

### 3.3 Trauer-Begleitung (Newsletter/Community)

**Modell:** Newsletter + perspektivisch Community

**Vision:**
- Woechentlicher Newsletter: Trauer-Tipps, Vorsorge-Infos
- Langfristiger Vertrauensaufbau
- Perspektivisch: Geschlossene Community fuer Trauernde

**Monetarisierung:**
- Newsletter: Gesponserte Inhalte (dezent, gekennzeichnet)
- Community: Freemium-Zugang
- WICHTIG: Trauer-Community darf NIEMALS aggressiv monetarisiert werden

**Zeitrahmen:** 6-12 Monate (Newsletter), 18+ Monate (Community)

---

## Monetarisierungs-Regeln (verbindlich)

### Regel 1: Trauerseiten-Schutz

| Seite                    | Monetarisierung | Begruendung                        |
|--------------------------|-----------------|------------------------------------|
| /trauerrede-schreiben    | VERBOTEN        | Trauer-Kontext                     |
| /tools/trauerrede        | VERBOTEN        | Trauer-Kontext                     |
| /kondolenzschreiben      | VERBOTEN        | Trauer-Kontext                     |
| /trauersprueche          | VERBOTEN        | Trauer-Kontext                     |

Keine Affiliate-Links, kein Lead-Gen, keine Werbung, keine gesponserten Inhalte. Keine Ausnahme.

### Regel 2: Vorsorge-Seiten duerfen monetarisiert werden

| Seite                             | Monetarisierung  | Erlaubte Formen                    |
|-----------------------------------|------------------|------------------------------------|
| /vorsorge/sterbegeldversicherung  | ERLAUBT          | Affiliate (Vergleich)              |
| /vorsorge/patientenverfuegung     | ERLAUBT          | Affiliate (Vorlagen)               |
| /vorsorge/testament               | ERLAUBT          | Affiliate (Vorlagen)               |
| /vorsorge/vorsorge-ordner         | ERLAUBT          | Lead-Magnet (PDF)                  |

Begruendung: User plant proaktiv und ist offen fuer Loesungen.

### Regel 3: Tool-Seiten nach Output

| Seite                             | Vor Output       | Nach Output                        |
|-----------------------------------|------------------|------------------------------------|
| /tools/bestattungskosten-rechner  | KEINE Monetaris. | Sterbegeld-Affiliate erlaubt       |
| /tools/vorsorge-check             | KEINE Monetaris. | Vorsorge-Cross-Sell erlaubt        |
| /tools/checkliste-todesfall       | KEINE Monetaris. | Bestatter-Lead erlaubt             |
| /tools/beerdigungsplaner          | KEINE Monetaris. | Bestatter-Lead erlaubt             |
| /tools/kostenrechner              | KEINE Monetaris. | Sterbegeld-Affiliate erlaubt       |
| /tools/trauerrede                 | KEINE Monetaris. | KEINE Monetaris. (Trauer)          |

### Regel 4: Lokal-Seiten

| Seite                    | Monetarisierung  | Erlaubte Formen                    |
|--------------------------|------------------|------------------------------------|
| /bestatter/[stadt]/      | ERLAUBT          | Bestatter-Leads, Premium-Listings  |
| /bestattung-in/[bl]/     | EINGESCHRAENKT   | Nur Verlinkung auf Stadtseiten     |

### Regel 5: Kennzeichnungspflicht

```
Affiliate-Links:
  - Im Text: "*" nach dem Link-Text
  - Im Footer der Seite: "* Affiliate-Link / Werbung"
  - Tooltip/Title-Attribut: "Werbelink -- wir erhalten eine Provision"

Gesponserte Inhalte:
  - Deutlich sichtbar: "Anzeige" oder "Gesponsert"
  - Nie als redaktioneller Content tarnen

Lead-Gen-Formulare:
  - DSGVO-Opt-in
  - Klar benennen, wer die Daten erhaelt
  - Link zur Datenschutzerklaerung
```

### Regel 6: Keine aggressive Werbung

```
VERBOTEN:
- Pop-ups mit Monetarisierungsinhalt
- Exit-Intent-Overlays mit Angeboten
- Countdown-Timer ("Nur noch heute!")
- Blinkende oder animierte Werbebanner
- Auto-Play-Videos mit Werbung
- Native Ads, die wie Content aussehen
- Preisvergleiche auf Trauerseiten

ERLAUBT:
- Dezente Affiliate-Links im Fliesstext
- CTA-Buttons nach Content (Stufe 3)
- Cross-Sell-Boxen am Seitenende
- Statische Hinweis-Boxen auf Vorsorge-Seiten
```

---

## Umsatz-Prognose (konservativ)

### Tier 1 (ab Monat 1-3)

| Kanal                      | Monatliche Visits | Conv. Rate | CPL/CPA    | Umsatz/Monat |
|----------------------------|-------------------|-----------|------------|--------------|
| Sterbegeld-Affiliate       | 2.000             | 1-2%      | 15-50 EUR  | 300-2.000    |
| Bestatter-Leads            | 5.000             | 2-4%      | 10-30 EUR  | 1.000-6.000  |
| Vorsorge-Dokument-Affiliate| 1.500             | 1-2%      | 5-15 EUR   | 75-450       |
| **Gesamt Tier 1**          |                   |           |            | **1.375-8.450** |

### Skalierung (ab Monat 6-12)

| Kanal                      | Monatliche Visits | Conv. Rate | CPL/CPA    | Umsatz/Monat |
|----------------------------|-------------------|-----------|------------|--------------|
| Sterbegeld-Affiliate       | 8.000             | 2-3%      | 15-50 EUR  | 2.400-12.000 |
| Bestatter-Leads            | 15.000            | 3-5%      | 15-30 EUR  | 6.750-22.500 |
| Vorsorge-Dokument-Affiliate| 5.000             | 1-2%      | 5-15 EUR   | 250-1.500    |
| Bestatter-Verzeichnis      | --                | --        | 29-149/Mon | 500-5.000    |
| Lead-Magnet (E-Mail)       | 3.000             | 5%        | --         | Langfristwert|
| **Gesamt skaliert**        |                   |           |            | **9.900-41.000** |

*Alle Zahlen sind Schaetzungen und haengen stark vom organischen Traffic ab.*

---

## Implementierungs-Reihenfolge

### Phase 1 (Sofort -- Woche 1-4)
1. Affiliate-Kennzeichnung auf allen Seiten implementieren
2. Sterbegeld-Vergleichs-CTA auf /vorsorge/sterbegeldversicherung
3. Affiliate-Links fuer Patientenverfuegung + Testament einbauen

### Phase 2 (Kurzfristig -- Monat 2-3)
4. Bestatter-Kontaktformular auf Stadtseiten implementieren
5. Lead-Weiterleitung an lokale Bestatter einrichten
6. Cross-Sell-Links nach Tool-Output implementieren

### Phase 3 (Mittelfristig -- Monat 3-6)
7. Vorsorge-Ordner PDF erstellen (Lead-Magnet)
8. E-Mail-System aufsetzen (Double-Opt-in, Nurturing)
9. Bestattungsvorsorge-Vergleich konzipieren

### Phase 4 (Langfristig -- Monat 6+)
10. Bestatter-Verzeichnis aufbauen
11. Bewertungssystem entwickeln
12. Newsletter + Community evaluieren
