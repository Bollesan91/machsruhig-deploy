Claude hat geantwortet: Diff-Check gegen v1-GAPs:
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/stuttgart/v2-from-chat-A.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/stuttgart/v2-from-chat-A.html

Diff-Check gegen v1-GAPs:

§-Verweise BestattG BW → umgesetzt (§§ 6, 13, 31, 37, 39 genannt mit Zuordnung)
Ruhezeit ohne Primärquelle → teilweise (§ 6 BestattG BW genannt, Satzungsstelle weiter unspezifisch)
Gebührentabelle ohne §-Verortung → kosmetisch umgesetzt (Spalte „Satzungsstelle" hinzugefügt, aber überall identischer Inhalt „Gebührensatzung 2024, Tarifteil" — kein echter §-Verweis; UNSURE-Kommentar bestätigt das)
Kostenspanne ohne zweite Quelle → umgesetzt (Stiftung Warentest + Aeternitas + Bundeskorridor 7.000–8.000 €)
Pragfriedhof-Zahlen ohne Quelle → teilweise (Formulierung „Nach Angaben des Garten-, Friedhofs- und Forstamts…" — keine spezifische URL/PDF-Stelle)
Hauptfriedhof Steinhaldenfeld zu dünn → teilweise (zweiter Absatz ausgebaut, Mahnmal-Kontext Luftangriffe ergänzt, aber weiterhin keine prominenten Bestatteten, kein Architekt — UNSURE-Kommentar bestätigt fehlende Recherche)
UNSURE-Kommentar Hölderlin → umgesetzt (Hoppenlau-Formulierung sauber, Tübingen-Grab erwähnt, UNSURE entfernt) — ABER: zwei neue UNSURE-Kommentare im Code (Hauptfriedhof-Architekt + Gebührensatzung-Tarifstellen + Kostenstudie-Quelle)
Schema.org-Inkonsistenzen → umgesetzt (Waldfriedhof Schema „1913 angelegt, 5. August 1914 eröffnet", Pragfriedhof „errichtet 1905–1907")
Wortzahl → umgesetzt (von ~1.500 auf grob ~2.300 Wörter)
FriedWald/RuheForst-Standorte → umgesetzt (Schurwald 15 km, Schönbuch konkret)
Bestatter-Sektion ohne lokalen Anker → teilweise (Bestatterverband BW e. V. genannt, „dreistellige Zahl" — aber weiter keine konkreten Stuttgarter Innungs-Adressen)
Cross-Links Nachbar-Städte → umgesetzt (eigene Sektion „Region Stuttgart" mit Esslingen, Ludwigsburg, Tübingen, Reutlingen, Heilbronn, Karlsruhe)
Lokal-kulturelle Tradition → umgesetzt (neue Sektion „Konfessionelle Prägung Stuttgarts", inhaltlich substantiell)
OG-Image generisch → umgesetzt (/assets/og/bestatter-stuttgart.png + og:image:alt)
Floskel „in besonderer Weise das 20. Jahrhundert spiegeln" → umgesetzt (zu „das 20. Jahrhundert konzentriert zeigen" + konkreter Mahnmal-Kontext umformuliert)

11 von 15 voll umgesetzt, 4 teilweise. Spürbarer Substanz-Gewinn. Trotzdem nicht in den 85+ Bereich, weil drei verbleibende Lücken den Kern „Primärquellen-Verortung" treffen.

SCORE: 83%

GAP:

Drei UNSURE-Kommentare stehen weiter im ausgelieferten Code. Hauptfriedhof-Architekt 1918 (Friedhöfe-Sektion, vor </p>), Gebührensatzung-Tarifstellen-Zuordnung (Kosten-Sektion), Lokal-Kostenstudie Stuttgart (Kosten-Sektion). UNSURE-Marker gehören weder in eine Page mit Score-85-Anspruch noch in einen Go-Live-Kandidaten. Entweder Recherche nachziehen oder die unsichere Formulierung kommentarlos stehen lassen.
Gebührentabelle: Spalte „Satzungsstelle" ist kosmetisch, nicht inhaltlich. Alle 9 Zellen tragen identischen Text „Gebührensatzung 2024, Tarifteil". Das ist kein §- oder Anlagenverweis, sondern eine Wiederholung der Tabellen-Überschrift. v1-GAP-Punkt 3 ist damit formal adressiert, inhaltlich nicht. Erwartete Auflösung: § X Abs. Y oder „Anlage Tarif, Pos. Z" pro Zeile aus dem PDF (Seite 3–7 der Stuttgarter Gebührensatzung).
Hauptfriedhof Steinhaldenfeld: keine prominenten Bestatteten. Pragfriedhof nennt 5 (Mörike, Zeppelin, Sutter, Rümelin, Pfeiffer), Waldfriedhof 8 (Heuss, Bosch, Schlemmer, Leonhardt, Klett, Bauknecht, Hirth-Familie), Hoppenlau 3 (Hauff, Schwab, Uhland) — Hauptfriedhof: 0. Stuttgart-Bad Cannstatt hat seit 1918 Industrielle, Politiker, Künstler beerdigt; mindestens 2–3 Namen mit Lebensdaten sind recherchierbar.
Pragfriedhof-Zahlen weiter ohne konkrete Quellenstelle. „21 Hektar, 29.000 Grabstellen, drittgrößte Fläche, größte Belegung" — Formulierung „Nach Angaben des Garten-, Friedhofs- und Forstamts und übereinstimmenden Darstellungen der Stadtgeschichte" ist eine Generalformel, keine Verortung. Für eine Score-85-Page Pflicht: konkrete PDF/URL der Friedhofsstatistik der Stadt Stuttgart oder Wegfall der Hektar-/Stellen-Zahlen.
Lokal-Kostenstudie nur Bestatter-Vergleichsportal. Trotz hinzugefügter Bundes-Quellen (Stiftung Warentest, Aeternitas) bleibt der Stuttgart-spezifische Korridor 3.300–11.400 € / 6.570 € unverändert auf einer einzigen kommerziellen Quelle (bestattungen-meister.de) gestützt. UNSURE-Kommentar im Code bestätigt das. Verbraucherzentrale BW könnte hier eine zweite Quelle liefern; sie ist im Quellenblock bereits gelistet, im Fließtext bei der Kostenaussage aber nicht referenziert.
Quellenblock-Schwäche: drei Quellen ohne tiefen Link. Stuttgarter Nachrichten, Stuttgarter Zeitung, Stiftung Warentest zeigen jetzt nur noch auf die Domain-Roots (stuttgarter-nachrichten.de/, stuttgarter-zeitung.de/, test.de). v1 hatte bei zwei dieser Quellen Deep-Links (/inhalt.pragfriedhof-stuttgart-150-jahre.html, /thema/Waldfriedhof). Rückbau ist eine Regression gegenüber v1.
Innungs-/Verbandsadressen Stuttgart unscharf. „Bestatterverband Baden-Württemberg e. V." wird genannt, aber ohne Adresse, ohne Mitgliederzahl, ohne URL. „Verband unabhängiger Bestatter (VuB) Baden-Württemberg" ebenso. Verlinkung auf BDB.de hilft nur bedingt — der BW-Landesverband hat eigenen Auftritt.
„Drei der vier Hauptfriedhöfe werden interreligiös genutzt" — Aussage nicht durchgehend belegbar. Konfessionelle-Prägung-Sektion endet mit dieser Behauptung. Pragfriedhof (russisch-orthodoxe Kirche) und Hauptfriedhof (muslimisch + armenisch) sind klar belegt. Waldfriedhof Degerloch wird im Text als interreligiös an keiner Stelle ausgewiesen — entweder Hinweis im Waldfriedhof-Absatz ergänzen oder Zahl auf „zwei" korrigieren.
§ 13 BestattG BW als Rechtsgrundlage Leichenschau — Paragraph prüfen. Die Aussage „Rechtsgrundlage ist § 13 BestattG BW" steht ohne Verlinkung auf den Volltext. Für eine §-zitierende Page erwartbar: Direktlink auf landesrecht-bw.de mit Anker zum §, oder mindestens § im Quellen-Block separat aufgeführt. Dasselbe gilt für die § 31 / § 37 / § 39 / § 6 BestattG BW — alle namentlich zitiert, keiner einzeln verlinkt.




