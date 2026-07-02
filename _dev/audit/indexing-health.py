"""
Indexierungs-Gesundheits-Audit: pro indexierbarer Seite (aus sitemap.xml) Signale,
die fuer 'discovered, not indexed' relevant sind:
  - sichtbare Wortzahl (thin content?)
  - interne Inbound-Links (Orphan/under-linked?)
  - Title-Laenge, Meta-Description (+Laenge), Canonical, OG-Image
  - JSON-LD-Schema-Typen; FAQPage ohne sichtbaren FAQ-Block (Heuristik)
Rein lesend, keine Schreibvorgaenge.
"""
import os, re, html, urllib.parse
from pathlib import Path
from collections import defaultdict

HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = HERE.parent.parent

def loc_to_rel(loc):
    p = urllib.parse.unquote(loc.replace("https://machsruhig.de", ""))
    if p == "/": return "index.html"
    if p.endswith("/"): return p.strip("/") + "/index.html"
    return p.strip("/") + ".html"

# indexierbare Seiten aus Sitemap
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
pages = []  # (url_path, relfile)
for loc in re.findall(r"<loc>([^<]+)</loc>", sm):
    rel = loc_to_rel(loc)
    if (ROOT / rel).exists():
        pages.append((loc.replace("https://machsruhig.de",""), rel))

def visible_words(t):
    t = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    t = re.sub(r"<style[\s\S]*?</style>", " ", t, flags=re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    return len(re.findall(r"\b\w+\b", t))

# Inbound-Link-Zaehlung: ueber ALLE html-Dateien hrefs sammeln
def norm_href(h):
    h = h.split("#")[0].split("?")[0]
    if h.startswith("http"):
        if "machsruhig.de" not in h: return None
        h = re.sub(r"^https?://(www\.)?machsruhig\.de", "", h)
    if not h.startswith("/"): return None
    return h.rstrip("/") or "/"

inbound = defaultdict(set)
all_html = list(ROOT.rglob("*.html"))
for f in all_html:
    if "/_dev/" in f.as_posix() or "/node_modules/" in f.as_posix(): continue
    src = f.relative_to(ROOT).as_posix()
    try: txt = f.read_text(encoding="utf-8", errors="replace")
    except: continue
    for h in re.findall(r'href="([^"]+)"', txt):
        nh = norm_href(h)
        if nh: inbound[nh].add(src)

rows = []
for url_path, rel in pages:
    t = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
    words = visible_words(t)
    title = re.search(r"<title>([^<]*)</title>", t)
    title = title.group(1).strip() if title else ""
    md = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', t, re.I)
    md = md.group(1) if md else ""
    canonical = bool(re.search(r'rel="canonical"', t, re.I))
    og = bool(re.search(r'property="og:image"', t, re.I))
    schemas = re.findall(r'"@type"\s*:\s*"([^"]+)"', t)
    has_faq_schema = "FAQPage" in schemas
    # sichtbarer FAQ-Block-Heuristik: <details> oder "Häufige Fragen"/FAQ-Ueberschrift
    visible_faq = bool(re.search(r"<details|Häufige Fragen|Häufig gestellte|FAQ", t, re.I))
    key = url_path.rstrip("/") or "/"
    inb = len(inbound.get(key, set()))
    rows.append(dict(url=url_path, words=words, inbound=inb, title_len=len(title),
                     md_len=len(md), canonical=canonical, og=og,
                     faq_schema_no_block=(has_faq_schema and not visible_faq),
                     n_schema=len(set(schemas))))

def flag(r):
    f=[]
    if r["words"]<350: f.append(f"THIN({r['words']}w)")
    if r["inbound"]<=2: f.append(f"ORPHAN({r['inbound']}in)")
    if r["title_len"]==0 or r["title_len"]>62: f.append(f"TITLE({r['title_len']})")
    if r["md_len"]==0: f.append("noMETA")
    elif r["md_len"]>165: f.append(f"META({r['md_len']})")
    if not r["canonical"]: f.append("noCANON")
    if not r["og"]: f.append("noOG")
    if r["faq_schema_no_block"]: f.append("FAQschema!block")
    if r["n_schema"]==0: f.append("noSCHEMA")
    return f

print(f"Indexierbare Seiten: {len(rows)}\n")
print("=== SEITEN MIT FLAGS (sortiert: wenigste Inbound-Links zuerst) ===")
flagged=[(r,flag(r)) for r in rows]
flagged=[x for x in flagged if x[1]]
flagged.sort(key=lambda x:(x[0]["inbound"], x[0]["words"]))
for r,fl in flagged:
    print(f"{r['inbound']:>2}in {r['words']:>4}w  {r['url']:<45} {' '.join(fl)}")
print(f"\nGeflaggt: {len(flagged)}/{len(rows)}")
# Aggregat
from collections import Counter
c=Counter()
for _,fl in flagged:
    for x in fl: c[x.split('(')[0]] += 1
print("\n=== Häufigkeit je Flag-Typ ===")
for k,v in c.most_common(): print(f"  {k}: {v}")
