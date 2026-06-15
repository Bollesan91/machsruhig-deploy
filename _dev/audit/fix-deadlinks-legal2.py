#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P1-Legal Batch 2 (alle Ziele 15.06. curl-200 + claim-verifiziert):
- dortmund LSG NRW L 9 SO 49/23 (23.05.2024): justiz.nrw-Sammel-404 -> sozialgerichtsbarkeit.de
  Direktentscheidung (Ankertext 'NRWE-Rechtsprechungsdatenbank' -> 'sozialgerichtsbarkeit.de').
- hannover Nds. BestattG: toter VORIS-Doc -> VORIS-BestattG-Wurzeldokument.
- bremen § 4 BestG HB: lexsoft -> offizielles Transparenzportal Bremen (BestG vom 16.10.1990).
Asserts vor je einem Write."""
import io, os, re, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TRANSP = ('https://www.transparenz.bremen.de/metainformationen/'
          'gesetz-ueber-das-friedhofs-und-bestattungswesen-in-der-freien-hansestadt-bremen-'
          'vom-16-oktober-1990-66670?asl=bremen203_tpgesetz.c.55340.de&amp;template=20_gp_ifg_meta_detail_d')

SG = 'https://www.sozialgerichtsbarkeit.de/node/176600'
# (datei, [(old,new),...], verbotene-rest-substring)
EDITS = [
    ('bestatter/dortmund/index.html', [
        ('<a href="https://www.justiz.nrw/nrwe/lsgs/duesseldorf/lsg_nrw/" rel="external">L 9 SO 49/23, NRWE-Rechtsprechungsdatenbank</a>',
         '<a href="' + SG + '" rel="external">L 9 SO 49/23 (sozialgerichtsbarkeit.de)</a>'),
        # zweites Vorkommen (Quellen-Liste, gleicher Beschluss) nur URL umbiegen
        ('https://www.justiz.nrw/nrwe/lsgs/duesseldorf/lsg_nrw/', SG),
    ], 'justiz.nrw/nrwe/lsgs/duesseldorf/lsg_nrw/'),
    ('bestatter/hannover/index.html', [
        ('https://voris.wolterskluwer-online.de/browse/document/c30bf7d5-7a96-4c39-8a73-fc25b81b7e21',
         'https://voris.wolterskluwer-online.de/browse/document/1844a478-3f1b-3638-a476-c36200712f7e'),
    ], 'document/c30bf7d5-7a96-4c39-8a73-fc25b81b7e21'),
    ('bestattung-in/bremen/index.html', [
        ('https://www.lexsoft.de/cgi-bin/lexsoft/justizportal_nrw.cgi?xid=168754,5', TRANSP),
    ], 'lexsoft.de/cgi-bin/lexsoft/justizportal_nrw.cgi?xid=168754,5'),
]

def main():
    for rel, reps, forbidden in EDITS:
        f = os.path.join(ROOT, rel)
        t = io.open(f, encoding='utf-8').read()
        for old, new in reps:
            assert old in t, 'NICHT gefunden %s: %s' % (rel, old[:60])
            t = t.replace(old, new)
        assert forbidden not in t, 'Rest geblieben %s: %s' % (rel, forbidden)
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            json.loads(blk)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        print('FIXED', rel)
    print('--- 3 Dateien (4 Links)')

if __name__ == '__main__':
    main()
