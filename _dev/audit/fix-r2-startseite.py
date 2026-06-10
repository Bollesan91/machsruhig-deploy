#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roadmap R2 (2026-06-10, Loop-Iteration 1) — Startseite "Produkt statt Portal":
1. Hero: Marken-H1 bleibt, Lead auf Kern-Nutzen zugespitzt + 2 Hero-CTAs
   (Angebot pruefen / Kosten berechnen) + Akut-Link zur Checkliste.
2. Hauptpfade zuerst: Kartenreihenfolge Angebotspruefer -> Rechner -> Checkliste
   -> Rest (Vorsorge/Trauer rutschen nach hinten).
3. Trust-Strip direkt unter dem Karten-Grid (Browser-lokal, unabhaengig,
   keine Weitergabe ohne Einwilligung, offene Methodik).
4. Neue Sektion "So funktioniert machsruhig" (3 Schritte) mit Mini-Ampel-
   Beispiel aus dem Angebotspruefer (Link auf #ap-beispiel).
QUICK-WIN (Weg B): Vorsorge-Hub-Kachel entfernt, die faelschlich
"Vorsorgevollmacht" hiess und auf den Kommt-bald-Vorsorge-Ordner zeigte.
"""
import io, re, sys

def load(p):
    return io.open(p, encoding='utf-8').read()

def save(p, t):
    io.open(p, 'w', encoding='utf-8', newline='').write(t)

# ===== Startseite =====
P = 'index.html'
t = load(P)

# --- 1. Hero ---
OLD_LEAD = '''    <p class="mr-lead">
      Unabhängiger Wegweiser, um <strong>Vorsorge</strong> in Ruhe zu regeln, einen <strong>Trauerfall</strong> Schritt für Schritt zu bewältigen und eine <strong>Bestattung</strong> ohne Verkaufsdruck zu planen. In deinem Tempo. Nur was du wirklich brauchst, wenn du es brauchst.
    </p>
  </header>'''
NEW_LEAD = '''    <p class="mr-lead">
      Unabhängiger Wegweiser für <strong>Trauerfall, Bestattung und Vorsorge</strong>: Versteh, was eine Bestattung kostet, prüfe das Angebot des Bestatters — und entscheide in Ruhe, <strong>bevor du etwas unterschreibst</strong>. Kostenlos, ohne Anmeldung, ohne Verkaufsdruck.
    </p>
    <div class="mr-hero-ctas">
      <a href="/tools/angebotspruefer/" class="mr-btn mr-btn-primary" data-track="cta">Bestatter-Angebot prüfen</a>
      <a href="/tools/bestattungskosten-rechner/" class="mr-btn mr-btn-secondary" data-track="cta">Kosten berechnen</a>
    </div>
    <p class="mr-hero-akut">Akuter Todesfall? <a href="/tools/checkliste-todesfall/">Zur Checkliste — was jetzt zu tun ist →</a></p>
  </header>'''
assert t.count(OLD_LEAD) == 1
t = t.replace(OLD_LEAD, NEW_LEAD, 1)

# Hero-CTA-Styles in den Page-Style-Block
CSS_ANCHOR = '.mr-section-title{'
NEW_CSS = '''.mr-hero-ctas{display:flex;gap:12px;flex-wrap:wrap;margin:20px 0 10px}
.mr-btn{display:inline-block;padding:12px 22px;border-radius:8px;text-decoration:none;font-size:15px;font-weight:600;transition:background 0.2s,border-color 0.2s}
.mr-btn-primary{background:var(--mr-primary);color:#fff}
.mr-btn-primary:hover{background:var(--mr-primary-hover,#6d5a38)}
.mr-btn-secondary{background:var(--mr-bg-card);color:var(--mr-text);border:2px solid var(--mr-border)}
.mr-btn-secondary:hover{border-color:var(--mr-primary)}
.mr-hero-akut{font-size:14px;color:var(--mr-text-muted)}
.mr-hero-akut a{color:var(--mr-primary)}
.mr-trust-strip{display:flex;flex-wrap:wrap;gap:8px 24px;margin:22px 4px 0;font-size:13.5px;color:var(--mr-text-muted)}
.mr-trust-strip span::before{content:"✓ ";color:var(--mr-primary);font-weight:700}
.mr-steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}
.mr-step{background:var(--mr-bg-card);border:1px solid var(--mr-border);border-radius:var(--mr-radius);padding:20px 22px;font-size:14.5px;line-height:1.6}
.mr-step .num{display:inline-block;width:26px;height:26px;border-radius:50%;background:var(--mr-primary);color:#fff;text-align:center;line-height:26px;font-weight:700;font-size:14px;margin-bottom:8px}
.mr-mini-ampel{display:inline-flex;align-items:center;gap:8px;background:#f0f6f0;border:1px solid #cce0cc;border-radius:8px;padding:6px 12px;font-size:13px;margin-top:10px}
.mr-section-title{'''
assert t.count(CSS_ANCHOR) == 1
t = t.replace(CSS_ANCHOR, NEW_CSS, 1)

# --- 2. Karten-Reihenfolge ---
cards = re.findall(r'<a href="[^"]*" class="mr-card">.*?</a>', t, re.S)
assert len(cards) == 9, len(cards)
def href(c):
    return re.match(r'<a href="([^"]*)"', c).group(1)
order = ['/tools/angebotspruefer/', '/tools/bestattungskosten-rechner/', '/tools/checkliste-todesfall/',
         '/beerdigung-planen', '/bestattungsarten', '/trauerrede-schreiben', '/kondolenzschreiben',
         '/vorsorge/', '/bestatter/']
by = {href(c): c for c in cards}
assert set(by) == set(order), set(by) ^ set(order)
grid_start = t.find('<div class="mr-grid">')
sect_end = t.find('</section>', grid_start)
assert grid_start > 0 and sect_end > grid_start
TRUST = '''    <div class="mr-trust-strip">
      <span>Kostenlos, ohne Anmeldung</span>
      <span>Rechner &amp; Checks laufen in deinem Browser</span>
      <span>Unabhängig — keine Weitergabe ohne deine Einwilligung</span>
      <span><a href="/methodik" style="color:var(--mr-primary)">Offene Methodik &amp; Quellen</a></span>
    </div>
  '''
new_grid = '<div class="mr-grid">\n\n      ' + '\n\n      '.join(by[h] for h in order) + '\n\n    </div>\n' + TRUST
t = t[:grid_start] + new_grid + t[sect_end:]

# --- 4. So-funktioniert-Sektion vor der Staedte-Sektion ---
ST_ANCHOR = '  <section aria-labelledby="staedte-heading" style="margin-top:64px">'
SOFUNKT = '''  <section aria-labelledby="sofunkt-heading" style="margin-top:56px">
    <h2 id="sofunkt-heading" class="mr-section-title">So funktioniert machsruhig</h2>
    <div class="mr-steps">
      <div class="mr-step"><span class="num">1</span><br><strong>Verstehen.</strong> Was kostet eine Bestattung, welche Fristen gelten? Ratgeber und <a href="/tools/bestattungskosten-rechner/" style="color:var(--mr-primary)">Kostenrechner</a> geben dir den Rahmen — bundesland-genau.</div>
      <div class="mr-step"><span class="num">2</span><br><strong>Prüfen.</strong> Angebot vom Bestatter da? Der <a href="/tools/angebotspruefer/" style="color:var(--mr-primary)">Angebotsprüfer</a> vergleicht Preis und Posten mit der regionalen Spanne.<br><span class="mr-mini-ampel"><strong style="color:#5a8a5a">✓</strong> Preis wirkt plausibel</span><br><a href="/tools/angebotspruefer/#ap-beispiel" style="color:var(--mr-primary);font-size:13px">Beispiel-Ergebnis ansehen →</a></div>
      <div class="mr-step"><span class="num">3</span><br><strong>In Ruhe entscheiden.</strong> Du bekommst eine konkrete Fragenliste fürs Bestatter-Gespräch. Nichts muss sofort unterschrieben werden — du darfst vergleichen.</div>
    </div>
  </section>

''' + ST_ANCHOR
assert t.count(ST_ANCHOR) == 1
t = t.replace(ST_ANCHOR, SOFUNKT, 1)

save(P, t)
print('index.html: Hero + Reorder + Trust + So-funktioniert OK')

# ===== Quick-Win: Vorsorge-Hub-Kachel (falsch beschriftet -> Kommt-bald-Seite) raus =====
V = 'vorsorge/index.html'
tv = load(V)
TILE = '''      <a href="/vorsorge/vorsorge-ordner/" class="mr-topic-card">
        <h3>Vorsorgevollmacht</h3>
        <p>Bevollmächtige eine Vertrauensperson, deine rechtlichen, finanziellen und persönlichen Angelegenheiten zu regeln. Verhindert eine gerichtliche Betreuerbestellung.</p>
        <span class="card-link">Zum Vorsorge-Ordner &#8594;</span>
      </a>

'''
assert tv.count(TILE) == 1, tv.count(TILE)
tv = tv.replace(TILE, '', 1)
save(V, tv)
print('vorsorge/index.html: Fehl-Kachel (Vorsorgevollmacht -> Kommt-bald-Ordner) entfernt')
print('FERTIG')
