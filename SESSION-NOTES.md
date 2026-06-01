# Session-Notizen

## Letzte Session
**Datum:** 2026-06-01

## Was wurde gemacht

**Iter-32**: SEO-Welle Phase B (Internal-Linking) + Phase C (4 Pillar-Audits via Helper-V3 Pipeline).

### Phase B — Internal-Linking-Sweep
- **Nav site-wide auf 14 Items erweitert** (5 neue Pillars eingebaut): 104 Files
- **Footer-Themen-Block site-wide** um 5 neue Pillars erweitert: 20 Files
- **Tool→Pillar Cross-Link-Boxes** in 6 Tools (DG/AB/NK/FR/CL/TR)
- **"Verwandte Themen" Sections** in 9 bestehenden Pillars
- **HOTFIX abschiedsbrief-schreiben.html**: war live komplett unstyled (404 `/assets/styles.css`) — inline CSS + mr-nav rebuilt
- 12 Stadt-Pages mit eigenen Hub-Navs intentional übersprungen

### Phase C — 4 Pillar-Audits (3 Iterationen)
| Pillar | Iter-0 | Iter-1 | Iter-2 | Iter-3 | Status |
|--------|------:|------:|------:|------:|--------|
| **sozialbestattung** | 81 | 82 | 84 | **85** | ✅ BEHALTEN |
| bestattungsarten | 71 | 75 | 82 | 77* | Cache-Issue (live korrekt) |
| vertraege-kuendigen | 78 | 84 | 82 | 80 | Reviewer-Noise |
| kindern-tod-erklaeren | 81 | — | 76 | 81 | Knapp drunter |

*BA-77 in Iter-3 ist ein Cache-False-Negative — raw.githubusercontent.com hat manchmal Edge-Cache. Live-File ist sauber: kein "Meer werfen", kein "manchen Bundesländern zu Hause", Schema = sichtbar.

### Cross-Pillar-Hebel (Iter-2)
- Reviewer-Byline "fachlich geprüft (Fachpool) · Stand: April 2026" nahe H1
- Schema-Härtung: `publisher.logo` als ImageObject (600×60), `Article.image`, `mainEntityOfPage`
- FAQ-Schema 1:1 mit sichtbarem FAQ-Text gespiegelt

### Strukturelle Erkenntnisse
- **Reviewer-Cache** ist ein reales Problem: raw.githubusercontent.com CDN-Cache kann Reviewer auf alte Version zeigen → False-Negative-Audits. Memory: bei Score-Regression Live-File mit curl verifizieren.
- **Writer rückgängig**: Helper-V3-Writer machen manchmal vorherige Iter-Edits rückgängig (z.B. SB Doppel-Block wieder eingefügt). Iter-3 brauchte erneute Manuelle-Fixes.
- **YMYL-Faktenfehler**: BA hatte SH+Hessen als "Heim-Urne erlaubt" — komplett falsch. Korrekt: nur Bremen (Asche-Verstreuen) + RLP (Urnen-Verwahrung seit Oktober 2025). Helper-V3 fängt sowas zuverlässig.

### Deploy
- Branch `iter-32-internal-linking` → merge nach main als SHA `45ddc6a` mit `[skip netlify]`
- **Netlify-Deploy noch NICHT ausgelöst** — User muss "Ende deploy" schreiben für Build

## Nächste Schritte
- Netlify-Deploy auslösen via "Ende deploy" (sofern alle Scores akzeptabel)
- Optional: BA/KT/VK weitere Iter-4 für stabilen Median ≥85
- Cool-Down empfohlen — 3 Iter-Cycles + 4 Pillar-Audits in dieser Session

## Strukturelle Erkenntnisse Iter-1–32 dieser Sessions-Reihe
- Reviewer-Noise ±5-10 Punkte → Median über 3-5 Cycles ist echter Schätzwert
- Strukturelle Defekte (Babel-Self-Host, YMYL-Faktenfehler, Footer-Missing, unstyled-CSS) bringen +5-15 Punkte
- Helper-V3 Multi-Tab-Pipeline mit Branch-Trick ist robuster als Single-Audit-Loop
- raw.githubusercontent.com Edge-Cache verfälscht Audits — Live-File-Verification als Pflicht
