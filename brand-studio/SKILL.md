---
name: brand-studio
description: >
  End-to-end UI redesign and rebranding that looks intentionally designed instead of generic
  AI output. Understands the whole project first, proposes 3–5 distinct visual directions as
  rendered previews, turns the chosen one into brand guidelines saved in the repo (BRAND.md +
  design tokens), confirms them with the user, then rebrands the UI and verifies it with
  screenshots. Use when the user asks for a better/new/redesigned UI, a rebrand, brand
  guidelines, a design system for their app, "make it look better", "less generic", "not AI
  slop", "polish the UI", or "it looks like every other AI app". Also handles quick reviews of
  an existing UI. Combines design direction, branding, and implementation in one flow.
---

# Brand Studio

AI-generated UIs look alike because the model picks the statistically average choice at every
decision point. This skill forces explicit, non-default decisions, lets the user pick a
direction, locks it into brand guidelines, and then verifies the build visually.

**Slop is defaulting, not decorating.** There are two failure modes, and both are slop:

- **Template slop**: purple gradients, glow blobs, three icon cards, `rounded-2xl` everywhere.
- **Sterile slop**: the overcorrection. Beige background, one gray serif, hairline borders,
  no color, no imagery, no motion. Safe, "tasteful", and forgettable.

The goal is a UI with a point of view and some *energy*. Remove the defaults, then replace them
with bold, specific choices.

## Choosing the mode

| Request | Mode |
|---|---|
| "Better UI", redesign, rebrand, "make it look good", new project UI | **Full flow** (Phases 1–6) |
| Project already has `BRAND.md` / design tokens and asks for a new page or polish | Skip to **Phase 5**, building under the existing brand |
| "Review my UI" / "what's wrong with this design" | **Review only** (bottom of file) |
| One small component tweak | Phase 5 rules only, no options round |

Two user checkpoints are mandatory in the full flow: **choosing a direction** (Phase 3) and
**approving the brand** (Phase 4). Don't touch app code before both.

## Phase 1: Understand the project

Read before designing. Skim broadly, then write a short **project read** in chat:

- **What it is and who it's for:** README, docs, PLAN.md/PROJECT.md, landing copy, package
  name, marketing pages. Who are the users, what's the job, what's the tone (serious tool,
  playful consumer app, premium, technical)?
- **What exists:** framework and styling stack (Tailwind config, CSS variables, component
  library such as shadcn, MUI, or native), existing logo/colors/fonts, any `BRAND.md`,
  `DESIGN.md`, Figma links, or design tokens.
- **Screens that matter:** list the key routes/screens (landing, dashboard, core flow) and
  screenshot the current state if it runs (dev server + built-in browser, or the `run` skill).
- **Constraints:** brand assets that must stay (logo, legal colors), accessibility needs,
  dark mode, mobile, i18n.

Ask the user only what the code can't tell you: things like a hard brand constraint, or
products they admire. At most 2–3 questions, and skip them if the answers are clear.

## Phase 2: Generate 3–5 directions

Each direction is a genuinely different answer, not five shades of the same idea. Span the
range: at least one safe-but-sharp option, one bold option, and one unexpected option. Each
direction includes:

1. **Name + one-line pitch** ("Field Manual: 1970s NASA documentation, utilitarian and confident").
2. **Reference:** real products/eras/print styles. Never "modern and clean".
3. **Type:** display + text face (see `${CLAUDE_SKILL_DIR}/references/palettes-and-type.md`).
4. **Palette:** neutral ramp + primary accent + optional secondary colors, as hex values.
5. **Energy level (1–5)** and density (tool-dense vs airy).
6. **2–3 signature moves:** committed, memorable details (oversized type hero, color-blocked
   sections, custom pattern/illustration, unusual grid, a playful interaction).
7. **Why it fits this project**, tied to the Phase 1 read.

**Render them.** Descriptions alone aren't enough. For each direction, build a preview of the
project's *real* key screen with real copy from the project (not lorem):

- Write self-contained HTML files to `design/options/option-N-<slug>.html` in the repo (or
  the scratchpad if the user doesn't want files in the repo), plus an `index.html` that
  shows all options side by side.
- If an Artifact tool with a Design type is available, you may publish the options there
  instead (run its quickstart first), so they're viewable and shareable.
- Screenshot each at 1440 and 375 and check them against the ban list before showing them.
  Every option must pass. Don't show a strawman.

Present a compact comparison table (name · feel · energy · best for) and the preview links.

## Phase 3: User chooses

Ask the user to pick one, or to mix ("option 2's type with option 4's colors"). Use
AskUserQuestion with the option names when available. Iterate on the previews if asked.
Don't proceed on your own guess.

## Phase 4: Write the brand guidelines, then confirm

Turn the chosen direction into durable guidelines using
`${CLAUDE_SKILL_DIR}/references/brand-template.md`:

- **`BRAND.md`** at the repo root (or `docs/BRAND.md` if a docs folder exists): essence,
  voice, logo usage, color, type, spacing, radius/elevation, iconography, imagery, motion,
  component rules, do/don't examples, accessibility.
- **Tokens in the project's native format:** Tailwind theme (`tailwind.config` or CSS
  `@theme` for v4), CSS custom properties, or platform equivalents (SwiftUI `Color` assets,
  Flutter `ThemeData`, RN theme object). The tokens are the source of truth, and BRAND.md
  references them.
- If the repo has a `CLAUDE.md`, add one line pointing to BRAND.md so future sessions build
  on-brand automatically.

If there is no repo, give the guidelines as a document instead (a Docs artifact if available).

Then **confirm with the user**: show a summary (palette swatches, type specimen, voice, and
2–3 key rules) and ask for approval or edits. Rebranding only starts after a clear yes.

## Phase 5: Rebrand the project

Plan the rollout, then implement in this order so the app never looks half-migrated:

1. **Tokens and globals:** fonts, CSS variables/theme, base styles, dark mode.
2. **Primitives:** buttons, inputs, cards, nav, badges. Re-theme the component library
   rather than forking it.
3. **Key screens:** the ones from Phase 1, highest-traffic first, applying signature moves.
4. **Copy pass:** rewrite generic copy in the brand voice (ban list in slop-patterns.md).
5. **Remaining screens + states:** empty, loading, error, hover, focus, disabled.

Build rules:

- Avoid every pattern in `${CLAUDE_SKILL_DIR}/references/slop-patterns.md` unless the brand
  justifies it. The list bans *defaults*, not *effects*.
- **Hierarchy through type, not boxes.** Vary rhythm across sections, and left-align body text.
- **Spend the boldness budget.** Every screen gets at least one moment of contrast: a dramatic
  type-scale jump, a saturated color block, imagery/illustration, or texture.
- **Motion with personality:** a few crafted moments, respecting `prefers-reduced-motion`.
- **Tokens only.** No magic hex values or pixel numbers outside the token files.
- **Accessibility is non-negotiable:** 4.5:1 text contrast, visible focus, 44px targets.
- Keep behavior unchanged. This is a visual and copy change. Run the existing tests/build.

For large projects, confirm the screen list and order with the user before step 3, and
commit in logical chunks if the user wants commits.

## Phase 6: Verify and critique

Never declare it done without seeing it. Screenshot the key screens at 1440 and 375 (and in
dark mode if supported), score against `${CLAUDE_SKILL_DIR}/references/critique-rubric.md`,
fix anything below 3, and re-screenshot. Also check that the result matches BRAND.md. Ask
yourself explicitly: *"Is this boring?"* If yes, push the signature moves before polishing.

Report: the chosen direction, the files created (BRAND.md, tokens), the screens changed,
before/after screenshots, the scores, and anything left to do.

## Review only

Screenshot, run the rubric, and output a prioritized list of concrete changes (file + what to
change), worst offenders first. If there's no brand yet, offer to run the full flow.
