#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R7b — Auflagen aus NO-GO-79-Review /sozialbestattung:
HOCH-1: Trauerredner widerspricht eigenem BSG-Zitat (B 8 SO 20/22 R: freier
  Trauerredner gehoert zu den erforderlichen Kosten) -> Tabelle korrigiert;
  derselbe Fehler steht im §74-Block der Hamburg-Stadtseite -> mitgefixt.
HOCH-2: Bayern-Beispiel falsch (Art. 15 BestV: weiter Verwandtenkreis, aber
  KEIN nichtehelicher Lebensgefaehrte) -> Bayern als Gegenbeispiel, SH/Nds.
  als Beispiele mit Lebensgemeinschafts-Pflicht.
MITTEL-1: Mythen-Eintrag dritter Erbe + Solvenz-Vorbehalt (Leitsatz 2).
MITTEL-2: SGB II laut BSG gleichrangig mit SGB XII (regelmaessig unzumutbar).
MITTEL-3: Schonvermoegen-Spanne nach unten geoeffnet (OVG NRW 2021: 7.000 €).
MITTEL-4: Lead entschaerft (zivilrechtliche Haftung bleibt).
MITTEL-5: formloser Antrag + Stundung/Direktabrechnung beim Bestatter.
FAQ-Texte sind in JSON-LD + sichtbar zeichengleich -> expect=2.
"""
import io, sys

P = 'sozialbestattung.html'
t = io.open(P, encoding='utf-8').read()

def rep(old, new, expect=1):
    global t
    c = t.count(old)
    if c != expect:
        print('FATAL: %r -> %d (erwartet %d)' % (old[:75], c, expect)); sys.exit(1)
    t = t.replace(old, new)

# HOCH-1: Tabelle — Trauerredner nach links (enthalten), rechts defensiver Ersatz
rep('<tr><td>Einfacher Sarg oder einfache Urne (auch schlichte Schmuckurne)</td><td>Externer Trauerredner</td></tr>',
    '<tr><td>Einfacher Sarg oder einfache Urne (auch schlichte Schmuckurne)</td><td>Zeitungs-Traueranzeigen und Danksagungskarten</td></tr>')
rep('<tr><td>Gegebenenfalls eine einfache Trauerfeier</td><td>Aufwendige Trauerfeier-Gestaltung</td></tr>',
    '<tr><td>Gegebenenfalls eine einfache Trauerfeier</td><td>Aufwendige Trauerfeier-Gestaltung</td></tr>\n          <tr><td>Ein freier Trauerredner in einfachem Rahmen (BSG, B 8 SO 20/22 R: gehört zu den erforderlichen Kosten)</td><td></td></tr>')

# HOCH-2: Bayern-Beispiel ersetzen
rep('<li><strong>Bayern und einige weitere Länder:</strong> Hier kann je nach Landesgesetz auch der Lebensgefährte in die Pflicht genommen werden.</li>',
    '<li><strong>Schleswig-Holstein und Niedersachsen:</strong> Hier kann auch der Partner einer auf Dauer angelegten Lebensgemeinschaft bestattungspflichtig sein.</li>\n      <li><strong>Bayern:</strong> Umgekehrtes Beispiel — der Pflichtigenkreis ist weit (bis zu Geschwistern, Neffen und Nichten), umfasst aber den nichtehelichen Lebensgefährten gerade nicht.</li>')

# MITTEL-1: Solvenz-Vorbehalt im Mythen-Eintrag
rep('Vorrangig bestattungspflichtige Angehörige behalten den Anspruch nach § 74 SGB XII auch dann, wenn ein Dritter erbt — das hat das Bundessozialgericht ausdrücklich klargestellt',
    'Vorrangig bestattungspflichtige Angehörige behalten den Anspruch nach § 74 SGB XII auch dann, wenn ein Dritter erbt — sofern ein Ausgleichsanspruch gegen den Erben nicht realistisch durchsetzbar ist. Das hat das Bundessozialgericht ausdrücklich klargestellt')

# MITTEL-2: SGB II gleichrangig (Zumutbarkeits-Sektion + Schnell-Check)
rep('Wer selbst Sozialhilfe oder Grundsicherung nach SGB XII bezieht, gilt regelmäßig als nicht in der Lage, die Bestattungskosten zu tragen — die Unzumutbarkeit wird in diesen Fällen grundsätzlich anerkannt. Bei Bürgergeld nach SGB II ist es ein starkes Indiz, aber das Sozialamt prüft im Einzelfall.',
    'Wer selbst Sozialhilfe oder Grundsicherung nach SGB XII oder Bürgergeld nach SGB II bezieht, gilt nach der Rechtsprechung des Bundessozialgerichts regelmäßig als nicht in der Lage, die Bestattungskosten zu tragen — die Unzumutbarkeit wird in diesen Fällen grundsätzlich anerkannt.')
rep('<strong>Du beziehst selbst Sozialhilfe oder Grundsicherung (SGB XII)?</strong>\n        <p style="font-size:14px;margin:4px 0 0">Dann wird die Unzumutbarkeit regelmäßig anerkannt — stelle den Antrag. Sammle die Unterlagen aus der Checkliste unten.</p>',
    '<strong>Du beziehst selbst Sozialhilfe, Grundsicherung (SGB XII) oder Bürgergeld (SGB II)?</strong>\n        <p style="font-size:14px;margin:4px 0 0">Dann wird die Unzumutbarkeit nach der BSG-Rechtsprechung regelmäßig anerkannt — stelle den Antrag. Sammle die Unterlagen aus der Checkliste unten.</p>')
rep('''      <div style="background:var(--mr-bg);border:1px solid var(--mr-border);border-radius:10px;padding:14px 18px">
        <strong>Du beziehst Bürgergeld (SGB II) oder lebst von geringem Einkommen ohne verwertbares Vermögen?</strong>
        <p style="font-size:14px;margin:4px 0 0">Starkes Indiz für die Übernahme, aber Einzelfallprüfung — Antrag stellen lohnt sich. Eine Sterbegeld- oder Lebensversicherung der verstorbenen Person wird vorrangig angerechnet.</p>
      </div>''',
    '''      <div style="background:var(--mr-bg);border:1px solid var(--mr-border);border-radius:10px;padding:14px 18px">
        <strong>Du lebst von geringem Einkommen ohne verwertbares Vermögen?</strong>
        <p style="font-size:14px;margin:4px 0 0">Einzelfallprüfung mit guten Chancen — Antrag stellen lohnt sich. Eine Sterbegeld- oder Lebensversicherung der verstorbenen Person wird vorrangig angerechnet.</p>
      </div>''')

# MITTEL-3: Schonvermoegen-Spanne (Fliesstext + FAQ 2x)
rep('Anerkannt wurden Beträge in einer Größenordnung von etwa 8.700 bis 10.500 € — das Verwaltungsgericht Münster hielt rund 10.500 € für angemessen.',
    'Die Rechtsprechung ist dabei nicht einheitlich: Das Verwaltungsgericht Münster hielt rund 10.500 € für angemessen, das OVG Nordrhein-Westfalen (Beschluss vom 25.05.2021, 12 A 2454/18) dagegen nur 7.000 € — je nach Gericht also etwa 7.000 bis 10.500 €.')
rep('Gerichte haben Vorsorgesummen in einer Größenordnung von etwa 8.700 bis 10.500 € als angemessen anerkannt (das Verwaltungsgericht Münster etwa 10.500 €).',
    'Die anerkannte Höhe ist je nach Gericht unterschiedlich — etwa 7.000 € (OVG NRW 2021) bis rund 10.500 € (VG Münster).', 2)

# MITTEL-4: Lead entschaerft
rep('Wenn ein Mensch stirbt und die Angehörigen die Bestattungskosten nicht tragen können, muss niemand die Beisetzung aus eigener Not vorfinanzieren.',
    'Wenn ein Mensch stirbt und die Angehörigen die Bestattungskosten nicht tragen können, soll niemand auf den Kosten einer würdigen Bestattung sitzen bleiben.')

# MITTEL-5: formloser Antrag + Bestatter-Rolle (in Antrag-Sektion, vor Unterlagen-h3)
rep('<h3>Welche Unterlagen werden meist verlangt?</h3>',
    '''<p>Der Antrag ist <strong>formlos möglich</strong> — ein einfaches Schreiben oder eine persönliche Vorsprache genügt; viele Ämter halten eigene Formulare bereit. Und sprich offen mit dem Bestattungsunternehmen darüber, dass ein Antrag nach § 74 SGB XII läuft: Viele Bestatter kennen das Verfahren, bieten einfache Leistungspakete dafür an und vereinbaren eine <strong>Stundung bis zur Entscheidung des Amts</strong> oder rechnen direkt mit dem Sozialamt ab. Das vermeidet Mahnkosten, falls sich die Bearbeitung zieht.</p>
    <h3>Welche Unterlagen werden meist verlangt?</h3>''')

io.open(P, 'w', encoding='utf-8', newline='').write(t)
for s in ['7.000 € (OVG NRW 2021)']:
    assert t.count(s) == 2, s
assert t.count('8.700') == 0
print('R7b sozialbestattung OK')

# --- Hamburg: derselbe Trauerredner-Fehler im §74-Block ---
H = 'bestatter/hamburg/index.html'
th = io.open(H, encoding='utf-8').read()
old = 'Nicht regelmäßig übernommen werden gehobene Särge, Trauerredner, größere Blumenarrangements, Traueranzeigen oder Grabsteine.'
new = 'Nicht regelmäßig übernommen werden gehobene Särge, größere Blumenarrangements, Traueranzeigen oder Grabsteine; ein freier Trauerredner in einfachem Rahmen gehört nach dem Bundessozialgericht dagegen zu den erforderlichen Kosten (BSG, 12.12.2023, B 8 SO 20/22 R).'
assert th.count(old) == 1
io.open(H, 'w', encoding='utf-8', newline='').write(th.replace(old, new, 1))
print('R7b hamburg Trauerredner OK')
