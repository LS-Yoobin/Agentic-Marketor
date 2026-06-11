import sys
import threading
import numpy as np
from jarvis import config
from jarvis.transcriber import Transcriber
from jarvis.speaker import Speaker
from jarvis.listener import Listener
from jarvis.brain import Brain
from jarvis.tools import build_tool_registry


def main():
    print("Initialising Jarvis...")
    print("Loading transcriber...")
    transcriber = Transcriber(model_size=config.WHISPER_MODEL)
    print("Loading speaker...")
    speaker = Speaker(voice=config.TTS_VOICE)
    print("Loading tools...")
    tool_registry = build_tool_registry()
    print("Loading brain...")
    brain = Brain(api_key=config.ANTHROPIC_API_KEY, tool_registry=tool_registry)
    print("All components loaded.")

    from PyQt6.QtWidgets import QApplication
    from jarvis.overlay import Overlay
    app = QApplication(sys.argv)
    print("Loading overlay...")
    overlay = Overlay()

    def on_audio_ready(audio: np.ndarray):
        overlay.signals.set_listening.emit(False)

        text = transcriber.transcribe(audio)
        if not text.strip():
            return

        print(f"You: {text}")
        overlay.signals.update_text.emit(text, "...")

        def process():
            reply = brain.process(text)
            print(f"Jarvis: {reply}")
            overlay.signals.update_text.emit(text, reply)
            speaker.speak(reply)

        threading.Thread(target=process, daemon=True).start()

    listener = Listener(
        hotkey=config.HOTKEY,
        wake_word_sensitivity=config.WAKE_WORD_SENSITIVITY,
        on_audio_ready=on_audio_ready,
    )

    def on_listening_start():
        overlay.signals.set_listening.emit(True)

    # Patch listener to signal overlay on recording start
    original_start = listener._start_recording
    def patched_start():
        on_listening_start()
        original_start()
    listener._start_recording = patched_start

    listener.start()
    overlay.show()
    print("Jarvis is ready.")
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
