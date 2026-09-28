# Tech Stack Guide (Phase 3)

**Core rule: choose the most free, self-hostable, and open-source stack possible.** Paid services only when the user explicitly accepts the cost.

**Delegate to installed skills when available.** Before finalizing any layer, check whether a relevant skill is installed (e.g. a `supabase` skill for database/auth design, a framework-specific skill). If one matches a chosen technology, invoke it during planning for that layer instead of relying on the guidance below alone. If not installed, the decision trees here stand on their own.

**Always pin to current versions.** Training data goes stale. Before finalizing, web-search the latest stable major version of each chosen framework/library (e.g. "Next.js latest stable version") and record it in PLAN.md. Never plan against a remembered version.

**Verify free-tier terms too, not just versions.** Free tiers change more often than versions do: they get removed, capped, or restricted. For each hosted service you choose, fetch its current pricing page and confirm the free tier still exists and fits the project. The defaults below were last verified in **September 2026**. Treat any caveat below as something to re-check, not as settled fact.

---

## Decision trees

### Frontend
- Default: **Next.js** (free, Vercel free tier, widely supported)
- Purely static / content site: **Astro** or plain HTML/JS
- Mobile needed: **React Native** (Expo; EAS free tier has a monthly build cap and blocks builds rather than billing); add web later via the same monorepo
- Heavy interactivity, no SEO need (internal tool): **Vite + React**

### Backend
- Default: **Next.js API routes / route handlers** (colocated, no extra service)
- Heavy backend (long jobs, Python ecosystem, ML): **FastAPI**
- Node service without Next: **Express** or **Hono**
- Avoid: paid BaaS unless the user explicitly accepts cost

### Database
- Default: **SQLite** (local/dev) → **Turso** (free tier, SQLite at the edge; the monthly *row-write* cap is the limit you usually hit first)
- Relational + hosted + auth bundled: **Supabase** (free tier, Postgres). **Free projects auto-pause after ~7 days of inactivity**, so warn the user before a demo or launch. *If chosen and a `supabase` skill is installed, invoke it for schema/RLS design.*
- Simple key-value / cache: **Upstash Redis** (free tier)
- Vector search: **pgvector** on Supabase, or SQLite-vec for small scale
- Avoid: paid-only databases

### ORM / data access
- TypeScript default: **Drizzle** (light, SQL-first). **Prisma** is fine if the user prefers it: v7+ dropped the Rust engine, so it's no longer a poor fit for edge runtimes
- Python: **SQLAlchemy** or **SQLModel**
- Rule: pick one and state it; don't leave data access ad hoc

### Auth
- Default: **Better Auth**: free, open-source, self-managed, framework-agnostic
- If already on Supabase: **Supabase Auth**
- Not for new projects: **Auth.js (NextAuth)**. Since Sept 2025 the Better Auth team maintains it with security patches only, and new projects are pointed to Better Auth. Keep it only when extending an existing Auth.js app
- Skip auth entirely for single-user/local tools — note it as a non-goal
- Avoid: Auth0/Clerk paid tiers

### Hosting
- Static, no server logic: **GitHub Pages** (always the first choice when possible — completely free, custom domains)
- Frontend with SSR: **Vercel Hobby** (free, but **non-commercial use only**, and this is enforced) or **Cloudflare Workers with Static Assets** (free tier; Cloudflare now puts new investment into Workers rather than Pages, so prefer Workers for new projects)
  - If the project will make money, don't plan on Vercel Hobby. Budget for Vercel Pro or use Cloudflare Workers
- Backend / full-stack containers: **Render** (free web services spin down when idle, so expect a cold start of several seconds; no card needed)
  - Avoid planning on **Fly.io** (no free tier for new accounts) or **Railway** (short trial credit, then a tiny monthly credit) as "free" hosts. They're fine as paid options
- Decision rule: no server-side logic → GitHub Pages, full stop

### File storage (if needed)
- Default: **Cloudflare R2** (free tier, zero egress fees even on paid) or **Supabase Storage** if already on Supabase
- Local-first tools: plain filesystem

### Email (if needed)
- Transactional: **Resend** (free tier, but its *daily* send cap bites before the monthly one) or **Brevo** (free tier, higher daily allowance)
- Rule: design so email is non-blocking — the app must work if email fails

### Background jobs / scheduling (if needed)
- Simple cron: **GitHub Actions scheduled workflows** (free) or **Cloudflare Workers Cron Triggers** / Vercel Cron
- Queues/events: **Inngest** (free tier pauses at the cap instead of billing overage) or **Upstash QStash** (free daily message cap)
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
- Product analytics: **PostHog** (generous free tier; also covers error tracking and session replay if you want one tool)
- Avoid Google Analytics for new projects (consent/banner burden)

### Error monitoring
- Default: **Sentry** (free Developer tier, **1 user only**). Add it at the Deploy milestone, not before. PostHog's error tracking is an alternative if PostHog is already in use

### Payments (if monetizing)
- **Stripe** — free to integrate, per-transaction fee only
- One-time payments: Stripe Checkout (hosted page — least code)
- Subscriptions: Stripe Billing + customer portal (don't build your own portal)

### AI / LLM (if needed)
- Default: **Anthropic API** (Claude) or **OpenAI API**
- Free/local: **Ollama** (fully free, local) or **Groq** (free tier with rate limits; the set of free models changes, and some popular Llama models were moved off the free tier in Aug 2026, so confirm the specific model is still free before planning on it)
- Rule: put the model name and pricing assumption in PLAN.md; LLM cost is the most common hidden cost — cap it in the free tier design

---

## Documenting the choice
For every layer actually used, record in PLAN.md: **choice, pinned current version, one-line reason** (and cost if any). Explicitly list layers deliberately skipped ("no auth — single-user tool") so future sessions don't add them by reflex.
