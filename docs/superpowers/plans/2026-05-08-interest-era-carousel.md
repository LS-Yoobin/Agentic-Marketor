# "Perfection is Killing Your Growth" Carousel Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a 6-slide HTML Instagram carousel for Yoobin's personal brand using the established neon green dark theme and "The Move / Why It Works" two-part layout.

**Architecture:** Single self-contained HTML file with all 6 slides rendered as 360×450px divs. Shared CSS at the top, per-slide HTML below, html2canvas+JSZip scripts at bottom for PNG export. No external dependencies beyond CDN links.

**Tech Stack:** HTML/CSS, Inter (Google Fonts CDN), html2canvas 1.4.1, JSZip 3.10.1, FileSaver.js 2.0.5

**Spec:** `docs/superpowers/specs/2026-05-08-interest-era-carousel-design.md`

---

## File Structure

| File | Action | Purpose |
|------|--------|---------|
| `output/Carousels/2026-05-08/6-slide-perfection-killing-growth.html` | Create | The complete carousel |

---

## Task 1: Scaffold the HTML file with shared CSS and page chrome

**Files:**
- Create: `output/Carousels/2026-05-08/6-slide-perfection-killing-growth.html`

- [ ] **Step 1: Create the file with doctype, head, and shared CSS**

  The shared CSS must define these classes (copy from `output/Carousels/2026-05-07/8-slide-cofounder-before-after.html` as reference):

  ```css
  /* Reset */
  *{margin:0;padding:0;box-sizing:border-box}

  /* Page */
  body{background:#0a0a0a;padding:24px 16px 40px}

  /* Meta header */
  .meta{text-align:center;margin-bottom:16px;font-family:'Inter',sans-serif}
  .meta h1{font-size:14px;color:#ccc;font-weight:700;margin-bottom:2px}
  .meta .sub{font-size:10px;color:#555;letter-spacing:2px;text-transform:uppercase}
  .fmt{display:inline-block;padding:2px 10px;border-radius:20px;font-size:9px;font-weight:700;
       letter-spacing:1.5px;text-transform:uppercase;margin-top:4px;
       background:rgba(0,255,127,0.12);color:#00FF7F}

  /* Carousel container */
  .carousel{display:flex;flex-direction:column;align-items:center;gap:14px}

  /* Slide wrapper */
  .sw{display:flex;flex-direction:column;align-items:center;gap:3px;position:relative;width:360px}
  .sn{font-family:'Inter',sans-serif;font-size:9px;color:#444;text-transform:uppercase;letter-spacing:2px}

  /* Slide base */
  .slide{width:360px;height:450px;background:#0D1117;position:relative;overflow:hidden;
         box-shadow:0 4px 24px rgba(0,0,0,0.5);border-radius:6px}

  /* Layout helpers */
  .c{display:flex;flex-direction:column;align-items:center;justify-content:center;
     padding:40px;text-align:center;height:100%;position:relative}
  .l{display:flex;flex-direction:column;justify-content:center;
     padding:32px 32px 64px 44px;height:100%;position:relative}

  /* Decorative */
  .ab{position:absolute;left:0;top:0;bottom:0;width:4px;
      background:linear-gradient(to bottom,transparent 5%,rgba(0,255,127,0.45) 40%,
      rgba(0,255,127,0.45) 60%,transparent 95%);z-index:2}
  .rb{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
      width:220px;height:220px;
      background:radial-gradient(circle,rgba(0,255,127,0.07),transparent 70%);
      border-radius:50%;pointer-events:none}
  .dot{position:absolute;inset:0;
       background-image:radial-gradient(circle,rgba(0,255,127,0.06) 1px,transparent 1px);
       background-size:28px 28px;pointer-events:none;z-index:0}

  /* Watermark */
  .bm{position:absolute;bottom:18px;left:18px;font-family:'Inter',sans-serif;
      font-size:12px;font-weight:700;color:rgba(0,255,127,0.5);z-index:10;letter-spacing:1px}

  /* z-index content wrapper */
  .zz{position:relative;z-index:2}

  /* THE MOVE / WHY IT WORKS labels */
  .ml{font-family:'Inter',sans-serif;font-size:10px;font-weight:700;
      color:#9CA3AF;letter-spacing:3px;text-transform:uppercase;margin-bottom:8px;
      position:relative;z-index:2}
  .ml.green{color:#00FF7F}

  /* Move headline */
  .mh{font-family:'Inter',sans-serif;font-size:22px;font-weight:700;
      color:#FFFFFF;line-height:1.3;margin-bottom:0;position:relative;z-index:2}

  /* Divider between move and why */
  .dv{height:1px;background:linear-gradient(to right,rgba(0,255,127,0.6),rgba(0,255,127,0.15));
      margin:14px 0;position:relative;z-index:2}

  /* Why it works body */
  .wb{font-family:'Inter',sans-serif;font-size:14px;color:#9CA3AF;
      font-style:italic;line-height:1.6;position:relative;z-index:2}

  /* Theme label (top of each content slide) */
  .tl{font-family:'Inter',sans-serif;font-size:10px;font-weight:700;
      color:#00FF7F;letter-spacing:3px;text-transform:uppercase;
      margin-bottom:18px;position:relative;z-index:2}

  /* Save button */
  .dl-btn{position:absolute;top:24px;right:0;z-index:20;background:#00FF7F;color:#0D1117;
          border:none;border-radius:20px;padding:5px 12px;font-family:'Inter',sans-serif;
          font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;
          cursor:pointer;opacity:0;transition:opacity .2s;pointer-events:none}
  .sw:hover .dl-btn{opacity:1;pointer-events:auto}

  /* Save All button row */
  .sa{text-align:center;margin:0 0 16px}
  .sa button{background:#00FF7F;color:#0D1117;border:none;border-radius:24px;
             padding:10px 28px;font-family:'Inter',sans-serif;font-size:11px;font-weight:700;
             letter-spacing:2px;text-transform:uppercase;cursor:pointer;
             box-shadow:0 4px 18px rgba(0,255,127,.3)}
  ```

  Add Google Fonts import at top of `<style>`:
  ```css
  @import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,700;1,400&display=swap');
  ```

  Add CDN scripts before `</body>`:
  ```html
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js"></script>
  ```

  Add the saveSlide / saveAllSlides script block — copy verbatim from `output/Carousels/2026-05-07/8-slide-cofounder-before-after.html` (search for `function saveSlide`).

- [ ] **Step 2: Add page meta header and Save All button inside `<body>`**

  ```html
  <div class="meta">
    <h1>Perfection is killing your growth.</h1>
    <div class="sub">Yoobin Personal Brand · Content Strategy · May 8</div>
    <span class="fmt">Instagram Carousel · 6 Slides · 1080×1350</span>
  </div>
  <div class="sa"><button onclick="saveAllSlides()">Save All Slides</button></div>
  <div class="carousel">
    <!-- slides go here -->
  </div>
  ```

- [ ] **Step 3: Open file in browser, confirm page chrome renders correctly**

  Expected: dark background page, green badge, "Save All Slides" button visible. No slides yet — that's fine.

---

## Task 2: Slide 1 — Hook

**Files:**
- Modify: `output/Carousels/2026-05-08/6-slide-perfection-killing-growth.html`

- [ ] **Step 1: Add Slide 1 inside `.carousel`**

  ```html
  <!-- SLIDE 1: HOOK -->
  <div class="sw">
    <div class="sn">Slide 1 of 6 — Hook</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <!-- Ghost word -->
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;
                  font-size:110px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-4px;
                  transform:rotate(-8deg);user-select:none;pointer-events:none;z-index:1;
                  line-height:1;">PERFECT.</div>
      <!-- Dot grid -->
      <div class="dot"></div>
      <!-- Left accent bar -->
      <div class="ab"></div>
      <!-- Radial glow -->
      <div class="rb"></div>
      <!-- Content -->
      <div class="c">
        <div class="zz">
          <div style="font-family:'Inter',sans-serif;font-size:10px;font-weight:700;
                      color:#00FF7F;letter-spacing:3px;text-transform:uppercase;
                      margin-bottom:18px;">CONTENT STRATEGY · REAL TALK</div>
          <div style="font-family:'Inter',sans-serif;font-size:34px;font-weight:700;
                      color:#FFFFFF;line-height:1.15;margin-bottom:16px;">
            "Perfection is<br>killing your growth."
          </div>
          <div style="width:44px;height:2px;background:#00FF7F;margin:0 auto 16px;
                      box-shadow:0 0 8px rgba(0,255,127,0.5);"></div>
          <div style="font-family:'Inter',sans-serif;font-size:15px;color:#9CA3AF;
                      font-style:italic;line-height:1.55;max-width:260px;">
            I sat down with a content creator who's been in the game for a decade.
            This is what I actually learned.
          </div>
        </div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>
  ```

- [ ] **Step 2: Verify in browser**

  Expected: dark slide, "PERFECT." ghost word faint in bg, headline centered, italic context copy below divider, watermark bottom-left.

---

## Task 3: Slides 2–5 — Content Slides (Identity, Content, Platform, Growth)

**Files:**
- Modify: `output/Carousels/2026-05-08/6-slide-perfection-killing-growth.html`

- [ ] **Step 1: Add Slide 2 — Identity**

  ```html
  <!-- SLIDE 2: IDENTITY -->
  <div class="sw">
    <div class="sn">Slide 2 of 6 — Identity</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;
                  font-size:100px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-3px;
                  user-select:none;pointer-events:none;z-index:1;line-height:1;">YOU.</div>
      <div class="dot"></div>
      <div class="ab"></div>
      <div class="rb"></div>
      <div class="l">
        <div class="tl">IDENTITY</div>
        <div class="ml">THE MOVE</div>
        <div class="mh">Stop copying everyone else.</div>
        <div class="dv"></div>
        <div class="ml green">WHY IT WORKS</div>
        <div class="wb">The moment you stop copying, you start evolving into who you're meant to become. Tie your business to a niche that resonates naturally — don't force it.</div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>
  ```

- [ ] **Step 2: Add Slide 3 — Content**

  ```html
  <!-- SLIDE 3: CONTENT -->
  <div class="sw">
    <div class="sn">Slide 3 of 6 — Content</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;
                  font-size:100px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-3px;
                  user-select:none;pointer-events:none;z-index:1;line-height:1;">DATA.</div>
      <div class="dot"></div>
      <div class="ab"></div>
      <div class="rb"></div>
      <div class="l">
        <div class="tl">CONTENT</div>
        <div class="ml">THE MOVE</div>
        <div class="mh">Let the data talk.<br>Let the words land.</div>
        <div class="dv"></div>
        <div class="ml green">WHY IT WORKS</div>
        <div class="wb">Consistency builds the foundation. Analytics tell you what's actually working. Wordplay is what makes people stop scrolling.</div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>
  ```

- [ ] **Step 3: Add Slide 4 — Platform**

  ```html
  <!-- SLIDE 4: PLATFORM -->
  <div class="sw">
    <div class="sn">Slide 4 of 6 — Platform</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;
                  font-size:100px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-3px;
                  user-select:none;pointer-events:none;z-index:1;line-height:1;">DAILY.</div>
      <div class="dot"></div>
      <div class="ab"></div>
      <div class="rb"></div>
      <div class="l">
        <div class="tl">PLATFORM</div>
        <div class="ml">THE MOVE</div>
        <div class="mh">Show up every day.<br>Use Trial Reels.</div>
        <div class="dv"></div>
        <div class="ml green">WHY IT WORKS</div>
        <div class="wb">TikTok rewards volume. Instagram rewards precision. Trial Reels let you test reach without risking your existing audience.</div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>
  ```

- [ ] **Step 4: Add Slide 5 — Growth**

  ```html
  <!-- SLIDE 5: GROWTH -->
  <div class="sw">
    <div class="sn">Slide 5 of 6 — Growth</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;
                  font-size:100px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-3px;
                  user-select:none;pointer-events:none;z-index:1;line-height:1;">ASK.</div>
      <div class="dot"></div>
      <div class="ab"></div>
      <div class="rb"></div>
      <div class="l">
        <div class="tl">GROWTH</div>
        <div class="ml">THE MOVE</div>
        <div class="mh">Network. Reach out.<br>Just ask.</div>
        <div class="dv"></div>
        <div class="ml green">WHY IT WORKS</div>
        <div class="wb">The DM you don't send is the collab that never happens. Cold outreach isn't cringe — it's confidence. Grow as often as you can.</div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>
  ```

- [ ] **Step 5: Verify all 4 content slides in browser**

  Expected: each slide has its theme label (green, uppercase), THE MOVE bold white headline, green gradient divider, WHY IT WORKS italic gray copy. Ghost word visible faintly in bottom-right corner of each. Watermark present.

---

## Task 4: Slide 6 — CTA

**Files:**
- Modify: `output/Carousels/2026-05-08/6-slide-perfection-killing-growth.html`

- [ ] **Step 1: Add Slide 6**

  ```html
  <!-- SLIDE 6: CTA -->
  <div class="sw">
    <div class="sn">Slide 6 of 6 — CTA</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div class="dot"></div>
      <div class="rb"></div>
      <div class="c">
        <div class="zz">
          <div style="font-family:'Inter',sans-serif;font-size:26px;font-weight:700;
                      color:#FFFFFF;line-height:1.25;margin-bottom:16px;">
            We're not in the<br>social media era anymore.
          </div>
          <div style="width:44px;height:2px;background:#00FF7F;margin:0 auto 16px;
                      box-shadow:0 0 8px rgba(0,255,127,0.5);"></div>
          <div style="font-family:'Inter',sans-serif;font-size:15px;color:#9CA3AF;
                      font-style:italic;line-height:1.6;margin-bottom:20px;max-width:260px;">
            We're in the interest media era.<br>
            People follow people they genuinely resonate with.
          </div>
          <div style="font-family:'Inter',sans-serif;font-size:18px;font-weight:700;
                      color:#00FF7F;letter-spacing:0.5px;
                      text-shadow:0 0 20px rgba(0,255,127,0.3);">
            Follow @yoobinseo
          </div>
        </div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>
  ```

- [ ] **Step 2: Verify CTA slide in browser**

  Expected: no left accent bar, no ghost word, centered layout, white headline, green divider, italic gray body, green glowing CTA line.

---

## Task 5: Final QA and export test

**Files:**
- Modify: `output/Carousels/2026-05-08/6-slide-perfection-killing-growth.html` (fix any issues)

- [ ] **Step 1: Full visual QA — scroll all 6 slides**

  Check:
  - [ ] Slide 1: ghost word, centered layout, italic copy, watermark
  - [ ] Slides 2–5: theme label, THE MOVE / WHY IT WORKS two-part layout, ghost word, watermark
  - [ ] Slide 6: no ghost word, no accent bar, CTA line glows green
  - [ ] No text overflow on any slide
  - [ ] @yoobinseo watermark on every slide

- [ ] **Step 2: Test Save PNG on one slide**

  Hover over any slide → "Save PNG" button appears → click → PNG downloads. Confirm PNG is 360×450px and renders crisply.

- [ ] **Step 3: Test Save All Slides**

  Click "Save All Slides" → ZIP downloads with 6 PNG files named `slide-1.png` through `slide-6.png`.

- [ ] **Step 4: Commit**

  ```bash
  git add "output/Carousels/2026-05-08/6-slide-perfection-killing-growth.html"
  git add "docs/superpowers/specs/2026-05-08-interest-era-carousel-design.md"
  git add "docs/superpowers/plans/2026-05-08-interest-era-carousel.md"
  git commit -m "feat: add interest era carousel — perfection killing growth (personal brand)"
  ```
