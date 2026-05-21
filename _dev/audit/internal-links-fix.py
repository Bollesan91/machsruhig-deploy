#!/usr/bin/env python3
"""
Internal-Links-Fixer
====================
Wendet die kuratierten Fixes auf identifizierte broken interne Links an.

Regelarten (in dieser Reihenfolge):
1. REWRITE       : href-Wert ersetzen (Tippfehler / besserer Ersatz). Wendet sich
                   sowohl auf <a href="…"> als auch auf JSON-LD "item":"…" an.
2. DROP_ENTIRELY : entfernt Anchor + ggf. umgebenden Separator (·, &middot;, |, …).
                   Reihenfolge je Target:
                     a) <li>…anchor…</li> → ganzes <li> droppen
                     b) "sep anchor" oder "anchor sep" → beide droppen
                     c) bare anchor (Nav-Link-Container) → nur anchor droppen
3. UNLINK        : Fallback — Anchor weg, Text bleibt (für Inline-Use im Fließtext).
                   Für Targets, deren Text auch nach Unlink lesbar bleibt.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
HOST_PREFIX = "https://machsruhig.de"


# (href, replacement_href)
REWRITES = [
    ("/bestattung", "/bestatter/"),
    ("/kosten/", "/bestattungskosten"),
    ("/ueber/", "/ueber-uns"),
    ("/kostenrechner", "/tools/kostenrechner/"),
    ("/checklisten/", "/tools/checkliste-todesfall/"),
    ("/checklisten/erste-72-stunden/", "/tools/checkliste-todesfall/"),
    ("/ratgeber/checkliste-todesfall/", "/tools/checkliste-todesfall/"),
    ("/ratgeber/bestattungsvorsorge/", "/vorsorge/bestattungsvorsorge/"),
    ("/ratgeber/vorsorge/", "/vorsorge/"),
    ("/ratgeber/patientenverfuegung/", "/vorsorge/patientenverfuegung/"),
    ("/vorsorge/bestattungsvorsorgevertrag/", "/vorsorge/bestattungsvorsorge/"),
    ("/tools/brief-an-meine-liebsten", "/tools/abschiedsbrief/"),
    ("/bestatter-in/saarbruecken/", "/bestatter/saarbruecken/"),
    ("/bestatter/freiburg-im-breisgau/", "/bestatter/freiburg/"),
    ("/bestattungsarten/feuerbestattung/", "/bestattungsarten"),
    ("/bestattungsarten/feuerbestattung", "/bestattungsarten"),
    ("/bestattungsarten/baumbestattung/", "/bestattungsarten"),
    ("/bestattungsarten/seebestattung/", "/bestattungsarten"),
    ("/bestattungsarten/seebestattung", "/bestattungsarten"),
    ("/bestattungsarten/reerdigung/", "/bestattungsarten"),
]


# Ziele, die NUR in Nav/Footer auftreten und vollständig entfernt werden sollen
# (inkl. umgebender Trenner). Hier passt KEIN UNLINK.
DROP_ENTIRELY_TARGETS = {
    "/ratgeber/",
    "/ratgeber",
    "/wissen/",
    "/quellen/",
    "/redaktion/",
    "/redaktion",
    "/kontakt/",
    "/kontakt",
}


# Restliche Ziele ohne sinnvollen Ersatz: <li> droppen (wenn solo) oder Inline
# unlinken (Text bleibt).
UNLINK_TARGETS = {
    "/trauerfeier/",
    "/vorsorge/friedwald-baumbestattung/",
    "/ratgeber/seebestattung/",
    "/ratgeber/trauerfeier/",
    "/ratgeber/sozialbestattung/",
    "/ratgeber/bestatter-auswaehlen/",
    "/ratgeber/erbschein-antrag/",
    "/ratgeber/friedwald-ruheforst/",
    "/ratgeber/sterbeurkunde/",
    "/ratgeber/trauerredner/",
    "/ratgeber/bestattungsverfuegung/",
    "/ratgeber/trauerhilfe/",
    "/bestatter/offenbach/",
    "/bestatter/offenbach-am-main/",
    "/bestatter/herne/",
    "/bestatter/recklinghausen/",
    "/bestatter/heilbronn/",
    "/bestatter/bremerhaven/",
    "/bestatter/esslingen/",
    "/bestatter/brandenburg-an-der-havel/",
    "/bestatter/goettingen/",
    "/bestatter/weimar/",
    "/bestatter/jena/",
    "/bestatter/gera/",
    "/bestatter/iserlohn/",
    "/bestatter/schwerte/",
    "/bestatter/witten/",
    "/bestatter/hattingen/",
    "/bestatter/hildesheim/",
    "/bestatter/ulm/",
    "/bestatter/pforzheim/",
    "/bestatter/flensburg/",
    "/bestatter/muenchen/waldfriedhof-solln/",
    "/bestatter/muenchen/bogenhausen/",
    "/bestatter/muenchen/perlacher-forst/",
    "/bestatter/wuerzburg/",
    "/bestatter/wilhelmshaven/",
    "/bestatter/schwerin/",
    "/bestatter/stralsund/",
    "/bestatter/ludwigsburg/",
    "/bestatter/tuebingen/",
    "/bestatter/reutlingen/",
    "/bestatter/solingen/",
    "/bestatter/remscheid/",
}


SEP_PATTERNS = [
    r"\s*·\s*",
    r"\s*&middot;\s*",
    r"\s*\|\s*",
    r"\s*&bull;\s*",
]


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


def apply_rewrites(html: str, counts: dict) -> str:
    for old, new in REWRITES:
        for variant in (old, HOST_PREFIX + old):
            replacement_value = new if variant == old else HOST_PREFIX + new
            # 1) <a href="…">
            needle = f'href="{variant}"'
            replacement = f'href="{replacement_value}"'
            n = html.count(needle)
            if n:
                html = html.replace(needle, replacement)
                counts[f"REWRITE href {variant} -> {new}"] = (
                    counts.get(f"REWRITE href {variant} -> {new}", 0) + n
                )
            # 2) JSON-LD BreadcrumbList "item":"…" — nur fully-qualified
            if variant.startswith("http"):
                needle2 = f'"item":"{variant}"'
                replacement2 = f'"item":"{replacement_value}"'
                n2 = html.count(needle2)
                if n2:
                    html = html.replace(needle2, replacement2)
                    counts[f"REWRITE jsonld {variant} -> {new}"] = (
                        counts.get(f"REWRITE jsonld {variant} -> {new}", 0) + n2
                    )
    return html


def apply_drop_entirely(html: str, counts: dict) -> str:
    for target in DROP_ENTIRELY_TARGETS:
        for variant in (target, HOST_PREFIX + target):
            anchor_re = (
                r'<a\s+href="' + re.escape(variant) + r'"(?:\s+[^>]*)?>(?:[^<]*)</a>'
            )
            # A) <li>…anchor…</li> → ganzes <li>
            li_pat = re.compile(
                r"<li>\s*" + anchor_re + r"\s*</li>",
                re.IGNORECASE,
            )
            html, n = li_pat.subn("", html)
            if n:
                counts[f"DROP_LI {variant}"] = counts.get(f"DROP_LI {variant}", 0) + n

            # B) "sep anchor" oder "anchor sep" → beide weg
            for sep in SEP_PATTERNS:
                pat_after = re.compile(sep + anchor_re, re.IGNORECASE)
                html, n = pat_after.subn("", html)
                if n:
                    counts[f"DROP_SEP_ANCHOR {variant}"] = (
                        counts.get(f"DROP_SEP_ANCHOR {variant}", 0) + n
                    )
                pat_before = re.compile(anchor_re + sep, re.IGNORECASE)
                html, n = pat_before.subn("", html)
                if n:
                    counts[f"DROP_ANCHOR_SEP {variant}"] = (
                        counts.get(f"DROP_ANCHOR_SEP {variant}", 0) + n
                    )

            # C) Bare anchor (Nav-Link-Container, kein Trenner)
            bare_pat = re.compile(anchor_re, re.IGNORECASE)
            html, n = bare_pat.subn("", html)
            if n:
                counts[f"DROP_BARE_A {variant}"] = (
                    counts.get(f"DROP_BARE_A {variant}", 0) + n
                )
    return html


def apply_unlink(html: str, counts: dict) -> str:
    for target in UNLINK_TARGETS:
        for variant in (target, HOST_PREFIX + target):
            li_pat = re.compile(
                r'<li>\s*<a\s+href="'
                + re.escape(variant)
                + r'"(?:\s+[^>]*)?>([^<]*)</a>\s*</li>',
                re.IGNORECASE,
            )
            html, n = li_pat.subn("", html)
            if n:
                counts[f"DROP_LI {variant}"] = counts.get(f"DROP_LI {variant}", 0) + n

            a_pat = re.compile(
                r'<a\s+href="'
                + re.escape(variant)
                + r'"(?:\s+[^>]*)?>(.*?)</a>',
                re.IGNORECASE | re.DOTALL,
            )
            html, n = a_pat.subn(lambda m: m.group(1), html)
            if n:
                counts[f"UNLINK {variant}"] = counts.get(f"UNLINK {variant}", 0) + n
    return html


def main():
    pages = get_pages()
    total_changes = 0
    changed_files = 0
    per_op_counts: dict = {}
    per_file: dict = {}

    for p in pages:
        try:
            original = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        file_counts: dict = {}
        html = original
        html = apply_rewrites(html, file_counts)
        html = apply_drop_entirely(html, file_counts)
        html = apply_unlink(html, file_counts)
        if html != original:
            p.write_text(html, encoding="utf-8")
            changed_files += 1
            file_total = sum(file_counts.values())
            total_changes += file_total
            per_file[str(p.relative_to(ROOT))] = file_total
            for k, v in file_counts.items():
                per_op_counts[k] = per_op_counts.get(k, 0) + v

    print("=== Internal-Links-Fixer ===")
    print(f"Pages geändert:       {changed_files}")
    print(f"Edits gesamt:         {total_changes}")
    print()
    print("--- Per-Operation ---")
    for op, n in sorted(per_op_counts.items(), key=lambda kv: -kv[1]):
        print(f"  {n:4}  {op}")
    print()
    print("--- Per-Datei (Top 20) ---")
    for f, n in sorted(per_file.items(), key=lambda kv: -kv[1])[:20]:
        print(f"  {n:4}  {f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
