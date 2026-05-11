import numpy as np
from faster_whisper import WhisperModel


class Transcriber:
    def __init__(self, model_size: str = "base.en"):
        self._model = WhisperModel(model_size, device="cpu", compute_type="int8")

    def transcribe(self, audio: np.ndarray) -> str:
        segments, _ = self._model.transcribe(audio, language="en")
        return " ".join(s.text.strip() for s in segments).strip()
