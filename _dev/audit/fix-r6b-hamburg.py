#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R6b — Auflagen aus NO-GO-54-Review der Hamburg-Stadtseite.
KRITISCH 1: Kostenkonsistenz — anonym ueberall 2.830-3.365; Typisch-Untergrenze
  5.000 (>= eigene Postensumme 4.745); Einaescherungs-Spanne ergaenzt.
KRITISCH 2: Tourismus-Ton aus FAQ/JSON-LD ("Ein Muss fuer Hamburg!" etc.).
HOCH: Check24-Affiliate aus Sozialblock raus; Email im Formular Pflicht;
  Service-Schema entfernt; Gebuehrenstand-Hinweis; Wahlfreiheit-Superlativ
  gedaempft (Friedhofszwang genannt).
MITTEL/GERING: 40->30 Jahre; "Mitte des 19. Jh." raus; Vor-1877-Verstorbene
  (Schroeder/Chateauneuf) gestrichen; Waldbestattung 2.525->ca. 2.500 + SH-
  Hinweis; Fristen-Selbstwiderspruch; Standesamt-Doppelung in Akutbox;
  Tabellen-Spaltenkopf; Reederei-Anpreisung neutral; Feebox-Note ehrlich;
  Muenchen-Link/Footer-Link; Article-image; Tippfehler "Vergleich mehrere";
  Ilandkoppel-Ortsangabe; Telefonseelsorge ergaenzt; "draengt nichts" vs 36h.
FAQ-Aenderungen: sichtbarer Text und JSON-LD sind zeichengleich -> expect=2.
"""
import io, sys

P = 'bestatter/hamburg/index.html'
t = io.open(P, encoding='utf-8').read()

def rep(old, new, expect=1):
    global t
    c = t.count(old)
    if c != expect:
        print('FATAL: %r -> %d (erwartet %d)' % (old[:75], c, expect)); sys.exit(1)
    t = t.replace(old, new)

# ===== KRITISCH 1: Kostenkonsistenz =====
# FAQ1 (JSON-LD + sichtbar): Typisch-Untergrenze + anonym + Einaescherung + Tippfehler
rep('Für eine vollständige Erdbestattung mit Trauerfeier rechne mit 4.500–7.000 €. Günstiger: anonyme Beisetzung ab ca. 3.200 € oder unbegleitete Seebestattung als Reederei-Paket ab 1.049 € (zzgl. Einäscherung bei Bestatter). Vergleich mehrere Bestatter, denn Preise variieren.',
    'Für eine vollständige Erdbestattung mit Trauerfeier rechne mit etwa 5.000–7.000 €. Günstiger: anonyme Beisetzung ab ca. 2.830 € gesamt oder unbegleitete Seebestattung als Reederei-Paket ab 1.049 € (zzgl. Einäscherung, bundesweit üblich ca. 300–550 €, über den Bestatter). Vergleiche mehrere Bestatter, denn die Preise variieren.', 2)

# Kostenbox: Reduziert + Typisch angleichen
rep('<td>ca. 2.800–3.400&nbsp;€</td><td>Anonyme Beisetzung (Friedhofsanteil 1.250–1.420&nbsp;€ + Bestatter ca. 1.580–1.945&nbsp;€); Seebestattung unbegleitet als Reederei-Paket ab 1.049&nbsp;€ zzgl. Einäscherung und Bestatterleistungen</td>',
    '<td>ca. 2.830–3.365&nbsp;€</td><td>Anonyme Beisetzung (Friedhofsanteil 1.250–1.420&nbsp;€ + Bestatter ca. 1.580–1.945&nbsp;€); Seebestattung unbegleitet als Reederei-Paket ab 1.049&nbsp;€ zzgl. Einäscherung (bundesweit üblich ca. 300–550&nbsp;€) und Bestatterleistungen</td>')
rep('<td>ca. 4.500–7.000&nbsp;€</td>', '<td>ca. 5.000–7.000&nbsp;€</td>')

# ===== KRITISCH 2: Tourismus-Ton =====
rep('Mit Führungen, Cafés und Parkplätzen ist er täglich für Besucher offen. Ein Muss für Hamburg!',
    'Der Friedhof ist täglich geöffnet; die Verwaltung bietet Führungen und ein Besucherzentrum an.', 2)
rep('<li>Touristische Attraktionsstatus — ein Muss für Hamburg-Besucher</li>\n', '')

# ===== HOCH =====
# Check24-Affiliate aus dem Sozialbestattungs-Block entfernen
rep('''    <div class="mr-hint" style="border-left-color:var(--mr-accent);background:var(--mr-bg-card)">
      <strong>Vorsorge-Tipp gegen Sozialbestattung:</strong> Eine Sterbegeldversicherung deckt die Bestattungskosten ab, damit Angehörige nicht in die § 74-Lage geraten. Vergleichsrechner für Tarife und Versicherungssummen: <a href="https://www.check24.de/sterbegeldversicherung/" rel="sponsored noopener" target="_blank">→ Sterbegeldversicherung vergleichen (Check24)</a>. Hinweis: machsruhig verlinkt diesen Vergleich als Affiliate, der dabei verdiente Anteil finanziert die Redaktion — ohne Mehrkosten für Dich.
    </div>
''', '')

# Email im Lead-Formular Pflicht
rep('<span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">Email</span>\n            <input type="email" name="email" style=',
    '<span style="display:block;font-size:13px;font-weight:600;margin-bottom:4px">Email *</span>\n            <input type="email" name="email" required style=')

# Service-Schema entfernen (machsruhig ist kein Funeral-Services-Provider)
rep('''    {
      "@type": "Service",
      "name": "Bestatter in Hamburg finden",
      "description": "Finde lokale Bestatter in Hamburg. Informationen zu Ohlsdorf, Seebestattungen, Gebühren und Bestattungsrecht.",
      "areaServed": {
        "@type": "City",
        "name": "Hamburg"
      },
      "serviceType": "Funeral Services",
      "provider": {
        "@id": "https://machsruhig.de/#org"
      },
      "author": {
        "@id": "https://machsruhig.de/#redaktion"
      }
    },
''', '')

# Gebuehrenstand-Hinweis + Feebox-Note ehrlich (keine Aufschluesselung versprochen)
rep('Auswahl aus den weiter unten ausführlich aufgeschlüsselten Posten — Bestatterleistungen kommen je nach Bestattungsart hinzu. Stand der Seite: Juni 2026.',
    'Auswahl der wichtigsten Posten — Bestatterleistungen kommen je nach Bestattungsart hinzu. Verbindlich sind die jeweils aktuellen Sätze der Gebührenordnung der Hamburger Friedhöfe AöR. Stand der Seite: Juni 2026.')

# Wahlfreiheit-Superlativ (FAQ6, JSON-LD + sichtbar)
rep('Hamburger haben außergewöhnlich viel Wahlfreiheit und können ihre Bestattungsform völlig individuell gestalten.',
    'Innerhalb des gesetzlichen Rahmens — Friedhofszwang gilt auch in Hamburg, mit Ausnahmen wie der Seebestattung — bleibt viel Spielraum für die Gestaltung.', 2)
rep('Hamburger haben außergewöhnlich viel Wahlfreiheit bei der Gestaltung ihrer Abschiedszeremonie und können ihre Bestattungsform sehr individuell und würdevoll wählen — ganz nach ihren Wünschen und Werten.',
    'Innerhalb des gesetzlichen Rahmens bleibt dabei viel Raum, den Abschied nach den Wünschen und Werten der verstorbenen Person zu gestalten.')

# ===== MITTEL =====
# Fristen-Selbstwiderspruch FAQ4 (2x) + Akutbox-Intro vs. 36h
rep('Erdbestattung muss spätestens nach 10 Tagen erfolgen — dies gibt der Familie ausreichend Zeit (mehr als in Bayern oder anderen Ländern) für Trauerfeier-Planung und Behördengänge.',
    'Erdbestattung muss spätestens nach 10 Tagen erfolgen — mehr Zeit als etwa in Bayern (dort 4 Tage) für Trauerfeier-Planung und Behördengänge.', 2)
rep('Wenn ein Mensch verstorben ist, drängt erst einmal nichts.',
    'Wenn ein Mensch verstorben ist, drängt — abgesehen von Leichenschau und Überführung (36 Stunden) — zunächst wenig.')

# Standesamt-Doppelung: Adressliste aus Akutbox raus (steht in eigener Sektion)
rep('Die sieben Hamburger Standesämter sind: Hamburg-Mitte (Caffamacherreihe 1–3, 20355), Altona, Eimsbüttel (Grindelberg 62–66, 20144), Hamburg-Nord (Kümmellstraße 5–7, 20249), Wandsbek (Schloßstraße 60, 22041), Bergedorf und Harburg (Harburger Rathausforum 3, 21073). ',
    'Eine Übersicht der sieben Bezirks-Standesämter mit Adressen steht weiter unten auf dieser Seite. ')
rep('<th>Standesamt (Adresse, soweit auf dieser Seite belegt)</th>', '<th>Standesamt</th>')

# Faktenfehler Ohlsdorf-Historie
rep('eine Idee, die <strong>rund vierzig Jahre vor dem Münchner Waldfriedhof (eröffnet 1907)</strong> umgesetzt wurde',
    'eine Idee, die <strong>rund dreißig Jahre vor dem Münchner Waldfriedhof (eröffnet 1907)</strong> umgesetzt wurde')
rep('war für die Mitte des 19. Jahrhunderts eine ungewöhnliche Weitsicht', 'war für die damalige Zeit eine ungewöhnliche Weitsicht')
rep(', Theaterdirektor <strong>Friedrich Ludwig Schröder</strong> (1744–1816) sowie der Architekt <strong>Alexis de Chateauneuf</strong> (1799–1853)', '')

# Waldbestattung FAQ5 (2x): Pseudo-Praezision + SH-Verortung
rep('(3) Waldbestattung: ab 2.525 € (Gesamtpaket, keine Grabpflicht).',
    '(3) Wald-/Baumbestattung: ab ca. 2.500 € als Anbieter-Komplettpaket (z. B. FriedWald Kisdorf in Schleswig-Holstein nahe Hamburg; keine Grabpflege nötig).', 2)

# Reederei-Anpreisung neutralisieren
rep('Spezialisierte Reedereien wie die Seebestattungs-Reederei Hamburg organisieren diese Zeremonien seit Jahrzehnten und bieten Erfahrung, Respekt und sichere Abläufe.',
    'Spezialisierte Reedereien organisieren diese Zeremonien seit Jahrzehnten.')

# Links: Muenchen-Karte + Footer
rep('<a href="/bestatter/" class="mr-card" style="text-decoration:none;padding:1.25rem;text-align:center;">\n          <strong>München</strong>',
    '<a href="/bestatter/muenchen/" class="mr-card" style="text-decoration:none;padding:1.25rem;text-align:center;">\n          <strong>München</strong>')
rep('<a href="/bestatter/muenchen/">Bestatter</a>', '<a href="/bestatter/">Bestatter</a>')

# ===== GERING =====
rep('"image": "https://machsruhig.de/assets/og-image.png"', '"image": "https://machsruhig.de/assets/og-cities/hamburg.png"')
rep('</a> in Ohlsdorf-Wellingsbüttel sowie', '</a> in Ohlsdorf sowie')

# Telefonseelsorge in der Akutbox (nach Schritt 1)
rep('sie ist die Grundvoraussetzung für alle weiteren Schritte.</p>',
    'sie ist die Grundvoraussetzung für alle weiteren Schritte. Wer in diesen Stunden seelischen Beistand braucht: Die <strong>Telefonseelsorge</strong> ist rund um die Uhr kostenlos erreichbar unter 0800&nbsp;111&nbsp;0&nbsp;111 und 0800&nbsp;111&nbsp;0&nbsp;222.</p>')

io.open(P, 'w', encoding='utf-8', newline='').write(t)

# Sanity: FAQ-Paritaet — jeder geaenderte FAQ-Text muss weiterhin 2x vorkommen
for s in ['rechne mit etwa 5.000–7.000', 'ab ca. 2.830 € gesamt',
          'Besucherzentrum an.', 'Friedhofszwang gilt auch in Hamburg',
          'dort 4 Tage', 'FriedWald Kisdorf in Schleswig-Holstein nahe Hamburg']:
    c = t.count(s)
    if c != 2:
        print('FATAL Paritaet: %r -> %d' % (s, c)); sys.exit(1)
if t.count('"@type": "Service"') != 0 or t.count('check24.de/sterbegeldversicherung') != 0:
    print('FATAL: Service/Affiliate noch da'); sys.exit(1)
print('R6b OK: 2 KRITISCH + 5 HOCH + MITTEL/GERING angewendet, FAQ-Paritaet verifiziert')
