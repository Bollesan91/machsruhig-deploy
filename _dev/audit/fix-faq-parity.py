#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4.1-Dogfood: FAQ-Schema↔sichtbar-Parität (Linter-Klasse L3).
- Klasse A (7 Seiten mit sichtbarem FAQ): FAQPage-mainEntity vollständig aus dem
  sichtbaren <details><summary>/faq-answer-DOM regenerieren → 100 % Parität für
  Frage UND Antwort. Orphan-JSON-LD-Fragen ohne sichtbaren Block fallen weg.
- Klasse C (2 Tool-Seiten ohne sichtbaren FAQ): FAQPage-Node aus dem @graph
  entfernen (Schema ohne sichtbaren Inhalt = strukturierte-Daten-Verstoß; die
  FAQ-Inhalte leben auf den Artikelseiten, nicht auf dem Tool).
Alle Asserts VOR dem einzigen Write je Datei.
"""
import io, os, re, json, sys, html as htmlmod

CLASS_A = ['bestatter/halle/index.html', 'bestattung-in/nordrhein-westfalen/index.html',
           'kindern-tod-erklaeren.html', 'tools/danksagung/index.html',
           'vorsorge/digitaler-nachlass/index.html',
           'vorsorge/sterbegeldversicherung/index.html', 'vorsorge/vorsorge-ordner/index.html']
CLASS_C = ['tools/abschiedsbrief/index.html', 'tools/fristen-radar/index.html']

def clean(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = htmlmod.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

def parse_details(html):
    """Liefert [(frage, antwort)] aus sichtbaren <details>-Blöcken."""
    out = []
    for d in re.finditer(r'<details\b[^>]*>(.*?)</details>', html, re.S | re.I):
        block = d.group(1)
        sm = re.search(r'<summary\b[^>]*>(.*?)</summary>', block, re.S | re.I)
        if not sm:
            continue
        q = clean(sm.group(1))
        ans_html = block[sm.end():]
        am = re.search(r'(?:class|className)="faq-answer"[^>]*>(.*?)(?:</div>\s*)?$', ans_html, re.S | re.I)
        a = clean(am.group(1)) if am else clean(ans_html)
        if q and a:
            out.append((q, a))
    return out

def replace_faqpage(html, transform):
    """Ersetzt das erste FAQPage-Node-mainEntity via transform(list)->list|None.
    None => Node ganz aus @graph entfernen."""
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        raw = m.group(1)
        try:
            data = json.loads(raw)
        except Exception:
            continue
        # Container bestimmen: dict-mit-@graph | top-level-list | standalone FAQPage
        graph = None
        if isinstance(data, dict) and isinstance(data.get('@graph'), list):
            graph = data['@graph']
        elif isinstance(data, list):
            graph = data
        elif isinstance(data, dict) and data.get('@type') == 'FAQPage':
            newqa = transform(data.get('mainEntity', []))
            if newqa is None:
                return html[:m.start()] + html[m.end():], 'removed-standalone'
            data['mainEntity'] = newqa
            nj = json.dumps(data, ensure_ascii=False, indent=2)
            return html[:m.start(1)] + nj + html[m.end(1):], 'rebuilt'
        if graph is None:
            continue
        idx = next((i for i, n in enumerate(graph) if isinstance(n, dict) and n.get('@type') == 'FAQPage'), None)
        if idx is None:
            continue
        node = graph[idx]
        newqa = transform(node.get('mainEntity', []))
        if newqa is None:
            del graph[idx]
        else:
            node['mainEntity'] = newqa
        new_json = json.dumps(data, ensure_ascii=False, indent=2)
        return html[:m.start(1)] + new_json + html[m.end(1):], ('removed' if newqa is None else 'rebuilt')
    return html, 'no-faqpage'

def main():
    total = 0
    for rel in CLASS_A:
        html = io.open(rel, encoding='utf-8').read()
        qa = parse_details(html)
        assert qa, 'A: keine sichtbaren FAQ-Paare in %s' % rel
        mainentity = [{"@type": "Question", "name": q,
                       "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]
        new_html, status = replace_faqpage(html, lambda _old: mainentity)
        assert status == 'rebuilt', 'A: %s -> %s' % (rel, status)
        # Verify: jede neue Frage steht sichtbar
        vis = clean(re.sub(r'<script\b.*?</script>', ' ', new_html, flags=re.S | re.I))
        for q, _ in qa:
            assert q[:60] in vis, 'A-Verify fehlgeschlagen: %s / %s' % (rel, q[:40])
        # JSON-LD parsebar
        m = re.search(r'<script type="application/ld\+json">(.*?)</script>', new_html, re.S)
        json.loads(m.group(1))
        io.open(rel, 'w', encoding='utf-8', newline='').write(new_html)
        print('A rebuilt %-46s %d FAQ' % (rel, len(qa)))
        total += 1

    for rel in CLASS_C:
        html = io.open(rel, encoding='utf-8').read()
        assert '<summary' not in html, 'C: %s hat doch sichtbaren FAQ' % rel
        new_html, status = replace_faqpage(html, lambda _old: None)
        assert status in ('removed', 'removed-standalone'), 'C: %s -> %s' % (rel, status)
        assert 'FAQPage' not in new_html, 'C: FAQPage-Rest in %s' % rel
        m = re.search(r'<script type="application/ld\+json">(.*?)</script>', new_html, re.S)
        if m:
            json.loads(m.group(1))
        io.open(rel, 'w', encoding='utf-8', newline='').write(new_html)
        print('C removed FAQPage %-40s' % rel)
        total += 1

    print('--- %d Seiten gefixt' % total)

if __name__ == '__main__':
    main()
