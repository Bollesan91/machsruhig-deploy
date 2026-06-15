#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verzeichnis/Provider-Reste (15.06., Ziele curl-200):
REPOINT:
- bochum BDB Bestatter-finden -> bestatter.de/verzeichnis/
- hagen bestatter-nrw PLZ-Suche(404) -> BDB-Verzeichnis (national, deckt Hagen)
- krefeld BDB-Markenzeichen: verband.bestatter.de -> bestatter.de (Subdomain migriert)
- bielefeld FriedWald Lichtenau(404) -> friedwald.de/standorte (Standortfinder)
ENT-LINKEN (kein Live-1:1):
- bochum caritas-nrw Bestattungsrecht; bremen taspo-News (2015)
Asserts vor je einem Write."""
import io, os, re, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
VERZ = 'https://www.bestatter.de/verzeichnis/'
PLAN = {
    'bestatter/bochum/index.html': {
        'repoint': [('https://www.bestatter.de/bestatter-finden/', VERZ)],
        'delink': ['https://www.caritas-nrw.de/rechtinformationsdienst/bestattungsrecht/bestattung-bestattungsrecht-bestattungsp'],
    },
    'bestatter/hagen/index.html': {
        'repoint': [('https://www.bestatter-nrw.de/bestatter-suche?plz=58095', VERZ)],
        'delink': [],
    },
    'bestatter/krefeld/index.html': {
        'repoint': [('https://verband.bestatter.de/verband/markenzeichen-der-bestatter/',
                     'https://www.bestatter.de/verband/markenzeichen-der-bestatter/')],
        'delink': [],
    },
    'bestatter/bielefeld/index.html': {
        'repoint': [('https://www.friedwald.de/standort/lichtenau', 'https://www.friedwald.de/standorte')],
        'delink': [],
    },
    'bestattung-in/bremen/index.html': {  # taspo evtl. auf BL-bremen ODER bestatter/bremen
        'repoint': [],
        'delink': ['https://taspo.de/gruene-branche/neues-bestattungsgesetz-private-ascheverstreuung-in-bremen-ab-2015-erlaubt/'],
    },
}

def main():
    nrp = ndl = 0
    for rel, plan in list(PLAN.items()):
        f = os.path.join(ROOT, rel)
        if not os.path.exists(f):
            continue
        t = io.open(f, encoding='utf-8').read()
        changed = False
        for old, new in plan['repoint']:
            if old in t:
                t = t.replace(old, new); nrp += 1; changed = True
                assert old not in t, 'repoint-Rest %s' % rel
        for url in plan['delink']:
            pat = re.compile(r'<a\s+href="' + re.escape(url) + r'"[^>]*>(.*?)</a>', re.S)
            t, c = pat.subn(lambda m: m.group(1), t)
            if c:
                ndl += c; changed = True
                assert ('href="' + url + '"') not in t, 'delink-Rest %s' % rel
        if not changed:
            continue
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            json.loads(blk)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        print('FIXED', rel)
    # taspo evtl. auf bestatter/bremen statt BL: separat fangen
    for rel in ['bestatter/bremen/index.html']:
        f = os.path.join(ROOT, rel)
        t = io.open(f, encoding='utf-8').read()
        url = 'https://taspo.de/gruene-branche/neues-bestattungsgesetz-private-ascheverstreuung-in-bremen-ab-2015-erlaubt/'
        pat = re.compile(r'<a\s+href="' + re.escape(url) + r'"[^>]*>(.*?)</a>', re.S)
        t2, c = pat.subn(lambda m: m.group(1), t)
        if c:
            io.open(f, 'w', encoding='utf-8', newline='').write(t2); ndl += c
            print('FIXED', rel, '(taspo)')
    print('--- %d repoints, %d delinks' % (nrp, ndl))

if __name__ == '__main__':
    main()
