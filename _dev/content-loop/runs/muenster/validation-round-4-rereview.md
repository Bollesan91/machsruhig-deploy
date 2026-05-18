Ich hole die aktuelle Version und prüfe.

Fetching: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/muenster/index.html?cb=1779089919773
Fetched: https://raw.githubusercontent.com/Bollesan91/machsruhig-deploy/content-loop-pipeline/bestatter/muenster/index.html?cb=1779089919773

STADT: Münster

VERDICT: ❌ FAIL — 2 Deploy-Blocker, JSX-Fix sichtbar, aber Architektur weiterhin SEO-tödlich.

MAJOR-FUND 1: Babel-Client-Side-JSX bleibt — Lead-Formular für Google unsichtbar (P0, Deploy-Blocker) Trotz JSX-Fix wird <LeadForm/> weiterhin via @babel/standalone im Browser kompiliert und in den leeren <div id="lead-form-container"> injiziert. Googlebot rendert das Formular nicht zuverlässig → Hauptconversion-Element fehlt im indexierten HTML. Das ist exakt der Deploy-Blocker, der projektweit schon 9× gefixt wurde. Lösung: serverseitig statisches <form>-Markup inlinen (Hybrid-Architektur, wie für Gold-Cities entschieden), React-Widget nur progressive enhancement.

MAJOR-FUND 2: CSS-Block defekt — @media print schluckt halben Footer/Nav-Reset (P0, Visueller Bug) Im Style-Block ab @media print{.no-print,.mr-nav, fehlt die schließende } des print-Selectors, danach folgen .mr-nav-divider, .mr-nav-toggle und ein zweiter @media(max-width:640px)-Block innerhalb der print-Regel. Folge: Mobile-Nav-Toggle-Styles und Footer-Verstecken werden nur im Druckmodus aktiv, nicht im normalen Viewport. Auf Mobile bricht das Burger-Menü. Re-Check-Script sollte das fangen.

MAJOR-FUND 3: noindex aktiv — Seite wird nicht indexiert <meta name="robots" content="noindex,follow"> blockt jede SEO-Wirkung. Vermerk verweist auf BACKLOG-AUDIT.md (Gold-Template-Upgrade). Solange das steht, ist Pass 4 inhaltlich Makulatur für Ranking. Entscheidung nötig: Münster Gold-Upgrade ziehen oder noindex akzeptiert lassen.

Empfehlung: Nicht deployen. Fund 1+2 sind harte Blocker.