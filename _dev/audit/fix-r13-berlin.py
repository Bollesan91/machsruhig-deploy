#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R13 (Stadtseiten-Welle, Berlin) — Hamburg-Muster:
1. Kosten konsolidiert: Zweite Kosten-Sektion ("Bestattungskosten in Berlin",
   Korridor-Tabelle der Bestatter-Auswertungen) in die erste integriert, mit
   expliziter Quellen-Trennung (Senats-Broschuere landeseigene vs.
   Bestatter-Korridore inkl. konfessioneller Traeger) — die nackten Zahlen
   widersprachen sich sonst scheinbar.
2. Leerer "Gesamtbudget"-h3-Stub gefuellt: reduziert/typisch/gehoben-Box aus
   belegten Seiten-Zahlen (anonym 300-600 Friedhofsanteil; einfache Bestattung
   2.500-5.000 ohne Feier; Premium-Wahlstelle bis 4.000+ zzgl. Feier).
3. Reorder: Sozialbestattung VOR das Anfrage-Formular; Kultur-/Historie-Bloecke
   (Zahlen, Hauptfriedhoefe, Besonderheiten, Institute) hinter das Formular.
4. Stand-Daten vereinheitlicht (Juni 2026).
"""
import io, sys

P = 'bestatter/berlin/index.html'
t = io.open(P, encoding='utf-8').read()

def rep(old, new, expect=1):
    global t
    c = t.count(old)
    if c != expect:
        print('FATAL: %r -> %d (erwartet %d)' % (old[:70], c, expect)); sys.exit(1)
    t = t.replace(old, new)

def cut(start, end, label):
    global t
    i = t.find(start)
    if i < 0: print('FATAL Start: %s' % label); sys.exit(1)
    j = t.find(end, i)
    if j < 0: print('FATAL Ende: %s' % label); sys.exit(1)
    block = t[i:j]
    t = t[:i] + t[j:]
    return block

# --- 4. Stand ---
rep('<span>Stand: 9. Juni 2026</span>', '<span>Stand: 11. Juni 2026</span>')
rep('<p><strong>Stand:</strong> Mai 2026. Gebühren und Pauschalen können sich ändern.</p>',
    '<p><strong>Stand:</strong> Juni 2026. Gebühren und Pauschalen können sich ändern.</p>')

# --- 1.+2. Kosten konsolidieren ---
# Zweite Kosten-Sektion ausschneiden (inkl. oeffnendem div)
S2_START = '  <div class="mr-section">\n    <h2>Bestattungskosten in Berlin</h2>'
S2_END = '  <div class="mr-section">\n    <h2>Bestattungsrecht in Berlin</h2>'
sec2 = cut(S2_START, S2_END, 'Kosten-Sektion 2')

# Kern der Sektion 2 extrahieren (Intro + Tabelle + Gesamtbudget-Satz + Tool-Hint)
inner2 = sec2.replace('  <div class="mr-section">\n    <h2>Bestattungskosten in Berlin</h2>\n', '')
inner2 = inner2.rstrip()
if inner2.endswith('</div>'):
    inner2 = inner2[:-len('</div>')].rstrip()  # schliessendes Sektions-div ab

# In Sektion 1 am "Gesamtbudget"-Stub einsetzen, mit Quellen-Trennung + Budget-Box
STUB = '''    <h3>Gesamtbudget für eine Beerdigung</h3>
    <div class="mr-hint">'''
NEW = '''    <h3>Spannweite inklusive konfessioneller Träger und Lage</h3>
    <p style="font-size:14px;color:var(--mr-text-muted)">Die Tabelle oben zeigt die <strong>landeseigenen</strong> Friedhöfe nach der Senats-Broschüre. Rechnet man konfessionelle Träger und Lage-Unterschiede dazu, ergeben sich breitere Korridore — ausgewertet aus den Gebührenordnungen 2025/26 durch Berliner Bestatter:</p>
''' + inner2.replace('<h2>Bestattungskosten in Berlin</h2>', '').replace('<p>Berliner Friedhofsgebühren werden <strong>nicht zentral festgelegt</strong>, sondern pro Bezirk in der jeweiligen <strong>Friedhofsgebührenordnung</strong> beschlossen; konfessionelle Träger haben eigene Gebührensätze. Daraus ergibt sich eine deutliche Spannweite zwischen einfachen Reihengräbern und Wahlgrabstellen in prominenter Lage. Die folgende Übersicht fasst typische Korridore zusammen, basierend auf den von Berliner Bestattern (Hahn Bestattungen, November, Heimkehr, Januar) ausgewerteten Gebührenordnungen 2025/26.</p>', '<p style="font-size:13px;color:var(--mr-text-muted)">Quelle: Auswertungen Berliner Bestatter (Hahn, November, Heimkehr, Januar). Dass die Untergrenzen unter den landeseigenen Sätzen liegen, erklärt sich durch einzelne günstigere konfessionelle und Bezirks-Gebührenordnungen.</p>') + '''

    <h3>Gesamtbudget für eine Beerdigung in Berlin</h3>
    <div class="mr-table-wrap">
      <table class="mr-table">
        <thead><tr><th>Variante</th><th>Gesamtspanne</th><th>Was drin ist</th></tr></thead>
        <tbody>
          <tr><td><strong>Reduziert</strong></td><td>unter 2.500&nbsp;€</td><td>Anonyme Beisetzung (Friedhofsanteil 300–600&nbsp;€) oder Direktkremation mit Urnenreihengrab — Berlin hat die niedrigsten Friedhofsgebühren aller Landeshauptstädte</td></tr>
          <tr><td><strong>Typisch</strong></td><td>ca. 2.500–5.000&nbsp;€</td><td>Einfache Erd- oder Feuerbestattung mit Bestatterleistungen, ohne große Trauerfeier</td></tr>
          <tr><td><strong>Gehoben</strong></td><td>über 5.000&nbsp;€</td><td>Wahlgrab in prominenter Lage (bis 4.000&nbsp;€+ allein die Grabstelle), hochwertiger Sarg, große Trauerfeier, Grabmal</td></tr>
        </tbody>
      </table>
    </div>
    <div class="mr-hint">'''
rep(STUB, NEW)

# --- 3. Reorder ---
ANDERE = '<div class="mr-cta-block" style="background:var(--mr-bg-card);border:2px solid var(--mr-border);text-align:left;padding:28px 24px">'
if t.count(ANDERE) != 1:
    # Formular-Container-Anker robust finden
    ANDERE = '<h2 style="text-align:center">Kostenlose Anfrage an Bestatter in Berlin</h2>'
    assert t.count(ANDERE) == 1

S_ZAHLEN  = '  <div class="mr-section">\n    <h2>Berliner Friedhofslandschaft in Zahlen</h2>'
S_HAUPT   = '  <div class="mr-section">\n    <h2>Drei Hauptfriedhöfe — die Berliner Kulturschwere</h2>'
S_BESOND  = '  <div class="mr-section">\n    <h2>Besonderheiten Berlins</h2>'
S_INST    = '  <div class="mr-section">\n    <h2>Berliner Bestatterinstitute und Verbände</h2>'
S_RECHT   = '  <div class="mr-section">\n    <h2>Bestattungsrecht in Berlin</h2>'
S_ANDERE_STAEDTE_SEC = '<h2>Bestatter in anderen Städten</h2>'
S_SOZIAL  = '  <div class="mr-section">\n    <h2>Sozialbestattung in Berlin'
S_FAQ     = '  <div class="mr-section">\n    <h2>Häufig gestellte Fragen (FAQ)</h2>'
S_WAHL    = '  <div class="mr-section">\n    <h2>Bestatter-Wahl in Berlin — Qualitätskriterien</h2>'

hist1 = cut(S_ZAHLEN, S_HAUPT, 'Zahlen')        # Zahlen
hist2 = cut(S_HAUPT, S_RECHT, 'Hauptfriedhoefe') # Hauptfriedhoefe (endet vor Recht)
hist3 = cut(S_BESOND, S_INST, 'Besonderheiten')
# Institute endet vor "andere Staedte"-section
i = t.find(S_INST); j = t.find('<section class="mr-section"', i)
if i < 0 or j < 0: print('FATAL Institute'); sys.exit(1)
hist4 = t[i:j]; t = t[:i] + t[j:]

# Sozialbestattung ausschneiden (endet vor FAQ) und VOR das Formular setzen
soz = cut(S_SOZIAL, S_FAQ, 'Sozial')
assert t.count(S_WAHL) == 1
t = t.replace(S_WAHL, soz.rstrip() + '\n\n' + S_WAHL)

# Historie hinter das Formular (vor FAQ) einsetzen
assert t.count(S_FAQ) == 1
t = t.replace(S_FAQ, hist1.rstrip() + '\n\n' + hist2.rstrip() + '\n\n' + hist3.rstrip() + '\n\n' + hist4.rstrip() + '\n\n' + S_FAQ)

io.open(P, 'w', encoding='utf-8', newline='').write(t)

# Sanity: Reihenfolge ab <body>
order = ['Schnelle Hilfe', 'Berlin in Kernfakten', 'Welches Standesamt',
         'Was nach einem Todesfall in Berlin', 'Friedhöfe in Berlin',
         'Gebühren und Kosten für Bestattungen', 'Gesamtbudget für eine Beerdigung in Berlin',
         'Bestattungsrecht in Berlin', 'Sozialbestattung in Berlin',
         'Bestatter-Wahl in Berlin', 'Kostenlose Anfrage an Bestatter in Berlin',
         'Berliner Friedhofslandschaft in Zahlen', 'Drei Hauptfriedhöfe',
         'Besonderheiten Berlins', 'Berliner Bestatterinstitute',
         'Häufig gestellte Fragen']
pos = t.find('<body>')
for o in order:
    p2 = t.find(o, pos)
    if p2 < 0: print('FATAL Reihenfolge: %s fehlt' % o); sys.exit(1)
    pos = p2
print('R13 OK: Kosten konsolidiert + Budget-Box + Reorder verifiziert')
