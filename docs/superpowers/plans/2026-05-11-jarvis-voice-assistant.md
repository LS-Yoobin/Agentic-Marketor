# Jarvis Voice Assistant Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Windows voice assistant that activates via wake word or hotkey, transcribes speech locally, routes commands to Claude with tool use, and responds with a British TTS voice + on-screen overlay.

**Architecture:** Audio triggers (wake word / hotkey) → faster-whisper STT → Claude API with tool definitions → tool executor → Edge-TTS voice + PyQt overlay. All components are independent modules wired together in main.py.

**Tech Stack:** Python 3.11+, faster-whisper, openwakeword, keyboard, anthropic SDK, spotipy, google-api-python-client, edge-tts, PyQt6, sounddevice, pycaw, pyautogui, python-dotenv, pytest

---

## File Map

| File | Responsibility |
|------|---------------|
| `jarvis/config.py` | Load all settings from `.env`, expose typed constants |
| `jarvis/transcriber.py` | Wrap faster-whisper, accept audio bytes → return text |
| `jarvis/speaker.py` | Wrap edge-tts, speak text async |
| `jarvis/listener.py` | Hotkey + wake word detection, audio capture with silence detection |
| `jarvis/tools/__init__.py` | Tool registry: maps tool names → callables + Claude tool schemas |
| `jarvis/tools/computer.py` | open_app, type_text, adjust_volume, search_web, get_datetime |
| `jarvis/tools/spotify.py` | play_music, pause_music, resume_music, skip_track |
| `jarvis/tools/email_tool.py` | send_email, read_emails |
| `jarvis/brain.py` | Claude API call with tools, conversation history, tool dispatch |
| `jarvis/overlay.py` | PyQt6 always-on-top overlay window |
| `jarvis/main.py` | Wire all components together, run event loop |
| `tests/test_config.py` | Config loading from env vars |
| `tests/test_transcriber.py` | Whisper wrapper with mocked model |
| `tests/test_brain.py` | Claude routing, tool dispatch, history management |
| `tests/test_speaker.py` | TTS wrapper with mocked edge-tts |
| `tests/tools/test_computer.py` | Computer tools with mocked subprocess/pyautogui/pycaw |
| `tests/tools/test_spotify.py` | Spotify tools with mocked spotipy |
| `tests/tools/test_email_tool.py` | Email tools with mocked Gmail API |
| `.env.example` | Template for required environment variables |
| `requirements.txt` | All dependencies pinned |
| `README.md` | Setup guide |

---

## Task 1: Project Scaffolding

**Files:**
- Create: `jarvis/` (directory)
- Create: `jarvis/__init__.py`
- Create: `jarvis/tools/__init__.py` (empty for now)
- Create: `tests/__init__.py`
- Create: `tests/tools/__init__.py`
- Create: `requirements.txt`
- Create: `.env.example`
- Create: `pytest.ini`

- [ ] **Step 1: Create directory structure**

```
mkdir jarvis
mkdir jarvis\tools
mkdir tests
mkdir tests\tools
```

- [ ] **Step 2: Create requirements.txt**

```
faster-whisper==1.1.0
openwakeword==0.6.0
keyboard==0.13.5
edge-tts==6.1.10
PyQt6==6.7.0
anthropic==0.40.0
spotipy==2.24.0
google-api-python-client==2.143.0
google-auth-httplib2==0.2.0
google-auth-oauthlib==1.2.1
pyautogui==0.9.54
pycaw==20240210
comtypes==1.4.4
python-dotenv==1.0.1
sounddevice==0.5.0
numpy==1.26.4
pytest==8.3.2
pytest-asyncio==0.24.0
```

- [ ] **Step 3: Create .env.example**

```
ANTHROPIC_API_KEY=your_key_here
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
GMAIL_CREDENTIALS_PATH=./credentials.json
WAKE_WORD_SENSITIVITY=0.5
HOTKEY=ctrl+space
TTS_VOICE=en-GB-RyanNeural
WHISPER_MODEL=base.en
```

- [ ] **Step 4: Create pytest.ini**

```ini
[pytest]
testpaths = tests
asyncio_mode = auto
```

- [ ] **Step 5: Create empty `__init__.py` files**

```python
# jarvis/__init__.py  (empty)
# jarvis/tools/__init__.py  (empty for now)
# tests/__init__.py  (empty)
# tests/tools/__init__.py  (empty)
```

- [ ] **Step 6: Install dependencies**

```
pip install -r requirements.txt
```

- [ ] **Step 7: Commit**

```bash
git add .
git commit -m "feat: scaffold jarvis project structure"
```

---

## Task 2: Config Module

**Files:**
- Create: `jarvis/config.py`
- Create: `tests/test_config.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_config.py
import os
import pytest
from unittest.mock import patch


def test_config_loads_anthropic_key():
    with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"}):
        import importlib
        import jarvis.config as cfg
        importlib.reload(cfg)
        assert cfg.ANTHROPIC_API_KEY == "test-key"


def test_config_defaults():
    with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "k"}, clear=True):
        import importlib
        import jarvis.config as cfg
        importlib.reload(cfg)
        assert cfg.HOTKEY == "ctrl+space"
        assert cfg.TTS_VOICE == "en-GB-RyanNeural"
        assert cfg.WHISPER_MODEL == "base.en"
        assert cfg.WAKE_WORD_SENSITIVITY == 0.5


def test_config_raises_if_anthropic_key_missing():
    with patch.dict(os.environ, {}, clear=True):
        import importlib
        import jarvis.config as cfg
        with pytest.raises(ValueError, match="ANTHROPIC_API_KEY"):
            importlib.reload(cfg)
```

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/test_config.py -v
```
Expected: FAIL — module doesn't exist yet

- [ ] **Step 3: Write config.py**

```python
# jarvis/config.py
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

def _require(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise ValueError(f"{key} is required in .env")
    return val

ANTHROPIC_API_KEY = _require("ANTHROPIC_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI", "http://localhost:8888/callback")
_project_root = Path(__file__).parent.parent
GMAIL_CREDENTIALS_PATH = Path(os.getenv("GMAIL_CREDENTIALS_PATH",
                               str(_project_root / "credentials.json")))
WAKE_WORD_SENSITIVITY = float(os.getenv("WAKE_WORD_SENSITIVITY", "0.5"))
HOTKEY = os.getenv("HOTKEY", "ctrl+space")
TTS_VOICE = os.getenv("TTS_VOICE", "en-GB-RyanNeural")
WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base.en")
```

- [ ] **Step 4: Run tests to verify they pass**

```
pytest tests/test_config.py -v
```
Expected: 3 PASS

- [ ] **Step 5: Commit**

```bash
git add jarvis/config.py tests/test_config.py
git commit -m "feat: add config module with .env loading"
```

---

## Task 3: Transcriber (Speech-to-Text)

**Files:**
- Create: `jarvis/transcriber.py`
- Create: `tests/test_transcriber.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_transcriber.py
from unittest.mock import MagicMock, patch
import numpy as np


def test_transcribe_returns_text():
    mock_model = MagicMock()
    mock_segment = MagicMock()
    mock_segment.text = " Hello Jarvis"
    mock_model.transcribe.return_value = ([mock_segment], None)

    with patch("faster_whisper.WhisperModel", return_value=mock_model):
        from jarvis.transcriber import Transcriber
        t = Transcriber(model_size="base.en")
        audio = np.zeros(16000, dtype=np.float32)
        result = t.transcribe(audio)
        assert result == "Hello Jarvis"


def test_transcribe_returns_empty_string_on_silence():
    mock_model = MagicMock()
    mock_model.transcribe.return_value = ([], None)

    with patch("faster_whisper.WhisperModel", return_value=mock_model):
        from jarvis.transcriber import Transcriber
        t = Transcriber(model_size="base.en")
        audio = np.zeros(16000, dtype=np.float32)
        result = t.transcribe(audio)
        assert result == ""
```

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/test_transcriber.py -v
```
Expected: FAIL

- [ ] **Step 3: Write transcriber.py**

```python
# jarvis/transcriber.py
import numpy as np
from faster_whisper import WhisperModel


class Transcriber:
    def __init__(self, model_size: str = "base.en"):
        self._model = WhisperModel(model_size, device="cpu", compute_type="int8")

    def transcribe(self, audio: np.ndarray) -> str:
        segments, _ = self._model.transcribe(audio, language="en")
        return " ".join(s.text.strip() for s in segments).strip()
```

- [ ] **Step 4: Run tests to verify they pass**

```
pytest tests/test_transcriber.py -v
```
Expected: 2 PASS

- [ ] **Step 5: Commit**

```bash
git add jarvis/transcriber.py tests/test_transcriber.py
git commit -m "feat: add whisper transcriber module"
```

---

## Task 4: Speaker (Text-to-Speech)

**Files:**
- Create: `jarvis/speaker.py`
- Create: `tests/test_speaker.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_speaker.py
import asyncio
from unittest.mock import AsyncMock, patch, MagicMock


def test_speak_calls_edge_tts():
    mock_communicate = MagicMock()
    mock_communicate.play = AsyncMock()

    with patch("edge_tts.Communicate", return_value=mock_communicate):
        from jarvis.speaker import Speaker
        s = Speaker(voice="en-GB-RyanNeural")
        s.speak("Hello there")
        mock_communicate.play.assert_called_once()


def test_speak_strips_empty_string():
    with patch("edge_tts.Communicate") as mock_cls:
        from jarvis.speaker import Speaker
        s = Speaker(voice="en-GB-RyanNeural")
        s.speak("   ")
        mock_cls.assert_not_called()
```

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/test_speaker.py -v
```
Expected: FAIL

- [ ] **Step 3: Write speaker.py**

```python
# jarvis/speaker.py
import asyncio
import edge_tts


class Speaker:
    def __init__(self, voice: str = "en-GB-RyanNeural"):
        self._voice = voice

    def speak(self, text: str) -> None:
        if not text.strip():
            return
        asyncio.run(self._speak_async(text))

    async def _speak_async(self, text: str) -> None:
        communicate = edge_tts.Communicate(text, self._voice)
        await communicate.play()
```

- [ ] **Step 4: Run tests to verify they pass**

```
pytest tests/test_speaker.py -v
```
Expected: 2 PASS

- [ ] **Step 5: Commit**

```bash
git add jarvis/speaker.py tests/test_speaker.py
git commit -m "feat: add edge-tts speaker module"
```

---

## Task 5: Computer Control Tools

**Files:**
- Create: `jarvis/tools/computer.py`
- Create: `tests/tools/test_computer.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/tools/test_computer.py
from unittest.mock import patch, MagicMock
import subprocess


def test_open_app_launches_process():
    with patch("subprocess.Popen") as mock_popen:
        from jarvis.tools.computer import open_app
        result = open_app("notepad")
        mock_popen.assert_called_once_with(["notepad"], shell=True)
        assert "Opening" in result


def test_type_text_calls_pyautogui():
    with patch("pyautogui.typewrite") as mock_type:
        from jarvis.tools.computer import type_text
        result = type_text("hello world")
        mock_type.assert_called_once_with("hello world", interval=0.05)
        assert "Typed" in result


def test_adjust_volume_clamps_to_range():
    mock_sessions = MagicMock()
    mock_volume = MagicMock()
    with patch("pycaw.pycaw.AudioUtilities.GetAllSessions", return_value=[]):
        with patch("pycaw.pycaw.AudioUtilities.GetSpeakers") as mock_spk:
            mock_spk.return_value.Activate.return_value.QueryInterface.return_value = mock_volume
            from jarvis.tools.computer import adjust_volume
            result = adjust_volume(150)  # should clamp to 100
            mock_volume.SetMasterVolumeLevelScalar.assert_called_once_with(1.0, None)
            assert "100" in result


def test_get_datetime_returns_string():
    from jarvis.tools.computer import get_datetime
    result = get_datetime()
    assert "2026" in result or len(result) > 5


def test_search_web_opens_browser():
    with patch("webbrowser.open") as mock_open:
        from jarvis.tools.computer import search_web
        result = search_web("python tutorials")
        mock_open.assert_called_once()
        assert "Searching" in result
```

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/tools/test_computer.py -v
```
Expected: FAIL

- [ ] **Step 3: Write computer.py**

```python
# jarvis/tools/computer.py
import subprocess
import webbrowser
from datetime import datetime
import pyautogui
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import ctypes

pyautogui.FAILSAFE = False


def open_app(name: str) -> str:
    subprocess.Popen([name], shell=True)
    return f"Opening {name}."


def type_text(text: str) -> str:
    pyautogui.typewrite(text, interval=0.05)
    return f"Typed: {text}"


def adjust_volume(level: int) -> str:
    level = max(0, min(100, level))
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volume.SetMasterVolumeLevelScalar(level / 100.0, None)
    return f"Volume set to {level}%."


def search_web(query: str) -> str:
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)
    return f"Searching for: {query}"


def get_datetime() -> str:
    now = datetime.now()
    return now.strftime("It's %A, %B %d %Y at %I:%M %p.")
```

- [ ] **Step 4: Run tests to verify they pass**

```
pytest tests/tools/test_computer.py -v
```
Expected: 5 PASS

- [ ] **Step 5: Commit**

```bash
git add jarvis/tools/computer.py tests/tools/test_computer.py
git commit -m "feat: add computer control tools"
```

---

## Task 6: Spotify Tools

**Files:**
- Create: `jarvis/tools/spotify.py`
- Create: `tests/tools/test_spotify.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/tools/test_spotify.py
from unittest.mock import MagicMock, patch


def _make_spotify_tool(premium=True):
    mock_sp = MagicMock()
    mock_sp.current_user.return_value = {
        "product": "premium" if premium else "free"
    }
    mock_sp.search.return_value = {
        "tracks": {"items": [{"uri": "spotify:track:abc123", "name": "Test Song"}]}
    }
    return mock_sp


def test_play_music_searches_and_plays():
    mock_sp = _make_spotify_tool()
    with patch("spotipy.Spotify", return_value=mock_sp):
        with patch("spotipy.oauth2.SpotifyOAuth"):
            from jarvis.tools.spotify import SpotifyTools
            s = SpotifyTools(mock_sp)
            result = s.play_music("Kendrick Lamar")
            mock_sp.start_playback.assert_called_once()
            assert "Playing" in result


def test_play_music_handles_no_results():
    mock_sp = _make_spotify_tool()
    mock_sp.search.return_value = {"tracks": {"items": []}}
    with patch("spotipy.Spotify", return_value=mock_sp):
        from jarvis.tools.spotify import SpotifyTools
        s = SpotifyTools(mock_sp)
        result = s.play_music("xyznotatrack123")
        assert "couldn't find" in result.lower()


def test_pause_music():
    mock_sp = _make_spotify_tool()
    from jarvis.tools.spotify import SpotifyTools
    s = SpotifyTools(mock_sp)
    result = s.pause_music()
    mock_sp.pause_playback.assert_called_once()
    assert "Paused" in result


def test_skip_track():
    mock_sp = _make_spotify_tool()
    from jarvis.tools.spotify import SpotifyTools
    s = SpotifyTools(mock_sp)
    result = s.skip_track()
    mock_sp.next_track.assert_called_once()
    assert "Skipped" in result
```

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/tools/test_spotify.py -v
```
Expected: FAIL

- [ ] **Step 3: Write spotify.py**

```python
# jarvis/tools/spotify.py
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from jarvis import config


def create_spotify_client() -> spotipy.Spotify | None:
    if not config.SPOTIFY_CLIENT_ID:
        return None
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=config.SPOTIFY_CLIENT_ID,
        client_secret=config.SPOTIFY_CLIENT_SECRET,
        redirect_uri=config.SPOTIFY_REDIRECT_URI,
        scope="user-modify-playback-state user-read-playback-state"
    ))
    try:
        user = sp.current_user()
        if user.get("product") != "premium":
            print("Warning: Spotify Premium required for playback control.")
            return None
    except Exception:
        return None
    return sp


class SpotifyTools:
    def __init__(self, client: spotipy.Spotify):
        self._sp = client

    def play_music(self, query: str) -> str:
        results = self._sp.search(q=query, limit=1, type="track")
        items = results["tracks"]["items"]
        if not items:
            return f"I couldn't find anything matching '{query}' on Spotify."
        uri = items[0]["uri"]
        name = items[0]["name"]
        self._sp.start_playback(uris=[uri])
        return f"Playing {name}."

    def pause_music(self) -> str:
        self._sp.pause_playback()
        return "Paused."

    def resume_music(self) -> str:
        self._sp.start_playback()
        return "Resumed."

    def skip_track(self) -> str:
        self._sp.next_track()
        return "Skipped to next track."
```

- [ ] **Step 4: Run tests to verify they pass**

```
pytest tests/tools/test_spotify.py -v
```
Expected: 4 PASS

- [ ] **Step 5: Commit**

```bash
git add jarvis/tools/spotify.py tests/tools/test_spotify.py
git commit -m "feat: add spotify tools"
```

---

## Task 7: Email Tools

**Files:**
- Create: `jarvis/tools/email_tool.py`
- Create: `tests/tools/test_email_tool.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/tools/test_email_tool.py
from unittest.mock import MagicMock, patch


def _mock_gmail_service():
    service = MagicMock()
    msg_resource = service.users.return_value.messages.return_value
    msg_resource.send.return_value.execute.return_value = {"id": "abc"}
    msg_resource.list.return_value.execute.return_value = {
        "messages": [{"id": "1"}, {"id": "2"}]
    }
    msg_resource.get.return_value.execute.return_value = {
        "snippet": "Test email snippet",
        "payload": {"headers": [
            {"name": "From", "value": "test@example.com"},
            {"name": "Subject", "value": "Test Subject"}
        ]}
    }
    return service


def test_send_email_calls_gmail_api():
    mock_service = _mock_gmail_service()
    with patch("jarvis.tools.email_tool.build_gmail_service", return_value=mock_service):
        from jarvis.tools.email_tool import EmailTools
        e = EmailTools(mock_service)
        result = e.send_email("intern@example.com", "Reminder", "Don't forget the meeting.")
        mock_service.users().messages().send.assert_called_once()
        assert "Sent" in result


def test_read_emails_returns_summaries():
    mock_service = _mock_gmail_service()
    with patch("jarvis.tools.email_tool.build_gmail_service", return_value=mock_service):
        from jarvis.tools.email_tool import EmailTools
        e = EmailTools(mock_service)
        result = e.read_emails(2)
        assert "Test Subject" in result or "snippet" in result.lower()
```

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/tools/test_email_tool.py -v
```
Expected: FAIL

- [ ] **Step 3: Write email_tool.py**

```python
# jarvis/tools/email_tool.py
import base64
from email.mime.text import MIMEText
from pathlib import Path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from jarvis import config

SCOPES = ["https://www.googleapis.com/auth/gmail.send",
          "https://www.googleapis.com/auth/gmail.readonly"]
TOKEN_PATH = Path("./token.json")


def build_gmail_service():
    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                config.GMAIL_CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_PATH.write_text(creds.to_json())
    return build("gmail", "v1", credentials=creds)


class EmailTools:
    def __init__(self, service):
        self._service = service

    def send_email(self, to: str, subject: str, body: str) -> str:
        msg = MIMEText(body)
        msg["to"] = to
        msg["subject"] = subject
        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        self._service.users().messages().send(
            userId="me", body={"raw": raw}).execute()
        return f"Sent email to {to}."

    def read_emails(self, count: int = 5) -> str:
        results = self._service.users().messages().list(
            userId="me", maxResults=count).execute()
        messages = results.get("messages", [])
        if not messages:
            return "Your inbox is empty."
        summaries = []
        for m in messages:
            msg = self._service.users().messages().get(
                userId="me", id=m["id"], format="full").execute()
            headers = {h["name"]: h["value"]
                       for h in msg["payload"]["headers"]}
            summaries.append(
                f"From: {headers.get('From', '?')} | "
                f"Subject: {headers.get('Subject', '?')} | "
                f"{msg.get('snippet', '')[:80]}"
            )
        return "\n".join(summaries)
```

- [ ] **Step 4: Run tests to verify they pass**

```
pytest tests/tools/test_email_tool.py -v
```
Expected: 2 PASS

- [ ] **Step 5: Commit**

```bash
git add jarvis/tools/email_tool.py tests/tools/test_email_tool.py
git commit -m "feat: add gmail email tools"
```

---

## Task 8: Tool Registry

**Files:**
- Modify: `jarvis/tools/__init__.py`
- Create: `tests/tools/test_registry.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/tools/test_registry.py
from unittest.mock import MagicMock, patch


def test_all_tools_registered():
    mock_sp = MagicMock()
    mock_gmail = MagicMock()
    with patch("jarvis.tools.spotify.create_spotify_client", return_value=mock_sp):
        with patch("jarvis.tools.email_tool.build_gmail_service", return_value=mock_gmail):
            from jarvis.tools import build_tool_registry
            registry = build_tool_registry()
            expected = {
                "play_music", "pause_music", "resume_music", "skip_track",
                "send_email", "read_emails",
                "open_app", "type_text", "adjust_volume", "search_web", "get_datetime"
            }
            assert set(registry["functions"].keys()) == expected
            assert len(registry["schemas"]) == len(expected)


def test_tool_schemas_have_required_fields():
    mock_sp = MagicMock()
    mock_gmail = MagicMock()
    with patch("jarvis.tools.spotify.create_spotify_client", return_value=mock_sp):
        with patch("jarvis.tools.email_tool.build_gmail_service", return_value=mock_gmail):
            from jarvis.tools import build_tool_registry
            registry = build_tool_registry()
            for schema in registry["schemas"]:
                assert "name" in schema
                assert "description" in schema
                assert "input_schema" in schema
```

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/tools/test_registry.py -v
```
Expected: FAIL

- [ ] **Step 3: Write tools/__init__.py**

```python
# jarvis/tools/__init__.py
from jarvis.tools.computer import open_app, type_text, adjust_volume, search_web, get_datetime
from jarvis.tools.spotify import SpotifyTools, create_spotify_client
from jarvis.tools.email_tool import EmailTools, build_gmail_service


def build_tool_registry() -> dict:
    spotify = create_spotify_client()

    gmail = None
    try:
        gmail = build_gmail_service()
    except Exception as e:
        print(f"Gmail not available: {e}")

    spotify_tools = SpotifyTools(spotify) if spotify else None
    email_tools = EmailTools(gmail) if gmail else None

    def _disabled(name):
        return lambda **_: f"{name} is not available (check credentials)."

    functions = {
        "open_app": lambda name: open_app(name),
        "type_text": lambda text: type_text(text),
        "adjust_volume": lambda level: adjust_volume(int(level)),
        "search_web": lambda query: search_web(query),
        "get_datetime": lambda: get_datetime(),
        "play_music": (spotify_tools.play_music if spotify_tools
                       else _disabled("Spotify")),
        "pause_music": (spotify_tools.pause_music if spotify_tools
                        else _disabled("Spotify")),
        "resume_music": (spotify_tools.resume_music if spotify_tools
                         else _disabled("Spotify")),
        "skip_track": (spotify_tools.skip_track if spotify_tools
                       else _disabled("Spotify")),
        "send_email": (email_tools.send_email if email_tools
                       else _disabled("Gmail")),
        "read_emails": (email_tools.read_emails if email_tools
                        else _disabled("Gmail")),
    }

    schemas = [
        {"name": "play_music", "description": "Search Spotify and play a track, artist, or playlist",
         "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
        {"name": "pause_music", "description": "Pause Spotify playback",
         "input_schema": {"type": "object", "properties": {}}},
        {"name": "resume_music", "description": "Resume Spotify playback",
         "input_schema": {"type": "object", "properties": {}}},
        {"name": "skip_track", "description": "Skip to next Spotify track",
         "input_schema": {"type": "object", "properties": {}}},
        {"name": "send_email", "description": "Send an email via Gmail",
         "input_schema": {"type": "object", "properties": {
             "to": {"type": "string"}, "subject": {"type": "string"}, "body": {"type": "string"}
         }, "required": ["to", "subject", "body"]}},
        {"name": "read_emails", "description": "Read recent inbox emails",
         "input_schema": {"type": "object", "properties": {
             "count": {"type": "integer", "default": 5}
         }}},
        {"name": "open_app", "description": "Open an application by name",
         "input_schema": {"type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]}},
        {"name": "type_text", "description": "Type text at the current cursor position",
         "input_schema": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}},
        {"name": "adjust_volume", "description": "Set system volume 0-100",
         "input_schema": {"type": "object", "properties": {"level": {"type": "integer"}}, "required": ["level"]}},
        {"name": "search_web", "description": "Open browser with a Google search",
         "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
        {"name": "get_datetime", "description": "Get the current date and time",
         "input_schema": {"type": "object", "properties": {}}},
    ]

    return {"functions": functions, "schemas": schemas}
```

- [ ] **Step 4: Run tests to verify they pass**

```
pytest tests/tools/test_registry.py -v
```
Expected: 2 PASS

- [ ] **Step 5: Commit**

```bash
git add jarvis/tools/__init__.py tests/tools/test_registry.py
git commit -m "feat: add tool registry with all integrations"
```

---

## Task 9: Brain (Claude API + Tool Routing)

**Files:**
- Create: `jarvis/brain.py`
- Create: `tests/test_brain.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_brain.py
from unittest.mock import MagicMock, patch


def _make_text_response(text):
    mock_resp = MagicMock()
    mock_resp.stop_reason = "end_turn"
    block = MagicMock()
    block.type = "text"
    block.text = text
    mock_resp.content = [block]
    return mock_resp


def _make_tool_response(tool_name, tool_input, tool_use_id="id1"):
    mock_resp = MagicMock()
    mock_resp.stop_reason = "tool_use"
    block = MagicMock()
    block.type = "tool_use"
    block.name = tool_name
    block.input = tool_input
    block.id = tool_use_id
    mock_resp.content = [block]
    return mock_resp


def test_brain_returns_text_response():
    mock_client = MagicMock()
    mock_client.messages.create.return_value = _make_text_response("Hello, how can I help?")
    registry = {"functions": {}, "schemas": []}

    with patch("anthropic.Anthropic", return_value=mock_client):
        from jarvis.brain import Brain
        b = Brain(api_key="test", tool_registry=registry)
        result = b.process("hello")
        assert result == "Hello, how can I help?"


def test_brain_executes_tool_and_returns_followup():
    mock_client = MagicMock()
    tool_resp = _make_tool_response("get_datetime", {})
    followup = _make_text_response("It's Monday.")
    mock_client.messages.create.side_effect = [tool_resp, followup]

    registry = {
        "functions": {"get_datetime": lambda: "It's Monday, May 11 2026 at 9:00 PM."},
        "schemas": [{"name": "get_datetime", "description": "Get date",
                     "input_schema": {"type": "object", "properties": {}}}]
    }

    with patch("anthropic.Anthropic", return_value=mock_client):
        from jarvis.brain import Brain
        b = Brain(api_key="test", tool_registry=registry)
        result = b.process("what time is it")
        assert result == "It's Monday."
        assert mock_client.messages.create.call_count == 2


def test_brain_history_capped_at_12_messages():
    mock_client = MagicMock()
    mock_client.messages.create.return_value = _make_text_response("ok")
    registry = {"functions": {}, "schemas": []}

    with patch("anthropic.Anthropic", return_value=mock_client):
        from jarvis.brain import Brain
        b = Brain(api_key="test", tool_registry=registry)
        for i in range(10):
            b.process(f"message {i}")
        call_args = mock_client.messages.create.call_args
        messages = call_args.kwargs["messages"]
        # capped at 12 and most recent message is last
        assert len(messages) <= 12
        assert messages[-1]["content"] == "message 9"


def test_brain_tool_error_not_stored_in_history():
    mock_client = MagicMock()
    tool_resp = _make_tool_response("open_app", {"name": "badapp"})
    followup = _make_text_response("I couldn't open that app.")
    mock_client.messages.create.side_effect = [tool_resp, followup]

    def broken_tool(name):
        raise RuntimeError("App not found")

    registry = {
        "functions": {"open_app": broken_tool},
        "schemas": []
    }

    with patch("anthropic.Anthropic", return_value=mock_client):
        from jarvis.brain import Brain
        b = Brain(api_key="test", tool_registry=registry)
        result = b.process("open badapp")
        assert result == "I couldn't open that app."
        # history should only have the original user message pair, not error state
        assert len(b._history) == 2
```

- [ ] **Step 2: Run test to verify it fails**

```
pytest tests/test_brain.py -v
```
Expected: FAIL

- [ ] **Step 3: Write brain.py**

```python
# jarvis/brain.py
import anthropic

SYSTEM_PROMPT = """You are Jarvis, a highly capable personal AI assistant. 
You speak in a concise, professional British tone — helpful, direct, never verbose.
You have tools to control Spotify, send emails, open apps, type text, and more.
Always use a tool if the user's request maps to one. Keep responses under 2 sentences."""

MAX_HISTORY = 12  # 6 exchanges


class Brain:
    def __init__(self, api_key: str, tool_registry: dict):
        self._client = anthropic.Anthropic(api_key=api_key)
        self._tools = tool_registry["functions"]
        self._schemas = tool_registry["schemas"]
        self._history: list[dict] = []

    def process(self, user_text: str) -> str:
        self._history.append({"role": "user", "content": user_text})
        if len(self._history) > MAX_HISTORY:
            self._history = self._history[-MAX_HISTORY:]

        response = self._client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            tools=self._schemas,
            messages=self._history,
        )

        if response.stop_reason == "tool_use":
            return self._handle_tool_use(response)

        reply = next(b.text for b in response.content if b.type == "text")
        self._history.append({"role": "assistant", "content": reply})
        return reply

    def _handle_tool_use(self, response) -> str:
        tool_block = next(b for b in response.content if b.type == "tool_use")
        tool_fn = self._tools.get(tool_block.name)

        try:
            tool_result = tool_fn(**tool_block.input) if tool_fn else "Tool not available."
        except Exception as e:
            tool_result = f'{{"error": "{str(e)}"}}'

        followup_messages = self._history + [
            {"role": "assistant", "content": response.content},
            {"role": "user", "content": [{
                "type": "tool_result",
                "tool_use_id": tool_block.id,
                "content": str(tool_result)[:200],
            }]}
        ]

        followup = self._client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=512,
            system=SYSTEM_PROMPT,
            tools=self._schemas,
            messages=followup_messages,
        )

        reply = next(b.text for b in followup.content if b.type == "text")
        # Only store clean exchange in history (not tool call internals)
        self._history.append({"role": "assistant", "content": reply})
        return reply
```

- [ ] **Step 4: Run tests to verify they pass**

```
pytest tests/test_brain.py -v
```
Expected: 4 PASS

- [ ] **Step 5: Commit**

```bash
git add jarvis/brain.py tests/test_brain.py
git commit -m "feat: add claude brain with tool use and conversation history"
```

---

## Task 10: Listener (Audio Capture + Hotkey + Wake Word)

**Files:**
- Create: `jarvis/listener.py`

> Note: `listener.py` interfaces directly with audio hardware and the keyboard driver. Unit tests require mocking at a very deep level and add little value. Manual integration testing is the right approach here.

- [ ] **Step 1: Write listener.py**

```python
# jarvis/listener.py
import threading
import queue
import numpy as np
import sounddevice as sd
import keyboard
from openwakeword.model import Model as WakeWordModel

SAMPLE_RATE = 16000
CHUNK_SIZE = 1280  # 80ms at 16kHz
SILENCE_THRESHOLD_RMS = 0.01  # ~-40 dB
SILENCE_DURATION = 1.5  # seconds of silence before stopping
MAX_DURATION = 30.0  # max recording seconds
MIN_DURATION = 0.5  # min recording seconds


class Listener:
    def __init__(
        self,
        hotkey: str = "ctrl+space",
        wake_word_sensitivity: float = 0.5,
        on_audio_ready=None,
    ):
        self._hotkey = hotkey
        self._sensitivity = wake_word_sensitivity
        self._on_audio_ready = on_audio_ready
        self._recording = False
        self._audio_buffer = []
        self._wakeword_model = None

    def start(self):
        self._check_hotkey_conflict()
        keyboard.add_hotkey(self._hotkey, self._on_hotkey_press)
        self._start_wake_word_listener()
        print(f"Jarvis ready. Say 'Hey Jarvis' or press {self._hotkey}.")

    def _check_hotkey_conflict(self):
        try:
            keyboard.add_hotkey(self._hotkey, lambda: None)
            keyboard.remove_hotkey(self._hotkey)
        except Exception:
            print(f"Warning: hotkey {self._hotkey} may conflict with another app.")

    def _on_hotkey_press(self):
        if not self._recording:
            self._start_recording()

    def _start_recording(self):
        self._recording = True
        self._audio_buffer = []
        threading.Thread(target=self._record_until_silence, daemon=True).start()

    def _record_until_silence(self):
        silence_samples = 0
        silence_limit = int(SILENCE_DURATION * SAMPLE_RATE / CHUNK_SIZE)
        max_chunks = int(MAX_DURATION * SAMPLE_RATE / CHUNK_SIZE)
        min_chunks = int(MIN_DURATION * SAMPLE_RATE / CHUNK_SIZE)
        chunks_recorded = 0

        def callback(indata, frames, time, status):
            nonlocal silence_samples, chunks_recorded
            chunk = indata[:, 0].copy()
            self._audio_buffer.append(chunk)
            chunks_recorded += 1
            rms = np.sqrt(np.mean(chunk ** 2))
            if rms < SILENCE_THRESHOLD_RMS:
                silence_samples += 1
            else:
                silence_samples = 0

        with sd.InputStream(samplerate=SAMPLE_RATE, channels=1,
                            blocksize=CHUNK_SIZE, callback=callback):
            while self._recording:
                sd.sleep(80)
                if (chunks_recorded > min_chunks and
                        silence_samples >= silence_limit):
                    break
                if chunks_recorded >= max_chunks:
                    break

        self._recording = False
        if chunks_recorded >= min_chunks and self._on_audio_ready:
            audio = np.concatenate(self._audio_buffer)
            self._on_audio_ready(audio)

    def _start_wake_word_listener(self):
        self._wakeword_model = WakeWordModel(
            wakeword_models=["hey_jarvis"],
            inference_framework="onnx"
        )
        threading.Thread(target=self._wake_word_loop, daemon=True).start()

    def _wake_word_loop(self):
        def callback(indata, frames, time, status):
            audio_chunk = (indata[:, 0] * 32768).astype(np.int16)
            predictions = self._wakeword_model.predict(audio_chunk)
            if predictions.get("hey_jarvis", 0) >= self._sensitivity:
                if not self._recording:
                    print("Wake word detected.")
                    self._start_recording()

        with sd.InputStream(samplerate=SAMPLE_RATE, channels=1,
                            blocksize=CHUNK_SIZE, dtype="float32",
                            callback=callback):
            while True:
                sd.sleep(100)
```

- [ ] **Step 2: Manual smoke test**

Create a temporary script `test_listener_manual.py`:
```python
from jarvis.listener import Listener
import time

def on_audio(audio):
    print(f"Got audio: {len(audio)} samples ({len(audio)/16000:.1f}s)")

l = Listener(hotkey="ctrl+space", on_audio_ready=on_audio)
l.start()
time.sleep(30)
```
Run it, press `Ctrl+Space`, speak a sentence, verify audio is captured.

- [ ] **Step 3: Commit**

```bash
git add jarvis/listener.py
git commit -m "feat: add audio listener with hotkey and wake word"
```

---

## Task 11: Overlay (PyQt6 UI)

**Files:**
- Create: `jarvis/overlay.py`

> PyQt6 UI components are not unit-testable without a display. Manual testing applies.

- [ ] **Step 1: Write overlay.py**

```python
# jarvis/overlay.py
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                              QSystemTrayIcon, QMenu)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QObject
from PyQt6.QtGui import QIcon, QColor, QPalette


class OverlaySignals(QObject):
    update_text = pyqtSignal(str, str)  # (user_text, jarvis_text)
    set_listening = pyqtSignal(bool)


class Overlay(QWidget):
    def __init__(self):
        super().__init__()
        self.signals = OverlaySignals()
        self.signals.update_text.connect(self._update_text)
        self.signals.set_listening.connect(self._set_listening)
        self._hide_timer = QTimer()
        self._hide_timer.setSingleShot(True)
        self._hide_timer.timeout.connect(self.hide)
        self._setup_ui()
        self._setup_tray()

    def _setup_ui(self):
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedWidth(320)

        layout = QVBoxLayout()
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(6)

        self._status_label = QLabel("●")
        self._status_label.setStyleSheet("color: #666; font-size: 10px;")

        self._user_label = QLabel("")
        self._user_label.setWordWrap(True)
        self._user_label.setStyleSheet(
            "color: #aaa; font-size: 12px; font-style: italic;")

        self._jarvis_label = QLabel("")
        self._jarvis_label.setWordWrap(True)
        self._jarvis_label.setStyleSheet(
            "color: white; font-size: 14px; font-weight: bold;")

        layout.addWidget(self._status_label)
        layout.addWidget(self._user_label)
        layout.addWidget(self._jarvis_label)
        self.setLayout(layout)

        self.setStyleSheet(
            "QWidget { background-color: rgba(15, 15, 20, 200); "
            "border-radius: 10px; }")

        screen = QApplication.primaryScreen()
        if screen:
            geo = screen.geometry()
            self.move(geo.width() - 340, 40)
        else:
            self.move(1580, 40)  # fallback for headless/multi-monitor

    def _setup_tray(self):
        self._tray = QSystemTrayIcon(self)
        self._tray.setToolTip("Jarvis")
        tray_menu = QMenu()
        tray_menu.addAction("Show", self.show)
        tray_menu.addAction("Quit", QApplication.quit)
        self._tray.setContextMenu(tray_menu)
        self._tray.activated.connect(lambda _: self.show())
        self._tray.show()

    def _update_text(self, user_text: str, jarvis_text: str):
        self._user_label.setText(f'You: "{user_text}"')
        self._jarvis_label.setText(f"Jarvis: {jarvis_text}")
        self.adjustSize()
        self.show()
        self._hide_timer.start(8000)

    def _set_listening(self, listening: bool):
        if listening:
            self._status_label.setText("● Listening...")
            self._status_label.setStyleSheet("color: #00ff88; font-size: 10px;")
            self.show()
            self._hide_timer.stop()
        else:
            self._status_label.setText("●")
            self._status_label.setStyleSheet("color: #666; font-size: 10px;")
```

- [ ] **Step 2: Manual smoke test**

Create `test_overlay_manual.py`:
```python
import sys
from PyQt6.QtWidgets import QApplication
from jarvis.overlay import Overlay
import threading, time

app = QApplication(sys.argv)
overlay = Overlay()
overlay.show()

def test_updates():
    time.sleep(1)
    overlay.signals.set_listening.emit(True)
    time.sleep(2)
    overlay.signals.set_listening.emit(False)
    overlay.signals.update_text.emit("play some music", "Playing Kendrick Lamar.")

threading.Thread(target=test_updates, daemon=True).start()
sys.exit(app.exec())
```
Run it, verify: listening dot turns green, text appears, window auto-hides after 8 seconds.

- [ ] **Step 3: Commit**

```bash
git add jarvis/overlay.py
git commit -m "feat: add pyqt6 always-on-top overlay"
```

---

## Task 12: Main Orchestrator

**Files:**
- Create: `jarvis/main.py`

- [ ] **Step 1: Write main.py**

```python
# jarvis/main.py
import sys
import threading
import numpy as np
from PyQt6.QtWidgets import QApplication

from jarvis import config
from jarvis.transcriber import Transcriber
from jarvis.speaker import Speaker
from jarvis.listener import Listener
from jarvis.brain import Brain
from jarvis.overlay import Overlay
from jarvis.tools import build_tool_registry


def main():
    app = QApplication(sys.argv)

    print("Initialising Jarvis...")
    transcriber = Transcriber(model_size=config.WHISPER_MODEL)
    speaker = Speaker(voice=config.TTS_VOICE)
    overlay = Overlay()
    tool_registry = build_tool_registry()
    brain = Brain(api_key=config.ANTHROPIC_API_KEY, tool_registry=tool_registry)

    def on_audio_ready(audio: np.ndarray):
        overlay.signals.set_listening.emit(False)

        text = transcriber.transcribe(audio)
        if not text.strip():
            return

        print(f"You: {text}")
        overlay.signals.update_text.emit(text, "...")

        def process():
            reply = brain.process(text)
            print(f"Jarvis: {reply}")
            overlay.signals.update_text.emit(text, reply)
            speaker.speak(reply)

        threading.Thread(target=process, daemon=True).start()

    listener = Listener(
        hotkey=config.HOTKEY,
        wake_word_sensitivity=config.WAKE_WORD_SENSITIVITY,
        on_audio_ready=on_audio_ready,
    )

    def on_listening_start():
        overlay.signals.set_listening.emit(True)

    # Patch listener to signal overlay on recording start
    original_start = listener._start_recording
    def patched_start():
        on_listening_start()
        original_start()
    listener._start_recording = patched_start

    listener.start()
    overlay.show()
    print("Jarvis is ready.")
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Integration test — run Jarvis end-to-end**

```
python -m jarvis.main
```
Test these commands:
- Press `Ctrl+Space`, say "What time is it?" → Jarvis responds with time
- Press `Ctrl+Space`, say "Open Notepad" → Notepad launches
- Press `Ctrl+Space`, say "Search for Python tutorials" → Browser opens
- (If Spotify credentials set) Say "Play some lo-fi music" → Spotify plays

- [ ] **Step 3: Commit**

```bash
git add jarvis/main.py
git commit -m "feat: wire all components in main orchestrator"
```

---

## Task 13: README

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write README.md**

```markdown
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
```

- [ ] **Step 2: Run full test suite**

```
pytest -v
```
Expected: All tests pass

- [ ] **Step 3: Final commit**

```bash
git add README.md
git commit -m "docs: add setup README for Jarvis"
```

---

## Run Order Summary

```
Task 1  → Scaffolding
Task 2  → config.py
Task 3  → transcriber.py
Task 4  → speaker.py
Task 5  → tools/computer.py
Task 6  → tools/spotify.py
Task 7  → tools/email_tool.py
Task 8  → tools/__init__.py (registry)
Task 9  → brain.py
Task 10 → listener.py
Task 11 → overlay.py
Task 12 → main.py
Task 13 → README.md
```
