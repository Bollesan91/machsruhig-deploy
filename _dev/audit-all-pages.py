#!/usr/bin/env python3
"""
machsruhig.de - Kombinierter Site-Audit
SEO + Content + Technik + Monetarisierung in einem Durchlauf.

Kategorien:
- homepage      : Startseite
- hub           : Vorsorge-Hub, Beerdigung-planen
- stadt         : 50 Stadtseiten
- bundesland    : 16 Bundesland-Seiten
- tool          : Interaktive Tools (Rechner, Generatoren)
- vorsorge      : Vorsorge-Cluster-Seiten
- content       : Info-Content (Trauerrede, Sprüche, Kondolenz ...)
- tool-content  : Content-Seiten mit Tool-Funktion (Mischung)
- legal         : Impressum, Datenschutz, Methodik, 404

Score: 100 Punkte, kategorie-spezifische Gewichtung.
"""
from __future__ import annotations
import os
import re
import json
from html.parser import HTMLParser
from pathlib import Path
from dataclasses import dataclass, field, asdict

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "_dev", "node_modules"}
SKIP_FILES = {"404.html"}  # Wird separat als "legal" behandelt

# --- Kategorisierung -------------------------------------------------------

def categorize(rel_path: str) -> str:
    p = rel_path.replace("\\", "/")
    if p == "index.html":
        return "homepage"
    if p in ("impressum.html", "datenschutz.html", "methodik.html", "404.html"):
        return "legal"
    if p in ("vorsorge/index.html", "beerdigung-planen.html"):
        return "hub"
    if p.startswith("bestatter/"):
        return "stadt"
    if p.startswith("bestattung-in/"):
        return "bundesland"
    if p.startswith("vorsorge/"):
        return "vorsorge"
    if p.startswith("tools/"):
        # Abschiedsbrief, Fristen-Radar, Notfallkarte sind content-lastige Tools
        if any(n in p for n in ("abschiedsbrief", "fristen-radar", "notfallkarte", "danksagung")):
            return "tool-content"
        return "tool"
    if p in ("bestattungskosten.html", "bestattungsarten.html",
             "trauerrede-schreiben.html", "trauersprueche.html",
             "kondolenzschreiben.html", "kindern-tod-erklaeren.html",
             "vertraege-kuendigen.html"):
        return "content"
    return "other"


# --- HTML-Parser ----------------------------------------------------------

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta_description = ""
        self.canonical = ""
        self.robots = ""
        self.og_title = ""
        self.og_description = ""
        self.og_image = ""
        self.h1_count = 0
        self.h1_texts: list[str] = []
        self.h2_count = 0
        self.h3_count = 0
        self.jsonld_blocks: list[dict] = []
        self.internal_links: set[str] = set()
        self.external_links: set[str] = set()
        self.affiliate_links: set[str] = set()
        self.images_total = 0
        self.images_missing_alt = 0
        self.has_main = False
        self.has_nav = False
        self.has_footer = False
        self.has_skip_link = False
        self.forms = 0
        self.inline_styles = 0
        self.inline_scripts_bytes = 0
        self.body_text_parts: list[str] = []
        self.cta_buttons = 0  # Buttons/Links mit CTA-Klassen
        self.lang = ""
        self.viewport = ""

        # Parser-State
        self._in_title = False
        self._in_body = False
        self._in_skip = False
        self._in_h1 = False
        self._in_jsonld = False
        self._jsonld_buf = ""
        self._in_inline_script = False
        self._inline_script_buf = ""
        self._in_script_src = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)

        if tag == "html":
            self.lang = a.get("lang", "")

        elif tag == "title":
            self._in_title = True

        elif tag == "meta":
            name = (a.get("name") or "").lower()
            prop = (a.get("property") or "").lower()
            content = a.get("content", "")
            if name == "description":
                self.meta_description = content
            elif name == "viewport":
                self.viewport = content
            elif name == "robots":
                self.robots = content
            elif prop == "og:title":
                self.og_title = content
            elif prop == "og:description":
                self.og_description = content
            elif prop == "og:image":
                self.og_image = content

        elif tag == "link":
            rel = (a.get("rel") or "").lower()
            if "canonical" in rel:
                self.canonical = a.get("href", "")

        elif tag == "body":
            self._in_body = True

        elif tag == "main":
            self.has_main = True

        elif tag == "nav":
            self.has_nav = True

        elif tag == "footer":
            self.has_footer = True

        elif tag == "h1":
            self.h1_count += 1
            self._in_h1 = True

        elif tag == "h2":
            self.h2_count += 1

        elif tag == "h3":
            self.h3_count += 1

        elif tag == "form":
            self.forms += 1

        elif tag == "a":
            href = a.get("href", "")
            cls = (a.get("class") or "").lower()
            if "btn" in cls or "cta" in cls:
                self.cta_buttons += 1
            # Skip-Link?
            if "skip" in cls or "skip" in href:
                self.has_skip_link = True
            if href:
                if href.startswith("http://") or href.startswith("https://"):
                    if "machsruhig.de" in href:
                        self.internal_links.add(href)
                    else:
                        self.external_links.add(href)
                        # Affiliate-Heuristik
                        low = href.lower()
                        if any(x in low for x in [
                            "awin", "tradedoubler", "affilinet", "webgains",
                            "dela", "solidar", "afilio", "?ref=", "?aff=",
                            "utm_source=machsruhig", "affiliate", "partner-id"
                        ]):
                            self.affiliate_links.add(href)
                elif href.startswith("mailto:") or href.startswith("tel:"):
                    pass
                elif href.startswith("#"):
                    pass
                else:
                    self.internal_links.add(href)

        elif tag == "button":
            cls = (a.get("class") or "").lower()
            if "btn" in cls or "cta" in cls:
                self.cta_buttons += 1

        elif tag == "img":
            self.images_total += 1
            alt = a.get("alt")
            if alt is None or alt.strip() == "":
                self.images_missing_alt += 1

        elif tag == "script":
            if a.get("type") == "application/ld+json":
                self._in_jsonld = True
                self._jsonld_buf = ""
            elif a.get("src"):
                self._in_script_src = True
            else:
                self._in_inline_script = True
                self._inline_script_buf = ""

        # Inline-Styles?
        if "style" in a and a["style"]:
            self.inline_styles += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
        elif tag == "body":
            self._in_body = False
        elif tag == "script":
            if self._in_jsonld:
                try:
                    # JSON-LD kann Array oder Objekt sein
                    data = json.loads(self._jsonld_buf.strip())
                    if isinstance(data, list):
                        self.jsonld_blocks.extend([d for d in data if isinstance(d, dict)])
                    elif isinstance(data, dict):
                        self.jsonld_blocks.append(data)
                except Exception:
                    self.jsonld_blocks.append({"_PARSE_ERROR": True, "_raw": self._jsonld_buf[:200]})
                self._in_jsonld = False
                self._jsonld_buf = ""
            elif self._in_inline_script:
                self.inline_scripts_bytes += len(self._inline_script_buf)
                self._in_inline_script = False
                self._inline_script_buf = ""
            elif self._in_script_src:
                self._in_script_src = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1:
            self.h1_texts.append(data.strip())
        if self._in_jsonld:
            self._jsonld_buf += data
        if self._in_inline_script:
            self._inline_script_buf += data
        if self._in_body and not self._in_inline_script and not self._in_jsonld and not self._in_script_src:
            self.body_text_parts.append(data)


# --- Audit-Checks ---------------------------------------------------------

@dataclass
class PageAudit:
    path: str
    category: str
    size_bytes: int
    word_count: int
    score: int = 0
    max_score: int = 100
    issues: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    wins: list[str] = field(default_factory=list)
    # Rohdaten
    title_len: int = 0
    meta_desc_len: int = 0
    h1_count: int = 0
    h2_count: int = 0
    internal_links: int = 0
    external_links: int = 0
    affiliate_links: int = 0
    jsonld_types: list[str] = field(default_factory=list)
    images_missing_alt: int = 0
    has_canonical: bool = False
    has_og: bool = False
    has_monetization_cta: bool = False


def extract_body_text(parts: list[str]) -> str:
    joined = " ".join(parts)
    joined = re.sub(r"\s+", " ", joined).strip()
    return joined


def jsonld_types(blocks: list[dict]) -> list[str]:
    """Rekursive @type-Extraktion. Beruecksichtigt @graph und verschachtelte Objekte."""
    types = []

    def walk(node):
        if isinstance(node, dict):
            t = node.get("@type")
            if isinstance(t, list):
                types.extend(t)
            elif t:
                types.append(t)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    for b in blocks:
        if "_PARSE_ERROR" in b:
            types.append("PARSE_ERROR")
            continue
        walk(b)
    return types


def audit_page(path: Path, rel: str) -> PageAudit:
    html = path.read_text(encoding="utf-8", errors="ignore")
    parser = PageParser()
    try:
        parser.feed(html)
    except Exception as e:
        # Parser-Fehler = kritischer Issue
        result = PageAudit(
            path=rel, category=categorize(rel),
            size_bytes=len(html.encode("utf-8")),
            word_count=0,
        )
        result.issues.append(f"HTML-Parser-Fehler: {e}")
        return result

    category = categorize(rel)
    body_text = extract_body_text(parser.body_text_parts)
    word_count = len(body_text.split())
    jtypes = jsonld_types(parser.jsonld_blocks)

    # JSX-Leak-Detektion (Babel-Standalone = client-side rendering = SEO-tot)
    has_babel_standalone = "@babel/standalone" in html or "babel.min.js" in html
    jsx_leak_count = (
        html.count("style={{")
        + html.count(" className=")
        + len(re.findall(r"<>\s*<", html))
    )
    # Monetarisierungs-Detektion (Affiliate/Lead/Kostenpflichtig)
    html_lower = html.lower()
    has_monetization = bool(
        parser.affiliate_links
        or "affiliate" in html_lower
        or 'data-event="affiliateclick"' in html_lower
        or 'trackaffiliate' in html_lower
        or 'dela' in html_lower
        or 'solidar' in html_lower
        or "bestatter-kontaktformular" in html_lower
        or "lead-form" in html_lower
    )

    audit = PageAudit(
        path=rel,
        category=category,
        size_bytes=len(html.encode("utf-8")),
        word_count=word_count,
        title_len=len((parser.title or "").strip()),
        meta_desc_len=len(parser.meta_description or ""),
        h1_count=parser.h1_count,
        h2_count=parser.h2_count,
        internal_links=len(parser.internal_links),
        external_links=len(parser.external_links),
        affiliate_links=len(parser.affiliate_links),
        jsonld_types=jtypes,
        images_missing_alt=parser.images_missing_alt,
        has_canonical=bool(parser.canonical),
        has_og=bool(parser.og_title and parser.og_description),
        has_monetization_cta=has_monetization,
    )

    score = 0

    # --- TECHNIK-BASIS (immer, 30 Punkte) ----------------------------------

    # lang + viewport (4 P)
    if parser.lang in ("de", "de-DE"):
        score += 2; audit.wins.append("lang-Attribut korrekt")
    else:
        audit.issues.append(f"lang-Attribut fehlt oder falsch: '{parser.lang}'")

    if "width=device-width" in parser.viewport:
        score += 2
    else:
        audit.issues.append("Viewport-Meta fehlt oder falsch")

    # Title (5 P)
    tlen = audit.title_len
    if tlen == 0:
        audit.issues.append("Title fehlt komplett")
    elif tlen < 30:
        score += 2
        audit.warnings.append(f"Title sehr kurz ({tlen} Zeichen, Ziel 50-60)")
    elif tlen > 65:
        score += 3
        audit.warnings.append(f"Title zu lang ({tlen} Zeichen, Ziel 50-60)")
    else:
        score += 5

    # Meta-Description (5 P)
    dlen = audit.meta_desc_len
    if dlen == 0:
        audit.issues.append("Meta-Description fehlt")
    elif dlen < 120:
        score += 2
        audit.warnings.append(f"Meta-Description zu kurz ({dlen} Zeichen, Ziel 140-160)")
    elif dlen > 165:
        score += 3
        audit.warnings.append(f"Meta-Description zu lang ({dlen} Zeichen)")
    else:
        score += 5

    # Canonical (4 P)
    if parser.canonical:
        if parser.canonical.startswith("https://www.machsruhig.de") or parser.canonical.startswith("https://machsruhig.de"):
            score += 4
        else:
            score += 2
            audit.warnings.append(f"Canonical nicht absolut machsruhig.de: {parser.canonical[:60]}")
    else:
        audit.issues.append("Canonical-Link fehlt")

    # Open Graph (3 P)
    if parser.og_title and parser.og_description:
        score += 2
        if parser.og_image:
            score += 1
        else:
            audit.warnings.append("OG-Image fehlt")
    else:
        audit.warnings.append("Open-Graph-Tags unvollständig")

    # Semantik: main, nav, footer (4 P)
    semantic_hits = sum([parser.has_main, parser.has_nav, parser.has_footer])
    score += semantic_hits + (1 if semantic_hits == 3 else 0)
    if not parser.has_main:
        audit.issues.append("<main>-Landmark fehlt")
    if not parser.has_footer:
        audit.warnings.append("<footer> fehlt")

    # H1 (3 P)
    if parser.h1_count == 1:
        score += 3
    elif parser.h1_count == 0:
        audit.issues.append("Kein H1 vorhanden")
    else:
        score += 1
        audit.warnings.append(f"{parser.h1_count} H1-Elemente (sollte genau 1 sein)")

    # Bilder mit alt (2 P)
    if parser.images_total == 0 or parser.images_missing_alt == 0:
        score += 2
    else:
        audit.warnings.append(f"{parser.images_missing_alt}/{parser.images_total} Bilder ohne alt-Attribut")

    # --- CONTENT-TIEFE (kategorie-spezifisch, 30 Punkte) -------------------

    # Wort-Zahl-Ziele je Kategorie
    word_targets = {
        "homepage": (600, 1200),
        "hub": (1000, 2500),
        "stadt": (500, 1200),
        "bundesland": (400, 1000),
        "tool": (250, 800),           # Tools dürfen schlanker sein
        "tool-content": (800, 2500),
        "vorsorge": (1500, 4000),     # Vorsorge = Monetarisierung = Tiefe!
        "content": (1500, 4000),
        "legal": (100, 5000),
        "other": (300, 3000),
    }
    lo, hi = word_targets.get(category, (300, 3000))

    if category == "legal":
        score += 15  # Legal-Seiten bekommen pauschal Punkte, kein Content-Audit sinnvoll
    else:
        if word_count < lo * 0.5:
            audit.issues.append(f"Content extrem dünn: {word_count} Wörter (Ziel ≥ {lo})")
        elif word_count < lo:
            score += 5
            audit.warnings.append(f"Content dünn: {word_count} Wörter (Ziel ≥ {lo})")
        elif word_count <= hi:
            score += 15
            audit.wins.append(f"Content-Tiefe passend ({word_count} Wörter)")
        else:
            score += 13
            audit.warnings.append(f"Content sehr lang ({word_count} Wörter) - evtl. splitten")

    # H2-Struktur (5 P)
    if parser.h2_count >= 3:
        score += 5
    elif parser.h2_count >= 1:
        score += 3
        audit.warnings.append(f"Nur {parser.h2_count} H2 - Struktur ausbaufähig")
    else:
        audit.issues.append("Keine H2-Gliederung")

    # Interne Links (5 P) - Content-Silo
    target_internal = {
        "homepage": 10, "hub": 10, "stadt": 8, "bundesland": 8,
        "tool": 5, "tool-content": 8, "vorsorge": 10, "content": 10,
        "legal": 3, "other": 5,
    }
    needed = target_internal.get(category, 5)
    if audit.internal_links >= needed:
        score += 5
    elif audit.internal_links >= needed / 2:
        score += 2
        audit.warnings.append(f"Nur {audit.internal_links} interne Links (Ziel ≥ {needed})")
    else:
        audit.issues.append(f"Zu wenig interne Links: {audit.internal_links} (Ziel ≥ {needed})")

    # Schema.org (5 P)
    relevant_schema = {
        "homepage": ["Organization", "WebSite"],
        "hub": ["WebPage", "BreadcrumbList"],
        "stadt": ["LocalBusiness", "BreadcrumbList", "Place", "FAQPage"],
        "bundesland": ["WebPage", "BreadcrumbList", "Place"],
        "tool": ["WebApplication", "SoftwareApplication", "HowTo"],
        "tool-content": ["HowTo", "Article", "WebPage"],
        "vorsorge": ["Article", "FAQPage", "Product", "Service"],
        "content": ["Article", "FAQPage", "HowTo"],
        "legal": [],
        "other": ["WebPage"],
    }
    wanted = relevant_schema.get(category, [])
    has_any = len(audit.jsonld_types) > 0
    has_wanted = any(t in audit.jsonld_types for t in wanted)
    if category == "legal":
        score += 5
    elif has_wanted:
        score += 5; audit.wins.append(f"Schema: {', '.join(set(audit.jsonld_types))[:60]}")
    elif has_any:
        score += 2
        audit.warnings.append(f"Schema vorhanden aber nicht ideal: {audit.jsonld_types}")
    else:
        audit.issues.append(f"Kein Schema.org - Ziel: {wanted}")

    # --- MONETARISIERUNG (15 Punkte, kategorie-spezifisch) ----------------

    # Nur Seiten mit Monetarisierungs-Potenzial bewerten
    monetize_expected = category in ("homepage", "hub", "stadt", "bundesland",
                                      "vorsorge", "content", "tool-content")

    if not monetize_expected:
        score += 15  # Tools/Legal müssen nicht monetarisieren
    else:
        if has_monetization:
            score += 10; audit.wins.append("Monetarisierungs-Element vorhanden")
            if audit.affiliate_links > 0:
                score += 3
            if parser.cta_buttons >= 2:
                score += 2
            elif parser.cta_buttons >= 1:
                score += 1
        else:
            if category in ("stadt", "bundesland"):
                audit.issues.append("Keine Monetarisierung (Lead-Form oder Affiliate fehlt)")
            elif category in ("vorsorge", "hub"):
                audit.issues.append("Keine Affiliate/Lead-Integration - Vorsorge ist KERN-Monetarisierung")
            elif category == "content":
                audit.warnings.append("Kein Monetarisierungs-Hook (Cross-Sell/Affiliate)")
            else:
                audit.warnings.append("Kein Monetarisierungs-Hook")

    # --- SEO-EXTRAS (10 Punkte) -------------------------------------------

    # robots-Meta nicht noindex (3 P)
    if "noindex" in (parser.robots or "").lower():
        if category in ("legal", "other"):
            score += 3  # legal darf noindex sein
        else:
            audit.issues.append(f"noindex gesetzt (category={category})")
    else:
        score += 3

    # Inline-Code sparsam (2 P)
    if parser.inline_scripts_bytes < 5000:
        score += 2
    elif parser.inline_scripts_bytes < 20000:
        score += 1
        audit.warnings.append(f"Viel Inline-JS: {parser.inline_scripts_bytes} Bytes")
    else:
        audit.warnings.append(f"Sehr viel Inline-JS: {parser.inline_scripts_bytes} Bytes")

    if parser.inline_styles < 5:
        score += 2
    elif parser.inline_styles < 20:
        score += 1
        audit.warnings.append(f"{parser.inline_styles} Inline-Style-Attribute")
    else:
        audit.warnings.append(f"Sehr viele Inline-Styles: {parser.inline_styles}")

    # H1-Keyword-Match (3 P, nur für SEO-relevante Kategorien)
    h1 = " ".join(parser.h1_texts).lower()
    title_lower = parser.title.lower()
    if h1 and title_lower:
        # Wenigstens zwei signifikante Wörter sollten in beiden vorkommen
        h1_words = set(w for w in re.findall(r"[a-zäöüß]+", h1) if len(w) > 4)
        title_words = set(w for w in re.findall(r"[a-zäöüß]+", title_lower) if len(w) > 4)
        overlap = h1_words & title_words
        if len(overlap) >= 2:
            score += 3
        elif overlap:
            score += 1
            audit.warnings.append("H1 und Title nur gering überlappend")
        else:
            audit.issues.append("H1 und Title haben keine Keyword-Überlappung")
    else:
        pass  # Bereits als H1-Issue erfasst

    audit.score = min(score, 100)

    # JSX-Leak = automatischer Score-Cap auf 40 (Deploy-Blocker)
    if jsx_leak_count >= 5 and has_babel_standalone:
        audit.issues.append(
            f"DEPLOY-BLOCKER: JSX wird client-side via @babel/standalone kompiliert "
            f"({jsx_leak_count} JSX-Leaks). Google sieht kein H1, keinen Content."
        )
        audit.score = min(audit.score, 40)
    elif jsx_leak_count >= 2:
        audit.warnings.append(f"{jsx_leak_count} JSX-Leaks im HTML - evtl. Build-Problem")

    return audit


# --- Main -----------------------------------------------------------------

def collect_pages(root: Path) -> list[Path]:
    pages = []
    for p in root.rglob("*.html"):
        rel = p.relative_to(root).as_posix()
        if any(part in SKIP_DIRS for part in rel.split("/")):
            continue
        if rel.startswith("templates/"):
            continue  # Templates nicht auditieren
        pages.append(p)
    return sorted(pages)


def main():
    pages = collect_pages(ROOT)
    results: list[PageAudit] = []
    for p in pages:
        rel = p.relative_to(ROOT).as_posix()
        results.append(audit_page(p, rel))

    # --- Ausgabe ----------------------------------------------------------
    by_cat: dict[str, list[PageAudit]] = {}
    for r in results:
        by_cat.setdefault(r.category, []).append(r)

    print("=" * 78)
    print("MACHSRUHIG.DE - KOMBINIERTER AUDIT")
    print("=" * 78)
    print(f"Seiten gesamt: {len(results)}")
    overall_avg = sum(r.score for r in results) / max(len(results), 1)
    print(f"Gesamt-Score: {overall_avg:.1f}/100")
    print()
    print("Score nach Kategorie:")
    for cat in sorted(by_cat.keys()):
        items = by_cat[cat]
        avg = sum(i.score for i in items) / len(items)
        print(f"  {cat:15s} {len(items):3d} Seiten   Ø {avg:5.1f}/100")

    # Top-Issues
    all_issues: dict[str, int] = {}
    for r in results:
        for iss in r.issues:
            # Gruppieren auf Grund-Muster
            key = re.sub(r"\d+", "N", iss)[:70]
            all_issues[key] = all_issues.get(key, 0) + 1

    print()
    print("TOP 15 ISSUES (site-weit):")
    for iss, cnt in sorted(all_issues.items(), key=lambda x: -x[1])[:15]:
        print(f"  [{cnt:3d}x]  {iss}")

    # Schwächste Seiten
    print()
    print("SCHWÄCHSTE 15 SEITEN:")
    for r in sorted(results, key=lambda x: x.score)[:15]:
        print(f"  {r.score:3d}/100  [{r.category:12s}]  {r.path}")

    # Per-Kategorie-Details
    print()
    print("=" * 78)
    print("KATEGORIE-DETAILS")
    print("=" * 78)
    for cat in sorted(by_cat.keys()):
        items = sorted(by_cat[cat], key=lambda x: x.score)
        avg = sum(i.score for i in items) / len(items)
        print(f"\n--- {cat.upper()} ({len(items)} Seiten, Ø {avg:.1f}) ---")
        # Aggregierte Issues pro Kategorie
        cat_issues: dict[str, int] = {}
        for r in items:
            for iss in r.issues:
                key = re.sub(r"\d+", "N", iss)[:70]
                cat_issues[key] = cat_issues.get(key, 0) + 1
        for iss, cnt in sorted(cat_issues.items(), key=lambda x: -x[1])[:8]:
            print(f"    [{cnt:3d}x] {iss}")

    # JSON-Report für Backlog
    report_path = ROOT / "_dev" / "AUDIT-REPORT.json"
    report = {
        "meta": {
            "pages": len(results),
            "avg_score": round(overall_avg, 2),
            "by_category": {
                cat: {
                    "count": len(items),
                    "avg_score": round(sum(i.score for i in items) / len(items), 2),
                }
                for cat, items in by_cat.items()
            },
        },
        "pages": [asdict(r) for r in results],
    }
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nJSON-Report: {report_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
