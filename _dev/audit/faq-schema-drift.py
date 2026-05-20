#!/usr/bin/env python3
"""
FAQ-Schema-Drift-Audit
======================
Vergleicht JSON-LD FAQPage Entries mit dem sichtbaren HTML-FAQ-Block
(<details><summary>…</summary><div class="faq-answer">…</div></details>)
auf allen Stadt-Pages (/bestatter/*/index.html).

Findet:
- COUNT  : unterschiedliche Anzahl Q/A
- Q_TEXT : Question-Name in JSON-LD ≠ <summary>-Text in HTML
- A_TEXT : Answer-Text in JSON-LD ≠ <div class="faq-answer">-Text in HTML
- NO_LD  : keine FAQPage im JSON-LD
- NO_HTML: kein sichtbarer FAQ-Block
- CLEAN  : voller Match

Output: Markdown-Report + JSON-Dump für Folge-Fixes.
"""

import json
import re
import sys
import unicodedata
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CITIES_DIR = ROOT / "bestatter"
REPORT_MD = ROOT / "_dev" / "audit" / "faq-schema-drift-report.md"
REPORT_JSON = ROOT / "_dev" / "audit" / "faq-schema-drift-report.json"


def normalize(text: str) -> str:
    """Normalize for comparison: strip tags, collapse whitespace, NFC, drop typo-graphic noise."""
    text = unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = unicodedata.normalize("NFC", text)
    # Vereinheitliche typografische Anführungszeichen / Gedankenstriche für Vergleich
    text = text.replace("»", '"').replace("«", '"')
    text = text.replace("„", '"').replace("“", '"').replace("”", '"')
    text = text.replace("‚", "'").replace("‘", "'").replace("’", "'")
    text = text.replace("—", "-").replace("–", "-")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_jsonld_faq(html: str):
    """Findet alle FAQPage-Einträge in <script type="application/ld+json"> Blöcken."""
    faqs = []
    for m in re.finditer(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        html,
        re.DOTALL,
    ):
        raw = m.group(1).strip()
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            continue
        for node in iter_graph(data):
            if isinstance(node, dict) and node.get("@type") == "FAQPage":
                me = node.get("mainEntity", [])
                if isinstance(me, dict):
                    me = [me]
                for q in me:
                    if not isinstance(q, dict):
                        continue
                    name = q.get("name", "")
                    ans = q.get("acceptedAnswer", {})
                    text = ans.get("text", "") if isinstance(ans, dict) else ""
                    faqs.append({"q": name, "a": text})
    return faqs


def iter_graph(data):
    """Yield top-level node + alle @graph-Einträge."""
    if isinstance(data, dict):
        yield data
        graph = data.get("@graph")
        if isinstance(graph, list):
            yield from graph
    elif isinstance(data, list):
        for item in data:
            yield from iter_graph(item)


FAQ_HEADER_RE = re.compile(
    r"<h2[^>]*>\s*(?:[^<]*?)(?:FAQ|Häufig|H&auml;ufig|Fragen)[^<]*?</h2>",
    re.IGNORECASE | re.DOTALL,
)


def extract_html_faq(html: str):
    """Findet sichtbare FAQ-Blöcke. Strikt: nur <details> innerhalb einer Section,
    die mit einem FAQ-Header (<h2>…FAQ|Häufig|Fragen…</h2>) beginnt.

    Stützt zwei Antwort-Stile:
    1. mr-faq-Wrapper mit <div class="faq-answer">…</div>
    2. plain <details><summary>…</summary><p|div>…</p|div></details>

    Filtert: <details class="…mr-nav-mobile…"> und ähnliche Nav-Elemente.
    """
    faqs = []
    headers = list(FAQ_HEADER_RE.finditer(html))
    if not headers:
        return faqs

    # Bestimme FAQ-Bereich(e): von jedem FAQ-Header bis zum nächsten <h2> oder </section>
    spans = []
    for i, h in enumerate(headers):
        start = h.end()
        end_h2 = re.search(r"<h2[^>]*>", html[start:])
        end_sect = re.search(r"</section\b", html[start:])
        candidates = [c.start() for c in [end_h2, end_sect] if c]
        end = start + min(candidates) if candidates else len(html)
        spans.append((start, end))

    for start, end in spans:
        region = html[start:end]
        # Stil A: <details><summary>…</summary>…</details>
        for det in re.finditer(
            r"<details([^>]*)>\s*<summary[^>]*>(.*?)</summary>\s*(.*?)</details>",
            region,
            re.DOTALL,
        ):
            attrs = det.group(1) or ""
            if re.search(r"mr-nav-mobile|nav-mobile|class=[\"'][^\"']*nav", attrs):
                continue
            q = det.group(2).strip()
            if q in {"☰", "&#9776;"} or len(q) <= 3:
                continue
            body = det.group(3).strip()
            inner = re.search(
                r'<div\s+class="faq-answer"[^>]*>(.*?)</div>',
                body,
                re.DOTALL,
            )
            a = inner.group(1).strip() if inner else body
            faqs.append({"q": q, "a": a})
        if faqs:
            continue
        # Stil B (fallback): <div class="mr-faq__item|faq-item"><h3>…</h3><p>…</p></div>
        for item in re.finditer(
            r'<div\s+class="(?:mr-faq__item|faq-item)"[^>]*>\s*<h3[^>]*>(.*?)</h3>\s*(.*?)</div>',
            region,
            re.DOTALL,
        ):
            q = item.group(1).strip()
            a = item.group(2).strip()
            faqs.append({"q": q, "a": a})
    return faqs


def compare(ld, html_list):
    """Vergleicht JSON-LD-FAQs vs HTML-FAQs. Gibt Liste von Issues zurück."""
    issues = []
    if len(ld) != len(html_list):
        issues.append(
            {
                "type": "COUNT",
                "ld_count": len(ld),
                "html_count": len(html_list),
            }
        )
    for i, (ld_q, html_q) in enumerate(zip(ld, html_list)):
        nq_ld = normalize(ld_q["q"])
        nq_html = normalize(html_q["q"])
        na_ld = normalize(ld_q["a"])
        na_html = normalize(html_q["a"])
        if nq_ld != nq_html:
            issues.append(
                {
                    "type": "Q_TEXT",
                    "index": i,
                    "ld": ld_q["q"],
                    "html": html_q["q"],
                }
            )
        if na_ld != na_html:
            issues.append(
                {
                    "type": "A_TEXT",
                    "index": i,
                    "question": ld_q["q"],
                    "ld_preview": ld_q["a"][:200],
                    "html_preview": html_q["a"][:200],
                }
            )
    return issues


def audit_city(city_dir: Path):
    index = city_dir / "index.html"
    if not index.exists():
        return None
    html = index.read_text(encoding="utf-8")
    ld = extract_jsonld_faq(html)
    html_faq = extract_html_faq(html)

    result = {
        "city": city_dir.name,
        "ld_count": len(ld),
        "html_count": len(html_faq),
        "ld": ld,
        "html": html_faq,
        "issues": [],
        "status": "CLEAN",
    }
    if not ld and not html_faq:
        result["status"] = "NO_FAQ"
        return result
    if not ld:
        result["status"] = "NO_LD"
        result["issues"].append({"type": "NO_LD"})
        return result
    if not html_faq:
        result["status"] = "NO_HTML"
        result["issues"].append({"type": "NO_HTML"})
        return result

    issues = compare(ld, html_faq)
    if issues:
        result["status"] = "DRIFT"
        result["issues"] = issues
    return result


def main():
    if not CITIES_DIR.is_dir():
        print(f"FATAL: {CITIES_DIR} nicht gefunden", file=sys.stderr)
        sys.exit(1)

    skip = {"index.html"}  # Umlaut-Duplikate (lübeck, mönchengladbach) bewusst NICHT skippen:
                            # sie sind aktive Pages ohne noindex, müssen drift-frei bleiben.

    results = []
    for city_dir in sorted(CITIES_DIR.iterdir()):
        if not city_dir.is_dir():
            continue
        if city_dir.name in skip:
            continue
        r = audit_city(city_dir)
        if r:
            results.append(r)

    # Markdown-Report
    drift = [r for r in results if r["status"] == "DRIFT"]
    no_ld = [r for r in results if r["status"] == "NO_LD"]
    no_html = [r for r in results if r["status"] == "NO_HTML"]
    no_faq = [r for r in results if r["status"] == "NO_FAQ"]
    clean = [r for r in results if r["status"] == "CLEAN"]

    lines = []
    lines.append("# FAQ-Schema-Drift-Audit")
    lines.append("")
    lines.append(f"**Stand:** {Path(__file__).name} — alle Stadt-Pages")
    lines.append("")
    lines.append("## Zusammenfassung")
    lines.append("")
    lines.append(f"- **Total Cities:** {len(results)}")
    lines.append(f"- **CLEAN:** {len(clean)}")
    lines.append(f"- **DRIFT:** {len(drift)}")
    lines.append(f"- **NO_LD (HTML ohne JSON-LD FAQPage):** {len(no_ld)}")
    lines.append(f"- **NO_HTML (JSON-LD ohne HTML-Block):** {len(no_html)}")
    lines.append(f"- **NO_FAQ (gar keine FAQ):** {len(no_faq)}")
    lines.append("")

    if drift:
        lines.append("## DRIFT (JSON-LD ≠ HTML)")
        lines.append("")
        for r in drift:
            lines.append(f"### {r['city']}  (LD={r['ld_count']}, HTML={r['html_count']})")
            lines.append("")
            for issue in r["issues"]:
                if issue["type"] == "COUNT":
                    lines.append(
                        f"- **COUNT-Mismatch:** JSON-LD hat {issue['ld_count']} Q/A, HTML hat {issue['html_count']}"
                    )
                elif issue["type"] == "Q_TEXT":
                    lines.append(f"- **Q_TEXT[{issue['index']}]**")
                    lines.append(f"  - LD:   `{issue['ld']}`")
                    lines.append(f"  - HTML: `{issue['html']}`")
                elif issue["type"] == "A_TEXT":
                    lines.append(f"- **A_TEXT[{issue['index']}]** — {issue['question']}")
                    lines.append(f"  - LD:   `{issue['ld_preview']}…`")
                    lines.append(f"  - HTML: `{issue['html_preview']}…`")
            lines.append("")

    if no_ld:
        lines.append("## NO_LD (HTML-FAQ ohne JSON-LD FAQPage)")
        lines.append("")
        for r in no_ld:
            lines.append(f"- {r['city']} (HTML={r['html_count']})")
        lines.append("")

    if no_html:
        lines.append("## NO_HTML (JSON-LD FAQPage ohne sichtbaren HTML-Block)")
        lines.append("")
        for r in no_html:
            lines.append(f"- {r['city']} (LD={r['ld_count']})")
        lines.append("")

    if no_faq:
        lines.append("## NO_FAQ (keine FAQ-Sektion)")
        lines.append("")
        for r in no_faq:
            lines.append(f"- {r['city']}")
        lines.append("")

    if clean:
        lines.append("## CLEAN")
        lines.append("")
        lines.append(", ".join(r["city"] for r in clean))
        lines.append("")

    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")

    # JSON-Dump
    REPORT_JSON.write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Stdout-Summary
    print(f"Total Cities  : {len(results)}")
    print(f"CLEAN         : {len(clean)}")
    print(f"DRIFT         : {len(drift)}  -> {', '.join(r['city'] for r in drift) or '-'}")
    print(f"NO_LD         : {len(no_ld)}  -> {', '.join(r['city'] for r in no_ld) or '-'}")
    print(f"NO_HTML       : {len(no_html)}  -> {', '.join(r['city'] for r in no_html) or '-'}")
    print(f"NO_FAQ        : {len(no_faq)}  -> {', '.join(r['city'] for r in no_faq) or '-'}")
    print()
    print(f"Report: {REPORT_MD.relative_to(ROOT)}")
    print(f"JSON  : {REPORT_JSON.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
