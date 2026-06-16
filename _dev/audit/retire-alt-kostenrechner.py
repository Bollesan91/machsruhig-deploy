#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Altes, falsches Duplikat /tools/kostenrechner/ stilllegen:
- 9 Inbound-Links -> /tools/bestattungskosten-rechner/ (korrektes BL-Modell-Tool).
- Sitemap-Eintrag entfernen.
Redirect (_redirects) wird separat ergaenzt. Asserts vor je Write."""
import io, os, re, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OLD = '/tools/kostenrechner'
NEW = '/tools/bestattungskosten-rechner/'

def main():
    files = [f for f in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True)
             if os.sep + '_dev' + os.sep not in f
             and os.sep + 'kostenrechner' + os.sep not in f]  # das alte Tool selbst nicht anfassen
    n = 0
    for f in files:
        t0 = io.open(f, encoding='utf-8').read()
        if OLD not in t0:
            continue
        t = t0.replace('"' + OLD + '/"', '"' + NEW + '"').replace('"' + OLD + '"', '"' + NEW + '"')
        # kein href mehr auf das alte Tool
        assert ('"' + OLD + '"') not in t and ('"' + OLD + '/"') not in t, 'Rest-Link in %s' % f
        if t != t0:
            io.open(f, 'w', encoding='utf-8', newline='').write(t)
            print('REPOINT', os.path.relpath(f, ROOT).replace(os.sep, '/'))
            n += 1
    # Sitemap: alte URL-Zeile entfernen (NEW ist bereits separat gelistet)
    sm = os.path.join(ROOT, 'sitemap.xml')
    s = io.open(sm, encoding='utf-8').read()
    before = s
    # entferne das <url>...kostenrechner/...</url>-Element (ein-/mehrzeilig tolerant)
    s = re.sub(r'\s*<url>(?:(?!</url>).)*?/tools/kostenrechner/(?:(?!</url>).)*?</url>', '', s, flags=re.S)
    if s == before:
        # Fallback: nur die loc-Zeile
        s = re.sub(r'\s*<loc>[^<]*?/tools/kostenrechner/?</loc>', '', s)
    assert '/tools/kostenrechner' not in s, 'Sitemap-Rest'
    if s != before:
        io.open(sm, 'w', encoding='utf-8', newline='').write(s)
        print('SITEMAP bereinigt')
    print('--- %d HTML-Dateien repointed' % n)

if __name__ == '__main__':
    main()
