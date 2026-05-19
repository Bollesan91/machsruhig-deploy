#!/usr/bin/env python3
"""Batch 6 NRW-Trio Sozialbestattung: Mönchengladbach + Mülheim + Oberhausen.
Alle § 8 BestG NRW + § 74 SGB XII + BSG B 8 SO 20/10 R.
"""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

MG_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Mönchengladbach: Kostenübernahme nach § 74 SGB XII</h2>
    <p>Wenn die Bestattungskosten für die Verpflichteten eine unzumutbare Härte darstellen, übernimmt der Sozialhilfeträger die erforderlichen Kosten nach <strong>§ 74 SGB XII</strong>. In Mönchengladbach ist der Fachbereich Soziales und Wohnen (50) der Stadt Mönchengladbach zuständig. Die Leistung ist nachrangig: Vermögen und Ansprüche des Nachlasses (z. B. Sterbegeldversicherung, Witwenrente, Bankguthaben) sowie zumutbares Einkommen der Antragsteller werden zuerst herangezogen.</p>
    <p>Bestattungspflichtig sind in Nordrhein-Westfalen nach <strong>§ 8 BestG NRW</strong> die Angehörigen in gesetzlicher Reihenfolge (Ehegatte/eingetragener Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder). Die Bestattungspflicht besteht unabhängig von Erbschaft oder Unterhaltspflicht und ist nicht mit der Kostentragungspflicht identisch.</p>
    <h3>Zuständige Stelle</h3>
    <p>Stadt Mönchengladbach — Fachbereich Soziales und Wohnen (50), Sachgebiet Bestattungskosten<br>
    Verwaltungsgebäude Fliethstraße, Fliethstraße 86–88, 41061 Mönchengladbach<br>
    Telefon: <a href="tel:+4921612583250">02161 25-8325</a><br>
    E-Mail: <a href="mailto:FB50-Bestattungskosten@moenchengladbach.de">FB50-Bestattungskosten@moenchengladbach.de</a></p>
    <p>Zuständig ist die Gemeinde, die zuletzt Sozialhilfe an den Verstorbenen geleistet hat; andernfalls die Gemeinde am Sterbeort.</p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Übernommen werden die <strong>erforderlichen</strong> Kosten einer einfachen, ortsüblichen und würdigen Bestattung: Sarg bzw. Urne in einfacher Ausführung, Überführung, Einäscherung (bei Feuerbestattung), Grabstelle in einfacher Ausführung (in der Regel Reihengrab), Erstanlage und Trauerfeier in schlichtem Rahmen. Das Bundessozialgericht hat im Urteil <strong>B 8 SO 20/10 R vom 25.08.2011</strong> klargestellt, dass auch eine erste Grabherrichtung sowie ein einfacher Grabstein zu den erforderlichen Kosten zählen können.</p>
    <p><strong>Nicht übernommen</strong> werden: Wahlgrab statt Reihengrab, aufwendige Sarg- oder Urnenausstattung, umfangreicher Blumenschmuck, Trauerdrucksachen über das Notwendige hinaus, Bewirtung der Trauergäste, Zweitschriften von Urkunden in größerer Zahl sowie Grabpflege.</p>
    <h3>Wann der Antrag gestellt werden muss</h3>
    <p>Der Antrag sollte <strong>vor Beauftragung des Bestatters</strong> oder unmittelbar danach gestellt werden — spätestens jedoch, bevor die Bestattung bezahlt wird. Eine Antragstellung nach vollständiger Zahlung ist zwar möglich, erschwert aber die Prüfung der Erforderlichkeit der einzelnen Positionen. Wir empfehlen, sich vor Vertragsunterzeichnung beim Fachbereich Soziales und Wohnen zur voraussichtlichen Bewilligung beraten zu lassen und ein Kostenangebot des Bestatters dem Antrag beizufügen.</p>
  </div>

'''

MUELHEIM_SOZIAL = '''<section class="mr-section" aria-labelledby="sozial-h">
  <h2 id="sozial-h">Sozialbestattung in Mülheim an der Ruhr</h2>
  <p>Reicht der Nachlass nicht aus und können die Bestattungspflichtigen die Kosten nicht aus eigenen Mitteln tragen, übernimmt das Sozialamt nach <strong>§ 74 SGB XII</strong> die erforderlichen Bestattungskosten. Anspruchsgrundlage ist nicht Bedürftigkeit der Antragstellenden allein, sondern die <strong>Unzumutbarkeit</strong> der Kostentragung; das Bundessozialgericht hat in seiner Grundsatzentscheidung <strong>B 8 SO 20/10 R vom 25.08.2011</strong> klargestellt, dass die Zumutbarkeit unter Berücksichtigung der gesamten Vermögens-, Einkommens- und persönlichen Verhältnisse zu prüfen ist — auch eine Erbausschlagung entbindet nicht automatisch von der Kostentragungspflicht. Wer in Mülheim bestattungspflichtig ist, ergibt sich aus <strong>§ 8 BestG NRW</strong>: in dieser Reihenfolge Ehegatte oder eingetragener Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern und volljährige Enkelkinder.</p>
  <h3>Zuständige Stelle</h3>
  <p>Zuständig ist das Sozialamt am Sterbeort (§ 98 Abs. 3 SGB XII), in Mülheim also bei einem hier eingetretenen Todesfall:</p>
  <p><strong>Sozialamt der Stadt Mülheim an der Ruhr</strong><br>
  Ruhrstraße 1 (Gebäude Thyssen-Schachtbau), Zimmer 421<br>
  45468 Mülheim an der Ruhr<br>
  Telefon: <a href="tel:+4920845550610">0208 455-5061</a><br>
  E-Mail: <a href="mailto:sozialamt@muelheim-ruhr.de">sozialamt@muelheim-ruhr.de</a><br>
  Vorsprache nur nach Terminvereinbarung.</p>
  <p>Für Personen, die zu Lebzeiten Hilfe zum Lebensunterhalt nach dem 3. Kapitel SGB XII durch die Stadt Mülheim bezogen haben, ist Mülheim unabhängig vom Sterbeort zuständig.</p>
  <h3>Was übernommen wird — und was nicht</h3>
  <p>Übernahmefähig sind die für eine <strong>würdige, einfache Bestattung</strong> erforderlichen Kosten: einfacher Sarg oder Urne, Überführung, Friedhofsgebühren für ein Reihen- oder Urnenreihengrab nach der Mülheimer Gebührensatzung vom 20. Dezember 2022, einfache Trauerfeier, Sterbeurkunden. Für einen Grabstein sind drei Kostenvoranschläge vorzulegen. <strong>Nicht übernommen</strong> werden Repräsentationskosten wie aufwendige Wahlgräber, Traueranzeigen, Trauerkaffee, Blumenschmuck über das Notwendige hinaus oder gehobene Sargmodelle. Eigenes Einkommen und Vermögen der Bestattungspflichtigen sowie Guthaben auf Konten der verstorbenen Person sind vorrangig einzusetzen.</p>
  <h3>Antragszeitpunkt</h3>
  <p>Der Antrag ist nach gefestigter Rechtsprechung <strong>innerhalb von sechs Wochen ab Kenntnis der Bestattungspflicht</strong> beim Sozialamt zu stellen — spätere Anträge können abgelehnt werden. Praktisch heißt das: <strong>vor</strong> Beauftragung des Bestattungsunternehmens das Sozialamt informieren, damit der Bestatter den Auftrag von Anfang an im Rahmen der übernahmefähigen Kosten kalkulieren kann. Eine Vorabbewilligung ist nicht möglich; das Sozialamt prüft erst nach Vorlage der Rechnungen, der finanziellen Nachweise (Kontoauszüge der letzten drei Monate der verstorbenen Person) und gegebenenfalls der Erbausschlagung.</p>
</section>

'''

OBERHAUSEN_SOZIAL = '''<section class="mr-section" aria-labelledby="sozialbestattung">
  <h2 id="sozialbestattung">Sozialbestattung in Oberhausen: Kostenübernahme nach § 74 SGB XII</h2>
  <p>Reichen Nachlass und eigenes Einkommen der bestattungspflichtigen Angehörigen nicht aus, um die Bestattungskosten zu tragen, übernimmt das Sozialamt der Stadt Oberhausen die <strong>erforderlichen Kosten der Bestattung</strong> nach <strong>§ 74 SGB XII</strong>. Maßgeblich ist die sozialhilferechtliche Zumutbarkeit: Geprüft werden Einkommen und Vermögen der zur Kostentragung verpflichteten Person, der Nachlass der verstorbenen Person und etwaige Leistungen Dritter (Sterbegeldversicherung, Beihilfe, gesetzliche Unfallversicherung). Wer bestattungspflichtig ist, richtet sich in Oberhausen nach <strong>§ 8 BestG NRW</strong> — diese Norm legt die Rangfolge der Pflichtigen fest (Ehegatte/eingetragene Lebenspartner, volljährige Kinder, Eltern, Geschwister, Großeltern, Enkelkinder).</p>
  <h3>Zuständige Stelle in Oberhausen</h3>
  <p>Anträge nach § 74 SGB XII bearbeitet die <strong>Be- und Erstattungsstelle der Stadt Oberhausen</strong> (Fachbereich 3-2-50, Sozialamt) im Sozialrathaus:</p>
  <ul>
    <li>Be- und Erstattungsstelle, Sozialrathaus, Essener Straße 53, 46047 Oberhausen</li>
    <li>E-Mail: <a href="mailto:bestattungskosten@oberhausen.de">bestattungskosten@oberhausen.de</a></li>
    <li>Telefon: <a href="tel:+492088250">0208 825-0</a> (zentrale Vermittlung der Stadt Oberhausen, Terminvereinbarung nach vorheriger telefonischer Absprache)</li>
  </ul>
  <p>Örtlich zuständig ist grundsätzlich das Sozialamt des Sterbeortes. Hat die verstorbene Person bis zum Tod Hilfe zum Lebensunterhalt oder Grundsicherung nach dem SGB XII bezogen, bleibt der bisherige Leistungsträger zuständig. Bezug von Bürgergeld nach dem SGB II begründet diese Ausnahme nicht — dann gilt wieder das Sozialamt des Sterbeortes.</p>
  <h3>Was übernommen wird — und was nicht</h3>
  <p>§ 74 SGB XII deckt nur die <em>erforderlichen</em> Kosten einer ortsüblichen, einfachen Bestattung. Übernommen werden typischerweise: einfacher Sarg bzw. Urne, Überführung im Stadtgebiet, Grabnutzungsgebühr für ein Reihengrab nach Friedhofsgebührensatzung der Stadt Oberhausen, Grabbereitung, Einäscherungsgebühr (bei Feuerbestattung), eine schlichte Trauerfeier sowie eine einfache Grabkennzeichnung. <strong>Nicht übernommen</strong> werden Aufwendungen für Wahlgrabstätten gegenüber Reihengräbern, Trauerredner über das übliche Maß hinaus, Bewirtungskosten, Traueranzeigen, Blumenschmuck über das einfache Maß hinaus und aufwendige Grabsteine. Das Bundessozialgericht hat zur Reichweite des Begriffs „erforderliche Kosten" in der Leitentscheidung <strong>BSG, Urteil vom 25.08.2011, B 8 SO 20/10 R</strong> klargestellt, dass sich die Erforderlichkeit nach den ortsüblichen Mindeststandards einer würdevollen Bestattung bemisst — nicht nach den Wünschen der Angehörigen oder den Standards des Bestatters.</p>
  <h3>Antragszeitpunkt</h3>
  <p>Der Antrag kann <strong>vor oder nach der Bestattung</strong> gestellt werden. Empfehlenswert ist die Kontaktaufnahme vor Auftragserteilung an den Bestatter: So lässt sich vorab klären, welcher Leistungsumfang als „erforderlich" anerkannt wird, und Streit über nachträglich nicht erstattungsfähige Positionen vermeiden. Ein Antrag nach der Bestattung ist zulässig, sollte aber zeitnah erfolgen — der bundesweit anerkannte Richtwert liegt bei rund zwei Monaten nach dem Todestag. Bestattungspflichtige sind nicht verpflichtet, eine Bestattung zu unterlassen, weil die Kostenfrage ungeklärt ist; die ordnungsbehördliche Bestattungspflicht nach § 8 BestG NRW bleibt bestehen.</p>
</section>

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

# Mönchengladbach — anchor before "Wie du einen Bestatter findest" Bestatter-Wahl section
mg_anchor = '  <div class="mr-section">\n    <h2>Wie du einen Bestatter findest</h2>'
do_insert('bestatter/moenchengladbach/index.html', mg_anchor, MG_SOZIAL, 'MOENCHENGLADBACH')

# Mülheim — anchor: before bestatter section
mh_anchor = '<section class="mr-section" aria-labelledby="bestatter-h">'
ok = do_insert('bestatter/muelheim/index.html', mh_anchor, MUELHEIM_SOZIAL, 'MUELHEIM')
if not ok:
    # try alternatives
    with open('bestatter/muelheim/index.html','r',encoding='utf-8') as f: s = f.read()
    alts = [
        '<section class="mr-section" aria-labelledby="bestatter">',
        '<h2 id="bestatter"',
        '<h2>Bestatter-Wahl in Mülheim',
        '<h2>Bestatter in Mülheim',
    ]
    for a in alts:
        if a in s and s.count(a) == 1:
            print(f'  MUELHEIM fallback anchor: {a[:60]}')
            do_insert('bestatter/muelheim/index.html', a, MUELHEIM_SOZIAL, 'MUELHEIM')
            break

# Oberhausen — anchor before Was-tun section
ob_anchor = '<section class="mr-section" aria-labelledby="todesfall">'
ok = do_insert('bestatter/oberhausen/index.html', ob_anchor, OBERHAUSEN_SOZIAL, 'OBERHAUSEN')
if not ok:
    with open('bestatter/oberhausen/index.html','r',encoding='utf-8') as f: s = f.read()
    alts = [
        '<section class="mr-section" id="todesfall">',
        '<h2 id="todesfall"',
        '<h2>Was nach einem Todesfall in Oberhausen',
    ]
    for a in alts:
        if a in s and s.count(a) == 1:
            print(f'  OBERHAUSEN fallback anchor: {a[:60]}')
            do_insert('bestatter/oberhausen/index.html', a, OBERHAUSEN_SOZIAL, 'OBERHAUSEN')
            break

# Update dateModified for all 3
print('\n=== dateModified UPDATE ===')
for city in ['moenchengladbach','muelheim','oberhausen']:
    fp = f'bestatter/{city}/index.html'
    with open(fp,'r',encoding='utf-8') as f: s = f.read()
    orig = s
    s = re.sub(r'"dateModified":\s*"\d{4}-\d{2}-\d{2}"', '"dateModified": "2026-05-19"', s)
    if s != orig:
        with open(fp,'w',encoding='utf-8') as f: f.write(s)
        m = re.search(r'"dateModified":\s*"([^"]+)"', s)
        print(f'{city}: dateModified = {m.group(1)}')

print('\n=== VERIFICATION ===')
for city in ['moenchengladbach', 'muelheim', 'oberhausen']:
    fp = f'bestatter/{city}/index.html'
    with open(fp,'r',encoding='utf-8') as f: s = f.read()
    nul_ok = len(s.rstrip('\x00')) == len(s)
    has_sozial = 'Sozialbestattung in ' in s
    has_sgb = '§ 74 SGB XII' in s
    has_bsg = 'B 8 SO 20/10 R' in s
    has_nrw = '§ 8 BestG NRW' in s
    sec_o = len(re.findall(r'<section\b', s))
    sec_c = len(re.findall(r'</section>', s))
    print(f'{city}: len={len(s)}, NUL={nul_ok}, Sozial={has_sozial}, §74={has_sgb}, BSG={has_bsg}, §8 NRW={has_nrw}, <section>={sec_o}/{sec_c}')
