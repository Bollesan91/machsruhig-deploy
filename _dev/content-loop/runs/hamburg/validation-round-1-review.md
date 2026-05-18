Ich lade die Hamburg-Seite und prüfe nur auf MAJOR-Issues.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/hamburg/index.html?cb=1779092903790
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/hamburg/index.html?cb=1779092903790

STADT: Hamburg

VERDICT: ❌ NICHT DEPLOY-READY — 2 sachliche MAJOR-Fehler, 1 strukturelles MAJOR-Risiko

MAJOR #1 — Falsche Rechtsgrundlage (YMYL-kritisch) HmbBestattG wird als „zuletzt 2020 reformiert" zitiert. Das Hamburgische Bestattungsgesetz datiert vom 14.09.1988 mit Novellen, u.a. 2010 (Sargpflicht-Lockerung für muslimische Bestattungen) — keine umfassende Reform 2020 bekannt. Bitte konkrete Fundstelle (HmbGVBl + §) verifizieren oder Aussage entfernen. Risiko: Vertrauensverlust + Schema.org-Widerspruch zu „primary-source-backed".

MAJOR #2 — Widerspruch in Kostenangaben (Inkonsistenz)

Meta-Description + FAQ-Schema: Seebestattung „3.000–5.000 €"
Body: „ab 1.049 € unbegleitet"
FAQ#1 sichtbar: „Seebestattung ab 2.900 €"

Drei verschiedene Preise auf einer Seite. Google rich snippets ziehen aus FAQ-Schema → User sieht 3.000–5.000 €, klickt, liest 1.049 €. Klassischer Trust-Killer + potenziell UWG-relevant.

MAJOR #3 — Schema/Content-Mismatch beim Autorenmodell Schema.org nennt nur Organization, aber kein author/Person-Objekt am Service/FAQPage. Im sichtbaren Content steht „Redaktion machsruhig.de" — ohne author im Graph kein E-E-A-T-Signal. Für YMYL der dünnste Punkt der Seite. Fachpool-Reviewer (laut Autorenmodell-Entscheidung) fehlt komplett.

Empfehlung: Block-für-Deploy bis #1 + #2 gefixt. #3 in nächstem Sprint.

(243 Wörter)