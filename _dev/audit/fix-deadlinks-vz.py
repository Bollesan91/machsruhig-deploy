#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VZ-Dead-Link-Repair (15.06., alle Ziele curl-200):
- 4 'beratung-{Land}'-Links -> jeweilige Landes-Verbraucherzentrale (eigene Domain).
- 4 entfernte VZ-Artikel (kein Live-Aequivalent auf verbraucherzentrale.de) -> ENT-LINKEN
  (Innentext bleibt als Quellenangabe, toter href faellt weg; kein geratenes Ziel).
Asserts vor je einem Write pro Datei; JSON-LD parsebar."""
import io, os, re, json, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

REPOINT = {
    'https://www.verbraucherzentrale.de/beratung-brandenburg': 'https://www.verbraucherzentrale-brandenburg.de/',
    'https://www.verbraucherzentrale.de/beratung-mv': 'https://www.verbraucherzentrale-mv.eu/',
    'https://www.verbraucherzentrale.de/beratung-sachsen-anhalt': 'https://www.verbraucherzentrale-sachsen-anhalt.de/',
    'https://www.verbraucherzentrale.de/beratung-thueringen': 'https://www.vzth.de/',
}
DELINK = [
    'https://www.verbraucherzentrale.de/wissen/vertraege-reklamation/kundenrechte/bestattungskosten-was-eine-beerdigung-kostet-13518',
    'https://www.verbraucherzentrale.de/wissen/vertraege-reklamation/kundenrechte/todesfall-was-erben-jetzt-tun-muessen-11607',
    'https://www.verbraucherzentrale.de/wissen/geld-versicherungen/sparen-und-anlegen/erbschaft-und-testament-die-wichtigsten-regeln-23802',
    'https://www.verbraucherzentrale.de/wissen/vertraege-reklamation/sterbefall-und-vorsorge',
]

def delink(html, url):
    pat = re.compile(r'<a\s+href="' + re.escape(url) + r'"[^>]*>(.*?)</a>', re.S)
    return pat.subn(lambda m: m.group(1), html)

def main():
    files = [f for f in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)
             if os.sep + '_dev' + os.sep not in f]
    nrepoint = ndelink = nfiles = 0
    for f in sorted(files):
        t0 = io.open(f, encoding='utf-8').read()
        t = t0
        for old, new in REPOINT.items():
            if old + '"' in t:
                t = t.replace(old + '"', new + '"'); nrepoint += 1
        for url in DELINK:
            t, c = delink(t, url); ndelink += c
        if t == t0:
            continue
        # Asserts: keine der DELINK-URLs mehr als href; repoint-Alt-URLs weg
        for url in DELINK:
            assert ('href="' + url + '"') not in t, 'delink-Rest %s in %s' % (url[:50], f)
        for old in REPOINT:
            assert ('href="' + old + '"') not in t, 'repoint-Rest %s in %s' % (old, f)
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            json.loads(blk)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        rel = os.path.relpath(f, ROOT).replace(os.sep, '/')
        print('FIXED', rel)
        nfiles += 1
    print('--- %d Dateien, %d repoints, %d delinks' % (nfiles, nrepoint, ndelink))

if __name__ == '__main__':
    main()
