#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R3c (Loop-Iteration 2, Re-Review NO-GO 64) — verbleibende Blocker H1-H4 + M1-M5 + L:
H1 Keyfact anonym-Mix -> Direktkremation 1.000-2.200 | H2 Sarg-Selbstwiderspruch |
H3 Sozial-FAQ Par.-74-konform (DOM, LD regeneriert; auch Zumutbarkeit statt Armut,
Erbausschlagung, Anspruchsnorm statt Ermessen) | H4 Spartipp 40-50% -> ~30% modellnah |
M1 Erben->bestattungspflichtige Person | M2 "Friedhoefe erheben Grabpflegegebuehren"
sachlich falsch | M3 Grabmal-Einzelfall statt kategorisch | M4 Durchschnitt mit
Quellenzuordnung | M5 Grabpflege-Asymmetrie in FAQ deklariert |
L1 Spartipp-Titel/FAQ | L2/L3 zweiten CTA-Block raus | L4 Quellenbox ergaenzt |
L5 Fussnote Richtwert-Arten | L6 "Typisch" -> "Mitte der Spanne".
"""
import io, re, sys, json

P = 'bestattungskosten.html'
t = io.open(P, encoding='utf-8').read()

def rep(old, new, expect=1):
    global t
    c = t.count(old)
    if c != expect:
        print('FATAL: %r -> %d (erwartet %d)' % (old[:70], c, expect)); sys.exit(1)
    t = t.replace(old, new)

# H1
rep('<li>Einfachste Variante (anonym): 1.000–2.000 €</li>',
    '<li>Einfachste Variante (Direktkremation): 1.000–2.200 €</li>')
# M4 Keyfact + FAQ (FAQ: DOM+LD -> 2)
rep('<li>Durchschnittliche Kosten: 6.000–8.000 €</li>',
    '<li>Durchschnittliche Kosten laut Branchenangaben (BDB): 6.000–8.000 €</li>')
rep('Im Durchschnitt kostet eine Bestattung in Deutschland 6.000–8.000 €.',
    'Im Durchschnitt kostet eine Bestattung in Deutschland laut Branchenangaben (BDB) 6.000–8.000 €.', 2)
# M5 FAQ-Asymmetrie deklarieren (DOM+LD)
rep('eine Feuerbestattung mit Urnengrab liegt im Modell bei ca. 3.400–8.200 €, eine Erdbestattung inkl. Grabpflege bei ca. 5.300–14.300 €.',
    'eine Feuerbestattung mit Urnengrab liegt im Modell bei ca. 3.400–8.200 € (ohne Grabpflege; mit: ca. 3.800–9.700 €), eine Erdbestattung inkl. Grabpflege bei ca. 5.300–14.300 €.', 2)
# H2 Sarg
rep('Ein einfacher Sarg kostet 500–1.000 €, ein edlerer 1.500–3.000 €.',
    'Ein einfacher Sarg kostet im Modell 600–1.000 €, mittlere Ausführungen 1.200–2.200 €; Premium-Modelle liegen darüber.')
# H4 Spartipp
rep('onen deutlich günstiger als Erdbestattungen — oft 40–50 % weniger.</p>',
    'onen deutlich günstiger als Erdbestattungen — rechnet man die Grabpflege mit ein, im Modell oft rund 30 % weniger.</p>')
# H3 Sozial-FAQ (DOM+LD -> 2)
rep('Das Sozialamt kann die Kosten für eine Bestattung übernehmen, wenn die Erben zu arm sind (§74 SGB XII). Die Bestattung ist einfach und kostengünstig (1.500–2.500 €) und umfasst das Notwendigste — keine Trauerfeier oder Grabstein.',
    'Wenn dir als bestattungspflichtiger Person die Kosten nicht zumutbar sind, übernimmt das Sozialamt die erforderlichen Kosten einer ortsüblichen, würdigen Bestattung (§ 74 SGB XII) — das gilt auch, wenn du das Erbe ausgeschlagen hast. Geprüft wird die Zumutbarkeit im Einzelfall; vorrangig zählen der Nachlass und Leistungen wie ein Sterbegeld. In der Regel ohne Trauerfeier; ob ein einfaches Grabmal übernommen wird, entscheidet die Kommune.', 2)
# M1 Sozial-Intro
rep('Wenn die Erben die Bestattung nicht bezahlen können, hilft das Sozialamt.',
    'Wenn der bestattungspflichtigen Person die Kosten nicht zumutbar sind, übernimmt das Sozialamt.')
# M3 Enthalten-Liste: Nicht-Element raus + Einzelfall-Satz
rep('''      <li>Behördengänge</li>
      <li>Keine Trauerfeier, kein Grabstein</li>
    </ul>

    <p>Die Kosten liegen bei 1.500–2.500 €, je nach Region.</p>''',
    '''      <li>Behördengänge</li>
    </ul>
    <p>In der Regel ist keine Trauerfeier enthalten; ob ein einfaches Grabmal übernommen wird, entscheidet die Kommune im Einzelfall. Die Kommune trägt die ortsüblichen Kosten direkt.</p>''')
# M2 Grabpflege ist keine Friedhofsgebuehr
rep('Friedhöfe erheben Grabpflegegebühren für den Zeitraum der Ruhe (meistens 20–25 Jahre). Im Modell liegen sie bei',
    'Grabpflege ist keine Friedhofsgebühr: Über die Ruhezeit (meistens 20–25 Jahre) pflegst du das Grab selbst oder beauftragst eine Friedhofsgärtnerei (Dauergrabpflege). Im Modell liegen die Kosten bei')
# L1 Spartipp-Titel + FAQ-Satz (DOM+LD -> 2)
rep('<h4>4. Friedhofsgemeinde statt privat</h4>', '<h4>4. Gebührensatzungen vergleichen</h4>')
rep('nutze einfache Materialien, wähle einen kommunalen Friedhof, organisiere eine schlichte Trauerfeier',
    'nutze einfache Materialien, vergleiche die Gebührensatzungen der Friedhöfe vor Ort, organisiere eine schlichte Trauerfeier', 2)
# L2/L3 zweiten CTA-Block entfernen
m = re.search(r'\s*<div class="mr-cta-block no-print">\s*<h2>Berechne deine Kosten</h2>.*?</div>', t, re.S)
assert m and len(m.group(0)) < 800, 'CTA-Block 2 nicht sauber gefunden'
t = t.replace(m.group(0), '', 1)
# L5 Fussnote
rep('<p>Modell-Basisspannen ohne Grabpflege und vor Regionalfaktor (Herleitung in der',
    '<p>Erd- und Feuerbestattung: Modell-Basisspannen ohne Grabpflege und vor Regionalfaktor; See-, Baum-, anonyme Bestattung und Direktkremation: Richtwert-Spannen außerhalb des Komponentenmodells (Herleitung in der')
# L6 Spaltenkopf
rep('<th>Typisch</th>', '<th>Mitte der Spanne</th>')
# L4 Quellenbox ergaenzen
rep('<li>Jeweiliges Landesbestattungsgesetz des Bundeslandes</li>',
    '''<li>Regionalfaktoren: Friedhofsgebühren der Landeshauptstädte, Datengrundlage Aeternitas e. V., tabellarisch aufbereitet in <a href="https://www.check24.de/sterbegeldversicherung/friedhofsgebuehren-deutschland/" target="_blank" rel="noopener" style="color:var(--mr-primary)">dieser Übersicht</a></li>
      <li><a href="https://www.gesetze-im-internet.de/sgb_12/__74.html" target="_blank" rel="noopener" style="color:var(--mr-primary)">§ 74 SGB XII</a> (Sozialbestattung) · <a href="https://www.gesetze-im-internet.de/estg/__33.html" target="_blank" rel="noopener" style="color:var(--mr-primary)">§ 33 EStG</a> (außergewöhnliche Belastung)</li>
      <li>Jeweiliges Landesbestattungsgesetz des Bundeslandes</li>''')

# FAQ-LD aus DOM regenerieren
pairs = re.findall(r'<summary>([^<]+)</summary><div class="faq-answer">(?:<p>)?(.*?)(?:</p>)?</div>', t, re.S)
st = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()
m = re.search(r'(<script type="application/ld\+json">\s*)(\{.*?\})(\s*</script>)', t, re.S)
g = json.loads(m.group(2))
fn = [n for n in g['@graph'] if n.get('@type') == 'FAQPage'][0]
fn['mainEntity'] = [{'@type': 'Question', 'name': st(q), 'acceptedAnswer': {'@type': 'Answer', 'text': st(a)}} for q, a in pairs]
t = t[:m.start()] + m.group(1) + json.dumps(g, ensure_ascii=False, separators=(',', ':')) + m.group(3) + t[m.end():]

io.open(P, 'w', encoding='utf-8', newline='').write(t)
print('R3c OK (%d FAQ-Paare regeneriert)' % len(pairs))
