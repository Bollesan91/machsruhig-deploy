#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Islam-Pillar: primaer-verifiziertes 8-Laender-Inventar Sargpflicht/Frist (Workflow islam-laenderrecht,
# je Land Gesetzestext vom offiziellen Landesrecht-Portal, § + woertliches Zitat). Ersetzt die vagen
# Bullets durch eine belegte Tabelle; korrigiert die veraltete 'Sachsen+Sachsen-Anhalt strikt'-Aussage
# (SA hat zum 1.10.2025 geoeffnet, Ministerium-PM bestaetigt) in FAQ + JSON-LD. Asserts vor Write.
import io, re, json
p = "islamische-bestattung.html"
s = io.open(p, encoding="utf-8").read()

OLD_UL = '''    <ul>
      <li><strong>Generell erlaubt</strong> ist die Tuchbestattung unter anderem in Hamburg (das die Sargpflicht 1998 als erstes Land abschaffte), Brandenburg, Mecklenburg-Vorpommern und Nordrhein-Westfalen.</li>
      <li><strong>Über religiöse Ausnahmen möglich</strong> ist sie in den meisten übrigen Ländern.</li>
      <li><strong>Am längsten strikt</strong> waren zuletzt vor allem Sachsen und Sachsen-Anhalt; die Rechtslage ändert sich hier gerade schnell (Rheinland-Pfalz hat die Sargpflicht z.&nbsp;B. zum Oktober 2025 gelockert). Verlasse dich nicht auf einen pauschalen Länder-Stand — prüfe für dein Bundesland die aktuelle Regelung und frage beim konkreten Friedhof nach.</li>
    </ul>'''

NEW_TABLE = '''    <p>Konkret für die großen Bundesländer — Stand der jeweiligen Landes-Bestattungsgesetze, primär geprüft 07/2026:</p>
    <div class="mr-table-wrap">
      <table class="mr-table">
        <thead><tr><th>Bundesland</th><th>Sarglose Tuchbestattung</th><th>Früheste Erdbestattung</th></tr></thead>
        <tbody>
          <tr><td>Nordrhein-Westfalen</td><td>generell möglich — kein gesetzlicher Sargzwang, die Friedhofssatzung entscheidet (§&nbsp;11 BestG&nbsp;NRW)</td><td>24 Stunden (§&nbsp;13 Abs.&nbsp;2)</td></tr>
          <tr><td>Bayern</td><td>aus religiösen Gründen, der Friedhofsträger kann sie zulassen (§&nbsp;30 Abs.&nbsp;2 BestV)</td><td>48 Stunden (§&nbsp;18 BestV)</td></tr>
          <tr><td>Baden-Württemberg</td><td>aus religiösen Gründen (§&nbsp;39 BestattG, §&nbsp;4 BestattVO)</td><td>keine feste Frist — zulässig nach der ärztlichen Leichenschau (§&nbsp;36 BestattG)</td></tr>
          <tr><td>Hessen</td><td>aus religiösen Gründen, der Gemeindevorstand gestattet sie (§&nbsp;18 Abs.&nbsp;2 FBG)</td><td>48 Stunden; religiöse Verkürzung nur eng begrenzt (§&nbsp;16 Abs.&nbsp;4)</td></tr>
          <tr><td>Niedersachsen</td><td>über Einzelfall-Ausnahme der Gesundheitsbehörde bei „wichtigem Grund“ (§&nbsp;11 Abs.&nbsp;1)</td><td>48 Stunden (§&nbsp;9 Abs.&nbsp;1)</td></tr>
          <tr><td>Berlin</td><td>aus religiösen Gründen auf bestimmten Grabfeldern (Transport zum Grab im Sarg) (§&nbsp;18 Abs.&nbsp;2)</td><td>keine feste gesetzliche Wartefrist</td></tr>
          <tr><td>Sachsen-Anhalt</td><td>seit Oktober 2025 zulässig; der Friedhofsträger kann widersprechen (§&nbsp;15)</td><td>keine feste Frist mehr (48-Stunden-Regel gestrichen)</td></tr>
          <tr><td>Sachsen</td><td><strong>nicht erlaubt</strong> — ausnahmslose Sargpflicht (§&nbsp;16 Abs.&nbsp;3 SächsBestG)</td><td>48 Stunden (§&nbsp;19)</td></tr>
        </tbody>
      </table>
    </div>
    <p style="font-size:14px;color:var(--mr-text-muted)">In allen übrigen Bundesländern ist die Tuchbestattung ebenfalls möglich — meist aus religiösen Gründen, teils (wie in NRW) generell. <strong>Sachsen ist damit das einzige Land mit noch ausnahmsloser Sargpflicht</strong> (Sachsen-Anhalt hat als vorletztes zum Oktober 2025 geöffnet). Die genaue Regelung steht im jeweiligen Landesgesetz; letztverbindlich ist die Satzung des konkreten Friedhofs.</p>'''

OLD_FAQ = "Am längsten strikt waren zuletzt vor allem Sachsen und Sachsen-Anhalt; die Rechtslage ändert sich hier gerade schnell (Rheinland-Pfalz hat die Sargpflicht z. B. zum Oktober 2025 gelockert)."
NEW_FAQ = "Von den Bundesländern hat allein Sachsen noch eine ausnahmslose Sargpflicht; Sachsen-Anhalt hat die Tuchbestattung zum Oktober 2025 geöffnet, Nordrhein-Westfalen erlaubt sie generell, die meisten anderen aus religiösen Gründen."

assert s.count(OLD_UL) == 1, ("UL", s.count(OLD_UL))
assert s.count(OLD_FAQ) == 2, ("FAQ/JSON-LD", s.count(OLD_FAQ))
s = s.replace(OLD_UL, NEW_TABLE)
s = s.replace(OLD_FAQ, NEW_FAQ)

# JSON-LD muss weiter parsen
for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
    json.loads(m.group(1))
# keine veraltete Aussage mehr
assert "Am längsten strikt" not in s and "Sachsen und Sachsen-Anhalt; die Rechtslage" not in s, "Rest alte Aussage"
io.open(p, "w", encoding="utf-8").write(s)
print("OK: 8-Laender-Tabelle eingefuegt, FAQ+JSON-LD korrigiert, JSON-LD parst.")
