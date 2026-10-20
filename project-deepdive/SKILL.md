---
name: project-deepdive
description: >
  Interview prep for the user's own projects, especially vibe-coded ones they need to explain with
  confidence. Builds a private INTERVIEW.md per project from the actual code (pitch, architecture,
  one request traced through file:line, decisions and alternatives, verified numbers vs résumé
  claims, failure modes, scaling, likely questions with answers, and a list of parts the user may
  not understand), then quizzes the user one question at a time and tracks weak spots. Trigger on
  "deep dive into <project>", "prep me to talk about <project>", "interview prep for my projects",
  "quiz me on <project>", "what would an interviewer ask about this", "I don't understand my own
  code". For job-application messages use outreach; for code quality use code-reviewer.
---

# Project Deep-Dive Skill

The goal is that the user can explain the project without notes, defend its decisions, and admit
its limits precisely. Every claim in the notes must come from the code, its history or a run, never
from the README's marketing or the résumé alone: an interviewer who probes a wrong claim does more
damage than a gap the user names honestly.

## Where notes live

Private, outside public repos: `~/Library/Mobile Documents/com~apple~CloudDocs/get to know me/projects/<project>/INTERVIEW.md`
(template: `${CLAUDE_SKILL_DIR}/references/interview-template.md`). If it exists, update it; don't
regenerate. Résumé claims about the project: hub `PROFILE.md` (Professional background).

## Mode: build

1. **Map (cheap).** Get a structural map without reading everything. Prefer Codex, falling back to
   a `sonnet` Explore subagent:
   `codex exec -C <repo> -s read-only -o <scratch>/map.md "List entry points, main modules with one-line roles, external services and APIs, data stores, how to run and test, and the 5 files that matter most. Cite paths. No opinions." </dev/null`
   Add `git log --oneline | wc -l`, `git log --format='%ad' --date=short | tail -1` (start date),
   and `git shortlog -sn` (who wrote it).
2. **Trace one real path.** Pick the core user action (one request, one pipeline run, one training
   step) and follow it through the code yourself, recording `file:line` at each hop. This is the
   section interviewers probe most; read the code for it, don't infer.
3. **Decisions.** For each major choice (framework, model, data store, retrieval method, protocol),
   record what was chosen, the realistic alternatives, and why, from commit messages, PLAN/DESIGN
   docs or the code. If the reason isn't recorded anywhere, write `reason not recorded` and add it
   to Questions for the user; never invent a rationale.
4. **Numbers.** List every metric the résumé, README or slides claim. Mark each `verified`
   (where: script, log, test output), `unverified`, or `contradicted`. Offer to rerun cheap checks;
   use `long-run` for anything over 5 minutes.
5. **Gaps.** List parts the user is likely not to understand: generated or copied code, complex
   config, concurrency, auth, prompt chains, math. For each, a 3–5 line plain explanation.
6. **Questions.** 12–20 likely questions across: walkthrough, design trade-offs, scale ("10× users"),
   failure ("what breaks first"), testing, security, "what would you do differently", and one or two
   behavioural STAR stories the project supports. Short model answers grounded in the notes.
7. Ask the user the open Questions in one batch, write their answers in, then show the 30-second
   pitch and the weakest three areas.

## Mode: quiz

1. Read `INTERVIEW.md`, especially the Quiz log. Prioritise weak and never-asked topics.
2. Ask **one** question at a time, as an interviewer would, with a follow-up if the answer is
   shallow. Don't show the model answer first.
3. Grade against the notes and code: `solid`, `partial` (what was missing), or `wrong` (the
   correct point, with `file:line`). Keep feedback to 2–3 lines.
4. After 5–8 questions or when the user stops, append to the Quiz log: date, topics, grades, and
   the next topics to drill.

## Token rules

- Never read the whole repo. Map first, then read only the traced path and the files behind each
  decision.
- Lockfiles, generated code, `node_modules`, datasets and checkpoints are out of scope.
- One project per session; offer `handoff` between projects.
