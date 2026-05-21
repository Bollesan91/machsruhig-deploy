"""
Insert Quellen-Section in 4 Cities ohne dieses Modul.
Generic template mit Stadt-Hauptseite + Bundesland-Gesetz + BSG + interne BL-Page.
"""
import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"


CITY_INFO = {
    "braunschweig": dict(
        display="Braunschweig",
        bl_slug="niedersachsen",
        bl_name="Niedersachsen",
        bl_law_short="NBestattG",
        bl_law_url="https://www.aeternitas.de/inhalt/bestattungsgesetze/niedersachsen",
        city_friedhof="https://www.braunschweig.de/leben/umwelt_naturschutz/friedhof_bestattung/",
        city_friedhof_label="Stadt Braunschweig — Friedhof und Bestattung",
    ),
    "essen": dict(
        display="Essen",
        bl_slug="nordrhein-westfalen",
        bl_name="Nordrhein-Westfalen",
        bl_law_short="BestG NRW",
        bl_law_url="https://recht.nrw.de/lrgv/gesetz/19022022-gesetz-ueber-das-friedhofs-und-bestattungswesen-bestattungsgesetz-bestg-nrw",
        city_friedhof="https://www.essen.de/leben/buergerservice/dienstleistungen_a_z/bestattungen.de.html",
        city_friedhof_label="Stadt Essen — Bestattungen und Friedhöfe",
    ),
    "gelsenkirchen": dict(
        display="Gelsenkirchen",
        bl_slug="nordrhein-westfalen",
        bl_name="Nordrhein-Westfalen",
        bl_law_short="BestG NRW",
        bl_law_url="https://recht.nrw.de/lrgv/gesetz/19022022-gesetz-ueber-das-friedhofs-und-bestattungswesen-bestattungsgesetz-bestg-nrw",
        city_friedhof="https://www.gelsendienste.de/",
        city_friedhof_label="GELSENDIENSTE — Friedhöfe und Bestattungen",
    ),
    "hagen": dict(
        display="Hagen",
        bl_slug="nordrhein-westfalen",
        bl_name="Nordrhein-Westfalen",
        bl_law_short="BestG NRW",
        bl_law_url="https://recht.nrw.de/lrgv/gesetz/19022022-gesetz-ueber-das-friedhofs-und-bestattungswesen-bestattungsgesetz-bestg-nrw",
        city_friedhof="https://www.hagen.de/web/de/fachbereiche/fb_68/index.html",
        city_friedhof_label="Stadt Hagen — Hagener Betrieb für Stadtentwässerung, Friedhöfe und Forst",
    ),
}


def build_section(slug):
    info = CITY_INFO[slug]
    city = info["display"]
    return f"""  <div class="mr-sources">
    <h2>Quellen</h2>
    <ul>
      <li><a href="{info['city_friedhof']}" rel="noopener" target="_blank">{info['city_friedhof_label']}</a></li>
      <li><a href="{info['bl_law_url']}" rel="noopener" target="_blank">{info['bl_law_short']} — Volltext der Landes-Bestattungsregelung</a></li>
      <li><a href="https://www.gesetze-im-internet.de/sgb_12/__74.html" rel="noopener" target="_blank">§ 74 SGB XII — Bestattungskosten (Sozialhilfeträger)</a></li>
      <li><a href="https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2011/2011_08_25_B_8_SO_20_10_R.html" rel="noopener" target="_blank">BSG, Urteil vom 25.08.2011 — B 8 SO 20/10 R (Zumutbarkeitsmaßstab Bestattungskosten)</a></li>
      <li><a href="https://www.gesetze-im-internet.de/pstg/__28.html" rel="noopener" target="_blank">§ 28 PStG — Anzeige des Sterbefalls (Personenstandsgesetz)</a></li>
      <li><a href="/bestattung-in/{info['bl_slug']}/">machsruhig — Bestattung in {info['bl_name']} (Bundeslandseite mit allen §-Verweisen)</a></li>
      <li><a href="https://www.bestatter.de" rel="noopener" target="_blank">Bundesverband Deutscher Bestatter (BDB) — Mitgliedersuche mit Ortsfilter {city}</a></li>
    </ul>
  </div>

"""


# Anchor: insert AFTER FAQ-Section but BEFORE mr-trust or before footer/main close
# Easier: insert before <div class="mr-trust"> if exists, else before </main>
TRUST_RE = re.compile(r'<div class="mr-trust"', re.IGNORECASE)
MAIN_END_RE = re.compile(r'</main>', re.IGNORECASE)

processed = []
skipped_already = []
skipped_no_anchor = []

for slug in CITY_INFO:
    p = BESTATTER / slug / "index.html"
    if not p.exists():
        skipped_no_anchor.append(slug + " (missing)")
        continue
    text = p.read_text(encoding="utf-8", errors="replace")

    # Skip if already has mr-sources or h2 Quellen
    if 'class="mr-sources"' in text or re.search(r"<h2[^>]*>[^<]*Quellen", text, re.IGNORECASE):
        skipped_already.append(slug)
        continue

    # Find anchor
    m = TRUST_RE.search(text)
    if not m:
        m = MAIN_END_RE.search(text)
    if not m:
        skipped_no_anchor.append(slug)
        continue

    line_start = text.rfind("\n", 0, m.start()) + 1
    section = build_section(slug)
    new_text = text[:line_start] + section + text[line_start:]
    p.write_text(new_text, encoding="utf-8")
    processed.append(slug)

print(f"Processed: {len(processed)}")
for s in processed:
    print(f"  {s}")
print(f"\nSkipped (already): {len(skipped_already)}")
for s in skipped_already:
    print(f"  {s}")
print(f"\nSkipped (no anchor): {len(skipped_no_anchor)}")
