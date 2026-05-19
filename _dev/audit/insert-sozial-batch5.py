#!/usr/bin/env python3
"""Batch 5 Niedersachsen-Trio Sozialbestattung:
- Braunschweig: REPLACE existing section (Strukturberater fand pre-existing Modul, schlug Ersatz vor)
- Oldenburg: INSERT new section
- Osnabrück: INSERT new section
All use § 8 Abs. 3 BestattG Niedersachsen + BSG B 8 SO 20/10 R.
"""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# ============================================================
# BRAUNSCHWEIG (REPLACE existing section)
# ============================================================
# The existing section spans from <section class="mr-section" id="sozialbestattung"> to </section>
# We replace it with the enhanced version (adds § 8 Abs. 3 NBestattG + BSG + Was-vs-Nicht structure)

BRAUNSCHWEIG_NEW = '''<section class="mr-section" id="sozialbestattung">
    <h2>Sozialbestattung in Braunschweig</h2>
    <p>Reicht der Nachlass nicht aus und ist auch den Bestattungspflichtigen die Kostentragung nicht zuzumuten, übernimmt der Sozialhilfeträger nach <a href="https://www.gesetze-im-internet.de/sgb_12/__74.html" rel="noopener" target="_blank">§ 74 SGB XII</a> die erforderlichen Kosten einer einfachen, ortsüblichen Bestattung. In Braunschweig ist dafür der Fachbereich Soziales und Gesundheit der Stadt zuständig.</p>
    <h3>Wer ist bestattungspflichtig?</h3>
    <p>Nach <strong>§ 8 Abs. 3 BestattG Niedersachsen</strong> haben in folgender Rangfolge für die Bestattung zu sorgen: Ehegattin/Ehegatte beziehungsweise eingetragene Lebenspartnerin/Lebenspartner, Kinder, Enkelkinder, Eltern, Großeltern, Geschwister. Sorgt niemand für die Bestattung, veranlasst nach § 8 Abs. 4 die Gemeinde die Bestattung; die vorrangig Verpflichteten haften als Gesamtschuldner. Die Bestattungspflicht nach öffentlichem Recht besteht unabhängig davon, ob die Person Erbe ist oder das Erbe ausschlägt — das Bundessozialgericht hat in seinem Urteil <strong>B 8 SO 20/10 R vom 25.08.2011</strong> klargestellt, dass auch Erbausschlagende Anspruch auf Kostenübernahme nach § 74 SGB XII haben können, sofern sie bestattungspflichtig sind und die Belastung unzumutbar ist.</p>
    <h3>Zuständige Stelle in Braunschweig</h3>
    <p>Stadt Braunschweig, Fachbereich Soziales und Gesundheit, Besondere Einzelfallhilfen (50.34), Naumburgstraße 25, 38124 Braunschweig. Antragsformulare sind montags, mittwochs und freitags von 9:00 bis 12:30 Uhr in der Infothek erhältlich; die Beantragung ist auch online über das <a href="https://service.braunschweig.de/dienstleistungen/-/egov-bis-detail/dienstleistung/172034/show" rel="noopener" target="_blank">Serviceportal der Stadt Braunschweig</a> möglich. Zuständigkeit nach § 98 SGB XII: war die verstorbene Person Sozialhilfeempfängerin, bleibt der bisherige Träger zuständig, sonst der Träger am Sterbeort.</p>
    <h3>Was wird übernommen — und was nicht?</h3>
    <p><strong>Übernommen werden</strong> die erforderlichen Kosten einer würdigen, einfachen Bestattung nach Maßstab unterer und mittlerer Einkommen: einfacher Sarg oder Urne, Überführung im Stadtgebiet, Friedhofsgebühren für eine einfache Grabstelle, schlichte Trauerfeier, einfache Grabkennzeichnung. Die übernahmefähige Größenordnung bewegt sich in Niedersachsen erfahrungsgemäß bei rund 3.000 bis 4.500 €; verbindlich sind die Vereinbarungen der Stadt mit den Braunschweiger Bestattern.</p>
    <p><strong>Nicht übernommen werden</strong> Mehrkosten für gehobene Sarg- oder Urnenausstattung, aufwändige Trauerfeiern, Blumenschmuck über das Übliche hinaus, Traueranzeigen, Trauerdruck, Bewirtung, Grabstein und Grabpflege sowie Überführungen ins Ausland. Übernommen werden nur Kosten, die nicht aus dem Nachlass oder aus Versicherungsleistungen (Sterbegeld, Lebensversicherung) gedeckt sind — diese sind vorrangig einzusetzen.</p>
    <h3>Antrag möglichst vor Auftragserteilung</h3>
    <p>Der Antrag soll grundsätzlich vor Beauftragung des Bestatters gestellt werden, mindestens aber muss der Bestatter ausdrücklich auf den geplanten Antrag hingewiesen werden. Nur so ist sichergestellt, dass nach den Stadt-Vereinbarungen abgerechnet werden kann; Mehrkosten müssen sonst von den Antragstellenden selbst getragen werden. Eine rückwirkende Übernahme ist nach gefestigter Rechtsprechung zwar nicht ausgeschlossen, in der Praxis aber riskant: Rechnungen, die das ortsübliche Maß übersteigen, werden gekürzt. Beizulegen sind Sterbeurkunde, Kontoauszüge der letzten drei Monate (Verstorbene und Antragsteller), Vermögens- und Einkommensnachweise, Versicherungsnachweise sowie alle Bestattungsrechnungen.</p>
    <div class="callout">
      <strong>Hinweis:</strong> Bei nachträglich bekannt werdendem Nachlass oder Versicherungsleistungen kann die Stadt übernommene Kosten zurückfordern. Wer das Erbe ausgeschlagen hat, bleibt bestattungspflichtig nach § 8 BestattG, kann aber gleichwohl Anspruch auf Kostenübernahme nach § 74 SGB XII haben (BSG B 8 SO 20/10 R).
    </div>
  </section>'''

# Find the existing braunschweig section and replace it
fp = 'bestatter/braunschweig/index.html'
with open(fp,'r',encoding='utf-8') as f: s = f.read()
orig_len = len(s)
# Match the entire existing section (greedy from open to first </section> + linebreak)
pattern = r'<section class="mr-section" id="sozialbestattung">.*?</section>'
m = re.search(pattern, s, re.DOTALL)
if m:
    print(f'BRAUNSCHWEIG: existing section found ({len(m.group(0))} chars), REPLACE')
    s_new = s[:m.start()] + BRAUNSCHWEIG_NEW + s[m.end():]
    with open(fp,'w',encoding='utf-8') as f: f.write(s_new)
    print(f'  WROTE BRAUNSCHWEIG: {orig_len} -> {len(s_new)} (delta {len(s_new)-orig_len})')
else:
    print('BRAUNSCHWEIG: existing section NOT FOUND — ABORT')

# ============================================================
# OLDENBURG (INSERT new section before <aside class="cross-links">)
# ============================================================
OLDENBURG_SOZIAL = '''<section class="mr-section">
  <h2>Sozialbestattung in Oldenburg: Wenn die Kosten nicht zumutbar sind</h2>
  <p>Wenn die nach <strong>§ 8 Abs. 3 Niedersächsisches Bestattungsgesetz (NBestattG)</strong> bestattungspflichtigen Angehörigen die Kosten der Bestattung nicht aus eigenen Mitteln tragen können, greift <strong>§ 74 SGB XII</strong>. Danach werden „die erforderlichen Kosten der Bestattung übernommen, soweit den hierzu Verpflichteten nicht zugemutet werden kann, die Kosten zu tragen". Anspruchsberechtigt ist nicht der oder die Verstorbene, sondern der oder die bestattungspflichtige Angehörige — das ist seit dem Grundsatzurteil des Bundessozialgerichts vom <strong>25.08.2011 (Az. B 8 SO 20/10 R)</strong> höchstrichterlich geklärt. Zumutbarkeit prüft das Sozialamt einzelfallbezogen anhand von Einkommen, Vermögen und Nachlass.</p>
  <h3>Zuständige Stelle in Oldenburg</h3>
  <p>Oldenburg ist kreisfreie Stadt; zuständig ist daher das städtische Sozialamt selbst, nicht ein Landkreis. Anträge auf Übernahme der Bestattungskosten nach § 74 SGB XII nimmt der <strong>Fachdienst Soziale Hilfen der Stadt Oldenburg</strong> entgegen:</p>
  <p>Stadt Oldenburg — Amt für Soziale Hilfen<br>
  Pferdemarkt 14, 26121 Oldenburg<br>
  Telefon: <a href="tel:+4944123544444">0441 235-4444</a><br>
  E-Mail: <a href="mailto:soziales@stadt-oldenburg.de">soziales@stadt-oldenburg.de</a><br>
  Sprechzeiten: Mo, Di, Do 8–12 und 13.30–15.30 Uhr · Fr 8–12 Uhr · Mi nach Vereinbarung</p>
  <p>Wichtig: Die Sozialbestattung ist von der ordnungsbehördlichen Bestattung nach § 8 Abs. 4 NBestattG zu unterscheiden — letztere ordnet das Ordnungsamt nur an, wenn niemand der Bestattungspflicht überhaupt nachkommt; die Kosten werden anschließend ebenfalls bei den Pflichtigen geltend gemacht.</p>
  <h3>Was übernommen wird — und was nicht</h3>
  <p>Übernommen werden die „erforderlichen" Kosten einer ortsüblichen, einfachen, aber würdigen Bestattung. Dazu zählen üblicherweise einfacher Sarg oder Urne, Überführung im Stadtgebiet, Friedhofsgebühren für ein Reihengrab auf einem städtischen Friedhof, Beisetzungsgebühr, Sterbeurkunden und eine schlichte Trauerfeier. <strong>Nicht übernommen</strong> werden in der Regel: Wahlgrabstätten in besonderer Lage, aufwendige Grabsteine, Trauerkaffee, Blumenschmuck über das Maß einer einfachen Bestattung hinaus und Bestattungsvorsorgekosten, die durch Nachlassvermögen oder Sterbegeldversicherung gedeckt sind. Der Nachlass der oder des Verstorbenen ist vorrangig einzusetzen.</p>
  <h3>Antragszeitpunkt</h3>
  <p>Der Antrag sollte <strong>vor</strong> Vertragsschluss mit dem Bestatter beim Sozialamt gestellt werden — jedenfalls aber so früh wie möglich. Eine rückwirkende Übernahme ist zwar möglich, das Sozialamt prüft dann aber besonders streng, ob die in Anspruch genommenen Leistungen tatsächlich erforderlich und ortsüblich waren. Wer einen teuren Bestattungsvertrag abschließt, bevor die Kostenübernahme geklärt ist, riskiert, auf der Differenz zur amtlichen Erforderlichkeitsschwelle sitzen zu bleiben. Praktisch sinnvoll: noch am Tag des Sterbefalls einen ersten Antrag stellen und mit dem Bestatter offen kommunizieren, dass eine Kostenübernahme nach § 74 SGB XII geprüft wird — seriöse Anbieter kennen das Verfahren.</p>
</section>

'''

# Find anchor before <aside class="cross-links"> in Oldenburg
fp = 'bestatter/oldenburg/index.html'
with open(fp,'r',encoding='utf-8') as f: s = f.read()
orig_len = len(s)
# Try multiple anchor patterns
oldenburg_anchors = [
    '<aside class="cross-links">',
    '  <aside class="cross-links">',
    '<aside class=\"cross-links\">',
]
inserted = False
for a in oldenburg_anchors:
    n = s.count(a)
    if n == 1:
        s_new = s.replace(a, OLDENBURG_SOZIAL + a)
        with open(fp,'w',encoding='utf-8') as f: f.write(s_new)
        print(f'OLDENBURG: anchor "{a[:40]}..." matches=1, INSERTED')
        print(f'  WROTE OLDENBURG: {orig_len} -> {len(s_new)}')
        inserted = True
        break
if not inserted:
    # Try inserting before the FAQ section instead
    fallback = '  <section class="mr-faq'
    if fallback in s:
        s_new = s.replace(fallback, OLDENBURG_SOZIAL + fallback, 1)
        with open(fp,'w',encoding='utf-8') as f: f.write(s_new)
        print(f'OLDENBURG: fallback anchor "{fallback}" used')
        print(f'  WROTE OLDENBURG: {orig_len} -> {len(s_new)}')
    else:
        print('OLDENBURG: NO anchor found — manual review needed')

# ============================================================
# OSNABRÜCK (INSERT before "ablauf" section)
# ============================================================
OSNABRUECK_SOZIAL = '''<section class="mr-section" aria-labelledby="sozialbestattung">
    <h2 id="sozialbestattung">Sozialbestattung in Osnabrück</h2>
    <p>Wenn die Verpflichteten die Kosten einer Bestattung nicht aus eigenen Mitteln und nicht aus dem Nachlass der verstorbenen Person aufbringen können, übernimmt der Sozialhilfeträger nach <strong>§ 74 SGB XII</strong> die „erforderlichen Kosten der Bestattung". Anspruchsgrundlage ist nicht die wirtschaftliche Lage der verstorbenen Person, sondern die der bestattungspflichtigen Angehörigen. Die Bestattungspflicht selbst ergibt sich in Niedersachsen aus <strong>§ 8 Abs. 3 BestattG Niedersachsen</strong> und trifft in fester Reihenfolge Ehegatten oder Lebenspartner, volljährige Kinder, Eltern und weitere Verwandte. Der Anspruch nach § 74 SGB XII steht damit nur denjenigen zu, die tatsächlich zur Bestattung verpflichtet sind.</p>
    <h3>Zumutbarkeit — die zentrale Hürde</h3>
    <p>§ 74 SGB XII verlangt, dass den Verpflichteten die Übernahme der Bestattungskosten nicht zugemutet werden kann. Das Bundessozialgericht hat mit Urteil vom <strong>25. August 2011 (Az. B 8 SO 20/10 R)</strong> klargestellt, dass die Zumutbarkeitsprüfung an die jeweiligen Vermögens- und Einkommensverhältnisse anknüpft, nicht starr an die Sozialhilfegrenzen. Maßgeblich ist eine Gesamtbetrachtung der wirtschaftlichen Verhältnisse zum Zeitpunkt der Bestattung; auch Personen oberhalb der Sozialhilfeschwelle können anspruchsberechtigt sein, wenn die Kostenübernahme im Einzelfall unzumutbar wäre.</p>
    <h3>Zuständige Stelle in Osnabrück</h3>
    <p>Da Osnabrück kreisfreie Stadt ist, ist der städtische Fachbereich Soziales selbst Träger der Sozialhilfe. Anträge sind zu richten an:</p>
    <p><strong>Stadt Osnabrück — Fachbereich Soziales</strong><br>
    Stadthaus 2, Natruper-Tor-Wall 5, 49076 Osnabrück<br>
    Telefon: <a href="tel:+495413232500">0541 323-2500</a><br>
    E-Mail: über das <a href="https://www.osnabrueck.de/" rel="noopener" target="_blank">Serviceportal der Stadt Osnabrück</a></p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Übernommen werden die <em>erforderlichen</em> Kosten einer ortsüblichen, einfachen, aber würdigen Bestattung. Dazu zählen üblicherweise: einfacher Sarg bzw. Urne, Überführung im örtlichen Rahmen, Grabnutzungsgebühr für ein einfaches Reihengrab (Erd- oder Urnenreihengrab), Bestattungs- und Krematoriumsgebühr, Trauerhallennutzung im einfachen Rahmen sowie ein schlichtes Grabmal. <strong>Nicht übernommen</strong> werden in der Regel: Wahlgrabstätten, aufwendige Grabmale, Trauerfeiern mit gehobener Ausstattung, Traueranzeigen über das Notwendige hinaus, Trauerredner sowie Bewirtungskosten. Der Nachlass der verstorbenen Person ist vorrangig zur Kostendeckung einzusetzen.</p>
    <h3>Antragszeitpunkt</h3>
    <p>Der Antrag sollte <strong>möglichst vor</strong> der Beauftragung des Bestatters beim Fachbereich Soziales gestellt werden. Eine spätere Antragstellung ist zwar nicht ausgeschlossen, birgt aber das Risiko, dass nachträglich angefallene Kosten oberhalb des „erforderlichen" Rahmens nicht erstattet werden. Bestatter in Osnabrück kennen das Verfahren und beraten regelmäßig zu den entsprechenden Kostenrahmen einer „Sozialamtsbestattung". Die Antragsfrist nach § 74 SGB XII ist nicht ausdrücklich geregelt; nach gefestigter Rechtsprechung muss der Antrag aber zeitnah zur Bestattung gestellt werden.</p>
  </section>

'''

# Find the section before ablauf
fp = 'bestatter/osnabrueck/index.html'
with open(fp,'r',encoding='utf-8') as f: s = f.read()
orig_len = len(s)
osnabrueck_anchor = '<section class="mr-section" aria-labelledby="ablauf">'
n = s.count(osnabrueck_anchor)
print(f'OSNABRÜCK: anchor "<section ... ablauf>" matches = {n}')
if n == 1:
    s_new = s.replace(osnabrueck_anchor, OSNABRUECK_SOZIAL + osnabrueck_anchor)
    with open(fp,'w',encoding='utf-8') as f: f.write(s_new)
    print(f'  WROTE OSNABRÜCK: {orig_len} -> {len(s_new)}')
else:
    # Fallback: try other anchor patterns
    alt_anchors = [
        '<section class="mr-section" id="ablauf">',
        '<section id="ablauf"',
        '<h2 id="ablauf"',
    ]
    inserted = False
    for a in alt_anchors:
        if a in s and s.count(a) == 1:
            s_new = s.replace(a, OSNABRUECK_SOZIAL + a)
            with open(fp,'w',encoding='utf-8') as f: f.write(s_new)
            print(f'  WROTE OSNABRÜCK with fallback "{a}": {orig_len} -> {len(s_new)}')
            inserted = True
            break
    if not inserted:
        print('OSNABRÜCK: no usable anchor — manual review')

# ============================================================
# VERIFICATION
# ============================================================
print('\n=== VERIFICATION ===')
for city in ['braunschweig', 'oldenburg', 'osnabrueck']:
    fp = f'bestatter/{city}/index.html'
    with open(fp,'r',encoding='utf-8') as f: s = f.read()
    nul_ok = len(s.rstrip('\x00')) == len(s)
    has_sozial = 'Sozialbestattung in ' in s
    has_sgb = '§ 74 SGB XII' in s
    has_bsg = 'B 8 SO 20/10 R' in s
    has_nieder = '§ 8 Abs. 3 BestattG Niedersachsen' in s or '§ 8 Abs. 3 NBestattG' in s or '§ 8 Abs. 3 Niedersächsisches Bestattungsgesetz' in s
    sec_open = len(re.findall(r'<section\b', s))
    sec_close = len(re.findall(r'</section>', s))
    balanced = sec_open == sec_close
    print(f'{city}: len={len(s)}, NUL-ok={nul_ok}, Sozial={has_sozial}, §74={has_sgb}, BSG={has_bsg}, §8 Abs.3={has_nieder}, <section>={sec_open}/{sec_close} balanced={balanced}')
