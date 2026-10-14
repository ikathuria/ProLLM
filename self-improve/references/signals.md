# Signals → likely causes

Each signal is a lead to follow up, not a verdict. Confirm it by reading the transcript around
the moment before you file a finding.

| Signal (digest field) | What it usually means | Check | Typical fix layer |
|---|---|---|---|
| `corrections`, restated asks, "still…" | Output missed intent | Did the skill say to confirm X, or assume it? Was the user's ask ambiguous? | Skill instruction / habit |
| Same correction in ≥2 sessions with one skill | Systematic skill gap | Find the SKILL.md line (or missing line) that produced it | Skill instruction |
| `interrupts` soon after a Skill call | Skill went off in the wrong direction or ran too long | What was it doing when interrupted? Was a checkpoint missing? | Skill instruction (add a confirm gate) |
| Skill invoked, then the user redirects to another approach | Wrong trigger | Compare the user's words with `description:` of this and sibling skills | Skill trigger |
| A skill never fires where it obviously should have | Trigger too narrow | Search prompts for its domain words in sessions without it | Skill trigger |
| `tool_errors` with the same message across sessions | Broken command, path, or API in the skill | Reproduce the command | Skill tooling |
| `repeated_bash_failures` | Retry loop: guessing instead of reading the error | Did it change approach after the 2nd failure? | Skill instruction ("on failure, read X") or project context |
| `edit_churn` (a file edited ≥5×) | Iterating blind: no spec, no visual check, or flip-flopping | Were edits responding to user feedback, or self-correction? | Skill instruction (verify step) / habit (state the target up front) |
| `permission_rejects`, denied calls | Skill asks for actions the user's mode blocks | Which tool, and is it necessary? | Skill instruction / settings suggestion |
| `compactions` > 0, very long sessions | Context overload | Was the session doing many unrelated tasks? | Habit (split sessions) / skill (fan out to subagents) |
| `subagent_tool_errors` high | Subagent prompts lack context or tools | Read one subagent transcript | Skill instruction (subagent brief) |
| Cost outlier for a skill | Over-research, wrong model tier, big fan-out | `model_cost`: Opus on work Haiku/Sonnet could do? | Skill instruction (model/budget per stage) |
| `api_errors`, MCP connection failures | Environment | — | Environment (not a skill edit) |
| A skill in many sessions, few signals | Working well | What does it do that others don't? | Copy the pattern elsewhere |

## Not evidence

- Errors the skill handled and recovered from in one step (e.g. a file-not-found while probing).
- Corrections about content the user only decided on mid-session (a change of mind, not a miss).
- This skill's own runs, and sessions where the user was testing or debugging a skill on purpose.
