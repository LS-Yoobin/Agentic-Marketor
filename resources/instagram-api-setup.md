# Instagram API Setup Guide

One-time setup to connect the Performance Feedback Agent to your Instagram account.
Takes approximately 15–20 minutes.

---

## Prerequisites

- Instagram account switched to **Professional** (Creator or Business)
- A **Facebook Page** linked to your Instagram
- A free account at **developers.facebook.com**

---

## Step 1: Create a Meta App

1. Go to [developers.facebook.com](https://developers.facebook.com)
2. Click **My Apps** → **Create App**
3. Select **Other** → **Business**
4. Give your app a name (e.g. "Yoobin Analytics") → click **Create App**

---

## Step 2: Add Instagram Graph API Product

1. In your app dashboard, click **Add Product**
2. Find **Instagram Graph API** → click **Set Up**

---

## Step 3: Generate a User Access Token

1. Go to **Tools** → **Graph API Explorer**
2. Select your app from the dropdown
3. Click **Generate Access Token**
4. Log in with Facebook and grant permissions:
   - `instagram_basic`
   - `instagram_manage_insights`
   - `pages_show_list`
   - `pages_read_engagement`
5. Copy the short-lived token

---

## Step 4: Exchange for a Long-Lived Token

Run this in your terminal (replace values).

**Windows (PowerShell):** use `curl.exe` — plain `curl` in PowerShell is a different command and won't work:

```bash
curl.exe -i -X GET "https://graph.facebook.com/v18.0/oauth/access_token?grant_type=fb_exchange_token&client_id=YOUR_APP_ID&client_secret=YOUR_APP_SECRET&fb_exchange_token=SHORT_LIVED_TOKEN"
```

Copy the `access_token` from the response. This token lasts **60 days**.

---

## Step 5: Get Your Instagram User ID

```bash
curl.exe "https://graph.facebook.com/v18.0/me/accounts?access_token=YOUR_LONG_TOKEN"
```

Find the Page ID, then:

```bash
curl.exe "https://graph.facebook.com/v18.0/YOUR_PAGE_ID?fields=instagram_business_account&access_token=YOUR_LONG_TOKEN"
```

Copy the `instagram_business_account.id` value.

---

## Step 6: Fill in .env

Open `.env` in the project root and fill in all values:

```
INSTAGRAM_APP_ID=your_app_id
INSTAGRAM_APP_SECRET=your_app_secret
INSTAGRAM_ACCESS_TOKEN=your_long_lived_token
INSTAGRAM_TOKEN_EXPIRY=2026-06-12
INSTAGRAM_USER_ID=your_instagram_user_id
```

---

## Token Refresh (every 60 days)

When the agent warns you about token expiry, run this to refresh:

```bash
curl.exe -i -X GET "https://graph.facebook.com/v18.0/oauth/access_token?grant_type=fb_exchange_token&client_id=YOUR_APP_ID&client_secret=YOUR_APP_SECRET&fb_exchange_token=YOUR_CURRENT_TOKEN"
```

Update `INSTAGRAM_ACCESS_TOKEN` and `INSTAGRAM_TOKEN_EXPIRY` in `.env`.

---

## Testing the Connection

Once `.env` is filled in, test it by saying in Claude Code:
> "Test my Instagram API connection"

The agent will call `GET /me/media` and list your 5 most recent posts.
