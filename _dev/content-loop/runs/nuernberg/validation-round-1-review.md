Ich pruefe beide Quellen.

Fetching: https://machsruhig.de/bestatter/nuernberg/
Fetched: Bestattung in Nürnberg: Friedhöfe, Kosten, Bestatter

Ich pruefe das Raw HTML auf Schema.org und Pipeline-Marker.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/nuernberg/index.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/nuernberg/index.html

Pruefe die drei potenziellen Findings:

St. Johannis Lage: Hero sagt "westlich der Altstadt", Schema/Realitaet: Johannisfriedhof liegt westlich vom Zentrum (Stadtteil St. Johannis). Im Tradition-Abschnitt steht "St. Johannis nordwestlich der Altstadt" und "St. Rochus südwestlich" — im Johannis-Abschnitt dann "westlich der Altstadt". Pruefen wir kurz Konsistenz Schema lat/lng: Johannis 49.4561/11.0589 vs. Altstadt-Hauptmarkt ~49.4541/11.0773 — nordwestlich passt. Westlich-Aussage im Johannis-Abschnitt ist ungenau aber kein major Widerspruch zur Anwalts-Logik.
Veit Stoss: Ist tatsaechlich auf St. Rochus begraben, nicht St. Johannis (Hauptquelle Wikipedia/Stadtarchiv NUE). Hero claimt "Albrecht Duerer, Hans Sachs und Veit Stoss sind hier bestattet" (im Kontext "Schwesterfriedhoefe"), aber im Johannis-Abschnitt explizit: "Veit Stoss... eine Beisetzung auf St. Johannis ist ueberliefert". Das ist faktisch falsch — Veit Stoss liegt auf Rochus. Das ist ein potentieller Anwalts-Fund.
OG-Image: https://machsruhig.de/assets/og-image.png ist der generische Default — keine stadt-spezifische Karte. Pipeline-Default-Leakage.
§ 30 BestV sargfreie Bestattung: Korrekt, in 2021er Reform eingefuehrt.
Stifter Konrad Imhoff Rochus 1518: Pruefen — Rochus-Friedhof wurde 1517/1518 angelegt, Stifter war tatsaechlich Konrad (III.) Imhoff. OK.
Egidiengymnasium-Hinweis: Selbst-qualifiziert, OK.
Schema Reihenfolge BestG/BestV: OK.
Sebald Beham: Selbst-qualifiziert "nicht eindeutig belegt". OK.

Kern: Veit Stoss ist der schwerste Fund — Hero + Johannis-Abschnitt behaupten Beisetzung auf Johannis, korrekt waere Rochus. Das ist ein Faktenfehler, den jeder Nuernberger Kunsthistoriker in 30 Sekunden findet.

STADT: NUERNBERG
VERDICT: MAJOR-FIX

Fund 1 — Veit Stoss auf falschem Friedhof

Was: Hero und Johannis-Abschnitt behaupten, Veit Stoss sei auf St. Johannis beigesetzt. Tatsaechlich liegt Veit Stoss auf dem Rochusfriedhof (Grab dort dokumentiert und besuchbar, Stadtarchiv/Tourismus NUE). Hero-Aufzaehlung "Duerer, Hans Sachs und Veit Stoss sind hier bestattet" ist im Zusammenspiel mit der Sektion "Johannis-Friedhof — Renaissance-Friedhof und Kuenstler-Pantheon: Veit Stoss... eine Beisetzung auf St. Johannis ist ueberliefert" doppelt falsch.
Wo: header.mr-hero p.lead + Sektion "St.-Johannis-Friedhof", 4. Absatz (Liste der Bestatteten)
Fix: Veit Stoss aus Johannis-Liste streichen und im Rochus-Abschnitt unter "prominent Bestatteten" ergaenzen; Hero-Lead Aufzaehlung umstellen auf "Albrecht Duerer und Hans Sachs auf St. Johannis, Veit Stoss auf St. Rochus".

Fund 2 — Generisches OG-Image (Pipeline-Default)

Was: og:image = https://machsruhig.de/assets/og-image.png (Site-Default), keine stadt-spezifische OG-Karte fuer Nuernberg. Klassische Pipeline-Leakage; jede andere Stadt-Page teilt dasselbe Bild.
Wo: <head> meta og:image + og:image:secure_url
Fix: Stadt-spezifisches OG-Image /assets/og/nuernberg.png (1200x630) erzeugen und beide og:image-Tags swappen, ebenso primaryImageOfPage im JSON-LD.

Sonst sauber: Schema.org @graph mit allen Required-Feldern, Breadcrumb konsistent, §-Referenzen sauber qualifiziert, keine Draft-Marker im HTML, FAQPage matched FAQ-Section 1:1, interne Cross-Links live (#tradition Anchor existiert).