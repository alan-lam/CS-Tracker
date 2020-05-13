import time, ctypes, os
from datetime import datetime
from PIL import ImageGrab

DATA_DIR = os.path.join('CS Numbers', 'Data')

def currentTime():
    dt = datetime.now().strftime("%H:%M:%S:%f")[:-3]
    return dt

def on_press(key):
    if key == keyboard.Key.esc:
        return False

def takeScreenshot(minsElapsed):
    screenWidth = ctypes.windll.user32.GetSystemMetrics(0)
    screenHeight = ctypes.windll.user32.GetSystemMetrics(1)
    screenshot = ImageGrab.grab((13*screenWidth//14, 0, screenWidth-60, screenHeight//36))
    screenshot.save(os.path.join(DATA_DIR, f'{minsElapsed}.png'), 'PNG')

try:
    print(f'[{currentTime()}] Start recording...')
    i = 1
    while True:
        time.sleep(600)
        mins = i*5
        takeScreenshot(mins)
        i += 1
        print(f'[{currentTime()}] {mins} minutes has passed')
except KeyboardInterrupt:
    print(f'[{currentTime()}] Stop recording...')
    import cs
