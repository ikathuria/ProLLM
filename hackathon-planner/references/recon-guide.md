# Hackathon Recon Guide (Phase 2)

Goal: turn "I'm entering hackathon X" into a **Judging Model** — what is scored, by whom, with what weights, and what past winners looked like — before any idea is chosen. Rules change per event; always fetch the live rules page rather than relying on this file's base rates.

---

## Step 1: Fetch the rules & overview (primary sources only)

WebFetch the event's Devpost/lablab/DoraHacks/Kaggle page and its **Rules** page (e.g. `<event>.devpost.com/rules`). If a page won't load (DoraHacks and Kaggle often fail), search for a cached/summary source and mark the fields **UNVERIFIED**; ask the user to paste the rules text if critical fields are missing.

Extract into the brief's *Hackathon Facts* table:

| Field | Notes |
|---|---|
| Dates: build window, submission deadline (with timezone!) | Convert to the user's timezone; note "video due later than code" splits (e.g. ElevenLabs: 2h build, 24h to submit video) |
| Team size | Solo allowed? Max? |
| Required tech / model / sponsor API | Is usage mandatory or just a bonus prize? |
| New-work rule | "New work only" (Google, Mistral) vs prior projects allowed if documented (OpenAI). If the user has existing code, this decides what's legal |
| AI-assistance rules | Disclosure format? Session ID? (OpenAI Build Week required README disclosure + Codex session ID; MLH disqualifies for non-disclosure.) No page found bans AI-generated code, but confirm |
| Submission package | Video length cap, repo public?, live URL?, writeup, deck PDF, architecture diagram, cloud-deployment proof |
| **Judging criteria + weights** | Exact wording; note if weighted or equal |
| **Judges & judging method** | Human panel, staff, community vote, **AI-assisted/automated** (search rules for "AI", "automated", "LLM", "analysis") |
| Prizes & categories | Sponsor-feature prizes, People's Choice, regional, "most creative", etc. Multiple prizes = multiple targets |
| Themes/tracks | Free-form vs prescribed problem statements |
| Event type | App-building vs research/eval (e.g. Kaggle red-teaming rewards findings, not apps) |

## Step 2: Classify the judging model

Common criteria families seen across 17 recent events (modal first):
1. **Impact / Technical / Creativity / Presentation**, usually equal (~8 of 17; Mistral 25% each).
2. **Innovation / Technical / Demo**, weighted to Innovation (Gemini Live Agent: 40/30/30 + bonus).
3. **Technical-heavy weighted** (Gemini 3: Technical 40 / Innovation 30 / Impact 20 / Presentation 10).
4. **Impact-first storytelling** (Kaggle Gemma: impact ~40%).
5. **Product/business lens** (lablab, DoraHacks: presentation, business value, tech application, originality).
6. **MLH classic**: Technology, Learning, Originality, Completion.
7. **Vague two-lens** (Anthropic invitational events: no formal published rubric; staff-judged).

Then decide the **build-time weighting**: convert each criterion's weight into a share of effort. Equal-weight events reward being solid everywhere; weighted events justify skewing.

If the judging is AI-assisted or AI-triaged, flag it: the Evidence Plan must then prioritize verifiable, text-legible artifacts (README claim→code table, spoken claims, no-login live URL). See `judging-playbook.md`.

## Step 3: Past winners of THIS hackathon (or its series)

Search in order:
1. `<event name> winners` / `<host> announces winners` (host blog: claude.com/blog, blog.google, elevenlabs.io/blog, ai.meta.com).
2. Devpost project gallery → filter "Winner" (`<event>.devpost.com/project-gallery`). Open 5–8 winning project pages: read tagline, "What it does", video length, tech used, whether a live URL existed.
3. Prior editions of the same series (e.g. earlier Opus/Gemini/ElevenLabs events).
4. Winner interviews/recaps and judge posts (LinkedIn, X, blogs). Judge quotes explaining *why* are rare and valuable — quote verbatim with URL.

For each winner record: name, prize, one-liner, domain, AI technique, demo style, the "moment", builder background (insider?), team size, and **what the judges/criteria rewarded**. Cap at ~8 winners; stop when patterns repeat.

Compare against `winning-patterns.md`: which cross-event patterns hold for *this* event, and which are event-specific (e.g. a sponsor's newest feature, a preferred domain)?

If no past editions exist (new event): say so, use the cross-event base rates, and lean harder on the stated criteria.

## Step 4: Check the field

To gauge saturation: scan the current event's project gallery (if public) or forum for what people are already building. Note the 3 most common idea shapes so you can avoid them or differentiate. (Gallery may be empty until the deadline — note that.)

## Step 5: Budget & output

Budget ~15–25 searches/fetches for a single hackathon. For a fast pass with a single URL, rules page + winners page + 5 winner project pages is the minimum. Write findings into the brief's *Hackathon Facts*, *Judging Model*, and *Winner Patterns for This Event* sections. Keep a **Could not access** list. Distinguish "found nothing" from "couldn't load".

**Deep option:** when the user says stakes are high or the event has a large multi-year history, fan out two subagents (general-purpose, sonnet): one for rules/criteria/judging method, one for past winners; give each fully self-contained prompts and the honesty rules above. Otherwise run it inline.
