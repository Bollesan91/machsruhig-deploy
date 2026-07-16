#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update-sitemap-lastmod.py - setzt <lastmod> je Sitemap-URL auf das tatsaechliche
letzte Git-Commit-Datum der zugehoerigen Datei, aber NUR wenn Git neuer ist als
der aktuelle Eintrag (ehrlicher Recrawl-Nudge, kein lastmod-Gaming).
Quelle der Aenderungsdaten: git log seit --since (Default 2026-06-17).
Idempotent. Aufruf: python _dev/scripts/update-sitemap-lastmod.py [--since YYYY-MM-DD] [--apply]
"""
import os, re, sys, subprocess, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SM = os.path.join(ROOT, "sitemap.xml")
BASE = "https://machsruhig.de"

ap = argparse.ArgumentParser()
ap.add_argument("--since", default=None,
                help="YYYY-MM-DD; Default = Datum des letzten sitemap.xml-Commits (wartungsfrei)")
ap.add_argument("--apply", action="store_true")
ap.add_argument("--commit", action="store_true",
                help="nach --apply sitemap.xml auto-committen (Deploy-Ritual, ein Befehl)")
args = ap.parse_args()

# --since wartungsfrei ableiten: alle Seiten-Aenderungen SEIT dem letzten Sitemap-Sync
if args.since is None:
    r = subprocess.run(["git", "log", "-1", "--format=%cs", "--", "sitemap.xml"],
                       cwd=ROOT, capture_output=True, text=True).stdout.strip()
    args.since = r if re.match(r"^\d{4}-\d{2}-\d{2}$", r or "") else "2026-06-17"
    print(f"[since auto] letzter sitemap.xml-Commit: {args.since}")

# 1. file -> letztes Commit-Datum (reverse-chron => erster Treffer = neuestes)
# git parst nackte Daten als "heute + JETZIGE Uhrzeit" -> explizit Mitternacht, sonst faellt der Commit-Tag selbst raus
out = subprocess.run(["git", "log", f"--since={args.since} 00:00:00", "--format=%cs", "--name-only"],
                     cwd=ROOT, capture_output=True, text=True).stdout
date_re = re.compile(r"^\d{4}-\d{2}-\d{2}$")
fdate, cur = {}, None
for line in out.splitlines():
    line = line.strip()
    if not line:
        continue
    if date_re.match(line):
        cur = line
    elif cur and line not in fdate:
        fdate[line] = cur

def loc_to_file(loc):
    p = loc.replace(BASE, "").strip("/")
    if p == "":
        return "index.html"
    cands = ([p + "/index.html", p + ".html"] if loc.endswith("/")
             else [p + ".html", p + "/index.html"])
    for c in cands:
        if os.path.isfile(os.path.join(ROOT, c.replace("/", os.sep))):
            return c
    return None

xml = open(SM, encoding="utf-8").read()
upd, missing = [], []

def repl(m):
    block = m.group(0)
    loc = re.search(r"<loc>([^<]+)</loc>", block).group(1)
    lm = re.search(r"<lastmod>([^<]+)</lastmod>", block)
    f = loc_to_file(loc)
    if not f:
        missing.append(loc); return block
    gd = fdate.get(f.replace(os.sep, "/"))
    if gd and lm and gd > lm.group(1):
        upd.append((loc, lm.group(1), gd))
        return block.replace(f"<lastmod>{lm.group(1)}</lastmod>", f"<lastmod>{gd}</lastmod>")
    return block

xml2 = re.sub(r"<url>.*?</url>", repl, xml, flags=re.S)
print(f"{'APPLY' if args.apply else 'DRY-RUN'} | {len(upd)} lastmod aktualisiert | {len(missing)} loc ohne Datei")
for loc, a, b in upd:
    print(f"  {a} -> {b}  {loc}")
if missing:
    print("  -- loc ohne lokale Datei (uebersprungen):")
    for x in missing[:15]:
        print("     ?", x)
if args.apply and upd:
    open(SM, "w", encoding="utf-8").write(xml2)
    print("geschrieben.")
    if args.commit:
        subprocess.run(["git", "add", "sitemap.xml"], cwd=ROOT, check=True)
        msg = f"Sitemap: lastmod-Recrawl-Nudge ({len(upd)} Seiten auf echtes Commit-Datum) [skip netlify]"
        subprocess.run(["git", "-c", "user.name=Bollesan91", "-c", "user.email=cbollweg@gmx.de",
                        "commit", "--no-verify", "-m", msg], cwd=ROOT, check=True)
        print(f"committet: {msg}")
elif args.commit:
    print("nichts zu committen (keine lastmod-Aenderung).")
