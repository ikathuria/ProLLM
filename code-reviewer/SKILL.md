---
name: code-reviewer
description: >
  Thorough, low-noise code review of a diff, branch, PR, or set of files, judged against
  the repository's own conventions rather than generic style opinions. Trigger when the
  user asks to "review my code", "review this PR/branch/diff", "check my changes before I
  push", "is this ready to merge", or "what's wrong with this code". Gathers project
  context first, reviews in focused passes (correctness, security, data/concurrency,
  conventions, tests, simplicity), verifies every finding against the code before
  reporting it, and outputs a severity-ranked list with file:line, a failure scenario, and
  a concrete fix. Can apply fixes on request.
---

# Code Reviewer Skill

A good review finds the bugs that matter and nothing else. The two failure modes to avoid:
**missing real defects** and **drowning the author in false positives and style nits.**
Every reported finding must survive a verification step.

## Stage 1 — Determine the target

- Nothing specified → uncommitted changes + commits on the current branch not on the base
  (`git diff $(git merge-base HEAD origin/main)...` plus `git diff HEAD`).
- PR number/URL → `gh pr view <n> --json title,body,baseRefName,files` and `gh pr diff <n>`.
- Paths → review those files in full.
State the target and size (files, +/− lines) in one line before reviewing.

## Stage 2 — Gather context (don't review a diff in a vacuum)

- Read `CLAUDE.md`, `CONTRIBUTING.md`, linter/formatter configs, and the PR description/linked
  issue — these define *intent* and *conventions*.
- For each changed function, read the **whole function and its callers/callees**, not just
  the hunk. Many bugs live in how changed code interacts with unchanged code.
- Find 1–2 existing examples of the same kind of code (another endpoint, component, migration)
  to learn the local idiom.
- Note what tooling already enforces (types, lint, formatter) — don't report what CI catches.
- Run the tests and type checker if cheap; record failures as findings.

## Stage 3 — Review in passes

Go through `${CLAUDE_SKILL_DIR}/references/review-checklist.md` one pass at a time — focused
passes catch more than one mixed read:
1. **Correctness** — logic, edge cases, error paths, off-by-one, null/empty, wrong assumptions.
2. **Security** — injection, authz/authn gaps, secrets, unsafe deserialization, SSRF, path traversal.
3. **Data & concurrency** — migrations, transactions, races, idempotency, resource leaks.
4. **API & compatibility** — breaking changes to public interfaces, schemas, configs, CLIs.
5. **Tests** — does a test fail if the change is reverted? Missing cases for new branches.
6. **Conventions & simplicity** — deviations from the repo's own patterns, duplicated helpers
   that already exist, dead code, needless abstraction.
7. **Performance** — only where it plausibly matters (N+1 queries, hot loops, unbounded growth).

For diffs over ~500 lines or spanning unrelated areas, split by area and run passes in
parallel subagents, each given the context from Stage 2; merge and dedupe their findings.

## Stage 4 — Verify every finding

For each candidate, before reporting it:
- Trace the actual code path — confirm the input that triggers it can really reach it.
- Check whether it's already handled elsewhere (validation upstream, a guard in the caller, a test).
- When feasible, prove it: a failing test, a quick script, or a concrete input/output.
- Drop it if you can't articulate a concrete failure scenario. Downgrade to **question** if
  it depends on intent you can't determine.

## Stage 5 — Report

Use `${CLAUDE_SKILL_DIR}/references/report-format.md`. Ranked by severity:
- **Blocker** — bug, security hole, data loss, or breaking change; must fix before merge.
- **Should fix** — likely bug in edge cases, missing test for new logic, convention break with real cost.
- **Consider** — simplification or clarity with clear payoff. Max ~5; skip pure taste.
- **Question** — needs the author's intent.

Each finding: `file:line`, one-sentence defect, concrete failure scenario, and a suggested fix
(code snippet when short). End with a one-line verdict: *ready to merge*, *merge after blockers*,
or *needs rework*, plus anything you didn't review (generated files, vendored code).

Also say what's good if something is notably well done — briefly, once.

## Options

- `--fix` / "fix them": apply Blocker + Should-fix fixes, run tests, report what changed.
- `--comment` / "post on the PR": ask for confirmation, then post inline comments via
  `gh api repos/{owner}/{repo}/pulls/{n}/comments` (one per finding). Never approve or
  request changes on the user's behalf unless asked.
- "quick review": correctness + security passes only, blockers only.
