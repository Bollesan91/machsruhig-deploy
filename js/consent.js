/* mach's ruhig — Consent-Layer für anonyme Reichweiten-Statistiken
   Lädt Umami + tracking.js NUR nach Opt-In (localStorage 'mr-consent'='accepted').
   Vor Entscheidung: Banner unten. Nach Reject: keine Analytics.
   Stand: 2026-06-05 — nur Umami (cookielos, EU), Ahrefs entfernt. DSGVO/TTDSG-konform. */
(function(){
  'use strict';
  var KEY = 'mr-consent';
  var UMAMI_WEBSITE_ID = '6b6629ff-27b8-427b-863c-76b549cb52ba';

  // Safe no-op shims — ensure window.plausible / window.mrTrack never throw,
  // egal ob Consent gegeben oder nicht
  window.plausible = window.plausible || function(){};
  window.mrTrack = window.mrTrack || function(){};

  function loadAnalytics(){
    // Umami (cookieless, EU-gehostet via cloud.umami.is)
    var u = document.createElement('script');
    u.defer = true;
    u.src = 'https://cloud.umami.is/script.js';
    u.setAttribute('data-website-id', UMAMI_WEBSITE_ID);
    document.head.appendChild(u);
    // Plausible-Shim auf Umami umleiten (manche Tools rufen window.plausible)
    window.plausible = function(e, o){ if (window.umami) window.umami.track(e, (o && o.props) || {}); };
    // Site-internes Event-Routing
    var t = document.createElement('script');
    t.defer = true;
    t.src = '/js/tracking.js';
    document.head.appendChild(t);
  }

  function setConsent(value){
    try { localStorage.setItem(KEY, value); } catch(_){}
    var banner = document.getElementById('mr-consent-banner');
    if (banner) banner.parentNode.removeChild(banner);
    if (value === 'accepted') loadAnalytics();
  }

  function showBanner(){
    if (document.getElementById('mr-consent-banner')) return;
    var b = document.createElement('div');
    b.id = 'mr-consent-banner';
    b.className = 'no-print';
    b.setAttribute('role', 'region');
    b.setAttribute('aria-label', 'Cookie- und Statistik-Einwilligung');
    b.style.cssText = 'position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid #E8E0D6;box-shadow:0 -4px 16px rgba(0,0,0,0.06);padding:16px 20px;z-index:9999;font-family:"DM Sans",system-ui,sans-serif;font-size:14px;line-height:1.5;color:#2D2319';
    b.innerHTML =
      '<div style="max-width:960px;margin:0 auto;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between">' +
        '<div style="flex:1;min-width:260px;color:#5a4f43">' +
          '<strong style="color:#2D2319">Anonyme Reichweiten-Statistiken?</strong> ' +
          'Wir nutzen Umami (cookielos, EU-gehostet), um zu verstehen, was hilft — ohne IP-Speicherung und ohne deine Eingaben. ' +
          'Du kannst widersprechen. <a href="/datenschutz" style="color:#7A6B5D">Mehr Infos</a>.' +
        '</div>' +
        '<div style="display:flex;gap:8px;flex-wrap:wrap">' +
          '<button type="button" id="mr-consent-reject" style="background:transparent;border:1px solid #E8E0D6;border-radius:99px;padding:8px 18px;font-size:14px;cursor:pointer;font-family:inherit;color:#73655A">Ablehnen</button>' +
          '<button type="button" id="mr-consent-accept" style="background:#7A6B5D;border:none;border-radius:99px;padding:8px 22px;font-size:14px;cursor:pointer;font-family:inherit;color:#fff;font-weight:600">Einverstanden</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(b);
    document.getElementById('mr-consent-accept').addEventListener('click', function(){ setConsent('accepted'); });
    document.getElementById('mr-consent-reject').addEventListener('click', function(){ setConsent('rejected'); });
  }

  var current;
  try { current = localStorage.getItem(KEY); } catch(_) { current = null; }

  if (current === 'accepted') {
    loadAnalytics();
  } else if (current === 'rejected') {
    // do nothing — keine Analytics-Loads
  } else {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', showBanner);
    } else {
      showBanner();
    }
  }
})();
