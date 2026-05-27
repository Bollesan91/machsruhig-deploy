#!/usr/bin/env python3
"""
apply-author-block.py — Sprint #4, Schritt 1

Ersetzt auf 13 YMYL-Seiten die existierende <p class="meta">-Zeile durch
einen strukturierten Autoren-Block (div.mr-article-meta).

Features:
- Dry-Run-Modus: zeigt pro Seite die Diff ohne zu schreiben
- Apply-Modus: schreibt die Änderungen in die Dateien
- Preserves existierende Stand-Dates und Lesezeit-Angaben (Ehrlichkeit)
- Regex-basiert, ignoriert Variantenvielfalt der Meta-Zeile

Usage:
  python3 _dev/apply-author-block.py --dry-run    # nur zeigen
  python3 _dev/apply-author-block.py --apply      # ausführen
"""

import re
import sys
from pathlib import Path

# 13 YMYL-Seiten für Sprint #4
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

# Regex: findet <p class="meta">...</p> Zeile (auch mit mehrzeiligem Inhalt, aber typisch einzeilig)
META_PATTERN = re.compile(
    r'<p\s+class="meta"\s*>(.*?)</p>',
    re.DOTALL
)

def extract_stand_and_lesezeit(inner_html):
    """Parst 'Stand: April 2026 · Lesezeit: ca. X Minuten · Methodik' → dict."""
    # Normalisieren: HTML-Entities → Unicode, HTML-Tags weg für Analyse
    text = inner_html.replace("&middot;", "·").replace("&nbsp;", " ")
    text_clean = re.sub(r"<[^>]+>", "", text)
    
    stand_match = re.search(r"Stand:\s*([^·]+?)(?:\s*·|\s*$)", text_clean)
    lesezeit_match = re.search(r"Lesezeit:\s*([^·]+?)(?:\s*·|\s*$)", text_clean)
    
    return {
        "stand": stand_match.group(1).strip() if stand_match else "April 2026",
        "lesezeit": lesezeit_match.group(1).strip() if lesezeit_match else None,
    }


def build_author_block(meta_info):
    """Konstruiert den neuen <div class="mr-article-meta">-Block."""
    lesezeit = meta_info["lesezeit"]
    stand = meta_info["stand"]
    
    # Inline-Styles, weil 13 Seiten noch kein zentrales CSS einbinden
    lesezeit_part = (
        f'<span class="mr-meta-sep" aria-hidden="true"> · </span>'
        f'<span>Lesezeit: {lesezeit}</span>'
    ) if lesezeit else ""
    
    return (
        '<div class="mr-article-meta" '
        'style="margin-top:16px;font-size:13px;color:var(--mr-warm,#7A6B5D);line-height:1.6">'
        '<div>'
        '<strong style="color:var(--mr-text,#2D2319);font-weight:600">Redaktion machsruhig.de</strong>'
        '<span class="mr-meta-sep" aria-hidden="true"> · </span>'
        f'<span>Stand: {stand}</span>'
        '</div>'
        '<div style="margin-top:4px">'
        '<a href="/methodik" style="color:var(--mr-warm,#7A6B5D);text-decoration:underline">Wie entstehen unsere Inhalte?</a>'
        f'{lesezeit_part}'
        '</div>'
        '</div>'
    )


def process_file(path, apply=False):
    """Verarbeitet eine Datei. Returns (changed, diff_or_error)."""
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        return False, f"FEHLER beim Lesen: {e}"
    
    matches = list(META_PATTERN.finditer(content))
    if not matches:
        return False, "KEIN <p class=\"meta\"> gefunden"
    if len(matches) > 1:
        return False, f"WARNUNG: {len(matches)} meta-Zeilen gefunden — skip zur Sicherheit"
    
    m = matches[0]
    inner = m.group(1)
    meta_info = extract_stand_and_lesezeit(inner)
    new_block = build_author_block(meta_info)
    
    old_html = m.group(0)
    new_content = content[:m.start()] + new_block + content[m.end():]
    
    diff = (
        f"  ALT: {old_html[:100]}{'...' if len(old_html) > 100 else ''}\n"
        f"  NEU: Stand={meta_info['stand']}, Lesezeit={meta_info['lesezeit']}, Methodik-Link ja"
    )
    
    if apply:
        path.write_text(new_content, encoding="utf-8")
    
    return True, diff


def main():
    mode_dry = "--dry-run" in sys.argv
    mode_apply = "--apply" in sys.argv
    
    if not (mode_dry or mode_apply):
        print("Usage: python3 _dev/apply-author-block.py [--dry-run | --apply]")
        sys.exit(1)
    
    root = Path(__file__).resolve().parent.parent
    mode_label = "DRY-RUN (keine Schreibvorgänge)" if mode_dry else "APPLY (Änderungen werden geschrieben)"
    
    print(f"=== {mode_label} ===\n")
    
    success = 0
    skipped = 0
    
    for rel_path in TARGETS:
        path = root / rel_path
        if not path.exists():
            print(f"✗ {rel_path}: Datei nicht gefunden")
            skipped += 1
            continue
        
        changed, info = process_file(path, apply=mode_apply)
        marker = "✓" if changed else "✗"
        print(f"{marker} {rel_path}")
        print(info)
        print()
        
        if changed:
            success += 1
        else:
            skipped += 1
    
    print(f"=== Zusammenfassung: {success} verarbeitet, {skipped} übersprungen ===")


if __name__ == "__main__":
    main()
