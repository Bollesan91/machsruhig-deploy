#!/usr/bin/env python3
"""Bulk-Fix v2: Article-Schema (image+publisher.logo) + og:image:alt
Idempotent über alle bestatter/<city>/index.html.
"""
import re
import os
import glob
import json

BESTATTER_DIR = 'bestatter'
GENERIC_OG = 'https://machsruhig.de/assets/og-image.png'
LOGO_URL = 'https://machsruhig.de/assets/logo.png'

# Patterns
JSONLD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL)
OG_IMAGE_RE = re.compile(r'<meta property="og:image" content="([^"]+)"')
OG_ALT_RE = re.compile(r'<meta property="og:image:alt"')

def fix_jsonld(jsonld_str, city, og_img_url):
    """Fix Article schema in JSON-LD. Add image + publisher.logo if missing."""
    try:
        data = json.loads(jsonld_str)
    except json.JSONDecodeError:
        return jsonld_str, False
    
    modified = False
    
    # Handle both {@graph: [...]} and direct object
    graph = data.get('@graph', []) if isinstance(data, dict) and '@graph' in data else [data] if isinstance(data, dict) else data
    
    for obj in graph:
        if not isinstance(obj, dict):
            continue
        t = obj.get('@type', '')
        if t == 'Article' or (isinstance(t, list) and 'Article' in t):
            # Fix image
            if 'image' not in obj:
                obj['image'] = og_img_url
                modified = True
            # Fix publisher.logo
            pub = obj.get('publisher')
            if isinstance(pub, dict) and 'logo' not in pub:
                pub['logo'] = {'@type': 'ImageObject', 'url': LOGO_URL}
                modified = True
    
    if modified:
        return json.dumps(data, ensure_ascii=False, indent=2), True
    return jsonld_str, False

def main():
    total = 0
    fixed_article = 0
    added_og_alt = 0
    unchanged = 0
    
    for path in sorted(glob.glob(f'{BESTATTER_DIR}/*/index.html')):
        city = os.path.basename(os.path.dirname(path))
        with open(path, 'r', encoding='utf-8') as f:
            original = f.read()
        
        content = original
        page_modified = False
        
        # Find OG image URL for this page (use it for Article.image if generic, else just use generic)
        og_match = OG_IMAGE_RE.search(content)
        og_img_for_city = og_match.group(1) if og_match else GENERIC_OG
        
        # Fix 1: Article-Schema image + publisher.logo
        def replace_jsonld(m):
            nonlocal page_modified
            jsonld_str = m.group(1)
            fixed_str, mod = fix_jsonld(jsonld_str, city, og_img_for_city)
            if mod:
                page_modified = True
                return f'<script type="application/ld+json">{fixed_str}</script>'
            return m.group(0)
        
        new_content = JSONLD_RE.sub(replace_jsonld, content)
        if new_content != content:
            content = new_content
            fixed_article += 1
            print(f'  [{city}] Article-Schema: image + publisher.logo ergänzt')
        
        # Fix 2: og:image:alt missing
        if og_match and not OG_ALT_RE.search(content):
            alt_text = f'Bestattung in {city.capitalize()} — Friedhöfe, Kosten, Bestatter | machsruhig.de'
            alt_tag = f'<meta property="og:image:alt" content="{alt_text}">'
            # Insert after og:image
            og_idx = content.find('<meta property="og:image"')
            if og_idx >= 0:
                line_end = content.find('>', og_idx) + 1
                content = content[:line_end] + '\n' + alt_tag + content[line_end:]
                added_og_alt += 1
                page_modified = True
                print(f'  [{city}] og:image:alt ergänzt')
        
        if content != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            total += 1
        else:
            unchanged += 1
    
    print(f'\n=== Summary v2 ===')
    print(f'Cities geprüft: {total + unchanged}')
    print(f'Cities mit Fix: {total}')
    print(f'  Article-Schema-Fix: {fixed_article} cities')
    print(f'  og:image:alt-Fix: {added_og_alt} cities')
    print(f'Cities unchanged: {unchanged}')

main()
