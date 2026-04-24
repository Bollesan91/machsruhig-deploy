#!/usr/bin/env python3
"""
machsruhig.de - Bundesland-Seite Re-Check

Automatisierter Ehrlichkeits-Check für bearbeitete Bundesländer-Seiten.
Nicht perfekt, aber fängt die häufigsten Fallen ab, die mir beim direkten
Schreiben durchrutschen können.

Aufruf:
    python3 _dev/bundesland-recheck.py bestattung-in/thüringen/index.html
    python3 _dev/bundesland-recheck.py --all

Der Re-Check ersetzt NICHT den Audit-Score. Er prüft Inhaltsqualität,
nicht SEO-Struktur.
"""
from __future__ import annotations
import sys
import re
import json
from pathlib import Path
from dataclasses import dataclass, field

ROOT = Path(__file__).resolve().parent.parent

# Farbcodes für Terminal
C_RED = "\033[91m"
C_YELLOW = "\033[93m"
C_GREEN = "\033[92m"
C_BLUE = "\033[94m"
C_RESET = "\033[0m"
C_BOLD = "\033[1m"


@dataclass
class CheckFinding:
    level: str  # BLOCKER, WARN, INFO
    category: str
    message: str
    snippet: str = ""


def check_page(path: Path) -> list[CheckFinding]:
    """Führt alle Checks auf einer Bundesland-Seite aus."""
    html = path.read_text()
    findings: list[CheckFinding] = []

    # Body-Text für Analyse extrahieren (ohne Script/Style)
    main_match = re.search(r"<main[^>]*>(.*?)</main>", html, re.DOTALL)
    main_html = main_match.group(1) if main_match else html
    body_text = re.sub(r"<script[^>]*>.*?</script>", " ", main_html, flags=re.DOTALL)
    body_text = re.sub(r"<style[^>]*>.*?</style>", " ", body_text, flags=re.DOTALL)
    body_text_html = body_text
    body_text = re.sub(r"<[^>]+>", " ", body_text)
    body_text = re.sub(r"\s+", " ", body_text)

    # --- CHECK 1: Struktur & Minimum-Content ---
    word_count = len(body_text.split())
    if word_count < 1200:
        findings.append(
            CheckFinding(
                "WARN",
                "Content-Umfang",
                f"Nur {word_count} Wörter — für Bundesland-Seite eher dünn "
                f"(BW/MV/LSA/TH liegen bei 1700-2400).",
            )
        )

    # --- CHECK 2: §-Referenzen ---
    para_refs = re.findall(r"§\s*\d+", body_text)
    if len(para_refs) < 8:
        findings.append(
            CheckFinding(
                "WARN",
                "§-Referenzen",
                f"Nur {len(para_refs)} §-Referenzen — YMYL-Rechtsseite sollte "
                f"≥ 8 konkrete Paragraphen belegen.",
            )
        )

    # --- CHECK 3: Externe Primärquellen ---
    ext_links = re.findall(r'<a href="https?://[^"]+"[^>]*rel="noopener"', html)
    if len(ext_links) < 10:
        findings.append(
            CheckFinding(
                "WARN",
                "Primärquellen",
                f"Nur {len(ext_links)} externe Verlinkungen — Ziel: ≥ 10 "
                f"Primärquellen.",
            )
        )

    # --- CHECK 4: Pietätslosigkeiten ---
    pietaet_patterns = [
        (r"Tourist\w*\s*(Bestat|Ostsee|\.)", "touristische Bestattungs-Formulierung"),
        (r"Schnäppchen|günstig\s+(sterben|bestatten)", "Preismarketing"),
        (r"Trauer\w*\s*(gleich\s+)?mit\s+(Urlaub|Ferien)", "Trauer+Urlaub-Mix"),
        (r"Deal|Angebot|Rabatt|Schnäppchen", "Marketing-Vokabular"),
    ]
    for pattern, desc in pietaet_patterns:
        for m in re.finditer(f"[^.]*{pattern}[^.]*", body_text, re.IGNORECASE):
            findings.append(
                CheckFinding(
                    "BLOCKER",
                    "Pietät",
                    f"Mögliche pietätlose Formulierung: {desc}",
                    snippet=m.group(0).strip()[:150],
                )
            )

    # --- CHECK 5: Unbelegte Superlativ-/Erstmaligkeits-Aussagen ---
    risky_claims = [
        (r"\berst\w+\s+deutsche\w*\b", "Erstmalig-in-Deutschland-Aussage"),
        (r"\beinzig\w+\s+in\s+Deutschland", "Einzig-in-Deutschland-Aussage"),
        (r"bundesweit\w*\s+Vorreiter", "Vorreiter-Aussage"),
        (r"\b(erste|zweite|dritte|vierte|fünfte|sechste)\s+Krematorium\s+Deutschlands?\b", "Krematoriums-Rang-Zahl"),
        (r"\bstrengste\b", "Strengste-Regelung-Aussage"),
    ]
    for pattern, desc in risky_claims:
        for m in re.finditer(f"[^.]*{pattern}[^.]*", body_text, re.IGNORECASE):
            snippet = m.group(0).strip()[:200]
            # Quellennähe prüfen: ist im gleichen Absatz ein rel="noopener"-Link?
            findings.append(
                CheckFinding(
                    "INFO",
                    "Starke Aussage",
                    f"{desc} — Quellennähe manuell prüfen:",
                    snippet=snippet,
                )
            )

    # --- CHECK 6: Städte außerhalb des Bundeslandes? ---
    # Heuristik: bekannte Zuordnungsfehler aus früherer MV-Seite
    bundesland_filename = path.parent.name
    external_city_mapping = {
        "mecklenburg-vorpommern": ["Lübeck", "Kiel", "Flensburg", "Hamburg", "Bremen"],
        "schleswig-holstein": ["Rostock", "Wismar", "Schwerin", "Greifswald"],
        "sachsen-anhalt": ["Leipzig", "Dresden", "Chemnitz"],
        "sachsen": ["Magdeburg", "Halle", "Dessau"],
        "thüringen": ["Leipzig", "Dresden", "Kassel"],
        "hessen": ["Würzburg", "Stuttgart", "Mainz"],
        "bayern": ["Ulm", "Kassel"],
        "baden-württemberg": ["München", "Nürnberg", "Mainz"],
        "nordrhein-westfalen": ["Frankfurt", "Kassel", "Bremen"],
        "rheinland-pfalz": ["Frankfurt", "Saarbrücken", "Karlsruhe"],
        "saarland": ["Trier", "Mainz", "Karlsruhe"],
        "niedersachsen": ["Hamburg", "Bremen", "Magdeburg"],
        "brandenburg": ["Berlin", "Magdeburg"],
        "berlin": ["Potsdam", "Frankfurt (Oder)"],
        "hamburg": ["Lübeck", "Bremen"],
        "bremen": ["Hamburg", "Oldenburg"],
    }
    foreign_cities = external_city_mapping.get(bundesland_filename, [])
    for city in foreign_cities:
        pattern = rf"\b{re.escape(city)}\b"
        if re.search(pattern, body_text):
            # Ist die Erwähnung im Kontext "als Nachbarstadt" oder als Bestandteil?
            for m in re.finditer(f"[^.]*\\b{re.escape(city)}\\b[^.]*", body_text):
                snippet = m.group(0).strip()[:200]
                # Harmlose Erwähnungen: "Ausfahrt startet von ... Hamburg" ok
                if re.search(r"(Hamburg|Bremen).*Ausfahrt|Küsten|Hohe See", snippet):
                    continue
                findings.append(
                    CheckFinding(
                        "BLOCKER",
                        "Geografie",
                        f"'{city}' erwähnt, liegt aber NICHT in {bundesland_filename}! "
                        f"Unbedingt prüfen — klassischer Lübeck-in-MV-Fehler.",
                        snippet=snippet,
                    )
                )

    # --- CHECK 7: Sekundärquellen als Primärquellen getarnt ---
    sekundaer_domains = [
        "bestattung-information.de",
        "bestattungen.de",
        "bestatter.org",
        "trauerrede-schreiben.com",
        "meine-kartenmanufaktur.de",
        "loeer-bestattungen.de",
    ]
    for domain in sekundaer_domains:
        if domain in html:
            # Prüfen: wird das kontextuell als Sekundärquelle markiert?
            context_window = 300
            for m in re.finditer(f"https?://[^\"]*{re.escape(domain)}[^\"]*", html):
                start = max(0, m.start() - context_window)
                end = min(len(html), m.end() + context_window)
                surrounding = html[start:end]
                flagged = any(
                    marker in surrounding.lower()
                    for marker in ["sekundär", "verzeichnis", "portal"]
                )
                if not flagged:
                    findings.append(
                        CheckFinding(
                            "WARN",
                            "Quellen-Hygiene",
                            f"{domain} verlinkt ohne Sekundärquellen-Markierung. "
                            f"Transparenz erhöhen.",
                        )
                    )

    # --- CHECK 8: Falsche Absolutaussagen zu Sargpflicht/Fristen ---
    # Häufige Sachfehler, die gerne ins Template rutschen
    # Hinweis: '8 Tage' ist in Bayern (§ 19 BestV) und Sachsen (§ 19 SächsBestG, "Werktage") gesetzlich korrekt!
    # Wir flaggen daher nur '7 Tage' und nur dann, wenn KEIN BestV/SächsBestG-Beleg in der Nähe steht.
    fehler_templates = [
        (r"Sargpflicht[:.\s]+Nein[^a-z]", "'Sargpflicht: Nein' — in den meisten Bundesländern FALSCH"),
        (r"Mindestfrist[:.\s]+24\s*h", "'Mindestfrist 24h' — nur in einigen BL korrekt (z.B. nicht TH/LSA)"),
        (r"Höchstfrist[:.\s]+7\s*Tag", "'Höchstfrist 7 Tage' — meist 10 Tage; in BY/SN gilt 8 Tage"),
    ]
    for pattern, desc in fehler_templates:
        if re.search(pattern, body_text, re.IGNORECASE):
            findings.append(
                CheckFinding(
                    "BLOCKER",
                    "Template-Sachfehler",
                    f"Verdächtige Template-Formulierung: {desc}",
                )
            )

    # --- CHECK 9: Landesrecht-Volltext verlinkt? ---
    has_landesrecht_link = bool(
        re.search(r"landesrecht[-.]\w+\.de|gesetze-im-internet\.de", html)
    )
    if not has_landesrecht_link:
        findings.append(
            CheckFinding(
                "WARN",
                "Landesrecht-Link",
                "Kein Link zum Landesrecht-Portal gefunden. "
                "Landesrecht-Volltext sollte verlinkt sein.",
            )
        )

    return findings


def format_findings(path: Path, findings: list[CheckFinding]) -> str:
    """Formatiert die Funde für Terminal-Ausgabe."""
    lines = []
    lines.append(f"\n{C_BOLD}=== Re-Check: {path.relative_to(ROOT)} ==={C_RESET}")

    blockers = [f for f in findings if f.level == "BLOCKER"]
    warnings = [f for f in findings if f.level == "WARN"]
    infos = [f for f in findings if f.level == "INFO"]

    if blockers:
        lines.append(f"\n{C_RED}{C_BOLD}🚫 {len(blockers)} BLOCKER{C_RESET}")
        for f in blockers:
            lines.append(f"  {C_RED}❌ [{f.category}] {f.message}{C_RESET}")
            if f.snippet:
                lines.append(f"     Text: \"{f.snippet}\"")

    if warnings:
        lines.append(f"\n{C_YELLOW}{C_BOLD}⚠  {len(warnings)} WARNUNG{C_RESET}")
        for f in warnings:
            lines.append(f"  {C_YELLOW}! [{f.category}] {f.message}{C_RESET}")
            if f.snippet:
                lines.append(f"     Text: \"{f.snippet}\"")

    if infos:
        lines.append(f"\n{C_BLUE}{C_BOLD}ℹ  {len(infos)} HINWEIS (prüfen){C_RESET}")
        for f in infos:
            lines.append(f"  {C_BLUE}· [{f.category}] {f.message}{C_RESET}")
            if f.snippet:
                lines.append(f"     Text: \"{f.snippet[:150]}...\"")

    if not findings:
        lines.append(f"  {C_GREEN}✅ Keine automatisch erkennbaren Probleme.{C_RESET}")

    # Merkhilfe: Checks, die Skript NICHT ersetzt
    lines.append(f"\n{C_BOLD}Manuell immer noch zu prüfen:{C_RESET}")
    lines.append("  · Sachrichtigkeit jeder §-Referenz gegen Original-Gesetzestext")
    lines.append("  · Friedhofsflächen/Eröffnungsjahre gegen Primärquelle der Stadt")
    lines.append("  · Ob Aussagen wie 'als einziges Bundesland' wirklich durch Quelle gedeckt")
    lines.append("  · Ton: würde ein Angehöriger das als respektvoll empfinden?")

    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 _dev/bundesland-recheck.py <path> | --all")
        sys.exit(1)

    if args[0] == "--all":
        pages = sorted((ROOT / "bestattung-in").glob("*/index.html"))
    else:
        pages = [ROOT / args[0]] if not Path(args[0]).is_absolute() else [Path(args[0])]

    total_blockers = 0
    total_warnings = 0
    for page in pages:
        if not page.exists():
            print(f"{C_RED}Datei nicht gefunden: {page}{C_RESET}")
            continue
        findings = check_page(page)
        print(format_findings(page, findings))
        total_blockers += sum(1 for f in findings if f.level == "BLOCKER")
        total_warnings += sum(1 for f in findings if f.level == "WARN")

    # Exit-Code: nur Blocker blockieren automatisierte Pipelines
    print(f"\n{C_BOLD}Zusammenfassung: {total_blockers} Blocker, {total_warnings} Warnungen{C_RESET}")
    sys.exit(1 if total_blockers > 0 else 0)


if __name__ == "__main__":
    main()
