#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-friedhof-lotse.py — Register -> Gebuehren-Vergleich (Studien-Engine + Seite).
Friedl/Helfer-V4.1: Qualitaet sitzt im Datensatz + Provenienz; die Seite wird GENERIERT.
Liest _dev/claims/friedhofsgebuehren.json, rechnet roh + auf 20 Jahre normiert (Nutzungsdauer
je Stadt Zitat-belegt ODER Ruhezeit-Konvention, geflaggt) und schreibt:
  data/friedhofsgebuehren-vergleich.json   (Datensatz, cron-regenerierbar)
  friedhoefe/gebuehren/index.html          (server-gerenderte Seite; JS nur Sortieren/Filtern)
Asserts VOR jedem Write (Lektion 17). DRY default; --apply schreibt beides.
"""
import os, sys, json, re, html as _html

DRY = "--apply" not in sys.argv
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = json.load(open(os.path.join(ROOT, "_dev", "claims", "friedhofsgebuehren.json"), encoding="utf-8"))
OUT_JSON = os.path.join(ROOT, "data", "friedhofsgebuehren-vergleich.json")
OUT_HTML = os.path.join(ROOT, "friedhoefe", "gebuehren", "index.html")
STAND = "2026-07-06"  # Generierungs-Stand (Prüf-/Renderdatum); Register-Prüfdaten je Stadt getrennt

BL_NAME = {"BW":"Baden-Württemberg","BY":"Bayern","BE":"Berlin","BB":"Brandenburg","HB":"Bremen",
           "HH":"Hamburg","HE":"Hessen","MV":"Mecklenburg-Vorpommern","NI":"Niedersachsen",
           "NRW":"Nordrhein-Westfalen","RP":"Rheinland-Pfalz","SL":"Saarland","SN":"Sachsen",
           "ST":"Sachsen-Anhalt","SH":"Schleswig-Holstein","TH":"Thüringen"}

ND_ZITAT = {
    "Köln":25,"Frankfurt am Main":25,"Braunschweig":25,"Dortmund":25,"Dresden":20,"Düsseldorf":20,
    "Duisburg":20,"Erfurt":20,"Essen":25,"Halle (Saale)":30,"Hamm":30,"Hannover":20,"Heidelberg":25,
    "Kiel":25,"Ludwigshafen am Rhein":30,"Leipzig":20,"Magdeburg":20,"Mannheim":15,"Mönchengladbach":25,
    "Mülheim an der Ruhr":25,"Oberhausen":30,"Rostock":20,"Saarbrücken":20,"Stuttgart":20,"Wiesbaden":30,
    "Wuppertal":20,"Chemnitz":20,"Berlin":20,
}
ND_KONVENTION = {"Bochum","Bremen","Gelsenkirchen","Hagen","Lübeck","Münster","Oldenburg","Krefeld","Mainz"}


def num(x):
    try: return float(x)
    except (TypeError, ValueError): return None

def fold(s):
    s = s.lower()
    for a, b in (("ä","ae"),("ö","oe"),("ü","ue"),("ß","ss")): s = s.replace(a, b)
    return re.sub(r"[^a-z]", "", s)

def slug(stadt): return fold(stadt.split("(")[0].split()[0])

def esc(s): return _html.escape(str(s), quote=True)

def eur(n): return f"{int(round(n)):,}".replace(",", ".")


# ---------- Datenschicht ----------
out = []
for c in REG["staedte"]:
    st = c.get("stadt"); bl = c.get("bundesland")
    grab = num(c.get("grabnutzung_betrag_eur")); einheit = c.get("grabnutzung_einheit")
    beis = num(c.get("beisetzung_betrag_eur")) or 0.0; ruhe = c.get("ruhezeit_jahre")
    if grab is None: continue
    if einheit == "pro_jahr":
        nd, nd_basis, nd_flag = 20, "Jahresgebühr × 20 Jahre", False
        grab_20j = grab * 20
        roh_hinweis = f"{eur(grab)} €/Jahr"
    else:
        if st in ND_ZITAT: nd, nd_basis, nd_flag = ND_ZITAT[st], "Nutzungsdauer laut Satzung", False
        elif st in ND_KONVENTION: nd, nd_basis, nd_flag = ruhe, "Nutzungsdauer = Ruhezeit (Satzungstarif nennt keine abweichende Dauer)", True
        else: nd, nd_basis, nd_flag = ruhe, "Ruhezeit (Fallback)", True
        assert nd, f"{st}: keine Nutzungsdauer"
        grab_20j = grab / nd * 20
        roh_hinweis = f"{eur(grab)} € für {nd} Jahre"
    out.append({
        "stadt": st, "slug": slug(st), "bundesland": bl, "bl_name": BL_NAME.get(bl, bl),
        "grabnutzung_eur": round(grab, 2), "grabnutzung_einheit": einheit,
        "nutzungsdauer_jahre": nd, "nutzungsdauer_basis": nd_basis, "nd_konvention": nd_flag,
        "beisetzung_eur": round(beis, 2), "ruhezeit_jahre": ruhe,
        "roh_summe_eur": round(grab + beis), "roh_hinweis": roh_hinweis,
        "vergleich_20j_eur": round(grab_20j + beis),
        "satzung_url": (c.get("satzung_url") or "").split(" ;")[0].split(" ")[0],
        "grabnutzung_paragraph": c.get("grabnutzung_paragraph"),
        "last_checked": c.get("last_checked"), "confidence": c.get("confidence"),
    })

# ---------- Asserts vor Write ----------
assert len(out) == 50, f"erwartet 50, bekam {len(out)}"
assert all(r["vergleich_20j_eur"] > 0 for r in out), "0/neg Vergleichswert"
assert len({r["stadt"] for r in out}) == 50, "Stadt-Dublette"
for r in out:
    assert os.path.isfile(os.path.join(ROOT, "friedhoefe", r["slug"], "index.html")), f"Dead-Link {r['slug']}"
    assert r["satzung_url"].startswith("http"), f"{r['stadt']}: keine Satzungs-URL"

ranked = sorted(out, key=lambda r: r["vergleich_20j_eur"])
lo, hi = ranked[0], ranked[-1]
med = ranked[len(ranked)//2]
maxv = hi["vergleich_20j_eur"]
n_konv = sum(1 for r in out if r["nd_konvention"])


# ---------- SVG-Chart (sortiert, neutral, Preis-Transparenz — kein Wert-Urteil) ----------
rowH, labW, padR, chartW = 15, 152, 62, 360
svgH = len(ranked) * rowH + 30
bars = []
for i, r in enumerate(ranked):
    y = 24 + i * rowH
    w = max(2, r["vergleich_20j_eur"] / maxv * chartW)
    bars.append(
        f'<text x="{labW-6}" y="{y+9}" text-anchor="end" class="cl">{esc(r["stadt"])}</text>'
        f'<rect x="{labW}" y="{y}" width="{w:.1f}" height="{rowH-4}" rx="1.5" class="cb"/>'
        f'<text x="{labW+w+5:.1f}" y="{y+9}" class="cv">{eur(r["vergleich_20j_eur"])} €</text>')
medx = labW + med["vergleich_20j_eur"] / maxv * chartW
chart = (
    f'<svg viewBox="0 0 {labW+chartW+padR} {svgH}" role="img" '
    f'aria-label="Balkendiagramm: Erd-Wahlgrab-Kosten (20 Jahre) in 50 Städten, von Berlin 805 € bis Mainz 4.714 €" '
    f'style="width:100%;height:auto;font-family:\'DM Sans\',system-ui,sans-serif">'
    f'<line x1="{medx:.1f}" y1="18" x2="{medx:.1f}" y2="{svgH-6}" class="cmed"/>'
    f'<text x="{medx:.1f}" y="12" text-anchor="middle" class="cmedl">Median {eur(med["vergleich_20j_eur"])} €</text>'
    + "".join(bars) + '</svg>')


# ---------- Tabellenzeilen (Default: nach Vergleichswert aufsteigend) ----------
trs = []
for r in ranked:
    flag = ' <abbr title="Nutzungsdauer aus der Ruhezeit abgeleitet (Satzungstarif nennt keine eigene Dauer)">≈</abbr>' if r["nd_konvention"] else ""
    src = f'<a href="{esc(r["satzung_url"])}" rel="nofollow noopener" target="_blank">Satzung↗</a>' if r["satzung_url"] else "—"
    trs.append(
        f'<tr data-name="{esc(fold(r["stadt"]))}" data-bl="{esc(r["bundesland"])}" '
        f'data-v20="{r["vergleich_20j_eur"]}" data-roh="{r["roh_summe_eur"]}" data-nd="{r["nutzungsdauer_jahre"]}">'
        f'<td class="c-stadt"><a href="/friedhoefe/{esc(r["slug"])}/">{esc(r["stadt"])}</a>'
        f'<span class="c-bl">{esc(r["bl_name"])}</span></td>'
        f'<td class="c-num c-v20"><strong>{eur(r["vergleich_20j_eur"])} €</strong></td>'
        f'<td class="c-num c-roh">{eur(r["grabnutzung_eur"])} €<span class="c-sub">{esc(r["roh_hinweis"].split("für ")[-1] if "für" in r["roh_hinweis"] else r["roh_hinweis"])}</span></td>'
        f'<td class="c-num">{eur(r["beisetzung_eur"])} €</td>'
        f'<td class="c-num">{r["nutzungsdauer_jahre"]} J.{flag}</td>'
        f'<td class="c-src">{src}<span class="c-sub">geprüft {esc(r["last_checked"])}</span></td>'
        f'</tr>')

bl_options = "".join(f'<option value="{k}">{esc(v)}</option>'
                     for k, v in sorted(BL_NAME.items(), key=lambda kv: kv[1])
                     if any(r["bundesland"] == k for r in out))

jsonld = {
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "Dataset", "name": "Friedhofsgebühren in 50 deutschen Städten (Erd-Wahlgrab)",
         "description": "Eigenerhobenes Register der Friedhofsgebühren für ein einstelliges Erd-Wahlgrab (Grabnutzung + Beisetzung) in den 50 größten deutschen Städten, aus den amtlichen Gebührensatzungen (§ 5 UrhG), auf 20 Jahre normiert. Zweimal re-verifiziert.",
         "url": "https://machsruhig.de/friedhoefe/gebuehren/",
         "license": "https://creativecommons.org/licenses/by/4.0/",
         "creator": {"@type": "Organization", "name": "machsruhig.de", "url": "https://machsruhig.de"},
         "spatialCoverage": {"@type": "Country", "name": "Deutschland"},
         "isAccessibleForFree": True, "inLanguage": "de-DE",
         "variableMeasured": ["Grabnutzungsgebühr Erd-Wahlgrab", "Beisetzungsgebühr", "Ruhezeit", "Nutzungsdauer"]},
        {"@type": "CollectionPage", "name": "Friedhofsgebühren im Städtevergleich",
         "url": "https://machsruhig.de/friedhoefe/gebuehren/", "inLanguage": "de-DE",
         "publisher": {"@type": "Organization", "name": "machsruhig.de", "url": "https://machsruhig.de"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Start", "item": "https://machsruhig.de/"},
            {"@type": "ListItem", "position": 2, "name": "Friedhöfe", "item": "https://machsruhig.de/friedhoefe/"},
            {"@type": "ListItem", "position": 3, "name": "Gebühren", "item": "https://machsruhig.de/friedhoefe/gebuehren/"}]},
    ]}

TEMPLATE = r"""<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Friedhofsgebühren: Was ein Grab in 50 Städten kostet | mach's ruhig</title><meta name="description" content="Was kostet ein Grab? Friedhofsgebühren für ein Erd-Wahlgrab in 50 deutschen Städten im Vergleich — von 805 € (Berlin) bis 4.714 € (Mainz). Aus den amtlichen Satzungen erhoben, auf 20 Jahre normiert, mit Quelle je Stadt."><meta name="robots" content="index,follow"><link rel="canonical" href="https://machsruhig.de/friedhoefe/gebuehren/"><meta property="og:title" content="Friedhofsgebühren im Städtevergleich — was ein Grab kostet"><meta property="og:description" content="Erd-Wahlgrab in 50 Städten: von 805 € (Berlin) bis 4.714 € (Mainz). Amtliche Satzungen, auf 20 Jahre normiert, Quelle je Stadt."><meta property="og:type" content="website"><meta property="og:image" content="https://machsruhig.de/assets/og-image.png"><meta property="og:url" content="https://machsruhig.de/friedhoefe/gebuehren/"><meta property="og:locale" content="de_DE"><meta property="og:site_name" content="mach's ruhig">
<script defer src="https://cloud.umami.is/script.js" data-website-id="6b6629ff-27b8-427b-863c-76b549cb52ba"></script><script>window.plausible=function(e,o){if(window.umami)window.umami.track(e,(o&&o.props)||{});};</script>
<script defer src="/js/tracking.js?v=20260702"></script>
<script type="application/ld+json">__JSONLD__</script>
<style>
@font-face{font-family:'DM Sans';font-style:normal;font-display:swap;font-weight:300 700;src:url('/fonts/dm-sans-latin-wght-normal.woff2') format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}@font-face{font-family:'Fraunces';font-style:normal;font-display:swap;font-weight:400 800;src:url('/fonts/fraunces-latin-wght-normal.woff2') format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}
*{box-sizing:border-box;margin:0;padding:0}body{font-family:'DM Sans',system-ui,sans-serif;background:#faf8f5;color:#2D2319;font-size:16px;line-height:1.6}
.mr-nav{position:sticky;top:0;z-index:100;background:rgba(250,248,245,.95);border-bottom:1px solid #E8E0D6;padding:0}
.mr-nav-inner{max-width:900px;margin:0 auto;display:flex;align-items:center;gap:6px 14px;flex-wrap:wrap;min-height:56px;padding:0 20px}
.mr-nav-logo{margin-right:auto;font-family:'Fraunces',Georgia,serif;font-size:18px;font-weight:700;color:#2D2319;text-decoration:none;white-space:nowrap}.mr-nav-logo span{color:#7A6B5D}
.mr-nav-links{display:flex;gap:4px}.mr-nav-links a{font-size:13px;color:#73655A;text-decoration:none;padding:6px 10px}.mr-nav-links a.active{color:#7A6B5D;font-weight:600}
.mr-nav-toggle{display:none;background:none;border:none;cursor:pointer;color:#2D2319}
.mr-content{max-width:900px;margin:0 auto;padding:0 20px}
.mr-breadcrumb{font-size:13px;color:#73655A;padding:14px 0 0}.mr-breadcrumb a{color:#73655A}
.mr-hero{padding:26px 0 8px}.mr-hero h1{font-size:clamp(26px,4.4vw,38px);font-weight:800;line-height:1.18;margin-bottom:14px;font-family:'Fraunces',Georgia,serif}
.mr-hero .lead{font-size:17.5px;line-height:1.65;color:#4a4038;max-width:680px}
.stat{display:flex;flex-wrap:wrap;gap:14px;margin:22px 0 8px}
.stat .card{flex:1 1 150px;background:#FFFDF9;border:1px solid #E8E0D6;border-radius:12px;padding:14px 16px}
.stat .big{font-size:26px;font-weight:800;font-family:'Fraunces',Georgia,serif;color:#2D2319;line-height:1.1}
.stat .lbl{font-size:12.5px;color:#73655A;margin-top:3px}
.mr-section{margin:34px 0}.mr-section h2{font-size:21px;font-weight:700;margin-bottom:14px;font-family:'Fraunces',Georgia,serif}
details.methodik{background:#FFFAF5;border:1px solid #E8E0D6;border-left:4px solid #866E45;border-radius:8px;padding:14px 18px;margin:18px 0;font-size:14.5px}
details.methodik summary{font-weight:600;cursor:pointer;color:#2D2319}details.methodik ul{margin:10px 0 2px 18px}details.methodik li{margin:5px 0}
.chartwrap{background:#FFFDF9;border:1px solid #E8E0D6;border-radius:12px;padding:16px 14px;overflow-x:auto}
.cl{font-size:9.5px;fill:#4a4038}.cb{fill:#B08D57}.cv{font-size:9px;fill:#73655A}.cmed{stroke:#C6402F;stroke-width:1;stroke-dasharray:3 3}.cmedl{font-size:9px;fill:#C6402F;font-weight:600}
.controls{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:0 0 12px}
.controls input,.controls select{padding:9px 12px;border:1px solid #E8E0D6;border-radius:9px;font-size:14px;font-family:inherit;background:#faf8f5;color:#2D2319}
.controls input{flex:1 1 190px;max-width:280px}
.sortbtn{padding:8px 12px;border:1px solid #E8E0D6;border-radius:9px;background:#FFFDF9;font-size:13px;cursor:pointer;color:#2D2319;font-family:inherit}
.sortbtn[aria-pressed="true"]{background:#866E45;color:#fff;border-color:#866E45}
.tablewrap{overflow-x:auto;border:1px solid #E8E0D6;border-radius:12px}
table.lotse{width:100%;border-collapse:collapse;font-size:14px;min-width:560px;background:#FFFDF9}
table.lotse th{text-align:left;font-size:11.5px;letter-spacing:.02em;text-transform:uppercase;color:#73655A;font-weight:600;padding:11px 12px;border-bottom:1.5px solid #E8E0D6;white-space:nowrap}
table.lotse td{padding:10px 12px;border-bottom:1px solid #F0EAE1;vertical-align:top}
table.lotse tr:last-child td{border-bottom:none}
.c-num{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
.c-stadt a{color:#2D2319;text-decoration:none;font-weight:600}.c-stadt a:hover{color:#7A6B5D;text-decoration:underline}
.c-bl,.c-sub{display:block;font-size:11.5px;color:#8a7d70;font-weight:400}
.c-v20 strong{color:#2D2319}.c-src a{color:#866E45;font-size:13px}
.norm-note{font-size:13px;color:#73655A;margin:10px 2px 0}
.mr-cta{background:#2D2319;border-radius:14px;padding:22px 22px;color:#F5EFE7;margin:30px 0}
.mr-cta h2{color:#fff;font-size:19px;margin-bottom:6px;font-family:'Fraunces',Georgia,serif}
.mr-cta p{font-size:14.5px;color:#D9CFC2;margin-bottom:14px}
.mr-cta .btns{display:flex;flex-wrap:wrap;gap:10px}
.mr-cta a{display:inline-block;padding:11px 18px;border-radius:9px;text-decoration:none;font-size:14.5px;font-weight:600}
.mr-cta a.primary{background:#C9A227;color:#2D2319}.mr-cta a.secondary{background:transparent;color:#F5EFE7;border:1px solid #6b5d4d}
.mr-sources{background:#f4f0eb;border:1px solid #E8E0D6;border-radius:10px;padding:16px 18px;font-size:13.5px;color:#4a4038;margin:26px 0}
.mr-sources h2{font-size:15px;margin-bottom:8px;font-family:'DM Sans',sans-serif}.mr-sources ul{margin:6px 0 0 18px}.mr-sources li{margin:4px 0}
.mr-footer{background:#f4f0eb;border-top:1px solid #E8E0D6;margin-top:56px;padding:36px 20px;color:#73655A;text-align:center;font-size:13px}.mr-footer a{color:#73655A;margin:0 10px}
.empty{display:none;padding:18px;text-align:center;color:#73655A;font-size:14px}
@media(max-width:760px){.mr-nav-toggle{display:inline-flex;align-items:center;margin-left:auto}.mr-nav-links{display:none;flex-basis:100%;flex-direction:column;gap:0;padding:6px 0 4px}.mr-nav.open .mr-nav-links{display:flex}.mr-nav-links a{padding:11px 6px;font-size:15px}.c-roh .c-sub{white-space:normal}}
</style><link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/dm-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/fonts/fraunces-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
</head><body>
<nav class="mr-nav no-print"><div class="mr-nav-inner">
<a href="/" class="mr-nav-logo">mach's <span>ruhig</span></a>
<button class="mr-nav-toggle" aria-label="Menü öffnen" type="button"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12h18M3 6h18M3 18h18"/></svg></button>
<div class="mr-nav-links"><a href="/was-tun-nach-todesfall">Was tun?</a><a href="/beerdigung-planen">Beerdigung</a><a href="/bestattungskosten">Kosten</a><a href="/friedhoefe/" class="active">Friedhöfe</a><a href="/bestatter/">Bestatter</a><a href="/tools/angebotspruefer/">Angebot prüfen</a></div>
</div></nav>
<main class="mr-content">
<nav class="mr-breadcrumb" aria-label="Brotkrumen"><a href="/">Start</a> › <a href="/friedhoefe/">Friedhöfe</a> › Gebühren</nav>
<div class="mr-hero">
<h1>Was kostet ein Grab? Friedhofsgebühren in 50 Städten</h1>
<p class="lead">Für ein einstelliges <strong>Erd-Wahlgrab</strong> — Grabnutzung plus Beisetzung, auf 20 Jahre gerechnet — reicht die Spanne vom günstigsten bis zum teuersten Ort auf mehr als das Fünffache. Alle Zahlen stammen aus den <strong>amtlichen Gebührensatzungen</strong> der Städte (öffentlich, § 5 UrhG), sind zweimal geprüft und je Stadt mit Quelle belegt.</p>
<div class="stat">
<div class="card"><div class="big">__LO_EUR__ €</div><div class="lbl">am günstigsten — __LO_STADT__</div></div>
<div class="card"><div class="big">__HI_EUR__ €</div><div class="lbl">am teuersten — __HI_STADT__</div></div>
<div class="card"><div class="big">__FAKTOR__×</div><div class="lbl">Unterschied zwischen teuerster und günstigster Stadt</div></div>
</div>
</div>

<details class="methodik" open><summary>Wie wir rechnen (Methodik &amp; Grenzen)</summary>
<ul>
<li><strong>Einheit:</strong> einstelliges Erd-Wahlgrab in regulärer Standardlage (keine Premium-/Sonderzone). Verglichen wird <strong>Grabnutzung + Beisetzung</strong> (Öffnen/Schließen). Trauerhalle, Grabstein und Grabpflege sind <em>nicht</em> enthalten.</li>
<li><strong>Auf 20 Jahre normiert:</strong> Jahresgebühr-Städte × 20; Einmalsummen ÷ ihre Nutzungsdauer × 20 — damit ein 30-Jahre-Grab mit einem 20-Jahre-Grab vergleichbar wird. Roh-Betrag und Nutzungsdauer je Stadt stehen in der Tabelle.</li>
<li><strong>Nutzungsdauer:</strong> wo der Satzungstarif keine eigene Dauer nennt (mit „≈“ markiert), setzen wir die gesetzliche Ruhezeit an — man erwirbt das Nutzungsrecht in der Regel für diese Zeit. Das ist der eine Punkt, den man je Stadt genau lesen sollte.</li>
<li><strong>Nicht 1:1 vergleichbar bleibt:</strong> was eine Stadt unter „Beisetzung“ bündelt, ist unterschiedlich (manche zählen nur Öffnen/Schließen, andere mehr). Die Spanne zeigt die Größenordnung, kein centgenaues Ranking.</li>
<li><strong>Quelle:</strong> jede Zahl aus der amtlichen Gebührensatzung der Stadt (§ 5 UrhG = gemeinfrei), Stand und Link je Zeile. Kein fremdes Verzeichnis kopiert — eigenerhoben.</li>
</ul>
</details>

<section class="mr-section">
<h2>Alle 50 Städte im Diagramm</h2>
<div class="chartwrap">__CHART__</div>
<p class="norm-note">Erd-Wahlgrab, Grabnutzung (auf 20 Jahre) + Beisetzung. Sortiert von günstig nach teuer.</p>
</section>

<section class="mr-section">
<h2>Tabelle — sortieren &amp; filtern</h2>
<div class="controls">
<input type="search" id="q" placeholder="Stadt suchen …" autocomplete="off" aria-label="Stadt suchen">
<select id="blf" aria-label="Bundesland filtern"><option value="">Alle Bundesländer</option>__BL_OPTIONS__</select>
<button class="sortbtn" data-sort="v20" aria-pressed="true">Preis ↑</button>
<button class="sortbtn" data-sort="name" aria-pressed="false">A–Z</button>
</div>
<div class="tablewrap"><table class="lotse">
<thead><tr><th>Stadt</th><th class="c-num">Grab gesamt<br>20 Jahre</th><th class="c-num">Grabnutzung<br>(roh)</th><th class="c-num">Beisetzung</th><th class="c-num">Nutzungs&shy;dauer</th><th>Quelle</th></tr></thead>
<tbody id="tb">__ROWS__</tbody>
</table></div>
<p class="empty" id="empty">Keine Stadt gefunden.</p>
<p class="norm-note">„Grab gesamt (20 Jahre)“ = Grabnutzung auf 20 Jahre normiert + Beisetzung. „≈“ = Nutzungsdauer aus der Ruhezeit abgeleitet. Stadtname öffnet die volle Friedhofs-Übersicht.</p>
</section>

<div class="mr-cta">
<h2>Und was heißt das für deinen Fall?</h2>
<p>Die Friedhofsgebühr ist nur ein Teil der Bestattungskosten. Rechne deine Gesamtkosten für deine Stadt aus — oder lass ein Bestatter-Angebot kostenlos auf Vollständigkeit und faire Posten prüfen.</p>
<div class="btns"><a class="primary" href="/tools/bestattungskosten-rechner/" data-track="cta">Bestattungskosten berechnen</a><a class="secondary" href="/tools/angebotspruefer/" data-track="cta">Angebot prüfen lassen</a></div>
</div>

<div class="mr-sources">
<h2>Quellen &amp; Nutzung</h2>
<ul>
<li>Grundlage: eigenerhobenes Register der Friedhofsgebühren, aus den <strong>amtlichen Gebührensatzungen</strong> der 50 Städte (kommunale Satzungen = amtliche Werke, § 5 UrhG, gemeinfrei). Die Satzungsquelle jeder Stadt ist in der Tabellenspalte „Quelle“ verlinkt.</li>
<li>Rechenweg und Grabkosten-Modell: siehe <a href="/methodik">Methodik</a>. Register zweimal unabhängig aus der Satzung geprüft; Prüfdatum je Stadt in der Tabelle.</li>
<li>Der Datensatz steht unter <a href="https://creativecommons.org/licenses/by/4.0/deed.de" rel="noopener" target="_blank">CC&nbsp;BY&nbsp;4.0</a> — Weiterverwendung mit Quellenangabe „machsruhig.de“ erwünscht (z. B. für Presse). Fehler gefunden? <a href="/kontakt">Sag uns Bescheid.</a></li>
</ul>
</div>
</main>
<footer class="mr-footer"><p>© 2026 mach's ruhig · <a href="/impressum">Impressum</a> · <a href="/datenschutz">Datenschutz</a> · <a href="/methodik">Methodik</a></p></footer>
<script>
/* Nav-Toggle */(function(){var b=document.querySelector(".mr-nav-toggle"),n=document.querySelector(".mr-nav");if(b&&n){b.setAttribute("aria-expanded","false");b.addEventListener("click",function(){var o=n.classList.toggle("open");b.setAttribute("aria-expanded",o?"true":"false")})}})();
/* Filter + Sort */(function(){
var tb=document.getElementById("tb"),q=document.getElementById("q"),blf=document.getElementById("blf"),empty=document.getElementById("empty");
if(!tb)return;var rows=[].slice.call(tb.querySelectorAll("tr")),sort="v20";
function fold(s){return s.toLowerCase().replace(/ä/g,"ae").replace(/ö/g,"oe").replace(/ü/g,"ue").replace(/ß/g,"ss");}
function apply(){
var term=fold(q.value.trim()),bl=blf.value,vis=0;
rows.forEach(function(r){var ok=(!term||r.getAttribute("data-name").indexOf(term)>=0)&&(!bl||r.getAttribute("data-bl")===bl);r.style.display=ok?"":"none";if(ok)vis++;});
empty.style.display=vis?"none":"block";}
function doSort(key){
sort=key;
document.querySelectorAll(".sortbtn").forEach(function(b){b.setAttribute("aria-pressed",b.getAttribute("data-sort")===key?"true":"false");});
var sorted=rows.slice().sort(function(a,b){
if(key==="name")return a.getAttribute("data-name")<b.getAttribute("data-name")?-1:1;
return (+a.getAttribute("data-v20"))-(+b.getAttribute("data-v20"));});
sorted.forEach(function(r){tb.appendChild(r);});}
q.addEventListener("input",apply);blf.addEventListener("change",apply);
document.querySelectorAll(".sortbtn").forEach(function(b){b.addEventListener("click",function(){doSort(b.getAttribute("data-sort"));});});
})();
</script>
</body></html>"""

html_out = (TEMPLATE
    .replace("__JSONLD__", json.dumps(jsonld, ensure_ascii=False))
    .replace("__CHART__", chart)
    .replace("__ROWS__", "".join(trs))
    .replace("__BL_OPTIONS__", bl_options)
    .replace("__LO_EUR__", eur(lo["vergleich_20j_eur"])).replace("__LO_STADT__", esc(lo["stadt"]))
    .replace("__HI_EUR__", eur(hi["vergleich_20j_eur"])).replace("__HI_STADT__", esc(hi["stadt"]))
    .replace("__FAKTOR__", f'{hi["vergleich_20j_eur"]/lo["vergleich_20j_eur"]:.1f}'.replace(".", ",")))

# HTML-Asserts vor Write
_ph = re.findall(r'__[A-Z][A-Z_]+__', html_out)
assert not _ph, f"unersetzter Platzhalter: {_ph}"
# F3-Selbstcheck: keine deutsche Öffnung „ mit ASCII-Schließung " im SICHTBAREN Text (nicht Attribute)
_vis = re.sub(r'<[^>]+>', ' ', html_out)
assert not re.search(r'„[^„“"]*?"', _vis), "F3-Risiko: „ mit ASCII-Schließzeichen im sichtbaren Text"
for j in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html_out, re.S):
    json.loads(j)  # JSON-LD parsebar

print(f"Datensatz: {len(out)} Städte · Spread {lo['stadt']} {eur(lo['vergleich_20j_eur'])} € → {hi['stadt']} {eur(hi['vergleich_20j_eur'])} € ({hi['vergleich_20j_eur']/lo['vergleich_20j_eur']:.1f}×)")
print(f"ND-Basis: {50-n_konv-12+ (0)} … Konvention-Flags: {n_konv}")
print(f"HTML: {len(html_out)} Bytes, {len(trs)} Tabellenzeilen, JSON-LD valide")

if DRY:
    print(f"\n[DRY] wuerde schreiben:\n  {OUT_JSON}\n  {OUT_HTML}\n  (mit --apply)")
else:
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    os.makedirs(os.path.dirname(OUT_HTML), exist_ok=True)
    payload = {"_doc": "Friedhofsgebuehren-Vergleich Erd-Wahlgrab; Grabnutzung 20J-normiert + Beisetzung.",
               "stand": STAND, "spread": {"guenstigste": lo["stadt"], "guenstigste_eur": lo["vergleich_20j_eur"],
               "teuerste": hi["stadt"], "teuerste_eur": hi["vergleich_20j_eur"]},
               "staedte": sorted(out, key=lambda r: r["stadt"])}
    json.dump(payload, open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(OUT_HTML, "w", encoding="utf-8").write(html_out)
    print(f"\n[OK] geschrieben: {OUT_JSON}  +  {OUT_HTML}")
