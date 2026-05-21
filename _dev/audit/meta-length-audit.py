#!/usr/bin/env python3
"""
meta-length-audit.py
====================
Walks all URLs in sitemap.xml, resolves each to a local HTML file,
extracts <title>, <meta name="description">, og:title, og:description,
twitter:title, twitter:description and reports lengths.

Flags:
  - title > 65 (target)  / Google trunkiert ~60-70
  - description > 165 (target) / Google trunkiert ~150-170

Pages with <meta name="robots" content="*noindex*"> are flagged and skipped
in the "fix" recommendation set.

Outputs a Markdown report to _dev/audit/meta-length-report.md
"""

from __future__ import annotations
import os
import re
import sys
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parent.parent.parent
SITEMAP = REPO / "sitemap.xml"
REPORT = REPO / "_dev" / "audit" / "meta-length-report.md"

TITLE_MAX = 65
DESC_MAX = 165

NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def url_to_path(url: str) -> Path | None:
    """Map https://machsruhig.de/<path> to a local file."""
    base = "https://machsruhig.de"
    if not url.startswith(base):
        return None
    rel = unquote(url[len(base):])
    if rel == "" or rel == "/":
        return REPO / "index.html"
    # strip leading slash
    rel = rel.lstrip("/")
    # if trailing slash → directory index
    if rel.endswith("/"):
        return REPO / rel / "index.html"
    # try as file
    p_html = REPO / (rel + ".html")
    if p_html.exists():
        return p_html
    p_dir = REPO / rel / "index.html"
    if p_dir.exists():
        return p_dir
    p_direct = REPO / rel
    if p_direct.exists() and p_direct.is_file():
        return p_direct
    return None


TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
META_RE = re.compile(
    r'<meta\s+([^>]*?)/?>', re.I
)


def parse_meta(html: str) -> dict:
    """Return dict with title, description, og:title, og:description,
    twitter:title, twitter:description, robots, lengths."""
    out: dict = {}
    m = TITLE_RE.search(html)
    out["title"] = m.group(1).strip() if m else None

    # walk meta tags
    metas = {}
    for match in META_RE.finditer(html):
        attrs_raw = match.group(1)
        # parse name/property + content
        nm = re.search(r'\b(name|property)\s*=\s*"([^"]+)"', attrs_raw, re.I)
        ct = re.search(r'\bcontent\s*=\s*"([^"]*)"', attrs_raw, re.I)
        if nm and ct:
            metas[nm.group(2).lower()] = ct.group(1)
    out["description"] = metas.get("description")
    out["og_title"] = metas.get("og:title")
    out["og_description"] = metas.get("og:description")
    out["twitter_title"] = metas.get("twitter:title")
    out["twitter_description"] = metas.get("twitter:description")
    out["robots"] = metas.get("robots")
    return out


def load_sitemap_urls() -> list[str]:
    tree = ET.parse(SITEMAP)
    root = tree.getroot()
    urls = []
    for u in root.findall("sm:url", NS):
        loc = u.find("sm:loc", NS)
        if loc is not None and loc.text:
            urls.append(loc.text.strip())
    return urls


def main():
    urls = load_sitemap_urls()
    rows = []
    for url in urls:
        path = url_to_path(url)
        if path is None or not path.exists():
            rows.append({"url": url, "path": None, "error": "missing"})
            continue
        html = path.read_text(encoding="utf-8", errors="replace")
        meta = parse_meta(html)
        t_len = len(meta["title"]) if meta["title"] else 0
        d_len = len(meta["description"]) if meta["description"] else 0
        noindex = bool(meta["robots"] and "noindex" in meta["robots"].lower())
        rows.append({
            "url": url,
            "path": str(path.relative_to(REPO)),
            "title": meta["title"],
            "title_len": t_len,
            "description": meta["description"],
            "desc_len": d_len,
            "og_title": meta["og_title"],
            "og_description": meta["og_description"],
            "twitter_title": meta["twitter_title"],
            "twitter_description": meta["twitter_description"],
            "robots": meta["robots"],
            "noindex": noindex,
        })

    title_long = [r for r in rows if r.get("title_len", 0) > TITLE_MAX]
    desc_long = [r for r in rows if r.get("desc_len", 0) > DESC_MAX]
    title_long_idx = [r for r in title_long if not r.get("noindex")]
    desc_long_idx = [r for r in desc_long if not r.get("noindex")]

    lines: list[str] = []
    lines.append("# Meta-Length Audit")
    lines.append("")
    lines.append(f"- Targets: title ≤ {TITLE_MAX} chars, description ≤ {DESC_MAX} chars")
    lines.append(f"- URLs in sitemap: **{len(rows)}**")
    lines.append(f"- Titles too long: **{len(title_long)}** "
                 f"(davon indexierbar: {len(title_long_idx)})")
    lines.append(f"- Descriptions too long: **{len(desc_long)}** "
                 f"(davon indexierbar: {len(desc_long_idx)})")
    lines.append("")

    lines.append("## Titles > {} chars".format(TITLE_MAX))
    lines.append("")
    lines.append("| Len | noindex | File | Current Title |")
    lines.append("|---:|:---:|---|---|")
    for r in sorted(title_long, key=lambda x: -x["title_len"]):
        nx = "yes" if r["noindex"] else ""
        lines.append(f"| {r['title_len']} | {nx} | `{r['path']}` | {r['title']} |")
    lines.append("")

    lines.append("## Descriptions > {} chars".format(DESC_MAX))
    lines.append("")
    lines.append("| Len | noindex | File | Current Description |")
    lines.append("|---:|:---:|---|---|")
    for r in sorted(desc_long, key=lambda x: -x["desc_len"]):
        nx = "yes" if r["noindex"] else ""
        lines.append(f"| {r['desc_len']} | {nx} | `{r['path']}` | {r['description']} |")
    lines.append("")

    # missing pages
    missing = [r for r in rows if r.get("error") == "missing"]
    if missing:
        lines.append("## Missing local files (sitemap URL → no file)")
        for r in missing:
            lines.append(f"- {r['url']}")
        lines.append("")

    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written → {REPORT.relative_to(REPO)}")
    print(f"  titles > {TITLE_MAX}: {len(title_long)} ({len(title_long_idx)} indexierbar)")
    print(f"  descs  > {DESC_MAX}: {len(desc_long)} ({len(desc_long_idx)} indexierbar)")

    # also dump JSON for tooling
    json_path = REPORT.with_suffix(".json")
    json_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
