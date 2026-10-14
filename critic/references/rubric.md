# Critique rubric

Score each dimension **pass / concern / fail**, with a one-line reason and a locator (section,
equation, table, file:line) for every concern or fail.

1. **Claim clarity**: is the claim precise and falsifiable? Could two readers disagree on what it says?
2. **Soundness**: do the math, logic and method actually support it? Check every derivation step
   and every assumption; name hidden assumptions.
3. **Evidence fit**: do the results show *this* claim, or something weaker or adjacent?
   Sample size, baselines, ablations, variance, cherry-picking, leakage, metric choice.
4. **Novelty**: search for the closest prior work (≥3 targeted searches, including the last 12
   months of preprints). Name the closest papers and what exactly differs. "Not found" must
   list the searches run.
5. **Threats to validity**: what alternative explanation fits the same evidence? What
   setting would break it?
6. **Significance**: if true, does it matter? To whom? Is it a gap *because it doesn't matter*?

## Output format

```markdown
## Verdict: <sound & novel | sound, novelty unclear | promising but unproven | flawed | already done>
**Weakest point:** <one sentence>

| Dimension | Score | Reason (locator) |
|---|---|---|

### Top issues
1. <issue>: <why it matters> → <concrete fix or test>

### Closest prior work
- <paper/product> (<link>): <what overlaps, what differs>

### What would change the verdict
- <specific result, proof, or comparison>
```

Rules: no praise padding, no "overall a strong submission". If it's good, the verdict says so
and the issues list is short.
