# Daten-Spende Angebotsprüfer — Schema & Redaktionsregeln

Stand: 03.07.2026 · Feature live seit Commit (siehe git log `angebots-spende`)

## Was es ist
Am Ende des Angebotsprüfers kann der Nutzer per **aktivem Klick** („Eckdaten anonym spenden") die anonymen
Eckdaten seines Checks an das Netlify-Form `angebots-spende` senden. Kein Auto-Submit, kein vorangekreuztes
Häkchen, Button erst im Ergebnis-Schritt sichtbar. Die Karte zeigt VOR dem Klick exakt die Werte, die gesendet würden.

## Datensatz-Schema (Netlify Form `angebots-spende`)
| Feld | Inhalt | Anmerkung |
|---|---|---|
| bestattungsart | Key, z. B. `feuerbestattung` | aus BESTATTUNGSARTEN |
| bundesland | Klartext, z. B. `Bayern` | 16 Buckets |
| summe_gerundet | auf volle 100 € gerundet | De-Identifikation |
| posten | sortierte Keys, kommasepariert | Ja/Nein-Häkchen |
| separat | sortierte Keys, kommasepariert | separat abgerechnete Posten |
| pauschal | `ja`/`nein` | |
| ampel_preis | `green`/`yellow`/`red` | |
| ampel_vollstaendigkeit | `green`/`yellow`/`red`/`nicht_pruefbar` | `nicht_pruefbar` bei Pauschale |
| tool_version | z. B. `ap-2026-07` | Schema-Evolution |

**Bewusst NICHT enthalten:** Freitexte, Namen, Kontaktdaten, Bestatter-Name, Angebots-Dokument, IP im Datensatz
(Netlify-Transport-Logs sind davon getrennt, DSE Abschnitt 3), Kennungen/Cookies.

## Harte Regeln (nicht verhandelbar — Design-Grundlage der DSGVO-Einschätzung)
1. **Nie** Freitextfelder oder personenbezogene Felder ergänzen, ohne die komplette Rechtsbasis neu zu bewerten.
2. **Nie** das Angebots-PDF/Foto hochladen lassen.
3. **Veröffentlichung nur aggregiert ab ≥ 25 Datensätzen pro ausgewerteter Gruppe** (steht öffentlich in DSE 6a
   + Tool-Karte — ist damit ein einlösbares Versprechen, kein Marketing).
4. Einzeldatensätze werden nie veröffentlicht oder weitergegeben.
5. Ausreißer-Handling bei Auswertung: Plausibilitätsfenster (z. B. 500–50.000 €), Rest verwerfen — Spam/Bots
   sind trotz Honeypot möglich, curl-Fakes sowieso (Groq-Lektion: Abuse einplanen).

## Bekannte Test-Datensätze (bei Auswertung abziehen)
- 03.07.2026: 1 Smoke-Test-Submission durch Claude (Browser-Smoke nach Deploy), tool_version `ap-2026-07`.

## Wo die Texte stehen (bei Änderung synchron halten!)
- Tool: DS-Kasten oben + Spende-Karte im Ergebnis (`tools/angebotspruefer/index.html`)
- `datenschutz.html` Abschnitt 6a (`#daten-spende`) + Tool-Tabelle + „drei Ausnahmen"-Satz
- `methodik.html` Tool-Tabelle (**wortgleich** mit DSE!) + „Drei Ausnahmen"-Absatz

## Abruf der Daten
Netlify Dashboard → Forms → `angebots-spende` (Bolle-Login) · Export CSV. Bei relevantem Volumen:
API-Export automatisieren (Netlify Forms API, Token nötig — noch nicht eingerichtet).
