#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P1-Dead-Link-Repair: jede Ersatz-URL am 15.06. curl-200 + claim-verifiziert
(NRW BestG aktuelle Fassung; RLP mwwg-Seite bietet BestG-Volltext UND
Totenfuersorge-Muster; BSG B 8 SO 20/10 R Volltext via lexetius; aeternitas neue Pfade).
Asserts: jedes old vorhanden -> ersetzt -> JSON-LD parsebar. Ein Write je Datei."""
import io, os, re, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
NRW = 'https://recht.nrw.de/lrgv/gesetz/19022022-gesetz-ueber-das-friedhofs-und-bestattungswesen-bestattungsgesetz-bestg-nrw/'
RLP = 'https://mwwg.rlp.de/themen/gesundheit/bestattungsgesetz-1'
LEX = 'https://lexetius.com/2011,5999'
BSG_OLD = 'https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2011/2011_08_25_B_08_SO_20_10_R.html'

EDITS = [
    ('methodik.html',
     'https://recht.nrw.de/lmi/owa/br_text_anzeigen?v_id=36220110914100654580', NRW),
    ('bestatter/bielefeld/index.html',
     'https://recht.nrw.de/lmi/owa/br_text_anzeigen?v_id=10000000000000000295', NRW),
    ('bestatter/duisburg/index.html',
     'https://recht.nrw.de/lmi/owa/br_text_anzeigen?v_id=10000000000000000327', NRW),
    ('bestattung-in/rheinland-pfalz/index.html',
     '"https://mwg.rlp.de/themen/gesundheit/bestattungsgesetz"', '"' + RLP + '"'),
    ('bestatter/mainz/index.html',
     '"https://mwg.rlp.de/themen/gesundheit/bestattungsgesetz"', '"' + RLP + '"'),
    ('bestatter/frankfurt/index.html', BSG_OLD, LEX),
    # magdeburg: href + sichtbarer Ankertext "bsg.bund.de" -> "lexetius.com"
    ('bestatter/magdeburg/index.html',
     '<a href="' + BSG_OLD + '" rel="noopener" target="_blank">bsg.bund.de</a>',
     '<a href="' + LEX + '" rel="noopener" target="_blank">lexetius.com</a>'),
    ('bestatter/aachen/index.html',
     'https://www.aeternitas.de/fuer-betroffene/bestattung/was-kostet-eine-bestattung',
     'https://www.aeternitas.de/fuer-betroffene/kosten-und-vorsorge/kostenueberblick'),
    ('tools/danksagung/index.html',
     'https://www.aeternitas.de/inhalt/trauerbegleitung',
     'https://www.aeternitas.de/fuer-betroffene/trauerfall/was-tun-im-trauerfall/hilfe-in-der-trauer'),
]

def main():
    # gruppiere nach Datei (mehrere Edits/Datei moeglich)
    byfile = {}
    for rel, old, new in EDITS:
        byfile.setdefault(rel, []).append((old, new))
    total = 0
    for rel, edits in byfile.items():
        f = os.path.join(ROOT, rel)
        t = io.open(f, encoding='utf-8').read()
        for old, new in edits:
            assert old in t, 'NICHT gefunden in %s: %s' % (rel, old[:70])
            t = t.replace(old, new)
            assert new in t, 'Ersatz fehlt in %s' % rel
        # kein toter Rest dieser old-URLs
        for old, _ in edits:
            base = old.strip('"')
            assert base not in t, 'Rest geblieben in %s: %s' % (rel, base[:60])
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            json.loads(blk)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        print('FIXED %-44s %d Edit(s)' % (rel, len(edits)))
        total += len(edits)
    print('--- %d Edits in %d Dateien' % (total, len(byfile)))

if __name__ == '__main__':
    main()
