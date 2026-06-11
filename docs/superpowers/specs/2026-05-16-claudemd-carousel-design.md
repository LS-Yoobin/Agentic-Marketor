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
**Headline (quote block):** "My app is called Bloggo. It's iOS only. The brand voice is warm, not corporate. Don't use jargon."
**Quote styling:** Rendered as a styled blockquote — neon green (#00FF7F) left border (3–4px), slight left indent, italic text in #D1D5DB, contained in a rounded dark card (#161B22). Not a code block, not plain body text.
**Subtext (below quote card):** Close the chat. Open a new one. Start over.

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
**Layout:** Left-aligned with accent sidebar bar. Uses the accent sidebar bar decoration.
**List items — styled as neon bullet rows:**
Each item renders as a horizontal row: neon green bullet (•, #00FF7F, bold) on the left, item text in white (#FFFFFF, 16px) beside it. Rows are stacked vertically with 14px gap between them.
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
**Layout:** Left-aligned with accent sidebar bar.
**Steps — styled as large numbered rows:**
Each step: large neon green step number (32px bold, #00FF7F) on the left, step text in white (16px) to the right, stacked vertically with 20px gap. Numbers are visually dominant — they're the anchor for scanning.
1. Create a file called `CLAUDE.md` in your project root
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
- **Font:** Inter — import via `https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,700;1,400&display=swap`. Fallback stack: `'Inter', -apple-system, BlinkMacSystemFont, sans-serif`.
- **Font weights:** 700 bold for headlines, 400 regular for subtext/body, 10px uppercase letter-spaced for labels
- **Layout:** Centered slides (slides 1, 3, 6, 8) — content centered horizontally and vertically. Left-aligned slides (slides 2, 4, 5, 7) — content left-aligned with accent sidebar bar on the left edge.
- **Accent sidebar bar:** 4px wide vertical bar on the left edge of the slide, gradient from transparent at top/bottom to rgba(0,255,127,0.45) in the middle.
- **Dot grid overlay:** `radial-gradient(circle, rgba(0,255,127,0.06) 1px, transparent 1px)` at 28px × 28px, covers full slide, z-index 0.
- **Radial glow:** Centered on slide (top 50%, left 50%), 220×220px circle, `radial-gradient(circle, rgba(0,255,127,0.07), transparent 70%)`. Behind content, z-index 1.
- **Ghost text watermark:** Large (100–110px), ultra-light opacity (rgba(0,255,127,0.04)), bold, positioned bottom-right, slightly rotated (-8deg), behind all content. Text content: "CLAUDE.MD" on slides 1–4; "MEMORY." on slides 5–8.
- **Slide counter:** Format "Slide X of 8" — 9px, #444, uppercase, letter-spacing 2px, displayed above the slide card.
- **Branding:** `@yoobinseo` — bottom-left, 12px, bold, rgba(0,255,127,0.5), z-index 10.
- **Export:** HTML file with "Save All Slides" button using html2canvas + JSZip + FileSaver.js (CDN). Per-slide "Save PNG" button appears on hover.

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
