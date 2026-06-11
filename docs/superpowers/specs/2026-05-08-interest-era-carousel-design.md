# Design Spec: "Perfection is Killing Your Growth" Carousel

**Date:** 2026-05-08
**Type:** Instagram Carousel — Yoobin Personal Brand
**Notion destination:** `notion-personal` → YOOBIN Content Engine

---

## Overview

A 6-slide personal brand carousel summarizing insights from a meeting with a content creator who's been in the game for a decade. Theme: stop chasing perfection, start building real resonance.

---

## Caption

"Perfection is killing your growth."

Today I met with a content creator who's been in the game for a decade…

and the biggest thing I learned wasn't about the algorithm.

It was this: Be unapologetically yourself.

Because the moment you stop copying everyone else… you actually start evolving into who you're meant to become.

[full caption as provided by user]

---

## Visual System

- **Background:** `#0D1117`
- **Accent:** `#00FF7F` (neon green)
- **Text:** `#FFFFFF` (headlines), `#9CA3AF` (body/italic)
- **Font:** Inter (700 bold headlines, 400 italic body)
- **Decorative elements:** dot grid, radial glow, left accent bar, ghost word in background
- **Watermark:** `@yoobinseo` bottom-left
- **Dimensions:** 360×450px (1080×1350 export ratio)
- **Format:** HTML with html2canvas + JSZip Save All Slides

---

## Slide Layout: "The Move / Why It Works"

Each content slide uses a two-part stacked layout:
- **Top half:** `THE MOVE` label + bold white headline
- **Divider:** `rgba(0,255,127,0.25)` horizontal rule
- **Bottom half:** `WHY IT WORKS` label + italic gray supporting copy

---

## Slide Plan

### Slide 1 — Hook
- **Layout:** Centered (`.c` class). Left accent bar. Dot grid. Radial glow centered.
- **Ghost word:** "PERFECT." — oversized, rotated ~-8deg, `rgba(0,255,127,0.04)`, bottom-right quadrant
- **Tag line (small, top):** "CONTENT STRATEGY · REAL TALK" — 10px, #00FF7F, uppercase
- **Headline:** "Perfection is killing your growth." — 34px bold white
- **Divider:** 44px green rule
- **Context line:** "I sat down with a content creator who's been in the game for a decade. This is what I actually learned." — 16px italic #9CA3AF
- **Watermark:** `@yoobinseo` bottom-left

Content slides 2–5 all use the `.l` left-aligned layout with left accent bar, dot grid, and radial glow. Ghost words per slide listed below. No ghost word on Slide 6.

### Slide 2 — Identity
**Points covered:** Be unapologetically yourself · Tie business to a niche naturally
- **Ghost word:** "YOU." — `rgba(0,255,127,0.04)`, bottom-right
- **THE MOVE:** Stop copying everyone else.
- **WHY IT WORKS:** The moment you stop copying, you start evolving into who you're meant to become. Tie your business to a niche that resonates naturally — don't force it.

### Slide 3 — Content
**Points covered:** Consistency + Analytics never lie · Verbage / Wordplay
- **Ghost word:** "DATA." — `rgba(0,255,127,0.04)`, bottom-right
- **THE MOVE:** Let the data talk. Let the words land.
- **WHY IT WORKS:** Consistency builds the foundation. Analytics tell you what's actually working. Wordplay is what makes people stop scrolling.

### Slide 4 — Platform
**Points covered:** Show up every day · Leverage Trial Reels
- **Ghost word:** "DAILY." — `rgba(0,255,127,0.04)`, bottom-right
- **THE MOVE:** Show up every day. Use Trial Reels.
- **WHY IT WORKS:** TikTok rewards volume. Instagram rewards precision. Trial Reels let you test reach without risking your existing audience.

### Slide 5 — Growth
**Points covered:** Network as often as you can · Just ask + offer your services · Cold outreach
- **Ghost word:** "ASK." — `rgba(0,255,127,0.04)`, bottom-right
- **THE MOVE:** Network. Reach out. Just ask.
- **WHY IT WORKS:** The DM you don't send is the collab that never happens. Cold outreach isn't cringe — it's confidence. Grow as often as you can.

### Slide 6 — CTA
- **Layout:** Centered (`.c` class). Dot grid. Radial glow. No ghost word. No left accent bar.
- **Headline:** "We're not in the social media era anymore." — 26px bold white
- **Divider:** 44px green rule
- **Body:** "We're in the interest media era. People follow people they genuinely resonate with." — 16px italic #9CA3AF
- **CTA line:** "Follow @yoobinseo" — 18px bold #00FF7F, neon glow text-shadow
- **Watermark:** `@yoobinseo` bottom-left (standard position, distinct from CTA line above)

---

## Full Caption

"Perfection is killing your growth."

Today I met with a content creator who's been in the game for a decade…

and the biggest thing I learned wasn't about the algorithm.

It was this:

Be unapologetically yourself.

Because the moment you stop copying everyone else…

you actually start evolving into who you're meant to become.

We also talked content strategy.

Post.
Analyze.
Learn.
Adapt.

TikTok rewards volume.
Instagram rewards precision.

Trial reels matter.
Wordplay matters.
Networking matters.

But none of it works long term if the person behind the content isn't real.

We're not in the social media era anymore.

We're in the interest media era.

People follow people they genuinely resonate with.

That's the game now.

---

## Output

- File: `output/Carousels/2026-05-08/6-slide-perfection-killing-growth.html`
- Includes per-slide Save PNG buttons and Save All Slides batch download
