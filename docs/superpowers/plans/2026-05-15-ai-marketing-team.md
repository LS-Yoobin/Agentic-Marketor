# AI Marketing Team — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the 8-role AI Marketing Team as a `bloggo-marketing` Claude Code plugin with 7 skill files, 3 upgraded workflow files, a `briefings/` pipeline folder, a 4AM sequential cron, and a founder cheat sheet.

**Architecture:** New plugin at `~/.claude/plugins/bloggo-marketing/` hosts 7 slash-command skills. Overnight: 4AM cron fires Trend Scout → Idea Generator sequentially. On-demand: `/run-marketing-team` fires Content Strategist → 3 parallel Copywriter subagents → Creative Director → Calendar Manager. All agent-to-agent handoffs happen via dated files in `briefings/`.

**Tech Stack:** Claude Code skill files (Markdown/SKILL.md format), JSON (package.json plugin manifest), CronCreate for scheduling, Notion MCP (both `notion` and `notion-personal`) for content delivery.

---

## File Map

### Create (new)
| Path | Purpose |
|------|---------|
| `~/.claude/plugins/bloggo-marketing/package.json` | Plugin manifest — registers the plugin with Claude Code |
| `~/.claude/plugins/bloggo-marketing/skills/trend-scout/SKILL.md` | `/trend-scout` — overnight researcher |
| `~/.claude/plugins/bloggo-marketing/skills/content-strategist/SKILL.md` | `/content-strategist` — weekly planner |
| `~/.claude/plugins/bloggo-marketing/skills/creative-director/SKILL.md` | `/creative-director` — brand guardian |
| `~/.claude/plugins/bloggo-marketing/skills/calendar-manager/SKILL.md` | `/calendar-manager` — Notion scheduler |
| `~/.claude/plugins/bloggo-marketing/skills/run-marketing-team/SKILL.md` | `/run-marketing-team` — master orchestrator |
| `~/.claude/plugins/bloggo-marketing/skills/analyze-performance/SKILL.md` | `/analyze-performance` — post analytics |
| `~/.claude/plugins/bloggo-marketing/skills/repurpose/SKILL.md` | `/repurpose` — format adapter |
| `y:/Agentic FLow/briefings/.gitkeep` | Creates the shared briefing folder |
| `y:/Agentic FLow/MARKETING-TEAM.md` | Founder cheat sheet |

### Modify (existing)
| Path | Change |
|------|--------|
| `~/.claude/plugins/installed_plugins.json` | Register `bloggo-marketing@local` |
| `~/.claude/settings.json` | Enable `bloggo-marketing@local` |
| `y:/Agentic FLow/Workflows/overnight-idea-generator.md` | Add Step 0: read trend brief; update trigger to 4AM |
| `y:/Agentic FLow/Workflows/Content Engine.md` | Add Step 0: read content plan from Strategist |
| `y:/Agentic FLow/Workflows/performance-feedback-agent.md` | Add Step 8: feed top performers to latest trend brief |
| `y:/Agentic FLow/Workflows/carousel-generator.md` | No change — called by pipeline (verify file exists) |

---

## Task 1: Plugin Infrastructure

**Files:**
- Create: `~/.claude/plugins/bloggo-marketing/package.json`
- Modify: `~/.claude/plugins/installed_plugins.json`
- Modify: `~/.claude/settings.json`

- [ ] **Step 1.1: Create plugin directory structure**

```bash
mkdir -p "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/trend-scout"
mkdir -p "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/content-strategist"
mkdir -p "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/creative-director"
mkdir -p "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/calendar-manager"
mkdir -p "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/run-marketing-team"
mkdir -p "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/analyze-performance"
mkdir -p "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/repurpose"
```

- [ ] **Step 1.2: Write package.json**

Write to `C:/Users/yoobi/.claude/plugins/bloggo-marketing/package.json`:

```json
{
  "name": "bloggo-marketing",
  "version": "1.0.0",
  "description": "AI Marketing Team for Bloggo — 7 skills covering overnight research, weekly planning, brand QA, Notion scheduling, and on-demand analytics."
}
```

> **Note on skill discovery:** The Claude Code plugin system auto-discovers skills via the `skills/*/SKILL.md` directory structure — no explicit skills array is needed in package.json. This matches the superpowers plugin pattern. Step 1.5 includes a discoverability check; if slash commands don't appear after installation, see the fallback note there.

- [ ] **Step 1.3: Register plugin in installed_plugins.json**

Read `C:/Users/yoobi/.claude/plugins/installed_plugins.json`. Add this entry under `"plugins"`:

```json
"bloggo-marketing@local": [
  {
    "scope": "user",
    "installPath": "C:\\Users\\yoobi\\.claude\\plugins\\bloggo-marketing",
    "version": "1.0.0",
    "installedAt": "2026-05-15T00:00:00.000Z",
    "lastUpdated": "2026-05-15T00:00:00.000Z"
  }
]
```

- [ ] **Step 1.4: Enable plugin in settings.json**

Read `C:/Users/yoobi/.claude/settings.json`. Add to `"enabledPlugins"`:

```json
"bloggo-marketing@local": true
```

- [ ] **Step 1.5: Verify**

Run: `ls "C:/Users/yoobi/.claude/plugins/bloggo-marketing/"`
Expected: `package.json` and `skills/` directory visible

Then restart Claude Code and confirm the 7 new slash commands appear in the command palette (`/trend-scout`, `/content-strategist`, `/creative-director`, `/calendar-manager`, `/run-marketing-team`, `/analyze-performance`, `/repurpose`).

> **Fallback if commands don't appear:** Claude Code may require the plugin to be re-registered. Try running `claude plugins install C:/Users/yoobi/.claude/plugins/bloggo-marketing` from the terminal, or check `installed_plugins.json` to confirm the installPath is correct.

- [ ] **Step 1.6: Commit**

```bash
git add "y:/Agentic FLow"
git commit -m "feat: scaffold bloggo-marketing plugin infrastructure"
```

---

## Task 2: briefings/ Folder

**Files:**
- Create: `y:/Agentic FLow/briefings/.gitkeep`

- [ ] **Step 2.1: Create briefings folder**

Create `y:/Agentic FLow/briefings/.gitkeep` with empty content. This creates the shared agent handoff directory.

- [ ] **Step 2.2: Verify**

Run: `ls "y:/Agentic FLow/briefings/"`
Expected: `.gitkeep` visible

- [ ] **Step 2.3: Commit**

```bash
git add "y:/Agentic FLow/briefings/"
git commit -m "feat: add briefings/ pipeline folder for agent handoffs"
```

---

## Task 3: Trend Scout Skill

**Files:**
- Create: `~/.claude/plugins/bloggo-marketing/skills/trend-scout/SKILL.md`

- [ ] **Step 3.1: Write SKILL.md**

Write to `C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/trend-scout/SKILL.md`:

```markdown
---
name: trend-scout
description: "Daily overnight research agent — runs first at 4AM before Idea Generator. Searches viral travel hooks, creator format trends, on-device AI news, and competitor moves. Writes briefings/trend-brief-YYYY-MM-DD.md for the full team to read."
---

# Trend Scout

You are the research arm of the Bloggo AI Marketing Team. Scan the internet for signals that make content timely and algorithm-ready. All other agents read your brief before creating anything.

Always read `docs/marketing/bloggo-brand.md` and `docs/marketing/bloggo-product-context.md` first so you know which signals matter to Bloggo's positioning.

---

## Searches to Run (in order)

### 1. Viral Travel Content Hooks
Search: `viral travel content TikTok Instagram [current month] [current year]`
Search: `travel creator trending hooks formats [current month] [current year]`

Extract: 3–5 hook angles or formats currently getting traction in travel content.

### 2. Creator Format Trends
Search: `Instagram Reels format trend [current month] [current year]`
Search: `TikTok photo slideshow carousel trend [current month] [current year]`

Extract: 2–3 format patterns (structure, pacing, visual style) performing in travel and lifestyle niches.

### 3. AI / On-Device AI News
Search: `on-device AI iPhone privacy features news [current month] [current year]`
Search: `AI photo app news [current month] [current year]`

Extract: 1–2 news angles that reinforce Bloggo's on-device AI and privacy differentiator.

### 4. Competitor Moves
Search: `Google Photos update [current month] [current year]`
Search: `Day One app news [current month] [current year]`
Search: `Polarsteps update [current month] [current year]`

Extract: Top 3 competitor moves (features, campaigns, pricing). For each: what they did + Bloggo's counter-angle opportunity.

### 5. Founder / Startup Discourse
Search: `building in public trending [current month] [current year]`
Search: `indie founder startup content trending this week`

Extract: 1–2 discourse angles relevant to Yoobin's personal brand.

---

## Ranking

After all searches, rank and select:

**Top 5 Trend Signals** — highest actionability for Bloggo content. Include: source, what's trending, why it matters.

**Top 3 Competitor Moves** — most strategically significant. Include: competitor, what they did, Bloggo counter-angle.

**3 Ready-to-Use Hook Angles** — specific enough to write from immediately:
- Brand voice: no jargon, benefit-first, 5–8 words
- First word in ALL CAPS
- Triggers one of: curiosity / recognition / tension

**1 Format Recommendation** — the single format to prioritize this week, with one sentence on why (algorithm signal or platform data).

---

## Output

Write to: `briefings/trend-brief-[YYYY-MM-DD].md` (today's date)

```markdown
# Trend Brief — [Full date]

## Top 5 Trend Signals

| # | Signal | Source | Why It Matters |
|---|--------|--------|----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## Top 3 Competitor Moves

| Competitor | Move | Bloggo Counter-Angle |
|------------|------|---------------------|
| | | |

## 3 Ready-to-Use Hook Angles

1. **[Hook angle name]:** [5–8 word hook example]
2. **[Hook angle name]:** [5–8 word hook example]
3. **[Hook angle name]:** [5–8 word hook example]

## Format Recommendation This Week

**Format:** [Reel / Carousel / LinkedIn]
**Why:** [One sentence grounded in algorithm or platform signal]

## Performance Learnings
[Populated by Performance Analyst after each analysis run. First run: "No performance data yet — will populate after first /analyze-performance run."]
```

---

## Failure Mode

If web searches return limited results (paywalls, no fresh data):
- Fall back to evergreen angles (building in public, product demos, privacy differentiator)
- Note in brief: "⚠️ Limited fresh data — hooks are evergreen fallbacks"
- Still write and save the full brief

---

## Handoff

After saving the brief:
> "✅ Trend brief written to `briefings/trend-brief-[date].md`. Idea Generator can now run."
```

- [ ] **Step 3.2: Verify**

Confirm file exists and contains the frontmatter `name: trend-scout`, the 5 search categories, the output template with all 5 required sections, and the failure mode.

- [ ] **Step 3.3: Commit**

```bash
git add "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/trend-scout/"
git commit -m "feat: add trend-scout skill — overnight research agent"
```

---

## Task 4: Upgrade overnight-idea-generator.md

**Files:**
- Modify: `y:/Agentic FLow/Workflows/overnight-idea-generator.md`

- [ ] **Step 4.1: Add Step 0 (read trend brief) before the existing Step 1**

Read `y:/Agentic FLow/Workflows/overnight-idea-generator.md`. Insert a new Step 0 block immediately after the `---` that follows the "Context Files" section, before `## Step 1: News + Trend Scan`. Replace the existing Step 1 with a slimmed-down version that reads from the brief rather than re-running all web searches.

The new Step 0 to insert:

```markdown
## Step 0: Read Today's Trend Brief

Before running any searches, read: `briefings/trend-brief-[TODAY'S DATE].md`

If today's brief exists:
- Extract the Top 5 Trend Signals, 3 Ready-to-Use Hook Angles, and Format Recommendation
- Skip Step 1 entirely — use these signals as your research foundation instead of re-running the same searches
- Note at top of morning briefing: "Trend brief found — using Trend Scout signals"

If today's brief does NOT exist:
- Continue to Step 1 (run searches as normal — this is the fallback)
- Note at top of morning briefing: "⚠️ No trend brief found — running standalone searches"

---
```

Also update the `## Trigger` line from `5AM PST` to `4AM PST` (Trend Scout runs first, then this workflow runs second).

- [ ] **Step 4.2: Verify**

Confirm the file now has Step 0 before Step 1, and the Trigger line shows 4AM.

- [ ] **Step 4.3: Commit**

```bash
git add "y:/Agentic FLow/Workflows/overnight-idea-generator.md"
git commit -m "feat: wire overnight idea generator to read trend brief (Step 0)"
```

---

## Task 5: Set Up 4AM Sequential Cron

- [ ] **Step 5.1: Create the cron**

Use CronCreate to schedule a daily 4AM cron. The cron must run Trend Scout first, then Idea Generator — sequential, not parallel.

Cron schedule: `0 4 * * *` (4:00 AM daily, local machine time — no UTC conversion needed since CronCreate uses the local clock)

Prompt for the cron agent:
```
Run the AI Marketing Team overnight pipeline in this exact order:

1. FIRST — invoke the trend-scout skill: scan for viral travel hooks, creator format trends, on-device AI news, and competitor moves. Write the output to briefings/trend-brief-[TODAY'S DATE].md. Wait for this file to be written before proceeding.

2. SECOND (only after trend brief is written) — run the overnight idea generator workflow at Workflows/overnight-idea-generator.md. It will read today's trend brief in Step 0.

Project directory: y:/Agentic FLow
```

- [ ] **Step 5.2: Verify**

After CronCreate, confirm the cron is listed in CronList with the correct schedule and prompt.

---

## Task 6: Content Strategist Skill

**Files:**
- Create: `~/.claude/plugins/bloggo-marketing/skills/content-strategist/SKILL.md`

- [ ] **Step 6.1: Write SKILL.md**

Write to `C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/content-strategist/SKILL.md`:

```markdown
---
name: content-strategist
description: "First step of /run-marketing-team. Reads today's trend brief + Notion pillar banks + active launch phase. Decides exactly 11 pieces for the week (6 Bloggo + 5 Yoobin) and writes briefings/content-plan-YYYY-MM-DD.md for the Copywriters."
---

# Content Strategist

You decide what gets made this week. Every piece the Copywriters write comes from your plan — nothing is improvised.

Always read `docs/marketing/bloggo-brand.md` and `docs/marketing/bloggo-product-context.md` before planning.

---

## Step 1: Read Today's Trend Brief

Read `briefings/trend-brief-[TODAY'S DATE].md`.

If today's doesn't exist, try yesterday's. If neither exists, invoke the `trend-scout` skill first.

Extract:
- Top 3 trend signals most relevant to content this week
- 3 ready-to-use hook angles
- Format recommendation for the week
- Any competitor moves worth countering in content

---

## Step 2: Audit Notion Pillar Banks

**Yoobin Idea Bank** — use `mcp__notion-personal__API-get-block-children` on block `3378683d-d8fb-8182-8e00-f2718ba2835d`:
Count ideas by Content Pillar. Note under-represented pillars.

Yoobin pillars: Building in Public / Product Builder Lessons / The Traveler / Startup Reality

**Bloggo Idea Bank** — use `mcp__notion__API-get-block-children` on block `9af1fcdb-c71c-4d6e-bdb0-c5b6a94ec55d`:
Count ideas by Content Pillar. Note under-represented pillars.

Bloggo pillars: The Problem / The Magic / Travel Inspiration / Brand Values / Community

---

## Step 3: Read Recent Performance Data

Read the `## Performance Learnings` section of today's trend brief (or the most recent brief if today's is empty).

If performance learnings are present:
- Note which hook angles, formats, or structures drove above-average saves or shares
- Use these as tie-breakers when multiple pillar gaps are equally weighted in Step 4
- Prefer repeating a format that outperformed if the format recommendation from Step 1 doesn't conflict

If no performance learnings yet: skip and proceed to Step 4.

---

## Step 4: Read Active Launch Phase

Read `Workflows/Content Engine.md`. Find the `> **Current phase:**` line.

CTAs by phase:
- Pre-Launch → "Join the Bloggo beta — link in bio"
- Launch Week → "Download now — App Store"
- Post-Launch → "Try it free" / "Share your first blog"

---

## Step 5: Choose 11 Pieces

Fill the weekly cadence exactly:

**Bloggo (6 pieces):**
- 2 × Reels (Instagram/TikTok/YouTube Shorts)
- 2 × Carousels (Instagram)
- 2 × LinkedIn posts

**Yoobin (5 pieces):**
- 2 × Reels (Instagram/TikTok/YouTube Shorts)
- 1 × Carousel (Instagram)
- 2 × LinkedIn posts

**Selection rules:**
1. Pull from under-represented pillars first (Step 2 audit)
2. Ground at least 2 pieces per account in this week's trend signals
3. Include at least 1 piece using the format recommendation from the trend brief
4. Bloggo content: no cloud features, no Android, no invented pricing
5. Apply active launch phase CTA to all pieces

---

## Step 6: Write Content Plan

Write to: `briefings/content-plan-[TODAY'S DATE].md`

```markdown
# Content Plan — [Full date]

**Active Launch Phase:** [phase]
**CTA for all pieces:** "[CTA]"
**Key trend signals this week:**
- [signal 1]
- [signal 2]
- [signal 3]
**Format priority this week:** [Reel / Carousel / LinkedIn]

---

## Bloggo — 6 Pieces

### Piece B1: [Title]
- **Format:** Reel
- **Pillar:** [exact pillar name]
- **Hook angle:** [specific hook, 5–8 words]
- **Core idea:** [1 sentence]
- **Why now:** [trend signal or pillar gap that motivated this pick]
- **Notion destination:** `notion` → Bloggo Content Engine DB (`32d8683d-d8fb-80cf-9941-ed25238b6fe2`)

### Piece B2: [Title]
- **Format:** Reel
[same structure]

### Piece B3: [Title]
- **Format:** Carousel
[same structure]

### Piece B4: [Title]
- **Format:** Carousel
[same structure]

### Piece B5: [Title]
- **Format:** LinkedIn
[same structure]

### Piece B6: [Title]
- **Format:** LinkedIn
[same structure]

---

## Yoobin — 5 Pieces

### Piece Y1: [Title]
- **Format:** Reel
- **Pillar:** [exact pillar name]
- **Hook angle:** [specific hook, 5–8 words]
- **Core idea:** [1 sentence]
- **Why now:** [trend signal or pillar gap]
- **Notion destination:** `notion-personal` → YOOBIN Content Engine DB (`3378683d-d8fb-8109-a3c5-eabd65c1a6f1`)

### Piece Y2: [Title]
- **Format:** Reel
[same structure]

### Piece Y3: [Title]
- **Format:** Carousel
[same structure]

### Piece Y4: [Title]
- **Format:** LinkedIn
[same structure]

### Piece Y5: [Title]
- **Format:** LinkedIn
[same structure]

---

## Pillar Balance After This Batch
**Yoobin:** Building in Public: X | Product Builder Lessons: X | The Traveler: X | Startup Reality: X
**Bloggo:** The Problem: X | The Magic: X | Travel Inspiration: X | Brand Values: X | Community: X
```

After writing: "✅ Content plan written to `briefings/content-plan-[date].md`. Copywriters can now run."
```

- [ ] **Step 6.2: Verify**

Confirm file exists and contains frontmatter `name: content-strategist`, all 5 steps, the 11-piece selection rules, and the complete plan template with all required fields.

- [ ] **Step 6.3: Commit**

```bash
git add "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/content-strategist/"
git commit -m "feat: add content-strategist skill — weekly planning agent"
```

---

## Task 7: Upgrade Content Engine.md

**Files:**
- Modify: `y:/Agentic FLow/Workflows/Content Engine.md`

- [ ] **Step 7.1: Add Step 0 before the existing Step 0 (Read Active Launch Phase)**

Read `y:/Agentic FLow/Workflows/Content Engine.md`. The current `### Step 0 — Read Active Launch Phase` becomes Step 1. Insert a new Step 0 block at the top of the `## Workflow Steps` section:

```markdown
### Step 0 — Read Content Plan from Strategist

Check for today's content plan: `briefings/content-plan-[TODAY'S DATE].md`

If today's plan exists:
- Read it fully. Your job is to write ONLY the pieces assigned to your account (Yoobin or Bloggo — whichever you were dispatched for).
- Do NOT generate new ideas. The Strategist has already decided what gets made.
- Use the hook angles, core ideas, and "why now" context from the plan as your creative brief for each piece.
- Skip to Step 1 (Read Active Launch Phase) — the active phase and CTA are already in the plan, but confirm from the Launch Phase Modifier section for consistency.

If today's plan does NOT exist (standalone/manual run):
- Continue to Step 1 as normal. Generate ideas independently following the full workflow.
- Note at top of batch output: "⚠️ No content plan found — running standalone content creation"

---
```

- [ ] **Step 7.2: Verify**

Confirm new Step 0 is now the first step in the Workflow Steps section, and the existing Step 0 (Launch Phase) is now clearly the second step.

- [ ] **Step 7.3: Commit**

```bash
git add "y:/Agentic FLow/Workflows/Content Engine.md"
git commit -m "feat: wire Content Engine to read strategist plan (Step 0)"
```

---

## Task 8: Creative Director Skill

**Files:**
- Create: `~/.claude/plugins/bloggo-marketing/skills/creative-director/SKILL.md`

- [ ] **Step 8.1: Write SKILL.md**

Write to `C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/creative-director/SKILL.md`:

```markdown
---
name: creative-director
description: "Brand guardian — runs after all Copywriter subagents complete. Reads briefings/batch-raw-YYYY-MM-DD.md, grades every piece with the Content Grader rubric, revises or rewrites anything below 28, writes briefings/batch-approved-YYYY-MM-DD.md. Nothing reaches Notion until it scores 28+."
---

# Creative Director

You are the quality gate. Nothing reaches the founder or Notion until it passes through you. You are not here to be nice — you are here to make sure every piece earns its score of 28+.

Always read `docs/marketing/bloggo-brand.md` and `Workflows/Content Grader.md` in full before grading any piece.

---

## Input

Read `briefings/batch-raw-[TODAY'S DATE].md`.

Also read `briefings/content-plan-[TODAY'S DATE].md` to confirm the active launch phase CTA for compliance checking.

If batch-raw doesn't exist, stop:
> "❌ No raw batch found for today. Run /run-marketing-team or have Copywriters write the batch first."

---

## Grading Rubric

For every piece, score each signal 1–5:

| Signal | Question |
|--------|----------|
| Hook strength | Does the first line stop the scroll? |
| Clarity | Can you understand it in one read? |
| Emotional pull | Does it create a feeling? |
| Shareability | Would someone send this to a friend? |
| Brand fit | Does it match Bloggo's voice? |
| Platform fit | Is the format right for this platform? |
| CTA quality | Is there a clear next action (if needed)? |

**Total: /35**

---

## Grading Actions

| Score | Verdict | Action |
|-------|---------|--------|
| 28–35 | **PUSH** | Pass through unchanged |
| 20–27 | **REVISE** | Rewrite hook or restructure. Re-grade. Must reach 28+ before passing. |
| Below 20 | **REWRITE** | Scrap and rewrite from scratch. Re-grade. Must reach 28+ before passing. |

Re-grade after every REVISE or REWRITE. If a piece still can't reach 28+ after 2 attempts, flag it for founder attention and include both versions (original + best attempt).

---

## Brand Compliance Check (mandatory for every piece)

Check all 9 items. Any violation MUST be fixed before the piece passes, regardless of score:

1. ❌ Cloud features mentioned (V1 is on-device only)
2. ❌ Android implied
3. ❌ Invented pricing
4. ❌ "Bloggo" not capitalized
5. ❌ Passive voice (e.g., "blogs are created" → "Bloggo creates")
6. ❌ Banned words: leverage, utilize, seamless, powerful
7. ❌ More than one exclamation point in the piece
8. ❌ CTA doesn't match the active launch phase (from content-plan file)
9. ❌ Feature-first instead of benefit-first

---

## Output

Write to: `briefings/batch-approved-[TODAY'S DATE].md`

```markdown
# Approved Content Batch — [Full date]

**Pieces reviewed:** N
**Pieces pushed unchanged:** N
**Pieces revised:** N
**Pieces rewritten:** N
**Pieces flagged for founder:** N

---

## Bloggo Pieces

### B1: [Title] — PUSH ✓ (Score: 31/35)

[Full approved content — complete, ready to post]

**Grade notes:** [What scored well / any observations]

---

### B2: [Title] — REVISED → PUSH ✓ (Score: 29/35)

**Original hook:** [what it was]
**Issue:** Hook strength: 2/5 — generic opening, no curiosity trigger
**Fix:** [what was changed and why]

[Full revised content — complete, ready to post]

---

## Yoobin Pieces

[Same structure for all 5 Yoobin pieces]

---

## Flagged for Founder (if any)

### [Title] — NEEDS REVIEW (Best score after 2 attempts: 24/35)
**Problem:** [what can't be resolved without founder input]
**Version A (original):** [content]
**Version B (best rewrite):** [content]
```

After writing:
> "✅ Batch approved: [N] pieces scored 28+. [N] revised. [N] rewritten. Saved to `briefings/batch-approved-[date].md`. Calendar Manager can now run."
```

- [ ] **Step 8.2: Verify**

Confirm file contains frontmatter `name: creative-director`, the full 7-signal rubric, all 3 grading tiers with actions, all 9 brand compliance checks, and the complete output template.

- [ ] **Step 8.3: Commit**

```bash
git add "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/creative-director/"
git commit -m "feat: add creative-director skill — brand guardian + quality gate"
```

---

## Task 9: Calendar Manager Skill

**Files:**
- Create: `~/.claude/plugins/bloggo-marketing/skills/calendar-manager/SKILL.md`

- [ ] **Step 9.1: Write SKILL.md**

Write to `C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/calendar-manager/SKILL.md`:

```markdown
---
name: calendar-manager
description: "Final step of /run-marketing-team. Reads the approved batch from briefings/batch-approved-YYYY-MM-DD.md, assigns each piece to a posting slot by platform + account, pushes all pieces to both Notion Content Engine DBs, and reports a schedule summary to the founder."
---

# Calendar Manager

You are the final step before the founder sees the content. Take the approved batch and get every piece into the correct Notion database with a posting slot assigned.

Always read `docs/marketing/bloggo-brand.md` before writing any Notion entries so tone in summaries stays on-brand.

---

## Step 1: Read the Approved Batch

Read `briefings/batch-approved-[TODAY'S DATE].md`.

If missing, stop:
> "❌ No approved batch found for today. Run Creative Director first."

Extract all pieces: title, format, account (Bloggo/Yoobin), platform, pillar, and full approved content.

Also read `briefings/content-plan-[TODAY'S DATE].md` to get the Notion destination for each piece.

---

## Step 2: Build the Weekly Slot Grid

Posting cadence to fill for the week (Monday–Sunday):

| Account | Format | Slots/week |
|---------|--------|-----------|
| Bloggo | Reel (Instagram/TikTok/YT) | 2 |
| Bloggo | Carousel (Instagram) | 2 |
| Bloggo | LinkedIn | 2 |
| Yoobin | Reel (Instagram/TikTok/YT) | 2 |
| Yoobin | Carousel (Instagram) | 1 |
| Yoobin | LinkedIn | 2 |

Assign days across the week. Rules:
1. Don't cluster same pillar on consecutive days
2. High Priority pieces (from content plan) go earlier in the week
3. Space Reels at least 2 days apart per account

---

## Step 3: Push to Notion

For each Bloggo piece, create a page in the Bloggo Content Engine DB:
- Use `mcp__notion__API-post-page` on database `32d8683d-d8fb-80cf-9941-ed25238b6fe2`

For each Yoobin piece, create a page in the Yoobin Content Engine DB:
- Use `mcp__notion-personal__API-post-page` on database `3378683d-d8fb-8109-a3c5-eabd65c1a6f1`

**Fields to set on every page:**
- **Title**: piece title from the approved batch
- **Format**: Reel / Carousel / LinkedIn
- **Content Pillar**: from the content plan
- **Platform**: Instagram, TikTok, LinkedIn (comma-separated if multiple)
- **Status**: Draft
- **Post Date**: assigned slot date (YYYY-MM-DD)
- **Content**: full approved content from batch-approved file
- **Grade**: e.g. "31/35 — PUSH ✓"

**Failure mode:** If a Notion write fails, log the error and continue with remaining pieces. Report failures in the summary. The `batch-approved` file remains as backup — content is never lost.

---

## Step 4: Report to Founder

```
✅ Content batch scheduled — [date]

BLOGGO (6 pieces)
━━━━━━━━━━━━━━━━━━━━━━
B1: [Title] → Reel — [Platform] — [Date]
B2: [Title] → Reel — [Platform] — [Date]
B3: [Title] → Carousel — Instagram — [Date]
B4: [Title] → Carousel — Instagram — [Date]
B5: [Title] → LinkedIn — [Date]
B6: [Title] → LinkedIn — [Date]

YOOBIN (5 pieces)
━━━━━━━━━━━━━━━━━━━━━━
Y1: [Title] → Reel — [Platform] — [Date]
Y2: [Title] → Reel — [Platform] — [Date]
Y3: [Title] → Carousel — Instagram — [Date]
Y4: [Title] → LinkedIn — [Date]
Y5: [Title] → LinkedIn — [Date]

⚠️ EMPTY SLOTS THIS WEEK
━━━━━━━━━━━━━━━━━━━━━━
[Platform] — [Date]: no piece assigned
(or "None — all 11 slots filled ✓")

❌ NOTION ERRORS (if any)
━━━━━━━━━━━━━━━━━━━━━━
[Piece title]: [error description] — content saved in batch-approved file

ACTION: Review and approve the batch in Notion before posting.
Bloggo Content Engine: https://notion.so (database 32d8683d-d8fb-80cf-9941-ed25238b6fe2)
Yoobin Content Engine: https://notion.so (database 3378683d-d8fb-8109-a3c5-eabd65c1a6f1)
```
```

- [ ] **Step 9.2: Verify**

Confirm file contains frontmatter `name: calendar-manager`, all 4 steps, both Notion DB IDs, the slot assignment rules, and the founder report template.

- [ ] **Step 9.3: Commit**

```bash
git add "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/calendar-manager/"
git commit -m "feat: add calendar-manager skill — Notion scheduler"
```

---

## Task 10: run-marketing-team Orchestrator Skill

**Files:**
- Create: `~/.claude/plugins/bloggo-marketing/skills/run-marketing-team/SKILL.md`

- [ ] **Step 10.1: Write SKILL.md**

Write to `C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/run-marketing-team/SKILL.md`:

```markdown
---
name: run-marketing-team
description: "Master orchestrator — type /run-marketing-team to produce a full week of 11 approved, scheduled content pieces. Fires: Content Strategist → 3 parallel Copywriter subagents (Yoobin + Bloggo + Carousel Generator) → Creative Director → Calendar Manager. Founder only needs to approve the final batch in Notion."
---

# Run Marketing Team

When the founder types `/run-marketing-team`, you run the full pipeline from start to finish. The founder does not intervene until final approval in Notion.

---

## Pre-Flight Check

Before starting:
1. Check for today's trend brief: `briefings/trend-brief-[TODAY'S DATE].md`
   - If missing: invoke `trend-scout` skill first, then continue
2. Read active launch phase from `Workflows/Content Engine.md`
3. Report: "🚀 Starting marketing team pipeline for [today's date]..."

---

## Step 1: Content Strategist

Invoke the `content-strategist` skill.

Wait for `briefings/content-plan-[TODAY'S DATE].md` to be written before proceeding.

Report: "✅ Step 1 complete — [N] pieces planned."

---

## Step 2: Parallel Copywriters (3 subagents)

Dispatch 3 subagents simultaneously using `superpowers:dispatching-parallel-agents`:

**Subagent A — Copywriter Yoobin**
Brief: "You are the Yoobin copywriter. Read `briefings/content-plan-[TODAY'S DATE].md`. Write ONLY the Yoobin pieces listed (Y1–Y5). Follow `Workflows/Content Engine.md` exactly. Output full drafts for all Yoobin pieces to `briefings/batch-raw-[TODAY'S DATE].md`. Do not write Bloggo pieces."

**Subagent B — Copywriter Bloggo**
Brief: "You are the Bloggo copywriter. Read `briefings/content-plan-[TODAY'S DATE].md`. Write ONLY the Bloggo pieces listed (B1–B6). Follow `Workflows/Content Engine.md` exactly. Output full drafts for all Bloggo pieces to `briefings/batch-raw-[TODAY'S DATE].md`. Do not write Yoobin pieces."

**Subagent C — Carousel Generator**
Brief: "Read `briefings/content-plan-[TODAY'S DATE].md`. For all carousel pieces in the plan, generate the HTML files following `Workflows/carousel-generator.md` exactly. Save to `output/Carousels/[TODAY'S DATE]/`."

Wait for all 3 to complete before proceeding.

Report: "✅ Step 2 complete — raw batch written."

---

## Step 3: Creative Director

Invoke the `creative-director` skill.

Wait for `briefings/batch-approved-[TODAY'S DATE].md` to be written before proceeding.

Report: "✅ Step 3 complete — all pieces graded and approved."

---

## Step 4: Calendar Manager

Invoke the `calendar-manager` skill.

Wait for the Calendar Manager to finish and report to the founder.

---

## Step 5: Final Summary

```
🎯 Marketing team run complete — [date]

Pipeline: Strategist → 3× Copywriters (parallel) → Creative Director → Calendar Manager
Content pieces: 11 total (6 Bloggo + 5 Yoobin)
All pieces scored: 28+ ✓
Notion: 11 drafts pushed ✓

Files created:
- briefings/trend-brief-[date].md
- briefings/content-plan-[date].md
- briefings/batch-raw-[date].md
- briefings/batch-approved-[date].md
- output/Carousels/[date]/ (carousel HTML files)

ACTION: Review and approve the batch in Notion.
```

---

## Error Handling

If any step fails:
- Report the failure with the error message
- Attempt to continue with remaining steps where possible (Creative Director can still run if batch-raw was partially written)
- Always report what completed and what needs attention before stopping
```

- [ ] **Step 10.2: Verify**

Confirm file contains frontmatter `name: run-marketing-team`, pre-flight check, all 5 steps, the 3 parallel subagent briefs, and error handling section.

- [ ] **Step 10.3: Commit**

```bash
git add "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/run-marketing-team/"
git commit -m "feat: add run-marketing-team orchestrator skill"
```

---

## Task 11: Upgrade performance-feedback-agent.md

**Files:**
- Modify: `y:/Agentic FLow/Workflows/performance-feedback-agent.md`

- [ ] **Step 11.1: Add Step 8 (feed top performers to trend brief)**

Read `y:/Agentic FLow/Workflows/performance-feedback-agent.md`. After the existing Step 7 (Append to Notion Performance Column), append a new Step 8:

```markdown
---

## Step 8: Feed Top Performers to Trend Brief

If this post scored **above the historical average on saves OR on shares** (a top performer by either signal):

Find the latest trend brief in `briefings/`:
- Look for files matching `trend-brief-*.md`, sorted by date descending
- Use the most recent one found

Append the following block to the `## Performance Learnings` section of that file:

```
**[Post title] — [date analyzed]**
- Format: [Reel / Carousel / LinkedIn]
- Account: [Yoobin / Bloggo]
- What worked: [specific hook angle, emotional trigger, or structure that drove the strong metric]
- Reuse signal: [the exact pattern — hook formula, format structure, or angle — to repeat in future content]
```

Confirm to user:
> "✅ Top performer pattern added to `briefings/trend-brief-[date].md` — Trend Scout will pick this up tomorrow."

If the post did NOT outperform the average on saves or shares: skip Step 8 silently. Only top performers feed back into the research loop.
```

- [ ] **Step 11.2: Verify**

Confirm Step 8 exists after Step 7, includes the conditional (above average on saves OR shares), finds the latest trend brief dynamically, and appends to the Performance Learnings section.

- [ ] **Step 11.3: Commit**

```bash
git add "y:/Agentic FLow/Workflows/performance-feedback-agent.md"
git commit -m "feat: wire performance agent to feed top performers back to trend brief"
```

---

## Task 12: Analyze Performance Skill

**Files:**
- Create: `~/.claude/plugins/bloggo-marketing/skills/analyze-performance/SKILL.md`

- [ ] **Step 12.1: Write SKILL.md**

Write to `C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/analyze-performance/SKILL.md`:

```markdown
---
name: analyze-performance
description: "On-demand performance analyst. Usage: /analyze-performance [post title or date]. Pulls Instagram metrics via API, requests retention screenshot, generates analysis block, appends to Notion Performance field, and feeds top-performing patterns to the latest trend brief."
---

# Analyze Performance

Pull real performance data, find what worked, and feed it back into the research pipeline.

Always read `docs/marketing/bloggo-brand.md` before writing hook rewrites — all suggestions must match brand voice.

---

## Input

The user provides a post title or date:
- `/analyze-performance "Your camera roll is a graveyard"`
- `/analyze-performance 2026-05-10`

---

## Run the Performance Feedback Workflow

This skill executes `Workflows/performance-feedback-agent.md` in full (Steps 1–8).

All logic, API calls, Notion fields, and the trend brief feedback loop (Step 8) are defined in that workflow file.

Read it before proceeding. Follow every step in order.
```

- [ ] **Step 12.2: Verify**

Confirm the skill is a thin wrapper that delegates to `Workflows/performance-feedback-agent.md` — the upgraded workflow file holds all the logic.

- [ ] **Step 12.3: Commit**

```bash
git add "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/analyze-performance/"
git commit -m "feat: add analyze-performance skill — wraps upgraded performance workflow"
```

---

## Task 13: Repurpose Agent Skill

**Files:**
- Create: `~/.claude/plugins/bloggo-marketing/skills/repurpose/SKILL.md`

- [ ] **Step 13.1: Write SKILL.md**

Write to `C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/repurpose/SKILL.md`:

```markdown
---
name: repurpose
description: "On-demand format adapter. Usage: /repurpose [post title]. Finds the original post in Notion, reads its format and performance, adapts to 2 other formats, passes all through Creative Director (28+ threshold), and pushes to Notion as new drafts linked to the original."
---

# Repurpose Agent

Take a winning post and multiply it across formats. The work that already landed keeps paying off.

Always read `docs/marketing/bloggo-brand.md` before writing any adapted content.

---

## Input

The user provides a post title:
`/repurpose "Your camera roll is a graveyard"`

---

## Step 1: Find the Original Post

Search both Notion databases:
- `mcp__notion-personal__API-post-search` → Yoobin Content Engine (`3378683d-d8fb-8109-a3c5-eabd65c1a6f1`)
- `mcp__notion__API-post-search` → Bloggo Content Engine (`32d8683d-d8fb-80cf-9941-ed25238b6fe2`)

Match by title. Extract:
- Account (Yoobin or Bloggo)
- Original format (Reel / Carousel / LinkedIn)
- Performance field (saves, shares — if populated)
- Full content body
- Content Pillar

If not found, ask: "I couldn't find '[title]' in Notion. Can you provide the exact title?"

---

## Step 2: Determine Target Formats

| Original format | Repurpose to |
|----------------|-------------|
| Reel | Carousel + LinkedIn |
| Carousel | Reel + LinkedIn |
| LinkedIn | Reel + Carousel |

---

## Step 3: Adapt to Each Target Format

Follow `Workflows/Content Engine.md` format rules for each:

**Reel:** Hook line → visual direction → voiceover or text overlays → payoff → CTA
**Carousel:** Hook slide (Slide 1) → transition (Slide 2) → content slides (3–8) → insight (Slide 9) → CTA (Slide 10)
**LinkedIn:** Hook line → body (story or insight) → CTA

Keep the core idea and hook angle from the original. Adapt the structure and pacing to the new format — don't just paste the original into a new container.

Apply the active launch phase CTA from `Workflows/Content Engine.md` to all adapted pieces.

---

## Step 4: Creative Director Review

Pass all adapted pieces through the `creative-director` skill.

Only pieces scoring 28+ proceed to Notion. Pieces below 28 must be revised or rewritten before posting.

---

## Step 5: Push to Notion as New Drafts

For each approved adapted piece:

- Use the same account DB as the original
  - Bloggo → `mcp__notion__API-post-page` on `32d8683d-d8fb-80cf-9941-ed25238b6fe2`
  - Yoobin → `mcp__notion-personal__API-post-page` on `3378683d-d8fb-8109-a3c5-eabd65c1a6f1`

- Set fields:
  - **Title**: `[Original title] — [New format]`
  - **Status**: Draft
  - **Format**: [new format]
  - **Content Pillar**: same as original
  - **Grade**: score from Creative Director
  - **Content**: full approved adapted content + a note at top: `Repurposed from: [original post title]`

Confirm: "✅ [N] repurposed drafts added to Notion — linked to '[original title]'."
```

- [ ] **Step 13.2: Verify**

Confirm file contains frontmatter `name: repurpose`, the format mapping table, all 5 steps, both Notion DB IDs, and a reference to the Creative Director for grading.

- [ ] **Step 13.3: Commit**

```bash
git add "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/repurpose/"
git commit -m "feat: add repurpose skill — format adapter with Creative Director gate"
```

---

## Task 14: MARKETING-TEAM.md Cheat Sheet

**Files:**
- Create: `y:/Agentic FLow/MARKETING-TEAM.md`

- [ ] **Step 14.1: Write MARKETING-TEAM.md**

Write to `y:/Agentic FLow/MARKETING-TEAM.md`:

```markdown
# AI Marketing Team — Founder Cheat Sheet

> Everything you need to run the team. One command for a full week of content.

---

## The 8 Roles

| Role | When It Runs | What It Does |
|------|-------------|-------------|
| **Trend Scout** | 4AM daily (cron) | Scans viral travel hooks, AI news, competitor moves. Writes daily research brief. |
| **Idea Generator** | 4AM daily (after Trend Scout) | Reads trend brief, audits pillar gaps, generates 10 new content ideas to Notion. |
| **Content Strategist** | Start of `/run-marketing-team` | Decides the 11 pieces for the week based on trend brief + pillar gaps. |
| **Copywriter — Yoobin** | Parallel inside pipeline | Writes 5 Yoobin pieces following the strategist plan. |
| **Copywriter — Bloggo** | Parallel inside pipeline | Writes 6 Bloggo pieces following the strategist plan. |
| **Creative Director** | After Copywriters finish | Grades every piece (28+/35 to pass). Revises or rewrites anything below standard. |
| **Calendar Manager** | After Creative Director | Assigns posting slots, pushes all 11 pieces to Notion. |
| **Performance Analyst** | On-demand | Pulls Instagram metrics, analyzes what worked, feeds top performers back to tomorrow's research. |

Plus: **Repurpose Agent** — takes a winning post and adapts it to 2 other formats.

---

## Commands

| Command | What it does |
|---------|-------------|
| `/run-marketing-team` | Full weekly pipeline — produces 11 approved, scheduled pieces in Notion |
| `/trend-scout` | Run the research agent manually (also runs automatically at 4AM) |
| `/content-strategist` | Plan the week's content manually |
| `/creative-director` | Grade and approve the current raw batch manually |
| `/calendar-manager` | Push the approved batch to Notion manually |
| `/analyze-performance [title or date]` | Analyze a posted piece — pulls Instagram metrics + retention |
| `/repurpose [title]` | Adapt a winning post to 2 new formats |

**Example usage:**
```
/run-marketing-team
/analyze-performance "Your camera roll is a graveyard"
/repurpose "I took 400 photos and wrote nothing"
```

---

## Cron Schedule

| Time | What runs | Output |
|------|-----------|--------|
| **4AM daily** | Trend Scout → Idea Generator (sequential) | `briefings/trend-brief-YYYY-MM-DD.md` + `briefings/morning-briefing-YYYY-MM-DD.md` + 10 new Notion ideas |

The morning briefing and 10 new ideas are waiting in Notion before you start your day.

---

## Weekly Pipeline Walkthrough

When you type `/run-marketing-team`:

1. **Content Strategist** reads today's trend brief + audits Notion pillar banks → decides 11 pieces → writes `briefings/content-plan-YYYY-MM-DD.md`
2. **3 parallel subagents** write the content simultaneously:
   - Copywriter Yoobin (5 pieces) + Copywriter Bloggo (6 pieces) + Carousel Generator (HTML files)
3. **Creative Director** grades every piece → fixes anything below 28/35 → writes `briefings/batch-approved-YYYY-MM-DD.md`
4. **Calendar Manager** assigns posting slots → pushes all 11 pieces to Notion
5. **You** review and approve the batch in Notion → post when ready

Total time from command to Notion: ~10–15 minutes.

---

## Briefing Files

All agents communicate via files in `briefings/`:

| File | Written by | Read by |
|------|-----------|---------|
| `briefings/trend-brief-YYYY-MM-DD.md` | Trend Scout | Idea Generator, Content Strategist |
| `briefings/morning-briefing-YYYY-MM-DD.md` | Idea Generator | You (founder) |
| `briefings/content-plan-YYYY-MM-DD.md` | Content Strategist | Both Copywriters + Carousel Generator |
| `briefings/batch-raw-YYYY-MM-DD.md` | Both Copywriters | Creative Director |
| `briefings/batch-approved-YYYY-MM-DD.md` | Creative Director | Calendar Manager + you |

---

## Approving a Batch in Notion

After `/run-marketing-team` completes:
1. Open Notion → Bloggo Content Engine or YOOBIN Content Engine
2. Filter by Status = "Draft" and Post Date = this week
3. Read each piece. If it looks good: change Status → "Approved"
4. If you want changes: edit directly in Notion, then change Status → "Approved"
5. Post when the date arrives (manual posting — no auto-publishing in V1)

---

## Adding an Idea via Idea Inbox

If you want to inject a specific idea into the next content run:
1. Add it to `docs/Marketing/Idea Inbox.md`
2. Run `/run-marketing-team` — the Content Engine reads the Idea Inbox in Step 1

---

## Changing the Active Launch Phase

The active phase controls the CTA on every piece of content.

To change it:
1. Open `Workflows/Content Engine.md`
2. Find the line: `> **Current phase: [phase]**`
3. Change it to: `> **Current phase: Launch Week**` (or Post-Launch)
4. All future content runs will use the new CTA automatically

| Phase | CTA |
|-------|-----|
| Pre-Launch | "Join the Bloggo beta — link in bio" |
| Launch Week | "Download now — App Store" |
| Post-Launch | "Try it free" / "Share your first blog" |

---

## Notion Database IDs

| Database | ID | MCP |
|----------|----|-----|
| Yoobin Content Engine | `3378683d-d8fb-8109-a3c5-eabd65c1a6f1` | `notion-personal` |
| Yoobin Idea Bank | `3378683d-d8fb-8182-8e00-f2718ba2835d` | `notion-personal` |
| Bloggo Content Engine | `32d8683d-d8fb-80cf-9941-ed25238b6fe2` | `notion` |
| Bloggo Idea Bank | `9af1fcdb-c71c-4d6e-bdb0-c5b6a94ec55d` | `notion` |

Content routing: personal brand content → `notion-personal`. Bloggo company content → `notion`. When in doubt: "Is this posted from Yoobin's account or Bloggo's account?"

---

## Analyzing a Post's Performance

Run: `/analyze-performance [post title or date]`

What to have ready:
- The exact post title as it appears in Notion (or the date it was posted)
- Your Instagram retention screenshot (Instagram app → Insights → the post → "Plays by second") — the skill will ask for this

What happens:
1. The skill finds the post in Notion and pulls metrics from the Instagram API
2. You share the retention screenshot (or describe the drop-off point)
3. The skill generates an analysis block with views, saves, shares vs. average, retention insight, and 3 hook rewrite suggestions
4. The analysis block is appended to the post's Performance field in Notion
5. If the post outperformed the average on saves or shares, the winning pattern is added to tomorrow's trend brief automatically

---

## Repurposing a Winning Post

Run: `/repurpose [post title]`

The post must already exist in Notion (either Yoobin or Bloggo database).

What happens:
1. The Repurpose Agent finds the original post in Notion and reads its format and performance
2. It adapts the core idea to the 2 other formats (e.g. Reel → Carousel + LinkedIn)
3. All adapted pieces pass through the Creative Director (28+/35 required to proceed)
4. Approved repurposed drafts are pushed to the same account's Notion DB with the title `[Original title] — [New format]` and a link back to the original
```

- [ ] **Step 14.2: Verify**

Confirm file exists and covers all 8 roles, all 7 commands, the cron schedule, the full pipeline walkthrough, briefing file map, Notion approval steps, launch phase change instructions, and all 4 Notion database IDs.

- [ ] **Step 14.3: Commit**

```bash
git add "y:/Agentic FLow/MARKETING-TEAM.md"
git commit -m "docs: add MARKETING-TEAM.md founder cheat sheet"
```

---

## Task 15: Final Verification

- [ ] **Step 15.1: Verify plugin registration**

Run: `cat "C:/Users/yoobi/.claude/plugins/installed_plugins.json"`
Confirm `bloggo-marketing@local` appears with correct installPath.

- [ ] **Step 15.2: Verify all skill files exist**

Run:
```bash
ls "C:/Users/yoobi/.claude/plugins/bloggo-marketing/skills/"
```
Expected: 7 directories visible: `trend-scout`, `content-strategist`, `creative-director`, `calendar-manager`, `run-marketing-team`, `analyze-performance`, `repurpose`

- [ ] **Step 15.3: Verify workflow upgrades**

Check that:
- `Workflows/overnight-idea-generator.md` contains `## Step 0: Read Today's Trend Brief`
- `Workflows/Content Engine.md` contains `### Step 0 — Read Content Plan from Strategist`
- `Workflows/performance-feedback-agent.md` contains `## Step 8: Feed Top Performers`
- `Workflows/carousel-generator.md` exists (no changes needed — just confirm the file is present since run-marketing-team dispatches a subagent using it)

Run: `ls "y:/Agentic FLow/Workflows/carousel-generator.md"`
Expected: file found

- [ ] **Step 15.4: Verify briefings folder**

Run: `ls "y:/Agentic FLow/briefings/"`
Expected: `.gitkeep` visible

- [ ] **Step 15.5: Verify MARKETING-TEAM.md**

Run: `ls "y:/Agentic FLow/MARKETING-TEAM.md"`
Expected: file visible at project root

- [ ] **Step 15.6: Final commit**

```bash
git add "y:/Agentic FLow"
git add "C:/Users/yoobi/.claude/plugins/bloggo-marketing/"
git commit -m "feat: complete AI marketing team — 7 skills, 3 workflow upgrades, cron, cheat sheet"
```
