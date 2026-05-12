import os
os.environ.setdefault("ANTHROPIC_API_KEY", "test")

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
        # history should only have the original user message + assistant reply (2 items)
        assert len(b._history) == 2
