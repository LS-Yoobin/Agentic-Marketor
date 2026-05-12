from jarvis.tools.computer import open_app, type_text, adjust_volume, search_web, get_datetime
from jarvis.tools.spotify import SpotifyTools, create_spotify_client
from jarvis.tools.email_tool import EmailTools, build_gmail_service


def build_tool_registry() -> dict:
    spotify = create_spotify_client()

    gmail = None
    try:
        gmail = build_gmail_service()
    except Exception as e:
        print(f"Gmail not available: {e}")

    spotify_tools = SpotifyTools(spotify) if spotify else None
    email_tools = EmailTools(gmail) if gmail else None

    def _disabled(name):
        return lambda **_: f"{name} is not available (check credentials)."

    functions = {
        "open_app": lambda name: open_app(name),
        "type_text": lambda text: type_text(text),
        "adjust_volume": lambda level: adjust_volume(int(level)),
        "search_web": lambda query: search_web(query),
        "get_datetime": lambda: get_datetime(),
        "play_music": (spotify_tools.play_music if spotify_tools
                       else _disabled("Spotify")),
        "pause_music": (spotify_tools.pause_music if spotify_tools
                        else _disabled("Spotify")),
        "resume_music": (spotify_tools.resume_music if spotify_tools
                         else _disabled("Spotify")),
        "skip_track": (spotify_tools.skip_track if spotify_tools
                       else _disabled("Spotify")),
        "send_email": (email_tools.send_email if email_tools
                       else _disabled("Gmail")),
        "read_emails": (email_tools.read_emails if email_tools
                        else _disabled("Gmail")),
    }

    schemas = [
        {"name": "play_music", "description": "Search Spotify and play a track, artist, or playlist",
         "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
        {"name": "pause_music", "description": "Pause Spotify playback",
         "input_schema": {"type": "object", "properties": {}}},
        {"name": "resume_music", "description": "Resume Spotify playback",
         "input_schema": {"type": "object", "properties": {}}},
        {"name": "skip_track", "description": "Skip to next Spotify track",
         "input_schema": {"type": "object", "properties": {}}},
        {"name": "send_email", "description": "Send an email via Gmail",
         "input_schema": {"type": "object", "properties": {
             "to": {"type": "string"}, "subject": {"type": "string"}, "body": {"type": "string"}
         }, "required": ["to", "subject", "body"]}},
        {"name": "read_emails", "description": "Read recent inbox emails",
         "input_schema": {"type": "object", "properties": {
             "count": {"type": "integer", "default": 5}
         }}},
        {"name": "open_app", "description": "Open an application by name",
         "input_schema": {"type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]}},
        {"name": "type_text", "description": "Type text at the current cursor position",
         "input_schema": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}},
        {"name": "adjust_volume", "description": "Set system volume 0-100",
         "input_schema": {"type": "object", "properties": {"level": {"type": "integer"}}, "required": ["level"]}},
        {"name": "search_web", "description": "Open browser with a Google search",
         "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
        {"name": "get_datetime", "description": "Get the current date and time",
         "input_schema": {"type": "object", "properties": {}}},
    ]

    return {"functions": functions, "schemas": schemas}
