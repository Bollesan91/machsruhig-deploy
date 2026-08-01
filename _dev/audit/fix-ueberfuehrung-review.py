#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ueberfuehrung-Seite: Tab-Review-Findings (Score 71) nach Stufe-3-Eigenverifikation.
# F3  MINOR: Leichenpass-Behoerde in Checkliste/Dokumentenliste/Tabelle kategorisch "Gesundheitsamt" —
#            tatsaechlich bundeslandabhaengig (NRW Ordnungsbehoerde, BY Gemeinde, BW Ortspolizeibehoerde).
# F8/F9 MAJOR: Bestattungsfonds — "aehnlich einer Versicherung auf Gegenseitigkeit" suggeriert Aufsicht/
#            Rechtsanspruch, die es nicht gibt; Grab-/Beisetzungskosten am Ort haeufig nicht gedeckt.
# F10 MAJOR: Sozialamt/Kostentragung fehlte ganz. § 74 SGB XII primaer verifiziert (gesetze-im-internet):
#            "Die erforderlichen Kosten einer Bestattung werden uebernommen, soweit den hierzu
#            Verpflichteten nicht zugemutet werden kann, die Kosten zu tragen."
import io, re, json
p = "ueberfuehrung-ausland.html"
s = io.open(p, encoding="utf-8").read()

pairs = []

# --- F3: Behoerden-Konsistenz (5 Stellen, teils 2x = JSON-LD + sichtbar) ---
pairs.append((
 'in Deutschland in der Regel vom Gesundheitsamt',
 'in Deutschland je nach Bundesland vom Gesundheitsamt, von der Ordnungsbehörde oder von der Gemeinde', 2))
pairs.append((
 'von der zuständigen Behörde am Sterbeort (meist dem Gesundheitsamt)',
 'von der zuständigen Behörde am Sterbeort (je nach Bundesland Gesundheitsamt, Ordnungsbehörde oder Gemeinde)', 1))
pairs.append((
 '<strong>Leichenpass</strong> (Totenpass / Laissez-passer, vom Gesundheitsamt)',
 '<strong>Leichenpass</strong> (Totenpass / Laissez-passer, von der zuständigen Behörde am Sterbeort)', 1))
pairs.append((
 '<tr><td>Leichenpass (Gesundheitsamt)</td>',
 '<tr><td>Leichenpass (zuständige Behörde)</td>', 1))
pairs.append((
 '<li>☐ Leichenpass beim Gesundheitsamt beantragt</li>',
 '<li>☐ Leichenpass bei der zuständigen Behörde beantragt (je nach Bundesland Gesundheitsamt, Ordnungsbehörde oder Gemeinde — im Zweifel bei der Stadt erfragen)</li>', 1))

# --- F9: Rechtsnatur der Fonds nicht als Versicherung framen ---
pairs.append((
 'die Kosten der Überführung und Bestattung übernimmt — ähnlich einer Versicherung auf Gegenseitigkeit.',
 'die Kosten der Überführung und Bestattung übernimmt — dem Prinzip nach eine Solidarkasse. Rechtlich ist ein solcher Fonds aber <strong>kein beaufsichtigter Versicherer</strong>.', 1))

# --- F8+F9: Hinweis-Box inhaltlich aufruesten ---
OLD_HINT = '<strong>Vor dem Beitritt die Satzung lesen:</strong> Leistungen, Beiträge, Wartezeiten und die abgedeckten Zielländer unterscheiden sich je Verein erheblich. Der DİTİB-Fonds etwa führt derzeit nur in die Türkei über. Prüfe vor einem Beitritt, welche Länder abgedeckt sind, wer mitversichert ist und was im Fall einer Bestattung in Deutschland gezahlt wird. Wer keinen passenden Fonds hat, kann die Überführung auch über eine Sterbegeld- oder Bestattungsvorsorge absichern.'
NEW_HINT = ('<strong>Vor dem Beitritt die Satzung lesen:</strong> Leistungen, Beiträge, Wartezeiten und die abgedeckten Zielländer unterscheiden sich je Verein erheblich. Der DİTİB-Fonds etwa führt derzeit nur in die Türkei über. '
            'Ein Bestattungsfonds ist <strong>keine beaufsichtigte Versicherung</strong>: Es gibt in der Regel keine Versicherungsaufsicht und keinen Sicherungsfonds, und viele Satzungen gewähren die Unterstützung ausdrücklich ohne Anerkennung eines Rechtsanspruchs. '
            'Klär deshalb vor dem Beitritt: Besteht ein einklagbarer Anspruch? Gibt es eine Wartezeit nach dem Eintritt? Was passiert mit den Beiträgen bei Austritt oder wenn du einmal nicht zahlst? Welche Länder sind abgedeckt, wer ist mitversichert? '
            'Und besonders wichtig: <strong>Grab- und Beisetzungskosten am Bestattungsort sind häufig nicht enthalten</strong> — sie können vierstellig ausfallen und bleiben dann bei der Familie. Wer keinen passenden Fonds hat, kann die Überführung auch über eine Sterbegeld- oder Bestattungsvorsorge absichern.')
pairs.append((OLD_HINT, NEW_HINT, 1))

for old, new, n in pairs:
    c = s.count(old)
    assert c == n, ("Anker", c, "erwartet", n, old[:70])
for old, new, n in pairs:
    s = s.replace(old, new)

# --- F10: Sozialamt/Kostentragung ergaenzen (nach der Komplettpreis-Warnung) ---
ANCHOR = '''Gerade die Kosten im Zielland (Grab, Bestattung vor Ort) sind nicht immer eingerechnet.
    </div>
  </section>'''
BOX = '''Gerade die Kosten im Zielland (Grab, Bestattung vor Ort) sind nicht immer eingerechnet.
    </div>
    <div class="mr-hint">
      <strong>Wer trägt die Kosten — und was zahlt das Sozialamt?</strong> Zahlen muss zunächst, wer den Auftrag erteilt; im Innenverhältnis tragen die Erben die Bestattungskosten (§&nbsp;1968 BGB), daneben können die nach Landesrecht Bestattungspflichtigen herangezogen werden. Reicht das Geld nicht, übernimmt das Sozialamt nach §&nbsp;74 SGB&nbsp;XII die <em>erforderlichen</em> Kosten einer Bestattung — „soweit den hierzu Verpflichteten nicht zugemutet werden kann, die Kosten zu tragen&#8220;. Maßstab ist dabei eine ortsübliche, einfache Bestattung in Deutschland: <strong>Die Mehrkosten einer Überführung ins Ausland werden in aller Regel nicht übernommen.</strong> Wer die Überführung beauftragt und auf eine spätere Kostenübernahme hofft, bleibt darauf also meist selbst sitzen. Kläre die Kostenfrage deshalb vor der Beauftragung — beim Sozialamt und, wenn vorhanden, beim Bestattungsfonds.
    </div>
  </section>'''
assert s.count(ANCHOR) == 1, ("F10-Anker", s.count(ANCHOR))
s = s.replace(ANCHOR, BOX)

for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
    json.loads(m.group(1))
assert 'beim Gesundheitsamt beantragt' not in s
io.open(p, "w", encoding="utf-8").write(s)
print("OK: F3 (5 Stellen), F8/F9 (Framing + Hinweis), F10 (§74 SGB XII Box). JSON-LD parst.")
