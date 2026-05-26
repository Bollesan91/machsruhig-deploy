# Cluster × v2.4 Konsistenz-Sweep — PASS 3 (Re-Audit-Tunes + RE-OPEN-Fix)
#
# Helper-V3 Re-Audit (Tab 1532777193) Verdict:
# - 2 PASS (#2 vergleichen, #3 versteckte-kosten, #6 erd, #7 feuer)
# - 4 TUNE: #1 og-meta, #4 breadcrumb, #5 body-intent (separater Task #35), Tool-meta
# - 1 RE-OPEN: #8 seebestattung Friedhof/Grabpflege-Selbstwiderspruch
#
# Diese PASS 3 adressiert: alle TUNES ausser #5 + den RE-OPEN.

import os, sys
sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ----- bestatter-angebot-pruefen: "10 Fragen" in og + article description -----
PAGE1 = "bestatter-angebot-pruefen.html"
PAGE1_FIXES = [
    (
        '<meta property="og:description" content="Prüfe in 3 Minuten, ob dein Bestatter-Angebot vollständig und plausibel ist. Ampel-Bewertung + 10 Fragen für den Bestatter.">',
        '<meta property="og:description" content="Prüfe in 3 Minuten, ob dein Bestatter-Angebot vollständig und plausibel ist. Ampel-Bewertung + Klärungspunkte und Fragen für den Bestatter.">',
    ),
    (
        '"description":"Bestatter-Angebot prüfen: Posten, Pauschalen, rote Flaggen und 10 Fragen für deinen Bestatter."',
        '"description":"Bestatter-Angebot prüfen: Posten, Pauschalen, rote Flaggen und Klärungspunkte für deinen Bestatter."',
    ),
]

# ----- was-muss: Breadcrumb-Label -----
PAGE4 = "was-muss-im-kostenvoranschlag-stehen.html"
PAGE4_FIXES = [
    (
        '{"@type":"ListItem","position":3,"name":"Kostenvoranschlag-Pflichtposten","item":"https://machsruhig.de/was-muss-im-kostenvoranschlag-stehen"}',
        '{"@type":"ListItem","position":3,"name":"Kostenvoranschlag-Kernposten","item":"https://machsruhig.de/was-muss-im-kostenvoranschlag-stehen"}',
    ),
    (
        '<a href="/bestattungskosten">Bestattungskosten</a> › Kostenvoranschlag-Pflichtposten</div>',
        '<a href="/bestattungskosten">Bestattungskosten</a> › Kostenvoranschlag-Kernposten</div>',
    ),
]

# ----- Tool meta-description -----
TOOL = "tools/angebotspruefer/index.html"
TOOL_FIXES = [
    (
        '<meta name="description" content="Kostenloser Angebots-Check: Ist dein Bestatter-Angebot vollständig und plausibel? Ampel-Bewertung, Liste vermisster Posten und 10 konkrete Fragen für den Bestatter.">',
        '<meta name="description" content="Kostenloser Angebots-Check: Ist dein Bestatter-Angebot vollständig und plausibel? Ampel-Bewertung, Liste der Klärungspunkte und konkrete Fragen für den Bestatter.">',
    ),
]

# ----- Seebestattung: art-spezifische Pendants statt Friedhof/Grabpflege-Sätze -----
SEE = "seebestattung-angebot-pruefen.html"
SEE_FIXES = [
    # "Das Wichtigste" — Friedhof-Zeile raus, See-Pendant rein
    (
        "<li>Friedhofsgebühren variieren regional bis zu 300 % — Stadt vs. Land.</li>",
        "<li>Reederei-Pauschale + Begleitfahrt variieren je nach Anbieter und Beisetzungsgebiet (Nordsee, Ostsee, Mittelmeer).</li>",
    ),
    (
        "<li>Friedhofsgebühren, Krematorium und Grabpflege werden oft als Fremdleistungen separat berechnet.</li>",
        "<li>Krematorium, Reederei und seetaugliche Urne werden meist als Fremdleistungen separat berechnet.</li>",
    ),
    (
        "<li>Endsummen 50 % unter dem typischen Rahmen sind ein Klärungspunkt — oft sind Friedhofsgebühren, Grabstein oder Grabpflege separat berechnet.</li>",
        "<li>Endsummen 50 % unter dem typischen Rahmen sind ein Klärungspunkt — bei der Seebestattung oft Begleitfahrt, seetaugliche Urne oder Reederei separat berechnet.</li>",
    ),
    # Range-Statement — Friedhof/Grabpflege raus
    (
        "Liegt dein Angebot deutlich außerhalb dieses Rahmens, ist das ein Klärungspunkt. Nach unten kann es bedeuten, dass Posten separat berechnet sind (Friedhofsgebühren, Grabstein, Grabpflege) — frag nach, was wirklich enthalten ist. Nach oben deutet es auf Premium-Posten, die du dir bewusst aussuchen solltest.",
        "Liegt dein Angebot deutlich außerhalb dieses Rahmens, ist das ein Klärungspunkt. Nach unten kann es bedeuten, dass Posten separat berechnet sind (Reederei, Begleitfahrt, seetaugliche Urne) — frag nach, was wirklich enthalten ist. Nach oben deutet es auf Premium-Posten, die du dir bewusst aussuchen solltest.",
    ),
    # Rote Flaggen: Friedhofsgebühren-Bullet raus, durch See-Pendant ersetzen
    (
        '<li><strong>Friedhofsgebühren nicht ausgewiesen.</strong> Bei Erdbestattung und Urnenbeisetzung fallen sie immer an. Wenn sie nicht im Angebot stehen, sind sie meist als Fremdleistung separat — frag den Bestatter, ob 600–2.800 € später dazukommen.</li>',
        '<li><strong>Reederei-Pauschale ohne Aufschlüsselung.</strong> Frag, ob Schiff, Seekarte und Beisetzungsurkunde wirklich enthalten sind. Begleitfahrt für Angehörige (300–800 €) wird häufig separat berechnet.</li>',
    ),
    (
        '<li><strong>Auffällig niedrige Endsumme.</strong> Wenn das Gesamt­angebot 50 % unter dem typischen Rahmen liegt, klär die Vollständigkeit: oft sind Friedhofsgebühren, Grabstein oder Grabpflege separat. Lass dir <em>schriftlich</em> bestätigen, dass keine weiteren Kosten auf dich zukommen.</li>',
        '<li><strong>Auffällig niedrige Endsumme.</strong> Wenn das Gesamt­angebot 50 % unter dem typischen Rahmen liegt, klär die Vollständigkeit: oft sind Begleitfahrt, seetaugliche Urne oder Reederei-Aufschläge separat. Lass dir <em>schriftlich</em> bestätigen, dass keine weiteren Kosten auf dich zukommen.</li>',
    ),
    # Grabpflege-Bullet raus, durch See-Pendant ersetzen
    (
        '<li><strong>Grabpflege separat.</strong> Grabpflege über 20 Jahre kann 1.600–5.000 € kosten und ist üblicherweise nicht im Erstangebot enthalten. Frag den Preis trotzdem ab, damit du planen kannst.</li>',
        '<li><strong>Begleitfahrt mit Angehörigen.</strong> Die Mitfahrt kostet typisch 300–800 € je nach Personenzahl und Strecke. Wenn dein Erstangebot keine klare Pauschale dafür enthält, klär das vor der Unterschrift.</li>',
    ),
]

PLAN = [
    (PAGE1, PAGE1_FIXES),
    (PAGE4, PAGE4_FIXES),
    (TOOL, TOOL_FIXES),
    (SEE, SEE_FIXES),
]

if __name__ == "__main__":
    total = 0
    for rel, fixes in PLAN:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print(f"SKIP {rel}: not found")
            continue
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        orig = text
        changes = []
        for old, new in fixes:
            if old in text:
                text = text.replace(old, new)
                changes.append(f"  applied: {old[:70]}...")
            else:
                changes.append(f"  MISS:    {old[:70]}...")
        if text != orig:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            total += 1
            print(f"MOD {rel}")
        else:
            print(f"--- {rel}")
        for c in changes:
            print(c)
    print(f"\nTotal modified pass 3: {total}/{len(PLAN)}")
