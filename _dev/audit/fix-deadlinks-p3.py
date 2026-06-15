#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P3-Dead-Links (Historie/Promi/Film-Location, nice-to-have): ENT-LINKEN.
Alle 404 (15.06.). Kein Substanz-Claim haengt daran -> toter href weg, Text bleibt.
Ein Write je Datei, Asserts."""
import io, os, re, json, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
URLS = [
    'https://berliner-abendblatt.de/berlin-news/app-fuehrt-auf-stefan-heyms-spuren-durch-chemnitz-id321816',
    'https://lev-touren.de/index.php/stationen-bunker-wiesdorf/karl-krekeler-strasse',
    'https://www.lokalkompass.de/hagen/c-natur-garten/kulturhistorische-schaetze-grabstaetten-bekannter-persoenlichkeiten-auf-den-hagener-friedhoefen_a1445979',
    'https://www.juedischesmuseum.de/besuch/alter-juedischer-friedhof-battonnstrasse/',
    'https://www.kiel.de/de/kiel_zukunft/stadtgeschichte/ehrenbuerger/hans_von_koester.php',
    'https://www.krefeld.de/de/inhalt/teil-47-1915-die-erste-feuerbestattung-findet-in-krefeld-statt/',
    'https://www.krfrm.de/venue/waldfriedhof-darmstadt/',
    'https://www.wiesbaden.de/microsite/stadtlexikon/a-z/friedhof-biebrich.php',
    'https://www.stadt-muenster.de/filmservice/locations/ueberwasserfriedhof.html',
]

def main():
    files = [f for f in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)
             if os.sep + '_dev' + os.sep not in f]
    nfiles = nlinks = 0
    for f in sorted(files):
        t0 = io.open(f, encoding='utf-8').read()
        t = t0
        for url in URLS:
            pat = re.compile(r'<a\s+href="' + re.escape(url) + r'"[^>]*>(.*?)</a>', re.S)
            t, c = pat.subn(lambda m: m.group(1), t)
            nlinks += c
        if t == t0:
            continue
        for url in URLS:
            assert ('href="' + url + '"') not in t, 'Rest %s in %s' % (url[:40], f)
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            json.loads(blk)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        print('DELINKED', os.path.relpath(f, ROOT).replace(os.sep, '/'))
        nfiles += 1
    print('--- %d Dateien, %d Links ent-linkt' % (nfiles, nlinks))

if __name__ == '__main__':
    main()
