Ich pruefe Hannover - Live und Raw parallel.

Fetching: https://machsruhig.de/bestatter/hannover/
Fetched: Bestattung in Hannover: Friedhöfe, Kosten und Bestatter

Live-Page okay. Aber: og:image ist assets/og-image.png - das ist der generische Default (nicht Hannover-spezifisch). Jetzt Raw-Source fuer Schema und Pipeline-Marker:

Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/hannover/index.html
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/hannover/index.html

Pruefung der kritischen Punkte:

Inhaltlich: §7/§9 BestattG Niedersachsen, 8-Tage-Frist, 48h-Mindestfrist, 6-Wochen-Urnenfrist - korrekt. Friedhoefe (Gartenfriedhof 1741, Engesohde 1864, Seelhorst 1924/68ha, Lahe 1968/37ha, Ricklingen mit Krematorium) inhaltlich plausibel und mit Wikipedia-Quellen belegt. Theodor-Lessing-Disclaimer (in Marienbad, NICHT Engesohde) ist sogar ein Pluspunkt - aktive Halluzinations-Abwehr. Wilhelm Busch / Schwitters / Hase / Georgi / Kopf auf Engesohde - korrekt.

Strukturwidersprueche: Keine. Keyfacts, Sektionen, FAQ und Schema sind konsistent. 16 staedtische Friedhoefe, Seelhorst 68ha, Engesohde 1864 - durchgaengig.

SEO/Schema: WebPage, City, Article (datePublished/Modified), BreadcrumbList, 5x Place mit Adressen+PLZ, FAQPage mit 6 Q&A. @graph komplett.

Markante Funde:

STADT: HANNOVER VERDICT: MAJOR-FIX

1. Generisches OG-Image (Default statt Stadt-spezifisch)

Was: og:image zeigt auf https://machsruhig.de/assets/og-image.png — der generische Site-Default. Im Brief explizit als Pipeline-Leakage gelistet. Beim Teilen auf LinkedIn/WhatsApp/Twitter erscheint kein Hannover-Bezug; reduziert CTR und wirkt im Vergleich zu Konkurrenten unfertig.
Wo: <meta property="og:image"> im <head> + primaryImageOfPage in WebPage-Schema (zeigt auch auf Default).
Fix: City-spezifische OG-Card (z.B. /assets/og/hannover.png 1200×630) generieren und in og:image + primaryImageOfPage referenzieren — wie Gold-City-Pages.

2. FAQ HTML ↔ Schema-Mismatch (Section-Count + Inhaltsbreite)

Was: HTML-FAQ hat 7 Fragen (inkl. „Gibt es naturnahe Bestattungsformen direkt in Hannover?"), Schema-FAQPage nur 6 — die Naturnahe-Frage fehlt komplett. Zusaetzlich: Frage „Bestattungsfrist" + „Welcher ist der groesste Friedhof" enthalten im HTML ausfuehrlichere Antworten als im Schema. Google-Rich-Result-Test wirft Mismatch; gleichzeitig SEO-Schaden, weil Long-Tail-Antwort (Baumgrabfeld Lahe) nicht als Rich Snippet eligible.
Wo: <script type="application/ld+json"> FAQPage.mainEntity vs. <div class="mr-faq"> letztes <details>.
Fix: 7. Frage 1:1 ins Schema nachziehen + 2 verkuerzte Antworten an HTML-Wortlaut angleichen.

3. Article-Schema unvollstaendig (image + publisher.logo fehlen)

Was: Schema Article hat weder image noch publisher.logo (ImageObject mit url). Beides ist von Google fuer Article-Rich-Results als erforderlich/empfohlen markiert; ohne diese Felder kein Article-Card im Discover/News. Bei Hagen war das @graph komplett — hier inkonsistent zur Pipeline.
Wo: Schema-Block {"@type":"Article",...}.
Fix: "image":["https://machsruhig.de/assets/og/hannover.png"] und "publisher":{"@type":"Organization","name":"machsruhig.de","logo":{"@type":"ImageObject","url":"https://machsruhig.de/assets/logo.png"}} ergaenzen.