# -*- coding: utf-8 -*-
"""P2-3 Brand-Normalisierung (Bolle-Entscheid 18.06.):
Wortmarke = "mach's ruhig" (straight apostrophe), Footer-(C) = "(C) 2026".
Nur drei Flaechen, je anker-gebunden:
  1) <title> Marken-Suffix   2) og:site_name content   3) Footer-(C)-Praefix
NICHT angefasst: Logo (schon kanonisch), href/canonical/og:url-Domains,
Taglines (Bolle hat nur Wortmarke+Jahr entschieden).
Alle Asserts VOR dem einzigen Write (Bolle-Regel)."""
import os, re

CANON = "mach's ruhig"  # straight apostrophe U+0027

TITLE_RE  = re.compile(r"(machsruhig\.de|machsruhig|machs ruhig)(\s*</title>)")
OG_RE     = re.compile(r"(og:site_name\"\s+content=\")(machsruhig\.de|machsruhig|machs ruhig)(\")")
# Footer (C): optionales Jahr/Jahresspanne + Marken-Token (inkl. schon-kanonisch -> no-op)
FOOTER_RE = re.compile(r"©\s*(?:20\d\d(?:[–—\-]20\d\d)?)?\s*(?:machsruhig\.de|machsruhig|machs ruhig|mach's ruhig)")

def transform(s):
    s = TITLE_RE.sub(lambda m: CANON + m.group(2), s)
    s = OG_RE.sub(lambda m: m.group(1) + CANON + m.group(3), s)
    s = FOOTER_RE.sub("© 2026 " + CANON, s)
    return s

changes = []   # (path, new_content)
n_title = n_og = n_foot = 0
for root, _, fs in os.walk('.'):
    if os.sep + '_dev' in os.sep + root or '.git' in root or 'node_modules' in root:
        continue
    for f in fs:
        if not f.endswith('.html'):
            continue
        p = os.path.join(root, f)
        s = open(p, encoding='utf-8').read()
        new = transform(s)
        if new == s:
            continue
        # --- ASSERTS pro Datei, VOR jedem Write ---
        # (a) Domain in href/canonical/og:url unberuehrt
        assert s.count("https://machsruhig.de") == new.count("https://machsruhig.de"), "DOMAIN-LINK gefaehrdet: " + p
        # (b) keine Domain-Korruption
        assert "mach's ruhig.de" not in new, "KORRUPTION mach's ruhig.de: " + p
        assert "mach'sruhig" not in new, "KORRUPTION mach'sruhig: " + p
        # (c) Logo bleibt kanonisch (Anzahl unveraendert)
        assert s.count("mach's <span>ruhig</span>") == new.count("mach's <span>ruhig</span>"), "LOGO veraendert: " + p
        n_title += len(TITLE_RE.findall(s))
        n_og    += len(OG_RE.findall(s))
        n_foot  += len(FOOTER_RE.findall(s)) - new.count("© 2026 " + CANON + " ") * 0  # info only
        changes.append((p, new))

print("Dateien mit Aenderung:", len(changes))
print("title-Treffer:", n_title, " og-Treffer:", n_og)
for p, new in changes:
    open(p, 'w', encoding='utf-8').write(new)
print("geschrieben.")
