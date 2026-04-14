# TikTok Slideshow Agent — Bloggo
**Call this workflow at the start of each content day or planning session.**

---

## What This Workflow Does

Generates a 7-post TikTok blueprint for the Bloggo company page.
Output: slide-by-slide production briefs ready to build in Canva, with audio pairing and captions.

---

## How to Call It

Say to Claude:

> "Run the TikTok slideshow agent. Here are my metrics from yesterday: [paste metrics]. Plan tomorrow's 7 posts."

Or if starting fresh:

> "Run the TikTok slideshow agent. No metrics yet. Plan the next 7 posts."

---

## Input Claude Needs From You

| Input | Where to find it | Required? |
|-------|-----------------|-----------|
| Yesterday's top-performing post (hook + views + likes + saves) | Your TikTok analytics | Yes |
| Any post that flopped (hook + why you think it didn't work) | Your TikTok analytics | Optional but valuable |
| Any format that felt hard to produce | Your own judgment | Optional |
| Upcoming product news or feature to highlight | Your brain | Optional |

If you have no metrics yet, skip the metrics input and Claude will default to the proven formula.

---

## The Proven Formula (Do Not Break)

Every 10-slide post follows this exact structure — it's what performed:

| Slide | Purpose |
|-------|---------|
| 1 | Hook — specific number + emotional loss or curiosity |
| 2 | Transition — reframe the problem in one line |
| 3–7 | Numbered items — specific, relatable, one per slide |
| 8 | Insight — save-worthy quote, no image, pure text |
| 9 | Solution — Bloggo appears here and only here |
| 10 | CTA — logo + "Link in bio" + mascot |

**Rules:**
- Product (Bloggo) does NOT appear until Slide 9
- Slide 8 is always the save-bait quote — no visual, just text
- Numbered items use gold accent on the number
- Mascot (Spunky-Cat) on Slide 1 (peeking) and Slide 8 (thinking) and Slide 10 (confident)

---

## Daily Post Mix (7 Posts)

| # | Time | Format | Purpose |
|---|------|--------|---------|
| 1 | 7am | 10-slide | Anchor post — emotional problem list. Open strong. |
| 2 | 9am | 1-slide | Quote/statement. Rides Post 1 momentum. |
| 3 | 11am | 10-slide | Second emotional list. Different angle, different audience segment. |
| 4 | 1pm | 1-slide | Relatable statement. Comment bait. |
| 5 | 3pm | 5-slide | Feature/product reveal. Mid-day curiosity push. |
| 6 | 6pm | 5-slide | Relatable list or comparison. Broadest reach post. |
| 7 | 9pm | 10-slide | Emotional closer. End-of-day save + follow push. |

---

## Audience Segments to Rotate Through

Each 10-slider should target a different segment. Don't hit the same audience twice in one day.

| Segment | What they care about | Best hook style |
|---------|---------------------|-----------------|
| Lapsed Documentarian | Guilt about backlog trips they never wrote | "X trips in your camera roll. Zero blogs." |
| Memory Keeper | Preserving feelings, not just photos | "5 things that disappear from travel memories" |
| Social Sharer | Polished, shareable output to send friends | "5 photos you can't explain anymore" |
| Frequent Traveler | Speed and efficiency | "What Bloggo does in 60 seconds" |

---

## Brand Specs (Never Change)

| Element | Value |
|---------|-------|
| Background | `#0D1117` deep navy |
| Text | `#FFFFFF` white |
| Accent | `#C9A84C` warm gold |
| Font | Inter Bold (headlines) / Inter Regular (body) |
| Max words/slide | 10 |
| Padding | 60px all sides |
| Logo | Bottom right, every slide, 40px height |
| Cat paw swipe | Bottom right, 80px — all slides except final CTA |

---

## Mascot Prompts (Copy-Paste Ready)

### Peeking (use on Slide 1 of 10-sliders)
```
@Spunky-Cat — keep the necklace and pendant around the cat's neck exactly
consistent with the Spunky-Cat element. Same style throughout.

black cartoon cat character, chunky round body, large expressive eyes,
short pointy ears, small white claw tips, slightly mischievous personality,
necklace with pendant around neck matching @Spunky-Cat exactly,
clean 2D cartoon illustration style, thick black outlines, subtle shading,
no background (transparent), isolated character,
only top half of head visible — cropped at the chin — as if peeking up
from below the frame, both large round eyes wide open and looking upward,
pupils dilated, eyebrows raised high in exaggerated surprise,
peering expression, low angle framing, tight crop on top of head,
soft flat lighting, no harsh shadows, vector cartoon style, clean cel-shaded look

negative: realistic, photorealistic, blurry, background, shadow drop,
gradient background, white background, gray background, full body,
extra limbs, deformed, ugly, low quality, watermark, text, logo
```
**Placement:** Bottom left — head peeking up from bottom edge of slide.

---

### Thinking (use on Slide 8 insight slide)
```
@Spunky-Cat — keep the necklace and pendant around the cat's neck exactly
consistent with the Spunky-Cat element. Same style throughout.

black cartoon cat character, chunky round body, large expressive eyes,
short pointy ears, small white claw tips, slightly mischievous personality,
necklace with pendant around neck matching @Spunky-Cat exactly,
clean 2D cartoon illustration style, thick black outlines, subtle shading,
no background (transparent), isolated character, full body visible,
seated upright, one front paw raised and resting gently under the chin
in a classic thinking pose, elbow resting on bent knee, head tilted
slightly to the left, eyes looking upward to the left as if deep in thought,
brow slightly furrowed in contemplation, three-quarter front angle,
soft flat lighting from front-left, no harsh shadows,
vector cartoon style, clean cel-shaded look

negative: realistic, photorealistic, blurry, background, shadow drop,
gradient background, white background, gray background, extra limbs,
deformed, ugly, low quality, watermark, text, logo
```
**Placement:** Bottom right — 40px from right, 40px from bottom. ~20% slide height.

---

### Confident (use on CTA slide — Slide 10)
```
@Spunky-Cat — keep the necklace and pendant around the cat's neck exactly
consistent with the Spunky-Cat element. Same style throughout.

black cartoon cat character, chunky round body, large expressive eyes,
short pointy ears, small white claw tips, slightly mischievous personality,
necklace with pendant around neck matching @Spunky-Cat exactly,
clean 2D cartoon illustration style, thick black outlines, subtle shading,
no background (transparent), isolated character, full body visible,
sitting upright on both hind legs, one front paw resting flat on the ground
beside it, other arm relaxed at side, head facing directly forward toward
viewer, slight confident smirk, one eyebrow slightly raised, half-lidded
eyes conveying cool self-assurance, front-facing camera angle, centered
framing, soft flat lighting from above, no harsh shadows, vector cartoon
style, clean cel-shaded look

negative: realistic, photorealistic, blurry, background, shadow drop,
gradient background, white background, gray background, extra limbs,
deformed, ugly, low quality, watermark, text, logo
```
**Placement:** Bottom left — 40px from left, 40px from bottom. ~25% slide height.

---

## Audio Strategy

**Default:** Love Between the Lines (proven, 332k+ posts, emotionally matches the brand)

**When to use alternatives:**
- Humor/meme posts → find trending relatable audio (TikTok search → Sounds → This Week)
- Feature/product posts → find clean upbeat trending audio
- Comment-bait 1-sliders → match the emotional register of the text

**How to find trending audio:** TikTok → Search → Sounds tab → filter "This Week" → target 50k–500k posts

---

## Metrics-Based Learning (Fill in after each day)

After posting, log results. Claude reads these before generating the next day's plan.

### How to log:
Paste this into your message when calling the agent next time:

```
Yesterday's results:
- Best performer: [hook] — [views]v / [likes]l / [saves]s / [follows]f
- Worst performer: [hook] — [views]v / [likes]l
- Format that got most saves: [10/5/1-slide]
- Format that got most follows: [10/5/1-slide]
- Any comments worth noting: [paste standout comments]
```

### What Claude does with this:
- Repeats the hook structure of the best performer
- Avoids the angle/format of the worst performer
- Adjusts the day's format mix based on what's converting

---

## Ideas Bank Reference

All unused content ideas are tracked in:
`output/Content/tiktok-ideas-bank.md`

Before generating new ideas, Claude will check this file for unused hooks and mark used ones as ✓.

---

## Files This Workflow Produces

| File | Location | What's in it |
|------|----------|-------------|
| Daily blueprint | `output/Content/tiktok-dayN-blueprint-YYYY-MM-DD.md` | 7 production briefs, captions, audio, metrics log |
| Ideas bank | `output/Content/tiktok-ideas-bank.md` | 20+ hooks with format + angle + audio |

---

## Canva Build Order (Fastest)

1. Open `#0D1117` as master background, Inter Bold loaded
2. Build the CTA slide (Slide 10) first — use as template for all slides
3. Build all 1-slide posts first (10 min each)
4. Build 5-slide posts next (45 min each)
5. Build 10-slide posts last (90 min each) — do in one focused session
6. Export all as PNG, download to phone, post at scheduled times

**Total build time for 7 posts:** ~5–6 hours if building all same day.
**Shortcut:** Build 1-sliders and 5-sliders first. Post those. Build 10-sliders while earlier posts are live.
