# Cluster-Pages × v2.4 Konsistenz-Sweep — PASS 2
# Adressiert: JSON-LD FAQ "Lockangebot"-Q + restliche "Pflicht-Posten" in Body-HTML.

import os, sys
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

# Patterns repeated across ALL 8 (JSON-LD FAQ Q + HTML FAQ accordion)
ALL_8 = [
    # JSON-LD FAQ — Lockangebot Q
    (
        '{"@type":"Question","name":"Was ist ein Lockangebot bei Bestattern?","acceptedAnswer":{"@type":"Answer","text":"Ein Lockangebot ist ein ungewöhnlich niedriges Angebot, das nur Grundleistungen abdeckt. Friedhofsgebühren, Krematoriumskosten oder Trauerfeier kommen später separat dazu — die Endsumme liegt dann oft deutlich über vergleichbaren Komplettangeboten. Liegt ein Angebot 50 % unter typischen Marktpreisen, lass dir vorab schriftlich bestätigen, welche Folgekosten noch entstehen können.',
        '{"@type":"Question","name":"Was bedeuten auffällig niedrige Bestatter-Angebote?","acceptedAnswer":{"@type":"Answer","text":"Ein Angebot, das deutlich unter dem typischen Rahmen liegt, ist kein Urteil — aber ein Klärungspunkt. Häufig fehlen Friedhofsgebühren, Krematoriumskosten oder Grabpflege im Erst-Angebot, weil sie als Fremdleistung separat berechnet werden. Liegt ein Angebot 50 % unter typischen Marktpreisen, lass dir vorab schriftlich bestätigen, welche Folgekosten noch entstehen können.',
    ),
    # HTML FAQ accordion — Lockangebot Q
    (
        '<details><summary>Was ist ein Lockangebot bei Bestattern?</summary><div class="faq-answer">Ein Lockangebot ist ein ungewöhnlich niedriges Angebot, das nur Grundleistungen abdeckt. Friedhofsgebühren, Krematoriumskosten oder Trauerfeier kommen später separat dazu — die Endsumme liegt dann oft deutlich über vergleichbaren Komplettangeboten. Liegt ein Angebot 50 % unter typischen Marktpreisen, lass dir vorab schriftlich bestätigen, welche Folgekosten noch entstehen können.</div></details>',
        '<details><summary>Was bedeuten auffällig niedrige Bestatter-Angebote?</summary><div class="faq-answer">Ein Angebot, das deutlich unter dem typischen Rahmen liegt, ist kein Urteil — aber ein Klärungspunkt. Häufig fehlen Friedhofsgebühren, Krematoriumskosten oder Grabpflege im Erst-Angebot, weil sie als Fremdleistung separat berechnet werden. Liegt ein Angebot 50 % unter typischen Marktpreisen, lass dir vorab schriftlich bestätigen, welche Folgekosten noch entstehen können.</div></details>',
    ),
]

# Per-File "Pflicht-Posten" in Body (Bestattungsart-Pages)
PER_FILE = {
    "erdbestattung-angebot-pruefen.html": [
        ("Ein vollständiges Erdbestattung-Angebot sollte diese Pflicht-Posten klar ausweisen:",
         "Ein vollständiges Erdbestattung-Angebot sollte diese Kern-Posten klar ausweisen:"),
    ],
    "feuerbestattung-angebot-pruefen.html": [
        ("Ein vollständiges Feuerbestattung-Angebot sollte diese Pflicht-Posten klar ausweisen:",
         "Ein vollständiges Feuerbestattung-Angebot sollte diese Kern-Posten klar ausweisen:"),
    ],
    "seebestattung-angebot-pruefen.html": [
        ("diese Pflicht-Posten klar ausweisen:",
         "diese Kern-Posten klar ausweisen:"),
    ],
    "was-muss-im-kostenvoranschlag-stehen.html": [
        # Headline may carry "Pflicht-Posten"
        ("Pflicht-Posten + Form-Anforderungen",
         "Kern-Posten + Form-Anforderungen"),
    ],
}

def process(path, file_name):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    original = text
    changes = []
    for old, new in ALL_8:
        if old in text:
            text = text.replace(old, new)
            changes.append(f"  [ALL-8] {old[:60]}...")
    for old, new in PER_FILE.get(file_name, []):
        if old in text:
            text = text.replace(old, new)
            changes.append(f"  [SPEC]  {old[:60]}...")
    if text != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return True, changes
    return False, []

if __name__ == "__main__":
    total = 0
    for fname in FILES:
        path = os.path.join(ROOT, fname)
        modified, changes = process(path, fname)
        status = "MOD" if modified else "---"
        print(f"{status} {fname}")
        for c in changes:
            print(c)
        if modified:
            total += 1
    print(f"\nTotal modified pass 2: {total}/{len(FILES)}")
