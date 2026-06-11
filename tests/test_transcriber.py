from unittest.mock import MagicMock, patch
import numpy as np
import sys
import importlib


def test_transcribe_returns_text():
    mock_model = MagicMock()
    mock_segment = MagicMock()
    mock_segment.text = " Hello Jarvis"
    mock_model.transcribe.return_value = ([mock_segment], None)

    with patch("faster_whisper.WhisperModel", return_value=mock_model):
        # Remove the module from cache to force reimport with fresh patch
        if "jarvis.transcriber" in sys.modules:
            del sys.modules["jarvis.transcriber"]
        from jarvis.transcriber import Transcriber
        t = Transcriber(model_size="base.en")
        audio = np.zeros(16000, dtype=np.float32)
        result = t.transcribe(audio)
        assert result == "Hello Jarvis"


def test_transcribe_returns_empty_string_on_silence():
    mock_model = MagicMock()
    mock_model.transcribe.return_value = ([], None)

    with patch("faster_whisper.WhisperModel", return_value=mock_model):
        # Remove the module from cache to force reimport with fresh patch
        if "jarvis.transcriber" in sys.modules:
            del sys.modules["jarvis.transcriber"]
        from jarvis.transcriber import Transcriber
        t = Transcriber(model_size="base.en")
        audio = np.zeros(16000, dtype=np.float32)
        result = t.transcribe(audio)
        assert result == ""
