#!/usr/bin/env python3
"""
FAQ-JSON-LD-Regenerator
=======================
Regeneriert den FAQPage-JSON-LD-Eintrag aus dem sichtbaren HTML-FAQ-Block
(Single Source of Truth = HTML).

Strategie:
- Extrahiere sichtbare FAQs aus dem mr-faq / <details>-Block unter dem
  „Häufig gestellte Fragen / FAQ / Fragen"-H2.
- Konvertiere Antwort-Text in Plain-Text (HTML-Tags strippen, &amp; etc. entschlüsseln).
- Ersetze den FAQPage-Eintrag im @graph in-place.
- Falls bisher kein FAQPage existiert (NO_LD): Eintrag im @graph einfügen.

Default: --dry-run (zeigt Diff, schreibt nicht).
Aktiv schreiben: --write.
"""

import argparse
import json
import re
import sys
import unicodedata
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CITIES_DIR = ROOT / "bestatter"

# Wiederverwendet aus faq-schema-drift.py
FAQ_HEADER_RE = re.compile(
    r"<h2[^>]*>\s*(?:[^<]*?)(?:FAQ|Häufig|H&auml;ufig|Fragen)[^<]*?</h2>",
    re.IGNORECASE | re.DOTALL,
)


def html_to_plain(text: str) -> str:
    """Strippt HTML-Tags, entschlüsselt Entities, kollabiert Whitespace."""
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_html_faq(html: str):
    """Identisch zu faq-schema-drift.py: nur FAQ-Section-<details>."""
    faqs = []
    headers = list(FAQ_HEADER_RE.finditer(html))
    if not headers:
        return faqs
    spans = []
    for h in headers:
        start = h.end()
        end_h2 = re.search(r"<h2[^>]*>", html[start:])
        end_sect = re.search(r"</section\b", html[start:])
        candidates = [c.start() for c in [end_h2, end_sect] if c]
        end = start + min(candidates) if candidates else len(html)
        spans.append((start, end))
    for start, end in spans:
        region = html[start:end]
        for det in re.finditer(
            r"<details([^>]*)>\s*<summary[^>]*>(.*?)</summary>\s*(.*?)</details>",
            region,
            re.DOTALL,
        ):
            attrs = det.group(1) or ""
            if re.search(r"mr-nav-mobile|nav-mobile|class=[\"'][^\"']*nav", attrs):
                continue
            q = html_to_plain(det.group(2))
            if q in {"☰", ""} or len(q) <= 3:
                continue
            body = det.group(3).strip()
            inner = re.search(
                r'<div\s+class="faq-answer"[^>]*>(.*?)</div>',
                body,
                re.DOTALL,
            )
            a_html = inner.group(1) if inner else body
            a = html_to_plain(a_html)
            faqs.append({"q": q, "a": a})
    return faqs


def find_jsonld_blocks(html: str):
    """Findet alle JSON-LD <script>-Blöcke. Yields (match, parsed_data)."""
    for m in re.finditer(
        r'(<script[^>]*type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)',
        html,
        re.DOTALL,
    ):
        try:
            data = json.loads(m.group(2).strip())
        except json.JSONDecodeError:
            continue
        yield m, data


def build_faq_node(faqs):
    """Baut FAQPage-Node aus FAQ-Liste."""
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f["a"],
                },
            }
            for f in faqs
        ],
    }


def detect_format(raw_body: str):
    """Erkenne JSON-LD-Format: minified vs indented.
    Gibt (indent_value, separators) für json.dumps zurück.
    """
    # Wenn original-Body keinen Linebreak hat → minified
    if "\n" not in raw_body.strip():
        return None, (",", ":")
    # Indent = erste Einrückung NACH `{` oder `[` am Body-Start
    m = re.search(r"[{\[]\n( +)[\"{\[]", raw_body)
    indent = len(m.group(1)) if m else 2
    return indent, (",", ": ")


def regenerate_page(html: str, faqs):
    """Ersetzt FAQPage im @graph (dict) oder in der Top-Level-List durch neuen Node.
    Format (minified/indented) wird aus dem Original beibehalten."""
    new_node = build_faq_node(faqs)
    for m, data in find_jsonld_blocks(html):
        raw_body = m.group(2)
        # Stil 1: {"@graph": [...]}
        if isinstance(data, dict) and isinstance(data.get("@graph"), list):
            container = data["@graph"]
        # Stil 2: Top-level [...]
        elif isinstance(data, list):
            container = data
        else:
            continue

        action = None
        for i, node in enumerate(container):
            if isinstance(node, dict) and node.get("@type") == "FAQPage":
                merged = dict(new_node)
                if "@id" in node:
                    merged["@id"] = node["@id"]
                container[i] = merged
                action = "replaced"
                break
        if action is None:
            container.append(new_node)
            action = "inserted"

        indent, sep = detect_format(raw_body)
        # Behalte führenden/abschließenden Whitespace im Body bei (z.B. \n vor `{`)
        leading = re.match(r"\s*", raw_body).group(0)
        trailing = re.search(r"\s*\Z", raw_body).group(0)
        new_json = json.dumps(data, ensure_ascii=False, indent=indent, separators=sep)
        new_body = leading + new_json + trailing
        new_html = html[: m.start()] + m.group(1) + new_body + m.group(3) + html[m.end():]
        return new_html, action
    return html, "noop"


def extract_faq_node_from_html(src: str):
    """Extrahiert das FAQPage-Objekt — unterstützt @graph-dict und top-level-list."""
    for m, data in find_jsonld_blocks(src):
        if isinstance(data, dict) and isinstance(data.get("@graph"), list):
            container = data["@graph"]
        elif isinstance(data, list):
            container = data
        else:
            continue
        for node in container:
            if isinstance(node, dict) and node.get("@type") == "FAQPage":
                return node
    return None


def diff_preview(old: str, new: str, city: str):
    """Zeigt nur den FAQPage-Bereich aus old & new (parsed via JSON, robust)."""
    print(f"\n=== {city} ===")
    for label, src in [("OLD", old), ("NEW", new)]:
        node = extract_faq_node_from_html(src)
        print(f"\n--- {label} FAQPage ---")
        if node:
            qs = node.get("mainEntity", [])
            print(f"({len(qs)} Q/A)")
            for i, q in enumerate(qs):
                name = q.get("name", "?")
                text = q.get("acceptedAnswer", {}).get("text", "")
                print(f"  [{i}] Q: {name}")
                print(f"      A: {text[:240]}{'…' if len(text) > 240 else ''}")
        else:
            print("  (kein FAQPage)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--city", help="Single city to process (default: all)")
    ap.add_argument("--write", action="store_true", help="Actually write files (default: dry-run)")
    ap.add_argument("--diff", action="store_true", help="Show diff preview")
    ap.add_argument("--skip", default="lübeck,mönchengladbach,darmstadt", help="Comma-separated cities to skip")
    args = ap.parse_args()

    skip = set(args.skip.split(","))

    if args.city:
        cities = [CITIES_DIR / args.city]
    else:
        cities = sorted([p for p in CITIES_DIR.iterdir() if p.is_dir() and p.name not in skip])

    summary = {"replaced": [], "inserted": [], "noop": [], "no_html_faq": []}
    for city_dir in cities:
        if city_dir.name in skip:
            continue
        index = city_dir / "index.html"
        if not index.exists():
            continue
        html = index.read_text(encoding="utf-8")
        faqs = extract_html_faq(html)
        if not faqs:
            summary["no_html_faq"].append(city_dir.name)
            continue
        new_html, action = regenerate_page(html, faqs)
        summary[action].append(city_dir.name)
        if action == "noop":
            continue
        if args.diff:
            diff_preview(html, new_html, city_dir.name)
        if args.write and new_html != html:
            index.write_text(new_html, encoding="utf-8")

    print(f"\n--- Summary ({'WRITE' if args.write else 'DRY-RUN'}) ---")
    for k, v in summary.items():
        print(f"{k:14}: {len(v)}  -> {', '.join(v) if v else '-'}")


if __name__ == "__main__":
    main()
