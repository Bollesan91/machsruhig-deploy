#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R1e (2026-06-10) — Live-Validity-FAIL beheben (Bezugsgroessen-Luecke):
ROOT CAUSE (Altbestand, nicht heute eingefuehrt): renderStep4() lief nur beim
Init mit leerer Bestattungsart -> ALLE Posten/Separat-Eintraege mit condBA
wurden nie gerendert (Friedhof-separat unsichtbar, Urne bei Feuerbestattung
unsichtbar, Krematorium-separat unsichtbar). Schritt-3-Anweisung ("hak separat
an") lief dadurch ins Leere -> falsche Beruhigung bei separat abgerechneten
Friedhofsgebuehren (haeufigster Realfall).
FIX 1: Bei Bestattungsart-Wahl Schritt-4-Listen fuer die gewaehlte Art neu
rendern (+ Posten-States zuruecksetzen, da BA-abhaengig).
FIX 2 (Validity-Nebenbefund): Gruen-Text nicht "liegt im ueblichen Rahmen"
behaupten, wenn die Summe sichtbar unter der angezeigten Untergrenze liegt
(Toleranzband) -> ehrliche Variante "knapp unter dem Rahmen - unauffaellig".
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

patch(P, [
    # FIX 1: Schritt-4-Listen bei BA-Wahl neu rendern
    ("""      btn.addEventListener('click',function(){
        state.bestattungsart=btn.dataset.ba;
        track('toolStep',{tool:'angebotspruefer',step:'1-select'});
        setStep(2);
      });""",
     """      btn.addEventListener('click',function(){
        state.bestattungsart=btn.dataset.ba;
        // R1e-Fix: Schritt-4-Listen sind BA-abhaengig (condBA/excludeBA) — neu rendern,
        // sonst bleiben sie auf dem Init-Stand (leere BA) und condBA-Posten fehlen komplett.
        state.posten={};state.separat={};state.info={};
        renderStep4();
        track('toolStep',{tool:'angebotspruefer',step:'1-select'});
        setStep(2);
      });""", 1),
    # FIX 2: Ehrlicher Gruen-Text im Toleranzband
    ("    var ps=priceMap[result.priceStatus], cs=compMap[result.completenessStatus];",
     """    var ps=priceMap[result.priceStatus], cs=compMap[result.completenessStatus];
    // R1e: Toleranzband ehrlich benennen — nicht "im Rahmen" behaupten, wenn die Summe
    // sichtbar unter der angezeigten Untergrenze liegt.
    if(result.priceStatus==='green'&&result.sum<result.rangeMin){
      ps={icon:ps.icon,title:ps.title,text:'Die Gesamtsumme liegt knapp unter dem üblichen Rahmen für '+esc(result.ba.name)+' in '+esc(state.bundesland)+' — das ist unauffällig.'};
    }
    if(result.priceStatus==='green'&&result.sum>result.rangeMax){
      ps={icon:ps.icon,title:ps.title,text:'Die Gesamtsumme liegt knapp über dem üblichen Rahmen für '+esc(result.ba.name)+' in '+esc(state.bundesland)+' — das ist unauffällig.'};
    }""", 1),
])
print('FERTIG')
