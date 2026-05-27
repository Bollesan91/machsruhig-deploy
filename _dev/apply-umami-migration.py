"""Plausible → Umami Migration.
Replaces all Plausible script-tags with Umami + Plausible-shim.
Existing window.plausible() event-calls bleiben funktional via Shim.
"""
from pathlib import Path
import re
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Umami snippet + Plausible-Shim
UMAMI_BLOCK = '<script defer src="https://cloud.umami.is/script.js" data-website-id="6b6629ff-27b8-427b-863c-76b549cb52ba"></script><script>window.plausible=function(e,o){if(window.umami)window.umami.track(e,(o&&o.props)||{});};</script>'

# Plausible patterns (multiple varieties seen in inventory)
PLAUSIBLE_PATTERNS = [
    # Standard
    '<script defer data-domain="machsruhig.de" src="https://plausible.io/js/script.js"></script>',
    # Variants with different attribute order
    '<script defer src="https://plausible.io/js/script.js" data-domain="machsruhig.de"></script>',
]

# Plus: secondary plausible window-shim (existing pattern in some files)
PLAUSIBLE_WINDOW_SHIM = '<script>window.plausible=window.plausible||function(){(window.plausible.q=window.plausible.q||[]).push(arguments)}</script>'

# Process all HTML
root = Path('.')
total_replaced = 0
files_changed = 0
no_match = []

for p in root.rglob('*.html'):
    if '_dev' in p.parts or 'node_modules' in p.parts:
        continue
    s = p.read_text(encoding='utf-8', errors='ignore')
    original = s
    n = 0
    # Replace primary Plausible script-tag
    for pattern in PLAUSIBLE_PATTERNS:
        if pattern in s:
            s = s.replace(pattern, UMAMI_BLOCK)
            n += 1
    # Remove duplicate plausible-window-shim (we now have own shim from Umami-block)
    if PLAUSIBLE_WINDOW_SHIM in s:
        s = s.replace(PLAUSIBLE_WINDOW_SHIM, '')
        n += 1
    if n > 0:
        p.write_text(s, encoding='utf-8', newline='\n')
        files_changed += 1
        total_replaced += n

# Re-scan for any plausible.io leftover
print(f"\nFiles changed: {files_changed}")
print(f"Total replacements: {total_replaced}")

leftover_count = 0
for p in root.rglob('*.html'):
    if '_dev' in p.parts or 'node_modules' in p.parts:
        continue
    s = p.read_text(encoding='utf-8', errors='ignore')
    if 'plausible.io' in s:
        leftover_count += 1
        print(f"  LEFTOVER plausible.io in: {p}")
print(f"\nFiles with residual 'plausible.io' script-tag: {leftover_count}")

# Verify Umami present
umami_count = 0
for p in root.rglob('*.html'):
    if '_dev' in p.parts or 'node_modules' in p.parts:
        continue
    s = p.read_text(encoding='utf-8', errors='ignore')
    if 'cloud.umami.is' in s:
        umami_count += 1
print(f"Files with new Umami-script: {umami_count}")
