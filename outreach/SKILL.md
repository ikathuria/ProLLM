---
name: outreach
description: >
  Drafts professional outreach messages for a job search: LinkedIn connection notes,
  referral asks, replies to recruiters or contacts, follow-ups, thank-you notes, and cold
  emails. Works from a private profile file (background, work authorization, target roles,
  tone rules) so the user never re-explains who they are, and keeps a log of what was sent and
  what got replies. Trigger on "reply to this LinkedIn message", "ask X for a referral",
  "write a follow-up", "draft a cold email to a recruiter", "how should I respond to this
  recruiter", or when the user pastes a LinkedIn profile or message and asks what to say.
---

# Outreach Skill

Good outreach is short, specific to the person, and makes the ask easy to say yes to. The
recurring failures: generic messages, re-explaining the user's background every session, and
stating stale facts (e.g. an old work-authorization status).

## Step 1: Load the profile (never re-ask what's in it)

Read `~/.claude/outreach/PROFILE.md`. It's private and lives outside any repo.
- **Missing:** bootstrap it. Look for profile data in the current project (`PROJECT.md`,
  `config/profile.json`, a resume), draft PROFILE.md from
  `${CLAUDE_SKILL_DIR}/references/profile-template.md`, show it, and ask the user to confirm or
  fix it. Ask only for what you couldn't find.
- **Present:** check its *Last confirmed* date. If it's older than ~30 days, ask one question:
  "Is anything in your profile out of date (work authorization, target roles, graduation)?"
- When the user states a new fact mid-session ("CPT isn't allowed anymore"), update
  PROFILE.md immediately and mention it in one line.

## Step 2: Understand the target

From what the user pasted: who the person is (role, company, how they're connected, any shared
school/employer), and what the user wants (referral, info, reply, follow-up). If the ask
involves specific roles, confirm job IDs or links are in hand. If the user wants you to find
roles, do that first and list them for approval.

## Step 3: Draft

Follow `${CLAUDE_SKILL_DIR}/references/message-patterns.md`. Defaults:
- LinkedIn connection note: ≤300 characters. Message: 60–120 words. Email: ≤150 words.
- One clear ask. Make it easy: offer the job IDs, a resume link, or a short blurb they can forward.
- One specific, true connection point (shared employer, school, their post, their team's work).
  Never invent one.
- Follow the profile's tone rules and "never say" list exactly.

Give **one** draft by default, plus a shorter variant only if the length limit is tight.
Don't send anything; the user sends it.

## Step 4: Log

If the user has a job-search project that already tracks outreach (a recruiters/outreach table,
an API, or a CLI, as described in its PROJECT.md), use that: read the person's history from it
before drafting, and log new messages and replies there. Don't keep a second log. Otherwise,
append to `~/.claude/outreach/LOG.md`: date, person (name + company), channel, type of ask, and
the message's first line. When the user later says someone replied (or didn't), record the
outcome. Before drafting to someone already in the log, read their entries and don't repeat an
ask too soon (wait ~7 days before a follow-up unless they replied).

Every ~10 recorded outcomes, note in PROFILE.md's *What works* section which openings and asks
got replies.
