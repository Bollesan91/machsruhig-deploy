#!/usr/bin/env python3
"""
Stadt-Page-Modul-Heatmap (V2)
=============================
Audit auf 6 Pflicht-Module pro Stadt-Page mit flexiblen Header-Regex.

Module:
- akut:    Akutbox / "Was tun nach Todesfall" / Erste-Schritte
- kosten:  Bestattungskosten / Friedhofsgebühren
- bestwahl: Bestatter wählen / auswählen / finden / vergleichen
- sozial:  Sozialbestattung / § 74 SGB XII
- faq:     Häufige Fragen / FAQ
- quellen: Quellen-Section

Output:
- Markdown-Heatmap nach Score sortiert
- Total-Statistik
"""
import re
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]

MODULE_PATTERNS = {
    "akut": [
        r"<h2[^>]*>[^<]*(?:Akutbox|Akut-Box|[Nn]ach einem Todesfall|Erste(?:n)?\s+24\s+Stunden?|Erste(?:n)?\s+72\s+Stunden?|Sofort.{0,5}tun|Im\s+Akutfall|Was tun nach|ersten Schritte|in den ersten Tagen)",
    ],
    "kosten": [
        r"<h2[^>]*>[^<]*(?:Bestattungskosten|Kosten\s+(?:in|einer)|Friedhofsgebühren|Was kostet|Gebühren und Kosten|Gebühren\s+(?:in|der|für))",
    ],
    "bestwahl": [
        r"<h2[^>]*>[^<]*(?:Bestatter.*(?:wählen|w\\u00e4hlen|wahl|finden|auswählen|ausw\\u00e4hlen|auswahl|vergleichen|prüfen|pr\\u00fcfen)|(?:Wie|Welch[er]).{0,30}Bestatter|Bestatter\s+in\s+\w+\s+(?:wählen|auswählen|finden))",
    ],
    "sozial": [
        r"<h2[^>]*>[^<]*Sozialbestattung",
        r"§\s*74\s*SGB\s*XII",
    ],
    "faq": [
        r"<h2[^>]*>[^<]*(?:FAQ|Häufig|H&auml;ufig|Häufige Fragen|Fragen zur|Häufig gestellte)",
    ],
    "quellen": [
        r"<h2[^>]*>[^<]*(?:Quellen|Belege|Referenzen)",
    ],
}


def detect_modules(html):
    flags = {}
    for module, patterns in MODULE_PATTERNS.items():
        flags[module] = any(re.search(p, html, re.IGNORECASE | re.DOTALL) for p in patterns)
    return flags


def is_noindex(html):
    return bool(re.search(r'<meta\s+name="robots"\s+content="[^"]*noindex', html, re.IGNORECASE))


def main():
    cities_dir = ROOT / "bestatter"
    rows = []
    for p in sorted(cities_dir.iterdir()):
        if not p.is_dir():
            continue
        index = p / "index.html"
        if not index.exists():
            continue
        html = index.read_text(encoding="utf-8")
        flags = detect_modules(html)
        score = sum(1 for v in flags.values() if v)
        noindex = is_noindex(html)
        rows.append((p.name, flags, score, noindex, len(html)))

    rows.sort(key=lambda r: (r[2], r[0]))

    # Markdown
    out = []
    out.append("# Stadt-Page Modul-Heatmap (V2)")
    out.append("")
    out.append(f"**Stand:** automatisch generiert, {len(rows)} Stadt-Pages.")
    out.append("")
    out.append("## Übersicht")
    out.append("")
    totals = {k: 0 for k in MODULE_PATTERNS}
    for _, flags, *_ in rows:
        for k, v in flags.items():
            if v:
                totals[k] += 1
    out.append("| Modul | Vorhanden | Lücken |")
    out.append("|---|---:|---:|")
    for k, t in totals.items():
        out.append(f"| {k} | {t} | {len(rows) - t} |")
    out.append("")
    out.append("## Score-Verteilung")
    out.append("")
    from collections import Counter
    score_dist = Counter(r[2] for r in rows)
    for s in sorted(score_dist.keys(), reverse=True):
        out.append(f"- **{s}/6:** {score_dist[s]} Cities")
    out.append("")
    out.append("## Heatmap (sortiert nach Score, schlechteste zuerst)")
    out.append("")
    out.append("| Stadt | Akut | Kost | Bestwahl | Sozial | FAQ | Quellen | Score | noindex |")
    out.append("|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|")
    syms = {True: "✓", False: "✗"}
    for name, flags, score, noindex, _ in rows:
        ni = "⚠️" if noindex else "—"
        out.append(
            f"| {name} | {syms[flags['akut']]} | {syms[flags['kosten']]} | "
            f"{syms[flags['bestwahl']]} | {syms[flags['sozial']]} | "
            f"{syms[flags['faq']]} | {syms[flags['quellen']]} | "
            f"**{score}/6** | {ni} |"
        )

    report = "\n".join(out)
    report_path = ROOT / "_dev" / "audit" / "module-heatmap-v2.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"Report: {report_path.relative_to(ROOT)}")
    print(f"\nTotals over {len(rows)} cities:")
    for k, t in totals.items():
        print(f"  {k}: {t}/{len(rows)}")


if __name__ == "__main__":
    main()
