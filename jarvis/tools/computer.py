import subprocess
import webbrowser
from datetime import datetime
import pyautogui

pyautogui.FAILSAFE = False

# Lazy imports - these will be imported on first use to allow mocking
AudioUtilities = None
IAudioEndpointVolume = None
CLSCTX_ALL = None


def _ensure_audio_imports():
    """Lazy load audio imports on first use."""
    global AudioUtilities, IAudioEndpointVolume, CLSCTX_ALL
    if AudioUtilities is None:
        from pycaw.pycaw import AudioUtilities as AU, IAudioEndpointVolume as IAE
        from comtypes import CLSCTX_ALL as CLSCTX
        AudioUtilities = AU
        IAudioEndpointVolume = IAE
        CLSCTX_ALL = CLSCTX


def open_app(name: str) -> str:
    subprocess.Popen([name], shell=True)
    return f"Opening {name}."


def type_text(text: str) -> str:
    pyautogui.typewrite(text, interval=0.05)
    return f"Typed: {text}"


def adjust_volume(level: int) -> str:
    _ensure_audio_imports()

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
