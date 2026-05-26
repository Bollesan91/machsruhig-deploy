# Cluster-Pages × Angebotspruefer v2.4 Konsistenz-Sweep
# Helper-V3 Outcome-Validity-Audit (Tab 1532777190) ergab 0 PASS / 3 critical / 4 medium / 2 low.
# Dieser Sweep konsolidiert die 8 Cluster-Pages mit dem v2.4-Tool-Wording.

import os, re, sys, io

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILES = [
    "bestatter-angebot-pruefen.html",
    "bestatter-angebot-vergleichen.html",
    "bestattungskosten-versteckte-kosten.html",
    "was-muss-im-kostenvoranschlag-stehen.html",
    "bestatter-rechnung-pruefen.html",
    "erdbestattung-angebot-pruefen.html",
    "feuerbestattung-angebot-pruefen.html",
    "seebestattung-angebot-pruefen.html",
]

# Identical-pattern replacements (ALL-8)
ALL_8 = [
    # Line 85 ish: "Liste der vermissten Posten" -> "Liste der Klärungspunkte"
    (
        "Liste der vermissten Posten · 10 Fragen für deinen Bestatter",
        "Liste der Klärungspunkte · Fragen für deinen Bestatter",
    ),
    # Line 98: Lockangebot keyfact
    (
        "<li>Lockangebote unter 50 % des typischen Rahmens sollten dich aufhorchen lassen.</li>",
        "<li>Endsummen 50 % unter dem typischen Rahmen sind ein Klärungspunkt — oft sind Friedhofsgebühren, Grabstein oder Grabpflege separat berechnet.</li>",
    ),
    # Line 144/146: "Lockangebot hindeuten"
    (
        "Liegt dein Angebot deutlich außerhalb dieses Rahmens, ist das ein Klärungspunkt. Nach unten kann es auf ein Lockangebot hindeuten (Folgekosten kommen später), nach oben auf Premium-Posten, die du dir bewusst aussuchen solltest.",
        "Liegt dein Angebot deutlich außerhalb dieses Rahmens, ist das ein Klärungspunkt. Nach unten kann es bedeuten, dass Posten separat berechnet sind (Friedhofsgebühren, Grabstein, Grabpflege) — frag nach, was wirklich enthalten ist. Nach oben deutet es auf Premium-Posten, die du dir bewusst aussuchen solltest.",
    ),
    # Line 152/154: "Fehlende Friedhofsgebühren" — Tool sagt: separat ist OK
    (
        "<strong>Fehlende Friedhofsgebühren.</strong> Bei Erdbestattung und Urnenbeisetzung auf einem Friedhof sind sie pflicht. Wenn sie nicht im Angebot stehen, kommen sie später separat — und sie können 600–2.800 € betragen.",
        "<strong>Friedhofsgebühren nicht ausgewiesen.</strong> Bei Erdbestattung und Urnenbeisetzung fallen sie immer an. Wenn sie nicht im Angebot stehen, sind sie meist als Fremdleistung separat — frag den Bestatter, ob 600–2.800 € später dazukommen.",
    ),
    # Line 153/155: "Lockend niedrige Endsumme" + "fehlt sehr wahrscheinlich etwas"
    (
        "<strong>Lockend niedrige Endsumme.</strong> Wenn das Gesamt­angebot 50 % unter dem typischen Rahmen liegt, fehlt sehr wahrscheinlich etwas. Lass dir <em>schriftlich</em> bestätigen, dass keine weiteren Kosten auf dich zukommen.",
        "<strong>Auffällig niedrige Endsumme.</strong> Wenn das Gesamt­angebot 50 % unter dem typischen Rahmen liegt, klär die Vollständigkeit: oft sind Friedhofsgebühren, Grabstein oder Grabpflege separat. Lass dir <em>schriftlich</em> bestätigen, dass keine weiteren Kosten auf dich zukommen.",
    ),
    # Line 154/156: Grabpflege "auf Anfrage" — Tool: INFO_POSTEN, kein Mangel
    (
        "<strong>Grabpflege „auf Anfrage\".</strong> Grabpflege über 20 Jahre kann 1.600–5.000 € kosten. Ohne klare Aussage im Erstangebot wird das oft erst nach der Bestattung diskutiert.",
        "<strong>Grabpflege separat.</strong> Grabpflege über 20 Jahre kann 1.600–5.000 € kosten und ist üblicherweise nicht im Erstangebot enthalten. Frag den Preis trotzdem ab, damit du planen kannst.",
    ),
    # Line 162/164: "18 Posten" + "10 Fragen"
    (
        "Unser kostenloser Angebots-Check fragt dich systematisch nach 18 Posten, vergleicht deine Endsumme mit dem regionalen Rahmen und gibt dir eine Ampel + 10 Fragen für deinen Bestatter.",
        "Unser kostenloser Angebots-Check fragt dich nach den typischen Kosten-Posten (je nach Bestattungsart 9–18), vergleicht deine Endsumme mit dem regionalen Rahmen und gibt dir eine Ampel + Klärungspunkte für deinen Bestatter.",
    ),
]

# Per-File specific replacements
PER_FILE = {
    "bestatter-angebot-pruefen.html": [
        # meta description: "Pauschalen sind verdächtig" -> "schwer vergleichbar"
        (
            'welche Pauschalen sind verdächtig',
            'welche Pauschalen schwer vergleichbar sind',
        ),
    ],
    "bestatter-angebot-vergleichen.html": [
        # Multi-Vergleichs-Versprechen dämpfen (Tool prüft 1 Angebot/Lauf)
        # meta description / hero — let runtime grep find actual exact strings
    ],
    "bestatter-rechnung-pruefen.html": [
        # CTA-Hinweis: Tool ist für Angebot VOR Entscheidung, nicht Rechnung NACH
        (
            '<h2>Direkt zum Angebots-Check</h2>\n    <p>Ampel-Bewertung deines Angebots in 3 Minuten · Liste der Klärungspunkte · Fragen für deinen Bestatter</p>',
            '<h2>Angebots-Check (vor der Unterschrift)</h2>\n    <p>Unser Tool prüft das <em>Angebot vor</em> der Beauftragung — für die Rechnungsprüfung nach Beisetzung dient diese Seite. Ampel + Klärungspunkte für dein Erst-Angebot in 3 Minuten.</p>',
        ),
    ],
    "erdbestattung-angebot-pruefen.html": [
        ('Erdbestattung-Angebot prüfen — Sarg, Grabstelle, Beisetzung und alle Pflicht-Posten.',
         'Erdbestattung-Angebot prüfen — Sarg, Grabstelle, Beisetzung und alle Kern-Posten.'),
        ('Welche Pflicht-Posten sind in einem Erdbestattung-Angebot?',
         'Welche Kern-Posten gehören in ein Erdbestattung-Angebot?'),
        ('also 6 Pflicht-Posten',
         'also 6 Kern-Posten'),
    ],
    "feuerbestattung-angebot-pruefen.html": [
        ('Feuerbestattung-Angebot prüfen — Einäscherung, Urne, Beisetzung und alle Pflicht-Posten.',
         'Feuerbestattung-Angebot prüfen — Einäscherung, Urne, Beisetzung und alle Kern-Posten.'),
    ],
    "was-muss-im-kostenvoranschlag-stehen.html": [
        ('Was muss in einem Bestatter-Kostenvoranschlag stehen? Pflicht-Posten + Form-Anforderungen.',
         'Was sollte in einem Bestatter-Kostenvoranschlag stehen? Kern-Posten + Form-Anforderungen.'),
    ],
    "seebestattung-angebot-pruefen.html": [
        ('typischer Rahmen (3.500–6.500 €), Reederei-Posten, Begleitfahrt und Pflicht-Posten',
         'typischer Rahmen (3.500–6.500 €), Reederei-Posten, Begleitfahrt und Kern-Posten'),
    ],
}

def process(path, file_name):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    original = text
    changes = []
    # ALL-8 patterns
    for old, new in ALL_8:
        if old in text:
            count = text.count(old)
            text = text.replace(old, new)
            changes.append(f"  [ALL-8] x{count}: {old[:60]}...")
    # Per-file patterns
    for old, new in PER_FILE.get(file_name, []):
        if old in text:
            count = text.count(old)
            text = text.replace(old, new)
            changes.append(f"  [SPEC]  x{count}: {old[:60]}...")
    if text != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return True, changes
    return False, []

if __name__ == "__main__":
    total_modified = 0
    for fname in FILES:
        path = os.path.join(ROOT, fname)
        if not os.path.exists(path):
            print(f"SKIP {fname}: not found")
            continue
        modified, changes = process(path, fname)
        status = "MOD" if modified else "---"
        print(f"{status} {fname}")
        for c in changes:
            print(c)
        if modified:
            total_modified += 1
    print(f"\nTotal modified: {total_modified}/{len(FILES)}")
