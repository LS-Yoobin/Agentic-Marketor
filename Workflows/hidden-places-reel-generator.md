# Hidden Places Reel Generator

## Trigger
Cron runs this at 5AM PST (13:00 UTC) daily.
Also runnable manually: "Run the hidden places reel generator"

---

## Purpose

Generate 10 daily reel briefs for Bloggo's Instagram/TikTok — each one a visually captivating hidden place in the world paired with a free stock video source, a curiosity hook, and a full caption that answers the hook and ties in Bloggo's value.

---

## Context Files — Read Before Generating

- `docs/marketing/bloggo-brand.md` — brand voice, tone, writing rules
- `docs/marketing/bloggo-product-context.md` — product features, personas, differentiators

---

## Step 1: Pick 10 Places

Select 10 **genuinely obscure, visually captivating** places from around the world.

**Rules:**
- No tourist traps (no Paris, Santorini, Bali, Iceland Blue Lagoon, Machu Picchu, etc.)
- Geographic diversity required — spread across: Americas, Europe, Africa, Asia, Oceania, Middle East/Central Asia
- Each place must have a **counterintuitive, visually answerable fact** — something you can *see* in the video that triggers a "wait, why does it look like that?" reaction
- Do not repeat places used in recent runs — aim for fresh content every day

**Good examples of the place + fact pattern:**
- Lake Hillier (Australia) → water is naturally pink due to bacteria and algae
- Fly Geyser (Nevada, USA) → man-made accident that grew into a colorful geothermal structure
- Socotra Island (Yemen) → alien-looking Dragon Blood Trees found nowhere else on Earth
- Zhangye Danxia (China) → layered rainbow rock formations from mineral deposits
- Waitomo Glowworm Caves (New Zealand) → cave ceiling covered in bioluminescent glowworms that look like stars

---

## Step 2: For Each Place, Build the Reel Brief

For each of the 10 places, produce all of the following:

### 2a. Interesting Fact
One wild, counterintuitive, or visually explainable fact about the place. Must be the kind of thing that makes someone stop scrolling and ask "wait, why?"

### 2b. Hook Question
A short question (5–10 words) that:
- The video will visually answer in the first 3 seconds
- Creates genuine curiosity — the viewer *has* to read the caption to get the answer
- Is tied directly to the fact and the visual of the video

Good hooks: "Why is this water pink?", "Why do these trees look alien?", "Why does this cave ceiling glow?"
Bad hooks: "Have you heard of this place?", "You need to visit here"

### 2c. Free Video Source
Provide:
- A specific **Pexels search term** that will return footage of this place or its defining visual feature
- The full Pexels video search URL: `https://www.pexels.com/search/videos/[search-term-hyphenated]/`
- Also provide a Pixabay fallback URL: `https://pixabay.com/videos/search/[search-term-hyphenated]/`
- The search term must match the *visual hook* — if the hook is about pink water, the video must show pink water

### 2d. On-Screen Text Overlays (3 lines)
```
Line 1: [The hook question]
Line 2: Answer in caption ↓
Line 3: You'd remember this... if you wrote it down in Bloggo
```

### 2e. Caption
Write the full Instagram/TikTok caption using this exact structure:

```
Secret places to travel — [Place Name], [Country]

[2–3 sentences answering the hook question. Plain, warm language. Explain the fact clearly — the kind of explanation that makes someone feel smart for learning it. No jargon.]

[1 sentence Bloggo tie-in. Connect the emotional experience of discovering this place to Bloggo's core value: preserving travel memories so you don't lose them. Must feel earned and specific — not generic. The Bloggo line should reflect why THIS place, THIS kind of discovery moment, is exactly what Bloggo is built to save.]

#wanderlust #hiddenplaces #[place-specific-tag] #traveltok #secretplaces #travelblogger
```

**Bloggo CTA examples (use as tone reference, don't copy verbatim):**
- "The kind of detail you'd only remember if you actually wrote it down."
- "Most people see the photo. Bloggo saves the story behind it."
- "A place this strange deserves more than a camera roll. Bloggo writes the story for you."
- "You took the photo. But did you save what it felt like to be there?"

**Caption rules:**
- Title ALWAYS starts with "Secret places to travel"
- ALWAYS include `#wanderlust #hiddenplaces`
- Add 2–3 place-specific or travel niche hashtags
- Never mention cloud, Android, or pricing
- Never use passive voice, jargon, or exclamation marks more than once

---

## Step 3: Write Output File

Save all 10 reel briefs to:
`output/Content/hidden-places-reels-[YYYY-MM-DD].md`

Use this exact format for each entry:

```markdown
## 🎬 Reel [N]: [Place Name]

**Location:** [City/Region, Country]
**Interesting Fact:** [1–2 sentences]
**Hook:** "[Hook question]"
**Video Search Term:** [exact Pexels search string]
**Pexels Video URL:** https://www.pexels.com/search/videos/[search-term]/
**Pixabay Fallback:** https://pixabay.com/videos/search/[search-term]/

**On-Screen Text:**
- Line 1: "[Hook question]"
- Line 2: "Answer in caption ↓"
- Line 3: "You'd remember this... if you wrote it down in Bloggo"

**Caption:**
Secret places to travel — [Place Name], [Country]

[answer paragraph]

[Bloggo tie-in sentence]

#wanderlust #hiddenplaces #[tag] #traveltok #secretplaces #travelblogger

---
```

---

## Step 4: Push to Notion

After generating, create a new page in the **Bloggo Content Engine** (`notion` MCP) titled:
`Hidden Places Reels — [Month Day, Year]`

Page content: paste the full markdown output of all 10 reel briefs.

Use `mcp__notion__API-post-search` to find the Bloggo Content Engine database, then `mcp__notion__API-post-page` to create the page.

**Failure mode:** If Notion write fails, log the error. The output file is the source of truth — never lose the content because of a Notion error.

---

## Quality Check Before Saving

Before writing the file, verify each of the 10 entries:
- [ ] Place is genuinely obscure (not a top-10 tourist destination)
- [ ] Hook question is visual and answerable by the video
- [ ] Video search term matches the hook visual
- [ ] Caption answers the hook clearly in 2–3 sentences
- [ ] Bloggo tie-in is specific and earned — not generic
- [ ] Title starts with "Secret places to travel"
- [ ] `#wanderlust #hiddenplaces` present in every caption
- [ ] Geographic diversity: at least 5 different continents represented
