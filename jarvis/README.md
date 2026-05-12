# Jarvis — Voice Assistant

Always-on Windows voice assistant. Activate with "Hey Jarvis" or Ctrl+Space.

## Setup

### 1. Install dependencies
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment
Copy `.env.example` to `.env` and fill in:

```
ANTHROPIC_API_KEY=   # from console.anthropic.com
SPOTIFY_CLIENT_ID=   # from developer.spotify.com (Premium required)
SPOTIFY_CLIENT_SECRET=
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
```

### 3. Gmail setup
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a project → enable Gmail API
3. Create OAuth credentials (Desktop app) → download as `credentials.json`
4. Place `credentials.json` in the project root
5. On first run, a browser window opens for OAuth consent

### 4. Run
```
python -m jarvis.main
```

## Commands

Say anything naturally. Examples:
- "Hey Jarvis, play Kendrick Lamar"
- "What time is it?"
- "Open Spotify"
- "Send an email to intern@example.com, subject Reminder, tell them the meeting is at 3pm"
- "Search for the best coffee shops in Tokyo"
- "Set volume to 60"
- "Type hello world"

## Hotkey
Default: `Ctrl+Space` — hold to record, release when done speaking.
Change via `HOTKEY` in `.env`.
