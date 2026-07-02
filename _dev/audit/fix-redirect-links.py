#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Interne Links, die ueber _redirects-301 laufen, direkt aufs Ziel ziehen.
# Nur exakte href-Matches einfacher Regeln (keine Splats, keine %-encodierten).
# DRY default; --apply schreibt. Asserts: Ziel existiert lokal, kein Selbst-Link.
import os, re, sys, glob
DRY = "--apply" not in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# _redirects parsen
rules = {}
for ln in open(os.path.join(ROOT, "_redirects"), encoding="utf-8"):
    ln = ln.strip()
    if not ln or ln.startswith("#"): continue
    parts = ln.split()
    if len(parts) < 3: continue
    src, dst, code = parts[0], parts[1], parts[2]
    if "*" in src or "%" in src or ":" in src: continue
    if not code.startswith("301"): continue
    rules[src] = dst

def target_exists(dst):
    p = dst.strip("/")
    if p == "": return True
    for cand in (p + "/index.html", p + ".html"):
        if os.path.isfile(os.path.join(ROOT, cand.replace("/", os.sep))): return True
    return False

# Zielketten aufloesen (dst selbst redirectet?) max 3 Hops
def resolve(d, depth=0):
    if depth > 3: return d
    if d in rules: return resolve(rules[d], depth+1)
    if d.rstrip("/") in rules: return resolve(rules[d.rstrip("/")], depth+1)
    return d

changed = {}
skipped_missing = set()
files = [f for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)
         if os.sep+"_dev"+os.sep not in f and os.sep+"templates"+os.sep not in f]
for f in files:
    html = open(f, encoding="utf-8").read()
    orig = html
    for src, dst in rules.items():
        final = resolve(dst)
        if not target_exists(final):
            skipped_missing.add(f"{src} -> {final}"); continue
        if src == final: continue
        html = html.replace(f'href="{src}"', f'href="{final}"')
    if html != orig:
        n = sum(1 for a, b in zip([orig], [html]))  # count files
        changed[os.path.relpath(f, ROOT)] = len(re.findall(r'href="', orig)) - 0
        if not DRY: open(f, "w", encoding="utf-8").write(html)

print(f"=== {'DRY-RUN' if DRY else 'APPLY'} === Regeln: {len(rules)} | Dateien geaendert: {len(changed)}")
for k in sorted(changed): print("  ", k)
if skipped_missing:
    print("-- Redirect-Ziele ohne lokale Datei (NICHT ersetzt):")
    for s in sorted(skipped_missing)[:10]: print("   ?", s)
