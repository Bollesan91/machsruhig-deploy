Claude hat geantwortet: Ich hole erst Briefing und Page.

Ich hole erst Briefing und Page.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Web durchsucht

BRIEFING_OK.

Jetzt adversarial gelesen — drei substantielle Schwächen, ehrlich:

SCHWÄCHE 1: Paragraphen-Salat im Block „Bestattungsrecht in Stuttgart" — § 37 für Fristen und § 39 für Sargpflicht sind sachlich falsch zugeordnet, und § 31 für die Verfügungsberechtigten existiert in dieser Form ebenfalls nicht im BestattG BW

Die Page zitiert sehr selbstbewusst „§ 37 BestattG BW" für Bestattungsfristen (96 Stunden), „§ 39 BestattG BW" für Sargpflicht/Tuchbestattung und „§ 31 BestattG BW" für die Rangfolge der Bestattungspflichtigen. Das BestattG BW hat aber nur 20 Paragraphen — §§ 31, 37, 39 existieren schlicht nicht. Die Sargpflicht und die Tuchbestattungs-Ausnahme stehen in § 32 BestattV (Bestattungsverordnung), die Bestattungsfristen in § 37 BestattV (nicht im Gesetz), die Bestattungspflichtigen-Rangfolge in § 31 BestattV. Die Stadt-Page verwechselt durchgängig Gesetz und Verordnung — und das auf einer Seite, die ihre USP ausdrücklich auf „paragraphenscharf" und „BestattG BW" stützt (Hero, Meta-Description, Schema.org-Article alle so). Dazu kommt die Ruhezeit: „§ 6 BestattG BW" wird sowohl im Recht-Block als auch in der FAQ zitiert; § 6 BestattG BW regelt aber Leichenschau-Verfahren, nicht Ruhezeiten. Ruhezeit-Bemessung steht in § 5 BestattV. Fix: Sämtliche § im Recht-Block prüfen gegen den tatsächlichen Volltext (Landesrecht-BW.de), durchgängig „BestattG BW" durch „BestattVO BW" ersetzen wo es um Frist/Sarg/Pflichtige/Ruhezeit geht, und einen einzigen klaren Satz zur Trennung Gesetz↔Verordnung einziehen. Solange das nicht stimmt, ist die Page bei Erstkontakt eines Stuttgarter Bestatters oder Friedhofsmitarbeiters fachlich diskreditiert — und genau die sind die Hauptzeugen für die Lead-Akzeptanz.

SCHWÄCHE 2: Die Kostentabelle hat eine durchgehende Pseudo-Belegspalte „Gebührensatzung 2024, Tarifteil" — neunmal identisch, ohne eine einzige präzise Stelle, mit einem HTML-Kommentar der das selbst eingesteht

Die Tabelle „Bestattungskosten in Stuttgart — Gebühren 2025" listet 9 Positionen, jede mit der Spalten-Belegung „Gebührensatzung 2024, Tarifteil" — neunmal wortgleich. Direkt unter der Tabelle steht ein HTML-Kommentar: „UNSURE: ... die exakte §- oder Anlagenstellen-Zuordnung pro Zelle ist im PDF nachzuschlagen. Daher generischer Verweis ‚Gebührensatzung 2024, Tarifteil'; präzisere Stellen werden in Round 4 ergänzt." Das ist Schwäche-8 + Schwäche-1 + Schwäche-12 in Personalunion: Die Spalte existiert nur, um Belegtiefe vorzutäuschen, leistet aber faktisch null Verortung — und die Page weiß das selbst, schiebt es aber auf eine spätere Runde. Gleichzeitig sind die konkreten Eurobeträge (940 / 1.960 / 605 / 1.010 / 92 / 87 / 98) für einen Außenstehenden unprüfbar, weil keine § oder Anlagen-Nummer dabeisteht. Ein adversarialer Faktencheck müsste das ganze PDF durchblättern. Fix: Entweder die Spalte rausnehmen und durch einen einzigen Satz vor der Tabelle ersetzen („Alle Beträge aus Anlage 1 der Friedhofsgebührensatzung 5.12.2024, abrufbar [PDF-Link]"), oder die Spalte einmal sauber befüllen mit echten Anlage-Positionsnummern. Aktuell schafft die Spalte zusätzliche Angriffsfläche, ohne zusätzliche Glaubwürdigkeit zu liefern.

SCHWÄCHE 3: Die „Marktauswertungen lokaler Bestatter"-Zahlen (3.300 / 11.400 / 6.570 €) hängen in der Luft — keine Quelle, kein Portal, keine Stichprobengröße, und der HTML-Kommentar darunter outet sie als Bestatter-Vergleichsportal-Auswertung ohne Verbraucherquelle

Die Page nennt drei sehr konkrete Stuttgart-Zahlen — Untergrenze 3.300 €, Obergrenze 11.400 €, Mittelwert 6.570 € — und nennt sie zweimal (Fließtext + FAQ-Schema + sichtbares FAQ-Accordion). Die Belegformel ist beide Male „nach Marktauswertungen lokaler Bestatter" bzw. „nach Marktwerten" — keine Studie, kein Portal, kein Jahr, keine n. Der HTML-Kommentar darunter sagt offen: „Die Lokalspanne stützt sich auf Bestatter-Vergleichsportal-Auswertung". Das ist exakt Kategorie 1 (Quellen-Lücke) + Kategorie 12 (Halluzinations-Verdacht): ein 6.570-€-Mittelwert auf den Euro ist eine Behauptung, die nach einer veröffentlichten Erhebung klingt, aber keine ist. Außerdem behauptet der Text danach „Stuttgart liegt damit knapp unter dem bundesweiten Standardwert" und vergleicht 6.570 mit „7.000 bis 8.000 Euro" — der Vergleich ist nur stichhaltig, wenn der 6.570er-Wert auch belastbar ist. Fix: Entweder echte Quelle benennen (Bestattungen.de-Statistik, Aeternitas-Marktbericht, Verbraucherzentrale BW — eine der drei muss explizit dahinter) mit Jahr und Methode, oder die Zahlen rausnehmen und nur die Stadt-Gebühren plus den bundesweiten Stiftung-Warentest-Korridor stehen lassen. Eine erfundene Präzision (6.570 €) auf einer Seite, die in der Hero verspricht „§-Verweise aufs BestattG BW" und in der Methodik-Verlinkung Primärquellen-Treue suggeriert, ist die größte Vertrauenslücke der Seite — größer als die §-Fehler, weil sie auch nach dem Lesen unbemerkt bleibt.

EHRLICHE %-ZAHL: 73 %

Begründung in einem Satz: Die Page ist strukturell, narrativ und im Stuttgart-Lokalkolorit (Hoppenlau-Romantik, Pragfriedhof-Russlandbrücke, Heuss/Bosch-Distanz) ausgezeichnet gebaut — aber die juristische Belegtiefe ist auf mehreren Stellen Pseudo-Präzision (falsche §, generische Tabellenbelege, ungesicherte Marktzahlen), und das ist auf einer Page, die ihre USP genau darüber definiert, ein Glaubwürdigkeits-Schnitt unter 85.




