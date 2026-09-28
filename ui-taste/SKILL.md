---
name: ui-taste
description: >
  Makes UIs look intentionally designed instead of generic AI output. Use when building,
  restyling, or reviewing any web or mobile UI — pages, landing pages, dashboards,
  components — and whenever the user says "make it look better", "less generic",
  "not AI slop", "polish the UI", or "it looks like every other AI app". Commits to a
  specific design direction before writing code, bans the common AI-default patterns,
  and finishes with a screenshot-based self-critique pass.
---

# UI Taste Skill

AI-generated UIs look alike because the model picks the statistically average choice at every
decision point. This skill forces explicit, non-default decisions and then verifies them visually.

## Step 1 — Commit to a direction (before any code)

Write a 5-line **design brief** in chat and stick to it:

1. **Reference:** one or two real products/eras/print styles this should feel like
   (e.g. "Linear's density + Swiss poster typography", "1970s NASA manual", "Stripe docs").
   Never "modern and clean" — that is the slop default.
2. **Type:** a display face and a text face, chosen for the reference. Not Inter-for-everything.
   Pull options from `${CLAUDE_SKILL_DIR}/references/palettes-and-type.md`.
3. **Color:** one neutral ramp + ONE accent, with a stated reason. Hex values.
4. **Density & rhythm:** base spacing unit and whether this is dense (tool) or airy (marketing).
5. **One signature move:** a single memorable detail (an unusual grid, a typographic hero,
   a distinctive border treatment, real data in the hero). Only one.

If the project already has a design system or brand tokens, the brief *adopts* them — read
existing CSS/Tailwind config first and don't invent a parallel system.

## Step 2 — Build under the ban list

Read `${CLAUDE_SKILL_DIR}/references/slop-patterns.md` and avoid every pattern in it unless
the brief explicitly justifies it. The high-frequency offenders:

- Purple→blue / indigo gradients, gradient text, glowing blobs behind the hero
- Emoji or generic Lucide icons as feature bullets; three identical feature cards in a row
- Everything centered; every section the same height and padding
- `rounded-2xl` + `shadow-lg` on every surface; glassmorphism by default
- Filler copy: "Unlock the power of…", "Seamless", "Elevate your workflow", lorem-ish stats
- Hover `scale-105` on everything; fade-in-on-scroll on every section

Rules that produce the opposite:

- **Hierarchy through type, not boxes.** Use size/weight/color contrast before adding cards or borders.
- **Vary rhythm.** Sections differ in layout (asymmetric split, full-bleed, list, table). Left-align body text.
- **Real content.** Use plausible, specific copy and data — product names, numbers, dates. Specific beats generic.
- **Restraint with radius and shadow.** Pick one radius scale and one elevation; most surfaces get neither.
- **Tokens, not magic numbers.** Define spacing, color, and type as CSS variables / Tailwind theme and use only those.
- **States exist.** Hover, focus-visible, disabled, empty, loading, error — design each, don't leave defaults.
- **Accessibility is non-negotiable:** 4.5:1 text contrast, visible focus, 44px touch targets, prefers-reduced-motion.

## Step 3 — Look at it, then critique

Never declare a UI done without seeing it. Run the app (dev server + built-in browser, or
the `run` skill), screenshot at desktop (1440) and mobile (375), then score against
`${CLAUDE_SKILL_DIR}/references/critique-rubric.md`. Fix everything scoring below 3 and
re-screenshot. Report the brief, the scores, and what you changed.

## Reviewing an existing UI

When asked only to review: skip Step 2, screenshot, run the rubric, and output a prioritized
list of concrete changes (file + what to change), worst offenders first.
