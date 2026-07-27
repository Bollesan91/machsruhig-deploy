#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix-authorship.py — Audit-Fix #1/#2/#17/#26: institutionelle Byline -> Namensautor
+ ehrliches Status-Label + Entfernung falscher Fachpool-/Review-Behauptungen.
LIVE-Seiten (ohne _dev/). JSON-LD via echtem Parse+Walk (robust ggü. Struktur-Varianten:
inline-Autor, @id-Referenz auf #redaktion-Entitaet, description-Feld, Fachpool-Reviewer-Knoten).
Asserts VOR dem einzigen Write je Datei. Aufruf: python _dev/audit/fix-authorship.py [--apply]
"""
import os, re, glob, json, copy, sys

APPLY = "--apply" in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NAME = "Marie-Therese Bollweg"
UEBER = "https://machsruhig.de/ueber-uns"
STATUS_TXT = "redaktionell recherchiert, nicht extern fachlich geprüft"

LDJSON_RE = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)

def conv_person(d):
    new = {}
    if "@id" in d: new["@id"] = d["@id"]
    new["@type"] = "Person"; new["name"] = NAME; new["url"] = UEBER
    return new

def walk(o):
    if isinstance(o, list):
        r = []
        for x in o:
            y = walk(x)
            if y is not None: r.append(y)
        return r
    if isinstance(o, dict):
        o.pop("reviewedBy", None)
        nm = o.get("name")
        if isinstance(nm, str) and "Fachpool" in nm:
            return None                      # Reviewer-Knoten ganz raus
        if isinstance(nm, str) and "Redakt" in nm:
            return conv_person(o)            # Redaktions-/Autor-Org -> Person
        for k in list(o.keys()):
            v = walk(o[k])
            if v is None: o.pop(k, None)
            else: o[k] = v
        return o
    return o

def fix_ldjson(s):
    def repl(m):
        try:
            data = json.loads(m.group(2))
        except Exception:
            return m.group(0)                 # unparsebar -> unberuehrt (Assert faengt es spaeter)
        new = walk(copy.deepcopy(data))
        if new == data:
            return m.group(0)
        return m.group(1) + "\n" + json.dumps(new, ensure_ascii=False, indent=2) + "\n" + m.group(3)
    return LDJSON_RE.sub(repl, s)

# --- sichtbare Bylines ---
PROSE = [   # Prosa/„von der …" zuerst, sonst entsteht „Von der Redaktion: …"
    ('Von der <strong>machsruhig Redaktion</strong>', 'Von <strong>%s</strong>' % NAME),
    ('von der <strong>machsruhig Redaktion</strong>', 'von <strong>%s</strong>' % NAME),
]
BYLINES = ['<strong>machsruhig Redaktion</strong>', '<strong>Redaktion machsruhig.de</strong>']
BYLINE_NEW = '<strong>Redaktion: %s</strong>' % NAME
SEP = '<span class="mr-meta-sep" aria-hidden="true"> · </span>'
ANCHOR = BYLINE_NEW + SEP
STATUS_SPAN = '<span class="mr-review-status">%s</span>%s' % (STATUS_TXT, SEP)
PLAIN_ANCHOR = BYLINE_NEW + ' · '            # meta-line / <p class="byline">
PLAIN_STATUS = BYLINE_NEW + ' · ' + STATUS_TXT + ' · '

FORBIDDEN = ['Fachpool-Reviewer', 'Bestattungsfachpool',
             'Fachliche Prüfung:</strong> Fachpool', 'Fachliche Erstellung: machsruhig',
             'Fachliche Reviewer: Bestattungsfachpool']

def bespoke(rel, s):
    n = 0
    if rel == 'bestatter/darmstadt/index.html':
        o = 'Fachliche Erstellung: machsruhig Redaktion mit Fachpool-Reviewer Bestattungsrecht'
        n += s.count(o); s = s.replace(o, 'Redaktion: %s · %s' % (NAME, STATUS_TXT))
    if rel == 'bestatter/kiel/index.html':
        o1 = '<span><strong>Autor:</strong> machsruhig Redaktion</span>'
        n += s.count(o1); s = s.replace(o1, '<span><strong>Autor:</strong> %s</span>' % NAME)
        o2 = '<span><strong>Fachliche Prüfung:</strong> Fachpool-Reviewer</span>'
        n += s.count(o2); s = s.replace(o2, '<span><strong>Status:</strong> nicht extern fachlich geprüft</span>')
    if rel == 'bestatter/regensburg/index.html':
        o1 = '<a href="/">Redaktion & Fachpool</a>'
        n += s.count(o1); s = s.replace(o1, '<a href="/ueber-uns">Über uns</a>')
        o2 = 'Erstellt von der machsruhig Redaktion. Fachliche Reviewer: Bestattungsfachpool. Quellenstand: Mai 2026.'
        n += s.count(o2); s = s.replace(o2, 'Erstellt von %s. Redaktionell recherchiert, nicht extern fachlich geprüft. Quellenstand: Mai 2026.' % NAME)
    return s, n

files = [p for p in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)
         if (os.sep + "_dev" + os.sep) not in p]
done, errs = [], []
for p in sorted(files):
    rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
    src = open(p, encoding="utf-8").read()
    s = fix_ldjson(src)
    for o, nw in PROSE: s = s.replace(o, nw)
    for inst in ('machsruhig Redaktion', 'Redaktion machsruhig.de'):   # meta-author + Recherche-Byline (Legacy)
        s = s.replace('<meta name="author" content="%s"' % inst, '<meta name="author" content="%s"' % NAME)
        s = s.replace('Recherche: %s' % inst, 'Recherche: %s' % NAME)
    # Klartext-Byline in <p class="meta"> (kein <strong>): Ratgeber-Legacy
    for inst in ('Redaktion machsruhig.de', 'machsruhig Redaktion'):
        s = s.replace('<p class="meta">%s · ' % inst,
                      '<p class="meta">Redaktion: %s · %s · ' % (NAME, STATUS_TXT))
    nb = 0
    for b in BYLINES: nb += s.count(b); s = s.replace(b, BYLINE_NEW)
    st = 0
    if ANCHOR in s and STATUS_SPAN not in s:
        s = s.replace(ANCHOR, ANCHOR + STATUS_SPAN, 1); st = 1
    elif PLAIN_ANCHOR in s and STATUS_TXT not in s:
        s = s.replace(PLAIN_ANCHOR, PLAIN_STATUS, 1); st = 1
    s, nbsp = bespoke(rel, s)
    if s == src:
        continue
    # --- Asserts VOR Write ---
    err = None
    for m in LDJSON_RE.finditer(s):
        try: json.loads(m.group(2))
        except Exception as e: err = "JSON-LD kaputt: %s" % e; break
    if not err:
        for m in LDJSON_RE.finditer(s):
            if re.search(r'"name"\s*:\s*"[^"]*Redakt[^"]*"', m.group(2)):
                err = "Autor-Restname mit 'Redakt' im JSON-LD"; break
    if not err:
        for bad in FORBIDDEN:
            if bad in s: err = "verbotener Rest-String: %s" % bad; break
    if not err and '"reviewedBy"' in s: err = "reviewedBy nicht entfernt"
    if not err and 'machsruhig Redaktion' in s: err = "Rest 'machsruhig Redaktion' sichtbar/roh"
    if not err and 'Redaktion machsruhig.de' in s: err = "Rest 'Redaktion machsruhig.de' sichtbar/roh"
    if err:
        errs.append("%s -> %s" % (rel, err)); continue
    done.append((rel, nb, st, nbsp))
    if APPLY:
        open(p, "w", encoding="utf-8").write(s)

print("=== %s === geaendert %d | Fehler %d" % ("APPLY" if APPLY else "DRY", len(done), len(errs)))
print("byline-Renames gesamt: %d | Status-Labels: %d | bespoke: %d"
      % (sum(d[1] for d in done), sum(d[2] for d in done), sum(d[3] for d in done)))
no_status = [d[0] for d in done if d[1] and not d[2]]
if no_status:
    print("Byline aber KEIN Status-Label (%d): %s" % (len(no_status), ", ".join(no_status)))
if errs:
    print("--- FEHLER ---")
    for e in errs: print("  ", e)
