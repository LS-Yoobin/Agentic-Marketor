# How to Use Your Marketing Agent

This is your complete reference for running the Bloggo social media content strategy system.
The agent handles all execution. Your job is to review, approve, and occasionally direct.

---

## The Big Picture

You have two accounts, four platforms, and a pre-built workflow the agent follows every time.

| Account | Platforms | What It Does |
|---------|-----------|--------------|
| **Personal Brand** | Instagram, TikTok, YouTube, LinkedIn | Founder journey + product builder content — builds your credibility and authority |
| **Bloggo Company Page** | Instagram, TikTok, YouTube, LinkedIn | Brand identity, product awareness, organic reach |

The agent reads everything in your `docs/Marketing/` folder before writing a single word. You never have to re-explain Bloggo's voice, features, or rules — it's all in the files.

---

## How to Run a Content Batch

A content batch is one week of ready-to-post content for both accounts across all platforms.

### What to say

> "Run the social media content engine strategy workflow."

That's it. The agent will:

1. Check your Idea Inbox for any ideas you've submitted
2. Search the web for trending topics, competitor moves, and timely hooks
3. Load every marketing file as context
4. Generate content ideas across both accounts
5. Write full drafts (Reel scripts, carousels, LinkedIn posts)
6. Grade every piece — PUSH, REVISE, or REWRITE
7. Deliver a structured batch ready for your review

### What you get back

A single document with content for both accounts, organized like this:

```
📦 Content Batch — [Week / Date]

BLOGGO COMPANY PAGE
├── Reel script (+ YouTube title, description, hashtags)
├── Carousel (slide by slide)
└── LinkedIn post

PERSONAL BRAND PAGE
├── Reel script (+ YouTube title, description, hashtags)
├── Carousel (slide by slide)
└── LinkedIn post

RESEARCH FINDINGS THIS WEEK
└── 3–5 bullet summary of trends that shaped the batch
```

Each piece has a grade score and a PUSH verdict. Anything that didn't pass was already revised before it reached you.

### Default batch size

- **Bloggo page:** 6 pieces per week (2 Reel scripts, 2 Carousels, 2 LinkedIn posts)
- **Personal Brand:** 5 pieces per week (2 Reel scripts, 1 Carousel, 2 LinkedIn posts)
- TikTok and YouTube Shorts use the same Reel scripts — no extra work

### Request a smaller batch

> "Run the workflow but only give me 3 pieces for each account."

The agent will comply with whatever size you specify.

---

## How to Submit Your Own Ideas

Your ideas always come first. The agent prioritizes them above everything it generates on its own.

### Option 1 — Tell the agent directly

Just say it in chat:

> "I want to do a Reel about the moment I submitted Bloggo to the App Store — the waiting, the uncertainty, the lesson."

The agent will match it to a content pillar, pick the best platform and format, write it, grade it, and include it in the next batch.

### Option 2 — Drop it in the Idea Inbox

Open this file and add your idea at the bottom:

**File:** `docs/Marketing/Idea Inbox.md`

Write in any format. No structure required. Examples:

```
- Reel idea: show what happens when you tap to blog for the first time
- LinkedIn post: hardest part of waiting for App Store approval
- Carousel: 5 things I wish I knew before building an iOS app
- TikTok: I have 3,000 photos from my last trip and zero captions
```

The next time you run a content batch, the agent checks the inbox first and builds those ideas before anything else.

### What happens if an idea breaks a brand rule

The agent won't silently drop it. It will include a **Brand Rule Conflicts** section in the batch output with:
- What the conflict is
- A suggested compliant alternative

---

## How to Change the Launch Phase

The launch phase controls the call-to-action on every piece of content. There are three phases:

| Phase | When | CTA |
|-------|------|-----|
| **Pre-Launch** | Now — waiting for App Store approval | "Join the Bloggo beta — link in bio" |
| **Launch Week** | When you manually release | "Download now — App Store" |
| **Post-Launch** | After release, sustained growth | "Try it free" / "Share your first blog" |

### How to switch phases

Open the workflow file and find this line near the top:

**File:** `Workflows/social-media-content-strategy.md`

```
> **Current phase: Pre-Launch**
```

Change it to whichever phase applies:

```
> **Current phase: Launch Week**
```

The next content batch will automatically use the new CTA across every piece of content on every platform. You do not need to tell the agent anything else.

---

## How to Request Timely Research

Every content batch already includes a Research Pulse — the agent searches for trends before generating ideas. But you can also ask for a standalone research run.

### Request trending hooks for a specific topic

> "Search for what's trending in travel photography right now and give me 5 hook ideas for Bloggo's Instagram."

### Request a competitor check

> "Look up what Day One and Polarsteps have been posting lately. Any angles we can counter or complement?"

### Request a format trend check

> "What Reel formats are performing well in the travel niche this week? Find examples and suggest which we should try."

---

## How to Request a Specific Format

You don't have to run a full batch every time. You can ask for one specific piece.

### Examples

> "Write me a carousel for the Bloggo company page about why your travel photos are already a story."

> "Write a LinkedIn post for my personal brand about the experience of waiting for App Store approval."

> "Give me 10 hook options for a Reel about camera roll chaos — personal brand account."

> "Write a TikTok script using the viral hook → conflict → escalation → payoff formula. Topic: the moment you realize you've forgotten the name of every restaurant from your last trip."

---

## How to Review and Approve a Batch

When the agent delivers a content batch, you have three options:

### Approve everything
> "Approved. I'll schedule these."

### Approve with changes
> "Approve the carousels but rewrite the LinkedIn posts — make them more personal and less brand-y."

### Reject a specific piece
> "The first Reel isn't hitting. Try a different angle — lead with the memory problem, not the camera roll chaos."

The agent will revise, re-grade, and return the updated version.

---

## How the IDE Context Works

Two things in your code editor affect what the agent sees:

### Opening a file
When you open a file in the IDE, the agent gets a notification that you opened it — but does **not** automatically read its contents. It's a soft signal that the file might be relevant to what you're asking.

### Selecting / highlighting text
When you **highlight text** in the IDE, that selected text is sent directly into the conversation. The agent can read it exactly as if you'd pasted it into the chat.

**This is useful for:**
- Pointing the agent to a specific section without copy-pasting
- Sharing raw content or notes you want incorporated
- Showing the agent a piece of content you want refined or graded

---

## Quick Reference — What to Say

| What You Want | What to Say |
|---------------|-------------|
| Full weekly content batch | "Run the social media content strategy workflow" |
| Smaller batch | "Run the workflow, give me 3 pieces per account" |
| One specific piece | "Write a Reel script for [topic] for [account]" |
| Submit an idea | "I have an idea: [describe it]" or add to Idea Inbox |
| Trend research | "Search for what's trending in [topic] right now" |
| Grade existing content | "Grade this post using the Content Grader: [paste content]" |
| Hook options | "Give me 10 hook ideas for [topic]" |
| Rewrite a piece | "Rewrite this for the [account] using [pillar] angle: [paste]" |
| Switch launch phase | Edit `Current phase:` in the workflow file |
| Add an idea for later | Add it to `docs/Marketing/Idea Inbox.md` |

---

## Files Reference

| File | What It Is | When You Touch It |
|------|-----------|------------------|
| `Workflows/content Engine.md` | The agent's operating instructions | To change the launch phase |
| `docs/Marketing/Idea Inbox.md` | Where you drop raw ideas | Whenever inspiration hits |
| `docs/Marketing/bloggo-brand.md` | Brand voice and copy rules | If Bloggo's voice/positioning changes |
| `docs/Marketing/bloggo-product-context.md` | Full product identity and features | When new features ship |
| `docs/Workflows/Content Grader.md` | Scoring rubric for every post | Reference only |
| `docs/Marketing/Viral Short-Form Video Playbook.md` | Reel/TikTok formula | Reference only |
| `docs/Marketing/Instagram Carousel Cheat Sheet.md` | Carousel structure guide | Reference only |
| `docs/Marketing/marketing-research.md` | Market and competitor data | Reference only |

---

## Brand Rules — Always On

These never change. The agent applies them to every piece of content automatically.

1. Never mention cloud features — Bloggo V1 is on-device only
2. iOS only — no Android implication
3. Privacy is a feature — lead with it when relevant
4. "Bloggo" is always capitalized
5. Active voice — "Bloggo creates" not "blogs are created"
6. Lead with the benefit, not the feature
7. No jargon — "leverage," "utilize," "seamless," "powerful" are banned
8. Short sentences. One idea per sentence.
9. No more than one exclamation point per post
