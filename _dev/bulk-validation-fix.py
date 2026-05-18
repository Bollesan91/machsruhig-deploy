#!/usr/bin/env python3
"""Bulk-Fix für systemische Validation-Issues über alle bestatter/<city>/index.html.

Behebt:
1. UNSURE-Kommentare aus Production-HTML strippen
2. Nav-Link /bestatter/muenchen/ -> /bestatter/ (außer auf muenchen-Page selbst)

Beide Fixes sind sicher idempotent.
"""
import re
import os
import glob

BESTATTER_DIR = 'bestatter'

UNSURE_PATTERN = re.compile(r'<!--\s*UNSURE[\s\S]*?-->', re.IGNORECASE)
MUENCHEN_LINK = re.compile(r'href="/bestatter/muenchen/"')

total = 0
fixed_unsure = 0
fixed_nav = 0
unchanged = 0

for path in sorted(glob.glob(f'{BESTATTER_DIR}/*/index.html')):
    city = os.path.basename(os.path.dirname(path))
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()
    
    content = original
    
    # Fix 1: Strip UNSURE comments
    unsure_count = len(UNSURE_PATTERN.findall(content))
    if unsure_count > 0:
        content = UNSURE_PATTERN.sub('', content)
        fixed_unsure += 1
        print(f'  [{city}] UNSURE: {unsure_count} Kommentare entfernt')
    
    # Fix 2: Nav-Link to muenchen (only if NOT on muenchen page itself)
    if city != 'muenchen':
        nav_count = len(MUENCHEN_LINK.findall(content))
        if nav_count > 0:
            content = MUENCHEN_LINK.sub('href="/bestatter/"', content)
            fixed_nav += 1
            print(f'  [{city}] Nav-Link: {nav_count}x /bestatter/muenchen/ -> /bestatter/')
    
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        total += 1
    else:
        unchanged += 1

print(f'\n=== Summary ===')
print(f'Cities geprüft: {total + unchanged}')
print(f'Cities mit Fix: {total}')
print(f'  UNSURE-Strip: {fixed_unsure} cities')
print(f'  Nav-Link-Fix: {fixed_nav} cities')
print(f'Cities unchanged: {unchanged}')
