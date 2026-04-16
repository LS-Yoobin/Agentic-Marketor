# Bloggo Instagram Carousel Generator

> Run this workflow every morning at 5:00 AM to generate a fresh batch of ready-to-screenshot carousels.
> Output is saved to `output/Carousels/[YYYY-MM-DD]/`

---

## Reference Files — Read These First, Every Run

Before generating any content, read all of the following:

| File | Purpose |
|------|---------|
| `@docs/marketing/bloggo-product-context.md` | What Bloggo is, features, differentiators, personas |
| `@docs/marketing/bloggo-brand.md` | Voice, tone, writing rules, what NOT to say |
| `@docs/marketing/Instagram Carousel Cheat Sheet.md` | Hook types, slide formula, viral structure |
| `@docs/marketing/Carasoul.md` | Visual styling blueprint — fonts, colors, layout rules |
| `@docs/marketing/Idea Inbox.md` | Topic ideas backlog to pull from |

Do not write a single word of copy before reading `bloggo-brand.md`. Tone violations make the content unusable.

---

## Task

Generate **4 carousels** per run:
- 1 × **1-slide post** — single powerful statement, high shareability
- 1 × **3–5 slide post** — quick punchy series, relatable moment
- 2 × **8–10 slide post** — deep authority builders, save-worthy (different hook angles)

Build each carousel as a **self-contained HTML file** following the styling blueprint in `Carasoul.md`.

Save all files to: `output/Carousels/[TODAY'S DATE]/`

---

## Daily Topic Rotation

Rotate through these angles across the week:

| Day | Angle |
|-----|-------|
| Monday | Pain point — memory loss, photo backlog guilt |
| Tuesday | Product education — how Bloggo works, what it detects |
| Wednesday | Founder/builder story — personal journey |
| Thursday | Relatable moment — "6 months later", blank page anxiety |
| Friday | Counterintuitive / WTF hook — challenges assumptions |
| Saturday | Privacy differentiator — on-device AI, photos never leave |
| Sunday | Aspirational — the trip that deserved a story |

If today's angle doesn't feel fresh, check `docs/marketing/Idea Inbox.md` for alternatives.

---

## Carousel Structure Formula

Follow this formula from `Instagram Carousel Cheat Sheet.md` exactly:

```
Slide 1   →  HOOK        Stop the scroll. 3–8 words. Curiosity or tension.
Slide 2   →  TRANSITION  Why should they keep swiping? One sentence.
Slides 3–8 → CONTENT     Reveal one idea per slide. Never dump everything at once.
Slide 9   →  INSIGHT     The save-worthy moment. The reframe. The aha.
Slide 10  →  CTA         One action only.
```

For **3–5 slide posts**, compress: Hook → Transition → 1–2 content slides → Insight/CTA.
For **1-slide posts**: Hook only. CTA lives in the caption.
For **2 × 8–10 slide posts**: use two different hook types from the table below — e.g., one Fear/WTF and one Story or Contrarian. Do not repeat the same angle.

---

## Copy Rules

Pull these from `bloggo-brand.md` — they are non-negotiable:

- Max **10 words per slide**
- **Active voice** — "Bloggo creates" not "blogs are created"
- Lead with **benefit**, not feature
- Bold **1–3 emotional keywords** per content slide
- **No exclamation points** except on CTA slide
- **Never mention cloud features** — V1 is on-device only
- **"Bloggo" is always capitalized**
- No jargon: no "leverage", "seamless", "powerful", "utilize"

---

## HTML Build Rules

Follow `docs/marketing/Carasoul.md` exactly:

| Element | Rule |
|---------|------|
| Background | `#FFFFFF` every slide, no exceptions |
| Accent color | `#138EFF` |
| Slide 1 font | See Hook Slide Typography section below |
| Slides 2–9 font | Jost (closest available substitute for Glacial Indifference) |
| Slide 10 font | Chewy |
| Gradient text | Slide 2 only — `#138EFF → #3BBAFF → #6DD5FA → #59E0C5` |
| Content slides | Left-aligned with blue accent bar (slides 3–8) |
| Bloggo watermark | Bottom-left, slides 2–9 only |
| Cat paw | Bottom-right, slides 2–9 only — `<img class="pw" src="../../../docs/Assets/Black%20cat%20paw%20pointing%20right%201.png" alt="">` |
| App icon (CTA slide) | Use the real logo PNG — `<img src="../../../docs/Assets/Frame%20427320199Bloggo%20Rounded%20Corners%20logo.png" alt="Bloggo" style="width:52px;height:52px;object-fit:contain;">` — **never use the gradient+emoji placeholder** |
| Mascot placeholder | **Do NOT** use `.mp` dashed placeholder boxes inside slides. Graphics are described in `.gfx-note` blocks only. |
| Graphics notes | **Do NOT** place graphic descriptions inside the slide. Instead, add a `.gfx-note` div INSIDE the `.sw` wrapper, AFTER the `.slide` closing tag. See format below. |

Slide preview size for screenshotting: **360 × 450px** (maintains 4:5 ratio).

### Cat Paw CSS

```css
.pw{position:absolute;bottom:8px;right:10px;width:36px;height:auto;z-index:10;opacity:0.9}
```

---

## Hook Slide Typography

The hook slide (Slide 1) text often wraps badly at large Chewy sizes inside the 360px-wide slide (effective text width ~280px). Follow this pattern:

**Rule:** Use Jost italic for long setup phrases. Reserve short Chewy for the 1–3 hero words.

| Font | Use for | Size |
|------|---------|------|
| Jost italic, `#6B7280` | Long setup phrases (10+ chars) | 18–20px |
| Chewy, `#1A1A1A` | Supporting short words ("is a", "It's the") | 36–52px |
| Chewy, `#138EFF` | The hero word(s) — 1–3 words max | 52–72px |

**Safe Chewy character limits per line:**
- 72px → max ~8 chars
- 52px → max ~12 chars
- 46px → max ~16 chars

**Example hook structure:**
```html
<div style="font-family:'Jost',sans-serif;font-style:italic;font-size:20px;color:#6B7280;line-height:1.4;">Your camera roll</div>
<div style="font-family:'Chewy',cursive;font-size:38px;color:#1A1A1A;line-height:1.1;margin-top:6px;">is a</div>
<div style="font-family:'Chewy',cursive;font-size:72px;color:#138EFF;line-height:0.9;">graveyard</div>
<div style="font-family:'Jost',sans-serif;font-style:italic;font-size:18px;color:#6B7280;line-height:1.4;margin-top:10px;">of stories you'll never tell.</div>
```

---

## 1-Slide Post Visual Template

1-slide posts must NOT be text-only. Every 1-slider requires these elements:

| Element | CSS class | Description |
|---------|-----------|-------------|
| Top gradient bar | `.tb` | 5px bar across the top, `#138EFF → #59E0C5` |
| Ghost quote mark | `.dq` | `"` character, 220px, `opacity:0.04`, centered bg decoration |
| Subtitle tagline | `.st` | Jost italic, 15px, `#9CA3AF`, below the main quote |
| CTA badge | `.cb` | Blue outlined pill, Jost 700, `#138EFF`, "BETA IN BIO" or similar |
| Bloggo watermark | `.bm` | Bottom-left, Chewy, `rgba(19,142,255,0.6)` |
| Cat paw | `.pw` | Bottom-right, PNG |

**Required CSS additions for 1-sliders:**
```css
.tb{position:absolute;top:0;left:0;right:0;height:5px;background:linear-gradient(to right,#138EFF,#59E0C5);z-index:10}
.dq{position:absolute;font-size:220px;color:rgba(19,142,255,0.04);line-height:1;top:-15px;left:0;right:0;text-align:center;pointer-events:none;z-index:0;font-family:Georgia,serif;user-select:none}
.st{font-family:'Jost',sans-serif;font-size:15px;color:#9CA3AF;font-style:italic;margin-top:18px;line-height:1.4;position:relative;z-index:2}
.cb{display:inline-block;margin-top:14px;font-family:'Jost',sans-serif;font-size:10px;font-weight:700;color:#138EFF;letter-spacing:2.5px;text-transform:uppercase;position:relative;z-index:2;border:1.5px solid rgba(19,142,255,0.35);padding:4px 12px;border-radius:20px}
.bm{position:absolute;bottom:18px;left:18px;font-family:'Chewy',cursive;font-size:18px;color:rgba(19,142,255,0.6);z-index:10}
.pw{position:absolute;bottom:8px;right:10px;width:36px;height:auto;z-index:10;opacity:0.9}
```

### Graphic Note Format

For every slide with a mascot placeholder, add this block inside the `.sw` wrapper AFTER the `.slide` closing `</div>`:

```html
<div class="sw">
  <div class="sn">Slide N — Hook</div>
  <div class="slide">
    <!-- slide content -->
    <div class="mp" style="...">Cat: brief label</div>
  </div>
  <div class="gfx-note"><b>Slide N — Graphic:</b> [Visual description of what to create. Include the Higgsfield AI prompt on the same line.]</div>
</div>
```

Required CSS to include in every file that uses `.gfx-note`:
```css
.gfx-note{max-width:360px;margin:2px auto 0;padding:8px 12px;background:rgba(19,142,255,0.05);border:1px dashed rgba(19,142,255,0.25);border-radius:6px;font-family:'Jost',sans-serif;font-size:10px;color:#4a7fb5;line-height:1.6}
.gfx-note b{color:#138EFF;font-weight:700}
```

---

## Graphics Brief (Higgsfield Prompts)

For every carousel, generate a **Higgsfield prompt** for each slide that needs the black cat mascot:

| Slide type | Prompt direction |
|------------|-----------------|
| Hook — curiosity | Cat surrounded by floating question marks, curious expression |
| Hook — pain/fear | Cat staring at overflowing camera roll or empty notebook |
| Transition — small moments | Cat sitting very small and still, quiet energy |
| Content — memory fading | Cat watching a butterfly float away, slightly reaching for it |
| Insight / save-bait | Cat sitting next to a glowing journal or open book |
| CTA | Cat waving excitedly, welcoming body language |
| Product | Cat looking at glowing phone screen showing a blog |

Include the Higgsfield prompt as a `.gfx-note` block **below** each slide in the `.sw` wrapper — NOT as a badge inside the slide itself. See the Graphic Note Format section above.

---

## Output Files

Name each file clearly:

```
output/Carousels/[YYYY-MM-DD]/
  1-slide-[hook-slug].html
  3-slide-[hook-slug].html
  8-slide-[hook-slug-a].html
  8-slide-[hook-slug-b].html
```

Example:
```
output/Carousels/2026-04-15/
  1-slide-camera-roll-story.html
  3-slide-6-months-later.html
  8-slide-graveyard-of-stories.html
  8-slide-stopped-writing.html
```

---

## Notion Destination

After generating, push a content brief to Notion:

- **Bloggo company carousels** → `notion` MCP → **Bloggo Content Engine**
- **Yoobin personal brand carousels** (founder story angle) → `notion-personal` MCP → **YOOBIN Content Engine**

When in doubt: is this posted from Bloggo's account or Yoobin's account?

---

## Quality Checklist

Before saving each carousel HTML file:

**All carousels:**
- [ ] All backgrounds are `#FFFFFF`
- [ ] Slides 2–9 use Jost font
- [ ] Slide 10 uses Chewy font
- [ ] Slide 2 has gradient text
- [ ] Content slides (3–8) are left-aligned
- [ ] Blue accent bar on left-aligned slides
- [ ] 1–3 keywords bolded per content slide
- [ ] No slide exceeds 10 words
- [ ] Cat paw PNG on slides 2–9 bottom-right (not emoji)
- [ ] Bloggo watermark on slides 2–9 bottom-left
- [ ] No `.mp` dashed placeholder boxes inside any slide
- [ ] Higgsfield prompts as `.gfx-note` blocks BELOW each mascot slide (not inside the slide)
- [ ] No cloud features mentioned
- [ ] "Bloggo" capitalized throughout
- [ ] Brand voice check passed (no jargon, active voice, benefit-first)
- [ ] CTA is one action only
- [ ] `.brief` box includes "Supporting Graphics:" section listing each slide that needs a graphic (or "None — text only")

**Hook slide (Slide 1) typography:**
- [ ] Long setup phrases use Jost italic at 18–20px, not large Chewy
- [ ] Hero word(s) are short Chewy at 52–72px — max 8–12 chars per line
- [ ] No text line wraps awkwardly (check char count against size table)

**1-slide posts only:**
- [ ] Top gradient bar (`.tb`) present
- [ ] Ghost quote mark decoration (`.dq`) present
- [ ] Subtitle tagline (`.st`) present
- [ ] CTA badge (`.cb`) present
- [ ] Bloggo watermark (`.bm`) present
- [ ] Cat paw PNG (`.pw`) present

**Per run (4 carousels):**
- [ ] 1 × 1-slide post generated
- [ ] 1 × 3–5 slide post generated
- [ ] 2 × 8–10 slide posts generated (different hook angles)

---

## Schedule

This workflow runs at **5:00 AM daily**.
Output will be ready in `output/Carousels/[TODAY'S DATE]/` by the time you wake up.
