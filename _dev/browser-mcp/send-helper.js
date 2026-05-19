// Robust send-helper for claude.ai via Browser-MCP
// Solves: concurrency-block, send-button-timing, return-value-race
//
// USAGE in browser-MCP javascript_tool:
//   window.__sendPrompt(PROMPT_TEXT).then(r => window.__r = r)
//   ... later check: window.__r
//
// Or inline:
//   (() => { ... see below ... })()

window.__sendPrompt = async function(promptText, opts = {}) {
  const {
    maxWaitMs = 30000,         // wait up to 30s for concurrency to clear
    pollIntervalMs = 1500,     // recheck every 1.5s
    typeDelayMs = 600,         // pause after typing before clicking
    verifySent = true,         // wait for user-message DOM after click
    verifyTimeoutMs = 8000     // wait up to 8s to verify
  } = opts;

  const log = (m) => { window.__sendLog = (window.__sendLog || []); window.__sendLog.push(`[${Date.now()}] ${m}`); };
  
  // 1. Find input (contenteditable)
  const ce = document.querySelector('[contenteditable="true"]');
  if (!ce) return { status: 'NO_INPUT', err: 'No contenteditable element found' };

  // 2. Insert text
  ce.focus();
  const sel = window.getSelection();
  const range = document.createRange();
  range.selectNodeContents(ce);
  range.collapse(false);
  sel.removeAllRanges();
  sel.addRange(range);
  document.execCommand('insertText', false, promptText);
  log('typed');
  
  await new Promise(r => setTimeout(r, typeDelayMs));

  // 3. Find send button — claude.ai uses aria-label containing "send" or "senden"
  const findBtn = () => [...document.querySelectorAll('button')].find(b => {
    const al = (b.getAttribute('aria-label') || '').toLowerCase();
    return (al.includes('send') || al.includes('senden')) && !al.includes('stop');
  });

  // 4. Concurrency-check loop: detect "Zu viele Antworten" + wait until input is sendable
  const hasConcurrencyBlock = () => /zu viele antworten|too many|capacity/i.test(document.body.innerText.slice(-3000));
  
  const initialUserMsgCount = document.querySelectorAll('[data-testid="user-message"]').length;
  
  const t0 = Date.now();
  let attempts = 0;
  while (Date.now() - t0 < maxWaitMs) {
    attempts++;
    
    // Check concurrency block
    if (hasConcurrencyBlock()) {
      log(`attempt ${attempts}: concurrency-block detected, waiting ${pollIntervalMs}ms`);
      await new Promise(r => setTimeout(r, pollIntervalMs));
      continue;
    }
    
    // Try to find + click send button
    const btn = findBtn();
    if (!btn) {
      log(`attempt ${attempts}: no send button found, waiting`);
      await new Promise(r => setTimeout(r, pollIntervalMs));
      continue;
    }
    if (btn.disabled) {
      log(`attempt ${attempts}: send button disabled, waiting`);
      await new Promise(r => setTimeout(r, pollIntervalMs));
      continue;
    }
    
    // Click!
    btn.click();
    log(`attempt ${attempts}: CLICKED at ${Date.now()-t0}ms`);
    
    // Wait a moment for either: user-msg to appear (success) OR concurrency-block to appear (fail)
    await new Promise(r => setTimeout(r, 1200));
    
    if (hasConcurrencyBlock()) {
      log(`attempt ${attempts}: concurrency-block AFTER click, retrying`);
      continue;
    }
    
    if (verifySent) {
      // Wait for user-message DOM to appear
      const tv = Date.now();
      while (Date.now() - tv < verifyTimeoutMs) {
        const cur = document.querySelectorAll('[data-testid="user-message"]').length;
        if (cur > initialUserMsgCount) {
          log(`verified sent (msg count ${initialUserMsgCount} -> ${cur})`);
          return { status: 'SENT', attempts, ms: Date.now()-t0 };
        }
        await new Promise(r => setTimeout(r, 400));
      }
      log('verify timeout — sent but no user-msg DOM');
      return { status: 'SENT_UNVERIFIED', attempts, ms: Date.now()-t0 };
    }
    
    return { status: 'SENT', attempts, ms: Date.now()-t0 };
  }
  
  return { status: 'TIMEOUT', attempts, ms: Date.now()-t0 };
};

console.log('__sendPrompt helper installed');
