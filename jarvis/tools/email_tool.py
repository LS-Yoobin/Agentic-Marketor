import base64
from email.mime.text import MIMEText
from pathlib import Path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from jarvis import config

SCOPES = ["https://www.googleapis.com/auth/gmail.send",
          "https://www.googleapis.com/auth/gmail.readonly"]
TOKEN_PATH = Path("./token.json")


def build_gmail_service():
    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                config.GMAIL_CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_PATH.write_text(creds.to_json())
    return build("gmail", "v1", credentials=creds)


class EmailTools:
    def __init__(self, service):
        self._service = service

    def send_email(self, to: str, subject: str, body: str) -> str:
        msg = MIMEText(body)
        msg["to"] = to
        msg["subject"] = subject
        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        self._service.users().messages().send(
            userId="me", body={"raw": raw}).execute()
        return f"Sent email to {to}."

    def read_emails(self, count: int = 5) -> str:
        results = self._service.users().messages().list(
            userId="me", maxResults=count).execute()
        messages = results.get("messages", [])
        if not messages:
            return "Your inbox is empty."
        summaries = []
        for m in messages:
            msg = self._service.users().messages().get(
                userId="me", id=m["id"], format="full").execute()
            headers = {h["name"]: h["value"]
                       for h in msg["payload"]["headers"]}
            summaries.append(
                f"From: {headers.get('From', '?')} | "
                f"Subject: {headers.get('Subject', '?')} | "
                f"{msg.get('snippet', '')[:80]}"
            )
        return "\n".join(summaries)
