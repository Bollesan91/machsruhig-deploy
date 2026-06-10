#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quickfixes 2026-06-10 (Session: Daten-PR-Seite Review):
1. site.css: doppelten FAQ-Marker entfernen (.mr-faq summary::before "+ " —
   Duplikat zu summary::after '+' aus Z.66; betraf 87 Seiten mit "+ Frage +")
2. bestattungskosten-nach-bundesland.html:
   a) Lesezeit 6 -> 4 Minuten (777 Woerter ~ 4 min)
   b) Quellen BDB / Stiftung Warentest / Aeternitas verlinken (URLs verifiziert 10.06.)
   c) CTA-Block-H2 "Bestatter-Angebot pruefen" -> h3 (Heading-Redundanz nach
      Section-H2 "Du hast schon ein konkretes Angebot?")
3. Cache-Bust site-weit: site.css?v=20260611 -> v=20260612 (Cloudflare-Edge)
"""
import io, os, glob, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
os.chdir(ROOT)

def patch(path, replacements, must_all=True):
    with io.open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    n = 0
    for old, new in replacements:
        c = text.count(old)
        if c == 0:
            msg = 'MISS: %r in %s' % (old[:60], path)
            if must_all:
                print('FATAL ' + msg); sys.exit(1)
            print('warn ' + msg); continue
        if c > 1:
            print('FATAL: %r nicht eindeutig (%dx) in %s' % (old[:60], c, path)); sys.exit(1)
        text = text.replace(old, new)
        n += 1
    with io.open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)
    return n

# --- 1. site.css: doppelten Marker raus ---
n = patch('assets/css/site.css', [
    ('.mr-faq summary::before{ content: "+ "; color: var(--color-accent); font-weight: 700; }\n.mr-faq details[open] summary::before{ content: "− "; }\n', ''),
])
print('site.css: %d Ersetzungen' % n)

# --- 2. Bundesland-Seite ---
PAGE = 'bestattungskosten-nach-bundesland.html'
n = patch(PAGE, [
    ('<span>Lesezeit: ca. 6 Minuten</span>', '<span>Lesezeit: ca. 4 Minuten</span>'),
    ('<li>Bundesverband Deutscher Bestatter (BDB): Kostenbenchmark Bestattungen</li>',
     '<li><a href="https://www.bestatter.de/" target="_blank" rel="noopener" style="color:var(--mr-primary)">Bundesverband Deutscher Bestatter (BDB)</a>: Kostenbenchmark Bestattungen</li>'),
    ('<li>Stiftung Warentest: Bestattungskosten und -vorsorge</li>',
     '<li><a href="https://www.test.de/thema/sterbefall/" target="_blank" rel="noopener" style="color:var(--mr-primary)">Stiftung Warentest</a>: Bestattungskosten und -vorsorge</li>'),
    ('<li>Aeternitas e.V.: Friedhofsgebühren-Vergleiche</li>',
     '<li><a href="https://www.aeternitas.de/" target="_blank" rel="noopener" style="color:var(--mr-primary)">Aeternitas e.V.</a>: Friedhofsgebühren-Vergleiche</li>'),
    ('<div class="mr-cta-block no-print">\n    <h2>Bestatter-Angebot prüfen</h2>',
     '<div class="mr-cta-block no-print">\n    <h3>Bestatter-Angebot prüfen</h3>'),
])
print('%s: %d Ersetzungen' % (PAGE, n))

# --- 3. Cache-Bust site-weit ---
files = [p for p in glob.glob('**/*.html', recursive=True)
         if not p.replace('\\', '/').startswith('_dev/')]
bumped = 0
for p in files:
    with io.open(p, 'r', encoding='utf-8') as f:
        t = f.read()
    if 'site.css?v=20260611' in t:
        t = t.replace('site.css?v=20260611', 'site.css?v=20260612')
        with io.open(p, 'w', encoding='utf-8', newline='') as f:
            f.write(t)
        bumped += 1
print('Cache-Bust: %d Dateien v=20260611 -> v=20260612' % bumped)
