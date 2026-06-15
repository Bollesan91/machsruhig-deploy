#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kommunale Friedhof/Standesamt-Links Dresden/Karlsruhe/Duisburg (15.06., Ziele curl-200).
Repoint quote-delimitiert (karlsruhe /b3/friedhoefe ist Praefix von .../staedtische_friedhoefe).
DE-LINK nur die spezifische tote Krematoriums-Entgeltordnung (gone, kein 1:1)."""
import io, os, re, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
D = 'https://www.dresden.de'
K = 'https://www.karlsruhe.de'
PLAN = {
    'bestatter/dresden/index.html': {
        'repoint': [
            (D + '/de/leben/gesellschaft/friedhoefe.php', D + '/de/stadtraum/umwelt/gruenes-dresden/Friedhoefe.php'),
            (D + '/de/leben/gesellschaft/friedhoefe/staedtische-friedhoefe/johannisfriedhof.php', D + '/de/stadtraum/umwelt/gruenes-dresden/Friedhoefe.php'),
            (D + '/de/rathaus/dienstleistungen/standesamt.php', D + '/de/rathaus/dienstleistungen/sterbefall.php'),
        ],
        'delink': [D + '/media/pdf/satzungen/entgeltordnung-humankrematorium-tolkewitz.pdf'],
    },
    'bestatter/karlsruhe/index.html': {
        'repoint': [
            (K + '/b3/friedhoefe/staedtische_friedhoefe', K + '/stadt-rathaus/sterbefall-friedhoefe/friedhoefe-in-karlsruhe'),
            (K + '/b3/friedhoefe', K + '/stadt-rathaus/sterbefall-friedhoefe/friedhoefe-in-karlsruhe'),
            (K + '/standesamt', K + '/stadt-rathaus/sterbefall-friedhoefe/bestattung-und-services'),
        ],
        'delink': [],
    },
    'bestatter/duisburg/index.html': {
        'repoint': [
            ('https://www.duisburg.de/microsites/friedhoefe/friedhoefe/hauptfriedhof.php', 'https://www.duisburg-friedhof.de/'),
            ('https://www.duisburg.de/microsites/friedhoefe/friedhoefe/waldfriedhof.php', 'https://www.duisburg-friedhof.de/'),
            ('https://www.duisburg.de/microsites/standesamt/', 'https://service.duisburg.de/suche/-/vr-bis-detail/einrichtung/10/show'),
        ],
        'delink': [],
    },
}

def main():
    nrp = ndl = 0
    for rel, plan in PLAN.items():
        f = os.path.join(ROOT, rel)
        t = io.open(f, encoding='utf-8').read()
        for old, new in plan['repoint']:
            needle = '"' + old + '"'
            assert needle in t, 'repoint NICHT gefunden %s: %s' % (rel, old[-45:])
            t = t.replace(needle, '"' + new + '"'); nrp += 1
        for url in plan['delink']:
            pat = re.compile(r'<a\s+href="' + re.escape(url) + r'"[^>]*>(.*?)</a>', re.S)
            t, c = pat.subn(lambda m: m.group(1), t)
            assert c >= 1, 'delink 0 %s' % rel
            ndl += c
        for old, _ in plan['repoint']:
            assert ('"' + old + '"') not in t, 'repoint-Rest %s: %s' % (rel, old[-40:])
        for url in plan['delink']:
            assert ('href="' + url + '"') not in t, 'delink-Rest %s' % rel
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            json.loads(blk)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        print('FIXED %-34s rp=%d dl=%d' % (rel.split('/')[1], len(plan['repoint']), len(plan['delink'])))
    print('--- %d repoints, %d delinks' % (nrp, ndl))

if __name__ == '__main__':
    main()
