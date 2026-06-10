# -*- coding: utf-8 -*-
# Fix-Skript R2: Helper-V3-Review Runde 2 (2026-06-10)
# Pflicht: Abschiedsbrief-FAQ "Werden meine Worte gespeichert?" — sichtbare FAQ (JS-Array)
#          und JSON-LD FAQPage sagen unqualifiziert "nicht an einen Server gesendet";
#          KI-Ausnahme ergaenzen, beide Stellen wortgleich (Google verlangt Deckungsgleichheit).
# Minor:   Danksagung-Modal Lagehinweis "unten auf der Seite" -> "auf dieser Seite"
#          (Button sitzt oben unter der Ergebnis-Ueberschrift).
# Kein Multi-Line-Regex auf JSON-LD (Projekt-Tabu) — nur exakte Einzeilen-String-Matches.
import io, sys

OLD_FAQ = "Dein Entwurf wird ausschließlich in deinem Browser gespeichert (localStorage) und nicht an einen Server gesendet. Die Seite selbst nutzt anonyme Reichweiten-Statistiken (Umami), die nur den Seitenbesuch erfassen, nicht deinen Brieftext."
NEW_FAQ = "Dein Entwurf wird in deinem Browser gespeichert (localStorage) und nicht automatisch an einen Server gesendet. Einzige Ausnahme: Wenn du die optionale KI-Verfeinerung nutzt, werden deine Texte bei jeder Verfeinerung an Groq Inc. (USA) übermittelt — nur nach deiner Einwilligung. Die Seite selbst nutzt anonyme Reichweiten-Statistiken (Umami), die nur den Seitenbesuch erfassen, nicht deinen Brieftext."

FIXES = [
    # (Datei, alt, neu, erwartete Treffer)
    ("tools/abschiedsbrief/index.html", OLD_FAQ, NEW_FAQ, 2),  # JSON-LD Z.66 + sichtbare FAQ Z.364, wortgleich
    ("tools/danksagung/index.html",
     "im Datenschutz-Hinweis unten auf der Seite.",
     "im Datenschutz-Hinweis auf dieser Seite.", 1),
]

errors = 0
for path, old, new, expected in FIXES:
    with io.open(path, "r", encoding="utf-8") as f:
        content = f.read()
    n = content.count(old)
    if n != expected:
        print(f"FEHLER {path}: {n} Treffer (erwartet {expected}): {old[:70]!r}")
        errors += 1
        continue
    content = content.replace(old, new)
    with io.open(path, "w", encoding="utf-8", newline="") as f:
        f.write(content)
    print(f"OK {path} ({n} Stellen)")

sys.exit(1 if errors else 0)
