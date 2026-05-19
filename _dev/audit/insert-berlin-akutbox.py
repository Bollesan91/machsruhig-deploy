#!/usr/bin/env python3
"""Insert Akutbox in bestatter/berlin/index.html — Berlin-spezifisch mit Bezirksstandesamt-Logik."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

fp = 'bestatter/berlin/index.html'
with open(fp, 'r', encoding='utf-8') as f:
    s = f.read()
orig = s

AKUTBOX = '''
  <div class="mr-section" id="akut-todesfall">
    <h2>Was nach einem Todesfall in Berlin zu tun ist — 6 Schritte</h2>
    <p>Wenn ein Angehöriger in Berlin verstirbt, sind die ersten Tage durch enge Fristen und die zwölf Berliner Bezirke geprägt. Wichtig zu wissen: Berlin ist Stadtstaat, hat aber <strong>kein zentrales Sterbe-Standesamt</strong>. Zuständig ist immer das <strong>Bezirksstandesamt des Sterbeorts</strong> — also dort, wo die Person tatsächlich verstorben ist, nicht wo sie gewohnt hat. Das Standesamt I in Berlin (Schönstedtstr. 5, 13357 Berlin) ist nur für Sterbefälle Deutscher im Ausland zuständig (Auslandsstandesamt der Bundesrepublik).</p>

    <ol style="margin-left:20px;margin-top:12px;margin-bottom:12px;line-height:1.8;">
      <li style="margin-bottom:10px;"><strong>Arzt rufen und Totenschein ausstellen lassen.</strong> Bei einem Todesfall zu Hause: ärztlichen Bereitschaftsdienst (116 117) oder Hausarzt verständigen. Im Krankenhaus oder Pflegeheim übernimmt das Personal. Der Arzt stellt den Totenschein (Todesbescheinigung) aus — Voraussetzung für alles Weitere.</li>

      <li style="margin-bottom:10px;"><strong>Bestatter beauftragen.</strong> Berliner Verstorbene müssen nach <strong>§ 15 BestattG BE</strong> innerhalb von <strong>36 Stunden</strong> in eine Leichenhalle oder ein Krematorium überführt werden. Hole nach Möglichkeit zwei bis drei schriftliche Kostenvoranschläge ein. Der Bestatter kann auf Wunsch auch die Sterbefallanzeige beim Standesamt übernehmen.</li>

      <li style="margin-bottom:10px;"><strong>Sterbefall beim Bezirksstandesamt anzeigen.</strong> Die Anzeige muss nach <strong>§ 28 PStG</strong> innerhalb von <strong>drei Werktagen</strong> erfolgen — zuständig ist das Standesamt des Bezirks, in dem die Person verstorben ist (z. B. Standesamt Pankow, wenn der Tod in einem Krankenhaus in Pankow eingetreten ist). Die Sterbeurkunde wird vom selben Bezirksstandesamt ausgestellt. Erforderlich: Totenschein, Personalausweis, Geburtsurkunde, ggf. Heiratsurkunde. Übernimmt das Bestattungsunternehmen meist mit.</li>

      <li style="margin-bottom:10px;"><strong>Friedhof auswählen.</strong> Berlin hat 222 Friedhöfe in <strong>dreifacher Trägerschaft</strong> mit eigenen Gebührenordnungen: 85 landeseigene Friedhöfe (verwaltet durch die Grünflächenämter der zwölf Bezirke), 118 evangelische Gemeindefriedhöfe (EKBO), neun katholische sowie zehn weitere — jüdisch, muslimisch, russisch-orthodoxe und der britische Soldatenfriedhof. Es gibt <strong>keinen Wohnortzwang</strong>; du kannst bezirksübergreifend wählen.</li>

      <li style="margin-bottom:10px;"><strong>Grabart festlegen.</strong> Erd- oder Feuerbestattung, Reihen- oder Wahlgrab, Urnen-, Baum- oder anonyme Beisetzung. Die Gebührenordnungen unterscheiden sich je Bezirk und Träger deutlich. Religiöse Bestattung ohne Sarg (Leichentuch) ist auf bestimmten Grabfeldern aus religiösen Gründen möglich. Die bisherige 48-Stunden-Wartefrist (vormals § 21 BestattG BE) wurde mit der Reform 2024 abgeschafft — muslimische und jüdische Bestattungen können damit zeitnah erfolgen.</li>

      <li style="margin-bottom:10px;"><strong>Trauerfeier organisieren.</strong> Termin mit Friedhof und Bestatter abstimmen, ggf. Trauerredner oder Pfarrer/Imam buchen, Anzeige aufgeben, Trauerkarten versenden. Das BestattG BE nennt keine starre Maximalfrist bis zur Bestattung — in der Praxis koordiniert das zuständige Bezirksamt; üblich sind je nach Bestattungsart wenige Tage bis etwa zwei Wochen.</li>
    </ol>

    <div class="mr-hint">
      <strong>Berliner Besonderheit:</strong> Wer mit dem Sterbebezirk nicht vertraut ist, findet die Adresse des zuständigen Bezirksstandesamts unter <a href="https://service.berlin.de/standorte/standesaemter/" rel="noopener" target="_blank">service.berlin.de — Standesämter</a>. Vertue dich nicht: Eine Anzeige beim falschen Bezirk wird abgewiesen und kostet Tage.
    </div>
  </div>

'''

# Anchor: after end of Keyfacts (</ul></div>), before <h2>Friedhöfe in Berlin
anchor = '    </ul>\n  </div>\n\n  <div class="mr-section">\n    <h2>Friedhöfe in Berlin</h2>'
replace = '    </ul>\n  </div>\n' + AKUTBOX + '  <div class="mr-section">\n    <h2>Friedhöfe in Berlin</h2>'
n = s.count(anchor)
print(f'Anchor (Akutbox): {n}')
if n == 1:
    s = s.replace(anchor, replace)
    print('  AKUTBOX inserted')

if s != orig:
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(s)
    print(f'\nWROTE: {len(orig)} -> {len(s)} bytes (+{len(s)-len(orig)})')
else:
    print('\nNO CHANGES (anchor did not match)')
