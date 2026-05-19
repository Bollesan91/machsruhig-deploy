#!/usr/bin/env python3
"""Batch 3 NRW-Trio Sozialbestattung: Düsseldorf + Duisburg + Bielefeld."""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# ============================================================
# DÜSSELDORF (Landeshauptstadt NRW)
# ============================================================
DUESSELDORF_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Düsseldorf — wenn die Kosten nicht tragbar sind</h2>
    <p>Reicht der Nachlass nicht aus und können die Bestattungspflichtigen die Kosten aus eigenem Einkommen und Vermögen nicht aufbringen, übernimmt das Sozialamt unter den Voraussetzungen des <a href="https://www.gesetze-im-internet.de/sgb_12/__74.html" rel="noopener" target="_blank"><strong>§ 74 SGB XII</strong></a> die <strong>erforderlichen Kosten einer einfachen, ortsüblichen Bestattung</strong>. Die Leistung ist nachrangig: Eigenes Einkommen und Vermögen sowie der Nachlass des Verstorbenen müssen vorrangig eingesetzt werden. Wer in Düsseldorf zur Bestattung verpflichtet ist, ergibt sich aus <strong>§ 8 BestG NRW</strong>: in fester Reihenfolge Ehegatte oder Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder.</p>
    <h3>Zuständige Stelle in Düsseldorf</h3>
    <p>Anträge sind beim <strong>Amt für Soziales</strong> der Landeshauptstadt Düsseldorf zu stellen — Fachbereich <strong>Unterstützung im Alter, bei Pflegebedürftigkeit und zur Existenzsicherung (51/84)</strong>, Sachbearbeitung Bestattungskosten.<br>
    Anschrift: <strong>Willi-Becker-Allee 8, 40227 Düsseldorf</strong><br>
    Telefon: <a href="tel:+4921189911">0211 89-91</a><br>
    E-Mail: <a href="mailto:bestattungskosten@duesseldorf.de">bestattungskosten@duesseldorf.de</a></p>
    <p>Eine telefonische Antragstellung ist nicht möglich; Termine werden nach Vereinbarung vergeben. Zuständig ist Düsseldorf, wenn die verstorbene Person hier zuletzt Sozialhilfe oder Grundsicherung bezogen hat — ansonsten das Sozialamt am Sterbeort.</p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Erstattungsfähig ist der Standardrahmen einer würdigen Bestattung: einfacher Sarg oder Urne, Versorgung und Überführung im Stadtgebiet, Friedhofsgebühren für ein <strong>Reihengrab</strong> nach Düsseldorfer Gebührentarif, Beisetzungsgebühr, Trauerhallennutzung sowie bei Feuerbestattung die Einäscherung im Krematorium Stoffeler Friedhof. <strong>Nicht übernommen</strong> werden in der Regel: Wahlgrabstätten statt Reihengrab, Trauerdruck und Trauerfeier-Ausstattung über das Notwendige hinaus, Bewirtung, Grabstein oberhalb des satzungsrechtlich erforderlichen Maßes, Anreise- und Übernachtungskosten von Angehörigen sowie Überführungen aus dem oder ins Ausland. Maßstab ist das Urteil des Bundessozialgerichts vom <strong>25.08.2011 (BSG B 8 SO 20/10 R)</strong>: erstattungsfähig sind ortsübliche, einfache und würdige Kosten — keine pauschalen Höchstsätze, sondern eine Einzelfallprüfung anhand des Düsseldorfer Gebührentarifs.</p>
    <h3>Antragszeitpunkt</h3>
    <p>Der Antrag sollte <strong>vor der Beauftragung des Bestatters</strong> gestellt werden, damit das Sozialamt eine Kostenübernahmeerklärung ausstellt und der Bestatter direkt abrechnet. Eine <strong>rückwirkende Antragstellung</strong> ist möglich, wenn die Bestattung aufgrund der Zehn-Tage-Frist nach § 13 BestG NRW bereits durchgeführt werden musste — die Rechnungen sollten dann zeitnah, spätestens innerhalb weniger Monate nach der Bestattung, eingereicht werden. Allgemeine Hintergründe zur Sozialbestattung finden Angehörige auf unserer Seite zu den <a href="/bestattungskosten">Bestattungskosten</a>.</p>
  </div>

'''

# ============================================================
# DUISBURG
# ============================================================
DUISBURG_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Duisburg — wenn die Kosten nicht zu tragen sind</h2>
    <p>Eine Bestattung kostet in Duisburg erfahrungsgemäß 6.000 bis 9.000 Euro. Können die nach <strong>§ 8 BestG NRW</strong> bestattungspflichtigen Angehörigen (Reihenfolge: Ehegatte/eingetragener Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder) diese Kosten nicht aus eigenem Einkommen und Vermögen aufbringen, übernimmt das Sozialamt nach <strong>§ 74 SGB XII</strong> die erforderlichen Kosten — soweit ihnen die Kostentragung nicht zugemutet werden kann. Die Sozialbestattung ist abzugrenzen von der ordnungsbehördlichen Bestattung nach § 8 Abs. 1 BestG NRW, die das Bürger- und Ordnungsamt veranlasst, wenn überhaupt keine Angehörigen bestatten — bei der Sozialbestattung bleibt die Totenfürsorge bei den Angehörigen.</p>
    <h3>Voraussetzungen — wer Anspruch hat</h3>
    <p>Antragsberechtigt ist, wer nach Erbrecht, Unterhaltsrecht oder § 8 BestG NRW bestattungspflichtig ist und die Kosten nachweislich nicht tragen kann. Geprüft werden Einkommen und Vermögen der Antragsteller sowie das Erbe — der Nachlass des Verstorbenen ist vorrangig einzusetzen. Empfänger von Bürgergeld, Grundsicherung im Alter oder geringer Renten erfüllen die Voraussetzungen regelmäßig. Das Bundessozialgericht hat mit Urteil vom <strong>25. August 2011 (Az. B 8 SO 20/10 R)</strong> klargestellt, dass auch Schulden, laufende Verpflichtungen und die individuelle Lebenslage in die Zumutbarkeitsprüfung einzubeziehen sind.</p>
    <h3>Zuständige Stelle in Duisburg</h3>
    <p>Zuständig ist das <strong>Amt für Soziales und Wohnen der Stadt Duisburg</strong><br>
    Schwanenstraße 5–7, 47051 Duisburg<br>
    Telefon (Call Duisburg): <a href="tel:+4920394000">0203 94000</a><br>
    E-Mail: <a href="mailto:amt-fuer-soziales-und-wohnen@stadt-duisburg.de">amt-fuer-soziales-und-wohnen@stadt-duisburg.de</a></p>
    <p>Antragsformulare sind dort erhältlich; eine schriftliche Antragstellung ist nicht zwingend formgebunden, aber dringend empfohlen. War der Verstorbene zu Lebzeiten Sozialhilfeempfänger, bleibt der bislang zuständige Sozialhilfeträger zuständig.</p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Übernommen werden die <strong>erforderlichen Kosten einer einfachen, ortsüblichen und würdigen Bestattung</strong>: einfacher Sarg oder Urne, hygienische Versorgung, Überführung im Stadtgebiet, Friedhofsgebühren für ein einfaches Reihengrab (bei Wahlgrabstellen nur, soweit ein Reihengrab nicht verfügbar ist), Krematoriumsgebühr bei Feuerbestattung, Trauerhallennutzung, Sterbeurkunden und ggf. ein einfaches Grabzeichen, soweit die Friedhofssatzung dies vorschreibt. Bei muslimischer Bestattung wird die rituelle Waschung anerkannt.</p>
    <p><strong>Nicht übernommen</strong> werden: Trauerfeier-Erweiterungen (Musik, Blumenschmuck über das Übliche hinaus), Trauerredner-Honorare, Trauerkaffee, Todesanzeigen, Anreisekosten der Angehörigen, Auslandsüberführungen, aufwendige Grabsteine und die spätere Grabpflege.</p>
    <h3>Antrag rechtzeitig stellen</h3>
    <p>Der Antrag kann <strong>vor oder nach</strong> der Bestattung gestellt werden — empfohlen ist die Antragstellung <strong>vor</strong> der Beauftragung des Bestatters. Mit einer schriftlichen Kostenübernahmeerklärung des Sozialamts rechnet der Bestatter direkt mit der Behörde ab. Wird der Antrag erst nach der Bestattung gestellt, prüft das Amt nur noch die Kosten, die als erforderlich gelten — alles darüber Hinausgehende bleibt bei den Angehörigen. Erforderliche Unterlagen: Sterbeurkunde, Bestatter-Kostenvoranschlag, Gebührenbescheid des Friedhofs, Einkommens- und Vermögensnachweise (Renten-/Leistungsbescheide, Kontoauszüge der letzten drei Monate), Nachweise zum Erbe.</p>
  </div>

'''

# ============================================================
# BIELEFELD (uses mr-service class which exists in own CSS)
# ============================================================
BIELEFELD_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Bielefeld — wenn die Kosten nicht getragen werden können</h2>
    <p>Reicht der Nachlass der verstorbenen Person nicht aus und sind die bestattungspflichtigen Angehörigen finanziell nicht in der Lage, die Kosten zu tragen, übernimmt das Sozialamt nach <strong><a href="https://www.gesetze-im-internet.de/sgb_12/__74.html" rel="noopener" target="_blank">§ 74 SGB XII</a></strong> die <em>erforderlichen Kosten</em> einer einfachen, würdigen Bestattung. Voraussetzung ist, dass das Tragen der Kosten den Verpflichteten nicht zugemutet werden kann; das Sozialamt prüft Einkommen und Vermögen aller in Betracht kommenden Personen. Bestattungspflichtig ist in Bielefeld die in <strong>§ 8 BestG NRW</strong> festgelegte Reihenfolge der Angehörigen: Ehegatte beziehungsweise eingetragener Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern und volljährige Enkelkinder. Wichtig: Auch wer die Erbschaft <strong>ausgeschlagen</strong> hat, bleibt nach Landesrecht bestattungspflichtig — das Bundessozialgericht hat mit Urteil vom <strong>25. August 2011 (Az. B 8 SO 20/10 R)</strong> bestätigt, dass die öffentlich-rechtliche Bestattungspflicht durch eine Erbausschlagung nicht entfällt; der Anspruch auf Kostenübernahme nach § 74 SGB XII bleibt davon unberührt.</p>
    <h3>Zuständige Stelle in Bielefeld</h3>
    <div class="mr-service">
      <strong>Amt für soziale Leistungen — Sozialamt, Abteilung SGB XII 1 (außerhalb von Einrichtungen)</strong>
      <dl class="mr-service-grid">
        <dt>Anschrift</dt><dd>Neues Rathaus, Niederwall 23, 33602 Bielefeld</dd>
        <dt>Telefon</dt><dd>0521 51-0 (BürgerServiceCenter)</dd>
        <dt>Fax</dt><dd>0521 51-8212</dd>
        <dt>E-Mail</dt><dd><a href="mailto:sozialhilfe@bielefeld.de">sozialhilfe@bielefeld.de</a></dd>
        <dt>Zuständig</dt><dd>Bestattungskosten-Übernahme, wenn die verstorbene Person in Bielefeld verstorben ist oder hier SGB-XII-Leistungen bezogen hat</dd>
      </dl>
    </div>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Übernommen werden nur die <strong>erforderlichen Kosten einer Bestattung einfacher, aber würdiger Art</strong>. Die Stadt Bielefeld hat dazu eine Vereinbarung mit den örtlichen Bestattungsunternehmen geschlossen, in der die anerkennungsfähigen Höchstbeträge für eine Sozialbestattung festgelegt sind. Regelmäßig getragen werden die Grundleistungen des Bestatters (einfacher Sarg oder Urne, Überführung im Stadtgebiet, hygienische Versorgung), die Friedhofsgebühren für eine einfache Grabstelle nach Gebührensatzung der Stadt sowie eine schlichte Trauerfeier am Grab. <strong>Nicht übernommen</strong> werden Repräsentations- und Wahlleistungen: aufwendige Särge oder Urnen, Wahlgrabstätten anstelle eines Reihengrabs, Trauerdruck und Zeitungsanzeigen, Grabstein und Grabeinfassung, Erstbepflanzung und Grabpflege, Trauerredner oder umfangreiche musikalische Begleitung sowie Bewirtung der Trauergäste. Wer eine über das Notwendige hinausgehende Bestattung wünscht, trägt die Mehrkosten selbst.</p>
    <h3>Antragszeitpunkt — vor Auftragserteilung Rücksprache halten</h3>
    <p>Der Antrag auf Kostenübernahme sollte <strong>zeitnah nach dem Sterbetag</strong> beim Sozialamt gestellt werden — anders als bei vielen anderen Sozialhilfeleistungen ist ein Antrag nach § 74 SGB XII auch <em>nach</em> der Bestattung noch möglich. Die Stadt Bielefeld empfiehlt jedoch ausdrücklich, das Bestattungsunternehmen bereits bei Auftragserteilung darauf hinzuweisen, dass eine Sozialbestattung beantragt wird; nur so lässt sich vermeiden, dass kostspielige Zusatzleistungen beauftragt werden, die später nicht übernommen werden. Erforderlich sind unter anderem Sterbeurkunde, Rechnung des Bestatters mit Einzelnachweisen, Gebührenbescheid der Friedhofsverwaltung, Kontoauszüge der verstorbenen Person der letzten drei Monate, Nachlasserklärung, Vermögenserklärung der Antragsteller sowie Einkommens- und Vermögensnachweise aller bestattungspflichtigen Angehörigen. Der Antrag kann persönlich abgegeben oder über den Online-Dienst der Stadt Bielefeld mit BundID-Konto eingereicht werden; die Antragstellung selbst ist gebührenfrei.</p>
  </div>

'''

# ============================================================
# INSERT LOGIC
# ============================================================
def do_insert(fp, anchor, insert_html, label, mode='before'):
    with open(fp, 'r', encoding='utf-8') as f:
        s = f.read()
    orig_len = len(s)
    n = s.count(anchor)
    print(f'{label}: anchor matches = {n}')
    if n != 1:
        print(f'  ABORT: expected 1, got {n}')
        return False
    if mode == 'before':
        new_s = s.replace(anchor, insert_html + anchor)
    else:
        new_s = s.replace(anchor, anchor + insert_html)
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(new_s)
    print(f'  WROTE {label}: {orig_len} -> {len(new_s)} (+{len(new_s)-orig_len})')
    return True

# Düsseldorf — insert BEFORE Was-tun section (per plan)
duesseldorf_anchor = '  <div class="mr-section">\n    <h2>Was nach einem Todesfall in Düsseldorf zu tun ist</h2>'
do_insert('bestatter/duesseldorf/index.html', duesseldorf_anchor, DUESSELDORF_SOZIAL, 'DUESSELDORF')

# Duisburg — insert BEFORE Bestatter-Wahl section
duisburg_anchor = '  <div class="mr-section">\n    <h2>Bestatter-Wahl in Duisburg</h2>'
do_insert('bestatter/duisburg/index.html', duisburg_anchor, DUISBURG_SOZIAL, 'DUISBURG')

# Bielefeld — insert BEFORE Bestatter-Wahl section
bielefeld_anchor = '  <div class="mr-section">\n    <h2>Bestatter-Wahl in Bielefeld</h2>'
do_insert('bestatter/bielefeld/index.html', bielefeld_anchor, BIELEFELD_SOZIAL, 'BIELEFELD')

# ============================================================
# VERIFICATION
# ============================================================
print('\n=== VERIFICATION ===')
for city in ['duesseldorf', 'duisburg', 'bielefeld']:
    fp = f'bestatter/{city}/index.html'
    with open(fp, 'r', encoding='utf-8') as f:
        s = f.read()
    nul_ok = len(s.rstrip('\x00')) == len(s)
    has_sozial = ('Sozialbestattung in ' in s)
    has_sgb = '§ 74 SGB XII' in s
    has_bsg = 'B 8 SO 20/10 R' in s
    has_nrw = '§ 8 BestG NRW' in s
    sec_open = len(re.findall(r'<section\b', s))
    sec_close = len(re.findall(r'</section>', s))
    tag_balanced = (sec_open == sec_close)
    print(f'{city}: len={len(s)}, NUL-ok={nul_ok}, Sozial={has_sozial}, §74={has_sgb}, BSG={has_bsg}, §8 NRW={has_nrw}, <section>={sec_open}/{sec_close} balanced={tag_balanced}')
