# Session-Notizen

## Letzte Session
**Datum:** 23. April 2026 (Nachmittag/Abend, Bundesländer-Sprint)
**Deploy-Status:** Alle Änderungen mit "ende deploy" gepusht und deployed.

## Was wurde gemacht

### ✅ 5 von 16 Bundesländer-Seiten komplett überarbeitet

Jede Seite wurde von ~350 Wörtern auf ~1700-2400 Wörter ausgebaut, mit
strikter Primärquellen-Orientierung, korrekten Paragraphen-Verweisen,
konkreten Städte-/Friedhofsdaten und dem einheitlichen Schema-Set
WebPage + Place + Article + BreadcrumbList + FAQPage.

**Audit-Score jeweils von ~54-71 auf 85/100.**
**Re-Check jeweils 0 Blocker, 0 Warnungen.**

| Bundesland | Commit | Wörter | Quellen | §-Ref | Score |
|---|---|---|---|---|---|
| Baden-Württemberg | `3aa73c5` | 2359 | 32 | 23 | 85 |
| Mecklenburg-Vorpommern | `ee6df0b` | 1832 | 23 | 25 | 85 |
| Sachsen-Anhalt | `9adb45a` | 1785 | 21 | 19 | 85 |
| Thüringen | `f9b3cad` + `a6e6009` | 1744 | 19 | 32 | 85 |
| **Brandenburg** | `e529f2d` | 1751 | 22 | 34 | 85 |

### ✅ Audit-Skript rekalibriert (Commit `a1a3db9`)

`_dev/audit-all-pages.py` bekam einen `PRE_LAUNCH_MODE`-Flag, der
Bundesland/Content-Seiten ohne Monetarisierungs-Penalty bewertet,
solange Phase F (Monetarisierung) noch nicht aktiv ist. Sobald Phase F
rollt, muss `PRE_LAUNCH_MODE = False` gesetzt werden — dann spiegeln
die Scores die volle Monetarisierungs-Realität.

### ✅ Plausible-Tracking zentralisiert (Commit `5493cee`)

Init-Code und Plausible-Script-Tag in `js/tracking.js` verschoben.
Alle überarbeiteten Seiten verweisen jetzt nur noch auf diese eine
Datei statt jeweils eigenen Init-Code zu enthalten.

### ✅ Re-Check-Skript neu: `_dev/bundesland-recheck.py` (Commit `a6e6009`)

Automatisierter Ehrlichkeits-Check, der den Audit-Score ergänzt und
speziell auf **Sachrichtigkeit** prüft. Checks:
- Content-Umfang (≥ 1200 Wörter)
- §-Referenzen (≥ 8)
- Externe Primärquellen (≥ 10)
- Pietätlosigkeiten ("touristische Bestattung" etc.)
- Unbelegte Superlative (Krematoriums-Ränge, "einzige in Deutschland")
- Städte aus falschem Bundesland (Lübeck-in-MV-Fehler-Detektor)
- Sekundärquellen ohne Markierung (bestattung-information.de u.a.)
- Template-Sachfehler ("Sargpflicht: Nein", "Mindestfrist 24h" etc.)
- Landesrecht-Volltext-Link vorhanden

Aufruf: `python3 _dev/bundesland-recheck.py <pfad>` oder `--all`.
Bei den 11 noch unbearbeiteten Bundesländer-Seiten meldet das Skript
zusammen ~21 Blocker und ~44 Warnungen — diese Seiten dürfen also NICHT
live gehen, auch wenn der Audit-Score bei 71-81 liegt.

### ✅ GO-LIVE-CHECKLIST erweitert

`GO-LIVE-CHECKLIST.md` hat jetzt:
- **Re-Check als festen Blocker-Schritt** (Abschnitt A.0)
- **Begriffspräzisions-Kriterium** (z.B. "Grabanlagen" ≠ "Grabstätten"
  in Primärquellen)
- **9-Schritte-Workflow** für jede neue Bundesländer-Überarbeitung
  (Recherche → Content → Struktur → Audit → Re-Check → manueller
  Re-Check → Stufe-1 Gate → Commit mit [skip netlify] → auf
  "ende deploy" warten)

### ✅ Selbstkritischer Re-Check der 4 fertigen Seiten

Nach Bolles Aufforderung "check nochmal ob die 4 scores berechtigt sind"
wurde Thüringen nachgeschärft, weil bei ehrlicher Prüfung Stellen
aufgefallen waren, die noch nicht 85-Niveau hatten:
- "43.800 Grabstätten" → "43.800 Grabanlagen" (Primärquelle-Wortlaut)
- "1897 das fünfte Krematorium Deutschlands" → relativiert zu "ein
  frühes Krematorium" (Rang nur durch Wikipedia belegt)
- Süddeutsch-Vergleich entfernt (unbelegt)
- "Thüringer Besonderheit" → "Merkmal" (Differenzierung gibt's anderswo)
- Erfurt-Gebühren explizit als Sekundärportal markiert

BW, MV, LSA, TH sind damit ehrlich 85, nicht nur Audit-85.

## Workflow-Lehren dieser Session

1. **Audit-Score allein genügt nicht für Go-Live.** Der Score misst
   Struktur/SEO/Schema, aber nicht Sachrichtigkeit. Der neue Re-Check
   ergänzt diese Lücke.
2. **Primärquellen-Wortlaut bleibt Primärquellen-Wortlaut.** Selbst
   kleine Umformulierungen ("Grabanlagen" → "Grabstätten") können
   die Bedeutung verschieben.
3. **Sekundärquellen als solche markieren.** Wenn Gebühren nicht aus
   der Original-Gebührensatzung, sondern aus einem Verzeichnisportal
   stammen, gehört das transparent in den Text.
4. **"ende deploy"-Trigger strikt respektieren.** Die 8 Session-Commits
   wurden alle mit [skip netlify] gepusht; erst auf explizites Signal
   wurde ein Deploy-Commit erzeugt.

## Nächste Schritte

### Bundesländer-Seiten: 11 weitere zu überarbeiten

Sortiert nach Dringlichkeit (Blocker-Anzahl beim Re-Check, abstufend
von Audit-Score):

| Nächste | Audit | Re-Check Blocker |
|---|---|---|
| Bremen | 81 | 3 |
| Niedersachsen | 80 | 3 |
| Sachsen | 71 | 3 |
| Hamburg | 71 | 2 |
| Schleswig-Holstein | 79 | 2 |
| Berlin | 81 | 2 |
| Rheinland-Pfalz | 80 | 2 |
| NRW | 78 | 1 |
| Bayern | 81 | 1 |
| Hessen | 80 | 1 |
| Saarland | 71 | 1 |

Empfehlung für nächste Session: **Sachsen** — inhaltlich spannend, weil
Sachsen mit Bayern noch zu den restriktiven Bundesländern bei der
Sargpflicht gehört (Gegenstück zur LSA-Reform vom September 2025).

### Weitere offene Punkte (aus BACKLOG)

- **Vorsorge-Ordner:** strategische Entscheidung fällig — die
  "Kommt bald"-Platzhalter sind YMYL-fragwürdig
- **10 Tool-Seiten** warten auf A.3 Static-Shell-Umbau
- **PRE_LAUNCH_MODE auf False** setzen, sobald Phase F aktiv rollt
- **17 kaputte interne Links sitewide** (Phase D)
- **sitemap.xml stale** (45 noindex-Städte, Phase D)
- **B.2.2 Reviewer-Zeile aktivieren**, wenn Fachpool real
- **D.2.1 Gold-Städte** auf Score ≥ 85 mit FuneralHome-Schema

## Offene Fragen

Keine aktuell.
