#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R8 — Methodik + Datenschutz (Trust):
1. Tool-Datenschutz-Matrix pro Tool, IDENTISCH auf /methodik und /datenschutz
   (gleiche Begriffe, Roadmap-Soll #36/#37). Datenfluesse aus Code-Inventar:
   localStorage: checkliste-todesfall, fristen-radar, beerdigungsplaner,
   abschiedsbrief; Netlify-Forms: beerdigungsplaner, bestattungskosten-rechner,
   vorsorge-check; KI (mr-ai.js -> Netlify-Fn -> Groq): trauerrede, danksagung,
   abschiedsbrief; alles andere rein clientseitig.
2. Methodik: letzte Pruefdaten je Inhalts-Cluster ergaenzt.
3. Danksagung-Tool: Falschsatz "Umami nur nach Cookie-Opt-In" -> konsistent
   mit Datenschutz §9 (cookielos, berechtigtes Interesse). (Punkt-Fix aus dem
   Consent-PBI; das Banner-Modell selbst bleibt eigener Arbeitsblock.)
"""
import io, sys

def rep_in(path, old, new, expect=1):
    t = io.open(path, encoding='utf-8').read()
    c = t.count(old)
    if c != expect:
        print('FATAL %s: %r -> %d (erwartet %d)' % (path, old[:60], c, expect)); sys.exit(1)
    io.open(path, 'w', encoding='utf-8', newline='').write(t.replace(old, new))

MATRIX = '''<div class="mr-table-wrap" style="margin:16px 0">
      <table class="mr-table" style="font-size:13.5px">
        <thead><tr><th>Tool</th><th>Eingaben bleiben im Browser?</th><th>Lokale Speicherung auf deinem Gerät?</th><th>Wird etwas übertragen?</th></tr></thead>
        <tbody>
          <tr><td>Checkliste Todesfall</td><td>ja</td><td>ja — dein Abhak-Stand (localStorage, jederzeit löschbar)</td><td>nein</td></tr>
          <tr><td>Bestattungskosten-Rechner</td><td>ja</td><td>nein</td><td>nur, wenn du aktiv das optionale Anfrage-Formular absendest</td></tr>
          <tr><td>Kostenrechner (Schnell-Version)</td><td>ja</td><td>nein</td><td>nein</td></tr>
          <tr><td>Angebotsprüfer</td><td>ja</td><td>nein</td><td>nein</td></tr>
          <tr><td>Fristen-Radar</td><td>ja</td><td>ja — dein Abhak-Stand (localStorage)</td><td>nein</td></tr>
          <tr><td>Beerdigungsplaner</td><td>ja</td><td>ja — dein Planungsstand (localStorage)</td><td>nur, wenn du aktiv das optionale Formular absendest</td></tr>
          <tr><td>Vorsorge-Check</td><td>ja</td><td>nein</td><td>nur, wenn du aktiv das optionale Formular absendest</td></tr>
          <tr><td>Notfallkarte</td><td>ja</td><td>nein</td><td>nein — auch der Druck erfolgt lokal</td></tr>
          <tr><td>Trauerrede / Danksagung / Abschiedsbrief</td><td>ja (Grundfunktion)</td><td>nur Abschiedsbrief: dein Entwurf (localStorage)</td><td>nur der optionale KI-Entwurf: nach ausdrücklicher Einwilligung und Klick auf „Generieren" an unsere Server-Funktion und Groq, Inc. (USA)</td></tr>
        </tbody>
      </table>
    </div>'''

# --- 1a. Datenschutz §6: Matrix nach dem ersten Absatz ---
rep_in('datenschutz.html',
  '''<p>Eine Ausnahme gilt für die optionalen KI-Textentwürfe in den Tools Trauerrede, Danksagung und Abschiedsbrief — diese beschreibt der folgende Abschnitt.</p>''',
  '''<p>Im Einzelnen, mit denselben Begriffen, die auch auf den Tool-Seiten stehen:</p>
  ''' + MATRIX + '''
  <p>„Lokale Speicherung" bedeutet: Die Daten liegen ausschließlich im Speicher deines eigenen Browsers (localStorage) und lassen sich dort jederzeit von dir löschen — wir haben darauf keinen Zugriff. Eine Ausnahme von „alles bleibt im Browser" gilt nur für die optionalen KI-Textentwürfe in den Tools Trauerrede, Danksagung und Abschiedsbrief — diese beschreibt der folgende Abschnitt.</p>''')

# --- 1b. Methodik: dieselbe Matrix in der Tools-Sektion ---
rep_in('methodik.html',
  '''<p><strong>Ausnahme sind die KI-gestützten Textentwürfe</strong> (Trauerrede, Danksagung, Abschiedsbrief): Wenn du dort auf „Generieren“ klickst, werden die von dir eingegebenen Angaben zur Texterstellung an unsere Server-Funktion und von dort an einen KI-Dienstleister übermittelt. Die Nutzung ist freiwillig — ohne Klick auf „Generieren“ wird nichts übertragen. Details regelt die <a href="/datenschutz" style="color:var(--mr-primary)">Datenschutzerklärung</a>.</p>''',
  '''<p><strong>Ausnahme sind die KI-gestützten Textentwürfe</strong> (Trauerrede, Danksagung, Abschiedsbrief): Wenn du dort auf „Generieren“ klickst, werden die von dir eingegebenen Angaben zur Texterstellung an unsere Server-Funktion und von dort an einen KI-Dienstleister übermittelt. Die Nutzung ist freiwillig — ohne Klick auf „Generieren“ wird nichts übertragen. Details regelt die <a href="/datenschutz" style="color:var(--mr-primary)">Datenschutzerklärung</a>.</p>
    <h3>Datenfluss pro Tool</h3>
    <p>Dieselbe Übersicht steht wortgleich in der <a href="/datenschutz" style="color:var(--mr-primary)">Datenschutzerklärung</a>:</p>
    ''' + MATRIX)

# --- 2. Methodik: letzte Pruefdaten je Cluster ---
rep_in('methodik.html',
  '''<p style="font-size:14px;color:var(--mr-text-muted)">Größere Aktualisierungen dokumentieren wir am Ende der Seite im Änderungslog. So können Leser nachvollziehen, was sich gegenüber einer früheren Version substanziell geändert hat.</p>''',
  '''<p style="font-size:14px;margin-bottom:8px"><strong>Letzte Prüfungen je Inhalts-Cluster:</strong> Landesbestattungsgesetze und Rechtstexte — Mai 2026 · Kostendaten und Bundesland-Index (Modell V2) — Juni 2026 · Tool-Logik — fortlaufend bei jeder Änderung.</p>
    <p style="font-size:14px;color:var(--mr-text-muted)">Größere Aktualisierungen dokumentieren wir am Ende der Seite im Änderungslog. So können Leser nachvollziehen, was sich gegenüber einer früheren Version substanziell geändert hat.</p>''')

# --- 3. Danksagung: Umami-Falschsatz ---
rep_in('tools/danksagung/index.html',
  'Die Seite nutzt anonyme Reichweiten-Statistiken (Umami) nur nach Cookie-Opt-In.',
  'Die Seite nutzt anonyme, cookielose Reichweiten-Statistiken (Umami) — deine Eingaben werden davon nicht erfasst.')

print('R8 OK: Matrix (2x identisch) + Cluster-Pruefdaten + Danksagung-Konsistenz')
