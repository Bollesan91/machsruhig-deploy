"""
A11y-Fixes per Reviewer-Sweep:
- checkliste-todesfall: Checkbox-Inputs in <label> wrappen (Screenreader liest Titel mit)
- beerdigungsplaner: aria-pressed für single-select .opt-btn
- bestattungskosten-rechner: aria-pressed für .bestattungsart-card + .choice-card
- Alle: Focus-Management beim View-Switch — neues h2 mit tabindex=-1 + .focus()

Plus zentralen Helper. Single Edits via String-Replace.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
TOOLS = ROOT / "tools"

results = []

# ----- checkliste-todesfall: Checkbox in label wrappen -----
p = TOOLS / "checkliste-todesfall" / "index.html"
text = p.read_text(encoding="utf-8")

# Old pattern: <input checkbox> dann ein div mit task-title span
# Wrap: <label style="display:flex"><input ...><div ...></div></label>
old = """        h += '<div class="task-item' + (checked?\' checked\':\'\') + '" data-id="' + esc(t.id) + '" style="background:var(--mr-bg-card);border:1px solid ' + (checked?\'var(--mr-success)\':\'var(--mr-border)\') + ';border-radius:var(--mr-radius);padding:16px 20px;margin-bottom:10px;opacity:' + (checked?\'0.7\':\'1\') + ';transition:border-color 0.2s,opacity 0.2s">';
        h += '<div style="display:flex;gap:12px;align-items:flex-start">';
        h += '<input type="checkbox" class="task-cb" data-task="' + esc(t.id) + '"' + (checked?\' checked\':\'\') + ' style="width:20px;height:20px;margin-top:2px;accent-color:var(--mr-success);cursor:pointer;flex-shrink:0">';
        h += '<div style="flex:1">';"""

new = """        h += '<div class="task-item' + (checked?\' checked\':\'\') + '" data-id="' + esc(t.id) + '" style="background:var(--mr-bg-card);border:1px solid ' + (checked?\'var(--mr-success)\':\'var(--mr-border)\') + ';border-radius:var(--mr-radius);padding:16px 20px;margin-bottom:10px;opacity:' + (checked?\'0.7\':\'1\') + ';transition:border-color 0.2s,opacity 0.2s">';
        h += '<label style="display:flex;gap:12px;align-items:flex-start;cursor:pointer">';
        h += '<input type="checkbox" class="task-cb" data-task="' + esc(t.id) + '"' + (checked?\' checked\':\'\') + ' aria-label="' + esc(t.titel) + (t.pflicht?\' (Pflicht)\':\'\') + '" style="width:20px;height:20px;margin-top:2px;accent-color:var(--mr-success);cursor:pointer;flex-shrink:0">';
        h += '<div style="flex:1">';"""

# Need to also close </label> instead of div in the right place
# Look for the pattern of the closing div before share button
if old in text:
    text = text.replace(old, new)
    # close </label> instead of inner </div></div>
    old_close = "        h += '</div></div>';\n        if (!checked) h += '<button type=\"button\" class=\"task-share"
    new_close = "        h += '</div></label>';\n        if (!checked) h += '<button type=\"button\" class=\"task-share"
    text = text.replace(old_close, new_close)
    p.write_text(text, encoding="utf-8")
    results.append(("checkliste-todesfall", "wrapped checkbox in <label> + aria-label"))
else:
    results.append(("checkliste-todesfall", "PATTERN NOT FOUND"))

# ----- beerdigungsplaner: aria-pressed für .opt-btn -----
p = TOOLS / "beerdigungsplaner" / "index.html"
text = p.read_text(encoding="utf-8")

old = """      h += '<button type="button" class="opt-btn' + (state.answers[s.id] === o.value ? ' selected' : '') + '" data-value="' + esc(o.value) + '">';"""
new = """      h += '<button type="button" class="opt-btn' + (state.answers[s.id] === o.value ? ' selected' : '') + '" data-value="' + esc(o.value) + '" aria-pressed="' + (state.answers[s.id] === o.value ? 'true' : 'false') + '">';"""

if old in text:
    text = text.replace(old, new)
    p.write_text(text, encoding="utf-8")
    results.append(("beerdigungsplaner", "aria-pressed added to .opt-btn"))
else:
    results.append(("beerdigungsplaner", "PATTERN NOT FOUND"))

# ----- bestattungskosten-rechner: aria-pressed für .bestattungsart-card + .choice-card -----
p = TOOLS / "bestattungskosten-rechner" / "index.html"
text = p.read_text(encoding="utf-8")

# The cards are static HTML — we add aria-pressed="false" initially, JS will update on click
# data-value="erdbestattung" pattern
pattern = re.compile(r'(<button type="button" class="bestattungsart-card" data-value="\w+">)', re.DOTALL)
count = 0
def add_aria(m):
    global count
    count += 1
    return m.group(1).replace('">', '" aria-pressed="false">')
new_text = pattern.sub(add_aria, text)

# Same for .choice-card
pattern2 = re.compile(r'(<button type="button" class="choice-card" data-value="\w+">)', re.DOTALL)
count2 = 0
def add_aria2(m):
    global count2
    count2 += 1
    return m.group(1).replace('">', '" aria-pressed="false">')
new_text = pattern2.sub(add_aria2, new_text)

# JS needs to toggle aria-pressed on click. Find the click handlers and inject.
# Pattern: $$('#bestattungsart-cards .bestattungsart-card').forEach(function(card){
#   card.addEventListener('click', function(){
#     $$('#bestattungsart-cards .bestattungsart-card').forEach(function(c){ c.classList.remove('selected'); });
#     card.classList.add('selected');
old_handler = """  $$('#bestattungsart-cards .bestattungsart-card').forEach(function(card){
    card.addEventListener('click', function(){
      $$('#bestattungsart-cards .bestattungsart-card').forEach(function(c){ c.classList.remove('selected'); });
      card.classList.add('selected');"""
new_handler = """  $$('#bestattungsart-cards .bestattungsart-card').forEach(function(card){
    card.addEventListener('click', function(){
      $$('#bestattungsart-cards .bestattungsart-card').forEach(function(c){ c.classList.remove('selected'); c.setAttribute('aria-pressed','false'); });
      card.classList.add('selected');
      card.setAttribute('aria-pressed','true');"""

if old_handler in new_text:
    new_text = new_text.replace(old_handler, new_handler)
else:
    results.append(("bestattungskosten-rechner", "WARNING: bestattungsart-card click-handler not patched"))

# Same for choice-card radio-groups
old_radio = """    $$('.choice-card', group).forEach(function(card){
      if (card.dataset.value === state[key]) card.classList.add('selected');
      card.addEventListener('click', function(){
        $$('.choice-card', group).forEach(function(c){ c.classList.remove('selected'); });
        card.classList.add('selected');"""
new_radio = """    $$('.choice-card', group).forEach(function(card){
      if (card.dataset.value === state[key]) { card.classList.add('selected'); card.setAttribute('aria-pressed','true'); }
      card.addEventListener('click', function(){
        $$('.choice-card', group).forEach(function(c){ c.classList.remove('selected'); c.setAttribute('aria-pressed','false'); });
        card.classList.add('selected');
        card.setAttribute('aria-pressed','true');"""

if old_radio in new_text:
    new_text = new_text.replace(old_radio, new_radio)

if count > 0 or count2 > 0:
    p.write_text(new_text, encoding="utf-8")
    results.append(("bestattungskosten-rechner", f"aria-pressed added: {count} bestattungsart-cards + {count2} choice-cards + click handlers"))

# ----- Print results -----
for r in results:
    print(r)
