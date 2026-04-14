# Content Automation System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build two automated agents — a Performance Feedback Agent and an Overnight Idea Generator — that close the content feedback loop and eliminate the daily ideation bottleneck.

**Architecture:** Workflow markdown files extend the existing Claude Code workflow pattern. A `.env` file stores Instagram API credentials. Claude Code's CronCreate schedules the nightly idea generator at 5AM PST. Notion MCP tools write directly to both Content Engine workspaces.

**Tech Stack:** Claude Code workflows, Notion MCP (`notion` + `notion-personal`), Instagram Graph API (REST via Bash/curl), Claude Code CronCreate, Web Search

---

## Confirmed Notion IDs (do not change)

| Resource | ID |
|----------|-----|
| Yoobin Content Engine page | `3378683d-d8fb-8060-b964-d8c5ac388789` |
| Yoobin Content Engine DB | `3378683d-d8fb-8109-a3c5-eabd65c1a6f1` |
| Yoobin Content Idea Bank table (block) | `3378683d-d8fb-8182-8e00-f2718ba2835d` |
| Bloggo Content Engine page | `32d8683d-d8fb-80f7-9e4f-d7fbecd719c1` |
| Bloggo Content Engine DB | `32d8683d-d8fb-80cf-9941-ed25238b6fe2` |
| Bloggo Content Idea Bank table (block) | `9af1fcdb-c71c-4d6e-bdb0-c5b6a94ec55d` |

---

## File Map

| File | Action | Purpose |
|------|---------|---------|
| `Workflows/performance-feedback-agent.md` | Create | Instructions for Agent 1 |
| `Workflows/overnight-idea-generator.md` | Create | Instructions for Agent 2 |
| `.env` | Create | Instagram API credentials template |
| `resources/instagram-api-setup.md` | Create | Step-by-step API setup guide for user |
| `Magic/.gitkeep` | Create | Initializes Magic/ folder |

---

## Pre-flight: One-Time User Actions

Before implementing, the user must complete these in Notion:

1. **Change the Performance column type** in both Content Engine databases from `URL` to `Text`:
   - Go to Yoobin Content Engine → click "Performance" column header → change type to "Text"
   - Do the same in Bloggo Content Engine
   - ⚠️ Without this change, the Performance Feedback Agent cannot write analysis text

2. **Expand the Bloggo Content Idea Bank table** from 6 to 10 columns:
   - The Bloggo table currently has 6 columns; the Yoobin table already has 10
   - Add 4 more columns to match: Content Pillar, Format, Confidence, Why It Works

---

## Task 1: Create Magic/ Folder

**Files:**
- Create: `Magic/.gitkeep`

- [ ] **Step 1: Create the Magic folder**

```bash
mkdir -p "y:/Agentic FLow/Magic"
touch "y:/Agentic FLow/Magic/.gitkeep"
```

Expected: `Magic/` directory exists with `.gitkeep` placeholder

---

## Task 2: Create .env Template

**Files:**
- Create: `.env`

- [ ] **Step 1: Create the .env file** with placeholder values

File contents:
```
# Instagram Graph API Credentials
# See resources/instagram-api-setup.md for how to get these values

INSTAGRAM_APP_ID=
INSTAGRAM_APP_SECRET=
INSTAGRAM_ACCESS_TOKEN=
INSTAGRAM_TOKEN_EXPIRY=    # ISO 8601 format only: YYYY-MM-DD (e.g. 2026-06-12)
INSTAGRAM_USER_ID=
```

- [ ] **Step 2: Verify .env is not tracked by git** (if repo exists)

If a `.gitignore` exists, confirm `.env` is listed. If not, add it.

---

## Task 3: Create Instagram API Setup Guide

**Files:**
- Create: `resources/instagram-api-setup.md`

- [ ] **Step 1: Write the setup guide**

File contents:

```markdown
# Instagram API Setup Guide

One-time setup to connect the Performance Feedback Agent to your Instagram account.
Takes approximately 15–20 minutes.

---

## Prerequisites

- Instagram account switched to **Professional** (Creator or Business)
- A **Facebook Page** linked to your Instagram
- A free account at **developers.facebook.com**

---

## Step 1: Create a Meta App

1. Go to [developers.facebook.com](https://developers.facebook.com)
2. Click **My Apps** → **Create App**
3. Select **Other** → **Business**
4. Give your app a name (e.g. "Yoobin Analytics") → click **Create App**

---

## Step 2: Add Instagram Graph API Product

1. In your app dashboard, click **Add Product**
2. Find **Instagram Graph API** → click **Set Up**

---

## Step 3: Generate a User Access Token

1. Go to **Tools** → **Graph API Explorer**
2. Select your app from the dropdown
3. Click **Generate Access Token**
4. Log in with Facebook and grant permissions:
   - `instagram_basic`
   - `instagram_manage_insights`
   - `pages_show_list`
   - `pages_read_engagement`
5. Copy the short-lived token

---

## Step 4: Exchange for a Long-Lived Token

Run this in your terminal (replace values):

```bash
curl -i -X GET "https://graph.facebook.com/v18.0/oauth/access_token
  ?grant_type=fb_exchange_token
  &client_id=YOUR_APP_ID
  &client_secret=YOUR_APP_SECRET
  &fb_exchange_token=SHORT_LIVED_TOKEN"
```

Copy the `access_token` from the response. This token lasts **60 days**.

---

## Step 5: Get Your Instagram User ID

```bash
curl "https://graph.facebook.com/v18.0/me/accounts?access_token=YOUR_LONG_TOKEN"
```

Find the Page ID, then:

```bash
curl "https://graph.facebook.com/v18.0/YOUR_PAGE_ID?fields=instagram_business_account&access_token=YOUR_LONG_TOKEN"
```

Copy the `instagram_business_account.id` value.

---

## Step 6: Fill in .env

Open `.env` in the project root and fill in all values:

```
INSTAGRAM_APP_ID=your_app_id
INSTAGRAM_APP_SECRET=your_app_secret
INSTAGRAM_ACCESS_TOKEN=your_long_lived_token
INSTAGRAM_TOKEN_EXPIRY=2026-06-12   ← 60 days from today
INSTAGRAM_USER_ID=your_instagram_user_id
```

---

## Token Refresh (every 60 days)

When the agent warns you about expiry, run this to refresh:

```bash
curl -i -X GET "https://graph.facebook.com/v18.0/oauth/access_token
  ?grant_type=fb_exchange_token
  &client_id=YOUR_APP_ID
  &client_secret=YOUR_APP_SECRET
  &fb_exchange_token=YOUR_CURRENT_TOKEN"
```

Update `INSTAGRAM_ACCESS_TOKEN` and `INSTAGRAM_TOKEN_EXPIRY` in `.env`.

---

## Testing the Connection

Once `.env` is filled in, test it by saying in Claude Code:
> "Test my Instagram API connection"

The agent will call `GET /me/media` and list your 5 most recent posts.
```

---

## Task 4: Create Performance Feedback Agent Workflow

**Files:**
- Create: `Workflows/performance-feedback-agent.md`

- [ ] **Step 1: Write the workflow file**

File contents:

```markdown
# Performance Feedback Agent

## Trigger
User says: "analyze performance for: [post title or date]"

---

## Step 1: Token Expiry Check

Read the `.env` file and check `INSTAGRAM_TOKEN_EXPIRY`.

- If the expiry date is within 7 days from today:
  > ⚠️ "Your Instagram API token expires on [date]. See resources/instagram-api-setup.md for refresh instructions."
  Continue anyway.

- If the expiry date has already passed:
  > ❌ "Your Instagram API token has expired. Please refresh it using resources/instagram-api-setup.md before running this agent."
  Stop here.

---

## Step 2: Find the Matching Notion Page

Search for the post in both Notion workspaces using the title or date provided:

1. Search `notion-personal` (YOOBIN Content Engine DB: `3378683d-d8fb-8109-a3c5-eabd65c1a6f1`)
2. Search `notion` (Bloggo Content Engine DB: `32d8683d-d8fb-80cf-9941-ed25238b6fe2`)

Match by:
- Title substring (case-insensitive)
- OR Post Date field matching the provided date

If no match found, ask the user:
> "I couldn't find '[title/date]' in either Notion database. Can you provide the exact title or date?"

---

## Step 3: Pull Instagram Metrics

Read `INSTAGRAM_ACCESS_TOKEN` and `INSTAGRAM_USER_ID` from `.env`.

**Fetch recent media list:**
```
GET https://graph.facebook.com/v18.0/{INSTAGRAM_USER_ID}/media
  ?fields=id,caption,timestamp,media_type
  &access_token={INSTAGRAM_ACCESS_TOKEN}
```

Match the post by:
1. Caption text containing the Notion page title
2. OR timestamp within ±1 day of the Notion Post Date

**Fetch post insights:**
```
GET https://graph.facebook.com/v18.0/{ig_media_id}/insights
  ?metric=impressions,reach,saved,shares,comments_count
  &access_token={INSTAGRAM_ACCESS_TOKEN}
```

Store: impressions, reach, saved, shares, comments_count

---

## Step 4: Get Historical Average

Query the same Notion database for all pages that have Performance data (non-empty Performance field).

Extract numeric values (views, saves, shares) from past Performance entries to calculate:
- Average impressions
- Average saves
- Average shares

If fewer than 3 past entries exist, note "insufficient history for comparison" and skip the comparison.

---

## Step 5: Request Retention Screenshot

Say to the user:
> "Please paste or upload your Instagram retention screenshot for this post (from Instagram Insights → Plays by second). I'll analyze the drop-off point."

Wait for the user to provide an image or describe the retention data.

---

## Step 6: Generate Analysis

Using all collected data, generate the following analysis:

```
[DATE]
Views: [impressions] | Saves: [saved] | Shares: [shares] | Reach: [reach]
vs avg: Views [+/-X%] | Saves [+/-Xx] | Shares [+/-X%]

[Retention insight from screenshot — where the drop-off occurred and why]

→ Hook rewrites:
  1. [rewrite 1 — curiosity angle]
  2. [rewrite 2 — relatable angle]
  3. [rewrite 3 — controversial/bold angle]

→ Next time: [1-2 specific improvement notes based on data]
```

---

## Step 7: Append to Notion Performance Column

Find the Notion page from Step 2.

Patch the Performance field (text type) by **appending** the new analysis block — do not overwrite existing content.

Format: prepend with a divider line if existing content is present.

Use:
- `notion-personal` API if the post is from Yoobin Content Engine
- `notion` API if the post is from Bloggo Content Engine

Confirm to the user:
> "✅ Analysis appended to '[post title]' in Notion."
```

---

## Task 5: Create Overnight Idea Generator Workflow

**Files:**
- Create: `Workflows/overnight-idea-generator.md`

- [ ] **Step 1: Write the workflow file**

File contents:

```markdown
# Overnight Idea Generator

## Trigger
Cron runs this at 5AM PST (13:00 UTC) daily.
Also runnable manually: "Run the overnight idea generator"

---

## Step 1: Trend Scan

Run web searches to find what's performing right now:

1. Search: "TikTok trending content for founders and startup builders this week"
2. Search: "Instagram Reels performing well travel and travel app niche [current month year]"
3. Search: "Indie hacker and building in public viral content this week"

Extract 5–8 trend signals: specific topics, formats, sounds, hooks that are getting traction.

**Failure mode:** If searches return no usable results, fall back to evergreen angles (building in public, day-in-the-life, product demos, relatable founder moments).

---

## Step 2: Pillar Audit

Read the current Content Idea Bank tables in both Notion workspaces to understand what's already stocked.

- Yoobin table block: `3378683d-d8fb-8182-8e00-f2718ba2835d`
- Bloggo table block: `9af1fcdb-c71c-4d6e-bdb0-c5b6a94ec55d`

Count ideas already in the bank by Content Pillar. Note any pillars that are over- or under-represented.

---

## Step 3: Generate 10 Ideas

Generate **5 ideas for Yoobin** and **5 ideas for Bloggo**, balanced across pillars.

### Yoobin content pillars (balance across these):
- Building in Public
- Product Builder Lessons
- The Traveler
- Startup Reality

### Bloggo content pillars (balance across these):
- The Problem
- The Magic
- Travel Inspiration
- Brand Values
- Community

### Rules:
- Never repeat an idea already in the bank
- Match each idea to a trend signal from Step 1 where possible
- Prioritize pillars that are under-represented in the current bank
- Every idea must have all 10 fields filled in

### For each idea, generate all 10 fields:

| Field | Description |
|-------|-------------|
| **Idea** | The core concept in 1 sentence |
| **Hook** | Opening line (5–8 words, stops the scroll) |
| **Category** | Trend-based / Evergreen / Reactive |
| **Priority** | High / Medium / Low |
| **Payoff** | What the viewer gets by the end |
| **Hook Type** | Curiosity / Relatable / Controversial / Emotional |
| **Content Pillar** | Matched pillar from the list above |
| **Format** | Reel / Carousel / LinkedIn |
| **Confidence** | High Confidence / Experimental / Viral Potential |
| **Why It Works** | 1–2 sentences: trend signal or psychology behind it |

---

## Step 4: Add Ideas to Notion Tables

Add rows to both Content Idea Bank tables.

**Yoobin** — append 5 rows to table block `3378683d-d8fb-8182-8e00-f2718ba2835d`:
- Use `notion-personal` API
- Use `mcp__notion-personal__API-patch-block-children` to append `table_row` blocks
- Each row must have exactly 10 cells in the same column order as the table header

**Bloggo** — append 5 rows to table block `9af1fcdb-c71c-4d6e-bdb0-c5b6a94ec55d`:
- Use `notion` API
- Same approach

> ⚠️ Before appending rows to either table, read the first row (header row) using `get-block-children` on the table block to confirm the current column order. Write cells in that exact order.

**Failure mode:** If a Notion write fails, skip it and continue. Save all 10 ideas to the Magic/ briefing file regardless. Log the Notion error in the briefing file.

---

## Step 5: Save Morning Briefing

Write a briefing file to `Magic/briefing-[YYYY-MM-DD].md`.

Format:

```markdown
# Morning Briefing — [Date]

## 10 Ideas Added to Notion

### Yoobin (5 ideas)
| # | Idea | Hook | Pillar | Format | Confidence |
|---|------|------|--------|--------|------------|
| 1 | ... | ... | ... | ... | ... |
...

### Bloggo (5 ideas)
| # | Idea | Hook | Pillar | Format | Confidence |
|---|------|------|--------|--------|------------|
| 1 | ... | ... | ... | ... | ... |
...

## Pillar Balance (ideas in bank after today)
**Yoobin:** Building in Public: X | Product Builder Lessons: X | The Traveler: X | Startup Reality: X
**Bloggo:** The Problem: X | The Magic: X | Travel Inspiration: X | Brand Values: X | Community: X

## Trend Signals Used Today
- [signal 1]
- [signal 2]
...

## Notion Status
- Yoobin: ✅ 5 rows added / ❌ [error if failed]
- Bloggo: ✅ 5 rows added / ❌ [error if failed]
```
```

---

## Task 6: Set Up Cron Job

- [ ] **Step 1: Use CronCreate to schedule the overnight idea generator**

Schedule: 5AM PST = 13:00 UTC daily

Cron expression: `0 13 * * *`

Cron prompt: `Read and execute the workflow at Workflows/overnight-idea-generator.md`

- [ ] **Step 2: Manually trigger a test run first**

Before relying on the cron, manually run the overnight idea generator once:
> "Run the overnight idea generator"

Verify:
- 5 rows were added to Yoobin Content Idea Bank in Notion
- 5 rows were added to Bloggo Content Idea Bank in Notion
- `Magic/briefing-[today].md` was created with correct format
- Pillar balance is shown

Only set up the cron after a successful manual test run.

---

## Verification Checklist

### Performance Feedback Agent
- [ ] Trigger: "analyze performance for: [a real post title]"
- [ ] Confirm Instagram API returns metrics (curl to `/me/media` works)
- [ ] Paste a retention screenshot — confirm analysis is generated
- [ ] Check Notion: Performance field was appended (not overwritten)
- [ ] Run a second time on same post — confirm it appended a second entry below the first
- [ ] Test token expiry warning: temporarily set `INSTAGRAM_TOKEN_EXPIRY` to yesterday's date

### Overnight Idea Generator
- [ ] Manual trigger works end-to-end
- [ ] 5 Yoobin rows + 5 Bloggo rows visible in Notion tables
- [ ] Briefing doc created in `Magic/` with correct format
- [ ] Pillars are balanced across the 10 ideas
- [ ] Cron fires at 5AM PST (check next morning)

---

## Known Limitations

- **Instagram retention data** is screenshot-only (not available via API). YouTube Analytics API integration can replace this in the future — the workflow file is designed to accept either source.
- **Performance column** must be changed from URL → Text type in Notion before Agent 1 can write to it. See Pre-flight section.
- **Content Idea Bank tables** are Notion simple tables (not databases). Rows are added as `table_row` blocks. Column order matters — the workflow must match the existing column order exactly.
