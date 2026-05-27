# Strategy-First Content Workflow — Design Spec

**Date:** 2026-05-27
**Status:** Draft
**Goal:** Upgrade the AI Marketing Team to be strategy-led, voice-authentic, and self-correcting — applying six content principles from an 8M-follower creator: strategy > trends, resonance > reach, automate repetitive tasks, review analytics regularly, you are the niche, right audience over large audience.

---

## Problem

The existing AI Marketing Team is optimized for output quality but not strategic alignment. Agents produce on-brand, well-scored content — but no agent asks:

- Does this piece serve our 3-month narrative?
- Could only Yoobin have written this?
- Are we attracting the right people or just more people?
- What did we learn from last week?

Without these checks, the system risks producing high-quality content that drifts — chasing trends, sounding generic, and growing the wrong audience.

---

## Solution Overview

Five components:

1. **`docs/marketing/strategy-compass.md`** — the strategic north star all agents read before acting
2. **`docs/marketing/yoobin-voice.md`** — Yoobin's unique POV anchor, read by Yoobin-facing agents
3. **`meetings/` folder** — raw material from user calls and co-founder sessions, wired into the pipeline
4. **Agent upgrades** — Trend Scout, Content Strategist, Creative Director, Idea Generator each get new steps wired to the above documents
5. **Monday 8AM weekly review cron** — automated synthesis of what resonated, what drifted, and whether the compass needs updating

---

## Component 1: `docs/marketing/strategy-compass.md`

### Purpose
The single document that defines what the content system is building toward. Every agent reads it before making decisions. Trends are inputs — the compass is the filter.

### Structure

```markdown
# Strategy Compass

## Current Narrative Arc
[The story we're telling right now — specific to this month/quarter. Not "we're building a startup" but the actual chapter: e.g. "Final push to App Store launch — every piece makes a future Bloggo user feel like they were there."]

**Active through:** [date]

---

## The Right Audience
[Tight description of who we're trying to reach — not a persona, a resonance definition. E.g.: "Follows 2–3 indie founders. Saves posts, doesn't just like them. Building something or seriously thinking about it. Cares about privacy and craft over hype."]

**Resonance signals:** [What tells us we reached the right person — saves > likes ratio, DMs, comments that say "this is exactly me", shares to close friends not broadcast]

---

## What We're Saying NO To
[Explicit list of trends, topics, formats we won't chase even if they're performing. Updated when needed.]

- [ ] Example: viral "day in my life" formats that don't connect to building
- [ ] Example: AI hype content that leads with technology, not human benefit

---

## Strategic Pillars With Purpose
[Not just pillar names — the WHY behind each one, so agents understand what job each pillar is doing in the overall strategy]

**Yoobin pillars:**
- Building in Public — [what this pillar is building toward strategically]
- Product Builder Lessons — [purpose]
- The Traveler — [purpose]
- Startup Reality — [purpose]

**Bloggo pillars:**
- The Problem — [purpose]
- The Magic — [purpose]
- Travel Inspiration — [purpose]
- Brand Values — [purpose]
- Community — [purpose]

---

## Current Phase
[Pre-Launch / Launch Week / Post-Launch]

**CTA:** [current CTA — mirrors Content Engine.md]

---

## Compass Version History
| Date | Change | Why |
|------|--------|-----|
| 2026-05-27 | Initial compass | Strategy-first workflow launch |
```

### Owner
**Written and maintained by:** Yoobin (founder)
**Updated when:** narrative arc shifts, phase changes, or Weekly Review flags ⚠️ or 🔴

---

## Component 2: `docs/marketing/yoobin-voice.md`

### Purpose
The authenticity anchor for all Yoobin personal brand content. Captures what only Yoobin can say. Prevents the Creative Director from approving technically competent but generically founder-sounding pieces.

### Structure

```markdown
# Yoobin Voice Document

## The "Only I Can Say This" Test
Before writing or approving any Yoobin piece, ask: if you replace "I" with "any founder," does the piece lose meaning? If not, it fails. Rewrite until it passes.

---

## Specific Lived Experiences
[Real moments from building Bloggo that no other founder has. Specific, named, dated where possible.]

- [Experience 1 — specific moment, not generic category]
- [Experience 2]
- [Experience 3]

---

## Strong Opinions and Takes
[Things Yoobin actually believes that other founders might push back on. Not "work hard and stay consistent" but real, specific, possibly controversial positions.]

- [Opinion 1]
- [Opinion 2]

---

## Voice Markers
[How Yoobin actually talks — recurring phrases, energy, cadence. What makes her voice recognizable.]

- [Marker 1]
- [Marker 2]

---

## Anti-Patterns (What Generic Sounds Like)
[Specific examples of what Yoobin content sounds like when it's being generic — so the Creative Director can catch it]

- ❌ "Building a startup is hard but worth it" — could be anyone
- ❌ "I learned that consistency matters" — could be anyone
- ✓ [Specific Yoobin example of authentic voice]

---

## Voice Document Version History
| Date | Change |
|------|--------|
| 2026-05-27 | Initial document |
```

### Owner
**Written and maintained by:** Yoobin (founder)
**Updated when:** new experiences become content-worthy, voice evolves, anti-patterns are spotted in the wild

---

## Component 3: `meetings/` Folder

### Purpose
Raw material from user calls and co-founder sessions. Connected to the content pipeline so insights don't sit unused.

### Location
`meetings/` at the project root.

### File Naming
`YYYY-MM-DD-[type]-[brief-description].md`

**Types:** `user-call`, `cofounder`, `investor`, `research`

**Examples:**
- `2026-05-27-user-call-sarah-onboarding-feedback.md`
- `2026-05-20-cofounder-feature-cut-decision.md`

### Note Format

```markdown
# [Meeting Title]

**Date:** YYYY-MM-DD
**Type:** user-call / cofounder / investor / research
**Participants:** [names or roles]

---

## Key Takeaways
- [Bullet point takeaways]

---

## Potential Content Angles
[Optional — leave blank if you want agents to surface these]
- [Angle 1]
- [Angle 2]

---

## Follow-up Actions
- [ ] [Action item]
```

### Agent Connections
- **Idea Generator** (4AM cron) — scans `meetings/` for notes from the past 7 days, generates 2–3 content ideas per note, adds to Notion idea bank
- **Content Strategist** — scans `meetings/` for notes from the past 14 days, surfaces as "Why now" angles and "Building in Public" raw material
- **Weekly Review** — flags any meeting notes from the past week not yet converted to content

---

## Component 4: Agent Upgrades

### 4a. Trend Scout Upgrade

**New Step 6 — Strategy Filter** (runs after all searches, before writing the brief):

For every trend signal found, evaluate against `docs/marketing/strategy-compass.md`:
- **Aligned with narrative arc** → surfaces normally in the brief
- **Off-strategy** → moved to a new `## Skipped Signals` section at the bottom of the brief with a one-line reason

**New column in trend signals table — "Yoobin Angle":**
For each signal, propose how Yoobin specifically would frame it, grounded in `docs/marketing/yoobin-voice.md`. Not the generic founder take — her specific take.

**Updated brief output template adds:**
```markdown
## Yoobin Angles
| Signal | Yoobin's Specific Frame |
|--------|------------------------|
| | |

## Skipped Signals (Off-Strategy)
| Signal | Reason skipped |
|--------|---------------|
| | |
```

---

### 4b. Content Strategist Upgrade

**New Step 0 — Read Strategy Documents** (before reading the trend brief):

Read `docs/marketing/strategy-compass.md` and `docs/marketing/yoobin-voice.md`. Extract:
- Current narrative arc and active-through date
- What we're saying NO to right now
- Resonance definition for our specific audience

Then scan `meetings/` for notes from the past 14 days. Flag any customer insights or product decisions worth grounding a piece in.

Then proceed to trend brief. The compass is the **lens** — trends and pillar gaps are **raw material**.

**New field on every piece in the content plan:**
```
- **Strategic Purpose:** [one sentence — what does this piece do for the 3-month arc?]
- **Source:** [Trend signal / Pillar gap / Meeting note — YYYY-MM-DD]
```

If the Strategist cannot articulate a strategic purpose for a piece, it should not be included in the plan.

---

### 4c. Creative Director Upgrade

The 28/35 scoring threshold is unchanged. Two new items added to the brand compliance checklist (9 items → 11 items):

**Check 10 — Strategic Fit** (all pieces):
> Read `docs/marketing/strategy-compass.md`. Does this piece serve the current narrative arc? Could it have been posted any month by any founder without losing meaning? If yes → flag. Must be revised to connect to the current arc before passing.

**Check 11 — Voice Authenticity** (Yoobin pieces only):
> Read `docs/marketing/yoobin-voice.md`. Does this pass the "only Yoobin can say this" test? If you can replace "I" with "any founder" and the piece still works → flag. Must include at least one specific lived experience, opinion, or voice marker from the voice document before passing.

Both are **pass/fail gates** — not scoring signals. A piece scoring 34/35 still gets sent back if it fails Check 10 or 11.

---

### 4d. Idea Generator Upgrade

**New Step 0 — Scan Meeting Notes** (before running news searches):

Scan `meetings/` for notes created in the past 7 days.

For each note found:
- Extract key takeaways
- Generate 2–3 content ideas grounded in the meeting insight
- Label each idea with its source: `[Meeting: YYYY-MM-DD-type-description]`

Add these to the Notion idea bank alongside the usual trend-derived ideas.

If no new meeting notes found: proceed normally, skip this step silently.

---

## Component 5: Monday 8AM Weekly Review Cron

### Schedule
`0 8 * * 1` — 8AM every Monday

Runs after the 4AM trend brief is already written, so the review feeds into the same morning's content planning if `/run-marketing-team` is run that day.

### What It Reads
- All `briefings/` files from the past 7 days
- Notion Content Engine (both accounts) — posts from 7–14 days ago (old enough to have real metrics)
- Performance learnings already appended to trend briefs
- `meetings/` — notes from the past 7 days not yet converted to content

### Output
`briefings/weekly-review-YYYY-MM-DD.md`

### Review Brief Structure

```markdown
# Weekly Review — [Full date]

## 1. Resonance Report
[Which pieces from last week are showing saves/shares above average?
Which got comments that feel like "this is exactly me"?
Flag top performers — pattern to repeat.]

| Piece | Format | Account | Signal | vs. Average |
|-------|--------|---------|--------|-------------|

**Top performer pattern:** [what specifically drove the strong signal]

---

## 2. Strategic Drift Audit
[Did every piece this week have a clear strategic purpose?
Did any off-strategy trends make it into the final batch anyway?
Were all Yoobin pieces grounded in her specific voice?]

- Pieces with clear strategic purpose: N/11
- Pieces that felt generic or trend-chasing: [list]
- Yoobin pieces that passed voice authenticity in execution: N/5

---

## 3. Unused Meeting Insights
[Meeting notes from the past 7 days not yet converted to content]

| Note | Key Insight | Suggested Piece |
|------|-------------|----------------|

---

## 4. Compass Update Recommendation

**Verdict:** ✅ On track / ⚠️ Adjust / 🔴 Review needed

- ✅ **On track** — compass is current, no changes needed. Run `/run-marketing-team`.
- ⚠️ **Adjust** — [specific field to update, why, suggested new language]
- 🔴 **Review needed** — [what drifted, what needs to be rethought before the next run]
```

### Founder Action
- ✅ On track → Read in 2 minutes, run `/run-marketing-team`
- ⚠️ Adjust → Update one field in `strategy-compass.md` (~10 min), then run
- 🔴 Review needed → Revisit compass before running (~30 min)

---

## Full Updated Pipeline

```
4AM daily:    Trend Scout (strategy-filtered + Yoobin-angled)
              → Idea Generator (reads meetings/ + trend brief)
              → 10 new ideas in Notion

8AM Monday:   Weekly Review
              → briefings/weekly-review-YYYY-MM-DD.md
              → compass update flag for founder

On demand:    /run-marketing-team
              Step 0: Strategist reads compass + voice + meetings/
              Step 1: 3 parallel copywriters (compass-briefed)
              Step 2: Creative Director (11 compliance checks)
              Step 3: Calendar Manager → Notion

On demand:    /analyze-performance → feeds top performers to trend brief
On demand:    /repurpose → adapts winning posts to 2 new formats
```

---

## Files Changed

### Create (new)
| File | Purpose |
|------|---------|
| `docs/marketing/strategy-compass.md` | Strategic north star — founder writes, all agents read |
| `docs/marketing/yoobin-voice.md` | Voice authenticity anchor — founder writes, Yoobin-facing agents read |
| `meetings/.gitkeep` | Creates the meetings/ folder in git |
| `meetings/README.md` | Note format guide for the folder |
| `~/.claude/plugins/bloggo-marketing/skills/weekly-review/SKILL.md` | New `/weekly-review` skill — the agent that runs at 8AM Monday |
| `briefings/weekly-review-YYYY-MM-DD.md` | Generated each Monday by the review cron (output, not tracked) |

### Modify (existing)
| File | Change |
|------|--------|
| `~/.claude/plugins/bloggo-marketing/skills/trend-scout/SKILL.md` | Add Step 6: strategy filter + Yoobin angle column |
| `~/.claude/plugins/bloggo-marketing/skills/content-strategist/SKILL.md` | Add Step 0: read compass + voice + meetings/ + strategic purpose field |
| `~/.claude/plugins/bloggo-marketing/skills/creative-director/SKILL.md` | Add checks 10 and 11 to brand compliance checklist |
| `~/.claude/plugins/bloggo-marketing/skills/run-marketing-team/SKILL.md` | Add compass + voice doc to pre-flight check |
| `Workflows/overnight-idea-generator.md` | Add Step 0: scan meetings/ before running searches |

### New Cron
| Schedule | What runs |
|----------|-----------|
| `0 8 * * 1` (8AM Monday) | Weekly Review agent — reads performance, audits drift, writes review brief, flags compass update if needed |

---

## What the Founder Does

| Task | Time | When |
|------|------|------|
| Write `strategy-compass.md` (initial) | ~30 min | Once, before first run |
| Write `yoobin-voice.md` (initial) | ~30 min | Once, before first run |
| Drop meeting notes in `meetings/` | ~5 min | After each call |
| Read weekly review brief | 2–5 min | Monday morning |
| Update compass if flagged ⚠️/🔴 | 10–30 min | As needed |

Total ongoing time: **~10 min/week** (if compass stays on track)

---

## Success Signals (3 months)

- Saves-to-views ratio trending up (resonance > reach working)
- Inbound DMs from people who sound like the right audience
- Yoobin pieces consistently passing the "only I can say this" test
- Weekly review is mostly ✅ On track, not ⚠️/🔴
- Meeting insights show up in content within 7 days of the call
