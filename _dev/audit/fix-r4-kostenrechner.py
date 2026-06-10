#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R4 (Loop-Iteration 3) — Kostenrechner "interpretieren statt rechnen".
Ist-Analyse: Kostenbloecke, PDF, Angebotspruefer-CTA, Lead-nach-Ergebnis,
5-Ebenen-Erklaerung existieren bereits. Ergaenzt wird gezielt:
1. Fix/verhandelbar/optional-Badge je Kostenblock (Kategorie-Header).
2. Sparhebel-Zeile je Kostenblock (aufgeklappter Body).
3. Ehrliche Einordnung statt Pseudo-Ampel: Vergleich der eigenen Auswahl mit
   der publizierten Basis-Spanne der Bestattungsart (vor Regionalfaktor) +
   Verweis auf den Bundesland-Vergleich.
4. "(300-400 %)"-Praezision -> "teils um ein Vielfaches" (Konsistenz site-weit).
"""
import io, sys

P = 'tools/bestattungskosten-rechner/index.html'
t = io.open(P, encoding='utf-8').read()

def rep(old, new, expect=1):
    global t
    c = t.count(old)
    if c != expect:
        print('FATAL: %r -> %d (erwartet %d)' % (old[:70], c, expect)); sys.exit(1)
    t = t.replace(old, new)

# 4. Praezision
rep('kommunale Gebühren, regional sehr unterschiedlich (300–400 %).',
    'kommunale Gebühren, regional sehr unterschiedlich (zwischen Kommunen teils um ein Vielfaches).')

# 1.+2. Badges + Sparhebel je Kategorie (Daten-Map + Render-Erweiterung)
rep("""    var ba = BESTATTUNGSARTEN[state.bestattungsart];
    var html = '<div class="results-container">';""",
    """    var ba = BESTATTUNGSARTEN[state.bestattungsart];
    // R4: Einordnung je Kostenblock — Badge (fix/vergleichbar/optional) + Sparhebel
    var CAT_META = {
      'Bestatterleistungen': {badge:'vergleichbar', tipp:'Sparhebel: 2–3 Angebote vergleichen — hier unterscheiden sich Anbieter am stärksten.'},
      'Sarg/Urne':           {badge:'wählbar',      tipp:'Sparhebel: einfache Modelle sind genauso würdevoll — Materialwahl macht hunderte Euro aus.'},
      'Kremierung':          {badge:'gebührenfix',  tipp:'Krematoriumsgebühren sind kaum verhandelbar; das Krematorium ist teils wählbar.'},
      'Friedhof':            {badge:'fix per Satzung', tipp:'Sparhebel: Grabart (Reihen-/Urnengrab) und Friedhofswahl — die Gebühr selbst ist nicht verhandelbar.'},
      'Trauerfeier':         {badge:'optional',     tipp:'Sparhebel: Umfang frei gestaltbar — eine kleine Feier ist genauso würdig.'},
      'Grabstein':           {badge:'optional, später', tipp:'Sparhebel: muss nicht sofort entschieden werden — in Ruhe vergleichen, oft erst nach Monaten nötig.'},
      'Grabpflege':          {badge:'gestaltbar',   tipp:'Sparhebel: Eigenpflege statt Dauergrabpflege-Vertrag; pflegeleichte Grabarten wählen.'},
      'Extras':              {badge:'optional',     tipp:'Sparhebel: Anzeigen, Blumen und Karten lassen sich klein halten oder selbst organisieren.'},
      'Sonstiges':           {badge:'optional',     tipp:'Sparhebel: Posten einzeln hinterfragen — nicht alles ist nötig.'}
    };
    var html = '<div class="results-container">';""")

rep("""      html += '<strong>' + esc(cat) + '</strong>';""",
    """      var meta = CAT_META[cat];
      html += '<strong>' + esc(cat) + (meta ? ' <span style="font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;background:rgba(122,107,93,0.10);color:#7A6B5D;border-radius:99px;padding:2px 8px;vertical-align:middle;margin-left:6px">' + esc(meta.badge) + '</span>' : '') + '</strong>';""")

rep("""      html += '<div class="cost-category-body">';
      categories[cat].forEach(function(item){""",
    """      html += '<div class="cost-category-body">';
      if (meta) html += '<div style="font-size:12.5px;color:var(--mr-text-muted);padding:8px 0 4px;line-height:1.5">' + esc(meta.tipp) + '</div>';
      categories[cat].forEach(function(item){""")

# 3. Einordnung gegen publizierte Basis-Spanne (vor Regionalfaktor)
rep("""    html += '<div><strong>' + fmt(costs.maxTotal) + ' €</strong></div>';
    html += '</div></div>';""",
    """    html += '<div><strong>' + fmt(costs.maxTotal) + ' €</strong></div>';
    html += '</div></div>';

    // R4: ehrliche Einordnung gegen das publizierte Basis-Szenario (vor Regionalfaktor)
    var BASIS = {
      erdbestattung:   {min:3700, max:9300, label:'Erdbestattung (Basis-Szenario ohne Grabpflege)'},
      feuerbestattung: {min:3380, max:8200, label:'Feuerbestattung (Basis-Szenario ohne Grabpflege)'},
      seebestattung:   {min:3500, max:6500, label:'Seebestattung (Richtwert)'},
      baumbestattung:  {min:3000, max:6000, label:'Baumbestattung (Richtwert)'},
      anonyme:         {min:1500, max:3500, label:'anonyme Bestattung (Richtwert)'}
    };
    var basis = BASIS[state.bestattungsart];
    if (basis) {
      var mid = (costs.minTotal + costs.maxTotal) / 2;
      var basisMid = (basis.min + basis.max) / 2;
      var lage;
      if (mid < basisMid * 0.85) lage = 'eher schlank — du hast Extras weggelassen oder günstige Optionen gewählt';
      else if (mid > basisMid * 1.3) lage = 'eher umfangreich — Extras und Region treiben die Summe';
      else lage = 'im typischen Bereich';
      html += '<p class="no-print" style="font-size:13.5px;color:var(--mr-text-muted);margin:10px 0 0;line-height:1.6">Zur Einordnung: Deine Auswahl liegt <strong style="color:var(--mr-text)">' + lage + '</strong>. Bundesweite Vergleichsbasis für die ' + esc(basis.label) + ': ca. ' + fmt(basis.min) + '–' + fmt(basis.max) + ' € vor Regionalfaktor — wie dein Bundesland liegt, zeigt der <a href="/bestattungskosten-nach-bundesland" style="color:var(--mr-primary)">Bundesland-Vergleich</a>.</p>';
    }""")

io.open(P, 'w', encoding='utf-8', newline='').write(t)
print('R4 OK: Badges + Sparhebel + Basis-Einordnung + Vielfaches-Fix')
