"""
Apply OoS-Findings fixes:
- Hamburg: HmbBestattG → HmbBestG (offizielle Abkürzung, ohne tt) + FAQ Q4 § 6 ergänzen
- Essen: erfundene § 15 Glaubensgemeinschafts-Klausel raus + § 13 Abs. 4 → § 13 Abs. 3
- Chemnitz: Heike Decker → Wilma Meyer (FAQ Q7 + Friedhof-Beschreibung)
"""
import os
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"


def fix_hamburg():
    p = BESTATTER / "hamburg" / "index.html"
    text = p.read_text(encoding="utf-8", errors="replace")
    orig = text
    # HmbBestattG → HmbBestG (offizielle Abkürzung)
    text = text.replace("HmbBestattG", "HmbBestG")
    # FAQ Q4: ergänze "§ 6 HmbBestG" in den FAQ-Text (HTML + JSON-LD)
    old_q4 = "Überführung in Leichenhalle innerhalb 36 Stunden (gesetzlich verpflichtend)"
    new_q4 = "Überführung in Leichenhalle innerhalb 36 Stunden (§ 6 HmbBestG)"
    text = text.replace(old_q4, new_q4)
    if text != orig:
        p.write_text(text, encoding="utf-8")
        return "patched"
    return "no-change"


def fix_essen():
    p = BESTATTER / "essen" / "index.html"
    text = p.read_text(encoding="utf-8", errors="replace")
    orig = text

    # FAQ JSON-LD Q6 — erfundene § 15 Glaubensgemeinschaft raus
    old_schema = "Das BestG NRW enthält in § 15 keinen ausdrücklichen allgemeinen Sargzwang; die Vorschrift sieht vor, dass Mitgliedern bestimmter Glaubensgemeinschaften eine sarglose Bestattung ermöglicht werden kann, soweit deren religiöse Vorschriften dies erfordern. Maßgeblich für die kommunalen Essener Friedhöfe ist zusätzlich die Friedhofssatzung der Stadt Essen in der aktuell gültigen Fassung – Angehörige sollten dies konkret bei Grün und Gruga Essen anfragen."
    new_schema = "Das BestG NRW enthält keinen ausdrücklichen Sargzwang. Anforderungen an Bestattungsbehältnisse (Verrottungs- und Verwesungsfähigkeit) ergeben sich aus § 11 BestG NRW; die konkrete Sarg- oder Tuchbestattungsregelung bestimmt die Friedhofssatzung der Stadt Essen (§ 4 BestG NRW als Satzungsermächtigung). Sarglose Bestattung aus religiösen Gründen — etwa muslimische Tuchbestattung — ist nach der Essener Friedhofssatzung möglich; Angehörige sollten dies konkret bei Grün und Gruga Essen anfragen."
    text = text.replace(old_schema, new_schema)

    # FAQ HTML (mr-faq-body) — selber Block, etwas anderer Wortlaut
    # Stelle 681 sollte gleich sein wie schema, also ersetzen wir den exakten String
    # → bereits durch replace oben abgedeckt

    # Fließtext-Variante (Zeile 396) — slightly different wording
    old_flow = "Das BestG NRW enthält in § 15 keinen ausdrücklichen allgemeinen Sargzwang – die Vorschrift sieht vor, dass Mitgliedern bestimmter Glaubensgemeinschaften eine Bestattung ohne Sarg ermöglicht werden kann, soweit deren religiöse Vorschriften dies erfordern; ob eine sarglose Bestattung konkret möglich ist, regelt ergänzend die örtliche Friedhofssatzung."
    new_flow = "Das BestG NRW enthält keinen ausdrücklichen Sargzwang. Anforderungen an Bestattungsbehältnisse (Verrottungs- und Verwesungsfähigkeit) stehen in § 11 BestG NRW; ob und unter welchen Bedingungen eine sarglose Bestattung — etwa muslimische Tuchbestattung — möglich ist, regelt die örtliche Friedhofssatzung der Stadt Essen nach § 4 BestG NRW."
    text = text.replace(old_flow, new_flow)

    # § 13 Abs. 4 → § 13 Abs. 3 (im Krematorium-Absatz)
    text = text.replace("§ 13 Abs. 4 BestG NRW", "§ 13 Abs. 3 BestG NRW")

    if text != orig:
        p.write_text(text, encoding="utf-8")
        return "patched"
    return "no-change"


def fix_chemnitz():
    p = BESTATTER / "chemnitz" / "index.html"
    text = p.read_text(encoding="utf-8", errors="replace")
    orig = text
    # Heike Decker → Wilma Meyer (FAQ + Fließtext)
    text = text.replace("Betriebsleiterin ist Heike Decker.", "Betriebsleiterin ist Wilma Meyer (Bestellung durch den Stadtrat im Februar 2024).")
    if text != orig:
        p.write_text(text, encoding="utf-8")
        return "patched"
    return "no-change"


for name, fn in (("hamburg", fix_hamburg), ("essen", fix_essen), ("chemnitz", fix_chemnitz)):
    print(f"  {name}: {fn()}")
