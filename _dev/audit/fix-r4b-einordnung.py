#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R4b (Review NO-GO 64) — Einordnungs-Logik mathematisch geschlossen:
K1: Vergleichssumme wird aus den Items OHNE Grabpflege und ZURUECKGERECHNET auf
    Faktor 1 gebildet (lokale Posten / multiplier) und gegen BASIS = exakte
    Komponentensummen ohne Extras verglichen -> Default-Nutzer landet
    definitionsgemaess "im typischen Bereich". Lage-Texte konditional
    (Extras nur nennen, wenn gewaehlt).
K2/M2/G1: CAT_META Friedhof/Kremierung je Bestattungsart (See/Baum =
    Anbieterpreis/vergleichbar; Erd-Tipp ohne Urnengrab).
M1: BASIS = Komponentensummen aller 5 Arten (Erd 3700-9300, Feuer 3380-8200,
    See 2850-6200, Baum 3050-7000, anonym 1800-3350) -> Tool kann ohne Extras
    nie ausserhalb der eigenen Vergleichsbasis liegen.
M3: Schwellen (+/-15 %, +30 %) in Methodik dokumentiert.
G2 Wording, G3 Icon, G4 Badge-Lesbarkeit.
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

# G3 Icon
rep("anonyme:          {name: 'Anonyme Bestattung',     desc: 'Beisetzung ohne Namensgrab', icon: '\U0001f910'}",
    "anonyme:          {name: 'Anonyme Bestattung',     desc: 'Beisetzung ohne Namensgrab', icon: '\U0001f54a'}")

# K2/M2/G1: CAT_META je Bestattungsart + G4 Badge-Style
rep("""    var CAT_META = {
      'Bestatterleistungen': {badge:'vergleichbar', tipp:'Sparhebel: 2–3 Angebote vergleichen — hier unterscheiden sich Anbieter am stärksten.'},
      'Sarg/Urne':           {badge:'wählbar',      tipp:'Sparhebel: einfache Modelle sind genauso würdevoll — Materialwahl macht hunderte Euro aus.'},
      'Kremierung':          {badge:'gebührenfix',  tipp:'Krematoriumsgebühren sind kaum verhandelbar; das Krematorium ist teils wählbar.'},
      'Friedhof':            {badge:'fix per Satzung', tipp:'Sparhebel: Grabart (Reihen-/Urnengrab) und Friedhofswahl — die Gebühr selbst ist nicht verhandelbar.'},""",
    """    var _ba = state.bestattungsart;
    var _friedhofMeta;
    if (_ba === 'seebestattung') {
      _friedhofMeta = {badge:'Anbieterpreis', tipp:'Reederei-Leistungen sind vergleichbar — Preise und Leistungsumfang unterscheiden sich je Anbieter.'};
    } else if (_ba === 'baumbestattung') {
      _friedhofMeta = {badge:'Anbieterpreis', tipp:'Wald-Anbieter (z. B. FriedWald, RuheForst) haben eigene Preislisten — Baumart und Platz bestimmen den Preis.'};
    } else if (_ba === 'erdbestattung') {
      _friedhofMeta = {badge:'fix per Satzung', tipp:'Sparhebel: Grabart (z. B. Reihengrab statt Wahlgrab) und Friedhofswahl — die Gebühr selbst ist nicht verhandelbar.'};
    } else {
      _friedhofMeta = {badge:'fix per Satzung', tipp:'Sparhebel: Grabart (z. B. Urnenreihengrab) und Friedhofswahl — die Gebühr selbst ist nicht verhandelbar.'};
    }
    var CAT_META = {
      'Bestatterleistungen': {badge:'vergleichbar', tipp:'Sparhebel: 2–3 Angebote vergleichen — hier unterscheiden sich Anbieter am stärksten.'},
      'Sarg/Urne':           {badge:'wählbar',      tipp:'Sparhebel: einfache Modelle sind genauso würdevoll — Materialwahl macht hunderte Euro aus.'},
      'Kremierung':          {badge:'Preis je Krematorium', tipp:'Kommunale Krematorien rechnen nach Gebührensatzung ab, private nach Preisliste — über die Wahl des Krematoriums teils beeinflussbar.'},
      'Friedhof':            _friedhofMeta,""")

# G4 Badge-Style
rep("font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;background:rgba(122,107,93,0.10);color:#7A6B5D",
    "font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;background:rgba(94,80,71,0.12);color:#5E5047")

# K1 + M1: Einordnung mathematisch geschlossen
rep("""    // R4: ehrliche Einordnung gegen das publizierte Basis-Szenario (vor Regionalfaktor)
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
    }""",
    """    // R4b: Einordnung mathematisch geschlossen — Vergleichssumme aus den Items
    // OHNE Grabpflege und auf Faktor 1 zurückgerechnet, gegen exakte Komponentensummen.
    // Schwellen (±15 % / +30 % um die Mitte) dokumentiert in /methodik#kostenmodell.
    var BASIS = {
      erdbestattung:   {min:3700, max:9300, label:'Erdbestattung'},
      feuerbestattung: {min:3380, max:8200, label:'Feuerbestattung'},
      seebestattung:   {min:2850, max:6200, label:'Seebestattung'},
      baumbestattung:  {min:3050, max:7000, label:'Baumbestattung'},
      anonyme:         {min:1800, max:3350, label:'anonyme Bestattung'}
    };
    var basis = BASIS[state.bestattungsart];
    if (basis) {
      var _mult = REGIONAL_MULTIPLIERS[state.bundesland] || 1.0;
      var compMin = 0, compMax = 0;
      costs.items.forEach(function(it){
        if (it.key === 'grabpflege') return;
        var f = LOCAL_FEE_KEYS[it.key] ? _mult : 1.0;
        compMin += it.min / f; compMax += it.max / f;
      });
      var mid = (compMin + compMax) / 2;
      var basisMid = (basis.min + basis.max) / 2;
      var hasExtras = state.aufbahrung || state.trauerfeier || state.blumenschmuck || state.grabstein || state.traueranzeige || state.sargQualitaet === 'hochwertig' || state.grabGrab === 'Doppelgrab';
      var lage;
      if (mid < basisMid * 0.85) lage = 'bewusst reduziert — ohne Extras bzw. mit günstigen Optionen';
      else if (mid > basisMid * 1.3) lage = hasExtras ? 'eher umfangreich — die gewählten Extras treiben die Summe' : 'am oberen Rand des Basis-Szenarios';
      else lage = 'im typischen Bereich des Basis-Szenarios';
      html += '<p class="no-print" style="font-size:13.5px;color:var(--mr-text-muted);margin:10px 0 0;line-height:1.6">Zur Einordnung: Ohne Grabpflege und vor Regionalfaktor gerechnet liegt deine Auswahl <strong style="color:var(--mr-text)">' + lage + '</strong> (Komponentensumme ' + esc(basis.label) + ': ca. ' + fmt(basis.min) + '–' + fmt(basis.max) + ' €). Wie dein Bundesland liegt, zeigt der <a href="/bestattungskosten-nach-bundesland" style="color:var(--mr-primary)">Bundesland-Vergleich</a>.</p>';
    }""")

io.open(P, 'w', encoding='utf-8', newline='').write(t)
print('R4b: K1+K2+M1+M2+G1-G4 OK')

# M3: Schwellen in Methodik dokumentieren
M = 'methodik.html'
tm = io.open(M, encoding='utf-8').read()
old = 'Der <a href="/tools/angebotspruefer/" style="color:var(--mr-primary)">Angebotsprüfer</a> nutzt für Erd- und Feuerbestattung genau diese Komponenten ohne Grabpflege'
new = 'Der Kostenrechner ordnet die eigene Auswahl grob ein (Vergleich der Komponentensumme ohne Grabpflege, vor Regionalfaktor, gegen die Szenario-Mitte; „reduziert" unter −15 %, „umfangreich" über +30 %) — eine Orientierung, keine Bewertung. Der <a href="/tools/angebotspruefer/" style="color:var(--mr-primary)">Angebotsprüfer</a> nutzt für Erd- und Feuerbestattung genau diese Komponenten ohne Grabpflege'
assert tm.count(old) == 1
io.open(M, 'w', encoding='utf-8', newline='').write(tm.replace(old, new, 1))
print('methodik.html: Schwellen dokumentiert')
