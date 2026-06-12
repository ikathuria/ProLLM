# ProLLM

Skills for creating projects with LLMs. Each top-level folder is a self-contained [Claude Code skill](https://docs.claude.com/en/docs/claude-code/skills) — instructions and reference material Claude loads on demand.

## Skills

| Skill | What it does |
|---|---|
| [`project-planner`](project-planner/) | Turns a raw idea into a Claude Code-ready build plan: research, free-first tech stack selection, milestone breakdown with testable tasks, and a `PLAN.md` + `PROJECT.md` pair structured for autonomous execution. Delegates research to `idea-research` when installed. |
| [`idea-research`](idea-research/) | Multi-agent idea validation. Fans out five parallel research agents — competitors, community pain (Reddit/HN), video demand (YouTube), news & search trends, technical feasibility — with per-agent model and search-budget tuning, synthesized into a `RESEARCH.md` with an honest build / don't-build verdict. A quick inline mode is available on request. |

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

## License

[MIT](LICENSE)
