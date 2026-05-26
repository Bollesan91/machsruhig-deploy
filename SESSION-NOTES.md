# Session-Notizen

## Letzte Session
**Datum:** 26. Mai 2026 (Abend/Nacht — Tools-Validity-Sweep + 6-Iter-Rebuild + Deploy)

## Was wurde gemacht
- **Audit + Validity-Sweep 3 Tools (Vorsorge-Check, Kostenrechner, Bestattungskosten-Rechner):** Initial-Audit via Helper-V3 Multi-Chat-Pipeline → 3 × `VALIDITY_FAIL`. Gleiche Pathologie-Klasse wie der Angebotsprüfer (Bezugsgröße + Anspruch>Datenbasis + Fehler-Asymmetrie). Audit-Doc: `_dev/audit/validity-tools-sweep-2026-05-26.md`.

- **P0-Versicherung (commit 8e04c46):** 3 Tools auf `noindex,nofollow` + Warn-Banner + 12 Body-CTA-Blöcke auf 10 Trust-Pages auf Fallback-Ratgeber umgeleitet. Pattern analog Angebotsprüfer-P0 (35c4008).

- **Tool-Rebuild über 6 Helper-V3-Iterationen (Branch-Trick auf `content-loop-pipeline`):**
  - **Iter-1 (Writer-Chat):** Vorsorge-Check v1 — Wirksamkeits-Selbstchecks pro Doc, Headline entkoppelt von missing.length (Reframe „N von M benannt"), Taxonomie erweitert (Unverheiratet-Slot + Auslands-Toggle), Sublabel-Klarheit, § 1777 → § 1782 BGB (Vormundschaftsreform 2023, Writer-Eigeninitiative). Kostenrechner mechanisch: Hero-Label „Bestatter- & Grundleistung", Friedhofsgebühr-Disclaimer, Region-Step-Skip See/Baum/anonym, Floor-Clamp. BKR mechanisch: Vergleichsbox kontextualisiert, Default-Annahmen-Block im Review-Step.
  - **Iter-1.1:** BKR Enum-Bug `'anonym'` → `'anonyme'` (Sparszenario-Branch war tot). Vorsorge-Check: Sorgerechtsverfügung über `hasMinorChildren`-Flag entkoppelt vom Single-Select-Familienstand.
  - **Iter-3:** Kostenrechner 5-Ebenen Punkt 5 (Doppelzähl-Falle: behauptete „Ebenen 1+2" obwohl auch Trauerfeier+Grabstein drin). Vorsorge-Check `isInScope`-Logik EXKLUSIV via `hasMinorChildren`-Flag (sorgerechtsverfuegung.situation:[]).
  - **Iter-4:** Banner-Stale auf allen 3 Tools (P0-Warnungen waren obsolet, sagten Bugs die längst gefixt waren) → durch neutrale `role="note"`-Scope-Hinweise ersetzt. Vorsorge-Check Restart-Leak (hasMinorChildren wurde nicht zurückgesetzt) + Prefill-Tatsachenbehauptung entfernt.
  - **Iter-5:** Kostenrechner Phantom-Region in „Deine Auswahl"-Tabelle + Print/Copy bei See/Baum/anonym (Region-Skip nur halb umgesetzt) — zus-Array conditional aufgebaut.
  - **Iter-6 Kontroll-Audit:** Regressions-Check Kostenrechner-Fix — kein neuer Bug, Border-Logik arraylängen-relativ, Berechnung entkoppelt, Print-Hygiene intakt.

- **Finale Validity-Verdicts (alle drei PASS):** Vorsorge-Check ✅ (Iter-5), Kostenrechner ✅ (Iter-6), Bestattungskosten-Rechner ✅ (Iter-5).

- **P0-Rollback (in dieser Session):** noindex,nofollow → index,follow auf allen 3 Tools, P0-Kommentar entfernt. 12 Body-CTA-Blöcke auf 10 Trust-Pages aus pre-P0-Stand (483c9f1) restored — direkte Tool-Links statt Fallback-Ratgeber. Neutraler Scope-Hinweis im Tool-Body bleibt (informativ, nicht warnend).

- **Deploy (Welle 1):** main aktualisiert mit content-loop-pipeline (Merge-Commit 5a2457b) + P0-Rollback (Commit 4f98ff7). Push löst Netlify-Deploy aus.

- **Hygiene-Welle (Commit 0b158d4):** 
  - Sitemap +9 URLs (Angebotsprüfer + 8 Cluster-Pages), 100→109
  - _redirects +15 /ratgeber/-Regeln (Stadt-Pages-Cleanup, 4 echte Mappings + 10 best-fit + catch-all)
  - vorsorge/index.html +6 Cards (Bestattungsvorsorge, Sorgerechtsverfügung, Digitaler Nachlass, Vorsorge-allein-leben, Sozialbestattung, Ohne-Vorsorge) — Hub jetzt 10 Cards total
  - sozialbestattung.html Quellenliste +2 BSG-Az (B 8 SO 20/10 R + B 8 SO 20/22 R) + VG-Münster als verlinkte Quellen
  - Lübeck/Mönchengladbach Cross-Canonical-Schleife behoben (Umlaut-Hauptversionen jetzt self-canonical statt zur noindex-ASCII zu zeigen)

- **Polish-Welle (Tool-Optional-Findings) — Helper-V3 GO_LIVE PASS:**
  - bestattungskosten.html: Inline-Link "Pillar-Ratgeber Sozialbestattung" nach Sozial-Section
  - beerdigung-planen.html: Inline-Link "Pillar Vorsorge allein leben"
  - BKR: Sarg-Multiplier-Cap (qualityMult=1.0) bei See/Baum/anonyme Bestattungsart — Kremationssarg ist Pflicht, "hochwertig 1,4×" macht dort keinen Sinn
  - KR: Floor-Band-Kollaps gefixt — `max = Math.max(floor+200, max)` statt fix `floor+200`. Vorher Spar-Szenario auf 200 €-Breite gestaucht.
  - Validation via 1 Helper-V3-Tab gegen content-loop-pipeline raw-URL (commit 953fc0c), 5/8 Punkte direkt PASS, 3 weitere lokal verifiziert. BSG-Az-Wording B 8 SO 20/22 R gegen BSG-Primärquelle (bsg.bund.de) selbst-verifiziert: korrekt — Urteil betrifft SGB-II-Bezieher, nicht SGB-XII (dejure-Titel war irreführend).



- **Review-Konsolidierung (Commit c1b9159 + Trigger): 7 Punkt-Fakten + Wording-Fixes aus 2 externen Audits.**
  - Datenfehler: Stuttgart 41→42, Hannover 16→19, Bonn Dutzend→40 (FAQ JSON-LD ≡ HTML synchron)
  - Trust: Bremen Fake-Reviewer-Label raus
  - Konsistenz: Homepage 50→48 Städte + ehrliches Vermittlungs-Wording, Berlin H1 Template-konsistent, Köln Du/Sie auf Du
  - NICHT in dieser Welle (eigene Phasen): Akutfall-Hero (6-8h, Phase A), Trustbox+Lead-Form-Disclosure-Komponente (Cross-Page), Schema-Pakete (WebPage+Article statt LocalBusiness), Top-15 Stadt-Pages auf Gold (10-15h pro Stadt), externe Reviewer (Messgate)

## Nächste Schritte (priorisiert, Messgate-Logik)

**Tools — Optional-Findings (kein Validity-FAIL mehr, Phase 2 wenn Bandbreite):**
1. Vorsorge-Check: Testament-Priority „dringend" auch für vermögende Singles (will-an-Patenkind-Fall) statt nur „empfohlen".
2. Vorsorge-Check: Out-of-Scope-Doc verschwindet lautlos (UX-Hinweis).
3. Vorsorge-Check: Fehlt-Tag hartcodiert rot — Severity-Signaling pro Priorität-Stufe differenzieren.
4. Kostenrechner: doppelte Flag-Definition `noRegion`/`_noRegion` → `isRegionlos(ba)`-Helper für DRY.
5. Kostenrechner: Floor-Band-Kollaps (fixe 200 € Breite im Spar-Szenario) — `max = Math.max(floor+200, maxRoh)`.
6. BKR: Sarg-Multiplier-Cap bei See/Baum/anonyme (Kremationssarg-Realismus).
7. BKR: Sparbranch-Text bedingt formulieren (greift derzeit unbedingt — kann bei See+gehoben knapp an Obergrenze).

**Hinter dem Messgate (erst wenn machsleicht-Indexierung beweist, dass Content rankt):**
8. Sozialbestattung: BSG-Az + VG-Münster-Az in Quellenliste verlinken (~10 Min, Soft-Polish offen aus früherer Session).
9. Lead-Funnel + Einwilligung sauber.
10. Autoren-/Redaktionsprofil + Trust.
11. Welle E (Tier-Bestattung, Auswanderer, Patchwork-Familie).

## Offene Fragen
- Keine akuten. 3 Tools strukturell durch Helper-V3-Adversarial-Audit (6 Iterationen) gegangen, alle VALIDITY_PASS, live ab diesem Deploy. Optional-Findings für Phase 2 dokumentiert.

---

# ───────── ARCHIV: frühere Sessions ─────────

## Session
**Datum:** 26. Mai 2026 (Abend — Angebotsprüfer-Rebuild v2.4 + ASCII-Canonical-Fix LIVE)

## Was wurde gemacht
- **Angebotsprüfer v2.4 LIVE, Validity-PASS:** Internes VALIDITY_FAIL (3/3) durch unabhängigen Helper-V3-Audit (frischer Chrome-Tab gegen Live-URL) bestätigt → 5 Iterationen Rebuild (v2 → v2.4-Polish). v2.4 hat im finalen Fresh-Tab-Audit (Tab 1532777164) bestanden. Kern-Änderungen: SEPARAT_KOSTEN-Logik (Friedhofsgebühren raus aus Range), INFO_POSTEN-Konstante (Grabstein/Grabpflege ohne Range-Abzug), pflicht-Flag aktiviert, Pauschale nicht abgestraft, ROT nur bei kumuliertem Risiko (sumRatio<0.3 AND klärungsRatio>=0.7 AND !userHasExplained), High-Side-ROT bei >=2x, YMYL-Wording ("Lockangebot" raus → neutrale Klärungs-Sprache).
- **P0-Versicherung während Rebuild:** Tool noindex + 16 CTAs (8 Seiten × 2) neutralisiert während v2-Bauphase, nach v2.3-Pass sauberer Rollback.
- **ASCII-Canonical-Fix:** `bestatter/luebeck/` + `bestatter/moenchengladbach/` ASCII-Stubs zeigen jetzt percent-encoded canonical auf Umlaut-Hauptversion (`l%C3%BCbeck` / `m%C3%B6nchengladbach`). Commit `123bb90`.
- **Cluster × v2.4 Konsistenz-Sweep + Page-5-Body-Rewrite + Welle C Sozialbestattung + Welle D Vorsorge-allein-leben** — siehe Git-History für Details.

---

# ───────── (Ältere Archive gekürzt — siehe Git-History) ─────────
