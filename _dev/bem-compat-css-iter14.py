#!/usr/bin/env python3
"""
iter-14 (2026-06-04): BEM-Compat-CSS fuer das alte Stadt-Template.
~29 Stadt-Seiten nutzen ein BEM-Markup (mr-keyfacts__title, <dl>, mr-friedhof,
mr-faq__item, mr-footer__*, mr-list, mr-section__lead ...), dessen Original-
Stylesheet (/assets/css/main.css) nie eingecheckt war und in iter-10 entfernt
wurde. Berlins Inline-CSS stylt nur Block-Klassen, keine BEM-Subelemente ->
Kernfakten unlesbar, Friedhof-Karten/Callouts/FAQ/Footer unstyled.

Fix: self-contained Compat-CSS vor das letzte </style> (last-wins). Element-
qualifizierte Selektoren schlagen `.mr-section p` etc. Additiv -> auf den
kanonischen Seiten harmlos (BEM-Klassen kommen dort nicht vor). Auf alle 52.
"""
import glob, os

MARKER = "iter-14 bem-compat"
CSS = """
/* """ + MARKER + """ (2026-06-04): Styles fuer das BEM-Stadt-Template (Kernfakten/Friedhof/FAQ/Footer/Listen) */
.mr-keyfacts__title{font-family:'Fraunces',Georgia,serif;font-size:18px;font-weight:700;margin:0 0 16px;color:var(--mr-text,#2D2319)}
.mr-keyfacts dl{display:grid;grid-template-columns:1fr 1fr;gap:16px 28px;margin:0}
.mr-keyfacts dl>div{display:flex;flex-direction:column;gap:2px;padding-left:16px;position:relative}
.mr-keyfacts dl>div::before{content:'';position:absolute;left:0;top:7px;width:8px;height:8px;border-radius:50%;background:var(--mr-accent,#866E45)}
.mr-keyfacts dt{font-weight:700;font-size:13px;color:var(--mr-text,#2D2319)}
.mr-keyfacts dd{margin:0;font-size:14px;line-height:1.5;color:var(--mr-text-muted,#73655A)}
@media(max-width:560px){.mr-keyfacts dl{grid-template-columns:1fr}}
.mr-friedhof{background:var(--mr-bg-card,#FFFDF9);border:1px solid var(--mr-border,#E8E0D6);border-radius:var(--mr-radius,12px);padding:24px 28px;margin:0 0 20px}
.mr-friedhof h3{font-family:'Fraunces',Georgia,serif;font-size:19px;font-weight:700;margin:0 0 6px;color:var(--mr-text,#2D2319)}
.mr-friedhof p{font-size:15px;line-height:1.7;color:var(--mr-text,#2D2319);margin:0 0 12px}
.mr-friedhof p.mr-friedhof__meta{font-size:13px;color:var(--mr-warm,#7A6B5D);margin:0 0 12px}
.mr-friedhof p.mr-friedhof__hiddengem{background:var(--mr-safety,#FFFAF5);border-left:4px solid var(--mr-accent,#866E45);border-radius:8px;padding:14px 18px;font-size:14px;line-height:1.6}
.mr-friedhof.mr-friedhof--compact{padding:16px 20px}
.mr-friedhof--compact h3{font-size:16px}
.mr-list{margin:0 0 16px;padding-left:1.5em}
.mr-list li{font-size:15px;line-height:1.7;color:var(--mr-text,#2D2319);margin-bottom:8px}
ol.mr-list--ordered{list-style:decimal}
ul.mr-list{list-style:disc}
.mr-faq__item{border:1px solid var(--mr-border,#E8E0D6);border-radius:8px;background:var(--mr-bg-card,#FFFDF9);padding:16px 20px;margin-bottom:10px}
.mr-faq__item h3{font-size:15px;font-weight:700;margin:0 0 8px;color:var(--mr-text,#2D2319)}
.mr-faq__item p{font-size:14px;line-height:1.7;color:var(--mr-text-muted,#73655A);margin:0}
.mr-section p.mr-section__lead,.mr-hero p.mr-hero__lead{font-size:17px;line-height:1.7;color:var(--mr-text,#2D2319)}
.mr-section p.mr-section__note,.mr-sources p.mr-sources__note{font-size:13px;color:var(--mr-text-muted,#73655A);line-height:1.6}
.mr-section p.mr-section__updated,.mr-hero p.mr-hero__updated{font-size:13px;color:var(--mr-warm,#7A6B5D)}
.mr-hero .mr-hero__eyebrow{font-size:13px;font-weight:600;color:var(--mr-warm,#7A6B5D);text-transform:uppercase;letter-spacing:.5px}
.mr-section.mr-crosslink{background:var(--mr-bg-card,#FFFDF9);border:1px solid var(--mr-border,#E8E0D6);border-radius:var(--mr-radius,12px);padding:20px 24px}
.mr-footer__inner{max-width:720px;margin:0 auto;text-align:center}
.mr-footer__brand{font-family:'Fraunces',Georgia,serif;font-weight:700;font-size:15px;color:var(--mr-text,#2D2319);margin:0 0 12px}
.mr-footer__nav{display:flex;flex-wrap:wrap;justify-content:center;gap:8px 18px;margin:0 0 12px;padding:0}
.mr-footer__nav a{font-size:13px;color:var(--mr-text-muted,#73655A);text-decoration:none}
.mr-footer__nav a:hover{color:var(--mr-primary,#7A6B5D)}
.mr-footer__note{font-size:12px;color:var(--mr-text-muted,#73655A);line-height:1.6;margin:0}
"""

changed = 0
for f in glob.glob("bestatter/*/index.html"):
    html = open(f, encoding="utf-8").read()
    if MARKER in html:
        continue
    idx = html.rfind("</style>")
    if idx == -1:
        print("  !! kein </style>:", f); continue
    open(f, "w", encoding="utf-8").write(html[:idx] + CSS + html[idx:])
    changed += 1
print(f"Geaendert: {changed}")
