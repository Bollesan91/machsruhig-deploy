# Session-Notiz machsruhig-deploy

**Datum:** 01.04.2026
**Letzter Commit:** b80b431 (Top-5-Stadtseiten angereichert)
**Branch:** main
**Undeployed Commits:** 4 (seit 95462b0)

## Was wurde in dieser Session gemacht

### Prio 1 — Impressum + Datenschutz
- Impressum + Datenschutz mit echten Rechtsinhalten befuellt (Marie-Therese Bollweg, Immenseeweg 12a, 22149 Hamburg)
- Referenz: machsleicht-deploy

### Prio 2 — Qualitaetspruefung
- 162 Dateien automatisiert geprueft (0 Fehler nach Fixes)
- PageSpeed Insights: Best Practices 100, SEO 100, Barrierefreiheit 92
- WCAG-AA-Kontraste auf allen 88 HTML-Seiten korrigiert (4 Farbwerte)
  - #8C7E6F -> #73655A (text-muted)
  - #A69279 -> #7A6B5D (warm)
  - #B8956A -> #866E45 (accent)
  - #B8B0A6 -> #73655A (footer)
- GSC Sitemap erfolgreich eingereicht
- Schema.org auf 45 Stadt-Seiten nachgeruestet

### Prio 3 — Navigation + Verlinkung
- Navigation um Kondolenz, Trauerspueche, Vorsorge-Check erweitert (alle 88 Seiten)
- Mobile Hamburger-Menu auf allen generierten Seiten ergaenzt
- Footer-Links um 5 neue Themen ergaenzt
- Cross-Links zwischen 9 Content-Seiten eingebaut
- llms.txt komplett aktualisiert

### Neue Tools (NICHT deployed)
- Bestattungskosten-Rechner: /tools/bestattungskosten-rechner (3-Schritt-Wizard, 16 Bundeslaender, regionaler Multiplikator)
- Trauerrede-Generator: /tools/trauerrede (5-Schritt-Baukasten, 4 Tonalitaeten, 11 Zitate, editierbarer Entwurf)
- Homepage: Topic-Cards jetzt klickbar, kein "Bald verfuegbar" mehr

### Performance + Infrastruktur (NICHT deployed)
- Font-Preloading auf allen 85 Seiten
- robots.txt
- _headers (Security + Cache-Control)
- _redirects (Trailing-Slash + alte Links)
- 404.html (eigene Fehlerseite)

### Top-5-Stadtseiten (NICHT deployed)
- Berlin, Hamburg, Muenchen, Koeln, Frankfurt mit echtem lokalen Content angereichert
- 2 unabhaengige Experten-Agenten haben Faktencheck durchgefuehrt
- Frankfurt: HessBestG-Datum korrigiert (ab 01.01.2026, nicht Sept. 2025)

## Was als naechstes zu tun ist

1. **Deploy** — 4 Commits warten auf Freigabe. User ist kostenbewusst bei Deploys!
2. **Visuelle Tests** — Neue Tools im Browser durchklicken (erst nach Deploy moeglich)
3. **Lead-Formular Backend** — Formulare senden nirgendwo hin. Braucht User-Entscheidung (Netlify Forms / Formspree / Mailto)
4. **Plausible Events** — Conversion-Tracking einrichten
5. **Restliche 45 Stadtseiten** — Template-Content anreichern (niedrige Prio)
6. **Visuelle Inhalte** — SVG-Illustrationen fuer mehr Vertrauen

## Wichtige Regeln

- Commits IMMER mit [skip netlify] — Deploy NUR auf ausdrueckliche Freigabe
- Keine Deploys vorschlagen — User entscheidet
- Git-User: Bollesan91 / cbollweg@gmx.de
- Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
- Commit-Sprache: Deutsch
