#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R1d (2026-06-10) — SEO-Review-Auflagen (GO 80):
M1 Tool-Basisspannen aus Methodik-Komponententabelle abgeleitet (Erd 3700-9300,
   Feuer 3380-8200 = konstant exakt 2800/5700 bzw. 2830/6100 + lokal) ->
   vollstaendig reproduzierbar; Landing-Beispiel neu gerechnet (NRW Feuer 3.600-9.000);
   Methodik-Satz zu Angebotspruefer-Spannen + uebrigen Bestattungsarten |
M2 Umami-Claim praezisiert (Nutzungsschritte, nicht nur Seitenbesuch) |
M3 Friedhof-separat-Abzug je Bestattungsart (statt pauschal 2.050) |
M4 anonyme: Sarg sichtbar, Friedhof-separat moeglich, "gekennzeichnete Grabstelle" |
K1 Beispiel-Treue | K2 Singular/Plural | K3 LD-Description | K4 Breadcrumb-Slash |
K6 Direktkremation-Selbstreferenz | K8 KEIN->kein.
"""
import io, sys

P = 'tools/angebotspruefer/index.html'

def patch(path, replacements):
    with io.open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()
    for i, (old, new, expect) in enumerate(replacements):
        c = text.count(old)
        if c != expect:
            print('FATAL #%d: %r -> %d (erwartet %d) in %s' % (i, old[:70], c, expect, path)); sys.exit(1)
        text = text.replace(old, new)
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)
    print('%s: %d Ersetzungen OK' % (path, len(replacements)))

patch(P, [
    # --- M1: Basisspannen = Komponententabelle (ohne Grabpflege) ---
    ("desc:'Sarg, Friedhof, Beisetzung mit Grabstelle',baseMin:4500,baseMax:9500,lokalMin:900,lokalMax:3600",
     "desc:'Sarg, Friedhof, Beisetzung mit Grabstelle',baseMin:3700,baseMax:9300,lokalMin:900,lokalMax:3600", 1),
    ("desc:'Einäscherung + Urnenbeisetzung auf Friedhof',baseMin:3500,baseMax:7500,lokalMin:550,lokalMax:2100",
     "desc:'Einäscherung + Urnenbeisetzung auf Friedhof',baseMin:3380,baseMax:8200,lokalMin:550,lokalMax:2100", 1),
    # Landing-Beispiel neu (NRW Feuer: 2830/6100 + 550/2100 x 1,36 -> 3.600-9.000)
    ('Der vergleichbare Rahmen liegt bei ca. 3.700–8.300 €:',
     'Der vergleichbare Rahmen liegt bei ca. 3.600–9.000 €:', 1),
    # --- M2: Umami-Claim ---
    ('Anonyme Reichweiten-Statistiken (Umami) erfassen nur den Seitenbesuch, nicht deine Eingaben.',
     'Anonyme Reichweiten-Statistiken (Umami) erfassen den Seitenbesuch und anonyme Nutzungsschritte (z. B. ob ein Check abgeschlossen wurde) — nicht deine Eingaben.', 1),
    # --- M3 + M4b: Friedhof-separat: condBA + Abzug je Bestattungsart ---
    ("friedhof:{label:'Friedhofsgebühren (Stadt rechnet direkt mit mir ab)',min:1300,max:2800,condBA:['erdbestattung','feuerbestattung','baumbestattung','direktkremation']},",
     "friedhof:{label:'Friedhofsgebühren (Stadt rechnet direkt mit mir ab)',min:1300,max:2800,condBA:['erdbestattung','feuerbestattung','baumbestattung','anonyme']},", 1),
    ("""        var mid=(sp.min+sp.max)/2;
        if(key==='friedhof'){
          lokalMin=Math.max(0,lokalMin-mid); lokalMax=Math.max(0,lokalMax-mid);
        } else {
          konstMin-=mid; konstMax-=mid;
        }""",
     """        var mid=(sp.min+sp.max)/2;
        if(key==='friedhof'){
          // V4.1: Abzug = modell-eigener Friedhofs-Anteil der gewaehlten Bestattungsart
          // (Erd 600-2800 -> 1700, Feuer 300-1500 -> 900, anonym 150-400 -> 275);
          // Baum: Waldfriedhof-Gebuehren stecken im konstanten Anteil (-1200).
          var fhMid={erdbestattung:1700,feuerbestattung:900,anonyme:275}[state.bestattungsart];
          if(fhMid===undefined){ konstMin-=1200; konstMax-=1200; }
          else { lokalMin=Math.max(0,lokalMin-fhMid); lokalMax=Math.max(0,lokalMax-fhMid); }
        } else {
          konstMin-=mid; konstMax-=mid;
        }""", 1),
    # --- M4a: Sarg auch bei anonymer Bestattung sichtbar (Kremationssarg Pflicht) ---
    ("{key:'sarg',label:'Sarg',pflicht:true,excludeBA:['seebestattung','anonyme'],info:'Bei Seebestattung Sondersarg im \"Krematorium\"-Posten enthalten'}",
     "{key:'sarg',label:'Sarg',pflicht:true,excludeBA:['seebestattung'],info:'Bei Seebestattung Sondersarg im \"Krematorium\"-Posten enthalten; bei anonymer Bestattung einfacher Kremationssarg'}", 1),
    # --- M4c: Beschreibung anonyme ---
    ("desc:'Einfache Bestattung ohne Grabstelle',baseMin:1500,baseMax:3500",
     "desc:'Einfache Bestattung ohne gekennzeichnete Grabstelle',baseMin:1500,baseMax:3500", 1),
    # --- K1: Beispiel-Treue ---
    ('<div class="ampel-title" style="font-size:17px">Ein Posten klären</div><p class="ampel-text" style="font-size:13px">Die Überführung war nicht eindeutig ausgewiesen — vor der Unterschrift nachfragen, ob sie im Preis enthalten ist.</p>',
     '<div class="ampel-title" style="font-size:17px">Ein paar Posten klären</div><p class="ampel-text" style="font-size:13px">Einzelne Pflicht-Posten waren nicht eindeutig ausgewiesen — die Liste unterm Ergebnis zeigt, welche (im Beispiel: die Überführung) und was vor der Unterschrift zu klären ist.</p>', 1),
    # --- K2: Singular/Plural ---
    ("completenessReasons.push('Einzelne Posten sind nicht ausgewiesen ('+klärung.length+' Punkte zum Klären). Beim Bestatter-Gespräch kurz ansprechen.');",
     "completenessReasons.push(klärung.length===1?'Ein Posten ist nicht ausgewiesen (1 Punkt zum Klären). Beim Bestatter-Gespräch kurz ansprechen.':'Einzelne Posten sind nicht ausgewiesen ('+klärung.length+' Punkte zum Klären). Beim Bestatter-Gespräch kurz ansprechen.');", 1),
    ("' · <em style=\"color:var(--mr-text-muted)\">(Rahmen angepasst um '+result.separatList.length+' separat-abgerechnete Posten)</em>'",
     "' · <em style=\"color:var(--mr-text-muted)\">(Rahmen angepasst um '+result.separatList.length+(result.separatList.length===1?' separat abgerechneten Posten':' separat abgerechnete Posten')+')</em>'", 1),
    # --- K3: LD-Description ---
    ('Ampel-Bewertung, vermisste Posten und konkrete Fragen für den Bestatter.',
     'Ampel-Einschätzung, nicht ausgewiesene Posten und konkrete Fragen für den Bestatter.', 1),
    # --- K4: Breadcrumb-Slash konsistent zum Canonical ---
    ('{"@type":"ListItem","position":3,"name":"Angebot prüfen","item":"https://machsruhig.de/tools/angebotspruefer"}',
     '{"@type":"ListItem","position":3,"name":"Angebot prüfen","item":"https://machsruhig.de/tools/angebotspruefer/"}', 1),
    # --- K6: Direktkremation-Selbstreferenz vermeiden ---
    ("Das kann legitim sein (z.B. Direktkremation als eigene Bestattungsart, Discounter, oder weil Posten separat abgerechnet werden)",
     "Das kann legitim sein ('+(state.bestattungsart==='direktkremation'?'z.B. Discounter-Anbieter, oder weil Posten separat abgerechnet werden':'z.B. Direktkremation als eigene Bestattungsart, Discounter, oder weil Posten separat abgerechnet werden')+')", 1),
    # --- K8: Caps raus ---
    ('Das ist KEIN Vorwurf, oft sind sie nur anders gebündelt.',
     'Das ist <em>kein</em> Vorwurf — oft sind sie nur anders gebündelt.', 1),
])

# --- M1: Methodik-Bezug Angebotspruefer ---
patch('methodik.html', [
    ('Ohne Grabpflege: ca. 3.400–8.200 € (Feuer) bzw. 3.700–9.300 € (Erd). Spannen = „alle Posten am unteren Rand“ bis „alle Posten am oberen Rand“.',
     'Ohne Grabpflege: ca. 3.400–8.200 € (Feuer) bzw. 3.700–9.300 € (Erd). Spannen = „alle Posten am unteren Rand“ bis „alle Posten am oberen Rand“. Der <a href="/tools/angebotspruefer/" style="color:var(--mr-primary)">Angebotsprüfer</a> nutzt für Erd- und Feuerbestattung genau diese Komponenten ohne Grabpflege; für See-, Baum-, anonyme Bestattung und Direktkremation verwendet er eigene Richtwert-Spannen außerhalb des Komponentenmodells.', 1),
])
print('FERTIG')
