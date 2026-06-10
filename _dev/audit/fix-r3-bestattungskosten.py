#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R3 (Loop-Iteration 2) — /bestattungskosten zur Money-Page:
1. "individual"-Fehler -> "individuell" (Review-Sofortpunkt).
2. Dreiteilung der Kosten direkt nach Keyfacts — mit Verhandelbar/Fix/
   Durchgereicht-Badges (deckt "Dreiteilung oben" + "verhandelbar vs. fix").
3. Beispielrechnung 3 Stufen aus den PUBLIZIERTEN Modell-Spannen
   (Direktkremation 1.000-2.200 / Feuer-Basis ca. 3.400-8.200 /
   Erd inkl. Grabpflege ca. 5.300-14.300 — alle vor Regionalfaktor,
   konsistent mit Methodik/Angebotspruefer, keine neuen Zahlen).
4. Angebotspruefer-Kontext-Block direkt nach "Die groessten Kostenposten".
5. Sozialbestattung frueh sichtbar: Keyfact-Zeile mit Anker-Link.
"""
import io, sys

P = 'bestattungskosten.html'
t = io.open(P, encoding='utf-8').read()

def rep(old, new, expect=1):
    global t
    c = t.count(old)
    if c != expect:
        print('FATAL: %r -> %d (erwartet %d)' % (old[:70], c, expect)); sys.exit(1)
    t = t.replace(old, new)

# 1. Sprachfehler
rep('Keine pseudo-Präzision: Kosten sind individual und variabel',
    'Keine Pseudo-Präzision: Kosten sind individuell und variabel')

# 5. Sozialbestattung frueh (als Keyfact-Ergaenzung)
rep('<li>Keine Pseudo-Präzision: Kosten sind individuell und variabel</li>',
    '<li>Keine Pseudo-Präzision: Kosten sind individuell und variabel</li>\n      <li>Geld ist knapp? Das Sozialamt kann übernehmen — <a href="/sozialbestattung" style="color:var(--mr-primary)">Sozialbestattung</a></li>')

# 2.+3. Dreiteilung + Beispielrechnung nach dem Keyfacts-/CTA-Block einfuegen
ANCHOR = '''  <div class="mr-cta-block no-print">
    <h2>Deine persönlichen Kosten berechnen</h2>'''
DREITEILUNG = '''  <section class="mr-section">
    <h2>Drei Arten von Kosten — nur eine ist verhandelbar</h2>
    <p>Jede Bestattungsrechnung besteht aus drei Blöcken. Wer sie auseinanderhält, weiß, wo sich Vergleichen lohnt — und wo nicht:</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:16px 0">
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:18px 20px;font-size:14px;line-height:1.6">
        <span style="display:inline-block;font-size:11px;font-weight:700;padding:3px 10px;border-radius:99px;text-transform:uppercase;letter-spacing:.04em;background:rgba(134,110,69,0.12);color:#866E45;margin-bottom:8px">Vergleichbar &amp; verhandelbar</span>
        <strong style="display:block;margin-bottom:4px">Bestatterleistungen</strong>
        Beratung, Überführung, Versorgung, Organisation, Sarg/Urne. Die eigene Leistung des Bestatters — hier unterscheiden sich Anbieter am stärksten. 2–3 Angebote vergleichen lohnt sich fast immer.
      </div>
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:18px 20px;font-size:14px;line-height:1.6">
        <span style="display:inline-block;font-size:11px;font-weight:700;padding:3px 10px;border-radius:99px;text-transform:uppercase;letter-spacing:.04em;background:rgba(94,80,71,0.10);color:#5E5047;margin-bottom:8px">Fix per Satzung</span>
        <strong style="display:block;margin-bottom:4px">Friedhofs- &amp; Kommunalgebühren</strong>
        Grabnutzung, Beisetzung, Trauerhalle. Von der Kommune festgelegt, beim Bestatter nicht verhandelbar — aber stark ortsabhängig. Sparen geht hier nur über Grabart oder Friedhofswahl.
      </div>
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:18px 20px;font-size:14px;line-height:1.6">
        <span style="display:inline-block;font-size:11px;font-weight:700;padding:3px 10px;border-radius:99px;text-transform:uppercase;letter-spacing:.04em;background:rgba(122,107,93,0.10);color:#7A6B5D;margin-bottom:8px">Durchgereicht &amp; wählbar</span>
        <strong style="display:block;margin-bottom:4px">Fremdleistungen</strong>
        Krematorium, Blumen, Traueranzeige, Trauerkaffee, Steinmetz. Werden weitergereicht — bei vielen davon entscheidest du Umfang und Zeitpunkt selbst (Grabstein z.&nbsp;B. oft erst nach Monaten).
      </div>
    </div>

    <h2 style="margin-top:36px">Was kostet es ungefähr? Drei Beispiel-Stufen</h2>
    <p>Modellierte Größenordnungen aus unserem <a href="/methodik#kostenmodell" style="color:var(--mr-primary)">Komponentenmodell</a> (bundesweites Basis-Szenario — dein Bundesland verschiebt vor allem die Friedhofsgebühren, <a href="/bestattungskosten-nach-bundesland" style="color:var(--mr-primary)">hier der Vergleich</a>):</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:16px 0">
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:18px 20px;font-size:14px;line-height:1.6">
        <strong style="display:block">Einfach</strong>
        <span style="font-family:'Fraunces',serif;font-size:22px;font-weight:700;color:var(--mr-text)">ca. 1.000–2.200&nbsp;€</span><br>
        Direktkremation: Einäscherung ohne Trauerfeier, Urne wird beigesetzt oder übergeben. Die günstigste echte Option.
      </div>
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:18px 20px;font-size:14px;line-height:1.6">
        <strong style="display:block">Mittel</strong>
        <span style="font-family:'Fraunces',serif;font-size:22px;font-weight:700;color:var(--mr-text)">ca. 3.400–8.200&nbsp;€</span><br>
        Feuerbestattung mit Urnengrab: Bestatter, Einäscherung, Urne, Friedhofsgebühren, Beisetzung — ohne Grabpflege und große Extras.
      </div>
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:18px 20px;font-size:14px;line-height:1.6">
        <strong style="display:block">Gehoben</strong>
        <span style="font-family:'Fraunces',serif;font-size:22px;font-weight:700;color:var(--mr-text)">ca. 5.300–14.300&nbsp;€</span><br>
        Erdbestattung mit Einzelgrab inkl. Grabpflege über die Ruhezeit — dazu kommen je nach Wunsch Trauerfeier, Grabstein, Anzeigen.
      </div>
    </div>
    <p style="font-size:13px;color:var(--mr-text-muted)">Keine erhobenen Marktpreise — Spannen reichen von „alle Posten am unteren Rand" bis „alle am oberen Rand". Deinen konkreten Rahmen liefert der Kostenrechner.</p>
  </section>

''' + ANCHOR
rep(ANCHOR, DREITEILUNG)

# 4. Angebotspruefer-Block nach den Kostenposten
ANCHOR2 = '''  <section class="mr-section">
    <h2>Regionale Unterschiede — Das große Kostengefälle</h2>'''
AP_BLOCK = '''  <div class="mr-hint no-print" style="margin:8px 0 24px">
    <strong>Du hast schon ein Angebot vor dir?</strong> Dann prüfe es Posten für Posten, bevor du unterschreibst: Der <a href="/tools/angebotspruefer/" style="color:var(--mr-primary)" data-track="cta">Angebotsprüfer</a> vergleicht Preis und Vollständigkeit mit der Spanne deines Bundeslands — Ampel und Fragenliste in 3 Minuten, kostenlos.
  </div>

''' + ANCHOR2
rep(ANCHOR2, AP_BLOCK)

io.open(P, 'w', encoding='utf-8', newline='').write(t)
print('R3 OK: individual-Fix, Sozial-Keyfact, Dreiteilung+Badges, 3-Stufen-Beispiel, Angebotspruefer-Block')
