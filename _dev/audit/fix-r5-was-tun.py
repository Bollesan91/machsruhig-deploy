#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R5 (Loop-Iteration 4) — /was-tun-nach-todesfall 8,5 -> 9,0:
1. Box "Bevor du einen Bestatter beauftragst" mit CTAs Kostenrahmen + Angebot
   pruefen (direkt nach der Bestatter-Karte in Sektion 2).
2. Box "Was du heute NICHT entscheiden musst" + "nicht sofort unterschreiben"
   (Schutz vor der ersten grossen Fehlentscheidung).
3. Interne Links: Fristen-Radar in der Fristen-Sektion.
(Druckversion der 24h: bewusst uebersprungen — das druckbare Artefakt ist die
verlinkte Checkliste; Print-CSS-Umbau waere eigener Block.)
"""
import io, sys

P = 'was-tun-nach-todesfall.html'
t = io.open(P, encoding='utf-8').read()

def rep(old, new, expect=1):
    global t
    c = t.count(old)
    if c != expect:
        print('FATAL: %r -> %d (erwartet %d)' % (old[:70], c, expect)); sys.exit(1)
    t = t.replace(old, new)

ANCHOR = '''    <div class="card">
      <span class="tag">Standesamt</span>
      <h3>Sterbeurkunde beantragen</h3>'''

BOX = '''    <div class="card">
      <span class="tag">Standesamt</span>
      <h3>Sterbeurkunde beantragen</h3>'''

rep('''Hol dir mehrere Kostenvoranschläge — die Preise unterscheiden sich erheblich.</p>
    </div>''',
    '''Hol dir mehrere Kostenvoranschläge — die Preise unterscheiden sich erheblich.</p>
    </div>''')

# 1.+2. Schutz-Boxen nach dem Bestatter/Standesamt-Kartenpaar
ANCHOR2 = '''  <div class="lblock">
    <h3>Diese Dokumente brauchst du fürs Standesamt</h3>'''
NEU = '''  <div class="lblock" style="border-left:4px solid var(--mr-accent,#866E45);padding-left:18px">
    <h3>Bevor du einen Bestatter beauftragst</h3>
    <p>Lass dir ein <strong>schriftliches Angebot</strong> geben und achte darauf, ob Bestatterleistungen, Friedhofsgebühren und Fremdleistungen getrennt aufgeführt sind. Du musst nicht das erste Angebot unterschreiben — du darfst vergleichen, auch im Trauerfall. Zwei Werkzeuge helfen dir dabei, kostenlos und ohne Anmeldung:</p>
    <p style="margin-top:10px"><a href="/tools/bestattungskosten-rechner/" data-track="cta" style="color:var(--mr-primary);font-weight:600">Kostenrahmen berechnen →</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="/tools/angebotspruefer/" data-track="cta" style="color:var(--mr-primary);font-weight:600">Angebot prüfen →</a></p>
  </div>

  <div class="lblock">
    <h3>Was du heute <em>nicht</em> entscheiden musst</h3>
    <p>Grabstein, Trauerkarten, Danksagungen, die endgültige Grabgestaltung — all das hat Wochen bis Monate Zeit. Auch die Trauerfeier lässt sich später ansetzen als viele denken. Unterschreibe heute nichts, was über die unmittelbar nötigen Schritte (Überführung, Versorgung) hinausgeht, wenn du dir unsicher bist — seriöse Bestatter setzen dich nicht unter Zeitdruck.</p>
  </div>

''' + ANCHOR2
rep(ANCHOR2, NEU)

# 3. Fristen-Radar in der Fristen-Sektion verlinken
rep('<h3>Fristen beachten</h3>',
    '<h3>Fristen beachten</h3>\n    <p style="font-size:14px;margin-bottom:8px">Alle Fristen für deinen Fall auf einen Blick sortiert der <a href="/tools/fristen-radar/" style="color:var(--mr-primary)">Fristen-Radar</a> — mit deinem Bundesland und Sterbedatum.</p>', 1)

io.open(P, 'w', encoding='utf-8', newline='').write(t)
print('R5 OK: Schutz-Boxen + CTAs + Fristen-Radar-Link')
