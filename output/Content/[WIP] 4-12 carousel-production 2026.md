# Carousel Production Brief — April 12, 2026
**Status: Ready to Build**
**Tool: Canva (recommended) or Figma**
**Dimensions: 1080 x 1080px (square) or 1080 x 1350px (portrait — more feed real estate)**

---

## Mascot Swipe Indicator — Cat Paw (Apply to All 3 Carousels)

Replace all generic arrows with the black cat paw pointing right.

**File:** `C:\Users\yoobi\OneDrive\Desktop\First Episod\Cat related graphics PNG\Black cat paw pointing right 1.png`

| Placement | Position | Size | Applies To |
|-----------|----------|------|------------|
| Bottom right corner | 40px from right edge, 40px from bottom | ~80px wide | Slides 1–9 of every carousel |
| Omit on Slide 10 | No paw on the CTA slide — nothing to swipe to | — | Slide 10 only |

**Style note:** The paw has a dark/transparent background — it blends naturally on the navy carousel background. Drop it in Canva as-is, no edits needed.

---

## Brand Specs (Apply to All 3 Carousels)

| Element | Value |
|---------|-------|
| Background | Deep navy — `#0D1117` |
| Primary text | White — `#FFFFFF` |
| Accent color | Warm gold — `#C9A84C` (use sparingly — numbers, highlights) |
| Font — headlines | Inter Bold or DM Sans Bold |
| Font — body | Inter Regular or DM Sans Regular |
| Max words per slide | 10 |
| Padding | 60px all sides minimum |
| Logo placement | Bottom right, every slide, small — 40px height |

---

## Mascot Character — Higgsfield Nano Banana Pro Prompt Format

All mascot images are generated in **Higgsfield Nano Banana Pro**.
Every prompt follows this exact structure for character consistency.

### Base Character DNA (include in every prompt)
```
@Spunky-Cat — keep the necklace and pendant around the cat's neck exactly
consistent with the Spunky-Cat element. Same style throughout.

black cartoon cat character, chunky round body, large expressive eyes,
short pointy ears, small white claw tips, slightly mischievous personality,
necklace with pendant around neck matching @Spunky-Cat exactly,
clean 2D cartoon illustration style, thick black outlines, subtle shading,
no background (transparent), isolated character, full body visible,
consistent character design, high quality, sharp edges
```

### Full Prompt Template
```
@Spunky-Cat — keep the necklace and pendant around the cat's neck exactly
consistent with the Spunky-Cat element. Same style throughout.

[BASE CHARACTER DNA]
[POSE — what the body is doing]
[EXPRESSION — what the face/eyes show]
[CAMERA — angle and framing]
[LIGHTING — how light hits the character]
[STYLE MODIFIERS — art direction]
[NEGATIVE PROMPT — what to exclude]
```

### Negative Prompt (use on every generation)
```
negative: realistic, photorealistic, blurry, background, shadow drop,
gradient background, white background, gray background, extra limbs,
deformed, ugly, low quality, watermark, text, logo
```

---

## What You Need to Provide

| Asset | Used In | Notes |
|-------|---------|-------|
| Bloggo app screenshot — trip blog view | Bloggo C#2 Slide 9, PB C#1 Slide 2 | Full screen iPhone screenshot, trip timeline visible |
| Photo of yourself (founder) | PB Carousel Slide 2 | Candid or semi-candid, not formal headshot |
| Bloggo logo PNG (transparent bg) | Every slide, bottom right corner | Export from Xcode assets or design file |

---

# CAROUSEL 1 — Bloggo Company Page
## "Your photos never leave your phone." (Privacy)

---

### Slide 1 — Hook
**Copy:** "Your photos never leave your phone."
**Layout:** Full bleed dark background. Single headline, centered, large.
**Visual:** Subtle bokeh/blur of a phone screen in the background — dark, barely visible.
**Source:** Search Unsplash → "smartphone dark background bokeh"
**Recommended photo:** [unsplash.com](https://unsplash.com) search: `phone dark minimal`
**Typography:** White, 52px bold, centered. Line break after "never leave"
**Accent:** Gold underline under "never leave your phone"

---

### Slide 2 — Transition: The Old Way
**Copy:** "Most AI apps work like this:
You upload photos → server → AI → result."
**Layout:** Left-aligned text. Right side: simple icon flow diagram.
**Visual:** Three icons in a horizontal row connected by arrows:
  - 📱 Phone icon → ☁️ Cloud icon → ⚙️ Gear icon
**Source:** Free icons from [icons8.com](https://icons8.com) — search "phone", "cloud upload", "ai"
  OR use Canva's built-in icon library (search same terms)
**Color:** Icons in muted grey (#555). Arrow in gold (#C9A84C).
**Typography:** Left side, white, 28px regular

---

### Slide 3 — The Problem
**Copy:** "Your locations. Your faces.
Your private moments.
On someone else's server."
**Layout:** Centered text. Full dark background.
**Visual:** Very subtle red tint overlay on background — low opacity (10%) to signal danger/wrongness
**No stock photo needed — pure typography slide**
**Typography:** 36px regular. "On someone else's server." in gold to create emphasis.

---

### Slide 4 — The Turn
**Copy:** "Bloggo works differently."
**Layout:** Centered. Minimal. Single line.
**Visual:** Thin gold horizontal line above and below the text. Nothing else.
**Effect:** This slide is intentionally sparse — the contrast creates impact
**Typography:** 48px bold. White. Centered.

---

### Slide 5 — The Solution
**Copy:** "Our AI runs entirely on your device.
On your phone. Offline."
**Layout:** Left-aligned text. Right side: phone mockup image.
**Visual:** Clean iPhone mockup — dark/minimal style
**Source:** Free mockup from [mockuphone.com](https://mockuphone.com) or search Canva → "iPhone mockup dark"
**No app screenshot needed — mockup can be blank/blurred**
**Typography:** 32px bold, left-aligned

---

### Slide 6 — Proof
**Copy:** "Never uploaded.
Never stored remotely.
Never seen by anyone but you."
**Layout:** Three lines, stacked, centered. Each line appears as its own visual beat.
**Visual:** Small checkmark icon (✓) in gold before each line
**Source:** Canva built-in icons or [flaticon.com](https://flaticon.com) → "checkmark minimal"
**Typography:** 34px regular. "Never" in gold on each line.

---

### Slide 7 — The Payoff
**Copy:** "You still get a beautiful,
AI-written travel blog."
**Layout:** Text left side. Right side: [BLOGGO APP SCREENSHOT]
**Visual:** ⚠️ NEED FROM YOU — Bloggo app screenshot showing a generated trip blog
**Frame it:** iPhone mockup frame around the screenshot (use Canva's device frame feature)
**Typography:** 32px bold, left-aligned, white

---

### Slide 8 — Emphasis
**Copy:** "In seconds.
Without the tradeoff."
**Layout:** Full centered. Large text. Minimal.
**Visual:** Dark background only. No image.
**Typography:** "In seconds." — 52px bold, white. "Without the tradeoff." — 32px regular, gold.

---

### Slide 9 — The Statement
**Copy:** "Privacy isn't a setting in Bloggo.
It's how the whole thing works."
**Layout:** Centered text. Subtle texture in background.
**Visual:** Dark linen or dark grain texture overlay — very subtle, low opacity
**Source:** Canva → "dark texture background" or [subtlepatterns.com](https://www.transparenttextures.com)
**Typography:** 30px regular, white, centered. Last sentence in gold.

---

### Slide 10 — CTA
**Copy:** "Join the Bloggo beta"
**Subtext:** "Link in bio"
**Layout:** Logo top center. Text center. Mascot bottom left.
**Visual:** [BLOGGO LOGO] — top center, 120px height
**Background:** Pure `#0D1117` — no texture, clean
**Typography:** "Join the Bloggo beta" — 36px bold, white. "Link in bio" — 20px regular, gold.

🐱 **MASCOT — Higgsfield Nano Banana Pro Prompt (C1 Slide 10):**
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
**Placement:** Bottom left corner — 40px from left, 40px from bottom. ~25% slide height.

---

# CAROUSEL 2 — Bloggo Company Page
## "5 travel memories you've already lost." (The Problem)

---

### Slide 1 — Hook
**Copy:** "5 travel memories you've already lost."
**Layout:** Full bleed travel photo background with dark gradient overlay (60% opacity)
**Visual:** Beautiful but slightly moody travel landscape — empty street, golden hour
**Source:** Unsplash → search `travel golden hour empty street` or `solo travel moody`
**Recommended:** [unsplash.com/photos](https://unsplash.com) — look for warm tones, wide shot, minimal people
**Typography:** White, 44px bold, centered, bottom third of slide

🐱 **MASCOT — Higgsfield Nano Banana Pro Prompt (C2 Slide 1):**
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
pupils dilated, eyebrows raised high in exaggerated surprise and curiosity,
ears perked forward, peering expression like caught eavesdropping,
low angle framing looking slightly upward at the face, tight crop on
the top of the head, soft flat lighting, no harsh shadows,
vector cartoon style, clean cel-shaded look

negative: realistic, photorealistic, blurry, background, shadow drop,
gradient background, white background, gray background, full body,
extra limbs, deformed, ugly, low quality, watermark, text, logo
```
**Placement:** Bottom left corner — head peeking up from the very bottom edge. Crop the image so only the top of the head is visible above the slide boundary.

---

### Slide 2 — Transition
**Copy:** "Not the photos.
The story behind them."
**Layout:** Dark background. No image. Pure text impact.
**Visual:** None — the contrast from Slide 1's photo to this blank slide IS the visual effect
**Typography:** "Not the photos." — 36px regular, muted grey (#AAAAAA). "The story behind them." — 44px bold, white.

---

### Slide 3 — Memory #1
**Copy:** "#1 — The restaurant name.
You remember the food.
You can't remember where it was."
**Layout:** Left-aligned text. Right: blurred restaurant photo, dark overlay.
**Visual:** Moody restaurant interior — warm light, bokeh
**Source:** Unsplash → `restaurant warm bokeh interior dark`
**Typography:** "#1 —" in gold, 24px. Rest in white, 28px regular.

---

### Slide 4 — Memory #2
**Copy:** "#2 — The day it happened.
Was that Tuesday in Rome or Thursday?
Your camera roll doesn't say."
**Layout:** Left-aligned text. Right: blurred calendar or city photo.
**Visual:** Aerial city shot, slightly blurred — Rome, Paris, any European city
**Source:** Unsplash → `Rome aerial blurred` or `European city aerial`
**Typography:** "#2 —" in gold. Rest white, 26px regular.

---

### Slide 5 — Memory #3
**Copy:** "#3 — The caption you meant to write.
You were going to do it later.
Later never came."
**Layout:** Centered text. Background: faint image of a blank open journal/notebook.
**Visual:** Open blank notebook, dark moody light — minimal, melancholic
**Source:** Unsplash → `open blank notebook dark moody`
**Typography:** "#3 —" in gold. "Later never came." — italic, slightly smaller, fades out

---

### Slide 6 — Memory #4
**Copy:** "#4 — Who else was there.
A face in the background.
A stranger who became a story."
**Layout:** Left text. Right: blurred photo of people at a distance — backs turned, candid.
**Visual:** Candid travel moment, people from behind, golden light
**Source:** Unsplash → `travel candid people golden hour backs`
**Typography:** "#4 —" in gold. Rest white, 26px.

---

### Slide 7 — Memory #5
**Copy:** "#5 — Why you took that photo.
The feeling. The reason.
Fading with every month that passes."
**Layout:** Full bleed photo background, heavy dark overlay.
**Visual:** Beautiful travel moment — sunset, ocean, mountain — something emotionally resonant
**Source:** Unsplash → `travel sunset emotional wide` or `mountain golden hour cinematic`
**Typography:** White centered, 28px. "Fading with every month that passes." — slightly smaller, faded opacity (70%)

---

### Slide 8 — The Insight (Aha Moment)
**Copy:** "Photos preserve the moment.
They don't preserve the meaning."
**Layout:** Full dark background. No image. Large centered text.
**Visual:** None — pure typography. This is the save-worthy slide.
**Typography:** "Photos preserve the moment." — 32px regular, muted white (#CCCCCC). "They don't preserve the meaning." — 40px bold, white.

🐱 **MASCOT — Higgsfield Nano Banana Pro Prompt (C2 Slide 8):**
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
slightly to the left, eyes looking upward to the left as if deep in
thought, brow slightly furrowed in contemplation, mouth closed in
a neutral-to-thoughtful expression, slight squint in eyes conveying
concentration, three-quarter front angle showing face and pose clearly,
soft flat lighting from front-left, no harsh shadows, vector cartoon
style, clean cel-shaded look

negative: realistic, photorealistic, blurry, background, shadow drop,
gradient background, white background, gray background, extra limbs,
deformed, ugly, low quality, watermark, text, logo
```
**Placement:** Bottom right corner — 40px from right, 40px from bottom. ~20% slide height.

---

### Slide 9 — The Solution
**Copy:** "Bloggo writes the story
while the memory is still fresh."
**Layout:** Left text. Right: [BLOGGO APP SCREENSHOT]
**Visual:** ⚠️ NEED FROM YOU — Bloggo screenshot showing a trip narrative/blog
**Frame:** iPhone device frame (Canva → Elements → "iPhone frame")
**Typography:** 32px bold, white, left-aligned.

---

### Slide 10 — CTA
**Copy:** "Join the Bloggo beta"
**Subtext:** "Link in bio"
**Layout:** Logo top center. Text center. Mascot bottom left.
**Visual:** [BLOGGO LOGO] top center, 120px height
**Background:** `#0D1117` — clean, no texture
**Typography:** 36px bold, white. "Link in bio" — 20px, gold.

🐱 **MASCOT — Higgsfield Nano Banana Pro Prompt (C2 Slide 10):**
```
Reuse the exact same image generated for C1 Slide 10.
Same pose, same expression, same placement.
```
**Placement:** Bottom left corner — 40px from left, 40px from bottom. ~25% slide height.

---

# CAROUSEL 3 — Personal Brand Page
## "5 things I learned building an AI-powered iOS app." (Product Builder)

---

### Slide 1 — Hook
**Copy:** "5 things I learned building
an AI-powered iOS app."
**Layout:** Dark background. Bold centered text. Top: small label "FOUNDER LESSONS"
**Visual:** Subtle code/terminal texture in the far background — barely visible, 8% opacity
**Source:** Unsplash → `code dark terminal background` or `developer dark screen`
**Label style:** "FOUNDER LESSONS" — 14px, letter-spaced, gold, above headline
**Typography:** 44px bold, white, centered.

---

### Slide 2 — Credibility
**Copy:** "I'm the co-founder of Bloggo — an app that
turns your travel photos into a blog using
on-device AI. Here's what building it taught me."
**Layout:** Left: [YOUR PHOTO] — cropped to circle or square, left column. Right: text.
**Visual:** ⚠️ NEED FROM YOU — a candid or semi-candid photo of yourself
**Photo style:** Not a headshot. Think: working at a desk, on your phone, at a café.
  Dark or natural light preferred to match brand.
**Secondary:** Below photo, small Bloggo logo + "@bloggo.app" or handle
**Typography:** 22px regular, white, right-aligned to photo.

---

### Slide 3 — Lesson #1
**Copy:** "#1 — On-device AI is 10x harder
than cloud AI.
And 10x more worth it."
**Layout:** Left-aligned. Clean dark background. Gold "#1 —" accent.
**Visual:** Minimal abstract: small phone icon (on-device) vs cloud icon with X through it
**Source:** [icons8.com](https://icons8.com) → "smartphone" + "cloud off" — white icons, small, decorative only
**Typography:** "#1 —" gold, 28px. Body white, 30px bold.

---

### Slide 4 — Lesson #2
**Copy:** "#2 — The feature users love most
is never the feature you spent
the most time on."
**Layout:** Centered text. Background: subtle abstract gradient — dark navy to dark teal
**Visual:** No photo needed — gradient background is the visual
**Canva:** Use gradient background tool — `#0D1117` to `#0D2233`
**Typography:** "#2 —" gold. Body white, 28px regular. Last line slightly smaller.

---

### Slide 5 — Lesson #3
**Copy:** "#3 — Submitting to the App Store
doesn't mean you're done.
It means the waiting begins."
**Layout:** Centered text. Background: faint App Store Connect screenshot — blurred heavily.
**Visual:** Screenshot of App Store Connect "Waiting for Review" status — your own screen
**Apply:** 80% dark overlay so it's barely visible — serves as texture, not readable
**⚠️ OPTIONAL from you:** A blurred screenshot of your App Store Connect screen
**OR use:** Dark background only if you prefer privacy
**Typography:** "#3 —" gold. "It means the waiting begins." — italic, white.

---

### Slide 6 — Lesson #4
**Copy:** "#4 — Your first 10 users will tell you more
than 10,000 survey responses."
**Layout:** Left-aligned. Dark. Minimal.
**Visual:** Small icon: two speech bubbles (representing real user conversation)
**Source:** Canva icon library → "speech bubble minimal" — white, small, decorative
**Typography:** "#4 —" gold, 28px. Body white, 30px regular.

---

### Slide 7 — Lesson #5
**Copy:** "#5 — You will rewrite the thing
you're most proud of. Twice.
That's how you know it's getting better."
**Layout:** Centered. Dark teal gradient background (same as Slide 4).
**Visual:** None — typography only
**Typography:** "#5 —" gold. "That's how you know it's getting better." — larger, bold, white.

---

### Slide 8 — Buildup
**Copy:** "None of this was in any book I read."
**Layout:** Centered. Single line. Full dark background.
**Visual:** None — pure text, intentionally sparse
**Typography:** 38px regular, muted white (#CCCCCC), centered. Italic.

---

### Slide 9 — Payoff
**Copy:** "All of it was in the build."
**Layout:** Centered. Single line. Full dark background.
**Visual:** None — pure text. Contrast with Slide 8 creates the emotional beat.
**Typography:** 48px bold, WHITE, centered. Full brightness — maximum contrast with Slide 8.

---

### Slide 10 — CTA
**Copy:** "Follow for more of the journey —
we're just getting started."
**Layout:** Text center. Your photo (small circle, top) or Bloggo logo. Mascot bottom left.
**Visual:** ⚠️ NEED FROM YOU — small circular crop of your photo (same as Slide 2)
**OR:** Bloggo logo if you prefer brand-forward close
**Typography:** 28px regular, white. "we're just getting started." — gold.

---

## Summary: What You Need to Provide

| # | Asset | Used In | Format |
|---|-------|---------|--------|
| 1 | Bloggo app screenshot — trip blog/timeline view | Bloggo C#2 Slide 9, PB C#1 Slide 2 | iPhone screenshot, portrait |
| 2 | Photo of yourself (candid/working) | PB Carousel Slides 2 + 10 | Any — crop to square in Canva |
| 3 | Bloggo logo (transparent PNG) | Every Slide 10 + PB Slide 2 | ✅ FOUND: `C:\Users\yoobi\Downloads\Blogo.png` — transparent background, drop directly into Canva |
| 4 | App Store Connect screenshot (optional) | PB Carousel Slide 5 | Will be blurred — privacy safe |

---

---

## Instagram Captions — Post-Ready Copy

> Copy-paste these directly when scheduling. Hashtags go at the bottom as written.
> Caption strategy: hook in line 1 (matches Slide 1), body that earns the save, single CTA, hashtag block.

---

### Caption — Carousel 1 (Bloggo Company Page — Privacy)
**Post with:** Slide 1 as cover image

```
Your travel photos never leave your phone.

Most AI apps upload your photos to a server to process them.
Your locations. Your faces. Your private moments — on someone else's computer.

Bloggo works differently.

Our AI runs entirely on your device. Offline. No cloud. No uploads. Ever.

You still get a beautiful, AI-written travel blog in seconds.
Just without the tradeoff.

Swipe to see how it works →

Join the Bloggo beta — link in bio.

#travelblog #privacyAI #ondeviceAI #travelphotos #AIprivacy #travelmemories #bloggo #travelapp #traveltech #iphoneapp
```

---

### Caption — Carousel 2 (Bloggo Company Page — The Problem)
**Post with:** Slide 1 as cover image

```
5 travel memories you've already lost.

Not the photos. The story behind them.

The restaurant name you can't remember.
The day it happened.
The caption you were going to write later.
The face in the background.
The reason you took that photo at all.

Photos preserve the moment.
They don't preserve the meaning.

Bloggo writes the story while the memory is still fresh — before the details fade.

Swipe to see which memory hits hardest →

Join the Bloggo beta — link in bio.

#travelmemories #travelblog #travelphotos #travelstories #traveldiary #bloggo #AItravel #travelapp #tripblog #traveljournaling
```

---

### Caption — Carousel 3 (Personal Brand — Founder Lessons)
**Post with:** Slide 1 as cover image
**Voice:** Founder first-person

```
5 things I learned building an AI-powered iOS app.

No startup book prepared me for any of this.

I'm the co-founder of Bloggo — an app that turns your travel photos into a full blog using on-device AI. Here's what building it actually taught me.

(Save this if you're building something right now.)

Swipe for all 5 →

Follow for more of the journey — we're just getting started.

#buildinpublic #indiedev #startupfounder #iOSdev #AIapp #productbuilder #appstore #startuplife #bloggo #techfounder
```

---

## Free Graphic Resources

| Resource | Best For |
|----------|----------|
| [unsplash.com](https://unsplash.com) | All travel photography — free, high-res |
| [pexels.com](https://pexels.com) | Travel + lifestyle photography backup |
| [icons8.com](https://icons8.com) | Icons (phone, cloud, AI, checkmark) |
| [canva.com](https://canva.com) | Design tool — has all icons, mockups, frames built in |
| [mockuphone.com](https://mockuphone.com) | Free iPhone mockup frames |
| [flaticon.com](https://flaticon.com) | Minimal icon sets |
| [transparenttextures.com](https://www.transparenttextures.com) | Subtle dark background textures |

---

## Canva Build Order (Fastest Path)

1. Create one master template in Canva: `1080x1080`, `#0D1117` background, Inter Bold font loaded
2. Build Slide 10 (CTA) first — use it as the base template for all other slides
3. Build Carousel 1 (privacy — all typography, no photos needed until Slide 7)
4. Build Carousel 2 (travel photos — download Unsplash images first, then drop in)
5. Build Carousel 3 (personal brand — add your photo last)
6. Export all as PNG, 300dpi

Once you have your Bloggo app screenshot and your photo, Slides 7/9 of C#2 and Slides 2/10 of C#3 are the only ones waiting on you.
