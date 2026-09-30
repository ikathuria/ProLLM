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
SEO checks passed    6/11 11/11 added OG image, fixed double H1
Lighthouse A11y/SEO/Perf  78/82/64  98/100/71
```
