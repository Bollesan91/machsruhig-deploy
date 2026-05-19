// Browser-MCP Send-Helper V3 — Single-shot smart-dispatch for claude.ai (May 2026 DOM)
//
// API:
//   __mcp.run(prompt, label, opts) → starts task, returns 'STARTED'
//   __mcp.status() → returns {phase, label, elapsed, error?, responseLen?}
//   __mcp.lastResult() → returns last completed response text (or null)
//
// Phases: 'idle' → 'sending' → 'streaming' → 'complete' | 'failed'
//
// V3 selectors (verified May 2026):
//   • Send-Button: button[aria-label*="Send"/"senden"]  (still works)
//   • User-Message: [data-testid="user-message"]
//   • Response-Complete-Signal: [data-testid="action-bar-copy"] count > initial
//     (each fully-rendered message — user + assistant — gets a copy button)
//   • Response-Text: last [data-testid="action-bar-copy"] container,
//     stripping "Claude hat geantwortet: " / "Claude responded: " prefix
//
// V3 improvements:
//   • Detects completion via action-bar-copy DOM-mutation (robust)
//   • Strips claude.ai aria-label echo from response text
//   • Background-tab tolerant (uses Date.now() wall-clock)

(function() {
  if (window.__mcp && window.__mcp.version === 3) return;

  const log = (state, m) => {
    state.log.push(`[+${Date.now() - state.startTime}ms] ${m}`);
    if (state.log.length > 50) state.log.shift();
  };

  window.__mcp = {
    version: 3,
    state: { phase: 'idle', label: null, startTime: null, error: null, lastResponse: null, log: [] },

    status: function() {
      const s = this.state;
      return {
        phase: s.phase, label: s.label,
        elapsed: s.startTime ? Date.now() - s.startTime : 0,
        error: s.error,
        responseLen: s.lastResponse ? s.lastResponse.length : 0,
        logTail: s.log.slice(-8)
      };
    },

    lastResult: function() { return this.state.lastResponse; },

    findSendBtn: function() {
      return [...document.querySelectorAll('button')].find(b => {
        const al = (b.getAttribute('aria-label') || '').toLowerCase();
        return (al.includes('send') || al.includes('senden')) && !al.includes('stop');
      });
    },

    copyBtns: function() {
      return document.querySelectorAll('[data-testid="action-bar-copy"]');
    },

    extractResponse: function() {
      // The last action-bar-copy button's nearest ancestor with substantial text is the response container
      const btns = [...this.copyBtns()];
      if (btns.length === 0) return '';
      const lastBtn = btns[btns.length - 1];
      // Walk up to find a container with substantial innerText
      let el = lastBtn;
      for (let i = 0; i < 8; i++) {
        el = el.parentElement;
        if (!el) break;
        const t = (el.innerText || '').trim();
        // Container must have response content (not just buttons/labels)
        if (t.length > 30) {
          // Strip claude.ai aria-label prefix
          return t
            .replace(/^Claude hat geantwortet:\s*/i, '')
            .replace(/^Claude responded:\s*/i, '')
            .trim();
        }
      }
      // Fallback: just return last button container text
      return (lastBtn.parentElement?.innerText || '').trim();
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
      a.href = url; a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(() => URL.revokeObjectURL(url), 5000);
    },

    run: function(prompt, label, opts) {
      opts = opts || {};
      const sendTimeoutMs = opts.sendTimeoutMs || 120000;
      const streamTimeoutMs = opts.streamTimeoutMs || 300000;
      const autoDownload = opts.autoDownload !== false;

      this.state = {
        phase: 'sending', label, startTime: Date.now(),
        error: null, lastResponse: null, log: []
      };

      const self = this;
      const s = self.state;

      (async () => {
        try {
          // 1. Wait for input
          log(s, 'wait input');
          let ce = null;
          for (let i = 0; i < 30; i++) {
            ce = document.querySelector('[contenteditable="true"]');
            if (ce) break;
            await new Promise(r => setTimeout(r, 300));
          }
          if (!ce) throw new Error('no input');

          // 2. Clear + type
          self.clearInput();
          await new Promise(r => setTimeout(r, 200));
          self.typePrompt(prompt);
          log(s, `typed ${prompt.length}c`);
          await new Promise(r => setTimeout(r, 600));

          // 3. Smart-send: click + verify user-message DOM mutation
          const initialUserCount = document.querySelectorAll('[data-testid="user-message"]').length;
          const initialCopyCount = self.copyBtns().length;
          const tSend = Date.now();
          const retries = [3000, 8000, 20000];
          let retryIdx = 0;
          let sent = false;

          while (Date.now() - tSend < sendTimeoutMs && !sent) {
            const btn = self.findSendBtn();
            if (!btn) { log(s, 'no-btn'); await new Promise(r => setTimeout(r, 1000)); continue; }
            if (btn.disabled) {
              const w = retries[Math.min(retryIdx, retries.length - 1)];
              log(s, `disabled wait${w}`);
              await new Promise(r => setTimeout(r, w));
              retryIdx++;
              continue;
            }

            btn.click();
            log(s, `click#${retryIdx + 1}`);

            // Verify
            const tV = Date.now();
            while (Date.now() - tV < 4000) {
              if (document.querySelectorAll('[data-testid="user-message"]').length > initialUserCount) {
                sent = true; break;
              }
              await new Promise(r => setTimeout(r, 300));
            }
            if (sent) break;

            // Re-type if input got cleared
            const curText = (document.querySelector('[contenteditable="true"]')?.innerText || '').trim();
            if (curText.length < 10) {
              log(s, 're-type');
              self.typePrompt(prompt);
              await new Promise(r => setTimeout(r, 600));
            }
            const w = retries[Math.min(retryIdx, retries.length - 1)];
            await new Promise(r => setTimeout(r, w));
            retryIdx++;
          }

          if (!sent) throw new Error(`send-timeout (${retryIdx} att)`);

          // 4. Streaming: wait for copy-btn count to grow by 2 (user-msg copy + assistant-msg copy)
          s.phase = 'streaming';
          log(s, `stream start (initialCopy=${initialCopyCount})`);

          const tStream = Date.now();
          let lastCount = initialCopyCount;
          let lastChangeAt = tStream;
          const targetCount = initialCopyCount + 2; // user + assistant copy-buttons

          while (Date.now() - tStream < streamTimeoutMs) {
            const curCount = self.copyBtns().length;
            if (curCount >= targetCount) {
              // Stream complete!
              log(s, `complete copy=${curCount}`);
              break;
            }
            if (curCount !== lastCount) {
              lastCount = curCount;
              lastChangeAt = Date.now();
            }
            await new Promise(r => setTimeout(r, 800));
          }

          if (self.copyBtns().length < targetCount) {
            throw new Error(`stream-timeout (copy=${self.copyBtns().length}, want=${targetCount})`);
          }

          // Give it 1s extra to fully render
          await new Promise(r => setTimeout(r, 1000));

          // 5. Extract response
          const responseText = self.extractResponse();
          log(s, `extract ${responseText.length}c`);
          s.lastResponse = responseText;

          // 6. Auto-download
          if (autoDownload && responseText) {
            self.downloadBlob(responseText, `${label}.txt`);
            log(s, `DL ${label}.txt`);
          }

          s.phase = 'complete';
          log(s, 'DONE');
        } catch (e) {
          s.phase = 'failed';
          s.error = e.message;
          log(s, `FAIL ${e.message}`);
        }
      })();

      return 'STARTED';
    }
  };
})();
