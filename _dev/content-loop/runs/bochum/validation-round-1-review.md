Ich übernehme die Reviewer-Rolle. Lade beide Quellen.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/bochum/index.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/bochum/index.html

Ich gehe das HTML systematisch durch und prüfe Fakten, Struktur, Schema und Cross-Links.

Auffälligkeiten gefunden:

Oviedo-Partnerstadt-Claim: Die Page behauptet, der "Oviedo-Ring" sei nach der Bochumer Partnerstadt Oviedo benannt. Bochumer Partnerstadt ist Oviedo (Spanien) — das stimmt. Aber: "vormals Sheffield-Ring"? Sheffield ist ebenfalls Bochumer Partnerstadt. Plausibel, aber ich sollte verifizieren — riskanter Faktencheck-Punkt.
PLZ-Block: "44787 — Bochum-Innenstadt", aber die Postleitzahlen 44787, 44789–44799 — die Klassifikation "44789–44799 Bochum-Süd" ist nicht korrekt. 44791, 44793 sind z.B. Innenstadt-/Hamme-/Hofstede-Bereich. Das ist eine Vereinfachung, die ein Konkurrent angreifen könnte, aber im "Toleranzraum" für Übersicht.
Schema.org Article fehlt image-Feld: Das Article-Objekt hat headline, author, publisher, datePublished, dateModified, mainEntityOfPage — aber kein image-Feld. Google verlangt für Article Schema das image-Property als required (sonst Rich-Results-Warning).
Nav-Link "Bestatter finden" zeigt auf /bestatter/muenchen/ — auf einer Bochum-Page ein Cross-Link zu München als generischer "Bestatter finden"-Link wirkt komisch, aber kein Bruch.
Footer Copyright "2024–2026" + Stand "15. Mai 2026" — konsistent.
§ 8 Reihenfolge: Ehegatte → Kinder → Eltern → Großeltern → Geschwister → Enkelkinder. Das entspricht BestG NRW §8 Abs. 1 — korrekt.
Hauptfriedhof eröffnet 18. April 1935 — konsistent über Keyfacts, Schema, Fließtext.
Lead behauptet "eines der wenigen geschlossen erhaltenen Beispiele nationalsozialistischer Friedhofsarchitektur im Ruhrgebiet" — starke Behauptung, wird aber im Body mit Denkmalliste 1989 untermauert. Verteidigbar.

Der Hauptfund ist Punkt 3 (Schema.org Article fehlt image). Das ist konkret, ein Konkurrent/SEO-Audit findet das in Minuten. Plus zwei weitere klare Schwächen prüfen — der Sheffield-Ring-Claim ist verifizierbar.

Web durchsucht
Web durchsucht

Wichtiger Fund: Die Umbenennung von Sheffield-Ring → Oviedo-Ring wurde 2022 beschlossen (für den südlichen Teil), und Wikipedia/Industriekultur bestätigen "Sheffield-Ring (heute Oviedo-Ring)". Der Claim auf der Page stimmt also. 
Wikipedia

ABER: Der PLZ-Block ist falsch. Die Page sagt "44787 — Bochum-Innenstadt" — das stimmt. Aber sie listet "44789–44799 Bochum-Süd, Wiemelhausen, Weitmar". Tatsächlich existiert in Bochum keine durchgängige PLZ-Reihe 44789–44799. Bochums PLZ sind 44787-44894 verstreut. Z.B. 44791 = Altenbochum/Laer (nicht Süd). Das ist eine geographische Vereinfachung, die ein Bestatter sofort sieht — aber unter "Toleranz für Übersicht" eingeordnet, ist es Major-Risiko für eine Bestatter-Page.

Lass mich noch ein letztes kritisches Element prüfen: das Schema.org Article ohne image Property.

Web durchsucht
Web durchsucht

Bestätigt: Google verlangt für Article Schema die Properties headline, image, datePublished, author und publisher — siehe Google Developer Docs und mehrere Validatoren. Die Bochum-Page hat im Article-Objekt kein image, was im Rich Results Test einen Error wirft.

Außerdem fehlt im publisher das logo als ImageObject — Google Docs sind hier strikt.

Ich habe genug. Finale Review:

STADT: BOCHUM VERDICT: MAJOR-FIX

1) Schema.org Article: image und Publisher-Logo fehlen

Was: Im JSON-LD @graph hat das Article-Objekt kein image-Property und der publisher ist nur {name} ohne logo (ImageObject). Beides ist von Google für Article-Rich-Results als required dokumentiert — Rich Results Test wirft Error, Article-Karte wird unterdrückt.
Wo: <script type="application/ld+json"> → @graph[5] (Article-Knoten)
Fix: "image":"https://machsruhig.de/assets/og-bochum.png" und "publisher":{"@type":"Organization","name":"machsruhig.de","logo":{"@type":"ImageObject","url":"https://machsruhig.de/assets/logo.png"}} ergänzen.

2) PLZ-Block faktisch ungenau / irreführend

Was: Auflistung "44789–44799 — Bochum-Süd, Wiemelhausen, Weitmar" suggeriert einen durchgängigen Block mit Süd-Zuordnung. Real verteilen sich diese PLZ über Altenbochum (44791), Laer, Querenburg etc. — keine "Süd"-Reihe. "44801–44809 Norden und Osten" mischt ebenfalls Stadtteile aus mehreren Bezirken. Ein Bestatter aus 44791 (Altenbochum, Hauptfriedhof-Stadtteil!) findet sich nicht im Süd-Block wieder.
Wo: Sektion "Bestatter und Beratung in Bochum" → <ul> mit PLZ-Bereichen
Fix: PLZ-Bereiche als "Stadtgebiet Bochum: 44787–44809 (Kernstadt mit allen Stadtbezirken außer Wattenscheid), 44866–44869 (Wattenscheid)" zusammenfassen, ohne Stadtteil-Zuordnung pro Range.

3) Nav-Link "Bestatter finden" zeigt auf München

Was: Auf der Bochum-Seite verweist der Nav-Link „Bestatter finden" auf /bestatter/muenchen/. Auf einer NRW-Stadtseite ein Cross-Link nach München als Default ist UX-Bruch und SEO-Signal-Streuung (Topical Inconsistency).
Wo: <nav class="mr-nav"> → letzter Link in .mr-nav-links
Fix: Auf ein Stadt-übergreifendes Verzeichnis /bestatter/ linken oder auf der aktuellen Stadt-Page den Link ausblenden.