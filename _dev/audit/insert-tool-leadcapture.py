"""
Insert Email-Capture-Block + Lead-Hook nach dem React-Tool-Container.
Tools: bestattungskosten-rechner, vorsorge-check, beerdigungsplaner
"""
import os
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
TOOLS = ROOT / "tools"


def build_lead_block(form_name, tool_label, intro_text, success_url):
    return f"""

  <section style="max-width:680px;margin:48px auto 0;padding:0 20px">
    <div class="mr-cta-block" style="background:#FFFDF9;border:2px solid #E8E0D6;border-radius:12px;padding:28px 24px;text-align:left">
      <h2 style="font-family:'Fraunces',serif;font-size:22px;font-weight:700;margin-bottom:8px;text-align:center">{tool_label}</h2>
      <p style="font-size:15px;color:#73655A;margin-bottom:20px;text-align:center">{intro_text}</p>
      <form name="{form_name}" method="POST" data-netlify="true" data-netlify-honeypot="bot-field" action="{success_url}" style="display:grid;gap:12px">
        <input type="hidden" name="form-name" value="{form_name}">
        <p hidden><label>Lass dieses Feld leer: <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
          <label style="display:block">
            <span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">Dein Name *</span>
            <input type="text" name="name" required style="width:100%;padding:10px 12px;border:1px solid #E8E0D6;border-radius:8px;font-size:15px">
          </label>
          <label style="display:block">
            <span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">Email *</span>
            <input type="email" name="email" required style="width:100%;padding:10px 12px;border:1px solid #E8E0D6;border-radius:8px;font-size:15px">
          </label>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
          <label style="display:block">
            <span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">PLZ (optional)</span>
            <input type="text" name="plz" pattern="[0-9]{{5}}" maxlength="5" style="width:100%;padding:10px 12px;border:1px solid #E8E0D6;border-radius:8px;font-size:15px">
          </label>
          <label style="display:block">
            <span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">Zeitrahmen (optional)</span>
            <select name="zeitrahmen" style="width:100%;padding:10px 12px;border:1px solid #E8E0D6;border-radius:8px;font-size:15px;background:#fff">
              <option value="">Bitte wählen</option>
              <option value="akut">Akut</option>
              <option value="planung">Planung</option>
              <option value="vorsorge">Vorsorge</option>
            </select>
          </label>
        </div>
        <label style="display:flex;gap:8px;align-items:flex-start;font-size:13px;color:#73655A">
          <input type="checkbox" name="datenschutz" required style="margin-top:3px">
          <span>Ich bin einverstanden, dass meine Email-Adresse zur Bearbeitung meiner Anfrage gespeichert wird. <a href="/datenschutz" target="_blank">Datenschutz</a></span>
        </label>
        <button type="submit" class="cta-primary" style="margin-top:8px;padding:14px 32px;background:#7A6B5D;color:#fff;border:none;border-radius:99px;font-weight:600;font-size:15px;cursor:pointer;font-family:inherit">Anfrage senden &mdash; kostenlos &amp; unverbindlich</button>
        <p style="font-size:12px;color:#73655A;text-align:center;margin-top:4px">Spamfrei · DSGVO-konform · Du kannst jederzeit widersprechen</p>
      </form>
    </div>
  </section>

"""


CONFIGS = {
    "bestattungskosten-rechner": {
        "form_name": "tool-lead-bestattungskosten",
        "tool_label": "Wir senden Dir Dein Ergebnis &mdash; und 3 Bestatter-Angebote",
        "intro_text": "Wir mailen Dir Dein Kostenrahmen-Ergebnis zur späteren Referenz und holen optional 3 unverbindliche Angebote von Bestattern in Deiner Region ein. Kein Newsletter, kein Spam.",
        "success_url": "/danke-bestatter-anfrage",
    },
    "vorsorge-check": {
        "form_name": "tool-lead-vorsorgecheck",
        "tool_label": "Vorsorge-Plan per Email &mdash; mit Folge-Tipps",
        "intro_text": "Wir mailen Dir Deine Vorsorge-Lücken-Auswertung. Optional: 7-tägige Email-Sequenz mit konkreten Schritten (Patientenverfügung, Testament, Vorsorgevollmacht).",
        "success_url": "/danke-bestatter-anfrage",
    },
    "beerdigungsplaner": {
        "form_name": "tool-lead-beerdigungsplaner",
        "tool_label": "Plan per Email &mdash; und Bestatter-Angebote",
        "intro_text": "Wir mailen Dir Deinen Beerdigungs-Plan. Optional: bis zu 3 Bestatter aus Deiner Region rufen unverbindlich zurück. Kein Vertrag, kein Druck.",
        "success_url": "/danke-bestatter-anfrage",
    },
}


def patch_tool(slug):
    p = TOOLS / slug / "index.html"
    if not p.exists():
        return "missing"
    text = p.read_text(encoding="utf-8", errors="replace")

    if slug not in CONFIGS:
        return "no-config"
    cfg = CONFIGS[slug]

    # Skip if form already present
    if f'name="{cfg["form_name"]}"' in text:
        return "already"

    # Insert AFTER </main>
    block = build_lead_block(
        cfg["form_name"],
        cfg["tool_label"],
        cfg["intro_text"],
        cfg["success_url"],
    )

    # Find </main>
    end_main = text.find("</main>")
    if end_main == -1:
        return "no-main-close"

    new_text = text[:end_main] + block + text[end_main:]
    p.write_text(new_text, encoding="utf-8")
    return "patched"


for slug in CONFIGS:
    print(f"  {slug}: {patch_tool(slug)}")
