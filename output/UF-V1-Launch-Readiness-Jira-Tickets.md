# Jira Tickets — V1 Launch Readiness
**Project:** UF- | **Epic:** V1 Launch Readiness

---

## EPIC
**UF- | V1 Launch Readiness**
Ensure Bloggo's core user flow, onboarding, and product identity are locked and clearly communicated before v1 launch.

---

## STORY 1 — Core Flow Clarity
**Summary:** User must instantly understand the Photos → Blog → Share transformation on first session

**Type:** Story
**Priority:** High
**Labels:** onboarding, ux, v1-critical

**Description:**
User interview sessions revealed that new users do not immediately understand what Bloggo does or how to get value from it. If a user doesn't grasp the core loop — camera roll gets turned into a blog — within the first session, they drop. The first session must deliver a guided success moment.

**Acceptance Criteria:**
- [ ] New user can complete the full flow (detect trip → generate blog) without external help
- [ ] The transformation (photos → organized → blog → share) is communicated visually, not just with text
- [ ] First session ends with a shareable or exportable blog — user feels a win
- [ ] No more than 2 onboarding screens before the user reaches the home screen

---

### TASK 1.1 — Design 1–2 Onboarding Screens
**Parent Story:** Core Flow Clarity
**Type:** Task
**Priority:** High

**Description:**
Design a maximum of 2 onboarding screens that communicate the core value proposition visually. Screens should show the before/after transformation: messy camera roll → beautiful blog. No feature lists. No jargon. One idea per screen.

**Acceptance Criteria:**
- [ ] Screen 1: Shows the problem (photos sitting unused)
- [ ] Screen 2: Shows the solution (Bloggo creates the blog for you)
- [ ] Copy reviewed against brand voice doc — warm, confident, simple
- [ ] Designs approved by founder before implementation

---

### TASK 1.2 — Build Visual Transformation Moment
**Parent Story:** Core Flow Clarity
**Type:** Task
**Priority:** High

**Description:**
Implement a visual "transformation" moment during or after blog generation — showing the user's actual photos being organized and turned into a blog. This is the product's magic moment and must feel satisfying and clear.

**Acceptance Criteria:**
- [ ] Animation or transition communicates photos → blog (not just a loading spinner)
- [ ] User sees their real photos in the output immediately after generation
- [ ] Moment feels fast — no perception of waiting more than a few seconds

---

### TASK 1.3 — Implement Guided First Session Flow
**Parent Story:** Core Flow Clarity
**Type:** Task
**Priority:** High

**Description:**
On first launch, guide the user directly into trip detection and blog generation rather than leaving them on an empty home screen. The goal is a guaranteed success moment in session 1.

**Acceptance Criteria:**
- [ ] First-time user is prompted to create their first blog immediately after onboarding
- [ ] App auto-suggests the most recent detectable trip to lower decision fatigue
- [ ] User reaches a completed or previewed blog before ending session 1
- [ ] Guest users can complete this flow (1 free blog export)

---
---

## STORY 2 — Product Identity Lock
**Summary:** Bloggo's in-app messaging and scope must be locked to travel storytelling for v1

**Type:** Story
**Priority:** High
**Labels:** messaging, brand, scope, v1-critical

**Description:**
User interviews revealed that Bloggo's product identity is drifting — some messaging implies it's a general memory or journaling app. For v1, Bloggo must be unambiguously positioned as a travel storytelling tool powered by your camera roll. Vague positioning leads to poor retention and harder marketing. Lock the scope, lock the copy.

**Bloggo v1 = Travel storytelling tool powered by your camera roll.**
Not "memories." Not "journaling." Not "photo organizer."

**Acceptance Criteria:**
- [ ] All in-app copy refers to trips and travel — not generic memories or moments
- [ ] Onboarding explicitly sets the expectation: Bloggo works with travel photos
- [ ] No screen uses the words "journal," "diary," or "organizer" as primary framing
- [ ] Brand voice doc updated to reflect locked scope
- [ ] Founder approves final copy pass before submission

---

### TASK 2.1 — Audit All In-App Copy for Scope Drift
**Parent Story:** Product Identity Lock
**Type:** Task
**Priority:** High

**Description:**
Do a full copy audit of every screen in the app. Flag any text that implies Bloggo works for everyday photos, general memories, or non-travel use cases. Compile a list of changes needed.

**Acceptance Criteria:**
- [ ] Every screen audited and documented
- [ ] Flagged copy listed with suggested replacement
- [ ] Audit doc shared with founder for review before changes are made

---

### TASK 2.2 — Rewrite Flagged Copy to Travel-First Framing
**Parent Story:** Product Identity Lock
**Type:** Task
**Priority:** High
**Depends on:** Task 2.1

**Description:**
Implement the approved copy changes from the audit. Every screen should speak directly to a traveler — someone with a camera roll full of trip photos they haven't done anything with yet.

**Acceptance Criteria:**
- [ ] All flagged copy updated in the app
- [ ] Copy reviewed against brand voice doc (warm, confident, simple — no jargon)
- [ ] Key screens updated: onboarding, home, empty states, paywall, share prompts

---

### TASK 2.3 — Update Empty States to Reinforce Travel Identity
**Parent Story:** Product Identity Lock
**Type:** Task
**Priority:** Medium

**Description:**
Empty states (no trips detected, no blogs yet) are a missed opportunity to reinforce what Bloggo is for. Update these to speak directly to the traveler persona and prompt action.

**Acceptance Criteria:**
- [ ] "No trips found" empty state rewritten to guide the user (e.g., "Traveled recently? Make sure Bloggo has access to your photos.")
- [ ] "No blogs yet" state includes a CTA that reinforces the value prop
- [ ] Empty states do not feel like errors — they feel like invitations
