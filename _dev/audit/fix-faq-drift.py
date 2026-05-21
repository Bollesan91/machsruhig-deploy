"""
FAQ-Schema-Drift FIXER
======================
Liest pro Stadt die HTML-FAQ-Q/A,
und schreibt das FAQPage-Schema im JSON-LD synchron.

Strategie: HTML ist die Wahrheit. JSON-LD wird daraus regeneriert.

- Existierender FAQPage-Node: mainEntity wird ersetzt.
- Kein FAQPage-Node: neuer Node wird ans Ende von @graph angefügt.
"""

import os
import re
import json
import html
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
BESTATTER_DIR = _HERE.parent.parent / "bestatter"
REPORT_PATH = _HERE / "faq-drift-report.json"

JSON_LD_RE = re.compile(
    r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',
    re.DOTALL | re.IGNORECASE,
)


def _clean_inner_html_to_text(s: str) -> str:
    """Convert inner HTML of a FAQ answer to a clean plain string for Schema."""
    if not s:
        return ""
    # Replace block-level breaks with spaces
    s = re.sub(r"</p\s*>", " ", s, flags=re.IGNORECASE)
    s = re.sub(r"<br\s*/?>", " ", s, flags=re.IGNORECASE)
    s = re.sub(r"</li\s*>", " ", s, flags=re.IGNORECASE)
    s = re.sub(r"</h[1-6]\s*>", " ", s, flags=re.IGNORECASE)
    # Strip all remaining tags
    s = re.sub(r"<[^>]+>", "", s)
    # Decode entities
    s = html.unescape(s)
    # Normalize whitespace
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _clean_question(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def extract_html_faq_pairs(html_text: str):
    """Return [(question, answer_text), ...] from the visible FAQ section."""
    faq_heading_re = re.compile(
        r'<h2[^>]*>([^<]*(?:FAQ|Häufige Fragen|Fragen)[^<]*)</h2>',
        re.IGNORECASE,
    )
    m = faq_heading_re.search(html_text)
    if not m:
        return []
    start = m.end()
    next_h2 = re.search(r"<h2|</section", html_text[start:], re.IGNORECASE)
    end = start + next_h2.start() if next_h2 else len(html_text)
    block = html_text[start:end]

    pairs = []

    # Pattern 1: <details><summary>Q</summary>A...</details>
    details_re = re.compile(
        r"<details[^>]*>\s*<summary[^>]*>(.*?)</summary>(.*?)</details>",
        re.DOTALL | re.IGNORECASE,
    )
    for dm in details_re.finditer(block):
        q = _clean_question(dm.group(1))
        a = _clean_inner_html_to_text(dm.group(2))
        if q and a:
            pairs.append((q, a))

    if pairs:
        return pairs

    # Pattern 2: <h3>Q</h3>...<p>A</p>... within block
    h3_re = re.compile(r"<h3[^>]*>(.*?)</h3>(.*?)(?=<h3|$)", re.DOTALL | re.IGNORECASE)
    for hm in h3_re.finditer(block):
        q = _clean_question(hm.group(1))
        a = _clean_inner_html_to_text(hm.group(2))
        if q and a:
            pairs.append((q, a))

    return pairs


def build_faq_node(city_slug: str, pairs):
    return {
        "@type": "FAQPage",
        "@id": f"https://machsruhig.de/bestatter/{city_slug}/#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a,
                },
            }
            for q, a in pairs
        ],
    }


def patch_html(idx_path: Path, city_slug: str):
    text = idx_path.read_text(encoding="utf-8", errors="replace")
    pairs = extract_html_faq_pairs(text)
    if not pairs:
        return "no-html-faq", 0

    faq_node = build_faq_node(city_slug, pairs)

    # Find first JSON-LD script that contains FAQPage or has @graph
    target_script = None
    for m in JSON_LD_RE.finditer(text):
        raw = m.group(2).strip()
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            continue
        # Prefer a script that has @graph (the main page schema)
        if isinstance(data, dict) and "@graph" in data:
            target_script = (m, raw, data)
            break

    if target_script is None:
        # Fallback: pick any FAQPage-only script
        for m in JSON_LD_RE.finditer(text):
            raw = m.group(2).strip()
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if isinstance(data, dict) and data.get("@type") == "FAQPage":
                target_script = (m, raw, data)
                break

    if target_script is None:
        return "no-jsonld-script", len(pairs)

    m, raw, data = target_script

    # Modify the JSON
    if "@graph" in data:
        graph = data["@graph"]
        # Remove any existing FAQPage nodes (defensive: keep first matched ID, replace)
        graph = [n for n in graph if not (isinstance(n, dict) and (n.get("@type") == "FAQPage"))]
        graph.append(faq_node)
        data["@graph"] = graph
    elif data.get("@type") == "FAQPage":
        data = faq_node
    else:
        # Convert single-node script into @graph
        data = {"@context": data.get("@context", "https://schema.org"), "@graph": [data, faq_node]}

    new_json = json.dumps(data, ensure_ascii=False, indent=2)
    new_script = m.group(1) + new_json + m.group(3)
    new_text = text[: m.start()] + new_script + text[m.end():]

    if new_text != text:
        idx_path.write_text(new_text, encoding="utf-8")
        return "patched", len(pairs)
    else:
        return "no-change", len(pairs)


def main():
    if REPORT_PATH.exists():
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
        drifted = [r["city"] for r in report if r["drift"]]
    else:
        # Fallback hardcoded list
        drifted = [
            "augsburg", "berlin", "bremen", "chemnitz",
            "darmstadt", "essen", "hamburg", "muelheim",
            "muenster", "rostock",
        ]

    print(f"Fixing FAQ-Schema-Drift for {len(drifted)} cities:")
    for slug in drifted:
        city_dir = BESTATTER_DIR / slug
        idx = city_dir / "index.html"
        if not idx.exists():
            print(f"  - {slug}: MISSING index.html")
            continue
        status, n = patch_html(idx, slug)
        print(f"  - {slug:<20} {status:<18} html_qa={n}")


if __name__ == "__main__":
    main()
