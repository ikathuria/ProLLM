# Report Format

```
Reviewed: <target> · <N files, +X/−Y> · tests: <pass/fail/not run> · types: <pass/fail/n/a>

### Blocker
1. **<one-sentence defect>** — `path/to/file.ts:42`
   Scenario: <concrete input/state → wrong result/crash/exposure>
   Fix: <what to change>
   ```ts
   // short suggested code, if helpful
   ```

### Should fix
2. …

### Consider
3. …

### Questions
- `file:line` — <what you need to know and why it matters>

**Verdict:** merge after blockers · Not reviewed: <generated files, lockfiles, …>
```

Rules:
- No finding without file:line and a scenario.
- One finding per root cause; list extra locations under it.
- No praise padding, no restating the diff, no generic advice ("add more tests").
- If there are zero findings, say so plainly and state what you checked.
