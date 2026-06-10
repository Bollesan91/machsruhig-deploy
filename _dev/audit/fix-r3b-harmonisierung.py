#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R3b (Loop-Iteration 2, Review NO-GO 58) — Legacy-Zahlenwelt von /bestattungskosten
ans Komponentenmodell anbinden. K1 Grabpflege-Mathe (3 unvereinbare Angaben),
K2 erfundene Sozialbestattungs-Voraussetzung (Par. 74 SGB XII korrekt),
K3 Hero-Spanne, M1-M10 (Kostenposten/Tabelle/FAQ/URLs/Doppelsektion/Sie-Form/
Quellen/Spartipp), S-Punkte. FAQ-LD wird aus dem DOM regeneriert (Paritaet).
"""
import io, re, sys, json

P = 'bestattungskosten.html'
t = io.open(P, encoding='utf-8').read()
warn = []

def rep(old, new, expect=1, hard=True):
    global t
    c = t.count(old)
    if c != expect:
        if hard:
            print('FATAL: %r -> %d (erwartet %d)' % (old[:70], c, expect)); sys.exit(1)
        warn.append('%r -> %d' % (old[:50], c)); return
    t = t.replace(old, new)

# K3 Hero
rep('Eine Bestattung kostet zwischen 2.000 und 15.000 Euro — je nachdem, wofür du dich entscheidest.',
    'Eine Bestattung kostet meist zwischen rund 1.000 € (Direktkremation) und 15.000 € und mehr (Erdbestattung mit allem Drum und Dran) — je nachdem, wofür du dich entscheidest und wo du wohnst.')

# K1 Grabpflege (3 Stellen vereinheitlicht auf Modell: Erd 80-250 EUR/J., ~20 J., 1.600-5.000)
rep('Diese liegen bei 10–50 € pro Jahr, je nach Region und Grabgröße. Über 25 Jahre addiert sich das zu 3.000–8.000 €.',
    'Im Modell liegen sie bei 80–250 € pro Jahr — über die übliche Ruhezeit von rund 20 Jahren also insgesamt ca. 1.600–5.000 €. Eigenpflege ist günstiger, professionelle Dauergrabpflege liegt darüber.')
rep('<li>Laufende Grabpflege: 3.000–8.000 € über 25 Jahre</li>',
    '<li>Laufende Grabpflege (Erdbestattung): ca. 1.600–5.000 € über ~20 Jahre</li>')
rep('Bei Erdbestattung entstehen Grabpflegegebühren für 20–25 Jahre (insgesamt 3.000–8.000 €). Grabstein-Instandhaltung kostet 50–200 € pro Jahr optional. Andere Bestattungsarten haben keine laufenden Kosten.',
    'Bei einer Erdbestattung fallen über die Ruhezeit (~20 Jahre) Grabpflegekosten von insgesamt ca. 1.600–5.000 € an, beim Urnengrab ca. 400–1.500 € über ~10 Jahre. See- und Baumbestattung sind weitgehend folgekostenfrei. Grabstein-Instandhaltung kommt optional dazu.', 2)

# K2 Sozialbestattung (Par. 74 SGB XII korrekt)
rep('''      <li>Die Erben bedürftig sind (Einkommen unter dem Existenzminimum)</li>
      <li>Der Verstorbene der Kommune als Bedürftiger bekannt war</li>
      <li>Keine Sterbegeldversicherung oder sonstige Mittel vorhanden sind</li>''',
    '''      <li>Dir als bestattungspflichtiger Person die Kosten nicht zumutbar sind — das prüft das Sozialamt im Einzelfall anhand deines Einkommens und Vermögens (§ 74 SGB XII)</li>
      <li>Der Nachlass des Verstorbenen und vorrangige Mittel (z.&nbsp;B. eine Sterbegeldversicherung) nicht ausreichen</li>''')

# M1 Kostenposten ans Modell
rep('<strong>Kosten: 2.000–4.000 €</strong><br>Dies ist der größte Einzelposten',
    '<strong>Kosten: meist 1.800–3.500 €</strong><br>Dies ist der größte Einzelposten')
rep('Urnen sind meist günstiger (300–1.500 €). Nutze keine unnötig teuren Modelle — es kommt auf die innere Würde an, nicht auf die Dekoration.',
    'Urnen sind deutlich günstiger (im Modell 80–400 €; aufwendige Modelle darüber). Ein einfacher Sarg ist genauso würdevoll wie ein teurer.')
m = re.search(r'<h3>Sarg oder Urne</h3>\s*<p><strong>Kosten: ([0-9.–-]+) €</strong>', t)
if m:
    rep(m.group(0), m.group(0).replace(m.group(1), 'ca. 600–2.200'), 1, hard=False)

# M7 Grabstein
rep('Ein Grabmal kostet einmalig 1.000–3.000 €.',
    'Ein Grabmal kostet einmalig meist 400–7.000 € — je nach Ausführung von einfach bis aufwendig (Modellwerte).', 1, hard=False)
m = re.search(r'<h3>Grabstein/Grabmal</h3>\s*<p><strong>Kosten: ([0-9.–-]+) €</strong>', t)
if m:
    rep(m.group(0), m.group(0).replace(m.group(1), '400–7.000'), 1, hard=False)

# M2 Bestattungsarten-Tabelle auf Modell-Basen (ohne Grabpflege) + Direktkremation
rep('''          <tr><td><strong>Erdbestattung</strong></td><td>6.000–15.000 €</td><td>8.000–10.000 €</td><td>Ja, 25 Jahre</td></tr>
          <tr><td><strong>Feuerbestattung</strong></td><td>2.000–8.000 €</td><td>3.500–5.000 €</td><td>Je nach Lagerung</td></tr>
          <tr><td><strong>Seebestattung</strong></td><td>3.000–6.000 €</td><td>4.000–5.000 €</td><td>Nein</td></tr>
          <tr><td><strong>Baumbestattung</strong></td><td>2.500–7.000 €</td><td>4.000–5.500 €</td><td>Nein</td></tr>
          <tr><td><strong>Anonyme Bestattung</strong></td><td>1.000–2.500 €</td><td>1.500–2.000 €</td><td>Nein</td></tr>''',
    '''          <tr><td><strong>Erdbestattung</strong></td><td>3.700–9.300 €</td><td>ca. 6.500 €</td><td>Ja, meist 20–25 Jahre</td></tr>
          <tr><td><strong>Feuerbestattung</strong></td><td>3.400–8.200 €</td><td>ca. 5.800 €</td><td>Urnengrab: ja, ~10 Jahre</td></tr>
          <tr><td><strong>Seebestattung</strong></td><td>3.500–6.500 €</td><td>ca. 5.000 €</td><td>Nein</td></tr>
          <tr><td><strong>Baumbestattung</strong></td><td>3.000–6.000 €</td><td>ca. 4.500 €</td><td>Nein</td></tr>
          <tr><td><strong>Anonyme Bestattung</strong></td><td>1.500–3.500 €</td><td>ca. 2.500 €</td><td>Nein</td></tr>
          <tr><td><strong>Direktkremation</strong></td><td>1.000–2.200 €</td><td>ca. 1.600 €</td><td>Nein</td></tr>''')
rep('<p>Die Kosten variieren je nach Bundesland, Friedhof, Wahl von Sarg/Urne und Extras wie Trauerfeier oder Grabstein.',
    '<p>Modell-Basisspannen ohne Grabpflege und vor Regionalfaktor (Herleitung in der <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik</a>) — die Mitte-Spalte ist der grobe Mittelwert. Die Kosten variieren je nach Bundesland, Friedhof, Wahl von Sarg/Urne und Extras wie Trauerfeier oder Grabstein.')

# M4 Keyfacts anonym/guenstigste -> Direktkremation
rep('1.000–2.000', 'rund 1.000–2.200 (Direktkremation)', 1, hard=False)

# FAQ-Antworten (DOM; LD wird unten regeneriert)
rep('Eine einfache Feuerbestattung liegt bei 2.000–4.000 €, eine Erdbestattung mit Grabstein bei 8.000–12.000 €. Die Kosten hängen stark von Region und Bestattungsart ab.',
    'Eine Direktkremation beginnt bei rund 1.000–2.200 €, eine Feuerbestattung mit Urnengrab liegt im Modell bei ca. 3.400–8.200 €, eine Erdbestattung inkl. Grabpflege bei ca. 5.300–14.300 €. Die Kosten hängen stark von Region und Bestattungsart ab.', 2, hard=False)

# M5 Rechner-URLs
rep('href="/tools/kostenrechner/" class="cta-primary"', 'href="/tools/bestattungskosten-rechner/" class="cta-primary"', 2)

# M6 doppelte Verwandte-Themen-Sektion (mr-related-topics) entfernen
m = re.search(r'\s*<section class="mr-related-topics" aria-label="Verwandte Themen">.*?</section>', t, re.S)
assert m, 'related-topics nicht gefunden'
t = t.replace(m.group(0), '', 1)

# M8 Sie-Form-Sektion
rep('<h2>Bestatter in Ihrer Nähe finden</h2>', '<h2>Bestatter in deiner Nähe finden</h2>')
rep('<p>Finden Sie einen passenden Bestatter in Ihrer Stadt – mit lokalen Informationen zu Friedhöfen, Gebühren und Bestattungsrecht.</p>',
    '<p>Finde einen passenden Bestatter in deiner Stadt — mit lokalen Informationen zu Friedhöfen, Gebühren und Bestattungsrecht.</p>')

# M9 Quellenbox
rep('<li>Bundesverband Deutscher Bestatter (BDB): Kostenbenchmark Bestattungen 2024</li>',
    '<li><a href="https://www.bestatter.de/" target="_blank" rel="noopener" style="color:var(--mr-primary)">Bundesverband Deutscher Bestatter (BDB)</a>: Kosteninformationen zu Bestattung und Friedhofsgebühren</li>')
rep('<li>Stiftung Warentest: Bestattungskosten und -vorsorge (2024)</li>',
    '<li><a href="https://www.test.de/thema/sterbefall/" target="_blank" rel="noopener" style="color:var(--mr-primary)">Stiftung Warentest</a>: Bestattungskosten und -vorsorge (zuletzt größere Veröffentlichung 2023)</li>')

# M10 Spartipp + Traeger-Formulierung
rep('<p>Kommunale Friedhöfe sind meistens 20–40 % günstiger als private. Prüfe beide Optionen.</p>',
    '<p>Die Gebühren unterscheiden sich erheblich — zwischen Friedhöfen derselben Stadt und zwischen kommunalen und kirchlichen Trägern. Ein Blick in die Gebührensatzungen lohnt sich.</p>')
rep('Von der Kommune festgelegt, beim Bestatter nicht verhandelbar',
    'Vom Friedhofsträger (Kommune oder Kirchengemeinde) per Gebührenordnung festgelegt, beim Bestatter nicht verhandelbar')

# S1/S2/S5
rep('Hole 3 schriftliche Angebote', 'Hole 2–3 schriftliche Angebote', 1, hard=False)
rep('ans Sozialamt oder die Hilfe zum Lebensunterhalt', 'an das Sozialamt deiner Kommune', 1, hard=False)

# S3 Beispielstufen in eigene Section
rep('''    <h2 style="margin-top:36px">Was kostet es ungefähr? Drei Beispiel-Stufen</h2>''',
    '''  </section>

  <section class="mr-section">
    <h2>Was kostet es ungefähr? Drei Beispiel-Stufen</h2>''')

# ===== FAQ-LD aus DOM regenerieren =====
pairs = re.findall(r'<summary>([^<]+)</summary><div class="faq-answer">(?:<p>)?(.*?)(?:</p>)?</div>', t, re.S)
assert len(pairs) >= 5, 'FAQ-Paare: %d' % len(pairs)
def strip_tags(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()
m = re.search(r'(<script type="application/ld\+json">\s*)(\{.*?\})(\s*</script>)', t, re.S)
g = json.loads(m.group(2))
faq_nodes = [n for n in g['@graph'] if n.get('@type') == 'FAQPage']
assert len(faq_nodes) == 1
faq_nodes[0]['mainEntity'] = [
    {'@type': 'Question', 'name': strip_tags(q),
     'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(a)}} for q, a in pairs]
new_ld = json.dumps(g, ensure_ascii=False, separators=(',', ':'))
t = t[:m.start()] + m.group(1) + new_ld + m.group(3) + t[m.end():]

io.open(P, 'w', encoding='utf-8', newline='').write(t)
print('R3b auf bestattungskosten.html OK (%d FAQ-Paare regeneriert)' % len(pairs))
if warn:
    print('WARN (soft-skips):'); [print('  -', w) for w in warn]

# S7 Methodik-Komponentenliste, S8 AP-Kommentar, M9-Label auf BL-Seite
def patch_file(p, old, new, hard=True):
    tt = io.open(p, encoding='utf-8').read()
    if tt.count(old) != 1:
        if hard: print('FATAL in %s: %r' % (p, old[:60])); sys.exit(1)
        print('  skip %s: %r' % (p, old[:50])); return
    io.open(p, 'w', encoding='utf-8', newline='').write(tt.replace(old, new))
    print('%s OK' % p)

patch_file('methodik.html',
    '(Bestatterleistungen, Sarg/Urne, Friedhofsgebühren, Beisetzung, Trauerfeier, Grabpflege u. a.)',
    '(Bestatterleistungen, Sarg/Urne, Friedhofsgebühren, Beisetzung, Grabpflege; optionale Posten wie Trauerfeier oder Grabstein sind nicht Teil des Standard-Szenarios)')
patch_file('tools/angebotspruefer/index.html',
    'baseRange (z.B. Erd 4500-9500)', 'baseRange (z.B. Erd 3700-9300)', hard=False)
patch_file('bestattungskosten-nach-bundesland.html',
    ': Kostenbenchmark Bestattungen</li>', ': Kosteninformationen zu Bestattung und Friedhofsgebühren</li>', hard=False)
print('FERTIG')
