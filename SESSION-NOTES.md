# Session-Notizen

## Letzte Session
**Datum:** 2026-05-31

## Was wurde gemacht

**Iter-31 SEO-Welle Phase A**: 5 neue Pillar-Pages via Helper-V3 Multi-Tab-Pipeline (Writer + Reviewer auf claude.ai, Branch-Trick `iter-31-seo-pillars`, Loop 240s).

### Pillar-Final-Scores (alle BEHALTEN nach Iter)
| Pillar | URL | Final | Iter-Anzahl |
|--------|-----|------:|----:|
| Notfallkarte | /notfallkarte | **88** | 1 |
| Danksagung-nach-Beerdigung | /danksagung-nach-beerdigung | **86** | 2 (Fix: Beispieltexte) |
| Was-tun-nach-Todesfall | /was-tun-nach-todesfall | **86** | 2 (Fix: E-E-A-T) |
| Fristen-nach-Todesfall | /fristen-nach-todesfall | **85** | 3 (Fix: § 580 → § 564 BGB!) |
| Abschiedsbrief-Schreiben | /abschiedsbrief-schreiben | 84 (BEHALTEN-Verdikt) | 3 (Footer-Hotfix) |

### Methodik
- Helper-V3 Pipeline: 1 Writer-Tab pro Pillar (fix-bar reusable) + frische Reviewer-Tabs pro Re-Audit
- Branch-Trick: alle Iters auf `iter-31-seo-pillars`, Reviewer auditet via raw.githubusercontent.com (kein Netlify-Build im Loop)
- Blob-Download-Workaround für Cookie/query-Filter beim HTML-Extract
- Loop 240s pro Wave

### Strukturelle Erkenntnisse
- **YMYL-Faktenfehler** (FR § 580 BGB statt § 564 BGB) hätte ohne Reviewer-Audit live ranken können — Helper-V3-Pipeline ist real-world critical
- **Footer-Forgotten-Pattern**: AB-Writer ließ Footer komplett weg (Impressumspflicht-Verletzung) — Reviewer fand das sofort
- **Strukturelle Fixes ≫ Polish**: Beispieltexte (DG), § 564 (FR), Footer (AB), E-E-A-T-Reviewer (WT) brachten je 4-6 Punkte

### Deploy
Branch `iter-31-seo-pillars` → merge nach main → Netlify-Deploy. Plus:
- sitemap.xml: 5 neue URLs ergänzt
- _redirects: 5 trailing-slash → extensionslose Redirects

## Nächste Schritte
- Phase B (optional): Internal-Linking-Sweep — Tools sollten auf neue Pillars zurücklinken
- Phase C (optional): Verbleibende Pillars (Bestattungsarten, Sozialbestattung, etc.) auditieren
- Cool-Down empfohlen — viel passiert in dieser Session

## Strukturelle Erkenntnisse 30+ Iters dieser Sessions-Reihe
- Reviewer-Noise ±5-10 Punkte → Median über 3-5 Cycles ist echter Schätzwert
- Strukturelle Defekte (Babel-Self-Host, Faktenfehler, Footer-Missing) bringen +5-15 Punkte
- Helper-V3 Multi-Tab-Pipeline mit Branch-Trick ist robuster als Single-Audit-Loop
