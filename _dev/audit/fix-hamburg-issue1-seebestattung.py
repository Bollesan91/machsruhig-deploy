#!/usr/bin/env python3
"""Issue 1 fix — merge two Seebestattung sections in bestatter/hamburg/index.html
into one consolidated section (keeps cultural opener from #1 + precise price
table from #2; drops contradicting 1.200-3.500 EUR range)."""
from pathlib import Path
import re, sys

FP = Path("bestatter/hamburg/index.html")
src = FP.read_text(encoding="utf-8")

# Anchors (exact h2 strings present in current file)
H2_A = "Seebestattung von Hamburg aus — deutsche Hauptstadt einer leisen Tradition"
H2_B = "Seebestattungen in Hamburg — Eine Tradition der Hafenstadt"

# Regex: each section is <div class="mr-section">...<h2>{anchor}</h2>...</div>
def section_pat(h2):
    return re.compile(
        r'  <div class="mr-section">\s*\n\s*<h2>' + re.escape(h2) + r'</h2>.*?\n  </div>\s*\n',
        re.DOTALL,
    )

m_a = section_pat(H2_A).search(src)
m_b = section_pat(H2_B).search(src)
if not (m_a and m_b):
    print(f"ERROR: anchors not found  A={bool(m_a)} B={bool(m_b)}")
    sys.exit(1)
if m_a.start() >= m_b.start():
    print("ERROR: order assumption violated"); sys.exit(1)

MERGED = '''  <div class="mr-section">
    <h2>Seebestattung von Hamburg aus — deutsche Hauptstadt einer leisen Tradition</h2>
    <p>Hamburg ist nicht zufällig das deutsche Zentrum der Seebestattung. Als seit Jahrhunderten größter Seehafen Deutschlands und Sitz zahlreicher Reedereien hat die Hansestadt nicht nur die maritime Logistik, sondern auch eine kulturelle Selbstverständlichkeit für die Beisetzung auf See. Mehrere spezialisierte Reedereien organisieren ganzjährig Seebestattungen — die Ausfahrten finden hauptsächlich auf <strong>Nordsee</strong> ab den Mündungen von Elbe und Weser statt, ergänzend auf der <strong>Ostsee</strong> ab Häfen wie Travemünde oder Kiel.</p>
    <p>Voraussetzung jeder Seebestattung ist eine vorherige <strong>Einäscherung</strong>; die Asche wird in einer wasserlöslichen <strong>Seeurne</strong> aus pflanzlichen Materialien beigesetzt. Die Beisetzung erfolgt in einem behördlich ausgewiesenen Seegebiet — die exakten Koordinaten werden den Angehörigen in einer „Seekarte mit Beisetzungsort" mitgeteilt, häufig ergänzt um den Eintrag im Bordbuch und eine kleine Trauerfeier an Bord. Die Bandbreite der Preise ergibt sich daraus, ob die Angehörigen an Bord begleiten („Beisetzung mit Angehörigen") oder ob die Reederei die Beisetzung in stiller Form ohne Trauergesellschaft vornimmt.</p>
    <h3>Bestattungsorte — Nord- oder Ostsee</h3>
    <ul style="margin-left:20px;margin-top:12px;margin-bottom:12px;">
      <li><strong>Nordsee:</strong> Seebestattungen vor Helgoland und anderen ausgewiesenen Zonen</li>
      <li><strong>Ostsee:</strong> Bestattungen in der Lübecker Bucht und anderen Gebieten</li>
    </ul>
    <h3>Kosten für Seebestattungen</h3>
    <p>Die Preise hängen von zwei Faktoren ab: ob bereits eine Einäscherung stattgefunden hat und ob Angehörige an Bord mitfahren. Es gibt zwei Preisebenen — Reederei-Paketpreise (nur Seebestattung) und Komplettpakete (inkl. Einäscherung und Bestatterleistungen):</p>
    <p><strong>Reederei-Paketpreise (Seebestattung allein, ohne Einäscherung):</strong></p>
    <ul style="margin-left:20px;margin-top:12px;margin-bottom:12px;">
      <li><strong>Unbegleitete Seebestattung:</strong> ab 1.049 € (Ost- oder Nordsee, inkl. MwSt.)</li>
      <li><strong>Begleitete Seebestattung (Ostsee):</strong> ca. 1.646 € (mit Familie an Bord)</li>
      <li><strong>Begleitete Seebestattung (Nordsee):</strong> ca. 1.895 € (längere Fahrtdistanz, höhere Treibstoffkosten)</li>
    </ul>
    <p><strong>Komplettpaket mit Einäscherung und Bestatterleistungen:</strong> typischerweise 2.900–5.000 € (abhängig von Begleitung, Region und gewähltem Bestatter)</p>
    <p><strong>Keine Friedhofsgebühren:</strong> Im Gegensatz zu Friedhofsbestattungen fallen für Seebestattungen keine dauerhaften Friedhofsgebühren an, was eine deutliche Kostenersparnis bedeutet.</p>
    <h3>Vorteile der Seebestattung</h3>
    <ul style="margin-left:20px;margin-top:12px;margin-bottom:12px;">
      <li><strong>Kein Grab zu pflegen:</strong> Nach der Beisetzung entfällt jede Grabpflicht — ein großer Vorteil für Familien, die nicht vor Ort wohnen oder die Grabpflege nicht leisten können.</li>
      <li><strong>Verbindung zur Stadt und Natur:</strong> Für viele Hamburger ist das Meer zentral. Eine Seebestattung ist eine würdevolle Verbindung zur See und zur maritimen Tradition Hamburgs.</li>
      <li><strong>Ökologisch:</strong> Bioabbaubare Urnen ermöglichen eine umweltfreundliche Beisetzung ohne künstliche Friedhofsstrukturen.</li>
      <li><strong>Kostengünstig:</strong> Besonders unbegleitete Seebestattungen sind eine preiswerte Option für kleine Budgets.</li>
    </ul>
    <p>Die Koordination übernimmt in der Regel der beauftragte Bestatter — viele Hamburger Bestattungsinstitute haben langjährige Kooperationen mit den auf Seebestattung spezialisierten Reedereien.</p>
  </div>
'''

# Replace section B with empty first (so subsequent positions stay valid), then A with merged.
out = src[:m_b.start()] + src[m_b.end():]
# Re-locate A in modified text
m_a2 = section_pat(H2_A).search(out)
if not m_a2:
    print("ERROR: lost A after removing B"); sys.exit(1)
out = out[:m_a2.start()] + MERGED + out[m_a2.end():]

# Sanity: ensure no two h2 left whose text starts with "Seebestattung"
h2_count = len(re.findall(r'<h2>Seebestattung[^<]*</h2>', out))
if h2_count != 1:
    print(f"ERROR: expected 1 Seebestattung <h2>, found {h2_count}"); sys.exit(1)

FP.write_text(out, encoding="utf-8")
print(f"OK Issue 1  src={len(src)}B  out={len(out)}B  diff={len(out)-len(src):+d}B  h2-count=1")
