Ich hole die Stuttgart-Seite und prüfe sie unbarmherzig.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/stuttgart/index.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/stuttgart/index.html

Ich habe die Seite gründlich durchgeprüft. Drei Major-Issues gefunden.

STADT: STUTTGART

VERDICT: MAJOR-FIX

1. Falsche §-Nummern BestattG BW (juristischer Kernfehler, mehrfach)

Wo: Sektion "Bestattungsrecht in Stuttgart" + Sektion "Was nach einem Todesfall zu tun ist" + FAQ + JSON-LD + Sources
Was: Die Seite nennt § 6 (Ruhezeit), § 31 (Bestattungspflichtige), § 37 (Frist), § 39 (Sarg), § 13 (Leichenschau). Das BestattG BW hat aber nur 36 Paragraphen und nutzt diese Nummerierung nicht: Bestattungspflicht = § 21, Sargpflicht/Ausnahme = § 32, Ruhezeit = § 6 BestattVO BW (Verordnung, nicht Gesetz). Die Landesrecht-BW-Links zielen ebenfalls auf falsche Paragraphen. Das ist YMYL-Halluzination und in 10 Min von jedem Anwalt findbar.
Fix: Komplette §-Mapping gegen aktuelles BestattG BW + BestattVO BW prüfen und korrigieren (inkl. Schema, FAQ, Sources).

2. Selbstwiderspruch Bestattungspflicht-Rangfolge (§ 31-Aussage)

Wo: Sektion "Bestattungsrecht", Absatz Bestattungspflichtige
Was: Text sagt: "Ehegatten/eingetragene Lebenspartner, sodann volljährige Kinder, Eltern, Geschwister, Großeltern und Enkel." In BW ist die korrekte Ordnung jedoch: Ehegatte → Kinder → Eltern → Geschwister → Großeltern → Enkel — aber eingetragene Lebenspartner fehlen heute, ersetzt durch Ehe für alle. Auch die Aussage "unabhängig von erbrechtlichen Verhältnissen" gilt nicht universell.
Fix: Wortlaut gegen aktuelle BW-Norm matchen, Reihenfolge verifizieren.

3. FAQ-Schema vs HTML Wortlaut-Mismatch (Frage 2)

Wo: JSON-LD FAQPage, Frage "Was kostet eine Bestattung in Stuttgart?"
Was: Schema-Antwort beginnt "Die Gesamtkosten ... liegen ... 3.000 bis über 11.000 Euro; eine separate Stuttgart-Studie ... liegt nicht vor." HTML-FAQ beginnt umgekehrt: "Eine separate Stuttgart-Studie ... liegt nicht vor. Erfahrungswerte ..." Reihenfolge und Wortlaut weichen ab → Google FAQ-Rich-Result-Risiko.
Fix: HTML-FAQ-Text 1:1 ins Schema spiegeln (gilt auch leicht für Frage 3 "armenisches Grabfeld" und Frage 4 "Ruhezeit").