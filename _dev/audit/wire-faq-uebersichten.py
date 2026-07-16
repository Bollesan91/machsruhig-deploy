#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FAQ (sichtbar + FAQPage-Schema) auf die 50 Friedhof-Uebersichten, aus dem
# 2x-verifizierten Register (gleiche Quelle wie der Gebuehren-Kasten -> drift-frei).
# 2 Fragen je Stadt: Kosten Erd-Wahlgrab + wer legt Gebuehren fest.
# Asserts VOR Write: JSON-LD parst, FAQPage==1, details +2, section-Balance.
import os, re, sys, json, glob
DRY = "--apply" not in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = json.load(open(os.path.join(ROOT, "_dev", "claims", "friedhofsgebuehren.json"), encoding="utf-8"))

def fold(s):
    s = (s or "").lower()
    for a, b in (("ä","ae"),("ö","oe"),("ü","ue"),("ß","ss")): s = s.replace(a, b)
    return re.sub(r"[^a-z]", "", s)
by = {fold(c["stadt"]): c for c in REG["staedte"]}
def find_city(slug):
    f = fold(slug)
    if f in by: return by[f]
    for k, v in by.items():
        if k.startswith(f) or f.startswith(k): return v
    return None

def eur(n):
    s = f"{n:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s[:-3] if s.endswith(",00") else s

def stadt_display(html):
    m = re.search(r'<h1>Friedh&ouml;fe in ([^<]+)</h1>|<h1>Friedhöfe in ([^<]+)</h1>', html)
    return (m.group(1) or m.group(2)).strip() if m else None

def qa(c, stadt):
    grab = eur(c["grabnutzung_betrag_eur"]); beis = eur(c["beisetzung_betrag_eur"]); ruhe = c["ruhezeit_jahre"]
    # Review F10: Stand-Jahr in die Antwort (Schema/Snippet kann allein zirkulieren)
    ym = re.findall(r'20\d\d', c.get("satzung_stand") or "")
    stand = f" (Stand der Satzung: {ym[-1]}, geprüft 07/2026)" if ym else " (geprüft 07/2026)"
    # Re-Audit 07/2026: Grabtyp je Stadt (Einheit B) statt "Einzelstelle"; kein Superlativ-Claim
    # (Review 13.07. M1); Berlin-Grundgebuehr-Sonderfall (M2); Pflicht-Zusaetze benannt.
    grabtyp = (c.get("grabtyp_einheit") or "Erd-Wahlgrab").strip()
    zusatz = f" Zusätzlich fällt an: {c['_pflicht_zusatz_box']}." if c.get("_pflicht_zusatz_box") else ""
    schluss = (" Einfachere Grabarten können günstiger sein. Das ist nicht der Gesamtpreis einer "
               "Bestattung: Bestatterleistungen, Sarg und Grabmal kommen hinzu.")
    if c.get("_grabzeile_sonder"):  # Berlin: kein separates Nutzungsrechts-Entgelt
        kosten_a = (f"Auf den landeseigenen (städtischen) Friedhöfen fallen je Bestattungsfall die Friedhofsgrundgebühr für eine Wahlgrabstätte plus die Verwaltungsgebühr für das Nutzungsrecht an — zusammen {grab} €; das schließt das Nutzungsrecht für die 20-jährige Ruhezeit ein. Die Erdbestattung kostet {beis} €{stand}.{zusatz}{schluss}")
    elif c["grabnutzung_einheit"] == "pro_jahr":
        gesamt = eur(round(c["grabnutzung_betrag_eur"] * ruhe))
        kosten_a = (f"Laut amtlicher Gebührensatzung kostet die Grabnutzung ({grabtyp}) {grab} € je Grabstelle und Jahr — bei {ruhe} Jahren Ruhezeit insgesamt rund {gesamt} € —, die Beisetzung {beis} €{stand}.{zusatz}{schluss}")
    else:
        kosten_a = (f"Laut amtlicher Gebührensatzung kostet die Grabnutzung ({grabtyp}) {grab} € einmalig für die Nutzungszeit von {ruhe} Jahren, die Beisetzung {beis} €{stand}.{zusatz}{schluss}")
    q1 = (f"Was kostet ein Grab in {stadt}?", kosten_a)
    # Review F9: Frage passend zur Antwort (kein "Wer", das die Antwort nicht einloest;
    # Gremium variiert je Stadt/Traeger — Stadtrat vs. AoeR-Verwaltungsrat — nicht raten)
    q2 = (f"Wo sind die Friedhofsgebühren in {stadt} geregelt?",
          f"In der amtlichen Gebührensatzung des kommunalen Friedhofsträgers — verbindlich ist stets die aktuell gültige Fassung. Kirchliche und jüdische Friedhöfe rechnen nach eigenen Ordnungen ab.")
    return [q1, q2]

REFRESH = "--refresh" in sys.argv
re_vis = re.compile(r'  <div class="mr-faq">\n    <h2>Häufige Fragen zu den Friedhöfen.*?</div>\n\n', re.S)
done=[];skip=[];err=[]
for p in sorted(glob.glob(os.path.join(ROOT, "friedhoefe", "*", "index.html"))):
    slug = os.path.basename(os.path.dirname(p))
    html = open(p, encoding="utf-8").read()
    if '"@type":"FAQPage"' in html or 'Häufige Fragen zu den Friedhöfen' in html:
        if not REFRESH: skip.append(slug+"(schon)"); continue
        h2 = re_vis.sub("", html, count=1)
        i = h2.find(',\n    {"@type":"FAQPage"')
        j = h2.find('\n  ]\n}\n</script>')
        if i < 0 or j < 0 or j < i: err.append(slug+": Refresh-Anker fehlt"); continue
        html = h2[:i] + h2[j:]
        if 'FAQPage' in html or 'Häufige Fragen zu den Friedhöfen' in html:
            err.append(slug+": Alt-FAQ nicht entfernbar"); continue
    c = find_city(slug); stadt = stadt_display(html)
    if not c or not stadt: err.append(slug+": Register/H1 fehlt"); continue
    qas = qa(c, stadt)
    # 1) Sichtbare FAQ vor dem "Passend dazu"-Block
    anchor = '  <div class="mr-related">'
    if html.count(anchor) != 1: err.append(slug+": related-Anker!=1"); continue
    vis = '  <div class="mr-faq">\n    <h2>Häufige Fragen zu den Friedhöfen in ' + stadt + '</h2>\n'
    for q, a in qas:
        vis += f'    <details><summary>{q}</summary><div class="faq-answer">{a}</div></details>\n'
    vis += '  </div>\n\n'
    new = html.replace(anchor, vis + anchor, 1)
    # 2) FAQPage in @graph (vor dem @graph-Ende)
    m = re.search(r'\n  \]\n\}\n</script>', new)
    if not m: err.append(slug+": JSON-LD-Ende nicht gefunden"); continue
    faq_node = ',\n    {"@type":"FAQPage","mainEntity":[' + ','.join(
        json.dumps({"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}}, ensure_ascii=False)
        for q, a in qas) + ']}'
    new = new[:m.start()] + faq_node + new[m.start():]
    # Asserts
    jm = re.search(r'<script type="application/ld\+json">(.*?)</script>', new, re.S)
    try:
        data = json.loads(jm.group(1))
        assert sum(1 for n in data.get("@graph", []) if n.get("@type") == "FAQPage") == 1
    except Exception as e:
        err.append(f"{slug}: JSON-LD kaputt: {e}"); continue
    if new.count('<details') != html.count('<details') + 2: err.append(slug+": details-Count"); continue
    if new.count('</div>') != html.count('</div>') + len(qas) + 1: err.append(slug+": div-Balance"); continue
    if not DRY: open(p, "w", encoding="utf-8").write(new)
    done.append(slug)
print(f"=== {'DRY' if DRY else 'APPLY'} === ok {len(done)} | skip {len(skip)} | err {len(err)}")
for e in err: print("  ERR", e)
