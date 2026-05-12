import os
os.environ.setdefault("ANTHROPIC_API_KEY", "test")

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
