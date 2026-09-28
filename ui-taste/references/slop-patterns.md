# AI Slop Patterns — Ban List

Each item: the pattern, why it reads as AI, and what to do instead.

## Color
| Pattern | Instead |
|---|---|
| Indigo/violet primary (`#6366f1`, `violet-500`) by default | Derive the accent from the reference; muted or unexpected hues (ochre, oxblood, forest, signal orange) |
| Purple→blue/pink gradient backgrounds, gradient text | Flat color; if a gradient, make it subtle and same-hue |
| Blurred glowing blobs / aurora behind hero | Real product screenshot, typography, or nothing |
| Pure `#000` on pure `#fff`, or gray-on-gray low contrast | Tinted neutrals (warm or cool), checked for contrast |
| Dark mode = slate-900 + neon accents | Designed dark palette with reduced-saturation accent |

## Layout
| Pattern | Instead |
|---|---|
| Hero: centered H1 + subtitle + two buttons + screenshot | Asymmetric hero, left-aligned, or lead with the product itself |
| 3 identical icon-cards "Features" grid | Varied layout: list with detail, alternating rows, a table, a single deep feature |
| Every section `py-24`, same max-width | Deliberate rhythm — tight and loose sections, some full-bleed |
| Cards inside cards inside cards | Flatten; use spacing and dividers |
| Bento grid for everything | Only when content actually has different sizes |

## Components & detail
| Pattern | Instead |
|---|---|
| `rounded-2xl shadow-xl` on all surfaces | One radius scale (e.g. 4/8), shadow only on floating layers |
| Glassmorphism / backdrop-blur panels | Solid surfaces unless layered over imagery |
| Emoji as icons ✨🚀 | No icon, a custom mark, or a consistent icon set used sparingly |
| Pill badges "New ✨" above every H1 | Remove |
| Fake testimonials with stock avatars | Real quotes or omit |
| Stats row "10k+ users · 99.9% uptime · 24/7" | Only true, specific numbers |

## Type
| Pattern | Instead |
|---|---|
| Inter/system for everything, one weight | Distinct display + text pairing, 2–3 weights, a real type scale |
| Huge bold H1, tiny gray body | Controlled scale (e.g. 1.25 ratio), readable body 16–18px, 60–75ch line length |
| Title Case Everywhere | Sentence case |

## Motion
| Pattern | Instead |
|---|---|
| Fade-up on every section scroll | Motion only where it communicates change |
| `hover:scale-105` on cards and buttons | Color/underline/border change; 150–200ms ease-out |

## Copy
Ban: "Unlock", "Elevate", "Seamless(ly)", "Supercharge", "Revolutionize", "Harness the power",
"Your all-in-one", "Built for the modern…", "Say goodbye to…". Write what the product does,
for whom, concretely.
