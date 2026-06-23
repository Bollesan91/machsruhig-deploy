# -*- coding: utf-8 -*-
"""Read-only Inventar der Tool-Seiten fuer den Quervernetzungs-Block."""
import glob, os, re, io

tools = sorted(glob.glob('tools/*/index.html'))

def find(t, pat):
    m = re.search(pat, t, re.I)
    return m.group(1).strip() if m else '?'

# Inbound zaehlen (gleiche Logik wie inbound-link-audit)
pages = [p for p in glob.glob('**/*.html', recursive=True)
         if (os.sep+'_dev') not in (os.sep+p) and os.path.basename(p) != '404.html']
texts = {p: io.open(p, encoding='utf-8').read() for p in pages}

def inbound(url):
    base = url.rstrip('/')
    pats = ['href="%s"' % base, 'href="%s/"' % base]
    return sum(1 for q in pages if any(x in texts[q] for x in pats))

for f in tools:
    t = texts[f]
    url = '/' + f[:-len('index.html')]
    title = find(t, r'<title>(.*?)</title>')
    h1 = find(t, r'<h1[^>]*>(.*?)</h1>')
    h1 = re.sub(r'<[^>]+>', '', h1)
    rel = []
    if 'mr-related-grid' in t: rel.append('mr-related')
    if 'mr-relation-grid' in t: rel.append('mr-relation')
    if re.search(r'Weitere (kostenlose )?(Helfer|Tools)', t, re.I): rel.append('WEITERE-HELFER')
    if re.search(r'Verwandte Themen', t): rel.append('Verwandte')
    # Footer-Anker: was kommt unmittelbar vor <footer
    fm = re.search(r'(.{0,40})(<footer)', t)
    before_footer = fm.group(1)[-40:] if fm else '(kein footer)'
    print("%-34s in=%-2d  rel=[%s]" % (url, inbound(url), ','.join(rel) or '-'))
    print("    title: %s" % title[:70])
    print("    h1   : %s" % h1[:70])
    print("    vor <footer>: ...%s" % before_footer)
