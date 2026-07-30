#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Islam-Pillar: Laender-Tabelle von 8 auf ALLE 16 Bundeslaender erweitern.
# Quelle: Workflows islam-laenderrecht (I+II), je Land amtlicher Gesetzes-/Verordnungstext
# vom offiziellen Landesrecht-Portal, § + woertliches Zitat, 16/16 Primaer-Konfidenz.
# Asserts vor Write; JSON-LD-Reparse-Gate.
import io, re, json
p = "islamische-bestattung.html"
s = io.open(p, encoding="utf-8").read()

OLD_ROWS_START = '          <tr><td>Nordrhein-Westfalen</td>'
OLD_ROWS_END = '        </tbody>'
i0 = s.find(OLD_ROWS_START)
i1 = s.find(OLD_ROWS_END, i0)
assert i0 > 0 and i1 > i0, "Tabellen-Anker nicht gefunden"

NEW_ROWS = '''          <tr><td>Baden-Württemberg</td><td>aus religiösen Gründen (§&nbsp;39 BestattG, §&nbsp;4 BestattVO)</td><td>keine feste Frist — zulässig nach der ärztlichen Leichenschau (§&nbsp;36)</td></tr>
          <tr><td>Bayern</td><td>aus religiösen Gründen, der Friedhofsträger kann sie zulassen (§&nbsp;30 Abs.&nbsp;2 BestV)</td><td>48 Stunden (§&nbsp;18 BestV)</td></tr>
          <tr><td>Berlin</td><td>aus religiösen Gründen auf bestimmten Grabfeldern; Transport zum Grab im Sarg (§&nbsp;18 Abs.&nbsp;2)</td><td>keine feste gesetzliche Wartefrist</td></tr>
          <tr><td>Brandenburg</td><td>landesrechtlich nicht verboten — Sargpflicht nur für die Beförderung (§&nbsp;18 Abs.&nbsp;2); die Friedhofssatzung entscheidet</td><td>48 Stunden; Ausnahme <strong>ausdrücklich aus religiösen Gründen</strong> möglich (§&nbsp;22 Abs.&nbsp;1)</td></tr>
          <tr><td>Bremen</td><td>aus religiösen Gründen (§&nbsp;4 Friedhofs- und BestattungsG)</td><td>48 Stunden, Ausnahmen behördlich (§&nbsp;16 LeichenwesenG)</td></tr>
          <tr><td>Hamburg</td><td>generell möglich — Erdbestattung „in Särgen oder Leichentüchern“ (§&nbsp;12 Abs.&nbsp;1)</td><td>keine feste Frist</td></tr>
          <tr><td>Hessen</td><td>aus religiösen Gründen, der Gemeindevorstand gestattet sie (§&nbsp;18 Abs.&nbsp;2 FBG)</td><td>48 Stunden; religiöse Verkürzung nur eng begrenzt (§&nbsp;16 Abs.&nbsp;4)</td></tr>
          <tr><td>Mecklenburg-Vorpommern</td><td>generell — sarglos, wenn es dem Willen der verstorbenen Person entspricht (§&nbsp;10 Abs.&nbsp;3)</td><td>24 Stunden; Ausnahmen durch das Gesundheitsamt (§&nbsp;11 Abs.&nbsp;2)</td></tr>
          <tr><td>Niedersachsen</td><td>über Einzelfall-Ausnahme der Gesundheitsbehörde bei „wichtigem Grund“ (§&nbsp;11 Abs.&nbsp;1)</td><td>48 Stunden (§&nbsp;9 Abs.&nbsp;1)</td></tr>
          <tr><td>Nordrhein-Westfalen</td><td>generell möglich — kein gesetzlicher Sargzwang, die Friedhofssatzung entscheidet (§&nbsp;11)</td><td><strong>24 Stunden</strong> (§&nbsp;13 Abs.&nbsp;2)</td></tr>
          <tr><td>Rheinland-Pfalz</td><td>generell — seit dem neuen Bestattungsgesetz vom September 2025 (§&nbsp;12); Transport zum Grab im Sarg</td><td>48 Stunden; Verkürzung <strong>auf Antrag aus religiösen Gründen</strong> (§&nbsp;23 Abs.&nbsp;2)</td></tr>
          <tr><td>Saarland</td><td>aus religiösen Gründen, der Friedhofsträger kann sie zulassen (§&nbsp;31 Abs.&nbsp;2)</td><td>48 Stunden; frühere Bestattung in begründeten Fällen genehmigungsfähig (§&nbsp;29 Abs.&nbsp;4)</td></tr>
          <tr><td>Sachsen</td><td><strong>nicht erlaubt</strong> — ausnahmslose Sargpflicht (§&nbsp;16 Abs.&nbsp;3 SächsBestG)</td><td>48 Stunden; Verkürzung nur bei Gesundheitsgefahr (§&nbsp;19)</td></tr>
          <tr><td>Sachsen-Anhalt</td><td>seit Oktober 2025 zulässig; der Friedhofsträger kann widersprechen (§&nbsp;15)</td><td>keine feste Frist mehr (48-Stunden-Regel gestrichen)</td></tr>
          <tr><td>Schleswig-Holstein</td><td>generell — kommunale Friedhofsträger <strong>müssen</strong> die sarglose Bestattung auf Wunsch zulassen (§&nbsp;26 Abs.&nbsp;4)</td><td>48 Stunden (§&nbsp;16 Abs.&nbsp;1)</td></tr>
          <tr><td>Thüringen</td><td>nur als Einzelfall-Ausnahme der Ordnungsbehörde im Einvernehmen mit dem Gesundheitsamt (§&nbsp;23 Abs.&nbsp;1)</td><td>48 Stunden; Ausnahmen durch die Gesundheitsbehörde (§&nbsp;20 Abs.&nbsp;1)</td></tr>
'''

s = s[:i0] + NEW_ROWS + s[i1:]

OLD_INTRO = '<p>Konkret für die großen Bundesländer — Stand der jeweiligen Landes-Bestattungsgesetze, primär geprüft 07/2026:</p>'
NEW_INTRO = '<p>Konkret für alle 16 Bundesländer — jeweils nach dem Landes-Bestattungsgesetz beziehungsweise der Bestattungsverordnung, im Gesetzestext geprüft 07/2026:</p>'
assert s.count(OLD_INTRO) == 1
s = s.replace(OLD_INTRO, NEW_INTRO)

OLD_TAIL = '<p style="font-size:14px;color:var(--mr-text-muted)">In allen übrigen Bundesländern ist die Tuchbestattung ebenfalls möglich — meist aus religiösen Gründen, teils (wie in NRW) generell. <strong>Sachsen ist damit das einzige Land mit noch ausnahmsloser Sargpflicht</strong> (Sachsen-Anhalt hat als vorletztes zum Oktober 2025 geöffnet). Die genaue Regelung steht im jeweiligen Landesgesetz; letztverbindlich ist die Satzung des konkreten Friedhofs.</p>'
NEW_TAIL = '<p style="font-size:14px;color:var(--mr-text-muted)"><strong>Sachsen ist das einzige Bundesland mit noch ausnahmsloser Sargpflicht</strong> — Sachsen-Anhalt hat als vorletztes zum Oktober 2025 geöffnet, Rheinland-Pfalz im September 2025. In Thüringen ist die Tuchbestattung nur über eine behördliche Einzelfall-Ausnahme möglich. Die Fristangabe ist die gesetzliche Wartezeit bis zur Erdbestattung; sie ist nicht identisch mit dem Zeitpunkt, zu dem alle Papiere vorliegen. <strong>Letztverbindlich ist immer die Satzung des konkreten Friedhofs</strong> — auch dort, wo das Landesrecht die Tuchbestattung erlaubt.</p>'
assert s.count(OLD_TAIL) == 1
s = s.replace(OLD_TAIL, NEW_TAIL)

for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
    json.loads(m.group(1))
assert s.count('<tr><td>') >= 16, "zu wenige Zeilen"
io.open(p, "w", encoding="utf-8").write(s)
print("OK: 16-Laender-Tabelle, Intro + Fussnote aktualisiert, JSON-LD parst.")
