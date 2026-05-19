#!/usr/bin/env python3
"""Batch 9 Multi-BL Sozialbestattung: Nürnberg (BY) + Bremen (HB) + Potsdam (BB)."""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

NUERNBERG_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Nürnberg — wenn die Kosten nicht getragen werden können</h2>
    <p>Können die Bestattungspflichtigen die Kosten einer ortsüblichen, einfachen Bestattung aus eigenen Mitteln und aus dem Nachlass nicht tragen, besteht nach <a href="https://www.gesetze-im-internet.de/sgb_12/__74.html" rel="noopener" target="_blank">§ 74 SGB XII</a> ein Anspruch auf Übernahme der erforderlichen Bestattungskosten durch den Sozialhilfeträger. Anspruchsberechtigt ist, wer zur Kostentragung verpflichtet ist — in Bayern bestimmt sich der Kreis nach <strong>§ 15 BestV</strong> in Verbindung mit <strong>§ 1 Abs. 1 Satz 2 Nr. 1 BestV</strong>, der die Reihenfolge der Bestattungspflichtigen festlegt (Ehegatte oder Lebenspartner, Kinder, Eltern, Großeltern, Enkelkinder, Geschwister, Kinder der Geschwister, Verschwägerte ersten Grades). Die Bestattungspflicht ist von der Erbenstellung unabhängig — auch wer das Erbe ausschlägt, kann bestattungspflichtig und damit antragsberechtigt bleiben.</p>
    <h3>„Erforderliche Kosten" — was übernommen wird</h3>
    <p>Übernommen werden nur die Kosten einer einfachen, ortsüblichen Bestattung. Das Bundessozialgericht hat mit Urteil vom <strong>25. August 2011 (Az. B 8 SO 20/10 R)</strong> den Begriff der „erforderlichen Kosten" konkretisiert und einen würdigen, aber schlichten Bestattungsstandard als Maßstab herausgearbeitet. Aufwändige Sarg- oder Grabsteinausführungen, eine umfangreiche Trauerfeier oder eine Bestattung auf einem besonders kostspieligen Wahlgrab werden in der Regel nicht abgedeckt; entscheidend ist der ortsübliche Standard, gemessen an den Gebührensätzen der städtischen Friedhöfe und marktüblichen Bestatterpreisen.</p>
    <h3>Antrag in Nürnberg — Zuständigkeit und Kontakt</h3>
    <p>Zuständig ist das <strong>Sozialamt der Stadt Nürnberg</strong> (Amt für Existenzsicherung und soziale Integration im Sozialreferat). Der Antrag sollte möglichst <strong>vor</strong> Beauftragung des Bestatters gestellt werden — zumindest aber unverzüglich nach dem Todesfall. Vorzulegen sind in der Regel: Sterbeurkunde, Kostenvoranschlag des Bestatters, Nachweise zu Einkommen und Vermögen der Bestattungspflichtigen, Nachlassaufstellung sowie ggf. Erbausschlagungsnachweis. Eine rückwirkende Antragstellung nach bereits durchgeführter Bestattung ist möglich, sollte aber nicht ohne Not gewählt werden.</p>
    <p><strong>Sozialamt Nürnberg — Amt für Existenzsicherung und soziale Integration</strong><br>
    Dietzstraße 4, 90443 Nürnberg<br>
    Telefon: <a href="tel:+499112315">0911 231-5</a> (Servicetelefon der Stadt Nürnberg)<br>
    E-Mail: <a href="mailto:sozialamt@stadt.nuernberg.de">sozialamt@stadt.nuernberg.de</a></p>
    <p><strong>Praxistipp:</strong> Bestatter in Nürnberg kennen das Verfahren und stellen häufig einen reduzierten „Sozialbestattungs-Kostenvoranschlag" aus, der sich am Erstattungsrahmen orientiert. Bei der Bestatterauswahl gezielt nach dieser Praxis fragen — das vereinfacht den Antrag und vermeidet Lücken zwischen Bestatterrechnung und Sozialamtsleistung.</p>
  </div>

'''

BREMEN_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Bremen — wenn die Kosten nicht tragbar sind</h2>
    <p>Wenn die zur Tragung der Bestattungskosten verpflichtete Person diese nicht oder nicht in voller Höhe aufbringen kann, übernimmt der Sozialhilfeträger nach <strong>§ 74 SGB XII</strong> die erforderlichen Kosten einer einfachen, würdevollen Bestattung. Maßstab ist die Zumutbarkeit: Geprüft werden Nachlass, Sterbegeldversicherungen, Bestattungsvorsorgeverträge sowie Einkommens- und Vermögensverhältnisse der pflichtigen Person. Erstattet werden Bestatter-Grundleistungen (Sarg/Urne, Überführung, einfacher Trauerfeier-Rahmen) und Friedhofsgebühren; nicht erstattet werden Bewirtung, aufwendiger Trauerdruck oder gehobene Sarg-/Grabausstattung.</p>
    <h3>Bestattungspflicht in Bremen — die Bremer Besonderheit</h3>
    <p>Anders als in den meisten Bundesländern regelt nicht das Bremische Friedhofs- und Bestattungsgesetz die Bestattungspflicht, sondern das <strong>Gesetz über das Leichenwesen</strong>. Nach <strong>§ 4 Abs. 1 Satz 1 Nr. 1</strong> dieses Gesetzes sind alle durch Eheschließung, eingetragene Lebenspartnerschaft, Abstammung, Schwägerschaft oder Lebensgemeinschaft verbundenen Angehörigen pflichtig — und zwar <strong>gleichrangig</strong>, ohne abgestufte Reihenfolge. Bremen ist damit bundesweit ein Sonderfall: Es kennt keine Rangfolge Ehegatte → Kinder → Eltern wie etwa Niedersachsen oder NRW. <strong>Großeltern und Enkelkinder sind in Bremen nicht bestattungspflichtig.</strong> Veranlassen die Angehörigen nicht innerhalb von zehn Tagen eine Bestattung, ordnet das Institut für Rechtsmedizin nach § 17 Abs. 2 Satz 2 des Gesetzes über das Leichenwesen eine Bestattung von Amts wegen an; die Kosten werden den Pflichtigen anschließend in Rechnung gestellt.</p>
    <h3>Zuständig: Amt für Soziale Dienste Bremen</h3>
    <p>Der Antrag auf Übernahme nach § 74 SGB XII ist an das <strong>Amt für Soziale Dienste der Stadtgemeinde Bremen</strong> zu richten — konkret an das Sozialzentrum, in dessen Bereich die verstorbene Person zuletzt gewohnt hat oder verstorben ist. Hatte sie zuletzt Sozialhilfe bezogen, ist der bisher leistende Träger zuständig. Eine starre Frist besteht nicht; ein Antrag kann auch nach erfolgter Bestattung gestellt werden, sollte aber im zeitlichen Zusammenhang erfolgen.</p>
    <p><strong>Amt für Soziale Dienste Bremen</strong><br>
    Bahnhofsplatz 29, 28195 Bremen<br>
    Telefon: <a href="tel:+494213619730">0421 361-9730</a> (Zentrale Wirtschaftliche Hilfen)<br>
    E-Mail: <a href="mailto:office@afsd.bremen.de">office@afsd.bremen.de</a></p>
    <p><strong>Höchstrichterlich geklärt:</strong> Nach Urteil des Bundessozialgerichts vom <strong>25.08.2011 (B 8 SO 20/10 R)</strong> umfasst der Anspruch nach § 74 SGB XII ausschließlich die <strong>erforderlichen</strong> Kosten einer einfachen, würdevollen Bestattung; Aufwendungen für gehobene Ausstattung oder Bewirtung der Trauergäste werden nicht erstattet. Das Erbe ist vorrangig einzusetzen.</p>
  </div>

'''

POTSDAM_SOZIAL = '''<section class="mr-section" id="sozialbestattung">
    <h2>Sozialbestattung in Potsdam: Was tun, wenn das Geld fehlt?</h2>
    <p>Reichen Nachlass und eigene Mittel der bestattungspflichtigen Person nicht aus, übernimmt das Sozialamt nach <strong>§ 74 SGB XII</strong> die <em>erforderlichen</em> Kosten einer einfachen, würdigen Bestattung. Erfasst sind in der Regel Sarg oder Urne, Überführung, Friedhofsgebühren für ein Reihengrab, einfache Trauerfeier und Trauerredner. Nicht erfasst sind Grabstein, Trauerkaffee oder repräsentative Ausstattung. Der Antrag muss <strong>vor</strong> Beauftragung des Bestatters gestellt werden, spätestens jedoch zeitnah — wer erst nach erfolgter Bestattung Rechnungen einreicht, riskiert eine Ablehnung wegen fehlender Mitwirkung.</p>
    <h3>Wer ist in Potsdam zuständig?</h3>
    <p>Zuständig ist die <strong>Landeshauptstadt Potsdam, Fachbereich Soziales und Inklusion</strong>, Arbeitsgruppe 3843 Hilfe zur Pflege und Bestattungskostenübernahme:</p>
    <p>Postanschrift: Friedrich-Ebert-Straße 79/81, 14469 Potsdam<br>
    Besucheradresse: Behlertstraße 3a, Haus M/N, 14467 Potsdam<br>
    Sozialberatung: <a href="tel:+493312892211">0331 289-2211</a><br>
    E-Mail: <a href="mailto:hilfezurpflege@rathaus.potsdam.de">hilfezurpflege@rathaus.potsdam.de</a></p>
    <p>Die örtliche Zuständigkeit richtet sich nach dem Sterbeort, nicht dem Bestattungsort; hat die verstorbene Person zuletzt Sozialhilfe nach SGB XII bezogen, bleibt der bisherige Träger zuständig.</p>
    <h3>Wer muss den Antrag stellen?</h3>
    <p>Antragsberechtigt sind ausschließlich die nach <strong>§ 20 Brandenburgisches Bestattungsgesetz (BbgBestG)</strong> bestattungspflichtigen Angehörigen in der dort vorgegebenen Reihenfolge — zuerst Ehe- oder eingetragene Lebenspartner, dann Kinder, Eltern, Geschwister, Enkelkinder, Großeltern, schließlich Personen aus einer dauerhaften nichtehelichen Lebensgemeinschaft. Bei mehreren Pflichtigen gleicher Stufe geht die ältere der jüngeren vor. Das Bundessozialgericht hat in seinem Urteil vom <strong>25.08.2011 (Az. B 8 SO 20/10 R)</strong> entschieden, dass die Zumutbarkeit der Kostentragung anhand der wirtschaftlichen Leistungsfähigkeit jedes einzelnen Pflichtigen zu prüfen ist — auch ein zerrüttetes oder gar nicht bestehendes persönliches Verhältnis zur verstorbenen Person kann im Einzelfall zur Unzumutbarkeit führen.</p>
    <p>Mitzubringen oder einzureichen sind der Antrag auf Bestattungskostenübernahme nach § 74 SGB XII, Sterbeurkunde, Kostenvoranschlag des Bestatters, Nachweise zu Einkommen und Vermögen aller Pflichtigen sowie Belege zum Nachlass (Konten, Versicherungen, Sterbegeld).</p>
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

# Nürnberg
nuernberg_anchor = '  <div class="mr-section">\n    <h2>Was nach einem Todesfall in Nürnberg zu tun ist</h2>'
do_insert('bestatter/nuernberg/index.html', nuernberg_anchor, NUERNBERG_SOZIAL, 'NUERNBERG')

# Bremen
bremen_anchor = '  <div class="mr-section">\n    <h2>Bestatter-Wahl in Bremen</h2>'
ok = do_insert('bestatter/bremen/index.html', bremen_anchor, BREMEN_SOZIAL, 'BREMEN')
if not ok:
    with open('bestatter/bremen/index.html','r',encoding='utf-8') as f: s = f.read()
    for a in ['<h2>Bestatter-Wahl in Bremen', '<h2>Bestatter in Bremen']:
        if a in s and s.count(a) == 1:
            do_insert('bestatter/bremen/index.html', a, BREMEN_SOZIAL, 'BREMEN (fallback)')
            break

# Potsdam — anchor before #ablauf section
potsdam_anchor = '<section class="mr-section" id="ablauf">'
ok = do_insert('bestatter/potsdam/index.html', potsdam_anchor, POTSDAM_SOZIAL, 'POTSDAM')
if not ok:
    with open('bestatter/potsdam/index.html','r',encoding='utf-8') as f: s = f.read()
    for a in ['<h2 id="ablauf"', '<h2>Was nach einem Todesfall in Potsdam']:
        if a in s and s.count(a) == 1:
            do_insert('bestatter/potsdam/index.html', a, POTSDAM_SOZIAL, 'POTSDAM (fallback)')
            break

# dateModified
print('\n=== dateModified UPDATE ===')
for city in ['nuernberg','bremen','potsdam']:
    fp = f'bestatter/{city}/index.html'
    with open(fp,'r',encoding='utf-8') as f: s = f.read()
    orig = s
    s = re.sub(r'"dateModified":\s*"\d{4}-\d{2}-\d{2}"', '"dateModified": "2026-05-19"', s)
    if s != orig:
        with open(fp,'w',encoding='utf-8') as f: f.write(s)

print('\n=== VERIFICATION ===')
for city in ['nuernberg', 'bremen', 'potsdam']:
    fp = f'bestatter/{city}/index.html'
    with open(fp,'r',encoding='utf-8') as f: s = f.read()
    has_sozial = 'Sozialbestattung in ' in s
    has_sgb = '§ 74 SGB XII' in s
    has_bsg = 'B 8 SO 20/10 R' in s
    sec_o = len(re.findall(r'<section\b', s))
    sec_c = len(re.findall(r'</section>', s))
    print(f'{city}: Sozial={has_sozial}, §74={has_sgb}, BSG={has_bsg}, <section>={sec_o}/{sec_c}')
