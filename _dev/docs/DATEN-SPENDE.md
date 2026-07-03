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

**Bewusst NICHT enthalten (Formularfelder):** Freitexte, Namen, Kontaktdaten, Bestatter-Name, Angebots-Dokument, Kennungen/Cookies.

**IP-Realität (03.07.2026 im Dashboard verifiziert):** Netlify speichert an JEDER Form-Submission die Absende-IP
(„Received … from <IP>") — nicht abschaltbar. Die DS-Texte sagen das ehrlich (Empfangs-Log, Art. 6 I f, fließt nicht
in Auswertungen). NIE wieder „keine IP im Datensatz" behaupten.

## Beschlossene Ausbaustufe: Cloudflare Worker + D1 (Bolle, 03.07.2026)
Ziel-Architektur für „richtige Speicherung": Worker-Endpunkt auf der Domain (same-origin) + D1-Datenbank.
Gewinne: Persistenz OHNE IP (Anonymitäts-Claim wird wieder wörtlich wahr), SQL für Preis-Index/Stufe 1,
server-seitige Validierung (Feld-Whitelist, Plausibilitätsfenster 500–50.000 €), kein 100/Monat-Limit,
bestehendes CF-Rate-Limit deckt den Endpunkt. **Nicht jetzt bauen** — Trigger (einer reicht):
(a) ~60+ Submissions/Monat, (b) Start Datenstrategie Stufe 1 (empirische Auswertung), (c) Anonymitäts-Story
muss wasserdicht sein (Partner-/Anwaltsgespräch). Aufwand ~1 Session inkl. V4.1-Gates; Alt-Daten per CSV migrieren;
DS-Texte dann zurückschärfen („keine IP im gespeicherten Datensatz" wieder zulässig).

## Harte Regeln (nicht verhandelbar — Design-Grundlage der DSGVO-Einschätzung)
1. **Nie** Freitextfelder oder personenbezogene Felder ergänzen, ohne die komplette Rechtsbasis neu zu bewerten.
2. **Nie** das Angebots-PDF/Foto hochladen lassen.
3. **Veröffentlichung nur aggregiert ab ≥ 25 Datensätzen pro ausgewerteter Gruppe** (steht öffentlich in DSE 6a
   + Tool-Karte — ist damit ein einlösbares Versprechen, kein Marketing).
4. Einzeldatensätze werden nie veröffentlicht oder weitergegeben.
5. Ausreißer-Handling bei Auswertung: Plausibilitätsfenster (z. B. 500–50.000 €), Rest verwerfen — Spam/Bots
   sind trotz Honeypot möglich, curl-Fakes sowieso (Groq-Lektion: Abuse einplanen).

## Bekannte Test-Datensätze (bei Auswertung abziehen; Löschen im Dashboard = Bolle-Entscheidung)
- 03.07.2026 `angebots-spende`: 1× bestattungsart=`smoketest-detection` (curl-Probe) + 1× feuerbestattung/Bayern/5600 (UI-Smoke), tool_version `ap-2026-07(-smoke)`.
- 03.07.2026 `bestatter-anfrage`: 1× name=`claude-smoketest` (Registrierungs-Gegenprobe) — KEIN echter Lead.

## Vorfall 03.07.2026: Form-Detection war nie aktiviert
Alle Netlify-Forms der Site (bestatter-anfrage auf ~50 Seiten, 3 Tool-Lead-Formulare) waren seit jeher tot —
POST → 404 von Netlify, weil „Form detection" (Pflicht-Toggle seit Ende 2023) nie eingeschaltet war.
03.07. aktiviert (Bolle-Login, Claude-Klick) + Redeploy → 5 Formulare erkannt, Ende-zu-Ende verifiziert.

## 30-Tage-Trennroutine (PFLICHT — oeffentlich zugesagt in DSE 6a + Tool-Karte!)
Monatlich (Bolle, ~2 Min, Dashboard): Forms -> angebots-spende -> "Download as CSV" (Eckdaten-Archiv ohne IP-Spalte
weiterverwenden) -> Submissions aelter 30 Tage loeschen (loescht IP+Zeitstempel). Gilt sinngemaess auch fuer die
Lead-Formulare ("wir loeschen sie, sobald die Anfrage bearbeitet ist"). Widerrufs-Zusage: Nutzer kann sich binnen
30 Tagen mit Absende-Zeitpunkt melden -> Submission gezielt loeschen.

## Publikations-Regeln (Welle 03.07., M11/M12)
- Nicht-ueberlappende Auswertungs-Zellen definieren (kein "BL gesamt" NEBEN "BL x Art" publizieren -> Differenzangriff).
- Median statt Mittelwert, publizierte Werte auf 100 EUR runden.
- Plausibilitaetsfenster 500-50.000 EUR; Ausreisser + auffaellige Serien (gleiche IP vor Trennung) verwerfen.

## Wo die Texte stehen (bei Änderung synchron halten!)
- Tool: DS-Kasten oben + Spende-Karte im Ergebnis (`tools/angebotspruefer/index.html`)
- `datenschutz.html` Abschnitt 6a (`#daten-spende`) + Tool-Tabelle + „drei Ausnahmen"-Satz
- `methodik.html` Tool-Tabelle (**wortgleich** mit DSE!) + „Drei Ausnahmen"-Absatz

## Abruf der Daten
Netlify Dashboard → Forms → `angebots-spende` (Bolle-Login) · Export CSV. Bei relevantem Volumen:
API-Export automatisieren (Netlify Forms API, Token nötig — noch nicht eingerichtet).
