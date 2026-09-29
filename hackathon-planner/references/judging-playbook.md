# Judging Playbook: Score Well with Human *and* AI Judges

For online hackathons, judging is asynchronous: someone (or something) reviews a submission page, a repo, and a video, usually quickly. Optimize for **legibility and verifiability**.

**Hard line:** optimize only through clarity, evidence, and honest framing. Never hide instructions to judges/LLMs in READMEs, repos, video, or metadata (hidden prompts, invisible text, "ignore previous instructions"). Academic venues treat this as misconduct, AI-judging pipelines sanitize for it, and no organizer would reward it. Never overstate what works; a WebMCP-style rule bans "overstated functionality" and judges verify.

---

## 1. How online judging actually works (sourced)

- **Requirements compliance is the first filter.** Instant discards: missing fields, wrong video length/format, broken demo or repo link, not using required tech, late submission. Some events (Gemini Live Agent Challenge) run an explicit pass/fail completeness check before scoring.
- **Human judging:** Devpost judges rate each criterion 1–5 stars, in sequence, with no written feedback. Devpost says judges aren't required to watch past ~3 minutes. Time per async submission: no hard data found.
- **AI-assisted judging exists but is event-specific.** No official AI scoring on Devpost/lablab/DoraHacks. Examples found:
  - OpenAI Build Week rules state judging "may utilize automated AI-driven analysis".
  - Devfolio "Push to Prod" (Apr 2026): an agent clones repos and checks pitch claims against code, writes a cited audit; cheaper model extracts per-criterion scores; code aggregates; humans decide.
  - hackathon-courtroom (Aug 2026): three blind LLM personas (Builder, Skeptic, Futurist) judged live URLs (headless browser), Whisper transcripts of the video, and submission text; deterministic aggregation; inputs sanitized against injection.
  - Genesis x Skelar 2026: Gemini scored pitch transcripts on innovation/technical depth/business impact/pitch quality (30% of final score).
  - HackJudge AI reads README, code, commit history, metadata; author flags LLM leniency, truncation, non-determinism.
- **Pattern: AI does verification and triage; humans make the final call.**

### What an AI judge can and cannot see
Likely sees: submission text, README, repo files and commit history, a **transcript** of the video audio, and possibly the live URL via headless browser. Likely does **not** see video visuals.
Implications:
1. **Say the key claims out loud** in the narration. If it isn't spoken or written, it may not exist.
2. **Make claims verifiable in the repo:** a claim in the writeup ("agent verifies against 3 sources") must be findable in code, with file paths named in the README.
3. **Live URL must work with no login** (or provide test credentials in the submission text), and be robust to a headless browser: no CAPTCHA, no popup walls, seeded demo data present on first load.
4. Known LLM-as-judge biases from general research: length/verbosity and position bias, leniency. Claims that LLM judges reward buzzwords or diagrams are UNVERIFIED. Don't pad; structure and specificity win.

---

## 2. Criteria → the evidence that scores

Map each of the hackathon's actual criteria (Phase 2) to concrete artifacts. Build the Evidence Plan in the brief from this table.

| Criterion (common wording) | Evidence that scores | Where it lives |
|---|---|---|
| **Technical execution / implementation** | Real repo with steady commit history; README "Architecture" section naming files/modules; tests or an eval with numbers; non-trivial use of sponsor tech; it actually runs end-to-end | Repo, README, video |
| **Innovation / creativity / originality** | A one-sentence "why this isn't X + a chatbot"; an unexpected mechanism or the retellable "moment" | Tagline, video first 15s |
| **Impact / real problem** | A named user (ideally a real person), a before/after with a number, a reason the problem is costly | Writeup "Inspiration", video hook |
| **Design / UX** | No-sign-up demo, seeded data, clean single flow, loading/empty/error states handled | Live URL, video |
| **Completeness / feasibility** | Deployed URL; the whole loop works, not screens; honest "What's next" | Live URL, writeup |
| **Presentation / demo** | ≤3 min video, working product visible in first 10–15s, one strong example, clear audio | Video |
| **Use of sponsor tech** | State exactly which feature and why it's load-bearing (what breaks without it) | README + video narration |
| **Responsible AI / safety / privacy** (increasingly common; Devpost panel treats disclosure as a differentiator) | AI-use disclosure, limits stated, no sensitive data stored, human-in-loop where stakes are high | README section |

Weight effort by the event's weights. Devpost usually can't weight, so equal-weight events reward being *strong across all four* over spiking on one. Explicit-weight events (e.g. Gemini 3: Technical 40 / Innovation 30 / Impact 20 / Presentation 10) should shift build time toward the heavy criteria.

---

## 3. The submission package (typical online requirements)

Modal package: public repo + live demo URL + ~3 min video + short writeup. Variations: lablab wants deployed URL, video ≤5 min, PDF deck; Gemini Live Agent wanted an architecture diagram and proof of cloud deployment; OpenAI Build Week wanted README disclosure of Codex use plus a session ID. **Always re-read the current rules page; this list is a base rate, not the rules.**

### README (write it for a skimming human or an LLM reading only this file)
1. One-line what + who it's for + the measured result (badge-style line at the very top).
2. **Try it:** live URL + test credentials/no-login note + 30-second path through the demo.
3. **Demo video** link.
4. The problem (named user, cost, number).
5. How it works: architecture diagram + a table of *claim → file/module that implements it*.
6. Evidence: eval numbers, test results, sample outputs (reproducible command).
7. **Sponsor tech used and why** (specific features).
8. **AI-assisted development disclosure:** which tools built it, what was human-decided vs agent-built. Required or strongly encouraged at OpenAI, MLH (non-disclosure can disqualify), Devpost panel. Include a session ID where the rules ask.
9. Limitations & what's next (honest).
10. Run locally.

### Devpost-style writeup sections
Inspiration → What it does → How we built it → Challenges → Accomplishments → What we learned → What's next → Built with → Try it out. Keep "Inspiration" to the real person/problem; put the number in the first paragraph.

### Repo signals
Commits spread across the event (a single final push raises flags; some events forbid pre-existing work), no committed secrets, no placeholder files, a license if the rules want open source, tests that run.

---

## 4. Demo video craft

Sourced guidance (Devpost, lablab, JetBrains judges): 2–3 minutes (check the event's cap); show the product **working within 10–15 seconds**; skip intros and sign-up; start logged in with seeded data; cut waits; one strong end-to-end example instead of a feature tour; screencast + clear narration beats fancy editing; be honest about what works.

Script skeleton (≈2:30):
| Time | Beat |
|---|---|
| 0:00–0:15 | Hook: the problem in one sentence, **with the number**, over the product already running |
| 0:15–1:30 | Live end-to-end run of the one flow. Narrate what's happening and *why it's hard* |
| 1:30–2:00 | The "moment" (the retellable beat) |
| 2:00–2:20 | How it works: architecture in 20 seconds, name the sponsor feature and what depends on it |
| 2:20–2:40 | Evidence (eval result) + honest limits + what's next |

- Narrate every claim you want scored (transcript-friendly). Captions: no source recommends them, but they cost little and help a transcript pass; optional.
- Pre-record rather than demo live; mock or cache slow calls; keep a fallback recording of a clean run.
- Record a **rough cut early** (see `agent-timeline.md`): the Opus 4.7 winners flagged the video as unexpectedly time-consuming.

---

## 5. Pre-submit audit (run as a checklist; also good as a final agent task)

- [ ] Every required field/link/format in the rules is satisfied; submitted early, not at the deadline.
- [ ] Live URL works in a fresh incognito window, no login, seeded data.
- [ ] Video within the length cap; first 15s shows the product; key claims spoken.
- [ ] Every claim in the writeup is true and findable in the repo.
- [ ] README top block: what, who, number, try-it, video.
- [ ] AI-assistance disclosure present in the format the rules require.
- [ ] No secrets in repo/history; no hidden text or judge-directed instructions anywhere.
- [ ] Sponsor tech usage stated specifically; required badges/logos included if asked.
- [ ] Team members/eligibility/prize-category boxes ticked.
