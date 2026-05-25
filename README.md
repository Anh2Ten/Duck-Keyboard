# Duck Keyboard 🦆

Funny keyboard sound app made with Python.

Every time you press a key, the app plays a duck sound.

Simple GUI, lightweight, multi-key support, and easy to build into `.exe`.

---

# Features

- Multi-key sound support
- Lightweight
- GUI toggle button
- Custom app icon
- Centered window
- Low CPU usage
- Build to single `.exe`
- Windows friendly

---

# Files

```text
duckKBS.py
duck.mp3
duck.ico
```

---

# Install Libraries

```bash
pip install pygame pynput pyinstaller
```

---

# Run Project

```bash
python duckKBS.py
```

---

# Build To EXE

```bash
python -m PyInstaller --onefile --noconsole --icon duck.ico --add-data "duck.mp3;." --add-data "duck.ico;." duckKBS.py
```

After build:

```text
dist/duckKBS.exe
```

---

# Notes

- Keep `duck.mp3` short for better performance
- `.wav` files are lower latency than `.mp3`
- Works best on Windows 10/11
- Close the GUI window to exit app

---

# Preview

```text
🦆 Duck Keyboard
by Anh2Ten

[ Toggle Sound ]
```

---

# Credits

made by Anh2Ten

have fun XD