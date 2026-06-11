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
