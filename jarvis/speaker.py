import asyncio
import edge_tts


class Speaker:
    def __init__(self, voice: str = "en-GB-RyanNeural"):
        self._voice = voice

    def speak(self, text: str) -> None:
        if not text.strip():
            return
        asyncio.run(self._speak_async(text))

    async def _speak_async(self, text: str) -> None:
        communicate = edge_tts.Communicate(text, self._voice)
        await communicate.play()
