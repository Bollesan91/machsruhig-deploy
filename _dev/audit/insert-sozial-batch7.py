#!/usr/bin/env python3
"""Batch 7 NRW-Trio Sozialbestattung: Hagen + Leverkusen + Wuppertal."""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

HAGEN_SOZIAL = '''<section class="mr-section" id="sozialbestattung">
    <h2>Sozialbestattung in Hagen: wenn die Kosten nicht getragen werden können</h2>
    <p>Sind die Bestattungspflichtigen finanziell nicht in der Lage, eine Bestattung zu finanzieren, übernimmt das Sozialamt die erforderlichen Kosten — geregelt in <a href="https://www.gesetze-im-internet.de/sgb_12/__74.html" rel="noopener" target="_blank">§ 74 SGB XII</a>. Voraussetzung ist, dass der nach <strong>§ 8 Abs. 1 BestG NRW</strong> Bestattungspflichtige die Kosten nicht aus eigenen Mitteln und nicht aus dem Nachlass des Verstorbenen aufbringen kann und ihm die Übernahme nicht zuzumuten ist. Geprüft wird die individuelle Zumutbarkeit — nicht die schematische Bedürftigkeit; auch Personen ohne laufenden Sozialhilfebezug haben Anspruch, wenn die Bestattungskosten ihre wirtschaftliche Leistungsfähigkeit übersteigen würden.</p>
    <h3>Zuständige Stelle in Hagen</h3>
    <p>Anträge auf Übernahme der Bestattungskosten nimmt der <strong>Fachbereich Jugend und Soziales der Stadt Hagen</strong> entgegen:</p>
    <p>Fachbereich Jugend und Soziales, Berliner Platz 22, 58089 Hagen<br>
    Telefon: <a href="tel:+4923312073163">02331/207-3163</a><br>
    E-Mail: <a href="mailto:jugendsoziales@stadt-hagen.de">jugendsoziales@stadt-hagen.de</a></p>
    <p>Telefonische Erreichbarkeit der Sachbearbeitung ist nach Angaben der Stadt Hagen werktags zwischen 8:30 und 9:30 Uhr.</p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Übernommen werden nach § 74 SGB XII die <strong>erforderlichen</strong> Kosten einer ortsüblichen Bestattung in einfacher, würdiger Form. Das umfasst in der Praxis: Sarg oder Urne in einfacher Ausführung, Überführung, eine schlichte Trauerfeier, Friedhofsgebühren des Wirtschaftsbetriebs Hagen für ein Reihengrab sowie die Erstanlage des Grabes. Das Bundessozialgericht hat in seiner Rechtsprechung (u.a. <strong>BSG, Urteil vom 25.08.2011, B 8 SO 20/10 R</strong>) klargestellt, dass sich der Erforderlichkeitsmaßstab an ortsüblichen Mindeststandards orientiert — also am bescheidenen, aber nicht entwürdigenden Niveau vor Ort. <strong>Nicht übernommen</strong> werden in der Regel: Trauerredner über das einfache Maß hinaus, aufwendige Blumendekoration, Trauerkaffee, Zeitungsanzeigen, Wahlgrabaufschläge gegenüber dem Reihengrab und die laufende Grabpflege nach der Erstanlage.</p>
    <h3>Antragszeitpunkt: möglichst vor Auftragserteilung</h3>
    <p>Der Antrag sollte nach Möglichkeit <strong>vor</strong> Auftragserteilung an den Bestatter gestellt werden — spätestens jedoch unverzüglich nach dem Todesfall. Eine spätere Antragstellung ist nicht ausgeschlossen, aber das Sozialamt prüft dann besonders sorgfältig, ob die in Auftrag gegebenen Leistungen das ortsüblich Erforderliche überschritten haben; übersteigende Beträge gehen zu Lasten des Antragstellers. Sinnvoll ist, bereits beim Erstgespräch mit dem Bestatter offen zu kommunizieren, dass eine Kostenübernahme nach § 74 SGB XII beantragt werden soll — viele Hagener Bestattungsunternehmen kennen das Verfahren und erstellen entsprechend angepasste Kostenvoranschläge.</p>
  </section>

'''

LEVERKUSEN_SOZIAL = '''<section class="mr-section" aria-labelledby="sozial-heading">
  <h2 id="sozial-heading">Sozialbestattung in Leverkusen — wenn die Kosten nicht tragbar sind</h2>
  <p>Bei Friedhofsgebühren, die in Leverkusen zu den höchsten in Nordrhein-Westfalen zählen, geraten kostentragungspflichtige Angehörige regelmäßig in finanzielle Überforderung. Für diese Fälle sieht <strong>§ 74 SGB XII</strong> die Übernahme der erforderlichen Bestattungskosten durch das Sozialamt vor — soweit den Verpflichteten nicht zugemutet werden kann, die Kosten selbst zu tragen. Maßgeblich ist nicht die Bedürftigkeit der oder des Verstorbenen, sondern die wirtschaftliche Lage der Person, die nach <strong>§ 8 BestG NRW</strong> zur Bestattung verpflichtet ist (Ehegatten, eingetragene Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder — in dieser Reihenfolge). Auch wer selbst keine Sozialhilfe bezieht, kann antragsberechtigt sein, wenn das eigene Einkommen und Vermögen die Kostentragung nicht zulässt.</p>
  <h3>Zuständige Stelle in Leverkusen</h3>
  <p>Anlaufstelle ist der <strong>Fachbereich Soziales der Stadt Leverkusen, Abteilung 502 — Soziale Leistungen</strong>, seit dem 8. Januar 2026 im neuen Zentralstandort:</p>
  <p>Hauptstraße 119, 51373 Leverkusen-Wiesdorf<br>
  Telefon: <a href="tel:+4921440650203">0214 406-50203</a> (Soziale Leistungen I)<br>
  E-Mail: <a href="mailto:502-soziale-leistungen@stadt.leverkusen.de">502-soziale-leistungen@stadt.leverkusen.de</a></p>
  <p>Zuständig ist das Sozialamt, das der verstorbenen Person bis zum Tod Sozialhilfe gewährt hat; lag keine Sozialhilfe vor, ist das Sozialamt des Sterbeorts zuständig.</p>
  <h3>Was übernommen wird — und was nicht</h3>
  <p>Übernommen werden ausschließlich die <strong>erforderlichen Kosten einer einfachen und würdigen Bestattung</strong>: Sarg oder Urne in einfacher Ausführung, Überführung im Stadtgebiet, einfache Sargausstattung, Grabgebühr für ein Reihengrab nach städtischer Gebührensatzung, einfache Grabherstellung, Trauerredner oder einfache kirchliche Trauerfeier sowie eine Sterbeurkunde. Das Bundessozialgericht hat in seinem Urteil <strong>B 8 SO 20/10 R vom 25.08.2011</strong> klargestellt, dass sich der Maßstab des „Erforderlichen" an den am Bestattungsort ortsüblichen Mindeststandards für eine würdige Bestattung orientiert. <strong>Nicht übernommen</strong> werden in der Regel Wahlgrab- statt Reihengrabgebühren, Grabstein und Grabeinfassung, Trauerkaffee, Traueranzeigen, Blumenschmuck über das einfache Maß hinaus sowie Kosten der Grabpflege.</p>
  <h3>Antragszeitpunkt</h3>
  <p>Der Antrag sollte <strong>vor</strong> der Bestattung gestellt werden, ist nach der Bestattung aber innerhalb angemessener Frist (in der Verwaltungspraxis bis zu zwei Monate nach dem Todestag) ebenfalls möglich. Empfohlen wird, dem Bestattungsunternehmen die Antragstellung mitzuteilen — viele Leverkusener Bestatter rechnen bei vorliegender Kostenübernahmeerklärung direkt mit dem Sozialamt ab. Erforderlich sind unter anderem Sterbeurkunde, Kostenvoranschlag des Bestatters, Nachweise zu Einkommen und Vermögen der antragstellenden Person sowie Angaben zum Nachlass.</p>
</section>

'''

# Wuppertal: tel-Link FIX +492025632015 (12 digits, was +4920256320150 with extra 0)
WUPPERTAL_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Wuppertal — wenn die Kosten nicht getragen werden können</h2>
    <p>Können bestattungspflichtige Angehörige die Kosten der Bestattung nicht aus eigenem Einkommen oder Vermögen aufbringen und ist der Nachlass des Verstorbenen aufgezehrt, besteht nach <strong>§ 74 SGB XII</strong> ein Anspruch auf Übernahme der erforderlichen Kosten durch den Sozialhilfeträger. Die Bestattungspflicht selbst ergibt sich in NRW aus <strong>§ 8 BestG NRW</strong>, der die Reihenfolge der bestattungspflichtigen Angehörigen (Ehegatte, eingetragener Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkel) festlegt. Bestattungspflicht und Kostentragungspflicht sind dabei rechtlich zu trennen — wer bestattungspflichtig ist, kann unabhängig davon einen Antrag auf Kostenübernahme stellen, wenn die Mittel fehlen.</p>
    <h3>Zuständige Stelle in Wuppertal</h3>
    <p>Zuständig für die Übernahme der Bestattungskosten nach § 74 SGB XII ist das <strong>Sozialamt der Stadt Wuppertal (Ressort 201 Soziales)</strong>:</p>
    <p>Verwaltungshaus Elberfeld, Neumarkt 10, 42103 Wuppertal<br>
    Telefon: <a href="tel:+492025632015">0202 563-2015</a><br>
    E-Mail: <a href="mailto:sozialamt@stadt.wuppertal.de">sozialamt@stadt.wuppertal.de</a></p>
    <p>Bezog die verstorbene Person zum Todeszeitpunkt bereits Sozialhilfeleistungen, ist die Dienststelle zuständig, die zuletzt Hilfe gewährt hat; in allen anderen Fällen das Sozialamt des Sterbeortes.</p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Übernommen werden die erforderlichen Kosten für eine <em>einfache, aber würdige, den ortsüblichen Verhältnissen entsprechende Bestattung</em>. Erstattungsfähig sind nur Aufwendungen, die unmittelbar der Bestattung selbst dienen — Sarg oder Urne in einfacher Ausführung, Überführung im Stadtgebiet, Grabnutzungsrecht für ein Reihengrab über die Ruhezeit, Beisetzungsgebühr, eine schlichte Trauerfeier am Grab. <strong>Nicht übernommen</strong> werden in aller Regel Grabstein und Einfassung, dauerhafte Grabpflege, Trauerdruck, Blumenschmuck über das übliche Maß hinaus, Trauerkaffee oder eine Erweiterung zum Wahlgrab. Das Sozialamt prüft vorrangig, ob der Nachlass die Kosten deckt; nur der ungedeckte Restbetrag wird übernommen. Die Bundessozialgerichts-Entscheidung <strong>B 8 SO 20/10 R vom 25.08.2011</strong> hat die Maßstäbe für Angemessenheit und Erforderlichkeit der erstattungsfähigen Kosten näher konkretisiert; im Einzelfall ist die jeweils aktuelle Verwaltungspraxis des zuständigen Trägers maßgeblich.</p>
    <h3>Antragszeitpunkt</h3>
    <p>Der Antrag auf Übernahme der Bestattungskosten ist <strong>möglichst vor Auftragserteilung an den Bestatter</strong> beim Sozialamt zu stellen — spätestens jedoch unverzüglich nach Bekanntwerden der Bestattungspflicht. Eine rückwirkende Übernahme bereits beglichener Rechnungen ist zwar nicht ausgeschlossen, in der Praxis aber an zusätzliche Nachweispflichten gebunden. Empfehlenswert ist, das ausgewählte Bestattungsunternehmen vorab über den geplanten Antrag zu informieren; die in Wuppertal ansässigen Bestatter kennen die geltenden Angemessenheitsgrenzen und können das Angebot entsprechend zuschneiden.</p>
  </div>

'''

def do_insert(fp, anchor, html, label):
    with open(fp,'r',encoding='utf-8') as f: s = f.read()
    n = s.count(anchor)
    print(f'{label}: anchor matches = {n}')
    if n == 1:
        s_new = s.replace(anchor, html + anchor)
        with open(fp,'w',encoding='utf-8') as f: f.write(s_new)
        print(f'  WROTE {label}: {len(s)} -> {len(s_new)}')
        return True
    return False

# Hagen — anchor before todesfall section
hagen_anchor = '<section class="mr-section" id="todesfall">'
ok = do_insert('bestatter/hagen/index.html', hagen_anchor, HAGEN_SOZIAL, 'HAGEN')
if not ok:
    with open('bestatter/hagen/index.html','r',encoding='utf-8') as f: s = f.read()
    for a in ['<h2 id="todesfall"', '<h2>Was nach einem Todesfall in Hagen']:
        if a in s and s.count(a) == 1:
            do_insert('bestatter/hagen/index.html', a, HAGEN_SOZIAL, 'HAGEN (fallback)')
            break

# Leverkusen — anchor before todesfall-heading section
lev_anchor = '<section class="mr-section" aria-labelledby="todesfall-heading">'
ok = do_insert('bestatter/leverkusen/index.html', lev_anchor, LEVERKUSEN_SOZIAL, 'LEVERKUSEN')
if not ok:
    with open('bestatter/leverkusen/index.html','r',encoding='utf-8') as f: s = f.read()
    for a in ['<h2 id="todesfall-heading"', '<h2>Was nach einem Todesfall in Leverkusen']:
        if a in s and s.count(a) == 1:
            do_insert('bestatter/leverkusen/index.html', a, LEVERKUSEN_SOZIAL, 'LEVERKUSEN (fallback)')
            break

# Wuppertal — anchor before Was-tun section (uses <div class="mr-section">)
wup_anchor = '  <div class="mr-section">\n    <h2>Was nach einem Todesfall in Wuppertal zu tun ist</h2>'
do_insert('bestatter/wuppertal/index.html', wup_anchor, WUPPERTAL_SOZIAL, 'WUPPERTAL')

# dateModified update
print('\n=== dateModified UPDATE ===')
for city in ['hagen','leverkusen','wuppertal']:
    fp = f'bestatter/{city}/index.html'
    with open(fp,'r',encoding='utf-8') as f: s = f.read()
    orig = s
    s = re.sub(r'"dateModified":\s*"\d{4}-\d{2}-\d{2}"', '"dateModified": "2026-05-19"', s)
    if s != orig:
        with open(fp,'w',encoding='utf-8') as f: f.write(s)
        m = re.search(r'"dateModified":\s*"([^"]+)"', s)
        print(f'{city}: dateModified = {m.group(1)}')

print('\n=== VERIFICATION ===')
for city in ['hagen', 'leverkusen', 'wuppertal']:
    fp = f'bestatter/{city}/index.html'
    with open(fp,'r',encoding='utf-8') as f: s = f.read()
    nul_ok = len(s.rstrip('\x00')) == len(s)
    has_sozial = 'Sozialbestattung in ' in s
    has_sgb = '§ 74 SGB XII' in s
    has_bsg = 'B 8 SO 20/10 R' in s
    has_nrw = '§ 8 BestG NRW' in s
    sec_o = len(re.findall(r'<section\b', s))
    sec_c = len(re.findall(r'</section>', s))
    # tel-link length check
    tel_bad = False
    for m in re.finditer(r'tel:\+(\d+)', s):
        d = m.group(1)
        if len(d) > 13:
            tel_bad = True
            print(f'  ⚠️ {city}: tel:+{d} ({len(d)} digits)')
    print(f'{city}: len={len(s)}, NUL={nul_ok}, Sozial={has_sozial}, §74={has_sgb}, BSG={has_bsg}, §8 NRW={has_nrw}, <section>={sec_o}/{sec_c}, tel-bad={tel_bad}')
