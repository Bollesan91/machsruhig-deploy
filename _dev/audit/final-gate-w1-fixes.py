#!/usr/bin/env python3
# FINAL-RELEASE-GATE Welle 1 — Fixes (4 Bullets + Bielefeld-Standalone), je primaerverifiziert.
import os
ROOT = r"C:\Users\Bolle\AppData\Local\Temp\machsruhig-deploy"

EDITS = [
    ("friedhoefe/muenchen/index.html",
     "auf dem Westfriedhof wurde 1955 das erste islamische Grabfeld Deutschlands angelegt; weitere muslimische Grabfelder bestehen auf dem Waldfriedhof und dem Neuen Südfriedhof.",
     "in München bestehen islamische Grabfelder seit 1955 — eines der frühesten in Deutschland: das erste entstand auf dem Waldfriedhof, weitere große Grabfelder folgten auf dem Westfriedhof und dem Neuen Südfriedhof. Gräber Richtung Mekka."),
    ("friedhoefe/duesseldorf/index.html",
     "muslimische Bestattungen sind in Düsseldorf seit 1963 möglich; das nach Mekka ausgerichtete muslimische Grabfeld liegt heute auf dem Friedhof Itter.",
     "muslimische Bestattungen sind in Düsseldorf seit 1963 möglich (zunächst auf dem Südfriedhof); das heute aktive, nach Mekka ausgerichtete muslimische Grabfeld liegt auf dem Friedhof Itter."),
    ("friedhoefe/braunschweig/index.html",
     "sarglose Bestattung im Leichentuch ist dort seit 2008 m&ouml;glich.",
     "sarglose Bestattung im Leichentuch ist dort seit 2006 m&ouml;glich."),
    ("friedhoefe/duisburg/index.html",
     "seit den 1990er-Jahren ein islamisches Grabfeld; 2021 wurde ein weiteres er&ouml;ffnet &mdash; Gr&auml;ber Richtung Mekka, Bestattung in reiner Erde.",
     "seit den 1990er-Jahren ein islamisches Grabfeld &mdash; Gr&auml;ber Richtung Mekka, Bestattung in reiner Erde."),
    ("friedhoefe/bielefeld/alter-friedhof/index.html",
     "<li><b>Status</b>Gartendenkmal, seit 2000 wieder für Bestattungen geöffnet</li>",
     "<li><b>Status</b>denkmalgeschützte Grünanlage, seit 2000 wieder für Bestattungen geöffnet</li>"),
    ("friedhoefe/bielefeld/alter-friedhof/index.html",
     "diente er vor allem als parkartige Grünanlage und Gartendenkmal.",
     "diente er vor allem als parkartige Grünanlage."),
    ("friedhoefe/bielefeld/alter-friedhof/index.html",
     "Seit dem Jahr <strong>2000</strong> wird der Alte Friedhof von der Stadt wieder als Bestattungsfriedhof betrieben.",
     "Seit dem Jahr <strong>2000</strong> wird der Alte Friedhof von der städtischen Friedhofs GmbH Bielefeld (Stadt und Bestatter) wieder als Bestattungsfriedhof betrieben."),
]

staged = []
for rel, old, new in EDITS:
    p = os.path.join(ROOT, rel)
    s = open(p, encoding="utf-8").read()
    assert s.count(old) == 1, f"{rel}: expected 1, got {s.count(old)} :: {old[:60]!r}"
    staged.append((p, old, new, rel))

for p, old, new, rel in staged:
    s = open(p, encoding="utf-8").read()
    open(p, "w", encoding="utf-8").write(s.replace(old, new, 1))
    print("OK", rel)
print(f"{len(staged)} edits applied.")
