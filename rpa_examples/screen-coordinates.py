import PySimpleGUI as sg
import pyautogui
import threading
import keyboard
import time

class OverlayApp:
    def __init__(self):
        self.window = None
        self.running = False
        self.thread = None

    def start_overlay(self):
        if self.running:
            return
        self.running = True
        self.thread = threading.Thread(target=self.run_overlay, daemon=True)
        self.thread.start()

    def stop_overlay(self):
        self.running = False
        if self.window:
            self.window.close()
            self.window = None

    def run_overlay(self):
        layout = [[sg.Text('', key='-COORD-', font=('Arial', 14), background_color='black', text_color='white', pad=(10, 5))]]
        self.window = sg.Window('Mouse Coordinates', layout, no_titlebar=True, keep_on_top=True, alpha_channel=0.8, finalize=True, grab_anywhere=True, background_color='black')
        while self.running:
            x, y = pyautogui.position()
            self.window['-COORD-'].update(f'X: {x}  Y: {y}')
            self.window.move(x+20, y+20)
            event, _ = self.window.read(timeout=20)
            if event == sg.WIN_CLOSED:
                self.running = False
                break
        if self.window:
            self.window.close()
            self.window = None

# --- Main logic ---
app = OverlayApp()

def toggle_overlay():
    if app.running:
        app.stop_overlay()
    else:
        app.start_overlay()

print("Press F8 to toggle the coordinate overlay. Press ESC to exit.")
keyboard.add_hotkey('F8', toggle_overlay)

try:
    while True:
        if keyboard.is_pressed('esc'):
            app.stop_overlay()
            break
        time.sleep(0.1)
except KeyboardInterrupt:
    pass