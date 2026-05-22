#!/usr/bin/env python3
"""
FAQ-Sync-Check: Verifiziert, dass JSON-LD FAQPage Question.name
mit visible <summary>-Texts übereinstimmt UND
dass JSON-LD Answer.text mit faq-answer-Inhalt matched.

Usage: python3 check-faq-sync.py file1.html [file2.html ...]
Exit-Code: 0 wenn alle synchron, 1 bei Mismatch.
"""
import sys
import re
import json
from pathlib import Path

def extract_jsonld_faqs(html):
    """Extract list of {name, text} from FAQPage JSON-LD blocks."""
    results = []
    for m in re.finditer(r'<script type="application/ld\+json">([\s\S]*?)</script>', html):
        block = m.group(1).strip()
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        graph = data.get('@graph', [data]) if isinstance(data, dict) else []
        if isinstance(data, list):
            graph = data
        for item in graph:
            if isinstance(item, dict) and item.get('@type') == 'FAQPage':
                for q in item.get('mainEntity', []):
                    name = q.get('name', '').strip()
                    text = q.get('acceptedAnswer', {}).get('text', '').strip()
                    results.append({'name': name, 'text': text})
    return results

def extract_visible_faqs(html):
    """Extract list of {q, a} from visible HTML <details><summary>.</summary><div class='faq-answer'>...</div></details> patterns."""
    results = []
    # Pattern: <details>...<summary>Q TEXT</summary><div class="faq-answer">A TEXT</div>...</details>
    detail_pattern = re.compile(r'<details[^>]*>([\s\S]*?)</details>', re.IGNORECASE)
    for m in detail_pattern.finditer(html):
        block = m.group(1)
        # Extract summary text (strip HTML tags within)
        summary_m = re.search(r'<summary[^>]*>(.*?)</summary>', block, re.DOTALL | re.IGNORECASE)
        if not summary_m:
            continue
        q_raw = summary_m.group(1)
        q = re.sub(r'<[^>]+>', '', q_raw).strip()
        # Extract faq-answer text (first div with class faq-answer)
        answer_m = re.search(r'<div class="faq-answer"[^>]*>(.*?)</div>', block, re.DOTALL | re.IGNORECASE)
        if answer_m:
            a_raw = answer_m.group(1)
            a = re.sub(r'<[^>]+>', '', a_raw).strip()
            # Normalize whitespace
            a = re.sub(r'\s+', ' ', a)
            results.append({'q': q, 'a': a})
    return results

def check_file(path):
    """Returns (mismatches_count, details)."""
    html = Path(path).read_text(encoding='utf-8')
    jsonld = extract_jsonld_faqs(html)
    visible = extract_visible_faqs(html)
    mismatches = []
    if not jsonld:
        return 0, ['No FAQPage JSON-LD found (skipping)']
    if not visible:
        return 1, ['JSON-LD has FAQs but no visible <details><summary>+faq-answer pattern']
    if len(jsonld) != len(visible):
        mismatches.append(f'Count mismatch: JSON-LD has {len(jsonld)} questions, visible has {len(visible)}')
    n = min(len(jsonld), len(visible))
    for i in range(n):
        if jsonld[i]['name'] != visible[i]['q']:
            mismatches.append(f"Q{i+1} NAME MISMATCH:\n  JSON-LD: {jsonld[i]['name']}\n  Visible: {visible[i]['q']}")
        # Normalize whitespace for answer comparison
        ans_json = re.sub(r'\s+', ' ', jsonld[i]['text']).strip()
        ans_vis = re.sub(r'\s+', ' ', visible[i]['a']).strip()
        if ans_json != ans_vis:
            mismatches.append(f"Q{i+1} ANSWER MISMATCH (excerpt):\n  JSON-LD: {ans_json[:120]}...\n  Visible: {ans_vis[:120]}...")
    return len(mismatches), mismatches

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 check-faq-sync.py file1.html [file2.html ...]')
        sys.exit(2)
    total_mismatches = 0
    for path in sys.argv[1:]:
        n, details = check_file(path)
        status = 'OK' if n == 0 else f'MISMATCH ({n})'
        print(f'\n=== {path}: {status} ===')
        for d in details:
            print(f'  {d}')
        total_mismatches += n
    print(f'\nTotal mismatches: {total_mismatches}')
    sys.exit(0 if total_mismatches == 0 else 1)

if __name__ == '__main__':
    main()
