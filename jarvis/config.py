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
