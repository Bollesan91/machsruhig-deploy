# -*- coding: utf-8 -*-
"""Hebel 1: internes Städte-Mesh. Bisher verlinken alle "Bestatter in anderen
Städten"-Blöcke nur die 5 Gold-Städte -> Nicht-Gold-Städte bekommen kaum Inbound
("crawled, not indexed"). Fix: jeder Block verlinkt die Bundesland-GESCHWISTER.
Asserts vor dem einzigen Write je Datei."""
import os, re, glob

BL = {
 "Baden-Württemberg": "freiburg heidelberg karlsruhe mannheim stuttgart".split(),
 "Bayern": "augsburg muenchen nuernberg regensburg".split(),
 "Berlin": ["berlin"], "Brandenburg": ["potsdam"], "Bremen": ["bremen"],
 "Hamburg": ["hamburg"],
 "Hessen": "darmstadt frankfurt kassel wiesbaden".split(),
 "Mecklenburg-Vorpommern": ["rostock"],
 "Niedersachsen": "braunschweig hannover oldenburg osnabrueck".split(),
 "Nordrhein-Westfalen": ("aachen bielefeld bochum bonn dortmund duesseldorf duisburg essen "
   "gelsenkirchen hagen koeln krefeld leverkusen moenchengladbach muelheim muenster oberhausen wuppertal").split(),
 "Rheinland-Pfalz": ["mainz"], "Saarland": ["saarbruecken"],
 "Sachsen": "chemnitz dresden leipzig".split(),
 "Sachsen-Anhalt": "halle magdeburg".split(),
 "Schleswig-Holstein": "kiel luebeck".split(), "Thüringen": ["erfurt"],
}
NAME = {"freiburg":"Freiburg","heidelberg":"Heidelberg","karlsruhe":"Karlsruhe","mannheim":"Mannheim",
 "stuttgart":"Stuttgart","augsburg":"Augsburg","muenchen":"München","nuernberg":"Nürnberg",
 "regensburg":"Regensburg","berlin":"Berlin","potsdam":"Potsdam","bremen":"Bremen","hamburg":"Hamburg",
 "darmstadt":"Darmstadt","frankfurt":"Frankfurt","kassel":"Kassel","wiesbaden":"Wiesbaden","rostock":"Rostock",
 "braunschweig":"Braunschweig","hannover":"Hannover","oldenburg":"Oldenburg","osnabrueck":"Osnabrück",
 "aachen":"Aachen","bielefeld":"Bielefeld","bochum":"Bochum","bonn":"Bonn","dortmund":"Dortmund",
 "duesseldorf":"Düsseldorf","duisburg":"Duisburg","essen":"Essen","gelsenkirchen":"Gelsenkirchen","hagen":"Hagen",
 "koeln":"Köln","krefeld":"Krefeld","leverkusen":"Leverkusen","moenchengladbach":"Mönchengladbach",
 "muelheim":"Mülheim","muenster":"Münster","oberhausen":"Oberhausen","wuppertal":"Wuppertal","mainz":"Mainz",
 "saarbruecken":"Saarbrücken","chemnitz":"Chemnitz","dresden":"Dresden","leipzig":"Leipzig","halle":"Halle",
 "magdeburg":"Magdeburg","kiel":"Kiel","luebeck":"Lübeck","erfurt":"Erfurt"}
GOLD = ["muenchen","berlin","koeln","frankfurt","hamburg"]
slug2bl = {c: bl for bl, cs in BL.items() for c in cs}

BLOCK_RE = re.compile(r'<h2>Bestatter in anderen Städten</h2>\s*<div[^>]*>.*?</div>', re.S)

def block(city):
    bl = slug2bl[city]
    sibs = [c for c in BL[bl] if c != city]
    if not sibs:  # Einzel-Stadt-BL -> Gold-Städte als Mesh
        sibs = [c for c in GOLD if c != city]
        heading = "Bestatter in weiteren Großstädten"
    else:
        heading = "Weitere Städte in " + bl
    links = " · ".join('<a href="/bestatter/%s/" style="color:var(--mr-primary)">%s</a>' % (s, NAME[s]) for s in sibs)
    return '<h2>%s</h2>\n      <p style="line-height:2.1">%s</p>' % (heading, links)

changed = 0
for d in sorted(glob.glob('bestatter/*/')):
    city = os.path.basename(d.rstrip('/\\'))
    f = os.path.join(d, 'index.html')
    if city not in slug2bl or not os.path.exists(f):
        continue
    s = open(f, encoding='utf-8').read()
    nb = block(city)
    if 'Bestatter in anderen Städten' in s:
        s2 = BLOCK_RE.sub(nb, s, count=1)
        assert 'Weitere Städte in' in s2 or 'weiteren Großstädten' in s2, "Regex griff nicht: " + f
    else:
        assert '</main>' in s, "kein </main>: " + f
        s2 = s.replace('</main>', '  <section class="mr-section">%s</section>\n\n</main>' % nb, 1)
    # Asserts vor Write
    assert s2 != s, "keine Aenderung: " + f
    assert '</main>' in s2 and 'mr-footer' in s2, "Struktur kaputt: " + f
    open(f, 'w', encoding='utf-8').write(s2)
    changed += 1
print("Städte-Mesh aktualisiert:", changed)
