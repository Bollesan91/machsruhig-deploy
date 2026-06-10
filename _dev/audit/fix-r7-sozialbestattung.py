#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R7 — /sozialbestattung (Soll lt. Review-Programm: "Oben: 'Wann zahlt
das Sozialamt?', Anspruch/Antrag/Unterlagen/Zustaendigkeit, § 74 verstaendlich,
Unterlagen-Download"). Ist: Inhalt weitgehend stark. Ergaenzt/gefixt wird:
1. Selbst-Check-Block "Zahlt das Sozialamt in deinem Fall?" direkt nach den
   Keyfacts (3 Konstellationen, nur aus bereits belegten Seiten-Aussagen).
2. Druckbare Unterlagen-Checkliste mit Print-Button (visibility-basiertes
   Print-CSS, kein neues Tool) — der "Unterlagen-Download".
3. Stand-Konsistenz: doppelte Meta-Zeile (Mai vs. Juni) -> eine Zeile Juni 2026;
   Quellen-Stand Juni; dateModified 2026-06-10.
4. BL-Links direkt statt ueber 301-Redirect.
"""
import io, sys

P = 'sozialbestattung.html'
t = io.open(P, encoding='utf-8').read()

def rep(old, new, expect=1):
    global t
    c = t.count(old)
    if c != expect:
        print('FATAL: %r -> %d (erwartet %d)' % (old[:70], c, expect)); sys.exit(1)
    t = t.replace(old, new)

# --- 3. Stand-Konsistenz ---
rep('"dateModified":"2026-06-01"', '"dateModified":"2026-06-10"')
rep('''    <p class="meta">Lesezeit ca. 9 Min · Stand Mai 2026</p>
    <p class="meta byline">Erstellt von machsruhig.de Redaktion · Stand: Juni 2026</p>''',
    '''    <p class="meta">Redaktion machsruhig.de · Lesezeit ca. 9 Min · Stand: Juni 2026</p>''')
rep('Eigene Aufbereitung Stand Mai 2026 auf Basis', 'Eigene Aufbereitung Stand Juni 2026 auf Basis')

# --- 4. Direkte BL-Links ---
rep('href="/bestatter-in-nordrhein-westfalen"', 'href="/bestattung-in/nordrhein-westfalen/"')
rep('href="/bestatter-in-bayern"', 'href="/bestattung-in/bayern/"')

# --- 1. Selbst-Check nach den Keyfacts ---
KEYFACTS_END = '''      <li>Die übernommenen Kosten liegen in der Praxis oft bei 1.500–3.500 €, variieren aber stark mit den kommunalen Friedhofsgebühren.</li>
    </ul>
  </div>'''
SELBSTCHECK = KEYFACTS_END + '''

  <section class="mr-section" id="schnellcheck" style="background:var(--mr-bg-card);border:2px solid var(--mr-accent);border-radius:var(--mr-radius);padding:24px 28px">
    <h2 style="border-bottom:none;padding-bottom:0;margin-bottom:8px">Zahlt das Sozialamt in deinem Fall? Der Schnell-Check</h2>
    <p style="font-size:14px;color:var(--mr-text-muted);margin-bottom:14px">Entscheidend ist die wirtschaftliche Lage der Person, die zahlen müsste — also deine, wenn du erbst oder bestattungspflichtig bist. Nicht die der verstorbenen Person.</p>
    <div style="display:grid;gap:10px">
      <div style="background:var(--mr-bg);border:1px solid var(--mr-border);border-radius:10px;padding:14px 18px">
        <strong>Du beziehst selbst Sozialhilfe oder Grundsicherung (SGB XII)?</strong>
        <p style="font-size:14px;margin:4px 0 0">Dann wird die Unzumutbarkeit regelmäßig anerkannt — stelle den Antrag. Sammle die Unterlagen aus der Checkliste unten.</p>
      </div>
      <div style="background:var(--mr-bg);border:1px solid var(--mr-border);border-radius:10px;padding:14px 18px">
        <strong>Du beziehst Bürgergeld (SGB II) oder lebst von geringem Einkommen ohne verwertbares Vermögen?</strong>
        <p style="font-size:14px;margin:4px 0 0">Starkes Indiz für die Übernahme, aber Einzelfallprüfung — Antrag stellen lohnt sich. Eine Sterbegeld- oder Lebensversicherung der verstorbenen Person wird vorrangig angerechnet.</p>
      </div>
      <div style="background:var(--mr-bg);border:1px solid var(--mr-border);border-radius:10px;padding:14px 18px">
        <strong>Du hast mittleres oder höheres Einkommen?</strong>
        <p style="font-size:14px;margin:4px 0 0">Dann ist eine Übernahme unwahrscheinlich — bei besonderen Belastungen ist im Einzelfall eine teilweise Übernahme möglich. Den Kostenrahmen senken hilft trotzdem: <a href="/tools/bestattungskosten-rechner/" style="color:var(--mr-primary)">Kostenrechner</a> und <a href="/tools/angebotspruefer/" style="color:var(--mr-primary)">Angebotsprüfer</a>.</p>
      </div>
    </div>
  </section>'''
rep(KEYFACTS_END, SELBSTCHECK)

# --- 2. Druckbare Unterlagen-Checkliste (ersetzt die einfache ul in der Antrag-Sektion nicht,
#     sondern ergaenzt sie um ein Druck-Artefakt direkt darunter) ---
ANCHOR = '''    <p>Die Bearbeitung kann mehrere Wochen dauern. Wer früh den Kontakt sucht und vollständige Unterlagen einreicht, beschleunigt das Verfahren in der Regel.</p>'''
CHECKLISTE = ANCHOR + '''
    <div id="unterlagen-checkliste" style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:20px 24px;margin:16px 0">
      <h3 style="margin-top:0">Unterlagen-Checkliste für den Antrag</h3>
      <ul style="list-style:none;margin:12px 0;padding:0;font-size:14.5px;line-height:2">
        <li>☐ Sterbeurkunde</li>
        <li>☐ Kostenvoranschlag oder Rechnung des Bestatters</li>
        <li>☐ Einkommensnachweise der antragstellenden Person (z.&nbsp;B. Lohnabrechnung, Renten- oder Leistungsbescheid)</li>
        <li>☐ Vermögensnachweise / Kontoauszüge der letzten Monate</li>
        <li>☐ Falls vorhanden: Bescheid über SGB-II- oder SGB-XII-Leistungen</li>
        <li>☐ Falls erfolgt: Nachweis über die Erbausschlagung (Nachlassgericht)</li>
        <li>☐ Falls verlangt: Mietvertrag, weitere Belege zur wirtschaftlichen Lage</li>
        <li>☐ Falls vorhanden: Nachweise zu Sterbegeld- oder Lebensversicherung der verstorbenen Person (wird vorrangig angerechnet)</li>
      </ul>
      <p style="font-size:13.5px;color:var(--mr-text-muted);margin:10px 0">Zuständig: Sozialamt am Sterbeort — bezog die verstorbene Person zuletzt Sozialhilfe, der bisherige Leistungsträger. Notiere dir hier Amt, Aktenzeichen und Ansprechperson:</p>
      <p style="font-size:14px;line-height:2.2;margin:0">Sozialamt: ______________________________ &nbsp; Telefon: ____________________<br>Aktenzeichen: ____________________ &nbsp; Ansprechperson: ____________________</p>
      <button type="button" class="no-print" onclick="document.body.classList.add('print-checkliste');window.print();" style="margin-top:16px;background:var(--mr-primary);color:#fff;border:none;border-radius:99px;padding:10px 24px;font-size:14px;font-weight:600;cursor:pointer;font-family:inherit">🖨️ Checkliste drucken / als PDF speichern</button>
    </div>'''
rep(ANCHOR, CHECKLISTE)

# Print-CSS + afterprint-Cleanup
rep('</style>', '''@media print{
  body.print-checkliste *{visibility:hidden}
  body.print-checkliste #unterlagen-checkliste, body.print-checkliste #unterlagen-checkliste *{visibility:visible}
  body.print-checkliste #unterlagen-checkliste{position:absolute;top:0;left:0;width:100%;border:none}
}
</style>''')
rep('</body>', '''<script>window.addEventListener('afterprint',function(){document.body.classList.remove('print-checkliste');});</script>
</body>''')

io.open(P, 'w', encoding='utf-8', newline='').write(t)

# Sanity
# Footer-Hinweis "Landesgesetze aller 16 BL (Stand Mai 2026)" ist site-weites
# Template und bezieht sich auf den Pruefstand der Gesetze — bleibt.
assert t.count('Stand Mai 2026') == 1, 'unerwartete Mai-Stand-Treffer'
assert t.count('schnellcheck') == 1 and t.count('unterlagen-checkliste') >= 3
print('R7 OK: Schnell-Check + Druck-Checkliste + Stand-Konsistenz + Direktlinks')
