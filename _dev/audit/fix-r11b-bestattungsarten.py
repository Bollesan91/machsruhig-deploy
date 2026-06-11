#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R11b — Auflagen aus NO-GO-52:
K1: Naturbestattungs-Rechtsaussage falsch (Bayern/BW erlauben KEINE
    Verstreuung — Anbieter sitzen in der Schweiz/Oesterreich, Asche wird
    ueberfuehrt).
K2: Alle Prosa-Spannen (mit "Euro" geschrieben) auf das kanonische Modell;
    FAQ "guenstigste" inkl. JSON-LD korrigiert (Direktkremation ist laut
    eigener Tabelle die guenstigste).
K/H: Diamantbestattung — Rechtslage DE ergaenzt (keine Asche-Aushaendigung an
    Private, Abwicklung ueber NL/CH, RLP-Oeffnung).
H:  FAQ "Bestattungsart aendern" — Vorsorge aendern vs. vollzogene Beisetzung
    (Umbettung genehmigungspflichtig, wichtiger Grund, oft abgelehnt).
M:  "ca. 70 %" -> "rund drei Viertel" (3x inkl. JSON-LD); Feuer-Tabellenzelle
    juristisch sauber (Bestattungswald = ausgewiesener Bestattungsplatz);
    Kolumbarium-"sehr preiswert"-Tonalitaet.
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

# K1: Naturbestattung
rep('Die Asche wird auf einer Almwiese oder spezialisierten Naturfläche verstreut. Dies ist nur in bestimmten Regionen erlaubt (besonders Bayern und Baden-Württemberg). Kosten: typischerweise 3.000 bis 4.500 Euro. Ein vollständiger Kreislauf zur Natur — die Asche wird Teil der Wiese, kein Grabstein, keine Grabpflicht. Es ist eine Wahl für umweltbewusste Menschen.',
    'Die Asche wird auf einer Almwiese oder einer anderen Naturfläche verstreut oder beigesetzt. In Deutschland lässt der Friedhofszwang das — von den im Rechtsabschnitt genannten Ausnahmen abgesehen — nicht zu: Solche Bestattungen laufen praktisch ausschließlich über Anbieter in der Schweiz oder in Österreich, wohin die Urne überführt wird. Die Preise sind freie Anbieterpreise (zzgl. Einäscherung und Überführung). Kein Grabstein, keine Grabpflege — eine Wahl für naturverbundene Menschen, die keinen festen Ort in der Nähe brauchen.')

# K2: Prosa-Spannen kanonisch
rep('Die Kosten für eine Erdbestattung liegen typischerweise zwischen 4.000 und 12.000 Euro.',
    'Die Kosten für eine Erdbestattung liegen typischerweise zwischen 3.700 und 9.300 Euro — zuzüglich Grabpflege über die Jahre, die die Gesamtsumme auf 5.300 bis 14.300 Euro heben kann.')
rep('Feuerbestattungen sind deutlich kostengünstiger als Erdbestattungen — typischerweise zwischen 2.000 und 5.000 Euro.',
    'Feuerbestattungen sind meist günstiger als Erdbestattungen — typischerweise zwischen 3.400 und 8.200 Euro (ohne Grabpflege); eine Direktkremation ohne Feier beginnt bei rund 1.000 Euro.')
rep('Die Kosten liegen typischerweise zwischen 4.000 und 6.000 Euro.',
    'Die Kosten liegen typischerweise zwischen 2.850 und 6.200 Euro.')
rep('Kosten: typischerweise 1.500 bis 3.500 Euro.</p>',
    'Kosten: typischerweise 3.050 bis 7.000 Euro.</p>')
rep('Kosten typischerweise 1.500 bis 3.500 Euro. Du besuchst die Nische, lässt Blumen da, magst aber keinen Grabstein im klassischen Sinne. Vorteil: Sehr preiswert und wartungsfrei. Nachteil: Weniger emotionale Verbindung, weniger Gestaltungsfreiheit.',
    'Die Kosten entsprechen einer Feuerbestattung; die Stellplatzgebühr für die Nische regelt die jeweilige Friedhofssatzung. Du besuchst die Nische und kannst Blumen ablegen — einen Grabstein im klassischen Sinne gibt es nicht. Vorteil: wartungsfrei und wetterunabhängig. Nachteil: weniger Gestaltungsfreiheit als ein eigenes Grab.')
rep('Die anonyme Bestattung ist die kostengünstigste Option — ab etwa 1.200–2.000 Euro.',
    'Die anonyme Bestattung gehört zu den günstigsten Optionen — typischerweise 1.800 bis 3.350 Euro.')

# K2: FAQ "guenstigste" (JSON-LD + sichtbar, unterschiedliche Wrapper, gleicher Text)
rep('Die anonyme Bestattung kostet ab etwa 1.200–2.000 Euro. Kolumbarium und einfache Baumbestattungen ab ca. 1.500–3.500 Euro. Zum Vergleich: Eine klassische Erdbestattung mit Grabstein kostet typischerweise 4.000–12.000 Euro.',
    'Die günstigste Form ist die Direktkremation ohne Trauerfeier (rund 1.000–2.200 Euro), gefolgt von der anonymen Beisetzung (rund 1.800–3.350 Euro). Zum Vergleich: Eine klassische Erdbestattung kostet typischerweise 3.700–9.300 Euro, mit Grabpflege über die Jahre 5.300–14.300 Euro.', 2)

# K/H: Diamantbestattung Rechtslage
rep('Kosten: 5.000–25.000 Euro (extrem teuer). Nur für Familien mit großem Budget und besonderem Anspruch. Nicht überall rechtlich akzeptiert oder religiös anerkannt.',
    'Kosten: 5.000–25.000 Euro als freie Anbieterpreise — zuzüglich der regulären Bestattung der übrigen Asche. Wichtig zur Rechtslage: In Deutschland wird die Totenasche grundsätzlich nicht an Privatpersonen ausgehändigt und eine Asche-Teilung ist nicht vorgesehen; Anbieter wickeln die Herstellung deshalb in der Regel über die Niederlande oder die Schweiz ab. Eine inländische Öffnung gibt es bislang nur in Rheinland-Pfalz, dessen neues Bestattungsgesetz Erinnerungsstücke aus Teilen der Asche zulässt.')

# H: FAQ Bestattungsart aendern (sichtbar + JSON-LD — exakten Text holen wir per Suche)
OLD_CHANGE = None
import re
m = re.search(r'"name":"Kann ich meine Bestattungsart[^"]*","acceptedAnswer":\{"@type":"Answer","text":"([^"]+)"', t)
if not m:
    print('FATAL: Aendern-FAQ nicht gefunden'); sys.exit(1)
old_answer = m.group(1)
new_answer = 'Zwei Fälle: Eine Vorsorge oder Verfügung kannst du jederzeit problemlos ändern, solange nichts vollzogen ist. Nach einer vollzogenen Beisetzung ist eine Änderung dagegen kaum möglich: Eine Umbettung greift in die Totenruhe ein, ist genehmigungspflichtig, setzt einen wichtigen Grund voraus und wird häufig abgelehnt.'
c = t.count(old_answer)
if c not in (1, 2):
    print('FATAL: Aendern-Antwort %d mal' % c); sys.exit(1)
t = t.replace(old_answer, new_answer)
print('Aendern-FAQ ersetzt (%dx): %s...' % (c, old_answer[:80]))

# M: 70 % -> rund drei Viertel (3x: JSON-LD, Keyfact, Sektion + sichtbare FAQ)
rep('Die Feuerbestattung ist mit ca. 70 % die häufigste Bestattungsart in Deutschland.',
    'Die Feuerbestattung ist mit rund drei Vierteln aller Bestattungen die häufigste Form in Deutschland.', 2)
rep('<li>Ca. 70 % der Bestattungen sind Feuerbestattungen in Deutschland</li>',
    '<li>Rund drei Viertel der Bestattungen in Deutschland sind Feuerbestattungen</li>')
rep('Mit etwa 70 % aller Bestattungen ist die Feuerbestattung (auch Kremation genannt) mittlerweile Standard in Deutschland.',
    'Mit rund drei Vierteln aller Bestattungen ist die Feuerbestattung (auch Kremation genannt) mittlerweile Standard in Deutschland.')

# M: Feuer-Tabellenzelle juristisch sauber
rep('<td>Ja — für die Urne gilt Friedhofszwang (Ausnahmen: See-, Baum-/Wald­bestattung)</td>',
    '<td>Ja — für die Urne gilt Friedhofszwang; Bestattungswälder und See sind dafür zugelassene Bestattungsplätze bzw. -formen</td>')

io.open(P, 'w', encoding='utf-8', newline='').write(t)
import json
mm = re.search(r'<script type="application/ld\+json">(.*?)</script>', t, re.S)
json.loads(mm.group(1))
assert t.count('70 %') == 0 and t.count('1.200–2.000') == 0 and t.count('4.000 und 12.000') == 0
print('R11b OK + JSON-LD valide')
