#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R9 — /beerdigung-planen "Entscheidungsnavigator statt Ratgeber":
1. Navigator-Block nach den Keyfacts: JETZT entscheiden / kann warten /
   was die Kosten treibt — mit Angebotspruefer prominent (CTA-Kompass).
2. Angebotspruefer-Hinweis in der Kosten-Sektion (war auf der Seite KOMPLETT
   unverlinkt).
3. Kosten-Konsistenz mit der Money-Page (kanonische Komponentensummen):
   Tabelle (mit Grabpflege, da eigene Spalte "Grabpflege: Ja"), Keyfacts,
   FAQ sichtbar UND JSON-LD (hier nicht zeichengleich -> separate Replaces).
4. Faktenfehler 48h: nicht "in allen Bundeslaendern" (Hamburg kennt keine
   starre Mindestfrist — steht auf unserer eigenen Hamburg-Seite).
5. Kostenrechner-Link auf das Tool statt auf die Money-Page; Stand/Datum.
"""
import io, sys

P = 'beerdigung-planen.html'
t = io.open(P, encoding='utf-8').read()

def rep(old, new, expect=1):
    global t
    c = t.count(old)
    if c != expect:
        print('FATAL: %r -> %d (erwartet %d)' % (old[:70], c, expect)); sys.exit(1)
    t = t.replace(old, new)

# --- 5. Stand/Datum ---
rep('"datePublished":"2026-04-01","dateModified":"2026-04-01"', '"datePublished":"2026-04-01","dateModified":"2026-06-11"')
rep('<span>Stand: April 2026</span>', '<span>Stand: Juni 2026</span>')

# --- 3a. Keyfacts ---
rep('<li>Die Kosten reichen von ca. 2.000 € (einfache Urne) bis über 15.000 €</li>',
    '<li>Die Kosten reichen von rund 1.000 € (Direktkremation ohne Feier) bis über 14.000 €</li>')

# --- 1. Entscheidungsnavigator nach den Keyfacts ---
NAV = '''  <section class="mr-section" id="entscheidungsnavigator" style="background:var(--mr-bg-card);border:2px solid var(--mr-accent);border-radius:var(--mr-radius);padding:24px 28px">
    <h2 style="border-bottom:none;padding-bottom:0;margin-bottom:8px">Was musst du wann entscheiden?</h2>
    <p style="font-size:14px;color:var(--mr-text-muted);margin-bottom:14px">Nicht alles muss sofort entschieden werden — und nicht alles kostet gleich viel. Dieser Überblick sortiert die Entscheidungen, bevor du in die Details gehst.</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">
      <div style="background:var(--mr-bg);border:1px solid var(--mr-border);border-radius:10px;padding:16px 18px">
        <strong style="display:block;margin-bottom:8px">In den ersten Tagen entscheiden</strong>
        <ul style="font-size:13.5px;line-height:1.7;margin:0;padding-left:18px">
          <li>Bestatter beauftragen — vorher 2–3 Angebote einholen</li>
          <li>Erd- oder Feuerbestattung — bestimmt fast alles Weitere</li>
          <li>Beisetzungsort grob festlegen (Friedhof, See, Wald)</li>
        </ul>
      </div>
      <div style="background:var(--mr-bg);border:1px solid var(--mr-border);border-radius:10px;padding:16px 18px">
        <strong style="display:block;margin-bottom:8px">Kann warten</strong>
        <ul style="font-size:13.5px;line-height:1.7;margin:0;padding-left:18px">
          <li>Grabstein — oft erst nach Monaten nötig</li>
          <li>Danksagungen — Wochen Zeit</li>
          <li>Endgültige Grabgestaltung und Dauergrabpflege</li>
          <li>Details der Trauerfeier — bis kurz vor dem Termin</li>
        </ul>
      </div>
      <div style="background:var(--mr-bg);border:1px solid var(--mr-border);border-radius:10px;padding:16px 18px">
        <strong style="display:block;margin-bottom:8px">Das treibt die Kosten</strong>
        <ul style="font-size:13.5px;line-height:1.7;margin:0;padding-left:18px">
          <li>Bestattungsart (Erd- teurer als Feuerbestattung)</li>
          <li>Sarg-/Urnen-Qualität</li>
          <li>Wahlgrab statt Reihengrab</li>
          <li>Umfang der Trauerfeier</li>
          <li>Grabpflege über die Jahre</li>
        </ul>
      </div>
    </div>
    <p style="font-size:14px;margin:14px 0 0">Liegt dir schon ein Bestatter-Angebot vor? Der <a href="/tools/angebotspruefer/" data-track="cta" style="color:var(--mr-primary);font-weight:600">Angebotsprüfer</a> zeigt in 3&nbsp;Minuten mit einer Ampel, ob Posten und Preise plausibel sind — bevor du unterschreibst.</p>
  </section>

'''
rep('  <div class="mr-cta-block no-print">\n    <h2>Beerdigung planen — mit Unterstützung</h2>', NAV + '  <div class="mr-cta-block no-print">\n    <h2>Beerdigung planen — mit Unterstützung</h2>')

# --- 3b. Bestattungsarten-Tabelle auf kanonische Spannen (inkl. Grabpflege wo "Ja") ---
rep('<tr><td><strong>Erdbestattung</strong></td><td>5.000–15.000 €</td><td>Ja</td><td>Klassisch, Sarg, Friedhof</td></tr>',
    '<tr><td><strong>Erdbestattung</strong></td><td>5.300–14.300 €</td><td>Ja</td><td>Klassisch, Sarg, Friedhof (inkl. Grabpflege)</td></tr>')
rep('<tr><td><strong>Feuerbestattung</strong></td><td>2.000–8.000 €</td><td>Je nach Ort</td><td>Häufigste Form (75 %)</td></tr>',
    '<tr><td><strong>Feuerbestattung</strong></td><td>3.400–9.700 €</td><td>Je nach Ort</td><td>Häufigste Form; Direktkremation ohne Feier ab ca. 1.000 €</td></tr>')
rep('<tr><td><strong>Seebestattung</strong></td><td>3.000–6.000 €</td><td>Nein</td><td>Verfügung nötig</td></tr>',
    '<tr><td><strong>Seebestattung</strong></td><td>2.850–6.200 €</td><td>Nein</td><td>Beisetzung der Urne auf See</td></tr>')
rep('<tr><td><strong>Waldbestattung</strong></td><td>2.500–7.000 €</td><td>Nein</td><td>Urne am Baum</td></tr>',
    '<tr><td><strong>Waldbestattung</strong></td><td>3.050–7.000 €</td><td>Nein</td><td>Urne am Baum</td></tr>')
rep('<tr><td><strong>Kolumbarium</strong></td><td>2.000–5.000 €</td><td>Nein</td><td>Urnenwand</td></tr>',
    '<tr><td><strong>Kolumbarium</strong></td><td>wie Feuerbestattung</td><td>Nein</td><td>Urnenwand statt Grab — Stellplatzgebühr je Friedhof</td></tr>')
rep('Eine ausführliche Beschreibung aller Bestattungsarten findest du auf unserer Seite',
    'Spannen = bundesweite Komponentensummen unseres Kostenmodells (Details in der <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Methodik</a>); regional kann es deutlich abweichen. Eine ausführliche Beschreibung aller Bestattungsarten findest du auf unserer Seite')

# --- 3c. FAQ sichtbar + JSON-LD (nicht zeichengleich -> einzeln) ---
rep('"text":"Je nach Bestattungsart zwischen 2.000 und 15.000 Euro. Feuerbestattung ab ca. 2.000 €, Erdbestattung im Schnitt 6.000–10.000 €."',
    '"text":"Je nach Bestattungsart zwischen rund 1.000 € (Direktkremation ohne Feier) und über 14.000 €. Eine Feuerbestattung mit Feier liegt meist bei 3.400–8.200 €, eine Erdbestattung inklusive Grabpflege bei 5.300–14.300 €."')
rep('<p>Je nach Bestattungsart zwischen 2.000 und 15.000 Euro. Eine einfache Feuerbestattung beginnt ab ca. 2.000 €, eine Erdbestattung mit Sarg und Grabstein kostet im Schnitt 6.000–10.000 €.</p>',
    '<p>Je nach Bestattungsart zwischen rund 1.000 € (Direktkremation ohne Feier) und über 14.000 €. Eine Feuerbestattung mit Feier liegt meist bei 3.400–8.200 €, eine Erdbestattung inklusive Grabpflege bei 5.300–14.300 €.</p>')

# --- 3d. Kosten-Sektion: Text + Tool-Link + Angebotspruefer ---
rep('Eine einfache Feuerbestattung kann ab 2.000 € möglich sein, eine klassische Erdbestattung mit Sarg, Grabstein und Grabpflege kostet schnell 10.000 € und mehr. Für eine individuelle Kostenschätzung nutze unseren <a href="/bestattungskosten" style="color:var(--mr-primary)">Kostenrechner</a>.',
    'Eine Direktkremation ohne Feier beginnt bei rund 1.000 €, eine klassische Erdbestattung mit Sarg, Grabstein und Grabpflege kostet schnell 10.000 € und mehr. Für eine individuelle Schätzung nutze den <a href="/tools/bestattungskosten-rechner/" style="color:var(--mr-primary)">Bestattungskosten-Rechner</a>; die Spannen im Detail erklärt die Seite <a href="/bestattungskosten" style="color:var(--mr-primary)">Bestattungskosten</a>.')
rep('<strong>Wichtig:</strong> Lass dir vom Bestatter ein detailliertes, schriftliches Angebot geben. Frage nach, was inkludiert ist und welche Posten extra anfallen. Seriöse Bestatter machen das transparent.',
    '<strong>Wichtig:</strong> Lass dir vom Bestatter ein detailliertes, schriftliches Angebot geben. Frage nach, was inkludiert ist und welche Posten extra anfallen. Seriöse Bestatter machen das transparent. Und bevor du unterschreibst: Der <a href="/tools/angebotspruefer/" style="color:var(--mr-primary);font-weight:600">Angebotsprüfer</a> sortiert die Posten und zeigt dir mit einer Ampel, ob die Summe im üblichen Rahmen liegt.')

# --- 4. 48h-Faktenfehler ---
rep('Das Bestattungsrecht ist in Deutschland Ländersache. Die wichtigste Regel: In allen Bundesländern darf eine Bestattung frühestens 48 Stunden nach dem Tod stattfinden. Die Höchstfrist variiert je nach Bundesland zwischen 4 Tagen (Baden-Württemberg, Bayern) und 10 Tagen (Berlin, Brandenburg, NRW).',
    'Das Bestattungsrecht ist in Deutschland Ländersache. In den meisten Bundesländern gilt eine Mindestwartezeit vor der Bestattung (häufig 48 Stunden); einzelne Länder — etwa Hamburg — kennen keine starre Mindestfrist. Die Höchstfrist für die Erdbestattung variiert je nach Bundesland zwischen 4 Tagen (z. B. Bayern) und 10 Tagen oder mehr (z. B. Berlin, Brandenburg, Hamburg, NRW).')

io.open(P, 'w', encoding='utf-8', newline='').write(t)
assert t.count('angebotspruefer') >= 3
print('R9 OK: Navigator + Angebotspruefer + Kosten-Konsistenz + 48h-Fix')
