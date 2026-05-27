#!/usr/bin/env python3
"""
stadt-quality-analysis.py — misst echte lokale Substanz pro Stadtseite.

Unterschied zum normalen Audit: zaehlt nicht Woerter, sondern Marker
fuer echten Mehrwert: Eigennamen von Friedhoefen, konkrete Eurozahlen,
Quellenangaben, Jahresdaten, Fristen.

Output: stadt-quality-report.md + stadt-quality.json
"""
import json
import os
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
STADT_DIR = ROOT / "bestatter"

# ---------- Substanz-Marker ----------

# Friedhofs-Eigennamen: "Waldfriedhof", "Nordfriedhof München", "Ohlsdorfer Friedhof"
# Muster: GrossWort direkt vor "friedhof" oder "Friedhof" mit Grosschreibung
RE_FRIEDHOF_NAME = re.compile(
    r"\b([A-ZÄÖÜ][a-zäöüß]{2,}(?:er)?(?:-\s?|\s)?(?:[Ff]riedhof|Friedhof))\b"
)

# Eurozahlen: "2.300 €", "1.200-1.800 €", "ab 500 €"
RE_EURO = re.compile(r"\b\d{1,3}(?:[.\s]\d{3})?(?:[\–\-]\d{1,3}(?:[.\s]\d{3})?)?\s?€")

# Jahreszahlen 1800-2099 (historische Details, Aktualitaet)
RE_JAHR = re.compile(r"\b(?:18|19|20)\d{2}\b")

# Quellen: "Quelle:", "laut", "gemaess §", "www.", "Bestattungsgesetz"
RE_QUELLE = re.compile(
    r"(?:Quelle|Quellen|laut|gemaess|gemäß|§\s?\d+|nach [A-ZÄÖÜ])"
)

# Fristen: "24 Stunden", "innerhalb von 36 Stunden", "§ 7"
RE_FRIST = re.compile(r"\b(\d{1,3})\s*(?:Stunden|Std\.?|Tage|Wochen|Monate|Jahre?)\b")

# Rechtsbezug Bundesland: "Bayerisches Bestattungsgesetz", "§ X BayBG"
RE_GESETZ = re.compile(
    r"(?:Bestattungsgesetz|Friedhofsgesetz|Bestattungs-\s?und\s?Friedhofsgesetz|"
    r"BestattG|FriedhofsG|§\s?\d+\s*(?:Abs\.?|Bay|NRW|Nds))"
)

# Template-Floskeln (Negativ-Marker, je mehr desto generischer)
GENERIC_PHRASES = [
    r"flexible zahlungsoptionen",
    r"finanzierungsm[oö]glichkeiten",
    r"kostenlose erstberatung",
    r"kostenvergleich",
    r"individuelle beratung",
    r"pers[oö]nliche betreuung",
    r"auf wunsch",
    r"nach ihren w[uü]nschen",
    r"in ihrer n[aä]he",
    r"24 stunden (?:erreichbar|verf[uü]gbar)",
    r"f[uü]r jeden geldbeutel",
    r"transparente preise",
]
RE_GENERIC = re.compile("|".join(GENERIC_PHRASES), re.I)


def strip_scripts_styles(html: str) -> str:
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.S | re.I)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.S | re.I)
    html = re.sub(r"<meta[^>]*>", "", html, flags=re.I)
    return html


def text_only(html: str) -> str:
    t = strip_scripts_styles(html)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def analyze(path: Path) -> dict:
    html = path.read_text(encoding="utf-8", errors="ignore")
    text = text_only(html)
    stadt = path.parent.name

    friedhof_names = set(m.group(1) for m in RE_FRIEDHOF_NAME.finditer(text))
    # Generische Treffer rausfiltern (z.B. "Der Friedhof" -> nur "Der Friedhof", kein Eigenname)
    friedhof_names = {f for f in friedhof_names
                      if not f.lower().startswith(("der ", "die ", "das ", "ein ", "eine "))
                      and len(f) > 9}  # Mindestens "XFriedhof" + was davor

    euro_hits = RE_EURO.findall(text)
    jahr_hits = [j for j in RE_JAHR.findall(text) if j not in ("2024", "2025", "2026")]
    quelle_hits = RE_QUELLE.findall(text)
    frist_hits = RE_FRIST.findall(text)
    gesetz_hits = RE_GESETZ.findall(text)
    generic_hits = RE_GENERIC.findall(text)

    words = len(text.split())

    # Qualitaets-Score
    # Substanz-Punkte
    substance = 0
    substance += min(len(friedhof_names) * 5, 25)     # max 25 (5 Friedhofs-Eigennamen)
    substance += min(len(euro_hits), 15)              # max 15 (15 Eurozahlen)
    substance += min(len(jahr_hits) * 2, 10)          # max 10 (historische Daten)
    substance += min(len(quelle_hits) * 3, 15)        # max 15 (Quellen/Rechtsbezug)
    substance += min(len(frist_hits), 10)             # max 10 (konkrete Fristen)
    substance += min(len(gesetz_hits) * 5, 15)        # max 15 (Bundesland-Recht)
    substance += min(words // 100, 10)                # max 10 (Wordcount-Bonus)
    # -> max 100

    # Generic-Abzug
    generic_penalty = min(len(generic_hits) * 3, 30)
    score = max(0, substance - generic_penalty)

    # Klassifizierung
    if score >= 70:
        tier = "GOLD"
    elif score >= 45:
        tier = "SILVER"
    elif score >= 25:
        tier = "BRONZE"
    else:
        tier = "GENERIC"

    return {
        "stadt": stadt,
        "score": score,
        "tier": tier,
        "words": words,
        "substance": substance,
        "generic_penalty": generic_penalty,
        "friedhof_names": sorted(friedhof_names),
        "friedhof_count": len(friedhof_names),
        "euro_count": len(euro_hits),
        "euro_samples": euro_hits[:5],
        "historic_years": sorted(set(jahr_hits))[:5],
        "quelle_count": len(quelle_hits),
        "frist_count": len(frist_hits),
        "gesetz_count": len(gesetz_hits),
        "generic_phrases_found": sorted(set(g.lower() for g in generic_hits)),
        "generic_count": len(generic_hits),
    }


def main():
    results = []
    for stadt_dir in sorted(STADT_DIR.iterdir()):
        if stadt_dir.is_dir():
            idx = stadt_dir / "index.html"
            if idx.exists():
                results.append(analyze(idx))

    results.sort(key=lambda r: -r["score"])

    tiers = defaultdict(list)
    for r in results:
        tiers[r["tier"]].append(r)

    # JSON
    (ROOT / "stadt-quality.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Markdown
    md = []
    md.append("# Stadtseiten-Qualitaetsanalyse")
    md.append("")
    md.append("**Gemessen:** Substanz (konkrete Friedhofsnamen, Euro-Betraege, Jahreszahlen, Quellen, Fristen, Bundesland-Recht) minus Generic-Floskeln")
    md.append("")
    md.append(f"**Seiten:** {len(results)}  ")
    md.append(f"**Ø Score:** {round(sum(r['score'] for r in results) / len(results), 1)}/100  ")
    md.append("")

    md.append("## Tier-Verteilung")
    md.append("")
    md.append("| Tier | Kriterium | Anzahl |")
    md.append("|---|---|---|")
    md.append(f"| GOLD | Score ≥70 — publish-ready | {len(tiers['GOLD'])} |")
    md.append(f"| SILVER | Score 45-69 — brauchbar, muss aufgeruestet | {len(tiers['SILVER'])} |")
    md.append(f"| BRONZE | Score 25-44 — dünn, Template-Upgrade noetig | {len(tiers['BRONZE'])} |")
    md.append(f"| GENERIC | Score <25 — praktisch wertlos fuer SEO/User | {len(tiers['GENERIC'])} |")
    md.append("")

    md.append("## Ranking aller Staedte")
    md.append("")
    md.append("| Rang | Stadt | Score | Tier | Friedhoefe | € | Quellen | Generics | Woerter |")
    md.append("|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(results, 1):
        md.append(
            f"| {i} | **{r['stadt']}** | {r['score']} | {r['tier']} | "
            f"{r['friedhof_count']} | {r['euro_count']} | {r['quelle_count']} | "
            f"{r['generic_count']} | {r['words']} |"
        )
    md.append("")

    # Details pro Tier
    for tier_name in ["GOLD", "SILVER", "BRONZE", "GENERIC"]:
        cities = tiers[tier_name]
        if not cities:
            continue
        md.append(f"## {tier_name}-Tier Details")
        md.append("")
        for r in cities[:10]:
            md.append(f"### {r['stadt']} — Score {r['score']}")
            if r["friedhof_names"]:
                md.append(f"- **Friedhoefe:** {', '.join(r['friedhof_names'])}")
            else:
                md.append("- **Friedhoefe:** _keine Eigennamen gefunden_")
            if r["euro_samples"]:
                md.append(f"- **Euro-Zahlen:** {', '.join(r['euro_samples'])}" +
                          (f" … (+{r['euro_count'] - 5})" if r['euro_count'] > 5 else ""))
            else:
                md.append("- **Euro-Zahlen:** _keine konkreten Betraege_")
            if r["generic_phrases_found"]:
                md.append(f"- **Generic-Floskeln ({r['generic_count']}x):** "
                          f"{', '.join(r['generic_phrases_found'][:3])}"
                          f"{' …' if len(r['generic_phrases_found']) > 3 else ''}")
            md.append("")
        if len(cities) > 10:
            md.append(f"_… plus {len(cities) - 10} weitere in diesem Tier (siehe JSON)_")
            md.append("")

    md.append("## Handlungsempfehlung")
    md.append("")
    md.append("Analog zum externen Audit:")
    md.append("")
    md.append("1. **GOLD-Tier behalten und indexiert lassen** — die sind Authority-Baustein.")
    md.append("2. **SILVER-Tier gezielt aufruesten** auf Golden-Template-Niveau, dann indexieren.")
    md.append("3. **BRONZE + GENERIC einfrieren** — NICHT loeschen, aber `noindex` setzen bis aufgeruestet. Sonst ziehen sie die Authority der guten Seiten runter.")
    md.append("4. **Reihenfolge beim Aufruesten:** Nach Stadtgroesse, nicht nach aktuellem Score.")
    md.append("")

    (ROOT / "stadt-quality-report.md").write_text("\n".join(md), encoding="utf-8")

    # Konsole
    print(f"Staedte: {len(results)}")
    print(f"Avg Score: {round(sum(r['score'] for r in results) / len(results), 1)}/100")
    print()
    print("Tier-Verteilung:")
    print(f"  GOLD    (>=70): {len(tiers['GOLD'])}")
    print(f"  SILVER  (45-69): {len(tiers['SILVER'])}")
    print(f"  BRONZE  (25-44): {len(tiers['BRONZE'])}")
    print(f"  GENERIC (<25):   {len(tiers['GENERIC'])}")
    print()
    print("Top 5:")
    for r in results[:5]:
        print(f"  {r['score']:3d} {r['tier']:7s} {r['stadt']:20s} "
              f"F:{r['friedhof_count']} €:{r['euro_count']} G:{r['generic_count']}")
    print()
    print("Bottom 5:")
    for r in results[-5:]:
        print(f"  {r['score']:3d} {r['tier']:7s} {r['stadt']:20s} "
              f"F:{r['friedhof_count']} €:{r['euro_count']} G:{r['generic_count']}")


if __name__ == "__main__":
    main()
