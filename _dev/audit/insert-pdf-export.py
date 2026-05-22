"""
Inject html2pdf.js + 'Als PDF speichern'-Button in 4 Tools.
Setup:
- html2pdf.js via CDN
- MutationObserver pattern, der Button neben existierenden 'Drucken'-Button injiziert
- Per-Tool spezifischer Selector für Export-Content
- Plausible-Tracking 'tool_export'
"""
import os
from pathlib import Path

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
TOOLS = ROOT / "tools"


def build_pdf_script(selector, filename, tool_label):
    return f"""

<!-- PDF-Export via html2pdf.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js" defer></script>
<style>
  .pdf-export-btn{{display:inline-flex;align-items:center;gap:6px;padding:10px 18px;background:#FFFDF9;color:#7A6B5D;border:2px solid #7A6B5D;border-radius:99px;font-weight:600;font-size:14px;cursor:pointer;margin-left:8px;transition:background 0.2s}}
  .pdf-export-btn:hover{{background:#7A6B5D;color:#fff}}
  body.exporting-pdf .mr-nav,body.exporting-pdf .mr-footer,body.exporting-pdf .pdf-export-btn,body.exporting-pdf [class*="export-controls"]{{display:none!important}}
</style>
<script>
(function(){{
  var EXPORT_SELECTOR = {selector!r};
  var FILENAME = {filename!r};
  var TOOL_LABEL = {tool_label!r};
  var injected = false;

  function exportPDF() {{
    var target = document.querySelector(EXPORT_SELECTOR) || document.getElementById('app');
    if (!target || target.children.length === 0) {{
      alert('Bitte erst Tool ausfüllen, dann PDF exportieren.');
      return;
    }}
    if (window.plausible) window.plausible('tool_export', {{ props: {{ type: 'pdf', tool: TOOL_LABEL }} }});
    document.body.classList.add('exporting-pdf');
    var opt = {{
      margin: 12,
      filename: FILENAME + '.pdf',
      image: {{ type: 'jpeg', quality: 0.95 }},
      html2canvas: {{ scale: 2, useCORS: true, logging: false }},
      jsPDF: {{ unit: 'mm', format: 'a4', orientation: 'portrait' }}
    }};
    if (typeof html2pdf === 'undefined') {{
      alert('PDF-Bibliothek lädt noch — bitte einen Moment warten und nochmal versuchen.');
      document.body.classList.remove('exporting-pdf');
      return;
    }}
    html2pdf().set(opt).from(target).save().then(function() {{
      document.body.classList.remove('exporting-pdf');
    }}).catch(function(err) {{
      console.error('PDF-Export-Fehler:', err);
      document.body.classList.remove('exporting-pdf');
      alert('PDF-Export fehlgeschlagen. Bitte versuche es mit der Drucken-Funktion (Drucker: Als PDF speichern).');
    }});
  }}

  function injectButton() {{
    if (injected) return;
    var printBtns = [].slice.call(document.querySelectorAll('button')).filter(function(b) {{
      var t = (b.textContent || '').toLowerCase();
      return t.indexOf('drucken') !== -1 || t.indexOf('print') !== -1;
    }});
    if (printBtns.length === 0) return;
    printBtns.forEach(function(printBtn) {{
      if (printBtn.nextElementSibling && printBtn.nextElementSibling.classList.contains('pdf-export-btn')) return;
      var pdfBtn = document.createElement('button');
      pdfBtn.textContent = 'Als PDF speichern';
      pdfBtn.className = 'pdf-export-btn';
      pdfBtn.type = 'button';
      pdfBtn.onclick = exportPDF;
      printBtn.parentNode.insertBefore(pdfBtn, printBtn.nextSibling);
    }});
    injected = true;
  }}

  // Try immediately + observe DOM for late React-renders
  window.addEventListener('load', injectButton);
  var observer = new MutationObserver(function() {{ injectButton(); }});
  observer.observe(document.body, {{ childList: true, subtree: true }});
}})();
</script>
"""


CONFIGS = {
    "abschiedsbrief": {
        "selector": ".preview-letter",
        "filename": "abschiedsbrief",
        "tool_label": "abschiedsbrief",
    },
    "vorsorge-check": {
        "selector": "#app",
        "filename": "vorsorge-check",
        "tool_label": "vorsorge-check",
    },
    "trauerrede": {
        "selector": "#app",
        "filename": "trauerrede",
        "tool_label": "trauerrede",
    },
    "notfallkarte": {
        "selector": ".nk-card-wrapper",
        "filename": "notfallkarte",
        "tool_label": "notfallkarte",
    },
}


def patch_tool(slug):
    p = TOOLS / slug / "index.html"
    if not p.exists():
        return "missing"
    text = p.read_text(encoding="utf-8", errors="replace")
    cfg = CONFIGS[slug]
    if "html2pdf" in text:
        return "already"
    script = build_pdf_script(cfg["selector"], cfg["filename"], cfg["tool_label"])
    end_body = text.rfind("</body>")
    if end_body == -1:
        return "no-body-close"
    new_text = text[:end_body] + script + text[end_body:]
    p.write_text(new_text, encoding="utf-8")
    return "patched"


for slug in CONFIGS:
    print(f"  {slug}: {patch_tool(slug)}")
