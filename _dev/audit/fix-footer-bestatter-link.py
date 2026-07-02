# -*- coding: utf-8 -*-
"""Footer-Link 'Bestatter finden'/'Bestatter' zeigt hart auf /bestatter/muenchen/ statt
auf die Uebersicht /bestatter/ (Audit P2-4). Nur die exakten Footer-Link-Texte ersetzen."""
import glob, os
pairs = [
    ('<a href="/bestatter/muenchen/">Bestatter finden</a>', '<a href="/bestatter/">Bestatter finden</a>'),
    ('<a href="/bestatter/muenchen/">Bestatter</a>', '<a href="/bestatter/">Bestatter</a>'),
]
nf = ni = 0
for f in glob.glob('**/*.html', recursive=True):
    p = f.replace(os.sep, '/')
    if '/_dev/' in p or 'node_modules' in p:
        continue
    t = open(f, encoding='utf-8').read()
    o = t
    for bad, good in pairs:
        c = t.count(bad)
        if c:
            t = t.replace(bad, good); ni += c
    if t != o:
        open(f, 'w', encoding='utf-8').write(t); nf += 1
print(f'Dateien: {nf}, Footer-Links umgebogen: {ni}')
rem = 0
for f in glob.glob('**/*.html', recursive=True):
    p = f.replace(os.sep, '/')
    if '/_dev/' in p or 'node_modules' in p:
        continue
    s = open(f, encoding='utf-8').read()
    rem += s.count('/bestatter/muenchen/">Bestatter<') + s.count('/bestatter/muenchen/">Bestatter finden<')
print('verbleibend:', rem)
