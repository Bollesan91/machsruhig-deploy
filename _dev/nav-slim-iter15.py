#!/usr/bin/env python3
"""
iter-15 (2026-06-04): Nav verschlankt + ausgerichtet (User-Wunsch).
- 12 Top-Links -> 7 Kern-Links (Was tun?/Beerdigung/Kosten/Vorsorge/Bestatter/
  Trauerrede/Notfallkarte). /ratgeber/ verworfen (leitet auf Startseite um).
- Haupt-Nav (nav|header mit class=mr-nav, balanciert) site-weit ersetzt.
- .mr-nav-inner auf max-width:720px (= Inhaltsbreite) -> linke Kante bündig
  mit dem Text, kein 'Schweben'; 7 Links passen einzeilig.
- Breadcrumb auf dieselbe Breite zentriert.
Nur Produktivseiten mit mr-nav-Wrapper (121).
"""
import glob, re, os

MARKER = "iter-15 nav-slim"

CANON_NAV = '''<nav class="mr-nav no-print">
  <div class="mr-nav-inner">
    <a href="/" class="mr-nav-logo">mach's <span>ruhig</span></a>
    <button class="mr-nav-toggle" aria-label="Menü öffnen" type="button"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg></button>
    <div class="mr-nav-links">
      <a href="/was-tun-nach-todesfall">Was tun?</a>
      <a href="/beerdigung-planen">Beerdigung</a>
      <a href="/bestattungskosten">Kosten</a>
      <a href="/vorsorge/">Vorsorge</a>
      <a href="/bestatter/">Bestatter</a>
      <a href="/trauerrede-schreiben">Trauerrede</a>
      <a href="/notfallkarte">Notfallkarte</a>
    </div>
  </div>
</nav>'''

NAV_CSS = """
/* """ + MARKER + """ (2026-06-04): 7-Link-Nav, an Inhaltsbreite (720px) ausgerichtet */
.mr-nav-inner{max-width:720px;margin:0 auto;display:flex;align-items:center;justify-content:flex-start;gap:6px 14px;flex-wrap:wrap;min-height:56px}
.mr-nav-logo{margin-right:auto;font-family:'Fraunces',Georgia,serif;font-size:18px;font-weight:700;color:var(--mr-text,#2D2319);text-decoration:none;white-space:nowrap}
.mr-breadcrumb{max-width:720px;margin:0 auto;padding:16px 20px 0}
"""

def _span_of_mr_nav(html):
    m = re.search(r'<(nav|header)\b[^>]*\bclass="mr-nav[ "]', html)
    if not m:
        return None
    tag = m.group(1); start = m.start()
    opens = [mm.start() for mm in re.finditer(r'<' + tag + r'\b', html)]
    closes = [(mm.start(), mm.end()) for mm in re.finditer(r'</' + tag + r'\s*>', html)]
    close_end = {p: e for p, e in closes}
    events = sorted([(p, 'o') for p in opens] + [(p, 'c') for p, e in closes])
    depth = 0
    for p, t in events:
        if p < start: continue
        depth += 1 if t == 'o' else -1
        if t == 'c' and depth == 0:
            return (start, close_end[p])
    return None

changed = []
for f in glob.glob("**/*.html", recursive=True):
    nf = f.replace("\\", "/")
    if nf.startswith("_dev/"):
        continue
    html = open(f, encoding="utf-8").read()
    span = _span_of_mr_nav(html)
    if not span:
        continue
    s, e = span
    new = html[:s] + CANON_NAV + html[e:]
    if MARKER not in new:
        idx = new.rfind("</style>")
        if idx != -1:
            new = new[:idx] + NAV_CSS + new[idx:]
    if new != html:
        open(f, "w", encoding="utf-8").write(new)
        changed.append(nf)

print(f"Geaendert: {len(changed)} Seiten")
