# Session-Notizen

## Letzte Session
**Datum:** 11. Mai 2026 (Multi-Chat-Pipeline auf 5 Top-Städte, dann Welle-1-Start)
**Deploy-Status:** ✅ 5 Top-Stadt-Pages live (Netlify auto-deploy)

## Was wurde gemacht

### 🚀 Top-5 Stadt-Pages durch Multi-Chat-V2-Pipeline → LIVE

Multi-Chat-Architektur mit echter Sycophancy-Isolation: **Chat A (Writer) + Chat B (Reviewer) + Chat C (Adversarial)** in separaten claude.ai Browser-Tabs via Chrome-MCP. Branch-Trick: jeder Chat fetcht raw-URLs aus `content-loop-pipeline`-Branch statt chunked-paste.

| Stadt | Wortzahl | Review-Score | Adversarial | Status |
|---|---|---|---|---|
| **München** | 5590 | 72% | 78% | v1→v2→v3 live |
| **Frankfurt** | 3264 | 74% | 76% | v1→v2→v3 live |
| **Berlin** | 3482 | 74% | 79% | v1→v2→v3 live |
| **Hamburg** | 3600 | 72% | 78% | v1→v3 live (Artifact-Workaround) |
| **Köln** | 1708 | 76% | 79% | v1→v2→v3 live |

**Pipeline-Beweis (Branch-Trick funktioniert):**
- Chat C (Adversarial) fand bei München v2: **"Hessen-Quelle für Bayern-BestV"** = Copy-Paste-Halluzination — Chat A allein hätte das nie gesehen
- Chat C bei München v2: **§ 17 BestV / 1.1.2023** = doppelter erfundener Paragraph + Datum
- Alle 3 Halluzinations-Verdachte in v3 korrigiert

**Layout/Schema konsistent:**
- mr-Klassen (mr-nav, mr-content, mr-hero, mr-keyfacts, etc.)
- DM Sans + Fraunces Fonts
- Schema.org: Article, FAQPage, BreadcrumbList, WebPage, Place pro Friedhof
- Skip-Link, Footer mit Cross-Links

### 🗺️ Sitemap aufgeräumt
- 45 Thin-Content-Städte aus Sitemap entfernt (haben noindex,follow seit 23.04.)
- 5 Top-Städte mit priority 0.7

### 📋 Welle 1 vorbereitet
- **Stuttgart Quellen-Pack** bereits geschrieben (Welle 1 erste Stadt)
- **STADT-QUEUE.md** mit allen 45 Städten in 3 Wellen (Top-15/Mid-15/Tail-15)
- **MASS-PIPELINE-RECIPE.md** als Schritt-für-Schritt-Anleitung
- **LOOP-TRIGGER.md** mit Slash-Command für autonomen `/loop`

## Nächste Schritte

### 🔄 /loop für 45 Städte aktivieren

**Im Claude-Code-CLI tippen:**

```
/loop arbeite die naechste unmarkierte Stadt aus _dev/content-loop/STADT-QUEUE.md ab nach MASS-PIPELINE-RECIPE.md. Vollstaendige V2-Pipeline pro Stadt (Quellen-Pack, Chat A, B, C, Final-Fix, deploy). ScheduleWakeup zwischen Staedten 1200s. Stopp wenn alle 45 abgehakt.
```

### Welle 1 (15 Städte, höchste Priorität)
Stuttgart, Düsseldorf, Leipzig, Dortmund, Essen, Bremen, Dresden, Hannover, Nürnberg, Duisburg, Bochum, Wuppertal, Bielefeld, Bonn, Münster

Stuttgart Quellen-Pack bereits fertig — Pipeline kann direkt mit Chat A v1 starten.

### Welle 2 (Mid-15)
Mannheim, Karlsruhe, Augsburg, Wiesbaden, Mainz, Kiel, Magdeburg, Saarbrücken, Potsdam, Erfurt, Freiburg, Lübeck, Oldenburg, Rostock, Kassel

### Welle 3 (Tail-15)
Mönchengladbach, Gelsenkirchen, Braunschweig, Chemnitz, Halle, Krefeld, Heidelberg, Regensburg, Hagen, Oberhausen, Osnabrück, Mülheim, Leverkusen, Darmstadt, Aachen

### Deploy-Strategie
- Nach Welle 1 (15 Pages): main commit + netlify deploy
- Nach Welle 2 (30 Pages): dito
- Nach Welle 3 (45 Pages): final + 100% Coverage erreicht

## Offene Fragen

- Soll Welle 2/3 in Priorität anders gewichtet werden? (z.B. nach Hauptstadt-Status)
- Stadt-Page-Variante für Stadtstaaten (Bremen) — Differenzierung wie bei Berlin/Hamburg?
- Sitemap auto-add nach jeder Welle: priority 0.6 → 0.7 + lastmod = heute?

## Erledigte PBIs (gesamt)

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 21, 22
+ Monetarisierung, Vorsorge-Cluster, 9 neue Tools/Seiten
+ Audit + Roadmap „Authority-first" (22.04.2026)
+ RP Elite-Niveau (24.04.2026)
+ **Content-Loop-Pilot Saarland + Hessen** (11.05.2026)
+ **Content-Loop V2 Multi-Chat-Pipeline (Chrome-MCP) Top-5 Stadt-Pages LIVE** (11.05.2026)
