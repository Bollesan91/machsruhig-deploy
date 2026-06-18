# -*- coding: utf-8 -*-
"""Wendet handgefertigte, gekuerzte <title> (<=60 Zeichen inkl. Marke) an.
/bestattungskosten-nach-bundesland ist AUSGENOMMEN (Presse-Neutralitaet)."""
import re
from pathlib import Path

ROOT = Path(".")

TITLES = {
 "kindern-tod-erklaeren.html": "Kindern den Tod erklären — altersgerecht | mach's ruhig",
 "tools/trauerrede/index.html": "Trauerrede-Generator — Schritt für Schritt | mach's ruhig",
 "notfallkarte.html": "Notfallkarte fürs Portemonnaie | mach's ruhig",
 "was-tun-nach-todesfall.html": "Was tun nach einem Todesfall? Checkliste | mach's ruhig",
 "danksagung-nach-beerdigung.html": "Danksagung nach Beerdigung — Vorlagen | mach's ruhig",
 "abschiedsbrief-schreiben.html": "Abschiedsbrief schreiben — Anleitung | mach's ruhig",
 "vorsorge/index.html": "Vorsorge: Verfügung, Vollmacht & Testament | mach's ruhig",
 "tools/beerdigungsplaner/index.html": "Beerdigungsplaner — Schritt für Schritt | mach's ruhig",
 "sozialbestattung.html": "Sozialbestattung: Wann das Sozialamt zahlt | mach's ruhig",
 "index.html": "Bestattung, Vorsorge & Trauer-Hilfe | mach's ruhig",
 "vorsorge-allein-leben.html": "Vorsorge ohne Familie: für Alleinstehende | mach's ruhig",
 "tools/abschiedsbrief/index.html": "Brief an meine Liebsten schreiben | mach's ruhig",
 "bestattungsarten.html": "Bestattungsarten im Vergleich | mach's ruhig",
 "vertraege-kuendigen.html": "Verträge kündigen nach Todesfall | mach's ruhig",
 "tools/notfallkarte/index.html": "Notfallkarte erstellen | mach's ruhig",
 "tools/bestattungskosten-rechner/index.html": "Bestattungskosten-Rechner | mach's ruhig",
 "vorsorge/digitaler-nachlass/index.html": "Digitaler Nachlass regeln | mach's ruhig",
 "tools/fristen-radar/index.html": "Fristen-Radar Todesfall | mach's ruhig",
 "beerdigung-planen.html": "Beerdigung planen — Schritt für Schritt | mach's ruhig",
 "vorsorge/ohne-vorsorge/index.html": "Ohne Vorsorge: Was dann passiert | mach's ruhig",
 "tools/danksagung/index.html": "Danksagung-Generator & Vorlagen | mach's ruhig",
 "vorsorge/sterbegeldversicherung/index.html": "Sterbegeldversicherung — lohnt sie sich? | mach's ruhig",
 "vorsorge/bestattungsvorsorge/index.html": "Bestattungsvorsorge zu Lebzeiten | mach's ruhig",
 "trauerrede-schreiben.html": "Trauerrede schreiben — Aufbau & Beispiele | mach's ruhig",
 "fristen-nach-todesfall.html": "Fristen nach Todesfall — Übersicht | mach's ruhig",
 "feuerbestattung-angebot-pruefen.html": "Feuerbestattung-Angebot prüfen | machsruhig",
 "tools/angebotspruefer/index.html": "Bestatter-Angebot prüfen — Ampel-Check | mach's ruhig",
 "bestatter-rechnung-pruefen.html": "Bestatter-Rechnung prüfen | machsruhig",
 "bestattung-in/mecklenburg-vorpommern/index.html": "Bestattung in Mecklenburg-Vorpommern | machsruhig",
 "erdbestattung-angebot-pruefen.html": "Erdbestattung-Angebot prüfen | machsruhig",
 "bestattung-in/index.html": "Bestattungsrecht der 16 Bundesländer | machsruhig",
 "bestatter-angebot-vergleichen.html": "Bestatter-Angebote vergleichen | machsruhig",
 "bestattung-in/sachsen/index.html": "Bestattung in Sachsen: Recht & Kosten | machsruhig",
 "bestattung-in/rheinland-pfalz/index.html": "Bestattung in Rheinland-Pfalz: Recht | machsruhig",
 "bestatter-angebot-pruefen.html": "Bestatter-Angebot prüfen — plausibel? | machsruhig",
}

changed, warn, skip = 0, [], []
for rel, new in TITLES.items():
    f = ROOT / rel
    if not f.exists():
        skip.append(rel); continue
    if len(new) > 60:
        warn.append((rel, len(new)))
    t = f.read_text(encoding="utf-8")
    nt, n = re.subn(r"<title>.*?</title>", "<title>" + new + "</title>", t, count=1, flags=re.DOTALL)
    if n == 1 and nt != t:
        f.write_text(nt, encoding="utf-8"); changed += 1
    elif n == 0:
        skip.append(rel + " (kein <title>)")

print(f"Titles gesetzt: {changed} | übersprungen: {len(skip)} | >60 Warnungen: {len(warn)}")
for r, l in warn: print(f"  WARN >60 ({l}): {r}")
for s in skip: print(f"  SKIP: {s}")
# Längen-Report
print("\nLängen je Title (Kontrolle):")
for rel, new in sorted(TITLES.items(), key=lambda x: -len(x[1])):
    print(f"  {len(new):>2}  {new}")
