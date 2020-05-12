import time, ctypes, os, cv2, random
import numpy as np
import tensorflow as tf
from pynput import keyboard
from PIL import ImageGrab
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

NUM_IMAGES = 201
TRAINING_DATA_DIR = os.path.join('CS Numbers', 'Training')
CATEGORIES = [str(i) for i in range(NUM_IMAGES)]
IMG_WIDTH = 38
IMG_HEIGHT = 21
BATCH_SIZE = 20
EPOCHS = 20

def on_press(key):
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

def createTrainingData():
    for category in CATEGORIES:
        path = os.path.join(TRAINING_DATA_DIR, category)
        for img in os.listdir(path):
            img_array = cv2.imread(os.path.join(path, img))
            training_data.append([img_array, category])

def testModel():
    for i in range(10):
        randomNumber = random.randrange(NUM_IMAGES)
        print(f'Testing {randomNumber}.png')
        img = cv2.imread(os.path.join(os.path.join('CS Numbers', 'Testing'), f'{randomNumber}.png'))
        img_array = img.reshape(-1, IMG_WIDTH, IMG_HEIGHT, 3)
        prediction = model.predict(img_array)
        prediction = list(prediction[0])
        print(f'Prediction: {CATEGORIES[prediction.index(max(prediction))]}')
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

training_data = []
createTrainingData()

X = []
y = []
for features, label in training_data:
    X.append(features)
    y.append(int(label))
X = np.array(X).reshape(-1, IMG_WIDTH, IMG_HEIGHT, 3)
y = np.asarray(y)

model = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=X.shape[1:]),
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(NUM_IMAGES)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

print('Fitting to model...')
history = model.fit(X, y, batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=False)
print(f'Accuracy: {history.history["accuracy"][-1]}')

testModel()

# startTime = time.time()
# with keyboard.Listener(on_press=on_press) as listener:
    # listener.join()
    
# i = 1
# while True:
    # time.sleep(600)
    # takeScreenshot(i*5)
    # i += 1
