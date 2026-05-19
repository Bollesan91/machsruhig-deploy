#!/usr/bin/env python3
"""Insert Sozialbestattung in Hannover."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

SOZIAL_HAN = '''
  <div class="mr-section">
    <h2>Sozialbestattung in Hannover — wenn die Kosten nicht tragbar sind</h2>
    <p>Wenn Erben oder Bestattungspflichtige die Kosten einer Bestattung nicht aus eigenen Mitteln aufbringen können, übernimmt der Sozialhilfeträger nach <strong>§ 74 SGB XII</strong> die „erforderlichen Kosten" einer einfachen, ortsüblichen Bestattung. Der Anspruch besteht nicht in Form einer Pauschale, sondern als Einzelfallprüfung — Maßstab ist nach Rechtsprechung des Bundessozialgerichts (BSG, Urteil vom 25.08.2011 — <strong>B 8 SO 20/10 R</strong>) eine würdige, ortsübliche Bestattung, orientiert an den Verhältnissen unterer und mittlerer Einkommensbezieher. Luxusleistungen, Bewirtung der Trauergäste und repräsentative Grabsteine sind nicht erstattungsfähig.</p>
    <h3>Wer ist antragsberechtigt? Reihenfolge nach § 8 Abs. 3 BestattG Niedersachsen</h3>
    <p>Anspruchsberechtigt ist ausschließlich, wer <strong>bestattungspflichtig</strong> ist — Nachbarn oder Freunde, die sich freiwillig um die Bestattung kümmern, erhalten keine Erstattung. Die Bestattungspflicht ergibt sich aus <strong>§ 8 Abs. 3 Niedersächsisches Bestattungsgesetz (BestattG)</strong> in folgender Rangfolge: (1) Ehegattin/Ehegatte oder eingetragene Lebenspartnerin/Lebenspartner, (2) volljährige Kinder, (3) Eltern, (4) volljährige Geschwister, (5) Großeltern, (6) volljährige Enkelkinder. Innerhalb derselben Rangstufe entscheidet die enge Beziehung zur verstorbenen Person.</p>
    <h3>Zuständige Stelle in Hannover</h3>
    <p>Für Verstorbene mit letztem Wohnsitz in der Landeshauptstadt Hannover ist der <strong>Fachbereich Soziales der Landeshauptstadt Hannover</strong> zuständig — die Stadt Hannover bearbeitet ihre Anträge selbstständig, abweichend von der sonstigen Zuständigkeit der Region Hannover für das Umland.</p>
    <p><strong>Fachbereich Soziales der Landeshauptstadt Hannover</strong><br>
    Hamburger Allee 25, 30161 Hannover<br>
    Telefon: 0511 168-45757<br>
    Den Antrag „Übernahme von Bestattungskosten gemäß § 74 SGB XII" stellt die Stadt online und als PDF auf <a href="https://hannover.gov.de/buergerservice/dienstleistungen/bestattungskosten-uebernahme-900000215-0.html" rel="noopener" target="_blank">hannover.gov.de</a> bereit.</p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p><strong>Übernommen werden</strong> regelmäßig: einfacher Sarg oder Urne, Überführung im Stadtgebiet, hygienische Versorgung, einfache Trauerfeier, Friedhofsgebühren für ein Reihen- oder Urnenreihengrab nach Satzung der Stadt Hannover, Erstanlage des Grabes, Sterbeurkunden und Traueranzeige in einfacher Form.</p>
    <p><strong>Nicht übernommen werden</strong>: Wahlgrab, repräsentativer Grabstein, Trauerredner über Standardumfang hinaus, Bewirtung von Trauergästen, Blumenschmuck über die Sargdekoration hinaus, Überführungen ins Ausland sowie alle Leistungen, die über das Maß einer „einfachen, ortsüblichen Bestattung" hinausgehen.</p>
    <h3>Antragszeitpunkt — möglichst vor Auftragsvergabe</h3>
    <p>Der Antrag sollte <strong>vor der Beauftragung des Bestatters</strong> oder unmittelbar danach gestellt werden. Praktisch: Bei Beauftragung des Bestattungsunternehmens schriftlich darauf hinweisen, dass ein Antrag nach § 74 SGB XII gestellt wird oder bereits gestellt wurde. Nicht anerkannte Kosten — etwa über das Niveau einer einfachen Bestattung hinausgehende Posten — trägt sonst die antragstellende Person selbst. Die <strong>8-Tage-Frist nach § 9 BestattG Niedersachsen</strong> für die Bestattung läuft unabhängig vom Antragsverfahren weiter.</p>
    <div class="mr-hint">
      <strong>Hinweis:</strong> Eine Erbausschlagung befreit <strong>nicht automatisch</strong> von der Bestattungspflicht nach § 8 Abs. 3 BestattG Niedersachsen — die öffentlich-rechtliche Pflicht besteht unabhängig von der erbrechtlichen Stellung fort. Bestattungspflichtige können dennoch einen Antrag nach § 74 SGB XII stellen, wenn die Kostenübernahme finanziell unzumutbar ist.
    </div>
  </div>

'''

fp = 'bestatter/hannover/index.html'
with open(fp, 'r', encoding='utf-8') as f: s = f.read()
orig = s
anchor = 'durchgereichten Friedhofsgebühren und Honorare Dritter (Pfarrer, Trauerredner, Floristik).</p>\n  </div>\n\n  <div class="mr-section">\n    <h2>Was nach einem Todesfall in Hannover zu tun ist</h2>'
replace = 'durchgereichten Friedhofsgebühren und Honorare Dritter (Pfarrer, Trauerredner, Floristik).</p>\n  </div>\n' + SOZIAL_HAN + '  <div class="mr-section">\n    <h2>Was nach einem Todesfall in Hannover zu tun ist</h2>'
n = s.count(anchor)
print(f'Hannover anchor: {n}')
if n == 1:
    s = s.replace(anchor, replace)
    with open(fp, 'w', encoding='utf-8') as f: f.write(s)
    print(f'WROTE Hannover: {len(orig)} -> {len(s)}')

import re
print(f'  Sozialbestattung Section: {bool(re.search(r"<h2>Sozialbestattung in Hannover", s))}')
print(f'  Hamburger Allee 25: {"Hamburger Allee 25" in s}')
print(f'  BSG B 8 SO 20/10 R: {"B 8 SO 20/10 R" in s}')
