# BRAND.md template

Fill every section with project-specific, concrete values. Delete a section only if it truly
doesn't apply. Keep it scannable: tables and short rules, not essays.

```markdown
# <Project> Brand Guidelines

> Source of truth for tokens: `<path to tokens file>`. If this doc and the tokens disagree, fix one.

## Essence
- **One line:** <what the product is, for whom>
- **Personality:** <3 adjectives>, not <3 adjectives it must never be>
- **Reference:** <real products/eras/print styles this should feel like>
- **Energy level:** <1–5> · **Density:** <dense tool / balanced / airy>

## Voice & copy
- Tone: <e.g. direct, dry wit, never hype>
- Do: <2–3 example phrases in voice>
- Don't: <banned words/patterns, e.g. "Unlock", "Seamless">
- Casing: sentence case for UI; <exceptions>

## Logo
- Files: <paths> · Clear space: <rule> · Min size: <px>
- Don't: stretch, recolor outside palette, place on busy imagery without a backing

## Color
| Token | Hex | Use |
|---|---|---|
| bg | | page background |
| surface | | cards, panels |
| text | | body text |
| muted | | secondary text |
| accent | | primary actions, key highlights |
| accent-2 | | color blocks, illustration, data |
| success / warning / danger | | status only |
Dark mode: <mapping or separate table>. Contrast checked: <pairs + ratios>.

## Typography
| Role | Font | Size / line-height | Weight | Tracking |
|---|---|---|---|---|
| Display | | | | |
| H1–H3 | | | | |
| Body | | 16–18px / 1.5 | | |
| Label / mono | | | | |
Loading: <Google Fonts / self-hosted, font-display: swap>. Numerals: tabular in tables.

## Layout & spacing
- Base unit: <4/8px> · Scale: <tokens>
- Max widths: <content / wide> · Grid: <columns, gutters>
- Section rhythm: <how tight/loose sections alternate>
- Breakpoints: <sm/md/lg/xl px values = token names>
- Responsive behavior: <how each key layout adapts. Nav → menu, tables → cards, grid columns per breakpoint, hero type `clamp()` range>

## Shape & depth
- Radius scale: <values + where each applies>
- Elevation: <shadow tokens + when to use>
- Borders: <weights, colors>

## Signature moves
1. <move>: <where it appears, how to apply it>
2. <move>
3. <move>

## Imagery & iconography
- Imagery: <screenshots / illustration style / photo treatment>
- Icons: <set, stroke weight, size, color rules>

## Motion
- Durations/easing: <tokens>
- Signature interactions: <list>
- Always honor prefers-reduced-motion.

## Components
Rules for buttons (variants, when to use), inputs, cards, nav, tables, empty/loading/error states.

## Do / Don't
| Do | Don't |
|---|---|
| | |

## Accessibility
AA contrast (4.5:1 body, 3:1 large/UI), visible focus ring spec, 44px targets, keyboard paths.
Contrast matrix: <token pair → ratio, light and dark>.

## SEO & metadata (web)
- Title format: `<Page> · <Brand>` (30–60 chars) · Description voice: <rule>, 70–160 chars
- OG/social image: <template/style, 1200×630, path> · Favicon set: <paths>
- Headings: one H1 per page, no skipped levels; don't use styled divs as headings.
```
