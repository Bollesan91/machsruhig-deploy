"""
Marktreife-Audit über 5 Dimensionen:
1. Tool-Quality (10 Tools)
2. Conversion-Funnel (CTAs, Lead-Capture)
3. Trust-Layer (E-E-A-T)
4. Performance (React+Babel, page-sizes)
5. Monetization (Affiliate, Bestatter-Partnership-Hooks)

Output: kompakter Befund pro Dimension + prioritizer Backlog.
"""
import os
import re
import json
from pathlib import Path
from collections import defaultdict

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
TOOLS = ROOT / "tools"
BESTATTER = ROOT / "bestatter"

# =====================================================================
# 1. TOOL-QUALITY-AUDIT
# =====================================================================
print("=" * 70)
print("1. TOOL-QUALITY-AUDIT (10 Tools)")
print("=" * 70)

tool_data = []
for tool in sorted(TOOLS.iterdir()):
    if not tool.is_dir():
        continue
    idx = tool / "index.html"
    if not idx.exists():
        continue
    text = idx.read_text(encoding="utf-8", errors="replace")
    size_kb = round(len(text.encode("utf-8")) / 1024.0, 1)

    # Tech-Indikatoren
    has_react = "ReactDOM" in text or "React.createElement" in text
    has_babel = "text/babel" in text or "babel.min" in text
    has_form = bool(re.search(r"<form\b", text))
    has_print = "@media print" in text or "window.print" in text
    has_export_pdf = "jsPDF" in text or "html2pdf" in text or "html2canvas" in text
    has_localStorage = "localStorage" in text or "sessionStorage" in text
    has_email_send = bool(re.search(r"mailto:|fetch.*api|api/.*lead|formspree|netlify-form", text, re.IGNORECASE))
    # Lead-Capture Indikatoren
    has_lead_qualified_event = "lead_qualified" in text
    has_cta_to_bestatter = "/bestatter/" in text
    has_cta_to_kostenrechner = "/tools/bestattungskosten-rechner" in text
    # Schema
    has_schema = "application/ld+json" in text
    has_softwareapp_schema = "SoftwareApplication" in text or "WebApplication" in text or "HowTo" in text
    # Title
    m = re.search(r"<title[^>]*>([^<]+)</title>", text)
    title = m.group(1) if m else "—"

    tool_data.append({
        "slug": tool.name,
        "size_kb": size_kb,
        "has_react_babel": has_react and has_babel,
        "has_form": has_form,
        "has_print": has_print,
        "has_export_pdf": has_export_pdf,
        "has_localStorage": has_localStorage,
        "has_email_send": has_email_send,
        "has_lead_event": has_lead_qualified_event,
        "has_cta_bestatter": has_cta_to_bestatter,
        "has_cta_kosten": has_cta_to_kostenrechner,
        "has_softwareapp_schema": has_softwareapp_schema,
        "title": title[:60],
    })

print(f"\n{'Tool':<28}{'KB':>5} {'React':>6} {'Form':>5} {'Prnt':>5} {'PDF':>4} {'Save':>5} {'CTAtoB':>6} {'Schma':>6}")
for t in tool_data:
    print(f"{t['slug']:<28}{t['size_kb']:>5} {'YES' if t['has_react_babel'] else '-':>6} "
          f"{'YES' if t['has_form'] else '-':>5} "
          f"{'YES' if t['has_print'] else '-':>5} "
          f"{'YES' if t['has_export_pdf'] else '-':>4} "
          f"{'YES' if t['has_localStorage'] else '-':>5} "
          f"{'YES' if t['has_cta_bestatter'] else '-':>6} "
          f"{'YES' if t['has_softwareapp_schema'] else '-':>6}")

react_babel_count = sum(1 for t in tool_data if t["has_react_babel"])
form_count = sum(1 for t in tool_data if t["has_form"])
lead_event_count = sum(1 for t in tool_data if t["has_lead_event"])
softwareapp_count = sum(1 for t in tool_data if t["has_softwareapp_schema"])
cta_bestatter_count = sum(1 for t in tool_data if t["has_cta_bestatter"])
cta_kosten_count = sum(1 for t in tool_data if t["has_cta_kosten"])

print(f"\nSummary:")
print(f"  React+Babel in-browser:           {react_babel_count}/10 (Performance-Killer)")
print(f"  Form-Tag:                          {form_count}/10")
print(f"  lead_qualified-Event:              {lead_event_count}/10 (in tracking.js definiert)")
print(f"  CTA -> Bestatter:                   {cta_bestatter_count}/10")
print(f"  CTA -> Kostenrechner:               {cta_kosten_count}/10 (self-ref ausschl.)")
print(f"  SoftwareApplication/HowTo Schema:  {softwareapp_count}/10 (besser für SERP)")

# =====================================================================
# 2. CONVERSION-FUNNEL-AUDIT
# =====================================================================
print()
print("=" * 70)
print("2. CONVERSION-FUNNEL-AUDIT")
print("=" * 70)

# Wie viele Cities haben CTA zu Tools / Vorsorge?
city_cta_data = defaultdict(int)
for c in sorted(BESTATTER.iterdir()):
    if not c.is_dir():
        continue
    idx = c / "index.html"
    if not idx.exists():
        continue
    text = idx.read_text(encoding="utf-8", errors="replace")
    if "/tools/bestattungskosten-rechner" in text:
        city_cta_data["bestattungskosten-rechner"] += 1
    if "/tools/checkliste-todesfall" in text:
        city_cta_data["checkliste-todesfall"] += 1
    if "/tools/vorsorge-check" in text:
        city_cta_data["vorsorge-check"] += 1
    if "/tools/beerdigungsplaner" in text:
        city_cta_data["beerdigungsplaner"] += 1
    if "/vorsorge/" in text:
        city_cta_data["vorsorge-hub"] += 1
    if "/vorsorge/sterbegeldversicherung" in text:
        city_cta_data["vorsorge/sterbegeldversicherung"] += 1
    if re.search(r'<a [^>]*href="https?://[^"]*check24', text, re.IGNORECASE):
        city_cta_data["check24-affiliate"] += 1
    if re.search(r'<a [^>]*href="https?://[^"]*dela', text, re.IGNORECASE):
        city_cta_data["dela-affiliate"] += 1
    if re.search(r'<form\b', text):
        city_cta_data["lead-form"] += 1

print(f"\nCity-Pages mit Outbound-Links (von 52 Cities):")
for k, v in sorted(city_cta_data.items(), key=lambda x: -x[1]):
    print(f"  {k:<35} {v:>3} / 52")

# =====================================================================
# 3. TRUST-LAYER (E-E-A-T)
# =====================================================================
print()
print("=" * 70)
print("3. TRUST-LAYER (E-E-A-T)")
print("=" * 70)

trust_pages = ["methodik.html", "ueber-uns.html", "impressum.html", "datenschutz.html"]
for p in trust_pages:
    path = ROOT / p
    if path.exists():
        text = path.read_text(encoding="utf-8", errors="replace")
        size = round(len(text.encode("utf-8")) / 1024.0, 1)
        # Count substantive content (paragraphs)
        p_count = len(re.findall(r"<p\b", text))
        h2_count = len(re.findall(r"<h2\b", text))
        # Author info?
        has_author = bool(re.search(r"redaktion|chefredakteur|autor|verantwortlich", text, re.IGNORECASE))
        # External cite/source?
        has_external_sources = len(re.findall(r'href="https?://(?!machsruhig)', text))
        print(f"  {p}: {size} KB, {p_count} <p>, {h2_count} <h2>, ext-sources: {has_external_sources}, author: {has_author}")
    else:
        print(f"  {p}: MISSING")

# Per-city Stand-Datum + author-block coverage
stand_count = 0
author_block_count = 0
sites_count = 0
for c in BESTATTER.iterdir():
    if not c.is_dir():
        continue
    idx = c / "index.html"
    if not idx.exists():
        continue
    sites_count += 1
    text = idx.read_text(encoding="utf-8", errors="replace")
    if re.search(r"Stand:?\s*\d", text):
        stand_count += 1
    if 'class="mr-article-meta"' in text:
        author_block_count += 1

print(f"\n  Per-City Trust-Signals:")
print(f"    Stand-Datum sichtbar:           {stand_count} / {sites_count}")
print(f"    Article-Meta-Block:             {author_block_count} / {sites_count}")

# =====================================================================
# 4. PERFORMANCE-AUDIT
# =====================================================================
print()
print("=" * 70)
print("4. PERFORMANCE-AUDIT")
print("=" * 70)

# React+Babel-Pages site-wide
react_pages = []
for p in ROOT.rglob("*.html"):
    if "node_modules" in str(p) or ".git" in str(p) or "_dev" in str(p):
        continue
    try:
        t = p.read_text(encoding="utf-8", errors="replace")
        if "text/babel" in t or "babel.min" in t:
            react_pages.append(p.relative_to(ROOT))
    except Exception:
        pass

print(f"\n  React+Babel in-browser Pages: {len(react_pages)}")
for p in react_pages[:15]:
    print(f"    {p}")

# Image-Audit: og-images
generic_og = 0
custom_og = 0
for c in BESTATTER.iterdir():
    if not c.is_dir():
        continue
    idx = c / "index.html"
    if not idx.exists():
        continue
    text = idx.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'<meta[^>]*property="og:image"[^>]*content="([^"]+)"', text)
    if m:
        url = m.group(1)
        if url.endswith("/assets/og-image.png") or url.endswith("/assets/og-image.jpg"):
            generic_og += 1
        else:
            custom_og += 1

print(f"\n  og:image-Coverage:")
print(f"    Generic (assets/og-image.png):  {generic_og} / 52")
print(f"    City-spezifisch:                {custom_og} / 52 — Round-4-Item")

# Page-Size Distribution (alle indexierbaren Pages)
sizes = []
for p in ROOT.rglob("index.html"):
    if "_dev" in str(p) or "node_modules" in str(p) or ".git" in str(p):
        continue
    try:
        kb = round(p.stat().st_size / 1024.0, 1)
        sizes.append((kb, p.relative_to(ROOT)))
    except Exception:
        pass
sizes.sort(reverse=True)
print(f"\n  Largest 5 Pages:")
for kb, p in sizes[:5]:
    print(f"    {kb} KB  {p}")

# =====================================================================
# 5. MONETIZATION-READINESS
# =====================================================================
print()
print("=" * 70)
print("5. MONETIZATION-READINESS")
print("=" * 70)

# Affiliate-Inventory site-wide
affiliate_partners = {
    "check24.de": 0,
    "amazon-partner": 0,
    "afilio": 0,
    "smartlaw": 0,
    "deutsche-anwaltshotline": 0,
    "solidar": 0,
    "dela": 0,
    "fineas": 0,
}
for p in ROOT.rglob("*.html"):
    if "_dev" in str(p) or "node_modules" in str(p) or ".git" in str(p):
        continue
    try:
        t = p.read_text(encoding="utf-8", errors="replace")
        for key in affiliate_partners:
            # match real outbound links to that partner
            if re.search(r'href="https?://[^"]*' + re.escape(key.split(".")[0]), t, re.IGNORECASE):
                affiliate_partners[key] += 1
    except Exception:
        pass

print(f"\n  Affiliate-Outbound-Links (sitewide):")
for p, cnt in sorted(affiliate_partners.items(), key=lambda x: -x[1]):
    print(f"    {p:<28} {cnt:>3} pages")

# Bestatter-Direkt-Affiliate / Lead-Capture
print(f"\n  Bestatter-Direkt-Hooks:")
print(f"    Lead-Forms auf Cities:          {city_cta_data['lead-form']} / 52 (alle aktuell FAKE)")
print(f"    Vorsorgevertrag-CTA in Cities:  ?")

# Vorsorge-CTAs / Funnel
print(f"\n  Vorsorge-Funnel-Touchpoints:")
print(f"    Cities mit Vorsorge-Link:       {city_cta_data['vorsorge-hub']} / 52")
print(f"    Cities mit Sterbegeldvers-Link: {city_cta_data['vorsorge/sterbegeldversicherung']} / 52")

print()
print("=" * 70)
print("AUDIT KOMPLETT")
print("=" * 70)
