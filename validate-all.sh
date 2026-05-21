#!/bin/bash
# machsruhig.de — Quality Gate Stufe 1
# Läuft alle automatischen Checks vor Go-Live oder Commit.
# Bei FAIL: nicht pushen, erst fixen.

set -e

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

echo "=============================================================="
echo "machsruhig.de — Quality Gate Stufe 1"
echo "=============================================================="
echo

FAIL=0

# --- Check 1: HTML-Syntax-Validität ---------------------------------------
echo "[1/6] HTML-Syntax..."
HTML_ERRORS=0
for f in $(find . -name "*.html" -not -path "./.git/*" -not -path "./_dev/*" -not -path "./templates/*" -not -path "./node_modules/*"); do
  # Python-HTMLParser rudimentäre Syntax-Prüfung
  ERR=$(python3 -c "
from html.parser import HTMLParser
class V(HTMLParser):
    def __init__(s):
        super().__init__()
        s.stack=[]; s.err=0
    def handle_starttag(s,t,a):
        if t not in ('br','hr','img','meta','link','input','area','base','col','embed','source','track','wbr'):
            s.stack.append(t)
    def handle_endtag(s,t):
        if not s.stack:
            s.err+=1
        elif s.stack[-1]!=t:
            s.err+=1
            if t in s.stack:
                while s.stack and s.stack[-1]!=t: s.stack.pop()
                if s.stack: s.stack.pop()
        else:
            s.stack.pop()
v=V()
try:
    v.feed(open('$f').read())
    print(v.err + len(v.stack))
except Exception as e:
    print(99)
" 2>/dev/null || echo 0)
  if [ "$ERR" != "0" ]; then
    echo "  ⚠  $f: $ERR Strukturfehler"
    HTML_ERRORS=$((HTML_ERRORS + 1))
  fi
done
if [ "$HTML_ERRORS" -eq 0 ]; then
  echo "  ✅ Alle HTML-Dateien strukturell valide"
else
  echo "  ❌ $HTML_ERRORS HTML-Dateien mit Strukturfehlern"
  FAIL=$((FAIL + 1))
fi
echo

# --- Check 2: Keine kritischen Platzhalter --------------------------------
echo "[2/6] Keine Platzhalter in Produktions-Seiten..."
PLACEHOLDERS=$(grep -rE '(\[STADT\]|\[BUNDESLAND\]|\[NAME\]|__TODO__|FIXME:|XXX:)' \
  --include="*.html" --exclude-dir=".git" --exclude-dir="_dev" --exclude-dir="templates" \
  --exclude-dir="node_modules" . 2>/dev/null | wc -l)
if [ "$PLACEHOLDERS" -eq 0 ]; then
  echo "  ✅ Keine Platzhalter gefunden"
else
  echo "  ❌ $PLACEHOLDERS Platzhalter in Produktions-Seiten"
  grep -rE '(\[STADT\]|\[BUNDESLAND\]|\[NAME\]|__TODO__|FIXME:|XXX:)' \
    --include="*.html" --exclude-dir=".git" --exclude-dir="_dev" --exclude-dir="templates" \
    --exclude-dir="node_modules" . 2>/dev/null | head -5
  FAIL=$((FAIL + 1))
fi
echo

# --- Check 3: Audit-Score-Prüfung -----------------------------------------
echo "[3/6] Audit-Score-Prüfung..."
python3 _dev/audit-all-pages.py > /dev/null 2>&1 || {
  echo "  ❌ Audit-Skript gescheitert"
  FAIL=$((FAIL + 1))
}
if [ -f "_dev/AUDIT-REPORT.json" ]; then
  AVG=$(python3 -c "import json; print(json.load(open('_dev/AUDIT-REPORT.json'))['meta']['avg_score'])")
  CRIT=$(python3 -c "
import json
r = json.load(open('_dev/AUDIT-REPORT.json'))
crit = [p for p in r['pages'] if any('DEPLOY-BLOCKER' in i for i in p['issues'])]
print(len(crit))
")
  echo "  ℹ  Gesamt-Score: $AVG/100"
  echo "  ℹ  Deploy-Blocker: $CRIT Seiten"
  if [ "$CRIT" -gt 0 ]; then
    echo "  ⚠  Es gibt Seiten mit DEPLOY-BLOCKER — in Phase A beseitigen"
  fi
  # Homepage muss ≥75 sein (harte Grenze)
  HP_SCORE=$(python3 -c "
import json
r = json.load(open('_dev/AUDIT-REPORT.json'))
hp = [p for p in r['pages'] if p['category'] == 'homepage']
print(hp[0]['score'] if hp else 0)
")
  if [ "$HP_SCORE" -lt 75 ]; then
    echo "  ❌ Homepage Audit-Score $HP_SCORE < 75 (Akzeptanzgrenze)"
    FAIL=$((FAIL + 1))
  else
    echo "  ✅ Homepage Audit-Score $HP_SCORE ≥ 75"
  fi
fi
echo

# --- Check 4: Kaputte interne Links ---------------------------------------
echo "[4/6] Interne Links..."
BROKEN=$(python3 -c "
import json
r = json.load(open('_dev/AUDIT-REPORT.json'))
print(r['meta'].get('broken_internal_links', 0))
" 2>/dev/null || echo 0)
if [ "$BROKEN" -eq 0 ]; then
  echo "  ✅ Alle internen Links führen zu existierenden Seiten"
else
  echo "  ⚠  $BROKEN kaputte interne Link-Vorkommnisse gefunden"
  echo "     (Details in _dev/AUDIT-REPORT.json unter 'broken_links')"
  # Kaputte Links sind Warnung, nicht Fail — manchmal gewollt (404-Test etc.)
fi
echo

# --- Check 5: Sitemap-Konsistenz ------------------------------------------
echo "[5/6] Sitemap-Konsistenz..."
if [ -f "sitemap.xml" ]; then
  SITEMAP_ENTRIES=$(grep -c "<loc>" sitemap.xml 2>/dev/null || echo 0)
  # Zähle indexable HTML-Dateien (ohne noindex)
  INDEXABLE=$(find . -name "*.html" \
    -not -path "./.git/*" -not -path "./_dev/*" -not -path "./templates/*" \
    -not -path "./node_modules/*" -not -name "404.html" | while read f; do
      if ! grep -q 'noindex' "$f"; then
        echo "$f"
      fi
    done | wc -l)
  echo "  ℹ  Sitemap: $SITEMAP_ENTRIES Einträge, $INDEXABLE indexierbare HTML-Seiten"
  DIFF=$((INDEXABLE - SITEMAP_ENTRIES))
  if [ "${DIFF#-}" -gt 10 ]; then
    echo "  ⚠  Sitemap weicht stark von Indexable-Count ab (Δ $DIFF)"
  else
    echo "  ✅ Sitemap-Konsistenz plausibel"
  fi
else
  echo "  ❌ sitemap.xml fehlt"
  FAIL=$((FAIL + 1))
fi
echo

# --- Check 6: OG-Image erreichbar -----------------------------------------
echo "[6/6] OG-Image vorhanden..."
OG_IMAGES=$(grep -rohE 'og:image"\s+content="[^"]+"' --include="*.html" \
  --exclude-dir=".git" --exclude-dir="_dev" --exclude-dir="templates" \
  --exclude-dir="node_modules" . 2>/dev/null | grep -oE 'content="[^"]+"' | sort -u)
if [ -z "$OG_IMAGES" ]; then
  echo "  ❌ Kein einziges og:image auf der gesamten Site"
  FAIL=$((FAIL + 1))
else
  MISSING=0
  for img in $(echo "$OG_IMAGES" | grep -oE 'content="[^"]+"' | cut -d'"' -f2); do
    # Normalisieren: absolute URL → lokaler Pfad
    local_path="${img#https://machsruhig.de}"
    local_path="${local_path#/}"
    if [ -z "$local_path" ] || [ ! -f "$local_path" ]; then
      echo "  ⚠  OG-Image nicht lokal gefunden: $img"
      MISSING=$((MISSING + 1))
    fi
  done
  if [ "$MISSING" -eq 0 ]; then
    UNIQUE_COUNT=$(echo "$OG_IMAGES" | wc -l)
    echo "  ✅ Alle OG-Image-Referenzen gültig ($UNIQUE_COUNT Varianten)"
  fi
fi
echo

# --- Zusammenfassung ------------------------------------------------------
echo "=============================================================="
if [ "$FAIL" -eq 0 ]; then
  echo "✅ STUFE 1 PASSED — weiter zu Stufe 2 (Elite Check manuell)"
  echo "=============================================================="
  exit 0
else
  echo "❌ STUFE 1 FAILED — $FAIL kritische Probleme"
  echo "Nicht pushen, erst fixen."
  echo "=============================================================="
  exit 1
fi
