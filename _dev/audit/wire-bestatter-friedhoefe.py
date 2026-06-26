#!/usr/bin/env python3
# Phase-1 Stadt-Hub: Bestatter-Stadtseiten -> Friedhof-Uebersicht der Stadt verlinken.
# Fuegt einen einheitlichen "Passend dazu"-mr-related-Block vor dem letzten </main> ein,
# NUR wenn (a) die Friedhof-Uebersicht /friedhoefe/<stadt>/ existiert UND
#          (b) die Seite sie noch NICHT verlinkt (idempotent).
# Umlaut-Dubletten-Dirs und Staedte ohne Friedhof-Uebersicht werden uebersprungen.
import os, sys, re

DRY = "--apply" not in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BL = {
 "baden-wuerttemberg":"Baden-Württemberg","bayern":"Bayern","berlin":"Berlin",
 "brandenburg":"Brandenburg","bremen":"Bremen","hamburg":"Hamburg","hessen":"Hessen",
 "mecklenburg-vorpommern":"Mecklenburg-Vorpommern","niedersachsen":"Niedersachsen",
 "nordrhein-westfalen":"Nordrhein-Westfalen","rheinland-pfalz":"Rheinland-Pfalz",
 "saarland":"Saarland","sachsen":"Sachsen","sachsen-anhalt":"Sachsen-Anhalt",
 "schleswig-holstein":"Schleswig-Holstein","thueringen":"Thüringen",
}
BL_SHORT = {"nordrhein-westfalen":"NRW"}
# stadt-slug -> (Anzeigename, bl-slug)
ST = {
 "freiburg":("Freiburg","baden-wuerttemberg"),"heidelberg":("Heidelberg","baden-wuerttemberg"),
 "karlsruhe":("Karlsruhe","baden-wuerttemberg"),"mannheim":("Mannheim","baden-wuerttemberg"),
 "stuttgart":("Stuttgart","baden-wuerttemberg"),
 "augsburg":("Augsburg","bayern"),"muenchen":("München","bayern"),"nuernberg":("Nürnberg","bayern"),
 "berlin":("Berlin","berlin"),"potsdam":("Potsdam","brandenburg"),"bremen":("Bremen","bremen"),
 "hamburg":("Hamburg","hamburg"),
 "frankfurt":("Frankfurt","hessen"),"kassel":("Kassel","hessen"),"wiesbaden":("Wiesbaden","hessen"),
 "rostock":("Rostock","mecklenburg-vorpommern"),
 "braunschweig":("Braunschweig","niedersachsen"),"hannover":("Hannover","niedersachsen"),
 "oldenburg":("Oldenburg","niedersachsen"),"osnabrueck":("Osnabrück","niedersachsen"),
 "aachen":("Aachen","nordrhein-westfalen"),"bielefeld":("Bielefeld","nordrhein-westfalen"),
 "bochum":("Bochum","nordrhein-westfalen"),"bonn":("Bonn","nordrhein-westfalen"),
 "dortmund":("Dortmund","nordrhein-westfalen"),"duesseldorf":("Düsseldorf","nordrhein-westfalen"),
 "duisburg":("Duisburg","nordrhein-westfalen"),"essen":("Essen","nordrhein-westfalen"),
 "gelsenkirchen":("Gelsenkirchen","nordrhein-westfalen"),"hagen":("Hagen","nordrhein-westfalen"),
 "hamm":("Hamm","nordrhein-westfalen"),"koeln":("Köln","nordrhein-westfalen"),
 "krefeld":("Krefeld","nordrhein-westfalen"),"leverkusen":("Leverkusen","nordrhein-westfalen"),
 "moenchengladbach":("Mönchengladbach","nordrhein-westfalen"),"muelheim":("Mülheim","nordrhein-westfalen"),
 "muenster":("Münster","nordrhein-westfalen"),"oberhausen":("Oberhausen","nordrhein-westfalen"),
 "wuppertal":("Wuppertal","nordrhein-westfalen"),
 "ludwigshafen":("Ludwigshafen","rheinland-pfalz"),"mainz":("Mainz","rheinland-pfalz"),
 "saarbruecken":("Saarbrücken","saarland"),
 "chemnitz":("Chemnitz","sachsen"),"dresden":("Dresden","sachsen"),"leipzig":("Leipzig","sachsen"),
 "halle":("Halle","sachsen-anhalt"),"magdeburg":("Magdeburg","sachsen-anhalt"),
 "kiel":("Kiel","schleswig-holstein"),"luebeck":("Lübeck","schleswig-holstein"),
 "erfurt":("Erfurt","thueringen"),
}

def block(slug, stadt, bl):
    blname = BL_SHORT.get(bl, BL[bl])
    return (
'  <div class="mr-related">\n'
'    <h2>Passend dazu</h2>\n'
'    <ul>\n'
f'      <li><a href="/friedhoefe/{slug}/">Friedhöfe in {stadt}</a> — Überblick, Träger und Gebühren</li>\n'
f'      <li><a href="/bestattung-in/{bl}/">Bestattungsrecht in {blname}</a> — Fristen, Sargpflicht, Ruhezeiten</li>\n'
'      <li><a href="/tools/bestattungskosten-rechner/">Bestattungskosten-Rechner</a> — Kostenrahmen für deine Region</li>\n'
'    </ul>\n'
'  </div>\n'
)

added=[]; skipped_linked=[]; skipped_noov=[]; errors=[]
for slug,(stadt,bl) in sorted(ST.items()):
    p = os.path.join(ROOT,"bestatter",slug,"index.html")
    ov = os.path.join(ROOT,"friedhoefe",slug,"index.html")
    if not os.path.exists(p): errors.append(f"{slug}: bestatter-Seite fehlt"); continue
    if not os.path.exists(ov): skipped_noov.append(slug); continue
    html = open(p,encoding="utf-8").read()
    if f'/friedhoefe/{slug}/' in html: skipped_linked.append(slug); continue
    if 'mr-related' in html: skipped_linked.append(slug+"(hat mr-related)"); continue
    if html.count("</main>")<1: errors.append(f"{slug}: kein </main>"); continue
    blk = block(slug,stadt,bl)
    # vor dem LETZTEN </main> einfuegen
    idx = html.rfind("</main>")
    new = html[:idx] + blk + html[idx:]
    # Asserts
    assert new.count("</main>")==html.count("</main>")
    assert new.count('class="mr-related"')==html.count('class="mr-related"')+1
    assert f'href="/friedhoefe/{slug}/"' in new
    if not DRY:
        open(p,"w",encoding="utf-8").write(new)
    added.append(slug)

print(f"=== {'DRY-RUN' if DRY else 'APPLY'} ===")
print(f"ADD ({len(added)}): {', '.join(added)}")
print(f"SKIP-schon-verlinkt ({len(skipped_linked)}): {', '.join(skipped_linked)}")
print(f"SKIP-keine-Uebersicht ({len(skipped_noov)}): {', '.join(skipped_noov)}")
if errors: print(f"FEHLER ({len(errors)}): {'; '.join(errors)}")
