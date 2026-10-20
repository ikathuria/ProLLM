# Daily check-in routine prompt

Used by `weekly-plan` daily mode. Replace `{REPOS}` with the routine's repo names (space-separated,
as cloned). Model: Haiku. Tools: Bash, Read, Glob, Grep. Read-only.

```
Daily check-in. READ-ONLY: do not edit, commit, push, open PRs or install anything.

Repos cloned in /home/user: {REPOS}. For each repo, cd into it, run `git fetch --all -q`, and set
B=origin/$(git rev-parse --abbrev-ref HEAD) (there is no origin/HEAD in these clones). Then collect:
1. Next step: in HANDOFF.md or docs/HANDOFF.md (read with `git show $B:<path>`), the first section
   whose heading contains "Next step", "Start here" or "Where we are"; take its first 3 non-empty
   lines. If there is no handoff, take the first unchecked `- [ ]` line of PLAN.md and prefix it
   "plan:". If neither exists, write "nothing recorded".
2. Queue: if QUEUE.md exists, count items by Status (ready / needs-me / review / blocked /
   running) and list the titles of needs-me and blocked items.
3. Overnight runs: `git for-each-ref --sort=-committerdate --format='%(refname:short) %(committerdate:relative)' 'refs/remotes/origin/claude/auto-*'`.
   For each branch updated in the last 24 hours: its last commit subject, and the item's Status
   line from `git show <branch>:QUEUE.md`. If `gh auth status` succeeds, also take the draft PR's
   `Result:` and `Needs you:` lines from `gh pr list --draft --json headRefName,body,url`.
4. Activity: `git log --since='24 hours ago' --oneline $B | wc -l`.
Do all repos in one or two Bash calls.

Quote the Status, Result and Needs-you fields exactly as written. Do not guess why something
failed and do not suggest new work.

Reply in at most 25 lines with these sections, skipping empty ones:
**Needs you:** needs-me, blocked, or a non-empty `Needs you:` (repo: item, one line each)
**Overnight runs:** repo: branch, result, PR link
**Next steps:** repo: quoted next step (one line each, truncate at 120 characters)
**Ready in queues:** repo: count
**Quiet:** repos with no activity in 7+ days (one line)
End with one line naming the single most urgent item.
```
