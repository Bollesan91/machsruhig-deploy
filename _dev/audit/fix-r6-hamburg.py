#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R6 (Loop-Iteration 5) — Stadtseite Hamburg "lokaler Proof":
1. Quickhelp-Block aus der Kontakt-Karten-aside herausloesen (sass faelschlich
   VOR deren h2 innerhalb von aria-label="Kontakt Friedhofsverwaltung") ->
   eigenstaendig direkt nach dem Hero.
2. Lokale Kostenbox min/typisch/gehoben (nur aus bereits belegten Seitenzahlen:
   anonym 2.830-3.365, Erd komplett 4.500-7.000, Seebestattung ab 1.049 zzgl.
   Einaescherung) + Kostenrechner/Angebotspruefer-CTA.
3. Historie nach unten: Ohlsdorf-Geschichte, Weitere Friedhoefe, Lokale
   Besonderheiten hinter das Anfrage-Formular (vor "Andere Staedte") schieben.
   Seebestattung bleibt oben (kostenrelevant).
4. Stand vereinheitlichen: Juni 2026, dateModified 2026-06-10.
5. Veralteten Briefing-HTML-Kommentar entfernen.
Keine neuen Fakten — reines Re-Arrangement + Verdichtung.
"""
import io, sys

P = 'bestatter/hamburg/index.html'
t = io.open(P, encoding='utf-8').read()

def rep(old, new, expect=1):
    global t
    c = t.count(old)
    if c != expect:
        print('FATAL: %r -> %d (erwartet %d)' % (old[:70], c, expect)); sys.exit(1)
    t = t.replace(old, new)

def cut(start, end, label):
    """Schneidet Block [start..end) aus und gibt ihn zurueck."""
    global t
    i = t.find(start)
    if i < 0:
        print('FATAL: Start nicht gefunden: %s' % label); sys.exit(1)
    j = t.find(end, i)
    if j < 0:
        print('FATAL: Ende nicht gefunden: %s' % label); sys.exit(1)
    block = t[i:j]
    t = t[:i] + t[j:]
    return block

# --- 1. Quickhelp aus der aside loesen ---
QH_START = '<div class="mr-quickhelp no-print"'
QH_END = '</div></div>\n<h2>Hamburger Friedhöfe AöR</h2>'
i = t.find(QH_START)
j = t.find(QH_END)
if i < 0 or j < 0 or j < i:
    print('FATAL: Quickhelp-Anker'); sys.exit(1)
quickhelp = t[i:j] + '</div></div>'
t = t[:i] + t[j + len('</div></div>\n'):]  # h2 bleibt in der aside

# Briefing-Kommentar entfernen + Quickhelp VOR die aside setzen
COMMENT = '''  <!-- Re-Arrangement (Stadt-Polish): Kontakt-Karte + Gebühren-Mini-Tabelle, ohne neue Recherche.
       HINWEIS Trägerschaft: Briefing nannte "Volksdorf, Wohldorf"; Page-Bestand und H3-Abschnitte
       nennen jedoch Ohlsdorf, Öjendorf, Bergedorf, Harburg als AöR-Friedhöfe. Page-konsistente
       Variante übernommen, um internen Widerspruch zu vermeiden. Bitte gegenprüfen. -->
'''
rep(COMMENT, '')
rep('  <aside class="mr-contact-card" aria-label="Kontakt Friedhofsverwaltung Hamburg">\n    <span class="mr-contact-eyebrow">Friedhofsverwaltung Hamburg</span>\n    \n',
    '  ' + quickhelp + '\n\n  <aside class="mr-contact-card" aria-label="Kontakt Friedhofsverwaltung Hamburg">\n    <span class="mr-contact-eyebrow">Friedhofsverwaltung Hamburg</span>\n    ')

# --- 2. Lokale Kostenbox min/typisch/gehoben nach der Feebox ---
FEEBOX_END = '''<p class="mr-feebox-note">Friedhofsgebühren nach Gebührenordnung der Hamburger Friedhöfe AöR (Stand 2025); Seebestattungs-Beträge als Reederei-Paketpreise. Auswahl aus den weiter unten ausführlich aufgeschlüsselten Posten — Bestatterleistungen kommen je nach Bestattungsart hinzu. Stand der Seite: Mai 2026.</p>
  </section>'''
KOSTENBOX = '''<p class="mr-feebox-note">Friedhofsgebühren nach Gebührenordnung der Hamburger Friedhöfe AöR (Stand 2025); Seebestattungs-Beträge als Reederei-Paketpreise. Auswahl aus den weiter unten ausführlich aufgeschlüsselten Posten — Bestatterleistungen kommen je nach Bestattungsart hinzu. Stand der Seite: Juni 2026.</p>
  </section>

  <section class="mr-section" id="kosten-hamburg" aria-label="Gesamtkosten-Einordnung Hamburg" style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:24px 28px;margin:0 0 32px">
    <h2 style="border-bottom:none;padding-bottom:0;margin-bottom:8px">Was kostet eine Bestattung in Hamburg insgesamt?</h2>
    <p style="font-size:14px;color:var(--mr-text-muted);margin-bottom:14px">Grobe Gesamtspannen aus den auf dieser Seite belegten Posten (Friedhofsgebühren + Bestatterleistungen, ohne Grabstein und Dauergrabpflege):</p>
    <div class="mr-table-wrap">
      <table class="mr-table">
        <thead><tr><th>Variante</th><th>Gesamtspanne</th><th>Was drin ist</th></tr></thead>
        <tbody>
          <tr><td><strong>Reduziert</strong></td><td>ca. 2.800–3.400&nbsp;€</td><td>Anonyme Beisetzung (Friedhofsanteil 1.250–1.420&nbsp;€ + Bestatter ca. 1.580–1.945&nbsp;€); Seebestattung unbegleitet als Reederei-Paket ab 1.049&nbsp;€ zzgl. Einäscherung und Bestatterleistungen</td></tr>
          <tr><td><strong>Typisch</strong></td><td>ca. 4.500–7.000&nbsp;€</td><td>Erdbestattung mit Sargwahlgrab (2.800–3.195&nbsp;€), Bestatterleistungen ab 1.945&nbsp;€ und Trauerfeier</td></tr>
          <tr><td><strong>Gehoben</strong></td><td>über 7.000&nbsp;€</td><td>Wahlgrab in besonderer Lage, hochwertiger Sarg, große Trauerfeier, Traueranzeigen und Grabmal</td></tr>
        </tbody>
      </table>
    </div>
    <p style="font-size:14px;margin-top:12px">Deinen persönlichen Rahmen — nach Bestattungsart und Auswahl — berechnest du im <a href="/tools/bestattungskosten-rechner/" style="color:var(--mr-primary);font-weight:600">Bestattungskosten-Rechner</a>. Liegt dir schon ein Angebot vor, zeigt der <a href="/tools/angebotspruefer/" style="color:var(--mr-primary);font-weight:600">Angebotsprüfer</a> in 3&nbsp;Minuten, ob Posten und Preise plausibel sind.</p>
  </section>'''
rep(FEEBOX_END, KOSTENBOX)

# --- 3. Historie nach unten ---
S_OHLSDORF = '  <div class="mr-section">\n    <h2>Friedhof Ohlsdorf — der größte Parkfriedhof der Welt</h2>'
S_WEITERE  = '  <div class="mr-section">\n    <h2>Weitere wichtige Friedhöfe in Hamburg</h2>'
S_SEE      = '  <div class="mr-section">\n    <h2>Seebestattung von Hamburg aus'
S_BESONDER = '  <div class="mr-section">\n    <h2>Lokale Besonderheiten Hamburgs — Kultur und Tradition</h2>'
S_SOZIAL   = '    <div class="mr-section" id="sozialbestattung-hamburg">'
ANDERE_STAEDTE = '<section class="mr-section" style="background: var(--mr-bg-card);">'

hist1 = cut(S_OHLSDORF, S_SEE, 'Ohlsdorf+Weitere')   # Ohlsdorf + Weitere Friedhoefe (zusammenhaengend)
if S_WEITERE not in hist1:
    print('FATAL: Weitere Friedhoefe nicht im Block'); sys.exit(1)
hist2 = cut(S_BESONDER, S_SOZIAL, 'Besonderheiten')

rep(ANDERE_STAEDTE,
    hist1.rstrip() + '\n\n' + hist2.rstrip() + '\n\n' + ANDERE_STAEDTE)

# --- 4. Stand/Datum ---
rep('"dateModified": "2026-06-09",', '"dateModified": "2026-06-10",')
rep('<span>Stand: 9. Juni 2026</span>', '<span>Stand: 10. Juni 2026</span>')

io.open(P, 'w', encoding='utf-8', newline='').write(t)

# Sanity: Reihenfolge pruefen
order = ['Schnelle Hilfe', 'Hamburger Friedhöfe AöR', 'Gebühren-Überblick',
         'Was kostet eine Bestattung in Hamburg insgesamt?',
         'Was nach einem Todesfall in Hamburg zu tun ist',
         'Seebestattung von Hamburg aus', 'Bestattungsrecht in Hamburg',
         'Sozialbestattung in Hamburg', 'Kostenlose Anfrage an Bestatter',
         'Friedhof Ohlsdorf — der größte', 'Weitere wichtige Friedhöfe',
         'Lokale Besonderheiten', 'Bestatter in anderen Städten',
         'Häufig gestellte Fragen']
# sequentiell ab Body suchen (JSON-LD im Head enthaelt dieselben Strings)
pos = t.find('<body>')
for o in order:
    p2 = t.find(o, pos)
    if p2 < 0:
        print('FATAL Reihenfolge: %s nicht (mehr) gefunden' % o); sys.exit(1)
    pos = p2
print('R6 OK: Quickhelp eigenstaendig, Kostenbox, Historie unten, Reihenfolge verifiziert')
