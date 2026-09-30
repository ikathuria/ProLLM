# ProLLM

Skills for creating projects with LLMs. Each top-level folder is a self-contained [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills) — instructions and reference material Claude loads on demand.

## Skills

Six skills, roughly in the order you'd use them on a project.

### Plan

| Skill | What it does | Try |
|---|---|---|
| [`idea-research`](idea-research/) | Multi-agent idea validation. Five parallel research agents cover competitors, community pain (Reddit/HN), video demand (YouTube), news & search trends, and technical feasibility, each with its own model and search budget. Their findings are combined into a `RESEARCH.md` with an honest build / don't-build verdict. A quick inline mode is available on request. | *"Is there a market for a habit tracker for ADHD?"* |
| [`project-planner`](project-planner/) | Turns a raw idea into a Claude Code-ready build plan: research, free-first stack selection, milestones with testable tasks, and a `PLAN.md` + `PROJECT.md` pair built for autonomous execution. Hands research to `idea-research` when it's installed. | *"I have an idea for an app that…"* |
| [`hackathon-planner`](hackathon-planner/) | Plans a hackathon entry to win. It fetches the event's live rules and judging criteria (flagging AI-assisted judging), studies past winners, and scores ideas against that rubric plus insider edge, demo moment, evidence, and risk. Outputs a `HACKATHON_PLAN.md` with an evidence plan, a demo-video script, and a timeline sized in coding-agent sessions rather than human hours. Grounded in a Sept 2026 review of ~36 winning projects across 9 AI hackathons. | *"Help me win the X build week"* |

### Build & design

| Skill | What it does | Try |
|---|---|---|
| [`brand-studio`](brand-studio/) | End-to-end anti-"AI slop" UI redesign. It reads the whole project and renders 3–5 distinct design directions as previews. You pick one, it writes `BRAND.md` + design tokens into the repo, confirms them with you, then rebrands the UI. It avoids both template slop and sterile over-minimalism, and it verifies the result with screenshot rubric scoring plus before/after accessibility (axe, contrast, keyboard) and SEO (meta, OG, headings, Lighthouse) audits. | *"Make this UI look better"* · *"Rebrand my app"* |

### Review & research

| Skill | What it does | Try |
|---|---|---|
| [`code-reviewer`](code-reviewer/) | Convention-aware, low-noise code review. It gathers repo context, reviews in focused passes (correctness, security, data/concurrency, API, tests, conventions, performance), and verifies every finding against the code. Reports severity-ranked findings with file:line, a failure scenario, and a fix. Can apply fixes or post PR comments. | *"Review my branch before I push"* |
| [`paper-reader`](paper-reader/) | Grounded paper reading and literature reviews. Single-paper mode writes a locator-tagged `PAPER_NOTES.md` and verifies every number and quote. Lit-review mode sets a protocol, runs a logged search, screens results, downloads open-access PDFs, and produces a review table, a synthesis, and a gap matrix in which every gap is checked with a targeted search. | *"Summarize arXiv 2401.01234"* · *"Lit review on RAG evaluation"* |

### How they compose

- `project-planner` runs `idea-research` for its research phase. `hackathon-planner` reuses parts of `idea-research` and `project-planner`'s stack guide.
- `hackathon-planner` hands the visual layer to `brand-studio`.
- Any existing `RESEARCH.md`, `PLAN.md`, or `BRAND.md` is read and reused rather than regenerated.
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
