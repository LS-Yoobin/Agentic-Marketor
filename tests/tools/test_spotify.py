import os
os.environ.setdefault("ANTHROPIC_API_KEY", "test")

from unittest.mock import MagicMock, patch


def _make_spotify_tool(premium=True):
    mock_sp = MagicMock()
    mock_sp.current_user.return_value = {
        "product": "premium" if premium else "free"
    }
    mock_sp.search.return_value = {
        "tracks": {"items": [{"uri": "spotify:track:abc123", "name": "Test Song"}]}
    }
    return mock_sp


def test_play_music_searches_and_plays():
    mock_sp = _make_spotify_tool()
    with patch("spotipy.Spotify", return_value=mock_sp):
        with patch("spotipy.oauth2.SpotifyOAuth"):
            from jarvis.tools.spotify import SpotifyTools
            s = SpotifyTools(mock_sp)
            result = s.play_music("Kendrick Lamar")
            mock_sp.start_playback.assert_called_once()
            assert "Playing" in result


def test_play_music_handles_no_results():
    mock_sp = _make_spotify_tool()
    mock_sp.search.return_value = {"tracks": {"items": []}}
    with patch("spotipy.Spotify", return_value=mock_sp):
        from jarvis.tools.spotify import SpotifyTools
        s = SpotifyTools(mock_sp)
        result = s.play_music("xyznotatrack123")
        assert "couldn't find" in result.lower()


def test_pause_music():
    mock_sp = _make_spotify_tool()
    from jarvis.tools.spotify import SpotifyTools
    s = SpotifyTools(mock_sp)
    result = s.pause_music()
    mock_sp.pause_playback.assert_called_once()
    assert "Paused" in result


def test_skip_track():
    mock_sp = _make_spotify_tool()
    from jarvis.tools.spotify import SpotifyTools
    s = SpotifyTools(mock_sp)
    result = s.skip_track()
    mock_sp.next_track.assert_called_once()
    assert "Skipped" in result
