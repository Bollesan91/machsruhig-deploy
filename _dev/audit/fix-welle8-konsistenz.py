#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welle 8 (2026-06-10) — Externes SEO-Review (8,1/10) Quick Wins:
P4 Hauptseite /bestattungskosten harmonisieren (Muenchen 1.500-2.500 zu niedrig,
   Berlin faelschlich als teures Grossstadt-Beispiel, 300-400%-Praezision) |
P3 "kein Landesdurchschnitt" sichtbar unter der Tabelle |
P8 Embed-Code im Presse-Block |
P10 Rueckverlinkung: 16(+2 Alias) BL-Hubs + Kostenrechner -> BL-Vergleich.
Zahlen exakt aus Modell V2 / CSV (Welle 6).
"""
import io, sys, glob

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
    print('%s: %d OK' % (path, len(replacements)))

LINKSTYLE = ' style="color:var(--mr-primary)"'
BLLINK = '<a href="/bestattungskosten-nach-bundesland"' + LINKSTYLE + '>Bundesland-Vergleich</a>'

# ===== P4: Hauptseite harmonisieren =====
HS = 'bestattungskosten.html'
patch(HS, [
    # Friedhofsgebuehren-Block: Spanne + Quelle + Link
    ('<strong>Kosten: 300–3.000 €</strong><br>Regionale Unterschiede sind hier enorm. Ein Grabplatz in München kostet 5–10 mal mehr als in einem kleinen Ort. Friedhofsgemeinden sind meist günstiger als private Friedhöfe.',
     '<strong>Kosten: je nach Kommune und Grabart von wenigen hundert bis über 4.500 €</strong><br>Regionale Unterschiede sind enorm — jede Kommune legt die Gebühren per Satzung selbst fest. Im Vergleich der Landeshauptstädte reicht die Spanne fürs Sargwahlgrab von 964 € (Berlin) bis 4.578 € (München), auf 20 Jahre Nutzungszeit vereinheitlicht (Aeternitas 2025). Das regionale Kostenniveau aller 16 Länder zeigt unser ' + BLLINK + '.', 1),
    # Intro-Satz: unbelegte 5-10x-Praezision raus
    ('Bestattungskosten sind nicht überall gleich. Ein Grabplatz in München kostet 5–10 mal mehr als in einem kleinen Ort an der Nordsee.',
     'Bestattungskosten sind nicht überall gleich. Ein Grabplatz in München kostet ein Vielfaches dessen, was eine kleine Gemeinde verlangt.', 1),
    # Stadt vs. Land: Berlin-Fehler korrigieren
    ('In Großstädten (München, Hamburg, Berlin) sind Friedhofsgebühren deutlich höher. Auf dem Land sind sie günstiger. Ein Sarg kostet überall ähnlich — die Region macht\'s bei Friedhofsgebühren aus.',
     'In vielen Großstädten (München, Hamburg, Düsseldorf) sind Friedhofsgebühren deutlich höher — aber nicht in allen: Berlin hat trotz Millionenstadt die günstigsten Gebühren aller Landeshauptstädte (Aeternitas 2025). Auf dem Land sind sie meist günstiger. Ein Sarg kostet überall ähnlich — die Region macht\'s bei den Friedhofsgebühren aus.', 1),
    # Beispiele: an Modell V2 / Aeternitas angleichen
    ('<p><strong>München:</strong> Friedhofsgebühren für Grabplatz 1.500–2.500 €, Bestattung gesamt 10.000–12.000 €<br>\n    <strong>Berlin:</strong> Friedhofsgebühren 500–1.000 €, Bestattung gesamt 6.000–8.000 €<br>\n    <strong>Kleinstadt (Nordfriesland):</strong> Friedhofsgebühren 200–400 €, Bestattung 4.000–5.000 €</p>',
     '<p><strong>München:</strong> teuerste Landeshauptstadt — Sargwahlgrab ca. 4.600 € (20 Jahre, Aeternitas 2025); Erdbestattung im Modell 7.200–20.800 € inkl. Grabpflege<br>\n    <strong>Berlin:</strong> günstigste Landeshauptstadt — Sargwahlgrab 964 €; Erdbestattung im Modell 4.000–9.800 € inkl. Grabpflege<br>\n    <strong>Kleine Gemeinden:</strong> Friedhofsgebühren oft nur wenige hundert Euro — verbindlich ist die Gebührensatzung der Kommune. Alle 16 Länder im ' + BLLINK + '.</p>', 1),
    # Tipp-Box: Grammatik
    ('oder beim Friedhofsverwaltung anfragbar', 'oder bei der Friedhofsverwaltung erfragbar', 1),
    # FAQ-Praezision "300-400 %" — LD und DOM haben hier (vorbestehend) verschiedene Texte
    ('Friedhofsgebühren können regional um 300–400 % variieren.',
     'Friedhofsgebühren unterscheiden sich zwischen Kommunen teils um ein Vielfaches.', 1),
    ('regionale Friedhofsgebühren (bis 300–400 % Unterschied)',
     'regionale Friedhofsgebühren (zwischen Kommunen teils um ein Vielfaches verschieden)', 1),
])

# ===== P3 + P8: BL-Seite =====
BL = 'bestattungskosten-nach-bundesland.html'
patch(BL, [
    # P3: sichtbare Einordnung direkt unter der Tabelle
    ('    </table>\n    </div>\n\n    <figure style="margin:28px 0 8px">',
     '    </table>\n    </div>\n    <p style="font-size:13px;color:var(--mr-text-muted);margin:6px 0 0"><strong>Landeshauptstadt-basierter Regionalindex — kein echter Landesdurchschnitt.</strong> Innerhalb eines Bundeslandes können Stadt und Land stark abweichen; verbindlich ist die Gebührensatzung deiner Kommune.</p>\n\n    <figure style="margin:28px 0 8px">', 1),
    # P8: Embed-Code im Presse-Block
    ('keine erhobenen Marktpreise.</span>\n  </div>',
     'keine erhobenen Marktpreise.</span><br><span style="font-size:12px;color:var(--mr-text-muted)">Einbettungscode (Grafik + Quellenlink): </span><textarea readonly onclick="this.select()" style="width:100%;height:64px;font-size:11px;font-family:monospace;margin-top:4px;border:1px solid var(--mr-border);border-radius:6px;padding:6px">&lt;a href=&quot;https://machsruhig.de/bestattungskosten-nach-bundesland&quot;&gt;&lt;img src=&quot;https://machsruhig.de/assets/data/bestattungskosten-index-2026.svg&quot; alt=&quot;Bestattungskosten-Index nach Bundesland 2026 — Quelle: machsruhig.de (CC BY 4.0)&quot; width=&quot;700&quot;&gt;&lt;/a&gt;</textarea>\n  </div>', 1),
])

# ===== P10a: Rueckverlinkung aus den 16(+Alias) BL-Hubs =====
IDX = {'bayern': ('Bayern', 136), 'nordrhein-westfalen': ('Nordrhein-Westfalen', 117),
       'saarland': ('das Saarland', 111), 'sachsen-anhalt': ('Sachsen-Anhalt', 107),
       'baden-wuerttemberg': ('Baden-Württemberg', 106), 'baden-württemberg': ('Baden-Württemberg', 106),
       'niedersachsen': ('Niedersachsen', 106), 'hamburg': ('Hamburg', 106),
       'hessen': ('Hessen', 102), 'thueringen': ('Thüringen', 100), 'thüringen': ('Thüringen', 100),
       'bremen': ('Bremen', 97), 'mecklenburg-vorpommern': ('Mecklenburg-Vorpommern', 96),
       'rheinland-pfalz': ('Rheinland-Pfalz', 96), 'schleswig-holstein': ('Schleswig-Holstein', 86),
       'brandenburg': ('Brandenburg', 85), 'sachsen': ('Sachsen', 81), 'berlin': ('Berlin', 75)}
hubs = sorted(glob.glob('bestattung-in/*/index.html'))
done = 0
for h in hubs:
    slug = h.replace('\\', '/').split('/')[1]
    if slug not in IDX:
        print('SKIP (kein BL):', h); continue
    name, idx = IDX[slug]
    with io.open(h, 'r', encoding='utf-8') as fh:
        t = fh.read()
    if 'bestattungskosten-nach-bundesland' in t:
        print('SKIP (schon verlinkt):', h); continue
    anchor = '<div class="mr-sources">'
    if t.count(anchor) != 1:
        print('FATAL: Anker %dx in %s' % (t.count(anchor), h)); sys.exit(1)
    box = ('<div class="mr-hint">\n    <strong>Wie teuer ist %s im Vergleich?</strong> Unser <a href="/bestattungskosten-nach-bundesland"%s>Bundesland-Vergleich</a> zeigt das modellierte Kostenniveau aller 16 Länder — %s: Index %d (100 = bundesweiter Referenzwert, verankert an den Friedhofsgebühren der Landeshauptstädte).\n  </div>\n\n  ' % (name, LINKSTYLE, name, idx))
    t = t.replace(anchor, box + anchor, 1)
    with io.open(h, 'w', encoding='utf-8', newline='') as fh:
        fh.write(t)
    done += 1
print('Hubs verlinkt: %d' % done)

# ===== P10b: Kostenrechner -> BL-Vergleich =====
patch('tools/bestattungskosten-rechner/index.html', [
    ('(Nur wenn du am Ende das optionale Formular ausfüllst, übermittelst du die dort eingegebenen Kontaktdaten.)</p>',
     '(Nur wenn du am Ende das optionale Formular ausfüllst, übermittelst du die dort eingegebenen Kontaktdaten.) Wie dein Bundesland im Vergleich liegt, zeigt der <a href="/bestattungskosten-nach-bundesland"' + LINKSTYLE + '>Bundesland-Vergleich</a>.</p>', 1),
])
print('FERTIG')
