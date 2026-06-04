#!/usr/bin/env python3
"""
iter-18 (2026-06-04): Mobile-Nav = Hamburger.
Bug: auf Mobile zeigte die Nav alle 7 Links vertikal gestapelt (kein Einklappen).
Der .mr-nav-toggle-Button war da, aber ohne Mobile-CSS/JS. Fix:
- Mobile-CSS (@media max-width:760px): Links per Default aus, Hamburger an,
  bei .mr-nav.open Links als Spalte.
- Winziges Toggle-JS vor </body> (Klick -> .open umschalten).
Beides idempotent (Marker), auf alle Seiten mit iter-15/16-Nav.
"""
import glob

CSS_MARKER = "iter-18 mobile-nav"
JS_MARKER = "iter-18-navjs"

CSS = """
/* """ + CSS_MARKER + """ (2026-06-04): Hamburger statt gestapelter Liste */
@media(max-width:760px){
  .mr-nav-inner{flex-wrap:wrap;gap:0;padding-top:8px;padding-bottom:8px}
  .mr-nav-toggle{display:inline-flex !important;align-items:center;margin-left:auto}
  .mr-nav-links{display:none;flex-basis:100%;flex-direction:column;gap:0;padding:6px 0 4px}
  .mr-nav.open .mr-nav-links{display:flex}
  .mr-nav-links a{padding:11px 6px;font-size:15px;border-radius:6px}
}
"""

JS = '<script>/*' + JS_MARKER + '*/(function(){var b=document.querySelector(".mr-nav-toggle"),n=document.querySelector(".mr-nav");if(b&&n){b.setAttribute("aria-expanded","false");b.addEventListener("click",function(){var o=n.classList.toggle("open");b.setAttribute("aria-expanded",o?"true":"false")})}})();</script>\n'

css_n = js_n = 0
for f in glob.glob("**/*.html", recursive=True):
    nf = f.replace("\\", "/")
    if nf.startswith("_dev/"):
        continue
    html = open(f, encoding="utf-8").read()
    if "iter-15 nav-slim" not in html and "iter-16 nav-graft" not in html:
        continue
    orig = html
    if CSS_MARKER not in html:
        idx = html.rfind("</style>")
        if idx != -1:
            html = html[:idx] + CSS + html[idx:]; css_n += 1
    if JS_MARKER not in html:
        idx = html.rfind("</body>")
        if idx != -1:
            html = html[:idx] + JS + html[idx:]; js_n += 1
        else:  # kein </body> -> vor </html>
            idx = html.rfind("</html>")
            if idx != -1:
                html = html[:idx] + JS + html[idx:]; js_n += 1
    if html != orig:
        open(f, "w", encoding="utf-8").write(html)
print(f"CSS injiziert: {css_n} | JS injiziert: {js_n}")
