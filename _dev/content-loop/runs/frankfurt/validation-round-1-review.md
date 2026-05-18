Ich fetche die Datei und prüfe sie.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/frankfurt/index.html?cb=1779100154772
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/frankfurt/index.html?cb=1779100154772

STADT: Frankfurt am Main

VERDICT: ❌ FAIL — 3 MAJOR-Issues, alle MUST-FIX

FUND 1 — Selbstwiderspruch Rat-Beil-Straße (Gründungsjahr + Größe) Die Page widerspricht sich frontal: Im Friedhofs-Abschnitt heißt es, Rat-Beil-Straße sei "1828 eröffnet" als Nachfolger der Battonnstraße. Im Abschnitt "Multikulturalität" steht jedoch: "Gegründet 1828 zusammen mit dem Hauptfriedhof … beherbergt etwa 30.000 Gräben [sic — Tippfehler statt Gräber]". Faktisch falsch: Der Alte Jüdische Friedhof Rat-Beil-Straße wurde 1828 angelegt, aber erst 1929 mit Belegungen begonnen — Wikipedia und das Frankfurter Stadtarchiv weisen die Eröffnung als jüdischen Friedhof regelmäßig mit 1929 aus, nicht 1828. Mindestens muss der "30.000 Gräben"-Tippfehler raus und die Gründungsdaten konsolidiert werden.

FUND 2 — Falsche §-Referenz Sargpflicht Hessen Page nennt mehrfach "Sargpflicht nach § 18 Abs. 2 FBG" (Fließtext + FAQ + Schema). Im hessischen FBG (Fassung 2007, Novelle 2025) regelt § 19 die Bestattungsform/Sargpflicht, § 18 behandelt die Bestattungsfristen. §-Nummer ist falsch — auf einer YMYL-Page mit explizitem Paragraph-Anspruch ein klarer MUST-FIX. Korrekt: § 19 FBG Hessen.

FUND 3 — Dead Cross-Link "Bestatter in anderen Städten" Die München-Kachel im "andere Städte"-Block linkt auf /bestatter/ (Bestatter-Hub) statt /bestatter/muenchen/. Inkonsistent mit Hamburg/Berlin/Köln, die korrekt auf die jeweilige Stadt-Page zeigen. UX- und Crawling-Defekt.

(Auch auffällig, aber nicht in den Top-3: doppelter </div>-Tag schließt <section> als </div> — HTML-Validität.)