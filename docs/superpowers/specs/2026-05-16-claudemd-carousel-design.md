# Spec: CLAUDE.md Deep Dive Carousel

**Date:** 2026-05-16
**Type:** Instagram carousel
**Brand:** Yoobin personal brand
**Notion destination:** `notion-personal` → YOOBIN Content Engine
**Slides:** 8
**Format:** 1080×1350 (portrait), neon green (#00FF7F) on dark (#0D1117), Inter font

---

## Purpose

A personal brand carousel teaching builders how CLAUDE.md works — framed as a founder's discovery story. Targets people who already use Claude but don't know this feature exists. Part of a broader "how I use Claude" content series.

## Angle

"I gave Claude a permanent memory and it changed how I work."
Outcome-first hook → personal frustration → discovery → explanation → payoff → CTA.

## Narrative Arc — Slide by Slide

### Slide 1 — Hook
**Label:** CLAUDE CODE · FOUNDER TIP
**Headline:** "I was re-explaining myself to Claude every single session."
**Subtext:** Every new chat. Same context. From scratch.

### Slide 2 — The frustration (concrete)
**Label:** THE PROBLEM
**Headline:** "My app is called Bloggo. It's iOS only. The brand voice is warm, not corporate. Don't use jargon."
**Subtext:** Close the chat. Open a new one. Start over.

### Slide 3 — The discovery
**Label:** THE TURNING POINT
**Headline:** "Then I found something called CLAUDE.md."
**Subtext:** Most Claude users have never heard of it.

### Slide 4 — What it actually is
**Label:** WHAT IT IS
**Headline:** "A file you put in your project folder that Claude reads automatically every time you open it."
**Subtext:** It's a permanent briefing note. It never forgets.

### Slide 5 — What I put in mine
**Label:** WHAT'S IN MINE
**List items (styled as bullet points):**
- What Bloggo is and who it's for
- My brand voice rules (what to say, what to avoid)
- Output format preferences
- Things Claude should never do

### Slide 6 — What changed
**Label:** THE RESULT
**Headline:** "Now Claude already knows my product, my tone, my rules."
**Subtext:** I haven't re-explained Bloggo in weeks.

### Slide 7 — How to set it up
**Label:** HOW TO DO IT
**Steps (numbered list):**
1. Create a file called `CLAUDE.md` in your project
2. Write what you want Claude to always know
3. That's it.

### Slide 8 — CTA
**Label:** SAVE THIS
**Headline:** "Save this if you use Claude daily."
**Subtext:** What would you put in yours? Drop it below.

---

## Visual Design

- **Background:** #0D1117 (dark navy)
- **Accent color:** #00FF7F (neon green)
- **Font:** Inter (700 bold for headlines, 400 for subtext)
- **Layout:** Mix of centered slides (hook, discovery, CTA) and left-aligned with accent bar (explanation, list slides)
- **Decorative elements:** dot grid overlay, radial glow, large ghost text watermark, accent sidebar bar
- **Branding:** `@yoobinseo` bottom-left on every slide
- **Slide counter:** small label above each slide (e.g. "Slide 1 of 8")
- **Export:** HTML file with "Save All Slides" button (html2canvas + JSZip)

## Content Series Context

This is **Deck 1** of a planned "How I use Claude" series. Future decks include:
- Context & steering
- Superpowers / Skills plugin
- My actual Claude workflow as a founder
- Mistakes I made with Claude
- 5 prompts I use every single day

## Success Criteria

- Hook slide communicates the pain point immediately without needing to read further
- Slide 4 explains CLAUDE.md in plain English — no jargon, no setup context required
- Slide 7 is actionable enough that someone could act on it immediately
- CTA invites comments (algorithm signal) and saves (utility signal)
