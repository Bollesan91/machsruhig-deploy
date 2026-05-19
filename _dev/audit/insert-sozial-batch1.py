#!/usr/bin/env python3
"""Insert Sozialbestattung in Frankfurt + Hannover + Kassel."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# =============== FRANKFURT ===============
SOZIAL_FFM = '''
  <div class="mr-section">
    <h2>Sozialbestattung in Frankfurt — wenn die Kosten nicht aufgebracht werden können</h2>

    <h3>Rechtsgrundlage: § 74 SGB XII und § 13 FBG Hessen</h3>
    <p>Wenn weder der Nachlass noch die bestattungspflichtigen Angehörigen die Bestattungskosten tragen können, übernimmt nach <strong>§ 74 SGB XII</strong> das Sozialamt die <em>erforderlichen</em> Kosten einer einfachen, ortsüblichen Bestattung. Voraussetzung: Die Kostentragung ist den Verpflichteten nicht zumutbar — geprüft wird einkommens- und vermögensabhängig. Das Bundessozialgericht hat in seinem Grundsatzurteil <strong>BSG, B 8 SO 20/10 R vom 25.08.2011</strong> klargestellt, dass „erforderlich" alle Kosten umfasst, die für eine würdige, den örtlichen Gepflogenheiten entsprechende Bestattung anfallen — auch über bloße Mindestleistungen hinaus, wenn diese ortsüblich sind.</p>
    <p>Wer überhaupt bestattungspflichtig ist, regelt in Frankfurt das <strong>Hessische Friedhofs- und Bestattungsgesetz (FBG)</strong>: <strong>§ 13 Abs. 1 FBG</strong> verpflichtet die Angehörigen, die Sorgemaßnahmen zu veranlassen; <strong>§ 13 Abs. 2 FBG</strong> definiert den Kreis der Angehörigen (Ehegatte, Lebenspartner, Kinder, Eltern, Großeltern, Enkel, Geschwister, Adoptiveltern und -kinder, Verlobte). Eine ausdrückliche Rangfolge nennt der Hessen-§ — anders als etwa Mecklenburg-Vorpommern oder NRW — nicht explizit; in der Verwaltungs- und Sozialgerichtspraxis gilt jedoch die Reihenfolge <strong>Ehegatte/Lebenspartner → volljährige Kinder → Eltern → Geschwister → Großeltern → Enkelkinder</strong>, hergeleitet aus § 14 Abs. 3 FBG (Vorrang des Ehegatten- und Kinderwillens) sowie ständiger Rechtsprechung.</p>

    <h3>Zuständige Stelle in Frankfurt: Besonderer Dienst 4</h3>
    <p>Für alle in Frankfurt am Main verstorbenen Personen bearbeitet seit dem 01.06.2019 zentral der <strong>Besondere Dienst 4 — Flüchtlinge und Auswärtige</strong> des Jugend- und Sozialamtes die Anträge nach § 74 SGB XII:</p>
    <p style="margin-left:20px;"><strong>Jugend- und Sozialamt Frankfurt — Besonderer Dienst 4</strong><br>
    Mainzer Landstraße 291, 60326 Frankfurt am Main (Gallus)<br>
    Telefon: 069 212-70009 · Fax: 069 212-40581<br>
    Öffnungszeiten: Mo–Fr 8:00–11:30 Uhr · Mo, Di, Do zusätzlich 13:00–15:00 Uhr<br>
    Anfahrt: S-Bahn S3/S4/S5/S6, Tram 11/14/21 bis Galluswarte</p>

    <h3>Was übernommen wird — und was nicht</h3>
    <p>Das Sozialamt entscheidet nach pflichtgemäßem Ermessen anhand festgelegter Höchstbeträge. Üblicherweise <strong>übernommen</strong> werden: einfacher Sarg bzw. einfache Urne, Holzkreuz, Friedhofsgebühren der Stadt Frankfurt (Erwerb des Nutzungsrechts, Öffnen/Schließen der Grabstelle), bei Feuerbestattung die Einäscherung, Arztkosten für den Totenschein. Über Trauerhalle, Blumenschmuck und einfache Grabplatte wird im Einzelfall entschieden. <strong>Nicht übernommen</strong> werden in der Regel: Trauerredner, Musiker, Trauerfeier-Dekoration, Kondolenzlisten, Traueranzeigen, aufwendige Grabsteine.</p>

    <h3>Wann der Antrag gestellt werden muss</h3>
    <p>Der Antrag kann <strong>vor oder nach der Bestattung</strong> gestellt werden — eine vorherige Genehmigung ist keine Voraussetzung. Wichtig: Antragsberechtigt sind die <em>bestattungspflichtigen Angehörigen</em> nach § 13 FBG, nicht der Bestatter selbst. Auf ausdrücklichen Wunsch kann das Sozialamt die Leistung im Einzelfall direkt an den Bestatter auszahlen. Hat der Verstorbene zu Lebzeiten Sozialleistungen bezogen, ist das Sozialamt zuständig, das zuletzt geleistet hat — andernfalls das Sozialamt am Sterbeort, also bei Tod in Frankfurt der Besondere Dienst 4.</p>
  </div>

'''

fp = 'bestatter/frankfurt/index.html'
with open(fp, 'r', encoding='utf-8') as f: s = f.read()
orig = s
anchor = '  <section class="mr-section" style="background: var(--mr-bg-card);">\n    <div class="mr-container">\n      <h2>Bestatter in anderen Städten</h2>'
replace = SOZIAL_FFM + anchor
n = s.count(anchor)
print(f'Frankfurt anchor: {n}')
if n == 1:
    s = s.replace(anchor, replace)
    with open(fp, 'w', encoding='utf-8') as f: f.write(s)
    print(f'  WROTE Frankfurt: {len(orig)} -> {len(s)}')

# =============== HANNOVER ===============
SOZIAL_HAN = '''
  <div class="mr-section">
    <h2>Sozialbestattung in Hannover — wenn die Kosten nicht tragbar sind</h2>
    <p>Wenn Erben oder Bestattungspflichtige die Kosten einer Bestattung nicht aus eigenen Mitteln aufbringen können, übernimmt der Sozialhilfeträger nach <strong>§ 74 SGB XII</strong> die „erforderlichen Kosten" einer einfachen, ortsüblichen Bestattung. Der Anspruch besteht nicht in Form einer Pauschale, sondern als Einzelfallprüfung — Maßstab ist nach Rechtsprechung des Bundessozialgerichts (BSG, Urteil vom 25.08.2011 — <strong>B 8 SO 20/10 R</strong>) eine würdige, ortsübliche Bestattung, orientiert an den Verhältnissen unterer und mittlerer Einkommensbezieher. Luxusleistungen, Bewirtung der Trauergäste und repräsentative Grabsteine sind nicht erstattungsfähig.</p>

    <h3>Wer ist antragsberechtigt? Reihenfolge nach § 8 Abs. 3 BestattG Niedersachsen</h3>
    <p>Anspruchsberechtigt ist ausschließlich, wer <strong>bestattungspflichtig</strong> ist — Nachbarn oder Freunde, die sich freiwillig um die Bestattung kümmern, erhalten keine Erstattung. Die Bestattungspflicht ergibt sich aus <strong>§ 8 Abs. 3 Niedersächsisches Bestattungsgesetz (BestattG)</strong> in folgender Rangfolge: (1) Ehegattin/Ehegatte oder eingetragene Lebenspartnerin/Lebenspartner, (2) volljährige Kinder, (3) Eltern, (4) volljährige Geschwister, (5) Großeltern, (6) volljährige Enkelkinder. Innerhalb derselben Rangstufe entscheidet die enge Beziehung zur verstorbenen Person. Wurde vertraglich zu Lebzeiten eine andere Person mit der Bestattung beauftragt, geht diese vertragliche Regelung der öffentlich-rechtlichen Reihenfolge vor.</p>

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
    <p>Der Antrag sollte <strong>vor der Beauftragung des Bestatters</strong> oder unmittelbar danach gestellt werden. Eine gesetzliche Frist nennt § 74 SGB XII nicht — je später der Antrag nach Eintritt der Kostentragungspflicht eingeht, desto eher kann das Sozialamt Zweifel an der Zumutbarkeit anmelden. Praktisch: Bei Beauftragung des Bestattungsunternehmens schriftlich darauf hinweisen, dass ein Antrag nach § 74 SGB XII gestellt wird oder bereits gestellt wurde. Nicht anerkannte Kosten — etwa über das Niveau einer einfachen Bestattung hinausgehende Posten — trägt sonst die antragstellende Person selbst. Die <strong>8-Tage-Frist nach § 9 BestattG Niedersachsen</strong> für die Bestattung läuft unabhängig vom Antragsverfahren weiter; die Bestattung darf wegen der Sozialamt-Prüfung nicht aufgeschoben werden.</p>

    <div class="mr-hint">
      <strong>Hinweis:</strong> Eine Erbausschlagung (sechs Wochen ab Kenntnis, beim Nachlassgericht oder Amtsgericht des eigenen Wohnsitzes) befreit <strong>nicht automatisch</strong> von der Bestattungspflicht nach § 8 Abs. 3 BestattG Niedersachsen — die öffentlich-rechtliche Pflicht besteht unabhängig von der erbrechtlichen Stellung fort. Bestattungspflichtige können dennoch einen Antrag nach § 74 SGB XII stellen, wenn die Kostenübernahme finanziell unzumutbar ist.
    </div>
  </div>

'''

fp = 'bestatter/hannover/index.html'
with open(fp, 'r', encoding='utf-8') as f: s = f.read()
orig = s
anchor = 'durchgereichten Friedhofsgebühren und Honorare Dritter (Pfarrer, Trauerredner, Floristik).</strong></p>\n  </div>\n\n  <div class="mr-section">\n    <h2>Was nach einem Todesfall in Hannover zu tun ist</h2>'
replace = 'durchgereichten Friedhofsgebühren und Honorare Dritter (Pfarrer, Trauerredner, Floristik).</strong></p>\n  </div>\n' + SOZIAL_HAN + '  <div class="mr-section">\n    <h2>Was nach einem Todesfall in Hannover zu tun ist</h2>'
n = s.count(anchor)
print(f'Hannover anchor: {n}')
if n == 1:
    s = s.replace(anchor, replace)
    with open(fp, 'w', encoding='utf-8') as f: f.write(s)
    print(f'  WROTE Hannover: {len(orig)} -> {len(s)}')

# =============== KASSEL ===============
SOZIAL_KAS = '''
  <section class="mr-section" id="sozialbestattung">
    <h2>Sozialbestattung in Kassel: § 74 SGB XII</h2>
    <p>Reicht der Nachlass nicht aus und ist auch den Bestattungspflichtigen die Kostentragung wirtschaftlich nicht zumutbar, übernimmt der örtliche Sozialhilfeträger nach <strong>§ 74 SGB XII</strong> die <em>erforderlichen Kosten der Bestattung</em>. Die Norm setzt keinen laufenden Sozialhilfebezug voraus – entscheidend ist die individuelle Zumutbarkeitsprüfung.</p>

    <h3>Wer ist bestattungspflichtig in Hessen?</h3>
    <p>Die Reihenfolge der Bestattungspflichtigen regelt <strong>§ 13 Hessisches Friedhofs- und Bestattungsgesetz (FBG)</strong>: Ehegatte oder eingetragene Lebenspartnerin bzw. Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, volljährige Enkel, Großeltern. Nur wer in dieser Rangfolge bestattungspflichtig ist, kann Antragsteller nach § 74 SGB XII sein. Die sozialhilferechtliche Kostentragungspflicht knüpft also unmittelbar an die landesrechtliche Bestattungspflicht aus dem FBG an.</p>

    <h3>Zuständiges Sozialamt: Stadt Kassel</h3>
    <p>Für Verstorbene mit letztem gewöhnlichem Aufenthalt im Stadtgebiet Kassel ist die <strong>Stadt Kassel als kreisfreie Stadt</strong> örtlicher Träger der Sozialhilfe (§ 3 Abs. 2 SGB XII). Anlaufstelle: Sozialamt der Stadt Kassel, Obere Königsstraße 8, 34117 Kassel (Rathaus), Telefon 0561 115 oder direkte Durchwahl 0561 787-1272 bzw. -1273, E-Mail sozialamt@kassel.de. Für Verstorbene mit Wohnsitz in den Umlandgemeinden ist hingegen der <strong>Landkreis Kassel</strong> zuständig (Kohlenstraße 132, 34121 Kassel, Telefon 0561 1003-1882).</p>

    <h3>Was wird übernommen?</h3>
    <p>Erstattet werden die <em>ortsüblichen, einfachen, würdigen</em> Bestattungskosten. In der Praxis typischerweise: einfacher Sarg oder Urne, Überführung im Stadtgebiet, Friedhofsgebühren für ein Reihengrab (kein Wahlgrab), bei Feuerbestattung die Einäscherung, eine schlichte Trauerfeier, Sterbeurkunden. Nicht übernommen werden in der Regel Grabmal, Trauerkaffee, Traueranzeigen, gehobener Blumenschmuck und Wahlgrabnutzungsrechte. Maßstab in Kassel ist die Erdbestattung im Reihengrab mit Trauerfeier nach Ziffer 5.2.1 der Gebührensatzung 2024 (2.327,00 Euro) bzw. die Urnenbeisetzung nach Einäscherung (Ziffern 6.1.1 und 6.4.1).</p>

    <h3>„Nicht zumutbar" – Leiturteil BSG B 8 SO 20/10 R</h3>
    <p>Das Bundessozialgericht hat mit Urteil vom 25. August 2011, Az. <strong>B 8 SO 20/10 R</strong>, die Maßstäbe für die Zumutbarkeit konkretisiert: Erforderlich ist eine Gesamtabwägung der wirtschaftlichen Leistungsfähigkeit der bestattungspflichtigen Person, der persönlichen Beziehung zum Verstorbenen und der konkreten Belastungssituation. Sozialhilfebezug ist keine Voraussetzung; eine bestehende Erwerbstätigkeit schließt Unzumutbarkeit nicht aus, wenn die Kosten die wirtschaftliche Existenz nachhaltig gefährden würden. Umgekehrt kann eine über Jahre nachweislich zerrüttete familiäre Beziehung die Unzumutbarkeit zusätzlich begründen.</p>

    <h3>Antragszeitpunkt: möglichst vor der Bestattung</h3>
    <p>Der Antrag sollte <strong>vor</strong> der Beauftragung des Bestatters beim Sozialamt eingereicht werden. Wer ohne vorherige Abstimmung ein teureres Paket beauftragt, riskiert, dass Mehrkosten gegenüber dem ortsüblichen Standard nicht erstattet werden. Eine nachträgliche Antragstellung ist nach der Rechtsprechung zwar grundsätzlich möglich; § 74 SGB XII enthält keine starre Ausschlussfrist, in der Verwaltungspraxis ist jedoch ein zeitnaher Antrag (Faustregel: innerhalb weniger Wochen nach Bestattung) zwingend. Beizufügen sind Kostenvoranschlag, Sterbeurkunde, Einkommens- und Vermögensnachweise des Antragstellers sowie ein Nachlassverzeichnis.</p>

    <div class="mr-callout"><strong>Tipp:</strong> Bei absehbar fehlender Leistungsfähigkeit vor Beauftragung kurz beim Sozialamt anfragen. Viele Kasseler Bestatter haben Routine mit § 74-Fällen und kalkulieren entsprechend.</div>
  </section>

'''

fp = 'bestatter/kassel/index.html'
with open(fp, 'r', encoding='utf-8') as f: s = f.read()
orig = s
# Anchor: between Todesfall-Schritte close and Bestatter-Wahl
import re
# Find the Todesfall section's closing and the next Bestatter section
m = re.search(r'(<h2>Was nach einem Todesfall in Kassel zu tun ist</h2>.*?</section>)\s*(\s*<section class="mr-section">\s*<h2>Bestatter in Kassel)', s, re.S)
if m:
    print(f'Kassel anchor pattern match start={m.start()}')
    s = s[:m.start(2)] + SOZIAL_KAS + s[m.start(2):]
    with open(fp, 'w', encoding='utf-8') as f: f.write(s)
    print(f'  WROTE Kassel: {len(orig)} -> {len(s)}')
else:
    print('Kassel anchor NOT FOUND — try alternate')
    # Alternate: insert before <h2>Quellen
    anchor2 = '<h2 id="quellen">Quellen'
    if anchor2 in s:
        s = s.replace(anchor2, SOZIAL_KAS + '  <section class="mr-section">\n    ' + anchor2)
        with open(fp, 'w', encoding='utf-8') as f: f.write(s)
        print(f'  WROTE Kassel (alt anchor): {len(orig)} -> {len(s)}')
