#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lint-friedhof.py — Friedl Stufe 1 (deterministische Gates) fuer Friedhofseiten.
Schwester zu lint-site.py; deckt die FRIEDL-Challenge-Dimensionen ab, die
maschinell entscheidbar sind. 0 FAIL ist Pflicht vor jedem Review und Deploy.
"Was der Linter faengt, ist kein Reviewer-Thema." (FRIEDL Stufe 1)

Geltungsbereich: alle Seiten unter friedhoefe/**.html
  Standalone = JSON-LD @type "Cemetery"   ·   Hub = "CollectionPage".

Checks (v1):
  F1  Arithmetik-Cross-Check: jede .fh-calc-Beispielsumme = Summe ihrer Posten
      (inkl. Multiplikation  betrag x jahre = ergebnis)            [Recht/Konsistenz]
  F2  Provenienz sichtbar: Gebuehren-Tabelle (€) ohne "gueltig ab" + Quelle  [Recht]
  F3  ASCII-" als typografisches Anfuehrungszeichen (sichtbar + JSON-LD-Wert);
      deutsche „ " (U+201E/U+201C) Pflicht — Paritaets-Falle (Lektion 3b)  [Konsistenz]
  F4  Standalone-Breadcrumb zeigt auf nicht existierenden Hub (Lektion 3a)  [Konsistenz]
  F5  Substanz-Gate: Standalone < 3 Gebuehrenzeilen UND < 5 Steckbrief-Fakten [Tiefe]
  F6  Aktualitaet: "geprueft am TT.MM.JJJJ" fehlt; > 18 Mon = FAIL; gueltig-ab sichtbar [Aktualitaet]
  F7  Bewertung/Siegel-Optik (Anti-Pattern 7 — wir geben Gebuehren wieder, bewerten nicht)
  F8  Indexierte Friedhofseite fehlt in sitemap.xml
  F9  Record-Cross-Check: Tarifstelle (NNNN) auf der Seite ≠ Betrag im Traeger-Record [Recht]
WARN:
  W1  Aktualitaet 12–18 Mon ohne Re-Pruefung
  W2  Standalone mit Gebuehren, aber kein Traeger-Record verknuepft
  W3  Near-Duplicate: 3-Shingle-Jaccard ≥ 0.80 zu einer Schwesterseite (Tiefe)

OFFEN (bewusst NICHT im Linter, FRIEDL "vor Vollserie loesen"):
  robuste Change-Detection je Traeger-Satzung (PDF-Hash bruechig) — bis dahin Q1-Sweep.

Aufruf: python _dev/scripts/lint-friedhof.py [--quiet]
Exit-Code 0 = gruen, 1 = FAILs vorhanden.
"""
import io, os, re, sys, json, html as _html, glob
from datetime import date

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
FRIEDHOF_DIR = os.path.join(ROOT, 'friedhoefe')
RECORD_GLOB = os.path.join(ROOT, '_dev', 'strategie', 'friedhoefe', '*-record.json')
QUIET = '--quiet' in sys.argv
TODAY = date.today()

# Wertungs-/Siegel-Phrasen (F7). Bewusst eng: "geprueft am" (Stand-Stempel) bleibt erlaubt.
RATING_PHRASES = [
    'bester friedhof', 'schönster friedhof', 'schoenster friedhof', 'testsieger',
    'gütesiegel', 'guetesiegel', 'zertifizierter friedhof', 'empfehlenswerter friedhof',
    'wir empfehlen diesen friedhof', 'top-friedhof', 'unser favorit',
]


def visible_text(html):
    t = re.sub(r'<script\b.*?</script>', ' ', html, flags=re.S | re.I)
    t = re.sub(r'<style\b.*?</style>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    return t


def norm_spaces(s):
    return re.sub(r'[\s ]+', ' ', _html.unescape(s)).strip()


def parse_eur(s):
    """'1.625', '2.828 €', '74' -> int. None wenn keine Zahl."""
    m = re.search(r'\d[\d.]*', s)
    if not m:
        return None
    return int(m.group(0).replace('.', ''))


def ld_string_values(node, out):
    """Sammelt rekursiv alle String-Werte aus einem JSON-LD-Knoten."""
    if isinstance(node, dict):
        for v in node.values():
            ld_string_values(v, out)
    elif isinstance(node, list):
        for v in node:
            ld_string_values(v, out)
    elif isinstance(node, str):
        out.append(node)


def load_records():
    """Traeger-Records: filename -> {data, tarif: {tarifstelle: betrag}}."""
    recs = []
    for fp in glob.glob(RECORD_GLOB):
        try:
            data = json.loads(io.open(fp, encoding='utf-8').read())
        except Exception:
            continue
        tarif = {}
        for g in data.get('gebuehren', []):
            ts, betrag = str(g.get('tarifstelle', '')).strip(), g.get('betrag')
            if ts and isinstance(betrag, (int, float)):
                tarif[ts] = int(betrag)
        recs.append({'file': os.path.basename(fp), 'data': data, 'tarif': tarif})
    return recs


def match_record(stadt, slug, recs):
    """Record fuer eine Friedhofseite: Dateiname '<stadt>-...' und slug in deckt_friedhoefe."""
    cand = []
    for r in recs:
        if not r['file'].startswith(stadt + '-'):
            continue
        deckt = r['data'].get('deckt_friedhoefe') or []
        if not slug or not deckt or slug in deckt:
            cand.append(r)
    return cand[0] if len(cand) == 1 else None


def shingles(text, k=3):
    toks = re.findall(r'\w+', text.lower())
    return set(tuple(toks[i:i + k]) for i in range(max(0, len(toks) - k + 1)))


def collect_pages():
    pages = []
    if not os.path.isdir(FRIEDHOF_DIR):
        return pages
    for dirpath, dirnames, filenames in os.walk(FRIEDHOF_DIR):
        for fn in filenames:
            if fn.endswith('.html'):
                pages.append(os.path.join(dirpath, fn))
    pages.sort()
    return pages


def main():
    recs = load_records()
    pages = collect_pages()
    sitemap = ''
    sp = os.path.join(ROOT, 'sitemap.xml')
    if os.path.exists(sp):
        sitemap = io.open(sp, encoding='utf-8', errors='replace').read()

    fails, warns = [], []
    standalone_shingles = {}  # rel -> shingles (fuer W3)

    for fp in pages:
        rel = os.path.relpath(fp, ROOT).replace('\\', '/')
        html = io.open(fp, encoding='utf-8', errors='replace').read()
        vis = visible_text(html)
        vis_n = norm_spaces(vis)

        # --- JSON-LD parsen + Seitentyp bestimmen ---
        ld_nodes, ld_values = [], []
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                data = json.loads(m.group(1))
            except Exception:
                continue  # Parsebarkeit deckt lint-site L2 ab
            nodes = data.get('@graph', [data]) if isinstance(data, dict) else data
            if isinstance(nodes, dict):
                nodes = [nodes]
            ld_nodes.extend(n for n in nodes if isinstance(n, dict))
        for n in ld_nodes:
            ld_string_values(n, ld_values)
        types = {n.get('@type') for n in ld_nodes}
        is_standalone = 'Cemetery' in types

        # --- Pfad-Teile (stadt/slug) ---
        parts = rel.split('/')  # friedhoefe/<stadt>/<slug>/index.html
        stadt = parts[1] if len(parts) > 1 else ''
        slug = parts[2] if len(parts) > 3 and parts[2] != 'index.html' else ''

        # ---- F3 ASCII-Anfuehrungszeichen (sichtbar + JSON-LD-Werte) ----
        if '"' in vis_n:
            snippet = vis_n[max(0, vis_n.find('"') - 25): vis_n.find('"') + 25]
            fails.append((rel, 'F3', 'ASCII-" im sichtbaren Text (deutsche „ " nutzen): …%s…' % snippet.strip()))
        for val in ld_values:
            if '"' in val:
                fails.append((rel, 'F3', 'ASCII-" in JSON-LD-Wert: "%s…"' % val[:40]))
                break

        # ---- F7 Bewertung/Siegel ----
        low = vis_n.lower()
        for ph in RATING_PHRASES:
            if ph in low:
                fails.append((rel, 'F7', 'Wertungs-/Siegel-Phrase: "%s"' % ph))

        # ---- F6 Aktualitaet ----
        has_fees = bool(re.search(r'class="fh-table"', html)) or '€' in vis_n
        m_pruef = re.search(r'gepr[üu]ft am (\d{2})\.(\d{2})\.(\d{4})', vis_n)
        if has_fees:
            if not m_pruef:
                fails.append((rel, 'F6', '"geprüft am TT.MM.JJJJ" fehlt auf Gebuehren-Seite'))
            else:
                d = date(int(m_pruef.group(3)), int(m_pruef.group(2)), int(m_pruef.group(1)))
                months = (TODAY.year - d.year) * 12 + (TODAY.month - d.month)
                if months > 18:
                    fails.append((rel, 'F6', 'Pruefstand %s älter als 18 Monate (Verfall)' % d.isoformat()))
                elif months > 12:
                    warns.append((rel, 'W1', 'Pruefstand %s 12–18 Monate alt — Re-Verifikation faellig' % d.isoformat()))
            if not re.search(r'g[üu]ltig ab \d{2}\.\d{2}\.\d{4}', vis_n):
                fails.append((rel, 'F6', 'Gebuehren ohne sichtbares "gültig ab TT.MM.JJJJ"'))

        # ---- F2 Provenienz sichtbar ----
        if 'class="fh-table"' in html and '€' in vis_n:
            has_validfrom = bool(re.search(r'g[üu]ltig ab', vis_n))
            has_source = bool(re.search(r'Geb[üu]hrenordnung|Geb[üu]hren[üu]bersicht|Satzung', vis_n))
            if not (has_validfrom and has_source):
                fails.append((rel, 'F2', 'Gebuehren-Tabelle ohne Provenienz (gültig-ab + Gebührenordnung/Satzung sichtbar)'))

        # ---- F1 Arithmetik der .fh-calc-Boxen ----
        for box in re.finditer(r'<div class="fh-calc">(.*?)</div>', html, re.S):
            inner = box.group(1)
            sum_m = re.search(r'<span class="sum">(.*?)</span>', inner, re.S)
            if not sum_m:
                continue
            soll = parse_eur(norm_spaces(visible_text(sum_m.group(1))))
            body = inner[:sum_m.start()]
            posten = []
            for line in re.split(r'<br\s*/?>', body):
                txt = norm_spaces(visible_text(line))
                if '=' not in txt:
                    continue
                # optionaler Multiplikations-Check: base x faktor = ergebnis
                mul = re.search(r'(\d[\d.]*)\s*€?\s*/?\s*\w*\s*[×x]\s*(\d+)\s*=\s*(\d[\d.]*)', txt)
                rhs = parse_eur(txt.rsplit('=', 1)[1])
                if mul:
                    base, fak, erg = parse_eur(mul.group(1)), int(mul.group(2)), parse_eur(mul.group(3))
                    if base is not None and erg is not None and base * fak != erg:
                        fails.append((rel, 'F1', 'Multiplikation falsch: %d × %d ≠ %d' % (base, fak, erg)))
                if rhs is not None:
                    posten.append(rhs)
            if soll is not None and posten and sum(posten) != soll:
                fails.append((rel, 'F1', 'Beispielsumme stimmt nicht: Σ%s = %d ≠ ausgewiesen %d'
                              % (posten, sum(posten), soll)))

        # ===== nur Standalone-Friedhofseiten =====
        if is_standalone:
            # F4 Breadcrumb-Hub existiert
            for href in re.findall(r'<nav class="mr-breadcrumb"[^>]*>(.*?)</nav>', html, re.S):
                for h in re.findall(r'href="(/friedhoefe/[^"]*)"', href):
                    p = h.split('#')[0].split('?')[0].lstrip('/').rstrip('/')
                    if not os.path.isfile(os.path.join(ROOT, p, 'index.html')):
                        fails.append((rel, 'F4', 'Breadcrumb zeigt auf fehlenden Hub: %s' % h))

            # F5 Substanz-Gate
            fee_rows = len(re.findall(r'<tbody>(.*?)</tbody>', html, re.S)
                           and re.findall(r'<tr>', re.search(r'<tbody>(.*?)</tbody>', html, re.S).group(1)) or [])
            facts = len(re.findall(r'<ul class="fh-facts">(.*?)</ul>', html, re.S)
                        and re.findall(r'<li>', re.search(r'<ul class="fh-facts">(.*?)</ul>', html, re.S).group(1)) or [])
            if fee_rows < 3 and facts < 5:
                fails.append((rel, 'F5', 'Substanz-Gate: nur %d Gebuehrenzeilen + %d Fakten (→ Aggregationszeile)'
                              % (fee_rows, facts)))

            # F8 Sitemap-Praesenz
            mrob = re.search(r'<meta name="robots" content="([^"]*)"', html)
            indexed = not (mrob and 'noindex' in mrob.group(1))
            canon = re.search(r'<link rel="canonical" href="([^"]+)"', html)
            if indexed and canon and canon.group(1) not in sitemap:
                fails.append((rel, 'F8', 'indexierte Seite fehlt in sitemap.xml: %s' % canon.group(1)))

            # F9 Record-Cross-Check (Tarifstelle -> Betrag)
            rec = match_record(stadt, slug, recs)
            tbody = re.search(r'<tbody>(.*?)</tbody>', html, re.S)
            seiten_tarife = []  # (tarifstelle, betrag)
            if tbody:
                for tr in re.findall(r'<tr>(.*?)</tr>', tbody.group(1), re.S):
                    tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)
                    if len(tds) < 2:
                        continue
                    label, amount = norm_spaces(visible_text(tds[0])), norm_spaces(visible_text(tds[-1]))
                    ts = re.findall(r'\((\d{2,4})\)', label)
                    betrag = parse_eur(amount)
                    if ts and betrag is not None:
                        seiten_tarife.append((ts[-1], betrag))
            if seiten_tarife:
                if not rec:
                    warns.append((rel, 'W2', 'Standalone mit Gebuehren, aber kein Traeger-Record verknuepft'))
                else:
                    for ts, betrag in seiten_tarife:
                        if ts in rec['tarif'] and rec['tarif'][ts] != betrag:
                            fails.append((rel, 'F9', 'Tarifstelle %s: Seite %d € ≠ Record %d € (%s)'
                                          % (ts, betrag, rec['tarif'][ts], rec['file'])))
                        elif ts not in rec['tarif']:
                            warns.append((rel, 'W2', 'Tarifstelle %s nicht im Record %s' % (ts, rec['file'])))

            standalone_shingles[rel] = shingles(vis_n)

    # ---- W3 Near-Duplicate (paarweise, ab 2 Standalone-Seiten) ----
    rels = sorted(standalone_shingles)
    for i in range(len(rels)):
        for j in range(i + 1, len(rels)):
            a, b = standalone_shingles[rels[i]], standalone_shingles[rels[j]]
            if not a or not b:
                continue
            jac = len(a & b) / len(a | b)
            if jac >= 0.80:
                warns.append((rels[i], 'W3', 'Near-Duplicate zu %s (3-Shingle-Jaccard %.2f ≥ 0.80)'
                              % (rels[j], jac)))

    if not QUIET:
        for rel, code, msg in fails:
            print('FAIL %s  %s  %s' % (code, rel, msg))
        for rel, code, msg in warns:
            print('WARN %s  %s  %s' % (code, rel, msg))
    by = {}
    for _, code, _ in fails:
        by[code] = by.get(code, 0) + 1
    print('--- lint-friedhof: %d Seiten, %d FAILs, %d WARNs %s' % (
        len(pages), len(fails), len(warns),
        ('(' + ', '.join('%s:%d' % kv for kv in sorted(by.items())) + ')') if by else ''))
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
