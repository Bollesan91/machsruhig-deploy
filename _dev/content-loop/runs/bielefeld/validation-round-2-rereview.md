Ich hole die aktuelle Bielefeld-Datei.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/bielefeld/index.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/bielefeld/index.html

Ich prüfe systematisch: Top-3-Claim, FAQ-Sync, Pellafriedhof, §-Nummern, Adressen, Cross-Links.

Systematische Prüfung:

Top-3-Claim: "drei größten Friedhöfe Deutschlands" mit Vergleich Ohlsdorf + München-Waldfriedhof. Ohlsdorf ~389 ha (#1), München-Waldfriedhof ~169 ha. Senne 98 ha → Top-3 ist tendenziös. Aber: "drei größten" könnte gemeint sein als "einer der drei größten" — Text sagt aber "gehört zu den drei größten" und nennt nur zwei Vergleichsanlagen. Hauptfriedhof Frankfurt (~70 ha), Südwestkirchhof Stahnsdorf (~206 ha), Hauptfriedhof Saarbrücken usw. — 98 ha ist nicht Top-3. Faktischer Fehler.
FAQ HTML vs Schema Sync:
Schema FAQ #4 (Ruhezeit): "Kindern unter sieben Jahren"
HTML FAQ #4: "Kindern bis zur Vollendung des siebten Lebensjahres"
Semantisch identisch, aber Wortlaut weicht ab → minor.
Schema #7 = muslimische Grabfelder, HTML letzter Eintrag = muslimische — Reihenfolge im HTML weicht ab (Baum vor muslim), Schema hat muslim vor Baum. Reihenfolge-Mismatch FAQPage Schema vs DOM.
Pellafriedhof 2017-Stop: Behauptung "Seit 2017 keine neuen Grabnutzungsrechte" — schwer verifizierbar. Bei Re-Review ohne Primärquelle = nicht als MAJOR markieren (UNSURE-Grenze).
§-Nummern: §9, §13, §14, §16 BestG NRW, §28 PStG — alle korrekt.
Adressen: Niederwall 23, Am Stadtholz 24, Brackweder Straße 80, Gunststraße 63 — plausibel, keine offensichtlichen Fehler.
Cross-Links: /bestatter/muenster/, /bestatter/dortmund/, /bestatter/koeln/ — Dortmund existiert per Pipeline. Münster/Köln-Status unklar, aber nicht /muenchen/ → ok per Vorgabe.

STADT: Bielefeld

VERDICT: MAJOR-FIX (2 Funde)

Fund 1 — Faktischer Fehler / Top-3-Übertreibung

Wo: §1 Sennefriedhof-Absatz: "gehört der Sennefriedhof zu den drei größten Friedhöfen Deutschlands — vergleichbare Anlagen finden sich in Hamburg-Ohlsdorf und München-Waldfriedhof"
Problem: Falsch. Top-3 sind Ohlsdorf (~389 ha), Stahnsdorf (~206 ha), München-Waldfriedhof (~169 ha). Senne mit 98 ha ist nicht Top-3, eher Top-10. Vergleich mit zwei Anlagen stützt "drei" nicht logisch.
Fix: Ersetzen durch "einer der größten Waldfriedhöfe Deutschlands — vergleichbar in Konzept und Größenordnung mit dem Hamburger Ohlsdorfer Friedhof und dem Münchner Waldfriedhof". Keine Rangbehauptung.

Fund 2 — FAQPage-Schema ↔ HTML Reihenfolgen-Mismatch

Wo: JSON-LD FAQPage vs <div class="mr-faq"> DOM
Problem: Schema-Reihenfolge endet mit Q7 "muslimische Grabfelder" → Q8 "Baumbestattungen". HTML hat umgekehrt: erst "Baumbestattungen", dann "muslimische Grabfelder". Google verlangt Schema-DOM-Parität, sonst Rich-Result-Risiko.
Fix: Im HTML die beiden <details>-Blöcke tauschen, sodass Reihenfolge dem Schema entspricht.

Pellafriedhof-Stop 2017 nicht als MAJOR markiert (Primärquelle fehlt, aber nicht offensichtlich falsch — UNSURE).