#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Korrektheits-Sweep: tote Stiftung-Warentest-Quelllinks (test.de, HTTP 404,
selbst gecurlt 15.06.2026) auf den lebenden, themengleichen Hub
test.de/thema/bestattung/ umbiegen (200; bereits auf bestattungskosten.html
und wuppertal verwendet -> konsistent). Linktext 'Stiftung Warentest' bleibt korrekt.
Die Kostenzahlen selbst werden NICHT angefasst (real + teils Finanztest-11/2023-belegt;
Spannen-Konsolidierung ist eine separate redaktionelle Aufgabe).
Asserts (Vorkommen vorhanden, JSON-LD-Parse) VOR dem einzigen Write je Datei.
"""
import io, os, re, json, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LIVE = 'test.de/thema/bestattung'
DEAD = [
    'test.de/Bestattung-und-Beerdigung-So-machen-Sie-es-richtig-4855859-0',
    'test.de/Bestattung-Kosten-und-Vergleich-1739987-0',
    'test.de/Bestatter-Was-eine-Bestattung-kostet-und-wie-Sie-sparen-koennen-5957571-0',
]

def ld_blocks(t):
    return re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S)

def main():
    files = [f for f in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)
             if os.sep + '_dev' + os.sep not in f]
    total = 0
    for f in sorted(files):
        old = io.open(f, encoding='utf-8').read()
        n = sum(old.count(d) for d in DEAD)
        if n == 0:
            continue
        new = old
        for d in DEAD:
            new = new.replace(d, LIVE)
        # Asserts VOR Write
        for d in DEAD:
            assert d not in new, 'toter Link blieb: %s in %s' % (d, f)
        assert new.count(LIVE) >= old.count(LIVE) + n, 'Ersetzungszahl stimmt nicht %s' % f
        for blk in ld_blocks(new):
            json.loads(blk)
        rel = os.path.relpath(f, ROOT).replace(os.sep, '/')
        io.open(f, 'w', encoding='utf-8', newline='').write(new)
        print('FIXED %-44s %d Link(s)' % (rel, n))
        total += 1
    print('--- %d Dateien' % total)

if __name__ == '__main__':
    main()
