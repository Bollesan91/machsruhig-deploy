from pathlib import Path
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

p = Path('index.html')
s = p.read_text(encoding='utf-8')
A1_OLD = "Über 50 deutsche Städte mit Friedhöfen, Kosten und konkreten Ansprechstellen — von Berlin bis München, von Hamburg bis Saarbrücken."
A1_NEW = "48 deutsche Städte mit Friedhöfen, Kosten und konkreten Ansprechstellen — von Berlin bis München, von Hamburg bis Saarbrücken."
assert A1_OLD in s, "A1 anchor missing"
s = s.replace(A1_OLD, A1_NEW)
A2_OLD = "→ Alle 50 Städte ansehen"
A2_NEW = "→ Alle 48 Städte ansehen"
assert A2_OLD in s, "A2 anchor missing"
s = s.replace(A2_OLD, A2_NEW)
A3_OLD = 'Wir sind kein Bestattungsunternehmen, kein Versicherungsmakler und keine Anwaltskanzlei. Wir verkaufen nichts und vermitteln keine Verträge. Wenn du eine konkrete Bestattung in Auftrag geben willst, einen Vorsorgevertrag abschließen oder rechtsverbindliche Beratung brauchst, ist die richtige Adresse ein <a href="/bestatter/muenchen/">Bestatter</a>, eine Versicherung oder ein Notar.'
A3_NEW = 'Wir sind kein Bestattungsunternehmen, kein Versicherungsmakler und keine Anwaltskanzlei. Unsere Inhalte sind redaktionell unabhängig. Auf einigen Stadtseiten kannst du über ein unverbindliches Formular drei Bestatter aus deiner Region anfragen — wenn daraus eine Beauftragung entsteht, kann machsruhig eine Vermittlungsvergütung vom Bestatter erhalten. Für dich entstehen dadurch keine Mehrkosten, und die Auswahl der Bestatter ist provisionsunabhängig. Für eine konkrete Bestattung, einen Vorsorgevertrag oder rechtsverbindliche Beratung ist die richtige Adresse ein <a href="/bestatter/muenchen/">Bestatter</a>, eine Versicherung oder ein Notar.'
assert A3_OLD in s, "A3 anchor missing"
s = s.replace(A3_OLD, A3_NEW)
p.write_text(s, encoding='utf-8', newline='\n')
print("A: Homepage gefixt")

p = Path('bestatter/stuttgart/index.html')
s = p.read_text(encoding='utf-8')
b_count = 0
for old, new in [
    ("41 städtische Friedhöfe", "42 städtische Friedhöfe"),
    ("41 städtischen Friedhöfen", "42 städtischen Friedhöfen"),
    ("alle 41 städtischen Friedhöfe", "alle 42 städtischen Friedhöfe"),
]:
    n = s.count(old)
    if n > 0:
        s = s.replace(old, new)
        b_count += n
p.write_text(s, encoding='utf-8', newline='\n')
print(f"B: Stuttgart 41->42 ({b_count} Stellen)")

p = Path('bestatter/hannover/index.html')
s = p.read_text(encoding='utf-8')
C_OLD = "Hannover unterhält rund 16 städtische Friedhöfe. Fünf davon prägen das Bestattungswesen der Stadt besonders"
C_NEW = "Hannover unterhält 19 städtische Friedhöfe — fünf große Hauptfriedhöfe und 14 kleinere Stadtteilfriedhöfe (Quelle: Landeshauptstadt Hannover). Die fünf großen prägen das Bestattungswesen der Stadt besonders"
assert C_OLD in s, "C anchor missing"
s = s.replace(C_OLD, C_NEW)
p.write_text(s, encoding='utf-8', newline='\n')
print("C: Hannover 16->19 gefixt")

p = Path('bestatter/bonn/index.html')
s = p.read_text(encoding='utf-8')
D_OLD_FAQ = "Bonn unterhält rund ein Dutzend städtischer Friedhöfe. Die zentralen sind der Alte Friedhof am Stadtgarten (seit 1934 nicht mehr für reguläre Beisetzungen geöffnet), der Südfriedhof in Kessenich als heutiger Hauptfriedhof, der Nordfriedhof an der Kölnstraße sowie der historisch bedeutsame Burgfriedhof Bad Godesberg. Hinzu kommen weitere Stadtbezirksfriedhöfe in Beuel, Endenich, Poppelsdorf und Mehlem."
D_NEW_FAQ = "Bonn unterhält rund 40 kommunale Friedhöfe (Quelle: Bundesstadt Bonn). Die zentralen sind der Alte Friedhof am Stadtgarten (seit 1934 nicht mehr für reguläre Beisetzungen geöffnet), der Südfriedhof in Kessenich als heutiger Hauptfriedhof, der Nordfriedhof an der Kölnstraße sowie der historisch bedeutsame Burgfriedhof Bad Godesberg. Hinzu kommen Stadtbezirksfriedhöfe in Beuel, Endenich, Poppelsdorf, Mehlem und weiteren Ortsteilen."
n_faq = s.count(D_OLD_FAQ)
assert n_faq >= 2, f"D FAQ anchor not found 2x (found {n_faq})"
s = s.replace(D_OLD_FAQ, D_NEW_FAQ)
D_OLD_LIST = "<li><strong>Städtische Friedhöfe:</strong> rund ein Dutzend</li>"
D_NEW_LIST = "<li><strong>Kommunale Friedhöfe:</strong> rund 40 (Quelle: Bundesstadt Bonn)</li>"
assert D_OLD_LIST in s, "D list anchor missing"
s = s.replace(D_OLD_LIST, D_NEW_LIST)
p.write_text(s, encoding='utf-8', newline='\n')
print(f"D: Bonn Dutzend->40 ({n_faq} FAQ + 1 Liste, JSON-LD synchron)")

p = Path('bestatter/bremen/index.html')
s = p.read_text(encoding='utf-8')
E_OLD = '<strong>machsruhig Redaktion</strong><span class="mr-meta-sep" aria-hidden="true"> · </span><span>Fachlich geprüft: Fachpool-Reviewer (in Anbindung)</span><span class="mr-meta-sep" aria-hidden="true"> · </span><span>Stand: 18. Mai 2026</span>'
E_NEW = '<strong>machsruhig Redaktion</strong><span class="mr-meta-sep" aria-hidden="true"> · </span><span>Stand: 18. Mai 2026</span>'
assert E_OLD in s, "E anchor missing"
s = s.replace(E_OLD, E_NEW)
p.write_text(s, encoding='utf-8', newline='\n')
print("E: Bremen Fake-Reviewer-Label entfernt")

p = Path('bestatter/berlin/index.html')
s = p.read_text(encoding='utf-8')
F_OLD = "<h1>Bestatter in Berlin finden — über 200 Friedhöfe, günstige Kosten & moderne Regeln</h1>"
F_NEW = "<h1>Bestattung in Berlin: über 200 Friedhöfe, Gebühren und Fristen</h1>"
assert F_OLD in s, "F anchor missing"
s = s.replace(F_OLD, F_NEW)
p.write_text(s, encoding='utf-8', newline='\n')
print("F: Berlin H1 Template-konsistent")

p = Path('bestatter/koeln/index.html')
s = p.read_text(encoding='utf-8')
g_count = 0
g_patches = [
    ("Sie selbst müssen praktisch nur den Arzt rufen und das Bestattungsinstitut beauftragen.",
     "Du musst praktisch nur den Arzt rufen und ein Bestattungsinstitut beauftragen."),
    ("Holen Sie 2–3 Vergleichsangebote ein.",
     "Hol dir 2–3 Vergleichsangebote."),
    ("sollten Sie mit 4.000–6.000 € rechnen",
     "rechne mit insgesamt 4.000–6.000 €"),
    ("Voraussetzung: Sie sind nach Erbrecht",
     "Voraussetzung: Du bist nach Erbrecht"),
]
for old, new in g_patches:
    n = s.count(old)
    if n > 0:
        s = s.replace(old, new)
        g_count += n
    else:
        print(f"  WARNING: G-anchor not found: {old[:60]}")
p.write_text(s, encoding='utf-8', newline='\n')
print(f"G: Koeln Du/Sie ({g_count} Vorkommen)")

s = Path('bestatter/koeln/index.html').read_text(encoding='utf-8')
residual_sie = sum(s.count(pp) for pp in [" Sie ", "Sie selbst", "Holen Sie", "sollten Sie", "wenn Sie", "Voraussetzung: Sie"])
print(f"  Koeln residual Sie: {residual_sie}")
