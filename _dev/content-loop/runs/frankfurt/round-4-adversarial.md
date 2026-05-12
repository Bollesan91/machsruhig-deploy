Claude hat geantwortet: Ich lese erst beide Dateien.

Ich lese erst beide Dateien.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/briefings/C-adversarial.md

Briefing verstanden. Jetzt die Page.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/frankfurt/v2-from-chat-A.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/_dev/content-loop/runs/frankfurt/v2-from-chat-A.html

BRIEFING_OK.

Jetzt adversariale Prüfung. Drei Stellen riechen verdächtig — der Hauptfriedhof "1957/58 auf über 70 Hektar erweitert", die Hessen-Novelle "30. September 2025" mit GVBl-Nummer, und die Gebührensätze. Ich verifiziere.

Searching the web
Web durchsucht

Punkt 1 (Hauptfriedhof-Erweiterung) — Page sagt "ursprünglich rund 7 Hektar" und "1957/58 auf über 70 Hektar erweitert". Wikipedia und die offizielle Friedhof-Frankfurt-Seite sagen: ursprünglich 5,6 / ca. 6 Hektar (nicht 7), und die letzte Erweiterung war 1952–1957 (nicht 1957/58). Frankfurt-Lese verwendet zwar "1957/58", aber Wikipedia und die Stadt selbst sind klarer. Außerdem: Page ignoriert die ganze Zwischenexpansion 1845-1912.

Jetzt prüfe ich die FBG-Novelle Hessen 30.09.2025.

Searching the web
Web durchsucht

Novelle 30.09.2025 ist bestätigt — gut. Aber: hessenschau schreibt explizit, dass schon nach altem FBG 2007 die 96-Stunden-Frist verlängert werden konnte (§16 Abs. 1) — Page präsentiert "vorher vier" als hartes Limit, was nicht ganz stimmt, aber das ist eine Nuance. Wichtiger: Page sagt "Sargpflicht nach § 18 Abs. 2 FBG" — ich muss prüfen, ob § 18 wirklich Sargpflicht ist. Im aeternitas-PDF-Auszug oben sehe ich § 18 nicht direkt. Ich prüfe direkt.

Searching the web
Web durchsucht

TREFFER, und es ist groß. § 18 FBG Hessen heißt "Bestattungsfeierlichkeiten" und regelt das Verbot des öffentlichen Ausstellens von Leichen und der Sargöffnung. Die religiöse Ausnahme von der Sargpflicht steht in § 18 Abs. 2 Satz 1 FBG — aber Sargpflicht selbst ist NICHT in § 18 geregelt. Das Mitglieds-Satzungsmuster vom Hessischen Städte- und Gemeindebund sagt sogar explizit: "eine Sargpflicht im Zusammenhang mit der Beförderung der Leiche (§ 15 Abs. ...)" — die Sargpflicht ergibt sich aus § 15 (Beförderung) bzw. § 19 (Erdbestattung), nicht § 18.

Die Page sagt mehrfach: "Sargpflicht nach § 18 Abs. 2 FBG bleibt bestehen" — das ist sachlich verkehrt. § 18 Abs. 2 enthält gerade die Ausnahme, nicht die Pflicht. Klassische Paragraphen-Halluzination.

Drittens prüfe ich die Frankfurter Gebührensätze.

Web durchsucht
Web durchsucht

Gebühren-Korridor 1.596/1.006/789 € ist bestätigt (Pietät-im-Prüfling stützt das). Aber: Page sagt im Quellen-Block "Friedhofs- und Bestattungsgebührenordnung der Stadt Frankfurt am Main (gültig seit 1.1.2025; Amtsblatt Nr. 52 / 155. Jhg. vom 24.12.2024)" — die offizielle PDF nennt "Amtsblatt der Stadt Frankfurt am Main vom 27.12.2022 / Nr. 52, S. 1.760" für die vorige Satzung (2023). Die 2025er Ordnung müsste in einem anderen Amtsblatt verkündet sein. 24.12.2024 / Nr. 52 / 155. Jhg. sieht erfunden aus — das gleiche Nummer-Muster wie die alte. Klassische Quellenfälschung.

Ich habe genug. Drei substantielle Schwächen sind belegt. Wortzahl ist deutlich über 1500 — das ist kein Thema. Adversariales Verdict:

BRIEFING_OK (verspätet — Bestätigung kommt im Verbund mit dem Befund).

SCHWÄCHE 1: Falsche Paragraphen-Zuordnung — "Sargpflicht nach § 18 Abs. 2 FBG" (Hessen-Recht-Sektion, FAQ "Welches Bestattungsrecht...", Spezialitäten "Jüdische Bestattung", Schema-FAQ) — § 18 FBG Hessen heißt "Bestattungsfeierlichkeiten" und verbietet das öffentliche Ausstellen von Leichen sowie die Sargöffnung. § 18 Abs. 2 enthält gerade die *Ausnahme* (sarglose Bestattung aus religiösen Gründen, eingefügt durch Gesetz vom 02.02.2013), nicht die Sargpflicht selbst. Die Sargpflicht ergibt sich aus § 15 (Beförderung) bzw. der Friedhofsordnung der Stadt, der Hessische Städte- und Gemeindebund verweist explizit auf § 15 Abs. 2 FBG. Drei Mal verkehrt zitiert, einmal sogar im FAQ-Schema.org-Markup → bleibt nach Indexierung in Google für immer falsch. **Fix:** Überall "Sargpflicht nach § 15 Abs. 2 FBG; religiöse Ausnahme nach § 18 Abs. 2 Satz 1 FBG" — sauber trennen zwischen Pflicht (§ 15) und Ausnahmenorm (§ 18 Abs. 2).

SCHWÄCHE 2: Quellen-Halluzinations-Verdacht bei der Gebührenordnung — Quellen-Block: "Friedhofs- und Bestattungsgebührenordnung der Stadt Frankfurt am Main (gültig seit 1.1.2025; **Amtsblatt Nr. 52 / 155. Jhg. vom 24.12.2024**)" — Diese Amtsblatt-Angabe ist nicht verifiziert. Die offizielle PDF der Stadt Frankfurt nennt für die *vorige* Satzung "Amtsblatt der Stadt Frankfurt am Main vom 27.12.2022 / Nr. 52, S. 1.760". Das Muster "Nr. 52, 24.12." sieht aus, als sei die Vorgängerangabe auf 2024 hochgerechnet worden, statt im echten Amtsblatt nachzuschlagen. **Fix:** Auf https://frankfurt.de Amtsblatt-Archiv 2024 nachschlagen, korrekte Nummer/Seite eintragen — oder die Detail-Klammer streichen und nur "in Kraft seit 1.1.2025" stehen lassen.

SCHWÄCHE 3: Sachliche Falschangabe zur Hauptfriedhof-Geschichte — Hauptfriedhof-Sektion: "**Ursprünglich rund 7 Hektar groß**, wurde der Friedhof 1957/58 auf über 70 Hektar erweitert" — Beide Zahlen schief. Wikipedia und die offizielle friedhof-frankfurt.de geben die Ursprungsfläche mit **ca. 6 Hektar bzw. 5,6 Hektar** an, nicht 7. Und die Erweiterung war kein einmaliger Sprung 1957/58, sondern eine vierstufige Geschichte (1845–1891 auf 18 ha → 1907–1912 auf 47 ha → 1927/28 auf 57 ha → 1952–1957 auf 70 ha). Die Sprung-Darstellung lässt 130 Jahre Friedhofs-Geschichte verschwinden — und auch die schöne Pointe, dass Ernst May (1928) den schlicht-sachlichen Stil der Erweiterung prägte. **Fix:** Absatz umschreiben: "Ursprünglich rund 6 Hektar groß, wurde der Hauptfriedhof in vier Etappen erweitert: 1891 auf 18 ha, 1912 auf 47 ha, 1928 (unter Ernst May und Max Bromme im Stil des "Neuen Frankfurt") auf 57 ha und 1957 auf die heutigen 70,1 ha — zehnmal die Anfangsfläche."

EHRLICHE %-ZAHL: 76%

Knappe Begründung der %-Zahl (nicht im Format-Block, weil Briefing's Format strikt ist, aber als Service): 76% weil Page strukturell gut aufgebaut ist, Wortzahl satt über 1500, Schema.org vollständig, Storytelling der vier Friedhöfe wirklich stark — aber: Paragraphen-Fehler in einer juristischen Aussage, der im FAQ-Schema verewigt wird, ist ein Vertrauens-Killer. Plus Halluzinations-Risiko bei der Amtsblatt-Quelle. Plus Faktenfehler beim Flaggschiff-Friedhof. Drei substantielle Vertrauensrisse → unter 85.




