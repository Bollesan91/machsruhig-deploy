# Go-Live-Checkliste — machsruhig.de YMYL-Seiten

> Diese Checkliste ersetzt eine rein numerische Audit-Score-Hürde.
> Eine Seite geht **nicht** live, solange auch nur EIN Punkt offen ist.
>
> Hintergrund: Der Audit-Score (`_dev/audit-all-pages.py`) prüft Technik
> und SEO-Struktur, aber nicht Sachrichtigkeit, Ethik oder Ton. Eine
> Seite mit Score 85 kann trotzdem einen §-Verweis falsch zitieren oder
> einen Stadtnamen ins falsche Bundesland legen (siehe MV alte Version:
> "FriedWald Lübeck-Umgebung" — Lübeck liegt in SH). Die Zahl lügt nicht,
> aber sie misst nicht alles.

Stand: 23. April 2026

---

## A) Inhaltliche Sachrichtigkeit (BLOCKER)

- [ ] **Automatischer Re-Check durchlaufen:**
      `python3 _dev/bundesland-recheck.py <pfad>` → 0 Blocker
- [ ] **Jede Rechtsaussage** ist mit einem konkreten Paragraphen belegt
      (z.B. "§ 15 BestattG M-V", nicht "laut Gesetz")
- [ ] **Jede Jahreszahl, jeder Flächen-/Mengenwert, jede Kostenspanne**
      stammt aus einer identifizierbaren Primärquelle und ist im Text
      oder im Quellenblock verlinkt
- [ ] **Keine erfundenen Fakten** — wenn eine Information nicht belegbar
      ist, wird sie entweder weggelassen oder transparent als Unsicherheit
      gekennzeichnet ("Belastbare Gesamtzahlen direkt bei X anfragen")
- [ ] **Geografische Prüfung**: Alle erwähnten Städte liegen tatsächlich
      im beschriebenen Bundesland (Beispiel-Fehler: Lübeck als
      MV-Nachbarort statt korrekt SH)
- [ ] **Aktualität**: Gesetzes-Stände, Friedhofssatzungen und Kostenwerte
      sind nicht älter als 2 Jahre oder mit dieser Einschränkung versehen
- [ ] **Begriffspräzision**: Wörter aus Primärquellen nicht umformulieren,
      ohne die Bedeutungsverschiebung zu prüfen (z.B. "Grabanlagen" ≠
      "Grabstätten" in Erfurt-Primärquelle)

## B) Ethischer YMYL-Check (BLOCKER)

- [ ] **Keine pietätlosen Formulierungen** — Trauer- und Bestattungsthemen
      werden mit der gebotenen Würde behandelt (Negativbeispiel:
      "Touristische Seebestattungen, Ostseeurlaub + Trauerfeier")
- [ ] **Kein manipulativer Druck** auf Trauernde — kein "Jetzt sofort
      buchen!", keine Countdown-Elemente, keine Scarcity-Tricks
- [ ] **Cross-Sell/Monetarisierung** ist sachlich und informativ, nicht
      aufdringlich — wenn überhaupt vorhanden in der aktuellen Phase
- [ ] **Barrierefreiheit**: Seite ist mit Tastatur navigierbar, skip-link
      vorhanden, Kontraste lesbar

## C) Technische Mindestkriterien (BLOCKER)

- [ ] **0 Strukturfehler** (HTML-Validator, `validate-all.sh` Stufe 1)
- [ ] **Stufe 1 Quality Gate PASSED** (`bash validate-all.sh`)
- [ ] **Canonical-URL korrekt** und absolut auf machsruhig.de
- [ ] **Meta-Title 50-65 Zeichen**, Meta-Description 140-165 Zeichen
- [ ] **OG-Image referenziert** und existiert physisch (`/assets/og-image.png`)
- [ ] **Schema.org-Validität**: JSON-LD parst ohne Fehler, Kategorie-
      relevante Typen vorhanden (Bundesland: WebPage + Place + Article)
- [ ] **Keine JSX-Leaks** im Static-HTML (= kein client-side Babel bei
      Content-Seiten)

## D) Redaktionelle Transparenz (WÜNSCHENSWERT, nicht blockend)

- [ ] **Autoren-Block** vorhanden ("Redaktion machsruhig.de · Stand: …")
- [ ] **Stand-Datum** stimmt mit tatsächlichem letzten Review überein
- [ ] **Link zur Methodik-Seite** am Seitenende
- [ ] **Quellenblock** mit mindestens 5 Primärquellen-Links bei YMYL-Seiten
- [ ] **Interessenkonflikt-Hinweis**, wenn Affiliate-Links vorhanden sind

## E) Audit-Score als Orientierungspunkt (nicht als Hürde)

Der Audit-Score ist **ein** Signal unter vielen. Eine seriöse Bandbreite:

| Score | Bedeutung |
|---|---|
| **< 70** | Technische oder strukturelle Mängel sind wahrscheinlich |
| **70-79** | Solide Basis, aber mindestens ein Abschnitt A–D lückenhaft |
| **80-89** | Produktionsreif, wenn A+B+C komplett abgehakt |
| **90+** | Nur mit aktiver Monetarisierung (Phase F) erreichbar |

**Wichtig:** Score 90+ bedeutet nicht automatisch "besser". In Pre-Launch
ist eine Seite mit Score 85 und vollständigen Abschnitten A+B+C **live-
tauglicher** als eine Seite mit Score 95, die einen Sachfehler enthält.

Eine Seite geht live, wenn **A+B+C komplett** sind — unabhängig vom Score.
Die 80/85/95-Marke ist Orientierung, nicht Gatekeeper.

---

## Zusatz: Sonderfall Bundesland-Seiten (YMYL-Recht)

Bei Bundesland-Seiten gilt zusätzlich zu A-E:

- [ ] **Landesbestattungsgesetz** mit Titel, Datum der letzten Änderung
      und Link zum Volltext (landesrecht-*.de oder gesetze-im-internet.de)
- [ ] **Mindestruhezeit** mit § belegt
- [ ] **Sargpflicht-Regelung** mit § belegt, inkl. Ausnahmen
- [ ] **Bestattungsfristen** (Minimal, Maximal) mit § belegt
- [ ] **Leichenschau-Regelung** mit § belegt
- [ ] **Mindestens 2 Städte** des Bundeslandes mit konkreten
      Friedhofsdaten (Fläche, Eröffnungsjahr, Krematorium ja/nein) aus
      Stadt-Primärquellen (nicht Bestatter-Portale)
- [ ] **Mindestens 1 Alleinstellungsmerkmal** des Bundeslandes heraus-
      gearbeitet (MV: Sargpflicht-Abschaffung; BW: früheste Einäscherungs-
      Reform 2014; Bayern: Sargpflicht streng; etc.)

---

## Arbeitsrhythmus für die 14 übrigen Bundesländer

Bis alle 16 Bundesländer-Seiten live sind, gilt:

1. Score allein qualifiziert **nicht** zum Go-Live
2. Für jede Bundesland-Seite wird dieser Checklisten-Durchlauf dokumentiert
3. Nach Phase F wird PRE_LAUNCH_MODE im Audit-Skript auf False gesetzt
   — dann spiegeln die Scores wieder die volle Monetarisierungs-Realität

## Workflow für jede neue Bundesländer-Überarbeitung

Der erprobte Ablauf aus BW/MV/LSA/TH:

1. **Recherche** (primärquellengestützt, 3-5 Web-Suchen):
   - Landesbestattungsgesetz (landesrecht-<BL>.de)
   - Gesetzesänderungen und Reformen (Presseportale der Landesregierung)
   - Städte-Primärquellen (Friedhofsverwaltung, Stadtportale)
   - Aeternitas-Übersicht und Wikipedia zum Gegencheck
2. **Content schreiben** — strikt mit §-Referenz zu jeder Rechtsaussage
3. **Struktur + Schema + Meta-Tags** auf BW/MV/LSA/TH-Niveau bringen
4. **Audit-Score** via `python3 _dev/audit-all-pages.py` prüfen
5. **Automatischer Re-Check** via `python3 _dev/bundesland-recheck.py <pfad>`
   — muss 0 Blocker zeigen
6. **Manueller Re-Check**: Ich lese die Seite gegen die Primärquellen nochmal
   kritisch durch und suche aktiv nach folgenden Fallen:
   - Wortabweichungen von der Primärquelle (z.B. "Grabstätten" statt "Grabanlagen")
   - Unbelegte Superlative ("erstes", "einzige", "strengste")
   - Sekundärquellen (Bestatter-Verzeichnisse) als Primärquellen getarnt
   - Annahmen als Fakten ("tendenziell moderater als süddeutsch")
7. **Stufe-1 Quality Gate** via `bash validate-all.sh`
8. **Commit** mit `[skip netlify]` — kein Auto-Deploy
9. Warten auf explizites "ende deploy" von Bolle
