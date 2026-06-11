# Bloggo Product Roadmap — Summer 2026
> Last updated: May 27, 2026 | Owner: Yoobin + Father | Status: Active

---

## 🧭 Strategic Overview

### The Goal
**Maximize user growth to understand what the market actually wants.**
We're not building for a spec. We're building to learn. Every feature ships a hypothesis. Every phase answers a question.

### The Growth Thesis
1. Ship two apps simultaneously — test two different acquisition hooks in parallel
2. Measure which one retains users (returns for a second trip)
3. Double down on the winner. Don't guess. Let the data decide.
4. Only add community/social once the core loop is proven sticky

### The Core Loop (V1)
> User captures or imports travel moments → AI organizes + writes the story → User shares it as a carousel or video → Someone sees it → Downloads the app

**Retention = someone returning to document their next trip.**

---

## 🏷️ Identity Pivot — Moving Away From "Blog"

"Bloggo" was born from LinkedSpaces. But "blog" carries baggage — people think walls of text, personal diary, 2009 Wordpress. That's not what we're building.

**What we're actually building:**
- A visual storytelling tool
- An automatic content creator for travelers
- A personal place archive + shareable story format
- Eventually: a place-discovery network

The output isn't a "blog." It's a visual narrative — shared as a **carousel** or **short video**.

### App Name Candidates (New App)

| Name | Content Format | Vibe | Notes |
|------|---------------|------|-------|
| **Trace** | A "trace" | Clean, evocative | "Leave your trace." Works for app + format. |
| **Roam** | A "roam" | Travel-forward, simple | "Roam your last trip." Playful. |
| **Drift** | A "drift" | Wandering, free-form | Young, lifestyle-forward. |
| **Folio** | A "folio" | Portfolio feel | Elevated. "Your travel folio." |
| **Waymark** | A "waymark" | Place-forward | Connects well to places/discovery V2. |
| **Loci** | A "locus" | Intellectual, unique | Plural of "place" in Latin. Unexpected. |
| **Passage** | A "passage" | Journey-forward | "Capture every passage." |
| **Mosaic** | A "mosaic" | Visual + collage feel | The photos form a mosaic. |
| **Chronicle** | A "chronicle" | Archival, serious | Slightly old-fashioned but timeless. |
| **Stamp** | A "stamp" | Passport metaphor | "Stamp your places." Fun and intuitive. |

> **Decision needed**: Pick a name before App Store submission. Run it through: (1) Is it taken on App Store? (2) Is the domain available? (3) Does it say what we do in one word?

### Content Format Name
Whatever the app is called, the content format should have its own word — like a Tweet, a Pin, a Snap.

**Leading candidate**: **a "trace"** — you trace a trip, you share your trace, you build your trace library.

---

## 📱 Two-App Strategy

| | **Bloggo** | **New App** |
|---|---|---|
| **Status** | In App Store limbo | To be submitted |
| **Entry point** | Library-first ("I have old photos") | Camera-first ("I'm traveling now") |
| **Hero action** | Tap to Blog | Open camera |
| **Navigation** | Current tab bar | Snapchat-style swipe |
| **Tagline angle** | "Your trips, turned into stories" | "Build your story as you travel" |
| **Target user** | The backlog traveler | The real-time traveler |

**Both apps run on the same codebase.** Every AI improvement benefits both.

**The test question:** Which entry point drives stronger 30-day retention?
- If camera-first wins → update Bloggo UX to match
- If library-first wins → new app pivots UX
- Either way, we learn something

---

## 👥 Intern Onboarding — Late June 2026

Engineering interns join late June. All tasks are scoped to free up the two founders for core AI and architecture work.

### Task Assignments

| Priority | Task | Why It Matters | Expected Output |
|----------|------|----------------|-----------------|
| 🔴 #1 | **Analytics instrumentation** | Can't measure retention without it. Every decision in Aug depends on this data. | Events: session start, moment created, export tapped, day-7/14/30 return. Tool: Mixpanel or PostHog. |
| 🔴 #2 | **Web viewer for share links** | Non-app users can't open share links today. Removes the biggest sharing friction. | Browser-rendered blog/trace — read-only, no auth, fetches via existing share API. |
| 🟡 #3 | **App Store submission assets** | New app needs screenshots, preview video, icon variants before submission. | Screenshots for 6.7" + 6.1", 30s app preview video, icon in all required sizes. |
| 🟡 #4 | **Snapchat-style nav shell** | Camera-first navigation needs to be built for new app. UI only — logic already exists. | Swipe-based nav: camera center, blogs/traces left, places right. Animations + transitions. |
| 🟢 #5 | **Unit test coverage** | Reduce regression risk as we iterate fast this summer. | Test coverage for blog generation pipeline, trip detection, and share link generation. |
| 🟢 #6 | **Performance profiling** | Identify bottlenecks before users complain about slow generation. | Profiling report: callsites, timings, iPhone 12/13 benchmarks. Founders decide what to optimize. |

**What NOT to assign interns:**
- Core on-device AI improvements (too much domain knowledge)
- Cloud backend architecture (too foundational)
- App Store review responses (product judgment)
- Camera or LLM pipeline changes

---

## 🗓️ Roadmap Phases

---

### Phase 0 — Foundation
**May 27 – June 30, 2026**

**Goal:** Lay the groundwork for a clean launch. No user-facing features ship this phase.

**Founders:**
- [ ] Clone Bloggo repo → new app bundle ID + target
- [ ] Decide new app name (run through App Store conflict check + domain check)
- [ ] Design new app icon + splash screen
- [ ] Architect the camera-first navigation (founders scaffold, interns finish)
- [ ] Decide: does the new app default to camera tab or let users choose?
- [ ] Reframe video feature: short-form story (<60s), positioned for DMs + Stories, not feed

**Interns (late June):**
- [ ] Analytics instrumentation
- [ ] App Store submission assets
- [ ] Begin Snapchat-style nav shell

**Decision gate at end of Phase 0:**
> Is the new app ready to submit? Name finalized? Icon done? Nav functional?

---

### Phase 1 — MVP Launch
**July 2026**

**Goal:** Get both apps in front of real users. Start measuring.

**Founders:**
- [ ] Submit new app to App Store
- [ ] If Bloggo gets approved: update App Store listing + screenshots, do NOT change UX yet
- [ ] Ship: on-device AI improvements
  - Better photo selection (Apple Vision Framework relevance scoring)
  - Better moment grouping (reduce noise, improve day/place clustering)
  - Natural language improvement for AI narratives
- [ ] Ship: video reframe
  - Shorter default clip length (target: 30–45s sweet spot)
  - Remove any "share to feed" language — replace with "send to Stories" / "send to friends"
  - Add muted autoplay preview in app before export
- [ ] Launch analytics: begin tracking retention cohorts

**Interns:**
- [ ] Finish Snapchat-style nav shell + QA
- [ ] Web viewer for share links (build + test)
- [ ] Begin unit test coverage

**Key metric to watch:**
> Week-1 and Week-2 retention by app. Are users coming back?

**Decision gate at end of Phase 1:**
> Which app has higher day-7 retention? Use this to prioritize Phase 2 focus.

---

### Phase 2 — Growth & Measure
**August 2026**

**Goal:** Understand what's working. Build the infrastructure for what's next.

**Founders:**
- [ ] Analyze 30-day retention cohort from both apps
- [ ] Ship hot fixes from user reviews and feedback
- [ ] Improve LLM narrative quality based on early user feedback
  - Are narratives too generic? Too long? Wrong tone?
  - Consider user-tunable "vibe" for narrative style (casual vs. editorial)
- [ ] Build cloud backup infrastructure (backend only — do NOT ship to users yet)
  - Auth-linked cloud storage
  - Blog/trace sync architecture
  - Encryption at rest
- [ ] UX decision: if camera-first shows stronger retention, begin Bloggo UX update spec

**Interns:**
- [ ] Finish unit test coverage
- [ ] Performance profiling report
- [ ] Accessibility pass (VoiceOver, Dynamic Type)

**Decision gate at end of Phase 2:**
> Cloud backup backend ready? Narrative quality improved? Which app is performing better?

---

### Phase 3 — Monetize
**September 2026**

**Goal:** Convert retained users into paying subscribers. Introduce the fear-of-loss paywall.

**The Paywall Moment:**
> After a user has saved 3+ trips/traces → show: *"Your memories are on one device. Back them up."*

This works because:
1. User already has emotional investment (3 trips they care about)
2. The fear of loss is real (phone breaks, gets lost, stolen)
3. The value is clear — not "get more features," but "keep what you have"

**Subscription Tiers (proposed):**

| Tier | Price (TBD) | What's included |
|------|------------|-----------------|
| **Free** | $0 | 1 exported trace/blog · On-device only · Share links |
| **Keeper** | ~$4.99/mo or ~$39.99/yr | Unlimited exports · Cloud backup · Sync across devices · Web viewer |
| **Creator** (V2) | ~$9.99/mo | Everything in Keeper + premium AI narratives + custom styles + priority processing |

> Pricing is directional — validate against comps (Day One: $34.99/yr, Notion: $8/mo, Polarsteps: free + Pro tier) before locking in.

**Founders:**
- [ ] Launch cloud backup to users (subscription-gated)
- [ ] Implement subscription flow (StoreKit 2 — already has product IDs in codebase)
- [ ] Build web viewer for share links (if interns haven't finished by now)
- [ ] Add paywall trigger: after 3rd trace saved → Keeper upsell
- [ ] A/B test: fear-of-loss message vs. feature-unlock message

**Decision gate at end of Phase 3:**
> What's the conversion rate? (Target: 3–5% of active users) · What's the churn rate in month 1?

---

### Phase 4 — Community Seeds
**Q4 2026 (Oct–Dec)**

**Goal:** Introduce the social layer. Private by default. Opt-in everything.

This is the LinkedSpaces model applied to travel:
- Following someone doesn't mean seeing everything they've saved
- Every trip and every place has its own privacy setting
- Users build their network slowly and intentionally

**Features:**
- [ ] User profile page (public URL: `app.com/@username`)
- [ ] Follow system (request-based, not open like Twitter)
- [ ] Per-trip privacy: Private / Friends only / Public
- [ ] Per-place privacy: override trip-level privacy for specific places
- [ ] Friends feed: see new trips from people you follow (within their privacy settings)
- [ ] Share to profile: "Add this trace to my public profile"

**What this is NOT yet:**
- Not a discovery feed for strangers
- Not place-based search
- Not algorithmic content

**Decision gate at end of Phase 4:**
> Are users opting in to public profiles? Are they using the follow system? Is sharing behavior changing?

---

### Phase 5 — Discovery Layer
**2027**

**Goal:** Become the place where people go to research travel, not just document it.

This is the long-term moat. As users save trips, Bloggo accumulates the richest place-experience dataset anywhere — full narrative context, ambient audio, AI-organized moments — not just "4 stars, good pasta."

**Features:**
- [ ] Place-centric discovery feed: search "Kyoto" → see public traces from other users
- [ ] Aggregated place pages: "1,247 Bloggo users have been here"
- [ ] Curated highlights: editorial picks of standout public traces
- [ ] The data advantage: every saved trip enriches the place graph
- [ ] Integration with map view: "Places visited by Bloggo users near you"

**The Beli/Yelp angle**: Bloggo's place data is qualitatively richer than any review app because it comes with full story context. You don't just see a rating — you see someone's full afternoon in that neighborhood.

---

## 💰 Monetization Conversion Ladder

```
FREE TIER
└── Create traces, on-device only, 1 export
    │
    ▼ (trigger: 3 traces saved)
KEEPER SUBSCRIPTION (~$4.99/mo)
└── Unlimited exports + cloud backup + sync + web viewer
    │
    ▼ (trigger: power user behavior, 10+ traces)
CREATOR SUBSCRIPTION (~$9.99/mo)
└── Premium AI narratives + custom styles + advanced features
    │
    ▼ (trigger: community launch, Q4 2026)
COMMUNITY FEATURES
└── Public profile + discovery visibility (bundled into Creator or separate tier)
```

**Why users convert (psychology):**
1. **Free tier is genuinely useful** — they use it, love it, invest in it
2. **Fear of loss** — 3 trips on one device = anxiety about losing them
3. **Identity** — public profile = travel identity = worth paying for
4. **Quality ceiling** — power users want better AI, not just more storage

---

## 📊 Success Metrics Per Phase

| Phase | Key Question | Metric | Target |
|-------|-------------|--------|--------|
| **Phase 0** | Are we ready to launch? | New app submitted to App Store | ✓ by July 1 |
| **Phase 1** | Are users coming back? | Day-7 retention by app | >25% |
| **Phase 1** | Which app wins? | Day-30 retention: new app vs Bloggo | Clear winner |
| **Phase 2** | Is the AI quality good? | App Store rating | >4.3 stars |
| **Phase 2** | Are we ready to monetize? | Cloud backup backend complete | ✓ |
| **Phase 3** | Will users pay? | Free → Paid conversion rate | 3–5% |
| **Phase 3** | Is churn low? | Month-1 churn rate | <15% |
| **Phase 4** | Do users want social? | % of users opting into public profile | >10% |
| **Phase 5** | Is the place graph valuable? | Discovery searches per day | TBD |

---

## ❓ Key Unknowns & Decision Gates

| Decision | When | Inputs Needed |
|----------|------|---------------|
| New app name finalized | June 2026 | App Store conflict check, domain availability |
| Camera-first vs library-first winner | End of July | Day-7 retention data from both apps |
| Bloggo UX update (if camera-first wins) | August | Retention data + user interviews |
| Subscription pricing | September | Competitive benchmarks + willingness-to-pay signal |
| Community features scope | Q4 | Phase 3 conversion rate + user feedback |
| Rebrand Bloggo to new name? | Q4 | Market traction data from parallel test |

---

## 🔗 Related Docs
- Brand guide: `docs/marketing/bloggo-brand.md`
- Product context: `docs/marketing/bloggo-product-context.md`
- Design spec: `docs/superpowers/specs/2026-05-27-product-roadmap-design.md`
