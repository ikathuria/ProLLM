# ProLLM

Skills for creating projects with LLMs. Each top-level folder is a self-contained [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills) — instructions and reference material Claude loads on demand.

## Skills

Eleven skills, roughly in the order you'd use them on a project.

### Plan

| Skill | What it does | Try |
|---|---|---|
| [`idea-research`](idea-research/) | Multi-agent idea validation. Four or five parallel research agents cover competitors, community pain (Reddit/HN), video demand (YouTube, consumer domains only), news & search trends, and technical feasibility, each with its own model and search budget. Their findings are combined into a `RESEARCH.md` with an honest build / don't-build verdict. A quick inline mode is available on request. | *"Is there a market for a habit tracker for ADHD?"* |
| [`project-planner`](project-planner/) | Turns a raw idea into a Claude Code-ready build plan: research, free-first stack selection, milestones with testable tasks, and a `PLAN.md` + `PROJECT.md` pair built for autonomous execution. Its execute mode then builds the plan in bounded batches of 1–3 milestones: it proposes a batch, builds and tests each milestone, commits, and stops to report. Hands research to `idea-research` when it's installed. | *"I have an idea for an app that…"* |
| [`hackathon-planner`](hackathon-planner/) | Plans a hackathon entry to win. It fetches the event's live rules and judging criteria (flagging AI-assisted judging), studies past winners, and scores ideas against that rubric plus insider edge, demo moment, evidence, and risk. Outputs a `HACKATHON_PLAN.md` with an evidence plan, a demo-video script, and a timeline sized in coding-agent sessions rather than human hours. Grounded in a Sept 2026 review of ~36 winning projects across 9 AI hackathons. | *"Help me win the X build week"* |

### Build & design

| Skill | What it does | Try |
|---|---|---|
| [`brand-studio`](brand-studio/) | End-to-end anti-"AI slop" UI redesign. It reads the whole project and renders 3–5 distinct design directions as previews. You pick one, it writes `BRAND.md` + design tokens into the repo, confirms them with you, then rebrands the UI. It avoids both template slop and sterile over-minimalism, and it verifies the result with screenshot rubric scoring plus before/after accessibility (axe, contrast, keyboard), responsiveness (320–2560px width sweep), and SEO (meta, OG, headings, Lighthouse) audits. | *"Make this UI look better"* · *"Rebrand my app"* |

### Review & research

| Skill | What it does | Try |
|---|---|---|
| [`code-reviewer`](code-reviewer/) | Convention-aware, low-noise code review. It gathers repo context, reviews in focused passes (correctness, security, data/concurrency, API, tests, conventions, performance), and verifies every finding against the code. Reports severity-ranked findings with file:line, a failure scenario, and a fix. Can apply fixes or post PR comments. | *"Review my branch before I push"* |
| [`paper-reader`](paper-reader/) | Grounded paper reading and literature reviews. Single-paper mode writes a locator-tagged `PAPER_NOTES.md` and verifies every number and quote. Lit-review mode sets a protocol, runs a logged search, screens results, downloads open-access PDFs, and produces a review table, a synthesis, and a gap matrix in which every gap is checked with a targeted search. | *"Summarize arXiv 2401.01234"* · *"Lit review on RAG evaluation"* |
| [`critic`](critic/) | An independent, skeptical review of an idea, research claim, proof, or result by a fresh agent with no stake in the conversation. It turns the claim into a neutral brief, scores it on soundness, evidence fit, novelty (with logged prior-art searches), threats to validity, and significance, and returns a verdict plus the single weakest point. A log means re-checks cover only what changed. | *"Poke holes in this defense idea"* · *"Run the novelty check again"* |

### Run & manage sessions

| Skill | What it does | Try |
|---|---|---|
| [`handoff`](handoff/) | Ends a long or drifting session without losing anything. It writes a short `HANDOFF.md` (state, decisions, open threads, gotchas, key files, next step), syncs `PROJECT.md`, and gives you a one-line prompt for a fresh session. Long sessions re-read their whole history on every turn, so this is the biggest cost saver for multi-day work. | *"Wrap up, I'm switching to the paper draft"* |
| [`long-run`](long-run/) | Launches long jobs (training, sweeps, evals) safely. It reviews the script, smoke-tests it end to end on a tiny input, estimates time and peak memory against the machine, adds checkpoints and resume, and runs the job detached. It then checks the log cheaply instead of polling from the main session. | *"Start the training run"* · *"Is my sweep still going?"* |
| [`outreach`](outreach/) | Job-search messages: referral asks, recruiter replies, follow-ups, cold emails. It works from a private profile (`~/.claude/outreach/PROFILE.md`, built from your project files on first run) so you never re-explain your background. It keeps facts like work authorization current and logs what was sent and what got replies. | *"Ask Priya for a referral for these two roles"* |

### Improve

| Skill | What it does | Try |
|---|---|---|
| [`self-improve`](self-improve/) | A retro on your own Claude Code sessions that then fixes your skills, built to be more specific than `/insights`. A stdlib script reduces local transcripts (`~/.claude/projects`) to a compact digest of friction signals: corrections, interrupts, tool errors, retry loops, edit churn, cost outliers. It reads **every** session in the window, using Sonnet helpers for large windows, and reports patterns counted across sessions rather than a few dramatic chats. The report leads with *what keeps going wrong*. Each finding gives its recurrence ("5 of 10 sessions"), quoted evidence with session IDs, the root cause (skill instruction, trigger, tooling, project CLAUDE.md, habit, or environment), and an exact diff or a before/after prompt rewrite. It applies only the fixes you approve and logs them to `~/.claude/self-improve/LEDGER.md`, so the next run checks whether each one helped. Plugin and external skills get suggestions only. A 30-day run over ~50 sessions costs a few hundred thousand tokens, mostly on Sonnet. | *"/self-improve on the last 30 days"* · *"Why does brand-studio keep failing?"* |

### How they compose

- `project-planner` runs `idea-research` for its research phase. `hackathon-planner` reuses parts of `idea-research` and `project-planner`'s stack guide.
- `project-planner` and `hackathon-planner` hand the visual layer to `brand-studio`: project-planner adds a gated brand task before feature screens and a final audit pass.
- Any existing `RESEARCH.md`, `PLAN.md`, or `BRAND.md` is read and reused rather than regenerated.
- `self-improve` tunes all of the above from real usage: it edits their `SKILL.md` and reference files and records each change in a ledger.
- Skills that fan out to subagents give each one a cheaper model (Sonnet or Haiku) and a search or turn budget. Opus is kept for judgment and final edits.
- `handoff` is offered at task boundaries by the other skills (paper-reader after a review, project-planner between milestone batches); `long-run` uses `code-reviewer` or a no-context reviewer before launching; `critic` complements `code-reviewer` (code) and `idea-research` (market).
- Every skill also works standalone.

## Installation

**Symlink (recommended).** Edits and `git pull` update the installed skills live:

```sh
git clone https://github.com/ikathuria/ProLLM.git
cd ProLLM
for s in */; do ln -sfn "$PWD/${s%/}" ~/.claude/skills/"${s%/}"; done
```

**Copy** a single skill instead:

```sh
# macOS / Linux
cp -r brand-studio ~/.claude/skills/

# Windows (PowerShell)
Copy-Item -Recurse brand-studio "$env:USERPROFILE\.claude\skills\"
```

**Project-level (shared with collaborators):** copy into `.claude/skills/` inside the project repo.

Then describe what you want and the matching skill triggers automatically, or invoke one explicitly, e.g. `/brand-studio`. Start a new session after installing.

### Optional: better Reddit research

Claude Code cannot fetch reddit.com directly, so `idea-research`'s community agent falls back to search snippets. For full Reddit thread + comment access, connect the free [reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy) MCP server (no API keys needed):

```sh
claude mcp add --transport stdio reddit-mcp-buddy -s user -- npx -y reddit-mcp-buddy
```

The skill detects it automatically and uses it when present.

## License

[MIT](LICENSE)
