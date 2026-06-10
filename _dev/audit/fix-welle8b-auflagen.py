#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welle 8b (2026-06-10) — Review-Auflagen (GO 84) + Zufallsfund:
M1 Attribution check24 auf Hauptseite | M2 dateModified/Stand Juni 2026 |
K1 FAQ-LD aus DOM regeneriert (Paritaet garantiert) | K2 "guenstigste" auf
Sarg-/Urnengraeber qualifiziert (HS + BL-Seite) | K3 letzter 300-400-Claim |
K4 Grabpflege-Halbsatz | BONUS: Steuer-FAQ-Faktenfehler korrigiert
(pauschales "Nein" -> § 33 EStG, soweit ueber Nachlass; verifiziert BMF/EStH).
"""
import io, sys, re, json

def patch(path, replacements):
    with io.open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()
    for i, (old, new, expect) in enumerate(replacements):
        c = text.count(old)
        if c != expect:
            print('FATAL #%d: %r -> %d (erwartet %d) in %s' % (i, old[:70], c, expect, path)); sys.exit(1)
        text = text.replace(old, new)
    with io.open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)
    print('%s: %d Ersetzungen OK' % (path, len(replacements)))

HS = 'bestattungskosten.html'
patch(HS, [
    # BONUS: Steuer-FAQ-Faktenfehler (DOM; LD wird unten aus DOM regeneriert)
    ('Nein, Bestattungskosten sind private Aufwendungen und nicht steuerlich absetzbar. Eine Sterbegeldversicherung, Trauerstiftungen oder das Sozialamt können helfen, die finanzielle Last zu tragen.',
     'In bestimmten Fällen ja: Trägst du die Kosten als Angehöriger und übersteigen sie den Nachlass (plus Ersatzleistungen wie ein Sterbegeld), kannst du den übersteigenden Teil als außergewöhnliche Belastung (§ 33 EStG) geltend machen — das Finanzamt zieht eine zumutbare Eigenbelastung ab und erkennt nur unmittelbare Bestattungskosten in angemessener Höhe an. Reicht der Nachlass aus, ist nichts absetzbar.', 1),
    # K3: letzter Praezisions-Claim
    ('<li>Regionale Unterschiede: bis zu 300–400 % Differenz</li>',
     '<li>Regionale Unterschiede: Friedhofsgebühren zwischen Kommunen teils um ein Vielfaches verschieden</li>', 1),
    # M2: sichtbares Stand-Datum
    ('Stand: April 2026', 'Stand: Juni 2026', 1),
    # M1 + K4: Friedhofsgebuehren-Block — Attribution + Grabpflege-Hinweis
    ('auf 20 Jahre Nutzungszeit vereinheitlicht (Aeternitas 2025). Das regionale Kostenniveau aller 16 Länder zeigt unser <a href="/bestattungskosten-nach-bundesland" style="color:var(--mr-primary)">Bundesland-Vergleich</a>.',
     'auf 20 Jahre Nutzungszeit vereinheitlicht (Aeternitas-Daten in der check24-Aufbereitung, 2025). Das regionale Kostenniveau aller 16 Länder zeigt unser <a href="/bestattungskosten-nach-bundesland" style="color:var(--mr-primary)">Bundesland-Vergleich</a> — dessen Spannen enthalten die volle Grabpflege über die Ruhezeit und liegen daher über den Werten hier.', 1),
    # M1 + K2: Stadt-vs-Land-Absatz
    ('Berlin hat trotz Millionenstadt die günstigsten Gebühren aller Landeshauptstädte (Aeternitas 2025).',
     'Berlin hat trotz Millionenstadt bei Sarg- und Urnengräbern die günstigsten Gebühren aller Landeshauptstädte (Aeternitas-Daten, check24-Aufbereitung 2025).', 1),
    # M1: Beispiele
    ('Sargwahlgrab ca. 4.600 € (20 Jahre, Aeternitas 2025)',
     'Sargwahlgrab ca. 4.600 € (20 Jahre; Aeternitas-Daten, check24-Aufbereitung)', 1),
])

# ===== K1: FAQ-LD aus DOM regenerieren (Paritaet garantiert) =====
with io.open(HS, 'r', encoding='utf-8') as fh:
    t = fh.read()
pairs = re.findall(r'<summary>([^<]+)</summary><div class="faq-answer"><p>(.*?)</p></div>', t, re.S)
assert len(pairs) == 6, 'erwartet 6 FAQ-Paare, gefunden %d' % len(pairs)
def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    return re.sub(r'\s+', ' ', s).strip()
m = re.search(r'(<script type="application/ld\+json">\s*)(\{.*?\})(\s*</script>)', t, re.S)
assert m, 'LD-Block nicht gefunden'
g = json.loads(m.group(2))
faq_nodes = [n for n in g['@graph'] if n.get('@type') == 'FAQPage']
assert len(faq_nodes) == 1
faq_nodes[0]['mainEntity'] = [
    {'@type': 'Question', 'name': strip_tags(q),
     'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(a)}}
    for q, a in pairs]
# M2: dateModified
for n in g['@graph']:
    if n.get('@type') == 'Article' and n.get('dateModified'):
        n['dateModified'] = '2026-06-10'
new_ld = json.dumps(g, ensure_ascii=False, separators=(',', ':'))
t = t[:m.start()] + m.group(1) + new_ld + m.group(3) + t[m.end():]
with io.open(HS, 'w', encoding='utf-8', newline='') as fh:
    fh.write(t)
print('FAQ-LD aus DOM regeneriert (6 Paare), dateModified 2026-06-10')

# ===== K2 auf BL-Seite (FAQ A2, DOM + LD) =====
patch('bestattungskosten-nach-bundesland.html', [
    ('die Hauptstadt hat laut Aeternitas die günstigsten Friedhofsgebühren aller Landeshauptstädte',
     'die Hauptstadt hat laut Aeternitas bei Sarg- und Urnengräbern die günstigsten Friedhofsgebühren aller Landeshauptstädte', 2),
])

# ===== Sitemap lastmod fuer /bestattungskosten =====
with io.open('sitemap.xml', 'r', encoding='utf-8') as fh:
    s = fh.read()
mm = re.search(r'(<loc>https://machsruhig\.de/bestattungskosten</loc>\s*<lastmod>)([0-9-]+)(</lastmod>)', s)
assert mm, 'sitemap-Eintrag /bestattungskosten nicht gefunden'
s = s[:mm.start()] + mm.group(1) + '2026-06-10' + mm.group(3) + s[mm.end():]
with io.open('sitemap.xml', 'w', encoding='utf-8', newline='') as fh:
    fh.write(s)
print('sitemap lastmod /bestattungskosten -> 2026-06-10')
print('FERTIG')
