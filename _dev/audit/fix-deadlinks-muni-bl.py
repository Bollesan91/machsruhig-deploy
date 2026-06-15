#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kommunale tote Links auf BL-/Hub-Seiten (15.06., Ziele curl-200 verifiziert):
REPOINT (klarer Live-Ersatz):
- bremen Waller Friedhof: ...friedhof-walle-2576 -> -2578 (ID gewechselt)
- bremen Gebuehrenordnung-PDF (tot) -> umweltbetrieb-bremen.de/friedhoefe/friedhofsgesetze-1471
- mainz Friedhoefe (Quelle) -> mainz.de/microsite/wb/bestattung/index.php (neue WBM-Microsite)
ENT-LINKEN (kein Live-1:1; /vv/produkte komplett migriert, neue Slugs nicht ermittelbar
-> nicht raten; Quellentext bleibt):
- mainz Reihengrab/Wahlgrab/Grabmalgenehmigung/Friedhofsatzung-PDF/Amtsblatt-PDF
- rheinland-pfalz: mainz-Ortsrecht-Friedhofssatzung-PDF
- brandenburg: Potsdam-Infoblatt-PDF (auch Flyer 404)
Asserts vor je einem Write."""
import io, os, re, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
UB = 'https://www.umweltbetrieb-bremen.de'

MAINZ_FRIED = ('https://www.mainz.de/freizeit-und-sport/im-gruenen/friedhoefe.php',
               'https://www.mainz.de/microsite/wb/bestattung/index.php')
PLAN = {
    'bestatter/bremen/index.html': {
        'repoint': [
            (UB + '/friedhoefe/unsere-staedtischen-friedhoefe/friedhof-walle-2576',
             UB + '/friedhoefe/unsere-staedtischen-friedhoefe/friedhof-walle-2578'),
            (UB + '/sixcms/media.php/13/2020_12_28_Aenderung_FHordnung_stadteig_Gebuehrenordnung.pdf',
             UB + '/friedhoefe/friedhofsgesetze-1471'),
        ],
        'delink': [],
    },
    'bestatter/mainz/index.html': {
        'repoint': [MAINZ_FRIED],
        'delink': [
            'https://www.mainz.de/vv/medien/wirtschaftsbetrieb-mainz---anstalt-des-oeffentlichen-rechts/Friedhofsatzung_1.11.2020.pdf',
            'https://www.mainz.de/vv/produkte/wirtschaftsbetrieb-mainz/Reihengrab.php',
            'https://www.mainz.de/vv/produkte/wirtschaftsbetrieb/Wahlgrab-Erwerb-eines-Nutzungsrechtes.php',
            'https://www.mainz.de/vv/produkte/wirtschaftsbetrieb/grabmalgenehmigung.php',
            'https://www.mainz.de/medien/internet/downloads/amtsblatt-2026/Amtsblatt_02_2026_16.01.2026.pdf',
        ],
    },
    'bestattung-in/rheinland-pfalz/index.html': {
        'repoint': [MAINZ_FRIED],
        'delink': [
            'https://www.mainz.de/verzeichnisse/ortsrecht/Friedhofssatzung_des_Wirtschaftsbetriebes_Mainz_Anstalt_des_oeffentlichen_Rechts__WBM__vom_10.12.2009.php.media/46347/Friedhofssatzung_AOeR.pdf',
        ],
    },
    'bestattung-in/brandenburg/index.html': {
        'repoint': [],
        'delink': ['https://vv.potsdam.de/vv/Infoblatt-zum-Bestattungsrecht_2025.pdf'],
    },
}

def main():
    nrp = ndl = 0
    for rel, plan in PLAN.items():
        f = os.path.join(ROOT, rel)
        t = io.open(f, encoding='utf-8').read()
        for old, new in plan['repoint']:
            assert old in t, 'repoint NICHT gefunden %s: %s' % (rel, old[-40:])
            t = t.replace(old, new); nrp += 1
            assert old not in t, 'repoint-Rest %s' % rel
        for url in plan['delink']:
            pat = re.compile(r'<a\s+href="' + re.escape(url) + r'"[^>]*>(.*?)</a>', re.S)
            t, c = pat.subn(lambda m: m.group(1), t)
            assert c >= 1, 'delink 0 Treffer %s: %s' % (rel, url[-40:])
            assert ('href="' + url + '"') not in t, 'delink-Rest %s' % rel
            ndl += c
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            json.loads(blk)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        print('FIXED %-40s rp=%d dl=%d' % (rel, len(plan['repoint']), len(plan['delink'])))
    print('--- %d repoints, %d delinks' % (nrp, ndl))

if __name__ == '__main__':
    main()
