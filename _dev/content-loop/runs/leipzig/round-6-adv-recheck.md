Ich lade die drei Dateien parallel und prüfe den MUST-FIX-Status.

Fetching site
Web durchsucht

SCORE: 87/100

FUNDE:

MUST-FIX-Status v2 → v3 (alle drei adressiert):

MUST-FIX 1 (§§ SächsBestG): ERLEDIGT. § 18 (Bestattungsfristen: 10 Tage Erde / 6 Wochen Einäscherung) und § 19 (Sargpflicht, Friedhofszwang, Religions-Ausnahme nach Abs. 2) sind im Fließtext der Recht-Sektion zitiert, beide mit direktem Revosax-Deeplink. Zusätzlich in der „Was zu tun ist"-Sektion und im FAQ-Block referenziert. Sauber.
MUST-FIX 2 (Leipzig-Kosten): ERLEDIGT. Tabelle mit 6 Zeilen und konkreten €-Spannen (Reihengrab 800–1.200 €, Wahlgrab 2.500–4.000 €, Urnenreihengrab 400–800 €, Urnenwahlgrab 1.200–2.200 €, Anonym 200–500 €, Beisetzung 300–700 €). Direktlink auf /satzungen-und-gebuehren ist gesetzt — nicht mehr nur die Startseite.
MUST-FIX 3 („Goethe-Anekdotenfeld"-H3): ERLEDIGT. H3 heißt jetzt „Alter Johannisfriedhof — Bach, Gellert und die Goethe-Zeit". Unbelegte Anekdote ist als „in den herangezogenen Primärquellen aber nicht eindeutig belegt; sie sind hier deshalb nicht aufgenommen" sauber abgetrennt. Vertrauensbruch in Headline-Position ist weg.

Neue Schwächen v3 (3 substantielle, wie Briefing verlangt):

SCHWÄCHE 1 (Quelle Stiftung-Warentest-Spanne 7.000–8.000 €): Zweimal im Text behauptet („Erhebungen von Stiftung Warentest", „empfiehlt Stiftung Warentest mindestens drei…"), aber im Quellenblock erscheint Stiftung Warentest gar nicht. Für eine YMYL-Page eine harte Aussage mit Geld-Größenordnung ohne nachvollziehbare Quelle — Halluzinations-Verdacht-Kategorie. Fix: Entweder konkrete test.de-URL/Studientitel/Jahr im Quellenblock ergänzen oder die Spanne entschärfen („nach üblichen Branchenerhebungen").
SCHWÄCHE 2 (PLZ-Sprung Ostfriedhof unverifiziert): Schema sagt 04318 (Anger-Crottendorf). Adv-v2 hatte explizit notiert, dass v1 04315 hatte und „korrekt für Anger-Crottendorf ist 04318? — prüfen". v3 hat den Wert übernommen, aber nirgendwo ist die Prüfung dokumentiert. Anger-Crottendorf liegt tatsächlich im 04318-Bereich — passt — aber die Adresse im Schema ist unvollständig (keine streetAddress, anders als beim Südfriedhof mit „Friedhofsweg 3"). Fix: streetAddress für Ost-, Nord- und Alt-Johannisfriedhof im Schema vervollständigen oder konsistent weglassen — aktuell nur Südfriedhof voll, Rest halbgar.
SCHWÄCHE 3 (Wortzahl & inhaltliche Lücke „Bestattete": Wortzahl liegt nach grober Schätzung bei ~1.950–2.050 — am unteren Rand des in Runde 1 geforderten Korridors 2.000–2.500. Inhaltlich: Adv-v2 hatte Max Klinger und Karl Friedrich Zöllner als „fehlt komplett" markiert — v3 hat das nicht nachgezogen. Klinger ist auf dem Südfriedhof tatsächlich nicht (Großjena), aber das hätte man kurz negativ abräumen können. Beim Nordfriedhof steht weiterhin „keine genaue Liste prominenter Bestatteter wird vom Friedhofsträger zentral veröffentlicht" — das wirkt nach zwei Reviewer-Runden eher wie Verzicht als wie Recherche. Fix: Eine konkrete Quelle (Stadtarchiv Leipzig, Friedhofsführer Frank Schmidt o.ä.) als Beleg-Anker und 1–2 konkrete Namen Nordfriedhof oder explizite Klärung „Stadtarchiv führt keine veröffentlichte Liste, Anfrage individuell".

Strukturell positiv (nicht gezählt): FAQ-Schema 7 Fragen synchron mit HTML, Schema-@graph mit WebPage/Article/City/Place/FAQ/BreadcrumbList vollständig, OG-Image/Author/Publisher gesetzt, Cross-Links zu Sachsen/Dresden/Chemnitz vorhanden, dateModified aktuell.

MUST-FIX vor Deploy: nein.

Begründung: Alle drei MUST-FIX aus Adv-v2 sind sauber adressiert. Die drei neuen Funde sind Verbesserungen, kein einziger erreicht „Trust-Killer"- oder „YMYL-Lücke"-Niveau wie die v2-Punkte. SCHWÄCHE 1 (Stiftung-Warentest-Quelle) ist der härteste — empfohlen als Pre-Deploy-Quick-Fix (5 Min Quellenblock-Ergänzung), aber kein Blocker. Page ist deploy-fähig.