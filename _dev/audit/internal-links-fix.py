#!/usr/bin/env python3
"""
Internal-Links-Fixer
====================
Wendet die kuratierten Fixes auf identifizierte broken interne Links an.

Regelarten:
- REWRITE       : ersetze href-Wert (Tippfehler / besserer Ersatz).
- DROP_LI_FIRST : prüfe ob <li>…<a href=X>…</a>…</li> NUR den Link enthält;
                  falls ja → ganzes <li> entfernen. Sonst Fallback auf UNLINK.
- UNLINK        : <a href=X>TEXT</a> → TEXT (Anchor weg, Text bleibt).
- DROP_ANCHOR   : entferne den gesamten <a>-Tag (inkl. Text). Für nackt im Nav/
                  Footer stehende Hub-Anker, wo verbliebener Text optisch falsch
                  wäre.

Konservativer Default: bei Unklarheit UNLINK statt DROP.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]

HOST_PREFIX = "https://machsruhig.de"


# (href_value, replacement_href_value) — beide /pfad UND host-prefixed Varianten
REWRITES = [
    # Hub-Tippfehler & Pfad-Korrekturen
    ("/bestattung", "/bestatter/"),               # Breadcrumb-Drift
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
    # Bestattungsarten-Subpages existieren nicht → flach auf Hub
    ("/bestattungsarten/feuerbestattung/", "/bestattungsarten"),
    ("/bestattungsarten/feuerbestattung", "/bestattungsarten"),
    ("/bestattungsarten/baumbestattung/", "/bestattungsarten"),
    ("/bestattungsarten/seebestattung/", "/bestattungsarten"),
    ("/bestattungsarten/seebestattung", "/bestattungsarten"),
    ("/bestattungsarten/reerdigung/", "/bestattungsarten"),
]


# Ziele OHNE sinnvollen Ersatz. Behandlung in folgender Reihenfolge:
#   1) wenn in <li>…</li> als alleiniger Inhalt: <li> ganz entfernen.
#   2) sonst: Anchor unlinken (Text bleibt als Plain-Text).
UNLINK_TARGETS = {
    # Hubs that simply don't exist
    "/ratgeber/",
    "/ratgeber",
    "/wissen/",
    "/trauerfeier/",
    "/quellen/",
    "/redaktion/",
    "/redaktion",
    "/kontakt/",
    "/kontakt",
    # Ratgeber-/Vorsorge-Subpages ohne eigenen Inhalt
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
    # Nicht-existente Stadt-Pages
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


# Anker, deren Resttext im Nav/Footer optisch sinnlos wäre → ganzer Tag weg.
# (Pfade die NUR in Footer-/Nav-Containern auftreten.)
DROP_ANCHOR_TARGETS = {
    "/redaktion/",
    "/redaktion",
}


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
            needle = f'href="{variant}"'
            replacement = f'href="{replacement_value}"'
            n = html.count(needle)
            if n:
                html = html.replace(needle, replacement)
                counts[f"REWRITE {variant} -> {new}"] = (
                    counts.get(f"REWRITE {variant} -> {new}", 0) + n
                )
    return html


def apply_unlink(html: str, counts: dict) -> str:
    for target in UNLINK_TARGETS:
        for variant in (target, HOST_PREFIX + target):
            # 1) <li>\s*<a href="variant"...>...</a>\s*</li>
            li_pat = re.compile(
                r'<li>\s*<a\s+href="'
                + re.escape(variant)
                + r'"(?:\s+[^>]*)?>([^<]*)</a>\s*</li>',
                re.IGNORECASE,
            )
            html, n = li_pat.subn("", html)
            if n:
                counts[f"DROP_LI {variant}"] = counts.get(f"DROP_LI {variant}", 0) + n

            # 2) Inline unlink: <a href="variant"...>TEXT</a> -> TEXT
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


def apply_drop_anchor(html: str, counts: dict) -> str:
    for target in DROP_ANCHOR_TARGETS:
        for variant in (target, HOST_PREFIX + target):
            pat = re.compile(
                r'<a\s+href="'
                + re.escape(variant)
                + r'"(?:\s+[^>]*)?>.*?</a>',
                re.IGNORECASE | re.DOTALL,
            )
            html, n = pat.subn("", html)
            if n:
                counts[f"DROP_ANCHOR {variant}"] = (
                    counts.get(f"DROP_ANCHOR {variant}", 0) + n
                )
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
        # Reihenfolge: erst Rewrites (sonst würden manche UNLINKs Treffer "stehlen"),
        # dann harte DROPs, zuletzt UNLINK.
        html = apply_rewrites(html, file_counts)
        html = apply_drop_anchor(html, file_counts)
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
