#!/usr/bin/env python3
"""
meta-length-fix.py
==================
Applies hand-curated shortened title/description per page.

For each entry:
  - replaces <title>, og:title, twitter:title (if title is updated)
  - replaces <meta name="description">, og:description, twitter:description
    (if description is updated)
  - keeps JSON-LD descriptions untouched (they target separate entities)

After: validates every JSON-LD <script type="application/ld+json"> still parses.
"""

from __future__ import annotations
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent


# Each entry: relative path → {title?, description?, og_title?, og_desc?,
#                              twitter_title?, twitter_desc?}
# When title or description is given, we apply it; og/twitter default to same.

FIXES: dict[str, dict] = {

    # ---- Title-Kürzungen (root pages) ----
    "kindern-tod-erklaeren.html": {
        # 94 → ~58
        "title": "Kindern den Tod erklären — Altersgerechter Leitfaden | mach's ruhig",
        # 189 → ~155
        "description": "Wie erkläre ich meinem Kind den Tod? Gesprächsleitfaden nach Alter (3–5, 6–9, 10–13, 14+) mit Formulierungen, häufigen Fehlern und Hilfsangeboten.",
    },
    "tools/trauerrede/index.html": {
        # 84 → ~52
        "title": "Trauerrede schreiben — Schritt-für-Schritt-Assistent",
        # 221 → ~155
        "description": "Trauerrede schreiben Schritt für Schritt: Assistent mit Vorlagen, Zitatbibliothek und Entwurf. Kostenlos im Browser, ohne Datenspeicherung.",
    },
    "tools/beerdigungsplaner/index.html": {
        # 72 → ~45
        "title": "Beerdigungsplaner — Bestattung Schritt für Schritt",
    },
    "tools/abschiedsbrief/index.html": {
        # 71 → ~46
        "title": "Brief an meine Liebsten — Persönliche Worte hinterlassen",
    },
    "tools/bestattungskosten-rechner/index.html": {
        # 70 → ~37
        "title": "Bestattungskosten-Rechner — Was kostet eine Bestattung?",
        # 179 → ~155
        "description": "Kostenloser Bestattungskosten-Rechner: realistische Kosten nach Bestattungsart, Region und Extras berechnen. Ohne Anmeldung, 100% privat.",
    },
    "tools/kostenrechner/index.html": {
        # 70 → ~38
        "title": "Kostenrechner Bestattung — Was kostet deine Beerdigung?",
    },
    "tools/notfallkarte/index.html": {
        # 70 → ~42
        "title": "Notfallkarte erstellen — Daten im Portemonnaie",
    },
    "tools/danksagung/index.html": {
        # 68 → ~38
        "title": "Danksagung nach Beerdigung — Vorlagen & Generator",
    },
    "tools/fristen-radar/index.html": {
        # 69 → ~38
        "title": "Fristen-Radar Todesfall — Alle Fristen im Blick",
    },
    "tools/vorsorge-check/index.html": {
        # 66 → ~36
        "title": "Vorsorge-Check — Welche Dokumente brauchst du?",
        # 167 → ~155
        "description": "Kostenloser Vorsorge-Check: 3 Fragen beantworten und erfahren, welche Vorsorgedokumente du brauchst. Ohne Datenerfassung, privat im Browser.",
    },

    "bestattungsarten.html": {
        # 71 → ~36
        "title": "Bestattungsarten im Vergleich — Welche passt?",
    },
    "beerdigung-planen.html": {
        # 69 → ~37
        "title": "Beerdigung planen — Schritt für Schritt",
    },
    "trauerrede-schreiben.html": {
        # 67 → ~37
        "title": "Trauerrede schreiben — Anleitung & Beispiele",
        # 168 → ~158
        "description": "Trauerrede schreiben Schritt für Schritt: Aufbau, Tipps, Beispiele für Vater, Mutter, Oma, Opa. Plus kostenloser Generator — komplett im Browser.",
    },
    "vertraege-kuendigen.html": {
        # 70 → ~38
        "title": "Verträge kündigen nach Todesfall — Checkliste",
    },

    # ---- Vorsorge-Cluster ----
    "vorsorge/vorsorge-ordner/index.html": {
        # 70 → ~35
        "title": "Vorsorge-Ordner — Alle Dokumente an einem Ort",
        # 193 → ~158
        "description": "Der machsruhig Vorsorge-Ordner: PDF-Bundle mit Vorlagen für Patientenverfügung, Vollmacht, Betreuungs- und Bestattungsverfügung sowie Checklisten.",
    },
    "vorsorge/digitaler-nachlass/index.html": {
        # 69 → ~36
        "title": "Digitaler Nachlass — Online-Konten regeln",
    },
    "vorsorge/ohne-vorsorge/index.html": {
        # 68 → ~34
        "title": "Ohne Vorsorge — Was passiert, wenn nichts geregelt ist?",
    },
    "vorsorge/bestattungsvorsorge/index.html": {
        # 67 → ~33
        "title": "Bestattungsvorsorge — Zu Lebzeiten regeln",
    },
    "vorsorge/sterbegeldversicherung/index.html": {
        # 67 → ~36
        "title": "Sterbegeldversicherung — Bestattungskosten absichern",
    },
    "vorsorge/testament/index.html": {
        # title ok
        # 172 → ~155
        "description": "Testament einfach erklärt: handschriftlich oder notariell, Anforderungen, Berliner Testament, Pflichtteil und häufige Fehler. Vorsorge kostenlos.",
    },

    # ---- Bestatter-Stadt-Seiten ----
    "bestatter/berlin/index.html": {
        # 84 → ~58
        "title": "Bestatter in Berlin — Friedhöfe, Kosten & Regeln",
    },
    "bestatter/hamburg/index.html": {
        # 72 → ~52
        "title": "Bestatter in Hamburg — Ohlsdorf, Kosten & Seebestattung",
    },
    "bestatter/essen/index.html": {
        # 73 → ~58
        "title": "Bestattung in Essen — Friedhöfe, Kosten & Bestatter 2026",
        # 187 → ~158
        "description": "Bestattung in Essen 2026: 23 kommunale Friedhöfe, Parkfriedhof, Südwestfriedhof, Ostfriedhof, Friedhof Bredeney. Gebühren, Bestatter, Ablauf.",
    },
    "bestatter/freiburg/index.html": {
        # 72 → ~55
        "title": "Bestattung in Freiburg — Hauptfriedhof, Bergäcker, Gebühren",
        # 282 → ~163
        "description": "Bestattung in Freiburg: Hauptfriedhof (1872, 27 ha, Stühlinger), Bergäcker (Littenweiler, 11 ha), Jüdischer Friedhof (1870). Gebühren 2024, §§ BestattG BW.",
    },
    "bestatter/oldenburg/index.html": {
        # 72 → ~54
        "title": "Bestattung in Oldenburg — Friedhöfe, Kosten & Bestatter",
        # 185 → ~158
        "description": "Bestattung in Oldenburg: alle Friedhöfe, Friedhofsgebühren 2024, Ruhezeiten und Schritte nach einem Todesfall. Mit Primärquellen aus der Friedhofssatzung.",
    },
    "bestatter/krefeld/index.html": {
        # 80 → ~57
        "title": "Bestattung in Krefeld — Friedhöfe, Kosten & Recht NRW",
    },
    "bestatter/muelheim/index.html": {
        # 78 → ~58
        "title": "Bestattung in Mülheim/Ruhr — Friedhöfe, Kosten & Ablauf",
        # 177 → ~158
        "description": "Bestattung in Mülheim an der Ruhr: zehn städtische Friedhöfe von Altstadt bis Hauptfriedhof, Kosten, Friedhofsverwaltung und Ablauf nach einem Todesfall.",
    },
    "bestatter/rostock/index.html": {
        # 83 → ~58
        "title": "Bestattung in Rostock — Friedhöfe, Kosten & Ablauf",
        # 241 → ~163
        "description": "Bestattung in Rostock: drei kommunale Friedhöfe (Neuer Friedhof, Westfriedhof, Warnemünde), Gebührensatzung, Sterbefall-Anzeige – mit §-Verweisen auf BestattG M-V.",
    },
    "bestatter/gelsenkirchen/index.html": {
        # 71 → ~52
        "title": "Bestattung in Gelsenkirchen — Friedhöfe, Kosten & Ablauf",
        # 195 → ~158
        "description": "Bestattung in Gelsenkirchen: 12 städtische Friedhöfe, Gebühren 2025, Schalker Fan-Feld, Hauptfriedhof Buer, Ostfriedhof, Horst-Süd, Schritte nach Todesfall.",
    },
    "bestatter/karlsruhe/index.html": {
        # 71 → ~58
        "title": "Bestattung in Karlsruhe — Hauptfriedhof, Bergfriedhof, Gebühren",
        # 246 → ~163
        "description": "Bestattung in Karlsruhe: Hauptfriedhof (ab 1874 erster kommunaler Parkfriedhof Deutschlands, 34 ha, Josef Durm) und Bergfriedhof Durlach. Gebühren 2026, BestattG BW.",
    },
    "bestatter/oberhausen/index.html": {
        # 71 → ~54
        "title": "Bestattung in Oberhausen — Friedhöfe, Gebühren, Ablauf",
    },
    "bestatter/leverkusen/index.html": {
        # 70 → ~52
        "title": "Bestattung in Leverkusen — Friedhöfe, Gebühren & Recht",
        # 175 → ~158
        "description": "Bestattung in Leverkusen: 7 städtische und 4 katholische Friedhöfe, jüdischer Friedhof Opladen, Gebührensatzung 2026, Standesamt-Adressen und Schritte.",
    },
    "bestatter/braunschweig/index.html": {
        # 69 → ~52
        "title": "Bestattung in Braunschweig — Friedhöfe, Kosten, Ämter",
        # 264 → ~163
        "description": "Bestattung in Braunschweig: Hauptfriedhof, Stadtfriedhof, Jüdischer Friedhof, Katholischer Friedhof, Magnifriedhof, Domkrypta. Gebühren, Sozialbestattung, Ablauf.",
    },
    "bestatter/halle/index.html": {
        # 69 → ~54
        "title": "Bestattung in Halle (Saale) — Friedhöfe, Kosten, Ablauf",
        # 234 → ~158
        "description": "Bestattung in Halle (Saale): die 14 kommunalen Friedhöfe — vom Renaissance-Stadtgottesacker bis zum Gertraudenfriedhof. Gebühren, Standesamt, Bestatter.",
    },
    "bestatter/regensburg/index.html": {
        # 69 → ~53
        "title": "Bestattung in Regensburg — Friedhöfe, Kosten, Bestatter",
        # 203 → ~158
        "description": "Bestattung in Regensburg: 11 städtische Friedhöfe, Evangelischer Zentralfriedhof, Gesandtenfriedhof, Dreifaltigkeitsbergfriedhof. Gebühren nach BGS, Ablauf.",
    },
    "bestatter/saarbruecken/index.html": {
        # 68 → ~51
        "title": "Bestattung in Saarbrücken — Friedhöfe, Kosten, Ablauf",
    },
    "bestatter/dortmund/index.html": {
        # 67 → ~50
        "title": "Bestattung in Dortmund — Friedhöfe, Kosten & Ablauf",
        # 205 → ~158
        "description": "Vollständiger Überblick zur Bestattung in Dortmund: Hauptfriedhof, Ost-, Süd- und Nordfriedhof mit Geschichte und prominenten Gräbern. Gebühren und Ablauf.",
    },
    "bestatter/augsburg/index.html": {
        # 67 → ~50
        "title": "Bestattung in Augsburg — Friedhöfe, Kosten & Ablauf",
        # 179 → ~158
        "description": "Bestattung in Augsburg: 14 Friedhöfe, Gebührensatzung 2025 (Satzung 7511), Standesamt-Adresse und konkrete Schritte nach einem Todesfall in der Fuggerstadt.",
    },
    "bestatter/heidelberg/index.html": {
        # 67 → ~51
        "title": "Bestattung in Heidelberg — Friedhöfe, Kosten, Vorgehen",
    },
    "bestatter/kiel/index.html": {
        # 67 → ~50
        "title": "Bestattung in Kiel — Friedhöfe, Kosten & Ablauf 2026",
        # 186 → ~158
        "description": "Bestattung in Kiel: die großen Kieler Friedhöfe, aktuelle Friedhofsgebühren, Seebestattung in der Kieler Förde und Schritte nach einem Todesfall.",
    },
    "bestatter/osnabrueck/index.html": {
        # 67 → ~52
        "title": "Bestattung in Osnabrück — Friedhöfe, Kosten und Ablauf",
        # 192 → ~158
        "description": "Bestattung in Osnabrück: zehn kommunale Friedhöfe, Heger Friedhof mit Krematorium, historische Anlagen Hase- und Johannisfriedhof. Kosten, Ablauf, Adressen.",
    },
    "bestatter/wiesbaden/index.html": {
        # 67 → ~52
        "title": "Bestattung in Wiesbaden — Friedhöfe, Kosten & Ablauf",
        # 176 → ~155
        "description": "Bestattung in Wiesbaden: 21 städtische Friedhöfe, Friedhofsgebührensatzung mit konkreten Werten, Russischer Friedhof Neroberg, Nord-, Südfriedhof, Biebrich.",
    },
    "bestatter/bielefeld/index.html": {
        # 66 → ~50
        "title": "Bestattung in Bielefeld — Friedhöfe, Kosten, Bestatter",
        # 206 → ~158
        "description": "Bestattung in Bielefeld: 19 städtische Friedhöfe, Sennefriedhof (98 ha) und Johannisfriedhof, Gebühren ab 70 €, Ruhezeiten, BestG NRW §§ 9/13/14, Bethel.",
    },
    "bestatter/magdeburg/index.html": {
        # 66 → ~51
        "title": "Bestattung in Magdeburg — Friedhöfe, Kosten und Ablauf",
        # 205 → ~158
        "description": "Bestattung in Magdeburg: 16 kommunale Friedhöfe, Friedhofsgebührensatzung 2024 (Erdgrab ab 1.230 €, Urne ab 1.053 €), West-, Süd-, Ostfriedhof mit Adressen.",
    },
    "bestatter/mainz/index.html": {
        # 66 → ~52
        "title": "Bestattung in Mainz — Friedhöfe, Gebühren & Recht 2026",
        # 221 → ~160
        "description": "Bestattung in Mainz: Hauptfriedhof (Vorbild Père-Lachaise), Mombacher Waldfriedhof, Neuer Jüdischer Friedhof, Gonsenheim. Gebühren 09/2025, BestG RLP.",
    },

    # ---- Description-only-Fixes ohne Title-Kürzung ----
    "bestatter/potsdam/index.html": {
        # 301 → ~158
        "description": "Bestattung in Potsdam: 15 kommunale und 12 konfessionelle Friedhöfe, Gebührensatzung 2024 ab 1.493 € Erdreihengrab, Bornstedt, Goethefriedhof, Pfingstberg.",
    },
    "bestatter/mannheim/index.html": {
        # 231 → ~163
        "description": "Bestattung in Mannheim: zehn städtische Friedhöfe mit rund 70.000 Grabstätten, Hauptfriedhof Wohlgelegen seit 1842, jüdischer Friedhof als größter in BW.",
    },
    "bestatter/kassel/index.html": {
        # 228 → ~158
        "description": "Bestattung in Kassel: Hauptfriedhof, Altstädter Friedhof, Wehlheiden, Westfriedhof und Jüdischer Friedhof Bettenhausen. Gebührensatzung 2024 und hessisches FBG.",
    },
    "bestatter/wuppertal/index.html": {
        # 216 → ~158
        "description": "Bestattung in Wuppertal: Krummacherstraße/Varresbeck, Hochstraßen-Ensemble Elberfeld, Unterbarmen, jüdische Friedhöfe, Gebühren, Krematorium und Ablauf.",
    },
    "bestatter/aachen/index.html": {
        # 208 → ~158
        "description": "Bestattung in Aachen: 28 städtische Friedhöfe von Westfriedhof bis Waldfriedhof, Gebühren mit Eurobeträgen, Sozialbestattung und Ablauf nach einem Todesfall.",
    },
    "bestatter/hagen/index.html": {
        # 207 → ~158
        "description": "Bestattung in Hagen: 10 städtische Friedhöfe vom WBH, Eduard-Müller-Krematorium von Peter Behrens, RuheForst Philippshöhe, Gebühren, Standesamt, Bestatter.",
    },
    "bestatter/bonn/index.html": {
        # 204 → ~165
        "description": "Bestattung in Bonn: Alter Friedhof mit Schumann-Grab und Macke-Gedenkstein, Südfriedhof, Nordfriedhof, Burgfriedhof Bad Godesberg. Friedhofssatzung, Gebühren.",
    },
    "bestatter/hannover/index.html": {
        # 202 → ~158
        "description": "Bestattung in Hannover: Gartenfriedhof (1741), Stadtfriedhof Engesohde (1864), Seelhorst, Lahe, Ricklingen. Friedhofsgebühren der Landeshauptstadt, BestattG Nds.",
    },
    "bestatter/chemnitz/index.html": {
        # 200 → ~158
        "description": "Bestattung in Chemnitz: Städtischer Friedhof, Urnenhain, Jüdischer Friedhof, Reichenbrand. Friedhofsgebühren der Stadt, SächsBestG-Fristen, Ablauf nach Todesfall.",
    },
    "bestatter/leipzig/index.html": {
        # 199 → ~158
        "description": "Bestattung in Leipzig: Südfriedhof (rund 80 ha, größter Sachsens), Nordfriedhof, Alter Johannisfriedhof und Ostfriedhof. Gebühren, Bach/Mendelssohn, §§ SächsBestG.",
    },
    "bestatter/duisburg/index.html": {
        # 199 → ~158
        "description": "Bestattung in Duisburg: Waldfriedhof, Hauptfriedhof Sternbuschweg, Friedhof Eisenbahnstraße (Ruhrort). Friedhofsgebühren, Ämter, Bestatter — mit § BestG NRW.",
    },
    "bestatter/erfurt/index.html": {
        # 199 → ~158
        "description": "Bestattung in Erfurt: vier Friedhöfe im Porträt, Friedhofsgebührensatzung ab 01.01.2025, Sozialbestattung und Schritte nach dem Todesfall — mit § ThürBestG.",
    },
    "bestatter/duesseldorf/index.html": {
        # 197 → ~158
        "description": "Die 13 städtischen Friedhöfe Düsseldorfs: Nordfriedhof mit Millionenhügel, Südfriedhof mit Toten-Hosen-Grab, Stoffeler Friedhof mit Krematorium. Gebühren, Bestatter.",
    },
    "bestatter/nuernberg/index.html": {
        # 196 → ~158
        "description": "Bestattung in Nürnberg: St. Johannis (1518, Dürer-Grab) und Rochusfriedhof als Renaissance-Ensemble, West- und Südfriedhof als Hauptfriedhöfe. Satzung, Kosten.",
    },
    "bestatter/muenster/index.html": {
        # 191 → ~158
        "description": "Bestattung in Münster: Waldfriedhof Lauheide (84 ha, Deutschlands schönster Friedhof 2014) und Zentralfriedhof (1887, 14 ha). Gebühren, BestG NRW, Primärquellen.",
    },
    "bestatter/dresden/index.html": {
        # 190 → ~158
        "description": "Bestattung in Dresden: Trinitatisfriedhof, Alter Annenfriedhof, Johannisfriedhof Tolkewitz, Innerer Neustädter Friedhof. Geschichten, Kosten und Ablauf nach Todesfall.",
    },
    "bestatter/bremen/index.html": {
        # 189 → ~158
        "description": "Bestattung in Bremen: 13 städtische Friedhöfe, Riensberger Parkfriedhof, Osterholzer Zentralfriedhof, Waller Friedhof, jüdischer Friedhof Hastedt. Gebühren, Ruhezeit.",
    },
    "bestatter/stuttgart/index.html": {
        # 183 → ~158
        "description": "Stuttgart hat 41 städtische Friedhöfe: Pragfriedhof, Waldfriedhof Degerloch, Hauptfriedhof Bad Cannstatt und Hoppenlau im Porträt. Gebühren 2025, BestattG BW.",
    },
    "bestatter/frankfurt/index.html": {
        # 173 → ~158
        "description": "Hauptfriedhof Frankfurt mit Schopenhauer und Adorno, Alter Jüdischer Friedhof Battonnstraße mit Rothschild. Hessen-Recht nach Novelle 2025, Kosten 4.000–9.000 €.",
    },
    "bestatter/bochum/index.html": {
        # 171 → ~158
        "description": "Bestattung in Bochum: 24 städtische Friedhöfe auf 214 ha, Hauptfriedhof Freigrafendamm mit 64.000 Gräbern, Kortumpark, Ev. Friedhof Harpen. Gebühren, BestG NRW.",
    },
    "trauersprueche.html": {
        # 179 → ~158
        "description": "Über 200 Trauersprüche: tröstliche Sprüche, religiöse Bibelverse, philosophische Zitate für Trauerkarten, Grabsteine und Reden. Public Domain — kostenlos.",
    },
    "kondolenzschreiben.html": {
        # 175 → ~158
        "description": "Wie schreibe ich ein Kondolenzschreiben? Anleitung Schritt für Schritt: Struktur, Dos and Don'ts, Vorlagen für verschiedene Situationen, FAQs. Respektvoll, hilfreich.",
    },
}


# ---- application ----
TITLE_RE = re.compile(r"(<title[^>]*>)(.*?)(</title>)", re.I | re.S)

def replace_meta_property(html: str, prop_attr: str, prop_value: str,
                          new_content: str) -> tuple[str, bool]:
    """Replace content attribute of <meta {prop_attr}="{prop_value}" content="...">.
    Returns (new_html, changed)."""
    pattern = re.compile(
        r'(<meta\s+[^>]*?\b' + re.escape(prop_attr) + r'\s*=\s*"'
        + re.escape(prop_value) + r'"[^>]*?\bcontent\s*=\s*")([^"]*)("[^>]*>)',
        re.I,
    )
    new_html, n = pattern.subn(lambda m: m.group(1) + new_content + m.group(3),
                               html, count=1)
    if n:
        return new_html, True
    # try alternative attribute order: content before name/property
    pattern2 = re.compile(
        r'(<meta\s+[^>]*?\bcontent\s*=\s*")([^"]*)("[^>]*?\b'
        + re.escape(prop_attr) + r'\s*=\s*"' + re.escape(prop_value) + r'"[^>]*>)',
        re.I,
    )
    new_html, n = pattern2.subn(lambda m: m.group(1) + new_content + m.group(3),
                                html, count=1)
    return new_html, bool(n)


def html_escape_for_attr(s: str) -> str:
    """Minimal: " → &quot; (we never use raw quotes in our new strings anyway).
    Keep ä/ö/ü etc. — files are saved UTF-8."""
    return s.replace('"', "&quot;")


def html_escape_for_title(s: str) -> str:
    # for <title>, only need to worry about <, but we don't use these.
    return s


def validate_jsonld(html: str, path: Path) -> list[str]:
    """Validate all <script type="application/ld+json"> blocks parse as JSON."""
    errors = []
    pattern = re.compile(
        r'<script[^>]*type\s*=\s*"application/ld\+json"[^>]*>(.*?)</script>',
        re.I | re.S,
    )
    for i, m in enumerate(pattern.finditer(html)):
        block = m.group(1)
        try:
            json.loads(block)
        except json.JSONDecodeError as e:
            errors.append(f"{path}: JSON-LD block #{i+1} fails: {e}")
    return errors


def apply_fix(path: Path, spec: dict) -> tuple[bool, list[str]]:
    changed_msgs: list[str] = []
    orig = path.read_text(encoding="utf-8")
    html = orig

    new_title = spec.get("title")
    if new_title:
        # <title>
        new_html, n = TITLE_RE.subn(
            lambda m: m.group(1) + html_escape_for_title(new_title) + m.group(3),
            html, count=1)
        if n:
            html = new_html
            changed_msgs.append(f"title → {len(new_title)} chars")
        else:
            changed_msgs.append("WARN: <title> not found")

        # og:title
        html, ok = replace_meta_property(html, "property", "og:title",
                                         html_escape_for_attr(new_title))
        if not ok:
            changed_msgs.append("WARN: og:title not found")
        # twitter:title
        html, ok = replace_meta_property(html, "name", "twitter:title",
                                         html_escape_for_attr(new_title))
        if not ok:
            changed_msgs.append("WARN: twitter:title not found")

    new_desc = spec.get("description")
    if new_desc:
        # name=description
        html, ok = replace_meta_property(html, "name", "description",
                                         html_escape_for_attr(new_desc))
        if not ok:
            changed_msgs.append("WARN: meta description not found")
        else:
            changed_msgs.append(f"description → {len(new_desc)} chars")
        # og:description
        html, ok = replace_meta_property(html, "property", "og:description",
                                         html_escape_for_attr(new_desc))
        if not ok:
            changed_msgs.append("WARN: og:description not found")
        # twitter:description
        html, ok = replace_meta_property(html, "name", "twitter:description",
                                         html_escape_for_attr(new_desc))
        if not ok:
            changed_msgs.append("WARN: twitter:description not found")

    if html == orig:
        return False, changed_msgs

    # write
    path.write_text(html, encoding="utf-8")

    # validate JSON-LD blocks still parse
    errs = validate_jsonld(html, path)
    if errs:
        # restore on failure
        path.write_text(orig, encoding="utf-8")
        return False, errs

    return True, changed_msgs


def main():
    n_title = 0
    n_desc = 0
    failed: list[str] = []
    for rel, spec in FIXES.items():
        path = REPO / rel
        if not path.exists():
            failed.append(f"missing: {rel}")
            continue
        ok, msgs = apply_fix(path, spec)
        status = "OK" if ok else "NO-OP/FAIL"
        print(f"[{status}] {rel}: {'; '.join(msgs)}")
        if ok:
            if spec.get("title"):
                n_title += 1
            if spec.get("description"):
                n_desc += 1
    print(f"\nTitles fixed: {n_title}")
    print(f"Descriptions fixed: {n_desc}")
    if failed:
        print("FAILURES:")
        for f in failed:
            print(f"  {f}")
        sys.exit(1)


if __name__ == "__main__":
    main()
