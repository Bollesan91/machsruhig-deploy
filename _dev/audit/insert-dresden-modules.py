#!/usr/bin/env python3
"""Insert Bestatter-Wahl-Checkliste + Sozialbestattung in Dresden."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print('cwd:', os.getcwd())

fp = 'bestatter/dresden/index.html'
with open(fp, 'r', encoding='utf-8') as f:
    s = f.read()
orig = s

BESTATTER_CHECKLIST = '''    <h3>Qualitäts-Checkliste: Worauf Sie vor Auftragserteilung achten sollten</h3>
    <p>Stiftung Warentest und die <a href="https://www.verbraucherzentrale-sachsen.de/" rel="noopener" target="_blank">Verbraucherzentrale Sachsen</a> raten dazu, vor Unterschrift folgende Punkte schriftlich zu prüfen:</p>
    <ul style="list-style:disc;padding-left:24px;margin:12px 0 16px;font-size:15px;line-height:1.8">
      <li><strong>Schriftlicher Kostenvoranschlag</strong> — getrennt nach Bestatterleistung (Sarg/Urne, Transport, Versorgung, Trauerfeier), Fremdkosten (Friedhof, Standesamt, Krematorium), Trauerdruck und Grabstein. Pauschalpreise ohne Aufschlüsselung sind ein Warnzeichen.</li>
      <li><strong>Mindestens drei Vergleichsangebote</strong> bei identischer Leistungsbeschreibung — der Preisunterschied innerhalb Dresdens kann bei gleicher Leistung mehrere Tausend Euro betragen.</li>
      <li><strong>Mitgliedschaft im <a href="https://www.bestatter.de" rel="noopener" target="_blank">Bundesverband Deutscher Bestatter</a></strong> oder im <strong>Landesinnungsverband des Sächsischen Bestattungsgewerbes</strong> — sowie freiwillig das <strong>RAL-Gütezeichen Bestattungsinstitut</strong>. Beides garantiert nicht den günstigsten Preis, aber dokumentierte Mindeststandards bei Versorgung, Ausbildung und Qualitätssicherung.</li>
      <li><strong>Transparenz bei der Friedhofswahl</strong> — Bestatter sollten neutral über kirchliche (Trinitatis, Annenfriedhof, Innerer Neustädter, Johannisfriedhof Tolkewitz) und städtische Optionen (Heidefriedhof, Nordfriedhof, Dölzschen, Urnenhain Tolkewitz) informieren, nicht nur jene mit denen sie selbst gut vernetzt sind.</li>
      <li><strong>Kein Verkaufsdruck im ersten Gespräch</strong> — seriöse Anbieter räumen Bedenkzeit ein und drängen nicht zu sofortigen Vertragsabschlüssen oder „Komplettpaketen" am Sterbetag.</li>
      <li><strong>Klare Information zu Pflicht- vs. Wahlleistungen</strong> — hygienische Versorgung, Sarg und Überführung sind Pflicht; aufwendige Einbettung, Trauerfeier-Extras oder erweiterte Aufbahrung sind freie Wahl.</li>
      <li><strong>Schriftliche Vertragsausfertigung</strong> — mündliche Zusagen zu Kosten oder Leistungen sind ohne Schriftform nicht belastbar.</li>
    </ul>
    <p>Bei Beschwerden oder Streitfällen ist die Verbraucherzentrale Sachsen (Beratungsstelle Dresden, Fetscherplatz 3) erste Anlaufstelle. Die <strong>Handwerkskammer Dresden</strong> führt zudem die Ombudsstelle für Innungsbetriebe.</p>
'''

SOZIAL_DRESDEN = '''    <h3>Sozialbestattung — wenn die Kosten nicht aufgebracht werden können</h3>
    <p>Können Hinterbliebene die Bestattungskosten weder aus dem Nachlass noch aus eigenem Einkommen und Vermögen tragen, übernimmt das Sozialamt nach <strong><a href="https://www.gesetze-im-internet.de/sgb_12/__74.html" rel="noopener" target="_blank">§ 74 SGB XII</a></strong> auf Antrag die <em>erforderlichen Kosten einer einfachen, ortsüblichen Bestattung</em> — ganz oder teilweise. Der Anspruch besteht für jene Person(en), die zur Kostentragung verpflichtet sind und denen diese Tragung nicht zugemutet werden kann. Die Bestattungspflicht selbst regelt landesrechtlich <strong>§ 10 SächsBestG</strong>.</p>
    <p>Zuständig in Dresden ist das <strong>Sozialamt der Landeshauptstadt Dresden, Abteilung Soziale Leistungen, Junghansstraße 2, 01277 Dresden</strong> (Telefon 0351-4884861, E-Mail <a href="mailto:sozialleistungen@dresden.de">sozialleistungen@dresden.de</a>). Anträge sind formfrei möglich; empfohlen wird das offizielle Formular „Antrag auf Übernahme von Bestattungskosten" (Vdr. 50.537/2). Beizulegen sind u. a. Sterbeurkunde, Erbschein bzw. Nachweis der Erbausschlagung, Kontoauszüge der letzten drei Monate, Einkommens- und Vermögensnachweise sowie sämtliche Rechnungen (Bestatter, Friedhof, ggf. Krematorium).</p>
    <p>Wichtig: Die Wahl von Bestatter und Friedhof bleibt frei — das Sozialamt schreibt weder ein bestimmtes Bestattungsunternehmen noch eine bestimmte Bestattungsform vor. Übernommen werden jedoch nur „erforderliche" Kosten einer einfachen ortsüblichen Bestattung; aufwendige Wahlleistungen werden nicht erstattet. Nach gefestigter Rechtsprechung des <strong>Bundessozialgerichts</strong> (u. a. BSG, Urteil vom 25.08.2011, Az. B 8 SO 20/10 R) gehört zu den erforderlichen Kosten auch eine Grabstelle in würdevoller Ausführung — eine grundsätzlich anonyme Bestattung kann das Sozialamt nicht erzwingen, wenn der Bestattungspflichtige eine schlichte Reihengrab- oder Urnenbestattung wünscht. Der Antrag kann auch <em>nach</em> der Bestattung gestellt werden; eine starre Frist gibt es nicht, jedoch sollte die Antragstellung zeitnah erfolgen.</p>
    <p>Sind keine bestattungspflichtigen Angehörigen ermittelbar oder kommen diese ihrer Pflicht trotz Aufforderung nicht nach, veranlasst gemäß <strong>§ 10 Abs. 3 SächsBestG</strong> die Ortspolizeibehörde — in Dresden das <strong>Ordnungsamt der Landeshauptstadt Dresden, Abteilung Sicherheitsangelegenheiten</strong> — die Bestattung ersatzweise auf Kosten der Bestattungspflichtigen. Diese sogenannte ordnungsbehördliche Bestattung ist von der Sozialbestattung nach § 74 SGB XII zu unterscheiden.</p>
'''

# Insert 1: Bestatter-Checkliste — as additional H3 inside existing Bestatter-Section, before closing </div>
# Anchor: "Bestattung in Chemnitz</a>.</p>\n  </div>"
anchor1 = '<a href="/bestatter/chemnitz/">Bestattung in Chemnitz</a>.</p>\n  </div>'
replace1 = '<a href="/bestatter/chemnitz/">Bestattung in Chemnitz</a>.</p>\n' + BESTATTER_CHECKLIST + '  </div>'
n1 = s.count(anchor1)
print(f'Anchor 1 (Bestatter-Checkliste): {n1}')
if n1 == 1:
    s = s.replace(anchor1, replace1)
    print('  CHECKLIST inserted')

# Insert 2: Sozialbestattung — after "Bestattungskosten</a>.</p>", before closing </div> of cost section
# Anchor: end of Stiftung Warentest paragraph
anchor2 = 'Eine ausführliche Darstellung der Kostenstruktur: <a href="/bestattungskosten">Bestattungskosten</a>.</p>\n  </div>'
replace2 = 'Eine ausführliche Darstellung der Kostenstruktur: <a href="/bestattungskosten">Bestattungskosten</a>.</p>\n' + SOZIAL_DRESDEN + '  </div>'
n2 = s.count(anchor2)
print(f'Anchor 2 (Sozialbestattung): {n2}')
if n2 == 1:
    s = s.replace(anchor2, replace2)
    print('  SOZIAL inserted')

if s != orig:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(s)
    print(f'\nWROTE: {len(orig)} -> {len(s)} bytes (+{len(s)-len(orig)})')
else:
    print('\nNO CHANGES (anchors did not match)')
