import time, ctypes
from pynput import keyboard
from PIL import ImageGrab

def on_press(key):
    global startTime
    if key == keyboard.Key.print_screen:
        minsElapsed = calculateMinutesElapsed()
        takeScreenshot(minsElapsed)
    elif key == keyboard.Key.esc:
        return False
        
def calculateMinutesElapsed():
    endTime = time.time()
    return (endTime - startTime) // 60
    
def takeScreenshot(minsElapsed):
    screenWidth = ctypes.windll.user32.GetSystemMetrics(0)
    screenHeight = ctypes.windll.user32.GetSystemMetrics(1)
    screenshot = ImageGrab.grab((13*screenWidth//14, 0, screenWidth-60, screenHeight//36))
    screenshot.save(f'{minsElapsed}.png', 'PNG')

startTime = time.time()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
# i = 1
# while True:
    # time.sleep(600)
    # takeScreenshot(i*5)
    # i += 1
