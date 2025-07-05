import sys
import pyautogui
from PyQt5 import QtCore, QtWidgets, QtGui
import threading
import keyboard

class OverlayWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.Tool
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(120, 45)

        # Styling
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                background-color: rgba(30, 30, 30, 200);
                color: #fff;
                font-size: 16px;
                border-radius: 12px;
                padding: 8px;
            }
        """)
        self.label.setGeometry(0, 0, 120, 45)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_coords)
        self.timer.start(25)  # Update every 25 ms

    def update_coords(self):
        x, y = pyautogui.position()
        self.label.setText(f"X: {x}\nY: {y}")
        self.move(x + 20, y + 20)

class OverlayController:
    def __init__(self):
        self.app = None
        self.overlay = None
        self.overlay_thread = None
        self.overlay_running = False

    def start_overlay(self):
        if self.overlay_running:
            return
        self.overlay_running = True
        self.overlay_thread = threading.Thread(target=self._run_overlay, daemon=True)
        self.overlay_thread.start()

    def stop_overlay(self):
        if self.overlay_running and self.overlay:
            QtCore.QMetaObject.invokeMethod(self.overlay, "close")
            self.overlay_running = False

    def _run_overlay(self):
        self.app = QtWidgets.QApplication([])
        self.overlay = OverlayWidget()
        self.overlay.show()
        self.app.exec_()

# Hotkey toggle logic
controller = OverlayController()

def toggle_overlay():
    if controller.overlay_running:
        controller.stop_overlay()
    else:
        controller.start_overlay()

print("Press F8 to toggle overlay. Press ESC to exit.")
keyboard.add_hotkey('F8', toggle_overlay)

try:
    while True:
        if keyboard.is_pressed('esc'):
            controller.stop_overlay()
            break
        QtCore.QThread.msleep(50)
except KeyboardInterrupt:
    pass
