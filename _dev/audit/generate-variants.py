#!/usr/bin/env python3
"""
Generate the 7 SEO cluster variants from the hub page template.
Each variant gets variant-specific title/meta/h1/lead + FAQ-overrides.
Most content (5-Ebenen, Rote Flaggen, 10 Fragen, Klärungsgespräch, Quellen, Footer) shared.
"""
from pathlib import Path
import re
import json

HUB_PATH = Path('bestatter-angebot-pruefen.html')
OUTPUT_DIR = Path('.')

# Read hub as template
HUB = HUB_PATH.read_text(encoding='utf-8')

# Variant configurations
VARIANTS = {
    'bestatter-angebot-vergleichen': {
        'title': 'Bestatter-Angebote vergleichen: Was zählt wirklich? | machsruhig',
        'meta_desc': 'Bestatter-Angebote vergleichen: Endsumme vs. Leistungsumfang, Pauschalen erkennen, fair entscheiden. Mit Vergleichs-Hilfe und Angebots-Check in 3 Minuten.',
        'og_desc': 'Wie vergleichst du Bestatter-Angebote fair? Endsumme vs. Posten — mit kostenlosem Check in 3 Min.',
        'h1': 'Bestatter-Angebote vergleichen: auf die Posten kommt es an',
        'breadcrumb_last': 'Angebote vergleichen',
        'canonical_suffix': '/bestatter-angebot-vergleichen',
        'lead': 'Drei Bestatter, drei Preise — aber sind die wirklich vergleichbar? Wer Angebote nur nach der Endsumme bewertet, vergleicht oft Äpfel mit Birnen. Diese Seite zeigt dir, wie du Bestatter-Angebote sauber gegenüberstellst — und worauf du achten musst, damit der „günstigste" Bestatter am Ende nicht der teuerste wird.',
        'intro_section_h2': 'Warum reicht der reine Preisvergleich nicht?',
        'intro_section_p': '<p>Wenn du drei Bestatter um ein Angebot bittest, bekommst du oft drei sehr unterschiedliche Zahlen — manchmal mit 30–50 % Spannweite. Der Unterschied entsteht selten daraus, dass ein Bestatter teurer arbeitet. Er entsteht aus zwei Dingen: <strong>was im Angebot enthalten ist</strong> und <strong>was als Fremdleistung später separat berechnet wird</strong>.</p><p>Bestatter A nennt 5.800 €, Bestatter B 7.200 €, Bestatter C 4.900 €. Erst beim genauen Lesen siehst du: Bei A sind Friedhofsgebühren nicht enthalten, bei C fehlt die Trauerhalle, bei B ist alles drin. Plötzlich ist B der günstigste — und auch der einzige, mit dem du planbar entscheiden kannst.</p><p>Diese Seite hilft dir, die Angebote so zu sortieren, dass du wirklich vergleichbare Zahlen vor dir hast.</p>',
        'faq_overrides': [
            ('Was ist der häufigste Fehler beim Vergleich von Bestatter-Angeboten?', 'Den günstigsten Endpreis zu wählen, ohne die Leistungsposten zu vergleichen. Das günstigste Angebot enthält oft weniger Posten (z.B. keine Friedhofsgebühren oder keine Trauerhalle). Diese kommen dann später dazu — und am Ende liegt der Gesamtpreis oft über dem, was ein scheinbar teureres Komplettangebot gekostet hätte.'),
            ('Wie viele Angebote sollte ich einholen?', 'Stiftung Warentest empfiehlt 2–3 Angebote. Mehr als 3 macht selten Sinn, weil der Aufwand des Vergleichens steigt und die Zeit drängt. Wichtiger als die Anzahl ist, dass jedes Angebot vollständig und aufgeschlüsselt ist.'),
        ]
    },
    'bestattungskosten-versteckte-kosten': {
        'title': 'Bestattungskosten: versteckte Kosten erkennen | machsruhig',
        'meta_desc': 'Versteckte Kosten bei der Bestattung: Welche Posten fehlen oft im Erstangebot? Wie erkennst du Pauschalen-Fallen? Mit Check-Tool und Fragenliste in 3 Min.',
        'og_desc': 'Versteckte Bestattungskosten erkennen — die häufigsten Fallen und wie du sie früh aufspürst.',
        'h1': 'Versteckte Kosten bei der Bestattung — die häufigsten Fallen',
        'breadcrumb_last': 'Versteckte Kosten',
        'canonical_suffix': '/bestattungskosten-versteckte-kosten',
        'lead': 'Auf dem Bestatter-Angebot stehen 5.800 €. Am Ende zahlst du 8.400 €. Wie konnte das passieren? Versteckte Kosten in Bestatter-Angeboten sind selten Betrug — meist sind sie systembedingt. Diese Seite zeigt dir, wo die Lücken typischerweise sitzen und wie du sie vor der Unterschrift aufdeckst.',
        'intro_section_h2': 'Wo sitzen die typischen Kostenfallen?',
        'intro_section_p': '<p>Versteckte Kosten entstehen nicht, weil ein Bestatter dich täuschen will. Sie entstehen, weil viele Posten <strong>als Fremdleistung</strong> oder <strong>als spätere Folgekosten</strong> erfasst werden und im Erstangebot nicht auftauchen. Wenn du sie kennst, kannst du gezielt nachfragen — und keine bösen Überraschungen erleben.</p><p>Die Stiftung Warentest hat 2024 in einer Untersuchung von Bestatter-Vergleichen festgestellt, dass viele Angebote zwar formal vollständig wirken, aber wichtige Folgeposten wie Grabpflege, Grabstein oder mehrere Sterbeurkunden komplett auslassen — nicht aus Absicht, sondern weil diese Posten erst Wochen oder Monate nach der Bestattung anfallen.</p><p>Im Folgenden zeigen wir dir das vollständige Kostenmodell mit allen 5 Ebenen — danach kommen die typischen Lücken, an denen Posten versteckt sein können.</p>',
        'faq_overrides': [
            ('Welche Kosten werden am häufigsten vergessen?', 'Mehrjährige Grabpflege (1.600–5.000 € über 20 Jahre), Grabstein (400–7.000 €), Sterbeurkunden (10–15 € pro Stück, üblich 5–10 Stück) und die Beurkundungsgebühr beim Standesamt. Diese Posten erscheinen selten im Erstangebot, weil sie zeitlich versetzt anfallen.'),
            ('Sind Friedhofsgebühren immer im Bestatter-Angebot enthalten?', 'Nein. Friedhofsgebühren sind kommunale Gebühren und werden je nach Bestatter entweder direkt durchgereicht oder du bekommst die Rechnung später von der Stadt. Frage explizit: „Sind die Friedhofsgebühren in dieser Endsumme enthalten oder kommt die Rechnung der Stadt separat?"'),
        ]
    },
    'was-muss-im-kostenvoranschlag-stehen': {
        'title': 'Was muss im Bestatter-Kostenvoranschlag stehen? | machsruhig',
        'meta_desc': 'Bestatter-Kostenvoranschlag: Welche Posten gehören rein, welche Angaben sind Pflicht, welche optional? Mit Vorlage zum Abhaken und Tool-Check in 3 Min.',
        'og_desc': 'Was muss in einem Bestatter-Kostenvoranschlag stehen? Pflicht-Posten + Form-Anforderungen.',
        'h1': 'Was muss in einem Bestatter-Kostenvoranschlag stehen?',
        'breadcrumb_last': 'Kostenvoranschlag-Pflichtposten',
        'canonical_suffix': '/was-muss-im-kostenvoranschlag-stehen',
        'lead': 'Ein Bestatter-Kostenvoranschlag ist mehr als eine Liste mit Endpreis. Er ist die Grundlage für deine Entscheidung — und im Streitfall auch das, woran sich der Bestatter messen lassen muss. Welche Posten gehören zwingend rein, welche sollten optional ausgewiesen sein und welche Angaben sind formal notwendig? Diese Seite gibt dir die Checkliste.',
        'intro_section_h2': 'Was unterscheidet einen seriösen Kostenvoranschlag von einer Pauschalrechnung?',
        'intro_section_p': '<p>Ein Kostenvoranschlag ist rechtlich ein <em>Kostenanschlag</em> im Sinne von § 649 BGB — er ist kein Festpreis, sondern eine ungefähre Schätzung der Werkleistung. Bei wesentlicher Überschreitung (Faustregel: 15–20 %) muss der Bestatter dich vor der Leistung informieren. Die Erstellung des Voranschlags selbst ist nach § 632 Abs. 3 BGB im Zweifel kostenlos — das heißt, du musst den Voranschlag nicht bezahlen, wenn nichts anderes vereinbart wurde.</p><p>Wenn der Bestatter dir nur eine Endsumme mit drei Stichpunkten gibt („Sarg, Beisetzung, Trauerfeier — 5.800 €"), dann ist das kein Kostenvoranschlag, sondern eine Pauschalrechnung. Bitte um eine aufgeschlüsselte Version. Seriöse Bestatter machen das ohne Murren — sie haben das Format ohnehin schon in ihrer Software.</p>',
        'faq_overrides': [
            ('Ist ein Bestatter-Kostenvoranschlag rechtlich bindend?', 'Ein Kostenvoranschlag (rechtlich: Kostenanschlag nach § 649 BGB) ist eine Schätzung, kein Festpreis. Der Bestatter darf abweichen, muss aber „wesentliche Überschreitungen" vor der Leistung anzeigen — sonst kann er den Mehrbetrag nicht durchsetzen. Faustregel: Bei mehr als 15–20 % Mehrkosten muss er dich informieren. Die Erstellung des Voranschlags ist nach § 632 Abs. 3 BGB im Zweifel kostenlos.'),
            ('Welche Mindestangaben muss ein Kostenvoranschlag enthalten?', 'Anschrift und Unterschrift des Bestatters, Datum, eindeutige Auflistung der Einzelposten mit Einzelpreisen, Trennung zwischen Bestatterleistungen und Fremdleistungen, voraussichtliche Endsumme inkl. MwSt., Gültigkeitsdauer des Angebots. Ohne diese Angaben ist es kein vollwertiger Voranschlag.'),
        ]
    },
    'bestatter-rechnung-pruefen': {
        'title': 'Bestatter-Rechnung prüfen: Posten und Pflicht-Angaben | machsruhig',
        'meta_desc': 'Bestatter-Rechnung prüfen: Stimmt sie mit dem Angebot überein? Welche Posten sind plausibel? Mit Check-Tool und Fragenliste in 3 Minuten.',
        'og_desc': 'Bestatter-Rechnung prüfen — was tun bei Abweichungen zum Kostenvoranschlag?',
        'h1': 'Bestatter-Rechnung prüfen — was darf abweichen?',
        'breadcrumb_last': 'Rechnung prüfen',
        'canonical_suffix': '/bestatter-rechnung-pruefen',
        'lead': 'Die Bestatter-Rechnung liegt im Briefkasten — und sie ist höher als das Angebot. Darf das? Was musst du jetzt prüfen, und worauf hast du als Auftraggeber Anspruch? Diese Seite zeigt dir, wie du eine Bestatter-Rechnung systematisch durchgehst und welche Abweichungen gerechtfertigt sind.',
        'intro_section_h2': 'Wann darf eine Bestatter-Rechnung vom Kostenvoranschlag abweichen?',
        'intro_section_p': '<p>Ein Kostenvoranschlag (rechtlich: Kostenanschlag nach § 649 BGB) ist eine Schätzung, die endgültige Rechnung darf davon abweichen. Aber nicht beliebig. Der Bestatter muss „wesentliche Überschreitungen" rechtzeitig anzeigen, damit du noch reagieren kannst — sonst kann er den Mehrbetrag nicht durchsetzen.</p><p>Als Faustregel gilt: Abweichungen bis 10 % sind im Rahmen, 10–20 % sollten begründet sein, über 20 % brauchen eine ausdrückliche Anzeige vor Beauftragung. Wenn die Rechnung deutlich höher ausfällt als der Voranschlag und der Bestatter dich darüber nicht informiert hat, hast du gute Chancen, die Differenz nicht zahlen zu müssen.</p>',
        'faq_overrides': [
            ('Wie hoch darf eine Bestatter-Rechnung über dem Voranschlag liegen?', 'Faustregel: Bis 10 % gilt als üblich, 10–20 % sollte der Bestatter begründen, ab 20 % muss er „wesentliche Überschreitungen" gemäß § 649 BGB vor der Leistungserbringung anzeigen. Ohne Anzeige bist du nicht verpflichtet, den Mehrbetrag zu zahlen.'),
            ('Welche Pflichtangaben muss eine Bestatter-Rechnung enthalten?', 'Rechnungssteller (Name + Anschrift), Empfänger, Rechnungsnummer + Datum, Steuer-Nr./USt-IdNr., Leistungszeitpunkt, Einzelposten + Einzelpreise, MwSt. separat ausgewiesen, Gesamtbetrag, Zahlungsfrist. Fehlt etwas davon, kannst du eine korrigierte Rechnung verlangen.'),
        ]
    },
    'erdbestattung-angebot-pruefen': {
        'title': 'Erdbestattung-Angebot prüfen: typischer Preisrahmen | machsruhig',
        'meta_desc': 'Erdbestattung-Angebot prüfen: Welche Posten gehören rein? Was kostet sie typischerweise (4.500–9.500 €)? Mit Ampel-Check und Fragenliste in 3 Min.',
        'og_desc': 'Erdbestattung-Angebot prüfen — Sarg, Grabstelle, Beisetzung und alle Pflicht-Posten.',
        'h1': 'Erdbestattung-Angebot prüfen — was sollte enthalten sein?',
        'breadcrumb_last': 'Erdbestattung-Angebot',
        'canonical_suffix': '/erdbestattung-angebot-pruefen',
        'lead': 'Eine Erdbestattung ist in Deutschland nach wie vor die häufigste Bestattungsart. Sie ist aber auch die kostenintensivste — typisch 4.500–9.500 € — und enthält viele Einzelposten, bei denen schnell Posten verloren gehen. Diese Seite zeigt dir, was in einem Erdbestattung-Angebot stehen muss und wo die häufigsten Lücken sitzen.',
        'intro_section_h2': 'Was macht ein Erdbestattung-Angebot besonders?',
        'intro_section_p': '<p>Die Erdbestattung hat — anders als Feuerbestattung oder Seebestattung — zwei besondere Kostenblöcke: einen <strong>Sarg</strong> (der für die Erdbestattung qualitativ höher sein muss als für die Verbrennung) und eine <strong>Grabstelle</strong> auf einem Friedhof, deren Gebühren regional stark variieren (Bayern 1,22-fach, MV 0,78-fach des Bundes-Mittels).</p><p>Hinzu kommt, dass die Erdbestattung in den meisten Bundesländern strenger geregelt ist als andere Bestattungsformen — Sarg- und Beisetzungsfristen sind kürzer (typisch 4–10 Tage), und die Grabnutzungsdauer ist länger (typisch 20–30 Jahre), was die Folgekosten für Grabpflege erhöht.</p><p>Ein vollständiges Erdbestattung-Angebot sollte mindestens diese sechs Pflicht-Posten klar ausweisen:</p><ul><li>Bestatterleistungen (Beratung, Organisation, Behörden)</li><li>Abholung + Überführung</li><li>Hygienische Versorgung</li><li>Sarg (Material + Ausstattung benannt)</li><li>Friedhofsgebühren (Grabstelle + Nutzung + Beisetzung)</li><li>Sterbeurkunden (Anzahl benannt)</li></ul>',
        'faq_overrides': [
            ('Was kostet eine Erdbestattung in Deutschland?', 'Eine Erdbestattung kostet typisch 4.500–9.500 € (Stand 2026). Die Spanne entsteht hauptsächlich durch regionale Friedhofsgebühren und die Wahl des Sargs. In Bayern liegt der Schnitt eher bei 5.500–11.600 € (Multiplikator 1,22), in Mecklenburg-Vorpommern bei 3.500–7.400 € (Multiplikator 0,78).'),
            ('Welche Pflicht-Posten sind in einem Erdbestattung-Angebot?', 'Bestatterleistungen, Abholung + Überführung, hygienische Versorgung, Sarg, Friedhofsgebühren (Grab + Nutzungsrecht + Beisetzungs-Service) und mehrere Sterbeurkunden — also 6 Pflicht-Posten. Optional sind Trauerfeier, Floristik, Aufbahrung und Grabstein.'),
        ]
    },
    'feuerbestattung-angebot-pruefen': {
        'title': 'Feuerbestattung-Angebot prüfen: Posten und Preisrahmen | machsruhig',
        'meta_desc': 'Feuerbestattung-Angebot prüfen: Welche Posten gehören rein (3.500–7.500 €)? Krematorium, Urne, zweite Leichenschau — was wirklich Pflicht ist.',
        'og_desc': 'Feuerbestattung-Angebot prüfen — Einäscherung, Urne, Beisetzung und alle Pflicht-Posten.',
        'h1': 'Feuerbestattung-Angebot prüfen — was muss enthalten sein?',
        'breadcrumb_last': 'Feuerbestattung-Angebot',
        'canonical_suffix': '/feuerbestattung-angebot-pruefen',
        'lead': 'Feuerbestattungen sind in Deutschland mittlerweile die häufigere Bestattungsart — sie sind günstiger als Erdbestattungen und flexibler in der Wahl der Beisetzungsform. Trotzdem haben sie eine eigene Kostenstruktur mit Posten, die bei der Erdbestattung nicht vorkommen (Krematorium, zweite Leichenschau, Urne). Diese Seite zeigt dir, was in einem Feuerbestattung-Angebot enthalten sein muss.',
        'intro_section_h2': 'Was unterscheidet ein Feuerbestattung-Angebot von einer Erdbestattung?',
        'intro_section_p': '<p>Bei einer Feuerbestattung kommen zwei spezielle Posten dazu, die du im Angebot finden solltest: <strong>Kremationsgebühren</strong> (300–550 €) und in den meisten Bundesländern eine zusätzliche <strong>qualifizierte Leichenschau</strong> vor der Einäscherung (50–150 €). Diese ist in den Landesbestattungsgesetzen geregelt und wird in der Praxis oft im Krematoriums-Posten verrechnet — manchmal aber auch separat ausgewiesen. Die genaue Ausgestaltung variiert nach Bundesland.</p><p>Dafür entfällt der teure Sarg — bei Feuerbestattung reicht ein einfacher Verbrennungssarg (600–1.800 € statt 800–2.200 € bei Erdbestattung). Auch die Friedhofsgebühren sind in der Regel niedriger, weil ein Urnengrab weniger Platz braucht als ein Sarggrab. Die typische Preisspanne liegt bei 3.500–7.500 €.</p><p>Ein vollständiges Feuerbestattung-Angebot sollte diese Pflicht-Posten klar ausweisen:</p><ul><li>Bestatterleistungen + Abholung + Versorgung</li><li>Verbrennungssarg</li><li>Krematorium (inkl. qualifizierter Leichenschau, falls in deinem Bundesland vorgesehen)</li><li>Urne</li><li>Friedhofsgebühren (Urnengrab + Beisetzung)</li><li>Sterbeurkunden</li></ul>',
        'faq_overrides': [
            ('Was kostet eine Feuerbestattung in Deutschland?', 'Eine Feuerbestattung kostet typisch 3.500–7.500 € (Stand 2026). Sie ist damit günstiger als eine Erdbestattung, weil Sarg, Friedhofsgebühren und Grabpflege niedriger ausfallen. Regional reicht die Spanne von etwa 3.000 € (Mecklenburg-Vorpommern) bis 9.000 € (Bayern, München).'),
            ('Was ist die qualifizierte Leichenschau vor Einäscherung?', 'In den meisten Bundesländern muss vor einer Einäscherung eine qualifizierte Leichenschau durch einen besonders qualifizierten Arzt erfolgen (Landesbestattungsgesetze, Ausgestaltung variiert). Sie kostet 50–150 € und wird in der Praxis oft im Krematoriums-Posten verrechnet — manchmal aber auch separat im Angebot ausgewiesen. Frage nach, falls du sie nicht findest.'),
        ]
    },
    'seebestattung-angebot-pruefen': {
        'title': 'Seebestattung-Angebot prüfen: was gehört rein? | machsruhig',
        'meta_desc': 'Seebestattung-Angebot prüfen: typischer Rahmen (3.500–6.500 €), Reederei-Posten, Begleitfahrt und Pflicht-Posten — mit Check-Tool in 3 Min.',
        'og_desc': 'Seebestattung-Angebot prüfen — Reederei, Begleitfahrt und alle Posten verstehen.',
        'h1': 'Seebestattung-Angebot prüfen — was sollte enthalten sein?',
        'breadcrumb_last': 'Seebestattung-Angebot',
        'canonical_suffix': '/seebestattung-angebot-pruefen',
        'lead': 'Seebestattungen sind eine besondere Variante: keine Grabstelle, dafür Reederei-Kosten und teils auch die Begleitfahrt der Angehörigen. Diese Seite zeigt dir, was ein Seebestattung-Angebot enthalten muss — und wo die Posten anders sortiert sind als bei Erd- oder Feuerbestattung.',
        'intro_section_h2': 'Was macht ein Seebestattung-Angebot besonders?',
        'intro_section_p': '<p>Bei einer Seebestattung entfällt der Friedhof — und damit auch die Friedhofsgebühren, das Grab und die langfristige Grabpflege. Das spart erheblich. Dafür kommen aber zwei Posten dazu, die in anderen Angeboten nicht auftauchen: die <strong>Reederei-Pauschale</strong> (300–900 € für das Schiff + Bestattungsfahrt) und gegebenenfalls die <strong>Begleitfahrt für Angehörige</strong> (300–800 € je nach Personenzahl und Strecke).</p><p>Außerdem braucht es eine spezielle <strong>seetaugliche Urne</strong> (i.d.R. aus Salzstein oder Zellulose, 80–250 €), die sich im Wasser auflöst. Eine Urne aus Metall oder Keramik ist für die Seebestattung nicht zugelassen.</p><p>Die typische Preisspanne liegt bei 3.500–6.500 € — also etwas unter der Feuerbestattung. Beliebte Beisetzungsgebiete sind die Nordsee (Helgoland, Cuxhaven), die Ostsee (Travemünde, Rostock) und in seltenen Fällen das Mittelmeer.</p><p>Ein vollständiges Seebestattung-Angebot sollte diese Pflicht-Posten klar ausweisen:</p><ul><li>Bestatterleistungen + Abholung</li><li>Verbrennungssarg + Krematorium (inkl. 2. Leichenschau)</li><li>Seetaugliche Urne</li><li>Reederei-Pauschale</li><li>Optional: Begleitfahrt für Angehörige</li><li>Sterbeurkunden</li></ul>',
        'faq_overrides': [
            ('Was kostet eine Seebestattung?', 'Eine Seebestattung kostet typisch 3.500–6.500 € (Stand 2026). Sie ist günstiger als Erd- oder Feuerbestattung mit Friedhofs-Beisetzung, weil keine Grab- oder Friedhofsgebühren anfallen. Aufpreise entstehen vor allem durch die Begleitfahrt der Angehörigen, falls gewünscht.'),
            ('Können Angehörige bei der Seebestattung dabei sein?', 'Ja, viele Reedereien bieten eine Begleitfahrt an (typisch 300–800 € je nach Personenzahl und Strecke). Manche Familien bestatten ohne Begleitfahrt (sogenannte „stille Seebestattung", ~300–500 € günstiger), andere wünschen eine Trauerfeier an Bord oder am Hafen vorab. Frage deinen Bestatter nach den Optionen.'),
        ]
    },
}

def build_variant(slug, config):
    """Generate variant HTML from hub template."""
    html = HUB

    # Replace title, meta-description, canonical
    html = re.sub(r'<title>[^<]+</title>', f'<title>{config["title"]}</title>', html, count=1)
    html = re.sub(r'<meta name="description" content="[^"]+"',
                  f'<meta name="description" content="{config["meta_desc"]}"', html, count=1)
    html = re.sub(r'<link rel="canonical" href="https://machsruhig\.de/[^"]+"',
                  f'<link rel="canonical" href="https://machsruhig.de{config["canonical_suffix"]}"', html, count=1)
    html = re.sub(r'<meta property="og:title" content="[^"]+"',
                  f'<meta property="og:title" content="{config["title"].rsplit(" | ", 1)[0]}"', html, count=1)
    html = re.sub(r'<meta property="og:description" content="[^"]+"',
                  f'<meta property="og:description" content="{config["og_desc"]}"', html, count=1)
    html = re.sub(r'<meta property="og:url" content="https://machsruhig\.de/[^"]+"',
                  f'<meta property="og:url" content="https://machsruhig.de{config["canonical_suffix"]}"', html, count=1)

    # JSON-LD Article + BreadcrumbList updates
    # Article headline
    html = re.sub(r'"headline":"[^"]+","description":"[^"]+","author"',
                  f'"headline":"{config["h1"]}","description":"{config["og_desc"]}","author"', html, count=1)
    # BreadcrumbList last item
    html = re.sub(r'\{"@type":"ListItem","position":3,"name":"[^"]+","item":"https://machsruhig\.de/bestatter-angebot-pruefen"\}',
                  f'{{"@type":"ListItem","position":3,"name":"{config["breadcrumb_last"]}","item":"https://machsruhig.de{config["canonical_suffix"]}"}}', html, count=1)

    # H1
    html = re.sub(r'<h1>[^<]+</h1>',
                  f'<h1>{config["h1"]}</h1>', html, count=1)

    # Breadcrumb last name
    html = re.sub(r'(<div class="mr-breadcrumb"><a href="/">Start</a> › <a href="/bestattungskosten">Bestattungskosten</a> › )Angebot prüfen</div>',
                  f'\\1{config["breadcrumb_last"]}</div>', html, count=1)

    # Lead (first .lead paragraph in mr-hero)
    html = re.sub(r'<p class="lead">[\s\S]*?</p>',
                  f'<p class="lead">{config["lead"]}</p>', html, count=1)

    # Replace the "Warum überhaupt..." section with variant intro
    intro_pattern = re.compile(r'(<section class="mr-section">\s*)<h2>Warum überhaupt ein Bestatter-Angebot prüfen\?</h2>[\s\S]*?</section>')
    new_intro = (
        f'<section class="mr-section">\n'
        f'    <h2>{config["intro_section_h2"]}</h2>\n'
        f'    {config["intro_section_p"]}\n'
        f'</section>'
    )
    html = intro_pattern.sub(new_intro, html, count=1)

    # FAQ-Overrides: replace first N JSON-LD + visible FAQ pairs with variant-specific ones
    overrides = config.get('faq_overrides', [])
    if overrides:
        # JSON-LD side: regex that correctly handles JSON-escaped quotes (\")
        # Pattern matches Question.name + acceptedAnswer.text properly
        jsonld_q_pattern = re.compile(
            r'\{"@type":"Question","name":"((?:[^"\\]|\\.)*)","acceptedAnswer":\{"@type":"Answer","text":"((?:[^"\\]|\\.)*)"\}\}'
        )
        def replace_jsonld_questions(match):
            block = match.group(0)
            for i, (newq, newa) in enumerate(overrides):
                qmatches = list(jsonld_q_pattern.finditer(block))
                if i < len(qmatches):
                    qm = qmatches[i]
                    safe_q = newq.replace('\\', '\\\\').replace('"', '\\"')
                    safe_a = newa.replace('\\', '\\\\').replace('"', '\\"')
                    new_entry = f'{{"@type":"Question","name":"{safe_q}","acceptedAnswer":{{"@type":"Answer","text":"{safe_a}"}}}}'
                    block = block[:qm.start()] + new_entry + block[qm.end():]
            return block
        html = re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>', replace_jsonld_questions, html, count=1)

        # Visible FAQ side: replace first N <details> blocks
        details_pattern = re.compile(r'<details><summary>([^<]+)</summary><div class="faq-answer">([^<]+)</div></details>')
        def replace_visible_iteratively(html_str):
            for i, (newq, newa) in enumerate(overrides):
                matches = list(details_pattern.finditer(html_str))
                if i < len(matches):
                    m = matches[i]
                    new_block = f'<details><summary>{newq}</summary><div class="faq-answer">{newa}</div></details>'
                    html_str = html_str[:m.start()] + new_block + html_str[m.end():]
            return html_str
        html = replace_visible_iteratively(html)

    return html

def main():
    for slug, config in VARIANTS.items():
        out = build_variant(slug, config)
        out_path = OUTPUT_DIR / f'{slug}.html'
        out_path.write_text(out, encoding='utf-8')
        print(f'Generated: {slug}.html ({len(out)} chars)')

if __name__ == '__main__':
    main()
