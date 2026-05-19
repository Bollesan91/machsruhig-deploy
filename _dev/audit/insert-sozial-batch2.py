#!/usr/bin/env python3
"""Insert Sozialbestattung modules for Bochum/Heidelberg/Mannheim + Akutbox+Sozial for Hamburg (Batch 2)."""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# ============================================================
# BOCHUM
# ============================================================
BOCHUM_SOZIAL = '''
  <div class="mr-section">
    <h2>Sozialbestattung in Bochum — Kostenübernahme nach § 74 SGB XII</h2>
    <p>Können die nach <a href="https://recht.nrw.de/lrgv/gesetz/19022022-gesetz-ueber-das-friedhofs-und-bestattungswesen-bestattungsgesetz-bestg-nrw" rel="noopener" target="_blank">§ 8 Abs. 1 BestG NRW</a> bestattungspflichtigen Angehörigen (Ehegatte/Lebenspartner, volljährige Kinder, Eltern, Großeltern, volljährige Geschwister, volljährige Enkelkinder) die Bestattungskosten nicht aus eigenen Mitteln und aus dem Nachlass der verstorbenen Person tragen, übernimmt das Sozialamt nach <strong>§ 74 SGB XII</strong> die <em>erforderlichen</em> Kosten der Bestattung. Maßgeblich ist die wirtschaftliche Zumutbarkeit für die bestattungspflichtige Person — nicht der Sozialhilfestatus der verstorbenen Person. Das Bundessozialgericht hat mit Urteil vom <strong>25.08.2011 (B 8 SO 20/10 R)</strong> klargestellt, dass die Prüfung der Zumutbarkeit individuell und unter Berücksichtigung der Einkommens- und Vermögensverhältnisse des Verpflichteten zu erfolgen hat — eine pauschale Ablehnung ist unzulässig.</p>
    <h3>Zuständige Stelle: Amt für Soziales Bochum</h3>
    <p>Zuständig ist in Bochum das <strong>Amt für Soziales</strong> der Stadt Bochum (nicht „Sozialamt" als Eigenname). Das Amt befindet sich seit der Standortzusammenführung im Husemann Karree:</p>
    <p>Stadt Bochum — Amt für Soziales<br>
    Husemann Karree (5. OG)<br>
    Viktoriastraße 14c, 44777 Bochum<br>
    Service-Center: <a href="tel:+492349100">0234 910-0</a><br>
    Schriftlich: <a href="https://www.bochum.de/Amt-fuer-Soziales" rel="noopener" target="_blank">Online-Kontaktformular der Stadt Bochum</a><br>
    Servicezeit (telefonisch): Mo–Mi 8–16 Uhr, Do 8–17 Uhr, Fr 8–14 Uhr. Persönliche Vorsprache nur nach Terminvereinbarung.</p>
    <h3>Was wird übernommen — und was nicht?</h3>
    <p><strong>Übernommen werden</strong> die <em>erforderlichen</em> Kosten einer ortsüblich einfachen Bestattung: Sarg oder Urne in einfacher Ausführung, Überführung, hygienische Versorgung, Sterbeurkunden-Gebühren, einfache Friedhofsgebühren für ein Reihengrab, Trauerhallennutzung in einfachem Rahmen sowie Standardträger-Leistungen. <strong>Nicht übernommen</strong> werden in der Regel: aufwendiger Sarg, Trauerdruck und Anzeigen, Trauerredner, Blumenschmuck über das Notwendige hinaus, Grabstein, Wahlgrab anstelle eines Reihengrabs sowie laufende Grabpflege. Die Übernahme erfolgt nachrangig: Vorrangig sind Nachlass, Sterbegelder aus Versicherungen sowie Leistungen anderer Träger (z. B. Berufsgenossenschaft).</p>
    <h3>Antrag möglichst vor Auftragsvergabe</h3>
    <p>Der Antrag kann formlos beim Amt für Soziales gestellt werden — <strong>idealerweise vor Beauftragung des Bestatters</strong>, damit Art und Umfang der Bestattung im erstattungsfähigen Rahmen bleiben. Wer einen Premium-Bestatterauftrag erteilt und im Nachgang die Erstattung beantragt, riskiert, dass nur ein Teil als „erforderlich" anerkannt wird. Eine nachträgliche Antragstellung bleibt möglich (Ausschlussfrist: ein Jahr ab Kenntnis der Verpflichtung), ist aber risikoreicher. Mitzubringen sind: Sterbeurkunde, Kostenvoranschlag des Bestatters, Nachweise über Einkommen und Vermögen der antragstellenden Person sowie Nachlassübersicht der verstorbenen Person. Hinweis der <strong>Verbraucherzentrale NRW</strong>: Im Zweifel vor Auftragsvergabe kurz beim Amt für Soziales anrufen.</p>
  </div>

'''

# ============================================================
# HEIDELBERG
# ============================================================
HEIDELBERG_SOZIAL = '''<section class="mr-section">
  <h2>Sozialbestattung in Heidelberg — wenn die Kosten nicht zu tragen sind</h2>
  <p>Wenn die Bestattungskosten die finanziellen Möglichkeiten der Bestattungspflichtigen übersteigen, gibt es einen Rechtsanspruch auf Kostenübernahme nach <strong>§ 74 SGB XII</strong> („Bestattungskosten"). Voraussetzung ist, dass die Übernahme der erforderlichen Kosten der verpflichteten Person nicht zugemutet werden kann — gemessen an Einkommen, Vermögen und einem etwaigen Nachlass des Verstorbenen. Wer bestattungspflichtig ist, ergibt sich in Baden-Württemberg aus <strong>§ 31 BestattG BW</strong> in der Reihenfolge: Ehegatte oder eingetragener Lebenspartner, volljährige Kinder, Eltern, volljährige Geschwister, Großeltern, volljährige Enkelkinder.</p>
  <h3>Zuständige Stelle in Heidelberg</h3>
  <p>Da Heidelberg ein Stadtkreis ist, ist <strong>nicht</strong> das Sozialamt des Rhein-Neckar-Kreises zuständig, sondern die Stadt selbst:</p>
  <p><strong>Amt für Soziales und Senioren der Stadt Heidelberg</strong><br>
  Eppelheimer Straße 13, 69115 Heidelberg<br>
  Telefon: <a href="tel:+49622158370000">06221 58-37000</a><br>
  E-Mail: <a href="mailto:sozialamt@heidelberg.de">sozialamt@heidelberg.de</a><br>
  Sprechzeiten: Dienstag, Donnerstag, Freitag 8–12 Uhr (Termine nach Vereinbarung möglich). Die Sachbearbeitung ist nach Anfangsbuchstaben des Nachnamens des Verstorbenen aufgeteilt.</p>
  <p>Die örtliche Zuständigkeit folgt einer einfachen Regel: Hat der Verstorbene Sozialhilfe bezogen, ist das Sozialamt zuständig, das die Leistung bis zum Tod erbracht hat. War das nicht der Fall, ist das Sozialamt des Sterbeortes zuständig.</p>
  <h3>Was übernommen wird — und was nicht</h3>
  <p>Übernommen werden die <strong>erforderlichen</strong> Kosten einer ortsüblichen, einfachen, aber würdigen Bestattung. Dazu zählen in der Regel: einfacher Sarg oder Urne, Überführung, Versorgung, Friedhofsgebühren für ein einfaches Reihengrab, Bestatterleistungen im Grundumfang, Sterbeurkunden, Kremationsgebühr bei Feuerbestattung sowie eine schlichte Trauerfeier. <strong>Nicht übernommen</strong> werden Wahlgräber mit erhöhter Liegezeit, aufwendige Sarg- oder Urnenausstattungen, Trauerredner, Blumenschmuck über das Notwendige hinaus, Steinmetzarbeiten, Traueranzeigen und Trauerkaffee. Die Praxis vieler Sozialämter orientiert sich an Pauschalen zwischen rund 1.500 € und 3.000 € zuzüglich Friedhofsgebühren — die genaue Obergrenze legt das Heidelberger Amt im Einzelfall fest.</p>
  <p>Ein wichtiger höchstrichterlicher Grundsatz: Nach dem Urteil des Bundessozialgerichts vom <strong>25.08.2011 (Az. B 8 SO 20/10 R)</strong> sind die Kosten nicht „zumutbar" allein deshalb, weil ein Nachlass formal vorhanden ist — entscheidend ist die tatsächliche wirtschaftliche Leistungsfähigkeit der bestattungspflichtigen Person. Auch eine Erbausschlagung schließt den Anspruch auf § 74 SGB XII nicht automatisch aus, solange die Bestattungspflicht nach § 31 BestattG BW fortbesteht.</p>
  <h3>Antragszeitpunkt</h3>
  <p>Der Antrag kann <strong>vor oder nach</strong> der Bestattung gestellt werden — eine vorherige Beratung beim Sozialamt ist allerdings dringend zu empfehlen, weil die Erforderlichkeit der einzelnen Kostenpositionen so im Vorfeld geklärt werden kann. Wer eine teure Bestattung beauftragt und erst danach Antrag stellt, riskiert, auf der Differenz zwischen tatsächlichen und „erforderlichen" Kosten sitzen zu bleiben.</p>
</section>

'''

# ============================================================
# MANNHEIM
# ============================================================
MANNHEIM_SOZIAL = '''  <div class="mr-section">
    <h2>Sozialbestattung in Mannheim — wenn die Kosten die Angehörigen überfordern</h2>
    <p>Reicht das Vermögen der verstorbenen Person nicht aus und sind die nach <strong>§ 31 BestattG BW</strong> bestattungspflichtigen Angehörigen (Ehegatte/Lebenspartner, volljährige Kinder, Eltern, Großeltern, volljährige Geschwister, Enkelkinder — in dieser Reihenfolge) wirtschaftlich nicht in der Lage, die Kosten zu tragen, übernimmt der Sozialhilfeträger nach <a href="https://www.gesetze-im-internet.de/sgb_12/__74.html" rel="noopener" target="_blank">§ 74 SGB XII</a> die <strong>erforderlichen Kosten</strong> einer ortsüblichen, einfachen, aber würdevollen Bestattung. Maßstab ist die Zumutbarkeit: Das Bundessozialgericht hat mit Urteil vom <strong>25.08.2011 (Az. B 8 SO 20/10 R)</strong> klargestellt, dass die Übernahme nicht nur bei Mittellosigkeit, sondern bereits dann greift, wenn dem Verpflichteten nach seinen wirtschaftlichen Verhältnissen die Tragung nicht zugemutet werden kann — auch ein Erbausschlagungsfall entbindet von der Kostenpflicht nach § 1968 BGB, nicht aber von der ordnungsbehördlichen Bestattungspflicht nach BestattG BW.</p>
    <h3>Zuständige Stelle in Mannheim</h3>
    <p>Anlaufstelle für Sozialbestattungen ist der <strong>Fachbereich Arbeit und Soziales der Stadt Mannheim</strong> (Sozialamt):</p>
    <p>Fachbereich Arbeit und Soziales<br>
    K 1, 7–13<br>
    68159 Mannheim<br>
    Telefon: <a href="tel:+496212939218">0621 293-9218</a> / <a href="tel:+496212939219">-9219</a><br>
    Fax: 0621 293-3444<br>
    E-Mail: <a href="mailto:arbeit.soziales@mannheim.de">arbeit.soziales@mannheim.de</a></p>
    <h3>Was übernommen wird — und was nicht</h3>
    <p><strong>Übernommen werden</strong> die ortsüblichen Kosten einer einfachen Bestattung: Sarg oder Urne in einfacher Ausführung, hygienische Versorgung, Überführung, Sterbeurkunden, kommunale Friedhofsgebühren für ein Reihengrab nach der Mannheimer Gebührensatzung (z. B. 910 € für 15 Jahre Erdreihengrab), einfache Trauerfeier und Beisetzung. <strong>Nicht übernommen werden</strong> in der Regel Wahlgräber, aufwendige Grabmale, repräsentative Sargmodelle, Trauerredner-Honorare über dem ortsüblichen Niveau, Bewirtung, Traueranzeigen und Grabpflege. Vorrangig einzusetzen sind Nachlassvermögen, Sterbegeldversicherungen sowie Leistungen Dritter (z. B. Berufsgenossenschaft bei Arbeitsunfall).</p>
    <h3>Antrag — Timing entscheidet</h3>
    <p>Der Antrag ist <strong>vor Beauftragung des Bestatters</strong> oder unmittelbar danach zu stellen — spätestens jedoch vor Begleichung der Rechnung. Wer ohne Rücksprache eine kostspielige Bestattung beauftragt und erst anschließend Übernahme beantragt, riskiert, dass nur der ortsübliche Mindestbetrag erstattet wird. Mitzubringen sind Sterbeurkunde, Kostenvoranschlag des Bestatters, Nachweise zum Nachlass (Kontoauszüge, Versicherungspolicen) sowie Einkommens- und Vermögensnachweise der antragstellenden Person.</p>
  </div>

'''

# ============================================================
# HAMBURG (Akutbox + Sozial — both modules)
# ============================================================
HAMBURG_AKUTBOX = '''  <div class="mr-section" id="akutbox-hamburg" style="background:#FFFAF5;border:2px solid var(--mr-accent);border-radius:var(--mr-radius);padding:24px 28px;margin:0 0 32px;">
    <h2 style="border-bottom:none;padding-bottom:0;margin-bottom:8px;">Was nach einem Todesfall in Hamburg zu tun ist — die ersten Schritte</h2>
    <p style="font-size:14px;color:var(--mr-text-muted);margin-bottom:16px;">Wenn ein Mensch verstorben ist, drängt erst einmal nichts. Diese sechs Schritte ordnen die ersten Tage in der für Hamburg geltenden Reihenfolge — vom Totenschein bis zur Trauerfeier.</p>
    <h3 style="margin-top:16px;">1. Arzt rufen und Totenschein ausstellen lassen</h3>
    <p>Erste Pflicht ist die ärztliche Leichenschau. Tritt der Tod zu Hause ein, ruft man die Hausärztin, den hausärztlichen Notdienst (116 117) oder bei unklaren Umständen den Rettungsdienst (112). In Krankenhäusern und Pflegeheimen veranlasst die Einrichtung die Leichenschau (§ 3 HmbBestattG). Die Ärztin oder der Arzt stellt die Todesbescheinigung (Totenschein) aus — sie ist die Grundvoraussetzung für alle weiteren Schritte.</p>
    <h3>2. Bestatter in Hamburg beauftragen</h3>
    <p>Die Überführung in eine Leichenhalle muss innerhalb von <strong>36 Stunden</strong> erfolgen (§ 6 HmbBestattG). In dieser Zeit wählt die Familie ein Bestattungsunternehmen — am besten nach Einholung von zwei bis drei Kostenvoranschlägen. Der Bestatter übernimmt anschließend Überführung, Sterbefallanzeige, Friedhofsabstimmung und Trauerfeier-Logistik. Hamburg-Wohnsitz der verstorbenen Person ist für eine Beisetzung in Ohlsdorf oder Öjendorf nicht Voraussetzung.</p>
    <h3>3. Sterbefall beim Standesamt anzeigen (3 Werktage)</h3>
    <p>Der Sterbefall muss spätestens am dritten auf den Tod folgenden Werktag dem Standesamt angezeigt werden (<a href="https://www.gesetze-im-internet.de/pstg/__28.html" rel="noopener" target="_blank">§ 28 PStG</a>). Zuständig ist in Hamburg <strong>immer das Standesamt des Bezirks, in dem die Person verstorben ist</strong> — nicht das Wohnsitz-Standesamt. Die sieben Hamburger Standesämter sind: Hamburg-Mitte (Caffamacherreihe 1–3, 20355), Altona, Eimsbüttel (Grindelberg 62–66, 20144), Hamburg-Nord (Kümmellstraße 5–7, 20249), Wandsbek (Schloßstraße 60, 22041), Bergedorf und Harburg (Harburger Rathausforum 3, 21073). Anzeige und Beurkundung übernimmt in der Regel der beauftragte Bestatter. Verstirbt jemand in einer Einrichtung (Krankenhaus, Pflegeheim), zeigt diese den Sterbefall direkt schriftlich an.</p>
    <h3>4. Friedhof wählen und Grabstelle festlegen</h3>
    <p>Hamburgs staatliche Friedhöfe (Ohlsdorf, Öjendorf, Bergedorf, Harburg u. a.) verwaltet die <strong>Hamburger Friedhöfe AöR</strong>. Über sie laufen Grabwahl, Trauerhallen-Reservierung und Gebühren. Daneben gibt es kirchliche und jüdische Friedhöfe sowie die Option einer Seebestattung über spezialisierte Reedereien. Sargwahlgräber liegen je nach Lage und Größe bei 2.800–3.195 Euro für 25 Jahre Ruhezeit; Urnenwahlgräber bei 2.000–2.230 Euro.</p>
    <h3>5. Bestattung anmelden und Termin koordinieren</h3>
    <p>Die Anmeldung der Bestattung bei der Hamburger Friedhöfe AöR übernimmt der Bestatter und stimmt Termin, Kapelle und Beisetzungsablauf ab. Eine Erdbestattung muss in Hamburg spätestens nach 10 Tagen erfolgt sein — eine vergleichsweise großzügige Frist. Bei Feuerbestattungen ist nach der Einäscherung in der Regel innerhalb eines Monats beizusetzen.</p>
    <h3>6. Trauerfeier gestalten</h3>
    <p>Trauerfeiern finden in einer der zwölf Kapellen auf Ohlsdorf, in der Aussegnungshalle Öjendorf oder in den Trauerhallen der bezirklichen Friedhöfe statt. Form und Umfang gestaltet die Familie frei: vom stillen Abschied am Grab bis zur Feier mit Musik, Rede und Predigt. Hilfreich für die Vorbereitung: <a href="/trauerrede-schreiben">Trauerrede schreiben</a> und <a href="/tools/checkliste-todesfall">Checkliste Todesfall</a>.</p>
  </div>

'''

HAMBURG_SOZIAL = '''  <div class="mr-section" id="sozialbestattung-hamburg">
    <h2>Sozialbestattung in Hamburg — Übernahme der Bestattungskosten nach § 74 SGB XII</h2>
    <p>Reichen Nachlass und eigene Mittel der bestattungspflichtigen Person nicht aus, übernimmt das Sozialamt die <strong>erforderlichen Kosten der Bestattung</strong> nach <strong>§ 74 SGB XII</strong>. Der Anspruch knüpft nicht an das Erbe an, sondern daran, ob es der oder dem Verpflichteten zumutbar ist, die Kosten selbst zu tragen. Antragsberechtigt ist, wer nach Hamburger Recht <em>kostentragungspflichtig</em> ist — das sind zunächst die Erben, sonst die in der gesetzlichen Rangfolge bestimmten Angehörigen.</p>
    <h3>Bestattungspflicht in Hamburg — Rangfolge nach § 11 HmbBestattG</h3>
    <p>Wer für die Bestattung zu sorgen hat, regelt das Hamburgische Bestattungsgesetz in <strong>§ 10 HmbBestattG</strong> (Bestattungspflicht) und <strong>§ 11 HmbBestattG</strong> (Reihenfolge der Angehörigen). Verpflichtet sind nacheinander: Ehegatten beziehungsweise Lebenspartnerin oder Lebenspartner, volljährige Kinder, Eltern, Geschwister und Enkel. Mehrere Gleichrangige haften als Gesamtschuldner. Wichtig: Die öffentlich-rechtliche Bestattungspflicht und die privatrechtliche Kostentragungspflicht sind nicht dasselbe — ein Anspruch nach § 74 SGB XII besteht nur für die kostentragungspflichtige Person.</p>
    <h3>Zuständige Stelle in Hamburg</h3>
    <p>Den Antrag stellt man beim <strong>Fachamt Grundsicherung und Soziales des Bezirksamts</strong>, in dem die verstorbene Person zuletzt ihren gewöhnlichen Aufenthalt hatte. In Hamburg sind das die bezirklichen Sozialämter in Mitte, Altona, Eimsbüttel, Nord, Wandsbek, Bergedorf und Harburg. Eine Hamburger Besonderheit: Die Sozialämter haben mit den Hamburger Bestattern eine Rahmenvereinbarung mit festgelegten Höchstsätzen für „ortsübliche" Bestattungsleistungen. Wer den Antrag <em>nach</em> der Beauftragung stellt, riskiert daher, auf der Differenz zwischen vereinbartem Preis und übernahmefähigem Satz sitzen zu bleiben.</p>
    <div class="mr-hint">
      <strong>Antrag möglichst vor der Beauftragung stellen.</strong> Die Hamburger Fachanweisung zu § 74 SGB XII lässt einen Anspruch bereits zu, wenn absehbar ist, dass niemand sonst die Bestattung veranlassen wird — eine vorherige ordnungsrechtliche Verfügung ist nicht erforderlich.
    </div>
    <h3>„Erforderliche Kosten" — was übernommen wird</h3>
    <p>Das Sozialamt zahlt eine schlichte, ortsübliche Bestattung: Sarg oder Urne, Überführung, Sterbefallanzeige, einfache Trauerfeier, Grabstelle und Erstbepflanzung. Nicht regelmäßig übernommen werden gehobene Särge, Trauerredner, größere Blumenarrangements, Traueranzeigen oder Grabsteine. Maßgeblich für den Umfang ist das Grundsatzurteil des Bundessozialgerichts vom <strong>25.08.2011, B 8 SO 20/10 R</strong>: „Erforderlich" sind danach die Kosten einer würdigen, dem örtlichen Standard entsprechenden Bestattung — nicht jedoch jede vom Auftraggeber gewünschte Zusatzleistung.</p>
    <p>Benötigte Unterlagen: Sterbeurkunde, Kostenvoranschlag des Bestatters, Nachweise zum Nachlass (Kontoauszüge, Erbausschlagung beim Nachlassgericht falls vorgenommen), Einkommens- und Vermögensnachweise der antragstellenden Person. Eine Übersicht zum Verfahren findet sich auf <a href="https://www.hamburg.de/" rel="noopener" target="_blank">hamburg.de</a> unter dem Stichwort „Übernahme von Bestattungskosten".</p>
  </div>

'''

# ============================================================
# INSERT LOGIC
# ============================================================

def do_insert(fp, anchor, insert_html, label, mode='before'):
    """mode: 'before' = insert BEFORE anchor; 'after' = insert AFTER anchor"""
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

# Bochum — insert AFTER closing </div> of Bestattungskosten section, BEFORE Was-tun section
bochum_anchor = '  <div class="mr-section">\n    <h2>Was nach einem Todesfall in Bochum zu tun ist</h2>'
do_insert('bestatter/bochum/index.html', bochum_anchor, BOCHUM_SOZIAL, 'BOCHUM', mode='before')

# Heidelberg — insert BEFORE Bestatter-section <section class="mr-section">\n  <h2>Bestatter in Heidelberg
heidelberg_anchor = '<section class="mr-section">\n  <h2>Bestatter in Heidelberg — worauf zu achten ist</h2>'
do_insert('bestatter/heidelberg/index.html', heidelberg_anchor, HEIDELBERG_SOZIAL, 'HEIDELBERG', mode='before')

# Mannheim — insert BEFORE Bestatter-Wahl section
mannheim_anchor = '  <div class="mr-section">\n    <h2>Bestatter-Wahl in Mannheim</h2>'
do_insert('bestatter/mannheim/index.html', mannheim_anchor, MANNHEIM_SOZIAL, 'MANNHEIM', mode='before')

# Hamburg Akutbox — insert BEFORE first H2 of content (Kernfakten Hamburg) so it appears at top
hamburg_akut_anchor = '    <h2>Kernfakten Hamburg</h2>'
# We need a unique anchor — adjust to include surrounding context
hamburg_akut_anchor2 = '  <div class="mr-keyfacts">\n    <h2>Kernfakten Hamburg</h2>'
# Check if anchor exists. Try simpler one if needed.
with open('bestatter/hamburg/index.html', 'r', encoding='utf-8') as f:
    hbg = f.read()
if hbg.count(hamburg_akut_anchor2) == 1:
    do_insert('bestatter/hamburg/index.html', hamburg_akut_anchor2, HAMBURG_AKUTBOX, 'HAMBURG-AKUTBOX', mode='before')
else:
    # Fallback: find the anchor pattern for Kernfakten - try alternative
    m = re.search(r'(<div class="mr-keyfacts"[^>]*>\s*<h2>Kernfakten Hamburg</h2>)', hbg)
    if m:
        actual_anchor = m.group(1)
        print(f'HAMBURG-AKUTBOX fallback anchor: {actual_anchor[:80]}')
        do_insert('bestatter/hamburg/index.html', actual_anchor, HAMBURG_AKUTBOX, 'HAMBURG-AKUTBOX', mode='before')
    else:
        print('HAMBURG-AKUTBOX: anchor NOT FOUND in any form')

# Hamburg Sozial — insert BEFORE Cross-City "Bestatter in anderen Städten" block
hamburg_sozial_anchor = '<section class="mr-section" style="background: var(--mr-bg-card);">'
do_insert('bestatter/hamburg/index.html', hamburg_sozial_anchor, HAMBURG_SOZIAL, 'HAMBURG-SOZIAL', mode='before')

# ============================================================
# VERIFICATION
# ============================================================
print('\n=== VERIFICATION ===')
for city in ['bochum', 'heidelberg', 'mannheim', 'hamburg']:
    fp = f'bestatter/{city}/index.html'
    with open(fp, 'r', encoding='utf-8') as f:
        s = f.read()
    rstrip_len = len(s.rstrip('\x00'))
    nul_ok = (rstrip_len == len(s))
    has_sozial = ('Sozialbestattung in ' in s)
    has_sgb = ('§ 74 SGB XII' in s or '§ 74 SGB XII' in s)
    has_bsg = ('B 8 SO 20/10 R' in s)
    sec_open = len(re.findall(r'<section\b', s))
    sec_close = len(re.findall(r'</section>', s))
    tag_balanced = (sec_open == sec_close)
    print(f'{city}: len={len(s)}, NUL-ok={nul_ok}, Sozial={has_sozial}, §74={has_sgb}, BSG={has_bsg}, <section> open/close={sec_open}/{sec_close} balanced={tag_balanced}')
