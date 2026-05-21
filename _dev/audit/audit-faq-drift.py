"""
FAQ-Schema-Drift-Audit
======================
Vergleicht je Stadt-Page:
- JSON-LD FAQPage (Schema.org)
- Sichtbarer HTML-FAQ-Block (h3/h4/details/summary)

Findet Drift wenn:
- Anzahl Q/A in Schema != Anzahl im HTML
- Question-Texte unterschiedlich
- Answer-Texte stark abweichend

Output: pro Stadt einen Drift-Score + Detail-Diff
"""

import os
import re
import json
import html
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
BESTATTER_DIR = _HERE.parent.parent / "bestatter"

JSON_LD_RE = re.compile(
    r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)


def normalize(s: str) -> str:
    if not s:
        return ""
    s = html.unescape(s)
    s = re.sub(r"<[^>]+>", " ", s)  # strip any inline HTML
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


def _iter_nodes(data):
    """Yield every dict-typed node from any nested JSON-LD structure."""
    if isinstance(data, dict):
        yield data
        # Recurse @graph if present
        if "@graph" in data and isinstance(data["@graph"], list):
            for child in data["@graph"]:
                yield from _iter_nodes(child)
    elif isinstance(data, list):
        for child in data:
            yield from _iter_nodes(child)


def extract_faq_jsonld(html_text: str):
    """Return list of (question, answer) tuples from any FAQPage JSON-LD."""
    out = []
    for match in JSON_LD_RE.finditer(html_text):
        raw = match.group(1).strip()
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            continue
        for item in _iter_nodes(data):
            t = item.get("@type")
            if t == "FAQPage" or (isinstance(t, list) and "FAQPage" in t):
                main = item.get("mainEntity", []) or []
                if isinstance(main, dict):
                    main = [main]
                for q in main:
                    if not isinstance(q, dict):
                        continue
                    name = q.get("name", "")
                    answer_obj = q.get("acceptedAnswer", {})
                    if isinstance(answer_obj, dict):
                        atext = answer_obj.get("text", "")
                    else:
                        atext = ""
                    out.append((name, atext))
    return out


def extract_html_faq(html_text: str):
    """
    Find visible FAQ block: look for <h2> with 'FAQ' or 'Häufige Fragen' or 'Fragen'
    then collect <details><summary>Q</summary>...A...</details> pairs OR
    <h3>Q</h3><p>A</p> pairs until next <h2>.
    """
    # Find FAQ section heading
    faq_heading_re = re.compile(
        r'<h2[^>]*>([^<]*(?:FAQ|Häufige Fragen|Fragen)[^<]*)</h2>',
        re.IGNORECASE,
    )
    m = faq_heading_re.search(html_text)
    if not m:
        return []
    start = m.end()
    # End at next <h2 or </section
    next_h2 = re.search(r"<h2|</section", html_text[start:], re.IGNORECASE)
    end = start + next_h2.start() if next_h2 else len(html_text)
    block = html_text[start:end]

    qa = []
    # Pattern 1: <details><summary>Q</summary>...A...</details>
    details_re = re.compile(
        r"<details[^>]*>\s*<summary[^>]*>(.*?)</summary>(.*?)</details>",
        re.DOTALL | re.IGNORECASE,
    )
    for dm in details_re.finditer(block):
        qa.append((dm.group(1), dm.group(2)))

    if qa:
        return qa

    # Pattern 2: <h3>Q</h3> followed by <p>A</p>
    h3_re = re.compile(r"<h3[^>]*>(.*?)</h3>(.*?)(?=<h3|$)", re.DOTALL | re.IGNORECASE)
    for hm in h3_re.finditer(block):
        qa.append((hm.group(1), hm.group(2)))

    return qa


def audit_city(city_dir: Path):
    idx = city_dir / "index.html"
    if not idx.exists():
        return None
    text = idx.read_text(encoding="utf-8", errors="replace")
    schema = extract_faq_jsonld(text)
    html_faq = extract_html_faq(text)

    res = {
        "city": city_dir.name,
        "schema_count": len(schema),
        "html_count": len(html_faq),
        "schema_questions": [normalize(q) for q, _ in schema],
        "html_questions": [normalize(q) for q, _ in html_faq],
        "schema_answers_chars": [len(normalize(a)) for _, a in schema],
        "html_answers_chars": [len(normalize(a)) for _, a in html_faq],
    }

    # Drift indicators
    res["count_mismatch"] = res["schema_count"] != res["html_count"]
    schema_qs = set(res["schema_questions"])
    html_qs = set(res["html_questions"])
    res["q_in_schema_only"] = sorted(schema_qs - html_qs)
    res["q_in_html_only"] = sorted(html_qs - schema_qs)
    res["drift"] = bool(
        res["count_mismatch"]
        or res["q_in_schema_only"]
        or res["q_in_html_only"]
    )
    return res


def main():
    rows = []
    for city in sorted(BESTATTER_DIR.iterdir()):
        if not city.is_dir():
            continue
        r = audit_city(city)
        if r is None:
            continue
        rows.append(r)

    drifted = [r for r in rows if r["drift"]]
    no_schema = [r for r in rows if r["schema_count"] == 0]
    no_html = [r for r in rows if r["html_count"] == 0 and r["schema_count"] > 0]

    print("FAQ-Schema-Drift-Audit\n" + "=" * 60)
    print(f"Total cities: {len(rows)}")
    print(f"With Schema FAQPage: {sum(1 for r in rows if r['schema_count'] > 0)}")
    print(f"With HTML FAQ: {sum(1 for r in rows if r['html_count'] > 0)}")
    print(f"DRIFTED: {len(drifted)}")
    print(f"NO SCHEMA at all: {len(no_schema)}")
    print(f"Schema but NO visible HTML FAQ: {len(no_html)}\n")

    print("Per-City Detail (drifted only):")
    print(
        f"{'City':<22}{'Schm':>5}{'Html':>5}{'OnlyS':>7}{'OnlyH':>7}  Verdict"
    )
    for r in drifted:
        verdict_parts = []
        if r["count_mismatch"]:
            verdict_parts.append(f"count {r['schema_count']}/{r['html_count']}")
        if r["q_in_schema_only"]:
            verdict_parts.append(f"+{len(r['q_in_schema_only'])} schema-only")
        if r["q_in_html_only"]:
            verdict_parts.append(f"+{len(r['q_in_html_only'])} html-only")
        verdict = ", ".join(verdict_parts)
        print(
            f"{r['city']:<22}{r['schema_count']:>5}{r['html_count']:>5}"
            f"{len(r['q_in_schema_only']):>7}{len(r['q_in_html_only']):>7}  {verdict}"
        )

    if no_schema:
        print("\nNO Schema FAQPage at all:")
        for r in no_schema:
            print(f"  - {r['city']} (html_faq_count={r['html_count']})")

    # JSON dump for downstream
    out_path = _HERE / "faq-drift-report.json"
    out_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nFull report written to {out_path}")


if __name__ == "__main__":
    main()
