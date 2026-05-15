Ich hole v5 und prüfe systematisch — besonders die UNSURE-Pipeline-Hygiene.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/hannover/v5-final.html

v5 vollständig. Jetzt die kritischen Checks systematisch.

Pipeline-Hygiene grep: <!-- UNSURE im Volltext durchsuchen — keine Treffer. Auch keine <!-- TODO, <!-- FIXME, <!-- NOTE Kommentare im Source. HTML ist sauber. ✓

Kube-Lebensdaten: v5 nennt nur „Stadtgartendirektor Hermann Kube" ohne Lebensdaten — die fragwürdigen 1874–1953 sind raus. ✓

Stiftung Warentest: Jetzt Deep-Link (test.de/Bestatter-Was-eine-Bestattung-kostet-...) + redaktioneller Disclaimer („Diese 2023er Stiftung-Warentest-Erhebung ist der bislang öffentlich verfügbare Vergleichsstand; neuere flächendeckende Vergleichszahlen liegen redaktionell derzeit nicht vor"). Erwähnungen: Kostenabschnitt-Body, Hinweisbox-Bestatterauswahl (indirekt), FAQ, Schema.org FAQ — 4 Stellen, davon nur eine mit Deep-Link, die anderen ohne Link. Das ist marginal verbessert aber nicht ganz behoben — die FAQ-Antwort und Schema.org-FAQ-Antwort verwenden „Finanztest 11/2023" weiterhin ohne URL. Streng genommen sollte der Link überall mitlaufen oder die Wiederholung gekürzt werden.

Friedhofszwang §: v5 sagt nicht mehr „§ 8 BestattG" oder andere konkrete Nummer für den Friedhofszwang — formuliert allgemein „Nach niedersächsischem Landesrecht dürfen Verstorbene grundsätzlich nur auf einem öffentlichen Friedhof… bestattet werden. Die Trägerschaft… ist in § 13 BestattG Niedersachsen auf Gemeinden…" Das ist eine andere Aussage als der Friedhofszwang selbst — § 13 NI BestattG regelt tatsächlich die Trägerschaft (Gemeinden, Kirchen, Religionsgemeinschaften ÖR), nicht direkt den Friedhofszwang. Die Aussage bleibt streng genommen leicht schief: „Friedhofszwang" wird behauptet, aber der genannte § betrifft die Trägerschaft. Niedersachsen regelt den Friedhofszwang faktisch über die Verbindung von § 13 (Trägerschaft) + § 8 BestattG (Beisetzungspflicht auf Friedhöfen) — die fehlende Präzisierung ist eine kleine Schwachstelle.

Neue Schwächen — systematische Suche:

Engesohde 22 ha vs Wikipedia 21,7 ha: v5 schreibt offen „rund 22 Hektar (Stadt Hannover; Wikipedia nennt 21,7 ha)" — transparenter Quellenkonflikt offen kommuniziert. OK.
Lahe 1968 / 37 ha: Wikipedia-Verlinkung als Quelle. Wikipedia ist als Sekundärquelle akzeptabel, aber für eine YMYL-Stadtseite suboptimal — keine offizielle Stadt-Quelle für die Lahe-Stammdaten. Kleine Schwäche.
Seelhorst 1924 eröffnet: v5 sagt „ab 1919 geplant und 1924 eröffnet". Schema.org-Beschreibung sagt nur „ab 1919 geplant" — Schema und Body stimmen nicht ganz überein (Schema fehlt das Eröffnungsjahr). Marginal.
Ricklingen-Eröffnungsjahr fehlt komplett: „in der Nachkriegszeit eröffnet" — keine konkrete Jahresangabe für Ricklingen. Bewusste Vagheit oder Recherche-Lücke? In einer Stadt-Seite, die Eröffnungsjahre für Gartenfriedhof/Engesohde/Seelhorst/Lahe präzise nennt, fällt das auf. Kleine inhaltliche Lücke.
Anonyme Gemeinschaftsgrabanlage Seelhorst „eine der frühen … 1970er/1980er Jahre": ohne Beleg, „frühe" ist eine Wertung. Quellengrund: nicht offensichtlich.
Charlotte Kestner Lebensdaten 1753–1828: Wikipedia-Standardwissen, ausreichend belegbar.
G.L.F. Laves 1788–1864: Standardwissen, OK.
SCORE: 87/100
v4-MUST-FIX-Status (3 Punkte)
Punkt	Status
Kube-Lebensdaten 1874–1953	✅ BEHOBEN — Lebensdaten ersatzlos entfernt, nur Funktion „Stadtgartendirektor" bleibt
Stiftung Warentest 11/2023	⚠️ TEILBEHOBEN — Deep-Link auf test.de jetzt vorhanden + Disclaimer zur Aktualität ergänzt, ABER Erwähnung weiterhin 4×: Body, Bestatterauswahl-Paragraph, FAQ-HTML, Schema.org-FAQ. Deep-Link nur im Body. FAQ-Antworten ohne URL → für RAG-Indexer Risiko
UNSURE-Kommentare + Friedhofszwang §	✅ BEHOBEN (UNSURE/TODO/FIXME-Kommentare: 0 Treffer im HTML, Pipeline-Hygiene sauber) — Friedhofszwang nur ⚠️ TEILBEHOBEN: Aussage steht, zitierter § 13 BestattG regelt jedoch Trägerschaft, nicht Friedhofszwang selbst (formal-juristische Unschärfe)
NEUE Schwächen (max 2)
Stadtfriedhof Ricklingen ohne konkretes Eröffnungsjahr — alle anderen vier Hauptfriedhöfe nennen ein präzises Jahr (1741 / 1864 / 1924 / 1968), Ricklingen nur „in der Nachkriegszeit". Inkonsistente Recherche-Tiefe; entweder Jahr nachtragen oder Vagheit konsistent begründen.
Lahe-Stammdaten primär über Wikipedia belegt — 1968/37 ha hängen am Wikipedia-Link, keine offizielle Stadt-Hannover-Quelle. Für eine YMYL-Stadtseite suboptimal; mindestens Friedhofs-Microsite der Stadt als Co-Beleg ergänzen.
MUST-FIX vor Deploy: NEIN

Die 3 v4-Blocker sind in der Substanz behoben (Kube vollständig, UNSURE-Hygiene vollständig, Warentest Deep-Link vorhanden). Verbleibende Punkte sind Qualitätsstufe nicht Deploy-Blocker. GO mit Empfehlung:

Quick-Win vor Deploy (5 min): Warentest-Link auch in die HTML-FAQ-Antwort und Schema.org-FAQ-Answer übernehmen — eine zusätzliche Verlinkung schließt das Restrisiko ohne strukturelle Änderung.
Empfehlung für nächste Iteration (nicht-blockend): Ricklingen-Jahr recherchieren; Lahe mit Stadt-Hannover-Quelle co-belegen; Friedhofszwang-§ präzisieren (§ 8 oder Trennung Trägerschaft/Bestattungspflicht).

v5 ist eine sauber durchgeführte Korrektur — die Pipeline-Hygiene-Verbesserung (keine UNSURE-Kommentare mehr im Output) ist der wichtigste Fortschritt gegenüber v4.