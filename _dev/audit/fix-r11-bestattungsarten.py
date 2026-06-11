#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R11 — /bestattungsarten (7,2 -> 8,5):
1. Vergleichstabelle kanonisiert (Komponentensummen des Kostenmodells statt
   freier Spannen — Baum war 1.500-3.500 statt 3.050-7.000!) + Spalten
   Zeit bis Beisetzung / Aufwand fuer Angehoerige; Feuer-Friedhofszwang-Fehler
   korrigiert ("Nein (optional)" -> Friedhofszwang mit Ausnahmen);
   Direktkremation als eigene Zeile.
2. Entscheidungshilfe: 4 Leitfragen mit Empfehlungspfaden.
3. Varianten-Beispiele: 3 Kurzprofile.
4. Keyfact-Spanne kanonisch; dateModified.
"""
import io, sys

P = 'bestattungsarten.html'
t = io.open(P, encoding='utf-8').read()

def rep(old, new, expect=1):
    global t
    c = t.count(old)
    if c != expect:
        print('FATAL: %r -> %d (erwartet %d)' % (old[:70], c, expect)); sys.exit(1)
    t = t.replace(old, new)

rep('"dateModified":"2026-06-01"', '"dateModified":"2026-06-11"')
rep('<li>Kosten reichen von 1.200 € (anonym) bis 25.000 € (Diamantbestattung)</li>',
    '<li>Kosten reichen von rund 1.000 € (Direktkremation) bis über 20.000 € (Diamantbestattung)</li>')

# --- 1. Tabelle komplett ersetzen (alter tbody + thead) ---
OLD_TABLE_HEAD = '''<thead>
          <tr>
            <th>Bestattungsart</th>
            <th>Kosten (typisch)</th>
            <th>Grabpflege nötig?</th>
            <th>Friedhof nötig?</th>
            <th>Gestaltungsfreiheit</th>
          </tr>
        </thead>'''
NEW_TABLE_HEAD = '''<thead>
          <tr>
            <th>Bestattungsart</th>
            <th>Kosten (bundesweite Spanne)</th>
            <th>Grabpflege nötig?</th>
            <th>Fester Trauerort?</th>
            <th>Zeit bis Beisetzung</th>
            <th>Aufwand für Angehörige</th>
          </tr>
        </thead>'''
rep(OLD_TABLE_HEAD, NEW_TABLE_HEAD)

OLD_ROWS = [
 ('<td><strong>Erdbestattung</strong></td>\n            <td>4.000–12.000 €</td>\n            <td>Ja, 20–30 Jahre</td>\n            <td>Ja</td>\n            <td>Hoch</td>',
  '<td><strong>Erdbestattung</strong></td>\n            <td>3.700–9.300 € (zzgl. Grabpflege über die Jahre)</td>\n            <td>Ja, über die Ruhezeit (oft 20–30 Jahre)</td>\n            <td>Ja — Grab auf dem Friedhof</td>\n            <td>wenige Tage (Frist nach Landesrecht)</td>\n            <td>hoch (Grabwahl, Pflege, Termine)</td>'),
 ('<td><strong>Feuerbestattung</strong></td>\n            <td>2.000–5.000 €</td>\n            <td>Nein/Gering</td>\n            <td>Nein (optional)</td>\n            <td>Hoch</td>',
  '<td><strong>Feuerbestattung</strong></td>\n            <td>3.400–8.200 € (zzgl. Grabpflege je nach Grabart)</td>\n            <td>je nach Grabart (Urnengrab: ja)</td>\n            <td>Ja — für die Urne gilt Friedhofszwang (Ausnahmen: See-, Baum-/Wald­bestattung)</td>\n            <td>Beisetzung meist Wochen nach der Einäscherung möglich</td>\n            <td>mittel</td>'),
 ('<td><strong>Seebestattung</strong></td>\n            <td>4.000–6.000 €</td>\n            <td>Nein</td>\n            <td>Nein</td>\n            <td>Mittel</td>',
  '<td><strong>Seebestattung</strong></td>\n            <td>2.850–6.200 €</td>\n            <td>Nein</td>\n            <td>Nein — Seekarte mit Beisetzungsposition</td>\n            <td>nach Einäscherung flexibel planbar</td>\n            <td>gering</td>'),
 ('<td><strong>Baumbestattung</strong></td>\n            <td>1.500–3.500 €</td>\n            <td>Nein</td>\n            <td>Nein</td>\n            <td>Mittel</td>',
  '<td><strong>Baumbestattung</strong></td>\n            <td>3.050–7.000 €</td>\n            <td>Nein — die Natur pflegt</td>\n            <td>Ja — der Baum als Gedenkort</td>\n            <td>nach Einäscherung flexibel planbar</td>\n            <td>gering</td>'),
 ('<td><strong>Kolumbarium</strong></td>\n            <td>1.500–3.500 €</td>\n            <td>Nein</td>\n            <td>Ja</td>\n            <td>Gering</td>',
  '<td><strong>Kolumbarium</strong></td>\n            <td>wie Feuerbestattung (Stellplatz­gebühr je Friedhof)</td>\n            <td>Nein</td>\n            <td>Ja — Urnenwand</td>\n            <td>nach Einäscherung flexibel planbar</td>\n            <td>gering</td>'),
 ('<td><strong>Anonyme Bestattung</strong></td>\n            <td>1.200–2.000 €</td>\n            <td>Nein</td>\n            <td>Ja</td>\n            <td>Gering</td>',
  '<td><strong>Anonyme Bestattung</strong></td>\n            <td>1.800–3.350 €</td>\n            <td>Nein</td>\n            <td>Nein — Gemeinschaftsfeld ohne Namen</td>\n            <td>Termin oft ohne Angehörige</td>\n            <td>sehr gering</td>'),
 ('<td><strong>Naturbestattung</strong></td>\n            <td>3.000–4.500 €</td>\n            <td>Nein</td>\n            <td>Nein</td>\n            <td>Mittel</td>',
  '<td><strong>Naturbestattung</strong> (Almwiese u.&nbsp;ä.)</td>\n            <td>Anbieterpreise, stark variabel</td>\n            <td>Nein</td>\n            <td>je nach Anbieter</td>\n            <td>nach Einäscherung flexibel planbar</td>\n            <td>gering</td>'),
 ('<td><strong>Diamantbestattung</strong></td>\n            <td>5.000–25.000 €</td>\n            <td>Nein</td>\n            <td>Teilweise</td>\n            <td>Mittel</td>',
  '<td><strong>Diamantbestattung</strong></td>\n            <td>5.000–25.000 € (Anbieterpreise, zzgl. Bestattung der übrigen Asche)</td>\n            <td>Nein</td>\n            <td>Erinnerungsstück statt Ort</td>\n            <td>Monate (Herstellung)</td>\n            <td>mittel</td>'),
]
for old, new in OLD_ROWS:
    rep(old, new)

# Direktkremation-Zeile nach der Feuerbestattung + Quellen-Hinweis unter Tabelle
rep('<td>mittel</td>\n          </tr>\n          <tr>\n            <td><strong>Seebestattung</strong></td>',
    '''<td>mittel</td>
          </tr>
          <tr>
            <td><strong>Direktkremation</strong> (ohne Feier)</td>
            <td>1.000–2.200 €</td>
            <td>je nach Beisetzungsform</td>
            <td>je nach Beisetzungsform</td>
            <td>schnellstmöglich, ohne Zeremonie</td>
            <td>minimal</td>
          </tr>
          <tr>
            <td><strong>Seebestattung</strong></td>''')
rep('            <td>Monate (Herstellung)</td>\n            <td>mittel</td>\n          </tr>\n        </tbody>\n      </table>\n    </div>\n  </section>',
    '''            <td>Monate (Herstellung)</td>
            <td>mittel</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p style="font-size:13.5px;color:var(--mr-text-muted);margin-top:10px">Kostenspannen = bundesweite Komponentensummen unseres Kostenmodells, ohne Grabpflege (Herleitung in der <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik</a>); Natur- und Diamantbestattung sind freie Anbieterpreise. Regional kann es deutlich abweichen — dein Bundesland zeigt der <a href="/bestattungskosten-nach-bundesland" style="color:var(--mr-primary)">Bundesland-Vergleich</a>.</p>
  </section>

  <section class="mr-section" id="entscheidungshilfe">
    <h2>Welche Bestattungsart passt? Vier Leitfragen</h2>
    <div style="display:grid;gap:10px">
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:10px;padding:14px 18px">
        <strong>1. Braucht ihr einen festen Ort zum Trauern?</strong>
        <p style="font-size:14px;margin:4px 0 0">Ja, mit Namen → Erdbestattung, Urnengrab oder Kolumbarium. Ja, aber in der Natur → Baumbestattung. Nein bzw. das Meer als Ort → Seebestattung. Bedenke: Bei der anonymen Bestattung gibt es keinen auffindbaren Ort — das belastet manche Angehörige später.</p>
      </div>
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:10px;padding:14px 18px">
        <strong>2. Wer kann sich um ein Grab kümmern?</strong>
        <p style="font-size:14px;margin:4px 0 0">Niemand vor Ort → pflegefreie Formen (Baum, See, Kolumbarium, Rasengrab). Familie in der Nähe und gewünscht → klassisches Erd- oder Urnengrab. Dauergrabpflege lässt sich auch einkaufen — das sind über 20 Jahre aber schnell mehrere Tausend Euro.</p>
      </div>
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:10px;padding:14px 18px">
        <strong>3. Was gibt das Budget her?</strong>
        <p style="font-size:14px;margin:4px 0 0">Sehr knapp → Direktkremation (ab ca. 1.000 €) oder anonyme Beisetzung; bei Bedürftigkeit zuerst die <a href="/sozialbestattung" style="color:var(--mr-primary)">Sozialbestattung</a> prüfen. Mittel → Feuerbestattung mit schlichter Feier. Der <a href="/tools/bestattungskosten-rechner/" style="color:var(--mr-primary)">Kostenrechner</a> rechnet deine Auswahl durch.</p>
      </div>
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:10px;padding:14px 18px">
        <strong>4. Gibt es einen Wunsch der verstorbenen Person?</strong>
        <p style="font-size:14px;margin:4px 0 0">Eine Bestattungsverfügung oder ein dokumentierter Wunsch hat Vorrang vor den Vorstellungen der Angehörigen. Für See- und einige Naturbestattungen verlangen Anbieter oft einen nachgewiesenen Willen der verstorbenen Person.</p>
      </div>
    </div>
    <h3 style="margin-top:20px">Drei typische Konstellationen</h3>
    <ul style="font-size:14.5px;line-height:1.8">
      <li><strong>Familiengrab vorhanden, Familie am Ort:</strong> Erdbestattung oder Urnenbeisetzung im bestehenden Grab — emotional naheliegend und spart die Grabstellen-Gebühr für ein neues Grab.</li>
      <li><strong>Kinder weit weg, niemand kann pflegen:</strong> Baumbestattung oder Kolumbarium — fester Gedenkort ohne Pflegepflicht.</li>
      <li><strong>Kleines Budget, stiller Abschied gewünscht:</strong> Direktkremation mit späterer Beisetzung im Urnenreihengrab oder anonyme Beisetzung; eine kleine Gedenkfeier lässt sich unabhängig davon privat gestalten.</li>
    </ul>
  </section>''')

io.open(P, 'w', encoding='utf-8', newline='').write(t)
print('R11 OK: Tabelle kanonisiert + Entscheidungshilfe + Beispiele')
