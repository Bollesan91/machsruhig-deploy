#!/usr/bin/env python3
"""Insert Sozialbestattung in Bonn."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

SOZIAL = '''
  <div class="mr-section">
    <h2>Sozialbestattung in Bonn — wenn die Kosten nicht tragbar sind</h2>
    <p>Wenn die zur Bestattung verpflichteten Angehörigen die Kosten aus persönlichen oder wirtschaftlichen Gründen nicht tragen können, übernimmt das Sozialamt nach <strong>§ 74 SGB XII</strong> die <em>erforderlichen</em> Bestattungskosten. „Erforderlich" meint eine ortsübliche, angemessene Bestattung — typischerweise im einfachen Reihengrab. Der Anspruch besteht unabhängig davon, ob der oder die Verstorbene zu Lebzeiten Sozialleistungen bezogen hat; geprüft werden die Einkommens- und Vermögensverhältnisse <strong>aller</strong> bestattungspflichtigen Personen.</p>
    <h3>Wer ist bestattungspflichtig?</h3>
    <p>Die Bestattungspflicht in Bonn richtet sich nach <strong>§ 8 BestG NRW</strong>: in dieser Reihenfolge Ehegatte oder eingetragene Lebenspartnerin/eingetragener Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder. Die Bestattungspflicht nach § 8 BestG NRW ist <strong>nicht identisch mit der Kostentragungspflicht</strong> nach § 1968 BGB (Erbe); der Bestattungspflichtige muss die Bestattung organisieren, kann aber gleichwohl die Kostenübernahme beantragen, wenn er sie nicht tragen kann (so im Grundsatz <strong>BSG, Urteil vom 25.08.2011, B 8 SO 20/10 R</strong>).</p>
    <h3>Was übernommen wird</h3>
    <p>Das Sozialamt Bonn übernimmt typischerweise: einfache Bestatterleistungen (Sarg oder Urne, Versorgung, Überführung im Stadtgebiet), Friedhofsgebühren nach Bonner Gebührenordnung für ein Reihengrab, Beisetzung, schlichte Trauerfeier in der Friedhofshalle und Sterbeurkunden. <strong>Nicht übernommen</strong> werden in der Regel: Wahlgrab, Grabstein, individueller Grabschmuck, größere Trauerfeier, Trauerdruck über das Nötige hinaus. Vorrangig sind eigenes Vermögen des Verstorbenen, Sterbegeldversicherungen und der Nachlass einzusetzen.</p>
    <h3>Wo und wann beantragen</h3>
    <p>Zuständig ist das <strong>Amt für Soziales und Wohnen der Bundesstadt Bonn — Bestattungskosten</strong>, Hans-Böckler-Straße 5, 53225 Bonn (Postanschrift: 53103 Bonn). Telefonisch erreichbar über Herrn Labs unter <a href="tel:+49228775853">0228 775853</a>, per E-Mail an <a href="mailto:wirtschaftlichehilfen@bonn.de">wirtschaftlichehilfen@bonn.de</a>. Beratungen erfolgen nur nach Terminvereinbarung.</p>
    <p><strong>Antragszeitpunkt:</strong> Der Antrag sollte <strong>vor Auftragserteilung an den Bestatter</strong> gestellt werden — spätestens jedoch zeitnah nach dem Todesfall, da die Bestattungsfrist nach § 13 BestG NRW läuft. Eine spätere Antragstellung ist möglich (der Anspruch verjährt nicht sofort), erschwert aber die Prüfung der Angemessenheit. Beizufügen sind: Sterbeurkunde, Bestatter-Kostenvoranschlag bzw. Rechnung, Bescheid über die Friedhofsgebühren, Einkommens- und Vermögensnachweise des Antragstellers (Kontoauszüge, Mietvertrag, Versicherungspolicen) sowie Nachweise zur finanziellen Lage des Verstorbenen.</p>
    <div class="mr-hint">
      <strong>Wichtig:</strong> Die <em>Sozialbestattung</em> nach § 74 SGB XII ist nicht zu verwechseln mit der <em>ordnungsbehördlichen Bestattung</em>: Letztere greift nur, wenn keine bestattungspflichtigen Angehörigen vorhanden sind oder diese ihrer Pflicht nicht nachkommen — das Ordnungsamt veranlasst dann die Bestattung und fordert die Kosten anschließend ein.
    </div>
  </div>

'''

fp = 'bestatter/bonn/index.html'
with open(fp, 'r', encoding='utf-8') as f: s = f.read()
orig = s
anchor = '  <div class="mr-section">\n    <h2>Was nach einem Todesfall in Bonn zu tun ist</h2>'
replace = SOZIAL + anchor
n = s.count(anchor)
print(f'Bonn anchor: {n}')
if n == 1:
    s = s.replace(anchor, replace)
    with open(fp, 'w', encoding='utf-8') as f: f.write(s)
    print(f'WROTE Bonn: {len(orig)} -> {len(s)}')

print(f'  Sozial-Section: {"<h2>Sozialbestattung in Bonn" in s}')
print(f'  § 8 BestG NRW: {"§ 8 BestG NRW" in s}')
print(f'  Hans-Böckler-Str: {"Hans-Böckler-Straße 5" in s}')
print(f'  BSG B 8 SO 20/10 R: {"B 8 SO 20/10 R" in s}')
