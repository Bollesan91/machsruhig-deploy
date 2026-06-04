#!/usr/bin/env python3
"""
iter-12 (2026-06-04): Stadt-Nav-Fragmentierung beenden — ALLE 52 auf kanonisches
Berlin-Nav normalisieren (Markup ersetzen) + garantiertes Nav-/Breadcrumb-CSS.

v2: BALANCIERTER Nav-Matcher (zaehlt <nav>/</nav>-Verschachtelung). Noetig, weil
einige Seiten ein verschachteltes <nav class="mr-nav"> ... <nav class="mr-nav-links">
haben — ein non-greedy Regex stoppt sonst am inneren </nav> und zerlegt das DOM.
"""
import glob, re, os

MARKER = "iter-12 nav-normalize"

NAV_CSS = """
/* """ + MARKER + """ (2026-06-04): kanonisches Nav-/Breadcrumb-CSS, garantiert auf jeder Stadt-Seite */
.mr-nav{position:sticky;top:0;z-index:100;background:rgba(250,248,245,.95);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-bottom:1px solid var(--mr-border,#E8E0D6);padding:0 20px}
.mr-nav-inner{max-width:960px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:8px;min-height:56px;flex-wrap:wrap}
.mr-nav-logo{font-family:'Fraunces',Georgia,serif;font-size:18px;font-weight:700;color:var(--mr-text,#2D2319);text-decoration:none;white-space:nowrap}
.mr-nav-logo span{color:var(--mr-primary,#7A6B5D)}
.mr-nav-links{display:flex;flex-wrap:wrap;gap:2px 4px;align-items:center}
.mr-nav-links a{font-size:13px;font-weight:500;color:var(--mr-text-muted,#73655A);text-decoration:none;padding:6px 10px;border-radius:8px;transition:color .2s,background .2s}
.mr-nav-links a:hover{color:var(--mr-text,#2D2319);background:rgba(122,107,93,.08)}
.mr-nav-divider{width:1px;height:16px;background:var(--mr-border,#E8E0D6);margin:0 4px}
.mr-nav-toggle{display:none;background:none;border:none;cursor:pointer;color:var(--mr-text,#2D2319);padding:8px}
.mr-breadcrumb ol{list-style:none;display:flex;flex-wrap:wrap;gap:0;margin:0;padding:0}
.mr-breadcrumb ol li{display:inline-flex;align-items:center}
.mr-breadcrumb ol li+li::before{content:'\\203A';margin:0 8px;color:var(--mr-text-muted,#73655A)}
"""

def _span_of_mr_nav(html):
    """Findet Start/Ende des Haupt-Nav-Wrappers (<nav> ODER <header> mit class='mr-nav'
    Token), balanciert ueber den jeweiligen Tag-Namen (handhabt Verschachtelung)."""
    m = re.search(r'<(nav|header)\b[^>]*\bclass="mr-nav[ "]', html)
    if not m:
        return None
    tag = m.group(1)
    start = m.start()
    opens = [mm.start() for mm in re.finditer(r'<' + tag + r'\b', html)]
    closes = [(mm.start(), mm.end()) for mm in re.finditer(r'</' + tag + r'\s*>', html)]
    close_end = {p: e for p, e in closes}
    events = sorted([(p, 'o') for p in opens] + [(p, 'c') for p, e in closes])
    depth = 0
    for p, t in events:
        if p < start:
            continue
        depth += 1 if t == 'o' else -1
        if t == 'c' and depth == 0:
            return (start, close_end[p])
    return None

def replace_main_nav(html, canon):
    span = _span_of_mr_nav(html)
    if not span:
        return html, False
    s, e = span
    return html[:s] + canon + html[e:], True

# Kanonisches Nav aus Berlin (balanciert extrahiert)
berlin = open("bestatter/berlin/index.html", encoding="utf-8").read()
_span = _span_of_mr_nav(berlin)
assert _span, "Berlin-Nav-Wrapper nicht gefunden!"
CANON_NAV = berlin[_span[0]:_span[1]]
assert CANON_NAV and 'mr-nav-logo' in CANON_NAV and 'mr-nav-links' in CANON_NAV, "Berlin-Nav nicht kanonisch!"
assert CANON_NAV.count('<nav') == CANON_NAV.count('</nav'), "Berlin-Nav unbalanciert!"

changed = []
for f in glob.glob("bestatter/*/index.html"):
    html = open(f, encoding="utf-8").read()
    new, did = replace_main_nav(html, CANON_NAV)
    if MARKER not in new:
        idx = new.rfind("</style>")
        if idx != -1:
            new = new[:idx] + NAV_CSS + new[idx:]
    if new != html:
        open(f, "w", encoding="utf-8").write(new)
        changed.append(os.path.basename(os.path.dirname(f)))

print(f"Kanonisches Nav: {CANON_NAV.count(chr(60)+'a ')} Links, balanciert={CANON_NAV.count('<nav')}/{CANON_NAV.count('</nav')}")
print(f"Geaendert: {len(changed)}")
