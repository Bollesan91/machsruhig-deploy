#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Register -> 50 Friedhof-Uebersichten: je Stadt IHRE verifizierte Erd-Wahlgrab-Zahl
# in die bestehende Gebuehren-Sektion. KEIN Staedte-Vergleich (Mainz-Berlin-Falle).
# Quelle: _dev/claims/friedhofsgebuehren.json (2x re-verifiziert, 01.07.2026).
# Idempotent. Asserts VOR Write (Lektion 17). DRY default; --apply schreibt.
import os, re, sys, json, glob
DRY = "--apply" not in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = json.load(open(os.path.join(ROOT, "_dev", "claims", "friedhofsgebuehren.json"), encoding="utf-8"))

def fold(s):
    s = (s or "").lower()
    for a, b in (("ä","ae"),("ö","oe"),("ü","ue"),("ß","ss")): s = s.replace(a, b)
    return re.sub(r"[^a-z]", "", s)

# Register nach Verzeichnis-Slug aufloesen
by_slug = {}
for c in REG["staedte"]:
    by_slug[fold(c["stadt"])] = c

def find_city(slug):
    f = fold(slug)
    if f in by_slug: return by_slug[f]
    for k, v in by_slug.items():
        if k.startswith(f) or f.startswith(k): return v
    return None

def eur(n):
    if n is None: return None
    s = f"{n:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s[:-3] if s.endswith(",00") else s

def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") \
        .replace("ä","&auml;").replace("ö","&ouml;").replace("ü","&uuml;") \
        .replace("Ä","&Auml;").replace("Ö","&Ouml;").replace("Ü","&Uuml;").replace("ß","&szlig;") \
        .replace("×","&times;").replace("§","&sect;").replace("—","&mdash;").replace("–","&ndash;")

def block(c):
    grab = eur(c.get("grabnutzung_betrag_eur")); beis = eur(c.get("beisetzung_betrag_eur"))
    ruhe = c.get("ruhezeit_jahre"); einheit = c.get("grabnutzung_einheit")
    if not grab or not beis or not ruhe: return None
    # Re-Audit 07/2026: Grabtyp je Stadt benannt (Einheit B) statt pauschal "Einzelstelle"
    grabtyp = esc((c.get("grabtyp_einheit") or "Erd-Wahlgrab").strip())
    if c.get("_grabzeile_sonder"):          # Berlin: Grundgebuehr-System, kein Nutzungsrechts-Entgelt
        grab_zeile = c["_grabzeile_sonder"]
    elif einheit == "pro_jahr":
        gesamt = eur(round(c["grabnutzung_betrag_eur"] * ruhe))
        # Review 02.07.: Zahlungsmodus nennen (z.B. Muenchen § 4(4): fuer die gesamte Ruhezeit im Voraus)
        grab_zeile = (f"Grabnutzung: <strong>{grab} &euro; je Grabstelle und Jahr</strong> "
                      f"(bei {ruhe} Jahren Ruhezeit rund {gesamt} &euro; &mdash; je nach Stadt "
                      f"f&uuml;r die gesamte Nutzungszeit im Voraus f&auml;llig)")
    else:
        grab_zeile = f"Grabnutzung: <strong>{grab} &euro;</strong> einmalig f&uuml;r die Nutzungszeit ({ruhe} Jahre)"
    netto = ' Betr&auml;ge netto (USt f&auml;llt bei kommunalen Friedhofsgeb&uuml;hren i.&thinsp;d.&thinsp;R. nicht an).' \
        if (c.get("netto_brutto") or "").strip().lower().startswith("netto") else ""
    if c.get("_ust_box"):
        netto = " " + esc(c["_ust_box"])
    # Re-Audit 07/2026 (Scope-Decision #1): bekannte Pflicht-Zusatzgebuehren je Stadt benennen
    # (_pflicht_zusatz_box = nutzerlesbare Fassung; interne Notiz _pflicht_zusatz_hinweis wird NICHT gerendert)
    zusatz = ""
    if c.get("_pflicht_zusatz_box"):
        zusatz = f"\n        <li>Zus&auml;tzlich f&auml;llt hier an: <strong>{esc(c['_pflicht_zusatz_box'])}</strong></li>"
    def de_ascii(s):
        # Register-Felder tragen teils ASCII-Transliterationen -> fuer Anzeige zurueckwandeln (Wort-Map, safe)
        for a, b in (("veroeffentlicht","veröffentlicht"),("Veroeffentlicht","Veröffentlicht"),
                     ("geaendert","geändert"),("Gebuehren","Gebühren"),("gebuehren","gebühren"),
                     ("Gebuehr","Gebühr"),("gueltig","gültig"),("Aenderung","Änderung"),
                     ("Saeule","Säule"),("fuer ","für "),("Staedt","Städt"),("staetten","stätten"),("Staetten","Stätten")):
            s = s.replace(a, b)
        return s
    para = de_ascii((c.get("grabnutzung_paragraph") or "").strip())
    # Review 02.07.: Paragraph deckt nur die Grabnutzung — so labeln (Berlin: Grundgebuehr-System -> "Beleg")
    para_label = "Beleg" if c.get("_grabzeile_sonder") else "Grabnutzung"
    para_txt = f" ({para_label}: {esc(para)})" if para and len(para) <= 60 else ""
    url = c.get("satzung_url", "").split(" ")[0]
    # Review 02.07.: Stand nicht mitten im Satz kappen — an Semikolon/Klammer schneiden, cap 130
    stand = de_ascii((c.get("satzung_stand") or "").split(";")[0].split(" (")[0].strip())
    if len(stand) > 130: stand = stand[:130].rsplit(" ", 1)[0] + " &hellip;"
    # Review 02.07.: KEIN erfundenes Lage-Label ("einfache Lage" existiert z.B. in Koeln nicht);
    # + Fussnote, dass der Umfang der Beisetzungsgebuehr je Stadt verschieden ist.
    return f'''    <div class="fh-gebuehren-beispiel" style="background:var(--mr-bg-card,#FFFDF9);border:1px solid var(--mr-border,#E8E0D6);border-left:4px solid var(--mr-accent,#866E45);border-radius:8px;padding:14px 18px;margin:14px 0">
      <strong style="font-size:14px">Beispiel aus der Satzung: {grabtyp} &mdash; g&uuml;nstigster regul&auml;rer Tarif f&uuml;r eine Sargbestattung</strong>
      <ul style="margin:8px 0 6px 18px;font-size:14px;line-height:1.7;padding:0">
        <li>{grab_zeile}</li>
        <li>Beisetzungsgeb&uuml;hr (Erdbestattung): <strong>{beis} &euro;</strong></li>{zusatz}
      </ul>
      <p style="font-size:12.5px;color:var(--mr-text-muted,#73655A);margin:6px 0 0;line-height:1.6">Direkt aus der <a href="{url}" rel="nofollow noopener" target="_blank" style="color:var(--mr-primary,#866E45)">amtlichen Geb&uuml;hrensatzung</a>{para_txt} &middot; Stand: {stand} &middot; von machsruhig gepr&uuml;ft am 13.07.2026.{netto} Was die Beisetzungsgeb&uuml;hr umfasst, unterscheidet sich je Stadt (teils nur Grab &ouml;ffnen/schlie&szlig;en, teils ein Leistungsb&uuml;ndel), und je nach Stadt k&ouml;nnen weitere Pflicht-Friedhofsgeb&uuml;hren (z.&thinsp;B. Grund-, Verwaltungs- oder j&auml;hrliche Unterhaltungsgeb&uuml;hren) hinzukommen. Das ist <strong>nicht</strong> der Gesamtpreis einer Bestattung &mdash; Bestatterleistungen, Sarg/Urne und Grabmal kommen hinzu (<a href="/tools/bestattungskosten-rechner/" style="color:var(--mr-primary,#866E45)">Kostenrechner</a>).</p>
    </div>
'''

re_geb_h2 = re.compile(r'<h2>Geb&uuml;hren|<h2>Gebühren')
# robust: Alt-Blöcke haben je nach Wiring-Version 4- oder 6-Space-Indent und
# inline-</div> (Box enthält keine verschachtelten divs -> non-greedy bis erstes </div> safe)
re_block = re.compile(r'[ \t]*<div class="fh-gebuehren-beispiel".*?</div>[ \t]*\r?\n?', re.S)
REFRESH = "--refresh" in sys.argv
done=[];skip=[];err=[]
for p in sorted(glob.glob(os.path.join(ROOT, "friedhoefe", "*", "index.html"))):
    slug = os.path.basename(os.path.dirname(p)); rel = os.path.relpath(p, ROOT)
    html = open(p, encoding="utf-8").read()
    if 'fh-gebuehren-beispiel' in html:
        if not REFRESH: skip.append(slug+"(schon)"); continue
        html2 = re_block.sub("", html, count=1)
        if 'fh-gebuehren-beispiel' in html2: err.append(slug+": Alt-Block nicht entfernbar"); continue
        html = html2
    c = find_city(slug)
    if not c: err.append(slug+": kein Register-Eintrag"); continue
    # Re-Audit 07/2026: STALE-Staedte (Werte unbelegt) NICHT regenerieren, bis Quelle gepinnt
    if c.get("_version_status") == "STALE":
        skip.append(slug+"(STALE - Werte unbelegt, wartet auf Quelle)"); continue
    b = block(c)
    if not b: err.append(slug+": unvollstaendige Daten"); continue
    m = re_geb_h2.search(html)
    if not m: err.append(slug+": keine Gebuehren-H2"); continue
    end = html.find("</section>", m.end())
    if end < 0: err.append(slug+": kein Sektions-Ende"); continue
    new = html[:end] + b + html[end:]
    # Asserts (Lektion 17)
    if new.count('fh-gebuehren-beispiel') != 1: err.append(slug+": Block!=1"); continue
    if new.count('</section>') != html.count('</section>'): err.append(slug+": section-Balance"); continue
    if new.count('<div') - new.count('</div>') != html.count('<div') - html.count('</div>'): err.append(slug+": div-Balance"); continue
    if not DRY: open(p, "w", encoding="utf-8").write(new)
    done.append(slug)
print(f"=== {'DRY' if DRY else 'APPLY'} === ok {len(done)} | skip {len(skip)} | err {len(err)}")
for e in err: print("  ERR", e)
for s in skip[:3]: print("  SKIP", s)
