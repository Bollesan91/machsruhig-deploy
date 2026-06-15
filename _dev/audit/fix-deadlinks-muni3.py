#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kommunal-Batch 3 (Rest), alle Ziele 15.06. curl-200. Global ueber alle Live-HTML
(faengt Doppel-Dirs moenchengladbach/moenchengladbach-Umlaut)."""
import io, os, re, json, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MH = 'https://cms.muelheim-ruhr.de/leben-in-muelheim/natur-und-umwelt/friedhoefe-in-muelheim-an-der-ruhr/'
REPOINT = [
    ('https://www.aachen.de/de/stadt_buerger/aachener_stadtbetrieb/leistungen/friedhoefe_und_krematorium/',
     'https://www.aachen.de/in-aachen-leben/sicherheit-ordnung/stadtbetrieb/friedhoefe-und-krematorium/'),
    ('https://www.muelheim-ruhr.de/cms/der_altstadtfriedhof.html', MH + 'unsere-friedhoefe-1'),
    ('https://www.muelheim-ruhr.de/cms/der_altstadtfriedhof_ein_-zeugnis_der_stadtgeschichte-_patenschaften_fuer_denkmalwerte_grabstaetten.html', MH + 'unsere-friedhoefe-1'),
    ('https://www.muelheim-ruhr.de/cms/friedhof_altstadt1.html', MH + 'unsere-friedhoefe-1'),
    ('https://www.muelheim-ruhr.de/cms/einzelne_friedhoefe1.html', MH + 'unsere-friedhoefe'),
    ('https://www.muelheim-ruhr.de/cms/friedhof_broich1.html', MH + 'unsere-friedhoefe'),
    ('https://www.wuppertal.de/rathaus-buergerservice/standesamt/',
     'https://www.wuppertal.de/rathaus-buergerservice/familie/inhaltsseiten-partnerschaft-ehe-und-kinder/themenseite-sterbefall.php'),
    ('https://service.moenchengladbach.de/suche/-/egov-bis-detail/dienstleistung/273115/show',
     'https://service.moenchengladbach.de/suche/-/egov-bis-detail/dienstleistung/261138/show'),
    ('https://www.friedhof-hamburg.de/service/grabsuche/', 'https://www.friedhof-hamburg.de/'),
    ('https://friedhof-hagen.de/wbh-friedhoefe/waldfriedhof-loxbaum', 'https://friedhof-hagen.de/'),
]
DELINK = ['https://www.duesseldorf.de/friedhof/krematorium']

def main():
    files = [f for f in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)
             if os.sep + '_dev' + os.sep not in f]
    nrp = ndl = nf = 0
    for f in sorted(files):
        t0 = io.open(f, encoding='utf-8').read()
        t = t0
        for old, new in REPOINT:
            if '"' + old + '"' in t:
                t = t.replace('"' + old + '"', '"' + new + '"'); nrp += 1
        for url in DELINK:
            pat = re.compile(r'<a\s+href="' + re.escape(url) + r'"[^>]*>(.*?)</a>', re.S)
            t, c = pat.subn(lambda m: m.group(1), t); ndl += c
        if t == t0:
            continue
        for old, _ in REPOINT:
            assert ('"' + old + '"') not in t, 'repoint-Rest %s in %s' % (old[-30:], f)
        for url in DELINK:
            assert ('href="' + url + '"') not in t, 'delink-Rest %s' % f
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            json.loads(blk)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        print('FIXED', os.path.relpath(f, ROOT).replace(os.sep, '/'))
        nf += 1
    print('--- %d Dateien, %d repoints, %d delinks' % (nf, nrp, ndl))

if __name__ == '__main__':
    main()
