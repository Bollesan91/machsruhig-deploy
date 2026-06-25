#!/usr/bin/env python3
# Muslim-Grabfeld-Pass Batch 2 — insert verified islamic-grave-field bullet
# before the first </ul> (Traeger-Arten list) of each city overview.
# All facts primary-verified 2026-06-25 (city/press + eslam + fowid/taz for Sachsen).
import os, sys

ROOT = r"C:\Users\Bolle\AppData\Local\Temp\machsruhig-deploy\friedhoefe"

BULLETS = {
    "aachen": '<li><strong>Islamisches Grabfeld:</strong> auf dem st&auml;dtischen Friedhof H&uuml;ls (Aachen-H&uuml;ls) gibt es ein muslimisches Grabfeld mit Gr&auml;bern Richtung Mekka und M&ouml;glichkeit zur rituellen Waschung; sarglose Bestattung im Leichentuch ist in NRW seit 2003 zul&auml;ssig.</li>',
    "augsburg": '<li><strong>Islamisches Grabfeld:</strong> auf dem Neuen Ostfriedhof gibt es ein muslimisches Grabfeld mit Gr&auml;bern Richtung Mekka; die rituelle Totenwaschung ist auf dem Friedhof G&ouml;ggingen m&ouml;glich.</li>',
    "bielefeld": '<li><strong>Islamisches Grabfeld:</strong> auf dem st&auml;dtischen Sennefriedhof bestehen seit 1995 islamische Grabfelder mit Gr&auml;bern Richtung Mekka (eigener Bereich, mit gesondertem Feld f&uuml;r verstorbene Kinder); Waschr&auml;ume in der neuen Friedhofskapelle.</li>',
    "bochum": '<li><strong>Islamisches Grabfeld:</strong> auf dem Hauptfriedhof (Freigrafendamm) besteht seit 1995 ein muslimisches Gr&auml;berfeld; 2025 kam ein neues Feld mit 168 Grabstellen und eigenem Gebetsbereich hinzu &mdash; Gr&auml;ber Richtung Mekka.</li>',
    "bonn": '<li><strong>Islamisches Grabfeld:</strong> auf dem st&auml;dtischen Nordfriedhof besteht seit 1990 ein muslimisches Grabfeld mit Gr&auml;bern Richtung Mekka.</li>',
    "braunschweig": '<li><strong>Islamisches Grabfeld:</strong> auf dem (evangelischen) Hauptfriedhof besteht seit 1994 ein muslimisches Grabfeld (Abteilung 83) mit Gr&auml;bern Richtung Mekka; sarglose Bestattung im Leichentuch ist dort seit 2008 m&ouml;glich.</li>',
    "chemnitz": '<li><strong>Muslimische Bestattung:</strong> Chemnitz hat (Stand 2024) kein eigens eingefriedetes islamisches Grabfeld; Verstorbene werden auf den st&auml;dtischen Friedh&ouml;fen im Rahmen des M&ouml;glichen nach muslimischem Brauch (Ausrichtung Richtung Mekka) bestattet. In Sachsen gilt zudem die Sargpflicht.</li>',
    "dresden": '<li><strong>Islamisches Grabfeld:</strong> auf dem (kommunalen) Heidefriedhof besteht seit 1996 eine muslimische Grabanlage (2012 erweitert); 2024 kam eine zweite Anlage f&uuml;r rund 150 Bestattungen hinzu &mdash; Gr&auml;ber und Aufbahrungstisch Richtung Mekka, mit Waschpl&auml;tzen. In Sachsen gilt allerdings die Sargpflicht.</li>',
}

results = []
for city, bullet in BULLETS.items():
    path = os.path.join(ROOT, city, "index.html")
    assert os.path.isfile(path), f"missing file: {path}"
    with open(path, encoding="utf-8") as f:
        html = f.read()
    assert "Islamisches Grabfeld" not in html and "Muslimische Bestattung:</strong>" not in html, f"{city}: bullet already present"
    idx = html.find("</ul>")
    assert idx != -1, f"{city}: no </ul> found"
    # sanity: the first </ul> must be the Traeger list (preceded by a konfessionell or kommunal <li> nearby)
    window = html[max(0, idx-1200):idx]
    assert "<li>" in window and ("Konfessionelle" in window or "konfessionell" in window or "Kommunale" in window or "kommunal" in window), f"{city}: first </ul> does not look like the Traeger list"
    new_html = html[:idx] + "      " + bullet + "\n    " + html[idx:]
    results.append((city, path, new_html))

# all asserts passed -> single write phase
for city, path, new_html in results:
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"OK  {city}")
print(f"\n{len(results)} files updated.")
