#!/usr/bin/env python3
"""
Sprint #2: 5 Gold-Städte von CSR-Lead-Form auf Static Shell umstellen.

Was passiert:
1. React + Babel-Standalone-Scripts entfernen
2. Lead-Form-Block durch statischen "Was wir für dich tun"-Block ersetzen
3. Mobile-Nav-Toggle von inline-onclick auf sauberes Vanilla-JS
4. OG-Image ergänzen (og-image.png)
5. Skip-Link-Inline-Style als CSS-Klasse
6. Methodik in Navigation ergänzen

Das Lead-Form wird in Phase F aktiviert — aktuell ist Trust-Layer wichtiger.
"""
import re
from pathlib import Path

CITIES = ["berlin", "frankfurt", "hamburg", "koeln", "muenchen"]
ROOT = Path(__file__).resolve().parent.parent  # _dev/ → repo root

# Das ist das statische Ersatz-HTML für den Lead-Form-Block
# Für jede Stadt wird {city_name} ersetzt
STATIC_REPLACEMENT = """  <div class="mr-hint" role="note">
    <strong>Bestatter in {city_name} finden:</strong>
    Wir sind unabhängig und vermitteln aktuell keine direkten Kontakte.
    Unsere Lead-Integration bauen wir nach sorgfältiger Prüfung in den kommenden Monaten auf
    (siehe <a href="/methodik">Methodik</a>). Bis dahin empfehlen wir:
    Vergleiche mindestens drei Bestatter, frage schriftliche Kostenvoranschläge an
    und achte auf Mitgliedschaft im <a href="https://www.bestatter.de" rel="noopener" target="_blank">Bundesverband Deutscher Bestatter</a>.
  </div>"""

# Mobile-Nav-Toggle-Ersatz (vanilla JS am Ende des body)
VANILLA_NAV_SCRIPT = """<script>
(function(){
  var btn = document.querySelector('.mr-nav-toggle');
  var menu = document.querySelector('.mr-nav-links');
  if(!btn || !menu) return;
  btn.setAttribute('aria-expanded', 'false');
  btn.setAttribute('aria-controls', 'mr-nav-links');
  menu.id = menu.id || 'mr-nav-links';
  btn.addEventListener('click', function(){
    var open = menu.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  menu.querySelectorAll('a').forEach(function(a){
    a.addEventListener('click', function(){
      if(window.innerWidth <= 760){
        menu.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  });
})();
</script>
</body>"""

# OG-Image-Meta-Tags (werden nach og:url eingefügt)
OG_IMAGE_TAGS = """<meta property="og:image" content="https://machsruhig.de/assets/og-image.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="mach's ruhig — Vorsorge, Trauer und Bestattung">
<meta property="og:locale" content="de_DE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://machsruhig.de/assets/og-image.png">"""

# Skip-Link als CSS (wird in <style> eingefügt falls nicht vorhanden)
SKIP_LINK_CSS = """.skip-link{position:absolute;top:-40px;left:0;background:var(--mr-primary);color:#fff;padding:8px 16px;z-index:200;border-radius:0 0 4px 0;transition:top 0.2s;text-decoration:none}.skip-link:focus{top:0}"""


def transform(city: str) -> tuple[bool, list[str]]:
    """Transformiere eine Stadt. Returns (success, notes)."""
    path = ROOT / "bestatter" / city / "index.html"
    if not path.exists():
        return False, [f"Datei nicht gefunden: {path}"]

    html = path.read_text(encoding="utf-8")
    original = html
    notes = []
    city_name = {"berlin": "Berlin", "frankfurt": "Frankfurt", "hamburg": "Hamburg",
                 "koeln": "Köln", "muenchen": "München"}[city]

    # --- 1. React/Babel/LeadForm-Scripts komplett entfernen -----------------
    # Alles zwischen den React-Imports und </body>
    pattern = re.compile(
        r'<script crossorigin src="https://unpkg\.com/react@18.*?</script>\s*'
        r'</body>',
        re.DOTALL
    )
    if pattern.search(html):
        html = pattern.sub(VANILLA_NAV_SCRIPT, html)
        notes.append("React + Babel + LeadForm entfernt, Vanilla-Nav eingefügt")
    else:
        notes.append("WARNING: Kein React-Block gefunden — schon sauber?")

    # --- 2. Lead-Form-Div durch statischen Block ersetzen -------------------
    leadform_pattern = re.compile(
        r'<div class="mr-form-wrap no-print">\s*'
        r'<h3>[^<]+</h3>\s*'
        r'<p>[^<]+</p>\s*'
        r'<div id="lead-form-container"></div>\s*'
        r'</div>',
        re.DOTALL
    )
    replacement = STATIC_REPLACEMENT.format(city_name=city_name)
    if leadform_pattern.search(html):
        html = leadform_pattern.sub(replacement, html)
        notes.append("Lead-Form-Div durch Hint-Block ersetzt")

    # --- 3. OG-Image-Tags einfügen (falls nicht vorhanden) ------------------
    if 'og:image' not in html:
        # Nach og:url einfügen
        html = re.sub(
            r'(<meta property="og:url"[^>]+>)',
            r'\1\n' + OG_IMAGE_TAGS,
            html,
            count=1
        )
        notes.append("OG-Image-Tags hinzugefügt")

    # --- 4. Skip-Link: Inline-Style durch CSS-Klasse ersetzen ---------------
    old_skip = re.compile(
        r'<a href="#main" class="skip-link"\s+style="[^"]*"\s+onFocus="[^"]*"\s+onBlur="[^"]*">([^<]+)</a>'
    )
    if old_skip.search(html):
        html = old_skip.sub(r'<a href="#main" class="skip-link">\1</a>', html)
        notes.append("Skip-Link Inline-Style durch CSS-Klasse ersetzt")

    # Ggf. skip-link-CSS in <style> einfügen
    if '.skip-link{' not in html and '<a href="#main" class="skip-link">' in html:
        # Nach ersten :root{ einfügen
        html = re.sub(
            r'(:root\{[^}]+\})',
            r'\1\n' + SKIP_LINK_CSS,
            html,
            count=1
        )
        notes.append("Skip-Link-CSS ergänzt")

    # --- 5. Mobile-Nav: inline onclick entfernen, button aufräumen ----------
    # Alt: <button ... onclick="document.querySelector('.mr-nav-links').classList.toggle('open')" ...>
    # Neu: ohne onclick (das Vanilla-JS macht das)
    html = re.sub(
        r'onclick="document\.querySelector\(\'\.mr-nav-links\'\)\.classList\.toggle\(\'open\'\)"\s*',
        '',
        html
    )

    # --- 6. Methodik-Link in Navigation ergänzen ----------------------------
    # Nach "Bestatter finden" einen Divider + Methodik einfügen
    nav_pattern = re.compile(
        r'(<a href="/bestatter/muenchen/">Bestatter finden</a>)\s*(</div>\s*</div>\s*</nav>)'
    )
    if nav_pattern.search(html) and '/methodik' not in html[html.find('mr-nav-links'):html.find('</nav>')]:
        html = nav_pattern.sub(
            r'\1\n      <div class="mr-nav-divider" aria-hidden="true"></div>\n      <a href="/methodik">Methodik</a>\n    \2',
            html
        )
        notes.append("Methodik-Link in Nav ergänzt")

    # --- 7. Mobile-Nav: aria-label aufräumen (Menü → Menü öffnen) -----------
    html = html.replace('aria-label="Menü"', 'aria-label="Menü öffnen" type="button"')

    # --- Schreiben ---------------------------------------------------------
    if html == original:
        return False, ["Keine Änderungen nötig"]

    path.write_text(html, encoding="utf-8")
    return True, notes


def main():
    print("=" * 70)
    print("Sprint #2: Gold-Städte Transformation")
    print("=" * 70)

    for city in CITIES:
        print(f"\n[{city.upper()}]")
        ok, notes = transform(city)
        status = "✅" if ok else "⚠"
        for n in notes:
            print(f"  {status} {n}")


if __name__ == "__main__":
    main()
