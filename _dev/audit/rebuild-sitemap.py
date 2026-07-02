"""
Sitemap-Regenerator:
- Per-Page lastmod aus Git-Log (letzter Commit der Datei)
- Stadt-Pages Priority 0.7 (vorher 0.6)
- Neue Hub-Page /bestattung-in/ ergänzt
- noindex-Pages (luebeck, moenchengladbach) ausgeschlossen
"""
import os
import re
import subprocess
from pathlib import Path
from datetime import date

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent

# noindex-Pages
NOINDEX = {"bestatter/luebeck", "bestatter/moenchengladbach"}


def git_lastmod(rel_path: str) -> str:
    """Return YYYY-MM-DD of the last git commit that touched this file."""
    try:
        out = subprocess.check_output(
            ["git", "log", "-1", "--format=%cs", "--", rel_path],
            cwd=str(ROOT),
            text=True,
        ).strip()
        return out or date.today().isoformat()
    except Exception:
        return date.today().isoformat()


def is_noindex(path: Path) -> bool:
    """Check if file has <meta name="robots" content="noindex">."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        return bool(re.search(r'<meta[^>]*name="robots"[^>]*content="[^"]*noindex', text, re.IGNORECASE))
    except Exception:
        return False


urls = []

# Startseite
urls.append({
    "loc": "https://machsruhig.de/",
    "lastmod": git_lastmod("index.html"),
    "changefreq": "weekly",
    "priority": "1.0",
    "comment": "Startseite",
})

# Kern-Content (Root-Landingpages) — AUTO-DISCOVERY statt Hardcode-Liste,
# damit nie wieder valide Seiten still aus der Sitemap fallen (Drift-Bug 06-2026:
# 19 Root-Seiten fehlten in der alten Hardcode-Liste). Prioritaet/changefreq per
# Lookup; neue Root-Seiten bekommen den Default 0.7/monthly automatisch.
ROOT_PRIO = {
    "beerdigung-planen": ("0.9", "monthly"),
    "bestattungsarten": ("0.9", "monthly"),
    "bestattungskosten": ("0.9", "monthly"),
    "bestattungskosten-nach-bundesland": ("0.8", "monthly"),
    "trauerrede-schreiben": ("0.85", "monthly"),
    "danksagung-nach-beerdigung": ("0.85", "monthly"),
    "abschiedsbrief-schreiben": ("0.85", "monthly"),
    "notfallkarte": ("0.85", "monthly"),
    "fristen-nach-todesfall": ("0.85", "monthly"),
    "was-tun-nach-todesfall": ("0.85", "monthly"),
    "kondolenzschreiben": ("0.8", "monthly"),
    "trauersprueche": ("0.8", "monthly"),
    "vertraege-kuendigen": ("0.8", "monthly"),
    "sozialbestattung": ("0.8", "monthly"),
    "vorsorge-allein-leben": ("0.8", "monthly"),
    "kindern-tod-erklaeren": ("0.75", "monthly"),
    "bestatter-angebot-pruefen": ("0.7", "monthly"),
    "bestatter-angebot-vergleichen": ("0.7", "monthly"),
    "bestatter-rechnung-pruefen": ("0.7", "monthly"),
    "bestattungskosten-versteckte-kosten": ("0.7", "monthly"),
    "erdbestattung-angebot-pruefen": ("0.7", "monthly"),
    "feuerbestattung-angebot-pruefen": ("0.7", "monthly"),
    "seebestattung-angebot-pruefen": ("0.7", "monthly"),
    "was-muss-im-kostenvoranschlag-stehen": ("0.7", "monthly"),
    "methodik": ("0.6", "monthly"),
    "ueber-uns": ("0.6", "yearly"),
    "fuer-bestatter": ("0.5", "monthly"),
    "kontakt": ("0.4", "yearly"),
    "impressum": ("0.3", "yearly"),
    "datenschutz": ("0.3", "yearly"),
}
EXCLUDE_ROOT = {"index.html", "404.html"}  # + alle danke-*.html (Conversion-Seiten, nicht in Sitemap)
for fname in sorted(f for f in os.listdir(ROOT) if f.endswith(".html")):
    if fname in EXCLUDE_ROOT or fname.startswith("danke-"):
        continue
    p = ROOT / fname
    if is_noindex(p):
        continue
    slug = fname[:-5]
    prio, cf = ROOT_PRIO.get(slug, ("0.7", "monthly"))
    urls.append({
        "loc": f"https://machsruhig.de/{slug}",
        "lastmod": git_lastmod(fname),
        "changefreq": cf,
        "priority": prio,
    })

# Tools
for tool in sorted(os.listdir(ROOT / "tools")):
    p = ROOT / "tools" / tool / "index.html"
    if not p.exists():
        continue
    if is_noindex(p):
        continue
    rel = f"tools/{tool}/index.html"
    urls.append({
        "loc": f"https://machsruhig.de/tools/{tool}/",
        "lastmod": git_lastmod(rel),
        "changefreq": "monthly",
        "priority": "0.7",
    })

# Vorsorge
if (ROOT / "vorsorge" / "index.html").exists():
    urls.append({
        "loc": "https://machsruhig.de/vorsorge/",
        "lastmod": git_lastmod("vorsorge/index.html"),
        "changefreq": "monthly",
        "priority": "0.85",
        "comment": "Vorsorge-Hub",
    })

vorsorge_pages = [
    ("bestattungsvorsorge", "0.75"),
    ("digitaler-nachlass", "0.7"),
    ("patientenverfuegung", "0.8"),
    ("sorgerechtsverfuegung", "0.7"),
    ("sterbegeldversicherung", "0.75"),
    ("testament", "0.8"),
    ("vorsorge-ordner", "0.7"),
    ("ohne-vorsorge", "0.65"),
]
for slug, prio in vorsorge_pages:
    rel = f"vorsorge/{slug}/index.html"
    if not (ROOT / rel).exists():
        continue
    if is_noindex(ROOT / rel):
        continue
    urls.append({
        "loc": f"https://machsruhig.de/vorsorge/{slug}/",
        "lastmod": git_lastmod(rel),
        "changefreq": "monthly",
        "priority": prio,
    })

# Bestatter-Hub
if (ROOT / "bestatter" / "index.html").exists():
    urls.append({
        "loc": "https://machsruhig.de/bestatter/",
        "lastmod": git_lastmod("bestatter/index.html"),
        "changefreq": "weekly",
        "priority": "0.9",
        "comment": "Bestatter-Hub",
    })

# Bestattung-in Hub (NEU 21.05)
if (ROOT / "bestattung-in" / "index.html").exists():
    urls.append({
        "loc": "https://machsruhig.de/bestattung-in/",
        "lastmod": git_lastmod("bestattung-in/index.html"),
        "changefreq": "weekly",
        "priority": "0.85",
        "comment": "Bestattung-in Hub (16 Bundesländer)",
    })

# BL-Pages
for bl in sorted(os.listdir(ROOT / "bestattung-in")):
    # Umlaut-Verzeichnisse sind Duplikate der ASCII-Kanons (baden-wuerttemberg, thueringen) → skip
    if bl in {"baden-württemberg", "thüringen"}:
        continue
    p = ROOT / "bestattung-in" / bl / "index.html"
    if not p.exists():
        continue
    if is_noindex(p):
        continue
    # URL-encode umlauts
    import urllib.parse
    bl_encoded = urllib.parse.quote(bl, safe="-")
    urls.append({
        "loc": f"https://machsruhig.de/bestattung-in/{bl_encoded}/",
        "lastmod": git_lastmod(f"bestattung-in/{bl}/index.html"),
        "changefreq": "monthly",
        "priority": "0.7",
    })

# Stadt-Pages
city_count = 0
for city in sorted(os.listdir(ROOT / "bestatter")):
    p = ROOT / "bestatter" / city / "index.html"
    if not p.exists():
        continue
    rel = f"bestatter/{city}/index.html"
    if is_noindex(p):
        print(f"  noindex (skip): {city}")
        continue
    # Skip lübeck / mönchengladbach (duplicate dirs with umlauts)
    if city in {"lübeck", "mönchengladbach"}:
        continue
    urls.append({
        "loc": f"https://machsruhig.de/bestatter/{city}/",
        "lastmod": git_lastmod(rel),
        "changefreq": "monthly",
        "priority": "0.7",  # vorher 0.6, neu 0.7
    })
    city_count += 1

# Build XML
out = ['<?xml version="1.0" encoding="UTF-8"?>']
out.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

last_comment = None
for u in urls:
    c = u.get("comment")
    if c and c != last_comment:
        out.append("")
        out.append(f"  <!-- === {c} === -->")
        last_comment = c
    out.append("  <url>")
    out.append(f'    <loc>{u["loc"]}</loc>')
    out.append(f'    <lastmod>{u["lastmod"]}</lastmod>')
    out.append(f'    <changefreq>{u["changefreq"]}</changefreq>')
    out.append(f'    <priority>{u["priority"]}</priority>')
    out.append("  </url>")

out.append("</urlset>")
out.append("")

sitemap_path = ROOT / "sitemap.xml"
new_text = "\n".join(out)
old_text = sitemap_path.read_text(encoding="utf-8") if sitemap_path.exists() else ""

sitemap_path.write_text(new_text, encoding="utf-8")

# Summary
from collections import Counter
date_counts = Counter(u["lastmod"] for u in urls)
print(f"\nGenerated {len(urls)} URLs:")
for date_, count in sorted(date_counts.items(), reverse=True):
    print(f"  {date_}: {count}")
print(f"\nCity-Pages: {city_count} (vorher 49)")
print(f"BL-Pages: {sum(1 for u in urls if '/bestattung-in/' in u['loc'] and u['loc'].endswith('/') and u['loc'] != 'https://machsruhig.de/bestattung-in/')}")
print(f"Tools: {sum(1 for u in urls if '/tools/' in u['loc'])}")
print(f"\nFile: {sitemap_path}")
print(f"Old size: {len(old_text)} chars / New size: {len(new_text)} chars")
