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
