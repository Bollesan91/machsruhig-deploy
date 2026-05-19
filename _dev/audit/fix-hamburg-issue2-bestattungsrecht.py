#!/usr/bin/env python3
"""Issue 2 fix — merge two Bestattungsrecht sections in bestatter/hamburg/index.html.
Keeps gesetzliche Einordnung + Stadtstaat-Hinweis aus #1, übernimmt detaillierte
Fristen + Besonderheiten aus #2; behält den Verweis auf die BL-Seite via mr-hint."""
from pathlib import Path
import re, sys

FP = Path("bestatter/hamburg/index.html")
src = FP.read_text(encoding="utf-8")

H2_A = "Bestattungsrecht in Hamburg — die Kurzfassung"
H2_B = "Bestattungsrecht in Hamburg — Fristen & Regelungen nach HmbBestattG"

def section_pat(h2):
    return re.compile(
        r'  <div class="mr-section">\s*\n\s*<h2>' + re.escape(h2) + r'</h2>.*?\n  </div>\s*\n',
        re.DOTALL,
    )

m_a = section_pat(H2_A).search(src)
m_b = section_pat(H2_B).search(src)
if not (m_a and m_b):
    print(f"ERROR: anchors not found A={bool(m_a)} B={bool(m_b)}"); sys.exit(1)
if m_a.start() >= m_b.start():
    print("ERROR: order assumption violated"); sys.exit(1)

MERGED = '''  <div class="mr-section">
    <h2>Bestattungsrecht in Hamburg — Fristen & Regelungen nach HmbBestattG</h2>
    <p>Da Hamburg ein Stadtstaat ist, fällt das Bestattungsrecht direkt unter das <strong>Hamburgische Bestattungsgesetz (HmbBestattG)</strong> vom 14. September 1988 (zuletzt mehrfach geändert; u.a. Novelle 2010 mit Lockerung der Sargpflicht für muslimische Bestattungen) — es gibt keine zusätzliche „Landesebene" über der Stadt. Hier die wichtigsten Fristen und Regeln im Überblick:</p>
    <h3>Überführungsfrist (Überführung in die Leichenhalle)</h3>
    <p>Nach einem Todesfall muss die verstorbene Person innerhalb von <strong>36 Stunden</strong> in eine Leichenhalle überführt werden — entweder in eine vom Bestatter oder in eine städtische Leichenhalle. Dies ist die gesetzliche Höchstfrist.</p>
    <h3>Bestattungsfrist (Erdbestattung)</h3>
    <p>Eine Erdbestattung muss spätestens nach <strong>10 Tagen</strong> nach Todesfeststellung durchgeführt sein. Hamburg kennt nach geltender Praxis <strong>keine starre Mindestfrist von 48 Stunden</strong> vor der Bestattung — entscheidend ist, dass die Leichenschau abgeschlossen ist. Im Bundesländervergleich ist das eine relativ großzügige Frist (z.B. Bayern: 4 Tage, Schleswig-Holstein: 14 Tage) und gibt der Familie ausreichend Zeit zur Organisation einer Trauerfeier und Behördengänge.</p>
    <h3>Urnenbeisetzungsfrist</h3>
    <p>Nach der Einäscherung muss eine Urnenbeisetzung im Regelfall innerhalb von <strong>1 Monat</strong> stattfinden. Ist dies nicht der Fall, veranlasst die zuständige Behörde die Beisetzung in einem nummerierten Grab. Dies gibt Familien ausreichend Flexibilität, insbesondere wenn Verwandte aus der Ferne anreisen.</p>
    <h3>Sargpflicht und Mindestruhezeit</h3>
    <p>Die Sargpflicht gilt grundsätzlich bei Erdbestattungen; seit der Novelle 2010 sind religiöse Ausnahmen für muslimische Bestattungen (Beisetzung im Leichentuch) zugelassen. Die Mindestruhezeit auf den Ohlsdorfer Wahlgräbern liegt bei <strong>25 Jahren</strong> für Erdbestattungen und ist in der jeweiligen Friedhofssatzung der Hamburger Friedhöfe AöR geregelt.</p>
    <h3>Lagerung von verstorbenen Personen</h3>
    <p>Falls die Überführung oder Bestattung verzögert wird, muss die Leiche in speziellen Kühlräumen gelagert werden — entweder beim Bestatter oder in der städtischen Leichenhalle.</p>
    <h3>Besonderheiten in Hamburg</h3>
    <ul style="margin-left:20px;margin-top:12px;margin-bottom:12px;">
      <li><strong>Anonyme Beisetzungen:</strong> Sind auf ausgewiesenen Arealen des Ohlsdorf, Öjendorf und anderer Friedhöfe möglich — ideal für Personen ohne Familienangehörige oder auf ausdrücklichen Wunsch.</li>
      <li><strong>Seebestattungen:</strong> Eine Tradition in Hamburg — völlig legal und gängig, organisiert durch spezialisierte Bestatter und Reedereien.</li>
      <li><strong>Waldbestattungen/Friedwald:</strong> Naturbestattungen in Wäldern nahe Hamburg (z.B. Friedwald Kisdorf) sind gestattet und erfreuen sich wachsender Beliebtheit.</li>
      <li><strong>Zuständige Behörde:</strong> Die Behörde für Umwelt, Klima, Energie und Agrarwirtschaft (BUKEA) ist zuständig für Friedhofswesen und Bestattungsangelegenheiten.</li>
    </ul>
    <div class="mr-hint">
      <strong>Die vollständige rechtliche Übersicht</strong> mit allen Paragraphen, Höchstfrist, Friedhofszwang und Sonderregelungen ist auf der Bundesland-Seite Hamburg aufgearbeitet: <a href="/bestattung-in/hamburg/">Bestattung in Hamburg — HmbBestattG im Detail</a>.
    </div>
  </div>
'''

# Replace B first, then A
out = src[:m_b.start()] + src[m_b.end():]
m_a2 = section_pat(H2_A).search(out)
if not m_a2:
    print("ERROR: lost A after removing B"); sys.exit(1)
out = out[:m_a2.start()] + MERGED + out[m_a2.end():]

h2_count = len(re.findall(r'<h2>Bestattungsrecht in Hamburg[^<]*</h2>', out))
if h2_count != 1:
    print(f"ERROR: expected 1 Bestattungsrecht <h2>, found {h2_count}"); sys.exit(1)

FP.write_text(out, encoding="utf-8")
print(f"OK Issue 2  src={len(src)}B  out={len(out)}B  diff={len(out)-len(src):+d}B  h2-count=1")
