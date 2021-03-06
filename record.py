import time, ctypes, os
from datetime import datetime
from PIL import ImageGrab

DATA_DIR = os.path.join('CS Numbers', 'Data')

def currentTime():
    return datetime.now().strftime("%H:%M:%S:%f")[:-3]

def takeScreenshot(minsElapsed):
    screenWidth = ctypes.windll.user32.GetSystemMetrics(0)
    screenHeight = ctypes.windll.user32.GetSystemMetrics(1)
    screenshot = ImageGrab.grab((13*screenWidth//14, 0, screenWidth-60, screenHeight//36))
    screenshot.save(os.path.join(DATA_DIR, f'{minsElapsed}.png'), 'PNG')

try:
    print('Press Ctrl+C to stop recording')
    print(f'[{currentTime()}] Start recording...')
    try:
        os.mkdir(DATA_DIR)
    except:
        pass # ignore exception if folder exists
    for i in range(1,7):
        time.sleep(300)
        mins = i*5
        if mins == 5:
            takeScreenshot('05')
        else:
            takeScreenshot(mins)
        i += 1
        print(f'[{currentTime()}] Screenshot captured at {mins} minutes')
    print(f'[{currentTime()}] Stop recording...')
    import plot
except KeyboardInterrupt:
    print(f'[{currentTime()}] Stop recording...')
    import plot
