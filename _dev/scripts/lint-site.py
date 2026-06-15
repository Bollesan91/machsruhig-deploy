#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lint-site.py — Helfer-V4.1 Stufe 1 (deterministische Gates) fuer machsruhig.
0 FAIL ist Pflicht vor jedem Review und jedem Deploy.

Checks (v1):
  L1  tote interne Links (href="/..." ohne Ziel-Datei)
  L2  JSON-LD nicht parsebar
  L3  FAQPage: JSON-LD-Fragen ohne sichtbares Pendant im Body
  L4  €-Betraege im FAQ-JSON-LD, die im sichtbaren Text fehlen (Drift-Klasse)
  L5  verbotene Strings (_dev/config/lint-verboten.txt)
  L6  Umami mehrfach eingebunden
  L7  var(--mr-*) ohne Fallback auf Seiten OHNE site.css
  L8  verschachteltes @media
  L9  doppelte id="..."-Attribute
  L10 Opt-In-Behauptung auf Head-Load-Seite (konditional)
  L11 className= ohne Babel/JSX
  L12 uneinheitlicher Seiten-Stand (Monat)
Aufruf: python _dev/scripts/lint-site.py [--quiet]
Exit-Code 0 = gruen, 1 = FAILs vorhanden.
"""
import io, os, re, sys, json, html as _html
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
SKIP_DIRS = {'.git', '_dev', 'node_modules', '.wrangler', '.claude', 'templates'}
QUIET = '--quiet' in sys.argv

def visible_text(html):
    t = re.sub(r'<script\b.*?</script>', ' ', html, flags=re.S | re.I)
    t = re.sub(r'<style\b.*?</style>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    return t

def norm_spaces(s):
    return re.sub(r'[\s ]+', ' ', _html.unescape(s)).strip()

def load_forbidden():
    p = os.path.join(ROOT, '_dev', 'config', 'lint-verboten.txt')
    out = []
    if os.path.exists(p):
        for line in io.open(p, encoding='utf-8'):
            line = line.strip()
            if line and not line.startswith('#'):
                out.append(line)
    return out

def load_redirect_sources():
    p = os.path.join(ROOT, '_redirects')
    exact, prefixes = set(), []
    if os.path.exists(p):
        for line in io.open(p, encoding='utf-8', errors='replace'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            src = line.split()[0]
            if src.endswith('*'):
                prefixes.append(src[:-1])
            else:
                exact.add(src.rstrip('/')) ; exact.add(src)
    return exact, prefixes

REDIR_EXACT, REDIR_PREFIX = (None, None)

def link_target_exists(href):
    global REDIR_EXACT, REDIR_PREFIX
    if REDIR_EXACT is None:
        REDIR_EXACT, REDIR_PREFIX = load_redirect_sources()
    path = href.split('#')[0].split('?')[0]
    if path in REDIR_EXACT or path.rstrip('/') in REDIR_EXACT:
        return True
    if any(path.startswith(pfx) for pfx in REDIR_PREFIX):
        return True
    if not path or path == '/':
        return True
    rel = path.lstrip('/')
    cand = [os.path.join(ROOT, rel.rstrip('/'), 'index.html'),
            os.path.join(ROOT, rel.rstrip('/') + '.html'),
            os.path.join(ROOT, rel)]
    return any(os.path.isfile(c) for c in cand)

def euro_amounts(text):
    # 1.234 / 12.345 / 939 vor optionalem Spannen-Teil, gefolgt von € im Umkreis
    out = set()
    for m in re.finditer(r'(\d{1,3}(?:\.\d{3})+|\d{3,4})(?=(?:[\s ]?(?:–|-|bis)[\s ]?\d[\d\.]*)?[\s ]?(?:€|Euro))', text):
        out.add(m.group(1))
    return out

def main():
    forbidden = load_forbidden()
    fails, warns, triages = [], [], []
    pages = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith('.html'):
                pages.append(os.path.join(dirpath, fn))
    pages.sort()

    for fp in pages:
        rel = os.path.relpath(fp, ROOT).replace('\\', '/')
        html = io.open(fp, encoding='utf-8', errors='replace').read()
        vis = norm_spaces(visible_text(html))

        # L1 tote interne Links
        for href in set(re.findall(r'href="(/[^"]*)"', html)):
            if href.startswith(('//', '/cdn-cgi')):
                continue
            if not link_target_exists(href):
                fails.append((rel, 'L1', 'toter interner Link: %s' % href))

        # L2-L4 JSON-LD
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            raw = m.group(1)
            try:
                data = json.loads(raw)
            except Exception as e:
                fails.append((rel, 'L2', 'JSON-LD nicht parsebar: %s' % e))
                continue
            nodes = data.get('@graph', [data]) if isinstance(data, dict) else data
            if isinstance(nodes, dict):
                nodes = [nodes]
            # JS-gerenderte FAQ (Babel/JSX, <details> nur in <script>) -> statisch nicht pruefbar
            js_faq = ('text/babel' in html or 'className=' in html)
            static_details = False
            _spans = [(mm.start(), mm.end()) for mm in re.finditer(r'<script[^>]*>.*?</script>', html, re.S | re.I)]
            for dm in re.finditer(r'<details', html):
                if not any(a <= dm.start() < b for a, b in _spans):
                    static_details = True; break
            for node in nodes:
                if not isinstance(node, dict) or node.get('@type') != 'FAQPage':
                    continue
                if js_faq and not static_details:
                    continue  # L3 nicht statisch entscheidbar -> Browser-Smoke (Stufe 3)
                for q in node.get('mainEntity', []):
                    name = norm_spaces(q.get('name', ''))
                    if name and name[:60] not in vis:
                        fails.append((rel, 'L3', 'FAQ-Frage ohne sichtbares Pendant: %s…' % name[:50]))
                    ans = norm_spaces((q.get('acceptedAnswer') or {}).get('text', ''))
                    for amt in euro_amounts(ans):
                        if amt not in vis:
                            fails.append((rel, 'L4', 'Betrag %s € nur im JSON-LD, nicht im sichtbaren Text' % amt))

        # L5 verbotene Strings
        for s in forbidden:
            if s in html:
                fails.append((rel, 'L5', 'verbotener String: "%s"' % s[:50]))

        # L6 Umami
        c = html.count('umami.is/script.js')
        if c > 1:
            fails.append((rel, 'L6', 'Umami %d× eingebunden' % c))

        # L7 var ohne Fallback auf Standalone-Seiten
        if 'assets/css/site.css' not in html:
            novars = sorted(set(re.findall(r'var\((--mr-[a-z-]+)\)(?!,)', html)))
            if novars:
                fails.append((rel, 'L7', 'var() ohne Fallback (kein site.css): %s' % ', '.join(novars[:5])))

        # L8 nested @media
        for blk in re.finditer(r'@media[^{]*\{', html):
            depth, i = 1, blk.end()
            while i < len(html) and depth > 0:
                if html[i] == '{':
                    depth += 1
                elif html[i] == '}':
                    depth -= 1
                elif html.startswith('@media', i):
                    fails.append((rel, 'L8', 'verschachteltes @media'))
                    depth = 0
                i += 1

        # L10 Opt-In-Behauptung auf Head-Load-Seite (konditional)
        if 'umami.is/script.js' in html and 'consent.js' not in html:
            if re.search(r'nur nach (deinem )?(Cookie-)?Opt-?In', html):
                fails.append((rel, 'L10', 'behauptet Opt-In, laedt Umami aber direkt im Head'))

        # L12 page-Stand-Konsistenz (mehrere verschiedene Monats-Staende = Drift)
        months = set(re.findall(r'Stand:?\s+(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s+20\d\d', html))
        if len(months) > 1:
            fails.append((rel, 'L12', 'uneinheitlicher Seiten-Stand: %s' % ', '.join(sorted(months))))

        # L11 className= ohne Babel (Browser ignoriert das Attr -> CSS-Klasse wirkungslos)
        if 'className=' in html and 'text/babel' not in html:
            fails.append((rel, 'L11', 'className= ohne Babel/JSX (sollte class= sein)'))

        # ===== TRIAGE (T-Codes: informational, kein Gate-Bruch) =====
        # T1 Tourismus-Ton/Superlative (LEKTION 11) — auf Stadt-/BL-Seiten
        if '/bestatter/' in rel or '/bestattung-in/' in rel:
            for w in ['ein muss', 'weltgrößt', 'weltberühmt', 'atemberaubend', 'touristenmagnet',
                      'geheimtipp', 'wahres juwel', 'perle ', 'schmuckstück', 'unvergesslich', 'einzigartig']:
                if w in vis.lower():
                    triages.append((rel, 'T1', 'Tourismus-Ton/Superlativ: "%s"' % w))
        # T2 Bundesland-Pauschale (LEKTION 8)
        for m2 in re.finditer(r'(.{0,18})(in allen Bundesländern|bundesweit einheitlich|überall in Deutschland gilt|in jedem Bundesland gilt)', html):
            pre = m2.group(1).lower()
            if 'nicht ' in pre or 'kein' in pre:   # korrekte Verneinung -> kein Befund
                continue
            post = html[m2.end():m2.end()+40].lower()
            if 'nur ' in post or 'randbereich' in post:  # "bundesweit einheitlich sind nur Randbereiche" = korrekt
                continue
            triages.append((rel, 'T2', 'BL-Pauschale: "%s"' % m2.group(2)))
        # T3 §-Kategorienfehler-Risiko (LEKTION 7): "bundesrecht" nahe Landesgesetz-Kürzel
        if re.search(r'bundesrecht\w*[^.]{0,120}(BestattG|BestG|Friedhofs)', html):
            triages.append((rel, 'T3', 'mögl. Landes/Bundesrecht-Kategorienfehler'))
        # T4 Check24-Affiliate im Sozialbestattungs-Kontext (LEKTION 21)
        si = html.find('Sozialbestattung')
        if si >= 0:
            win = html[si:si+3000]
            if 'check24.de/sterbegeldversicherung/"' in win or ('rel="sponsored' in win and 'check24' in win):
                triages.append((rel, 'T4', 'Check24-Affiliate-CTA im Sozial-Kontext'))
        # L9 doppelte IDs
        ids = re.findall(r'\bid="([^"]+)"', html)
        for dup in sorted({i for i in ids if ids.count(i) > 1}):
            fails.append((rel, 'L9', 'doppelte id="%s" (%d×)' % (dup, ids.count(dup))))

    # Baseline: bekannte Alt-FAILs (Abbau-Paket) zaehlen als WARN, nicht als Gate-Bruch
    bl_path = os.path.join(ROOT, '_dev', 'config', 'lint-bestand.txt')
    baseline = set()
    if os.path.exists(bl_path):
        for line in io.open(bl_path, encoding='utf-8'):
            line = line.strip()
            if line and not line.startswith('#'):
                baseline.add(line)
    hard, soft = [], []
    for rel, code, msg in fails:
        if '%s %s' % (code, rel) in baseline:
            soft.append((rel, code, msg))
        else:
            hard.append((rel, code, msg))
    fails = hard
    if not QUIET:
        for rel, code, msg in fails:
            print('FAIL %s  %s  %s' % (code, rel, msg))
        for rel, code, msg in soft:
            print('WARN %s  %s  (Bestand) %s' % (code, rel, msg))
    by = {}
    for _, code, _ in fails:
        by[code] = by.get(code, 0) + 1
    if triages:
        by_page = {}
        for rel, code, msg in triages:
            by_page.setdefault(rel, []).append('%s %s' % (code, msg))
        print('=== TRIAGE (informational, %d Treffer auf %d Seiten) ===' % (len(triages), len(by_page)))
        for rel in sorted(by_page):
            print('  ~ %s' % rel)
            for m in by_page[rel]:
                print('      %s' % m)
    print('--- lint-site: %d Seiten, %d FAILs, %d Bestands-WARNs %s' % (len(pages), len(fails), len(soft),
          ('(' + ', '.join('%s:%d' % kv for kv in sorted(by.items())) + ')') if by else ''))
    sys.exit(1 if fails else 0)

if __name__ == '__main__':
    main()
