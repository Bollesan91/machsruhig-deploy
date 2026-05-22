"""
Insert Bestatter-Anfrage Lead-Form (Netlify Forms) in alle 50 indexierbaren City-Pages.
Form-Setup:
- data-netlify="true"
- Honeypot bot-field
- action="/danke-bestatter-anfrage"
- Hidden Stadt-Feld (auto-filled)

Position: Am Ende der Bestatter-Wahl-Sektion.
"""
import os
import re
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"

# Display-Names for cities (matching what's used in headlines)
CITY_DISPLAY = {
    "muelheim": "Mülheim an der Ruhr",
    "moenchengladbach": "Mönchengladbach",
    "luebeck": "Lübeck",
    "duesseldorf": "Düsseldorf",
    "nuernberg": "Nürnberg",
    "muenchen": "München",
    "muenster": "Münster",
    "saarbruecken": "Saarbrücken",
    "koeln": "Köln",
    "osnabrueck": "Osnabrück",
}


def get_display(slug):
    if slug in CITY_DISPLAY:
        return CITY_DISPLAY[slug]
    return slug.capitalize()


def build_leadform(slug, city):
    return f"""    <div class="mr-cta-block" style="background:var(--mr-bg-card);border:2px solid var(--mr-border);text-align:left;padding:28px 24px">
      <h2 style="text-align:center">Kostenlose Anfrage an Bestatter in {city}</h2>
      <p style="text-align:center">Wir leiten Deine Anfrage an bis zu 3 geprüfte Bestatter weiter. Innerhalb von 24 Stunden erhältst Du unverbindliche Angebote per Telefon oder Email. Kein Vertrag, kein Risiko, kein Druck.</p>
      <form name="bestatter-anfrage" method="POST" data-netlify="true" data-netlify-honeypot="bot-field" action="/danke-bestatter-anfrage" style="margin-top:20px;display:grid;gap:12px">
        <input type="hidden" name="form-name" value="bestatter-anfrage">
        <input type="hidden" name="stadt" value="{city}">
        <p hidden><label>Lass dieses Feld leer: <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
        <label style="display:block">
          <span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">Dein Name *</span>
          <input type="text" name="name" required style="width:100%;padding:10px 12px;border:1px solid #E8E0D6;border-radius:8px;font-size:15px">
        </label>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
          <label style="display:block">
            <span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">PLZ *</span>
            <input type="text" name="plz" required pattern="[0-9]{{5}}" maxlength="5" style="width:100%;padding:10px 12px;border:1px solid #E8E0D6;border-radius:8px;font-size:15px">
          </label>
          <label style="display:block">
            <span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">Zeitrahmen *</span>
            <select name="zeitrahmen" required style="width:100%;padding:10px 12px;border:1px solid #E8E0D6;border-radius:8px;font-size:15px;background:#fff">
              <option value="">Bitte wählen</option>
              <option value="akut">Akut — Bestattung steht an</option>
              <option value="planung">In den nächsten Wochen</option>
              <option value="vorsorge">Vorsorge für später</option>
            </select>
          </label>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
          <label style="display:block">
            <span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">Email</span>
            <input type="email" name="email" style="width:100%;padding:10px 12px;border:1px solid #E8E0D6;border-radius:8px;font-size:15px">
          </label>
          <label style="display:block">
            <span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">Telefon (optional)</span>
            <input type="tel" name="telefon" style="width:100%;padding:10px 12px;border:1px solid #E8E0D6;border-radius:8px;font-size:15px">
          </label>
        </div>
        <label style="display:block">
          <span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">Bestattungsart (optional)</span>
          <select name="bestattungsart" style="width:100%;padding:10px 12px;border:1px solid #E8E0D6;border-radius:8px;font-size:15px;background:#fff">
            <option value="">Noch unentschieden / Beratungsbedarf</option>
            <option value="erdbestattung">Erdbestattung</option>
            <option value="feuerbestattung">Feuerbestattung (Urne)</option>
            <option value="seebestattung">Seebestattung</option>
            <option value="waldbestattung">Wald-/Baumbestattung</option>
            <option value="anonym">Anonyme Beisetzung</option>
          </select>
        </label>
        <label style="display:block">
          <span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">Anmerkungen (optional)</span>
          <textarea name="anmerkungen" rows="3" style="width:100%;padding:10px 12px;border:1px solid #E8E0D6;border-radius:8px;font-size:15px;resize:vertical"></textarea>
        </label>
        <label style="display:flex;gap:8px;align-items:flex-start;font-size:13px;color:var(--mr-text-muted)">
          <input type="checkbox" name="datenschutz" required style="margin-top:3px">
          <span>Ich bin einverstanden, dass meine Daten zur Bearbeitung meiner Anfrage gespeichert und an passende Bestatter weitergeleitet werden. <a href="/datenschutz" target="_blank">Datenschutz</a></span>
        </label>
        <button type="submit" class="cta-primary" style="margin-top:8px;border:none;cursor:pointer;font-family:inherit">Anfrage senden — kostenlos &amp; unverbindlich</button>
        <p style="font-size:12px;color:var(--mr-text-muted);text-align:center;margin-top:4px">Wir leiten Deine Anfrage spamfrei weiter. Du erhältst Angebote von bis zu 3 Bestattern in {city}. Kein automatischer Vertrag, kein Newsletter ohne Einwilligung.</p>
      </form>
    </div>

"""


# Insertion-Anker: am Ende der Bestatter-Wahl-Section
# Match: "Bestatter-Wahl", "Bestatter ... wählen", "Bestatter ... auswählen", "Bestatter und ..."
BEST_WAHL_H2_RE = re.compile(r'<h2[^>]*>[^<]*[Bb]estatter(?:-Wahl|[^<]*(?:wählen|auswählen|Wahl|Auswahl|Qualität|Verbände))', re.IGNORECASE)
NEXT_SECTION_RE = re.compile(r'<(?:div|section)[^>]*class="(?:mr-section|mr-faq|mr-sources|mr-trust)', re.IGNORECASE)


def patch_city(slug):
    p = BESTATTER / slug / "index.html"
    if not p.exists():
        return "missing"
    text = p.read_text(encoding="utf-8", errors="replace")

    # Skip if form already present
    if 'name="bestatter-anfrage"' in text:
        return "already"

    # Skip noindex
    if re.search(r'<meta[^>]*name="robots"[^>]*content="[^"]*noindex', text, re.IGNORECASE):
        return "noindex"

    city = get_display(slug)
    form = build_leadform(slug, city)

    # Find Bestatter-Wahl-h2
    m = BEST_WAHL_H2_RE.search(text)
    if not m:
        return "no-bestwahl-section"

    # Find next section after that h2
    after = text[m.end():]
    next_m = NEXT_SECTION_RE.search(after)
    if not next_m:
        return "no-next-section"

    insertion_zone_end = m.end() + next_m.start()
    section_block = text[m.end():insertion_zone_end]
    closing_offset = max(section_block.rfind("</div>"), section_block.rfind("</section>"))
    if closing_offset == -1:
        return "no-closing"

    absolute_insert = m.end() + closing_offset
    new_text = text[:absolute_insert] + form + text[absolute_insert:]
    p.write_text(new_text, encoding="utf-8")
    return "patched"


processed = []
skipped = []
for c in sorted(BESTATTER.iterdir()):
    if not c.is_dir():
        continue
    if c.name in {"lübeck", "mönchengladbach"}:
        continue
    status = patch_city(c.name)
    if status == "patched":
        processed.append(c.name)
    else:
        skipped.append((c.name, status))

print(f"Processed: {len(processed)}")
for s in processed[:10]:
    print(f"  {s}")
if len(processed) > 10:
    print(f"  ... +{len(processed)-10} more")
print(f"\nSkipped: {len(skipped)}")
for s, reason in skipped:
    print(f"  {s}: {reason}")
