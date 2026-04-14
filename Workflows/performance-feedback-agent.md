# Performance Feedback Agent

## Trigger
User says: "analyze performance for: [post title or date]"

---

## Step 1: Token Expiry Check

Read the `.env` file and check `INSTAGRAM_TOKEN_EXPIRY` (format: YYYY-MM-DD).

- If the expiry date is within 7 days from today:
  > ⚠️ "Your Instagram API token expires on [date]. See resources/instagram-api-setup.md for refresh instructions."
  Continue anyway.

- If the expiry date has already passed:
  > ❌ "Your Instagram API token has expired. Please refresh it using resources/instagram-api-setup.md before running this agent."
  Stop here.

---

## Step 2: Find the Matching Notion Page

Search for the post in both Notion workspaces using the title or date provided.

Search Yoobin Content Engine DB (`3378683d-d8fb-8109-a3c5-eabd65c1a6f1`) via `notion-personal`:
- Use `mcp__notion-personal__API-post-search` with the post title as query
- Filter by `object: page`

Search Bloggo Content Engine DB (`32d8683d-d8fb-80cf-9941-ed25238b6fe2`) via `notion`:
- Use `mcp__notion__API-post-search` with the post title as query
- Filter by `object: page`

Match by:
- Title substring (case-insensitive)
- OR Post Date field matching the provided date

If no match found, ask the user:
> "I couldn't find '[title/date]' in either Notion database. Can you provide the exact title or date?"

---

## Step 3: Pull Instagram Metrics

Read `INSTAGRAM_ACCESS_TOKEN` and `INSTAGRAM_USER_ID` from `.env`.

**Fetch recent media list** (use Bash with curl):
```bash
curl "https://graph.facebook.com/v18.0/$INSTAGRAM_USER_ID/media?fields=id,caption,timestamp,media_type&access_token=$INSTAGRAM_ACCESS_TOKEN"
```

Match the post by:
1. Caption text containing the Notion page title (case-insensitive substring match)
2. OR timestamp within ±1 day of the Notion Post Date

**Fetch post insights** once the ig_media_id is found:
```bash
curl "https://graph.facebook.com/v18.0/$IG_MEDIA_ID/insights?metric=impressions,reach,saved,shares,comments_count&access_token=$INSTAGRAM_ACCESS_TOKEN"
```

Store the returned values: impressions, reach, saved, shares, comments_count.

If the API returns an auth error, stop and tell the user:
> ❌ "Instagram API authentication failed. Please check your credentials in .env."

---

## Step 4: Get Historical Average

Query the same Notion database (Yoobin or Bloggo, whichever matched in Step 2) for all pages that have a non-empty Performance field.

Read the Performance text of each past entry and extract numeric values:
- Impressions / Views
- Saves
- Shares

Calculate simple averages. If fewer than 3 past entries exist with data, note:
> "Insufficient history for comparison (need 3+ past analyses)"
Skip the comparison and show only raw numbers.

---

## Step 5: Request Retention Screenshot

Say to the user:
> "Please paste or upload your Instagram retention screenshot for this post (Instagram app → Insights → the post → scroll to 'Plays by second'). I'll analyze the drop-off point."

Wait for the user to provide an image or describe what the retention curve shows (e.g. "dropped at 3.2 seconds").

---

## Step 6: Generate Analysis

Using all collected data, generate the following analysis block:

```
[DATE — today's date]
Views: [impressions] | Saves: [saved] | Shares: [shares] | Reach: [reach]
vs avg: Views [+/-X% or "first entry"] | Saves [+/-Xx or "first entry"] | Shares [+/-X%]

[Retention insight — where the drop-off occurred based on screenshot and why it likely happened]

→ Hook rewrites:
  1. [rewrite 1 — curiosity angle, 5–8 words]
  2. [rewrite 2 — relatable angle, 5–8 words]
  3. [rewrite 3 — bold/controversial angle, 5–8 words]

→ Next time: [1–2 specific, actionable improvement notes grounded in the data]
```

Always read `docs/marketing/bloggo-brand.md` before writing hook rewrites to ensure tone matches the brand voice. All rewrites must follow the brand's Do/Don't writing guidelines.

---

## Step 7: Append to Notion Performance Column

Find the Notion page ID from Step 2.

Read the current value of the Performance field on that page.

Build the new value:
- If Performance field is currently empty: use the analysis block as-is
- If Performance field already has content: prepend a divider `---` then append the new analysis block below the existing content

Patch the page using the correct API:
- Yoobin post → `mcp__notion-personal__API-patch-page`
- Bloggo post → `mcp__notion__API-patch-page`

Update the `Performance` property (type: text/rich_text) with the combined content.

Confirm to the user:
> "✅ Analysis appended to '[post title]' in Notion."
