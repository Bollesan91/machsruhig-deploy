#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welle 9 (2026-06-10) — Feinschliff aus externem Richtigkeits-Rating (8,6/10):
P1 Einordnungszeile direkt unter dem Lead (Landeshauptstadt-Index, kein
   Landesdurchschnitt) | P3 Klarstellung Index != Faktor x 100 in der Methodik
   (faengt das naive Nachrechnen ab — Reviewer-Misreading Thueringen 0,99->99;
   real ergibt die publizierte Formel Index 100, von R5/R6 16/16 reproduziert) |
P5 "Belegt vs. modelliert"-Box auf der BL-Seite.
P2/P4 waren bereits live (Welle 8b).
"""
import io, sys

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

BL = 'bestattungskosten-nach-bundesland.html'
patch(BL, [
    # P1: Einordnung direkt unter dem Lead
    ('verankert an den auf 20 Jahre vereinheitlichten Friedhofsgebühren der Landeshauptstädte.</p>',
     'verankert an den auf 20 Jahre vereinheitlichten Friedhofsgebühren der Landeshauptstädte.</p>\n    <p style="font-size:13px;color:var(--mr-text-muted);margin-top:6px"><strong>Landeshauptstadt-basierter Regionalindex — kein echter Landesdurchschnitt aller Kommunen.</strong></p>', 1),
    # P5: Belegt-vs-modelliert-Box vor der Quellen-Box
    ('  <div class="mr-sources">\n    <h2>Quellen &amp; Methodik</h2>',
     '''  <div class="mr-hint" style="margin:16px 0">
    <strong>Was ist belegt, was ist modelliert?</strong><br>
    <span style="font-size:14px"><strong>Belegt (Aeternitas 2025):</strong> die Friedhofsgebühren der 16 Landeshauptstädte je Grabart (z.&nbsp;B. München 4.578 €, Berlin 964 € fürs Sargwahlgrab, auf 20 Jahre vereinheitlicht) und die starke Spreizung zwischen Kommunen.<br>
    <strong>Modelliert (machsruhig.de):</strong> die bundesweiten Komponenten-Spannen des Standard-Szenarios, der daraus abgeleitete Index, die Euro-Spannen je Bundesland und die Annahme, dass die Grabpflege mit dem Regionalfaktor skaliert. Herleitung: <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik</a>.</span>
  </div>

  <div class="mr-sources">
    <h2>Quellen &amp; Methodik</h2>''', 1),
])

patch('methodik.html', [
    # P3: Index != Faktor x 100 klarstellen
    ('geteilt durch denselben Wert des Basis-Szenarios, mal 100; der Mittelwert der 16 Länderwerte liegt bei rund 100.</p>',
     'geteilt durch denselben Wert des Basis-Szenarios, mal 100; der Mittelwert der 16 Länderwerte liegt bei rund 100. <strong>Der Index ist damit bewusst nicht einfach Faktor mal 100:</strong> Weil die bundesweit konstanten Posten (Bestatterleistungen, Sarg/Urne) nicht mitskalieren, dämpfen sie die Spreizung — Thüringen hat z.&nbsp;B. den Faktor 0,99, aber Index 100. Alle Werte sind aus den hier veröffentlichten, gerundeten Faktoren exakt reproduzierbar.</p>', 1),
])
print('FERTIG')
