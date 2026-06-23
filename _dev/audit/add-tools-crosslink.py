# -*- coding: utf-8 -*-
"""Pass 2b: einheitlicher 'Weitere kostenlose Helfer'-Block auf allen Tool-Seiten.
Nutzt die site.css-native .mr-related-Box (ul/li/a). Jede Tool-Seite listet die
9 anderen Tools -> volle Quervernetzung, hebt alle Tools aus der Isolation."""
import io, os

# Reihenfolge = Anzeige-Reihenfolge; (slug, Titel, Kurzbeschreibung)
TOOLS = [
 ('bestattungskosten-rechner', 'Bestattungskosten-Rechner', 'Kostenrahmen für deine Region berechnen'),
 ('angebotspruefer',           'Bestatter-Angebot prüfen',   'Ein Angebot in wenigen Minuten auf Plausibilität prüfen'),
 ('checkliste-todesfall',      'Checkliste Todesfall',       'Was nach einem Sterbefall zu regeln ist'),
 ('fristen-radar',             'Fristen-Radar',              'Welche Fristen nach einem Todesfall jetzt laufen'),
 ('beerdigungsplaner',         'Beerdigungsplaner',          'Die Beerdigung Schritt für Schritt planen'),
 ('notfallkarte',              'Notfallkarte',               'Wichtige Kontakte und Infos für den Ernstfall festhalten'),
 ('vorsorge-check',            'Vorsorge-Check',             'Welche Vorsorge-Dokumente dir noch fehlen'),
 ('trauerrede',                'Trauerrede-Generator',       'Eine Trauerrede entwerfen'),
 ('danksagung',                'Danksagung-Generator',       'Dankesworte nach der Beerdigung formulieren'),
 ('abschiedsbrief',            'Brief an meine Liebsten',    'Einen persönlichen Abschiedsbrief schreiben'),
]

# Stufe 3: alle Ziele existieren?
for slug, _, _ in TOOLS:
    assert os.path.isdir(os.path.join('tools', slug)), 'Tool-Verzeichnis fehlt: %s' % slug

def block_for(self_slug):
    lis = []
    for slug, title, desc in TOOLS:
        if slug == self_slug:
            continue
        lis.append('<li><a href="/tools/%s/">%s</a> — %s</li>' % (slug, title, desc))
    return ('<div class="mr-related no-print" aria-label="Weitere Werkzeuge">\n'
            '<h2>Weitere kostenlose Helfer</h2>\n<ul>\n'
            + '\n'.join(lis) + '\n</ul>\n</div>\n')

ANCHORS = ['</main>', '<footer', '</body>']
plan = []
for slug, _, _ in TOOLS:
    f = os.path.join('tools', slug, 'index.html')
    t = io.open(f, encoding='utf-8').read()
    assert 'Weitere kostenlose Helfer' not in t, '%s hat den Block schon!' % slug
    anchor = next((a for a in ANCHORS if a in t), None)
    assert anchor, '%s: kein Anker gefunden' % slug
    plan.append((f, slug, t, anchor))

for f, slug, t, anchor in plan:
    blk = block_for(slug)
    new = t.replace(anchor, blk + anchor, 1)
    assert new != t and new.count('Weitere kostenlose Helfer') == 1, '%s: Insert fehlgeschlagen' % slug
    io.open(f, 'w', encoding='utf-8').write(new)
    n = blk.count('<li>')
    print('%-28s anchor=%-9s +%d Links' % (slug, anchor, n))

print('OK:', len(plan), 'Tool-Seiten')
