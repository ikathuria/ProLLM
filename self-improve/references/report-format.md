# Report format

The report is organized around **what is going wrong and how to fix it**, not around how the
user uses Claude. It's plain markdown, with no dashboard and no charts. Lead with problems.
Stats go last.

~~~markdown
# Self-improve report: <date>
Coverage: read <n>/<n> sessions (<window>) · projects: <name (k)>, … · skills: <name (k)>, …
Previous changes checked: <helped> helped, <no change> no change, <worse> worse

## What's going wrong (ranked by recurrence × cost)

### 1. <plain-language problem, e.g. "brand-studio rebuilds previews 3–4× before you see one">
**How often**: <k> of <n> relevant sessions · ~<turns / $ / minutes> lost
**Why**: <root cause in one or two sentences, quoting the SKILL.md line if relevant>
  [layer: instruction | trigger | tooling | project | habit | environment]
**Evidence**
- `a1b2c3d4` · 2026-10-08 · AmazonDevHack: "<user quote or error, ≤25 words>"
- `e5f6a7b8` · 2026-10-11 · Aura: "<…>"
**Fix**:
```diff
- old line                     (`<repo>/<skill>/SKILL.md`)
+ new line
```
<!-- for a habit, instead of a diff: -->
You sent: "<actual prompt>"
Try: "<rewritten prompt that would have avoided it>". Why: <one line>

## What to do differently (you, not the skills)
1. <specific habit change tied to findings above, with an example prompt>
2. …

## What's working (keep doing)
- <skill/habit>: <why it works, one line> → <where else to copy it, if anywhere>

## Previous changes
| Date | Skill | Change | Signal | Before → After | Verdict |

## Also seen
- <lower-ranked issues, one line each>

<one line of totals: sessions, cost, errors, corrections>

## Apply?
Reply "all", the numbers to apply (e.g. "1, 3"), or "none".
~~~

Rules:
- Max 8 findings. Each title states the problem, not a category ("Tool errors" is not a title).
- No finding may rest on one session unless that session alone was costly or got abandoned.
  If the top three findings all come from the same one or two chats, coverage failed; go back
  to Stage 2.
- "An error happened" is not a finding. Say which error, how often, why it recurs, and the change.
