"""
Verfeinere Essen § 11 → § 11 Abs. 1 + Material-Hinweis auf Friedhofssatzung.
Helper-V3 zweite Verifikation bestätigte: § 11 Abs. 1 BestG NRW regelt
Verrottungs-/Verwesungsfähigkeit (Abs. 1 ist die richtige Untergliederung).
"""
import os
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
p = ROOT / "bestatter" / "essen" / "index.html"

text = p.read_text(encoding="utf-8", errors="replace")
orig = text

# FAQ-JSON-LD
old_schema = "Das BestG NRW enthält keinen ausdrücklichen Sargzwang. Anforderungen an Bestattungsbehältnisse (Verrottungs- und Verwesungsfähigkeit) ergeben sich aus § 11 BestG NRW; die konkrete Sarg- oder Tuchbestattungsregelung bestimmt die Friedhofssatzung der Stadt Essen (§ 4 BestG NRW als Satzungsermächtigung). Sarglose Bestattung aus religiösen Gründen — etwa muslimische Tuchbestattung — ist nach der Essener Friedhofssatzung möglich; Angehörige sollten dies konkret bei Grün und Gruga Essen anfragen."
new_schema = "Das BestG NRW enthält keinen ausdrücklichen Sargzwang. Die grundlegende Anforderung, dass Bestattungsbehältnisse, Ausstattung und Totenbekleidung verrottungs- bzw. verwesungsfähig sein müssen, ergibt sich aus § 11 Abs. 1 BestG NRW (i.V.m. § 4 Abs. 2 zur Ruhezeit). Konkrete Materialvorgaben (Holzart, Lacke etc.) regelt das Landesgesetz nicht — diese stehen in der Friedhofssatzung der Stadt Essen (Satzungsermächtigung § 4 BestG NRW). Sarglose Bestattung aus religiösen Gründen — etwa muslimische Tuchbestattung — ist nach der Essener Friedhofssatzung möglich; Angehörige sollten dies konkret bei Grün und Gruga Essen anfragen."
text = text.replace(old_schema, new_schema)

# Fließtext
old_flow = "Das BestG NRW enthält keinen ausdrücklichen Sargzwang. Anforderungen an Bestattungsbehältnisse (Verrottungs- und Verwesungsfähigkeit) stehen in § 11 BestG NRW; ob und unter welchen Bedingungen eine sarglose Bestattung — etwa muslimische Tuchbestattung — möglich ist, regelt die örtliche Friedhofssatzung der Stadt Essen nach § 4 BestG NRW."
new_flow = "Das BestG NRW enthält keinen ausdrücklichen Sargzwang. Die Vorgabe, dass Bestattungsbehältnisse innerhalb der Ruhezeit verrotten und die Verwesung ermöglicht werden muss, ergibt sich aus § 11 Abs. 1 BestG NRW (i.V.m. § 4 Abs. 2). Ob und unter welchen Bedingungen eine sarglose Bestattung — etwa muslimische Tuchbestattung — möglich ist, regelt die örtliche Friedhofssatzung der Stadt Essen (Satzungsermächtigung § 4 BestG NRW)."
text = text.replace(old_flow, new_flow)

if text != orig:
    p.write_text(text, encoding="utf-8")
    print("essen: patched (§ 11 → § 11 Abs. 1 + Material-Hinweis)")
else:
    print("essen: no-change")
