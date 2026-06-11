import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                              QSystemTrayIcon, QMenu)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QObject
from PyQt6.QtGui import QIcon, QColor, QPalette


class OverlaySignals(QObject):
    update_text = pyqtSignal(str, str)  # (user_text, jarvis_text)
    set_listening = pyqtSignal(bool)


class Overlay(QWidget):
    def __init__(self):
        super().__init__()
        self.signals = OverlaySignals()
        self.signals.update_text.connect(self._update_text)
        self.signals.set_listening.connect(self._set_listening)
        self._hide_timer = QTimer()
        self._hide_timer.setSingleShot(True)
        self._hide_timer.timeout.connect(self.hide)
        self._setup_ui()
        self._setup_tray()

    def _setup_ui(self):
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedWidth(320)

        layout = QVBoxLayout()
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(6)

        self._status_label = QLabel("●")
        self._status_label.setStyleSheet("color: #666; font-size: 10px;")

        self._user_label = QLabel("")
        self._user_label.setWordWrap(True)
        self._user_label.setStyleSheet(
            "color: #aaa; font-size: 12px; font-style: italic;")

        self._jarvis_label = QLabel("")
        self._jarvis_label.setWordWrap(True)
        self._jarvis_label.setStyleSheet(
            "color: white; font-size: 14px; font-weight: bold;")

        layout.addWidget(self._status_label)
        layout.addWidget(self._user_label)
        layout.addWidget(self._jarvis_label)
        self.setLayout(layout)

        self.setStyleSheet(
            "QWidget { background-color: rgba(15, 15, 20, 200); "
            "border-radius: 10px; }")

        screen = QApplication.primaryScreen()
        if screen:
            geo = screen.geometry()
            self.move(geo.width() - 340, 40)
        else:
            self.move(1580, 40)  # fallback for headless/multi-monitor

    def _setup_tray(self):
        self._tray = QSystemTrayIcon(self)
        self._tray.setToolTip("Jarvis")
        tray_menu = QMenu()
        tray_menu.addAction("Show", self.show)
        tray_menu.addAction("Quit", QApplication.quit)
        self._tray.setContextMenu(tray_menu)
        self._tray.activated.connect(lambda _: self.show())
        self._tray.show()

    def _update_text(self, user_text: str, jarvis_text: str):
        self._user_label.setText(f'You: "{user_text}"')
        self._jarvis_label.setText(f"Jarvis: {jarvis_text}")
        self.adjustSize()
        self.show()
        self._hide_timer.start(8000)

    def _set_listening(self, listening: bool):
        if listening:
            self._status_label.setText("● Listening...")
            self._status_label.setStyleSheet("color: #00ff88; font-size: 10px;")
            self.show()
            self._hide_timer.stop()
        else:
            self._status_label.setText("●")
            self._status_label.setStyleSheet("color: #666; font-size: 10px;")
