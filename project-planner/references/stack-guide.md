# Tech Stack Guide (Phase 3)

**Core rule: choose the most free, self-hostable, and open-source stack possible.** Paid services only when the user explicitly accepts the cost.

**Delegate to installed skills when available.** Before finalizing any layer, check whether a relevant skill is installed (e.g. a `supabase` skill for database/auth design, a framework-specific skill). If one matches a chosen technology, invoke it during planning for that layer instead of relying on the guidance below alone. If not installed, the decision trees here stand on their own.

**Always pin to current versions.** Training data goes stale. Before finalizing, web-search the latest stable major version of each chosen framework/library (e.g. "Next.js latest stable version") and record it in PLAN.md. Never plan against a remembered version.

---

## Decision trees

### Frontend
- Default: **Next.js** (free, Vercel free tier, widely supported)
- Purely static / content site: **Astro** or plain HTML/JS
- Mobile needed: **React Native** (Expo free tier); add web later via the same monorepo
- Heavy interactivity, no SEO need (internal tool): **Vite + React**

### Backend
- Default: **Next.js API routes / route handlers** (colocated, no extra service)
- Heavy backend (long jobs, Python ecosystem, ML): **FastAPI**
- Node service without Next: **Express** or **Hono**
- Avoid: paid BaaS unless the user explicitly accepts cost

### Database
- Default: **SQLite** (local/dev) → **Turso** (free tier, SQLite at the edge)
- Relational + hosted + auth bundled: **Supabase** (free tier, Postgres) — *if chosen and a `supabase` skill is installed, invoke it for schema/RLS design*
- Simple key-value / cache: **Upstash Redis** (free tier)
- Vector search: **pgvector** on Supabase, or SQLite-vec for small scale
- Avoid: paid-only databases

### ORM / data access
- TypeScript default: **Drizzle** (light, SQL-first) — **Prisma** acceptable if the user prefers it
- Python: **SQLAlchemy** or **SQLModel**
- Rule: pick one and state it; don't leave data access ad hoc

### Auth
- Default: **Auth.js (NextAuth)** — free, self-managed
- If already on Supabase: **Supabase Auth**
- Skip auth entirely for single-user/local tools — note it as a non-goal
- Avoid: Auth0/Clerk paid tiers

### Hosting
- Static, no server logic: **GitHub Pages** (always the first choice when possible — completely free, custom domains)
- Frontend with SSR: **Vercel** (free tier) or **Cloudflare Pages**
- Backend / full-stack containers: **Railway** or **Fly.io** (free tiers — verify current free-tier terms, they change)
- Decision rule: no server-side logic → GitHub Pages, full stop

### File storage (if needed)
- Default: **Cloudflare R2** (free tier, no egress fees) or **Supabase Storage** if already on Supabase
- Local-first tools: plain filesystem

### Email (if needed)
- Transactional: **Resend** (free tier) or **Brevo** (free tier)
- Rule: design so email is non-blocking — the app must work if email fails

### Background jobs / scheduling (if needed)
- Simple cron: **GitHub Actions scheduled workflows** (free) or **Vercel Cron**
- Queues/events: **Inngest** or **Upstash QStash** (free tiers)
- Avoid running a dedicated worker host until something actually requires it

### Testing
- TypeScript: **Vitest** (unit) + **Playwright** (E2E, only for flows that matter)
- Python: **pytest**
- Rule: unit tests colocate with features; E2E covers the core feature's happy path at minimum

### CI/CD
- Default: **GitHub Actions** — one workflow: install, lint, typecheck, test on every PR/push to main
- Deploys ride the host's git integration (Vercel/Railway auto-deploy); don't hand-roll deploy scripts

### Analytics (if wanted)
- Default: **Umami** or **Plausible** (self-hosted free) / **Vercel Analytics** free tier
- Product analytics: **PostHog** (generous free tier)
- Avoid Google Analytics for new projects (consent/banner burden)

### Error monitoring
- Default: **Sentry** (free tier) — add at the Deploy milestone, not before

### Payments (if monetizing)
- **Stripe** — free to integrate, per-transaction fee only
- One-time payments: Stripe Checkout (hosted page — least code)
- Subscriptions: Stripe Billing + customer portal (don't build your own portal)

### AI / LLM (if needed)
- Default: **Anthropic API** (Claude) or **OpenAI API**
- Free/local: **Ollama** (fully free, local) or **Groq** (free tier)
- Rule: put the model name and pricing assumption in PLAN.md; LLM cost is the most common hidden cost — cap it in the free tier design

---

## Documenting the choice
For every layer actually used, record in PLAN.md: **choice, pinned current version, one-line reason** (and cost if any). Explicitly list layers deliberately skipped ("no auth — single-user tool") so future sessions don't add them by reflex.
