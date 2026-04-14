# Overnight Idea Generator

## Trigger
Cron runs this at 5AM PST (13:00 UTC) daily.
Also runnable manually: "Run the overnight idea generator"

---

## Context Files — Read Before Generating Ideas

Always read these before generating ideas. They define brand voice, content pillars, and product context:

- `docs/marketing/bloggo-brand.md` — brand voice, tone, writing rules
- `docs/marketing/bloggo-product-context.md` — product features, personas, differentiators
- `docs/workflow/Content Engine.md` — The COntent engine
- `docs/Marketing/Content Grader.md` — scoring rubric and content rules
- `docs/Marketing/Viral Short-Form Video Playbook.md` — Reel/video formula
- `docs/Marketing/Instagram Carousel Cheat Sheet.md` — carousel structure

---

## Step 1: News + Trend Scan

Run web searches to find what's happening in the world and what's performing in content right now:

**News searches:**
1. Search: `top world news today [current date]`
2. Search: `tech news AI startups today [current date]`
3. Search: `social media creator trends this week [current month] [current year]`
4. Search: `app store iOS trends today [current month] [current year]`

Extract 6–8 news headlines. For each include: headline, 1-sentence summary, and why it matters to a founder/creator.

**Content trend searches:**
1. Search: `TikTok trending content founders startup builders [current month] [current year]`
2. Search: `Instagram Reels travel app niche viral content [current month] [current year]`
3. Search: `building in public indie hacker content trending this week`
4. Search: `TikTok travel content trending this week`

Extract 5–8 content trend signals: specific topics, formats, angles, or hooks getting traction right now.

**Failure mode:** If web searches return no usable trend data, fall back to evergreen angles:
- Building in public / behind-the-scenes
- Day-in-the-life of a founder
- Product feature demos
- Relatable startup struggle moments
- Travel memory nostalgia

---

## Step 2: Pillar Audit

Read the current Content Idea Bank tables to understand what's already stocked.

**Yoobin Content Idea Bank** (use `mcp__notion-personal__API-get-block-children`):
- Table block ID: `3378683d-d8fb-8182-8e00-f2718ba2835d`

**Bloggo Content Idea Bank** (use `mcp__notion__API-get-block-children`):
- Table block ID: `3418683d-d8fb-806e-b72f-f984f06c3dfc`

For each table, read all rows and count ideas by Content Pillar column. Note which pillars are over-represented and which are empty or low.

---

## Step 3: Generate 10 Ideas

Generate **5 ideas for Yoobin** (personal brand) and **5 ideas for Bloggo** (company account).

### Yoobin content pillars — balance across these 4:
- Building in Public
- Product Builder Lessons
- The Traveler
- Startup Reality

### Bloggo content pillars — balance across these 5:
- The Problem
- The Magic
- Travel Inspiration
- Brand Values
- Community

### Rules:
- Do NOT repeat ideas already in the bank (check Step 2 results)
- Prioritize under-represented pillars from the audit
- Match each idea to a trend signal from Step 1 where possible
- Every idea must have all 10 fields filled in (no empty cells)
- Apply brand voice rules from `docs/marketing/bloggo-brand.md` to every hook
- Never mention cloud features, Android, or invented pricing

### 10 fields per idea:

| Field | What to write |
|-------|--------------|
| **Idea** | The core concept — 1 sentence describing what the content is about |
| **Hook** | Opening line that stops the scroll — 5–8 words, plain language, no jargon |
| **Category** | One of: Trend-based / Evergreen / Reactive |
| **Priority** | One of: High / Medium / Low |
| **Payoff** | What the viewer gets or feels by the end — 1 sentence |
| **Hook Type** | One of: Curiosity / Relatable / Controversial / Emotional |
| **Content Pillar** | Matched pillar name from the lists above (exact text) |
| **Format** | One of: Reel / Carousel / LinkedIn |
| **Confidence** | One of: High Confidence / Experimental / Viral Potential |
| **Why It Works** | 1–2 sentences explaining the trend signal or psychology behind this idea |

---

## Step 4: Add Rows to Notion Tables

Before writing, read the first row (header row) of each table to confirm the current column order:
- Use `mcp__notion-personal__API-get-block-children` on `3378683d-d8fb-8182-8e00-f2718ba2835d`
- Use `mcp__notion__API-get-block-children` on `9af1fcdb-c71c-4d6e-bdb0-c5b6a94ec55d`

Write cells in the exact column order shown in the header row.

**Add 5 Yoobin rows** to table `3378683d-d8fb-8182-8e00-f2718ba2835d`:
- Use `mcp__notion-personal__API-patch-block-children`
- Each child must be a `table_row` block with `cells` array matching the column count
- Each cell is an array of rich_text objects: `[{"type": "text", "text": {"content": "value"}}]`

**Add 5 Bloggo rows** to table `3418683d-d8fb-806e-b72f-f984f06c3dfc`:
- Use `mcp__notion__API-patch-block-children`
- Same structure

**Failure mode:** If a Notion write fails, log the error and continue. Save all ideas to the briefing file regardless — ideas should never be lost because of a Notion API error.

---

## Step 4b: Generate 7 Bloggo TikTok Slideshows

Generate 7 ready-to-build TikTok photo slideshow concepts for Bloggo's company account. TikTok photo slideshows hold attention longer than single videos and are currently favoured by the algorithm.

For each of the 7 slideshows include all of these fields:

| Field | What to write |
|-------|--------------|
| **Title** | The content concept — 1 sentence |
| **Pillar** | One of: The Problem / The Magic / Travel Inspiration / Brand Values / Community |
| **Hook Slide** | First slide text — max 8 words, scroll-stopping |
| **Slide Outline** | 5–7 slides, each under 10 words |
| **Caption** | Full TikTok caption: hook line + body + CTA + hashtags |
| **Why It Works** | 1 sentence on the trend or psychology behind it |

**Bloggo brand rules for all 7 slideshows:**
- Warm, confident, simple tone — never technical or jargon-heavy
- Lead with user benefit, not the feature
- Never mention cloud, Android, or pricing
- Privacy (on-device AI, photos never leave the phone) is a differentiator — use it when relevant
- CTA: "Join the Bloggo beta — link in bio" or "Follow for more"
- Bloggo one-liner: "Turn your travel photos into beautiful blogs in seconds — no writing required"

---

## Step 5: Save Morning Briefing

Write a file to `Magic/briefing-[YYYY-MM-DD].md` (use today's date).

Use this exact format:

```markdown
# Morning Briefing — [Full date, e.g. April 14, 2026]

## World & Tech News
| Headline | Summary | Why It Matters to You |
|----------|---------|----------------------|
| [headline] | [1-sentence summary] | [why it matters to a founder/creator] |
(6-8 rows)

## Content Trend Signals
- [signal 1 — what was trending and where]
- [signal 2]
(list all 5-8 signals)

## 10 Content Ideas Added to Notion

### Yoobin (5 ideas)
| # | Idea | Hook | Pillar | Format | Confidence |
|---|------|------|--------|--------|------------|
| 1 | [idea] | [hook] | [pillar] | [format] | [confidence] |
| 2 | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... | ... |

### Bloggo (5 ideas)
| # | Idea | Hook | Pillar | Format | Confidence |
|---|------|------|--------|--------|------------|
| 1 | [idea] | [hook] | [pillar] | [format] | [confidence] |
| 2 | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... | ... |

## Pillar Balance (ideas in bank after today)
**Yoobin:** Building in Public: X | Product Builder Lessons: X | The Traveler: X | Startup Reality: X
**Bloggo:** The Problem: X | The Magic: X | Travel Inspiration: X | Brand Values: X | Community: X

## 7 Bloggo TikTok Slideshows

### Slideshow 1
- **Title:**
- **Pillar:**
- **Hook Slide:**
- **Slide Outline:**
  1.
  2.
  3.
  4.
  5.
- **Caption:**
- **Why It Works:**

(repeat for all 7)

## Notion Status
- Yoobin: ✅ 5 rows added  (or ❌ Error: [describe what failed])
- Bloggo: ✅ 5 rows added  (or ❌ Error: [describe what failed])
```
