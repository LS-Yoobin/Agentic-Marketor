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
    from jarvis.tools.computer import adjust_volume

    mock_volume = MagicMock()
    mock_speaker = MagicMock()
    mock_activate = MagicMock()
    mock_speaker.GetSpeakers.return_value = mock_speaker
    mock_speaker.Activate.return_value = mock_activate
    mock_activate.QueryInterface.return_value = mock_volume

    with patch("jarvis.tools.computer.AudioUtilities", mock_speaker):
        with patch("jarvis.tools.computer.IAudioEndpointVolume") as mock_iface:
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
