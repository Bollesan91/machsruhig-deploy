#!/usr/bin/env python3
# Stadt-Hub sauber: die 50 Friedhof-Stadt-UEBERSICHTEN nach oben zum /friedhoefe/-Hub verlinken.
# Aendert HTML-Breadcrumb UND JSON-LD-BreadcrumbList konsistent (3-stufig: Start > Friedhoefe > Stadt).
# Idempotent (skip wenn schon verlinkt), JSON-LD-Parse als Assert. Nur depth-1 Uebersichten (nicht Hub, nicht Detailseiten).
import os, re, sys, json, glob
DRY = "--apply" not in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# nur friedhoefe/<stadt>/index.html (depth 1); Hub = friedhoefe/index.html ausschliessen; Detailseiten = depth 2 ausschliessen
paths = sorted(glob.glob(os.path.join(ROOT,"friedhoefe","*","index.html")))

re_html = re.compile(r'(<nav class="mr-breadcrumb"[^>]*><a href="/">Start</a> › )Friedhöfe ([^<]+?)(</nav>)')
re_json = re.compile(r'\{"@type":"ListItem","position":2,"name":"Friedhöfe ([^"]+)","item":"(https://machsruhig\.de/friedhoefe/[^"]+/)"\}')

def jsonld_ok(html):
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    if not m: return False
    try: json.loads(m.group(1)); return True
    except Exception: return False

done=[]; skip=[]; err=[]
for p in paths:
    slug = os.path.basename(os.path.dirname(p))
    html = open(p,encoding="utf-8").read()
    if '<a href="/friedhoefe/">Friedhöfe</a>' in html: skip.append(slug+"(schon)"); continue
    h2 = re_html.sub(r'\1<a href="/friedhoefe/">Friedhöfe</a> › \2\3', html, count=1)
    if h2 == html: skip.append(slug+"(kein-HTML-Match)"); continue
    j2 = re_json.sub(r'{"@type":"ListItem","position":2,"name":"Friedhöfe","item":"https://machsruhig.de/friedhoefe/"},\n      {"@type":"ListItem","position":3,"name":"\1","item":"\2"}', h2, count=1)
    if j2 == h2: err.append(slug+": kein-JSON-Match"); continue
    if not jsonld_ok(j2): err.append(slug+": JSON-LD kaputt"); continue
    # Asserts
    assert j2.count('<a href="/friedhoefe/">Friedhöfe</a>')==1
    assert '"position":3' in j2 and '"position":2,"name":"Friedhöfe"' in j2
    if not DRY: open(p,"w",encoding="utf-8").write(j2)
    done.append(slug)

print(f"=== {'DRY-RUN' if DRY else 'APPLY'} ===  Uebersichten gefunden: {len(paths)}")
print(f"GEAENDERT ({len(done)}): {', '.join(done)}")
print(f"SKIP ({len(skip)}): {', '.join(skip)}")
if err: print(f"FEHLER ({len(err)}): {'; '.join(err)}")
