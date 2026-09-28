# ProLLM

Skills for creating projects with LLMs. Each top-level folder is a self-contained [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills) — instructions and reference material Claude loads on demand.

## Skills

| Skill | What it does |
|---|---|
| [`project-planner`](project-planner/) | Turns a raw idea into a Claude Code-ready build plan: research, free-first tech stack selection, milestone breakdown with testable tasks, and a `PLAN.md` + `PROJECT.md` pair structured for autonomous execution. Delegates research to `idea-research` when installed. |
| [`idea-research`](idea-research/) | Multi-agent idea validation. Fans out five parallel research agents — competitors, community pain (Reddit/HN), video demand (YouTube), news & search trends, technical feasibility — with per-agent model and search-budget tuning, synthesized into a `RESEARCH.md` with an honest build / don't-build verdict. A quick inline mode is available on request. |
| [`ui-taste`](ui-taste/) | Anti-"AI slop" UI skill: commits to a concrete design brief (reference, type pairing, one accent, signature move) before coding, builds under a ban list of generic AI patterns, then screenshots and self-scores against a visual rubric. |
| [`paper-reader`](paper-reader/) | Grounded paper reading and literature reviews. Single-paper mode writes locator-tagged `PAPER_NOTES.md` and verifies every number and quote. Lit-review mode: scoping questions → protocol with fixed inclusion criteria → logged search (peer-reviewed first, preprint fallback, snowballing) → title/abstract then full-text screening → open-access PDF download → literature review table + thematic synthesis → gap matrix with each gap validated by a targeted search. |
| [`code-reviewer`](code-reviewer/) | Convention-aware, low-noise code review: gathers repo context, reviews in focused passes (correctness, security, data/concurrency, API, tests, conventions, performance), verifies every finding against the code, and reports severity-ranked findings with file:line, failure scenario, and fix. Optional `--fix` / PR comments. |

The skills compose: `project-planner` invokes `idea-research` for its research phase when both are installed, but each works standalone.

## Installation

Copy a skill folder into your skills directory:

**Personal (all projects):**

```sh
# macOS / Linux
cp -r project-planner ~/.claude/skills/

# Windows (PowerShell)
Copy-Item -Recurse project-planner "$env:USERPROFILE\.claude\skills\"
```

**Project-level (shared with collaborators):** copy into `.claude/skills/` inside the project repo.

Then just describe what you want to Claude — e.g. *"I have an idea for an app that..."* — and the skill triggers automatically. You can also invoke it explicitly with `/project-planner`.

### Optional: better Reddit research

Claude Code cannot fetch reddit.com directly, so `idea-research`'s community agent falls back to search snippets. For full Reddit thread + comment access, connect the free [reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy) MCP server (no API keys needed):

```sh
claude mcp add --transport stdio reddit-mcp-buddy -s user -- npx -y reddit-mcp-buddy
```

The skill detects it automatically and uses it when present.

## License

[MIT](LICENSE)
