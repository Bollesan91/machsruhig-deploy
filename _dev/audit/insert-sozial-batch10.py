#!/usr/bin/env python3
"""FINAL Batch 10 Sozialbestattung: Münster (NRW) + Rostock (MV) + Kiel (SH)."""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

MUENSTER_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Münster — wenn die Kosten nicht selbst getragen werden können</h2>
    <p>Reicht der Nachlass nicht aus und sind auch die bestattungspflichtigen Angehörigen finanziell nicht in der Lage, die Kosten zu tragen, übernimmt das <strong>Sozialamt der Stadt Münster</strong> nach <strong>§ 74 SGB XII</strong> die <em>erforderlichen</em> Bestattungskosten — also den ortsüblich angemessenen Rahmen einer einfachen, würdigen Bestattung. Die Stadt Münster hat dazu mit den örtlichen Bestattungsunternehmen pauschale Beträge für ein angemessenes ortsübliches Begräbnis vereinbart, sodass im Regelfall kein Eigenanteil anfällt, wenn die Voraussetzungen erfüllt sind. Wichtig: <strong>Den Antrag möglichst vor Beauftragung des Bestatters stellen</strong>, spätestens jedoch zeitnah nach der Bestattung.</p>
    <h3>Wer ist antragsberechtigt?</h3>
    <p>Antragsberechtigt ist die Person, die nach <strong>§ 8 Abs. 1 Satz 2 BestG NRW</strong> zur Bestattung verpflichtet ist — in der gesetzlichen Rangfolge Ehegatten, Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern und volljährige Enkelkinder. Vorrangig haften jedoch zivilrechtlich die Erben (§ 1968 BGB) und Unterhaltspflichtige; das Sozialamt prüft, ob aus dem Nachlass oder von vorrangig Verpflichteten Mittel verfügbar sind. Die örtliche Zuständigkeit richtet sich nach § 98 Abs. 3 SGB XII: bei laufendem Sozialhilfebezug der verstorbenen Person der bisherige Träger, sonst der Sterbeortträger.</p>
    <h3>Höchstrichterliche Klärung: Erbausschlagung schließt Anspruch nicht aus</h3>
    <p>Das <strong>Bundessozialgericht</strong> hat mit Urteil vom <strong>25.08.2011 (Az. B 8 SO 20/10 R)</strong> entschieden, dass die Verpflichtung zur Tragung der Bestattungskosten nicht zwingend an die Erbenstellung anknüpft. Auch wer das Erbe ausgeschlagen hat, aber landesrechtlich bestattungspflichtig bleibt, kann unter den Voraussetzungen des § 74 SGB XII einen Anspruch auf Kostenübernahme haben — die Zumutbarkeit der Eigenfinanzierung ist gesondert zu prüfen. Eine pauschale Ablehnung wegen Erbausschlagung ist damit nicht zulässig.</p>
    <h3>Ansprechpartner Sozialamt Münster (SG 56)</h3>
    <p><strong>Stadt Münster — Sozialamt, Sachgebiet 56 (Bestattungskosten)</strong><br>
    Hafenstraße 8, 48153 Münster<br>
    Telefon: <a href="tel:+492514925016">0251 492-5016</a><br>
    E-Mail: <a href="mailto:sozialamt-sg56@stadt-muenster.de">sozialamt-sg56@stadt-muenster.de</a></p>
  </div>

'''

ROSTOCK_SOZIAL = '''<section class="mr-section" id="sozialbestattung">
    <h2>Sozialbestattung in Rostock: Wenn die Kosten nicht zu tragen sind</h2>
    <p>Eine Bestattung kostet in Rostock je nach Bestattungsart und Grabwahl mehrere tausend Euro. Wer als Bestattungspflichtiger diese Kosten nicht aus eigenen Mitteln aufbringen kann, hat unter den Voraussetzungen des <strong>§ 74 SGB XII</strong> einen Anspruch auf Übernahme der „erforderlichen Kosten" durch den Sozialhilfeträger. Zuständig in der Hansestadt Rostock ist das Amt für Soziales und Teilhabe, Abteilung Sozialhilfe. Wichtig: Der Antrag sollte möglichst vor Auftragserteilung an das Bestattungsunternehmen gestellt werden — das verhindert spätere Streitfälle über die Erforderlichkeit einzelner Leistungspositionen.</p>
    <h3>Wer ist bestattungspflichtig — und wer kostenpflichtig?</h3>
    <p><strong>§ 9 Abs. 2 BestattG M-V</strong> legt die öffentlich-rechtliche Bestattungspflicht der volljährigen Angehörigen in folgender Reihenfolge fest: 1. Ehegatte, 2. Lebenspartner, 3. Kinder, 4. Eltern, 5. Geschwister, 6. Großeltern, 7. Enkelkinder, 8. sonstiger Partner einer auf Dauer angelegten nichtehelichen Lebensgemeinschaft. Diese ordnungsrechtliche Pflicht — die Bestattung zu veranlassen — ist von der zivilrechtlichen Kostentragungspflicht (§ 1968 BGB für Erben, § 74 SGB XII für Hilfebedürftige) zu unterscheiden. Sind keine Bestattungspflichtigen vorhanden oder kommen sie ihrer Pflicht nicht nach, sorgt nach § 9 Abs. 3 BestattG M-V die örtliche Ordnungsbehörde am letzten Hauptwohnsitz ersatzweise für die Bestattung.</p>
    <h3>Umfang der Kostenübernahme nach § 74 SGB XII</h3>
    <p>Das Bundessozialgericht hat in seiner Entscheidung vom <strong>25.08.2011 (Az. B 8 SO 20/10 R)</strong> den unbestimmten Rechtsbegriff der „erforderlichen Kosten" konkretisiert: Übernahmefähig ist eine einfache, ortsübliche und würdige Bestattung. Nicht erforderlich sind in der Regel aufwendige Trauerfeiern, repräsentative Grabmale oder Wahlgrabstätten, wenn ein Reihengrab ausreichend wäre. Eigenes Einkommen und Vermögen des Bestattungspflichtigen sowie der Nachlass des Verstorbenen sind vorrangig einzusetzen. Lebensversicherungen, Sterbegeldversicherungen und Vermögen aus dem Nachlass mindern den Anspruch entsprechend.</p>
    <h3>Antrag und Kontakt in Rostock</h3>
    <p>Zuständig ist die <strong>Hanse- und Universitätsstadt Rostock, Amt für Soziales und Teilhabe, Abteilung Sozialhilfe</strong>:</p>
    <p>St.-Georg-Straße 109, Haus II, 18055 Rostock<br>
    Telefon: <a href="tel:+493813812520">0381 381-2520</a><br>
    E-Mail: <a href="mailto:sozialamt@rostock.de">sozialamt@rostock.de</a></p>
    <p>Beizubringen sind in der Regel Sterbeurkunde, Kostenvoranschlag des Bestatters, Nachweise über Einkommen und Vermögen aller Bestattungspflichtigen, Nachlassaufstellung sowie ein Nachweis der Verwandtschaft. Die Frist zur Antragstellung ist nicht im Gesetz geregelt; die Rechtsprechung lässt aber regelmäßig nur Anträge zu, die in zeitlichem Zusammenhang mit dem Todesfall gestellt werden.</p>
  </section>

'''

KIEL_SOZIAL = '''<section class="mr-section">
    <h2>Sozialbestattung in Kiel: Hilfe nach § 74 SGB XII</h2>
    <p>Wenn Bestattungspflichtige die Kosten einer Bestattung finanziell nicht tragen können, übernimmt der Sozialhilfeträger nach <strong>§ 74 SGB XII</strong> die <em>erforderlichen</em> Bestattungskosten — soweit den Verpflichteten die Kostentragung nicht zugemutet werden kann. Bestattungspflichtig in Kiel sind nach <strong>§ 13 Abs. 2 BestattG SH</strong> in Verbindung mit § 2 Nr. 12 BestattG SH die volljährigen Hinterbliebenen in folgender Reihenfolge: Ehegattin oder Ehegatte, eingetragene Lebenspartnerin oder Lebenspartner, leibliche und adoptierte Kinder, Eltern, Geschwister, Großeltern und Enkelkinder.</p>
    <p>Die Kostentragung ist insbesondere dann unzumutbar, wenn der oder die Bestattungspflichtige selbst Bürgergeld, Grundsicherung im Alter oder Hilfe zum Lebensunterhalt nach SGB XII bezieht — bei laufendem Sozialleistungsbezug ist nach gefestigter höchstrichterlicher Rechtsprechung regelmäßig von Unzumutbarkeit auszugehen. Auch oberhalb der Einkommensgrenze des § 85 SGB XII ist eine Übernahme möglich, wenn die wirtschaftlichen Verhältnisse zum Zeitpunkt der Fälligkeit der Bestattungsrechnungen dies nahelegen. Das Bundessozialgericht hat in seinem Urteil vom <strong>25.08.2011 (Az. B 8 SO 20/10 R)</strong> klargestellt, dass der Sozialhilfeträger die Erforderlichkeit der Bestattungskosten nicht allein anhand pauschal begrenzender Vergütungssätze bestimmen darf, wenn die tatsächlichen Kosten höher sind — Maßstab sind eine einfache, würdige und ortsübliche Bestattung.</p>
    <h3>Zuständige Stelle in Kiel</h3>
    <p>Für die Übernahme der Bestattungskosten ist in der Landeshauptstadt Kiel das <strong>Amt für Wohnen und Grundsicherung, Bereich Hilfe zum Lebensunterhalt (nach dem SGB XII) und Bestattungskosten</strong> zuständig:</p>
    <p>Deliusstraße 2, 24114 Kiel<br>
    Telefon: <a href="tel:+49431115">+49 431 115</a> (einheitliche Behördennummer)<br>
    E-Mail: <a href="mailto:Grundsicherung@kiel.de">Grundsicherung@kiel.de</a></p>
    <p>Der Antrag kann formlos schriftlich oder über die zuständigen Sozialzentren der Stadt gestellt werden. Es gibt keine gesetzliche Antragsfrist; der Antrag sollte aber zeitnah nach Fälligkeit der Bestattungsrechnungen erfolgen, da für die Zumutbarkeitsprüfung die Einkommens- und Vermögensverhältnisse zum Fälligkeitszeitpunkt maßgeblich sind. Übernommen werden die unmittelbaren Bestattungskosten (z. B. einfacher Sarg oder Urne, Friedhofs- und Krematoriumsgebühren, Anlage der Grabstätte). Nicht übernommen werden Folgekosten wie Bewirtung von Trauergästen oder Grabstein.</p>
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

# Münster — anchor before mr-faq
muenster_anchor = '<div class="mr-faq">'
ok = do_insert('bestatter/muenster/index.html', muenster_anchor, MUENSTER_SOZIAL, 'MUENSTER')
if not ok:
    with open('bestatter/muenster/index.html','r',encoding='utf-8') as f: s = f.read()
    for a in ['  <div class="mr-faq">', '<h2>Häufige Fragen', '<section class="mr-faq']:
        if a in s and s.count(a) == 1:
            do_insert('bestatter/muenster/index.html', a, MUENSTER_SOZIAL, f'MUENSTER ({a[:40]})')
            break

# Rostock — anchor before todesfall section
rostock_anchor = '<section class="mr-section" id="todesfall">'
ok = do_insert('bestatter/rostock/index.html', rostock_anchor, ROSTOCK_SOZIAL, 'ROSTOCK')
if not ok:
    with open('bestatter/rostock/index.html','r',encoding='utf-8') as f: s = f.read()
    for a in ['<h2 id="todesfall"', '<h2>Was nach einem Todesfall in Rostock']:
        if a in s and s.count(a) == 1:
            do_insert('bestatter/rostock/index.html', a, ROSTOCK_SOZIAL, f'ROSTOCK ({a[:40]})')
            break

# Kiel — anchor before Seebestattung-Section
kiel_anchor = '<h2>Seebestattung in der Kieler Förde</h2>'
ok = do_insert('bestatter/kiel/index.html', kiel_anchor, KIEL_SOZIAL, 'KIEL')
if not ok:
    with open('bestatter/kiel/index.html','r',encoding='utf-8') as f: s = f.read()
    for a in ['<section class="mr-section">\n    <h2>Seebestattung', '<h2>Seebestattung']:
        if a in s and s.count(a) == 1:
            do_insert('bestatter/kiel/index.html', a, KIEL_SOZIAL, f'KIEL ({a[:40]})')
            break

# dateModified
print('\n=== dateModified UPDATE ===')
for city in ['muenster','rostock','kiel']:
    fp = f'bestatter/{city}/index.html'
    with open(fp,'r',encoding='utf-8') as f: s = f.read()
    orig = s
    s = re.sub(r'"dateModified":\s*"\d{4}-\d{2}-\d{2}"', '"dateModified": "2026-05-19"', s)
    if s != orig:
        with open(fp,'w',encoding='utf-8') as f: f.write(s)

print('\n=== VERIFICATION ===')
for city in ['muenster', 'rostock', 'kiel']:
    fp = f'bestatter/{city}/index.html'
    with open(fp,'r',encoding='utf-8') as f: s = f.read()
    has_sozial = 'Sozialbestattung in ' in s
    has_sgb = '§ 74 SGB XII' in s
    has_bsg = 'B 8 SO 20/10 R' in s
    sec_o = len(re.findall(r'<section\b', s))
    sec_c = len(re.findall(r'</section>', s))
    print(f'{city}: Sozial={has_sozial}, §74={has_sgb}, BSG={has_bsg}, <section>={sec_o}/{sec_c}')
