# Design Spec — Full-Stack Founder Tools Carousel

**Date:** 2026-05-16
**Output:** `output/Carousels/2026-05-16/11-slide-full-stack-founder-tools.html`
**Notion destination:** `notion-personal` → YOOBIN Content Engine (personal brand content)

---

## Concept

Personal brand Instagram carousel for Yoobin (@yoobinseo) about the tools used to run Bloggo as a solo founder wearing multiple hats: Product Engineer + Marketer.

**Hook:** "Building a startup means wearing every hat. Here are the tools that make it possible."
**Sub-hook:** "Product engineer by day. Marketer by night. These tools live in both worlds."

---

## Structure — 11 Slides

| # | Type | Label | Tool | Key Copy |
|---|------|-------|------|----------|
| 1 | Hook | — | — | "Building a startup means wearing every hat…" |
| 2 | Tool | BUILDER 01 | Claude | "The one running the agency." — Frontend dev, agentic workflows, built the entire marketing team in Claude |
| 3 | Tool | BUILDER 02 | Cursor | "Where the product gets built." — AI-native IDE, reasons about what you're building |
| 4 | Tool | RESEARCHER 01 · MOST SLEPT ON | NotebookLM | "Everyone's sleeping on this." — Drop in docs/videos/articles, get briefings, slide decks, study guides |
| 5 | Tool | RESEARCHER 02 | Gemini | "For what happened this week." — Current information, trends, competitor moves |
| 6 | Tool | CREATOR 01 | Nano Banana Pro | "Image gen that ships." — Fast assets: mockups, social visuals, thumbnails |
| 7 | Tool | CREATOR 02 | Higgsfield | "AI video with actual creative freedom." — More control than Runway, experimental content |
| 8 | Tool | CREATOR 03 | CapCut + Premiere | "The edit suite." — CapCut for speed, Premiere for final production quality |
| 9 | Tool | CREATOR 04 | Canva + Photoshop | "The design layer." — Canva for speed, Photoshop for precision |
| 10 | Insight | — | — | "The hat changes. The standard doesn't." |
| 11 | CTA | — | — | "Which hat is hardest to wear?" / Follow @yoobinseo |

---

## Visual Design

Matches existing Yoobin personal brand carousel system:

- **Background:** `#0D1117`
- **Accent:** `#00FF7F` (neon green)
- **Text:** `#FFFFFF` headlines, `#9CA3AF` body
- **Font:** Inter (Bold headlines, Regular body, Italic descriptions)
- **Slide size:** 360×450px (renders at 3× for 1080×1350 Instagram export)
- **Layout:** Left-aligned `l` layout for tool slides, centered `c` layout for hook/insight/CTA
- **Elements:** Left accent bar, dot grid, radial glow, ghost word background, `@yoobinseo` watermark
- **Hat labels replace tool numbers:** BUILDER 01/02, RESEARCHER 01/02, CREATOR 01–04

---

## Export

- Save All Slides button (ZIP of PNGs via html2canvas + JSZip)
- Per-slide Save PNG button (hover reveal)
