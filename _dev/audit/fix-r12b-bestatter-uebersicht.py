#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R12b — Auflagen aus NO-GO-58:
K1: Seite definiert keine --mr-*-Variablen (eigenes Inline-CSS, kein site.css)
    -> alle var(--mr-X) ohne Fallback bekommen die :root-Werte aus site.css
    als Fallback (Pattern der Seite selbst: var(--mr-text,#2D2319)).
H2: Seite laedt weder Umami noch tracking.js -> Site-Standard-Head eingefuegt,
    data-track mit unterscheidbaren Namen.
H3/H4: alle 16 Bundesland-Seiten existieren (Verzeichnis geprueft) ->
    BL-Sektion von 7 auf 16 vervollstaendigt, Trailing-Slash einheitlich.
M5: BreadcrumbList + CollectionPage-Schema.
M7: Hamburger-Button nur mobil (Media-Query statt always-on).
M8: role="search" + aria-live am Suchfeld.
"""
import io, re, sys

P = 'bestatter/index.html'
t = io.open(P, encoding='utf-8').read()

def rep(old, new, expect=1):
    global t
    c = t.count(old)
    if c != expect:
        print('FATAL: %r -> %d (erwartet %d)' % (old[:70], c, expect)); sys.exit(1)
    t = t.replace(old, new)

# K1: Fallbacks (Werte = :root aus assets/css/site.css)
FB = {'--mr-primary':'#7A6B5D','--mr-primary-hover':'#5E5047','--mr-bg':'#faf8f5',
      '--mr-bg-card':'#FFFDF9','--mr-border':'#E8E0D6','--mr-text':'#2D2319',
      '--mr-text-muted':'#73655A','--mr-accent':'#866E45','--mr-safety':'#FFFAF5',
      '--mr-radius':'12px'}
def add_fb(m):
    var = m.group(1)
    return 'var(%s,%s)' % (var, FB[var]) if var in FB else m.group(0)
before = len(re.findall(r'var\((--mr-[a-z-]+)\)', t))
t = re.sub(r'var\((--mr-[a-z-]+)\)(?!,)', add_fb, t)
after = len(re.findall(r'var\((--mr-[a-z-]+)\)(?!,)', t))
print('Fallbacks: %d var() ohne Fallback -> %d' % (before, after))
if after != 0:
    print('FATAL: var() ohne Fallback uebrig'); sys.exit(1)

# H2: Analytics-Head (Site-Standard) + sprechende data-track-Namen
rep('<style>',
    '''<script defer src="https://cloud.umami.is/script.js" data-website-id="6b6629ff-27b8-427b-863c-76b549cb52ba"></script><script>window.plausible=function(e,o){if(window.umami)window.umami.track(e,(o&&o.props)||{});};</script>
<script defer src="/js/tracking.js?v=20260609"></script>
<style>''')
rep('href="/tools/bestattungskosten-rechner/" data-track="cta"', 'href="/tools/bestattungskosten-rechner/" data-track="bestatter-hub-rechner"')
rep('href="/tools/angebotspruefer/" data-track="cta"', 'href="/tools/angebotspruefer/" data-track="bestatter-hub-pruefer"')

# M7: Hamburger nur mobil
rep('.mr-nav-toggle{display:inline-flex !important;align-items:center;margin-left:auto}',
    '.mr-nav-toggle{display:none;align-items:center;margin-left:auto}@media(max-width:760px){.mr-nav-toggle{display:inline-flex !important}}')

# M8: role/aria am Suchfeld
rep('<p style="margin:10px 0 18px"><label for="stadt-suche"',
    '<p style="margin:10px 0 18px" role="search"><label for="stadt-suche"')
rep('<span id="stadt-suche-leer" style="display:none;', '<span id="stadt-suche-leer" aria-live="polite" style="display:none;')

# H3/H4: BL-Sektion vervollstaendigen (alle 16, Trailing-Slash einheitlich)
rep('<section class="mr-section"><h2>Bundeslandseiten</h2><div class="city-grid"><a href="/bestattung-in/bayern">Bayern</a><a href="/bestattung-in/baden-wuerttemberg/">Baden-Württemberg</a><a href="/bestattung-in/nordrhein-westfalen">NRW</a><a href="/bestattung-in/hessen">Hessen</a><a href="/bestattung-in/niedersachsen">Niedersachsen</a><a href="/bestattung-in/sachsen">Sachsen</a><a href="/bestattung-in/saarland">Saarland</a></div></section>',
    '<section class="mr-section"><h2>Bestattungsrecht nach Bundesland</h2><p style="font-size:14px;color:var(--mr-text-muted,#73655A);margin-bottom:12px">Fristen, Sargpflicht und Friedhofsrecht regelt das jeweilige Landesgesetz — hier alle 16 Bundesländer:</p><div class="city-grid"><a href="/bestattung-in/baden-wuerttemberg/">Baden-Württemberg</a><a href="/bestattung-in/bayern/">Bayern</a><a href="/bestattung-in/berlin/">Berlin</a><a href="/bestattung-in/brandenburg/">Brandenburg</a><a href="/bestattung-in/bremen/">Bremen</a><a href="/bestattung-in/hamburg/">Hamburg</a><a href="/bestattung-in/hessen/">Hessen</a><a href="/bestattung-in/mecklenburg-vorpommern/">Mecklenburg-Vorpommern</a><a href="/bestattung-in/niedersachsen/">Niedersachsen</a><a href="/bestattung-in/nordrhein-westfalen/">Nordrhein-Westfalen</a><a href="/bestattung-in/rheinland-pfalz/">Rheinland-Pfalz</a><a href="/bestattung-in/saarland/">Saarland</a><a href="/bestattung-in/sachsen/">Sachsen</a><a href="/bestattung-in/sachsen-anhalt/">Sachsen-Anhalt</a><a href="/bestattung-in/schleswig-holstein/">Schleswig-Holstein</a><a href="/bestattung-in/thueringen/">Thüringen</a></div></section>')

# M5: Schema
SCHEMA = '''<script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"CollectionPage","name":"Bestattung in deutschen Städten","description":"Übersicht: Friedhöfe, Kosten, Bestattungsrecht und Bestatter-Wahl für 50 deutsche Städte.","url":"https://machsruhig.de/bestatter/","inLanguage":"de-DE","publisher":{"@type":"Organization","name":"machsruhig.de","url":"https://machsruhig.de"}},{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Start","item":"https://machsruhig.de/"},{"@type":"ListItem","position":2,"name":"Bestatter finden","item":"https://machsruhig.de/bestatter/"}]}]}</script>
'''
rep('<style>', SCHEMA + '<style>')

io.open(P, 'w', encoding='utf-8', newline='').write(t)
import json
m = re.search(r'<script type="application/ld\+json">(.*?)</script>', t, re.S)
json.loads(m.group(1))
print('R12b OK + Schema valide')
