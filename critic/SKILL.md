---
name: critic
description: >
  Independent, skeptical review of an idea, research claim, method, proof, experiment result,
  or design decision by a fresh agent with no stake in the conversation. Checks soundness,
  novelty against prior work, threats to validity, and whether the evidence supports the
  claim, and returns a verdict plus the single weakest point. Keeps a log so re-checks only
  cover what changed. Trigger on "critique this", "poke holes", "is this novel", "check the
  math", "run the novelty check again", "independent review", "review with a subagent that
  has no context", "am I fooling myself", "be honest, is this a bad idea", or "don't be a yes
  man". For code diffs use code-reviewer; for market viability use idea-research.
---

# Critic Skill

The main session has already agreed with the user many times and is biased toward its own
earlier answers. The critic's job is to be the reviewer who doesn't care: find what's wrong
before an advisor, reviewer or judge does. A critique that finds nothing important must say so
plainly, not invent problems.

## Step 1: Package the claim (main session)

Write `critique/<date>-<slug>/BRIEF.md` with only:
- **Claim**: what is being asserted, in one to three sentences. Precise enough to be wrong.
- **Evidence**: the results, derivations, data or citations offered for it (paths or pasted).
- **Context the reviewer needs**: definitions, the setting, constraints. Nothing about how
  the user feels about it, and nothing about what earlier reviews concluded.
- **Asked**: which checks to run (default: all in the rubric).

Strip persuasion. If the brief reads like a pitch, rewrite it as a claim.

**Re-checks:** if `critique/LOG.md` has an earlier review of the same claim, include only what
changed since then and the earlier findings to re-test. Don't re-run unchanged checks.

## Step 2: Review (fresh agent)

Launch one Agent with **no conversation context**: just the BRIEF.md path,
`${CLAUDE_SKILL_DIR}/references/rubric.md`, and WebSearch/WebFetch for prior-art checks.
Model: omit `model` (inherit) for novelty, proofs and final verdicts: this is the judgment
case. Use `"sonnet"` for a quick re-check of a single fixed issue.

Tell it: "You are a skeptical reviewer for a top venue. You did not write this. Your job is to
find the most important reasons it could be wrong, unoriginal or overstated. Verify every
prior-art claim with a search; cite what you find. Report in the rubric's format."

For a high-stakes claim (a paper submission, a thesis direction), run **two** reviewers in
parallel with different emphases (one on soundness/math, one on novelty/prior work) and merge.

## Step 3: Verify and report (main session)

- Check each finding against the evidence before passing it on. Drop ones that misread the
  brief, and say which.
- Don't soften. Lead with the verdict and the weakest point.
- Append to `critique/LOG.md`: date, claim, verdict, top issues, and status of earlier issues
  (fixed / still open / disputed).

Reply in chat with: verdict, weakest point, top 3 issues with a concrete fix or test for each,
and what would change the verdict. Point to the full review file.
