/**
 * machsruhig.de — Tracking & Analytics
 *
 * Plausible Analytics (cookieless, DSGVO-konform)
 * + Custom Events für erweiterte Analyse
 *
 * Diese Datei enthält:
 *  - Plausible-Queue-Init (vormals Inline-Script im HTML, zentralisiert)
 *  - Custom-Event-Logik
 *
 * Events (PBI-19):
 * - cta_click: Klick auf einen CTA-Button/Link
 * - scroll_50 / scroll_75: Scroll-Tiefe 50% / 75%
 * - tool_step: Schritt in einem Tool abgeschlossen
 * - tool_export: Tool-Ergebnis exportiert (Druck/PDF)
 * - lead_qualified: Lead-Formular abgeschickt
 * - faq_open: FAQ-Akkordeon geöffnet
 */

// Plausible Queue-Init (wenn Plausible-Script noch nicht geladen ist, puffern wir Events)
window.plausible = window.plausible || function() { (window.plausible.q = window.plausible.q || []).push(arguments); };

(function() {
  'use strict';

  // Plausible event helper (graceful fallback wenn Plausible nicht geladen)
  function track(eventName, props) {
    if (typeof window.plausible === 'function') {
      window.plausible(eventName, { props: props || {} });
    }
    // Debug-Modus: auskommentieren für Produktion
    // console.log('[mr-track]', eventName, props);
  }

  // === CTA Clicks ===
  // Trackt Klicks auf Elemente mit data-track="cta" oder class "cta-primary" / "cta-safety"
  document.addEventListener('click', function(e) {
    var el = e.target.closest('[data-track="cta"], .cta-primary, .cta-safety, .mr-cta-block a, .mr-lead-cta a');
    if (el) {
      track('cta_click', {
        text: (el.textContent || '').trim().substring(0, 60),
        href: el.getAttribute('href') || '',
        page: window.location.pathname
      });
    }
  });

  // === Scroll-Tiefe ===
  var scrolled50 = false;
  var scrolled75 = false;

  function checkScroll() {
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    var docHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (docHeight <= 0) return;
    var pct = (scrollTop / docHeight) * 100;

    if (!scrolled50 && pct >= 50) {
      scrolled50 = true;
      track('scroll_50', { page: window.location.pathname });
    }
    if (!scrolled75 && pct >= 75) {
      scrolled75 = true;
      track('scroll_75', { page: window.location.pathname });
      // Nach 75% brauchen wir nicht mehr zu lauschen
      window.removeEventListener('scroll', onScroll);
    }
  }

  var scrollTimer = null;
  function onScroll() {
    if (scrollTimer) return;
    scrollTimer = setTimeout(function() {
      scrollTimer = null;
      checkScroll();
    }, 200); // Throttle auf 200ms
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  // === FAQ Opens ===
  document.addEventListener('toggle', function(e) {
    if (e.target.tagName === 'DETAILS' && e.target.open) {
      var summary = e.target.querySelector('summary');
      track('faq_open', {
        question: summary ? summary.textContent.trim().substring(0, 80) : '',
        page: window.location.pathname
      });
    }
  }, true);

  // === Tool Events (global API für React-Tools) ===
  // React-Tools können diese Funktionen aufrufen:
  // window.mrTrack.toolStep(stepName, stepNumber)
  // window.mrTrack.toolExport(toolName, exportType)
  // window.mrTrack.leadQualified(formName, city)
  window.mrTrack = {
    toolStep: function(stepName, stepNumber) {
      track('tool_step', {
        step: stepName,
        step_number: stepNumber,
        page: window.location.pathname
      });
    },
    toolExport: function(toolName, exportType) {
      track('tool_export', {
        tool: toolName,
        type: exportType || 'print',
        page: window.location.pathname
      });
    },
    leadQualified: function(formName, city) {
      track('lead_qualified', {
        form: formName || 'bestatter-anfrage',
        city: city || '',
        page: window.location.pathname
      });
    },
    // Affiliate-Klick-Tracking (Monetarisierung)
    affiliateClick: function(provider, product, position) {
      track('affiliate_click', {
        provider: provider || '',
        product: product || '',
        position: position || '',
        page: window.location.pathname
      });
    },
    // Vorsorge-Conversion-Tracking
    vorsorgeStart: function(toolName) {
      track('vorsorge_start', {
        tool: toolName || '',
        page: window.location.pathname
      });
    },
    // Cross-Link-Tracking (interne Verlinkung)
    crossLink: function(from, to) {
      track('cross_link', {
        from: from || window.location.pathname,
        to: to || '',
        page: window.location.pathname
      });
    }
  };

  // === Affiliate-Link Tracking (automatisch) ===
  // Trackt Klicks auf externe Links mit data-affiliate oder rel="sponsored"
  document.addEventListener('click', function(e) {
    var el = e.target.closest('[data-affiliate], [rel="sponsored"], .mr-affiliate-link');
    if (el) {
      window.mrTrack.affiliateClick(
        el.getAttribute('data-affiliate') || '',
        el.getAttribute('data-product') || el.textContent.trim().substring(0, 40),
        el.getAttribute('data-position') || ''
      );
    }
  });

  // === Vorsorge CTA Tracking ===
  document.addEventListener('click', function(e) {
    var el = e.target.closest('.mr-vorsorge-cta a, [data-track="vorsorge"]');
    if (el) {
      window.mrTrack.vorsorgeStart(
        el.getAttribute('data-tool') || el.textContent.trim().substring(0, 40)
      );
    }
  });

})();
