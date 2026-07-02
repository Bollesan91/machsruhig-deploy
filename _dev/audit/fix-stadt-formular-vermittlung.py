# -*- coding: utf-8 -*-
"""#3 (Reviewer + Bolle 19.06.): Stadt-Formular sauber in Transparenz Partner
vs. Vermittlungspartner trennen. Bolle-Copy + Infobox. 52 Stadtseiten.
Asserts vor dem einzigen Write je Datei."""
import os, glob

OLD_HEAD = "Kostenlose Anfrage an Bestatter in "
NEW_HEAD = "Unverbindliche Anfrage an einen Bestatter in "

OLD_INTRO = ('<p style="text-align:center">Wenn in Deiner Region bereits ein passender Pilotpartner zu uns geh'
            'ört, leiten wir Deine Anfrage an ihn weiter. machsruhig baut dieses Netzwerk gerade auf — '
            'in vielen Regionen haben wir aktuell noch keinen Partner. Dann melden wir uns trotzdem und sagen '
            'Dir offen, ob und wann wir helfen können. Unverbindlich, kein Vertrag, kein Druck. machsruhig '
            'finanziert sich u. a. über die Vermittlung an Bestatter; für Dich entstehen durch eine '
            'Vermittlung keine zusätzlichen Kosten gegenüber einer direkten Anfrage beim Bestatter.</p>')

NEW_INTRO = ('<p style="text-align:center">Diese Anfrage ist ein <strong>Vermittlungsangebot</strong> und '
            'unabhängig vom <a href="/transparenz-kriterien" style="color:var(--mr-primary)">Transparenz-'
            'Partner-Status</a>. Transparenz Partner legen ihre Preisstruktur nach öffentlichen Kriterien '
            'offen; Vermittlungspartner können Anfragen erhalten. Ein Bestatter kann beides sein, muss es '
            'aber nicht.</p>\n'
            '      <p style="text-align:center">Wenn in Deiner Region ein passender Vermittlungspartner '
            'verfügbar ist, leiten wir Deine Anfrage weiter. Falls nicht, sagen wir Dir das offen. Es '
            'entsteht kein Vertrag, kein Newsletter und kein Verkaufsdruck. Eine mögliche Vermittlungs'
            'vergütung betrifft nur weitergeleitete Anfragen — nicht die Aufnahme als Transparenz '
            'Partner, nicht die Sichtbarkeit und nicht die Reihenfolge im Verzeichnis.</p>\n'
            '      <div style="background:var(--mr-bg,#faf8f5);border:1px solid var(--mr-border,#E8E0D6);'
            'border-radius:10px;padding:14px 18px;margin:16px 0;font-size:13px;line-height:1.55;text-align:left">\n'
            '        <strong style="display:block;margin-bottom:6px">Wichtig zur Einordnung</strong>\n'
            '        <p style="margin:0 0 5px"><strong>Transparenz Partner</strong> legt Preisbeispiele nach '
            '<a href="/transparenz-kriterien" style="color:var(--mr-primary)">öffentlichen Kriterien</a> '
            'offen — kostenlos, nicht käuflich, kein Qualitätsurteil.</p>\n'
            '        <p style="margin:0 0 5px"><strong>Vermittlungspartner</strong> kann auf Wunsch eine Anfrage '
            'erhalten — eine Vergütung kann nur hier entstehen.</p>\n'
            '        <p style="margin:0"><strong>Redaktionelle Inhalte</strong> bleiben unabhängig — '
            'kein Anbieter kann Platzierungen oder Empfehlungen kaufen.</p>\n'
            '      </div>')

files = glob.glob('bestatter/*/index.html')
n = 0
for p in files:
    s = open(p, encoding='utf-8').read()
    if OLD_HEAD not in s:
        continue  # Seite ohne Formular (z.B. /bestatter/ selbst hat kein "Kostenlose Anfrage")
    # --- Asserts vor Write ---
    assert OLD_INTRO in s, "Alt-Intro fehlt: " + p
    assert "passender Pilotpartner" in s, "Pilotpartner fehlt: " + p
    s2 = s.replace(OLD_INTRO, NEW_INTRO)
    s2 = s2.replace("passender Pilotpartner", "passender Vermittlungspartner")
    s2 = s2.replace(OLD_HEAD, NEW_HEAD)
    assert "passender Pilotpartner" not in s2, "Rest-Pilotpartner: " + p
    assert OLD_HEAD not in s2, "Rest-Alt-Head: " + p
    open(p, 'w', encoding='utf-8').write(s2)
    n += 1
print("Stadt-Formulare umgestellt:", n)
