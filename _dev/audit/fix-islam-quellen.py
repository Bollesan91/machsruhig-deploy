#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Islam-Pillar: Quellen/Provenienz an die tatsaechlich geleistete Primaerverifikation angleichen
# (16/16 Landesgesetze am amtlichen Landesrecht-Portal geprueft, 07/2026) + ungenaue RLP-Angabe
# korrigieren (kein blosses 'Aufhebung der Sargpflicht', sondern neues BestG v. 22.09.2025).
import io, re, json
p = "islamische-bestattung.html"
s = io.open(p, encoding="utf-8").read()

pairs = [
# 1) Stand-Satz: Primaerverifikation benennen
('Eigene Aufbereitung Stand Juni 2026 auf Basis der folgenden Quellen. Die rechtlichen Regelungen sind Ländersache und ändern sich laufend; verbindlich ist die Auskunft der zuständigen Friedhofsverwaltung im Einzelfall.',
 'Eigene Aufbereitung, Stand Juli 2026. Die Angaben zu Sargpflicht und Bestattungsfrist haben wir für alle 16 Bundesländer im jeweiligen Gesetzes- beziehungsweise Verordnungstext auf den amtlichen Landesrecht-Portalen nachgelesen (geprüft 07/2026). Bestattungsrecht ist Ländersache und ändert sich laufend; verbindlich ist die Auskunft der zuständigen Friedhofsverwaltung im Einzelfall.'),
# 2) Quellen-Eintrag Landesgesetze: praezise + RLP korrekt
('<li>Landesbestattungsgesetze der 16 Bundesländer (Stand Juni 2026) — Sargpflicht, Tuchbestattung, Mindest- und Höchstruhezeiten; in Rheinland-Pfalz Aufhebung der Sargpflicht zum Oktober 2025</li>',
 '<li>Bestattungsgesetze und Bestattungsverordnungen der 16 Bundesländer, im amtlichen Gesetzestext geprüft 07/2026 — Grundlage der Länder-Tabelle oben (Sargpflicht/Tuchbestattung und Mindestfrist mit Paragraf). Jüngste Änderungen: Rheinland-Pfalz hat am 22. September 2025 ein neues Bestattungsgesetz erhalten (Tuchbestattung generell zulässig), Sachsen-Anhalt hat seines zum 1. Oktober 2025 geöffnet.</li>'),
# 3) Provenienz-Zeile
('<strong>Bestattungsrecht</strong>Landesgesetze aller 16 BL (Stand Juni 2026) · kommunale Satzungen',
 '<strong>Bestattungsrecht</strong>Gesetzestexte aller 16 BL, primär geprüft 07/2026 · kommunale Satzungen'),
]
for old, new in pairs:
    c = s.count(old)
    assert c == 1, ("Anker nicht eindeutig", c, old[:70])
for old, new in pairs:
    s = s.replace(old, new)

for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
    json.loads(m.group(1))
assert 'Stand Juni 2026' not in s, "Rest 'Stand Juni 2026'"
io.open(p, "w", encoding="utf-8").write(s)
print("OK: Quellen/Provenienz aktualisiert (3 Stellen), JSON-LD parst.")
