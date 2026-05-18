Ich übernehme den Review. Erst die beiden Quellen ziehen.

Fetching: https://machsruhig.de/bestatter/krefeld/
Fetched: Bestattung in Krefeld — Friedhöfe, Kosten & Recht

Live-Seite gezogen. Jetzt Raw HTML aus dem GitHub-Repo für Schema/OG/Meta-Tag-Check.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/krefeld/index.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/krefeld/index.html

Beide Quellen vorliegend. Strict-Review:

Schwergewichts-Check:

BestG NRW §13 Fristen ✓ (24h / 10 Tage / 6 Wochen — alle korrekt)
Friedhofssatzung-Datum 18.12.2025 konsistent in allen Sektionen ✓
Adressen (Heideckstraße 127 / Rheinstraße 138 / Ostwall 175) konsistent zwischen Body + Schema + Keyfacts ✓
Schema.org: WebPage, Article, BreadcrumbList, City, Place, Organization, GovernmentOffice, FAQPage — alle Required-Felder gesetzt, @graph wrapper korrekt ✓
OG-Tags vollständig (title/desc/type/url/locale) ✓
Kein OG-Image (akzeptabel, BAR ist "generische OG-Image-Defaults" — hier fehlt komplett, kein default-Leak)
Keine <!-- UNSURE --> oder Babel/JSX-Marker ✓
Cross-Link zu /bestattung-in/nordrhein-westfalen/ vorhanden ✓
Tabellen vollständig, keine leeren Sektionen ✓

Mögliche Probleme prüfen:

Friedhof Hüls — Eröffnet 1862: Die DSGVO-Quelle KBK selbst nennt für den Hülser Friedhof typischerweise 1862. ✓
Krematorium "fünftes in Preußen, erstes im Rheinland": Quelle Stadtarchiv-Link wird zitiert. Akzeptabel.
Uerdingen Stadtrechte 1255: Korrekt (historisch belegt).
Linn eingemeindet 1901: Korrekt.
Hüls eingemeindet 1975: Korrekt (kommunale Neugliederung NRW).
Cornelius de Greiff 1781–1863: Korrekt.
Marianne Rhodius 1814–1902: Korrekt.
Hermann von Beckerath 1801–1870: Korrekt.

Realer Selbstwiderspruch gefunden:

FAQ-Schema (JSON-LD) für "Wo wird in Krefeld der Sterbefall beurkundet?" enthält den Satz "Der Sterbefall muss spätestens am dritten auf den Tod folgenden Werktag gemeldet werden." — diese Aussage steht nur im Schema, nicht im sichtbaren FAQ-Antworttext. Das ist Schema/HTML-Mismatch und wird von Google als manipulativ gewertet (Structured Data Policy: "do not mark up content that is not visible to readers"). Potenzieller Rich-Result-Verlust + Spam-Action-Risiko.

STADT: KREFELD VERDICT: MAJOR-FIX

1. FAQ-Schema enthält Aussage, die im sichtbaren FAQ fehlt

Was: JSON-LD-Antwort zur Standesamt-Frage enthält Satz "Der Sterbefall muss spätestens am dritten auf den Tod folgenden Werktag gemeldet werden." — dieser Satz ist im sichtbaren <details>-Block der gleichen Frage nicht vorhanden. Google-Structured-Data-Policy-Verstoß (invisible markup), riskiert Rich-Result-Entfernung der gesamten FAQ.
Wo: <script type="application/ld+json"> → FAQPage → letzte Question "Wo wird in Krefeld der Sterbefall beurkundet?" vs. <section> mit <h2>Häufige Fragen…</h2> → letztes <details>.
Fix: Im sichtbaren FAQ-Antworttext den Satz "Der Sterbefall muss spätestens am dritten auf den Tod folgenden Werktag gemeldet werden." ergänzen (z. B. nach "Zuständig ist das Standesamt Krefeld…"), damit Schema und HTML 1:1 übereinstimmen.

Sonst sauber. Nach Fix dieses einen Punkts → CLEAN.