#!/usr/bin/env python3
"""
apply-author-block-cleanup.py — Sprint #4, Schritt 2 (Nachbesserung)

Räumt technische Schuld aus Schritt 1 auf:
1. Entfernt Inline-Styles aus dem <div class="mr-article-meta">-Block
2. Fügt die CSS-Regel .mr-article-meta in den <style>-Block jeder Seite ein

Dry-Run und Apply wie vorher.
"""

import re
import sys
from pathlib import Path

TARGETS = [
    "beerdigung-planen.html",
    "bestattungsarten.html",
    "bestattungskosten.html",
    "kindern-tod-erklaeren.html",
    "kondolenzschreiben.html",
    "trauerrede-schreiben.html",
    "trauersprueche.html",
    "vertraege-kuendigen.html",
    "bestatter/berlin/index.html",
    "bestatter/frankfurt/index.html",
    "bestatter/hamburg/index.html",
    "bestatter/koeln/index.html",
    "bestatter/muenchen/index.html",
]

# Der Block, wie er aktuell im HTML steht (mit Inline-Styles)
# Wir parsen ihn, entfernen die style-Attribute, und bauen ihn sauber wieder auf.

# Regex, der den kompletten article-meta-Block matched
META_BLOCK_PATTERN = re.compile(
    r'<div\s+class="mr-article-meta"[^>]*>(.*?)</div>(?=\s*\n\s*</header>|\s*\n\s*\n|\s*</header>)',
    re.DOTALL
)

# Kompakter: Match auf äußerstes <div class="mr-article-meta" ...> bis passendes </div>
# Das ist tricky bei verschachtelten <div>. Ich nutze einen Tag-Counter.

def find_block_extent(content, start_tag_idx):
    """Findet das passende schließende </div> zum öffnenden <div class="mr-article-meta"> bei start_tag_idx."""
    # Start am öffnenden <div
    pos = start_tag_idx
    # Ende des öffnenden <div>-Tags finden
    open_end = content.find('>', pos) + 1
    depth = 1
    i = open_end
    while depth > 0 and i < len(content):
        next_open = content.find('<div', i)
        next_close = content.find('</div>', i)
        if next_close == -1:
            return None  # broken
        if next_open != -1 and next_open < next_close:
            depth += 1
            i = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                return (start_tag_idx, next_close + 6)
            i = next_close + 6
    return None


# Neue saubere Block-Form — ohne Inline-Styles
def build_clean_block(stand, lesezeit):
    lesezeit_part = ""
    if lesezeit:
        lesezeit_part = (
            '<span class="mr-meta-sep" aria-hidden="true"> · </span>'
            f'<span>Lesezeit: {lesezeit}</span>'
        )
    return (
        '<div class="mr-article-meta">'
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


def extract_meta(block_html):
    """Extrahiert Stand und Lesezeit aus dem vorhandenen Block."""
    # Jeden <div>-Inhalt einzeln extrahieren, damit wir "Stand" und "Lesezeit"
    # nicht aus verschiedenen Zeilen zusammenzimmern.
    inner_divs = re.findall(r'<div[^>]*>(.*?)</div>', block_html, flags=re.DOTALL)
    joined = " ".join(inner_divs)
    text = re.sub(r'<[^>]+>', ' ', joined)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # "Stand: April 2026 · …" oder "Stand: April 2026" am Ende
    stand_match = re.search(r'Stand:\s*([A-Za-zäöüÄÖÜ]+\s+\d{4})', text)
    lesezeit_match = re.search(r'Lesezeit:\s*(ca\.?\s*\d+\s*Minuten?)', text)
    return (
        stand_match.group(1).strip() if stand_match else "April 2026",
        lesezeit_match.group(1).strip() if lesezeit_match else None,
    )


# CSS-Regel, die in den <style>-Block eingefügt wird, falls noch nicht vorhanden
CSS_RULE = """
.mr-article-meta{margin-top:16px;font-size:13px;color:var(--mr-warm);line-height:1.6}
.mr-article-meta>div{display:block}
.mr-article-meta>div+div{margin-top:4px}
.mr-article-meta strong{color:var(--mr-text);font-weight:600}
.mr-article-meta a{color:var(--mr-warm);text-decoration:underline}
.mr-article-meta a:hover{color:var(--mr-primary)}
.mr-article-meta .mr-meta-sep{opacity:0.6}
"""


def process_file(path, apply=False):
    content = path.read_text(encoding='utf-8')
    actions = []
    
    # 1. Block-Refactor: Inline-Styles entfernen
    idx = content.find('<div class="mr-article-meta"')
    if idx == -1:
        return False, "KEIN mr-article-meta-Block gefunden"
    
    extent = find_block_extent(content, idx)
    if not extent:
        return False, "Block-Extent konnte nicht bestimmt werden"
    
    old_block = content[extent[0]:extent[1]]
    stand, lesezeit = extract_meta(old_block)
    new_block = build_clean_block(stand, lesezeit)
    
    if old_block == new_block:
        actions.append("Block: bereits sauber (nichts zu tun)")
    else:
        actions.append(f"Block: Inline-Styles entfernt (Stand={stand}, Lesezeit={lesezeit})")
        content = content[:extent[0]] + new_block + content[extent[1]:]
    
    # 2. CSS-Regel einfügen, falls noch nicht drin
    if '.mr-article-meta{' in content or '.mr-article-meta ' in content or '.mr-article-meta>' in content:
        actions.append("CSS: bereits vorhanden")
    else:
        # Vor </style> einfügen
        style_end = content.find('</style>')
        if style_end == -1:
            actions.append("CSS: FEHLER — kein </style> gefunden")
            return False, " | ".join(actions)
        content = content[:style_end] + CSS_RULE + content[style_end:]
        actions.append("CSS: Regel hinzugefügt vor </style>")
    
    if apply:
        path.write_text(content, encoding='utf-8')
    
    return True, " | ".join(actions)


def main():
    mode_dry = '--dry-run' in sys.argv
    mode_apply = '--apply' in sys.argv
    if not (mode_dry or mode_apply):
        print("Usage: python3 _dev/apply-author-block-cleanup.py [--dry-run | --apply]")
        sys.exit(1)
    
    mode_label = "DRY-RUN" if mode_dry else "APPLY"
    print(f"=== {mode_label} ===\n")
    
    root = Path(__file__).resolve().parent.parent
    success = 0
    failed = 0
    for rel_path in TARGETS:
        path = root / rel_path
        if not path.exists():
            print(f"✗ {rel_path}: nicht gefunden")
            failed += 1
            continue
        ok, info = process_file(path, apply=mode_apply)
        marker = "✓" if ok else "✗"
        print(f"{marker} {rel_path}")
        print(f"  {info}")
        print()
        if ok: success += 1
        else: failed += 1
    
    print(f"=== {success} verarbeitet, {failed} fehlgeschlagen ===")


if __name__ == "__main__":
    main()
