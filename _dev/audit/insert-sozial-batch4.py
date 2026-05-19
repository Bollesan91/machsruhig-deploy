#!/usr/bin/env python3
"""Batch 4 BW-Trio Sozialbestattung: Karlsruhe + Freiburg + Stuttgart.
NOTE: § 21 BestattG BW used (konsistent zu deployed Heidelberg/Mannheim).
"""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# ============================================================
# KARLSRUHE (Stadtkreis BW)
# ============================================================
KARLSRUHE_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Karlsruhe — wenn die Kosten nicht aufgebracht werden können</h2>
    <p>Wenn Bestattungspflichtige die Kosten einer Bestattung nicht aus eigenem Einkommen, Vermögen oder dem Nachlass tragen können, übernimmt das Sozialamt nach <strong>§ 74 SGB XII</strong> die erforderlichen Kosten — soweit dies den Verpflichteten nicht zugemutet werden kann. Wer zur Tragung verpflichtet ist, ergibt sich in Karlsruhe primär aus der Reihenfolge der Bestattungspflichtigen nach <strong>§ 21 BestattG BW</strong> (Ehegatte/Lebenspartner, volljährige Kinder, Eltern, Großeltern, Geschwister, Enkel). Wichtig: Auch wer nach Landesrecht bestattungspflichtig ist, hat einen Anspruch auf Übernahme — das hat das Bundessozialgericht im Urteil <strong>B 8 SO 20/10 R vom 25. August 2011</strong> ausdrücklich bestätigt. Eine sittliche oder vertragliche Verpflichtung allein reicht hingegen nicht.</p>
    <h3>Zuständige Stelle in Karlsruhe</h3>
    <p>Karlsruhe ist Stadtkreis und führt das Sozialamt in eigener Zuständigkeit. Erstkontakt ist die Anlauf- und Vermittlungsstelle der <strong>Sozial- und Jugendbehörde (SJB) der Stadt Karlsruhe</strong> im Rathaus an der Alb:</p>
    <p><strong>Sozial- und Jugendbehörde der Stadt Karlsruhe</strong><br>
    Rathaus an der Alb, Ernst-Frey-Straße 10, 76135 Karlsruhe<br>
    Anlauf- und Vermittlungsstelle: <a href="tel:+497211335415">0721 133-5415</a><br>
    E-Mail: <a href="mailto:infotheke@sjb.karlsruhe.de">infotheke@sjb.karlsruhe.de</a><br>
    Großempfängerpostfach: 76124 Karlsruhe</p>
    <p>Hatte die verstorbene Person bereits Sozialhilfe bezogen, ist das Sozialamt zuständig, das diese Leistung bis zum Tod gezahlt hat. Hatte sie keine Sozialhilfe bezogen, ist das Sozialamt des Sterbeortes zuständig — bei einem Sterbefall in Karlsruhe also die SJB.</p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Übernommen werden die Kosten einer <strong>ortsüblich einfachen, aber würdigen Bestattung</strong>. Dazu gehören Sarg oder Urne, einfache Ausstattung, Leichenhaus, Überführung im Stadtgebiet, die Grabnutzungs- und Bestattungsgebühren nach Karlsruher Satzung sowie das Herrichten des Grabes. <strong>Nicht übernommen</strong> werden in der Regel Trauerdruck und Trauerfeier in größerem Rahmen, Blumenschmuck über das Notwendige hinaus, Grabmal und Grabeinfassung, laufende Grabpflege sowie Trauerkleidung. Vorhandener Nachlass und Sterbegeldversicherungen werden vorrangig eingesetzt.</p>
    <h3>Antragszeitpunkt — möglichst vor Auftragserteilung</h3>
    <p>Der Antrag auf Übernahme der Bestattungskosten ist <strong>schriftlich</strong> bei der SJB zu stellen — am besten <strong>vor</strong> der Beauftragung des Bestatters, damit Umfang und Höhe der angemessenen Kosten abgestimmt sind. Eine spätere Antragstellung ist möglich, solange die Kosten noch nicht aus eigenem Vermögen beglichen wurden; die Kostentragungspflicht muss aber im Zeitpunkt der Bestattung bereits feststehen. Gegen den Bescheid kann innerhalb eines Monats Widerspruch eingelegt werden.</p>
  </div>

'''

# ============================================================
# FREIBURG (Stadtkreis BW)
# ============================================================
FREIBURG_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Freiburg — wenn die Kosten nicht getragen werden können</h2>
    <p>Reichen Nachlass und eigenes Einkommen der bestattungspflichtigen Angehörigen nicht aus, um die Bestattung zu finanzieren, übernimmt das Sozialamt nach <strong>§ 74 SGB XII</strong> die <em>erforderlichen</em> Kosten der Bestattung. Voraussetzung ist, dass den Verpflichteten nicht zugemutet werden kann, die Kosten selbst zu tragen — geprüft wird also die wirtschaftliche Lage der Bestattungspflichtigen, nicht die der verstorbenen Person. Wer bestattungspflichtig ist, richtet sich in Baden-Württemberg nach <strong>§ 21 BestattG BW</strong>: zuerst Ehegatte oder eingetragene/r Lebenspartner_in, dann volljährige Kinder, Eltern, Großeltern, volljährige Geschwister, Enkel. Diese Reihenfolge gilt strikt — wer in der Rangfolge vorne steht und leistungsfähig ist, trägt die Kosten zuerst.</p>
    <h3>Zuständige Stelle in Freiburg</h3>
    <p>Freiburg im Breisgau ist Stadtkreis; zuständig ist daher die Stadt selbst — nicht der umliegende Landkreis Breisgau-Hochschwarzwald. Antragsstelle ist das <strong>Amt für Soziales (AfS) der Stadt Freiburg</strong>, Abteilung <em>Existenzsichernde Leistungen und Hilfe zur Pflege</em>:</p>
    <p><strong>Amt für Soziales (AfS) — Stadt Freiburg im Breisgau</strong><br>
    Fehrenbachallee 12, Gebäude C, 79106 Freiburg (Rathaus im Stühlinger)<br>
    Telefon Empfang: <a href="tel:+497612013507">0761 201-3507</a> · Sachgebietsleitung Existenzsichernde Leistungen: <a href="tel:+497612013620">0761 201-3620</a><br>
    E-Mail: <a href="mailto:AfS@freiburg.de">AfS@freiburg.de</a></p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Übernommen werden nur die <strong>ortsüblichen, einfachen und würdigen</strong> Kosten einer Bestattung: einfacher Sarg oder Urne, Transport, einfache Trauerfeier, Grabnutzungsgebühr für ein Reihengrab (in Freiburg z. B. Erdreihengrab Erwachsene 346 € oder Urnenreihengrab 244 € nach Gebührenverzeichnis vom 19.3.2024), einfache Grabherstellung und eine schlichte Grabkennzeichnung. <strong>Nicht übernommen</strong> werden Wahlgräber mit erweiterten Nutzungsrechten, aufwendige Grabmale, Trauerdrucke über das Notwendige hinaus, Trauerkaffee oder Blumenschmuck in größerem Umfang. Maßstab ist das Urteil des <strong>Bundessozialgerichts vom 25.08.2011 (Az. B 8 SO 20/10 R)</strong>: Erforderlich ist, was eine sozialhilferechtlich angemessene, ortsübliche und würdige Bestattung kostet — nicht die billigste denkbare, aber auch nicht das, was die Angehörigen sich wünschen würden.</p>
    <h3>Antragszeitpunkt — möglichst vor Auftragserteilung</h3>
    <p>Der Antrag kann sowohl <strong>vor</strong> als auch <strong>nach</strong> der Bestattung gestellt werden. Die Stadt Freiburg empfiehlt ausdrücklich, sich <strong>vor</strong> Beauftragung eines Bestatters mit dem Amt für Soziales abzustimmen, damit das Amt vorab beurteilen kann, welche Leistungen erstattungsfähig sind. Wird der Antrag erst nach der Bestattung gestellt, müssen die Originalrechnung des Bestattungsinstituts, der Nachweis der Beziehung zur verstorbenen Person sowie Unterlagen zu Einkommen und Vermögen der antragstellenden Person und Angaben zum Nachlass eingereicht werden. Vorhandene Sterbegeldversicherungen oder Bestattungsvorsorgeverträge sind anzugeben — sie werden vorrangig eingesetzt.</p>
  </div>

'''

# ============================================================
# STUTTGART (Landeshauptstadt BW)
# ============================================================
STUTTGART_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Stuttgart — wenn die Kosten nicht tragbar sind</h2>
    <p>Reicht das Einkommen oder Vermögen der bestattungspflichtigen Angehörigen nicht aus, um die Bestattung zu finanzieren, übernimmt der Sozialhilfeträger nach <strong><a href="https://www.gesetze-im-internet.de/sgb_12/__74.html" rel="noopener" target="_blank">§ 74 SGB XII</a></strong> die <em>erforderlichen Kosten</em> einer einfachen, aber würdigen Bestattung. Die Norm verlangt, dass dem Verpflichteten die Kostentragung „nicht zugemutet werden kann" — geprüft wird die wirtschaftliche Leistungsfähigkeit des Antragstellers, nicht der Sozialhilfebezug der verstorbenen Person. Wer zu den Bestattungspflichtigen zählt, ergibt sich in Baden-Württemberg aus <strong>§ 21 BestattG BW</strong>: Ehegatten oder eingetragene Lebenspartner, volljährige Kinder, Eltern, Großeltern, volljährige Geschwister und Enkelkinder — in dieser Rangfolge, unabhängig vom Erbrecht.</p>
    <h3>Zuständige Stelle in Stuttgart</h3>
    <p>Träger der Sozialhilfe ist das <strong>Sozialamt der Landeshauptstadt Stuttgart</strong>, Eberhardstraße 33, 70173 Stuttgart, Telefon <a href="tel:+4971121659000">0711 216-59000</a>. Die Antragsannahme erfolgt nicht zentral, sondern dezentral durch den <strong>Bürgerservice Soziale Leistungen</strong> in den Bezirksämtern beziehungsweise in der Innenstadt — zuständig ist die Dienststelle, die bis zum Tod für die verstorbene Person SGB-XII-Leistungen erbracht hat. War die verstorbene Person nicht im Sozialhilfebezug, richtet sich die Zuständigkeit nach dem Wohnsitz der antragstellenden Person.</p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p>Erstattet werden die ortsüblichen Aufwendungen für eine einfache Bestattung: schlichter Sarg oder Urne, Friedhofs- und Bestattungsgebühren, Krematoriumsgebühr im Pragfriedhof, Überführung im Stadtgebiet, einfache Trauerfeier, Zweitschriften der Sterbeurkunde. Die Stuttgarter Friedhofsgebühren (Reihengrab Erd 940 €, Bestattungsgebühr 1.010 €, Einäscherung 605 €) fallen in der Regel unter das Erforderliche. <strong>Nicht übernommen</strong> werden Wahlgrabaufschläge, Grabsteine, dauerhafte Grabpflege, aufwendige Floristik, Trauerredner über Standardumfang hinaus, Traueranzeigen sowie Bewirtungskosten. Der Anspruch besteht nach dem Grundsatzurteil des Bundessozialgerichts vom <strong>25. August 2011 (Az. B 8 SO 20/10 R)</strong> unabhängig davon, ob die Erbschaft ausgeschlagen wurde — entscheidend ist allein die zivil- oder öffentlich-rechtliche Bestattungspflicht. Ein etwaiger Nachlass und eine vorhandene Sterbegeldversicherung werden vorab angerechnet.</p>
    <h3>Antragszeitpunkt</h3>
    <p>Der Antrag sollte <strong>möglichst vor Auftragsvergabe an den Bestatter</strong> gestellt werden, spätestens aber zeitnah nach der Bestattung — die Landeshauptstadt Stuttgart nennt als Richtwert <strong>zwei Monate</strong>. Der Bestatter muss zwingend vorab über den geplanten Antrag informiert werden, damit das Leistungsverzeichnis auf das Erforderliche begrenzt wird; ein nachträglich „aufgehübschter" Auftrag wird in der Differenz nicht erstattet. Erforderliche Belege: Nachweis der Bestattungspflicht (Verwandtschaft, Testament), vollständige Bestatter- und Friedhofsrechnungen, Nachlassaufstellung inklusive Sterbegeldversicherungen und Vorsorgeverträgen, Einkommens- und Vermögensnachweise der antragstellenden Person samt Ehepartner. Eine kompakte Aufgaben-Übersicht für die ersten Tage bietet die <a href="/tools/checkliste-todesfall">Checkliste Todesfall</a>.</p>
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

# Karlsruhe — insert BEFORE Was-tun section
karlsruhe_anchor = '  <div class="mr-section">\n    <h2>Was nach einem Todesfall in Karlsruhe zu tun ist</h2>'
do_insert('bestatter/karlsruhe/index.html', karlsruhe_anchor, KARLSRUHE_SOZIAL, 'KARLSRUHE')

# Freiburg — insert BEFORE Bestatter-Wahl section
freiburg_anchor = '  <div class="mr-section">\n    <h2>Bestatter-Wahl in Freiburg</h2>'
# Fallback if anchor not found, try alternatives
freiburg_html_path = 'bestatter/freiburg/index.html'
with open(freiburg_html_path, 'r', encoding='utf-8') as f: fbg_html = f.read()
if freiburg_anchor not in fbg_html:
    # try alternative
    alt1 = '  <div class="mr-section">\n    <h2>Bestatter in Freiburg'
    if alt1 in fbg_html:
        # find the rest of the H2 line
        m = re.search(r'(  <div class="mr-section">\n    <h2>Bestatter[^<]*</h2>)', fbg_html)
        if m:
            freiburg_anchor = m.group(1)
            print(f'FREIBURG fallback anchor: {freiburg_anchor[:80]}...')
do_insert(freiburg_html_path, freiburg_anchor, FREIBURG_SOZIAL, 'FREIBURG')

# Stuttgart — insert BEFORE Was-tun section
stuttgart_anchor = '  <div class="mr-section">\n    <h2>Was nach einem Todesfall in Stuttgart zu tun ist</h2>'
do_insert('bestatter/stuttgart/index.html', stuttgart_anchor, STUTTGART_SOZIAL, 'STUTTGART')

# ============================================================
# VERIFICATION
# ============================================================
print('\n=== VERIFICATION ===')
for city in ['karlsruhe', 'freiburg', 'stuttgart']:
    fp = f'bestatter/{city}/index.html'
    with open(fp, 'r', encoding='utf-8') as f:
        s = f.read()
    nul_ok = len(s.rstrip('\x00')) == len(s)
    has_sozial = ('Sozialbestattung in ' in s)
    has_sgb = '§ 74 SGB XII' in s
    has_bsg = 'B 8 SO 20/10 R' in s
    has_bw = '§ 21 BestattG BW' in s
    sec_open = len(re.findall(r'<section\b', s))
    sec_close = len(re.findall(r'</section>', s))
    tag_balanced = (sec_open == sec_close)
    print(f'{city}: len={len(s)}, NUL-ok={nul_ok}, Sozial={has_sozial}, §74={has_sgb}, BSG={has_bsg}, §21 BW={has_bw}, <section>={sec_open}/{sec_close} balanced={tag_balanced}')
