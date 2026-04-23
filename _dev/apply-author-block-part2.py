#!/usr/bin/env python3
"""
apply-author-block-part2.py — Sprint #4 Teil 2

Rollt den Autoren-Block auf die restlichen YMYL-Seiten aus:
- 16 Bundesländer (bestattung-in/)
- 8 Vorsorge-Seiten mit <p class="meta"> (Standard-Pattern)
- 1 Vorsorge-Seite ohne Meta (Fallback: nach <p class="lead">)

10 Tools werden NICHT angefasst — die brauchen erst Static Shells (Phase A.3).

Baut direkt den sauberen Block ohne Inline-Styles ein UND fügt die
.mr-article-meta-CSS-Regel lokal in den <style>-Block ein.

Dry-Run + Apply.
"""

import re
import sys
from pathlib import Path

# Standard-Pattern: hat <p class="meta"> → ersetzen
STANDARD_TARGETS = [
    # 16 Bundesländer
    "bestattung-in/baden-württemberg/index.html",
    "bestattung-in/bayern/index.html",
    "bestattung-in/berlin/index.html",
    "bestattung-in/brandenburg/index.html",
    "bestattung-in/bremen/index.html",
    "bestattung-in/hamburg/index.html",
    "bestattung-in/hessen/index.html",
    "bestattung-in/mecklenburg-vorpommern/index.html",
    "bestattung-in/niedersachsen/index.html",
    "bestattung-in/nordrhein-westfalen/index.html",
    "bestattung-in/rheinland-pfalz/index.html",
    "bestattung-in/saarland/index.html",
    "bestattung-in/sachsen-anhalt/index.html",
    "bestattung-in/sachsen/index.html",
    "bestattung-in/schleswig-holstein/index.html",
    "bestattung-in/thüringen/index.html",
    # 8 Vorsorge mit meta-Zeile
    "vorsorge/bestattungsvorsorge/index.html",
    "vorsorge/digitaler-nachlass/index.html",
    "vorsorge/index.html",
    "vorsorge/ohne-vorsorge/index.html",
    "vorsorge/patientenverfuegung/index.html",
    "vorsorge/sorgerechtsverfuegung/index.html",
    "vorsorge/sterbegeldversicherung/index.html",
    "vorsorge/testament/index.html",
]

# Fallback-Pattern: keine <p class="meta">, Einbau nach <p class="lead">
FALLBACK_TARGETS = [
    "vorsorge/vorsorge-ordner/index.html",
]


def extract_meta_from_block(block_html):
    """Extrahiert Stand und Lesezeit aus einer <p class="meta">-Zeile."""
    text = re.sub(r'<[^>]+>', ' ', block_html)
    text = re.sub(r'\s+', ' ', text).strip()
    stand_match = re.search(r'Stand:\s*([A-Za-zäöüÄÖÜ]+\s+\d{4})', text)
    lesezeit_match = re.search(r'Lesezeit:\s*(ca\.?\s*\d+\s*Minuten?)', text)
    return (
        stand_match.group(1).strip() if stand_match else "April 2026",
        lesezeit_match.group(1).strip() if lesezeit_match else None,
    )


def build_block(stand, lesezeit, indent="    "):
    """Baut den sauberen .mr-article-meta-Block ohne Inline-Styles."""
    lesezeit_part = ""
    if lesezeit:
        lesezeit_part = (
            '<span class="mr-meta-sep" aria-hidden="true"> · </span>'
            f'<span>Lesezeit: {lesezeit}</span>'
        )
    return (
        f'{indent}<div class="mr-article-meta">'
        '<div>'
        '<strong>Redaktion machsruhig.de</strong>'
        '<span class="mr-meta-sep" aria-hidden="true"> · </span>'
        f'<span>Stand: {stand}</span>'
        '</div>'
        '<div>'
        '<a href="/methodik">Wie entstehen unsere Inhalte?</a>'
        f'{lesezeit_part}'
        '</div>'
        '</div>'
    )


CSS_RULE = """
.mr-article-meta{margin-top:16px;font-size:13px;color:var(--mr-warm);line-height:1.6}
.mr-article-meta>div{display:block}
.mr-article-meta>div+div{margin-top:4px}
.mr-article-meta strong{color:var(--mr-text);font-weight:600}
.mr-article-meta a{color:var(--mr-warm);text-decoration:underline}
.mr-article-meta a:hover{color:var(--mr-primary)}
.mr-article-meta .mr-meta-sep{opacity:0.6}
"""


def process_standard(path, apply=False):
    """Standard-Pattern: <p class="meta"> → <div class="mr-article-meta">."""
    content = path.read_text(encoding='utf-8')
    actions = []
    
    # Block ersetzen
    meta_match = re.search(
        r'([ \t]*)<p\s+class="meta"\s*>(.*?)</p>',
        content,
        flags=re.DOTALL,
    )
    if not meta_match:
        return False, "KEIN <p class=\"meta\"> gefunden"
    
    indent = meta_match.group(1)
    old_inner = meta_match.group(2)
    stand, lesezeit = extract_meta_from_block(old_inner)
    new_block = build_block(stand, lesezeit, indent=indent)
    
    actions.append(f"Block: ersetzt (Stand={stand}, Lesezeit={lesezeit})")
    content = content[:meta_match.start()] + new_block + content[meta_match.end():]
    
    # CSS-Regel einfügen falls noch nicht drin
    if '.mr-article-meta{' in content or '.mr-article-meta ' in content or '.mr-article-meta>' in content:
        actions.append("CSS: bereits vorhanden")
    else:
        style_end = content.find('</style>')
        if style_end == -1:
            return False, " | ".join(actions) + " | FEHLER: kein </style>"
        content = content[:style_end] + CSS_RULE + content[style_end:]
        actions.append("CSS: Regel eingefügt")
    
    if apply:
        path.write_text(content, encoding='utf-8')
    return True, " | ".join(actions)


def process_fallback(path, apply=False):
    """Fallback: Block nach <p class="lead"> einfügen."""
    content = path.read_text(encoding='utf-8')
    actions = []
    
    # Check: ist der Block vielleicht schon da?
    if '<div class="mr-article-meta"' in content:
        actions.append("Block: bereits vorhanden")
    else:
        # Nach </p class="lead">-Ende einfügen
        lead_match = re.search(
            r'([ \t]*)<p\s+class="lead"[^>]*>(.*?)</p>',
            content,
            flags=re.DOTALL,
        )
        if not lead_match:
            return False, "KEIN <p class=\"lead\"> gefunden — unklarer Einfügepunkt"
        
        indent = lead_match.group(1)
        insertion_point = lead_match.end()
        new_block = "\n" + build_block("April 2026", None, indent=indent)
        
        content = content[:insertion_point] + new_block + content[insertion_point:]
        actions.append("Block: nach lead eingefügt (Stand=April 2026, keine Lesezeit)")
    
    # CSS-Regel
    if '.mr-article-meta{' in content or '.mr-article-meta ' in content or '.mr-article-meta>' in content:
        actions.append("CSS: bereits vorhanden")
    else:
        style_end = content.find('</style>')
        if style_end == -1:
            return False, " | ".join(actions) + " | FEHLER: kein </style>"
        content = content[:style_end] + CSS_RULE + content[style_end:]
        actions.append("CSS: Regel eingefügt")
    
    if apply:
        path.write_text(content, encoding='utf-8')
    return True, " | ".join(actions)


def main():
    mode_dry = '--dry-run' in sys.argv
    mode_apply = '--apply' in sys.argv
    if not (mode_dry or mode_apply):
        print("Usage: python3 _dev/apply-author-block-part2.py [--dry-run | --apply]")
        sys.exit(1)
    
    mode_label = "DRY-RUN" if mode_dry else "APPLY"
    print(f"=== {mode_label} — Sprint #4 Teil 2 (24 Seiten) ===\n")
    
    root = Path(__file__).resolve().parent.parent
    success = 0
    failed = 0
    
    print("--- Standard-Pattern (24 Seiten) ---")
    for rel in STANDARD_TARGETS:
        path = root / rel
        if not path.exists():
            print(f"✗ {rel}: nicht gefunden")
            failed += 1
            continue
        ok, info = process_standard(path, apply=mode_apply)
        marker = "✓" if ok else "✗"
        print(f"{marker} {rel}: {info}")
        if ok: success += 1
        else: failed += 1
    
    print("\n--- Fallback-Pattern (Vorsorge-Ordner, kein Meta-Tag) ---")
    for rel in FALLBACK_TARGETS:
        path = root / rel
        if not path.exists():
            print(f"✗ {rel}: nicht gefunden")
            failed += 1
            continue
        ok, info = process_fallback(path, apply=mode_apply)
        marker = "✓" if ok else "✗"
        print(f"{marker} {rel}: {info}")
        if ok: success += 1
        else: failed += 1
    
    print(f"\n=== {success} verarbeitet, {failed} fehlgeschlagen ===")


if __name__ == "__main__":
    main()
