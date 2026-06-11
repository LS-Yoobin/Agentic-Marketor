# Jarvis Voice Assistant — Design Spec

**Date:** 2026-05-11
**Status:** Approved

---

## Overview

A always-available Windows voice assistant inspired by Jarvis from Iron Man. Activated via wake word ("Hey Jarvis") or a global hotkey, it listens to natural language commands, uses Claude API with tool use to understand intent, executes integrations (Spotify, Gmail, computer control), speaks responses back via TTS, and displays text in an always-on-top overlay.

---

## Architecture

### Core Pipeline

```
[Wake word (OpenWakeWord) / Global Hotkey (keyboard lib)]
        ↓
[Record audio until silence]
        ↓
[faster-whisper → transcribed text]
        ↓
[Claude API — tool use — with last 6 exchanges as context]
        ↓
[Tool executor runs tool(s) OR returns plain text response]
        ↓
[Edge-TTS speaks response aloud]
[PyQt overlay displays transcription + response]
```

### Why Claude Tool Use (not rule-based)

Natural language routing — no rigid command phrases required. Claude reads intent and calls the appropriate tool. Handles ambiguous, casual, or chained requests gracefully.

---

## Components

### `main.py` — Orchestrator
- Initializes all components at startup
- Runs the main event loop
- Connects listener → transcriber → brain → speaker/overlay

### `listener.py` — Audio Trigger
- **Wake word**: OpenWakeWord model running in background thread, always monitoring mic
- **Hotkey**: Global `keyboard` hotkey (default: `Ctrl+Space`), hold to talk, release to stop
- On trigger: records audio, stops when silence exceeds 1.5 seconds (RMS below -40 dB) or after 30-second max timeout
- Minimum recording duration: 0.5 seconds (prevents accidental single-word captures)
- Both modes hand off a raw audio buffer to the transcriber
- On startup, logs a warning if `Ctrl+Space` is already registered by another process

### `transcriber.py` — Speech-to-Text
- Uses `faster-whisper` (local, no API cost)
- Model: `base.en` (fast, accurate for English)
- Returns plain text string

### `brain.py` — Claude API + Tool Routing
- Sends transcribed text to Claude with:
  - System prompt defining Jarvis personality
  - All tool definitions
  - Last 6 conversation turns as history (serialized as `{role, content}` pairs; tool results summarized to max 200 chars to stay under token limits)
  - Estimated max context per turn: ~500 tokens; 6 turns ≈ 3,000 tokens, well within Claude's window
- Parses Claude's response: either a tool call or plain text
- Executes tool via tool dispatcher, feeds result back to Claude for final response
- On tool execution error: Claude is notified with `{"error": "<reason>"}` and responds with a natural language apology to the user (e.g., "I couldn't connect to Spotify — make sure it's open.")
- Malformed tool results are NOT stored in conversation history to prevent context corruption

### `speaker.py` — Text-to-Speech
- Uses `edge-tts` (Microsoft Edge TTS, free, high quality)
- Default voice: `en-GB-RyanNeural` (British male, classic Jarvis feel)
- Async playback — doesn't block the UI

### `overlay.py` — Always-on-Top UI
- PyQt6 small translucent window, top-right corner of screen
- Shows:
  - Listening indicator (pulsing dot when active)
  - Transcribed user text
  - Jarvis text response
- Minimizes to system tray when not in use; click tray icon to restore
- Uses `Qt.WindowStaysOnTopHint` but NOT `Qt.WindowDoNotAcceptFocus` — prevents stealing keyboard focus from active apps
- Auto-hides after 8 seconds of inactivity to avoid obstructing full-screen apps

### `config.py` — Settings
- All sensitive values loaded from `.env` file via `python-dotenv` (never hardcoded)
- All file paths use `pathlib.Path` relative to project root — no absolute paths
- Settings:
  - `ANTHROPIC_API_KEY`
  - `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, `SPOTIFY_REDIRECT_URI`
  - `GMAIL_CREDENTIALS_PATH` (default: `./credentials.json`)
  - `WAKE_WORD_SENSITIVITY` (default: 0.5)
  - `HOTKEY` (default: `ctrl+space`)
  - `TTS_VOICE` (default: `en-GB-RyanNeural`)
  - `WHISPER_MODEL` (default: `base.en`)

---

## Tools

| Tool | Parameters | Description |
|------|-----------|-------------|
| `play_music` | `query: str` | Search Spotify and play matching track/artist/playlist |
| `pause_music` | — | Pause current Spotify playback |
| `resume_music` | — | Resume Spotify playback |
| `skip_track` | — | Skip to next track |
| `send_email` | `to: str, subject: str, body: str` | Send email via Gmail |
| `read_emails` | `count: int` | Read N most recent inbox emails, return summaries |
| `open_app` | `name: str` | Launch application by name (e.g. "Chrome", "Notion") |
| `type_text` | `text: str` | Type text at current cursor position |
| `adjust_volume` | `level: int` | Set system volume 0–100 |
| `search_web` | `query: str` | Open default browser with search query |
| `get_datetime` | — | Return current date and time |

---

## Integrations

### Spotify
- Library: `spotipy`
- Auth: Spotify Web API OAuth (PKCE flow, credentials stored in `config.py`)
- Requires: Spotify Premium (playback control API requirement)
- On startup: checks for Premium status via `current_user()` API; if free tier detected, Jarvis warns: "Spotify Premium is required for playback control." and disables Spotify tools gracefully

### Gmail
- Library: `google-api-python-client`
- Auth: OAuth2 via `credentials.json` (Google Cloud Console)
- Scopes: `gmail.send`, `gmail.readonly`
- First-time setup: user downloads `credentials.json` from Google Cloud Console (documented in README). On first run, browser opens for OAuth consent. Token saved to `token.json` for future sessions. If `token.json` expires, re-auth is triggered automatically.

### Computer Control
- Library: `pyautogui` for typing/mouse
- Library: `subprocess` for launching apps
- Library: `pycaw` for Windows audio control

---

## Conversation Memory

- Rolling window of last 6 exchanges stored in memory during session
- Cleared on restart (no persistence between sessions in v1)
- Enables follow-up commands: *"make it louder"*, *"send it to John too"*

---

## File Structure

```
jarvis/
├── main.py
├── listener.py
├── transcriber.py
├── brain.py
├── speaker.py
├── overlay.py
├── config.py
├── tools/
│   ├── __init__.py
│   ├── spotify.py
│   ├── email_tool.py
│   └── computer.py
├── requirements.txt
└── README.md
```

---

## Requirements

```
faster-whisper
openwakeword
keyboard
edge-tts
PyQt6
anthropic
spotipy
google-api-python-client
google-auth-httplib2
google-auth-oauthlib
pyautogui
pycaw
comtypes
python-dotenv
sounddevice
numpy
```

---

## Setup Steps (for README)

1. Clone repo, create virtualenv, `pip install -r requirements.txt`
2. Add Anthropic API key to `config.py`
3. Create Spotify app at developer.spotify.com → add client ID/secret to `config.py`
4. Create Google Cloud project → enable Gmail API → download `credentials.json`
5. Run `python main.py`
6. Say "Hey Jarvis" or press `Ctrl+Space`

---

## Out of Scope (v1)

- Cross-session memory / conversation history persistence
- Custom wake word training
- Android/Mac support
- Vision (screen reading)
- Calendar integration
- Multi-user support
