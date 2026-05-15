Ich hole mir die drei Dateien.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

Jetzt die adversariale Bewertung von v2. Ich gehe Briefing-streng durch — keine Sycophancy, drei substantielle Schwächen.

Wortzahl-Check v2: Lead + Intro + Bestattungsrecht + Friedhöfe + Kosten + Todesfall + Bestatter ≈ 1.900–2.000 Fließtext, mit FAQ/Keyfacts ≈ 2.400. Korridor ist damit OK.

Round-2-MUST-FIX-Abgleich:

Oviedo: durchgängig „Oviedo" — ✓ behoben
UNSURE-Marker: nicht mehr im HTML — ✓
Gebühren: jetzt sauber als „indikativ memovida.de Frühjahr 2024" gekennzeichnet — ✓
Sargpflicht-Keyfact: präzisiert — ✓
Stiftung-Warentest-Zahl: ersetzt durch Aeternitas-Spanne — ✓
Schritt-für-Schritt: jetzt <ol> mit nummerierten Steps — ✓
§-Zuordnung: §§ 13–15 differenziert — ✓

Aber: drei harte Schwächen bleiben, plus Neufunde.

SCORE: 79/100

FUNDE:

SCHWÄCHE 1 (Halluzinations-Verdacht, hoch): „Wilhelm Engel (1881–1945), Gewerkschafter und NS-Märtyrer" im Hauptfriedhof-Absatz — diese Person mit diesen Eckdaten lässt sich in den verlinkten Quellen (Wikipedia Zentralfriedhof Bochum, Volksbund, Stadt-Bochum-Erinnerungsorte) nicht belegen. Bochumer Gewerkschafter „Wilhelm Engel" mit Sterbedatum 1945 ist kein gängiger Erinnerungsort. Husemann ist solide belegt — Engel wirkt wie ergänzte Plausibilitäts-Füllung. Bei YMYL/NS-Erinnerungskultur ist eine nicht belegbare Personenangabe Deploy-Blocker. Verbesserung: Engel komplett streichen oder gegen Stadt-Bochum-Erinnerungsorte-Verzeichnis (steht in Quellen) verifizieren, sonst nur Husemann nennen plus „weitere Widerstandsgräber im Feld EG 6" ohne Namensnennung.
SCHWÄCHE 2 (Halluzinations-Verdacht + Quellen-Lücke): „Trauerhalle Ost im Brutalismus-Stil 1973/74 nach Plänen Ferdinand Keilmanns errichtet" — die Datierung 1973/74 und die Architekten-Zuschreibung „Ferdinand Keilmann" sind spezifisch genug, dass sie eine Primärquelle bräuchten. In der zitierten Wikipedia steht Keilmann nicht als Architekt der Ost-Trauerhalle (bzw. ist mehrdeutig). Zudem: Das Fritz-Bauer-Forum sitzt laut Eigenangaben nicht auf dem Gelände der ehemaligen Ost-Trauerhalle, sondern in einem umgebauten Krematoriums-/Verwaltungsbau — Aussage ist sachlich heikel. Verbesserung: Architekten-Name und Stilbezeichnung entfernen, nur „1970er-Jahre" und „heutige Nutzung Fritz-Bauer-Forum (verifizieren über fritz-bauer-forum.de)" — oder ganz raus.
SCHWÄCHE 3 (Generischer Satz + Floskel, Bestatter-Sektion): Die Bestatter-Sektion ist trotz Round-2-MUST-FIX immer noch zu wenig Bochum. „Alteingesessene Familienbetriebe — viele davon Mitglied der Bestatter-Innung Westfalen-Lippe" + die fünf Qualitätsindikatoren-Bullets sind 1:1 auf Dortmund/Essen/Köln übertragbar. Der versprochene Bochum-Marker fehlt: weder konkrete Innungs-Bochumer-Betriebe (oder Hinweis „Innungsverzeichnis"-Link mit PLZ-Filter), noch Trauerhallen-Liste mit Adressen (Große/Kleine TH Freigrafendamm-Adressen fehlen), noch die in Round 2 explizit geforderten Bergmannsbestattungs-Bezüge in der Bestattersektion (nicht im Intro). Der eine Bullet „Knappen-Begleitung" reicht nicht — das ist Lippenbekenntnis. Verbesserung: konkrete Bestatter-Innung-Westfalen-Lippe-Suchlink mit Bochum-PLZ einbauen (44787/44789/44791/44793/44795/44797/44799/44801/44803/44805/44807/44809), Trauerhallen-Adressen plus Kapazitäten ergänzen, ein eigener Mini-Absatz „Bergmannsbestattung in Bochum" mit Knappenverein-Kontaktebene (Knappenverein Bochum / IGBCE).
NEBEN-FUND (kein Score-Killer, aber notieren): § 8 BestG NRW — die Reihenfolge „Ehegatten → volljährige Kinder → Eltern → Großeltern → Geschwister → Enkel" ist gegen den Volltext zu prüfen. In NRW-Praxis ist die Reihenfolge: Ehegatte/Lebenspartner → volljährige Kinder → Eltern → Großeltern → Geschwister → Enkel — sieht passend aus, aber „Großeltern vor Geschwistern vor Enkeln" ist die Reihenfolge nach § 8 Abs. 1 BestG NRW. Wenn das gegen Volltext recht.NRW abgeglichen wurde: OK. Wenn nicht: 5min-Check vor Deploy.
NEBEN-FUND (FAQ-Entdopplung nur teilweise umgesetzt): Round-2-MUST-FIX forderte „mind. 3 der 7 FAQ-Antworten Mehrwert über Body hinaus". v2 hat marginal angereichert (Telefonnummer in Hauptfriedhof-FAQ, Adresse Technisches Rathaus in Gebühren-FAQ), aber 4 von 7 sind weiterhin ≥80% Wortgleich mit Body-Abschnitten. Reicht für Schema.org, nicht für User-Mehrwert.
NEBEN-FUND (OG-Image): Round-2-Hinweis OG-Image generisch — nicht adressiert in v2. /assets/og-image.png weiterhin der Default. Für eine als „Gold" gedachte Page Pflicht vor Deploy.

MUST-FIX vor Deploy: JA.

Begründung: Schwäche 1 (Wilhelm Engel) und Schwäche 2 (Keilmann 1973/74 + Fritz-Bauer-Forum-Verortung) sind nicht-verifizierte, sachlich-spezifische Behauptungen auf einer YMYL-Page im sensiblen NS-/Erinnerungskontext. Das ist die Sorte Detail, die ein Bochumer Lokaljournalist oder Stadtarchiv-Mitarbeiter in 2 Minuten als falsch identifiziert — Reputationsrisiko größer als der Content-Gewinn. Entweder Primärquelle (Stadt Bochum Erinnerungsorte-Verzeichnis steht ja in Quellenliste — heißt der Check ist machbar) oder ersatzlos streichen. Schwäche 3 ist nicht Deploy-Blocker, aber Page wird ohne Lokalisierung der Bestatter-Sektion nie über 85 kommen.

Score 79 reflektiert: substantieller Sprung von 68 (Round 2 hat viel ausgeräumt), aber zwei harte Halluzinations-Verdachte ziehen ~6 Punkte, generische Bestatter-Sektion ~3 Punkte, FAQ-Mehrwert/OG zusammen ~2 Punkte.