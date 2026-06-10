# -*- coding: utf-8 -*-
# Fix: Seiten-Stempel der 52 Stadtseiten auf 9. Juni 2026 (User-Anweisung 10.06.2026)
# Begruendung: Stadtseiten wurden am 09.06. substanziell geaendert (Schnellzugriff-Block);
#   Sitemap-lastmod sagt bereits 2026-06-09, sichtbarer Stempel sagte noch Mai => Inkonsistenz.
# CHIRURGISCH — NUR:
#   (1) "Stand: ..." INNERHALB der mr-article-meta-Zeile (Seiten-Stempel)
#   (2) Legacy <p class="stand">-Zeile (nur braunschweig)
#   (3) JSON-LD "dateModified": "2026-04-XX/2026-05-XX" -> "2026-06-09" (Single-Line-Value, kein Multi-Line-Regex)
# NICHT angefasst: Daten-/Satzungs-Staende im Content ("Stand: 17.12.2025", "Stand: 2022",
#   "Stand: 31.12.2024", "Gebuehren ... Stand: Mai 2026" in Keyfacts/Tabellen etc.)
import re, glob, io

NEU_SICHTBAR = 'Stand: 9. Juni 2026'
NEU_ISO = '2026-06-09'

files = sorted(glob.glob(r'bestatter/*/index.html'))
stat = []
for f in files:
    s = io.open(f, encoding='utf-8').read()
    orig = s
    n_meta = n_stand = n_dm = 0

    # (1) mr-article-meta-Zeile + (2) legacy class="stand": nur in diesen Zeilen ersetzen
    out_lines = []
    for line in s.split('\n'):
        if 'mr-article-meta' in line:
            line, k = re.subn(r'(<span>)Stand: [^<]{1,30}(</span>)', r'\g<1>' + NEU_SICHTBAR + r'\g<2>', line, count=1)
            n_meta += k
        elif 'class="stand"' in line:
            line, k = re.subn(r'Stand: [^<·]{1,30} ·', NEU_SICHTBAR + ' ·', line, count=1)
            n_stand += k
        out_lines.append(line)
    s = '\n'.join(out_lines)

    # (3) dateModified Single-Line-Value (NUR April/Mai-2026-Werte)
    s, n_dm = re.subn(r'("dateModified":\s*")2026-0[45]-\d\d(")', r'\g<1>' + NEU_ISO + r'\g<2>', s)

    if s != orig:
        io.open(f, 'w', encoding='utf-8').write(s)
    city = f.replace('\\', '/').split('/')[1]
    stat.append((city, n_meta, n_stand, n_dm))

print('%-22s meta stand dateMod' % 'city')
warn = []
for city, a, b, c in stat:
    flag = ''
    if a != 1:
        flag = ' <-- meta!=1'
        warn.append(city)
    print('%-22s %4d %5d %7d%s' % (city, a, b, c, flag))
print('\nDateien gesamt:', len(stat))
print('meta-Stempel ersetzt:', sum(a for _, a, _, _ in stat))
print('legacy p.stand ersetzt:', sum(b for _, _, b, _ in stat))
print('dateModified ersetzt:', sum(c for _, _, _, c in stat))
if warn:
    print('WARNUNG (meta!=1):', warn)

# Verifikation: keine Mai/April-Reste im Seiten-Stempel + Schutz-Check Quellen-Staende unveraendert
prot = 0
for f in files:
    s = io.open(f, encoding='utf-8').read()
    for line in s.split('\n'):
        if 'mr-article-meta' in line and re.search(r'Stand: [^<]*(Mai|April) 2026', line):
            print('REST-BEFUND', f, line[:120]); prot += 1
print('\nRest-Befunde im Seiten-Stempel:', prot)
a = io.open('bestatter/aachen/index.html', encoding='utf-8').read()
m = io.open('bestatter/moenchengladbach/index.html', encoding='utf-8').read()
print('Schutz-Check aachen "Stand: 17.12.2025" noch da:', 'Stand: 17.12.2025' in a)
print('Schutz-Check mgladbach "Stand: 31.12.2024" noch da:', 'Stand: 31.12.2024' in m)
print('Schutz-Check mgladbach "Stand: 2022" noch da:', 'Stand: 2022' in m)
