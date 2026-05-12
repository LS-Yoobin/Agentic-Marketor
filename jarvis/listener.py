import threading
import queue
import numpy as np
import sounddevice as sd
import keyboard
from openwakeword.model import Model as WakeWordModel

SAMPLE_RATE = 16000
CHUNK_SIZE = 1280  # 80ms at 16kHz
SILENCE_THRESHOLD_RMS = 0.01  # ~-40 dB
SILENCE_DURATION = 1.5  # seconds of silence before stopping
MAX_DURATION = 30.0  # max recording seconds
MIN_DURATION = 0.5  # min recording seconds


class Listener:
    def __init__(
        self,
        hotkey: str = "ctrl+space",
        wake_word_sensitivity: float = 0.5,
        on_audio_ready=None,
    ):
        self._hotkey = hotkey
        self._sensitivity = wake_word_sensitivity
        self._on_audio_ready = on_audio_ready
        self._recording = False
        self._audio_buffer = []
        self._wakeword_model = None

    def start(self):
        self._check_hotkey_conflict()
        keyboard.add_hotkey(self._hotkey, self._on_hotkey_press)
        self._start_wake_word_listener()
        print(f"Jarvis ready. Say 'Hey Jarvis' or press {self._hotkey}.")

    def _check_hotkey_conflict(self):
        try:
            keyboard.add_hotkey(self._hotkey, lambda: None)
            keyboard.remove_hotkey(self._hotkey)
        except Exception:
            print(f"Warning: hotkey {self._hotkey} may conflict with another app.")

    def _on_hotkey_press(self):
        if not self._recording:
            self._start_recording()

    def _start_recording(self):
        self._recording = True
        self._audio_buffer = []
        threading.Thread(target=self._record_until_silence, daemon=True).start()

    def _record_until_silence(self):
        silence_samples = 0
        silence_limit = int(SILENCE_DURATION * SAMPLE_RATE / CHUNK_SIZE)
        max_chunks = int(MAX_DURATION * SAMPLE_RATE / CHUNK_SIZE)
        min_chunks = int(MIN_DURATION * SAMPLE_RATE / CHUNK_SIZE)
        chunks_recorded = 0

        def callback(indata, frames, time, status):
            nonlocal silence_samples, chunks_recorded
            chunk = indata[:, 0].copy()
            self._audio_buffer.append(chunk)
            chunks_recorded += 1
            rms = np.sqrt(np.mean(chunk ** 2))
            if rms < SILENCE_THRESHOLD_RMS:
                silence_samples += 1
            else:
                silence_samples = 0

        with sd.InputStream(samplerate=SAMPLE_RATE, channels=1,
                            blocksize=CHUNK_SIZE, callback=callback):
            while self._recording:
                sd.sleep(80)
                if (chunks_recorded > min_chunks and
                        silence_samples >= silence_limit):
                    break
                if chunks_recorded >= max_chunks:
                    break

        self._recording = False
        if chunks_recorded >= min_chunks and self._on_audio_ready:
            audio = np.concatenate(self._audio_buffer)
            self._on_audio_ready(audio)

    def _start_wake_word_listener(self):
        try:
            self._wakeword_model = WakeWordModel(
                wakeword_models=["hey_jarvis"],
                inference_framework="onnx"
            )
            threading.Thread(target=self._wake_word_loop, daemon=True).start()
        except Exception as e:
            print(f"Wake word unavailable ({e}). Use hotkey {self._hotkey} instead.")

    def _wake_word_loop(self):
        def callback(indata, frames, time, status):
            audio_chunk = (indata[:, 0] * 32768).astype(np.int16)
            predictions = self._wakeword_model.predict(audio_chunk)
            if predictions.get("hey_jarvis", 0) >= self._sensitivity:
                if not self._recording:
                    print("Wake word detected.")
                    self._start_recording()

        with sd.InputStream(samplerate=SAMPLE_RATE, channels=1,
                            blocksize=CHUNK_SIZE, dtype="float32",
                            callback=callback):
            while True:
                sd.sleep(100)
