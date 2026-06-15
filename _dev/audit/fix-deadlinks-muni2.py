#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kommunal-Batch 2: Koeln/Leipzig/Essen repoint (curl-200); Hannover ent-linken
(hannover.de-Deep-Paths sind fragil -> Re-Rot-Risiko; ZeitZentrum-Gedenktafel ist Historie)."""
import io, os, re, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
REPOINT = [
    ('bestatter/koeln/index.html',
     'https://www.stadt-koeln.de/leben-in-koeln/umwelt-natur/friedhoefe',
     'https://www.stadt-koeln.de/leben-in-koeln/freizeit-natur-sport/friedhoefe/'),
    ('bestatter/leipzig/index.html',
     'https://www.leipzig.de/buergerservice-und-verwaltung/aemter-und-behoerdengaenge/dienstleistungen/dienstleistung/sterbefall-beurkunden',
     'https://www.leipzig.de/buergerservice-und-verwaltung/lebenslagen-und-themen/sterbefall'),
    ('bestatter/essen/index.html',
     'https://www.essen.de/leben/gesundheit/bestattung_friedhoefe/friedhoefe.de.html',
     'https://www.essen.de/dasistessen/leben_im_gruenen_/friedhoefe_/friedhoefe_in_essen.de.html'),
]
DELINK = [
    ('bestatter/hannover/index.html', [
        'https://www.hannover.de/Leben-in-der-Region-Hannover/Verwaltungen-Kommunen/Die-Verwaltung-der-Landeshauptstadt-Hannover/B%C3%BCrger%C3%A4mter-und-Standes%C3%A4mter',
        'https://www.hannover.de/Kultur-Freizeit/Architektur-Geschichte/Erinnerungskultur/ZeitZentrum-Zivilcourage/Aktuelles-Veranstaltungen/Meldungen-aus-2016/Enth%C3%BCllung-der-Gedenktafel-f%C3%BCr-die-Familie-Theodor-Lessing',
        'https://www.hannover.de/Leben-in-der-Region-Hannover/Verwaltungen-Kommunen/Die-Verwaltung-der-Landeshauptstadt-Hannover/Dezernate-und-Fachbereiche-der-LHH/Umwelt-und-Stadtgr%C3%BCn',
    ]),
]

def main():
    nrp = ndl = 0
    for rel, old, new in REPOINT:
        f = os.path.join(ROOT, rel)
        t = io.open(f, encoding='utf-8').read()
        assert '"' + old + '"' in t, 'repoint NICHT gefunden %s' % rel
        t = t.replace('"' + old + '"', '"' + new + '"'); nrp += 1
        assert '"' + old + '"' not in t, 'Rest %s' % rel
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            json.loads(blk)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        print('REPOINT', rel.split('/')[1])
    for rel, urls in DELINK:
        f = os.path.join(ROOT, rel)
        t = io.open(f, encoding='utf-8').read()
        for url in urls:
            pat = re.compile(r'<a\s+href="' + re.escape(url) + r'"[^>]*>(.*?)</a>', re.S)
            t, c = pat.subn(lambda m: m.group(1), t)
            assert c >= 1, 'delink 0 %s: %s' % (rel, url[-40:])
            ndl += c
            assert ('href="' + url + '"') not in t, 'Rest %s' % rel
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            json.loads(blk)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        print('DELINK', rel.split('/')[1], len(urls))
    print('--- %d repoints, %d delinks' % (nrp, ndl))

if __name__ == '__main__':
    main()
