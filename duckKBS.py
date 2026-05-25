import tkinter as tk
from pynput import keyboard
import pygame
import ctypes
import os
import sys

pygame.mixer.pre_init(
    frequency=44100,
    size=-16,
    channels=2,
    buffer=128
)

pygame.init()
pygame.mixer.init()

pygame.mixer.set_num_channels(64)


def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, path)


SOUND_PATH = resource_path("duck.mp3")
ICON_PATH = resource_path("duck.ico")

duck_sound = pygame.mixer.Sound(SOUND_PATH)
duck_sound.set_volume(0.4)

enabled = True

ignored_keys = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
}


def play_duck():
    if not enabled:
        return

    channel = pygame.mixer.find_channel(True)

    if channel:
        channel.play(duck_sound)


def update_status():
    if enabled:
        status_label.config(
            text="Âm thanh đang bật",
            fg="#16a34a"
        )

        toggle_button.config(
            text="Tắt âm thanh",
            bg="#ef4444",
            activebackground="#dc2626"
        )

    else:
        status_label.config(
            text="Âm thanh đang tắt",
            fg="#dc2626"
        )

        toggle_button.config(
            text="Bật âm thanh",
            bg="#2563eb",
            activebackground="#1d4ed8"
        )


def toggle_sound():
    global enabled

    enabled = not enabled

    update_status()


def on_press(key):
    if key in ignored_keys:
        return

    play_duck()


def hide_console():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()

    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 0)


def close_app():
    listener.stop()

    pygame.mixer.quit()

    root.destroy()

    os._exit(0)


listener = keyboard.Listener(on_press=on_press)
listener.daemon = True
listener.start()

hide_console()

root = tk.Tk()

root.title("Duck Keyboard - Anh2Ten")

window_width = 420
window_height = 320

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.resizable(False, False)
root.configure(bg="#f4f4f5")

root.protocol("WM_DELETE_WINDOW", close_app)

try:
    root.iconbitmap(ICON_PATH)
except:
    pass

main_frame = tk.Frame(
    root,
    bg="#f4f4f5"
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=24,
    pady=24
)

logo_label = tk.Label(
    main_frame,
    text="🦆",
    font=("Segoe UI Emoji", 42),
    bg="#f4f4f5"
)

logo_label.pack(
    pady=(0, 4)
)

title_label = tk.Label(
    main_frame,
    text="Duck Keyboard",
    font=("Segoe UI", 20, "bold"),
    bg="#f4f4f5",
    fg="#111827"
)

title_label.pack()

author_label = tk.Label(
    main_frame,
    text="by Anh2Ten",
    font=("Segoe UI", 10),
    bg="#f4f4f5",
    fg="#6b7280"
)

author_label.pack(
    pady=(0, 14)
)

status_label = tk.Label(
    main_frame,
    text="",
    font=("Segoe UI", 11, "bold"),
    bg="#f4f4f5"
)

status_label.pack(
    pady=(0, 12)
)

toggle_button = tk.Button(
    main_frame,
    text="",
    command=toggle_sound,
    font=("Segoe UI", 11, "bold"),
    fg="white",
    activeforeground="white",
    relief="flat",
    bd=0,
    padx=12,
    pady=10,
    cursor="hand2"
)

toggle_button.pack(
    fill="x",
    pady=(0, 10)
)

info_label = tk.Label(
    main_frame,
    text="Đóng cửa sổ để thoát ứng dụng",
    font=("Segoe UI", 9),
    bg="#f4f4f5",
    fg="#6b7280"
)

info_label.pack()

update_status()

root.mainloop()
