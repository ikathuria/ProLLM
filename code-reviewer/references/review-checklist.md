# Review Checklist (by pass)

Use as prompts, not a form — only report items that actually apply.

## 1. Correctness
- Boundary values: empty, zero, one, max, negative, unicode, very long input
- Null/undefined/None paths; optional chaining hiding real errors
- Error handling: swallowed exceptions, wrong error type, missing cleanup in failure paths, retries without backoff
- Async: missing `await`, unhandled promise rejections, fire-and-forget that should be awaited
- Conditionals: inverted logic, `==` vs `===`, operator precedence, fallthrough
- Time: timezones, DST, clock skew, date parsing
- Numbers: integer overflow, float equality, currency in floats, division by zero
- State: stale closures, mutation of shared/default arguments, cache invalidation

## 2. Security
- Untrusted input reaching SQL, shell, HTML, templates, file paths, regexes (ReDoS), URLs (SSRF)
- AuthZ: every new endpoint/action checks the caller may act on *this* resource (IDOR)
- Secrets in code, logs, error messages, client bundles
- Crypto: homemade crypto, weak randomness for tokens, missing constant-time compare
- Deserialization of untrusted data; `eval`-like constructs
- CORS, CSRF, cookie flags on new routes; RLS policies for new tables (Supabase/Postgres)
- Dependency additions: maintained? typosquat? needed?

## 3. Data & concurrency
- Migrations: reversible, safe on large tables (locks, backfills), default values, nullability
- Transactions around multi-step writes; idempotency of retries/webhooks
- Race conditions: check-then-act, concurrent requests, double submit
- Resource leaks: connections, file handles, listeners, timers, subscriptions
- Unbounded queries, pagination, memory growth

## 4. API & compatibility
- Changed signatures, response shapes, enum values, config keys, env vars, CLI flags
- Callers updated everywhere (grep for all usages)
- Versioning / deprecation path; docs and types updated

## 5. Tests
- Would a test fail if this change were reverted?
- New branches and error paths covered; assertions meaningful (not just "doesn't throw")
- Mocks don't hide the behavior under test; no flaky timing/sleep-based tests

## 6. Conventions & simplicity
- Matches how the repo already does this (naming, file layout, error style, logging, state mgmt)
- Re-implements an existing helper/util
- Dead code, commented-out code, leftover debug logs, TODOs without owner
- Abstraction that has one caller; config that is never varied

## 7. Performance (only if it plausibly matters)
- N+1 queries, queries in loops, missing indexes for new filters
- Re-renders / expensive work in render paths (React)
- Large payloads, synchronous I/O on hot paths
