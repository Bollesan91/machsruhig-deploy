"""
YMYL Fact-Fixes Batch-2 (Helper-V3 Round-2 Verdicts):
- Hamburg: § 3 HmbBestG -> § 2 HmbBestG (Veranlassung Leichenschau, NEU 2020)
- Berlin Line 571: § 21 BestattG BE (alt, abgeschafft 2024) -> § 16 BestattG BE (Bestattungspflichtige)
  + Rangfolge: Großeltern/Enkelkinder vertauscht -> § 16 Abs. 1: Enkelkinder VOR Großeltern
- München: 96 Stunden -> acht Tage (seit 1.4.2021, BestV-Novelle, GVBl. 2021 S. 138)
  + Art. 15 BayBestG -> Art. 15 Abs. 2 BayBestG i.V.m. § 15 BestV (präziser)
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
BESTATTER = ROOT / "bestatter"

results = []

# ---------- HAMBURG ----------
hh = BESTATTER / "hamburg" / "index.html"
txt = hh.read_text(encoding="utf-8")
before = txt.count("§ 3 HmbBestG")
txt = txt.replace(
    "In Krankenhäusern und Pflegeheimen veranlasst die Einrichtung die Leichenschau (§ 3 HmbBestG).",
    "In Krankenhäusern und Pflegeheimen veranlasst die Einrichtung die Leichenschau (§ 2 HmbBestG).",
)
after = txt.count("§ 3 HmbBestG")
hh.write_text(txt, encoding="utf-8")
results.append(("hamburg", "§ 3 -> § 2 HmbBestG", before, after))

# ---------- BERLIN ----------
be = BESTATTER / "berlin" / "index.html"
txt = be.read_text(encoding="utf-8")

# Fix 1: Line 571 — § 21 used for Bestattungspflicht. Korrekt: § 16 BestattG BE.
old571 = "Antragsberechtigt ist die Person, die nach <strong>§ 21 BestattG BE</strong> (Berliner Bestattungsgesetz) zur Bestattung verpflichtet ist — in der gesetzlichen Rangfolge: <em>Ehegatten/eingetragene Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder</em>."
new571 = "Antragsberechtigt ist die Person, die nach <strong>§ 16 BestattG BE</strong> (Berliner Bestattungsgesetz) zur Bestattung verpflichtet ist — in der gesetzlichen Rangfolge nach § 16 Abs. 1: <em>Ehegatten/eingetragene Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, volljährige Enkelkinder, Großeltern</em>."
n_be = 1 if old571 in txt else 0
txt = txt.replace(old571, new571)
be.write_text(txt, encoding="utf-8")
results.append(("berlin", "§ 21 -> § 16 BestattG BE + Rangfolge (Enkelkinder VOR Großeltern)", n_be, 1 - n_be))

# ---------- MÜNCHEN ----------
mu = BESTATTER / "muenchen" / "index.html"
txt = mu.read_text(encoding="utf-8")

# Fix 1: visible HTML line 114
old114 = "muss eine Leiche spätestens 96 Stunden nach Feststellung des Todes bestattet oder auf den Weg gebracht sein"
new114 = "muss eine Leiche spätestens acht Tage nach Feststellung des Todes bestattet oder auf den Weg gebracht sein (Frist neu gefasst durch BestV-Novelle vom 11. März 2021, GVBl. S. 138 — die zuvor geltende 96-Stunden-Frist ist damit entfallen)"
n1 = txt.count(old114)
txt = txt.replace(old114, new114)

# Fix 2: JSON-LD + FAQ visible — same wording
old_faq = "die Höchstfrist von 96 Stunden für Erd- oder Feuerbestattung folgt aus § 19 Abs. 1 BestV"
new_faq = "die Höchstfrist von acht Tagen für Erd- oder Feuerbestattung folgt aus § 19 Abs. 1 BestV (seit der BestV-Novelle vom 11. März 2021)"
n2 = txt.count(old_faq)
txt = txt.replace(old_faq, new_faq)

# Fix 3: Art. 15 BayBestG citation präziser machen
old_art15 = "Antragsberechtigt ist die Person, die nach <strong>Art. 15 Bayerisches BestG</strong> (Bayerisches Bestattungsgesetz) zur Bestattung verpflichtet ist — in der gesetzlichen Rangfolge: <em>Ehegatten/Lebenspartner, Kinder, Eltern, Geschwister, Großeltern, Enkelkinder</em>."
new_art15 = "Antragsberechtigt ist die Person, die nach <strong>Art. 15 Abs. 2 BayBestG</strong> i.V.m. <strong>§ 15 BestV</strong> zur Bestattung verpflichtet ist; nach Art. 15 Abs. 2 Satz 2 BayBestG soll sich die Reihenfolge der Verpflichteten nach dem Grad der Verwandtschaft oder Schwägerschaft richten — in der Regel: <em>Ehegatten/Lebenspartner, Kinder, Eltern, Geschwister, Großeltern, Enkelkinder</em>."
n3 = 1 if old_art15 in txt else 0
txt = txt.replace(old_art15, new_art15)

mu.write_text(txt, encoding="utf-8")
results.append(("muenchen", "§ 19 96h->8 Tage (visible+JSON-LD+FAQ)", n1 + n2, 0))
results.append(("muenchen", "Art. 15 BayBestG -> Art. 15 Abs. 2 BayBestG i.V.m. § 15 BestV", n3, 1 - n3))

for r in results:
    print(r)
