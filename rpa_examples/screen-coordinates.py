import tkinter as tk
import pyautogui
import threading
import keyboard
import time

class OverlayApp:
    def __init__(self):
        self.overlay = None
        self.running = False
        self.thread = None

    def start_overlay(self):
        if self.running:
            return
        self.running = True

        # Start Tkinter in a separate thread
        self.thread = threading.Thread(target=self.run_overlay, daemon=True)
        self.thread.start()

    def stop_overlay(self):
        if not self.running:
            return
        self.running = False
        if self.overlay:
            self.overlay.destroy()
            self.overlay = None

    def run_overlay(self):
        self.overlay = tk.Tk()
        self.overlay.overrideredirect(True)
        self.overlay.attributes("-topmost", True)
        self.overlay.attributes("-alpha", 0.8)

        self.label = tk.Label(
            self.overlay, text="", font=("Arial", 14),
            bg="black", fg="white", padx=10, pady=5
        )
        self.label.pack()

        self.update_position()
        self.overlay.mainloop()

    def update_position(self):
        if not self.running or not self.overlay:
            return
        x, y = pyautogui.position()
        self.label.config(text=f"X: {x}  Y: {y}")
        self.overlay.geometry(f"+{x+20}+{y+20}")
        self.overlay.after(20, self.update_position)

# --- Main logic ---
app = OverlayApp()

def toggle_overlay():
    if app.running:
        app.stop_overlay()
    else:
        app.start_overlay()

print("Press F8 to toggle the coordinate overlay. Press ESC to exit.")
keyboard.add_hotkey('F8', toggle_overlay)

# Keep the main thread alive, listen for ESC to exit
try:
    while True:
        if keyboard.is_pressed('esc'):
            app.stop_overlay()
            break
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
