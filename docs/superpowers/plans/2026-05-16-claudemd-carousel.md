# CLAUDE.md Deep Dive Carousel — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an 8-slide Instagram carousel HTML file teaching builders how CLAUDE.md works, framed as a founder discovery story.

**Architecture:** Single self-contained HTML file. All styles inline/in `<style>` block. Slides rendered as 360×450px divs (3× scale to 1080×1350 on export via html2canvas). No external dependencies beyond CDN scripts and Google Fonts.

**Tech Stack:** HTML, CSS (inline + style block), vanilla JS, html2canvas 1.4.1, JSZip 3.10.1, FileSaver.js 2.0.5 (all via CDN), Google Fonts (Inter)

**Reference:** Existing carousel pattern at `output/Carousels/2026-05-08/8-slide-ai-tools-team-of-2.html`
**Spec:** `docs/superpowers/specs/2026-05-16-claudemd-carousel-design.md`
**Output:** `output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html`

---

## File Structure

- **Create:** `output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html`
  - All 8 slides, shared CSS, export JS, page metadata

---

## CSS Class Reference (from existing carousel pattern)

| Class | Purpose |
|-------|---------|
| `.slide` | 360×450px slide container, `#0D1117` bg |
| `.c` | Centered layout (flexbox, center+center, padding 40px) |
| `.l` | Left-aligned layout (flexbox column, padding 32px 32px 64px 44px) |
| `.ab` | Accent sidebar bar (4px, left edge, green gradient) |
| `.rb` | Radial glow (220×220px centered circle) |
| `.dot` | Dot grid overlay |
| `.bm` | @yoobinseo branding (bottom-left) |
| `.tl` | Neon green label (10px uppercase, letter-spacing 3px) |
| `.ml` | Gray label (10px uppercase) — add `.green` for neon |
| `.mh` | Main headline (22px bold white) |
| `.dv` | Neon green divider line |
| `.wb` | Body/subtext (14px gray italic) |
| `.sw` | Slide wrapper (with hover Save PNG button) |
| `.sn` | Slide counter label |
| `.dl-btn` | Per-slide Save PNG hover button |
| `.sa` | Save All Slides button container |

---

## Task 1: Create the HTML shell

**Files:**
- Create: `output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html`

- [ ] **Step 1: Create the output directory and HTML shell**

Create `output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html` with this exact content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>I gave Claude a permanent memory</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,700;1,400&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0a0a;padding:24px 16px 40px}
.meta{text-align:center;margin-bottom:16px;font-family:'Inter',sans-serif}
.meta h1{font-size:14px;color:#ccc;font-weight:700;margin-bottom:2px}
.meta .sub{font-size:10px;color:#555;letter-spacing:2px;text-transform:uppercase}
.fmt{display:inline-block;padding:2px 10px;border-radius:20px;font-size:9px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin-top:4px;background:rgba(0,255,127,0.12);color:#00FF7F}
.carousel{display:flex;flex-direction:column;align-items:center;gap:14px}
.sw{display:flex;flex-direction:column;align-items:center;gap:3px;position:relative;width:360px}
.sn{font-family:'Inter',sans-serif;font-size:9px;color:#444;text-transform:uppercase;letter-spacing:2px}
.slide{width:360px;height:450px;background:#0D1117;position:relative;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.5);border-radius:6px}
.c{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:40px;text-align:center;height:100%;position:relative}
.l{display:flex;flex-direction:column;justify-content:center;padding:32px 32px 64px 44px;height:100%;position:relative}
.ab{position:absolute;left:0;top:0;bottom:0;width:4px;background:linear-gradient(to bottom,transparent 5%,rgba(0,255,127,0.45) 40%,rgba(0,255,127,0.45) 60%,transparent 95%);z-index:2}
.rb{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:220px;height:220px;background:radial-gradient(circle,rgba(0,255,127,0.07),transparent 70%);border-radius:50%;pointer-events:none}
.dot{position:absolute;inset:0;background-image:radial-gradient(circle,rgba(0,255,127,0.06) 1px,transparent 1px);background-size:28px 28px;pointer-events:none;z-index:0}
.bm{position:absolute;bottom:18px;left:18px;font-family:'Inter',sans-serif;font-size:12px;font-weight:700;color:rgba(0,255,127,0.5);z-index:10;letter-spacing:1px}
.zz{position:relative;z-index:2}
.ml{font-family:'Inter',sans-serif;font-size:10px;font-weight:700;color:#9CA3AF;letter-spacing:3px;text-transform:uppercase;margin-bottom:8px;position:relative;z-index:2}
.ml.green{color:#00FF7F}
.mh{font-family:'Inter',sans-serif;font-size:22px;font-weight:700;color:#FFFFFF;line-height:1.3;margin-bottom:0;position:relative;z-index:2}
.dv{height:1px;background:linear-gradient(to right,rgba(0,255,127,0.6),rgba(0,255,127,0.15));margin:14px 0;position:relative;z-index:2}
.wb{font-family:'Inter',sans-serif;font-size:14px;color:#9CA3AF;font-style:italic;line-height:1.6;position:relative;z-index:2}
.tl{font-family:'Inter',sans-serif;font-size:10px;font-weight:700;color:#00FF7F;letter-spacing:3px;text-transform:uppercase;margin-bottom:18px;position:relative;z-index:2}
.dl-btn{position:absolute;top:24px;right:0;z-index:20;background:#00FF7F;color:#0D1117;border:none;border-radius:20px;padding:5px 12px;font-family:'Inter',sans-serif;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;cursor:pointer;opacity:0;transition:opacity .2s;pointer-events:none}
.sw:hover .dl-btn{opacity:1;pointer-events:auto}
.sa{text-align:center;margin:0 0 16px}
.sa button{background:#00FF7F;color:#0D1117;border:none;border-radius:24px;padding:10px 28px;font-family:'Inter',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;cursor:pointer;box-shadow:0 4px 18px rgba(0,255,127,.3)}
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.5/FileSaver.min.js"></script>
</head>
<body>

<div class="meta">
  <h1>I gave Claude a permanent memory and it changed how I work</h1>
  <div class="sub">Yoobin Personal Brand · Claude Tips · May 16</div>
  <span class="fmt">Instagram Carousel · 8 Slides · 1080×1350</span>
</div>

<div class="sa"><button onclick="saveAllSlides()">Save All Slides</button></div>

<div class="carousel">
  <!-- SLIDES GO HERE -->
</div>

<script>
async function saveAllSlides(){
  var btn=document.querySelector('[onclick="saveAllSlides()"]');
  var orig=btn.textContent;
  var slides=document.querySelectorAll('.slide');
  var title=document.title.replace(/\s+/g,'-').toLowerCase();
  var zip=new JSZip();
  btn.disabled=true;
  for(var i=0;i<slides.length;i++){
    btn.textContent='Saving '+(i+1)+'/'+slides.length+'...';
    var canvas=await html2canvas(slides[i],{scale:3,useCORS:true,backgroundColor:'#0D1117'});
    var blob=await new Promise(function(r){canvas.toBlob(r,'image/png');});
    zip.file('slide-'+(i+1)+'.png',blob);
  }
  var zipBlob=await zip.generateAsync({type:'blob'});
  saveAs(zipBlob,title+'-slides.zip');
  btn.textContent=orig;
  btn.disabled=false;
}
function saveSlide(btn){
  var slide=btn.parentElement.querySelector('.slide');
  btn.style.opacity='0';
  html2canvas(slide,{scale:3,useCORS:true,backgroundColor:'#0D1117'}).then(function(canvas){
    var a=document.createElement('a');
    a.download=document.title.replace(/\s+/g,'-').toLowerCase()+'-slide-'+Date.now()+'.png';
    a.href=canvas.toDataURL('image/png');
    a.click();
    btn.style.opacity='';
  });
}
</script>
</body>
</html>
```

- [ ] **Step 2: Open the file in a browser and verify it renders** — dark background, green "Save All Slides" button, metadata header visible. No slides yet — that's expected.

- [ ] **Step 3: Commit**

```bash
git add output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html
git commit -m "feat: carousel shell — CLAUDE.md deep dive"
```

---

## Task 2: Slides 1–2 (Hook + Problem)

**Files:**
- Modify: `output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html`

Replace `<!-- SLIDES GO HERE -->` with the first two slides.

- [ ] **Step 1: Add Slide 1 — Hook (centered layout)**

```html
  <!-- SLIDE 1: HOOK -->
  <div class="sw">
    <div class="sn">Slide 1 of 8 — Hook</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;font-size:110px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-4px;transform:rotate(-8deg);user-select:none;pointer-events:none;z-index:1;line-height:1;">CLAUDE.MD</div>
      <div class="dot"></div>
      <div class="rb"></div>
      <div class="c">
        <div class="zz">
          <div class="tl">CLAUDE CODE · FOUNDER TIP</div>
          <div class="mh" style="font-size:26px;margin-bottom:16px;">"I was re-explaining myself to Claude every single session."</div>
          <div style="width:44px;height:2px;background:#00FF7F;margin:0 auto 16px;box-shadow:0 0 8px rgba(0,255,127,0.5);"></div>
          <div class="wb">Every new chat. Same context. From scratch.</div>
        </div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>

  <!-- SLIDE 2: THE PROBLEM -->
  <div class="sw">
    <div class="sn">Slide 2 of 8 — The Problem</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;font-size:110px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-4px;transform:rotate(-8deg);user-select:none;pointer-events:none;z-index:1;line-height:1;">CLAUDE.MD</div>
      <div class="dot"></div>
      <div class="ab"></div>
      <div class="rb"></div>
      <div class="l">
        <div class="tl">THE PROBLEM</div>
        <div style="background:#161B22;border-left:4px solid #00FF7F;border-radius:6px;padding:16px 18px;margin-bottom:18px;position:relative;z-index:2;">
          <div style="font-family:'Inter',sans-serif;font-size:14px;color:#D1D5DB;font-style:italic;line-height:1.6;">"My app is called Bloggo. It's iOS only. The brand voice is warm, not corporate. Don't use jargon."</div>
        </div>
        <div class="wb" style="margin-top:4px;">Close the chat. Open a new one. Start over.</div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>
```

- [ ] **Step 2: Open in browser — verify Slide 1 is centered with large headline and neon label. Verify Slide 2 has the green-bordered quote card and subtext below it.**

- [ ] **Step 3: Commit**

```bash
git add output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html
git commit -m "feat: slides 1-2 — hook and problem"
```

---

## Task 3: Slides 3–4 (Discovery + What It Is)

**Files:**
- Modify: `output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html`

Append after Slide 2, inside `.carousel`:

- [ ] **Step 1: Add Slide 3 — The Discovery (centered)**

```html
  <!-- SLIDE 3: THE DISCOVERY -->
  <div class="sw">
    <div class="sn">Slide 3 of 8 — The Discovery</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;font-size:110px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-4px;transform:rotate(-8deg);user-select:none;pointer-events:none;z-index:1;line-height:1;">CLAUDE.MD</div>
      <div class="dot"></div>
      <div class="rb"></div>
      <div class="c">
        <div class="zz">
          <div class="tl">THE TURNING POINT</div>
          <div class="mh" style="font-size:26px;margin-bottom:16px;">Then I found something called CLAUDE.md.</div>
          <div style="width:44px;height:2px;background:#00FF7F;margin:0 auto 16px;box-shadow:0 0 8px rgba(0,255,127,0.5);"></div>
          <div class="wb">Most Claude users have never heard of it.</div>
        </div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>

  <!-- SLIDE 4: WHAT IT IS -->
  <div class="sw">
    <div class="sn">Slide 4 of 8 — What It Is</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;font-size:110px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-4px;transform:rotate(-8deg);user-select:none;pointer-events:none;z-index:1;line-height:1;">CLAUDE.MD</div>
      <div class="dot"></div>
      <div class="ab"></div>
      <div class="rb"></div>
      <div class="l">
        <div class="tl">WHAT IT IS</div>
        <div class="mh" style="margin-bottom:14px;">"A file you put in your project folder that Claude reads automatically every time you open it."</div>
        <div class="dv"></div>
        <div class="wb">It's a permanent briefing note. It never forgets.</div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>
```

- [ ] **Step 2: Open in browser — verify Slide 3 centered with "THE TURNING POINT" label. Slide 4 left-aligned with accent sidebar, headline, divider, subtext.**

- [ ] **Step 3: Commit**

```bash
git add output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html
git commit -m "feat: slides 3-4 — discovery and explanation"
```

---

## Task 4: Slides 5–6 (What's In Mine + The Result)

**Files:**
- Modify: `output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html`

Ghost text switches to "MEMORY." from Slide 5 onward.

- [ ] **Step 1: Add Slide 5 — What's In Mine (left-aligned, neon bullet rows)**

```html
  <!-- SLIDE 5: WHAT'S IN MINE -->
  <div class="sw">
    <div class="sn">Slide 5 of 8 — What's In Mine</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;font-size:110px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-4px;transform:rotate(-8deg);user-select:none;pointer-events:none;z-index:1;line-height:1;">MEMORY.</div>
      <div class="dot"></div>
      <div class="ab"></div>
      <div class="rb"></div>
      <div class="l">
        <div class="tl">WHAT'S IN MINE</div>
        <div style="display:flex;flex-direction:column;gap:14px;position:relative;z-index:2;">
          <div style="display:flex;align-items:flex-start;gap:12px;">
            <span style="font-family:'Inter',sans-serif;font-size:18px;font-weight:700;color:#00FF7F;line-height:1.4;flex-shrink:0;">•</span>
            <span style="font-family:'Inter',sans-serif;font-size:16px;color:#FFFFFF;line-height:1.5;">What Bloggo is and who it's for</span>
          </div>
          <div style="display:flex;align-items:flex-start;gap:12px;">
            <span style="font-family:'Inter',sans-serif;font-size:18px;font-weight:700;color:#00FF7F;line-height:1.4;flex-shrink:0;">•</span>
            <span style="font-family:'Inter',sans-serif;font-size:16px;color:#FFFFFF;line-height:1.5;">My brand voice rules (what to say, what to avoid)</span>
          </div>
          <div style="display:flex;align-items:flex-start;gap:12px;">
            <span style="font-family:'Inter',sans-serif;font-size:18px;font-weight:700;color:#00FF7F;line-height:1.4;flex-shrink:0;">•</span>
            <span style="font-family:'Inter',sans-serif;font-size:16px;color:#FFFFFF;line-height:1.5;">Output format preferences</span>
          </div>
          <div style="display:flex;align-items:flex-start;gap:12px;">
            <span style="font-family:'Inter',sans-serif;font-size:18px;font-weight:700;color:#00FF7F;line-height:1.4;flex-shrink:0;">•</span>
            <span style="font-family:'Inter',sans-serif;font-size:16px;color:#FFFFFF;line-height:1.5;">Things Claude should never do</span>
          </div>
        </div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>

  <!-- SLIDE 6: THE RESULT -->
  <div class="sw">
    <div class="sn">Slide 6 of 8 — The Result</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;font-size:110px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-4px;transform:rotate(-8deg);user-select:none;pointer-events:none;z-index:1;line-height:1;">MEMORY.</div>
      <div class="dot"></div>
      <div class="rb"></div>
      <div class="c">
        <div class="zz">
          <div class="tl">THE RESULT</div>
          <div class="mh" style="font-size:24px;margin-bottom:16px;">"Now Claude already knows my product, my tone, my rules."</div>
          <div style="width:44px;height:2px;background:#00FF7F;margin:0 auto 16px;box-shadow:0 0 8px rgba(0,255,127,0.5);"></div>
          <div class="wb">I haven't re-explained Bloggo in weeks.</div>
        </div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>
```

- [ ] **Step 2: Open in browser — Slide 5 shows 4 neon-bullet rows (white text, green bullets). Slide 6 is centered with outcome headline.**

- [ ] **Step 3: Commit**

```bash
git add output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html
git commit -m "feat: slides 5-6 — what's in mine and result"
```

---

## Task 5: Slides 7–8 (How To + CTA)

**Files:**
- Modify: `output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html`

- [ ] **Step 1: Add Slide 7 — How To Set It Up (large neon numbered steps)**

```html
  <!-- SLIDE 7: HOW TO DO IT -->
  <div class="sw">
    <div class="sn">Slide 7 of 8 — How To Do It</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;font-size:110px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-4px;transform:rotate(-8deg);user-select:none;pointer-events:none;z-index:1;line-height:1;">MEMORY.</div>
      <div class="dot"></div>
      <div class="ab"></div>
      <div class="rb"></div>
      <div class="l">
        <div class="tl">HOW TO DO IT</div>
        <div style="display:flex;flex-direction:column;gap:20px;position:relative;z-index:2;">
          <div style="display:flex;align-items:flex-start;gap:16px;">
            <span style="font-family:'Inter',sans-serif;font-size:32px;font-weight:700;color:#00FF7F;line-height:1.1;flex-shrink:0;min-width:24px;">1</span>
            <span style="font-family:'Inter',sans-serif;font-size:16px;color:#FFFFFF;line-height:1.5;padding-top:6px;">Create a file called <span style="font-family:monospace;color:#00FF7F;background:rgba(0,255,127,0.1);padding:2px 6px;border-radius:4px;">CLAUDE.md</span> in your project root</span>
          </div>
          <div style="display:flex;align-items:flex-start;gap:16px;">
            <span style="font-family:'Inter',sans-serif;font-size:32px;font-weight:700;color:#00FF7F;line-height:1.1;flex-shrink:0;min-width:24px;">2</span>
            <span style="font-family:'Inter',sans-serif;font-size:16px;color:#FFFFFF;line-height:1.5;padding-top:6px;">Write what you want Claude to always know</span>
          </div>
          <div style="display:flex;align-items:flex-start;gap:16px;">
            <span style="font-family:'Inter',sans-serif;font-size:32px;font-weight:700;color:#00FF7F;line-height:1.1;flex-shrink:0;min-width:24px;">3</span>
            <span style="font-family:'Inter',sans-serif;font-size:16px;color:#FFFFFF;line-height:1.5;padding-top:6px;">That's it.</span>
          </div>
        </div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>

  <!-- SLIDE 8: CTA -->
  <div class="sw">
    <div class="sn">Slide 8 of 8 — CTA</div>
    <button class="dl-btn" onclick="saveSlide(this)">Save PNG</button>
    <div class="slide">
      <div style="position:absolute;bottom:-10px;right:-10px;font-family:'Inter',sans-serif;font-size:110px;font-weight:700;color:rgba(0,255,127,0.04);letter-spacing:-4px;transform:rotate(-8deg);user-select:none;pointer-events:none;z-index:1;line-height:1;">MEMORY.</div>
      <div class="dot"></div>
      <div class="rb"></div>
      <div class="c">
        <div class="zz">
          <div class="tl">SAVE THIS</div>
          <div class="mh" style="font-size:26px;margin-bottom:16px;">Save this if you use Claude daily.</div>
          <div style="width:44px;height:2px;background:#00FF7F;margin:0 auto 16px;box-shadow:0 0 8px rgba(0,255,127,0.5);"></div>
          <div class="wb">What would you put in yours?<br>Drop it below.</div>
        </div>
      </div>
      <div class="bm">@yoobinseo</div>
    </div>
  </div>
```

- [ ] **Step 2: Open in browser — Slide 7 shows large neon numbers (32px) with step text. `CLAUDE.md` filename styled in a green monospace pill. Slide 8 is centered with CTA.**

- [ ] **Step 3: Verify all 8 slides render correctly** — scroll through all slides, check:
  - All 8 slide counter labels show correctly ("Slide X of 8")
  - Ghost text shows "CLAUDE.MD" on slides 1–4, "MEMORY." on slides 5–8
  - @yoobinseo branding visible on every slide
  - Hover over any slide to confirm "Save PNG" button appears

- [ ] **Step 4: Test Save All Slides** — click the button, verify a ZIP downloads containing 8 PNG files at 1080×1350 (3× scale).

- [ ] **Step 5: Commit**

```bash
git add output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html
git commit -m "feat: slides 7-8 — how to and CTA, carousel complete"
```

---

## Task 6: Final check and Notion push

**Files:** None — verification and upload only

- [ ] **Step 1: Open the completed file in a browser. Do a final read-through of every slide's copy** — check for typos, verify the narrative flows logically slide to slide.

- [ ] **Step 2: Push to Notion** — destination is `notion-personal` → YOOBIN Content Engine. Add the file path and title as a new content entry.

- [ ] **Step 3: Final commit**

```bash
git add output/Carousels/2026-05-16/8-slide-claudemd-permanent-memory.html
git commit -m "done: CLAUDE.md carousel complete and pushed to Notion"
```
