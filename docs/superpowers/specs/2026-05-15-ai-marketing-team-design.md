# AI Marketing Team — Design Spec
**Date:** 2026-05-15
**Status:** Approved by user

---

## Problem

The founder is handling two distinct marketing efforts simultaneously — a personal brand (Yoobin) and a startup (Bloggo). The existing system has solid workflow files but suffers from two core problems:

1. **Research falls on the founder.** Trend scanning, competitor monitoring, and hook inspiration all require manual effort before any content can be created.
2. **No consistency enforcer.** Output quality varies run to run with no system-level gate ensuring brand standards are met before content reaches Notion.

---

## Solution

Convert the existing workflow-file system into a full **8-role AI Marketing Team** built on Claude Code Skills and parallel subagents. The team runs on an assembly-line model: research and idea generation run overnight on a cron, content creation fires from a single `/run-marketing-team` command, and a Creative Director enforces brand quality on every piece before it reaches Notion.

---

## Architecture

### Coordination Model: Assembly Line
Agents pass work to each other automatically via shared briefing files. The founder touches the system at two points only:
1. **Optionally** — set a weekly focus before running (e.g. "emphasize privacy this week")
2. **Required** — approve the final batch in Notion

### Trigger Model: Hybrid
- **4AM cron daily:** Trend Scout + Idea Generator run in parallel
- **Manual command:** `/run-marketing-team` fires the full content creation pipeline

---

## The 8 Roles

### 1. Trend Scout `[NEW]`
- **Trigger:** 4AM cron daily, runs in parallel with Idea Generator
- **Searches:** Viral travel hooks, TikTok/IG creator formats, AI/on-device AI news, competitor moves (Google Photos, Day One, Polarsteps), founder/startup discourse
- **Outputs:** Top 5 ranked trend signals, top 3 competitor moves, 3 ready-to-use hook angles, 1 format recommendation
- **Writes:** `briefings/trend-brief-YYYY-MM-DD.md`
- **Read by:** Idea Generator + Content Strategist

### 2. Idea Generator `[UPGRADE — was: overnight-idea-generator.md]`
- **Trigger:** 4AM cron daily, runs in parallel with Trend Scout
- **Change from current:** Now reads today's trend brief before generating ideas, grounding all 10 ideas in current trends rather than evergreen angles only
- **Still does:** Pillar audit in Notion, generates 5 Yoobin + 5 Bloggo ideas, pushes to both Notion idea banks, saves morning briefing to `briefings/`

### 3. Content Strategist `[NEW]`
- **Trigger:** First step of `/run-marketing-team`
- **Reads:** Today's trend brief + Notion pillar bank (gap audit) + recent performance data + current launch phase
- **Decides:** Which 11 pieces to create this week (format, pillar, account, priority order)
- **Writes:** `briefings/content-plan-YYYY-MM-DD.md`
- **Read by:** Copywriter subagents + Carousel Generator

### 4. Copywriter — Yoobin `[UPGRADE — was: Content Engine.md]`
- **Trigger:** Parallel subagent, fired by `/run-marketing-team` after Strategist completes
- **Change from current:** Now reads content plan from Strategist rather than operating independently. Produces only the pieces assigned to the Yoobin personal brand account.
- **Still does:** Reels, Carousels, LinkedIn posts in founder voice; applies active launch phase CTA

### 5. Copywriter — Bloggo `[UPGRADE — was: Content Engine.md]`
- **Trigger:** Parallel subagent, fired simultaneously with Copywriter — Yoobin
- **Change from current:** Same as above but for the Bloggo company account voice
- **Carousel Generator** runs as a third parallel subagent alongside both Copywriters

### 6. Creative Director / Brand Guardian `[NEW]`
- **Trigger:** After all Copywriter subagents complete; reviews the full batch
- **Uses:** Existing `docs/Marketing/Content Grader.md` rubric — no new grading system
- **Grading actions:**
  - 28–35: PUSH — passes through unchanged
  - 20–27: REVISE — rewrites hook or restructures, re-grades
  - Below 20: REWRITE — scraps and rewrites from scratch, re-grades
- **Also checks:** Brand voice violations (banned words, passive voice, cloud features, Android mentions), correct CTA for active launch phase
- **Writes:** `briefings/batch-YYYY-MM-DD.md` with all grades and notes
- **Nothing reaches Notion until it scores 28+**

### 7. Calendar Manager `[NEW]`
- **Trigger:** Final step of `/run-marketing-team`, after Creative Director approves batch
- **Does:** Reads approved batch → checks Notion for open posting slots this week → assigns each piece to a slot by platform + account → flags empty slots → pushes to Notion Content Engine DBs
- **Output to founder:** Summary of scheduled pieces + any empty slot warnings + Notion links for review

### 8. Performance Analyst `[UPGRADE — was: performance-feedback-agent.md]`
- **Trigger:** On-demand via `/analyze-performance [post title or date]`
- **Change from current:** After analysis, top-performing hooks and formats are appended to the latest trend brief so they inform the next Trend Scout run
- **Still does:** Pulls Instagram metrics via API, requests retention screenshot, generates analysis block, appends to Notion Performance field

### Bonus: Repurpose Agent `[NEW]`
- **Trigger:** On-demand via `/repurpose [post title]`
- **Does:** Finds original post in Notion → reads format + performance → adapts to 2 other formats (e.g. Reel → Carousel → LinkedIn thread) → passes all 3 through Creative Director → pushes to Notion as new drafts linked to original

---

## Full Pipeline Flow

```
OVERNIGHT — 4AM CRON
├── Trend Scout subagent     ── parallel ──┐
└── Idea Generator subagent  ─────────────┘
        ↓ briefings/trend-brief-YYYY-MM-DD.md
        ↓ briefings/morning-briefing-YYYY-MM-DD.md
        ↓ Notion idea banks (both)

YOU TYPE: /run-marketing-team
        ↓
Content Strategist
        ↓ briefings/content-plan-YYYY-MM-DD.md
        ↓
Copywriter — Yoobin  ── parallel ──┐
Copywriter — Bloggo  ──────────────┤
Carousel Generator   ──────────────┘
        ↓ briefings/batch-YYYY-MM-DD.md (raw)
        ↓
Creative Director (grades + fixes all pieces)
        ↓ briefings/batch-YYYY-MM-DD.md (approved)
        ↓
Calendar Manager → Notion (both DBs)
        ↓
YOU APPROVE BATCH IN NOTION ✓

ON-DEMAND
/analyze-performance [post] → Performance Analyst
/repurpose [post]           → Repurpose Agent → Creative Director → Notion
```

---

## File Structure

### New Claude Code Skills
Location: `~/.claude/plugins/bloggo-marketing/skills/`

| File | Slash Command | Role |
|------|--------------|------|
| `run-marketing-team.md` | `/run-marketing-team` | Master orchestrator |
| `trend-scout.md` | `/trend-scout` | Overnight research |
| `content-strategist.md` | `/content-strategist` | Weekly planning |
| `creative-director.md` | `/creative-director` | Quality enforcement |
| `calendar-manager.md` | `/calendar-manager` | Notion scheduling |
| `analyze-performance.md` | `/analyze-performance [post]` | Post analytics |
| `repurpose.md` | `/repurpose [post]` | Format adaptation |

All skills are callable standalone in addition to being part of the pipeline.

### Plugin Manifest
`~/.claude/plugins/bloggo-marketing/plugin.json` — registers all skills with Claude Code

### Upgraded Workflow Files
Location: `Workflows/` (existing, modified in place)

| File | Change |
|------|--------|
| `overnight-idea-generator.md` | Reads trend brief before generating |
| `Content Engine.md` | Reads content plan from Strategist |
| `performance-feedback-agent.md` | Feeds top performers to trend brief |
| `carousel-generator.md` | No change — called by pipeline |
| `tiktok-slideshow-agent.md` | No change — available standalone |

### Shared Briefing Files
Location: `briefings/` (new folder)

| File | Written by | Read by |
|------|-----------|---------|
| `trend-brief-YYYY-MM-DD.md` | Trend Scout | Idea Generator, Content Strategist |
| `content-plan-YYYY-MM-DD.md` | Content Strategist | All Copywriter subagents |
| `batch-YYYY-MM-DD.md` | Copywriters → Creative Director | Calendar Manager, founder |

### New Top-Level Files
| File | Purpose |
|------|---------|
| `MARKETING-TEAM.md` | Founder cheat sheet: all commands, cron schedule, pipeline guide, Notion IDs |
| `~/.claude/plugins/bloggo-marketing/plugin.json` | Plugin manifest |

---

## MARKETING-TEAM.md Contents

The guide file at the project root covers:
- Team overview: 8 roles in plain English
- Full command reference with example usage
- Cron schedule: what runs at 4AM and what it produces
- Pipeline walkthrough: step-by-step what `/run-marketing-team` does
- How to approve a batch in Notion
- How to add an idea via the Idea Inbox
- How to analyze a post's performance
- How to repurpose a winning post
- Notion database IDs for both workspaces
- Active launch phase and how to change it

---

## Notion Integration

All existing Notion IDs are preserved unchanged:

| Resource | ID | MCP |
|----------|----|-----|
| Yoobin Content Engine DB | `3378683d-d8fb-8109-a3c5-eabd65c1a6f1` | `notion-personal` |
| Yoobin Content Idea Bank | `3378683d-d8fb-8182-8e00-f2718ba2835d` | `notion-personal` |
| Bloggo Content Engine DB | `32d8683d-d8fb-80cf-9941-ed25238b6fe2` | `notion` |
| Bloggo Content Idea Bank | `9af1fcdb-c71c-4d6e-bdb0-c5b6a94ec55d` | `notion` |

Content routing rule (unchanged): personal brand content → `notion-personal`, Bloggo company content → `notion`.

---

## Cron Schedule

| Time | What runs | Produces |
|------|-----------|---------|
| 4AM daily | Trend Scout + Idea Generator (parallel) | `briefings/trend-brief-YYYY-MM-DD.md` + 10 new Notion ideas |

The existing overnight cron is updated from its current time to 4AM and its prompt updated to invoke both Trend Scout and Idea Generator as parallel subagents.

---

## Constraints Preserved

All existing brand rules are enforced system-wide by the Creative Director:
1. Never mention cloud features (V1 is on-device only)
2. iOS only — no Android
3. Privacy is a feature — lead with it when relevant
4. "Bloggo" always capitalized
5. Active voice always
6. Benefit-first, not feature-first
7. No jargon: leverage, utilize, seamless, powerful are banned
8. Short sentences, one idea per sentence
9. No more than one exclamation point per post

---

## What This Does Not Include

- Automated posting to Instagram/TikTok (requires separate API integration beyond scope)
- YouTube-specific scheduling (still manual upload after content is created)
- LinkedIn auto-posting (still manual)
- Real-time analytics dashboard (Performance Analyst is on-demand only)

---

## Success Criteria

- Founder types one command (`/run-marketing-team`) to produce a full week of content
- All content scores 28+ before reaching Notion — no manual grading required
- Research brief is waiting every morning without founder intervention
- Pillar balance is maintained automatically by Content Strategist
- Repurposing winning posts takes one command instead of a manual rewrite session
