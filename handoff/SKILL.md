---
name: handoff
description: >
  Wraps up a long or drifting Claude Code session so the next one starts cheap and informed:
  writes a short HANDOFF.md (state, decisions, open threads, key files, exact next step),
  syncs PROJECT.md if the project has one, and gives the user a one-line prompt to start the
  fresh session. Trigger on "wrap up", "hand off", "let's start a new chat", "I'm switching to
  X", "save where we are", "context is getting long", or before resuming after a usage-limit
  reset. Also offer it (one line, don't run it unasked) when a session has clearly changed task
  (e.g. lit review → experiments → paper draft) or has been compacted.
---

# Handoff Skill

Long sessions are expensive because every turn re-reads the whole history, and a fork pays for
that history again. The fix is to end sessions at task boundaries without losing anything. A
handoff is good if a fresh session can continue **from the file alone**, without the user
re-explaining.

## When to offer it (don't nag)

Offer once, in one line, only when one of these holds:
- The task has changed to a different kind of work (research → build, build → writing, a new feature area).
- The session has been compacted, or is about to resume after a usage-limit reset.
- The user says they're stepping away for a while ("checking in later", "I'll be back tomorrow").
Never offer more than once per session. Never offer mid-task.

## Step 1: Gather (from this session, not by re-reading the repo)

From the conversation so far, list:
- **Goal**: what the user is ultimately trying to do (one or two sentences, in their words where possible).
- **Done**: what was completed, with commit hashes or file paths.
- **Decisions**: choices made and *why*, including options rejected (so they don't get re-proposed).
- **Open threads**: unfinished work, running jobs (with PIDs, log paths, ETA), questions waiting on the user.
- **Gotchas**: things that cost time this session (a broken command, a wrong assumption, an env quirk) and their fix.
- **Key files**: the 3–8 files the next session must read first, and what's in each.
- **Next step**: the single concrete next action, plus how to verify it worked.

Run `git status --short` and `git log --oneline -5` so uncommitted work and the latest commits are recorded accurately.

## Step 2: Write

Write `HANDOFF.md` in the repo root (overwrite the previous one; git keeps the history).
Use `${CLAUDE_SKILL_DIR}/references/handoff-template.md`. Keep it under ~60 lines. A handoff
the next session has to skim is too long.

If `PROJECT.md` exists, update its status/progress section to match (don't duplicate the
whole handoff there). If the project's `CLAUDE.md` doesn't mention `HANDOFF.md`, add one line:
`If HANDOFF.md exists, read it first.`

Uncommitted changes: ask whether to commit them before handing off. Don't commit unasked
unless the project's CLAUDE.md says to.

## Step 3: Hand over

Reply with the path, the next step in one line, and the prompt to start the new session in its
own code block:

```
Read HANDOFF.md, then <next step>.
```

If the next session's work is a different kind of task, suggest a fitting model or skill
(e.g. "this part is mechanical, Sonnet is enough" or "this is a lit review, use paper-reader").
