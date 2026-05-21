"""
Insert Bestatter-Wahl-Modul in 19 Cities ohne dieses Modul.
Template entspricht Münster-Pattern, city-name + Bundesland substituiert.
Eingefügt vor der FAQ-Sektion (oder vor Vorsorge wenn vorhanden).
"""
import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"

CITY_BL = {
    # NRW
    "aachen": ("NRW", "nordrhein-westfalen", "Nordrhein-Westfalen"),
    "bochum": ("NRW", "nordrhein-westfalen", "Nordrhein-Westfalen"),
    "bonn": ("NRW", "nordrhein-westfalen", "Nordrhein-Westfalen"),
    "gelsenkirchen": ("NRW", "nordrhein-westfalen", "Nordrhein-Westfalen"),
    "moenchengladbach": ("NRW", "nordrhein-westfalen", "Nordrhein-Westfalen"),
    "muelheim": ("NRW", "nordrhein-westfalen", "Nordrhein-Westfalen"),
    "oberhausen": ("NRW", "nordrhein-westfalen", "Nordrhein-Westfalen"),
    # BY
    "augsburg": ("Bayern", "bayern", "Bayern"),
    # BE
    "berlin": ("Berlin", "berlin", "Berlin"),
    # NL
    "braunschweig": ("Niedersachsen", "niedersachsen", "Niedersachsen"),
    "hannover": ("Niedersachsen", "niedersachsen", "Niedersachsen"),
    # SN
    "dresden": ("Sachsen", "sachsen", "Sachsen"),
    # BW
    "heidelberg": ("Baden-Württemberg", "baden-württemberg", "Baden-Württemberg"),
    # HE
    "kassel": ("Hessen", "hessen", "Hessen"),
    "wiesbaden": ("Hessen", "hessen", "Hessen"),
    # SH
    "kiel": ("Schleswig-Holstein", "schleswig-holstein", "Schleswig-Holstein"),
    "luebeck": ("Schleswig-Holstein", "schleswig-holstein", "Schleswig-Holstein"),
    # RP
    "mainz": ("Rheinland-Pfalz", "rheinland-pfalz", "Rheinland-Pfalz"),
    # BB
    "potsdam": ("Brandenburg", "brandenburg", "Brandenburg"),
}

# Display-Name override (e.g., directory "muelheim" → display "Mülheim an der Ruhr")
CITY_DISPLAY = {
    "aachen": "Aachen",
    "augsburg": "Augsburg",
    "berlin": "Berlin",
    "bochum": "Bochum",
    "bonn": "Bonn",
    "braunschweig": "Braunschweig",
    "dresden": "Dresden",
    "gelsenkirchen": "Gelsenkirchen",
    "hannover": "Hannover",
    "heidelberg": "Heidelberg",
    "kassel": "Kassel",
    "kiel": "Kiel",
    "luebeck": "Lübeck",
    "mainz": "Mainz",
    "moenchengladbach": "Mönchengladbach",
    "muelheim": "Mülheim an der Ruhr",
    "oberhausen": "Oberhausen",
    "potsdam": "Potsdam",
    "wiesbaden": "Wiesbaden",
}


def build_module(slug):
    city = CITY_DISPLAY[slug]
    bl_short, bl_slug, bl_name = CITY_BL[slug]
    landesverband = f"Landesverband {bl_short}" if bl_short != bl_name else f"Landesverband {bl_short}"
    return f"""  <div class="mr-section">
    <h2>Bestatter-Wahl in {city} — Qualitätskriterien</h2>
    <p>Eine gesetzliche Pflicht zur Beauftragung eines bestimmten Bestatters besteht nicht. Wer eine Bestattung in {city} organisiert, kann frei wählen — und sollte das auch nutzen, weil die Preisspannen zwischen Bestattungsunternehmen erheblich sind. Sechs Kriterien helfen bei der Auswahl:</p>
    <ul style="margin:8px 0 16px 20px;font-size:15px;line-height:1.7;color:var(--mr-text)">
      <li><strong>Mitgliedschaft im <a href="https://www.bestatter.de" rel="noopener" target="_blank">Bundesverband Deutscher Bestatter (BDB)</a></strong> bzw. im {landesverband} — Mitglieder verpflichten sich auf Berufsbild, Mindestleistungsverzeichnis und Verbraucherinformation. Mitgliedersuche mit Ortsfilter {city} auf bestatter.de.</li>
      <li><strong>RAL-Gütezeichen Bestattungsinstitut</strong> — jährlich überprüfte Anforderungen an Räumlichkeiten, Verfahren und Hygiene. Verleihende Stelle: Markenverband / RAL Deutsches Institut für Gütesicherung und Kennzeichnung.</li>
      <li><strong>Transparente Preisliste</strong> mit Aufschlüsselung nach Pflichtleistungen, Wahlleistungen und Drittkosten (Friedhof, Krematorium, Drittanbieter). Mündliche Schätzungen ohne schriftlichen Kostenvoranschlag sind ein Warnsignal.</li>
      <li><strong>Schriftlicher Kostenvoranschlag</strong> vor Auftragserteilung — Verbraucherzentrale und Stiftung Warentest empfehlen mindestens drei Angebote zum Vergleich der Einzelposten (Sarg/Urne, Versorgung, Transport, Trauerhalle, Trauerdruck), nicht nur des Gesamtpreises.</li>
      <li><strong>Erfahrung mit Sonderformen</strong>: muslimische, jüdische, freie oder konfessionelle Trauerfeiern, Auslandsüberführung, Wald- oder Seebestattung. Frage explizit nach Referenzen — gerade bei religiösen Bestattungen sind Abstimmung mit Gemeinde und Friedhofsverwaltung kritisch.</li>
      <li><strong>Vorsorgevertrag</strong>: Wer zu Lebzeiten Vorsorge treffen möchte, kann mit dem Bestatter einen Vorsorgevertrag mit treuhänderischer Hinterlegung des Bestattungsbeitrags vereinbaren — der <a href="/tools/vorsorge-check">Vorsorge-Check</a> hilft bei der Strukturierung.</li>
    </ul>
    <p>Tipp: Notiere Dir vor dem ersten Bestatter-Gespräch die wichtigsten Eckdaten (gewünschte Bestattungsart, Friedhof, Trauerfeier-Wünsche, Budget-Rahmen). Das macht den Vergleich der Angebote belastbarer und schützt vor Aufschlägen für Leistungen, die nicht benötigt werden. Alle Bestattungsformen im Überblick: <a href="/bestattungsarten">Bestattungsarten</a>; Kosten-Korridor: <a href="/bestattungskosten">Bestattungskosten in Deutschland</a>.</p>
    <div class="mr-crosslinks">
      <strong>Mehr zum Bestattungsrecht:</strong>
      <a href="/bestattung-in/{bl_slug}/">Bestattungsrecht {bl_name}</a>·
      <a href="/bestattungsarten">Bestattungsarten</a>·
      <a href="/bestattungskosten">Kosten-Vergleich</a>·
      <a href="/tools/bestattungskosten-rechner">Bestattungskosten-Rechner</a>
    </div>
  </div>

"""


# Smart anchor: find FAQ h2, then find the section opening that contains it
FAQ_H2_RE = re.compile(r'<h2[^>]*>[^<]*(?:Häufige|FAQ|Fragen)', re.IGNORECASE)
SECTION_OPEN_RE = re.compile(r'<(?:div|section)[^>]*class="[^"]*(?:mr-section|mr-faq)[^"]*"[^>]*>')
# Fallback: before mr-sources
SOURCES_RE = re.compile(r'<(?:div|section)[^>]*class="[^"]*mr-sources[^"]*"', re.MULTILINE)

processed = []
skipped_already = []
skipped_no_anchor = []

for slug, _ in CITY_BL.items():
    city_dir = BESTATTER / slug
    idx = city_dir / "index.html"
    if not idx.exists():
        skipped_no_anchor.append(slug + " (missing dir)")
        continue
    text = idx.read_text(encoding="utf-8", errors="replace")

    # Skip if already has Bestatter-Wahl-h2
    if re.search(r"<h2[^>]*>[^<]*Bestatter-Wahl in", text, re.IGNORECASE):
        skipped_already.append(slug)
        continue

    # Find FAQ h2 position
    faq_m = FAQ_H2_RE.search(text)
    insert_at = None
    if faq_m:
        # Search backwards from FAQ h2 position to find the containing section opening
        prefix = text[:faq_m.start()]
        last_open = None
        for sm in SECTION_OPEN_RE.finditer(prefix):
            last_open = sm
        if last_open:
            # Go back to start of the line where the section opens
            line_start = text.rfind("\n", 0, last_open.start()) + 1
            insert_at = line_start

    if insert_at is None:
        # Fallback: before mr-sources
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
for s in skipped_already:
    print(f"  {s}")
print(f"\nSkipped (no anchor): {len(skipped_no_anchor)}")
for s in skipped_no_anchor:
    print(f"  {s}")
