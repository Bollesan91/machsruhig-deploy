# -*- coding: utf-8 -*-
# Fix-Skript: Helper-V3-Review Pflichtkorrekturen (Reviewer-Run 2026-06-10, NO-GO -> GO)
# A-1: Groq-Default-Retention (30-Tage-Abuse-Logs) statt "ausschliesslich zur Antwort"
# B-2: "vor jeder Uebermittlung informieren" -> "vor der ersten Nutzung"
# C-1: "einmalig an Groq" ist falsch (jede Regeneration = neuer Call) -> "bei jeder Generierung"
# C-2: Phantom-Opt-out -> echter Widerrufs-Button an window.mrAI.revokeConsent()
# C-3: "Opt-in vor jeder Generierung" widerspricht persistentem localStorage-Consent
# Nebenfix: "laut/gemaess Privacy-Policy" -> "nach eigenen Angaben" (Quelle ist das Services Agreement/DPA)
import io, sys

REVOKE_CSS = ".ai-revoke-btn{background:none;border:none;padding:0;color:var(--mr-primary,#7A6B5D);text-decoration:underline;cursor:pointer;font-size:inherit;font-family:inherit}.ai-revoke-btn:disabled{color:var(--mr-text-muted,#73655A);text-decoration:none;cursor:default}"

FIXES = {
    "datenschutz.html": [
        # A-1
        ("Groq verarbeitet die Eingaben nach eigenen Angaben ausschließlich zur Erstellung der Antwort und verwendet sie nicht für das Training von KI-Modellen.",
         "Nach eigenen Angaben speichert Groq die Eingaben nicht dauerhaft und verwendet sie nicht für das Training von KI-Modellen; eine kurzzeitige Protokollierung (bis zu 30 Tage) behält sich Groq lediglich zur Fehleranalyse und Missbrauchsabwehr vor."),
        # B-2
        ("über die wir dich vor jeder Übermittlung im Tool informieren",
         "über die wir dich im Tool vor der ersten Nutzung informieren"),
        # C-2-Begleitfix: Widerruf jetzt per Button im Tool moeglich
        ("Du kannst deine Einwilligung jederzeit mit Wirkung für die Zukunft widerrufen, indem du die KI-Funktion nicht erneut nutzt; da wir deine Eingaben nicht speichern, gibt es bei uns keine gespeicherten Daten, die nachträglich gelöscht werden müssten.",
         "Du kannst deine Einwilligung jederzeit mit Wirkung für die Zukunft widerrufen — direkt im jeweiligen Tool über „KI-Einwilligung widerrufen“; da wir deine Eingaben nicht speichern, gibt es bei uns keine gespeicherten Daten, die nachträglich gelöscht werden müssten."),
    ],
    "tools/trauerrede/index.html": [
        # C-3 (Z.319)
        ("· Opt-in vor jeder Generierung ·",
         "· Opt-in beim ersten Mal, danach direkt ·"),
        # C-1 (Z.1254)
        ("Deine Eingaben (Name, Charakter, Erinnerungen) werden einmalig an <strong>Groq Inc. (USA)</strong> gesendet",
         "Deine Eingaben (Name, Charakter, Erinnerungen) werden bei jeder Generierung an <strong>Groq Inc. (USA)</strong> gesendet"),
        # C-1 (Z.1300, Consent-Modal)
        ("<strong>einmalig an Groq Inc. (USA)</strong> übermittelt, dort von einem Sprachmodell (Llama&nbsp;3.3) verarbeitet und als zusammenhängende Trauerrede zurückgegeben",
         "<strong>bei jeder Generierung an Groq Inc. (USA)</strong> übermittelt, dort von einem Sprachmodell (Llama&nbsp;3.3) verarbeitet und als zusammenhängende Trauerrede zurückgegeben"),
        # Quellen-Hedge (Modal)
        ("Groq speichert die Eingaben gemäß eigener Privacy-Policy <strong>nicht für KI-Training</strong>.",
         "Groq verwendet die Eingaben nach eigenen Angaben <strong>nicht für KI-Training</strong>."),
        # C-2 (Modal-Widerrufstext)
        ("Du kannst die Einwilligung später widerrufen, indem du den Browser-Speicher dieser Seite leerst.",
         "Du kannst die Einwilligung jederzeit über „KI-Einwilligung widerrufen“ im Datenschutz-Hinweis unten auf der Seite widerrufen."),
        # C-1 + C-2 (Privacy-Notice Z.1327) + echter Widerrufs-Button
        ("""            <strong>Deine Privatsphäre:</strong> Deine Eingaben werden nach dem Wizard einmalig an Groq Inc. (USA) übermittelt, damit die KI daraus eine zusammenhängende Rede schreibt. Beim ersten Mal fragt dich ein Modal um Einwilligung — danach läuft die KI automatisch (Opt-out jederzeit über den Datenschutz-Hinweis unten). Groq speichert die Eingaben laut Privacy-Policy nicht für KI-Training. Die Seite nutzt anonyme Reichweiten-Statistiken (Umami) nur nach Cookie-Opt-In.
          </div>""",
         """            <strong>Deine Privatsphäre:</strong> Deine Eingaben werden bei jeder KI-Generierung an Groq Inc. (USA) übermittelt, damit die KI daraus eine zusammenhängende Rede schreibt. Beim ersten Mal fragt dich ein Modal um Einwilligung — danach läuft die KI direkt. Groq verwendet die Eingaben nach eigenen Angaben nicht für KI-Training. Die Seite nutzt anonyme Reichweiten-Statistiken (Umami) nur nach Cookie-Opt-In.{' '}
            <button type="button" className="ai-revoke-btn" onClick={(e) => { window.mrAI.revokeConsent(); e.target.textContent = 'Einwilligung widerrufen ✓ — vor der nächsten KI-Generierung fragen wir erneut.'; e.target.disabled = true; }}>KI-Einwilligung widerrufen</button>
          </div>"""),
        # CSS fuer Widerrufs-Button
        (".ai-style-hint{font-size:11px;color:var(--mr-text-muted);margin-top:6px;font-style:italic}</style>",
         ".ai-style-hint{font-size:11px;color:var(--mr-text-muted);margin-top:6px;font-style:italic}" + REVOKE_CSS + "</style>"),
    ],
    "tools/danksagung/index.html": [
        # C-3 (Z.318)
        ("· Opt-in vor jeder Generierung ·",
         "· Opt-in beim ersten Mal, danach direkt ·"),
        # C-1 (Z.800, Consent-Modal)
        ("<strong>einmalig an Groq Inc. (USA)</strong> übermittelt, dort von einem Sprachmodell (Llama 3.3) verarbeitet und als Danksagung zurückgegeben",
         "<strong>bei jeder Generierung an Groq Inc. (USA)</strong> übermittelt, dort von einem Sprachmodell (Llama 3.3) verarbeitet und als Danksagung zurückgegeben"),
        # Quellen-Hedge (Modal)
        ("Groq speichert die Eingaben laut Privacy-Policy <strong>nicht für KI-Training</strong>.",
         "Groq verwendet die Eingaben nach eigenen Angaben <strong>nicht für KI-Training</strong>."),
        # C-2 (Modal-Widerrufstext)
        ("Widerruf jederzeit durch Leeren des Browser-Speichers dieser Seite.",
         "Widerruf jederzeit über „KI-Einwilligung widerrufen“ im Datenschutz-Hinweis unten auf der Seite."),
        # C-1 + C-2 (Privacy-Notice Z.783) + echter Widerrufs-Button
        ("""<strong>Deine Privatsphäre:</strong> Deine Eingaben werden nach dem Wizard einmalig an Groq Inc. (USA) übermittelt, damit die KI alle drei Textvarianten schreibt. Beim ersten Mal fragt dich ein Modal um Einwilligung — danach läuft die KI automatisch (Opt-out jederzeit über den Datenschutz-Hinweis unten). Groq speichert die Eingaben laut Privacy-Policy nicht für KI-Training. Die Seite nutzt anonyme Reichweiten-Statistiken (Umami) nur nach Cookie-Opt-In.<br/><br/>""",
         """<strong>Deine Privatsphäre:</strong> Deine Eingaben werden bei jeder KI-Generierung an Groq Inc. (USA) übermittelt, damit die KI alle drei Textvarianten schreibt. Beim ersten Mal fragt dich ein Modal um Einwilligung — danach läuft die KI direkt. Groq verwendet die Eingaben nach eigenen Angaben nicht für KI-Training. Die Seite nutzt anonyme Reichweiten-Statistiken (Umami) nur nach Cookie-Opt-In.{' '}
            <button type="button" className="ai-revoke-btn" onClick={(e) => { window.mrAI.revokeConsent(); e.target.textContent = 'Einwilligung widerrufen ✓ — vor der nächsten KI-Generierung fragen wir erneut.'; e.target.disabled = true; }}>KI-Einwilligung widerrufen</button><br/><br/>"""),
        # CSS fuer Widerrufs-Button
        (".mr-ai-consent-modal .btn-cancel:hover{color:var(--mr-text)}</style>",
         ".mr-ai-consent-modal .btn-cancel:hover{color:var(--mr-text)}" + REVOKE_CSS + "</style>"),
    ],
    "tools/abschiedsbrief/index.html": [
        # Konsistenz: PrivacyNotice behauptet "nicht an einen Server uebertragen" ohne KI-Ausnahme
        ("""    React.createElement('p', null, 'Dein Brief-Entwurf wird ausschließlich in deinem Browser gespeichert (localStorage) und nicht an einen Server übertragen. Die Seite selbst nutzt anonyme Reichweiten-Statistiken (Umami), die nur den Seitenbesuch erfassen — nicht deinen Brieftext.')
  );""",
         """    React.createElement('p', null, 'Dein Brief-Entwurf wird ausschließlich in deinem Browser gespeichert (localStorage) und nicht an einen Server übertragen. Die Seite selbst nutzt anonyme Reichweiten-Statistiken (Umami), die nur den Seitenbesuch erfassen — nicht deinen Brieftext.'),
    React.createElement('p', null, 'Einzige Ausnahme: Wenn du die optionale KI-Verfeinerung nutzt, werden deine Texte bei jeder Verfeinerung an Groq Inc. (USA) übermittelt — nur nach deiner Einwilligung. ',
      React.createElement('button', {type: 'button', className: 'ai-revoke-btn', onClick: (e) => { window.mrAI.revokeConsent(); e.target.textContent = 'Einwilligung widerrufen ✓ — vor der nächsten Verfeinerung fragen wir erneut.'; e.target.disabled = true; }}, 'KI-Einwilligung widerrufen'))
  );"""),
        # Quellen-Hedge (Modal)
        ("Für die Verfeinerung werden die Texte deines Entwurfs an Groq Inc. (USA) gesendet und dort verarbeitet. Sie werden nicht für KI-Training gespeichert.",
         "Für die Verfeinerung werden die Texte deines Entwurfs bei jeder Verfeinerung an Groq Inc. (USA) gesendet und dort verarbeitet. Nach Groqs eigenen Angaben werden sie nicht für KI-Training verwendet."),
        # CSS fuer Widerrufs-Button
        (".mr-ai-consent-modal .btn-cancel{background:#fff;color:var(--mr-text-muted,#73655A);border-color:var(--mr-border,#E8E0D6)}</style>",
         ".mr-ai-consent-modal .btn-cancel{background:#fff;color:var(--mr-text-muted,#73655A);border-color:var(--mr-border,#E8E0D6)}" + REVOKE_CSS + "</style>"),
    ],
}

errors = 0
for path, repls in FIXES.items():
    with io.open(path, "r", encoding="utf-8") as f:
        content = f.read()
    for i, (old, new) in enumerate(repls, 1):
        n = content.count(old)
        if n != 1:
            print(f"FEHLER {path} #{i}: {n} Treffer (erwartet 1): {old[:80]!r}")
            errors += 1
            continue
        content = content.replace(old, new)
        print(f"OK {path} #{i}")
    if errors == 0:
        with io.open(path, "w", encoding="utf-8", newline="") as f:
            f.write(content)

sys.exit(1 if errors else 0)
