"""
Insert Sozialbestattung-Modul in 13 Cities ohne dieses Modul.
Phase-1-Variant: deterministisches Template mit BL-spezifischem §,
generische "Sozialamt der Stadt {City}"-Verweise.
Per-City Sozialamt-Details (Adresse/Tel/Email) sind separate Recherche-Aufgabe.
"""
import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"

# (city → bundesland-short, rangfolge-§, rangfolge-text, gesetzname)
CITY_BL = {
    "augsburg":     ("BY", "Art. 15 Bayerisches BestG",        "Ehegatten/Lebenspartner, Kinder, Eltern, Geschwister, Großeltern, Enkelkinder",                     "Bayerisches Bestattungsgesetz"),
    "muenchen":     ("BY", "Art. 15 Bayerisches BestG",        "Ehegatten/Lebenspartner, Kinder, Eltern, Geschwister, Großeltern, Enkelkinder",                     "Bayerisches Bestattungsgesetz"),
    "regensburg":   ("BY", "Art. 15 Bayerisches BestG",        "Ehegatten/Lebenspartner, Kinder, Eltern, Geschwister, Großeltern, Enkelkinder",                     "Bayerisches Bestattungsgesetz"),
    "berlin":       ("BE", "§ 21 BestattG BE",                  "Ehegatten/eingetragene Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder", "Berliner Bestattungsgesetz"),
    "dresden":      ("SN", "§ 10 Abs. 1 SächsBestG",            "Ehegatten/Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder",               "Sächsisches Bestattungsgesetz"),
    "erfurt":       ("TH", "§ 18 ThürBestG",                    "Ehegatten/Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder",               "Thüringer Bestattungsgesetz"),
    "essen":        ("NRW","§ 8 BestG NRW",                     "Ehegatten/eingetragene Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder", "Bestattungsgesetz Nordrhein-Westfalen"),
    "krefeld":      ("NRW","§ 8 BestG NRW",                     "Ehegatten/eingetragene Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder", "Bestattungsgesetz Nordrhein-Westfalen"),
    "mönchengladbach":("NRW","§ 8 BestG NRW",                   "Ehegatten/eingetragene Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder", "Bestattungsgesetz Nordrhein-Westfalen"),
    "halle":        ("ST", "§ 10 BestattG LSA",                 "Ehegatten/Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder",               "Bestattungsgesetz Sachsen-Anhalt"),
    "lübeck":       ("SH", "§ 13 Abs. 2 BestattG SH",          "Ehegatten/eingetragene Lebenspartner, volljährige Kinder, Eltern, Geschwister, Großeltern, Enkelkinder",                          "Bestattungsgesetz Schleswig-Holstein"),
    "mainz":        ("RP", "§ 9 BestG RLP",                    "Ehegatten/Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder",                "Bestattungsgesetz Rheinland-Pfalz"),
    "wiesbaden":    ("HE", "§ 13 FBG Hessen",                  "Ehepartner, Kinder, Eltern, Geschwister, Großeltern und Enkelkinder — ohne Rangfolge, gleichrangig",                                  "Hessisches Bestattungsgesetz"),
    "saarbruecken": ("SL", "§ 30 BestattG Saarland",           "Ehegatten/Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder",                "Saarländisches Bestattungsgesetz"),
}

CITY_DISPLAY = {
    "augsburg":         "Augsburg",
    "muenchen":         "München",
    "regensburg":       "Regensburg",
    "berlin":           "Berlin",
    "dresden":          "Dresden",
    "erfurt":           "Erfurt",
    "essen":            "Essen",
    "krefeld":          "Krefeld",
    "mönchengladbach":  "Mönchengladbach",
    "halle":            "Halle (Saale)",
    "lübeck":           "Lübeck",
    "mainz":            "Mainz",
    "wiesbaden":        "Wiesbaden",
    "saarbruecken":     "Saarbrücken",
}


def build_module(slug):
    city = CITY_DISPLAY[slug]
    bl_short, bl_par, rangfolge, gesetz = CITY_BL[slug]
    return f"""  <div class="mr-section">
    <h2>Sozialbestattung in {city} — wenn die Kosten nicht selbst getragen werden können</h2>
    <p>Reicht der Nachlass nicht aus und sind auch die bestattungspflichtigen Angehörigen finanziell nicht in der Lage, die Kosten zu tragen, übernimmt der Sozialhilfeträger nach <strong>§ 74 SGB XII</strong> die <em>erforderlichen</em> Bestattungskosten — also den ortsüblich angemessenen Rahmen einer einfachen, würdigen Bestattung. Wichtig: <strong>Den Antrag möglichst vor Beauftragung des Bestatters stellen</strong>, spätestens jedoch zeitnah nach der Bestattung. Eine rückwirkende Übernahme bereits beglichener Rechnungen ist nicht ausgeschlossen, in der Praxis aber an zusätzliche Nachweispflichten gebunden.</p>
    <h3>Wer ist antragsberechtigt?</h3>
    <p>Antragsberechtigt ist die Person, die nach <strong>{bl_par}</strong> ({gesetz}) zur Bestattung verpflichtet ist — in der gesetzlichen Rangfolge: <em>{rangfolge}</em>. Vorrangig haften zivilrechtlich die Erben (§ 1968 BGB) und Unterhaltspflichtige; das Sozialamt prüft, ob aus dem Nachlass oder von vorrangig Verpflichteten Mittel verfügbar sind. Die örtliche Zuständigkeit richtet sich nach § 98 Abs. 3 SGB XII: bei laufendem Sozialhilfebezug der verstorbenen Person bleibt der bisherige Träger zuständig, sonst der Träger am Sterbeort.</p>
    <h3>Höchstrichterliche Klärung: Erbausschlagung schließt Anspruch nicht aus</h3>
    <p>Das <strong>Bundessozialgericht</strong> hat mit Urteil vom <strong>25.08.2011 (Az. B 8 SO 20/10 R)</strong> entschieden, dass die Verpflichtung zur Tragung der Bestattungskosten nicht zwingend an die Erbenstellung anknüpft. Auch wer das Erbe ausgeschlagen hat, aber landesrechtlich bestattungspflichtig bleibt, kann unter den Voraussetzungen des § 74 SGB XII einen Anspruch auf Kostenübernahme haben — die Zumutbarkeit der Eigenfinanzierung ist gesondert zu prüfen. Eine pauschale Ablehnung wegen Erbausschlagung ist damit nicht zulässig.</p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Übernommen werden die erforderlichen Kosten für eine <em>einfache, aber würdige, den ortsüblichen Verhältnissen entsprechende Bestattung</em>: Sarg oder Urne in einfacher Ausführung, Überführung im Stadtgebiet, Grabnutzungsrecht für ein Reihengrab über die Ruhezeit, Beisetzungsgebühr, eine schlichte Trauerfeier am Grab. <strong>Nicht übernommen</strong> werden in der Regel Grabstein und Einfassung, dauerhafte Grabpflege, Trauerdruck, Blumenschmuck über das übliche Maß hinaus, Trauerkaffee oder eine Erweiterung zum Wahlgrab.</p>
    <h3>Ansprechpartner</h3>
    <p>Zuständig ist das <strong>Sozialamt der Stadt {city}</strong>. Die exakten Kontaktdaten (Adresse, Telefonnummer, E-Mail des zuständigen Sachgebiets Bestattungskosten) erhältst Du über den Bürgerservice der Stadt {city} (bundesweit einheitliche Behördennummer <a href="tel:115">115</a>) oder das Bürgerportal der Stadt. Vor Antragsstellung sollten alle Belege zum Vermögen und Einkommen der verstorbenen Person sowie zur eigenen finanziellen Lage gesammelt werden.</p>
  </div>

"""


# Smart anchor: find FAQ h2, then find the containing section opening
FAQ_H2_RE = re.compile(r'<h2[^>]*>[^<]*(?:Häufige|FAQ|Fragen)', re.IGNORECASE)
SECTION_OPEN_RE = re.compile(r'<(?:div|section)[^>]*class="[^"]*(?:mr-section|mr-faq)[^"]*"[^>]*>')
SOURCES_RE = re.compile(r'<(?:div|section)[^>]*class="[^"]*mr-sources[^"]*"', re.MULTILINE)

processed = []
skipped_already = []
skipped_no_anchor = []

for slug in CITY_BL:
    city_dir = BESTATTER / slug
    idx = city_dir / "index.html"
    if not idx.exists():
        skipped_no_anchor.append(slug + " (missing)")
        continue
    text = idx.read_text(encoding="utf-8", errors="replace")

    # Skip if already has Sozialbestattung h2
    if re.search(r"<h2[^>]*>[^<]*Sozialbestattung in", text, re.IGNORECASE):
        skipped_already.append(slug)
        continue

    # Find FAQ h2 position
    faq_m = FAQ_H2_RE.search(text)
    insert_at = None
    if faq_m:
        prefix = text[:faq_m.start()]
        last_open = None
        for sm in SECTION_OPEN_RE.finditer(prefix):
            last_open = sm
        if last_open:
            line_start = text.rfind("\n", 0, last_open.start()) + 1
            insert_at = line_start

    if insert_at is None:
        m = SOURCES_RE.search(text)
        if m:
            line_start = text.rfind("\n", 0, m.start()) + 1
            insert_at = line_start

    if insert_at is None:
        skipped_no_anchor.append(slug)
        continue

    module = build_module(slug)
    new_text = text[:insert_at] + module + text[insert_at:]
    idx.write_text(new_text, encoding="utf-8")
    processed.append(slug)

print(f"Processed: {len(processed)}")
for s in processed:
    print(f"  {s}")
print(f"\nSkipped (already): {len(skipped_already)}")
print(f"\nSkipped (no anchor): {len(skipped_no_anchor)}")
for s in skipped_no_anchor:
    print(f"  {s}")
