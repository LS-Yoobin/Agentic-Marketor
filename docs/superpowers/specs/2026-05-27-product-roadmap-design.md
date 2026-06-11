# Design Spec: Bloggo Product Roadmap — Summer 2026

> Type: Strategic design document
> Created: 2026-05-27
> Session: Brainstorming → Roadmap

---

## Problem

Bloggo V1 is stuck in App Store review limbo (>1 week, no Apple response). The team has a clear V1 product but needs a strategic plan for:
1. Getting to market despite the Apple delay
2. Testing the right UX and positioning hypothesis
3. Building toward monetization and community features
4. Maximizing user growth to validate product-market fit

---

## Decisions Made

### 1. Two-App Strategy
Clone Bloggo → submit as new app with camera-first UX while Bloggo waits.
- **Bloggo**: Library-first, retroactive, "Tap to Blog"
- **New App**: Camera-first, real-time, Snapchat-style navigation
- Both share the same codebase — improvements apply to both
- The parallel test answers: which acquisition hook retains better?

### 2. Identity Pivot
Move away from "blog" as the content format name. The output is a visual story — carousel or short video — not a text blog.
- New content format name: candidate is **"trace"** (you trace a trip)
- New app name: TBD — see naming candidates in main roadmap
- The format name should have social verb potential (like "tweet," "pin," "snap")

### 3. North Star Metric
**Day-30 retention** — users returning to document a second trip.
Not downloads, not signups, not exports. Return behavior.

### 4. Monetization Anchor
**Cloud backup as the fear-of-loss paywall.**
Trigger: after user saves 3+ trips/traces.
Message: "Your memories are on one device. Back them up."
- More psychologically effective than feature gates
- Aligns with memory-preservation core positioning
- Subscription tiers: Keeper (~$4.99/mo) → Creator (~$9.99/mo)

### 5. Community Architecture
**LinkedSpaces model applied to travel:**
- Follow system (request-based, not open)
- Per-trip AND per-place privacy controls (granular)
- Following someone ≠ seeing everything
- V2 goal: users build an intentional travel network, not a broadcast feed

### 6. Long-Term Discovery Vision
**Place-centric, not person-centric.**
Search "Kyoto" → see aggregated traces from opted-in users.
This is Beli/Yelp but with richer context: full narrative, photos, ambient audio.
The data moat: every trip saved enriches the place graph.

---

## Architecture Overview

### Two-App Nav Designs

**Bloggo (current):**
```
[Home: Tap to Blog] [My Trips] [Map] [Profile]
```

**New App (camera-first):**
```
←[My Traces]  [📷 Camera]  [My Places]→
```

### Monetization Flow
```
Free (1 export) → [3 traces trigger] → Keeper subscription → [10+ traces] → Creator tier
```

### Community Rollout
```
V1: Private blogs + share links
V1.5: Web viewer (no app needed)
V2.1: User profiles + follow + per-place privacy
V2.2: Public opt-in traces + place discovery
V3+: Place graph + data network
```

---

## Team & Constraints

- **Engineering**: 2 full-stack founders (Yoobin + father)
- **Interns**: Engineering background, joining late June 2026
- **Business**: 1 business-focused co-founder (Korea), 1 funding co-founder
- **Constraint**: Small team — intern tasks must be well-scoped and non-critical-path

---

## Risks

| Risk | Mitigation |
|------|-----------|
| Apple rejects new app as duplicate | Differentiate enough (new name, new UX, new positioning) |
| Retention doesn't improve with camera-first | The data answers the question — don't assume, measure |
| Cloud backup delayed past September | Start infrastructure in August no matter what |
| Interns slow the team down | Scope intern tasks tightly, no core path work |
| Naming takes too long | Time-box to 1 week. Ship with a name that's "good enough." |

---

## Reference
Full roadmap: `output/2026-05-27-bloggo-product-roadmap.md`
