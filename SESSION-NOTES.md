# Session-Notizen

## Letzte Session
**Datum:** 26. Mai 2026 (Repo-Reality-Check gegen externes Marktreife-Beraterpapier — Doppelsession ruhig+leicht, NUR Analyse, kein Code/Content geändert)

## Was wurde gemacht
Externes Beraterpapier ("Aufwand bis Marktreife, 260–480h") gegen den echten Repo-Stand geprüft (frischer Clone, Dateien einzeln gelesen, kein Pauschalurteil). Kernergebnis: **Das Papier ist featurelastig und unterschätzt den Ist-Stand massiv. machsruhig hat KEIN Contentproblem — es hat ein Trust-Tool-Problem und ein SEO-Hygiene-Detail.**

Verifizierte Befunde machsruhig:
- **Stadtseiten faktisch fertig:** 52 Seiten unter `bestatter/`, davon 50 mit 4.500–7.000 Wörtern (Friedhöfe, Gebühren, Sozialbestattung, Quellenbox, Schema). Plus 16 Bundesland-Seiten (2.500–3.350 W). Berater-Schätzung "Top 5–10 Städte auf Gold: 35–70h" ist gegenstandslos.
- **Angebotsprüfer = akutes Trust-Risiko, NICHT "starker Kernhebel":** Tool ist LIVE, `<meta robots: index,follow>`, eigener Canonical, und von **8 Seiten per CTA verlinkt**. Trägt den dokumentierten VALIDITY_FAIL 3/3 (siehe `_dev/audit/angebotspruefer-validity-fail-2026-05-23.md`): schlägt seriöse Angebote ROT, Wording Richtung "Lockangebot". Risiko ist latent (≈0 Traffic), wird real sobald Distribution greift.
- **Doppel-Slug-FALSCHALARM aufgelöst:** `moenchengladbach`/`luebeck` sind bereits `noindex,follow` UND nicht in der Sitemap (98 saubere URLs). Bewusste Entscheidung lt. Inline-Kommentar ("noindex bis Gold-Template-Upgrade"). KEIN 4–12h-Task. Einziger Mini-Rest: ASCII-Stub-Canonical zeigt aktuell self (ASCII) — sollte auf die Umlaut-Version zeigen, ~10 Min.

## Nächste Schritte (priorisiert, Messgate-Logik)
**Pflicht VOR Traffic:**
1. **Angebotsprüfer-Versicherung (P0, ~20–30 Min):** Tool auf `noindex` + die 8 CTAs ziehen/neutralisieren — ODER schneller Wording-Defuse (2–6h): "Lockangebot" raus, Preis nie allein ROT, Pauschale nie allein ROT, Default GELB statt ROT, "Pflicht"→"Klären", Ergebnis von Urteil auf Rückfragen.

**HINTER dem Messgate (erst wenn machsleicht-Indexierung beweist, dass Content rankt — gemeinsamer Strategie-Anker beider Projekte):**
2. Angebotsprüfer-Logik sauber rebuilden (15–40h, über Content-Loop, asynchron): severity pro Posten (critical/medium/info), Preisabweichung nur Signal, Pauschale = "unklar" nicht Fehler, ROT nur bei kumuliertem Risiko, Regressionstest mit 5–10 echten Angeboten.
3. ASCII-Canonical-Fix (~10 Min).
4. Lead-Funnel + Einwilligung sauber (12–30h); Autoren-/Redaktionsprofil + Trust (8–20h).

## Offene Fragen
- Angebotsprüfer: harte Versicherung (noindex+CTA raus) ODER Wording-Defuse als Sofortschritt? (Empfehlung: noindex, billigste sichere Variante, Rebuild ohne Zeitdruck dahinter.)

---

# ───────── ARCHIV: frühere Sessions ─────────


## Letzte Session
**Datum:** 23. Mai 2026 (Helper-V3-Methodik-Erweiterung + erster Validity-Run)

## Was wurde gemacht
- **HELPER-V3.md erweitert** (_dev/HELPER-V3.md, 12,5 KB → 21,5 KB): Neue **Stufe 0 — Artefakt-Typ bestimmt den Review-Fokus** (5 Typen: Content-Page / Tool / Funnel / Posting / Strategie). Pro Nicht-Content-Typ eine Validity-Linse:
  - Tool → Outcome-Validity (Tool adversarial *bedienen*, 6 Kern-Fragen, 3 Fehl-Input-Durchläufe)
  - Funnel → Promise-Delivery + Dark-Pattern
  - Posting → Claim + Pietät/Brand + Plattform-Policy
  - Strategie → Prämissen-Audit + Pre-Mortem (gefährlichster Typ, Sycophancy-Risiko)
  - Prinzip: Validity-Linse ist Pflicht, Dispatch-Loop skaliert mit Aufwand. Anti-Score-Anchoring gilt überall.
- **Erster echter Validity-Run** über tools/angebotspruefer/ → **VALIDITY_FAIL (3/3)**. Befund dokumentiert in `_dev/audit/angebotspruefer-validity-fail-2026-05-23.md`.

## Nächste Schritte
- **Angebotsprüfer Writer-Pass** (Tool ist LIVE mit dem FAIL): Preis nie allein ROT (Vollständigkeit = Anker, Preis max. GELB); Summen-Bezugsgröße definieren; Posten-Check als Klärungs- statt Vollständigkeits-Audit; Pauschale nicht abstrafen. KEIN Stadt/Friedhof-Ausbau.
- Optional: Validity-Run in separatem Tab gegen Live-URL gegenchecken (wasserdichter Sycophancy-Schutz).
- HELPER-V3 "Adversarial-Fundtypen"-Sektion um Tool/Funnel/Posting/Strategie-Fälle ergänzen, sobald echte Fälle da sind.

## Offene Fragen
- Soll der Funnel-Conversion-Check ausformuliert werden (aktuell nur Linse skizziert)?
