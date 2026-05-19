#!/usr/bin/env python3
"""Build 4 dispatch JS files for Batch 2: Bochum/Heidelberg/Mannheim (Sozial) + Hamburg (Akut+Sozial)."""
import sys, os, json
sys.stdout.reconfigure(encoding='utf-8')

os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

with open('_dev/audit/helper-v3-installer.js', 'r', encoding='utf-8') as f:
    helper = f.read()
# Extract only the IIFE line (line 4)
helper_iife = [l for l in helper.split('\n') if l.startswith('(function()')][0]

cities = [
    {
        'label': 'bochum-sozial-plan',
        'tabId': 1532775467,
        'prompt': """Du bist Strukturberater fuer eine Stadt-Page von machsruhig.de.

Stadt: Bochum

Fetch die Live-Version:
https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/bochum/index.html

Der Page fehlt: SOZIALBESTATTUNG-Modul.

Liefere PRAEZISEN Insert-Plan:
- EXAKTER ANCHOR (1-2 Zeilen aus aktuellem HTML)
- KOMPLETTER HTML-Code des Moduls (h2 + h3 + p tags, Klasse "mr-section")
- LOKALE SPEZIFIKA: Sozialamt Bochum (korrekte Behoerdenbezeichnung Stadt Bochum + Adresse + Telefon + E-Mail wenn moeglich)
- Bundesland NRW: § 8 BestG NRW (Bestattungspflicht-Reihenfolge)
- BSG-Urteil: B 8 SO 20/10 R vom 25.08.2011

Standardstruktur:
1. § 74 SGB XII Voraussetzungen + Bezug auf § 8 BestG NRW
2. Zustaendige Stelle Sozialamt Bochum (Adresse/Tel/Mail)
3. Was uebernommen wird vs. nicht uebernommen
4. Antragszeitpunkt (vor Auftragsvergabe optimal)

Output-Format:
=== MODUL: SOZIALBESTATTUNG ===
ANCHOR: <Zeile>
INSERT-CODE:
<HTML>

Max 500 Woerter. Adressen verifizieren ohne UNSURE."""
    },
    {
        'label': 'heidelberg-sozial-plan',
        'tabId': 1532775468,
        'prompt': """Du bist Strukturberater fuer eine Stadt-Page von machsruhig.de.

Stadt: Heidelberg

Fetch die Live-Version:
https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/heidelberg/index.html

Der Page fehlt: SOZIALBESTATTUNG-Modul.

Liefere PRAEZISEN Insert-Plan:
- EXAKTER ANCHOR (1-2 Zeilen aus aktuellem HTML)
- KOMPLETTER HTML-Code des Moduls (h2 + h3 + p tags)
- LOKALE SPEZIFIKA: Sozialamt Heidelberg / Amt fuer Soziales (korrekte Bezeichnung + Adresse + Telefon + E-Mail wenn moeglich)
- Bundesland Baden-Wuerttemberg: § 31 BestattG BW (Bestattungspflicht-Reihenfolge)
- BSG-Urteil: B 8 SO 20/10 R vom 25.08.2011

Standardstruktur:
1. § 74 SGB XII Voraussetzungen + Bezug auf § 31 BestattG BW
2. Zustaendige Stelle Sozialamt Heidelberg (Adresse/Tel/Mail)
3. Was uebernommen wird vs. nicht uebernommen
4. Antragszeitpunkt

Output-Format:
=== MODUL: SOZIALBESTATTUNG ===
ANCHOR: <Zeile>
INSERT-CODE:
<HTML>

Max 500 Woerter. Adressen verifizieren ohne UNSURE."""
    },
    {
        'label': 'mannheim-sozial-plan',
        'tabId': 1532775469,
        'prompt': """Du bist Strukturberater fuer eine Stadt-Page von machsruhig.de.

Stadt: Mannheim

Fetch die Live-Version:
https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/mannheim/index.html

Der Page fehlt: SOZIALBESTATTUNG-Modul.

Liefere PRAEZISEN Insert-Plan:
- EXAKTER ANCHOR (1-2 Zeilen aus aktuellem HTML)
- KOMPLETTER HTML-Code des Moduls (h2 + h3 + p tags)
- LOKALE SPEZIFIKA: Sozialamt Mannheim / Fachbereich Arbeit und Soziales (korrekte Bezeichnung + Adresse + Telefon + E-Mail wenn moeglich)
- Bundesland Baden-Wuerttemberg: § 31 BestattG BW (Bestattungspflicht-Reihenfolge)
- BSG-Urteil: B 8 SO 20/10 R vom 25.08.2011

Standardstruktur:
1. § 74 SGB XII Voraussetzungen + Bezug auf § 31 BestattG BW
2. Zustaendige Stelle Sozialamt Mannheim (Adresse/Tel/Mail)
3. Was uebernommen wird vs. nicht uebernommen
4. Antragszeitpunkt

Output-Format:
=== MODUL: SOZIALBESTATTUNG ===
ANCHOR: <Zeile>
INSERT-CODE:
<HTML>

Max 500 Woerter. Adressen verifizieren ohne UNSURE."""
    },
    {
        'label': 'hamburg-akut-sozial-plan',
        'tabId': 1532775470,
        'prompt': """Du bist Strukturberater fuer eine Stadt-Page von machsruhig.de.

Stadt: Hamburg (Stadtstaat)

Fetch die Live-Version:
https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/hamburg/index.html

Der Page fehlen ZWEI Module:
A) AKUTBOX: "Was nach einem Todesfall in Hamburg zu tun ist" (6 Schritte)
B) SOZIALBESTATTUNG: § 74 SGB XII

Liefere PRAEZISEN Insert-Plan fuer BEIDE Module:

A) AKUTBOX:
- EXAKTER ANCHOR
- 6 Schritte: Arzt+Totenschein / Bestatter / Standesamt Anzeige / Friedhof+Grab / Bestattung anmelden / Trauerfeier
- LOKAL: Standesamt Hamburg (Eimsbuettel/Mitte/Nord/etc) - welches ist zustaendig? § 28 PStG (3 Werktage)

B) SOZIALBESTATTUNG:
- EXAKTER ANCHOR (separat, anderer Anker als Akutbox)
- HTML-Code (h2 + h3 + p)
- LOKAL: Hamburger Fachamt Grundsicherung und Soziales / bezirkliches Sozialamt
- Bundesland Hamburg: § 19 HmbBestattG (Bestattungspflicht-Reihenfolge)
- BSG-Urteil: B 8 SO 20/10 R vom 25.08.2011

Output-Format:
=== MODUL A: AKUTBOX ===
ANCHOR: <Zeile>
INSERT-CODE:
<HTML>

=== MODUL B: SOZIALBESTATTUNG ===
ANCHOR: <Zeile>
INSERT-CODE:
<HTML>

Max 800 Woerter. Adressen verifizieren ohne UNSURE."""
    },
]

# Write each dispatch file
for c in cities:
    fp = f"_dev/audit/dispatch/dispatch-{c['label'].replace('-plan','')}.js"
    # JS string-escape the prompt
    prompt_js = json.dumps(c['prompt'])
    js = helper_iife + f"\nwindow.__mcp.run({prompt_js}, '{c['label']}')"
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f"{fp}: {len(js)} chars, tabId={c['tabId']}, label={c['label']}")

# Output tab assignment
print('---')
for c in cities:
    print(f"tabId={c['tabId']} -> {c['label']}")
