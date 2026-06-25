#!/usr/bin/env python3
# Muslim-Grabfeld-Pass Batch 3 (final 13) — insert verified islamic-grave-field
# bullet before the first </ul> (Traeger-Arten list) of each city overview.
# All facts primary-verified 2026-06-25 (city/press/Friedhofsverwaltung + eslam).
# Sachsen-Sargpflicht-Klausel bewusst gehedged ("grundsaetzlich weiterhin"):
# Stand Mai 2023 galt Sargpflicht, Ausnahmen nur geplant -> Inkrafttreten 2026 unbestaetigt.
import os

ROOT = r"C:\Users\Bolle\AppData\Local\Temp\machsruhig-deploy\friedhoefe"

BULLETS = {
    "duisburg": '<li><strong>Islamisches Grabfeld:</strong> auf dem (st&auml;dtischen) Waldfriedhof gibt es seit den 1990er-Jahren ein islamisches Grabfeld; 2021 wurde ein weiteres er&ouml;ffnet &mdash; Gr&auml;ber Richtung Mekka, Bestattung in reiner Erde.</li>',
    "gelsenkirchen": '<li><strong>Islamisches Grabfeld:</strong> auf dem Friedhof Hassel besteht (von Gelsendienste in Abstimmung mit der DİTİB-Gemeinde angelegt) ein muslimisches Grabfeld mit Gr&auml;bern Richtung Mekka; es wurde zuletzt erweitert.</li>',
    "halle": '<li><strong>Islamisches Grabfeld:</strong> auf dem (st&auml;dtischen) Gertraudenfriedhof besteht in Abteilung 33 ein muslimisches Grabfeld (erste Bestattung 1997) mit Gr&auml;bern Richtung Mekka.</li>',
    "hannover": '<li><strong>Islamisches Grabfeld:</strong> auf dem Stadtfriedhof St&ouml;cken besteht seit 1989 das (einzige) muslimische Gr&auml;berfeld Hannovers &mdash; Kopf der Verstorbenen Richtung Mekka, mit Waschraum und sargloser Tuchbestattung.</li>',
    "karlsruhe": '<li><strong>Islamisches Grabfeld:</strong> auf dem Hauptfriedhof gibt es seit 1984 ein muslimisches Grabfeld (Grabfeld 40) mit Ausrichtung Richtung Mekka; R&auml;ume f&uuml;r rituelle Waschung und Totengebet sind vorhanden.</li>',
    "kiel": '<li><strong>Islamisches Grabfeld:</strong> auf dem Ostfriedhof wurde 2000 ein islamisches Grabfeld eingeweiht (Gr&auml;ber Richtung Mekka); wegen gro&szlig;er Nachfrage kam 2015 ein zweites hinzu.</li>',
    "leipzig": '<li><strong>Islamisches Grabfeld:</strong> auf dem Ostfriedhof besteht seit 1997 das (einzige) muslimische Grabfeld Leipzigs mit Gr&auml;bern Richtung Mekka. In Sachsen gilt allerdings grunds&auml;tzlich weiterhin Sargpflicht (sarglose Bestattung nur eingeschr&auml;nkt).</li>',
    "mannheim": '<li><strong>Islamisches Grabfeld:</strong> auf dem Hauptfriedhof besteht seit den 1980er-Jahren ein islamisches Grabfeld (2014 neu eingeweiht/erweitert, mit Qibla-Stein) mit Gr&auml;bern Richtung Mekka; Baden-W&uuml;rttemberg erlaubt seit 2014 die sarglose Bestattung im Leichentuch.</li>',
    "moenchengladbach": '<li><strong>Islamisches Grabfeld:</strong> auf dem Hauptfriedhof besteht seit 2000 ein muslimisches Grabfeld; 2020 kam ein neues Feld f&uuml;r rund 400 Gr&auml;ber hinzu &mdash; Gr&auml;ber Richtung Mekka.</li>',
    "muenster": '<li><strong>Islamisches Grabfeld:</strong> auf dem (st&auml;dtischen) Waldfriedhof Lauheide besteht ein islamisches Grabfeld mit Gr&auml;bern Richtung Mekka.</li>',
    "nuernberg": '<li><strong>Islamisches Grabfeld:</strong> auf dem S&uuml;dfriedhof besteht ein eigens gestaltetes muslimisches Grabfeld (&bdquo;Muslimfeld&ldquo;) mit Gr&auml;bern Richtung Mekka; seit 2023 ist dort auch die sarglose Tuchbestattung m&ouml;glich.</li>',
    "wiesbaden": '<li><strong>Islamisches Grabfeld:</strong> auf dem S&uuml;dfriedhof sind seit 1987 muslimische Bestattungen m&ouml;glich (mehrere Grabfelder, Gr&auml;ber Richtung Mekka); sarglose Bestattung ist seit 2014 erlaubt, 2026 kam ein neues Grabfeld mit 309 Grabstellen hinzu.</li>',
    "wuppertal": '<li><strong>Islamisches Grabfeld:</strong> auf dem (evangelischen) Friedhof Norrenberg besteht ein muslimisches Gr&auml;berfeld (Platz f&uuml;r bis zu rund 900 Gr&auml;ber) mit Gr&auml;bern Richtung Mekka; die Friedhofsordnung erlaubt dort die sarglose Tuchbestattung. In Wuppertal entsteht zudem Deutschlands erster Friedhof in muslimischer Tr&auml;gerschaft.</li>',
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
    window = html[max(0, idx-1400):idx]
    assert "<li>" in window and any(k in window for k in ("Konfessionelle", "konfessionell", "Kommunale", "kommunal", "st&auml;dtisch", "Jüdische", "J&uuml;dische")), f"{city}: first </ul> not Traeger list"
    new_html = html[:idx] + "      " + bullet + "\n    " + html[idx:]
    results.append((city, path, new_html))

for city, path, new_html in results:
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"OK  {city}")
print(f"\n{len(results)} files updated.")
