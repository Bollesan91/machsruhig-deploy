#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Audit #16: Sterbegeldversicherung wirtschaftliche Neutralitaet.
# Primaerquelle Verbraucherzentrale ("rechnen sich oft nicht"): bei Abschluss im/kurz vor
# Rentenalter uebersteigen Beitraege oft die Leistung. Aktuelle Seite empfahl sie aber
# gerade "Aeltere 60+" -> korrigieren + prominenter Warnhinweis + Quellen. Asserts vor Write.
import io, sys
p = "vorsorge/sterbegeldversicherung/index.html"
s = io.open(p, encoding="utf-8").read()

WARN = '''  <div class="mr-hint" style="border-left-color:#a33">
    <strong>Wichtig — vorher nachrechnen:</strong> Verbraucherschützer bewerten Sterbegeldversicherungen kritisch. Die Verbraucherzentrale rät ausdrücklich: „Im Rentenalter oder kurz davor sollten Sie keine Sterbegeldversicherung abschließen" — denn „gerade bei Älteren sind schnell mehr Beiträge geflossen als die Hinterbliebenen im Todesfall erhalten". Der Beitrag steigt mit dem Sterberisiko, also mit dem Alter.
    <br><br>
    <strong>Rechenbeispiel (mit den Beitragswerten weiter unten):</strong> Wer mit 65 rund 70 € im Monat für 7.500 € einzahlt (Tarif ohne Gesundheitsfragen), hat nach etwa 9 Jahren so viel eingezahlt, wie die Angehörigen später ausgezahlt bekommen — wer länger lebt, zahlt unterm Strich drauf. Die durchschnittliche fernere Lebenserwartung mit 65 liegt deutlich über 9 Jahren. Für gesunde, jüngere Menschen mit dem günstigeren Tarif „mit Gesundheitsfragen" fällt die Rechnung freundlicher aus.
    <br><br>
    Oft günstiger als die Versicherung: zweckgebunden auf ein Tages-, Festgeld- oder Banksparplankonto sparen, oder ein <a href="/vorsorge/bestattungsvorsorge/">Bestattungsvorsorgevertrag mit Treuhandkonto</a>. Wirklich sinnvoll ist die Versicherung vor allem dann, wenn Vorerkrankungen andere Wege versperren und dir eine garantierte, sofort feststehende Auszahlung wichtig ist.
  </div>

'''

pairs = [
# 1) Warnbox vor "Was ist"-Abschnitt einfuegen
('''  <section class="mr-section">
    <h2>Was ist eine Sterbegeldversicherung?</h2>''',
 WARN + '''  <section class="mr-section">
    <h2>Was ist eine Sterbegeldversicherung?</h2>'''),

# 2) Einseitigen "praktische Loesung"-Verkauf ausbalancieren
('Eine Sterbegeldversicherung bietet daher eine praktische Lösung: Kleine Beiträge monatlich, großer Schutz im Todesfall.',
 'Eine Sterbegeldversicherung kann hier eine Lösung sein — kleine Beiträge monatlich, eine garantierte Auszahlung im Todesfall. Ob sie sich rechnet, hängt aber stark vom Eintrittsalter ab (siehe Warnhinweis oben): Für viele Ältere ist zweckgebundenes Sparen oder ein Bestattungsvorsorgevertrag am Ende günstiger.'),

# 3) "Besonders sinnvoll fuer" ehrlich (kein Blanket-"Aeltere 60+"/"Rentner")
('''    <h3>Besonders sinnvoll für:</h3>

    <ul style="margin:12px 0;padding-left:20px;color:var(--mr-text);">
      <li><strong>Rentner mit kleinen Ersparnissen:</strong> Sparen ist schwer, Versicherung erzwingt regelmäßige Zahlung</li>
      <li><strong>Ältere Menschen (60+ Jahre):</strong> Lebenserwartung sinkt, aber Bestattungskosten steigen. Schneller Schutz wichtig.</li>
      <li><strong>Menschen mit Vorerkrankungen:</strong> Versicherung ohne Gesundheitsfragen ist oft die einzige Option</li>
      <li><strong>Alleinlebende ohne Familie:</strong> Die Angehörigen sollen finanzielle Last nicht tragen</li>
      <li><strong>Menschen mit Bürgergeld/Sozialhilfe:</strong> Schonvermögen-Regel macht Versicherung attraktiv</li>
      <li><strong>Freiberufler/Selbstständige:</strong> Meist keine betriebliche Altersvorsorge, Risiko höher</li>
    </ul>''',
 '''    <h3>Besonders sinnvoll für:</h3>

    <ul style="margin:12px 0;padding-left:20px;color:var(--mr-text);">
      <li><strong>Menschen mit Vorerkrankungen:</strong> Der Tarif ohne Gesundheitsfragen akzeptiert auch, wer für eine normale Risikolebensversicherung abgelehnt würde — oft der einzige verbliebene Weg zu einer garantierten Auszahlung.</li>
      <li><strong>Wer eine sofort feststehende Summe will:</strong> Die Auszahlung steht (nach Ablauf einer etwaigen Wartezeit) vom Vertrag an fest — anders als beim Ansparen, das erst über Jahre wächst.</li>
      <li><strong>Alleinlebende ohne Angehörige:</strong> Damit im Todesfall niemand unvorbereitet die Kosten tragen muss (Alternative: Bestattungsvorsorgevertrag mit Treuhandkonto).</li>
      <li><strong>Bei Bürgergeld/Grundsicherung:</strong> Eine angemessene, zweckgebundene Vorsorge zählt als geschütztes Schonvermögen (§ 90 Abs. 3 SGB XII) — aber nur in angemessener Höhe.</li>
    </ul>

    <p style="font-size:14px;color:var(--mr-text-muted)">Für <strong>gesunde Ältere ohne akute Geldnot</strong> ist die Versicherung dagegen selten die günstigste Lösung — hier lohnt der Vergleich mit zweckgebundenem Sparen (siehe Warnhinweis oben).</p>'''),

# 4) "Weniger sinnvoll fuer" um den VZ-Kernpunkt erweitern
('''    <ul style="margin:12px 0;padding-left:20px;color:var(--mr-text);">
      <li><strong>Junge Menschen (unter 35):</strong> Einfacher, selbst zu sparen; Versicherung dauert 30+ Jahre</li>
      <li><strong>Menschen mit hohen Ersparnissen (über 15.000 €):</strong> Versicherung nicht nötig</li>
      <li><strong>Menschen mit starkem Netzwerk/Familie:</strong> Falls Familie bereits finanzielle Last tragen würde</li>
    </ul>''',
 '''    <ul style="margin:12px 0;padding-left:20px;color:var(--mr-text);">
      <li><strong>Wer im oder kurz vor dem Rentenalter abschließt:</strong> Hier übersteigen die eingezahlten Beiträge häufig die spätere Auszahlung — die Verbraucherzentrale rät in dieser Konstellation ausdrücklich ab.</li>
      <li><strong>Wer stattdessen zweckgebunden sparen kann:</strong> Tages-/Festgeld- oder Banksparplankonto bzw. ein Bestattungsvorsorgevertrag mit Treuhandkonto sind meist günstiger und flexibler.</li>
      <li><strong>Junge Menschen (unter 35):</strong> Einfacher, selbst zu sparen; die Versicherung läuft sonst 30+ Jahre.</li>
      <li><strong>Menschen mit ausreichenden Ersparnissen:</strong> Wer die Bestattungskosten aus Rücklagen decken kann, braucht keine Versicherung.</li>
      <li><strong>Menschen mit tragfähigem Familiennetz:</strong> Wenn Angehörige die Kosten ohnehin problemlos übernehmen würden.</li>
    </ul>'''),

# 5) Quelle Verbraucherzentrale konkretisieren
('<li>Verbraucherzentrale Deutschland — Sterbegeldversicherung FAQ</li>',
 '<li>Verbraucherzentrale — „Sterbegeldversicherungen rechnen sich oft nicht" (verbraucherzentrale.de, geprüft 07/2026)</li>'),

# 6) Trust-Hinweis: Verbraucherschutz-Quellen zuerst nennen (Balance)
('auf Basis von Publikationen des Verbandes der Versicherungswirtschaft, des DIA und der Stiftung Warentest zusammengestellt.',
 'auf Basis von Publikationen der Stiftung Warentest, der Verbraucherzentrale, des Verbandes der Versicherungswirtschaft und des DIA zusammengestellt.'),
]

for i, (old, new) in enumerate(pairs, 1):
    c = s.count(old)
    assert c == 1, "EDIT %d: erwartet 1, gefunden %d\n  %r" % (i, c, old[:70])
for old, new in pairs:
    s = s.replace(old, new)
io.open(p, "w", encoding="utf-8").write(s)
print("OK: 6 Edits angewandt, Warnbox + 2 Listen korrigiert + 2 Quellen-Fixes")
