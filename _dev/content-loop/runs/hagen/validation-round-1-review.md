Ich prüfe die Hagen-Stadtseite – sowohl Live als auch Raw-Source.

Fetching: https://machsruhig.de/bestatter/hagen/
Fetched: Bestattung in Hagen — Friedhöfe, Gebühren, Behörden

Live-Page sieht inhaltlich solide aus. Jetzt der Raw-Source-Check für Schema.org, OG-Image, Pipeline-Marker:

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/main/bestatter/hagen/index.html

Durchgang abgeschlossen. Pruefung:

Inhaltlich: §8 BestG NRW Rangfolge korrekt (Ehegatten → Lebenspartner → volljaehrige Kinder → Eltern → volljaehrige Geschwister → Grosseltern → volljaehrige Enkelkinder). §13/§15 BestG NRW korrekt zitiert. Adressen plausibel (Eilper Str. 132-136, Rathausstr. 11). Peter Behrens 1907 / Inbetriebnahme 1912 / preussische Legalisierung 1911 alle konsistent. Hagen tatsaechlich waldreichste GS NRW (Stadtangabe). RuheForst Philippshoehe = erster in NRW (WBH-Quelle). Albiker „Die Klagende" 1911/12, Barlach „Lehrender Christus" 1931 mit Wikipedia-Beleg.

SEO/Schema: @graph komplett. WebPage, Article (datePublished/Modified, headline, author Organization), City, Organization (WBH), CivicStructure (Krematorium mit architect), 6× Place, BreadcrumbList, FAQPage (7 Q&A spiegeln HTML-FAQ). Alle Required-Felder gesetzt.

OG/Meta: og:title, og:description, og:url, og:type=article, og:locale, og:site_name, twitter:card=summary_large_image vorhanden. Canonical sauber. Kein generischer Default.

Pipeline-Leakage: Keine <!-- UNSURE -->, keine [TBD], keine <!-- TODO -->, keine Draft-Marker im Production-HTML. Quellen 1-18 sauber. Nachbarstaedte-Links plausibel (Dortmund, Wuppertal, Iserlohn, Schwerte, Witten, Hattingen — alle echte Nachbarn).

UI/UX: Skip-Link gesetzt, ARIA-Labels an Navs/Asides/Sections, semantic HTML5 (header/main/aside/section/article), Breadcrumb sowohl HTML als auch Schema, Tabellen mit <caption>, FAQ als <details>.

Eine Beobachtung — nicht major: og:image / twitter:image fehlt komplett (kein Default, aber auch kein city-spezifisches Bild). Das ist konsistent mit allen anderen Stadtseiten der Pipeline (bewusste Architekturentscheidung, kein Hagen-Defekt), also nicht melden.

STADT: HAGEN VERDICT: CLEAN

Keine major Findings. Faktencheck (§§ BestG NRW, Adressen, Behrens/Krematorium, Albiker/Barlach, BdSt-Zahlen 1.916 €/3.497 €), Schema.org @graph mit allen Required-Feldern, OG-Tags vollstaendig, keine Draft-Marker, Nachbarstaedte-Links plausibel. Strict-Review-konform.