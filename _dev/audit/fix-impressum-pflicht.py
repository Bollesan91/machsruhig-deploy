#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# § 5 DDG (Anbieterkennzeichnung): Impressum muss von JEDER Seite leicht erkennbar,
# unmittelbar erreichbar und staendig verfuegbar sein. 40 Live-Seiten hatten keinen
# Impressum-Link (alle 17 Bundesland-Seiten, 21 Bestatter-Staedte, 2 Danke-Seiten).
# 38 haben eine aeltere Footer-Variante ohne "Rechtliches"-Spalte, 2 gar keinen Footer.
# Asserts vor jedem Write.
import io, os, glob, re

LEGAL = ('<p class="mr-footer-legal" style="margin-top:8px"><a href="/impressum">Impressum</a> · '
         '<a href="/datenschutz">Datenschutz</a> · <a href="/methodik">Methodik</a></p>')

COPY = ['<p>&copy; 2024–2026 machsruhig.de — Unabhängige Informationen zu Bestattung und Trauer.</p>',
        '<p>&copy; 2025–2026 machsruhig.de — Unabhängige Informationen zu Bestattung und Trauer.</p>']

MINI_FOOTER = ('<footer class="mr-footer no-print">\n  <div class="mr-footer-inner">\n'
               '    <div class="mr-footer-bottom">\n'
               '      <p>&copy; 2024–2026 machsruhig.de — Unabhängige Informationen zu Bestattung und Trauer.</p>\n'
               '      ' + LEGAL + '\n'
               '    </div>\n  </div>\n</footer>\n')

files = [p for p in glob.glob("**/*.html", recursive=True)
         if not p.startswith("_dev") and not p.startswith("templates")]
fixed_footer, fixed_mini, skipped, errs = [], [], 0, []

for p in sorted(files):
    s = io.open(p, encoding="utf-8").read()
    if 'href="/impressum' in s:
        skipped += 1
        continue
    orig = s
    if '<div class="mr-footer-bottom">' in s:
        hit = [c for c in COPY if c in s]
        if len(hit) != 1:
            errs.append(f"{p}: Copyright-Anker {len(hit)}x"); continue
        c = hit[0]
        if s.count(c) != 1:
            errs.append(f"{p}: Copyright nicht eindeutig"); continue
        s = s.replace(c, c + "\n      " + LEGAL)
        fixed_footer.append(p)
    elif '</body>' in s and '<footer' not in s:
        if s.count('</body>') != 1:
            errs.append(f"{p}: </body> nicht eindeutig"); continue
        s = s.replace('</body>', MINI_FOOTER + '</body>')
        fixed_mini.append(p)
    else:
        errs.append(f"{p}: kein bekanntes Footer-Muster"); continue

    # Asserts vor Write
    if 'href="/impressum"' not in s or 'href="/datenschutz"' not in s:
        errs.append(f"{p}: Links nach Fix nicht vorhanden"); continue
    if s.count('mr-footer-legal') != 1:
        errs.append(f"{p}: Legal-Zeile {s.count('mr-footer-legal')}x"); continue
    if len(s) <= len(orig):
        errs.append(f"{p}: Datei nicht gewachsen"); continue
    io.open(p, "w", encoding="utf-8").write(s)

print(f"Footer-Zeile ergaenzt: {len(fixed_footer)} | Mini-Footer neu: {len(fixed_mini)} | "
      f"hatten schon Impressum: {skipped} | Fehler: {len(errs)}")
for e in errs: print("  ERR", e)
for p in fixed_mini: print("  mini-footer:", p)
