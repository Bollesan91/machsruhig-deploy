#!/usr/bin/env python3
"""
Sitewide Health-Check
=====================
Konsolidiertes Audit über alle HTML-Pages:
- JSON-LD-Validität
- Asset-Pfade (CSS, JS, Fonts, Images)
- og:image-Existenz
- twitter:card-Coverage (bei Pages mit og:url)
- Schema.org @id-Referenz-Konsistenz
- Inline-Style oder valid externe CSS-Refs
- <h1>-Existenz
- Modul-Coverage (FAQ-Drift wird über faq-schema-drift.py separat erfasst)

Output: kurzer Konsolen-Report + optional --json.
"""
import json
import pathlib
import re
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]


def get_pages():
    pages = list(ROOT.glob("**/index.html")) + list(ROOT.glob("*.html"))
    return sorted(set(p for p in pages if "_dev" not in str(p) and ".git" not in str(p)))


def audit_jsonld(html):
    issues = []
    for m in re.finditer(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        html,
        re.DOTALL,
    ):
        try:
            json.loads(m.group(1).strip())
        except json.JSONDecodeError as e:
            issues.append(f"JSON-LD broken: {e}"[:80])
    return issues


def audit_assets(html, root):
    issues = []
    for m in re.finditer(
        r'(?:src|href)="(/[^"#?]+\.(?:png|jpg|jpeg|svg|webp|gif|css|js|woff2?))"',
        html,
    ):
        target = m.group(1)
        if not (root / target.lstrip("/")).exists():
            issues.append(f"asset missing: {target}")
    return issues


def audit_og(html, root):
    issues = []
    m = re.search(r'<meta\s+property="og:image"\s+content="([^"]+)"', html)
    if m:
        url = m.group(1).replace("https://machsruhig.de", "")
        if not (root / url.lstrip("/")).exists():
            issues.append(f"og:image missing: {url}")
    has_og_url = bool(re.search(r'<meta\s+property="og:url"', html))
    has_twitter = bool(re.search(r"twitter:card", html))
    if has_og_url and not has_twitter:
        issues.append("og:url ohne twitter:card")
    return issues


def audit_schema_refs(html):
    issues = []
    for m in re.finditer(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        html,
        re.DOTALL,
    ):
        try:
            data = json.loads(m.group(1).strip())
        except json.JSONDecodeError:
            continue
        defined = set()
        refs = []

        def walk(obj):
            if isinstance(obj, dict):
                if "@id" in obj and len(obj) > 1:
                    defined.add(obj["@id"])
                elif "@id" in obj and len(obj) == 1:
                    refs.append(obj["@id"])
                for k, v in obj.items():
                    if k != "@id":
                        walk(v)
            elif isinstance(obj, list):
                for item in obj:
                    walk(item)

        walk(data)
        for ref in refs:
            if ref not in defined and not (
                ref.startswith("https://machsruhig.de/#")
                or ref.startswith("https://machsruhig.de#")
            ):
                issues.append(f"unresolved @id ref: {ref}")
    return issues


def audit_html_hygiene(html):
    issues = []
    h1s = re.findall(r"<h1[^>]*>.*?</h1>", html, re.DOTALL)
    if not h1s:
        issues.append("no <h1>")
    elif len(h1s) > 1:
        issues.append(f"multi <h1> ({len(h1s)})")
    # imgs ohne alt
    img_no_alt = sum(1 for m in re.finditer(r"<img[^>]*>", html) if "alt=" not in m.group(0))
    if img_no_alt:
        issues.append(f"{img_no_alt} <img> ohne alt")
    # target=_blank ohne noopener
    for m in re.finditer(r'<a\s+[^>]*href="https?://[^"]+"[^>]*>', html):
        tag = m.group(0)
        if 'target="_blank"' in tag:
            rel = re.search(r'rel="([^"]+)"', tag)
            tokens = set(rel.group(1).split()) if rel else set()
            if "noopener" not in tokens and "noreferrer" not in tokens:
                issues.append("target=_blank ohne noopener")
                break
    return issues


def main():
    pages = get_pages()
    findings = defaultdict(list)
    for p in pages:
        rel = str(p.relative_to(ROOT))
        if p.name == "404.html":
            continue
        html = p.read_text(encoding="utf-8")
        for kind, fn in [
            ("jsonld", audit_jsonld),
            ("og", audit_og),
            ("schema_refs", audit_schema_refs),
            ("hygiene", audit_html_hygiene),
        ]:
            issues = fn(html) if kind not in ("og",) else fn(html, ROOT)
            if issues:
                findings[kind].extend((rel, i) for i in issues)
        a_issues = audit_assets(html, ROOT)
        if a_issues:
            findings["assets"].extend((rel, i) for i in a_issues)

    print(f"=== Sitewide Health-Check ({len(pages)-1} Pages, ohne 404.html) ===\n")
    totals = {k: len(v) for k, v in findings.items()}
    for k in ("jsonld", "assets", "og", "schema_refs", "hygiene"):
        n = totals.get(k, 0)
        print(f"{k:14}: {n} issues")
    print()
    for k, items in findings.items():
        if not items:
            continue
        print(f"--- {k} ---")
        for rel, msg in items[:15]:
            print(f"  {rel}: {msg}")
        if len(items) > 15:
            print(f"  ... +{len(items)-15} more")
        print()

    if "--json" in sys.argv:
        out_path = ROOT / "_dev" / "audit" / "sitewide-health-report.json"
        out_path.write_text(
            json.dumps(
                {k: [{"file": f, "msg": m} for f, m in v] for k, v in findings.items()},
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"Report: {out_path.relative_to(ROOT)}")

    return 0 if sum(totals.values()) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
