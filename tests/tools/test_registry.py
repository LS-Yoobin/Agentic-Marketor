import os
os.environ.setdefault("ANTHROPIC_API_KEY", "test")

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
