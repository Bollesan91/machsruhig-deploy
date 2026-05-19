#!/usr/bin/env python3
"""Batch 8 Ost-Trio Sozialbestattung: Leipzig (SN) + Chemnitz (SN) + Magdeburg (ST)."""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

LEIPZIG_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Leipzig — wenn die Kosten nicht tragbar sind</h2>
    <p>Reichen Nachlass und eigene Mittel der Bestattungspflichtigen nicht aus, kann das Sozialamt die <strong>erforderlichen Kosten der Bestattung</strong> nach <a href="https://www.gesetze-im-internet.de/sgb_12/__74.html" rel="noopener" target="_blank">§ 74 SGB XII</a> übernehmen. Voraussetzung ist, dass den Verpflichteten die Tragung der Kosten <strong>nicht zugemutet werden kann</strong>. Wer zur Bestattung verpflichtet ist, ergibt sich in Sachsen aus <strong>§ 10 Abs. 3 SächsBestG</strong>: in der dort genannten Rangfolge zunächst Ehegatten oder Lebenspartner, dann volljährige Kinder, Eltern, Großeltern, volljährige Geschwister, Enkelkinder und schließlich sonstige Sorgeberechtigte. Die Bestattungspflicht ist von der Kostentragungspflicht zu unterscheiden — sie kann auch dann bestehen, wenn § 74 SGB XII greift.</p>
    <h3>Zuständige Stelle: Sozialamt der Stadt Leipzig</h3>
    <p>Anträge auf Übernahme der Bestattungskosten richten Angehörige an das <strong>Sozialamt der Stadt Leipzig</strong>:</p>
    <p>Prager Straße 21, 04103 Leipzig<br>
    Telefon: <a href="tel:+493411234400">0341 123-4400</a><br>
    E-Mail: <a href="mailto:sozialamt@leipzig.de">sozialamt@leipzig.de</a></p>
    <p>Zuständig ist grundsätzlich das Sozialamt am letzten gewöhnlichen Aufenthaltsort des Verstorbenen; bei Versterben in Leipzig ist dies in aller Regel das Leipziger Sozialamt.</p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Übernommen werden nur die <strong>erforderlichen Kosten einer ortsüblichen, einfachen, aber würdigen Bestattung</strong>. Dazu zählen in der Regel ein einfacher Sarg oder eine schlichte Urne, hygienische Versorgung, Überführung im Stadtgebiet, Beisetzung in einem Reihen- oder Urnenreihengrab, Trauerhalle und Sterbeurkunden. <strong>Nicht übernommen</strong> werden in der Regel Wahlgrabstätten, Grabsteine und Grabeinfassungen, aufwendige Trauerfeiern, Blumenschmuck, Trauerdruck und Bewirtungen. Vor der Übernahme rechnet das Sozialamt vorhandenes <strong>Nachlassvermögen</strong>, Sterbegeldversicherungen und Leistungen Dritter gegen. Das <strong>Bundessozialgericht</strong> hat mit Urteil vom <strong>25. August 2011 (B 8 SO 20/10 R)</strong> die Maßstäbe für „erforderliche" Kosten näher konkretisiert.</p>
    <h3>Antragszeitpunkt — möglichst früh, spätestens parallel zur Beauftragung</h3>
    <p>Der Antrag sollte <strong>möglichst vor der Beauftragung des Bestatters</strong> gestellt werden, spätestens aber zeitnah danach. Es gibt keine starre Antragsfrist, das Sozialamt prüft jedoch streng, ob die in Rechnung gestellten Positionen tatsächlich erforderlich und ortsüblich waren. Wer ohne Abstimmung eine aufwendigere Bestattung beauftragt, riskiert, auf den Mehrkosten sitzen zu bleiben. Bei der ersten Kontaktaufnahme mit dem Bestatter sollten Angehörige daher offen mitteilen, dass eine Kostenübernahme nach § 74 SGB XII beantragt werden soll — viele Leipziger Bestatter haben Erfahrung mit dem Sozialamt und gestalten das Angebot entsprechend.</p>
  </div>

'''

CHEMNITZ_SOZIAL = '''  <section class="mr-section">
    <h2>Sozialbestattung in Chemnitz: Wenn die Kosten nicht zu tragen sind</h2>
    <p>Reicht der Nachlass nicht und können auch die bestattungspflichtigen Angehörigen die Kosten nicht aufbringen, übernimmt der Träger der Sozialhilfe die <em>erforderlichen</em> Bestattungskosten. Rechtsgrundlage ist <strong>§ 74 SGB XII</strong> in Verbindung mit <strong>§ 10 Abs. 3 SächsBestG</strong>, der die Kostentragungspflicht des Bestattungspflichtigen regelt. Maßstab der Erforderlichkeit ist nach ständiger Rechtsprechung des Bundessozialgerichts eine ortsübliche, würdige, aber einfache Bestattung — das Urteil <strong>B 8 SO 20/10 R vom 25.08.2011</strong> hat diesen Rahmen für Sachsen und bundesweit konkretisiert.</p>
    <h3>Zuständige Stelle in Chemnitz</h3>
    <p>Anlaufstelle ist das <strong>Sozialamt der Stadt Chemnitz</strong>:</p>
    <p>Bahnhofstraße 53, 09111 Chemnitz<br>
    Telefon: <a href="tel:+493714885001">0371 488-5001</a><br>
    E-Mail: <a href="mailto:sozialamt@stadt-chemnitz.de">sozialamt@stadt-chemnitz.de</a></p>
    <p>Zuständig ist der örtliche Sozialhilfeträger am Sterbeort, in der Regel also Chemnitz, wenn der Sterbefall im Stadtgebiet eingetreten ist. Der Antrag wird vom Bestattungspflichtigen — meist einem nahen Angehörigen — gestellt, nicht vom Verstorbenen oder vom Bestatter direkt.</p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Übernommen werden die ortsüblichen Grundkosten einer einfachen Bestattung: Sarg oder Urne in einfacher Ausführung, Überführung, Friedhofsgrundgebühr, Beisetzungsgebühr (Erdgrab öffnen 297,20 € bzw. Urnengrab öffnen 49,40 €), Grabnutzungsgebühr für ein Reihen- oder Urnenlösestellen-Grab nach der Gebührensatzung der Stadt Chemnitz sowie Trauerredner und einfache Trauerfeier in der Feierhalle (90,70 €). <strong>Nicht übernommen</strong> werden Wahlgräber in bevorzugter Lage, aufwendige Grabsteine, Floristik über das einfache Maß hinaus, Trauerdrucksachen, Bewirtung und Grabpflege. Vorrangig einzusetzen sind Nachlassvermögen, Sterbegelder, Lebensversicherungen und Unterhaltsansprüche.</p>
    <h3>Antragszeitpunkt</h3>
    <p>Der Antrag sollte so früh wie möglich gestellt werden — idealerweise vor der Beauftragung des Bestatters. Eine Vorab-Bewilligung ist nicht zwingend; die Kostenübernahme kann auch nach der Bestattung beantragt werden. Wer in Vorleistung getreten ist, muss die Erforderlichkeit der einzelnen Posten belegen — Originalrechnungen mit Einzelpositionen sind unverzichtbar. Vorsicht bei der Auswahl des Bestatters: Pauschalangebote ohne Einzelpositionen erschweren die Prüfung durch das Sozialamt und führen häufig dazu, dass Teilbeträge als nicht erforderlich abgelehnt werden.</p>
  </section>

'''

# Magdeburg: Normalize as standalone section (h2 instead of h3-in-Kosten as plan suggested)
# Tel-link: normalize +49391540-6712 to digits-only +493915406712 (12 digits)
MAGDEBURG_SOZIAL = '''  <section class="mr-section" id="sozialbestattung">
    <h2>Sozialbestattung in Magdeburg (§ 74 SGB XII)</h2>
    <p>Wenn Bestattungspflichtige die Kosten einer einfachen, angemessenen und würdigen Bestattung nicht aus eigenen Mitteln und nicht aus dem Nachlass tragen können, übernimmt das Sozialamt die erforderlichen Kosten nach <strong>§ 74 SGB XII</strong> („Bestattungskosten"). Wer in Sachsen-Anhalt zur Bestattung verpflichtet ist, regelt <strong>§ 10 BestattG LSA</strong>: Die Bestattungspflicht trifft in fester Reihenfolge zunächst Ehegatten und eingetragene Lebenspartner, dann volljährige Kinder, Eltern, volljährige Geschwister, Großeltern und volljährige Enkel. Die sozialhilferechtliche Kostentragungspflicht (§ 74 SGB XII) und die landesrechtliche Bestattungspflicht (§ 10 BestattG LSA) sind zwei getrennte Prüfungsebenen — wer bestattungspflichtig ist, ist nicht automatisch auch kostentragungspflichtig im Sinne des § 74 SGB XII (vgl. <strong>BSG, Urteil vom 25.08.2011, Az. B 8 SO 20/10 R</strong>).</p>
    <h3>Zuständige Stelle in Magdeburg</h3>
    <p>Für die Übernahme von Bestattungskosten ist in Magdeburg das <strong>Sozial- und Wohnungsamt, Leistungsbereich I</strong> zuständig:</p>
    <p>Wilhelm-Höpfner-Ring 4, 39116 Magdeburg<br>
    Telefon: <a href="tel:+493915406712">+49 391 540-6712</a></p>
    <p>Die Kontaktaufnahme erfolgt über das städtische Kontaktformular auf <a href="https://www.magdeburg.de/" rel="noopener" target="_blank">magdeburg.de</a>. Maßgeblich ist die <em>Verwaltungsvorschrift der Landeshauptstadt Magdeburg zur Übernahme von Bestattungskosten nach § 74 SGB XII</em> (Bestattungskostenrichtlinie), die Höchstbeträge und Angemessenheit konkretisiert.</p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Die Stadt übernimmt die Kosten einer einfachen, angemessenen und würdigen Bestattung. Dazu zählen insbesondere die Bestatterleistungen (einfacher Sarg bzw. Urne, Überführung, Versorgung), die Friedhofsgebühren (Grabnutzungsgebühr, Bestattungs-/Beisetzungsgebühr, gegebenenfalls eine einfache Kapellennutzung) sowie die Kosten der Einäscherung. <strong>Nicht übernommen</strong> werden Trauerfeier-Bewirtung, Trauerredner und Floristik über das einfache Maß hinaus, gehobene Grabarten (besondere Lage, Wahlgrab mit aufwendiger Gestaltung) und Grabmal in größerem Umfang. In Magdeburg findet die Beisetzung im Rahmen einer Sozialbestattung in der Praxis regelmäßig als Urnenbeisetzung auf städtischen Friedhöfen statt — meist auf West- oder Südfriedhof.</p>
    <h3>Antragszeitpunkt: möglichst vor Beauftragung des Bestatters</h3>
    <p>Der Antrag sollte <strong>vor Beauftragung des Bestatters</strong> gestellt werden, mindestens aber vor Bezahlung der Rechnungen. Welche Kosten im Einzelfall übernahmefähig sind, klärt das Sozial- und Wohnungsamt vorab. Wer Bestatter und Friedhof beauftragt, ohne mit dem Sozialamt gesprochen zu haben, riskiert, auf Rechnungsposten sitzen zu bleiben, die als „nicht erforderlich" eingestuft werden. Antragsformular, Hinweisblatt und Mitbringliste stehen auf magdeburg.de zum Download bereit; ein Onlineantrag ist über das städtische Portal möglich. Verfahren und Bescheid sind gebührenfrei; gegen den Bescheid kann innerhalb eines Monats Widerspruch erhoben werden.</p>
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

# Leipzig — anchor before FAQ
leipzig_anchor = '<div class="mr-faq">'
ok = do_insert('bestatter/leipzig/index.html', leipzig_anchor, LEIPZIG_SOZIAL, 'LEIPZIG')
if not ok:
    with open('bestatter/leipzig/index.html','r',encoding='utf-8') as f: s = f.read()
    alts = ['  <div class="mr-faq">', '<section class="mr-faq', '<h2>Häufige Fragen']
    for a in alts:
        if a in s and s.count(a) == 1:
            do_insert('bestatter/leipzig/index.html', a, LEIPZIG_SOZIAL, f'LEIPZIG ({a[:40]})')
            break

# Chemnitz — anchor before FAQ section
chemnitz_anchor = '  <section class="mr-section">\n    <h2>Häufige Fragen zur Bestattung in Chemnitz</h2>'
ok = do_insert('bestatter/chemnitz/index.html', chemnitz_anchor, CHEMNITZ_SOZIAL, 'CHEMNITZ')
if not ok:
    with open('bestatter/chemnitz/index.html','r',encoding='utf-8') as f: s = f.read()
    alts = ['<h2>Häufige Fragen zur Bestattung in Chemnitz</h2>', '<section class="mr-faq']
    for a in alts:
        if a in s and s.count(a) == 1:
            do_insert('bestatter/chemnitz/index.html', a, CHEMNITZ_SOZIAL, f'CHEMNITZ ({a[:40]})')
            break

# Magdeburg — insert as standalone section, before FAQ or Todesfall section
magdeburg_anchor = '<section class="mr-section" id="todesfall">'
ok = do_insert('bestatter/magdeburg/index.html', magdeburg_anchor, MAGDEBURG_SOZIAL, 'MAGDEBURG')
if not ok:
    with open('bestatter/magdeburg/index.html','r',encoding='utf-8') as f: s = f.read()
    alts = [
        '<h2 id="todesfall"',
        '<h2>Was nach einem Todesfall in Magdeburg',
        '  <section class="mr-section">\n    <h2>Was nach einem Todesfall',
        '<section class="mr-faq',
    ]
    for a in alts:
        if a in s and s.count(a) == 1:
            do_insert('bestatter/magdeburg/index.html', a, MAGDEBURG_SOZIAL, f'MAGDEBURG ({a[:40]})')
            break

# dateModified
print('\n=== dateModified UPDATE ===')
for city in ['leipzig','chemnitz','magdeburg']:
    fp = f'bestatter/{city}/index.html'
    with open(fp,'r',encoding='utf-8') as f: s = f.read()
    orig = s
    s = re.sub(r'"dateModified":\s*"\d{4}-\d{2}-\d{2}"', '"dateModified": "2026-05-19"', s)
    if s != orig:
        with open(fp,'w',encoding='utf-8') as f: f.write(s)
        m = re.search(r'"dateModified":\s*"([^"]+)"', s)
        print(f'{city}: dateModified = {m.group(1) if m else "?"}')

print('\n=== VERIFICATION ===')
for city in ['leipzig', 'chemnitz', 'magdeburg']:
    fp = f'bestatter/{city}/index.html'
    with open(fp,'r',encoding='utf-8') as f: s = f.read()
    nul_ok = len(s.rstrip('\x00')) == len(s)
    has_sozial = 'Sozialbestattung in ' in s
    has_sgb = '§ 74 SGB XII' in s
    has_bsg = 'B 8 SO 20/10 R' in s
    has_sn = ('§ 10 Abs. 3 SächsBestG' in s) or ('§ 10 BestattG LSA' in s)
    sec_o = len(re.findall(r'<section\b', s))
    sec_c = len(re.findall(r'</section>', s))
    print(f'{city}: len={len(s)}, NUL={nul_ok}, Sozial={has_sozial}, §74={has_sgb}, BSG={has_bsg}, BL-§={has_sn}, <section>={sec_o}/{sec_c}')
