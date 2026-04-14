# Bloggo — Complete Product Context

> This document is the single source of truth about the Bloggo app for marketing, research, and strategy work.
> Keep it updated as the product evolves.

---

## What Is Bloggo?

Bloggo is an **AI-powered iOS travel blog app** that automatically turns a user's existing photo library into beautiful, story-driven travel blogs — with zero writing required.

The core insight: most people take hundreds of photos on every trip but never do anything with them. Bloggo scans your photo library, detects trips using GPS and timestamps, organizes photos by day and place, and generates a complete narrative blog — all in seconds.

**One-line pitch:**
> "Turn your travel photos into beautiful blogs in seconds — no writing, no organizing, no blank page."

---

## The Problem It Solves

- People take thousands of travel photos but never create lasting memories from them
- Writing a travel blog is time-consuming and intimidating ("blank page anxiety")
- Photo albums are unorganized and hard to share meaningfully
- Existing blogging tools require manual effort, writing skill, and time
- Memories fade — photos without context lose meaning over time

---

## Core Features

### Auto-Trip Detection
- Scans the photo library for GPS + timestamp metadata
- Clusters photos into trips based on distance from home and date gaps
- Groups photos within a trip by day and place (restaurants, landmarks, hotels, etc.)
- Uses reverse geocoding to identify place names automatically

### AI Narrative Generation
- Generates a trip-level opening narrative (5–6 lines)
- Generates day-level summaries (4–6 lines per day)
- Generates place-level stories for each location visited
- Generates individual photo captions using computer vision
- All AI runs **on-device** — photos never leave the phone for processing

### Blog Editor
- Edit trip title, cover photo, day captions, place names
- Assign and edit place categories (restaurant, hotel, landmark, etc.)
- Remove or reorder places and photos
- Rich text editing for narratives
- Add notes to any place stop

### Story Mode (Slideshow)
- Magazine-style visual presentation of the entire blog
- Swipeable pages: cover, table of contents, day maps, place stories
- Designed for sharing on screen or exporting

### PDF Export
- Two styles: "Story Mode" (narrative-forward) and "Photos First" (gallery-forward)
- High-resolution, print-ready output
- Shareable via AirDrop, Files, or download to Photos

### Video Export
- Generates MP4 slideshow videos from blog pages
- Adjustable slide speed (default 3 seconds)
- Built-in soundtrack library for background music
- Saves to Camera Roll

### Interactive Maps
- Trip route visualization on a map
- "Places Visited" aggregate view across all trips and countries
- City-level and neighborhood-level detail

### In-App Camera ("Capture")
- Take photos directly in Bloggo and assign them to a trip
- **Vibe feature**: Records the last 10 seconds of ambient audio alongside each photo
- Location-tagged automatically

### Merge & Split
- Merge multiple trips into one blog
- Split a blog into separate trips

### Sharing
- **Secure share links**: server-assigned URLs for sharing individual blogs
- **Nearby Share**: Bluetooth/Wi-Fi device-to-device transfer with QR code or manual code
- Encrypted transfer for privacy

---

## User Journey (How Someone Uses Bloggo)

1. **Download & Onboard** — Set home location, grant photo library access
2. **"Tap to Blog"** — Single button on the home screen starts the scan
3. **Review Detected Trips** — See trips found, days, and photo counts
4. **Select Photos** — Optionally curate which photos to include
5. **Blog is Generated** — Full narrative blog created in seconds
6. **Edit (Optional)** — Tweak titles, captions, define place category, remove places
7. **Save & Share** — Export as PDF, video, or share via secure link or Nearby Share

**Time from tap to shareable blog: under 60 seconds for most trips.**

---

## Monetization Model

### Current State (V1 Launch)
- Cloud features are **not included in the first release** — all blogs are stored on-device only
- All signed-in users have full access to all V1 features
- Guests (not signed in) can create and export **1 blog** as a free trial

### V1 Feature Access
- Unlimited blog creation (on-device)
- PDF and video export
- Sharing via secure link and Nearby Share
- Merge and split blogs

### Post-V1 Monetization (Planned)
- Monthly and yearly Pro subscriptions (`com.bloggo.pro.monthly`, `com.bloggo.pro.yearly`)
- Cloud backup and sync
- Personal blog website
- Pricing TBD based on market research

### Conversion Trigger (V1)
After a guest exports their first blog, they see:
> "Save and export unlimited blogs. Guests can export one blog to try Bloggo."

---

## Target Users (Personas)

### 1. The Frequent Traveler
- Travels 4–10+ times per year (domestic and international)
- Takes 500–2,000 photos per trip
- Has a backlog of trips "I always meant to write up"
- Frustrated by Google Photos/Apple Photos not doing enough
- Values: efficiency, beautiful output, easy sharing with family

### 2. The Memory Keeper
- Travels less often but cherishes every trip deeply
- Wants a keepsake, not just photos
- Would love a "travel journal" but never has the discipline to write one
- Values: sentimentality, storytelling, permanence

### 3. The Social Sharer
- Travels with friends or family and wants to share the experience
- Currently uses Instagram Stories or WhatsApp dumps
- Wants something more polished and lasting
- Values: shareable formats, looks great, quick to produce

### 4. The Content Creator (Emerging)
- Maintains a travel blog or social presence
- Wants to cut the time it takes to produce content
- Would use Bloggo as a drafting/organizing tool
- Values: customization, export quality, narrative quality

---

## Key Differentiators vs. Competitors

| Feature | Bloggo | Google Photos | Apple Memories | Day One | Travel Blog Apps |
|---------|--------|--------------|----------------|---------|-----------------|
| Auto-detects trips from photos | ✓ | Partial | Partial | ✗ | ✗ |
| AI-written narratives | ✓ | ✗ | ✗ | ✗ | ✗ |
| On-device AI (private) | ✓ | ✗ | ✓ | ✗ | ✗ |
| PDF export | ✓ | ✗ | ✗ | ✓ | Varies |
| Video slideshow export | ✓ | ✓ | ✓ | ✗ | ✗ |
| Nearby device sharing | ✓ | ✗ | ✗ | ✗ | ✗ |
| Ambient audio capture (Vibe) | ✓ | ✗ | ✗ | ✗ | ✗ |
| Place-level storytelling | ✓ | ✗ | ✗ | ✗ | ✗ |
| Place categories | ✓ | ✗ | ✗ | ✗ | ✗ |
| Editable AI narratives | ✓ | ✗ | ✗ | N/A | Varies |

---

## Brand Voice & Personality

- **Warm** — This is about memories, not productivity
- **Confident** — The technology is sophisticated; we don't over-explain it
- **Simple** — Every feature should feel effortless; copy should be clear and jargon-free
- **Delightful** — Small moments of surprise and polish matter

**Tone examples:**
- ✓ "Your trips, turned into stories."
- ✓ "Bloggo removes blank page anxiety."
- ✓ "Thousands of photos. Zero stories written. We turn them into stories."
- ✗ "Leverage AI to generate narrative content from your photo metadata."

---

## Existing Marketing Copy (from the app)

| Location | Copy |
|----------|------|
| Onboarding problem screen | "Bloggo removes blank page anxiety." |
| Onboarding sub-headline | "Thousands of photos. Zero stories written. We turn them into stories." |
| Landing screen CTA | "Tap to Blog" / "Blog Your Trips in Seconds" |
| Paywall hero | "Make Every Trip Count" |
| Paywall sub | "Create blogs faster than ever!" |
| Guest upsell | "Save and export unlimited blogs. Guests can export one blog to try Bloggo." |
| Camera permission | "We use your camera so you can capture moments and add them to your blog." |
| Photo permission | "Bloggo reads your photo library to find travel photos and automatically organize them into trip blogs on your device." |
| Audio permission | "We record a short audio Vibe clip alongside your photo so you can relive the sounds of the moment." |

---

## Platform & Technical Facts

- **Platform**: iOS only (iPhone-first)
- **Minimum iOS**: iOS 15+ (some features iOS 18+)
- **App name**: Bloggo
- **Bundle ID**: fastblog (internal), Bloggo (public)
- **Sign-in methods**: Apple Sign-In, Google Sign-In, Email
- **AI**: On-device (local LLM + Apple Vision framework) — photos never leave the device for AI processing
- **Storage**: All blogs stored on-device only (V1); cloud backup planned post-launch
- **Backend**: Custom API for auth and share links
- **Deep links**: Password reset, email verification, trip share codes
- **Orientation**: Portrait (landscape only during video export)

---

## What We Don't Know Yet (Research Opportunities)

- Exact App Store category positioning (Travel? Lifestyle? Productivity?)
- Primary competitor set (direct travel blog apps, memory apps, AI writing apps)
- Pricing benchmarks for similar subscription apps
- Geographic markets with highest travel photography culture
- Instagram/TikTok creator overlap opportunity
- Enterprise/group travel use cases
