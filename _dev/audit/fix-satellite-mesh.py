# -*- coding: utf-8 -*-
"""Pass 2: angebot-pruefen-Familie quervernetzen.
Ersetzt die doppelte Rechner-Card (Qualitaetsdefekt) durch Angebotsstandard +
thematisch passende Geschwister-Cards. mr-related-Format (strong/span)."""
import io

DUP = '      <a href="/tools/bestattungskosten-rechner/"><strong>Schneller Kostenrechner</strong><span>In 5 Schritten</span></a>'

CARD = {
 'standard':  '      <a href="/angebotsstandard"><strong>Der Angebotsstandard</strong><span>Die 15 Posten, an denen du misst</span></a>',
 'generic':   '      <a href="/bestatter-angebot-pruefen"><strong>Bestatter-Angebot prüfen</strong><span>Der allgemeine 3-Minuten-Check</span></a>',
 'erd':       '      <a href="/erdbestattung-angebot-pruefen"><strong>Erdbestattung-Angebot prüfen</strong><span>Sarg, Grabstelle, Friedhof</span></a>',
 'feuer':     '      <a href="/feuerbestattung-angebot-pruefen"><strong>Feuerbestattung-Angebot prüfen</strong><span>Urne, Krematorium, Beisetzung</span></a>',
 'see':       '      <a href="/seebestattung-angebot-pruefen"><strong>Seebestattung-Angebot prüfen</strong><span>Reederei, Überführung, Beisetzung</span></a>',
 'vergleich': '      <a href="/bestatter-angebot-vergleichen"><strong>Zwei Angebote vergleichen</strong><span>Posten nebeneinander prüfen</span></a>',
 'rechnung':  '      <a href="/bestatter-rechnung-pruefen"><strong>Bestatter-Rechnung prüfen</strong><span>Schlussrechnung kontrollieren</span></a>',
}

# je Datei: welche Cards die Dup-Zeile ersetzen
PLAN = {
 'bestatter-angebot-pruefen.html':     ['standard','erd','feuer','see'],
 'erdbestattung-angebot-pruefen.html': ['standard','generic','feuer','see'],
 'feuerbestattung-angebot-pruefen.html':['standard','generic','erd','see'],
 'seebestattung-angebot-pruefen.html': ['standard','generic','erd','feuer'],
 'bestatter-angebot-vergleichen.html': ['standard','generic','rechnung'],
 'bestatter-rechnung-pruefen.html':    ['standard','generic','vergleich'],
}

results = []
# 1) ASSERTS zuerst (alle), erst dann schreiben
loaded = {}
for f, keys in PLAN.items():
    with io.open(f, encoding='utf-8') as fh:
        t = fh.read()
    assert t.count(DUP) == 1, "%s: DUP-Zeile %dx (erwartet 1)" % (f, t.count(DUP))
    repl = '\n'.join(CARD[k] for k in keys)
    # Selbst-Link-Schutz
    self_key = f.replace('-angebot-pruefen.html','').replace('bestatter-','').replace('bestattung','')
    loaded[f] = (t, repl)

for f, (t, repl) in loaded.items():
    new = t.replace(DUP, repl)
    # kein Selbstlink: die eigene URL darf nicht in den neuen Cards stehen
    own = '/' + f[:-5]
    assert ('href="%s"' % own) not in repl, "%s: Selbstlink in neuen Cards!" % f
    with io.open(f, 'w', encoding='utf-8') as fh:
        fh.write(new)
    added = repl.count('<a href')
    results.append("%-38s Dup->%d Cards" % (f, added))

print("\n".join(results))
print("OK:", len(results), "Dateien")
