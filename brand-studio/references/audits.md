# Accessibility & SEO audits

Run on every changed page/screen **before** the rebrand (baseline) and **after**. Record
results in a before/after table. The goal is no regressions and every blocker fixed.

## Accessibility (all projects)

**1. Automated scan: axe-core** (web). In the built-in browser, on each key route:

```js
await new Promise(r => { const s = document.createElement('script');
  s.src = 'https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js'; s.onload = r;
  document.head.appendChild(s); });
const r = await axe.run(document, { runOnly: ['wcag2a','wcag2aa','wcag21aa','wcag22aa','best-practice'] });
r.violations.map(v => ({ id: v.id, impact: v.impact, count: v.nodes.length, sample: v.nodes[0]?.target }));
```

Alternatives if the project has them: `npx @axe-core/cli <url>`, `npx lighthouse <url>
--only-categories=accessibility`, eslint-plugin-jsx-a11y, or the platform tools (Xcode
Accessibility Inspector, Android Accessibility Scanner). Fix all `critical` and `serious`
issues. Check the rest by hand.

**2. Palette contrast matrix.** Compute WCAG ratios for every text/background and UI/background
token pair in both light and dark mode (a short script over the token file is fine). Body text
needs at least 4.5:1, large text and UI parts at least 3:1. Record the table in BRAND.md.

**3. Manual checks** (axe can't do these):
- Keyboard: Tab through each key flow. Focus order is logical, focus is always visible, there
  are no traps, and modals return focus. A skip link exists on content sites.
- Semantics: landmarks (`header/nav/main/footer`), buttons are `<button>`, links are `<a>`,
  every input has a label, and icon-only controls have `aria-label`.
- Images: meaningful images have descriptive alt text, and decorative ones have `alt=""`.
- Motion: `prefers-reduced-motion` disables the non-essential animation.
- Zoom and reflow: at 200% zoom and 320px width nothing is cut off and there's no horizontal scroll.
- Color is never the only way information is shown (errors, status, charts).

## Responsiveness (all projects)

**1. Width sweep.** For each key screen, use `resize_window` in the built-in browser (custom
width/height, then reload) and screenshot at:

| Width | Represents |
|---|---|
| 320 | small phone (iPhone SE), the reflow floor |
| 375 / 390 | standard phone |
| 768 | tablet portrait |
| 1024 | tablet landscape / small laptop |
| 1280 | laptop |
| 1440 | desktop |
| 1920 | large desktop |
| 2560 | ultra-wide (quick check that content stays readable, not stretched) |

Also check phone landscape (e.g. 812×375). Reset the viewport to `desktop` when done. For
native apps, use the simulator on the smallest and largest supported devices and an iPad or
tablet if supported.

**2. Per-width automated check.** Run this at every width:

```js
(() => {
  const vw = document.documentElement.clientWidth, touch = vw < 1024, out = [];
  if (document.documentElement.scrollWidth > vw) out.push(`page h-scroll: ${document.documentElement.scrollWidth}px > ${vw}px`);
  for (const el of document.querySelectorAll('body *')) {
    const cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
    const id = el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/)[0] : '');
    if (r.right > vw + 1 && cs.position !== 'fixed') out.push(`overflows right: ${id} (${Math.round(r.right)}px)`);
    if (el.scrollWidth > el.clientWidth + 1 && ['visible','clip','hidden'].includes(cs.overflowX) && el.children.length === 0) out.push(`clipped text: ${id}`);
    if (touch && el.matches('a,button,input,select,textarea,[role=button],[tabindex]') && (r.width < 44 || r.height < 44)) out.push(`small target ${Math.round(r.width)}×${Math.round(r.height)}: ${id}`);
    if (touch && el.matches('p,li,td,label,input') && parseFloat(cs.fontSize) < 16) out.push(`small text ${cs.fontSize}: ${id}`);
  }
  return { vw, issues: [...new Set(out)].slice(0, 40) };
})()
```

Inline links within paragraphs may fall under 44px tall. That's acceptable if they're spaced,
so judge those by hand.

**3. Manual checks:**
- **Breakpoint transitions:** drag through ±50px around each breakpoint. Nothing should jump,
  overlap or collapse oddly at in-between widths.
- **Layout intent:** at every width the layout should look designed, not just stacked. Nav
  becomes a menu that works with touch and keyboard, tables become cards or scroll inside
  their container, multi-column grids reduce sensibly, and the hero type scales down
  (`clamp()`) instead of wrapping one word per line.
- **Touch:** nothing important is only reachable by hover. Hover styles use
  `@media (hover: hover)`.
- **Content stress:** long headings and names, ~30% longer text (translation), empty data and
  very full data, and large numbers. Text truncates with an ellipsis or wraps cleanly, never overlaps.
- **Media:** images use `srcset`/`sizes` or the framework's image component, keep their aspect
  ratio, and art-direct hero images on mobile when cropping hides the subject.
- **Viewport units:** full-height sections use `dvh`/`svh` (not raw `100vh`) so mobile browser
  bars don't cut them off. Respect safe areas (`env(safe-area-inset-*)`) for fixed bars.
- **Readability on wide screens:** body text stays at most ~75ch wide at 1920 and 2560.

## SEO (web projects with public pages; skip for auth-only apps)

Per public route, check with a quick DOM script in the browser plus the source:

```js
({ title: document.title, titleLen: document.title.length,
   desc: document.querySelector('meta[name=description]')?.content,
   h1s: [...document.querySelectorAll('h1')].map(h => h.textContent.trim()),
   headings: [...document.querySelectorAll('h1,h2,h3')].map(h => h.tagName),
   canonical: document.querySelector('link[rel=canonical]')?.href,
   og: [...document.querySelectorAll('meta[property^="og:"],meta[name^="twitter:"]')].map(m => [m.getAttribute('property')||m.name, m.content]),
   lang: document.documentElement.lang,
   viewport: !!document.querySelector('meta[name=viewport]'),
   imgsNoAlt: [...document.querySelectorAll('img:not([alt])')].length,
   icons: [...document.querySelectorAll('link[rel*=icon],link[rel=manifest]')].map(l => l.href) })
```

Must pass:
- A unique `<title>` of 30–60 chars, following the BRAND.md title format.
- A meta description of 70–160 chars, written in the brand voice and specific to the page.
- Exactly one H1, and headings that don't skip levels. A redesign must not turn headings into styled divs.
- `lang`, viewport, canonical, and Open Graph + Twitter tags with a **branded OG image** (1200×630).
- Favicon set (svg/ico, apple-touch-icon 180px, manifest icons) regenerated in the new brand.
- Image alt text, `width`/`height` set (no layout shift), and modern formats where possible.
- Fonts: `font-display: swap`, preload only the display face, and at most ~2 families and ~4 weights.
- Existing URLs, structured data (JSON-LD), robots.txt and sitemap still work after the rebrand.

**Performance / Lighthouse:** if possible run `npx lighthouse <url> --only-categories=performance,seo,accessibility,best-practices --output=json`
(or read Core Web Vitals from the browser). A rebrand must not drop scores. Watch for heavy
fonts, unoptimized hero images, and animation libraries added for a single effect.

## Report format

```
Audit        Before   After   Notes
axe (crit/serious)  3/7  0/0
Contrast pairs fail  4    0
Keyboard flows       ✗    ✓     modal focus trap fixed
Responsive issues (320–2560)  12  0  nav overflow at 768, table cards on mobile
SEO checks passed    6/11 11/11 added OG image, fixed double H1
Lighthouse A11y/SEO/Perf  78/82/64  98/100/71
```
