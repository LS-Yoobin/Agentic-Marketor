import spotipy
from spotipy.oauth2 import SpotifyOAuth
from jarvis import config


def create_spotify_client() -> spotipy.Spotify | None:
    if not config.SPOTIFY_CLIENT_ID:
        return None
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=config.SPOTIFY_CLIENT_ID,
        client_secret=config.SPOTIFY_CLIENT_SECRET,
        redirect_uri=config.SPOTIFY_REDIRECT_URI,
        scope="user-modify-playback-state user-read-playback-state"
    ))
    try:
        user = sp.current_user()
        if user.get("product") != "premium":
            print("Warning: Spotify Premium required for playback control.")
            return None
    except Exception:
        return None
    return sp


class SpotifyTools:
    def __init__(self, client: spotipy.Spotify):
        self._sp = client

    def play_music(self, query: str) -> str:
        results = self._sp.search(q=query, limit=1, type="track")
        items = results["tracks"]["items"]
        if not items:
            return f"I couldn't find anything matching '{query}' on Spotify."
        uri = items[0]["uri"]
        name = items[0]["name"]
        self._sp.start_playback(uris=[uri])
        return f"Playing {name}."

    def pause_music(self) -> str:
        self._sp.pause_playback()
        return "Paused."

    def resume_music(self) -> str:
        self._sp.start_playback()
        return "Resumed."

    def skip_track(self) -> str:
        self._sp.next_track()
        return "Skipped to next track."
