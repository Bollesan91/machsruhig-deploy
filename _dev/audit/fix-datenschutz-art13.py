#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Datenschutzerklaerung: Art.-13-Pflichtkatalog vervollstaendigen.
# Luecken (10.08.2026): (1) Speicherdauer/Kriterien (Art. 13 Abs. 2 lit. a) war ueber
# Abschnitte verstreut und fuer Server-Logs gar nicht angegeben; (2) Rechtsgrundlage fuer
# localStorage fehlte - § 25 Abs. 2 Nr. 2 TDDDG primaerverifiziert (gesetze-im-internet.de);
# (3) keine Aussage zu automatisierter Entscheidungsfindung (Art. 13 Abs. 2 lit. f) und
# zum Datenschutzbeauftragten (Art. 13 Abs. 1 lit. b). Asserts vor Write.
import io, re

p = "datenschutz.html"
s = io.open(p, encoding="utf-8").read()

# --- 1) localStorage-Rechtsgrundlage in Abschnitt 5 (Cookies) ---
OLD5 = ('<h2>5. Cookies</h2>\n  <p>Unsere Website verwendet keine Cookies. Wir setzen kein Google Analytics, '
        'kein Facebook Pixel und keine Werbe- oder Tracking-Cookies ein.</p>')
NEW5 = ('<h2>5. Cookies und lokale Speicherung</h2>\n  <p>Unsere Website verwendet keine Cookies. Wir setzen kein '
        'Google Analytics, kein Facebook Pixel und keine Werbe- oder Tracking-Cookies ein.</p>\n'
        '  <p>Einige Tools speichern deinen Bearbeitungsstand lokal in deinem Browser (localStorage) — etwa den '
        'Abhak-Stand der Checkliste oder deinen Planungsstand. Diese Daten verlassen dein Gerät nicht und du kannst '
        'sie jederzeit selbst löschen. Wir stützen diese Speicherung auf § 25 Abs. 2 Nr. 2 TDDDG: Sie ist unbedingt '
        'erforderlich, damit wir dir den von dir ausdrücklich gewünschten Dienst (ein Tool, das deinen Stand behält) '
        'bereitstellen können. Eine Einwilligung ist dafür nicht erforderlich. Welches Tool was lokal speichert, '
        'steht in der Tabelle in Abschnitt 6.</p>')

# --- 2) Speicherdauer-Uebersicht als eigener Abschnitt vor "10. Deine Rechte" ---
DAUER = '''  <h2>9a. Speicherdauer im Überblick</h2>
  <p>Wie lange Daten gespeichert werden, hängt davon ab, worum es geht. Diese Übersicht fasst zusammen, was in den Abschnitten oben im Einzelnen steht:</p>
  <div class="mr-table-wrap">
    <table class="mr-table">
      <thead><tr><th>Was</th><th>Wie lange</th></tr></thead>
      <tbody>
        <tr><td>Lokale Tool-Daten (localStorage)</td><td>bleiben auf deinem Gerät, bis du sie löschst — wir haben keinen Zugriff darauf</td></tr>
        <tr><td>Server-Logs beim Hoster (Netlify)</td><td>verarbeitet Netlify in eigener Verantwortung nach dessen Vorgaben; wir haben darauf keinen Zugriff und können einzelne Einträge nicht löschen</td></tr>
        <tr><td>Kontakt- und Anfrageformulare</td><td>bis deine Anfrage erledigt ist, danach löschen wir sie; gesetzliche Aufbewahrungspflichten bleiben unberührt</td></tr>
        <tr><td>Freiwillige Daten-Spende (Angebotsprüfer)</td><td>frühestens 30, spätestens 60 Tage nach Eingang trennen wir die Eckdaten von den technischen Empfangsdaten und löschen die ursprüngliche Übermittlung samt IP und Zeitstempel (Abschnitt 6a)</td></tr>
        <tr><td>KI-Textentwürfe (Groq)</td><td>wir speichern weder Eingaben noch Ergebnisse; Groq behält sich nach eigenen Angaben eine kurzzeitige Protokollierung von bis zu 30 Tagen zur Fehleranalyse vor (Abschnitt 7)</td></tr>
        <tr><td>Reichweitenmessung (Umami)</td><td>cookielos und ohne personenbeziehbare Speicherung deiner IP-Adresse (Abschnitt 9)</td></tr>
      </tbody>
    </table>
  </div>

'''

# --- 3) Automatisierte Entscheidungsfindung + DSB vor "12. Änderungen" ---
ZUSATZ = '''  <h2>11a. Keine automatisierte Entscheidungsfindung, kein Datenschutzbeauftragter</h2>
  <p>Wir setzen keine automatisierte Entscheidungsfindung einschließlich Profiling im Sinne von Art. 22 DSGVO ein. Unsere Tools rechnen zwar automatisch (etwa der Kostenrechner oder die Ampel im Angebotsprüfer), aber diese Ergebnisse sind unverbindliche Orientierung — sie entfalten dir gegenüber keine rechtliche Wirkung und niemand entscheidet auf dieser Grundlage über dich.</p>
  <p>Ein Datenschutzbeauftragter ist nicht bestellt, weil die gesetzlichen Voraussetzungen dafür (Art. 37 DSGVO, § 38 BDSG) hier nicht vorliegen. Für alle Datenschutzfragen erreichst du direkt die in Abschnitt 1 genannte verantwortliche Stelle.</p>

'''

pairs = [
    (OLD5, NEW5, 1),
    ('  <h2>10. Deine Rechte</h2>', DAUER + '  <h2>10. Deine Rechte</h2>', 1),
    ('  <h2>12. Änderungen</h2>', ZUSATZ + '  <h2>12. Änderungen</h2>', 1),
    ('Stand: Juni 2026', 'Stand: August 2026', 1),
]
for old, new, n in pairs:
    c = s.count(old)
    assert c == n, ("Anker", old[:60], "erwartet", n, "gefunden", c)
for old, new, n in pairs:
    s = s.replace(old, new)

# Asserts vor Write
for must in ['9a. Speicherdauer im Überblick', '§ 25 Abs. 2 Nr. 2 TDDDG',
             'Art. 22 DSGVO', 'Datenschutzbeauftragter ist nicht bestellt',
             'Recht auf Auskunft', 'Beschwerderecht']:
    assert must in s, "fehlt nach Fix: " + must
assert s.count('<h2>') >= 14, "Abschnittszahl unplausibel"
assert s.count('mr-table-wrap') >= 2, "Tabellen-Wrapper fehlt"
io.open(p, "w", encoding="utf-8").write(s)
print("OK: Speicherdauer-Uebersicht, § 25 TDDDG-Grundlage, Art.-22-/DSB-Klarstellung, Stand aktualisiert.")
