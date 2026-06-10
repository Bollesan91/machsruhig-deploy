# -*- coding: utf-8 -*-
# Fix Helper-V3 Review Runde 1 (Reviewer NO-GO -> GO nach M1):
#  M1: FAQPage-JSON-LD zeichengenau aus sichtbarem <details>-Text generieren (Paritaet)
#  K1: Keyfact "56 %" eindeutig formulieren
#  K2: Tabellen-<caption> (Modell-Klarstellung + a11y)
#  K3: Article.headline an H1 angleichen
# JSON-LD wird GEPARST und neu serialisiert (json.loads/dumps) — KEIN Multi-Line-Regex (checkliste-Lesson).
import re, json, io

F = 'bestattungskosten-nach-bundesland.html'
s = io.open(F, encoding='utf-8').read()
orig = s
report = []

# ---------- K1: Keyfact eindeutig ----------
k1_old = '<li>Spanne zwischen teuerstem und günstigstem Land: rund <strong>56 %</strong></li>'
k1_new = '<li>Teuerstes Land liegt im Modell rund <strong>56 %</strong> über dem günstigsten</li>'
assert s.count(k1_old) == 1, 'K1 Anker nicht eindeutig: %d' % s.count(k1_old)
s = s.replace(k1_old, k1_new, 1)
report.append('K1 Keyfact: ok')

# ---------- K2: Tabellen-caption ----------
k2_old = '    <table class="bl-table">\n      <thead>'
k2_new = ('    <table class="bl-table">\n'
          '      <caption style="caption-side:top;text-align:left;font-size:12px;color:var(--mr-text-muted);padding:0 0 8px">'
          'Modellierte Kostenspannen (Standard-Szenario) — keine erhobenen Marktpreise.</caption>\n'
          '      <thead>')
assert s.count(k2_old) == 1, 'K2 Anker nicht eindeutig: %d' % s.count(k2_old)
s = s.replace(k2_old, k2_new, 1)
report.append('K2 caption: ok')

# ---------- Sichtbare <details> extrahieren (Quelle der Wahrheit) ----------
faq_section = s[s.find('<section class="mr-faq">'):s.find('</section>', s.find('<section class="mr-faq">'))]
dets = re.findall(r'<details><summary>(.*?)</summary><div class="faq-answer"><p>(.*?)</p></div></details>', faq_section, re.S)
assert len(dets) == 5, 'Erwartet 5 sichtbare FAQ, gefunden %d' % len(dets)

def strip_tags(x):
    x = re.sub(r'<[^>]+>', '', x)          # alle Tags raus (Link-Text bleibt)
    x = x.replace('&amp;', '&')
    return re.sub(r'\s+', ' ', x).strip()

visible = [(strip_tags(q), strip_tags(a)) for q, a in dets]
report.append('Sichtbare FAQ extrahiert: %d' % len(visible))

# ---------- JSON-LD parsen, FAQPage + Article.headline ersetzen ----------
m = re.search(r'(<script type="application/ld\+json">)(.*?)(</script>)', s, re.S)
assert m, 'kein JSON-LD-Block'
data = json.loads(m.group(2))
graph = data['@graph']

h1 = strip_tags(re.search(r'<h1>(.*?)</h1>', s, re.S).group(1))

faq_done = art_done = False
for node in graph:
    if node.get('@type') == 'Article':
        node['headline'] = h1            # K3
        art_done = True
    if node.get('@type') == 'FAQPage':
        node['mainEntity'] = [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in visible
        ]                                # M1
        faq_done = True
assert art_done and faq_done, 'Article/FAQPage nicht gefunden'

new_json = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
s = s[:m.start()] + m.group(1) + '\n' + new_json + '\n' + m.group(3) + s[m.end():]
report.append('JSON-LD neu serialisiert: Article.headline=H1, FAQ=sichtbar (%d Q)' % len(visible))

io.open(F, 'w', encoding='utf-8').write(s)
print('\n'.join(report))

# ---------- VERIFIKATION ----------
print('\n=== VERIFIKATION ===')
s2 = io.open(F, encoding='utf-8').read()
m2 = re.search(r'<script type="application/ld\+json">(.*?)</script>', s2, re.S)
d2 = json.loads(m2.group(1))
print('JSON-LD valid: OK')
# Paritaet: jede JSON-LD-FAQ-Antwort muss als sichtbarer Plain-Text vorkommen
faq_section2 = s2[s2.find('<section class="mr-faq">'):s2.find('</section>', s2.find('<section class="mr-faq">'))]
dets2 = re.findall(r'<details><summary>(.*?)</summary><div class="faq-answer"><p>(.*?)</p></div></details>', faq_section2, re.S)
vis_set = set()
for q, a in dets2:
    vis_set.add((strip_tags(q), strip_tags(a)))
ok = 0; bad = 0
for node in d2['@graph']:
    if node.get('@type') == 'FAQPage':
        for qa in node['mainEntity']:
            q = qa['name']; a = qa['acceptedAnswer']['text']
            if (q, a) in vis_set:
                ok += 1
            else:
                bad += 1; print('  PARITAET-FEHLER:', q[:40])
print('FAQ-Paritaet sichtbar==schema: %d ok, %d Fehler' % (ok, bad))
# Article.headline == H1?
h1b = strip_tags(re.search(r'<h1>(.*?)</h1>', s2, re.S).group(1))
for node in d2['@graph']:
    if node.get('@type') == 'Article':
        print('Article.headline==H1:', node['headline'] == h1b, '|', node['headline'])
# K1/K2 sichtbar?
print('K1 neu vorhanden:', 'rund <strong>56 %</strong> über dem günstigsten' in s2)
print('K2 caption vorhanden:', '<caption' in s2 and 'keine erhobenen Marktpreise' in s2)
print('Phantomsatz Q3 weg (Beisetzungs- und Verwaltungs):', 'Beisetzungs- und Verwaltungsgebuehren' not in s2)
