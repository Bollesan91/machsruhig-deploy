"""
Apply Sozial-Research-Outputs auf city pages.
Ersetzt den generischen "Sozialamt der Stadt {City}"-Absatz durch
den city-specific HTML_SNIPPET aus Helper-V3 Writer-Outputs.
"""
import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"

# Per-city snippet (extracted from Helper-V3 outputs)
SNIPPETS = {
    "augsburg": """<p><strong>Amt für Soziale Leistungen, Senioren und Menschen mit Behinderung &ndash; Bestattungskosten</strong><br>
    Metzgplatz 1, 86150 Augsburg<br>
    Telefon: <a href="tel:+498213249558">0821 324-9558</a> (A&ndash;L) / <a href="tel:+498213249557">0821 324-9557</a> (M&ndash;Z)<br>
    E-Mail: <a href="mailto:bestattungskosten.soziales@augsburg.de">bestattungskosten.soziales@augsburg.de</a></p>""",

    "berlin": """<p><strong>Amt für Soziales des zuständigen Berliner Bezirksamts</strong><br>
    In Berlin ist die Sozialhilfe dezentral über die zwölf Bezirksämter organisiert. Zuständig ist grundsätzlich das Amt für Soziales des Bezirks am letzten Wohnsitz der verstorbenen Person (mit Berliner Meldeadresse) bzw. am Sterbeort (ohne Berliner Meldeadresse). Bei zuvor bezogener Sozialhilfe ist der Träger zuständig, von dem die verstorbene Person zuletzt Leistungen bezog (§ 98 SGB XII).<br>
    Service Berlin (zentrale Behördennummer): <a href="tel:115">115</a><br>
    Antrag &amp; Hinweise: <a href="https://service.berlin.de/dienstleistung/324527/" rel="noopener" target="_blank">service.berlin.de — Bestattungskosten beantragen</a><br>
    Übersicht aller Sozialämter: <a href="https://service.berlin.de/standorte/sozialaemter/" rel="noopener" target="_blank">service.berlin.de/standorte/sozialaemter</a></p>""",

    "dresden": """<p><strong>Landeshauptstadt Dresden, Sozialamt &ndash; Abt. Soziale Leistungen</strong><br>
    Junghansstraße 2, 01277 Dresden<br>
    Telefon: <a href="tel:+493514884861">0351 4884861</a><br>
    E-Mail: <a href="mailto:sozialleistungen@dresden.de">sozialleistungen@dresden.de</a></p>""",

    "erfurt": """<p><strong>Stadtverwaltung Erfurt &ndash; Amt für Soziales (Bürgerservice Soziales)</strong><br>
    Juri-Gagarin-Ring 150, 99084 Erfurt<br>
    Telefon: <a href="tel:+493616556161">0361 655-6161</a><br>
    E-Mail: <a href="mailto:soziales@erfurt.de">soziales@erfurt.de</a></p>""",

    "essen": """<p><strong>Amt für Soziales und Wohnen der Stadt Essen</strong><br>
    Altendorfer Str. 103, 45143 Essen<br>
    Telefon: <a href="tel:+492018850555">0201 88-50555</a></p>""",

    "halle": """<p><strong>Stadt Halle (Saale), Fachbereich Soziales, Abteilung Existenzsichernde Leistungen</strong><br>
    Südpromenade 30, 06128 Halle (Saale)<br>
    Telefon: <a href="tel:+493452215440">0345 2215440</a></p>""",

    "krefeld": """<p><strong>Stadt Krefeld, Fachbereich Soziales und Senioren — Abteilung Sozialhilfe und Unterhaltsvorschuss</strong><br>
    Konrad-Adenauer-Platz 17, 47803 Krefeld<br>
    Telefon: <a href="tel:+4921518630180">02151 86-3018</a><br>
    E-Mail: <a href="mailto:bestattungskosten-sozialhilfe@krefeld.de">bestattungskosten-sozialhilfe@krefeld.de</a></p>""",

    "lübeck": """<p><strong>Hansestadt Lübeck, Bereich Soziale Sicherung</strong><br>
    Kronsforder Allee 2-6, 23560 Lübeck<br>
    Telefon: <a href="tel:+49451115">0451 115</a><br>
    E-Mail: <a href="mailto:bestattungskosten@luebeck.de">bestattungskosten@luebeck.de</a></p>""",

    "mainz": """<p><strong>Landeshauptstadt Mainz, Amt für soziale Leistungen</strong><br>
    Stadthaus Kaiserstraße (Lauteren-Flügel), Kaiserstraße 3, 55116 Mainz<br>
    Telefon: <a href="tel:+496131115">06131 115</a></p>""",

    "muenchen": """<p><strong>Landeshauptstadt München, Sozialreferat &ndash; Amt für Soziale Sicherung, Wirtschaftliche Hilfen</strong><br>
    Sankt-Martin-Straße 53, 81669 München<br>
    Telefon: <a href="tel:+498923368323">089 233-68323</a><br>
    E-Mail: <a href="mailto:s-i-wh3.soz@muenchen.de">s-i-wh3.soz@muenchen.de</a></p>""",

    "mönchengladbach": """<p><strong>Stadt Mönchengladbach, Fachbereich Soziales und Wohnen (50), Sozial- und Eingliederungshilfe (50/20)</strong><br>
    Fliethstraße 86-88, 41061 Mönchengladbach<br>
    Telefon: <a href="tel:+492161258325">02161 25-8325</a><br>
    E-Mail: <a href="mailto:FB50-Bestattungskosten@moenchengladbach.de">FB50-Bestattungskosten@moenchengladbach.de</a></p>""",

    "regensburg": """<p><strong>Stadt Regensburg, Amt für Soziales &ndash; Abteilung Sozialhilfe</strong><br>
    Johann-Hösl-Straße 11b, 93053 Regensburg<br>
    Telefon: <a href="tel:+499415071502">0941 507-1502</a></p>""",

    "saarbruecken": """<p><strong>Regionalverband Saarbrücken &ndash; Sozialamt</strong><br>
    Europaallee 11, 66113 Saarbrücken<br>
    Telefon: <a href="tel:+496815064949">0681 506-4949</a><br>
    E-Mail: <a href="mailto:sozialamt@rvsbr.de">sozialamt@rvsbr.de</a></p>""",

    "wiesbaden": """<p><strong>Landeshauptstadt Wiesbaden &ndash; Sozialleistungs- und Jobcenter, Sozialhilfe (§ 74 SGB XII)</strong><br>
    Schwalbacher Straße 26, 65183 Wiesbaden<br>
    Telefon: <a href="tel:+49611313826">0611 313826</a><br>
    E-Mail: <a href="mailto:sozialhilfe@wiesbaden.de">sozialhilfe@wiesbaden.de</a></p>""",
}

# Suffix added after the snippet
SUFFIX = """
    <p>Vor Antragsstellung sollten alle Belege zum Vermögen und Einkommen der verstorbenen Person sowie zur eigenen finanziellen Lage gesammelt werden.</p>"""


# Find the generic placeholder paragraph (multi-variant)
PLACEHOLDER_RES = [
    re.compile(
        r'<p>Zuständig ist das <strong>Sozialamt der Stadt [^<]+</strong>\.\s*Die exakten Kontaktdaten[^<]*\(Adresse[^<]*\)[^<]*erhältst Du über den Bürgerservice[^<]*<a href="tel:115">115</a>[^<]*</p>\s*',
        re.DOTALL,
    ),
    re.compile(
        r'<p>Zuständig ist das <strong>Sozialamt der Stadt [^<]+?</strong>\..*?<a href="tel:115">115</a>.*?gesammelt werden\.</p>',
        re.DOTALL,
    ),
]


def apply_city(slug):
    city_dir = BESTATTER / slug
    idx = city_dir / "index.html"
    if not idx.exists():
        return "missing"
    if slug not in SNIPPETS:
        return "no-snippet"

    text = idx.read_text(encoding="utf-8", errors="replace")
    snippet = SNIPPETS[slug] + SUFFIX

    new_text = None
    for pat in PLACEHOLDER_RES:
        if pat.search(text):
            new_text = pat.sub(snippet, text, count=1)
            break

    if new_text is None:
        return "no-placeholder"

    if new_text == text:
        return "no-change"

    idx.write_text(new_text, encoding="utf-8")
    return "patched"


if __name__ == "__main__":
    for slug in SNIPPETS:
        status = apply_city(slug)
        print(f"  {slug}: {status}")
