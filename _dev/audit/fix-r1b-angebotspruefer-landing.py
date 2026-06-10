#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R1b (2026-06-10) — Angebotspruefer Landing + Ergebnis-Schaerfung:
B1 Kompakt-Intro vor Tool (3-Schritte + Anker zum Beispiel) |
B2 Statische, crawlbare Sektionen unter dem Tool: Leistungsarten-Dreiteilung,
   Beispiel-Ergebnis mit Ampeln, Pauschalen, Warnsignale |
C1 Empfehlungszeile nach den Ampeln (plausibel/nachfassen/erst klaeren) |
C2 "Bitte beim Bestatter klaeren" -> "Vor der Unterschrift klaeren" |
C3 Folge-CTA "Zweites Angebot einholen" neben Druck-Button.
Beispiel-Zahlen V2-konsistent: Feuerbestattung NRW, konst 2950-5400 +
lokal 550-2100 x 1,36 = 3.700-8.300 EUR (gerundet auf 100).
"""
import io, sys

P = 'tools/angebotspruefer/index.html'

def patch(path, replacements):
    with io.open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()
    for i, (old, new, expect) in enumerate(replacements):
        c = text.count(old)
        if c != expect:
            print('FATAL #%d: %r -> %d (erwartet %d)' % (i, old[:70], c, expect)); sys.exit(1)
        text = text.replace(old, new)
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)
    print('%s: %d Ersetzungen OK' % (path, len(replacements)))

# ===== B1: Kompakt-Intro vor dem Tool =====
INTRO = '''  <div class="no-print" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin:24px 0">
    <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:14px 16px;font-size:14px;line-height:1.5"><strong style="display:block;margin-bottom:4px">1 · Angebot zur Hand</strong><span style="color:var(--mr-text-muted)">Kostenvoranschlag oder Rechnung des Bestatters reicht.</span></div>
    <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:14px 16px;font-size:14px;line-height:1.5"><strong style="display:block;margin-bottom:4px">2 · Posten abhaken</strong><span style="color:var(--mr-text-muted)">Was steht drin, was kommt separat? 5 kurze Schritte.</span></div>
    <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:14px 16px;font-size:14px;line-height:1.5"><strong style="display:block;margin-bottom:4px">3 · Ampel + Fragenliste</strong><span style="color:var(--mr-text-muted)">Neutrale Einschätzung und konkrete Fragen fürs Gespräch. <a href="#ap-beispiel" style="color:var(--mr-primary)">Beispiel ansehen ↓</a></span></div>
  </div>

'''

# ===== B2: Statische Sektionen unter dem Tool =====
STATIC = '''
  <!-- R1b: Statische, crawlbare Erklaer-Sektionen (Landing-Ebene) -->
  <section class="no-print" style="margin:56px 0 0;border-top:1px solid var(--mr-border);padding-top:40px">
    <h2 style="font-family:'Fraunces',serif;font-size:24px;font-weight:700;margin-bottom:8px">So liest du ein Bestatter-Angebot</h2>
    <p style="font-size:15px;color:var(--mr-text-muted);line-height:1.6;max-width:640px;margin-bottom:20px">Jedes seriöse Angebot besteht aus drei Arten von Posten — und nur eine davon ist wirklich vergleichbar:</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px">
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:18px 20px;font-size:14px;line-height:1.6">
        <strong style="display:block;margin-bottom:6px">Bestatterleistungen</strong>
        Beratung, Überführung, Versorgung, Organisation. <strong>Das ist die eigene Leistung des Bestatters</strong> — hier unterscheiden sich Anbieter am stärksten, hier lohnt der Vergleich.
      </div>
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:18px 20px;font-size:14px;line-height:1.6">
        <strong style="display:block;margin-bottom:6px">Friedhofs- und Kommunalgebühren</strong>
        Grabnutzung, Beisetzung, Trauerhalle der Kommune. <strong>Per Gebührensatzung festgelegt</strong> — beim Bestatter nicht verhandelbar, er reicht sie nur durch. Regional sehr unterschiedlich (<a href="/bestattungskosten-nach-bundesland" style="color:var(--mr-primary)">Bundesland-Vergleich</a>).
      </div>
      <div style="background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:18px 20px;font-size:14px;line-height:1.6">
        <strong style="display:block;margin-bottom:6px">Fremdleistungen</strong>
        Krematorium, Blumen, Traueranzeige, Steinmetz. Werden <strong>durchgereicht</strong> — eine saubere Trennung im Angebot ist ein gutes Zeichen für Transparenz.
      </div>
    </div>

    <h2 id="ap-beispiel" style="font-family:'Fraunces',serif;font-size:24px;font-weight:700;margin:40px 0 8px">So sieht ein Ergebnis aus</h2>
    <p style="font-size:15px;color:var(--mr-text-muted);line-height:1.6;max-width:640px;margin-bottom:16px">Beispiel: Feuerbestattung in Nordrhein-Westfalen, Angebot über <strong>5.480 €</strong>, ein Posten nicht eindeutig ausgewiesen. Der vergleichbare Rahmen liegt bei ca. 3.700–8.300 €:</p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:16px 0">
      <div class="ampel-box green" style="margin:0;padding:20px 18px"><div style="font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--mr-text-muted);margin-bottom:6px;font-weight:600">Preis-Einschätzung</div><div class="ampel-icon" style="font-size:28px">✓</div><div class="ampel-title" style="font-size:17px">Preis wirkt plausibel</div><p class="ampel-text" style="font-size:13px">Die Gesamtsumme liegt im üblichen Rahmen für eine Feuerbestattung in NRW.</p></div>
      <div class="ampel-box yellow" style="margin:0;padding:20px 18px"><div style="font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--mr-text-muted);margin-bottom:6px;font-weight:600">Vollständigkeit</div><div class="ampel-icon" style="font-size:28px">?</div><div class="ampel-title" style="font-size:17px">Ein Posten klären</div><p class="ampel-text" style="font-size:13px">Die Überführung war nicht eindeutig ausgewiesen — vor der Unterschrift nachfragen, ob sie im Preis enthalten ist.</p></div>
    </div>
    <p style="font-size:14px;color:var(--mr-text-muted);line-height:1.6;max-width:640px">Dazu bekommst du eine Liste konkreter Fragen für das Bestatter-Gespräch — zum Ausdrucken oder als PDF. <a href="#main" style="color:var(--mr-primary)">Eigenes Angebot prüfen ↑</a></p>

    <h2 style="font-family:'Fraunces',serif;font-size:24px;font-weight:700;margin:40px 0 8px">Pauschalen: legitim — wenn klar ist, was drin ist</h2>
    <p style="font-size:15px;color:var(--mr-text-muted);line-height:1.7;max-width:640px">Ein Komplettpaket oder eine Pauschale ist nicht verdächtig — oft ist sie sogar fair kalkuliert. Entscheidend ist die <strong>Leistungsbeschreibung</strong>: Welche Posten sind enthalten, welche kommen separat dazu (typisch: Friedhofsgebühren, Traueranzeige, Grabstein)? Eine Pauschale ohne Leistungsbeschreibung ist der einzige Fall, in dem du vor der Unterschrift auf einer Aufschlüsselung bestehen solltest. Der Check oben behandelt Pauschalen deshalb als vollständig — und gibt dir die Klärungsfragen mit.</p>

    <h2 style="font-family:'Fraunces',serif;font-size:24px;font-weight:700;margin:40px 0 8px">Vier Signale, bei denen du nachfragen solltest</h2>
    <ul style="list-style:none;padding:0;max-width:640px">
      <li style="padding:10px 0 10px 26px;position:relative;font-size:15px;line-height:1.6;border-bottom:1px solid var(--mr-border)"><span style="position:absolute;left:0;color:var(--mr-accent)">→</span><strong>Nur eine Gesamtsumme</strong>, auch auf Nachfrage keine Posten-Aufschlüsselung.</li>
      <li style="padding:10px 0 10px 26px;position:relative;font-size:15px;line-height:1.6;border-bottom:1px solid var(--mr-border)"><span style="position:absolute;left:0;color:var(--mr-accent)">→</span><strong>Fremdleistungen ohne Trennung:</strong> Krematorium, Friedhofsgebühren oder Anzeigen verschwinden „im Paket" — Durchlaufposten sollten erkennbar sein.</li>
      <li style="padding:10px 0 10px 26px;position:relative;font-size:15px;line-height:1.6;border-bottom:1px solid var(--mr-border)"><span style="position:absolute;left:0;color:var(--mr-accent)">→</span><strong>Zeitdruck</strong> („gilt nur heute") — bei Bestattungen unüblich und unnötig. Du darfst in Ruhe entscheiden.</li>
      <li style="padding:10px 0 10px 26px;position:relative;font-size:15px;line-height:1.6"><span style="position:absolute;left:0;color:var(--mr-accent)">→</span><strong>Mündliche Zusagen</strong>, die nicht im schriftlichen Angebot stehen — bitte schriftlich bestätigen lassen.</li>
    </ul>
    <p style="font-size:13px;color:var(--mr-text-muted);margin-top:12px;max-width:640px">Keines dieser Signale ist ein Beweis für ein schlechtes Angebot — es sind Anlässe für eine Nachfrage. Seriöse Bestatter beantworten sie ohne Zögern.</p>
  </section>

'''

with io.open(P, 'r', encoding='utf-8') as fh:
    t = fh.read()

ANCHOR_BOX = '  <div class="no-print" style="background:var(--mr-safety);border:1px solid var(--mr-border);border-left:4px solid var(--mr-accent);border-radius:8px;padding:16px 20px;margin:24px 0;font-size:14px;line-height:1.6">\n    <strong style="color:var(--mr-text)">Deine Daten bleiben bei dir.</strong>'
assert t.count(ANCHOR_BOX) == 1
t = t.replace(ANCHOR_BOX, INTRO + ANCHOR_BOX, 1)

ANCHOR_MAIN_END = '</main></div>'
assert t.count(ANCHOR_MAIN_END) == 1
t = t.replace(ANCHOR_MAIN_END, STATIC + '</main></div>', 1)

with io.open(P, 'w', encoding='utf-8', newline='') as fh:
    fh.write(t)
print('B1+B2 eingefuegt')

# ===== C: Ergebnis-Schaerfung =====
patch(P, [
    # C1: Empfehlungszeile nach den Ampeln
    ("""    html+='</div>';

    // Was du beim Bestatter klären solltest (Zusammenfassung)""",
     """    html+='</div>';

    // R1b: Gesamt-Empfehlung aus beiden Ampeln
    var empf;
    if(result.priceStatus==='red'||result.completenessStatus==='red'){
      empf='Erst klären, dann entscheiden: Nimm die Fragenliste unten mit ins Gespräch — und hol parallel ein Vergleichsangebot ein.';
    } else if(result.priceStatus==='green'&&result.completenessStatus==='green'){
      empf='Das Angebot wirkt plausibel und vollständig. Nimm die Fragenliste trotzdem mit — und entscheide in Ruhe.';
    } else {
      empf='Mit der Fragenliste unten nachfassen — die offenen Punkte sind schnell geklärt, oft harmlos.';
    }
    html+='<p style="font-size:15px;line-height:1.6;background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:8px;padding:14px 18px;margin-bottom:24px"><strong>Unterm Strich:</strong> '+empf+'</p>';

    // Was du beim Bestatter klären solltest (Zusammenfassung)""", 1),
    # C2: Framing "Vor der Unterschrift klären"
    (">Bitte beim Bestatter klären</h3>'", ">Vor der Unterschrift klären</h3>'", 1),
    # C3: Folge-CTA Zweites Angebot
    ("""html+='<button type="button" class="btn btn-secondary" id="ap-restart">↺ Neues Angebot prüfen</button>';""",
     """html+='<button type="button" class="btn btn-secondary" id="ap-restart">↺ Neues Angebot prüfen</button>';
    html+='<a class="btn btn-secondary" href="/bestatter/" data-next-step="/bestatter/" style="text-decoration:none">Zweites Angebot: Bestatter finden</a>';""", 1),
])
print('FERTIG')
