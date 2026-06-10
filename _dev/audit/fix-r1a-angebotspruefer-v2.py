#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R1a (2026-06-10) — Angebotspruefer auf Modell V2:
Der Pruefer nutzte noch die V1-Multiplikatoren (BY 1,22 / MV 0,78, Kommentar
"single source of truth" = Kostenrechner, der heute auf V2 umgestellt wurde).
V2: Faktor (Aeternitas-Landeshauptstadt-Gebuehren) wirkt NUR auf den
ortsgebundenen Anteil (Friedhof+Beisetzung) je Bestattungsart; See/Baum/
Direktkremation regional-neutral (keine kommunale Friedhofsgebuehr im Paket).
Zusatz: doppelte Breadcrumb im Header entfernt, Ergebnis-Methodik-Text aktualisiert.
"""
import io, sys

P = 'tools/angebotspruefer/index.html'

def patch(path, replacements):
    with io.open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()
    for i, (old, new, expect) in enumerate(replacements):
        c = text.count(old)
        if c != expect:
            print('FATAL #%d: %r -> %d (erwartet %d)' % (i, old[:70], c, expect)); sys.exit(1)
        text = text.replace(old, new)
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)
    print('%s: %d Ersetzungen OK' % (path, len(replacements)))

OLD_BA = """  var BESTATTUNGSARTEN = {
    erdbestattung:{name:'Erdbestattung',icon:'⚰',desc:'Sarg, Friedhof, Beisetzung mit Grabstelle',baseMin:4500,baseMax:9500},
    feuerbestattung:{name:'Feuerbestattung',icon:'\U0001f525',desc:'Einäscherung + Urnenbeisetzung auf Friedhof',baseMin:3500,baseMax:7500},
    seebestattung:{name:'Seebestattung',icon:'\U0001f30a',desc:'Einäscherung + Beisetzung auf See',baseMin:3500,baseMax:6500},
    baumbestattung:{name:'Baumbestattung',icon:'\U0001f333',desc:'Einäscherung + Beisetzung an einem Baum',baseMin:3000,baseMax:6000},
    anonyme:{name:'Anonyme Bestattung',icon:'\U0001f54a',desc:'Einfache Bestattung ohne Grabstelle',baseMin:1500,baseMax:3500},
    direktkremation:{name:'Direktkremation',icon:'⚱',desc:'Einäscherung ohne Trauerfeier — Urne wird beigesetzt oder übergeben',baseMin:1000,baseMax:2200}
  };"""
NEW_BA = """  var BESTATTUNGSARTEN = {
    // V2 (Juni 2026): lokalMin/lokalMax = ortsgebundener Anteil (Friedhofsgebuehren+Beisetzung)
    // innerhalb der Base-Range — nur dieser wird mit dem Regionalfaktor skaliert.
    erdbestattung:{name:'Erdbestattung',icon:'⚰',desc:'Sarg, Friedhof, Beisetzung mit Grabstelle',baseMin:4500,baseMax:9500,lokalMin:900,lokalMax:3600},
    feuerbestattung:{name:'Feuerbestattung',icon:'\U0001f525',desc:'Einäscherung + Urnenbeisetzung auf Friedhof',baseMin:3500,baseMax:7500,lokalMin:550,lokalMax:2100},
    seebestattung:{name:'Seebestattung',icon:'\U0001f30a',desc:'Einäscherung + Beisetzung auf See',baseMin:3500,baseMax:6500,lokalMin:0,lokalMax:0},
    baumbestattung:{name:'Baumbestattung',icon:'\U0001f333',desc:'Einäscherung + Beisetzung an einem Baum',baseMin:3000,baseMax:6000,lokalMin:0,lokalMax:0},
    anonyme:{name:'Anonyme Bestattung',icon:'\U0001f54a',desc:'Einfache Bestattung ohne Grabstelle',baseMin:1500,baseMax:3500,lokalMin:250,lokalMax:700},
    direktkremation:{name:'Direktkremation',icon:'⚱',desc:'Einäscherung ohne Trauerfeier — Urne wird beigesetzt oder übergeben',baseMin:1000,baseMax:2200,lokalMin:0,lokalMax:0}
  };"""

OLD_BL = """  // Multiplier 1:1 aus bestattungskosten-rechner (single source of truth, Mai 2026)
  var BUNDESLAENDER = [
    {code:'BY',name:'Bayern',mult:1.22},{code:'BW',name:'Baden-Württemberg',mult:1.20},{code:'HE',name:'Hessen',mult:1.15},
    {code:'BE',name:'Berlin',mult:1.15},{code:'HH',name:'Hamburg',mult:1.20},{code:'BR',name:'Bremen',mult:1.05},
    {code:'NW',name:'Nordrhein-Westfalen',mult:1.05},{code:'NI',name:'Niedersachsen',mult:1.02},
    {code:'SH',name:'Schleswig-Holstein',mult:0.95},{code:'RP',name:'Rheinland-Pfalz',mult:0.95},
    {code:'SL',name:'Saarland',mult:0.90},{code:'BB',name:'Brandenburg',mult:0.80},
    {code:'TH',name:'Thüringen',mult:0.80},{code:'SN',name:'Sachsen',mult:0.82},
    {code:'ST',name:'Sachsen-Anhalt',mult:0.78},{code:'MV',name:'Mecklenburg-Vorpommern',mult:0.78}
  ];"""
NEW_BL = """  // V2-Friedhofs-Faktoren, 1:1 aus bestattungskosten-rechner (single source of truth, Juni 2026):
  // verankert an den Friedhofsgebuehren der Landeshauptstadt (Aeternitas 2025, 20 J. vereinheitlicht).
  // Wirkt NUR auf den ortsgebundenen Anteil (lokalMin/lokalMax) — Herleitung: /methodik#kostenmodell
  var BUNDESLAENDER = [
    {code:'BY',name:'Bayern',mult:1.76},{code:'BW',name:'Baden-Württemberg',mult:1.13},{code:'HE',name:'Hessen',mult:1.05},
    {code:'BE',name:'Berlin',mult:0.48},{code:'HH',name:'Hamburg',mult:1.12},{code:'BR',name:'Bremen',mult:0.94},
    {code:'NW',name:'Nordrhein-Westfalen',mult:1.36},{code:'NI',name:'Niedersachsen',mult:1.13},
    {code:'SH',name:'Schleswig-Holstein',mult:0.70},{code:'RP',name:'Rheinland-Pfalz',mult:0.91},
    {code:'SL',name:'Saarland',mult:1.24},{code:'BB',name:'Brandenburg',mult:0.68},
    {code:'TH',name:'Thüringen',mult:0.99},{code:'SN',name:'Sachsen',mult:0.60},
    {code:'ST',name:'Sachsen-Anhalt',mult:1.15},{code:'MV',name:'Mecklenburg-Vorpommern',mult:0.91}
  ];"""

OLD_CALC = """    // V2.1: Adjusted Range — wenn User Posten als "separat" markiert, aus Vergleich rausrechnen
    var baseMin=ba.baseMin, baseMax=ba.baseMax;
    var origMin=ba.baseMin;
    var separatList=[];
    Object.keys(SEPARAT_KOSTEN).forEach(function(key){
      var sp=SEPARAT_KOSTEN[key];
      if(sp.condBA && sp.condBA.indexOf(state.bestattungsart)===-1)return;
      if(sp.excludeBA && sp.excludeBA.indexOf(state.bestattungsart)>=0)return;
      if(state.separat[key]){
        // V3.1 (Range-Collapse-Fix): typischen Mittelwert abziehen — Breite bleibt erhalten,
        // statt asymmetrisch min/max gegeneinander auszuspielen (was die Range aufblähte).
        var mid=(sp.min+sp.max)/2;
        baseMin-=mid;
        baseMax-=mid;
        separatList.push(sp);
      }
    });
    // V3.1 Floor: Range darf nicht unter ~35% der Original-Untergrenze kollabieren und behält
    // eine sinnvolle Mindestbreite — sonst hebelt der Nutzer mit "separat"-Haken unbemerkt den
    // Unterpreis-Schutz aus (vorher kollabierte sie auf 200–… → immer grün).
    var floorMin=Math.round(origMin*0.35);
    if(baseMin<floorMin)baseMin=floorMin;
    if(baseMax<baseMin*1.4)baseMax=Math.round(baseMin*1.4);
    var rangeMin=Math.round(baseMin*mult/100)*100;
    var rangeMax=Math.round(baseMax*mult/100)*100;"""
NEW_CALC = """    // V4 (Modell V2, Juni 2026): Regionalfaktor wirkt nur auf den ortsgebundenen Anteil.
    // Range = (konstanter Anteil) + (lokaler Anteil × Faktor). Konsistent mit
    // Kostenrechner + /bestattungskosten-nach-bundesland (Herleitung: /methodik#kostenmodell).
    var konstMin=ba.baseMin-ba.lokalMin, konstMax=ba.baseMax-ba.lokalMax;
    var lokalMin=ba.lokalMin, lokalMax=ba.lokalMax;
    var origRangeMin=Math.round(konstMin+lokalMin*mult);
    var separatList=[];
    Object.keys(SEPARAT_KOSTEN).forEach(function(key){
      var sp=SEPARAT_KOSTEN[key];
      if(sp.condBA && sp.condBA.indexOf(state.bestattungsart)===-1)return;
      if(sp.excludeBA && sp.excludeBA.indexOf(state.bestattungsart)>=0)return;
      if(state.separat[key]){
        // V3.1 (Range-Collapse-Fix): typischen Mittelwert abziehen — Breite bleibt erhalten.
        // V4: Friedhofs-Posten ist ortsgebunden → wird aus dem lokalen Anteil abgezogen,
        // überregionale Posten (Krematorium, Trauerhalle) aus dem konstanten Anteil.
        var mid=(sp.min+sp.max)/2;
        if(key==='friedhof'){
          lokalMin=Math.max(0,lokalMin-mid); lokalMax=Math.max(0,lokalMax-mid);
        } else {
          konstMin-=mid; konstMax-=mid;
        }
        separatList.push(sp);
      }
    });
    var rangeMin=Math.round((konstMin+lokalMin*mult)/100)*100;
    var rangeMax=Math.round((konstMax+lokalMax*mult)/100)*100;
    // V3.1 Floor (auf regionalisierte Original-Untergrenze bezogen): Range darf nicht
    // kollabieren — sonst hebeln "separat"-Haken den Unterpreis-Schutz aus.
    var floorMin=Math.round(origRangeMin*0.35/100)*100;
    if(rangeMin<floorMin)rangeMin=floorMin;
    if(rangeMax<rangeMin*1.4)rangeMax=Math.round(rangeMin*1.4/100)*100;"""

OLD_METH = "Vergleich der Gesamtsumme mit typischen Preisrahmen nach Bestattungsart × Bundesland (Datenbasis: Stiftung Warentest, BDB, Aeternitas e.V., Verbraucherzentralen — Stand Mai 2026)."
NEW_METH = "Vergleich der Gesamtsumme mit typischen Preisrahmen nach Bestattungsart × Bundesland. Der regionale Anteil (Friedhofsgebühren, Beisetzung) ist an den Gebühren der Landeshauptstädte verankert (Aeternitas 2025), überregionale Posten sind bundesweit konstant angesetzt (Richtwerte: Stiftung Warentest, BDB, Verbraucherzentralen — Stand Juni 2026, Herleitung in der <a href=\"/methodik#kostenmodell\" style=\"color:var(--mr-primary)\">Methodik</a>)."

OLD_CRUMB = """    <div style="font-size:13px;color:var(--mr-text-muted);margin-bottom:16px">
      <a href="/" style="color:var(--mr-warm);text-decoration:none">Start</a> ›
      <a href="/bestattungskosten" style="color:var(--mr-warm);text-decoration:none">Bestattungskosten</a> ›
      Angebot prüfen
    </div>
"""

patch(P, [
    (OLD_BA, NEW_BA, 1),
    (OLD_BL, NEW_BL, 1),
    (OLD_CALC, NEW_CALC, 1),
    (OLD_METH, NEW_METH, 1),
    (OLD_CRUMB, '', 1),
])

# Plausibilitaets-Ausgabe der neuen Rahmen (Erd, ohne separat):
for bl, f in [('Berlin', 0.48), ('Bayern', 1.76), ('NRW', 1.36), ('Sachsen', 0.60)]:
    mn = round((4500 - 900 + 900 * f) / 100) * 100
    mx = round((9500 - 3600 + 3600 * f) / 100) * 100
    print('  Erdbestattung %s: %d-%d EUR (vorher V1: %d-%d)' % (bl, mn, mx,
          round(4500 * (1.15 if bl == 'Berlin' else 1.22 if bl == 'Bayern' else 1.05 if bl == 'NRW' else 0.82) / 100) * 100,
          round(9500 * (1.15 if bl == 'Berlin' else 1.22 if bl == 'Bayern' else 1.05 if bl == 'NRW' else 0.82) / 100) * 100))
print('FERTIG')
