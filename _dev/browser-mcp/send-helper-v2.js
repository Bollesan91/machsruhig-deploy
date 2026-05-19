// Browser-MCP Send-Helper V2 — Single-shot smart-dispatch for claude.ai
//
// API:
//   __mcp.run(prompt, label, opts) → starts task, returns 'STARTED'
//   __mcp.status() → returns {phase, label, elapsed, error?, responseLen?}
//   __mcp.lastResult() → returns last completed response text (or null)
//
// Phases: 'idle' → 'sending' → 'streaming' → 'complete' | 'failed'
//
// Improvements over V1:
//   • Button.disabled-Check (statt brüchigem "Zu viele Antworten"-Text-Scan)
//   • Input-Clear vor Retry (kein Doppel-Insert)
//   • User-Message-DOM-Verify (Click hat tatsächlich gesendet?)
//   • Auto-Download bei Completion (Stop-Button verschwindet + 2s stabil)
//   • Exponential Backoff bei Cap-Block (3s → 8s → 20s, max 3 retries)
//   • Background-Tab-Tolerant (verwendet Wall-Clock statt setTimeout-counts)

(function() {
  if (window.__mcp && window.__mcp.version === 2) {
    console.log('__mcp v2 already installed');
    return;
  }

  window.__mcp = {
    version: 2,
    state: { phase: 'idle', label: null, startTime: null, error: null, lastResponse: null, log: [] },

    log: function(m) {
      this.state.log.push(`[+${Date.now() - (this.state.startTime || Date.now())}ms] ${m}`);
      if (this.state.log.length > 50) this.state.log.shift();
    },

    status: function() {
      const s = this.state;
      const elapsed = s.startTime ? Date.now() - s.startTime : 0;
      return {
        phase: s.phase, label: s.label, elapsed,
        error: s.error,
        responseLen: s.lastResponse ? s.lastResponse.length : 0,
        logTail: s.log.slice(-6)
      };
    },

    lastResult: function() { return this.state.lastResponse; },

    findSendBtn: function() {
      return [...document.querySelectorAll('button')].find(b => {
        const al = (b.getAttribute('aria-label') || '').toLowerCase();
        return (al.includes('send') || al.includes('senden')) && !al.includes('stop');
      });
    },

    findStopBtn: function() {
      return document.querySelector('button[aria-label*="Stop"]');
    },

    clearInput: function() {
      const ce = document.querySelector('[contenteditable="true"]');
      if (!ce) return false;
      ce.focus();
      const sel = window.getSelection();
      const range = document.createRange();
      range.selectNodeContents(ce);
      sel.removeAllRanges();
      sel.addRange(range);
      document.execCommand('selectAll', false);
      document.execCommand('delete', false);
      return true;
    },

    typePrompt: function(text) {
      const ce = document.querySelector('[contenteditable="true"]');
      if (!ce) return false;
      ce.focus();
      const sel = window.getSelection();
      const range = document.createRange();
      range.selectNodeContents(ce);
      range.collapse(false);
      sel.removeAllRanges();
      sel.addRange(range);
      document.execCommand('insertText', false, text);
      return true;
    },

    downloadBlob: function(text, filename) {
      const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(() => URL.revokeObjectURL(url), 5000);
    },

    run: function(prompt, label, opts) {
      opts = opts || {};
      const sendTimeoutMs = opts.sendTimeoutMs || 120000;   // 2 min for cap to clear
      const streamTimeoutMs = opts.streamTimeoutMs || 300000; // 5 min for full response
      const stableMs = opts.stableMs || 2000;
      const autoDownload = opts.autoDownload !== false;

      // Reset state
      this.state = {
        phase: 'sending', label, startTime: Date.now(),
        error: null, lastResponse: null, log: []
      };

      const self = this;
      const log = (m) => self.log(m);

      (async () => {
        try {
          // 1. Wait for input element to be ready
          log('waiting for input element');
          let ce = null;
          for (let i = 0; i < 30; i++) {
            ce = document.querySelector('[contenteditable="true"]');
            if (ce) break;
            await new Promise(r => setTimeout(r, 300));
          }
          if (!ce) throw new Error('No contenteditable input found');

          // 2. Clear input + type prompt
          self.clearInput();
          await new Promise(r => setTimeout(r, 200));
          self.typePrompt(prompt);
          log(`typed prompt (${prompt.length} chars)`);
          await new Promise(r => setTimeout(r, 600));

          // 3. Smart-send with retries
          const initialUserCount = document.querySelectorAll('[data-testid="user-message"]').length;
          const tSend = Date.now();
          const retries = [3000, 8000, 20000]; // backoff for re-attempts
          let retryIdx = 0;
          let sent = false;

          while (Date.now() - tSend < sendTimeoutMs && !sent) {
            const btn = self.findSendBtn();
            if (!btn) { log('no send btn yet'); await new Promise(r => setTimeout(r, 1000)); continue; }
            if (btn.disabled) {
              const wait = retries[Math.min(retryIdx, retries.length - 1)];
              log(`btn disabled, wait ${wait}ms`);
              await new Promise(r => setTimeout(r, wait));
              retryIdx++;
              continue;
            }

            btn.click();
            log(`clicked send (attempt ${retryIdx + 1})`);

            // Verify: wait up to 4s for user-message DOM
            const tVerify = Date.now();
            while (Date.now() - tVerify < 4000) {
              if (document.querySelectorAll('[data-testid="user-message"]').length > initialUserCount) {
                sent = true; break;
              }
              await new Promise(r => setTimeout(r, 300));
            }

            if (sent) break;

            // Not sent — input may have been cleared by claude.ai. Re-type if input is empty.
            log('not sent after click, checking input');
            const curText = (document.querySelector('[contenteditable="true"]')?.innerText || '').trim();
            if (curText.length < 10) {
              log('input was cleared, re-typing');
              self.typePrompt(prompt);
              await new Promise(r => setTimeout(r, 600));
            }
            const wait = retries[Math.min(retryIdx, retries.length - 1)];
            log(`retry in ${wait}ms`);
            await new Promise(r => setTimeout(r, wait));
            retryIdx++;
          }

          if (!sent) throw new Error('Send-Timeout (max ' + (sendTimeoutMs/1000) + 's, ' + (retryIdx) + ' attempts)');

          // 4. Streaming phase: wait for Stop-Button to appear then disappear
          self.state.phase = 'streaming';
          log('streaming started');

          const tStream = Date.now();
          // Wait for stop button (might appear quickly or not at all if quick response)
          let stopSeen = false;
          for (let i = 0; i < 20; i++) {
            if (self.findStopBtn()) { stopSeen = true; break; }
            await new Promise(r => setTimeout(r, 500));
          }

          // Now wait for stop button to disappear + stable for stableMs
          let lastSeenStop = stopSeen ? Date.now() : 0;
          while (Date.now() - tStream < streamTimeoutMs) {
            if (self.findStopBtn()) {
              lastSeenStop = Date.now();
            } else if (lastSeenStop && Date.now() - lastSeenStop > stableMs) {
              break; // Stop button gone for stableMs → response complete
            }
            await new Promise(r => setTimeout(r, 500));
          }

          log('streaming complete');

          // 5. Extract response text — last assistant message
          // claude.ai uses various class names; try multiple
          const candidates = [
            ...document.querySelectorAll('[class*="font-claude-message"]'),
            ...document.querySelectorAll('article'),
            ...document.querySelectorAll('[data-testid*="message"]:not([data-testid="user-message"])')
          ];
          // Pick the very last one
          const lastMsg = candidates[candidates.length - 1];
          const responseText = lastMsg ? lastMsg.innerText : '';
          log(`extracted ${responseText.length} chars`);

          self.state.lastResponse = responseText;

          // 6. Auto-download
          if (autoDownload && responseText) {
            self.downloadBlob(responseText, `${label}.txt`);
            log(`downloaded as ${label}.txt`);
          }

          self.state.phase = 'complete';
          log('TASK COMPLETE');

        } catch (e) {
          self.state.phase = 'failed';
          self.state.error = e.message;
          log(`FAILED: ${e.message}`);
        }
      })();

      return 'STARTED';
    }
  };

  console.log('__mcp v2 installed');
})();
