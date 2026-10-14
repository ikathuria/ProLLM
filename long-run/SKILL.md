---
name: long-run
description: >
  Safely launches and watches long-running jobs (ML training, experiment sweeps, evaluations,
  data processing, scraping, builds) that take more than a few minutes: reviews the script,
  smoke-tests it end to end on a tiny input, estimates time and peak memory against the
  machine, adds checkpoints and resume, runs it detached with logs, and monitors cheaply
  instead of polling from the main session. Trigger on "run the experiment", "start
  training", "launch the sweep", "run this overnight", "kick off the eval", "is my run still
  going", "check on the job", or before any command expected to run longer than ~5 minutes.
---

# Long-Run Skill

The expensive failures with long jobs are a broken script discovered an hour in, a run that
swaps itself to a crawl, a job that dies with the session, and Opus re-reading the whole
conversation every few minutes to poll a log. Each step below prevents one of them.

## Step 1: Review before running

Read the script and its config. Check: inputs and outputs exist and are the intended ones;
seeds set; results won't overwrite earlier runs (timestamped output dir); obvious bugs in the
logic that produces the numbers. For anything that took real effort to write, run
`code-reviewer` on it, or a fresh review subagent with no context.

## Step 2: Smoke test (always)

Run the full pipeline end to end on a tiny input: a few batches, steps or samples, every
stage including saving, evaluation and the final summary. It must take under ~2 minutes.
A smoke test that skips the last stage doesn't count. Fix and repeat until it passes.

## Step 3: Estimate

From the smoke test, measure time per unit and peak memory (`/usr/bin/time -l` on macOS,
`nvidia-smi` for GPU). Extrapolate to the full run and compare with the machine:
`sysctl hw.memsize` / free memory, disk space for outputs and checkpoints.
- Estimated peak memory > ~80% of RAM: reduce batch size, stream data, or shard before launching.
  Swapping makes runs many times slower.
- Tell the user the estimate: "~2h 10m, peak ~14 GB of 24 GB, ~3 GB of outputs."

## Step 4: Make it resumable

Checkpoints every ~10–15 minutes of work (or per sweep item). On start, resume from the
latest checkpoint if one exists. Write progress lines to a log (`step N/M, ETA, metric`), so
status can be read from the log's tail without opening anything else.

## Step 5: Launch detached

Run it in the background so it survives the session: `nohup … > runs/<name>/run.log 2>&1 &`
(or the Bash tool's `run_in_background`). Prevent sleep for long local runs
(`caffeinate -i` on macOS). Record the PID, log path, output dir and ETA in the project's
`HANDOFF.md` or `PROJECT.md`, so any session can check on it.

## Step 6: Watch cheaply

Never foreground-`sleep` to poll, and don't keep the main session alive just to watch.
- Short waits within the session: Monitor with a condition on the log ("until `done` or `Traceback` appears").
- Long runs: tell the user the ETA and end the turn. When they check in, read only the last
  ~20 lines of the log and the PID status, or have a `model: "haiku"` subagent summarize the log.
- On failure: read the traceback, fix, re-run the smoke test, then resume from the checkpoint,
  not from scratch.

## Done

Report: the final metrics, where outputs are, total time vs the estimate, and anything that
went wrong.
