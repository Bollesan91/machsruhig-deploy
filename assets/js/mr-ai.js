// machsruhig.de — Frontend Helper für KI-Text-Generation
// Master-Modul für trauerrede, danksagung, abschiedsbrief
// Privacy: User muss einmalig Opt-in geben (gespeichert in localStorage)
//
// API:
//   window.mrAI.hasConsent()       → boolean
//   window.mrAI.grantConsent()     → setzt localStorage 'mr-ai-consent'
//   window.mrAI.revokeConsent()    → entfernt Consent
//   window.mrAI.generate({type, data}) → Promise<string>
//
// Events (window.dispatchEvent):
//   mr-ai:loading   — start
//   mr-ai:success   — fertig, detail.result
//   mr-ai:error     — fehler, detail.error/detail.retryAfter

(function () {
  'use strict';

  const ENDPOINT = '/.netlify/functions/ai-rede';
  const CONSENT_KEY = 'mr-ai-consent-v1';

  const mrAI = {
    hasConsent() {
      try {
        return localStorage.getItem(CONSENT_KEY) === 'granted';
      } catch (e) {
        return false;
      }
    },

    grantConsent() {
      try {
        localStorage.setItem(CONSENT_KEY, 'granted');
        localStorage.setItem(CONSENT_KEY + '-at', new Date().toISOString());
      } catch (e) {}
    },

    revokeConsent() {
      try {
        localStorage.removeItem(CONSENT_KEY);
        localStorage.removeItem(CONSENT_KEY + '-at');
      } catch (e) {}
    },

    async generate({ type, data, section }) {
      if (!type || !data) {
        throw new Error('type und data sind Pflicht');
      }
      if (!this.hasConsent()) {
        throw new Error('CONSENT_REQUIRED');
      }

      window.dispatchEvent(new CustomEvent('mr-ai:loading', { detail: { type, section } }));

      // Timeout/Abbruch: kein hängender Spinner bei Verbindungsloch (G6).
      // Section-Calls sind kürzer (15s), Vollrede großzügiger (30s).
      const ctrl = new AbortController();
      const timeoutMs = section ? 15000 : 30000;
      const timer = setTimeout(() => ctrl.abort(), timeoutMs);

      try {
        const resp = await fetch(ENDPOINT, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(section ? { type, data, section } : { type, data }),
          signal: ctrl.signal,
        });

        if (resp.status === 429) {
          const body = await resp.json().catch(() => ({}));
          const err = new Error('RATE_LIMIT');
          err.retryAfter = body.retryAfter || 60;
          err.reason = body.error || 'rate_limit';
          window.dispatchEvent(new CustomEvent('mr-ai:error', { detail: err }));
          throw err;
        }

        if (!resp.ok) {
          const body = await resp.json().catch(() => ({}));
          const err = new Error(body.error || `HTTP_${resp.status}`);
          err.status = resp.status;
          err.detail = body.detail;
          window.dispatchEvent(new CustomEvent('mr-ai:error', { detail: err }));
          throw err;
        }

        const body = await resp.json();
        if (!body.result) {
          const err = new Error('EMPTY_RESPONSE');
          window.dispatchEvent(new CustomEvent('mr-ai:error', { detail: err }));
          throw err;
        }

        window.dispatchEvent(new CustomEvent('mr-ai:success', {
          detail: { type, result: body.result, model: body.model },
        }));
        return body.result;
      } catch (err) {
        // Timeout/Abbruch in eine verständliche Meldung übersetzen (G6)
        if (err && err.name === 'AbortError') {
          const tErr = new Error('TIMEOUT');
          tErr.reason = 'timeout';
          window.dispatchEvent(new CustomEvent('mr-ai:error', { detail: tErr }));
          throw tErr;
        }
        if (err.message !== 'CONSENT_REQUIRED' && err.message !== 'RATE_LIMIT' && !err.status) {
          // Network/Parse-Error
          window.dispatchEvent(new CustomEvent('mr-ai:error', { detail: err }));
        }
        throw err;
      } finally {
        clearTimeout(timer);
      }
    },
  };

  window.mrAI = mrAI;
})();
