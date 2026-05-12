import sys
from unittest.mock import patch, MagicMock


def _clear_cache():
    for key in list(sys.modules.keys()):
        if "jarvis.tools.computer" in key:
            del sys.modules[key]


def test_open_app_launches_process():
    _clear_cache()
    with patch("subprocess.Popen") as mock_popen:
        from jarvis.tools.computer import open_app
        result = open_app("notepad")
        mock_popen.assert_called_once_with(["notepad"], shell=True)
        assert "Opening" in result


def test_type_text_calls_pyautogui():
    _clear_cache()
    with patch("pyautogui.typewrite") as mock_type:
        from jarvis.tools.computer import type_text
        result = type_text("hello world")
        mock_type.assert_called_once_with("hello world", interval=0.05)
        assert "Typed" in result


def test_adjust_volume_clamps_to_range():
    _clear_cache()
    mock_volume = MagicMock()
    mock_devices = MagicMock()
    mock_devices.Activate.return_value.QueryInterface.return_value = mock_volume

    with patch("jarvis.tools.computer.AudioUtilities") as mock_au:
        mock_au.GetSpeakers.return_value = mock_devices
        with patch("jarvis.tools.computer.IAudioEndpointVolume") as mock_iface:
            mock_iface._iid_ = "fake_iid"
            from jarvis.tools.computer import adjust_volume
            result = adjust_volume(150)  # should clamp to 100
            mock_volume.SetMasterVolumeLevelScalar.assert_called_once_with(1.0, None)
            assert "100" in result


def test_get_datetime_returns_string():
    _clear_cache()
    from jarvis.tools.computer import get_datetime
    result = get_datetime()
    assert len(result) > 5


def test_search_web_opens_browser():
    _clear_cache()
    with patch("webbrowser.open") as mock_open:
        from jarvis.tools.computer import search_web
        result = search_web("python tutorials")
        mock_open.assert_called_once()
        assert "Searching" in result
