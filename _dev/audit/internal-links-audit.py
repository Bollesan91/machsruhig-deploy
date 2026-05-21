#!/usr/bin/env python3
"""
Internal-Links-Audit
====================
Findet broken interne Links sitewide.

Logik:
- Sammelt alle href="..." Werte aus HTML-Pages.
- Filtert externe (http(s)://, mailto:, tel:, anchor #...).
- Normalisiert Ziele (relativ → absolut, trailing slash, query/fragment strippen).
- Berücksichtigt _redirects-Regeln (alte → neue Pfade).
- Berücksichtigt Pretty-URLs:
    /foo          → foo.html ODER foo/index.html
    /foo/         → foo/index.html
    /foo.html     → foo.html
- Existiert kein Ziel, gilt der Link als broken.

Output:
- Konsolen-Report mit Aggregation pro Ziel + Pages mit Verweis.
- Optional --json schreibt _dev/audit/internal-links-report.json.
"""
import json
import pathlib
import re
import sys
from collections import defaultdict
from urllib.parse import urlsplit, unquote

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITE_HOST_PREFIXES = ("https://machsruhig.de", "http://machsruhig.de")


def get_pages():
    pages = list(ROOT.glob("**/index.html")) + list(ROOT.glob("*.html"))
    return sorted(
        set(
            p
            for p in pages
            if "_dev" not in str(p)
            and ".git" not in str(p)
            and "templates" not in str(p)
            and "/archiv/" not in str(p)
        )
    )


def parse_redirects(redirects_path: pathlib.Path):
    """Returns dict[from_path] -> to_path (without trailing slash, leading /)."""
    rules = {}
    if not redirects_path.exists():
        return rules
    for line in redirects_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        src, dst = parts[0], parts[1]
        rules[src.rstrip("/") or "/"] = dst.rstrip("/") or "/"
    return rules


def candidate_fs_paths(path: str, root: pathlib.Path):
    """For URL path /foo or /foo/ returns possible filesystem paths."""
    if not path or path == "/":
        return [root / "index.html"]
    p = path.lstrip("/")
    cands = []
    # Trailing slash → only dir/index.html
    if path.endswith("/"):
        cands.append(root / p / "index.html")
    else:
        # Try literal file first (could end with .html)
        cands.append(root / p)
        if not p.endswith(".html"):
            cands.append(root / (p + ".html"))
        cands.append(root / p / "index.html")
    return cands


def exists_as_page(url_path: str, root: pathlib.Path, redirects: dict) -> bool:
    if any((c).exists() for c in candidate_fs_paths(url_path, root)):
        return True
    # Try redirect resolution (single hop is enough for our table).
    key = url_path.rstrip("/") or "/"
    if key in redirects:
        target = redirects[key]
        if any((c).exists() for c in candidate_fs_paths(target, root)):
            return True
        # Also try with trailing slash
        if any((c).exists() for c in candidate_fs_paths(target + "/", root)):
            return True
    return False


def extract_links(html: str):
    """Yield (href_raw, context_tag) tuples — href values from <a ... href="...">."""
    for m in re.finditer(r'<a\s+[^>]*href="([^"]+)"[^>]*>', html, re.IGNORECASE):
        yield m.group(1)


def normalize_to_path(href: str, current_page_url: str) -> str | None:
    """Returns the URL-path component for an internal link, or None if external/non-page."""
    h = href.strip()
    if not h:
        return None
    if h.startswith("#"):
        return None
    if h.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None
    # Absolute URL — only count machsruhig.de as internal
    if h.startswith("http://") or h.startswith("https://"):
        if not any(h.startswith(pre) for pre in SITE_HOST_PREFIXES):
            return None
        parsed = urlsplit(h)
        path = parsed.path or "/"
    elif h.startswith("/"):
        parsed = urlsplit(h)
        path = parsed.path
    else:
        # Relative — resolve against current page's directory
        base_dir = current_page_url.rsplit("/", 1)[0] + "/"
        # naive join
        joined = base_dir + h
        parts = []
        for seg in joined.split("/"):
            if seg == "..":
                if parts:
                    parts.pop()
            elif seg in ("", "."):
                continue
            else:
                parts.append(seg)
        path = "/" + "/".join(parts)
        parsed = urlsplit(path)
        path = parsed.path

    path = unquote(path)
    # Strip fragment/query already handled by urlsplit
    return path


def page_url_path(p: pathlib.Path) -> str:
    rel = p.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def main():
    pages = get_pages()
    redirects = parse_redirects(ROOT / "_redirects")

    broken_by_target = defaultdict(list)  # target → [(page, href_raw)]
    total_links = 0
    for p in pages:
        try:
            html = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        page_url = page_url_path(p)
        rel_page = str(p.relative_to(ROOT))
        for href in extract_links(html):
            total_links += 1
            target = normalize_to_path(href, page_url)
            if target is None:
                continue
            # Skip empty or self-anchor-only after normalization
            if not target:
                continue
            if exists_as_page(target, ROOT, redirects):
                continue
            broken_by_target[target].append((rel_page, href))

    pages_affected = {pg for refs in broken_by_target.values() for pg, _ in refs}

    print(f"=== Internal-Links-Audit ===")
    print(f"Pages gescannt:       {len(pages)}")
    print(f"Interne Links total:  {total_links}")
    print(f"Broken Targets:       {len(broken_by_target)}")
    print(f"Pages mit broken Lnk: {len(pages_affected)}")
    print()

    # Sort by frequency desc
    for target, refs in sorted(
        broken_by_target.items(), key=lambda kv: -len(kv[1])
    ):
        print(f"--- {target}  ({len(refs)} Vorkommen)")
        seen_pages = set()
        for pg, href in refs:
            if pg in seen_pages:
                continue
            seen_pages.add(pg)
            print(f"    {pg}    [{href}]")
        print()

    if "--json" in sys.argv:
        out_path = ROOT / "_dev" / "audit" / "internal-links-report.json"
        out_path.write_text(
            json.dumps(
                {
                    "summary": {
                        "pages_scanned": len(pages),
                        "internal_links_total": total_links,
                        "broken_targets": len(broken_by_target),
                        "pages_affected": len(pages_affected),
                    },
                    "broken": {
                        t: [{"page": pg, "href": h} for pg, h in refs]
                        for t, refs in broken_by_target.items()
                    },
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"Report: {out_path.relative_to(ROOT)}")

    return 0 if not broken_by_target else 1


if __name__ == "__main__":
    sys.exit(main())
