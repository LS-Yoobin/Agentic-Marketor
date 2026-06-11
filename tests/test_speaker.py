import asyncio
from unittest.mock import AsyncMock, patch, MagicMock
import sys


def test_speak_calls_edge_tts():
    mock_communicate = MagicMock()
    mock_communicate.play = AsyncMock()

    with patch("edge_tts.Communicate", return_value=mock_communicate):
        # Remove the module from cache to force reimport with fresh patch
        if "jarvis.speaker" in sys.modules:
            del sys.modules["jarvis.speaker"]
        from jarvis.speaker import Speaker
        s = Speaker(voice="en-GB-RyanNeural")
        s.speak("Hello there")
        mock_communicate.play.assert_called_once()


def test_speak_strips_empty_string():
    with patch("edge_tts.Communicate") as mock_cls:
        # Remove the module from cache to force reimport with fresh patch
        if "jarvis.speaker" in sys.modules:
            del sys.modules["jarvis.speaker"]
        from jarvis.speaker import Speaker
        s = Speaker(voice="en-GB-RyanNeural")
        s.speak("   ")
        mock_cls.assert_not_called()
