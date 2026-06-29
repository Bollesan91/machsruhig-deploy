#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lint-claims.py - Claim-Register-Gate fuer machsruhig.de.

Drei deterministische Checks, KEIN Netz:
  1. Schema       -> FAIL (blockt): Pflichtfelder, Datumsformat, gueltiger source_type.
  2. Drift        -> WARN: assert_contains-String steht nicht (mehr) auf der Seite
                    (Seite und Register sind auseinandergelaufen).
  3. Ueberfaellig -> WARN: zuletzt_geprueft + interval_months < heute.

Aufruf:
  python _dev/scripts/lint-claims.py
  python _dev/scripts/lint-claims.py --today 2027-08-01   # Datum simulieren (Demo)
  python _dev/scripts/lint-claims.py --page /bestatter/muenchen/

Exit 0, wenn keine Schema-FAILs (Ueberfaellig/Drift = WARN, blockt den Deploy nicht).
Exit 1 bei Schema-FAIL.
"""
import os, sys, json, argparse
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTER = os.path.join(ROOT, "_dev", "claims", "register.json")
ALLOWED_TYPES = {"amtlich", "sekundaer", "erfahrung", "unsicher"}
REQUIRED = ["id", "page", "file", "claim", "value", "source_url", "source_type", "last_checked", "interval_months"]

def parse_date(s):
    y, m, d = (int(x) for x in s.split("-"))
    return date(y, m, d)

def add_months(d0, n):
    m = d0.month - 1 + n
    y = d0.year + m // 12
    m = m % 12 + 1
    # Tag clampen (z.B. 31. -> Monatsende)
    for day in (d0.day, 28, 29, 30, 31):
        try:
            return date(y, m, min(d0.day, day))
        except ValueError:
            continue
    return date(y, m, 28)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--today", help="Datum YYYY-MM-DD simulieren (Demo)")
    ap.add_argument("--page", help="nur Claims dieser page pruefen")
    ap.add_argument("--strict", action="store_true", help="Drift/Ueberfaellig als Fehler werten (exit 1) - fuer CI/Cron")
    args = ap.parse_args()
    today = parse_date(args.today) if args.today else date.today()

    with open(REGISTER, encoding="utf-8") as f:
        data = json.load(f)
    claims = [c for c in data.get("claims", []) if not args.page or c.get("page") == args.page]

    fails, drift, overdue = [], [], []
    rows = []
    seen_ids = set()
    for c in claims:
        cid = c.get("id", "<ohne id>")
        # 1. Schema
        for k in REQUIRED:
            if k not in c or c[k] in (None, ""):
                fails.append(f"{cid}: Pflichtfeld '{k}' fehlt")
        if cid in seen_ids:
            fails.append(f"{cid}: doppelte id")
        seen_ids.add(cid)
        st = c.get("source_type")
        if st and st not in ALLOWED_TYPES:
            fails.append(f"{cid}: source_type '{st}' ungueltig (erlaubt: {sorted(ALLOWED_TYPES)})")
        try:
            lc = parse_date(c["last_checked"])
        except Exception:
            fails.append(f"{cid}: last_checked '{c.get('last_checked')}' kein YYYY-MM-DD")
            continue
        iv = c.get("interval_months", 12)
        nxt = add_months(lc, iv)

        # 2. Drift (assert_contains)
        status_drift = ""
        if c.get("assert_contains"):
            fp = os.path.join(ROOT, c["file"].replace("/", os.sep))
            if not os.path.isfile(fp):
                fails.append(f"{cid}: file '{c['file']}' nicht gefunden")
            else:
                html = open(fp, encoding="utf-8").read()
                if c["assert_contains"] not in html:
                    drift.append(f"{cid}: '{c['assert_contains']}' steht nicht mehr in {c['file']}")
                    status_drift = "DRIFT"

        # 3. Ueberfaellig
        status_age = "ok"
        if nxt < today:
            overdue.append(f"{cid}: faellig seit {nxt.isoformat()} (zuletzt {lc.isoformat()}, alle {iv} Mon.)")
            status_age = "UEBERFAELLIG"
        elif (nxt - today).days <= 30:
            status_age = f"bald ({(nxt-today).days}d)"

        rows.append((cid, st or "?", c["last_checked"], nxt.isoformat(),
                     status_drift or status_age))

    # Ausgabe
    w = max((len(r[0]) for r in rows), default=10)
    print(f"{'ID'.ljust(w)}  {'TYP'.ljust(9)}  {'ZULETZT'.ljust(10)}  {'NAECHSTE'.ljust(10)}  STATUS")
    for r in rows:
        print(f"{r[0].ljust(w)}  {r[1].ljust(9)}  {r[2].ljust(10)}  {r[3].ljust(10)}  {r[4]}")

    print(f"\n--- lint-claims: {len(claims)} Claims (Stichtag {today.isoformat()}) | "
          f"{len(fails)} Schema-FAIL | {len(drift)} Drift-WARN | {len(overdue)} Ueberfaellig-WARN")
    for x in fails:   print("  FAIL  " + x)
    for x in drift:   print("  WARN  Drift: " + x)
    for x in overdue: print("  WARN  Pruefung faellig: " + x)
    hard = bool(fails) or (args.strict and (drift or overdue))
    sys.exit(1 if hard else 0)

if __name__ == "__main__":
    main()
