"""
Komplettes Website-Audit — heatmap + tech-health + trust + lead/conversion.
Liefert JSON-Report + Markdown-Summary.
"""
import os
import re
import json
import html
from pathlib import Path
from collections import defaultdict

ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent
BESTATTER = ROOT / "bestatter"
BL_DIR = ROOT / "bestattung-in"

# ---------- Helpers ----------
JSON_LD_RE = re.compile(
    r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)
META_NOINDEX = re.compile(r'<meta[^>]*name="robots"[^>]*content="[^"]*noindex', re.IGNORECASE)
META_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.DOTALL | re.IGNORECASE)
META_DESC = re.compile(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', re.IGNORECASE)
CANONICAL = re.compile(r'<link[^>]*rel="canonical"[^>]*href="([^"]*)"', re.IGNORECASE)
OG_IMAGE = re.compile(r'<meta[^>]*property="og:image"', re.IGNORECASE)

H2_RE = re.compile(r"<h2[^>]*>(.*?)</h2>", re.DOTALL | re.IGNORECASE)
H3_RE = re.compile(r"<h3[^>]*>(.*?)</h3>", re.DOTALL | re.IGNORECASE)
INTERNAL_LINK_RE = re.compile(r'href="(/[^"#?]*)"')
EXTERNAL_LINK_RE = re.compile(r'href="(https?://[^"]*)"')

def strip_html(s):
    return re.sub(r"<[^>]+>", "", s).strip()


def audit_module_score(text):
    """Score 0-7 for 7 must-have modules."""
    score = 0
    missing = []
    h2s = [strip_html(h) for h in H2_RE.findall(text)]
    h2s_low = " || ".join(h2s).lower()
    text_low = text.lower()

    # 1. Akutbox / Todesfall-Schritte
    if any(k in h2s_low for k in ["todesfall", "akut", "nach einem todes", "erste schritte"]) or "akutbox" in text_low:
        score += 1
    else:
        missing.append("Akutbox")

    # 2. Kosten + Euro
    if "kosten" in h2s_low and re.search(r"\d+[.,]?\d*\s*€", text):
        score += 1
    else:
        missing.append("Kosten")

    # 3. Bestatter-Wahl
    if any(k in h2s_low for k in ["bestatter-wahl", "bestatter wählen", "bestatter w"]) or "bestatter-wahl" in text_low:
        score += 1
    else:
        missing.append("BestWahl")

    # 4. Sozialbestattung + § 74
    if "sozialbestattung" in h2s_low and "§ 74" in text:
        score += 1
    else:
        missing.append("Sozial")

    # 5. FAQ — h2 Häufige Fragen + ≥5 details/h3
    if "häufige fragen" in h2s_low or "faq" in h2s_low:
        # Count details summaries or h3 within the FAQ block
        m = re.search(r"<h2[^>]*>[^<]*(?:Häufige Fragen|FAQ)[^<]*</h2>(.*?)(?=<h2|$)", text, re.DOTALL | re.IGNORECASE)
        if m:
            block = m.group(1)
            qa_count = len(re.findall(r"<details", block, re.IGNORECASE)) + len(re.findall(r"<h3[^>]*>", block, re.IGNORECASE))
            if qa_count >= 5:
                score += 1
            else:
                missing.append(f"FAQ(only {qa_count})")
        else:
            missing.append("FAQ(noblock)")
    else:
        missing.append("FAQ")

    # 6. Quellen
    if "quellen" in h2s_low and "<ul" in text_low:
        score += 1
    else:
        missing.append("Quellen")

    # 7. Friedhof-Profile: ≥3 h3 mit "friedhof" oder genug Friedhof-Detail-Sections
    fhf_h3s = [h for h in H3_RE.findall(text) if "friedhof" in strip_html(h).lower() or "krematorium" in strip_html(h).lower()]
    if len(fhf_h3s) >= 3:
        score += 1
    else:
        missing.append(f"Fhf-Profile({len(fhf_h3s)})")

    return score, missing


def audit_one(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    size_kb = len(text.encode("utf-8")) / 1024.0

    # Score
    score, missing = audit_module_score(text)

    # Schema
    scripts = JSON_LD_RE.findall(text)
    schema_valid = 0
    schema_total = len(scripts)
    schema_types = set()
    for s in scripts:
        try:
            d = json.loads(s.strip())
            schema_valid += 1
            for n in _iter_nodes(d):
                t = n.get("@type")
                if isinstance(t, str):
                    schema_types.add(t)
                elif isinstance(t, list):
                    schema_types.update(t)
        except json.JSONDecodeError:
            pass

    # Meta
    title_m = META_TITLE.search(text)
    title = strip_html(title_m.group(1)) if title_m else ""
    desc_m = META_DESC.search(text)
    desc = desc_m.group(1) if desc_m else ""
    canon = CANONICAL.search(text).group(1) if CANONICAL.search(text) else ""
    og_img = bool(OG_IMAGE.search(text))
    noindex = bool(META_NOINDEX.search(text))

    # Internal links
    int_links = set(INTERNAL_LINK_RE.findall(text))

    # Encoding bugs
    body_match = re.search(r"<body[^>]*>(.*?)</body>", text, re.DOTALL | re.IGNORECASE)
    body = body_match.group(1) if body_match else text
    entity_bugs = len(re.findall(r"&[aou]uml;|&szlig;|&Auml;|&Ouml;|&Uuml;", body))

    # Trust signals
    has_stand = bool(re.search(r"Stand:?\s*\d|Stand der Daten", text))
    has_methodik = "methodik" in text.lower() or "redaktion machsruhig" in text.lower()
    has_author_block = bool(re.search(r'<div class="mr-article-meta"', text))

    # CTAs
    has_kostenrechner_cta = "/tools/bestattungskosten-rechner" in text or "Kostenrechner" in text
    has_planer_cta = "/beerdigung-planen" in text or "Planer" in text
    has_lead_form = bool(re.search(r"<form[^>]*", text))

    # Affiliate
    has_affiliate = bool(re.search(r"check24|dela|solidar|afilio|smartlaw|sterbegeld", text, re.IGNORECASE))

    return dict(
        path=str(path.relative_to(ROOT)),
        slug=path.parent.name,
        size_kb=round(size_kb, 1),
        score=score,
        missing=missing,
        schema_valid=schema_valid,
        schema_total=schema_total,
        schema_types=sorted(schema_types),
        title=title,
        title_len=len(title),
        desc_len=len(desc),
        canonical=canon,
        og_img=og_img,
        noindex=noindex,
        internal_link_count=len(int_links),
        entity_bugs=entity_bugs,
        has_stand=has_stand,
        has_methodik=has_methodik,
        has_author_block=has_author_block,
        has_kostenrechner_cta=has_kostenrechner_cta,
        has_planer_cta=has_planer_cta,
        has_lead_form=has_lead_form,
        has_affiliate=has_affiliate,
    )


def _iter_nodes(data):
    if isinstance(data, dict):
        yield data
        if "@graph" in data and isinstance(data["@graph"], list):
            for c in data["@graph"]:
                yield from _iter_nodes(c)
    elif isinstance(data, list):
        for c in data:
            yield from _iter_nodes(c)


# ---------- Run ----------

city_results = []
for d in sorted(BESTATTER.iterdir()):
    if not d.is_dir():
        continue
    idx = d / "index.html"
    if not idx.exists():
        continue
    city_results.append(audit_one(idx))

bl_results = []
if BL_DIR.exists():
    for d in sorted(BL_DIR.iterdir()):
        if not d.is_dir():
            continue
        idx = d / "index.html"
        if not idx.exists():
            continue
        bl_results.append(audit_one(idx))

# ---------- Aggregate ----------
# Score distribution
score_dist = defaultdict(list)
for r in city_results:
    score_dist[r["score"]].append(r["slug"])

# Missing module frequency
missing_freq = defaultdict(int)
for r in city_results:
    for m in r["missing"]:
        # Normalize FAQ variants
        key = m.split("(")[0]
        missing_freq[key] += 1

# Schema-health
broken_schema = [r for r in city_results if r["schema_valid"] != r["schema_total"]]
no_schema = [r for r in city_results if r["schema_total"] == 0]

# Entity bugs
entity_pages = [r for r in city_results if r["entity_bugs"] > 0]

# CTA / Lead
no_kostenrechner_cta = [r["slug"] for r in city_results if not r["has_kostenrechner_cta"]]
no_planer_cta = [r["slug"] for r in city_results if not r["has_planer_cta"]]
no_lead_form = [r["slug"] for r in city_results if not r["has_lead_form"]]
no_affiliate = [r["slug"] for r in city_results if not r["has_affiliate"]]

# Trust
no_stand = [r["slug"] for r in city_results if not r["has_stand"]]
no_author = [r["slug"] for r in city_results if not r["has_author_block"]]

# Title/Desc length issues
long_title = [(r["slug"], r["title_len"]) for r in city_results if r["title_len"] > 60]
short_desc = [(r["slug"], r["desc_len"]) for r in city_results if r["desc_len"] < 120]
long_desc = [(r["slug"], r["desc_len"]) for r in city_results if r["desc_len"] > 160]

# Duplicates
title_groups = defaultdict(list)
for r in city_results:
    title_groups[r["title"]].append(r["slug"])
dup_titles = {t: s for t, s in title_groups.items() if len(s) > 1}

# Sizes
sizes = sorted(city_results, key=lambda r: r["size_kb"], reverse=True)
top5_largest = [(r["slug"], r["size_kb"]) for r in sizes[:5]]
bot5_smallest = [(r["slug"], r["size_kb"]) for r in sizes[-5:]]

# noindex
noindex_pages = [r["slug"] for r in city_results if r["noindex"]]

# ---------- Output ----------
print("=" * 70)
print(f"AUDIT-REPORT — {len(city_results)} Stadt-Pages + {len(bl_results)} BL-Pages")
print("=" * 70)

print(f"\n## Score-Verteilung (Stadt-Pages)")
for s in sorted(score_dist.keys(), reverse=True):
    print(f"  {s}/7: {len(score_dist[s]):2}  — {', '.join(score_dist[s][:8])}{'...' if len(score_dist[s])>8 else ''}")

print(f"\n## Modul-Lücken (häufigkeit)")
for m, c in sorted(missing_freq.items(), key=lambda x: -x[1]):
    print(f"  {m:<14} fehlt in {c:2}/{len(city_results)}")

print(f"\n## Schema-Health")
print(f"  Valid/Total Scripts: total {sum(r['schema_valid'] for r in city_results)}/{sum(r['schema_total'] for r in city_results)}")
print(f"  Pages mit broken JSON-LD: {len(broken_schema)}")
print(f"  Pages ohne JSON-LD: {len(no_schema)}")

print(f"\n## Entity-Bugs (HTML-Entities in Body)")
print(f"  Pages mit &auml;/&uuml;/etc: {len(entity_pages)}")
for r in entity_pages[:5]:
    print(f"    - {r['slug']}: {r['entity_bugs']} entities")

print(f"\n## CTA / Lead-Gen Lücken")
print(f"  Pages ohne Kostenrechner-CTA: {len(no_kostenrechner_cta)} / {len(city_results)}")
print(f"  Pages ohne Planer-CTA: {len(no_planer_cta)} / {len(city_results)}")
print(f"  Pages ohne <form>: {len(no_lead_form)} / {len(city_results)}")
print(f"  Pages ohne Affiliate-Hint: {len(no_affiliate)} / {len(city_results)}")

print(f"\n## Trust / E-E-A-T")
print(f"  Pages ohne Stand-Datum: {len(no_stand)}")
print(f"  Pages ohne mr-article-meta Block: {len(no_author)}")

print(f"\n## Meta-Hygiene")
print(f"  Titles >60 Zeichen: {len(long_title)}")
for s, n in long_title[:5]:
    print(f"    - {s}: {n}")
print(f"  Descriptions <120: {len(short_desc)}")
print(f"  Descriptions >160: {len(long_desc)}")
print(f"  Duplicate Titles: {len(dup_titles)}")
for t, slugs in list(dup_titles.items())[:3]:
    print(f"    - {slugs}: '{t[:60]}'")

print(f"\n## Page Sizes")
print(f"  Largest 5:")
for s, kb in top5_largest:
    print(f"    {s}: {kb} KB")
print(f"  Smallest 5:")
for s, kb in bot5_smallest:
    print(f"    {s}: {kb} KB")

print(f"\n## noindex-Pages: {len(noindex_pages)}")
for s in noindex_pages:
    print(f"    - {s}")

# Save JSON
report = dict(
    city_results=city_results,
    bl_results=bl_results,
    score_distribution={str(k): v for k, v in score_dist.items()},
    missing_freq=missing_freq,
)
out = ROOT / "_dev" / "audit" / "website-audit-report.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"\nJSON report: {out}")
