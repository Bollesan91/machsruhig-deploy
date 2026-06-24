#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix-friedhof-quotes.py — Lektion #3b: deutsche Anfuehrungszeichen-Paritaet.
Ersetzt das schliessende ASCII-" (U+0022) durch das deutsche " (U+201C) NUR dort,
wo es ein oeffnendes „ (U+201E) schliesst. HTML-Attribut-Quotes (class="…",
href="…") bleiben unberuehrt, weil die Textklasse < > " „ ausschliesst und damit
nie ueber ein Tag hinweg matcht.

Asserts vor jedem Write: „-Anzahl konstant, ASCII-" sinkt exakt um N, U+201C steigt
um N, JSON-LD bleibt parsebar. Ein Write pro Datei.
"""
import io, os, re, sys, json, glob

OPEN, CLOSE, ASCII = '„', '“', '"'          # „  "  "
PAT = re.compile(OPEN + '([^' + OPEN + CLOSE + ASCII + ']*?)' + ASCII)
# Segmentiert HTML in Tags / <script> / <style> (= unantastbar) vs. sichtbaren Text.
SEG = re.compile(r'(<script\b.*?</script>|<style\b.*?</style>|<[^>]*>)', re.S | re.I)
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))


def jsonld_ok(html):
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        json.loads(m.group(1))
    return True


def replace_text_only(src):
    """Ersetzt „…" -> „…" NUR in sichtbaren Text-Knoten. Tags (Attribute!) und
    script/style-Bloecke bleiben unberuehrt — so kann kein Attribut-Quote (class="…",
    content="…", aria-label="…") zerstoert werden, selbst wenn ein „ im Attribut steht."""
    out, n = [], 0
    for i, seg in enumerate(SEG.split(src)):
        if i % 2 == 1:                       # ungerade = Tag / script / style -> unangetastet
            out.append(seg)
        else:
            seg, k = PAT.subn(OPEN + r'\1' + CLOSE, seg)
            n += k
            out.append(seg)
    return ''.join(out), n


def fix_file(fp):
    src = io.open(fp, encoding='utf-8').read()
    new, n = replace_text_only(src)
    if n == 0:
        return 0
    # Asserts
    assert new.count(OPEN) == src.count(OPEN), 'oeffnende „ veraendert'
    assert new.count(ASCII) == src.count(ASCII) - n, 'ASCII-\" nicht exakt um %d gesunken' % n
    assert new.count(CLOSE) == src.count(CLOSE) + n, 'U+201C nicht exakt um %d gestiegen' % n
    jsonld_ok(new)  # wirft bei kaputtem JSON-LD
    io.open(fp, 'w', encoding='utf-8').write(new)
    return n


def main():
    total, files = 0, 0
    for fp in sorted(glob.glob(os.path.join(ROOT, 'friedhoefe', '**', '*.html'), recursive=True)):
        n = fix_file(fp)
        if n:
            files += 1
            total += n
            print('  fixed %2d  %s' % (n, os.path.relpath(fp, ROOT).replace('\\', '/')))
    print('fix-friedhof-quotes: %d Schliessquotes in %d Dateien korrigiert' % (total, files))


if __name__ == '__main__':
    main()
