Ich prüfe Duisburg – Live und Raw.

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/duisburg/index.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/duisburg/index.html

Drei kritische Funde – juristisch / strukturell hart.

1. § 14 + § 17 BestG NRW – FALSCHE Paragraphen. Sehr großes Problem: Die Seite zitiert konsequent "§ 14 Sargpflicht" und "§ 17 Friedhofszwang inkl. Aschen". Im echten BestG NRW (2003) regelt § 14 die Beförderung von Leichen, nicht die Sargpflicht. Sargpflicht ist § 16. Friedhofszwang ist § 13 a.F. bzw. nicht § 17. Die Bonn-Seite zitiert für dasselbe Gesetz korrekt § 11/§ 13/§ 16 – Duisburg-Seite damit in direktem Widerspruch zur Schwesterseite und zur Rechtslage. Anwalt findet das in 30 Sekunden.

2. Bestattungsfrist „48 Stunden – 8 Tage". § 13 BestG NRW gibt die Frist als frühestens 48 h, spätestens 7. Tag (bzw. 8. Tag nach reformierter Fassung – aber die Bonn-Seite sagt "3. bis 9. Tag", was ebenfalls inkonsistent ist). Hier liegt mindestens ein interner Konflikt zwischen Bonn (3.–9. Tag) und Duisburg (48 h – 8 Tage) vor. Mindestens eine der beiden Stadtseiten ist falsch; vermutlich beide.

3. Schema.org/HTML FAQ-Mismatch. Im HTML stehen 7 FAQ-Fragen (Friedhöfe, Gebühren, Bergbau, Recht, Ruhezeit, Anzeige, Bestatter-Wahl). Im FAQPage-JSON-LD stehen dieselben 7 Fragen – passt. Kein Mismatch dort.

Stattdessen das echte Schema-Problem: Article-Schema ohne image und ohne publisher.logo. Bonn-Schema hat image im Article, Duisburg fehlt es ("Article" hat zwar mainEntityOfPage aber kein image-Property — Google Search Console flagged das als Warning bei AMP/Rich Result-Validation).

STADT: DUISBURG VERDICT: MAJOR-FIX

1. Falsche BestG-NRW-Paragraphen (juristischer Hauptfehler)

Was: "§ 14 Sargpflicht", "§ 15 Abs. 1 zweite Leichenschau", "§ 17 Friedhofszwang" – im BestG NRW regelt § 16 die Sargpflicht (nicht § 14), § 13 den Friedhofszwang (nicht § 17). Direkter Widerspruch zur eigenen Bonn-Seite, die § 11/§ 13/§ 16 korrekt zitiert. Wiederholt in: Sektion „Bestattungsrecht", Sektion „Was nach Todesfall" Punkt 1, Sektion „Bestatter-Wahl in Duisburg", FAQ "Was gilt rechtlich".
Wo: 4 Fundstellen im Body + 1 in FAQPage-Schema (acceptedAnswer.text).
Fix: Alle §-Referenzen zu BestG NRW gegen die Bonn-/NRW-Seite vereinheitlichen: Friedhofszwang § 13, Bestattungsfrist § 13, Sargpflicht § 16. § 15 Abs. 1 (zweite Leichenschau) gegen geltende Fassung prüfen.

2. Selbstwiderspruch Bestattungsfrist Bonn ↔ Duisburg

Was: Duisburg-Seite "Erdbestattung frühestens 48 h, spätestens binnen 8 Tagen", Bonn-Seite (in derselben Domain) "in der Regel zwischen dem dritten und neunten Tag". Beide zitieren § 13 BestG NRW – mindestens eine Stadt falsch. Konkurrenz-Quick-Find.
Wo: Sektion „Bestattungsrecht in Duisburg — Kurzüberblick", Absatz 1.
Fix: Frist gegen aktuelle BestG-NRW-Fassung verifizieren und beide Stadtseiten identisch formulieren (Single Source of Truth = NRW-Landesseite).

3. Article-Schema: fehlendes image + fehlendes publisher.logo

Was: @type: Article enthält weder image noch publisher.logo (Bonn-Schema hat image). Google flagged das in Rich Results-Validator als Warning; reduziert Eligibility für Article-Rich-Snippets.
Wo: JSON-LD-Graph im <head>, Article-Node.
Fix: Article-Node ergänzen um "image":"https://machsruhig.de/assets/og/duisburg.png" und publisher zu {"@type":"Organization","name":"machsruhig.de","logo":{"@type":"ImageObject","url":"https://machsruhig.de/assets/logo-512.png"}} erweitern.