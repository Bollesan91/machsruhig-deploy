#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R8b — Auflagen aus NO-GO-64 (Matrix-Code-Verifikations-Review):
HOCH-1: Checkliste Todesfall hatte KEIN localStorage (FAQ+Matrix versprachen
  es) -> Persistenz implementiert (Pattern wie Fristen-Radar): Laden bei Init,
  Speichern bei Toggle, Loeschen bei Neustart.
HOCH-2: Datenschutz-§6-Fliesstext widersprach der eigenen Matrix ("zu keinem
  Zeitpunkt uebermittelt", "beim Verlassen verworfen") -> auf Tabelle gestuetzt.
HOCH-3: §9 vs. gelebtes Doppel-Regime (Opt-in-Banner auf Tool-Seiten vs.
  Head-Load) -> Ist-Zustand ehrlich beschrieben; Vereinheitlichung bleibt
  eigener Arbeitsblock (ROADMAP-PBI).
HOCH-4: Tool-Formulare nicht von §8 abgedeckt + §2-Kollision ("keine Eingaben
  auf unseren Servern" vs. Netlify-Forms-Speicherung) -> §8 erweitert, §2
  praezisiert.
MITTEL-5/6: Fussnote unter beiden Matrizen (Umami erfasst Seitenbesuch, nicht
  Eingaben; Einstellungs-Flags in localStorage). MITTEL-10: "Server-Funktion"-
  Jargon in der Matrix vereinfacht.
"""
import io, sys

def rep_in(path, old, new, expect=1):
    t = io.open(path, encoding='utf-8').read()
    c = t.count(old)
    if c != expect:
        print('FATAL %s: %r -> %d (erwartet %d)' % (path, old[:60], c, expect)); sys.exit(1)
    io.open(path, 'w', encoding='utf-8', newline='').write(t.replace(old, new))

# ===== HOCH-1: Checkliste-Persistenz implementieren =====
C = 'tools/checkliste-todesfall/index.html'
rep_in(C, "var state = {bundesland:'', szenario:'', isForeign:false, checkedTasks:{}};",
    """var state = {bundesland:'', szenario:'', isForeign:false, checkedTasks:{}};
  try { var _saved = JSON.parse(localStorage.getItem('cl-checked') || '{}'); if (_saved && typeof _saved === 'object') state.checkedTasks = _saved; } catch(e) {}
  function persistChecked(){ try { localStorage.setItem('cl-checked', JSON.stringify(state.checkedTasks)); } catch(e) {} }""")
rep_in(C, """  function toggleTask(id){
    state.checkedTasks[id] = !state.checkedTasks[id];
    if (state.checkedTasks[id]) {
      track('toolStep', {tool:'checkliste-todesfall', step:'task_checked', task:id});
    }
    renderChecklist();
  }""",
    """  function toggleTask(id){
    state.checkedTasks[id] = !state.checkedTasks[id];
    if (state.checkedTasks[id]) {
      track('toolStep', {tool:'checkliste-todesfall', step:'task_checked', task:id});
    }
    persistChecked();
    renderChecklist();
  }""")
rep_in(C, """    $('#cl-restart-btn').addEventListener('click', function(){
      state.checkedTasks = {};""",
    """    $('#cl-restart-btn').addEventListener('click', function(){
      state.checkedTasks = {};
      persistChecked();""")

# ===== HOCH-2: §6-Fliesstext auf die Matrix stuetzen =====
rep_in('datenschutz.html',
  '<p>Die meisten unserer Tools (z.&nbsp;B. Kostenrechner, Vorsorge-Check, Beerdigungsplaner, Checkliste Todesfall, Fristen-Radar) laufen vollständig in deinem Browser. Deine Eingaben werden dabei zu keinem Zeitpunkt an unsere Server oder an Dritte übermittelt. Es findet keine serverseitige Verarbeitung, Speicherung oder Auswertung deiner Eingaben statt. Beim Verlassen der Seite oder Schließen des Browsers werden alle Eingaben verworfen.</p>',
  '<p>Unsere Tools laufen vollständig in deinem Browser. Was mit deinen Eingaben im Einzelnen geschieht — ob sie lokal auf deinem Gerät gespeichert werden und in welchen Fällen (nur auf deine aktive Aktion hin) etwas übertragen wird — zeigt die folgende Tabelle verbindlich pro Tool:</p>')

# ===== HOCH-3: §9 — Ist-Zustand mit Banner-Uebergang ehrlich beschreiben =====
rep_in('datenschutz.html',
  '<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an der anonymen, cookielosen Reichweitenmessung). Da keine personenbezogenen Daten verarbeitet werden, ist hierfür kein Einwilligungs-Banner erforderlich.</p>',
  '<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an der anonymen, cookielosen Reichweitenmessung); ein Einwilligungs-Banner ist dafür nicht erforderlich. Hinweis zum aktuellen Stand: Auf einem Teil unserer Tool-Seiten fragt derzeit dennoch ein Hinweis-Banner um Zustimmung, bevor Umami geladen wird — historisch strenger umgesetzt, wir vereinheitlichen das gerade. An Art und Umfang der Messung (anonym, cookielos, keine Eingaben) ändert das nichts.</p>')

# ===== HOCH-4a: §8 um Tool-Formulare erweitern =====
rep_in('datenschutz.html',
  '<p>Auf unseren Stadt-Seiten (z.B. /bestatter/muenchen/) bieten wir ein Kontaktformular an, über das du unverbindlich Informationen von Bestattern in deiner Nähe anfragen kannst. Wenn du dieses Formular absendest, werden folgende Daten verarbeitet:</p>',
  '<p>Auf unseren Stadt-Seiten (z.B. /bestatter/muenchen/) sowie optional in einigen Tools (Bestattungskosten-Rechner, Beerdigungsplaner, Vorsorge-Check) bieten wir Kontaktformulare an, über die du unverbindlich eine Anfrage stellen kannst. Nur wenn du ein solches Formular aktiv absendest, werden die dort angegebenen Daten verarbeitet — bei der Bestatter-Anfrage etwa:</p>')
rep_in('datenschutz.html',
  'Die Daten werden ausschließlich zur Vermittlung mit einem passenden Bestatter in deiner Region verwendet und nicht für andere Zwecke eingesetzt. Du kannst deine Einwilligung jederzeit widerrufen.</p>',
  'Die Daten werden ausschließlich zur Bearbeitung deiner jeweiligen Anfrage verwendet und nicht für andere Zwecke eingesetzt. Technisch nimmt unser Hoster Netlify (siehe Abschnitt 3) die Formulardaten entgegen und speichert sie für uns; wir löschen sie, sobald die Anfrage bearbeitet ist. Du kannst deine Einwilligung jederzeit widerrufen.</p>')

# ===== HOCH-4b: §2 praezisieren =====
rep_in('datenschutz.html',
  'Wir speichern keine Eingaben und keine Ergebnisse auf unseren Servern. Eine Ausnahme sind die optionalen KI-Textentwürfe — Details dazu in Abschnitt 7.</p>',
  'Tool-Eingaben und Ergebnisse speichern wir nicht auf unseren Servern. Zwei Ausnahmen, beide nur auf deine aktive Aktion hin: die optionalen KI-Textentwürfe (Abschnitt 7) und das Absenden eines Kontaktformulars (Abschnitt 8).</p>')

# ===== MITTEL-5/6/10: Fussnote unter beide Matrizen + Jargon =====
FOOTNOTE = '<p style="font-size:12.5px;color:var(--mr-text-muted);margin-top:8px">„Wird etwas übertragen? — nein" bezieht sich auf deine Eingaben. Unabhängig davon erfasst die anonyme, cookielose Reichweitenmessung (Umami) den Seitenbesuch selbst — nie deine Eingaben. Einstellungs-Flags (etwa deine Banner-Entscheidung oder KI-Einwilligung) speichern manche Seiten zusätzlich in localStorage; sie enthalten keine Eingaben.</p>'
for f in ['datenschutz.html', 'methodik.html']:
    rep_in(f, 'an unsere Server-Funktion und Groq, Inc. (USA)</td></tr>\n        </tbody>\n      </table>\n    </div>',
        'an unseren Server (Netlify) und den KI-Anbieter Groq, Inc. (USA)</td></tr>\n        </tbody>\n      </table>\n    </div>\n    ' + FOOTNOTE)

print('R8b OK: Persistenz + Paragraphen-Konsistenz + Fussnoten')
