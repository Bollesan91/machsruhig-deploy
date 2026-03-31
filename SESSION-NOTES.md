# Session-Notizen

## Letzte Session
**Datum:** 31. März 2026

## Was wurde gemacht
- PBI-3: DNS für machsruhig.de konfiguriert (INWX → Netlify)
  - Root A-Record → 75.2.60.5 (Netlify Load Balancer)
  - www CNAME → machsruhig.netlify.app
  - Wildcard (*) Record gelöscht
  - DNS-Verifizierung bei Netlify erfolgreich
  - SSL-Zertifikat (Let's Encrypt) angefordert, wartet auf Propagierung
- PBI-10: Fonts self-hosted (DM Sans + Fraunces als woff2, Google Fonts CDN entfernt — DSGVO-konform)
- PBI-6: sitemap.xml erstellt (3 Seiten: /, /impressum, /datenschutz)
- PBI-7: llms.txt erstellt (für AI-Crawler)
- PBI-21: Navigation/Header eingebaut (sticky, Cluster-Logik, Mobile Hamburger)
- PBI-22: Footer eingebaut (3-spaltig: Über uns, Themen, Rechtliches + Trust-Hinweise)
- Impressum + Datenschutz-Seiten auf self-hosted Fonts + einheitliches Layout umgestellt
- Git-Sync Skill aktualisiert: "Ende" = push ohne Deploy, "Ende deploy" = push mit Deploy
- Git für Windows auf Hannes' Rechner installiert (winget)

## Nächste Schritte
- SSL-Zertifikat prüfen (sollte inzwischen provisioniert sein)
- Alte Netlify-Projekte aufräumen (grand-wisp-519023 und bucolic-sprinkles-d7fe98)
- PBI-13/14/15: Templates erstellen (Info-, Tool-, Stadt-Seiten)
- PBI-16: Methodik-Seite
- PBI-17/18/19: Tracking (GSC, Analytics, Events)
- Danach: Content-Epics E1–E8 beginnen

## Offene Fragen
- Welches Analytics-Tool? (Plausible vs. GA4)
- Impressum-Daten noch ausstehend (TMG-Angaben)
- Datenschutzerklärung noch Platzhalter

## Erledigte PBIs (gesamt)
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 21, 22
