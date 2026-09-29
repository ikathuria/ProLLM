# What Wins: Evidence Base

Distilled from a September 2026 research pass over ~9 AI hackathons and ~36 winning projects (Anthropic "Built with Opus" 4.6/4.7/4.8, ElevenLabs Worldwide, Gemini API Competition, Gemma 3n Impact Challenge, Gemini 3, LlamaCon / Llama Impact, Mistral Worldwide, OpenAI gpt-oss red-teaming). Use this to generate and score ideas (Phase 3).

**Reliability note:** patterns below are drawn from public winner announcements. Sources rarely include judge quotes explaining *why* something won, so "why" statements are inference unless marked. Where the pattern is inference, it says so. Re-verify anything you plan to lean on hard; hackathon meta shifts every few months.

---

## Patterns among winners (ranked by how well-supported)

### 1. Domain insiders beat generalist engineers
Four of five Anthropic Opus 4.6 winners were non-engineers: a personal-injury lawyer (1st, CrossBeam, housing permits: "we have a permit crisis"), a cardiologist (3rd, PostVisit.ai), an infrastructure specialist (TARA), a musician (Conductr). Later winners: a geologist (LlamaCon, Geo-ML), an education specialist (Maieutic), lexicologists (ElevenLabs).
**Use:** the single strongest lever is *which problem you have inside knowledge of*. Ask the user what they know that a generalist doesn't (job, past job, family, hobby, community). Prefer ideas where the user can say "I've lived this."

### 2. Personal, high-stakes problems — especially accessibility
Vite Vere (cognitive disability; won Most Impactful + People's Choice on Gemini API, then 2nd on Gemma 3n), Gaze Link (ALS), Viddyscribe, Gemma Vision (blind users; built with input from the developer's blind brother), 3VA (cerebral palsy), Dream Assistant, Netra. ElevenLabs' RoadMate came from a teammate's friend's accident.
**Use:** a named real person with a real cost beats "users" in the abstract. If the user can talk to one real person with the problem before/during the build, that is worth more than a feature.

### 3. Unglamorous, costly problem + a number
Permits with a reported 90%+ first-time rejection rate (CrossBeam). Sim Francisco (Opus 4.8, 2nd) published predicted-vs-actual results: 81.3% vs 83.8% on the 2024 presidential vote, 70% vs 70.38% on a ballot measure.
**Use:** every project needs one *measured* claim. Plan the eval as a deliverable, not an afterthought.

### 4. Verification is a visible feature
Tekton (Opus 4.8, 1st) had verifier agents grade builds until tests pass and every component traceable to a source. Sim Francisco scored itself against reality. Red-teaming winners were judged on reproducible evidence.
**Use:** show the checking loop in the demo (source citations, pass/fail grading, before/after, held-out test set). This also reads well to AI judges (see `judging-playbook.md`).

### 5. Multimodal / voice / physical-world
In the 36-row winner table, ~9 involve voice and ~12 vision/video; hardware appears in Gemma Vision, Wrench Board, Custom Universe. On-device/offline is favoured at Gemma events (expected, given sponsor pitch).
**Use:** when the theme allows, a voice or camera input makes the demo self-evidently "not a chatbot." Weigh against the failure risk of live hardware/audio in a recorded demo.

### 6. Sponsor-feature prizes shape outcomes
Named prizes existed for Claude Managed Agents, Unsloth, Ollama, NVIDIA Jetson, LeRobot, Llama API. Winners often used the sponsor's newest feature.
**Use:** read the prize list; using the sponsor's headline feature earns extra eligibility *only if it's genuinely load-bearing*. Say specifically why it fits.

### 7. One memorable "moment"
GibberLink (ElevenLabs global winner: two voice agents realise they're both AI and switch to an audio protocol — one clear beat, covered by Forbes/TechCrunch). Mistral's global winner: an "agentic civilisation" that elected its own mayor. Outdraw AI, Virtual Puppet Theater: instantly graspable.
**Use:** define the one beat a judge will retell in one sentence. If you can't, the idea lacks a hook.

### 8. Small teams, 1–3 people
Where stated, most winners were 1–3 (Opus events allowed max 2). Not a rule; a base rate.

### 9. Odd-one-out: research-style events reward findings, not apps
OpenAI gpt-oss red-teaming (Kaggle) rewarded reproducible findings and eval libraries. Read the event type before assuming "build an app."

---

## Failures and judge complaints (sourced)

- "AI meaningfully integrated, not just a chatbot wrapper"; "a fresh angle, not an existing product with a chatbot bolted on" (lablab.ai guide).
- Judge Daren Tan (20+ hackathons, LinkedIn): identical vibe-coded designs everywhere; 8–10 disconnected features; LLM used where a form would do; poor tech choice for the domain, especially healthcare.
- lablab.ai: mid-hackathon pivots, no meaningful commit history, local-only builds with no deployed demo, over-engineering the AI layer.
- Devpost: polished UI with thin code, template/cosmetic resubmissions, ignoring the rubric.
- Mistral recap: winners "paused and rethought" rather than maximising technical complexity.

**Snippet-level / UNVERIFIED (do not present as fact):** "judges have seen a hundred GPT wrappers"; "early impressions dominate scoring"; specific ideas like "AI tutor" / "AI resume" being overused — no judge commentary found naming them. Generic chatbots, wellness bots and feature-stuffed assistants *are* named as weak.

**Inference (not sourced):** because agents make building cheap, expect judges to see many more competent-but-similar apps; differentiation shifts toward problem choice, real-user grounding, taste, and evidence. No organizer statement found saying this explicitly.

---

## Ideas the evidence says are strong vs weak

| Strong shape | Weak shape |
|---|---|
| Domain insider fixes a costly, specific workflow (permits, clinical follow-up, repair diagnostics) | Generic chatbot/RAG over docs |
| Accessibility tool built with/for one real person | "AI tutor / AI assistant for X" with no insider angle |
| Agent + verification loop with a measured accuracy claim | 8–10 loosely connected features |
| Voice/vision/hardware moment that's clear in 10 seconds | UI-polished shell over thin logic |
| One surprising, retellable beat | Sponsor tech name-dropped, not needed |
| Simulation/forecast scored against ground truth | Idea that needs users/data you can't get in the window |

## Gaps in this evidence base

Kaggle, lablab, Cerebral Valley, HF/Gradio and MLH winner galleries were not reached; Gemini 3 Devpost winners were snippet-only; OpenAI Open Model Hackathon winners not found; few direct judge quotes. Phase 2 of the skill should fill these gaps for the *specific* hackathon being entered.
