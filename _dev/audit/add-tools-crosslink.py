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
 ('danksagung',                'Danksagung-Generator',       'Dankesworte nach der Beerdigung entwerfen'),
 ('abschiedsbrief',            'Abschiedsbrief schreiben',   'Einen persönlichen Brief an deine Liebsten verfassen'),
]

META = {slug: (title, desc) for slug, title, desc in TOOLS}

# Kuratierte, thematisch nahe Geschwister je Tool (statt Vollmesh = weniger
# Boilerplate, staerkeres Relevanzsignal; Reviewer-Empfehlung). Plus Hub-Link.
CURATED = {
 'bestattungskosten-rechner': ['angebotspruefer','beerdigungsplaner','checkliste-todesfall'],
 'angebotspruefer':           ['bestattungskosten-rechner','beerdigungsplaner','checkliste-todesfall'],
 'checkliste-todesfall':      ['fristen-radar','beerdigungsplaner','bestattungskosten-rechner'],
 'fristen-radar':             ['checkliste-todesfall','beerdigungsplaner','bestattungskosten-rechner'],
 'beerdigungsplaner':         ['checkliste-todesfall','bestattungskosten-rechner','angebotspruefer'],
 'notfallkarte':              ['vorsorge-check','checkliste-todesfall','fristen-radar'],
 'vorsorge-check':            ['notfallkarte','bestattungskosten-rechner','checkliste-todesfall'],
 'trauerrede':                ['danksagung','abschiedsbrief'],
 'danksagung':                ['trauerrede','abschiedsbrief'],
 'abschiedsbrief':            ['trauerrede','danksagung','vorsorge-check'],
}

# Stufe 3: alle Ziele existieren?
for slug, _, _ in TOOLS:
    assert os.path.isdir(os.path.join('tools', slug)), 'Tool-Verzeichnis fehlt: %s' % slug
assert set(CURATED) == {s for s,_,_ in TOOLS}, 'CURATED deckt nicht alle Tools'
for self_slug, sibs in CURATED.items():
    assert self_slug not in sibs, 'Selbstlink in CURATED[%s]' % self_slug
    for s in sibs:
        assert s in META, 'Unbekanntes Tool in CURATED[%s]: %s' % (self_slug, s)
assert os.path.isfile(os.path.join('tools', 'index.html')), 'Hub /tools/index.html fehlt'

def block_for(self_slug):
    lis = []
    for slug in CURATED[self_slug]:
        title, desc = META[slug]
        lis.append('<li><a href="/tools/%s/">%s</a> — %s</li>' % (slug, title, desc))
    lis.append('<li><a href="/tools/"><strong>Alle kostenlosen Werkzeuge</strong></a> — Übersicht aller Helfer im Browser</li>')
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
