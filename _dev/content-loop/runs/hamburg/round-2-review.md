Claude hat geantwortet: Ich lese erstmal beide Files.

Ich lese erstmal beide Files.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/B-reviewer.md

Briefing verstanden. Jetzt die Page.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/hamburg/v1-from-chat-A.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/hamburg/v1-from-chat-A.html

BRIEFING_OK

SCORE: 72%

GAP:

§-Verweise zum HmbBestG fehlen komplett. Aussagen zu „abgeschaffter 48-Stunden-Mindestbestattungsfrist", „Sargpflicht mit religiöser Ausnahme" und „Höchstfrist" stehen ohne Paragraph-Nummer (§ 9 HmbBestG für Frist, § 13 HmbBestG für Sargpflicht — oder welche auch immer die korrekten sind). Die Seite verweist nur generisch auf die Bundeslandseite. Auch wenn das laut Page-Konzept die Stadt-Seite ist: ein Mindestmaß an §-Anker pro juristischer Aussage muss hier stehen, sonst wirkt jede Rechtsaussage wie Hörensagen.
Mindestruhezeit „25 Jahre auf Ohlsdorf nach dortiger Friedhofssatzung" steht ohne Quelle/Link/§. Die Friedhofssatzung der Hamburger Friedhöfe AöR ist online — direkter Deep-Link fehlt in der Quellenliste (nur die Träger-Startseite ist verlinkt).
Statistiken ohne Stand-Jahr und Primärquelle: „jährlich finden tausende Seebestattungen ab Hamburger Häfen statt" ist eine quantifizierende Aussage ohne Zahl, ohne Jahr, ohne Verweis. Statistisches Amt Nord ist zwar in der Quellenliste, aber keine konkrete Statistik (Sterbefälle Hamburg/Jahr, Anteil Feuerbestattungen, Anteil Seebestattungen) wird benutzt.
Kostenkorridor-Tabelle ohne Quellenanker. Die Zahlen (anonyme Feuerbestattung 1.500–2.500 €, Erdbestattung 6.500–10.000 € etc.) erscheinen aus dem Nichts. Aeternitas, Verbraucherzentrale Hamburg oder Stiftung Warentest müssen pro Zeile (oder mindestens unter der Tabelle) zitierbar sein. Friedhofsgebühren-Satzung der Hamburger Friedhöfe AöR müsste mit konkreten Beträgen verlinkt sein.
Friedhofs-Highlights: Ohlsdorf ist exzellent ausgearbeitet (Cordes, Kapellen, Prominente, Hidden Gems) — Öjendorf und Harburg dagegen bleiben Skizzen. Öjendorf: keine konkrete Architektur, kein Hidden-Gem-Detail, kein Name eines dort Bestatteten, kein Verweis auf den ehemaligen Steinbruch/See-Charakter des Öjendorfer Parks. Harburg: keine Gründungsjahr, keine Fläche, keine konkrete Kapelle benannt, kein Bestatteter. Asymmetrie zu Ohlsdorf ist zu groß.
Diebsteich/Altonaer Friedhof zu knapp und ohne konkreten Anker: kein Gründungsjahr, keine Fläche, keine prominenten Bestatteten genannt (auf dem alten Altonaer Friedhof liegen historisch relevante Persönlichkeiten — die fehlen komplett). „Sepulkrale Stille" ist Floskel.
Jüdische Friedhöfe Hamburgs: der historische Bedeutung wird nicht gerecht. Der Jüdische Friedhof Altona (Königstraße) gehört zu den ältesten und bedeutendsten sephardischen Friedhöfen Nordeuropas und ist auf der UNESCO-Welterbe-Tentativliste / mittlerweile Teil eines Welterbeantrags. Das fehlt vollständig — ein massiver Verlust an Hamburg-Substanz.
Cross-Links zu Stadtteilen / Hamburger Sub-Pages fehlen. „Bestatter in Eppendorf / Altona / Harburg / Wilhelmsburg" wäre der naheliegende Cross-Link-Layer; die Seite verlinkt nur auf Nachbarstädte (Bremen, Lübeck, Kiel, Hannover) und generische Tools.
Nav-Markup-Bug: <a href="/bestatter/muenchen/" class="active">Bestatter finden</a> — der active-Link zeigt auf München statt Hamburg. Footer hat denselben Bug: <a href="/bestatter/muenchen/">Bestatter</a>. Beide Links müssen auf /bestatter/hamburg/ bzw. /bestatter/ zeigen.
Floskeln vereinzelt: „hanseatisch-protestantisches Statement gegen Personenkult", „norddeutsch-protestantische Bescheidenheit", „sepulkrale Stille", „hanseatische See-Identität", „Hafen … vor der Haustür". Einzeln verkraftbar, in Summe für eine 85+-Page zu viel pathetische Eindeckung.
Seebestattung — historische Bedingung lückenhaft: § 28 BestattG-Bund-Vergleich oder Bezug zur Seebestattungs-Erlaubnis (Bundeswasserstraßen, BSH-Genehmigung) fehlt. Die zugelassenen Seebestattungsgebiete vor Helgoland/Norderney werden nicht benannt. Aussage „zugelassenes Seebestattungsgebiet" bleibt vage.
Schmidt-Grabnummer / Fedder-Grabnummer fehlen. Für Pilger-Informationen wären die konkreten Planquadrat-Bezeichnungen auf Ohlsdorf (z. B. Bestattete in Planquadrat AC 18 o. ä.) ein Substanz-Plus. Aktuell bleibt es bei „liegt auf Ohlsdorf".
Trauerfeier-Kapellen Ohlsdorf: „mehrere Kapellen unterschiedlicher Größe" ist generisch. Konkret: Kapellen 1–13 werden im Hidden-Gems-Absatz erwähnt, aber für die Trauerfeier-Planung fehlt die praktische Info, welche Kapellen wie viele Plätze haben oder wie reserviert wird.
Krematorium Ohlsdorf in Keyfacts erwähnt, aber im Fließtext nicht aufgegriffen (Geschichte, Lage, Kapazität, ob konfessionell oder kommunal getragen). Eine Stadt-Page mit Schwerpunkt Feuerbestattung sollte das Krematorium kurz einordnen.
Wortzahl-Schätzung: ~2.100 Wörter im Korridor — passt grundsätzlich, aber die Verteilung ist Ohlsdorf-lastig (geschätzt 40% Ohlsdorf, Rest dünn). Umverteilung nötig: weniger Cordes-Architektur-Doppelung, mehr Öjendorf/Harburg/Altona-Substanz.
„mr-cta-block" im Print-CSS referenziert, aber im DOM nicht vorhanden. Kein Funktions-Bug, aber Indikator für copy-pasten Template ohne Final-Sweep.
Author-Modell inkonsistent: laut Bolles Locked-Decision ist Author „machsruhig Redaktion" + Fachpool-Reviewer. Auf der Page steht nur „Redaktion machsruhig.de" — der Fachpool-Reviewer fehlt als zweite Linie der Verantwortung in der Meta-Box.




