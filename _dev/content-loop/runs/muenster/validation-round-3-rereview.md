Ich hole die Datei und prüfe.

Fetching site
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/muenster/index.html?cb=1779089315321

STADT: Münster

VERDICT: FAIL — 2 MAJOR-Issues blockieren Deploy.

FUND 1 — JSX-Syntax kaputt (Deploy-Blocker, kritisch): Die LeadForm-Komponente nutzt style={...} mit Object-Literalen, denen die äußeren geschweiften Klammern fehlen. Korrekt wäre style={{textAlign:'center',...}} — vorhanden ist nur style={textAlign:'center',...}. Das ist kein gültiges JSX und wird vom Babel-Standalone-Compiler im Browser mit einem SyntaxError abgebrochen → Lead-Formular rendert nicht, Lead-Capture = 0. Betrifft alle 8 Stellen im <script type="text/babel">-Block (submitted-View + alle Inputs/Selects/Button). Dies ist exakt der bekannte „Babel/client-side JSX invisible to Google + broken at runtime"-Pattern aus den 9 bereits behobenen Blockers — Regression an genau dieser Seite.

FUND 2 — CSS-Block strukturell zerstört: Der @media print-Block ab @media print{.no-print,.mr-nav, wird nie geschlossen. Stattdessen sind ab dort .mr-nav-divider, .mr-nav-toggle und ein zweiter geschachtelter @media(max-width:640px)-Block doppelt eingefügt (waren oben schon definiert) — und der äußere @media print schließt erst ganz am Ende mit .mr-footer{display:none}}. Folge: Im Print-Modus werden Navigation-Toggle-Styles & Mobile-Menü-Regeln als Print-Regeln interpretiert, regulärer Screen-Code bleibt aber funktional (weil oben schon korrekt definiert). Kein User-facing Crash, aber Audit-Score-relevant und Symptom eines fehlerhaften Bulk-Replace.

Empfehlung: Beide Funde via Cross-City-Check auf andere Pass-2-Seiten prüfen — Fund 1 ist mit hoher Wahrscheinlichkeit nicht Münster-spezifisch.